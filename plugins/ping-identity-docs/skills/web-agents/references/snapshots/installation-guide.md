---
title: agentadmin command
description: "Reference for all agentadmin command options: install, remove, list, enable, disable, validate, generate keys, and encrypt passwords."
component: web-agents
version: 2026
page_id: web-agents:installation-guide:agentadmin
canonical_url: https://docs.pingidentity.com/web-agents/2026/installation-guide/agentadmin.html
section_ids:
  i: "--i"
  agentadmin-s: "--s"
  n: "--n"
  agentadmin-l: "--l"
  g: "--g"
  e: "--e"
  d: "--d"
  o: "--o"
  r: "--r"
  agentadmin-k: "--k"
  p: "--p"
  vi: "--V[i]"
  v: "--v"
---

# agentadmin command

The `agentadmin` command manages Web Agent installation and keys. It returns `EXIT_SUCCESS` (or `0`) when it completes successfully, and `EXIT_FAILURE` (or a code greater than zero) when it fails.

The following options are supported:

## `--i`

Install a new agent instance.

Usage: `agentadmin --i`

|   |                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can set [environment variables](installer-env-vars.html) during installation by adding them to the command line when you install the agent. |

## `--s`

Install a new agent instance non-interactively.

Usage: `agentadmin --s web-server-config-file openam-url agent-url realm agent-profile-name agent-profile-password [--changeOwner] [--forceInstall]`

* *web-server-config-file*

  (Apache HTTP Server) The full path to the server configuration file. The installer modifies this file to include the agent configuration and module.

  (IIS and ISAPI agent only) The ID number of the IIS or ISAPI site in which to install the agent. To list the available sites in an IIS server and the relevant ID numbers, run `agentadmin.exe --n`.

* *am-url*

  The full URL of the AM instance that the agent will use. Ensure the deployment URI is specified.

  Example: `https://am.example.com:8443/am`

  |   |                                                                                                                                                                                                                                                                                                |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If a reverse proxy is configured between AM and the agent, set the AM URL to the proxy URL, for example, `https://proxy.example.com:443/am`. You can find information about setting up an environment for reverse proxies in [Apache as a reverse proxy](apache.html#configure-apache-server). |

* *agent-url*

  The full URL of the server on which the agent is running.

  Example: `https://agent.example.com:443`

* *realm*

  The AM realm containing the agent profile.

* *agent-profile-name*

  The name of the agent profile in AM.

* *agent-profile-password*

  The full path to the agent profile password file.

* `--changeOwner`

  Apache web agent for Unix only: Change the ownership of created directories to the user and group as specified in the Apache configuration file.

  To use this option, you must run the `agentadmin` command as the `root` user or with the `sudo` command. If you can't run the `agentadmin` command as the `root` user or with the `sudo` command, you must change the ownership manually.

* `--forceInstall`

  If the agent can't connect to the specified AM server during installation, proceed with a non-interactive installation instead of exiting.

## `--n`

(IIS and ISAPI agent only) List the sites available in an IIS server.

Example:

```
c:\web_agents\iis_agent\bin> agentadmin.exe --nIIS Server Site configuration:
     ====================================
     id       details
     ====================================

     Default Web Site
     application path:/, pool DefaultAppPool
     1.1.1    virtualDirectory path:/, configuration: C:\inetpub\wwwroot\web.config

     MySite
     application path:/, pool: MySite
     2.1.1    virtualDirectory path:/, configuration C:\inetpub\MySite\web.config
     application path:/MyApp1, pool: MySite
```

## `--l`

List configured agent instances.

Usage: `agentadmin --l`

Example:

```
$ ./agentadmin --l
AM Web Agent configuration instances:

      id:            agent_1
      configuration: /opt/web_agents/apache24_agent/bin/../instances/agent_1
      server/site:   /etc/httpd/conf/httpd.conf

      id:            agent_2
      configuration: /opt/web_agents/apache24_agent/bin/../instances/agent_2
      server/site:   /etc/httpd/conf/httpd.conf

      id:            agent_3
      configuration: /opt/web_agents/apache24_agent/bin/../instances/agent_3
      server/site:   /etc/httpd/conf/httpd.conf
```

## `--g`

(IIS and ISAPI agent only) Remove all agent instances and libraries from an installation.

Usage: `agentadmin.exe --g`

Learn more in [Remove IIS or ISAPI Web Agent](uninstallation.html#uninstall-iis-agent).

## `--e`

(IIS agent only) Enable an existing agent instance.

Usage: `agentadmin.exe --e agent-instance`

Learn more in [Disable and enable Web Agent on an IIS site or application](install-iis.html#proc-enable-disable-iis-web-policy-agent).

## `--d`

(IIS agent only) Disable an existing agent instance.

Usage: `agentadmin.exe --d agent-instance`

Learn more in [Disable and enable Web Agent on an IIS site or application](install-iis.html#proc-enable-disable-iis-web-policy-agent).

## `--o`

(IIS and ISAPI agent only) Modify Access Control Lists (ACLs) for files and folders related to a web agent instance.

Usage: `agentadmin.exe --o "identity_or_siteID" "directory" [--siteId]`

Usage: `agentadmin.exe --o "directory" --addAll --removeAll`

* *"identity\_or\_siteID"*

  Specify the identity to be added to the directory's ACLs. When used with the `--siteId` option, this option specifies a site ID.

* *"directory"*

  Specify the directory that would be modified.

* `[--siteId]`

  Specify that the `agentadmin` should use `identity_or_siteID` as a site ID.

* `--addAll`

  Add all agent application pool identities to the directory's ACLs. This option is not compatible with the `--removeAll` option.

* `--removeAll`

  Remove all agent application pool identities from the directory's ACLs. This option isn't compatible with the `--addAll` option.

  Example:

  ```
  C:\web_agents\iis_agent\bin> agentadmin.exe --o "IIS_user1" "C:\web_agents\iis_agent\lib"
  ```

  ```
  C:\web_agents\iis_agent\bin> agentadmin.exe --o "2" "C:\web_agents\iis_agent\lib" --siteId
  ```

  ```
  C:\web_agents\iis_agent\bin> agentadmin.exe --o  "C:\web_agents\iis_agent\lib" --addAll
  ```

## `--r`

Remove an existing agent instance.

Usage: `agentadmin --r agent-instance`

* *agent-instance*

  The ID of the agent configuration instance to remove.

  Respond `yes` when prompted to confirm removal.

  On IIS and ISAPI web agents, the `--r` option doesn't remove the web agent libraries because they can be in use by other agent instances configured on the same site. To remove all agent instances and libraries, use the `--g` option.

## `--k`

Generate a base64-encoded 256-bit random key.

Usage: `agentadmin --k [--rotate agent-instance]`

Learn more in [Rotate keys](../maintenance-guide/rotate-keys.html).

* *\--rotate*

  Rotate the key for the specified agent instance. Learn more in [Rotate keys](../maintenance-guide/rotate-keys.html).

* *agent-instance*

  The ID of the agent instance for which to rotate keys.

  * Unix

  * Windows

  ```
  $ cd /web_agents/apache24_agent/bin/
  $ ./agentadmin --k
  Encryption key value: ztw…​hM=
  ```

  ```
  C:\> cd web_agents{apache_agent_version}\bin
  C:\web_agents{apache_agent_version}\bin> agentadmin --k
  Encryption key value: ztw…​hM=
  ```

  * Unix

  * Windows

  ```
  $ cd /web_agents/apache24_agent/bin/
  $ ./agentadmin --k --rotate agent_n
  …​
  Key rotation was successful for instance: agent_n
  ```

  ```
  C:\> cd web_agents{apache_agent_version}\bin
  C:\web_agents{apache_agent_version}\bin> agentadmin --k --rotate agent_n
  …​
  Key rotation was successful for instance: agent_n
  ```

## `--p`

Use a generated encryption key to encrypt a new password.

Use a given key to encrypt a given password. The output is an AES-256-GCM encrypted password.

Usage: `agentadmin --p key password`

* *key*

  A key generated by the `agentadmin --k` command.

* *password*

  The password to encrypt.

  The following example creates an `agent-password.conf` file containing the encrypted password, where:

  * *key* is the key generated by the `agentadmin --k` command

  * */var/tmp/pwd.txt* is a text file containing the unencrypted password

  - Unix

  - Windows

  ```
  $ ./agentadmin --p key $(cat /var/tmp/pwd.txt)
  Encrypted password value: 07b…​dO4=
  ```

  ```
  $ agentadmin.exe --p key "newpassword"
  Encrypted password value: 07b…​dO4=
  ```

## `--V[i]`

Validate the installation. Use this command in conjunction with sustaining to troubleshoot installations.

The command validates the following points:

* The agent can reach the AM server(s) configured in [AM Connection URL](../properties-reference/com.sun.identity.agents.config.naming.url.html).

* Critical bootstrap properties are set. Learn more in [Agent configuration](../user-guide/about.html#configuration-location).

* For SSL communication, TLS/SSL libraries are available and SSL configuration properties are set.

* (IIS and ISAPI agent only) The agent is running in FIPS mode.

* The system has enough RAM and shared memory.

* The agent can log in to AM with the provided credentials and fetch the agent profile.

* The agent can decrypt the agent profile password by using the [Agent Profile Password Encryption Key](../properties-reference/com.sun.identity.agents.config.key.html) provided in `agent-key.conf`.

* WebSocket connections are available between the agent and AM.

* The core init and shutdown agent sequences are working as expected. This validation requires the `--Vi` flag.

* (IIS and ISAPI agent only) The agent is configured to run application pools in Integrated mode.

* When [Server Certificate Trust](../properties-reference/com.sun.identity.agents.config.trust.server.certs.html) is set to `true` to trust all certificates, the validator issues a warning to set the property to `false` in production environments.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | - To prevent service outage or an unresponsive agent, run the command only when the agent instance isn't actively protecting a website.

- On Unix, run the command as the same user or group that runs the web server. For example, to use the Apache HTTP Server `daemon` user:

  ```
  $ sudo -u daemon ./bin/agentadmin --V agent_1
  ```

  Running the command as a different user can cause the `log/system_0.log` and `log/monitor_0.pipe` files to be created with permissions that prevent the agent from writing to them, causing an error such as:

  ```
  …​ GMT ERROR   [0x7f0c9cf05700:22420]: unable to open event channel
  ```

- Make sure the user running the command has execute permission on the following directories:

  * `/web_agents/apache24_agent/instances/agent_nnn`

  * `/web_agents/apache24_agent/log` |

Usage:

`agentadmin --V[i] agent_instance [user name] [password file] [realm]`

* \[i]

  (Optional) Ensure that the core init and shutdown agent sequences are working as expected.

* agent\_instance

  (Required) The agent instance where to run the validation tests. For example, `agent_1`.

* user name

  (Optional) A user ID that exists in the AM server. Required only for the `validate_session_profile` test. For example, `bjensen`.

* password file

  (Optional) A file containing the password of the user ID used for the `validate_session_profile` test. For example, `/secure-directory/passwd.txt`

* realm

  (Optional) The realm of the user ID used for the `validate_session_profile` test. For example, `/alpha`.

Example:

```
$ ./agentadmin --Vi agent_1 bjensen passwd.txt /
Saving output to /web_agents/apache24_agent/bin/../log/validate_xxx.log

Running configuration validation for agent_1:

Agent instance is configured with 1 naming.url value(s):
1. https://am.example.com:8443/am is valid
selected https://am.example.com:8443/am as naming.url value
validate_bootstrap_configuration: ok
validate_ssl_libraries: ok
validate_agent_login: ok
get_allocator_blockspace_sz(): trying for configured cache size 16777216 bytes
validate_system_resources: ok
validate_session_profile: ok
validate_websocket_connection: ok
validate_worker_init_shutdown: ok

Result: 7 out of 7 tests passed, 0 skipped.
```

## `--v`

Display information about `agentadmin` build and version numbers, and available system resources.

Example:

```bash
PingAM Web Agent for Apache 2.4 AMD64 Server
 Version: 2026.6
 Revision: git hash
 Build machine: build hostname
 Build date: timestamp

 System Resources:
 total memory size: 7.7GB
 pre-allocated session/policy cache size: 1.0GB
 log buffer size: 128.5MB
 min audit log buffer size: 2MB, max 2.0GB
 total disk size: 162.4GB
 free disk space size: 89.6GB
 System contains sufficient resources (with remote audit log feature enabled).
```
