---
title: About backing up and restoring data
description: Administrators should make a comprehensive backup strategy and schedule that consist of daily, weekly, and monthly backups. The plan should include:
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_server_administration_guide:pd_ds_about_backup_restore_data
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_server_administration_guide/pd_ds_about_backup_restore_data.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# About backing up and restoring data

Administrators should make a comprehensive backup strategy and schedule that consist of daily, weekly, and monthly backups. The plan should include:

* Full backups of the PingDirectory server data, configuration, and backends

* A backup plan for the underlying file system

This dual purpose approach provides excellent coverage in the event that a server database must be restored for any reason.

|   |                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You can use `dsconfig create-recurring-task` to configure backups as recurring tasks and schedule those tasks as part of a recurring task chain. |

If you back up more than one backend, the `backup` tool creates a subdirectory within a specified backup directory for each backend. If you back up only a single backend, then the backup files are placed in the specified directory. A single directory can only contain files from one backend, so you cannot have backup files from multiple different backends in the same backup directory.

When performing a backup, the server records information about the current state of the server and backend, including:

* The server product name

* The server version

* The backend ID

* The set of base distinguished names (DNs) for the backend

* The Java class used to implement the backend logic

The backup descriptor also includes information about the Berkeley DB Java edition version and information about the attribute and virtual list view (VLV) indexes that have been defined.

When restoring a backup, the server compares the descriptor obtained from the backup with the current state of the server and backend. If any problems are identified, the server generates warnings or errors.

You can choose to ignore warnings using the `ignoreCompatibilityWarnings` option to the `restore` tool. Errors always cause the restore operation to fail.

For example, restoring a newer backup into an older version of the server results in a warning. Restoring an older backup into a new version of the server does not result in a warning, but because the `config` and `schema` backends require special handling, the server generates an error if the server versions do not match exactly the major, minor, point, and patch version numbers.

Both the `backup` and `restore` tools provide encryption options that can be used to specify which key to use for encrypting the backup:

* `--promptForEncryptionPassphrase`

* `--encryptionPassphraseFile`

* `--encryptionSettingsDefinitionID`

For backups encrypted with an encryption settings definition or an internal topology key, the server automatically determines the correct key.

Alternately, you can use the `--doNotEncrypt` argument to force a backup to be unencrypted even if automatic encryption is enabled.

If necessary, you can use the `--maxMegabytesPerSecond` argument to impose a limit on the rate at which the backup can be written to disk.
