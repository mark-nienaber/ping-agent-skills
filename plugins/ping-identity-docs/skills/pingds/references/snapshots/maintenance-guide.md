---
title: Accounts
description: Configure PingDS account lockout policies, manage account status, and send account status notifications by email.
component: pingds
version: 8.1
page_id: pingds:maintenance-guide:accounts
canonical_url: https://docs.pingidentity.com/pingds/8.1/maintenance-guide/accounts.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Authentication", "Features", "LDAP", "Setup &amp; Configuration"]
section_ids:
  configure-account-lockout: Account lockout
  manage-accounts: Account management
  disable-account: Disable an account
  reactivate-account: Activate a disabled account
  account-status-notification: Account status notifications
  mail-account-status-notifications: Send account status mail
  message_templates: Message templates
---

# Accounts

## Account lockout

Account lockout settings are part of password policy. The server locks an account after the specified number of consecutive authentication failures. For example, users are allowed three consecutive failures before being locked out for five minutes. Failures themselves expire after five minutes.

The aim of account lockout is not to punish users who mistype their passwords. It protects the directory when an attacker attempts to guess a user password with repeated attempts to bind.

|   |                                                                                                                                                                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Account lockout is not transactional across a replication topology. Under normal circumstances, replication propagates lockout quickly. If replication is ever delayed, an attacker with direct access to multiple replicas could try to authenticate up to the specified number of times on each replica before being locked out on all replicas. |

The following command adds a replicated password policy to activate lockout:

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
dn: cn=Lock after three failures,dc=example,dc=com
objectClass: top
objectClass: subentry
objectClass: ds-pwp-password-policy
cn: Lock after three failures
ds-pwp-password-attribute: userPassword
ds-pwp-default-password-storage-scheme: PBKDF2-HMAC-SHA256
ds-pwp-lockout-failure-expiration-interval: 5 m
ds-pwp-lockout-duration: 5 m
ds-pwp-lockout-failure-count: 3
subtreeSpecification: { base "ou=people" }
EOF
```

Users with this policy are locked out after three failed attempts in succession.

1. Successfully authenticate:

   ```console
   $ ldapsearch \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN "uid=bjensen,ou=people,dc=example,dc=com" \
    --bindPassword hifalutin \
    --baseDN dc=example,dc=com \
    uid=bjensen \
    mail
   ```

   Output

   ```
   dn: uid=bjensen,ou=People,dc=example,dc=com
   mail: bjensen@example.com
   ```

2. First failure:

   ```console
   $ ldapsearch \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN "uid=bjensen,ou=people,dc=example,dc=com" \
    --bindPassword fatfngrs \
    --baseDN dc=example,dc=com \
    uid=bjensen \
    mail
   ```

   Output

   ```
   The LDAP bind request failed: 49 (Invalid Credentials)
   ```

3. Second failure:

   ```console
   $ ldapsearch \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN "uid=bjensen,ou=people,dc=example,dc=com" \
    --bindPassword fatfngrs \
    --baseDN dc=example,dc=com \
    uid=bjensen \
    mail
   ```

   Output

   ```
   The LDAP bind request failed: 49 (Invalid Credentials)
   ```

4. Third failure:

   ```console
   $ ldapsearch \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN "uid=bjensen,ou=people,dc=example,dc=com" \
    --bindPassword fatfngrs \
    --baseDN dc=example,dc=com \
    uid=bjensen \
    mail
   ```

   Output

   ```
   The LDAP bind request failed: 49 (Invalid Credentials)
   ```

5. Try to authenticate:

   ```console
   $ ldapsearch \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN "uid=bjensen,ou=people,dc=example,dc=com" \
    --bindPassword hifalutin \
    --baseDN dc=example,dc=com \
    uid=bjensen \
    mail
   ```

   Locked out

   ```
   The LDAP bind request failed: 49 (Invalid Credentials)
   ```

## Account management

### Disable an account

1. Make sure the user running the `manage-account` command has access to perform the appropriate operations.

   Kirsten Vaughan is a member of the Directory Administrators group. For this example, she must have the `password-reset` privilege, and access to edit user attributes and operational attributes:

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
   dn: uid=kvaughan,ou=People,dc=example,dc=com
   changetype: modify
   add: ds-privilege-name
   ds-privilege-name: password-reset

   dn: ou=People,dc=example,dc=com
   changetype: modify
   add: aci
   aci: (target="ldap:///ou=People,dc=example,dc=com")(targetattr ="*||+")
    (version 3.0;acl "Admins can run amok"; allow(all)
     groupdn = "ldap:///cn=Directory Administrators,ou=Groups,dc=example,dc=com";)
   EOF
   ```

   Notice here that the directory superuser, `uid=admin`, assigns privileges. Any administrator with the `privilege-change` privilege can assign privileges. However, if the administrator can update administrator privileges, they can assign themselves the `bypass-acl` privilege. Then they are no longer bound by access control instructions, including both user data ACIs and global ACIs. For this reason, do not assign the `privilege-change` privilege to normal administrator users.

2. Set the account status to disabled:

   ```console
   $ manage-account \
    set-account-is-disabled \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=kvaughan,ou=people,dc=example,dc=com \
    --bindPassword bribery \
    --operationValue true \
    --targetDN uid=bjensen,ou=people,dc=example,dc=com \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin
   ```

   > **Collapse: Show output**
   >
   > ```
   > Account Is Disabled:  true
   > ```

### Activate a disabled account

Clear the disabled status:

```console
$ manage-account \
 set-account-is-disabled \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=kvaughan,ou=people,dc=example,dc=com \
 --bindPassword bribery \
 --operationValue false \
 --targetDN uid=bjensen,ou=people,dc=example,dc=com \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin
```

> **Collapse: Show output**
>
> ```
> Account Is Disabled:  false
> ```

## Account status notifications

DS servers can send mail about account status changes. The DS server needs an SMTP server to send messages, and needs templates for the mail it sends. By default, message templates are in English, and found in the `/path/to/opendj/config/messages/` directory.

DS servers generate notifications only when the server writes to an entry or evaluates a user entry for authentication. A server generates account enabled and account disabled notifications when the user account is enabled or disabled with the `manage-account` command. A server generates password expiration notifications when a user tries to bind.

For example, if you configure a notification for password expiration, that notification gets triggered when the user authenticates during the password expiration warning interval. The server does not automatically scan entries to send password expiry notifications.

DS servers implement controls that you can pass in an LDAP search to determine whether a user's password is about to expire. Refer to [Supported LDAP controls](../ldap-reference/controls.html) for a list. Your script or client application can send notifications based on the results of the search.

### Send account status mail

1. Configure an SMTP server to use when sending messages:

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
   ```

2. Prepare the DS server to mail users about account status.

   The following example configures the server to send text-format mail messages:

   ```console
   $ dsconfig \
    set-account-status-notification-handler-prop \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --handler-name "SMTP Handler" \
    --set enabled:true \
    --set email-address-attribute-type:mail \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

   Notice that the server finds the user's mail address on the attribute on the user's entry, specified by `email-address-attribute-type`. You can also configure the `message-subject` and `message-template-file` properties. Use interactive mode to make the changes.

   You find templates for messages by default under the `config/messages` directory. Edit the templates as necessary.

   If you edit the templates to send HTML rather than text messages, then set the advanced property, `send-email-as-html`:

   ```console
   $ dsconfig \
    set-account-status-notification-handler-prop \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --handler-name "SMTP Handler" \
    --set enabled:true \
    --set send-email-as-html:true \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

3. Adjust applicable password policies to use the account status notification handler you configured:

   ```console
   $ dsconfig \
    set-password-policy-prop \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --policy-name "Default Password Policy" \
    --set account-status-notification-handler:"SMTP Handler" \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

   When configuring a subentry password policy, set the `ds-pwp-account-status-notification-handler` attribute, an attribute of the `ds-pwp-password-policy` object class.

## Message templates

When editing the `config/messages` templates, use the following tokens, which the server replaces with text:

* `%%notification-type%%`

  The name of the notification type.

* `%%notification-message%%`

  The message for the notification.

* `%%notification-user-dn%%`

  The string representation of the user DN that is the target of the notification.

* `%%notification-user-attr:attrname%%`

  The value of the attribute specified by attrname from the user's entry.

  If the specified attribute has multiple values, then this is the first value encountered. If the specified attribute does not have any values, then this is an empty string.

* `%%notification-property:propname%%`

  The value of the specified property.

  If the specified property has multiple values, then this is the first value encountered. If the specified property does not have any values, then this is an empty string.

  Valid propname values include the following:

  * `account-unlock-time`

  * `new-password`

  * `old-password`

  * `password-expiration-time`

  * `password-policy-dn`

  * `seconds-until-expiration`

  * `seconds-until-unlock`

  * `time-until-expiration`

  * `time-until-unlock`

---

---
title: Backup and restore
description: Back up and restore PingDS directory data using dsbackup commands, volume snapshots, or cloud storage, including purging stale backup files.
component: pingds
version: 8.1
page_id: pingds:maintenance-guide:backup-restore
canonical_url: https://docs.pingidentity.com/pingds/8.1/maintenance-guide/backup-restore.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-12T12:15:36Z
keywords: ["Backup &amp; Restore", "Features", "LDAP", "Setup &amp; Configuration", "Storage"]
section_ids:
  how-backup-works: How backup works
  backup_process: Backup process
  cumulative-backups: Cumulative backups
  purge_old_backups: Purge old backups
  backup: Back up
  backup-task: Back up data (server task)
  schedule-backup: Back up data (scheduled task)
  backup-external: Back up data (external command)
  backup-config: Back up configuration files
  backup-snapshot: Back up using snapshots
  restore: Restore
  restore-online: Restore data (server task)
  restore-offline: Restore data (external command)
  restore-config: Restore configuration files
  restore-snapshot: Restore from a snapshot
  purge: Purge old files
  cloud-storage: Cloud storage
  efficiently_store_backup_files: Efficiently store backup files
  remote_storage: Remote storage
  restore_from_remote_backup: Restore from remote backup
---

# Backup and restore

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | * Backup archives are *not guaranteed to be compatible* across major and minor server releases. *Restore backups only on directory servers of the same major or minor version.*

  To share data between servers of different versions, either use replication, or use LDAP Data Interchange Format (LDIF) *(tooltip: \<div class="paragraph">&#xA;\<p>An IETF standard file format for representing LDAP directory content and modifications to directory content. Typically used to import and export LDAP-based directory information.\</p>&#xA;\</div>)*.

* DS servers use cryptographic keys to sign and verify the integrity of backup files, and to encrypt data. Servers protect these keys by encrypting them with the shared master key for a deployment. For portability, servers store the encrypted keys in the backup files.

  Any server can therefore restore a backup taken with the same server version, *as long as it holds a copy of the shared master key used to encrypt the keys*. |

## How backup works

DS directory servers store data in backends *(tooltip: \<div class="paragraph">
\<p>A repository to store directory data. Different implementations with different capabilities exist.\</p>
\</div>)*. The amount of data in a backend varies depending on your deployment. It can range from very small to very large. A JE backend can hold billions of LDAP entries, for example.

### Backup process

A JE backend stores data on disk using append-only log files with names like `number.jdb`. The JE backend writes updates to the highest-numbered log file. The log files grow until they reach a specified size (default: 1 GB). When the current log file reaches the specified size, the JE backend creates a new log file.

To avoid an endless increase in database size on disk, JE backends clean their log files in the background. A cleaner thread copies active records to new log files. Log files that no longer contain active records are deleted.

The DS backup process takes advantage of this log file structure. Together, a set of log files represents a backend at a point in time. The backup process essentially copies the log files to the backup directory. DS also protects the data and adds metadata to keep track of the log files it needs to restore a JE backend to the state it had when the backup task completed.

### Cumulative backups

DS backups are cumulative in nature. Backups reuse the JE files that did not change since the last backup operation. They only copy the JE files the backend created or changed. Files that did not change are shared between backups.

A set of backup files is fully standalone.

### Purge old backups

Backup tasks keep JE files until you purge them.

The backup purge operation prevents an endless increase in the size of the backup folder on disk. The purge operation does not happen automatically; you choose to run it. When you run a purge operation, it removes the files for old or selected backups. The purge does not impact the integrity of the backups DS keeps. It only removes log files that do not belong to any remaining backups.

## Back up

When you set up a directory server, the process creates a `/path/to/opendj/bak/` directory. You can use this for backups if you have enough local disk space, and when developing or testing backup processes. In deployment, store backups remotely to avoid losing your data and backups in the same crash.

### Back up data (server task)

When you schedule a backup as a server task, the DS server manages task completion. The server must be running when you schedule the task, and when the task runs:

1. Schedule the task on a running server, binding as a user with the `backend-backup` administrative privilege.

   The following example schedules an immediate backup task for the `dsEvaluation` backend:

   ```console
   $ dsbackup \
    create \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --backupLocation bak \
    --backendName dsEvaluation
   ```

   To back up all backends, omit the `--backendName` option.

   To back up more than one backend, specify the `--backendName` option multiple times.

   For details, refer to [dsbackup](../tools-reference/dsbackup.html).

### Back up data (scheduled task)

When you schedule a backup as a server task, the DS server manages task completion. The server must be running when you schedule the task, and when the task runs:

1. Schedule backups using the `crontab` format with the `--recurringTask` option.

   The following example schedules nightly online backup of all user data at 2 AM, notifying `diradmin@example.com` when finished, or on error:

   ```console
   $ dsbackup \
    create \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --backupLocation bak \
    --recurringTask "00 02 * * *" \
    --description "Nightly backup at 2 AM" \
    --taskId NightlyBackup \
    --completionNotify diradmin@example.com \
    --errorNotify diradmin@example.com
   ```

   For details, refer to [dsbackup](../tools-reference/dsbackup.html).

   Use the [manage-tasks](../tools-reference/manage-tasks.html) command to manage scheduled tasks. For background, read [Server tasks](server-process.html#server-tasks). For an example command, refer to [Status and tasks](../monitoring-guide/monitoring-status-and-tasks.html).

### Back up data (external command)

When you back up data without contacting the server, the `dsbackup create` command runs as an external command, independent of the server process. It backs up the data whether the server is running or not.

|   |                                                                                                                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When you back up LDIF-based backends with this method, the command does not lock the files. To avoid corrupting the backup files, do not run the `dsbackup create --offline` command on an LDIF backend simultaneously with any changes to the backend.This applies to LDIF backends, schema files, and the task backend, for example. |

Use this method to schedule backup with a third-party tool, such as the `cron` command:

1. Back up data without contacting the server process, and use the `--offline` option.

   The following example backs up the `dsEvaluation` backend immediately:

   ```console
   $ dsbackup \
    create \
    --offline \
    --backupLocation bak \
    --backendName dsEvaluation
   ```

   To back up all backends, omit the `--backendName` option.

   To back up more than one backend, specify the `--backendName` option multiple times.

   For details, refer to [dsbackup](../tools-reference/dsbackup.html).

### Back up configuration files

When you back up directory data using the `dsbackup` command, you do not back up server configuration files. The server stores configuration files under the `/path/to/opendj/config/` directory.

The server records snapshots of its configuration under the `/path/to/opendj/var/` directory. You can use snapshots to recover from misconfiguration performed with the `dsconfig` command. *Snapshots only reflect the main configuration file, `config.ldif`.*

1. Stop the server:

   ```console
   $ stop-ds
   ```

2. Back up the configuration files:

   ```console
   $ tar -zcvf backup-config-$(date +%s).tar.gz config
   ```

   By default, this backup includes the server keystore, so store it securely.

3. Start the server:

   ```console
   $ start-ds
   ```

### Back up using snapshots

Use the `dsbackup` command when possible for backup and restore operations. You can use snapshot technology as an alternative to the `dsbackup` command, but you must be careful how you use it.

While DS directory servers are running, database backend cleanup operations write data even when there are no pending client or replication operations. An ongoing file system backup operation may record database log files that are not in sync with each other.

Successful recovery after restore is only guaranteed under certain conditions.

The snapshots must:

* Be *atomic*, capturing the state of all files at exactly the same time.

  *If you are not sure that the snapshot technology is atomic, do not use it. Use the `dsbackup` command instead.*

  For example, Kubernetes deployments can use volume snapshots when the underlying storage supports atomic snapshots. Learn more in [Backup and restore using volume snapshots](https://docs.pingidentity.com/forgeops/2025.2/backup/snapshots.html).

  In contrast, *do not use VMWare snapshots* to back up a running DS server.

* Capture the state of all data (`db/`) and (`changelogDb/`) changelog files together.

  When using a file system-level snapshot feature, for example, keep at least all data and changelog files on the same file system. This is the case in a default server setup.

* Be paired with a specific server configuration.

  A snapshot of all files includes configuration files that may be specific to one DS server, and cannot be restored safely on another DS server with a different configuration. If you restore all system files, this principle applies to system configuration as well.

  For details on making DS configuration files as generic as possible, refer to [Property value substitution](../configref/expressions.html).

If snapshots in your deployment do not meet these criteria, *you must stop the DS server before taking the snapshot*. You must also take care not to restore incompatible configuration files.

**Backup and restore options**

|                           | `dsbackup` commands                                                                                   | Snapshots                                                                                |
| ------------------------- | ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| What is backed up         | DS backend data only                                                                                  | Potentially everything; at minimum DS backends, changelogs                               |
| Incremental backups       | Yes                                                                                                   | Depends on the snapshot tools                                                            |
| Portability               | Yes; restore backend data on any DS of the same major/minor version                                   | Depends; potentially limited to the same environment as with Kubernetes volume snapshots |
| Disaster recovery         | Optimal; restore data and delete old changelog                                                        | Potentially restores changelog only to clear it during recovery                          |
| Recover single server     | Potentially slower while rebuilding the local changelog; impacts the change number index (if enabled) | Optimal; restores everything to the previous state                                       |
| Choice of what to restore | Good; you choose which backends to restore                                                            | Bad; you restore the file system, potentially rolling back multiple backends at once     |
| Ease of use               | Medium; you must understand `dsbackup` commands and choose what to restore                            | Medium; you must understand platform tools and impact of restoring everything at once    |

## Restore

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | After you restore a replicated backend, replication brings it up to date with changes newer than the backup. Replication uses internal change log records to determine which changes to apply. This process happens *even if you only have a single server* that you configured for replication at setup time (by setting the replication port with the `--replicationPort port` option). To prevent replication from replaying changes newer than the backup you restore, refer to [Disaster recovery](../use-cases/disaster-recovery.html).Replication purges internal change log records, however, to prevent the change log from growing indefinitely. Replication can only bring the backend up to date if the change log still includes the last change backed up.For this reason, when you restore a replicated backend from backup, *the backup must be newer than the last purge of the replication change log (default: 3 days).*If no backups are newer than the replication purge delay, do not restore from a backup. Initialize the replica instead, without using a backup. For details, refer to [Manual initialization](../config-guide/repl-init.html). |

### Restore data (server task)

1. Verify the backup you intend to restore.

   The following example verifies the most recent backup of the `dsEvaluation` backend:

   ```console
   $ dsbackup \
    list \
    --backupLocation bak \
    --backendName dsEvaluation \
    --last \
    --verify
   ```

2. Schedule the restore operation as a task, binding as a user with the `backend-restore` administrative privilege.

   The following example schedules an immediate restore task for the `dsEvaluation` backend:

   ```console
   $ dsbackup \
    restore \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --backupLocation bak \
    --backendName dsEvaluation
   ```

   To restore the latest backups of more than one backend, specify the `--backendName` option multiple times.

   To restore a specific backup, specify the `--backupId` option. To restore multiple specific backups of different backends, specify the `--backupId` option multiple times.

   To list backup information without performing verification, use the `dsbackup list` command without the `--verify` option. The output includes backup IDs for use with the `--backupId` option.

   For details, refer to [dsbackup](../tools-reference/dsbackup.html).

### Restore data (external command)

1. Stop the server if it is running:

   ```console
   $ stop-ds --quiet
   ```

2. Verify the backup you intend to restore.

   The following example verifies the most recent backup of the `dsEvaluation` backend:

   ```console
   $ dsbackup \
    list \
    --backupLocation bak \
    --backendName dsEvaluation \
    --last \
    --verify
   ```

3. Restore using the `--offline` option.

   The following example restores the `dsEvaluation` backend:

   ```console
   $ dsbackup \
    restore \
    --offline \
    --backupLocation bak \
    --backendName dsEvaluation
   ```

   To restore the latest backups of more than one backend, specify the `--backendName` option multiple times.

   To restore a specific backup, specify the `--backupId` option. To restore multiple specific backups of different backends, specify the `--backupId` option multiple times.

   To list backup information without performing verification, use the `dsbackup list` command without the `--verify` option. The output includes backup IDs for use with the `--backupId` option.

   For details, refer to [dsbackup](../tools-reference/dsbackup.html).

4. Start the server:

   ```console
   $ start-ds --quiet
   ```

### Restore configuration files

1. Stop the server:

   ```console
   $ stop-ds --quiet
   ```

2. Restore the configuration files from the backup, overwriting existing files:

   ```console
   $ tar -zxvf backup-config-<date>.tar.gz
   ```

3. Start the server:

   ```console
   $ start-ds --quiet
   ```

### Restore from a snapshot

Use the `dsbackup` command when possible for backup and restore operations.

You can use snapshot technology as an alternative to the `dsbackup` command, but you must be careful how you use it. For details, refer to [Back up using snapshots](#backup-snapshot).

Take the following points into account before restoring a snapshot:

* When you restore files for a replicated backend, *the snapshot must be newer than the last purge of the replication change log (default: 3 days).*

* Stop the DS server before you restore the files.

* The DS configuration files in the snapshot must match the configuration where you restore the snapshot.

  If the configuration uses expressions, define their values for the current server before starting DS.

* When using snapshot files to initialize replication, only restore the data (`db/`) files for the target backend.

  Depending on the snapshot technology, you might need to restore the files separately, and then move only the target backend files from the restored snapshot.

* When using snapshot files to restore replicated data to a known state, stop all affected servers before you restore.

## Purge old files

Periodically purge old backup files with the `dsbackup purge` command. The following example removes all backup files older than the default replication purge delay:

```console
$ dsbackup \
 purge \
 --offline \
 --backupLocation bak \
 --olderThan 3d
```

This example runs the external command without contacting the server process. You can also purge backups by ID, or by backend name, and you can specify the number of backups to keep. For details, refer to [dsbackup](../tools-reference/dsbackup.html).

To purge files as a server task, use the task options, such as `--recurringTask`. The user must have the `backend-backup` administrative privilege to schedule a purge task.

## Cloud storage

You can push backup files to cloud storage and restore them from cloud storage.

Mount the cloud storage as a local filesystem and use the mount point as a local backup location. This approach works with the same commands and procedures as for local backups.

To mount the cloud storage as a local filesystem, use third-party tools such as the following:

* [Mountpoint for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mountpoint.html)

* [BlobFuse for Azure Cloud Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/blobfuse2-what-is)

* [Cloud Storage FUSE for Google Cloud Storage](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview?hl=en)

|   |                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------- |
|   | Ping Identity supports the DS backup and restore commands, not the third-party cloud storage filesystem tools. |

## Efficiently store backup files

DS backups are collections of files in a backup directory. To restore from backup, DS requires a coherent collection of backup files.

You can use the [dsbackup](../tools-reference/dsbackup.html) command to purge stale backup files from a backup directory. When you purge stale backup files, the command leaves a coherent collection of files you can use to restore data.

You should also store copies of backup files remotely to guard against the loss of data in a disaster.

### Remote storage

Perform the following steps to store copies of backup files remotely in an efficient way. These steps address backup of directory data, which is potentially very large, not [backup of configuration data](#backup-config), which is almost always small:

1. Choose a local directory or local network directory to hold backup files.

   Alternatively, you can back up to [cloud storage](#cloud-storage).

2. Schedule a regular backup task to back up files to the directory you chose.

   Make sure that the backup task runs more often than the replication purge delay. For example, schedule the backup task to run every three hours for a default purge delay of three days. Each time the task runs, it backs up only new directory backend files.

   For details, refer to the steps for [backing up directory data.](#backup)

3. Store copies of the local backup files at a remote location for safekeeping:

   1. [Purge old files](#purge) in the local backup directory.

      As described in [How backup works](#how-backup-works), DS backups are cumulative in nature; DS reuses common data that has not changed from previous backup operations when backing up data again. The set of backup files is fully standalone.

      The purge removes stale files without impacting the integrity of newer backups, reducing the volume of backup files to store when you copy files remotely.

   2. Regularly copy the backup directory and all the files it holds to a remote location.

      For example, copy all local backup files every day to a remote directory called `bak-date`:

      ```console
      $ ssh user@remote-storage mkdir /path/to/bak-date
      $ scp -R /path/to/bak/* user@remote-storage:/path/to/bak-date/
      ```

4. Remove old `bak-date` directories from remote storage in accordance with the backup policy for the deployment.

### Restore from remote backup

For each DS directory server to restore:

1. Install DS using the same [cryptographic keys and deployment ID](../security-guide/pki.html).

   Backup files are protected using keys derived from the DS deployment ID and password. You must use the same ones when recovering from a disaster.

2. [Restore configuration files](#restore-config).

3. [Restore](#restore) directory data from the latest remote backup folder.

After restoring all directory servers, validate that the restore procedure was a success.

---

---
title: Maintenance
description: "Overview of recurring PingDS administrative operations: tools, server process management, backup and restore, moving servers, and troubleshooting."
component: pingds
version: 8.1
page_id: pingds:maintenance-guide:preface
canonical_url: https://docs.pingidentity.com/pingds/8.1/maintenance-guide/preface.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["LDAP", "Setup &amp; Configuration"]
page_aliases: ["index.adoc"]
---

# Maintenance

These pages cover recurring administrative operations.

[icon: wrench, set=fas, size=3x]

#### [Tools](admin-tools.html)

Run DS command-line tools.

[icon: server, set=fas, size=3x]

#### [Server process](server-process.html)

Start, stop, restart DS.

[icon: hdd, set=fas, size=3x]

#### [Backup/restore](backup-restore.html)

Backup and restore data.

[icon: suitcase, set=fas, size=3x]

#### [Move a server](mv-servers.html)

Move a server to a new host.

[icon: tachometer-alt, set=fas, size=3x]

#### [Tuning](tuning.html)

Tune server performance.

[icon: ambulance, set=fas, size=3x]

#### [Troubleshooting](troubleshooting.html)

Solve common problems.

---

---
title: Maintenance tools
description: Reference for PingDS command-line tools, including tool usage, filesystem and version constraints, and descriptions of every available command.
component: pingds
version: 8.1
page_id: pingds:maintenance-guide:admin-tools
canonical_url: https://docs.pingidentity.com/pingds/8.1/maintenance-guide/admin-tools.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Features", "LDAP", "Setup &amp; Configuration"]
section_ids:
  cli-overview: Server commands
  trusted_certificates: Trusted certificates
  tools-properties: Default settings
---

# Maintenance tools

## Server commands

* Add DS server command-line tools to your PATH:

  * Bash

  * PowerShell

  ```console
  $ export PATH=/path/to/opendj/bin:$\{PATH}
  ```

  ```powershell
  $env:PATH += ";C:\path\to\opendj\bat"
  ```

* For reference information, use the `--help` option with any DS tool.

* All commands call Java programs. This means every command starts a JVM, so it takes longer to start than a native binary.

* The DS `bash-completion` command generates a completion script for the Bash shell that makes it easier to write other DS commands.

  The completion script depends on support for `bash-completion`, which is not included by default on macOS.

  To set up Bash completion for DS commands, source the output of the script:

  * Bash 4

  * Bash 3.2 macOS

  ```bash
  source <(/path/to/opendj/bin/bash-completion)
  ```

  ```bash
  # First, install bash-completion support.
  # Next:
  eval "$( /path/to/opendj/bin/bash-completion )"
  ```

  You can make completion available in any new interactive shell by adding it to your `~/.bash_profile` file, or `~/.bashrc` file if it is loaded by the new shell.

| DS running on…​     | DS installed from…​ | Default path to tools…​ |
| ------------------- | ------------------- | ----------------------- |
| Linux distributions | .zip                | `/path/to/opendj/bin`   |
| Linux distributions | .deb, .rpm          | `/opt/opendj/bin`       |
| Microsoft Windows   | .zip                | `C:\path\to\opendj\bat` |

The installation and upgrade tools, `setup`, and `upgrade`, are found in the parent directory of the other tools. These tools are not used for everyday administration.

| Commands                                                                                                                                                                       | Constraints                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dsbackup` `dsconfig` `export-ldif` `import-ldif` `rebuild-index` `setup` `setup-profile` `start-ds`                                                                           | When the server is offline, or when running commands in offline mode, these commands can modify server files. They must, therefore, access server files as a user who has the same filesystem permissions as the user who installs and runs the server.For most systems, the simplest way to achieve this is to run the command as the same user who installs and runs the server. When following best practices for auditing and separation of duty, provision administrative and server user accounts with compatible group or access control list permissions. |
| `backendstat` `create-rc-script` `encode-password` `setup` `setup-profile` `start-ds` `supportextract` `upgrade` `windows-service`                                             | These commands must be used with the local DS server in the same installation as the tools.These commands are not useful with non-DS servers.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `dsbackup` `changelogstat` `dsconfig` `dsrepl` `encode-password` `export-ldif` `import-ldif` `manage-account` `manage-tasks` `rebuild-index` `status` `stop-ds` `verify-index` | These commands must be used with DS servers having the same version as the command.These commands are not useful with non-DS servers.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `makeldif`                                                                                                                                                                     | This command depends on template files. The template files can make use of configuration files installed with DS servers under `config/MakeLDIF/`.The LDAP Data Interchange Format (LDIF) *(tooltip: \<div class="paragraph">&#xA;\<p>An IETF standard file format for representing LDAP directory content and modifications to directory content. Typically used to import and export LDAP-based directory information.\</p>&#xA;\</div>)* output can be used with any directory server.                                                                         |
| `base64` `ldapcompare` `ldapdelete` `ldapmodify` `ldappasswordmodify` `ldapsearch` `ldifdiff` `ldifmodify` `ldifsearch`                                                        | These commands can be used independently of DS servers, and are not tied to a specific version.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

| Command(1)                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `addrate`                   | Measure add and delete throughput and response time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `authrate`                  | Measure bind throughput and response time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `backendstat`               | Debug databases for pluggable backends.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `base64`                    | Encode and decode data in base64 format.Base64-encoding represents binary data in ASCII, and can be used to encode character strings in LDIF, for example.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `bash-completion`           | Generate a completion script for use with Bash shell. Requires `bash-completion` support.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `changelogstat`             | Debug file-based changelog databases.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `create-rc-script` (Linux)  | Generate a `systemd` service to start, stop, and restart the server, either directly or at system boot and shutdown.This lets you register and manage DS servers as services on Linux systems.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `dsbackup`                  | Back up or restore directory data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `dskeymgr`                  | Generate a deployment ID, a shared master key, a private CA certificate based on a deployment ID and password, or a key pair with the certificate signed by the private CA.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `dsconfig`                  | The `dsconfig` command is the primary command-line tool for viewing and editing DS server configurations. When started without arguments, `dsconfig` prompts you for administration connection information. Once connected to a running server, it presents you with a menu-driven interface to the server configuration.To edit the configuration when the server is not running, use the `--offline` command.Some advanced properties are not visible by default when you run the `dsconfig` command interactively. Use the `--advanced` option to access advanced properties.When you pass connection information, subcommands, and additional options to `dsconfig`, the command runs in script mode, so it is not interactive.You can prepare `dsconfig` batch scripts with the `--commandFilePath` option in interactive mode, then read from the batch file with the `--batchFilePath` option in script mode. Batch files can be useful when you have many `dsconfig` commands to run, and want to avoid starting the JVM for each command.Alternatively, you can read commands from standard input with the `--batch` option. |
| `dsrepl`                    | Manage data replication between directory servers to keep their contents in sync.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `encode-password`           | Encode a plaintext password according to one of the available storage schemes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `export-ldif`               | Export directory data to LDIF, the standard, portable, text-based representation of directory content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `import-ldif`               | Load LDIF content into the directory, which overwrites existing data. It cannot be used to append data to the backend database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `ldapcompare`               | Compare the attribute values you specify with those stored on entries in the directory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `ldapdelete`                | Delete one entry or an entire branch of subordinate entries in the directory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `ldapmodify`                | Modify the specified attribute values for the specified entries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `ldappasswordmodify`        | Modify user passwords.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `ldapsearch`                | Search a branch of directory data for entries that match the LDAP filter you specify.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `ldifdiff`                  | Display differences between two LDIF files. The output is LDIF.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `ldifmodify`                | Similar to the `ldapmodify` command, modify specified attribute values for specified entries in an LDIF file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `ldifsearch`                | Similar to the `ldapsearch` command, search a branch of data in LDIF for entries matching the LDAP filter you specify.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `makeldif`                  | Generate directory data in LDIF based on templates that define how the data should appear.The `makeldif` command generates test data that mimics data expected in production, and does not compromise real, potentially private information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `manage-account`            | Lock and unlock user accounts, and view and manipulate password policy state information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `manage-tasks`              | View information about tasks scheduled to run in the server, and cancel specified tasks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `modrate`                   | Measure modification throughput and response time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `rebuild-index`             | Rebuild an index stored in an indexed backend.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `searchrate`                | Measure search throughput and response time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `setup-profile`             | Configure a setup profile after initial installation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `start-ds`                  | Start one DS server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `status`                    | Display information about the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `stop-ds`                   | Stop one DS server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `supportextract`            | Collect troubleshooting information for technical support purposes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `verify-index`              | Verify that an index stored in an indexed backend is not corrupt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `windows-service` (Windows) | Register and manage one DS server as a Windows service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

(1) Linux names for the commands. Equivalent Windows commands have .bat extensions.

## Trusted certificates

When a client tool initiates a secure connection to a server, the server presents its digital certificate.

The tool must decide whether it does trust the server certificate and continues to negotiate a secure connection, or doesn't trust the server certificate and drops the connection. To trust the server certificate, the tool's truststore must contain the trusted certificate. The trusted certificate is a CA certificate, or the self-signed server certificate.

The following table explains how the tools locate the truststore.

| Truststore Option                        | Truststore Used                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| None                                     | The default truststore, `user.home/.opendj/keystore`, where *user.home* is the Java system property. *user.home* is `$HOME` on Linux and `%USERPROFILE%` on Windows. The keystore password is `OpenDJ`. Do not change the file name or the password.- In interactive mode, DS command-line tools prompt for approval to trust an unrecognized certificate, and whether to store it in the default truststore for future use.

- In silent mode, the tools rely on the default truststore. |
| `--use<Type>TrustStore {trustStorePath}` | DS only uses the specified truststore. The *\<Type>* in the option name reflects the trust store type.The tool fails with an error if it can't trust the server certificate.                                                                                                                                                                                                                                                                                                              |

## Default settings

You can set defaults in the `~/.opendj/tools.properties` file, as in the following example:

```ini
hostname=localhost
port=4444
bindDN=editable:dsAdminDN["uid=admin"]
bindPassword\:file=/path/to/.pwd
useSsl=true
trustAll=true
```

When you use an option with a colon, such as `bindPassword:file`, escape the colon with a backslash (`\:`) in the properties file.

The file location on Windows is `%UserProfile%\.opendj\tools.properties`.

---

---
title: Move a server
description: Move a PingDS server to a new host by stopping it, renewing the server certificate, updating the configuration, and transferring server files.
component: pingds
version: 8.1
page_id: pingds:maintenance-guide:mv-servers
canonical_url: https://docs.pingidentity.com/pingds/8.1/maintenance-guide/mv-servers.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Install", "LDAP", "Setup &amp; Configuration"]
---

# Move a server

The following procedure moves a server to the new host `new-server.example.com`. The steps skip creation of system accounts, startup scripts, and registration as a Windows service:

1. Stop the server:

   ```console
   $ stop-ds
   ```

2. Renew the server certificate to account for the new hostname.

   Skip this step if the server certificate is a wildcard certificate that is already valid for the new hostname.

   The following command renews the server certificate generated with a deployment ID and password:

   ```console
   $ dskeymgr \
    create-tls-key-pair \
    --deploymentId $DEPLOYMENT_ID \
    --deploymentIdPassword password \
    --keyStoreFile /path/to/opendj/config/keystore \
    --keyStorePassword:file /path/to/opendj/config/keystore.pin \
    --hostname localhost \
    --hostname new-server.example.com \
    --subjectDn CN=DS,O=PingIdentity.com
   ```

   For more command options, refer to [dskeymgr](../tools-reference/dskeymgr.html). The default validity for the certificate is one year.

3. Find and replace the old hostname with the new hostname in the server's configuration file, `config/config.ldif`.

   The following list includes configuration settings that may specify the server hostname:

   * `ds-cfg-advertised-listen-address`

   * `ds-cfg-bootstrap-replication-server`

   * `ds-cfg-listen-address`

   * `ds-cfg-server-fqdn`

   * `ds-cfg-source-address`

4. Move all files in the `/path/to/opendj` directory to the new server.

5. Start the server:

   ```console
   $ start-ds
   ```

6. If the server you moved is referenced by others as a replication bootstrap server, update the replication bootstrap server configuration on those servers.

---

---
title: Server processes
description: Start, stop, and restart PingDS servers on Linux and Windows, manage server tasks, and recover from crashes or disorderly shutdowns.
component: pingds
version: 8.1
page_id: pingds:maintenance-guide:server-process
canonical_url: https://docs.pingidentity.com/pingds/8.1/maintenance-guide/server-process.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Features", "LDAP"]
section_ids:
  start-server: Start a server
  stop-server: Stop a server
  stop-server-cleanly: Clean server retirement
  restart-server: Restart a server
  server-tasks: Server tasks
  crash-recovery: Server recovery
---

# Server processes

## Start a server

* Start the server in the background:

  ```console
  $ start-ds
  ```

  Alternatively, specify the `--no-detach` option to start the server in the foreground.

* (Linux) If the DS server was installed from a .deb or .rpm package, then service management scripts were created at setup time:

  ```none
  centos# service opendj start

  Starting opendj (via systemctl):                           [  OK  ]
  ```

  ```none
  ubuntu$ sudo service opendj start

  $Starting opendj: > SUCCESS.
  ```

* (Linux) Use a `systemd` service to manage DS.

  ```none
  # Create the service.
  # Unless you run DS as root,
  # set --userName to the user who installed the server:
  $ sudo create-rc-script \
  --systemdService /etc/systemd/system/opendj.service \
  --userName opendj

  # Register the service you created:
  $ sudo systemctl daemon-reload
  ```

  Manage the service with `systemctl`.

  ```console
  $ sudo systemctl start opendj
  ```

* (Windows) Register the DS server as a Windows service:

  ```powershell
  windows-service.bat --enableService
  ```

  Manage the service with Windows-native administration tools.

## Stop a server

Although DS servers are designed to recover from failure and disorderly shutdown, it is safer to shut the server down cleanly, because a clean shutdown reduces startup delays. During startup, the server attempts to recover database backend state. Clean shutdown prevents situations where the server cannot recover automatically.

### Clean server retirement

1. Before shutting down the system where the server is running, and before detaching any storage used for directory data, cleanly stop the server using one of the following techniques:

   * Use the `stop-ds` command:

     ```console
     $ stop-ds
     ```

   * (Linux) If the DS server was installed from a .deb or .rpm package, then service management scripts were created at setup time:

     ```none
     centos# service opendj stop

     Stopping opendj (via systemctl):                           [  OK  ]
     ```

     ```none
     ubuntu$ sudo service opendj stop

     $Stopping opendj: ... > SUCCESS.
     ```

   * (Linux) Use a `systemd` service to manage DS.

     ```none
     # Create the service.
     # Unless you run DS as root,
     # set --userName to the user who installed the server:
     $ sudo create-rc-script \
     --systemdService /etc/systemd/system/opendj.service \
     --userName opendj

     # Register the service you created:
     $ sudo systemctl daemon-reload
     ```

     Manage the service with `systemctl`.

     ```console
     $ sudo systemctl stop opendj
     ```

   * (Windows) Register the DS server once as a Windows service:

     ```powershell
     windows-service.bat --enableService
     ```

     Manage the service with Windows-native administration tools.

   *Do not intentionally kill the DS server process* unless the server is completely unresponsive. When stopping cleanly, the server writes state information to database backends, and releases locks that it holds on database files.

## Restart a server

* Use the `stop-ds` command:

  ```console
  $ stop-ds --restart
  ```

* (Linux) If the DS server was installed from a .deb or .rpm package, then service management scripts were created at setup time:

  ```none
  centos# service opendj restart

  Restarting opendj (via systemctl):                         [  OK  ]
  ```

  ```none
  ubuntu$ sudo service opendj restart

  $Stopping opendj: ... > SUCCESS.

  $Starting opendj: > SUCCESS.
  ```

* (Linux) Use a `systemd` service to manage DS.

  ```none
  # Create the service.
  # Unless you run DS as root,
  # set --userName to the user who installed the server:
  $ sudo create-rc-script \
  --systemdService /etc/systemd/system/opendj.service \
  --userName opendj

  # Register the service you created:
  $ sudo systemctl daemon-reload
  ```

  Manage the service with `systemctl`.

  ```console
  $ sudo systemctl restart opendj
  ```

* (Windows) Register the DS server once as a Windows service:

  ```powershell
  windows-service.bat --enableService
  ```

  Manage the service with Windows-native administration tools.

## Server tasks

The following server administration commands can be run in online and offline mode. They invoke data-intensive operations, and so potentially take a long time to complete. The links below are to the reference documentation for each command:

* [dsbackup](../tools-reference/dsbackup.html)

* [export-ldif](../tools-reference/export-ldif.html)

* [import-ldif](../tools-reference/import-ldif.html)

* [rebuild-index](../tools-reference/rebuild-index.html)

When you run these commands in online mode, they run as tasks *(tooltip: \<div class="paragraph">
\<p>A mechanism for remote access to server administrative actions.\</p>
\</div>)* on the server. Server tasks are scheduled operations that can run one or more times as long as the server is up. For example, you can schedule the `dsbackup` and `export-ldif` commands to run recurrently to back up server data on a regular basis.

You schedule a task as a directory administrator, sending the request to the administration port. You can therefore schedule a task on a remote server if you choose. When you schedule a task on a server, the command returns immediately, yet the task can start later, and might run for a long time before it completes. Use the [manage-tasks](../tools-reference/manage-tasks.html) command to manage scheduled tasks. For an example command, refer to [Status and tasks](../monitoring-guide/monitoring-status-and-tasks.html).

Although you can schedule a server task on a remote server, *the data for the task must be accessible to the server locally*. For example, when you schedule a backup task on a remote server, that server writes backup files to a file system on the remote server. Similarly, when you schedule a restore task on a remote server, that server restores backup files from a file system on the remote server.

The reference documentation describes the available options for each command:

* Configure email notification for success and failure

* Define alternatives on failure

* Start tasks immediately (`--start 0`)

* Schedule tasks to start at any time in the future

## Server recovery

DS servers can restart after a crash or after the server process is killed abruptly. After disorderly shutdown, the DS server must recover its database backends. Generally, DS servers return to service quickly.

Database recovery messages are found in the database log file, such as `/path/to/opendj/db/userData/dj.log`.

The following example shows two example messages from the recovery log. The first message is written at the beginning of the recovery process. The second message is written at the end of the process:

```none
[/path/to/opendj/db/userData]Recovery underway, found end of log
...
[/path/to/opendj/db/userData]Recovery finished: Recovery Info ...
```

The JVM's heap-based database cache is lost when the server stops or crashes. The cache must therefore be reconstructed from the directory database files. Database files might still be in the filesystem cache on restart, but rebuilding the JVM's heap-based database cache takes time. DS servers start accepting client requests before this process is complete.

---

---
title: Troubleshooting
description: Troubleshoot PingDS installation, performance, security, client connection, and replication problems, including debug logging and Java Flight Recorder.
component: pingds
version: 8.1
page_id: pingds:maintenance-guide:troubleshooting
canonical_url: https://docs.pingidentity.com/pingds/8.1/maintenance-guide/troubleshooting.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-08T11:44:16Z
keywords: ["Install", "LDAP", "Replication", "Security", "Troubleshooting"]
section_ids:
  troubleshoot-identify-problem: Define the problem
  troubleshoot-perfs: Performance
  troubleshoot-installation: Installation problems
  use_the_logs: Use the logs
  antivirus_interference: Antivirus interference
  je_initialization: JE initialization
  file_notification: File notification
  nosuchalgorithmexception: NoSuchAlgorithmException
  troubleshoot-reset-admin-passwords: Forgotten superuser password
  troubleshoot-use-jfr: Java Flight Recorder
  troubleshoot-enable-debug-logging: Debug-level logging
  troubleshoot-use-lockdown-mode: Lockdown mode
  troubleshoot-import: LDIF import
  troubleshoot-secure-connections: Security problems
  troubleshoot-incompatible-java-versions: Incompatible Java versions
  troubleshoot-incompatible-java-versions-new-key: Overcome incompatible Java versions to generate new keys
  troubleshoot-incompatible-java-versions-add-server: Overcome incompatible Java versions when adding new servers
  troubleshoot-certificate-authentication: Certificate-based authentication
  troubleshoot-fips: FIPS and key wrapping
  troubleshoot-compromised-key: Compromised keys
  troubleshoot-connections: Client problems
  use_the_logs_2: Use the logs
  client_access: Client access
  simple_paged_results: Simple paged results
  troubleshoot-repl: Replication problems
  replicas_do_not_connect: Replicas do not connect
  temporary_delays: Temporary delays
  use_the_logs_3: Use the logs
  troubleshoot-stale-data: Stale data
  incorrect_configuration: Incorrect configuration
  troubleshoot-get-help: Support
---

# Troubleshooting

## Define the problem

To solve your problem, save time by clearly defining it first. A problem statement *compares the difference between observed behavior and expected behavior*:

* What exactly is the problem?

  What is the behavior you expected?

  What is the behavior you observed?

* How do you reproduce the problem?

* When did the problem begin?

  Under similar circumstances, when does the problem not occur?

* Is the problem permanent?

  Intermittent?

  Is it getting worse? Getting better? Staying the same?

## Performance

Before troubleshooting performance, make sure:

* The system meets the DS [installation requirements](https://docs.pingidentity.com/pingds/release-notes/requirements.html).

* The [performance expectations are reasonable](../config-guide/tuning.html#perf-define-starting-points).

  For example, a deployment can use password policies with [cost-based, resource-intensive password storage schemes](../security-guide/pwp-strong-safe.html#configure-pwd-storage) such as Argon2, Bcrypt, PBKDF2, or Scrypt. This protects passwords at the cost of slow LDAP simple binds or HTTP username/password authentications and lower throughput.

When directory operations take too long, meaning request latency is high, fix the problem first in your test or staging environment. Perform these steps in order and stop when you find a fix:

1. Check for [unindexed searches](../config-guide/idx-what.html#review-unindexed-searches) and prevent them when possible.

   Unindexed searches are expensive operations, particularly for large directories. When unindexed searches consume the server's resources, performance suffers for concurrent operations and for later operations if an unindexed search causes widespread changes to database and file system caches.

2. Check [performance settings](../config-guide/tuning.html#perf-tweaking) for the server including JVM heap size and DB cache size.

   Try adding more RAM if memory seems low.

3. Read the request queue monitoring statistics [over LDAP](../monitoring-guide/ldap-monitoring.html#monitoring-work-queue-ldap) or [over HTTP](../monitoring-guide/http-monitoring.html#monitoring-work-queue-http).

   If many requests are in the queue, the troubleshooting steps are different for read and write operations. Read and review the request statistics available [over LDAP](../monitoring-guide/ldap-monitoring.html#monitoring-operation-stats-ldap) or [over HTTP](../monitoring-guide/http-monitoring.html#monitoring-operation-stats-http).

   If you persistently have many:

   * Pending read requests, such as unindexed searches or big searches, try adding CPUs.

   * Pending write requests, try adding IOPS, such as faster or higher throughput disks.

## Installation problems

### Use the logs

Installation and upgrade procedures result in a log file tracing the operation. The command output shows a message like the following:

```
See opendj-setup-profile-*.log for a detailed log of the failed operation.
```

### Antivirus interference

Prevent antivirus and intrusion detection systems from interfering with DS software.

Before using DS software with antivirus or intrusion detection software, consider the following potential problems:

* **Interference with normal file access**

  Antivirus and intrusion detection systems that perform virus scanning, sweep scanning, or deep file inspection are not compatible with DS file access, particularly write access.

  Antivirus and intrusion detection software have incorrectly marked DS files as suspect to infection, because they misinterpret normal DS processing.

  *Prevent antivirus and intrusion detection systems from scanning DS files*, except these folders:

  * `C:\path\to\opendj\bat\`

    Windows command-line tools

  * `/path/to/opendj/bin/`

    Linux command-line tools

  * `/path/to/opendj/extlib/`

    Optional `.jar` files used by custom plugins

  * `/path/to/opendj/lib/`

    Scripts and libraries shipped with DS servers

* **Port blocking**

  Antivirus and intrusion detection software can block ports that DS uses to provide directory services.

  Make sure that your software does not block the ports that DS software uses. For details, refer to [Administrative access](../security-guide/os.html#os-admin).

* **Negative performance impact**

  Antivirus software consumes system resources, reducing resources available to other services including DS servers.

  Running antivirus software can therefore have a significant negative impact on DS server performance. Make sure that you test and account for the performance impact of running antivirus software before deploying DS software on the same systems.

### JE initialization

When starting a directory server on a Linux system, make sure the server user can watch enough files. If the server user cannot watch enough files, you might read an error message in the server log like this:

```
InitializationException: The database environment could not be opened:
com.sleepycat.je.EnvironmentFailureException: (JE version) /path/to/opendj/db/userData
or its sub-directories to WatchService.
UNEXPECTED_EXCEPTION: Unexpected internal Exception, may have side effects.
Environment is invalid and must be closed.
```

### File notification

A directory server backend database monitors file events. On Linux systems, backend databases use the inotify API for this purpose. The kernel tunable `fs.inotify.max_user_watches` indicates the maximum number of files a user can watch with the inotify API.

Make sure this tunable is set to at least 512K:

```console
$ sysctl fs.inotify.max_user_watches
```

Output

```
fs.inotify.max_user_watches = 524288
```

If this tunable is set lower than that, update the `/etc/sysctl.conf` file to change the setting permanently, and use the `sysctl -p` command to reload the settings:

```none
$ echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf
[sudo] password for admin:

$ sudo sysctl -p
fs.inotify.max_user_watches = 524288
```

### NoSuchAlgorithmException

When running the `dskeymgr create-deployment-id` or `setup` command on an operating system with no support for the `PBKDF2WithHmacSHA256` `SecretKeyFactory` algorithm, the command displays this error:

```
NoSuchAlgorithmException: PBKDF2WithHmacSHA256 SecretKeyFactory not available
```

This can occur on operating systems where the default settings limit the available algorithms.

To fix the issue, enable support for the algorithm and run the command again.

## Forgotten superuser password

By default, DS servers store the entry for the directory superuser in an LDAP Data Interchange Format (LDIF) *(tooltip: \<div class="paragraph">
\<p>An IETF standard file format for representing LDAP directory content and modifications to directory content. Typically used to import and export LDAP-based directory information.\</p>
\</div>)* backend *(tooltip: \<div class="paragraph">
\<p>A repository to store directory data. Different implementations with different capabilities exist.\</p>
\</div>)*. Edit the file to reset the password:

1. Generate the encoded version of the new password:

   ```console
   $ encode-password --storageScheme PBKDF2-HMAC-SHA256 --clearPassword password
   ```

   Output

   ```
   {PBKDF2-HMAC-SHA256}10<hash>
   ```

2. Stop the server while you edit the LDIF file for the backend:

   ```console
   $ stop-ds
   ```

3. Replace the existing password with the encoded version.

   In the `db/rootUser/rootUser.ldif` file, carefully replace the `userPassword` value with the new, encoded password:

   ```ldif
   dn: uid=admin
   ...
   uid: admin
   userPassword: 
   ```

   Trailing whitespace is significant in LDIF. *Take care not to add any trailing whitespace at the end of the line.*

4. Restart the server:

   ```console
   $ start-ds
   ```

5. Verify that you can use the directory superuser account with the new password:

   ```console
   $ status \
    --bindDn uid=admin \
    --bindPassword password \
    --hostname localhost \
    --port 4444 \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --script-friendly
   ```

   Output

   ```
   "isRunning" : true,
   ```

## Java Flight Recorder

DS servers support the Java Flight Recorder (JFR) tool. While DS runs, JFR collects diagnostic and profiling data with minimal overhead. JFR recordings are much smaller than access log files.

* On Linux systems, JFR support is enabled by default.

  DS keeps the last 30 minutes of JFR events. DS stores temporary files in the `/path/to/opendj/var/jfr` folder until it writes the information to a flight recording `.jfr` file in the `/path/to/opendj/var` folder.

  For additional flexibility, set `DS_JFR_ENABLED=false` for the `start-ds` command and use the `DS_JAVA_ARGS` environment variable to set additional standard JFR configuration options.

* On Windows systems, JFR support is not enabled.

  Use the `DS_JAVA_ARGS` environment variable with the `start-ds.bat` command to provide custom JFR settings.

When a problem arises and DS is running, use the `supportextract` command promptly to capture the events leading up to the problem before DS discards older JFR files. You can also use a `jcmd <pid> JFR.dump` command to get a flight recording while DS is running.

|   |                                                                                                                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | JFR captures the following types of potentially sensitive information for long-running requests:- Client IP addresses

- Usernames

- Names of entries

- Search filtersThe flight recordings are like a log with no filtering of sensitive fields. Protect the JFR files as you would any others containing sensitive information. |

Provide the flight recording files to Ping Identity support personnel. They use the flight recordings to examine the server's internal state at the time of the problem. The JFR files complement the other data captured by the `supportextract` command. They can help support pinpoint a problem in a way logs and monitoring data can't.

## Debug-level logging

DS error log message severity levels are:

* `ERROR` (highest severity)

* `WARNING`

* `NOTICE`

* `INFO`

* `DEBUG` (lowest severity)

By default, DS error log severity levels are set as follows:

* Log `ERROR`, `WARNING`, `NOTICE`, and `INFO` replication (`SYNC`) messages.

* Log `ERROR`, `WARNING`, and `NOTICE` messages for other message categories.

You can change these settings when necessary to log debug-level messages.

|   |                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------- |
|   | DS debug-level logging can generate a high volume of messages. Use debug-level logging very sparingly on production systems. |

1. Choose the category you want to debug:

   | Category                  | Description                                                          |
   | ------------------------- | -------------------------------------------------------------------- |
   | `BACKEND`                 | Server backends                                                      |
   | `BACKUP`                  | Backup procedures                                                    |
   | `CONFIG`                  | Configuration management                                             |
   | `CORE`                    | Core server operations                                               |
   | `DEFAULT`                 | Messages with no specific category                                   |
   | `EXTENSIONS`              | Reserved for custom extensions                                       |
   | `EXTERNAL`                | External libraries                                                   |
   | `JVM`                     | Java virtual machine information                                     |
   | `LOGGING`                 | Server log publishers                                                |
   | `PLUGIN`                  | Server plugins                                                       |
   | `PROTOCOL`                | Server protocols                                                     |
   | `PROTOCOL.ASN1`           | ASN.1 encoding                                                       |
   | `PROTOCOL.HTTP`           | HTTP                                                                 |
   | `PROTOCOL.LDAP`           | LDAP                                                                 |
   | `PROTOCOL.LDAP_CLIENT`    | LDAP SDK client features                                             |
   | `PROTOCOL.LDAP_SERVER`    | LDAP SDK server features                                             |
   | `PROTOCOL.LDIF`           | LDIF                                                                 |
   | `PROTOCOL.SASL`           | SASL                                                                 |
   | `PROTOCOL.SMTP`           | SMTP                                                                 |
   | `PROTOCOL.SSL`            | SSL and TLS                                                          |
   | `SCHEMA`                  | LDAP schema                                                          |
   | `SECURITY`                | Security features                                                    |
   | `SECURITY.AUTHENTICATION` | Authentication                                                       |
   | `SECURITY.AUTHORIZATION`  | Access control and privileges                                        |
   | `SERVICE_DISCOVERY`       | Service discovery                                                    |
   | `SYNC`                    | Replication                                                          |
   | `SYNC.CHANGELOG`          | Replication changelog                                                |
   | `SYNC.CHANGENUMBER`       | Replication change number and change number index                    |
   | `SYNC.CONNECTIONS`        | Replication connections                                              |
   | `SYNC.HEARTBEAT`          | Replication heartbeat checks                                         |
   | `SYNC.LIFECYCLE`          | Replication lifecycle                                                |
   | `SYNC.PROTOCOL_MSGS`      | Replication protocol messages excluding updates and heartbeat checks |
   | `SYNC.PURGE`              | Replication changelog and historical data purge events               |
   | `SYNC.REPLAY`             | Replication replays and conflicts                                    |
   | `SYNC.STATE`              | Replication state changes including generation ID                    |
   | `SYNC.TOPOLOGY`           | Replication topology                                                 |
   | `SYNC.UPDATE_MSGS`        | Replication update messages                                          |
   | `TASK`                    | Server tasks                                                         |
   | `TOOLS`                   | Command-line tools                                                   |

   A monitoring user can [read the list of supported categories over LDAP](../monitoring-guide/ldap-monitoring.html#monitoring-logs).

2. Override the error log level specifically for the category or categories of interest.

   The following example enables debug-level logging for the replication lifecycle. As debug-level logging is of lower severity than the defaults, all the default log levels remain in effect:

   ```console
   $ dsconfig \
    set-log-publisher-prop \
    --add override-severity:SYNC.LIFECYCLE=DEBUG \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --publisher-name "File-Based Error Logger" \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

   The server immediately begins to write additional messages to the error log.

3. Read the messages:

   ```console
   $ tail -f /path/to/opendj/logs/errors
   ```

4. Restore the default settings as soon as debug-level logging is no longer required:

   ```console
   $ dsconfig \
    set-log-publisher-prop \
    --remove override-severity:SYNC.LIFECYCLE=DEBUG \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --publisher-name "File-Based Error Logger" \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

## Lockdown mode

Misconfiguration can put the DS server in a state where you must prevent users and applications from accessing the directory until you have fixed the problem.

DS servers support lockdown mode. Lockdown mode permits connections only on the loopback address, and permits only operations requested by superusers, such as `uid=admin`.

To put the DS server into lockdown mode, the server must be running. You cause the server to enter lockdown mode by starting a task. Notice that the modify operation is performed over the loopback address (accessing the DS server on the local host):

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
dn: ds-task-id=Enter Lockdown Mode,cn=Scheduled Tasks,cn=tasks
objectClass: top
objectClass: ds-task
ds-task-id: Enter Lockdown Mode
ds-task-class-name: org.opends.server.tasks.EnterLockdownModeTask
EOF
```

The DS server logs a notice message in `logs/errors` when lockdown mode takes effect:

```
...msg=Lockdown task Enter Lockdown Mode finished execution in the state Completed successfully
```

Client applications that request operations get a message concerning lockdown mode:

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
 --baseDN "" \
 --searchScope base \
 "(objectclass=*)" \
 +
```

> **Collapse: Show output**
>
> ```
> The LDAP bind request failed: 49 (Invalid Credentials)
> ```

Leave lockdown mode by starting a task:

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
dn: ds-task-id=Leave Lockdown Mode,cn=Scheduled Tasks,cn=tasks
objectClass: top
objectClass: ds-task
ds-task-id: Leave Lockdown Mode
ds-task-class-name: org.opends.server.tasks.LeaveLockdownModeTask
EOF
```

The DS server logs a notice message when leaving lockdown mode:

```
...msg=Leave Lockdown task Leave Lockdown Mode finished execution in the state Completed successfully
```

## LDIF import

* By default, DS directory servers check that entries you import match the LDAP schema.

  You can temporarily bypass this check with the `import-ldif --skipSchemaValidation` option.

* By default, DS servers ensure that entries have only one structural object class.

  You can relax this behavior with the advanced global configuration property, `single-structural-objectclass-behavior`.

  This can be useful when importing data exported from Sun Directory Server.

  For example, warn when entries have more than one structural object class, rather than rejecting them:

  ```console
  $ dsconfig \
   set-global-configuration-prop \
   --hostname localhost \
   --port 4444 \
   --bindDN uid=admin \
   --bindPassword password \
   --set single-structural-objectclass-behavior:warn \
   --trustStorePath /path/to/opendj/config/keystore \
   --trustStoreType PKCS12 \
   --trustStorePassword:file /path/to/opendj/config/keystore.pin \
   --no-prompt
  ```

* By default, DS servers check syntax for several attribute types. Relax this behavior using the advanced global configuration property, `invalid-attribute-syntax-behavior`.

* Use the `import-ldif -R rejectFile --countRejects` options to log rejected entries and to return the number of rejected entries as the command's exit code.

Once you resolve the issues, reinstate the default behavior to avoid importing bad data.

## Security problems

### Incompatible Java versions

Due to a change in Java APIs, the same DS deployment ID generates different CA key pairs with Java 11 compared to Java 17 and later. When running the `dskeymgr` and `setup` commands, use the same Java environment everywhere in the deployment.

|   |                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Running DS servers with incompatible Java versions is a problem when you use deployment ID-based CA certificates.If you [use your own CA](../install-guide/setup-own-keys.html), not one derived from a deployment ID, skip this section. |

When you run the commands with a Java version that doesn't match the deployment ID, DS displays a message such as the following:

```
The specified deployment ID with version '0' will cause interoperability problems with servers
running Java versions less than 17 if the deployment uses deployment ID-based PKI.
Follow the steps in the troubleshooting section of the documentation to resolve compatibility issues
with deployment IDs generated using a Java version prior to 17.
```

#### Overcome incompatible Java versions to generate new keys

When you upgrade servers in place, moving all servers from Java 11 or earlier to Java 17 or later, you first encounter the error message when using the `dskeymgr` command to renew or replace server TLS certificates.

Overcome the problem by [switching to a new deployment ID](../security-guide/key-management.html#replace-deployment-ids). The procedure includes replacement of server certificates.

#### Overcome incompatible Java versions when adding new servers

When you add new servers running on Java 17 or later to a deployment of replicated servers running Java 11 or earlier, the new servers can't replicate with the old servers. Replication breaks as soon as you use the `setup` command for a new server. The error log includes a message such as the following:

```
...category=SYNC severity=ERROR msgID=119 msg=Directory server DS(server_id)
encountered an unexpected error while connecting to replication server host:port for domain "base_dn":
ValidatorException: PKIX path validation failed: java.security.cert.CertPathValidatorException:
signature check failed
```

To work around the issue, follow these steps:

1. Install the most recent [supported Java 17 or later environment](https://docs.pingidentity.com/pingds/release-notes/requirements.html#prerequisites-java) on each DS server system.

2. Update all DS servers to use the most recent supported Java environment.

   If the default Java environment on the system isn't the most recent, use one of the following solutions:

   * Edit the `default.java-home` setting in the `opendj/config/java.properties` file.

   * Set `DS_JAVA_HOME` to the path to the correct Java environment.

   * Set `DS_JAVA_BIN` to the absolute path of the `java` command.

3. Export CA certificates generated with the different Java versions.

   1. Export the CA certificate from an old server:

      ```console
      $ keytool \
       -exportcert \
       -alias ca-cert \
       -keystore /path/to/old-server/config/keystore \
       -storepass:file /path/to/old-server/config/keystore.pin \
       -file java11-ca-cert.pem
      ```

   2. Export the CA certificate from a new server:

      ```console
      $ keytool \
       -exportcert \
       -alias ca-cert \
       -keystore /path/to/new-server/config/keystore \
       -storepass:file /path/to/new-server/config/keystore.pin \
       -file java17-ca-cert.pem
      ```

4. On *all* existing DS servers, import the *new* CA certificate:

   ```console
   $ keytool \
    -importcert \
    -trustcacerts \
    -alias alt-ca-cert \
    -keystore /path/to/old-server/config/keystore \
    -storepass:file /path/to/old-server/config/keystore.pin \
    -file java17-ca-cert.pem \
    -noprompt
   ```

5. On *all* new DS servers, import the *old* CA certificate:

   ```console
   $ keytool \
    -importcert \
    -trustcacerts \
    -alias alt-ca-cert \
    -keystore /path/to/new-server/config/keystore \
    -storepass:file /path/to/new-server/config/keystore.pin \
    -file java11-ca-cert.pem \
    -noprompt
   ```

The servers reload their keystores dynamically and replication works as expected.

Learn more about related key management procedures in these sections:

* [Replace deployment IDs](../security-guide/key-management.html#replace-deployment-ids) and deployment ID-based CAs

* [Replace a TLS key pair](../security-guide/key-management.html#replace-key-pair)

### Certificate-based authentication

Replication uses TLS to protect directory data on the network. Misconfiguration can cause replicas to fail to connect due to handshake errors. This leads to repeated error log messages such as the following:

```
...msg=Replication server accepted a connection from address
 to local address address but the SSL handshake failed.
 This is probably benign, but may indicate a transient network outage
 or a misconfigured client application connecting to this replication server.
 The error was: Received fatal alert: certificate_unknown
```

You can collect debug trace messages to help determine the problem. To display the TLS debug messages, start the server with `javax.net.debug` set:

```console
$ DS_JAVA_ARGS="-Djavax.net.debug=all" start-ds
```

The debug trace settings result in many, many messages. To resolve the problem, review the output of starting the server, looking in particular for handshake errors.

If the chain of trust for your PKI is broken somehow, consider renewing or replacing keys, as described in [Key management](../security-guide/key-management.html). Make sure that trusted CA certificates are configured as expected.

### FIPS and key wrapping

DS servers use [shared asymmetric keys](../security-guide/pki.html#about-deployment-ids) to protect shared symmetric secret keys for data encryption.

By default, DS uses direct encryption to protect the secret keys.

When using a FIPS-compliant security provider that doesn't allow direct encryption, such as Bouncy Castle, change the Crypto Manager configuration to set the advanced property, `key-wrapping-mode: WRAP`. With this setting, DS uses wrap mode to protect the secret keys in a compliant way.

### Compromised keys

How you handle the problem depends on which key was compromised:

* For keys generated by the server, or with a deployment ID and password, refer to [Retire secret keys](../security-guide/key-management.html#retire-secret-keys).

* For a private key whose certificate was signed by a CA, contact the CA for help. The CA might choose to publish a certificate revocation list (CRL) that identifies the certificate of the compromised key.

  Replace the key pair that has the compromised private key.

* For a private key whose certificate was self-signed, replace the key pair that has the compromised private key.

  Make sure the clients remove the compromised certificate from their truststores. They must replace the certificate of the compromised key with the new certificate.

## Client problems

### Use the logs

By default, DS servers record messages for LDAP client operations in the `logs/ldap-access.audit.json` log file.

> **Collapse: Show example log messages**
>
> In the access log, each message is a JSON object. This example formats each message to make it easier to read:
>
> ```none
> {
>   "eventName": "DJ-LDAP",
>   "client": {
>     "ip": "<clientIp>",
>     "port": 12345
>   },
>   "server": {
>     "ip": "<serverIp>",
>     "port": 1636
>   },
>   "request": {
>     "protocol": "LDAPS",
>     "operation": "BIND",
>     "connId": 3,
>     "msgId": 1,
>     "version": "3",
>     "dn": "uid=kvaughan,ou=people,dc=example,dc=com",
>     "authType": "SIMPLE"
>   },
>   "transactionId": "<uuid>",
>   "response": {
>     "status": "SUCCESSFUL",
>     "statusCode": "0",
>     "elapsedTime": 1,
>     "elapsedQueueingTime": 0,
>     "elapsedProcessingTime": 1,
>     "elapsedTimeUnits": "MILLISECONDS",
>     "additionalItems": {
>       "ssf": 128
>     }
>   },
>   "userId": "uid=kvaughan,ou=People,dc=example,dc=com",
>   "timestamp": "<timestamp>",
>   "_id": "<uuid>"
> }
> {
>   "eventName": "DJ-LDAP",
>   "client": {
>     "ip": "<clientIp>",
>     "port": 12345
>   },
>   "server": {
>     "ip": "<serverIp>",
>     "port": 1636
>   },
>   "request": {
>     "protocol": "LDAPS",
>     "operation": "SEARCH",
>     "connId": 3,
>     "msgId": 2,
>     "dn": "dc=example,dc=com",
>     "scope": "sub",
>     "filter": "(uid=bjensen)",
>     "attrs": ["cn"]
>   },
>   "transactionId": "<uuid>",
>   "response": {
>     "status": "SUCCESSFUL",
>     "statusCode": "0",
>     "elapsedTime": 3,
>     "elapsedQueueingTime": 0,
>     "elapsedProcessingTime": 3,
>     "elapsedTimeUnits": "MILLISECONDS",
>     "nentries": 1,
>     "entrySize": 591
>   },
>   "userId": "uid=kvaughan,ou=People,dc=example,dc=com",
>   "timestamp": "<timestamp>",
>   "_id": "<uuid>"
> }
> {
>   "eventName": "DJ-LDAP",
>   "client": {
>     "ip": "<clientIp>",
>     "port": 12345
>   },
>   "server": {
>     "ip": "<serverIp>",
>     "port": 1636
>   },
>   "request": {
>     "protocol": "LDAPS",
>     "operation": "UNBIND",
>     "connId": 3,
>     "msgId": 3
>   },
>   "transactionId": "<uuid>",
>   "timestamp": "<timestamp>",
>   "_id": "<uuid>"
> }
> {
>   "eventName": "DJ-LDAP",
>   "client": {
>     "ip": "<clientIp>",
>     "port": 12345
>   },
>   "server": {
>     "ip": "<serverIp>",
>     "port": 1636
>   },
>   "request": {
>     "protocol": "LDAPS",
>     "operation": "DISCONNECT",
>     "connId": 3
>   },
>   "transactionId": "0",
>   "response": {
>     "status": "SUCCESSFUL",
>     "statusCode": "0",
>     "elapsedTime": 0,
>     "elapsedTimeUnits": "MILLISECONDS",
>     "reason": "Client Unbind"
>   },
>   "timestamp": "<timestamp>",
>   "_id": "<uuid>"
> }
> ```

For details about the messages format, refer to [Access log format](../logging-guide/about-logs.html#log-common-audit).

By default, the server does not log internal LDAP operations corresponding to HTTP requests. To match HTTP client operations to internal LDAP operations:

1. Prevent the server from suppressing log messages for internal operations.

   Set `suppress-internal-operations:false` on the LDAP access log publisher.

2. Match the `request/connId` field in the HTTP access log with the same field in the LDAP access log.

### Client access

To help diagnose client errors due to access permissions, refer to [Effective rights](../security-guide/access.html#get-effective-rights).

### Simple paged results

DS servers support the [simple paged results control](https://www.rfc-editor.org/info/rfc2696) for JE backends. An LDAP search on other backends fails with LDAP result code 12 Unavailable Critical Extension:

```
# The LDAP search request failed: 12 (Unavailable Critical Extension)
# Additional Information:  The search request cannot be processed because it contains a critical control
  with OID 1.2.840.113556.1.4.319 that is not supported by the Directory Server for this type of operation
```

When requesting simple paged results, use a base DN served by a JE backend.

## Replication problems

### Replicas do not connect

If you set up servers with different deployment IDs, they cannot share encrypted data. By default, they also cannot trust each other's secure connections. You may read messages like the following in the `logs/errors` log file:

```
msg=Replication server accepted a connection from /address:port
to local address /address:port but the SSL handshake failed.
```

Unless the servers use your own CA, make sure their keys are generated with the same deployment ID/password. Either set up the servers again with the same deployment ID, or read [Replace deployment IDs](../security-guide/key-management.html#replace-deployment-ids).

### Temporary delays

Replication can generally recover from conflicts and transient issues. Temporary delays are normal and expected while replicas converge, especially when the write load is heavy. This is a feature of eventual convergence, not a bug.

Persistently long replication delays can be a problem for client applications. A client application gets an unexpectedly old view of the data when reading from a very delayed replica. Monitor replication delay and take action when you observe persistently long delays. For example, make sure the network connections between DS servers are functioning normally. Make sure the DS server systems are sized appropriately.

Find detailed suggestions about monitoring replication delays in either of the following sections:

* [Replication delay (LDAP)](../monitoring-guide/ldap-monitoring.html#monitoring-replication-delay-ldap)

* [Replication delay (Prometheus)](../monitoring-guide/http-monitoring.html#monitoring-replication-delay-http)

### Use the logs

By default, replication records messages in the log file, `logs/errors`. Replication messages have `category=SYNC`.

The messages have the following form. The following example message is folded for readability:

```
...msg=Replication server accepted a connection from 10.10.0.10/10.10.0.10:52859
 to local address 0.0.0.0/0.0.0.0:8989 but the SSL handshake failed.
 This is probably benign, but may indicate a transient network outage
 or a misconfigured client application connecting to this replication server.
 The error was: Remote host closed connection during handshake
```

### Stale data

DS replicas maintain historical information to bring replicas up to date and to resolve conflicts. To prevent historical information from growing without limit, DS replicas purge historical information after the [replication-purge-delay](../configref/objects-replication-synchronization-provider.html#replication-purge-delay) (default: 3 days).

A replica becomes irrevocably out of sync when, for example:

* You restore it from backup files older than the purge delay.

* You stop it for longer than the purge delay.

* The replica stays out of contact with other DS servers for longer than the purge delay.

You can monitor replication status to detect stale data [over LDAP](../monitoring-guide/ldap-monitoring.html#monitoring-replication-status-ldap) or [over HTTP with Prometheus](../monitoring-guide/http-monitoring.html#monitoring-replication-status-http).

If the status is not `Normal`, how you react depends on the value of the `ds-mon-status` attribute for LDAP, or `ds_replication_replica_status{status}` for Prometheus.

| Status          | Explanation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Actions to take                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Bad data`      | Replication is broken.Internally, DS replicas store a shorthand form of the initial state called a *generation ID*. The generation ID is a hash of the first 1000 entries in a backend, combined with the total number of entries. When the replicas' generation IDs match, the servers can replicate data without user intervention. When the replicas' generation IDs don't match for a given backend, the servers can't replicate the data.This status arises for one of the following reasons:- The replica and the replication server have different generation IDs for the data because the replica began with different data than its peer replicas.

- The fractional replication configuration for this replica doesn't match the backend data. For example, you reconfigured fractional replication to include or exclude different attributes, or you configured fractional replication incompatibly on different peer replicas.You must intervene to make sure the replicas with bad data start from the same initial state as their peers. Follow the suggested actions to take. Don't replace or reinitialize the backend data alone. DS stores the generation ID in the backend and in the changelog. The generation IDs in the backend and in the changelog must match on all peer replicas.DS 7.3 introduced this status. Earlier releases included this state as part of the `Bad generation id` status. | Whenever this status displays:1) If fractional replication is configured, make sure the configuration is compatible on all peer replicas.

   Learn more in [Fractional replication (advanced)](../config-guide/repl-fractional.html).

2) Initialize the replica with `Bad data` online from a replica with good data.

   Use the `dsrepl initialize` command to initialize the single bad replica. This fixes the bad generation IDs, correcting the problem in the backend and changelog data.

   Find an example in [Initialize over the network](../config-guide/repl-init.html#init-repl-online).

   If you can't initialize the replica with `Bad data` online, [remove it](../install-guide/uninstall.html) and [replace it with a new replica](../config-guide/repl-add-replica.html). |
| `Full update`   | Replication is operating normally.You have chosen to initialize replication over the network.The time to complete the operation depends on the network bandwidth and volume of data to synchronize.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Monitor the server output and wait for initialization to complete.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `Invalid`       | This status arises for one of the following reasons:- The replica has encountered a replication protocol error. This status can arise due to faulty network communication between the replica and the replication server.

- The replica has just started, and is initializing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | If this status happens during normal operation:1) Review the replica and replication server error logs, described in [About logs](../logging-guide/about-logs.html), for network-related replication error messages.

2) Independently verify network communication between the replica and the replication server systems.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `Normal`        | Replication is operating normally.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Nothing to do.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `Not connected` | This status arises for one of the following reasons:- The replica has just started and is not yet connected to the replication server.

- The replica cannot connect to a replication server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | If this status happens during normal operation:1) Review the replica and replication server error logs for network-related replication error messages.

2) Independently verify network communication between the replica and the replication server systems.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `Too late`      | The replica has fallen further behind the replication server than allowed by the [replication-purge-delay](../configref/objects-replication-synchronization-provider.html#replication-purge-delay). In other words, the replica is missing too many changes, and lacks the historical information required to synchronize with peer replicas.The replica no longer receives updates from replication servers. Other replicas that recognize this status stop returning referrals to this replica.DS 7.3 introduced this status. Earlier releases included this state as part of the `Bad generation id` status.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Whenever this status displays:1) Reinitialize replication for the replica that is too late.

   Learn more in [Manual initialization](../config-guide/repl-init.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

### Incorrect configuration

When replication is configured incorrectly, fixing the problem can involve adjustments on multiple servers. For example, adding or removing a bootstrap replication server means updating the `bootstrap-replication-server` settings in the synchronization provider configuration of other servers. (The settings can be hard-coded in the configuration, or read from the environment at startup time, as described in [Property value substitution](../configref/expressions.html). In either case, changing them involves at least restarting the other servers.)

Learn more in [Replication](../config-guide/replication.html) and the related pages.

## Support

Sometimes you can't resolve a problem yourself, and must ask for help or technical support. In such cases, identify the problem and how you reproduce it, and the version where you observe the problem:

```console
$ status --offline --version
```

Output

```
PingDS Server 8.1.1-20260626083155-d61d2a465330810b9f827a8e47416ad66365c629
Build <datestamp>
```

Be prepared to provide the following additional information:

* The Java home set in `config/java.properties`.

* Access and error logs showing what the server was doing when the problem started occurring.

* A copy of the server configuration file, `config/config.ldif`, in use when the problem started occurring.

* Other relevant logs or output, such as those from client applications experiencing the problem.

* A description of the environment where the server is running, including system characteristics, hostnames, IP addresses, Java versions, storage characteristics, and network characteristics. This helps to understand the logs and other information.

* The `.zip` file generated using the `supportextract` command.

  Before generating the `.zip` file, make sure your system has the commands `supportextract` requires:

  | Operating environment | Required commands                                                                                         |
  | --------------------- | --------------------------------------------------------------------------------------------------------- |
  | All systems           | The following commands installed as part of the Java Development Kit (JDK):- `jcmd`

  - `jmap`

  - `jstack` |
  | Linux systems         | * `kill`

  * `top` (if possible, a version that supports the `-H` option)                                  |

  Find an example showing how to use the command in [supportextract](../tools-reference/supportextract.html).

* Any additional [JFR flight recordings](#troubleshoot-use-jfr) captured at the time the problem arose.