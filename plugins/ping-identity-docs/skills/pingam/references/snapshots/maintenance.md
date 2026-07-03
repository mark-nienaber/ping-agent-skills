---
title: Back up configurations
description: Back up PingAM configuration files and directory data to recover from server loss or administrative errors
component: pingam
version: 8.1
page_id: pingam:maintenance:backup-restore
canonical_url: https://docs.pingidentity.com/pingam/8.1/maintenance/backup-restore.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Backup &amp; Restore"]
page_aliases: ["maintenance-guide:backup-restore.adoc"]
section_ids:
  backup-for-disaster: Back up instance configuration data
---

# Back up configurations

During normal production operations, you rely on directory replication to maintain multiple, current copies of AM's configuration. To recover from the loss of a server or from a serious administrative error, back up directory data and configuration files.

Find information on backing up your configuration directory server in [Backup and Restore](https://docs.pingidentity.com/pingds/8.1/maintenance-guide/backup-restore.html) in the DS documentation.

## Back up instance configuration data

This procedure backs up the configuration files stored with the server. You can restore this backup when rebuilding a failed server.

Consider the following when using this procedure:

* Refer to the documentation for your external directory server or work with your directory server administrator to back up and restore configuration data stored in the directory server.

  For PingDS, find information in [Backup and restore](https://docs.pingidentity.com/pingds/8.1/maintenance-guide/backup-restore.html) in the DS documentation.

* Do not restore configuration data from a backup of a different major version of AM. The structure of the configuration data can change from release to release.

Follow these steps for each AM server that you want to back up:

1. Stop AM or the container in which it runs.

2. Back up AM server files.

   This example uses the default configuration location, and excludes logs. `$HOME` is the home directory of the user who runs the web container where AM is deployed. AM is deployed in Apache Tomcat under `am`:

   ```bash
   $ cd $HOME
   $ zip -r AM-config-dir-backup-`date -u +%F-%H-%M`.zip am .openamcfg/* \
     -x am/var/debug/* am/var/audit/* am/var/stats*
   …​
   $ ls AM-config-dir-backup-*.zip
   AM-config-dir-backup-2022-10-01-05-07-50.zip
   ```

3. Start AM or the container in which it runs.
