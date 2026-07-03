---
title: Drop-in software update
description: Perform a drop-in software update for PingAM Web Agent on Apache HTTP Server, IIS, ISAPI, and NGINX Plus by replacing executable files, with rollback instructions.
component: web-agents
version: 2026
page_id: web-agents:upgrade:drop-in-upgrade
canonical_url: https://docs.pingidentity.com/web-agents/2026/upgrade/drop-in-upgrade.html
section_ids:
  perform_a_drop_in_software_update: Perform a drop-in software update
  roll_back_from_a_drop_in_software_update: Roll back from a drop-in software update
---

# Drop-in software update

## Perform a drop-in software update

1. Read the [release notes](https://docs.pingidentity.com/web-agents/release-notes/preface.html) for information about changes in Web Agent.

2. Download the agent binaries from [Ping Identity Product Downloads](https://product-downloads.pingidentity.com). Make sure you select the correct operating system and architecture.

3. Redirect client traffic away from the protected website.

4. Stop the web server where the agent is installed.

5. Replace the following executable files in the current installation with the corresponding files in the downloaded binaries, and make sure that they have the same permissions as the original files:

   * Apache Web Agent:

     * `web_agents/apache24_agent/lib/mod_openam.so`

     * `web_agents/apache24_agent/bin/agentadmin`

   * IIS Web Agent:

     * `web_agents/iis_agent/lib/mod_iis_openam_64.dll`

     * `web_agents/iis_agent/lib/mod_iis_openam_64.pdb`

     * `web_agents/iis_agent/lib/mod_iis_openam_32.dll`

     * `web_agents/iis_agent/lib/mod_iis_openam_32.pdb`

     * `web_agents/iis_agent/bin/agentadmin.exe`

     * `web_agents/iis_agent/bin/agentadmin.pdb`

   * ISAPI Web Agent:

     * `web_agents/iis_agent/lib/mod_isapi_openam_64.dll`

     * `web_agents/iis_agent/lib/mod_isapi_openam_64.pdb`

     * `web_agents/iis_agent/lib/mod_isapi_openam_32.dll`

     * `web_agents/iis_agent/lib/mod_isapi_openam_32.pdb`

     * `web_agents/iis_agent/bin/agentadmin.exe`

     * `web_agents/iis_agent/bin/agentadmin.pdb`

   * NGINX Plus Web Agent:

     * `web_agents/nginxversion-number_agent/lib/openam_ngx_auth_module.so`

     * `web_agents/nginxversion-number_agent/bin/agentadmin`

       Use the module in the directory for your NGINX version. The following example is for NGINX Plus R36: `web_agents/nginx36_agent/lib/openam_ngx_auth_module.so`

6. Start the web server where the agent is installed.

7. Validate that the agent is performing as expected in the following ways:

   * Check in `/path/to/web_agents/agent_type/log/system_n.log` that the new version of the agent is running.

   * Go to a protected page on the website and confirm whether you can access it according to your configuration.

   * Check logs files for errors.

   |   |                                                                                                                              |
   | - | ---------------------------------------------------------------------------------------------------------------------------- |
   |   | To troubleshoot your environment, run the [agentadmin command](../installation-guide/agentadmin.html) with the `--V` option. |

8. Allow client traffic to flow to the protected website.

## Roll back from a drop-in software update

|   |                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Before you roll back to an earlier version of Web Agent, consider whether any change to the configuration during or since upgrade could be incompatible with the earlier version. |

To roll back from a drop-in software update, run through the procedure in [Drop-in software update](#drop-in-software-update), but replace the executables with the earlier files, or with those from an earlier version of the agent.

---

---
title: Major upgrade
description: Perform a major upgrade of PingAM Web Agent with downtime, including backup, reinstallation, configuration review, and rollback instructions.
component: web-agents
version: 2026
page_id: web-agents:upgrade:major-upgrade
canonical_url: https://docs.pingidentity.com/web-agents/2026/upgrade/major-upgrade.html
section_ids:
  perform_a_major_upgrade: Perform a major upgrade
  roll_back_from_a_major_upgrade: Roll back from a major upgrade
---

# Major upgrade

## Perform a major upgrade

1. Read the [release notes](https://docs.pingidentity.com/web-agents/release-notes/preface.html) for information about changes in Web Agent.

2. Download the agent binaries from [Ping Identity Product Downloads](https://product-downloads.pingidentity.com). Make sure you select the correct operating system and architecture.

3. Plan for server downtime.

   Plan to route client applications to another server until the process is complete and you have validated the result. Make sure the owners of client application are aware of the change, and let them know what to expect.

4. Back up the directories for the agent installation and web server configuration and store them in version control so that you can roll back if something goes wrong:

   * In [local configuration mode](../user-guide/glossary.html#def-local-configuration-mode):

     ```
     $ cp -r /path/to/web_agents/apache24_agent /path/to/backup
     $ cp -r /path/to/apache/httpd/conf /path/to/backup
     ```

   * In [centralized configuration mode](../user-guide/glossary.html#def-central-configuration-mode), back up as described in AM's [Maintenance guide](https://docs.pingidentity.com/pingam/8.1/maintenance/backup-restore.html).

5. Redirect client traffic away from the protected website.

6. Stop the web server where the agent is installed.

7. Remove the old Web Agent, as described in [Remove Web Agent](../installation-guide/uninstallation.html).

8. Delete the following shared memory files:

   * `/dev/shm/am_cache_0`

   * `/dev/shm/am_log_data_0`

   Depending on your configuration, the files can be named differently.

9. If the HTTP proxy or certificate requires credentials, set installation environment variables for one or both of the following properties:

   * [Private Key Password](../properties-reference/com.forgerock.agents.config.cert.key.password.html)

   * [Proxy Server Password](../properties-reference/com.sun.identity.agents.config.forward.proxy.password.html)

   Learn more in AM\_SSL\_PASSWORD and AM\_PROXY\_PASSWORD in [Installation environment variables](../installation-guide/installer-env-vars.html).

10. Install the new agent.

    In [local configuration mode](../user-guide/glossary.html#def-local-configuration-mode), provide the [agent.conf](../user-guide/about.html#agent_conf) file.

    The installer generates the following files:

    * [agent-key.conf](../user-guide/about.html#agent_key_conf) containing the [Agent Profile Password Encryption Key](../properties-reference/com.sun.identity.agents.config.key.html)

    * [agent-password.conf](../user-guide/about.html#agent_password_conf) containing the [Agent Profile Password](../properties-reference/com.sun.identity.agents.config.password.html)

      When the HTTP proxy or certificate requires credentials, `agent-password.conf` should also contain one or both of [Private Key Password](../properties-reference/com.forgerock.agents.config.cert.key.password.html) and [Proxy Server Password](../properties-reference/com.sun.identity.agents.config.forward.proxy.password.html).

11. Review the agent configuration:

    * In [local configuration mode](../user-guide/glossary.html#def-local-configuration-mode), use the backed-up copy of `agent.conf` file for guidance, the agent's [release notes](https://docs.pingidentity.com/web-agents/release-notes/preface.html), and AM's [release notes](https://docs.pingidentity.com/pingam/release-notes/preface.html) to check for changes. Update the file manually to include properties for your environment.

      |   |                                                                                                                                                                                                       |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | To prevent errors, make sure the `agent.conf` file contains all required properties. For a list of required properties, refer to [Configuration files](../user-guide/about.html#configuration_files). |

    * In [centralized configuration mode](../user-guide/glossary.html#def-central-configuration-mode), review the agent's [release notes](https://docs.pingidentity.com/web-agents/release-notes/preface.html) and AM's [release notes](https://docs.pingidentity.com/pingam/release-notes/preface.html) to check for changes. If necessary, change the agent configuration using the AM admin UI.

12. In the new `agent-password.conf` file, set the value of [Agent Profile Password](../properties-reference/com.sun.identity.agents.config.password.html) to the value of the encrypted password.

13. (NGINX Plus and Unix Apache agents only) Configure shared runtime resources and shared memory. Learn more in [Configure shared runtime resources and memory](../installation-guide/post-installation.html#configuring-shared-memory).

14. Ensure the communication between AM and the web agent is secured with the appropriate keys. Learn more in [Configuring AM to sign authentication information](../installation-guide/pre-installation.html#configuring-agent-communication).

15. Start the web server where the agent is installed.

16. Allow client traffic to flow to the protected website.

17. Validate that the agent is performing as expected in the following ways:

    * Check in `/path/to/web_agents/agent_type/log/system_n.log` that the new version of the agent is running.

    * Go to a protected page on the website and confirm whether you can access it according to your configuration.

    * Check logs files for errors.

    |   |                                                                                                                              |
    | - | ---------------------------------------------------------------------------------------------------------------------------- |
    |   | To troubleshoot your environment, run the [agentadmin command](../installation-guide/agentadmin.html) with the `--V` option. |

## Roll back from a major upgrade

|   |                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Before you roll back to an earlier version of Web Agent, consider whether any change to the configuration during or since upgrade could be incompatible with the earlier version. |

To roll back from a major upgrade, run through the procedure in [Major upgrade](#major-upgrade), but use the backed up directories for the agent installation and web server configuration.

---

---
title: Post update and upgrade tasks
description: "Post-upgrade tasks for PingAM Web Agent: review release notes for new features and follow up with post-installation configuration steps."
component: web-agents
version: 2026
page_id: web-agents:upgrade:post-upgrade-tasks
canonical_url: https://docs.pingidentity.com/web-agents/2026/upgrade/post-upgrade-tasks.html
---

# Post update and upgrade tasks

After upgrade, review the [what's new](https://docs.pingidentity.com/web-agents/release-notes/whats-new.html) section in the release notes and consider activating new features and functionality.

For information about other post-installation options, refer to [Post-installation](../installation-guide/post-installation.html).

---

---
title: Upgrade
description: Upgrade guide for PingAM Web Agent, covering drop-in software updates and major upgrades, with guidance on when each type applies.
component: web-agents
version: 2026
page_id: web-agents:upgrade:preface
canonical_url: https://docs.pingidentity.com/web-agents/2026/upgrade/preface.html
page_aliases: ["index.adoc"]
section_ids:
  preface-examples: Example installation for this guide
---

# Upgrade

Web Agent supports the following types of upgrade:

* [Drop-in software update](drop-in-upgrade.html):

  Usually, an update from a version of Web Agent to a newer minor version, as defined in [Ping Identity End of Life (EOL) Software Tracker](https://support.pingidentity.com/s/article/Ping-Identity-EOL-Tracker#pamagents). For example, update from 2025.9 to 2025.11 can be a drop-in software update.

  Drop-in software updates can introduce additional functionality and fix bugs or security issues. Consider the following restrictions for drop-in software updates:

  * Don't require any update to the configuration

  * Can't cause feature regression

  * Can change default or previously configured behavior **only** for bug fixes and security issues

  * Can deprecate **but not remove** existing functionality

* [Major upgrade](major-upgrade.html):

  Usually, an upgrade from a version of Web Agent to a newer major version, as defined in [Ping Identity End of Life (EOL) Software Tracker](https://support.pingidentity.com/s/article/Ping-Identity-EOL-Tracker#pamagents). For example, upgrade from 2025.11 to 2026.6 is a major upgrade.

  Major upgrades can introduce additional functionality and fix bugs or security issues. Major upgrades do not have the restrictions of drop-in software update. Consider the following features of major upgrades:

  * Can require code or configuration changes

  * Can cause feature regression

  * Can change default or previously configured behavior

  * Can deprecate **and** remove existing functionality

This guide describes how to upgrade a single Web Agent instance. To upgrade sites with multiple Web Agent instances, one by one, stop, upgrade, and then restart each server individually, leaving the service running during the upgrade.

Find information about upgrade between supported versions of Web Agent in [Ping Identity End of Life (EOL) Software Tracker](https://support.pingidentity.com/s/article/Ping-Identity-EOL-Tracker#pamagents).

## Example installation for this guide

Unless otherwise stated, the examples in this guide assume the following installation:

* Web Agent installed on `https://agent.example.com:443`.

* AM installed on `https://am.example.com:8443/am`.

* Work in the top-level realm `/`.

If you use a different configuration, substitute in the procedures accordingly.