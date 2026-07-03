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
