---
title: About upgrades
description: Overview of PingDS upgrade scope, supported upgrade paths from DS 6 and later, and steps to activate new features after upgrading.
component: pingds
version: 8.1
page_id: pingds:upgrade-guide:about-upgrades
canonical_url: https://docs.pingidentity.com/pingds/8.1/upgrade-guide/about-upgrades.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Compatibility", "LDAP", "Replication", "Upgrade"]
section_ids:
  upgrade-features: Activate new features after upgrade
  upgrade-paths: Supported upgrades
---

# About upgrades

This documentation explains how to upgrade PingDS software. It doesn't cover upgrading DS client applications or changing the directory service schema or configuration. Keep those operations separate from the DS software upgrade.

|   |                                                                                                                                                                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This documentation assumes you:- Are upgrading from DS 7 or later.

- Performed all the recommended upgrade procedures when moving to the currently deployed version, including the "After you upgrade" procedures.If not, begin with the [upgrade documentation for DS 7.5](https://docs.pingidentity.com/pingds/7.5/upgrade-guide/preface.html). |

## Activate new features after upgrade

When you upgrade DS in place, the upgrade process preserves the existing configuration as much as possible. This maintains compatibility, but you do not have access to all new features immediately after upgrade.

You must take additional steps to complete the process, including activating new features.

## Supported upgrades

| From…​                                         | To…​                                                                        | Important Notes                                                                                                                                                                        |
| ---------------------------------------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Official DS release, version 6.0 or later      | Official DS release, same edition of directory server or replication server | Supported.                                                                                                                                                                             |
| Official ForgeRock release, 2.6.x to 5.5.x     | Official DS release, directory server or replication server                 | Not supported.1                                                                                                                                                                        |
| Official ForgeRock release, version 2.4 or 2.5 | Official DS release, directory server or replication server                 | Not supported.2                                                                                                                                                                        |
| Evaluation release                             | Official DS release                                                         | Not supported.The evaluation version includes an additional server plugin and configuration. Official releases do not have an upgrade task to remove the plugin and its configuration. |
| Unofficial build                               | Official DS release                                                         | Not supported.                                                                                                                                                                         |

1 Workaround: First upgrade to DS 6.5, then to DS 7.5.

2 Workaround: First upgrade to OpenDJ 2.6, then to DS 6.5, then to DS 7.5.

---

---
title: Add new servers
description: Steps to add new PingDS servers when upgrading by adding new servers, including index rebuilds and post-upgrade configuration.
component: pingds
version: 8.1
page_id: pingds:upgrade-guide:add-new-servers
canonical_url: https://docs.pingidentity.com/pingds/8.1/upgrade-guide/add-new-servers.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Compatibility", "LDAP", "Migration", "Replication", "Upgrade"]
section_ids:
  next_steps: Next steps
---

# Add new servers

|   |                                                                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If either of the following are true, begin with the [upgrade documentation for DS 7.5](https://docs.pingidentity.com/pingds/7.5/upgrade-guide/preface.html) instead:- The deployment includes DS 6.5 or earlier servers.

- The deployment hasn't yet moved to the DS 7 security model based on deployment IDs. |

Otherwise, [Install the new servers](../install-guide/preface.html) and rebuild indexes as necessary:

1. [Install the new server](../install-guide/preface.html) with settings compatible with those of the existing servers.

   Learn about changes since the deployed release in [Incompatible changes](https://docs.pingidentity.com/pingds/release-notes/changes.html).

2. If existing servers use [change number indexing](../config-guide/changelog.html#ecl-configure-changenumber-indexer), configure the settings on the new servers to match the same settings on the existing servers.

3. Rebuild untrusted `mail` indexes for the change to the `mail` attribute schema definition to allow UTF-8 characters.

   The definitions for DS 7.3 and later allow UTF-8, whereas earlier versions allow only ASCII. The change does not affect the data, but does affect `mail` indexes.

   For details, refer to [Automate index rebuilds](../config-guide/idx-config.html#automate-index-rebuilds).

## Next steps

* [icon: check-square-o, set=fa]Perform [these steps](before-you-upgrade.html) before you add servers

* [icon: check-square-o, set=fa]Add new servers:

  * [icon: check-square-o, set=fa]Follow [these instructions](add-new-servers.html) unless upgrading from DS 7.4.0

  * [icon: square-o, set=fa]*Follow [these instructions](from-740.html) when upgrading from DS 7.4.0*

* [icon: square-o, set=fa]Perform [these steps](after-you-upgrade.html) after you finish adding servers

---

---
title: After you add new servers
description: Post-upgrade checklist for PingDS deployments upgraded by adding new servers, covering backups, stale configs, and bootstrap updates.
component: pingds
version: 8.1
page_id: pingds:upgrade-guide:after-you-upgrade
canonical_url: https://docs.pingidentity.com/pingds/8.1/upgrade-guide/after-you-upgrade.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Compatibility", "LDAP", "Migration", "Replication", "Setup &amp; Configuration", "Troubleshooting", "Upgrade"]
section_ids:
  overview: Checklist
  upgrade-tuning: Tune settings
  upgrade_complete: Upgrade complete
---

# After you add new servers

The DS server upgrade process preserves the existing configuration as much as possible. This maintains compatibility, but there are more steps you must take.

## Checklist

Use this checklist to make sure you don't miss these important post-upgrade tasks:

* [icon: square-o, set=fa]Back up your directory data.1

* [icon: square-o, set=fa]Update your scripts to account for [Incompatible changes](https://docs.pingidentity.com/pingds/release-notes/changes.html).

* [icon: square-o, set=fa]Plan your move away from [deprecated](https://docs.pingidentity.com/pingds/release-notes/deprecation.html) features.

* [icon: square-o, set=fa]Move to dedicated service accounts for your directory applications.2

* [icon: square-o, set=fa]Manually review and purge the DS server configurations for stale references to old servers.3

* [icon: square-o, set=fa]Update bootstrap replication servers.4

* [icon: square-o, set=fa]Review [what's new and changed](https://docs.pingidentity.com/pingds/release-notes/index.html) and adopt useful improvements.

* [icon: square-o, set=fa][Tune settings](#upgrade-tuning).

1 Backup files are *not* compatible between versions.

2 You would not run all your applications as the Linux root user or the Windows Administrator. Stop using superuser accounts like `cn=Directory Manager` or `uid=admin` as service accounts. Many DS setup profiles create service accounts for applications to use when authenticating to DS. For examples of AM service accounts, refer to the `base-entries.ldif` files in setup profiles under the `opendj/template/setup-profiles/AM` directory.

3 You can read the `opendj/config/config.ldif` file to find stale references, but always use the [dsconfig](../tools-reference/dsconfig.html) command to make changes to the configuration.

4 After you upgrade by adding new servers, but before you retire old servers, update bootstrap replication server settings to [remove the old servers](../config-guide/repl-bootstrap.html#remove-bootstrap-replication-server), and [add the new DS servers](../config-guide/repl-bootstrap.html#add-bootstrap-replication-server).

## Tune settings

Major software releases include significant changes that can render existing tuning settings obsolete. When upgrading to a new major release of DS or Java software, revisit the system configuration, server configuration, and Java settings. As part of the upgrade process, adjust the settings appropriately to align your deployment with the new software version.

Learn more in the [release notes](https://docs.pingidentity.com/pingds/release-notes/requirements.html) and [Performance tuning](../config-guide/tuning.html).

## Upgrade complete

* [icon: check-square-o, set=fa]Perform [these steps](before-you-upgrade.html) before you add servers

* [icon: check-square-o, set=fa]Add new servers:

  * [icon: check-square-o, set=fa]Follow [these instructions](add-new-servers.html) unless upgrading from DS 7.4.0

  * [icon: check-square-o, set=fa]Follow [these instructions](from-740.html) when upgrading from DS 7.4.0

* [icon: check-square-o, set=fa]Perform [these steps](after-you-upgrade.html) after you finish adding servers

---

---
title: After you upgrade in place
description: Post-upgrade checklist for PingDS in-place upgrades, covering backups, service accounts, tuning, and optional new-feature activation.
component: pingds
version: 8.1
page_id: pingds:upgrade-guide:after-you-upgrade-in-place
canonical_url: https://docs.pingidentity.com/pingds/8.1/upgrade-guide/after-you-upgrade-in-place.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Compatibility", "LDAP", "Migration", "Replication", "Setup &amp; Configuration", "Troubleshooting", "Upgrade"]
section_ids:
  checklist: Checklist
  upgrade-tuning-in-place: Tune settings
  upgrade-in-place-new-features: Activate new features
  upgrade_complete: Upgrade complete
---

# After you upgrade in place

The DS server upgrade process preserves the existing configuration as much as possible. This maintains compatibility, but there are more steps you must take.

## Checklist

Use this checklist to make sure you don't miss these important post-upgrade tasks:

* [icon: square-o, set=fa]Back up your directory data.1

* [icon: square-o, set=fa]Update your scripts to account for [Incompatible changes](https://docs.pingidentity.com/pingds/release-notes/changes.html).

* [icon: square-o, set=fa]Plan your move away from [deprecated](https://docs.pingidentity.com/pingds/release-notes/deprecation.html) features.

* [icon: square-o, set=fa]Move to dedicated service accounts for your directory applications.2

* [icon: square-o, set=fa]Manually review and purge the DS server configurations for stale references to old servers.3

* [icon: square-o, set=fa]Review [what's new and changed](https://docs.pingidentity.com/pingds/release-notes/index.html) and adopt useful improvements.

* [icon: square-o, set=fa][Tune settings](#upgrade-tuning-in-place).

* [icon: square-o, set=fa]Optionally [activate new features](#upgrade-in-place-new-features).

1 Backup files are *not* compatible between versions.

2 You would not run all your applications as the Linux root user or the Windows Administrator. Stop using superuser accounts like `cn=Directory Manager` or `uid=admin` as service accounts. Many DS setup profiles create service accounts for applications to use when authenticating to DS. For examples of AM service accounts, refer to the `base-entries.ldif` files in setup profiles under the `opendj/template/setup-profiles/AM` directory.

3 You can read the `opendj/config/config.ldif` file to find stale references, but always use the [dsconfig](../tools-reference/dsconfig.html) command to make changes to the configuration.

## Tune settings

Major software releases include significant changes that can render existing tuning settings obsolete. When upgrading to a new major release of DS or Java software, revisit the system configuration, server configuration, and Java settings. As part of the upgrade process, adjust the settings appropriately to align your deployment with the new software version.

Learn more in the [release notes](https://docs.pingidentity.com/pingds/release-notes/requirements.html) and [Performance tuning](../config-guide/tuning.html).

## Activate new features

The DS `upgrade` command configures the following new features but doesn't enable them. Optionally enable the new features for use in your deployment:

* Enable the [HDAP](../rest-guide/preface.html) endpoint:

  ```console
  $ /path/to/opendj/bin/dsconfig \
   set-http-endpoint-prop \
   --endpoint-name "/hdap" \
   --set enabled:true \
   --hostname localhost \
   --port 4444 \
   --bindDN uid=admin \
   --bindPassword password \
   --no-prompt \
   --trustStorePath /path/to/opendj/config/keystore \
   --trustStoreType PKCS12 \
   --trustStorePassword:file /path/to/opendj/config/keystore.pin
  ```

* Enable the [`ds-pwp-state-json` virtual attribute](../ldap-guide/passwords-and-accounts.html#ldap-read-pwp-state):

  ```console
  $ /path/to/opendj/bin/dsconfig \
   set-virtual-attribute-prop \
   --name "Password Policy State" \
   --set enabled:true \
   --hostname localhost \
   --port 4444 \
   --bindDN uid=admin \
   --bindPassword password \
   --no-prompt \
   --trustStorePath /path/to/opendj/config/keystore \
   --trustStoreType PKCS12 \
   --trustStorePassword:file /path/to/opendj/config/keystore.pin
  ```

* Enable the `PBKDF2-HMAC-SHA512T256` password storage scheme if needed for interoperability with Microsoft Entra ID:

  ```console
  $ /path/to/opendj/bin/dsconfig \
   set-password-storage-scheme-prop \
   --scheme-name "PBKDF2-HMAC-SHA512T256" \
   --set enabled:true \
   --hostname localhost \
   --port 4444 \
   --bindDN uid=admin \
   --bindPassword password \
   --no-prompt \
   --trustStorePath /path/to/opendj/config/keystore \
   --trustStoreType PKCS12 \
   --trustStorePassword:file /path/to/opendj/config/keystore.pin
  ```

## Upgrade complete

* [icon: check-square-o, set=fa]Perform [these steps](before-you-upgrade-in-place.html) before you upgrade

* [icon: check-square-o, set=fa]Upgrade each:

  * [icon: check-square-o, set=fa][Directory server](upgrade-ds.html)

  * [icon: check-square-o, set=fa][Directory proxy](upgrade-proxy.html)

  * [icon: check-square-o, set=fa][Replication server](upgrade-rs.html)

  * [icon: check-square-o, set=fa][HDAP gateway](upgrade-rest.html)

* [icon: check-square-o, set=fa]Perform [these steps](after-you-upgrade-in-place.html) after you upgrade

---

---
title: Before you add new servers
description: Prerequisites before upgrading PingDS by adding new servers, including Java requirements and certificate authority readiness.
component: pingds
version: 8.1
page_id: pingds:upgrade-guide:before-you-upgrade
canonical_url: https://docs.pingidentity.com/pingds/8.1/upgrade-guide/before-you-upgrade.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Compatibility", "LDAP", "Upgrade"]
section_ids:
  supported_java: Supported Java
  upgrade-generated-cas-add: CAs from deployment IDs
  next_steps: Next steps
---

# Before you add new servers

Fulfill these requirements before upgrading PingDS software, especially before upgrading the software in a production environment. Also review the requirements listed in the [release notes](https://docs.pingidentity.com/pingds/release-notes/requirements.html).

## Supported Java

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * Always use a JVM with the latest security fixes.

* Make sure you have a supported Java environment installed on the system.

  If your default Java environment isn't appropriate, use one of the following solutions:

  * Edit the `default.java-home` setting in the `opendj/config/java.properties` file.

  * Set `DS_JAVA_HOME` to the path to the correct Java environment.

  * Set `DS_JAVA_BIN` to the absolute path of the `java` command.

* When running the `dskeymgr` and `setup` commands, use the same Java environment everywhere in the deployment and refer to [CAs from deployment IDs](#upgrade-generated-cas-add). |

DS software supports the following Java environments:

| Vendor                                                                                                                                                                                                                                                                                 | Versions |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| OpenJDK, including OpenJDK-based distributions:- AdoptOpenJDK/Eclipse Temurin Java Development Kit (Adoptium)

- Amazon Corretto

- Azul Zulu

- Oracle Java

- Red Hat OpenJDKPing Identity tests most extensively with AdoptOpenJDK/Eclipse Temurin.Use the HotSpot JVM if possible. | 25       |

TLS cipher support depends solely on the JVM. Learn more in [TLS settings](../security-guide/connections.html#tls-protocols-cipher-suites).

## CAs from deployment IDs

Due to a change to the Java platform between versions 11 and 17, the key pairs you generate with the `dskeymgr` and `setup` commands using Java 11 are incompatible with keys generated using Java 17 and later.

|   |                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Running DS servers with incompatible Java versions is a problem when you use deployment ID-based CA certificates.If you [use your own CA](../install-guide/setup-own-keys.html), not one derived from a deployment ID, skip this section. |

Replication breaks, for example, when you use the `setup` command for a new server with a more recent version of Java than was used to set up existing servers.

Find troubleshooting suggestions in [Overcome incompatible Java versions when adding new servers](../maintenance-guide/troubleshooting.html#troubleshoot-incompatible-java-versions-add-server).

## Next steps

* [icon: check-square-o, set=fa]Perform [these steps](before-you-upgrade.html) before you add servers

* [icon: square-o, set=fa]*Add new servers:*

  * [icon: square-o, set=fa]Follow [these instructions](add-new-servers.html) unless upgrading from DS 7.4.0

  * [icon: square-o, set=fa]Follow [these instructions](from-740.html) when upgrading from DS 7.4.0

* [icon: square-o, set=fa]Perform [these steps](after-you-upgrade.html) after you finish adding servers

---

---
title: Before you upgrade in place
description: Prerequisites for upgrading PingDS in place, including Java requirements, certificate authorities, credentials, and backups.
component: pingds
version: 8.1
page_id: pingds:upgrade-guide:before-you-upgrade-in-place
canonical_url: https://docs.pingidentity.com/pingds/8.1/upgrade-guide/before-you-upgrade-in-place.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Compatibility", "LDAP", "Upgrade"]
section_ids:
  supported_java: Supported Java
  upgrade-generated-cas: CAs from deployment IDs
  required_credentials: Required credentials
  back_up_first: Back up first
  disable_windows_service: Disable Windows service
  next_steps: Next steps
---

# Before you upgrade in place

Fulfill these requirements before upgrading PingDS software, especially before upgrading the software in a production environment. Also review the requirements listed in the [release notes](https://docs.pingidentity.com/pingds/release-notes/requirements.html).

## Supported Java

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * Always use a JVM with the latest security fixes.

* Make sure you have a supported Java environment installed on the system.

  If your default Java environment isn't appropriate, use one of the following solutions:

  * Edit the `default.java-home` setting in the `opendj/config/java.properties` file.

  * Set `DS_JAVA_HOME` to the path to the correct Java environment.

  * Set `DS_JAVA_BIN` to the absolute path of the `java` command.

* When running the `dskeymgr` and `setup` commands, use the same Java environment everywhere in the deployment and refer to [CAs from deployment IDs](#upgrade-generated-cas). |

DS software supports the following Java environments:

| Vendor                                                                                                                                                                                                                                                                                 | Versions |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| OpenJDK, including OpenJDK-based distributions:- AdoptOpenJDK/Eclipse Temurin Java Development Kit (Adoptium)

- Amazon Corretto

- Azul Zulu

- Oracle Java

- Red Hat OpenJDKPing Identity tests most extensively with AdoptOpenJDK/Eclipse Temurin.Use the HotSpot JVM if possible. | 25       |

TLS cipher support depends solely on the JVM. Learn more in [TLS settings](../security-guide/connections.html#tls-protocols-cipher-suites).

## CAs from deployment IDs

Due to a change to the Java platform between versions 11 and 17, the key pairs you generate with the `dskeymgr` and `setup` commands using Java 11 are incompatible with keys generated using Java 17 and later.

|   |                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Running DS servers with incompatible Java versions is a problem when you use deployment ID-based CA certificates.If you [use your own CA](../install-guide/setup-own-keys.html), not one derived from a deployment ID, skip this section. |

Replication breaks, for example, when you use the `setup` command for a new server with a more recent version of Java than was used to set up existing servers.

Find troubleshooting suggestions in [Overcome incompatible Java versions when adding new servers](../maintenance-guide/troubleshooting.html#troubleshoot-incompatible-java-versions-add-server).

## Required credentials

Perform the upgrade procedure as the user who owns the server files.

Make sure you have the credentials to run commands as this user.

## Back up first

Before upgrading, perform a full file system backup of the current server so that you can revert on failure. Make sure you stop the directory server and *back up the file system directory where the current server is installed*.

Backup archives are *not guaranteed to be compatible* across major and minor server releases. *Restore backups only on directory servers of the same major or minor version.*

## Disable Windows service

If you are upgrading a server registered as a Windows service, disable the Windows service before upgrade:

```powershell
windows-service.bat --disableService
```

After upgrade, enable the server as a Windows service again.

## Next steps

* [icon: check-square-o, set=fa]Perform [these steps](before-you-upgrade-in-place.html) before you upgrade

* [icon: square-o, set=fa]*Upgrade each:*

  * [icon: square-o, set=fa][Directory server](upgrade-ds.html)

  * [icon: square-o, set=fa][Directory proxy](upgrade-proxy.html)

  * [icon: square-o, set=fa][Replication server](upgrade-rs.html)

  * [icon: square-o, set=fa][HDAP gateway](upgrade-rest.html)

* [icon: square-o, set=fa]Perform [these steps](after-you-upgrade-in-place.html) after you upgrade

---

---
title: Directory proxy
description: Steps to upgrade a PingDS directory proxy server in place using the upgrade command.
component: pingds
version: 8.1
page_id: pingds:upgrade-guide:upgrade-proxy
canonical_url: https://docs.pingidentity.com/pingds/8.1/upgrade-guide/upgrade-proxy.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["LDAP", "Upgrade"]
section_ids:
  next_steps: Next steps
---

# Directory proxy

This page shows how to upgrade a directory proxy server in place. A directory proxy server has no local user data.

|   |                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Before upgrading, make sure you stop the server. Once you have unpacked the new server files, do not modify the server configuration until after you have completed the upgrade process. |

1. Make sure you've completed the tasks in [Before you upgrade in place](before-you-upgrade-in-place.html).

2. Stop the server.

3. Proceed to upgrade the server:

   1. When upgrading a server installed from the cross-platform ZIP distribution:

      * [Unpack the new files over the old files](../install-guide/install-files.html).

      * If the existing server uses a Java version that is no longer supported, follow the steps in [Java updates](../security-guide/java.html), but do not restart the server yet.

      * Run the [upgrade](../tools-reference/upgrade.html) command to bring the server up to date with the new software delivery.

        By default, the `upgrade` command runs interactively, requesting confirmation before making important configuration changes. For some potentially long-duration tasks, such as rebuilding indexes, the default choice is to defer the tasks until after upgrade.

        You can use the `--no-prompt` option to run the command non-interactively. In this case, the `--acceptLicense` option lets you accept the license terms non-interactively.

        When using the `--no-prompt` option, if the `upgrade` command cannot complete because it requires confirmation for a potentially long or critical task, then it exits with an error, and a message about how to finish making the changes. You can add the `--force` option to force a non-interactive upgrade to continue in this case, also performing long-running and critical tasks.

   2. When upgrading a server installed from native packages, use the system package management tools.

   Although unlikely, when the server configuration has changed in an incompatible way with the previous release, the `upgrade` command can fail when performing property value substitution for a configuration expression. If this happens, change the configuration to a static value during upgrade. Use the configuration expression again after you successfully run the `upgrade` command.

4. Start the upgraded server.

   At this point, the upgrade process is complete. Refer to the resulting `upgrade.log` file for a full list of operations performed.

5. If you disabled the Windows service to upgrade, enable it again:

   ```powershell
   windows-service.bat --enableService
   ```

## Next steps

* [icon: check-square-o, set=fa]Perform [these steps](before-you-upgrade-in-place.html) before you upgrade

* [icon: square-o, set=fa]Upgrade each:

  * [icon: check-square-o, set=fa][Directory server](upgrade-ds.html)

  * [icon: check-square-o, set=fa][Directory proxy](upgrade-proxy.html)

  * [icon: square-o, set=fa]*[Replication server](upgrade-rs.html)*

  * [icon: square-o, set=fa]*[HDAP gateway](upgrade-rest.html)*

* [icon: square-o, set=fa]Perform [these steps](after-you-upgrade-in-place.html) after you upgrade

---

---
title: Directory server
description: Steps to upgrade a PingDS directory server in place using the upgrade command.
component: pingds
version: 8.1
page_id: pingds:upgrade-guide:upgrade-ds
canonical_url: https://docs.pingidentity.com/pingds/8.1/upgrade-guide/upgrade-ds.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["LDAP", "Upgrade"]
section_ids:
  next_steps: Next steps
---

# Directory server

This page shows how to upgrade a directory server in place.

|   |                                                                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Before upgrading, make sure you stop the server. Once you have unpacked the new server files, do not modify the server configuration until after you have completed the upgrade process.Failure to follow the upgrade instructions can result in the loss of all user data. |

1. Make sure you've completed the tasks in [Before you upgrade in place](before-you-upgrade-in-place.html).

2. Stop the server.

3. Proceed to upgrade the server:

   1. When upgrading a server installed from the cross-platform ZIP distribution:

      * [Unpack the new files over the old files](../install-guide/install-files.html).

      * If the existing server uses a Java version that is no longer supported, follow the steps in [Java updates](../security-guide/java.html), but do not restart the server yet.

      * Run the [upgrade](../tools-reference/upgrade.html) command to bring the server up to date with the new software delivery.

        By default, the `upgrade` command runs interactively, requesting confirmation before making important configuration changes. For some potentially long-duration tasks, such as rebuilding indexes, the default choice is to defer the tasks until after upgrade.

        You can use the `--no-prompt` option to run the command non-interactively. In this case, the `--acceptLicense` option lets you accept the license terms non-interactively.

        When using the `--no-prompt` option, if the `upgrade` command cannot complete because it requires confirmation for a potentially long or critical task, then it exits with an error, and a message about how to finish making the changes. You can add the `--force` option to force a non-interactive upgrade to continue in this case, also performing long-running and critical tasks.

   2. When upgrading a server installed from native packages, use the system package management tools.

   Although unlikely, when the server configuration has changed in an incompatible way with the previous release, the `upgrade` command can fail when performing property value substitution for a configuration expression. If this happens, change the configuration to a static value during upgrade. Use the configuration expression again after you successfully run the `upgrade` command.

4. When the mutable data mounted at runtime differs from that of the instance where you first run the `upgrade` command, upgrade only mutable data by running the command again with the `--dataOnly` option at runtime.

   The `--dataOnly` option can be useful when running the server in a Docker container, for example.

5. Start the upgraded server.

   At this point, the upgrade process is complete. Refer to the resulting `upgrade.log` file for a full list of operations performed.

   Replication updates the upgraded server with changes that occurred during the upgrade process.

6. If you disabled the Windows service to upgrade, enable it again:

   ```powershell
   windows-service.bat --enableService
   ```

## Next steps

* [icon: check-square-o, set=fa]Perform [these steps](before-you-upgrade-in-place.html) before you upgrade

* [icon: square-o, set=fa]Upgrade each:

  * [icon: check-square-o, set=fa][Directory server](upgrade-ds.html)

  * [icon: square-o, set=fa]*[Directory proxy](upgrade-proxy.html)*

  * [icon: square-o, set=fa]*[Replication server](upgrade-rs.html)*

  * [icon: square-o, set=fa]*[HDAP gateway](upgrade-rest.html)*

* [icon: square-o, set=fa]Perform [these steps](after-you-upgrade-in-place.html) after you upgrade

---

---
title: HDAP gateway
description: Steps to upgrade the PingDS HDAP gateway by replacing it with the newer version and rewriting the configuration.
component: pingds
version: 8.1
page_id: pingds:upgrade-guide:upgrade-rest
canonical_url: https://docs.pingidentity.com/pingds/8.1/upgrade-guide/upgrade-rest.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["LDAP", "REST API", "Upgrade"]
section_ids:
  next_steps: Next steps
---

# HDAP gateway

Replace the HDAP gateway with the newer version, as for a fresh installation, and rewrite the configuration to work with the new version.

## Next steps

* [icon: check-square-o, set=fa]Perform [these steps](before-you-upgrade-in-place.html) before you upgrade

* [icon: square-o, set=fa]Upgrade each:

  * [icon: check-square-o, set=fa][Directory server](upgrade-ds.html)

  * [icon: check-square-o, set=fa][Directory proxy](upgrade-proxy.html)

  * [icon: check-square-o, set=fa][Replication server](upgrade-rs.html)

  * [icon: check-square-o, set=fa][HDAP gateway](upgrade-rest.html)

* [icon: square-o, set=fa]Perform [these steps](after-you-upgrade-in-place.html) after you upgrade

---

---
title: Replication server
description: Steps to upgrade a standalone PingDS replication server in place using the upgrade command.
component: pingds
version: 8.1
page_id: pingds:upgrade-guide:upgrade-rs
canonical_url: https://docs.pingidentity.com/pingds/8.1/upgrade-guide/upgrade-rs.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["LDAP", "Replication", "Upgrade"]
section_ids:
  next_steps: Next steps
---

# Replication server

This page shows how to upgrade a standalone replication server in place. A standalone replication server has no local user data. If the server holds user data, refer to [Directory server](upgrade-ds.html) instead.

|   |                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Before upgrading, make sure you stop the server. Once you have unpacked the new server files, do not modify the server configuration until after you have completed the upgrade process. |

1. Make sure you've completed the tasks in [Before you upgrade in place](before-you-upgrade-in-place.html).

2. Stop the server.

3. Proceed to upgrade the server:

   1. When upgrading a server installed from the cross-platform ZIP distribution:

      * [Unpack the new files over the old files](../install-guide/install-files.html).

      * If the existing server uses a Java version that is no longer supported, follow the steps in [Java updates](../security-guide/java.html), but do not restart the server yet.

      * Run the [upgrade](../tools-reference/upgrade.html) command to bring the server up to date with the new software delivery.

        By default, the `upgrade` command runs interactively, requesting confirmation before making important configuration changes. For some potentially long-duration tasks, such as rebuilding indexes, the default choice is to defer the tasks until after upgrade.

        You can use the `--no-prompt` option to run the command non-interactively. In this case, the `--acceptLicense` option lets you accept the license terms non-interactively.

        When using the `--no-prompt` option, if the `upgrade` command cannot complete because it requires confirmation for a potentially long or critical task, then it exits with an error, and a message about how to finish making the changes. You can add the `--force` option to force a non-interactive upgrade to continue in this case, also performing long-running and critical tasks.

   2. When upgrading a server installed from native packages, use the system package management tools.

   Although unlikely, when the server configuration has changed in an incompatible way with the previous release, the `upgrade` command can fail when performing property value substitution for a configuration expression. If this happens, change the configuration to a static value during upgrade. Use the configuration expression again after you successfully run the `upgrade` command.

4. Start the upgraded server.

   At this point, the upgrade process is complete. Refer to the resulting `upgrade.log` file for a full list of operations performed.

5. If you disabled the Windows service to upgrade, enable it again:

   ```powershell
   windows-service.bat --enableService
   ```

## Next steps

* [icon: check-square-o, set=fa]Perform [these steps](before-you-upgrade-in-place.html) before you upgrade

* [icon: square-o, set=fa]Upgrade each:

  * [icon: check-square-o, set=fa][Directory server](upgrade-ds.html)

  * [icon: check-square-o, set=fa][Directory proxy](upgrade-proxy.html)

  * [icon: check-square-o, set=fa][Replication server](upgrade-rs.html)

  * [icon: square-o, set=fa]*[HDAP gateway](upgrade-rest.html)*

* [icon: square-o, set=fa]Perform [these steps](after-you-upgrade-in-place.html) after you upgrade

---

---
title: "Strategy: in-place upgrade"
description: Overview of the PingDS in-place upgrade strategy, where you unpack new software over the old and run the upgrade command.
component: pingds
version: 8.1
page_id: pingds:upgrade-guide:in-place-upgrade
canonical_url: https://docs.pingidentity.com/pingds/8.1/upgrade-guide/in-place-upgrade.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
section_ids:
  next_steps: Next steps
---

# Strategy: in-place upgrade

These pages cover *in-place upgrades*. For servers, you unpack the new software over old and run the `upgrade` command, reusing the same host systems. Learn about the alternatives in [Upgrade strategies](strategies.html).

|   |                                                                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you use encryption and the default `cipher-transformation` settings, you cannot upgrade in place from DS 7.4.0. Upgrade by [adding new servers](new-servers.html) instead and refer to [Upgrade from DS 7.4.0](from-740.html) for details. |

## Next steps

* [icon: square-o, set=fa]*Perform [these steps](before-you-upgrade-in-place.html) before you upgrade*

* [icon: square-o, set=fa]Upgrade each:

  * [icon: square-o, set=fa][Directory server](upgrade-ds.html)

  * [icon: square-o, set=fa][Directory proxy](upgrade-proxy.html)

  * [icon: square-o, set=fa][Replication server](upgrade-rs.html)

  * [icon: square-o, set=fa][HDAP gateway](upgrade-rest.html)

* [icon: square-o, set=fa]Perform [these steps](after-you-upgrade-in-place.html) after you upgrade

---

---
title: "Strategy: new servers"
description: Overview of the PingDS upgrade strategy that adds new servers on new host systems and retires the old servers.
component: pingds
version: 8.1
page_id: pingds:upgrade-guide:new-servers
canonical_url: https://docs.pingidentity.com/pingds/8.1/upgrade-guide/new-servers.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
section_ids:
  next_steps: Next steps
---

# Strategy: new servers

These pages cover *upgrade by adding new servers* on new host systems, then retiring old servers. Learn about the alternatives in [Upgrade strategies](strategies.html).

## Next steps

* [icon: square-o, set=fa]*Perform [these steps](before-you-upgrade.html) before you add servers*

* [icon: square-o, set=fa]Add new servers:

  * [icon: square-o, set=fa]Follow [these instructions](add-new-servers.html) unless upgrading from DS 7.4.0

  * [icon: square-o, set=fa]Follow [these instructions](from-740.html) when upgrading from DS 7.4.0

* [icon: square-o, set=fa]Perform [these steps](after-you-upgrade.html) after you finish adding servers

---

---
title: Upgrade
description: Landing page for PingDS upgrade documentation, with links to upgrade strategies and step-by-step guides for in-place and new-server upgrades.
component: pingds
version: 8.1
page_id: pingds:upgrade-guide:preface
canonical_url: https://docs.pingidentity.com/pingds/8.1/upgrade-guide/preface.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["LDAP", "Upgrade"]
page_aliases: ["index.adoc"]
---

# Upgrade

These pages show you how to upgrade PingDS software.

[icon: info, set=fas, size=3x]

#### [About upgrades](about-upgrades.html)

Read this first.

[icon: chess-queen, set=fas, size=3x]

#### [Upgrade strategies](strategies.html)

Choose between upgrading in place and upgrading by adding servers.

[icon: circle-up, set=fas, size=3x]

#### [Upgrade in place](in-place-upgrade.html)

Overwrite old software to upgrade on the same server.

[icon: square-plus, set=fas, size=3x]

#### [Upgrade by adding servers](new-servers.html)

Add new servers then retire old ones.

Read the [release notes](https://docs.pingidentity.com/pingds/release-notes/index.html) before you upgrade DS software.

---

---
title: Upgrade from DS 7.4.0
description: Steps to upgrade from PingDS 7.4.0 when using default data encryption, working around an incompatibility introduced in that release.
component: pingds
version: 8.1
page_id: pingds:upgrade-guide:from-740
canonical_url: https://docs.pingidentity.com/pingds/8.1/upgrade-guide/from-740.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["LDAP", "Upgrade"]
section_ids:
  the_problem: The problem
  the_solution: The solution
  next_steps: Next steps
---

# Upgrade from DS 7.4.0

If the deployment includes a DS 7.4.0 server with [data encryption](../security-guide/data.html) using default settings, follow the procedures on this page.

If the deployment has no DS 7.4.0 servers or does not use data encryption, skip this page.

## The problem

Due to an issue (OPENDJ-10211) in the way DS 7.4.0 encrypts data on disk when using the default `cipher-transformation: AES/GCM/NoPadding` setting, the backend or changelog data on disk and encrypted with 7.4.0 is incompatible with all other DS versions.

If the deployment is configured with non-default `cipher-transformation` settings that do not use the AES algorithm and GCM mode, the problem doesn't affect the deployment. In this case, skip this page.

Otherwise, the directory data on disk uses incompatible encryption. Any binary backups of the backend data are also affected. You can't use the `upgrade` command to upgrade a DS server to 7.4.0 from earlier versions or from 7.4.0 to later versions.

## The solution

You *can* upgrade by adding new DS servers; follow these steps:

1. Upgrade by [adding new servers](add-new-servers.html), leaving existing 7.4.0 servers in operation during the upgrade.

   When initializing new servers, *do not use backup files*, as they use incompatible encryption. Instead, either [initialize data over the network](../config-guide/repl-init.html#init-repl-online) or [initialize all replicas from plaintext LDIF](../config-guide/repl-init.html#init-repl-ldif).

2. Change the [bootstrap replication servers](../config-guide/repl-bootstrap.html) for each server to stop using the DS 7.4.0 servers.

3. If you use backup files, create them from the new servers with compatible encryption.

4. Stop directing client application traffic to the DS 7.4.0 servers.

5. Wait until the replication purge delay has elapsed (default: 3 days) and retire the DS 7.4.0 servers.

## Next steps

* [icon: check-square-o, set=fa]Perform [these steps](before-you-upgrade.html) before you add servers

* [icon: check-square-o, set=fa]Add new servers:

  * [icon: check-square-o, set=fa]Follow [these instructions](add-new-servers.html) unless upgrading from DS 7.4.0

  * [icon: check-square-o, set=fa]Follow [these instructions](from-740.html) when upgrading from DS 7.4.0

* [icon: square-o, set=fa]*Perform [these steps](after-you-upgrade.html) after you finish adding servers*

---

---
title: Upgrade strategies
description: "Comparison of PingDS upgrade strategies: upgrading in place versus adding new servers, with advantages, disadvantages, and guidance on blue-green deployments."
component: pingds
version: 8.1
page_id: pingds:upgrade-guide:strategies
canonical_url: https://docs.pingidentity.com/pingds/8.1/upgrade-guide/strategies.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Compatibility", "LDAP", "Replication", "Upgrade"]
section_ids:
  upgrade-in-place: Upgrade in place
  upgrade-repl: On upgrading replicas
  add-new-servers: Add new servers
  upgrade-parallel: Blue-green deployment
---

# Upgrade strategies

When you upgrade to a new DS version, you choose between:

* [Upgrade in place](#upgrade-in-place): unpack the new software over the old software and run the `upgrade` command.

* [Add new servers](#add-new-servers) then retire old ones.

|   |                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------- |
|   | For some scenarios, like upgrading Docker images in a Kubernetes deployment, you must upgrade in place. |

## Upgrade in place

The most straightforward option when upgrading DS servers is to upgrade in place. DS software provides an `upgrade` command to simplify the process.

|   |                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you want to use new hardware, you can often still upgrade in place. [Move a server](../maintenance-guide/mv-servers.html) to the new hardware, then upgrade it in place. |

One by one, you stop, upgrade, and restart each server individually, leaving the service running during upgrade.

**Upgrade in place**

| Advantages                                                                                                     | Disadvantages                                                                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| No additional systems to manage.                                                                               | During the upgrade, the host system must meet the requirements for both the older version and the new release.For example, you may need to have more than one Java environment installed. The operating system must also be supported for both releases. |
| Simpler to understand.                                                                                         | Slower to roll back.Rollback involves restoring each server to its pre-upgrade state.Once a replica's databases have been upgraded, they cannot be rolled back.                                                                                          |
| Easier to maintain compatibility.To the extent possible, the `upgrade` command leaves the configuration as is. | You must manually enable new features after the upgrade.                                                                                                                                                                                                 |

### On upgrading replicas

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The in-place upgrade process is designed to support a rolling (sequential) upgrade of replicated servers.Do not upgrade all replicated servers at once in parallel, as this removes all replication changelog data simultaneously, breaking replication.If the deployment includes DS 7.4.0 servers with [data encryption](../security-guide/data.html) using default settings, you must [add new servers](#add-new-servers) instead. Learn more in [Upgrade from DS 7.4.0](from-740.html). |

When upgrading in place, follow these steps for each replica:

1. Direct client application traffic away from the server to upgrade.

2. Upgrade the replica.

3. Direct client application traffic back to the upgraded server.

## Add new servers

Adding new servers and then retiring old ones is an alternative to upgrading in place. You replicate data between old and new systems, leaving the service running during the upgrade.

|   |                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When upgrading by adding new servers, *reuse the server IDs of retired servers*. After you retire a server, reuse its server ID the next time you add a new server.This reduces the proliferation of obsolete server IDs polluting the replication topology state data. |

**Add new servers**

| Advantages                                                                                                           | Disadvantages                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Smoothly phase out old host systems.After successfully completing the upgrade, you gradually retire the old systems. | New host systems to manage.                                                                                                                                                                                                                                                                                                                                           |
| Faster to roll back.Old servers remain in operation until the upgrade completes successfully.                        | Harder to maintain compatibility.You must manually configure new servers to be fully compatible with existing servers, rather than relying on the `upgrade` command. This requires an in-depth understanding of both your existing configuration and the new configuration. Some new default settings may be incompatible with the old default settings, for example. |
|                                                                                                                      | Requires initializing the new replicas.Depending on the volume of data to synchronize, you can initialize at least the first new replica online. For deployments with medium to large data sets, initialize from exported LDIF or from backup files created using an upgraded DS server. In either case, you must plan the operation.                                 |
|                                                                                                                      | You must manually enable new features after the upgrade.                                                                                                                                                                                                                                                                                                              |

### Blue-green deployment

[Blue-green deployment](https://en.wikipedia.org/wiki/Blue%E2%80%93green_deployment) is a way of making changes by alternating "blue" and "green" servers:

* Start with existing servers that don't change.

* Add servers that apply the change.

* Validate the change.

  * On success, [update bootstrap replication server settings](../config-guide/repl-bootstrap.html) to target the new servers, then retire the old servers.

  * On failure, retire the servers that introduced the change.

You can use this method to:

* [Upgrade servers](new-servers.html).

* Upgrade or refresh a server computer's operating system or the JVM DS uses.

* Test compatible configuration changes.

* Apply patches.

|   |                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Whatever changes you make—​OS and JVM updates, configuration and schema changes, DS upgrades or patches, and so on—​keep the following in mind.*DS replicates the same data to all DS servers in the deployment, regardless of whether you think of them as "blue" servers or "green" servers.* |

It's better to roll out configuration, schema, and data changes separately from DS version upgrades.

When you write data to a "green" server, it replicates the change to the "blue" *and* the "green" servers. Likewise, changes to a "blue" server's data replicate to the "green" *and* the "blue" servers. You'll break things if you make changes to "blue" servers that render replicated data incompatible with "green" servers or the other way around. "Blue" and "green" servers are all part of the same deployment pool.

If a change could cause problems that only arise with live client applications, try a canary release. Direct a portion of client traffic to one server, make the change to the server, and monitor how the change affects the clients and DS.