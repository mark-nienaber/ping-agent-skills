---
title: Backup and restore
description: "Step through a PingDS backup and restore use case: schedule backups, simulate a server loss, and validate recovery."
component: pingds
version: 8.1
page_id: pingds:use-cases:backup-restore
canonical_url: https://docs.pingidentity.com/pingds/8.1/use-cases/backup-restore.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-12T12:15:36Z
keywords: ["Backup &amp; Restore", "LDAP", "Use Case", "Storage"]
section_ids:
  description: Description
  goals: Goals
  example_scenario: Example scenario
  prerequisites: Prerequisites
  knowledge: Knowledge
  actions: Actions
  tasks: Tasks
  task_1_schedule_a_recurring_backup_operation: "Task 1: Schedule a recurring backup operation"
  configure_backup_tasks: Configure backup tasks
  optional_back_up_data_now: (Optional) Back up data now
  task_2_simulate_the_loss_of_a_server: "Task 2: Simulate the loss of a server"
  task_3_recover_and_restore_the_lost_server: "Task 3: Recover and restore the lost server"
  validation: Validation
  whats_next: What's next
  explore_further: Explore further
  related_use_cases: Related use cases
  reference_material: Reference material
---

# Backup and restore

Plan DS backup and restore procedures for your deployment.

## Description

Estimated time to complete: 20 minutes *(tooltip: This assumes you complete the prerequisites beforehand.)*

Safely and regularly back up your directory data to recover quickly when accidents happen.

In this use case, you:

* Back up directory data using DS tools.

* Cause an incident requiring recovery.

* Restore directory data after an incident.

* Validate the data restore procedure.

## Goals

In completing this use case, you learn to:

* Use DS backup and restore tools.

* Schedule a recurring backup task.

* Restore directory data from backup files.

* Purge outdated backup files.

## Example scenario

As a directory service administrator, Pat plans to deploy directory services for critical identity data such as login credentials.

Pat knows good backup and restore plans are a must for identity and access services. If the data is lost, end users cannot authenticate, and account profiles are lost.

Pat plans to show other identity administrators how the backup and restore procedures work and get them to review the process before deployment.

## Prerequisites

### Knowledge

Before you start, bring yourself up to speed with Pat:

* Pat is familiar with the command line on the target operating system, a Linux distribution in this example.

* Pat knows how to use basic LDAP commands, having worked [examples to learn LDAP](../getting-started/ldap.html).

* Pat has already successfully completed [directory service installation and setup procedures](../install-guide/preface.html).

### Actions

Before you try this example, set up two replicated DS directory servers on your computer as described in [Install DS](../getting-started/install.html) and [Learn replication](../getting-started/replication.html).

## Tasks

Pat demonstrates how to back up and restore DS directory data from the evaluation profile. The order of the tasks is the same in deployment, but the directory data is different.

### Task 1: Schedule a recurring backup operation

When you use the DS tools, backup operations are incremental. You can take regular backups with a reasonable amount of disk space relative to your data.

#### Configure backup tasks

1. Schedule a regular backup task.

   The following example schedules an hourly backup task:

   ```console
   $ /path/to/opendj/bin/dsbackup \
    create \
    --backupLocation bak \
    --recurringTask "00 * * * *" \
    --description "Back up every hour" \
    --taskId HourlyBackup \
    --completionNotify diradmin@example.com \
    --errorNotify diradmin@example.com \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin
   ```

2. Schedule a task to remove backup data older than the replication purge delay.

   When you restore data from backup, the backup you restore must be more recent than the replication purge delay. If you restore from older data, the replica you restore can't replicate with other servers. The default replication purge delay is three days.

   The following example schedules an hourly task to remove outdated backup data:

   ```console
   $ /path/to/opendj/bin/dsbackup \
    purge \
    --backupLocation bak \
    --recurringTask "00 * * * *" \
    --description "Purge old backups every hour" \
    --olderThan "3 days" \
    --taskId HourlyPurge \
    --completionNotify diradmin@example.com \
    --errorNotify diradmin@example.com \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin
   ```

   This task ensures you won't fill up the disk with old backup data.

#### (Optional) Back up data now

At this point, the recurring backup task is scheduled; however, the next backup operation won't start until the top of the hour. If you want to continue this example without waiting for the task to run, you can back up the data now.

These steps demonstrate offline backup:

1. Stop the server:

   ```console
   $ /path/to/opendj/bin/stop-ds
   ```

2. Back up the data with the server offline:

   ```console
   $ /path/to/opendj/bin/dsbackup \
    create \
    --backupLocation bak \
    --offline
   ```

   The command writes the backup data to the `bak/` directory under the server installation directory.

3. Start the server:

   ```console
   $ /path/to/opendj/bin/start-ds
   ```

### Task 2: Simulate the loss of a server

1. Make sure you have at least one set of backup files:

   ```console
   $ /path/to/opendj/bin/dsbackup \
    list \
    --backupLocation bak \
    --offline
   ```

   This command runs on the files and can run in offline mode even if the server is up.

   If you are waiting for the hourly backup task to run, there may not be any backup files yet.

2. Simulate the loss of a server by stopping it abruptly and deleting the files.

   This example removes the `second-ds` server:

   ```console
   $ kill -9 <second-ds-pid>
   $ rm -rf /path/to/replica
   ```

3. Change an entry.

   You use this change later to validate the restore procedure and show replication replays changes occurring after the last backup operation:

   ```console
   $ /path/to/opendj/bin/ldapmodify \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDn uid=bjensen,ou=People,dc=example,dc=com \
    --bindPassword hifalutin << EOF
   dn: uid=bjensen,ou=People,dc=example,dc=com
   changetype: modify
   replace: description
   description: Updated after the replica crashed
   EOF
   ```

### Task 3: Recover and restore the lost server

1. Replace the lost server with the same configuration but don't start it.

   This example uses the evaluation profile:

   ```console
   $ cd ~/Downloads && unzip ~/Downloads/{ds_zip} && mv opendj /path/to/replica
   $ export DEPLOYMENT_ID=<deployment-id>
   $ /path/to/replica/setup \
    --serverId second-ds \
    --deploymentId $DEPLOYMENT_ID \
    --deploymentIdPassword password \
    --rootUserDn uid=admin \
    --rootUserPassword password \
    --hostname localhost \
    --ldapPort 11389 \
    --ldapsPort 11636 \
    --adminConnectorPort 14444 \
    --replicationPort 18989 \
    --bootstrapReplicationServer localhost:8989 \
    --profile ds-evaluation \
    --set ds-evaluation/generatedUsers:0 \
    --acceptLicense
   ```

   Rebuilding the basic server configuration depends on your deployment. For testing and deployment, adapt the commands to fit your process.

2. Restore the server data from backup:

   ```console
   $ /path/to/replica/bin/dsbackup \
    restore \
    --offline \
    --backendName dsEvaluation \
    --backupLocation /path/to/opendj/bak
   ```

3. Start the server:

   ```console
   $ /path/to/replica/bin/start-ds
   ```

   After the server starts and connects to other servers, replication replays changes from after the backup operation.

## Validation

Demonstrate the server you restored has the same data as the other replica.

1. Read the description you changed after the backup operation and server crash on `first-ds`:

   ```console
   $ /path/to/opendj/bin/ldapsearch \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDn uid=bjensen,ou=People,dc=example,dc=com \
    --bindPassword hifalutin \
    --baseDn dc=example,dc=com \
    "(cn=Babs Jensen)" \
    description
   ```

   > **Collapse: Show output**
   >
   > ```
   > dn: uid=bjensen,ou=People,dc=example,dc=com
   > description: Updated after the replica crashed
   > ```

2. Read the same data on the `second-ds` server you restored from backup:

   ```console
   $ /path/to/replica/bin/ldapsearch \
    --hostname localhost \
    --port 11636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDn uid=bjensen,ou=People,dc=example,dc=com \
    --bindPassword hifalutin \
    --baseDn dc=example,dc=com \
    "(cn=Babs Jensen)" \
    description
   ```

   > **Collapse: Show output**
   >
   > ```
   > dn: uid=bjensen,ou=People,dc=example,dc=com
   > description: Updated after the replica crashed
   > ```

   The data is the same on both servers. You have shown your backup and restore procedure is sound.

## What's next

After demonstrating the process, Pat implements backup and restore procedures for testing and deployment. These procedures become part of the organization's runbook, so operators can implement them quickly and easily.

Pat realizes disaster recovery is more than restoring backup files. Pat also implements [disaster recovery](disaster-recovery.html) procedures for testing and deployment as part of the organization's runbook.

## Explore further

This use case can serve as a template for DS test and production deployments. Adapt this example for deployment:

* Make sure the backup tasks run on more than one DS replica to avoid a single point of backup failure.

* To keep things simple, this example shows a backup on the local filesystem.

  In testing and deployment, make sure you store backup files remotely in a shared location. For example, consider mounting a remote filesystem and using it to store backup files.

  A shared remote location for backup files makes it easier to restore from the same backup on multiple replicas.

* If the filesystem on your servers supports atomic snapshots, consider [backing up DS with filesystem snapshots](../maintenance-guide/backup-restore.html#backup-snapshot).

### Related use cases

* [Disaster recovery](disaster-recovery.html)

### Reference material

| Reference                                                             | Description                                                                             |
| --------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| [Backup and restore](../maintenance-guide/backup-restore.html)        | Includes detailed examples and alternatives for backing up and restoring directory data |
| [Cryptographic keys](../security-guide/pki.html)                      | About keys, including those for encrypting and decrypting backup files                  |
| [dsbackup](../tools-reference/dsbackup.html)                          | Reference for the command-line tool                                                     |
| [Server tasks](../maintenance-guide/server-process.html#server-tasks) | On server tasks, like recurring backup operations                                       |
