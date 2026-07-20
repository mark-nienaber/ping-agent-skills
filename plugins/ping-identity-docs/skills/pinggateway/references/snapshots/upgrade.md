---
title: Migrating from web container mode to PingGateway standalone mode
description: Migrate PingGateway from .war web container delivery to standalone .zip mode, covering session replication, TLS, access logs, and configuration changes
component: pinggateway
version: 2026
page_id: pinggateway:upgrade:upgrade-war-to-zip
canonical_url: https://docs.pingidentity.com/pinggateway/2026/upgrade/upgrade-war-to-zip.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-04-01T17:53:34Z
keywords: ["Install", "Configuration", "Migration", "Authentication", "Certificates"]
section_ids:
  session_replication_between_pinggateway_instances: Session replication between PingGateway instances
  streaming_asynchronous_responses_and_events: Streaming asynchronous responses and events
  connection_reuse_when_client_certificates_are_used_for_authentication: Connection reuse when client certificates are used for authentication
  replacement_settings_for_migration_from_web_container_mode_with_tomcat: Replacement settings for migration from web container mode with Tomcat
---

# Migrating from web container mode to PingGateway standalone mode

An PingGateway .war file isn't created or delivered from PingGateway 2024.3. Consider these points when migrating from a .war delivery to a .zip delivery.

## Session replication between PingGateway instances

High-availability of sessions isn't supported by PingGateway in the .zip delivery.

## Streaming asynchronous responses and events

In [ClientHandler](../reference/ClientHandler.html) and [ReverseProxyHandler](../reference/ReverseProxyHandler.html), use only the default mode of `asyncBehavior:non_streaming`; responses are processed when the entity content is entirely available.

If the property is set to `streaming`, the setting is ignored.

## Connection reuse when client certificates are used for authentication

In [ClientHandler](../reference/ClientHandler.html) and [ReverseProxyHandler](../reference/ReverseProxyHandler.html), use only the default mode of `stateTrackingEnabled:true`; when a client certificate is used for authentication, connections can't be reused.

If the property is set to `false`, the setting is ignored.

## Replacement settings for migration from web container mode with Tomcat

| Feature                         | Setting for web container mode with Tomcat                                                                                                                                       | Replacement setting                                                                                                                                                                                                                                                                      |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Port number                     | Configure in the `Connector` element of `/path/to/tomcat/conf/server.xml`:```xml
<Connector port="8080" protocol="HTTP/1.1" connectionTimeout="20000" redirectPort="8443" />
``` | Configure the `connectors` property of [admin.json](../reference/AdminHttpApplication.html).                                                                                                                                                                                             |
| HTTPS server-side configuration | Create a keystore, and set up the SSL port in the `Connector` element of `/path/to/tomcat/conf/server.xml`.                                                                      | Create a keystore, set up secrets, and configure secrets stores, ports, and ServerTlsOptions in [admin.json](../reference/AdminHttpApplication.html).For information, refer to [Configure PingGateway for TLS (server-side)](../installation-guide/envvar-sysprop.html#server-side-tls). |
| Session cookie name             | Configure `WEB-INF/web.xml` when you unpack the PingGateway .war file.                                                                                                           | Configure the `session` property of [admin.json](../reference/AdminHttpApplication.html).                                                                                                                                                                                                |
| Access logs                     | Configure with `AccessLogValve`.                                                                                                                                                 | Configure in the Audit framework.For information, refer to [Auditing the PingGateway deployment](../maintenance-guide/auditing.html) and [PingGateway audit framework](../reference/AuditFramework.html).                                                                                |
| JDBC datasource                 | Configure in the `GlobalNamingResources` element of `/path/to/tomcat/conf/server.xml`.                                                                                           | Configure with the JdbcDataSource object.For information, refer to [JdbcDataSource](../reference/JdbcDataSource.html).For an example, refer to [Password replay from a database](../gateway-guide/credentials-database.html).                                                            |
| Environment variables           | Configure in `/path/to/tomcat/bin/setenv.sh`.                                                                                                                                    | Configure in `$HOME/.openig/bin/env.sh`, where `$HOME/.openig` is the instance directory.                                                                                                                                                                                                |
| Jar files                       | Add to to web container classpath; for example `/path/to/tomcat/webapps/ROOT/WEB-INF/lib`.                                                                                       | Add to `$HOME/.openig/extra`, where `$HOME/.openig` is the instance directory.                                                                                                                                                                                                           |

---

---
title: PingGateway upgrades
description: "Upgrade guide preface for PingGateway: overview of the upgrade process and links to release notes to read before upgrading"
component: pinggateway
version: 2026
page_id: pinggateway:upgrade:preface
canonical_url: https://docs.pingidentity.com/pinggateway/2026/upgrade/preface.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-04-01T17:53:34Z
keywords: ["Upgrade", "Configuration"]
page_aliases: ["index.adoc"]
---

# PingGateway upgrades

This guide shows you how to upgrade PingGateway software.

Read the [Release notes](https://docs.pingidentity.com/pinggateway/release-notes/preface.html) before you upgrade.

Product names changed when ForgeRock became part of Ping Identity. PingGateway was formerly known as ForgeRock Identity Gateway, for example. Learn more about the name changes from [New names for ForgeRock products](https://support.pingidentity.com/s/article/new-names-for-forgerock-products).

---

---
title: Planning the PingGateway upgrade
description: Complete key planning tasks before upgrading PingGateway, including reviewing release notes, checking requirements, planning downtime, backing up, and preparing a rollback strategy
component: pinggateway
version: 2026
page_id: pinggateway:upgrade:upgrade-planning
canonical_url: https://docs.pingidentity.com/pinggateway/2026/upgrade/upgrade-planning.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-04-01T17:53:34Z
---

# Planning the PingGateway upgrade

Do these planning tasks **before** you start an upgrade:

| Planning task                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Find the upgrade path                      | Refer to [Upgrading PingGateway](migrate.html) to see if you need a drop-in upgrade or a major upgrade.                                                                                                                                                                                                                                                                                                                                                                  |
| Find out what changed                      | Read the [release notes](https://docs.pingidentity.com/pinggateway/release-notes) for all releases between the current version and the new version. Understand the new features and changes in the new version compared to the current version.                                                                                                                                                                                                                          |
| Check the requirements                     | Make sure you meet all the requirements in the release notes for the new version. In particular, make sure you have a recent, supported [Java version](https://docs.pingidentity.com/pinggateway/release-notes/before-you-install.html#prerequisites-java).                                                                                                                                                                                                              |
| Plan for server downtime                   | At least one of your PingGateway servers will be down during upgrade. Plan to route client applications to another server until the upgrade process is complete and you have validated the result. Make sure the owners of client application are aware of the change, and let them know what to expect.If you have a single PingGateway server, make sure the downtime happens in a low-usage window, and make sure you let client application owners plan accordingly. |
| Back up                                    | The PingGateway configuration is a set of files, including `admin.json`, `config.json`, `logback.xml`, routes, and scripts. Back up the PingGateway configuration and store it in version control, so that you can roll back if something goes wrong.Back up any tools scripts you have edited for your deployment and any trust stores used to connect securely.                                                                                                        |
| Plan for [rollback](migrate.html#rollback) | Sometimes even a well-planned upgrade fails to go smoothly. In such cases, you need a plan to roll back smoothly to the pre-upgrade version.For PingGateway servers, roll back by restoring a backed-up configuration.                                                                                                                                                                                                                                                   |
| Prepare a test environment                 | Before applying the upgrade in your production environment, always try to upgrade PingGateway in a test environment. This will help you gauge the amount of work required, without affecting your production environment, and will help smooth out unforeseen problems.The test environment should resemble your production environment as closely as possible.                                                                                                          |

---

---
title: Upgrading PingGateway
description: Upgrade a single PingGateway instance using drop-in software updates or major upgrades, with binaries or Docker, including rollback steps
component: pinggateway
version: 2026
page_id: pinggateway:upgrade:migrate
canonical_url: https://docs.pingidentity.com/pinggateway/2026/upgrade/migrate.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-04-01T17:53:34Z
keywords: ["Configuration", "Upgrade", "Docker"]
section_ids:
  drop_in_software_update_with_binaries: Drop-in software update with binaries
  drop_in_software_update_with_docker_files: Drop-in software update with Docker files
  major_upgrade_with_binaries: Major upgrade with binaries
  major_upgrade_with_docker_files: Major upgrade with Docker files
  post_upgrade_tasks: Post upgrade tasks
  rollback: Rollback
---

# Upgrading PingGateway

Learn about upgrade between supported versions of PingGateway in the [Ping Identity End of Life (EOL) Software Tracker](https://support.pingidentity.com/s/article/Ping-Identity-EOL-Tracker#pgateway).

Learn about upgrade of routes in Studio in [Upgrade from an earlier version of Studio](../studio-guide/upgrade.html).

This section describes how to upgrade a single PingGateway instance. The most straightforward option when upgrading sites with multiple PingGateway instances is to upgrade in place. One by one, stop, upgrade, and then restart each server individually, leaving the service running during the upgrade.

PingGateway supports the following types of upgrade:

* Drop-in software update

  Usually, an update from a version of PingGateway to a newer minor version, as defined in the [Ping Identity End of Life (EOL) Software Tracker](https://support.pingidentity.com/s/article/Ping-Identity-EOL-Tracker#pgateway). For example, the update from 2023.2 to 2023.4.

  Drop-in software updates can introduce additional functionality and fix bugs or security issues. Consider the following restrictions for drop-in software updates:

  * Don't require any update to the configuration

  * Cannot cause feature regression

  * Can change default or previously configured behavior **only** for bug fixes and security issues

  * Can deprecate **but not remove** existing functionality

- Major upgrade

  Usually, an upgrade from a version of PingGateway to a newer major version, as defined in the [Ping Identity End of Life (EOL) Software Tracker](https://support.pingidentity.com/s/article/Ping-Identity-EOL-Tracker#pgateway). For example, the upgrade from 7.2 to 2023.2.

  Major upgrades can introduce additional functionality and fix bugs or security issues. Major upgrades don't have the restrictions of drop-in software update. Consider the following features of major upgrades:

  * Can require code or configuration changes

  * Can cause feature regression

  * Can change default or previously configured behavior

  * Can deprecate **and** remove existing functionality

## Drop-in software update with binaries

1. Read and act on [Planning the PingGateway upgrade](upgrade-planning.html).

2. Back up the PingGateway configuration and store it in version control so that you can roll back if something goes wrong.

3. [Downloading PingGateway](../installation-guide/download.html)

4. [Stop PingGateway](../installation-guide/start-stop.html#stopping).

5. Make the new configuration available on the file system.

   By default, PingGateway configuration files are located under `$HOME/.openig` (on Windows `%appdata%\OpenIG`). For information about how to use a different location, refer to [Configuration location](../configure/configure.html#configuration-location).

6. [Restart PingGateway](../installation-guide/start-stop.html) from the new installation directory.

7. In a test environment that simulates your production environment, validate that the upgraded service performs as expected with the new configuration. Check the logs for new or unexpected notifications or errors.

8. Allow client application traffic to flow to the upgraded site.

## Drop-in software update with Docker files

1. Read and act on [Planning the PingGateway upgrade](upgrade-planning.html).

2. Back up the PingGateway configuration and store it in version control so that you can roll back if something goes wrong.

3. [Stop the Docker image](../devops-guide/docker-basic.html#docker-stop-image).

4. [Build the new base image for PingGateway](../devops-guide/docker-basic.html#docker-build-image).

5. [Run the Docker image](../devops-guide/docker-basic.html#docker-run-image).

6. In a test environment that simulates your production environment, validate that the upgraded service performs as expected with the new configuration. Check the logs for new or unexpected notifications or errors.

7. Allow client application traffic to flow to the upgraded site.

## Major upgrade with binaries

1. Read and act on [Planning the PingGateway upgrade](upgrade-planning.html).

2. Use the [release notes](https://docs.pingidentity.com/pinggateway/release-notes) for **all** releases between the version you currently use and the new version, and create a new configuration as follows:

   * Review all incompatible changes and removed functionality, and adjust your configuration as necessary.

   * Switch to the replacement settings for deprecated functionality. Although [deprecated](https://docs.pingidentity.com/pinggateway/release-notes/stability.html#interface-stability) objects continue to work, they add to the notifications in the logs and are eventually removed.

   * Check the lists of fixes, limitations, and known issues to find out if they impact your deployment.

   * Recompile your Java extensions. The method signature or imports for supported and evolving APIs can change in each version.

   * Read the documentation updates for new examples and information that can help with your configuration.

3. Back up the PingGateway configuration and store it in version control so that you can roll back if something goes wrong.

4. [Downloading PingGateway](../installation-guide/download.html)

5. [Stop PingGateway](../installation-guide/start-stop.html#stopping).

6. Make the new configuration available on the file system.

   By default, PingGateway configuration files are located under `$HOME/.openig` (on Windows `%appdata%\OpenIG`). For information about how to use a different location, refer to [Configuration location](../configure/configure.html#configuration-location).

7. [Restart PingGateway](../installation-guide/start-stop.html) from the new installation directory.

8. In a test environment that simulates your production environment, validate that the upgraded service performs as expected with the new configuration. Check the logs for new or unexpected notifications or errors.

9. Allow client application traffic to flow to the upgraded site.

## Major upgrade with Docker files

1. Read and act on [Planning the PingGateway upgrade](upgrade-planning.html).

2. Use the [release notes](https://docs.pingidentity.com/pinggateway/release-notes) for **all** releases between the version you currently use and the new version, and create a new configuration as follows:

   * Review all incompatible changes and removed functionality, and adjust your configuration as necessary.

   * Switch to the replacement settings for deprecated functionality. Although [deprecated](https://docs.pingidentity.com/pinggateway/release-notes/stability.html#interface-stability) objects continue to work, they add to the notifications in the logs and are eventually removed.

   * Check the lists of fixes, limitations, and known issues to find out if they impact your deployment.

   * Recompile your Java extensions. The method signature or imports for supported and evolving APIs can change in each version.

   * Read the documentation updates for new examples and information that can help with your configuration.

3. Back up the PingGateway configuration and store it in version control so that you can roll back if something goes wrong.

4. [Stop the Docker image](../devops-guide/docker-basic.html#docker-stop-image).

5. [Build the new base image for PingGateway](../devops-guide/docker-basic.html#docker-build-image).

6. [Run the Docker image](../devops-guide/docker-basic.html#docker-run-image).

7. In a test environment that simulates your production environment, validate that the upgraded service performs as expected with the new configuration. Check the logs for new or unexpected notifications or errors.

8. Allow client application traffic to flow to the upgraded site.

## Post upgrade tasks

After upgrade, review the [what's new](https://docs.pingidentity.com/pinggateway/release-notes/whats-new.html) section in the release notes and consider activating new features and functionality.

## Rollback

|   |                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Before you roll back to a previous version of PingGateway, consider whether any change to the configuration during or since upgrade could be incompatible with the previous version. |

Roll back with binaries

1. Plan for server downtime

   Plan to route client applications to another server until the rollback process is complete and you have validated the result. Make sure the owners of client application are aware of the change, and let them know what to expect.

2. [Stop PingGateway](../installation-guide/start-stop.html)

3. [Download the replacement PingGateway .zip file](../installation-guide/download.html)

4. Make the new configuration available on the file system.

   By default, PingGateway configuration files are located under `$HOME/.openig` (on Windows `%appdata%\OpenIG`). For information about how to use a different location, refer to [Configuration location](../configure/configure.html#configuration-location).

5. [Restart PingGateway](../installation-guide/start-stop.html).

Roll back with Dockerfiles

1. Plan for server downtime

   Plan to route client applications to another server until the rollback process is complete and you have validated the result. Make sure the owners of client application are aware of the change, and let them know what to expect.

2. [Stop the Docker image](../devops-guide/docker-basic.html#docker-stop-image).

3. [Build the new base image for PingGateway](../devops-guide/docker-basic.html#docker-build-image).

4. [Run the Docker image](../devops-guide/docker-basic.html#docker-run-image).