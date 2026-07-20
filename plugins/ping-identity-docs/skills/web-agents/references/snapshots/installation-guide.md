---
title: agentadmin command
description: "Reference for all agentadmin command options: install, remove, list, enable, disable, validate, generate keys, and encrypt passwords."
component: web-agents
version: 2026
page_id: web-agents:installation-guide:agentadmin
canonical_url: https://docs.pingidentity.com/web-agents/2026/installation-guide/agentadmin.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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

---

---
title: Apache and IBM HTTP Web Agent
description: Install and configure PingAM Web Agent on Apache HTTP Server and IBM HTTP Server.
component: web-agents
version: 2026
page_id: web-agents:installation-guide:apache
canonical_url: https://docs.pingidentity.com/web-agents/2026/installation-guide/apache.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  install-apache: Install Apache or IBM HTTP Web Agent
  apache-multi-processing: Tune multi-processing modules
  install-apache-interactive: Install interactively
  install-apache-web-agent-vhost: Install on a virtual host
  silent-apache-agent-installation: Install silently
  apache-check-installation: Check the installation
  install_in_a_subrealm: Install in a subrealm
  error-log: Configure error logs
  configure-apache: Configure Apache or IBM HTTP Web Agent
  apache-amagent: AmAgent directive to switch the agent on or off
  example_where_amagent_is_on_globally_and_off_for_specific_directories: Example where AmAgent is On globally and Off for specific directories
  amagent_is_off_globally_and_on_for_specific_server_locations: AmAgent is Off globally and On for specific server locations
  apache-amauthprovider: AmAuthProvider directive to use Apache as the enforcement point
  when_amauthprovider_is_on_and_the_request_doesnt_match_a_not_enforced_rule: When AmAuthProvider is On and the request doesn't match a not-enforced rule
  when_amauthprovider_is_on_and_the_request_matches_a_not_enforced_rule: When AmAuthProvider is On and the request matches a not-enforced rule
  when_amauthprovider_is_on_and_require_amauth_isnt_specified: When AmAuthProvider is On and Require AmAuth isn't specified
  example_where_amauthprovider_is_off_globally_and_on_for_specific_directories: Example where AmAuthProvider is Off globally and On for specific directories
  apache-errordocument: AmAuthErrorDocument directive to authorize ErrorDocument internal redirects
  apache-bypass-preflight: AmBypassPreflightChecks directive to skip preflight permission checks on startup
  configure-apache-server: Apache as a reverse proxy
---

# Apache and IBM HTTP Web Agent

## Install Apache or IBM HTTP Web Agent

Consider the following before installing Apache or IBM HTTP Web Agent:

* SELinux can prevent the web server from accessing agent libraries, and the agent from being able to write to audit and debug logs. Learn more in [Troubleshoot](../maintenance-guide/troubleshooting.html).

* By default, 32 agent instances can run at the same time in a single installation. You can find information about changing the limit in *AM\_MAX\_AGENTS* in [Environment variables](../user-guide/configure-envvars.html).

* (For Apache Web Agent) By default, the agent replaces authentication functionality provided by Apache, for example, the `mod_auth_*` modules. Configure [Use Built-in Apache HTTPD Authentication Directives](../properties-reference/com.forgerock.agents.no.remoteuser.module.compatibility.html) to use built-in Apache authentication directives such as `AuthName`, `FilesMatch`, and `Require` for specified not-enforced URLs.

### Tune multi-processing modules

Apache and IBM HTTP server include Multi-Processing Modules (MPMs) that extend the functionality of a web server to support a wide variety of operating systems and customizations for a site.

Before installation, configure and tune MPMs, as follows:

* Configure one of the following modules:

  * `mpm-event` for Unix-based servers

  * `mpm-worker` for Unix-based servers

  * `mpm_winnt` for Windows servers

  The `prefork-mpm` module isn't adapted to high-traffic deployments. It can cause performance issues to both the agent and AM.

* Make sure that there are enough processes and threads available to service the expected number of client requests.

  MPM-related performance is configured in the file `conf/extra/http-mpm.conf`:

  ```none
  <IfModule mpm_worker_module>
  StartServers            2
  MaxRequestWorkers     150
  MinSpareThreads        25
  MaxSpareThreads        75
  ThreadsPerChild        25
  MaxConnectionsPerChild  0
  </IfModule>
  ```

  `MaxRequestWorkers` and `ThreadsPerChild` control the maximum number of concurrent requests. The default configuration allows 150 concurrent clients across 6 processes of 25 threads each.

  Configure `MaxRequestWorkers` and `ServerLimit` to get a high level of concurrent clients.

  To prevent problems registering the notification queue listener, don't change the default value of `MaxSpareThreads`, `ThreadLimit`, or `ThreadsPerChild`.

  For information about Apache configuration properties, refer to [Apache MPM worker](https://httpd.apache.org/docs/2.4/mod/worker.html).

### Install interactively

1. Review the information in [Before you install](pre-installation.html#before-install) and complete the [pre-installation tasks](pre-installation.html#preinstall-tasks).

2. (Optional) In environments where a user isn't defined in the Apache or IBM HTTP server configuration file `httpd.conf`, set the following environment variables in your command line session to change ownership of created directories.

   The following examples change ownership to the user `user`:

   ```
   $ export APACHE_RUN_USER=user
   $ export APACHE_RUN_GROUP=user
   ```

   Learn more in [Installation environment variables](installer-env-vars.html)

3. Shut down the Apache or IBM HTTP server where you plan to install the agent.

4. Make sure AM is running.

5. Run `agentadmin --i` to install the agent:

   * Apache on Linux

   * Apache on Windows

   * IBM HTTP Server on Linux

   ```
   $ cd /web_agents/apache24_agent/bin/
   $ ./agentadmin --i
   ```

   ```
   C:\> cd web_agents\apache24_agent\bin
   C:\path\to\web_agents\apache24_agent\bin> agentadmin.exe --i
   ```

   ```
   $ cd /web_agents/httpservern_agent/bin/
   $ ./agentadmin --i
   ```

6. When prompted, enter information for your deployment:

   |   |                                                       |
   | - | ----------------------------------------------------- |
   |   | To cancel the installation at any time, press Ctrl+C. |

   1. Enter the complete path to the Apache or IBM HTTP server configuration file:

      * Apache on Linux

      * Apache on Windows

      * IBM HTTP Server on Linux

      ```
      Configuration file [/opt/apache/conf/httpd.conf]: /etc/httpd/conf/httpd.conf
      ```

      ```
      Configuration file [/opt/apache/conf/httpd.conf]: /etc/httpd/conf/httpd.conf
      ```

      ```
      Configuration file [/opt/apache/conf/httpd.conf]: /opt/IBM/HTTPServer/conf/httpd.conf
      ```

   2. (Optional) When installing the agent as the root user, consider changing directory ownership to the same user and group specified in the server configuration:

      ```
      Change ownership of created directories using
      User and Group settings in httpd.conf
      [ q or 'ctrl+c' to exit ]
      (yes/no): [no]: yes
      ```

      This step appears only if environment variables are set as described in step 2, and `User` and `Group` are not defined in `httpd.conf`, such as in non Red Hat Enterprise Linux-based distributions.

      |   |                                                                                                             |
      | - | ----------------------------------------------------------------------------------------------------------- |
      |   | See which user or group is running the server by viewing the `Group` and `User` directives in `httpd.conf`. |

      The following errors can occur when the permissions are wrong:

      * Server fails to start up

      * Requests to a protected resource return a blank page

      * Log rotation errors

   3. Enter the full path to import an existing agent configuration file, or press Enter to skip the import.

      ```
      Existing agent.conf file: path/to/config/agent.conf
      ```

      The installer can import settings from an existing agent on the new installation and skip prompts for values present in the existing configuration file. You must re-enter the agent profile password.

   4. Enter the full URL for the AM instance that the agent will use, including the deployment URI:

      ```
      AM server URL: https://am.example.com:8443/am
      ```

      |   |                                                                                                                                                                                                                                                                                     |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | If a reverse proxy is configured between AM and the agent, set the AM URL to the proxy URL, for example, `https://proxy.example.com:443/am`. You can find information about setting up an environment for reverse proxies in [Apache as a reverse proxy](#configure-apache-server). |

   5. Enter the full URL of the agent:

      ```
      Agent URL: https://agent.example.com:443
      ```

   6. Enter the ID of the agent profile created in AM:

      ```
      Agent ID: web-agent
      ```

   7. Enter the [agent profile realm](../user-guide/glossary.html#def-agent-profile-realm):

      ```
      Agent realm/organization name: [/]:  / 
      ```

      |   |                            |
      | - | -------------------------- |
      |   | Realms are case-sensitive. |

   8. Enter the full path to the file containing the agent password:

      ```
      The path and name of the password file: /secure-directory/pwd.txt
      ```

   9. Review the configuration:

      ```
      Installation parameters:
         AM URL: https://am.example.com:8443/am
         Agent URL: https://agent.example.com:443
         Agent ID: web-agent
         Agent realm/organization name: /
         Agent password source: /secure-directory/pwd.txt

      Confirm configuration (yes/no): [no]:
      ```

   10. Accept or update the configuration:

       * To accept the configuration enter `yes`.

       * To change the configuration enter `no` or press Enter. The installer loops through the configuration prompts again using your provided settings as the default. Press Enter to accept each one or enter a replacement setting.

       On successful completion, the installer adds the agent as a module to the server configuration file `httpd.conf`. The agent adds a backup configuration file with the installation datestamp: `http.conf_amagent_yyyymmddhhmmss`.

7. (Unix only) Make sure the user or group running the Apache or IBM HTTP server has appropriate permissions for the following directories:

   * Apache on Linux

   * Apache on Windows

   * IBM HTTP Server on Linux

   ```
   Read permission:
   * /web_agents/apache24_agent/lib

   Read and write permission:
   * /web_agents/apache24_agent/instances/agent_n
   * /web_agents/apache24_agent/log

   Execute permission to validate an installation by using the agentadmin --V[i\] command:
   * /web_agents/apache24_agent/instances/agent_n
   * /web_agents/apache24_agent/log
   ```

   ```
   Read permission:
   * /web_agents/apache24_agent/lib

   Read and write permission:
   * /web_agents/apache24_agent/instances/agent_n
   * /web_agents/apache24_agent/log

   Execute permission to validate an installation by using the agentadmin --V[i\] command:
   * /web_agents/apache24_agent/instances/agent_n
   * /web_agents/apache24_agent/log
   ```

   ```
   Read permission:
   * /web_agents/httpservern_agent/lib

   Read and write permission:
   * /web_agents/httpservern_agent/instances/agent_n
   * /web_agents/httpservern_agent/log

   Execute permission to validate an installation by using the agentadmin --V[i\] command:
   * /web_agents/httpservern_agent/instances/agent_n
   * /web_agents/httpservern_agent/log
   ```

   |   |                                                                                                             |
   | - | ----------------------------------------------------------------------------------------------------------- |
   |   | See which user or group is running the server by viewing the `Group` and `User` directives in `httpd.conf`. |

   The following errors can occur when the permissions are wrong:

   * Server fails to start up

   * Requests to a protected resource return a blank page

   * Log rotation errors

   |   |                                                                                                                                                                                                        |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | The same issues can occur if SELinux is enabled in `enforcing` mode, and not configured to allow access to agent directories. Learn more in [Troubleshoot](../maintenance-guide/troubleshooting.html). |

8. Start the Apache or IBM HTTP server.

9. Check the installation, as described in [Check the installation](#apache-check-installation).

### Install on a virtual host

Web Agent instances can operate with multiple virtual hosts. Each configuration instance is independent and has its own configuration file, debug logs, and audit logs. Each instance can connect to a different AM realm, or even different AM servers.

Installing on a virtual host is a manual process that involves copying an instance directory created by the `agentadmin` installer and adding it to the configuration file of the virtual host.

1. Install an agent in the default root configuration, as described in [Install Apache or IBM HTTP Web Agent](#install-apache-web-agent). This agent is referred to as the *root agent*.

2. Create a profile for the agent on the virtual host, as described in [Create agent profiles](pre-installation.html#create-agent-profiles). This agent is referred to as the *virtual host agent*.

3. Create at least one AM policy to protect resources on the virtual host, as described in [Policies](https://docs.pingidentity.com/pingam/8.1/am-authorization/policies.html) in AM's *Authorization guide*.

4. Shut down the Apache or IBM HTTP server where you plan to install the agent.

5. Locate an agent configuration instance to duplicate, and make a copy. For example, copy `agent_1` to `agent_2`:

   * Apache on Linux

   * Apache on Windows

   * IBM HTTP Server on Linux

   ```
   $ cd /web_agents/apache24_agent/instances
   $ cp -r agent_1 agent_2
   ```

   ```
   c:\> cd c:\web_agents\apache24_agent\instances
   c:\path\to\web_agents\apache24_agent\instances> xcopy /E /I agent_1 agent_2
   ```

   ```
   $ cd /web_agents/httpservern_agent/instances
   $ cp -r agent_1 agent_2
   ```

6. Assign modify privileges to the new instance folder for the user that runs the virtual host. The following examples assign privileges for `agent_2` to a user named *user*:

   * Apache on Linux

   * Apache on Windows

   * IBM HTTP Server on Linux

   ```
   $ cd /web_agents/apache24_agent/instances
   $ chown -hR user agent_2
   ```

   ```
   c:\> cd c:\web_agents\apache24_agent\instances
   c:\path\to\web_agents\apache24_agent\instances> **icacls "agent_2" /grant user:M
   ```

   ```
   $ cd /web_agents/httpservern_agent/instances
   $ chown -hR user agent_2
   ```

7. In the new instance folder, edit the configuration as follows:

   1. In `agent.conf`, set the value of [Agent Profile Name](../properties-reference/com.sun.identity.agents.config.username.html) to the name of the profile you created for the virtual host agent. For example, set the value to `agent_2`.

   2. In `agent-password.conf` and `agent-key.conf`, configure the encryption key and password for the virtual host agent. Use a scenario that suits your environment:

      * Scenario 1: The password of the virtual host agent profile is the same as the password of the root agent profile\[[1](#_footnotedef_1 "View footnote.")].

        The encryption key and encryption password of the root agent and virtual host agent must match. Because you copied the configuration file, you don't need to do anything else.

      * Scenario 2: The password of the virtual host agent profile is different from the password of the root agent profile\[[2](#_footnotedef_2 "View footnote.")].

        Follow these steps to generate a new encryption key, encrypt the new password, and configure them in the profile of the virtual host agent:

        1. Generate a new encryption key:

           ```
           $ agentadmin --k
           Encryption key value: YWM…​5Nw==
           ```

        2. (Unix only) Store the agent profile password in a file, for example, `newpassword.file`.

        3. Encrypt the agent profile password:

           * Apache on Linux

           * Apache on Windows

           * IBM HTTP Server on Linux

           ```
           $ ./agentadmin --p "YWM…​5Nw==" "cat newpassword.file"
           Encrypted password value: 07b…​dO4=
           ```

           ```
           $ agentadmin.exe --p "YWM…​5Nw==" "newpassword"
           Encrypted password value: 07b…​dO4=
           ```

           ```
           $ ./agentadmin --p "YWM…​5Nw==" "cat newpassword.file"
           Encrypted password value: 07b…​dO4=
           ```

        4. Set the following property in `agent-key.conf`:

      * [Agent Profile Password Encryption Key](../properties-reference/com.sun.identity.agents.config.key.html) with the value of the generated encryption key:

        ```none
        com.sun.identity.agents.config.key = YWM...5Nw==
        ```

        1. Set the following property in `agent-password.conf`:

      * [Agent Profile Password](../properties-reference/com.sun.identity.agents.config.password.html) with the value of the encrypted password:

        ```none
        com.sun.identity.agents.config.password = 07b...dO4=
        ```

   3. Throughout the configuration, replace references to the original instance directory with the new instance directory. For example, replace `agent_1` with `agent_2` in the following properties:

      * [Local Agent Debug File Name](../properties-reference/com.sun.identity.agents.config.local.logfile.html)

      * [Local Agent Audit File Name](../properties-reference/com.sun.identity.agents.config.local.audit.logfile.html)

   4. Throughout the configuration, replace references to the original website being protected with the new website being protected. For example, replace `https://agent.example.com:443/amagent` with `https://customers.example.com:443/amagent` in the following properties:

      * [Agent Deployment URI Prefix](../properties-reference/com.sun.identity.agents.config.agenturi.prefix.html)

      * [FQDN Default](../properties-reference/com.sun.identity.agents.config.fqdn.default.html)

8. Edit the Apache or IBM HTTP server configuration file, `httpd.conf`:

   1. Find the following lines at the end of the file. The following example is for Apache agent on Linux, but you can adapt it to your configuration:

      ```
      LoadModule amagent_module /web_agents/apache24_agent/lib/mod_openam.so
      AmAgent On
      AmAgentConf /web_agents/apache24_agent/bin/../instances/agent_1/config/agent.conf
      ```

   2. Leave the first line, `LoadModule …​`, and move the other two lines on the virtual host configuration element of the default site, for example:

      ```
      <VirtualHost *:80>
      # This first-listed virtual host is also the default for *:80
      ServerName www.example.com
      ServerAlias example.com
      DocumentRoot "/var/www/html"
      AmAgent On
      AmAgentConf /web_agents/apache24_agent/instances/agent_1/config/agent.conf
      </VirtualHost>
      ```

   3. Copy the same two lines on the new virtual host, and replace `agent_1` with the new agent configuration instance folder, for example `agent_2`:

      ```
      <VirtualHost *:80>
      ServerName customers.example.com
      DocumentRoot "/var/www/customers"
      AmAgent On
      AmAgentConf /web_agents/apache24_agent/instances/agent_2/config/agent.conf
      </VirtualHost>
      ```

      |   |                                                                                                                                              |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | If the new virtual host configuration is in a separate file, copy the two configuration lines on the `VirtualHost` element within that file. |

9. Save and close the configuration file.

10. (Unix only) Make sure the user or group running the Apache or IBM HTTP server has appropriate permissions for the following directories:

    * Apache on Linux

    * Apache on Windows

    * IBM HTTP Server on Linux

    ```
    Read permission:
    * /web_agents/apache24_agent/lib

    Read and write permission:
    * /web_agents/apache24_agent/instances/agent_n
    * /web_agents/apache24_agent/log

    Execute permission to validate an installation by using the agentadmin --V[i\] command:
    * /web_agents/apache24_agent/instances/agent_n
    * /web_agents/apache24_agent/log
    ```

    ```
    Read permission:
    * /web_agents/apache24_agent/lib

    Read and write permission:
    * /web_agents/apache24_agent/instances/agent_n
    * /web_agents/apache24_agent/log

    Execute permission to validate an installation by using the agentadmin --V[i\] command:
    * /web_agents/apache24_agent/instances/agent_n
    * /web_agents/apache24_agent/log
    ```

    ```
    Read permission:
    * /web_agents/httpservern_agent/lib

    Read and write permission:
    * /web_agents/httpservern_agent/instances/agent_n
    * /web_agents/httpservern_agent/log

    Execute permission to validate an installation by using the agentadmin --V[i\] command:
    * /web_agents/httpservern_agent/instances/agent_n
    * /web_agents/httpservern_agent/log
    ```

    |   |                                                                                                             |
    | - | ----------------------------------------------------------------------------------------------------------- |
    |   | See which user or group is running the server by viewing the `Group` and `User` directives in `httpd.conf`. |

    The following errors can occur when the permissions are wrong:

    * Server fails to start up

    * Requests to a protected resource return a blank page

    * Log rotation errors

    |   |                                                                                                                                                                                                        |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    |   | The same issues can occur if SELinux is enabled in `enforcing` mode, and not configured to allow access to agent directories. Learn more in [Troubleshoot](../maintenance-guide/troubleshooting.html). |

11. Start the Apache or IBM HTTP server.

12. Check the installation, as described in [Check the installation](#apache-check-installation).

### Install silently

Use the `agentadmin --s` command for silent installation. Learn more in [agentadmin command](agentadmin.html).

1. Review the information in [Before you install](pre-installation.html#before-install) and complete the [pre-installation tasks](pre-installation.html#preinstall-tasks).

2. Shut down the Apache or IBM HTTP server where you plan to install the agent.

3. Make sure AM is running.

4. Run the `agentadmin --s` command with the required arguments. The following example is for Apache agent on Linux, but you can adapt it to your configuration:

   ```
   $ ./agentadmin --s \
     "/etc/httpd/conf/httpd.conf" \
     "https://am.example.com:8443/am" \
     "https://agent.example.com:443" \
     "/" \
     "webagent" \
     "/secure-directory/pwd.txt" \
     --changeOwner
   AM Web Agent for Apache Server installation.
   …​
   Installation complete.
   ```

5. (Unix only) Make sure the user or group running the Apache or IBM HTTP server has appropriate permissions for the following directories:

   * Apache on Linux

   * Apache on Windows

   * IBM HTTP Server on Linux

   ```
   Read permission:
   * /web_agents/apache24_agent/lib

   Read and write permission:
   * /web_agents/apache24_agent/instances/agent_n
   * /web_agents/apache24_agent/log

   Execute permission to validate an installation by using the agentadmin --V[i\] command:
   * /web_agents/apache24_agent/instances/agent_n
   * /web_agents/apache24_agent/log
   ```

   ```
   Read permission:
   * /web_agents/apache24_agent/lib

   Read and write permission:
   * /web_agents/apache24_agent/instances/agent_n
   * /web_agents/apache24_agent/log

   Execute permission to validate an installation by using the agentadmin --V[i\] command:
   * /web_agents/apache24_agent/instances/agent_n
   * /web_agents/apache24_agent/log
   ```

   ```
   Read permission:
   * /web_agents/httpservern_agent/lib

   Read and write permission:
   * /web_agents/httpservern_agent/instances/agent_n
   * /web_agents/httpservern_agent/log

   Execute permission to validate an installation by using the agentadmin --V[i\] command:
   * /web_agents/httpservern_agent/instances/agent_n
   * /web_agents/httpservern_agent/log
   ```

   |   |                                                                                                             |
   | - | ----------------------------------------------------------------------------------------------------------- |
   |   | See which user or group is running the server by viewing the `Group` and `User` directives in `httpd.conf`. |

   The following errors can occur when the permissions are wrong:

   * Server fails to start up

   * Requests to a protected resource return a blank page

   * Log rotation errors

   |   |                                                                                                                                                                                                        |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | The same issues can occur if SELinux is enabled in `enforcing` mode, and not configured to allow access to agent directories. Learn more in [Troubleshoot](../maintenance-guide/troubleshooting.html). |

6. Start the Apache or IBM HTTP server.

7. Check the installation, as described in [Check the installation](#apache-check-installation).

### Check the installation

1. After you start Apache or IBM HTTP server, check the error log to make sure startup was successful:

   ```
   [Tue Sep …​] AH00163:
   Apache/2.4.6 (CentOS) Web Agent/2026.6 configured — resuming normal operations
   ```

2. Make an HTTP request to a resource protected by the agent, then check the `/log/system_0.log` file to verify that no errors occurred on startup. The log should contain a message similar to this:

   ```
   [0x7fb89e7a6700:22]: Web Agent Version: 2026.6
   Revision: ab12cde, Container: Apache 2.4 Linux 64bit (Centos6),
   Build date: Mar …​
   ```

3. (Optional) If an AM policy is configured, test that the agent enforces a policy decision. For example, make an HTTP request to a protected resource and check that you are redirected to AM to authenticate. After authentication, AM redirects you back to the resource you tried to access.

### Install in a subrealm

Examples in this document install the agent in the top-level realm. To install the agent in a subrealm during interactive or silent installation, use the subrealm during the installation or in the response file.

For example, instead of:

```bash
Agent realm/organization name: [/]: /
```

specify:

```bash
Agent realm/organization name: [/]: /myrealm
```

Even though the agent is installed in a subrealm, the default login redirect requires the [user realm](../user-guide/glossary.html#def-user-realm) to be the top-level realm. You can find information about changing the user realm in [Login redirect](../user-guide/login-redirect.html).

### Configure error logs

Edit the server configuration file `httpd.conf` to log errors.

The following line, present by default in `httpd.conf`, logs warning conditions for the container:

```none
LogLevel warn
```

The following example line includes the agent error logs at debug-level:

```none
LogLevel warn amagent:debug
```

## Configure Apache or IBM HTTP Web Agent

The examples in this section are for Apache agent on Linux, but you can adapt them to your configuration.

|   |                                                                               |
| - | ----------------------------------------------------------------------------- |
|   | IBM HTTP server 9 supports Apache directives but IBM HTTP server 8.5 doesn't. |

### `AmAgent` directive to switch the agent on or off

Switch the agent on or off globally or independently for different server locations. Server locations include the global environment, a virtual host, a specific location, or a set of directory blocks. Use the following settings:

* `AmAgent On`

  The agent protects server locations. It allows or denies requests based on AM policy configuration and not-enforced rules.

* `AmAgent Off`

  Apache or IBM HTTP server protects server locations; the agent plays no part in protecting the server locations.

Default: `AmAgent` is set to `On` at a global level in the `httpd.conf` configuration file as follows:

```
AmAgent On
AmAgentConf /opt/web_agents/apache24_agent/instances/agent_1/config/agent.conf
AmAuthProvider Off
```

The `AmAgent` configuration is hierarchical. When it's `On` or `Off` globally it's set for all server locations except those explicitly specified otherwise.

|   |                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Consider setting `AmAgent` to `Off` for the following situations:- For server locations that need no AM authentication or policy, such as the public face of a website, or `/css` or `/images` directories.

- When Apache or IBM HTTP server is acting as a reverse proxy to AM or Advanced Identity Cloud, and you don't want the agent to take part in protecting AM or Advanced Identity Cloud. |

#### Example where `AmAgent` is `On` globally and `Off` for specific directories

In the following example `httpd.conf`, the agent is `On` globally and `Off` for the `/var/www/transaction` directory:

```
<Directory /var/www/>
    Options Indexes FollowSymLinks
    AllowOverride None
    Require all granted
</Directory>

<Directory /var/www/transaction>
    AmAgent Off
    Options Indexes FollowSymLinks
    AllowOverride None
    Require all granted
</Directory>

AmAgent On
AmAgentConf /opt/web_agents/apache24_agent/instances/agent_1/config/agent.conf
AmAuthProvider Off
```

* Accessing a resource in `/var/www/`

  The agent protects the resource, and overrides the `Require all granted` directive.

  To access the resource, the request must match a not-enforced rule in the agent configuration or be allowed by an AM policy evaluation.

* Accessing a resource in `/var/www/transaction`

  Apache or IBM HTTP server manages the access and applies the `Require all granted` directive. The agent plays no part in protecting the resource.

#### `AmAgent` is `Off` globally and `On` for specific server locations

|   |                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When `AmAgent` configuration is `Off`, configure the server location `/agent` as `On`. This allows AM to redirect requests to the `/agent` endpoint after authentication. |

In the following example `httpd.conf`, the agent is `Off` globally but `On` for the `/var/www/transaction` and `/agent` locations:

```
<Directory /var/www/>
    Options Indexes FollowSymLinks
    AllowOverride None
    Require all granted
</Directory>

<Directory /var/www/transaction>
    AmAgent On
    Options Indexes FollowSymLinks
    AllowOverride None
    Require all granted
</Directory>

<Location /agent>
    AmAgent On
</Location>

AmAgent Off
AmAgentConf /opt/web_agents/apache24_agent/instances/agent_1/config/agent.conf
AmAuthProvider Off
```

* Accessing a resource in `/var/www/`

  Apache or IBM HTTP server manages the access and applies the `Require all granted` directive. The agent plays no part in protecting the resource.

* Accessing a resource in `/var/www/transaction`

  The agent protects the resource, and overrides the `Require all granted` directive.

  To access the resource, the request must match a not-enforced rule in the agent configuration or be allowed by an AM policy evaluation.

### `AmAuthProvider` directive to use Apache as the enforcement point

When `AmAgent` is `On`, combine AM policy with Apache `Require` directives to control access globally or independently for different server locations. Server locations include the global environment, a virtual host, a specific location, or a set of directory blocks.

|   |                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Using multiple authorization sources increases complexity. To reduce the risk of an invalid security configuration, test and validate the directives. |

Use the following settings:

* `AmAuthProvider Off`

  The agent acts as the enforcement point, allowing or denying requests based on not-enforced rules and AM policies.

* `AmAuthProvider On`

  Apache or IBM HTTP server acts as the enforcement point, allowing or denying requests based on AM policy and Apache `Require` directives

  For information about `Require` directives, refer to [Require Directive](https://httpd.apache.org/docs/2.4/mod/mod_authz_core.html#require) on the Apache website. `Require AmAuth` is a directive specifically for Web Agent. When the directive is specified, users must be authenticated with AM. Otherwise, the agent redirects them to AM for authentication.

Default: `AmAuthProvider` is `Off`

The `AmAuthProvider` configuration is hierarchical. When it's `On` or `Off` globally it's set for all server locations except those explicitly specified otherwise.

For simplicity, it's recommended to leave `AmAuthProvider` as `Off` globally and set it to `On` for specific locations where you want Apache to act as the enforcement point.

#### When `AmAuthProvider` is `On` and the request doesn't match a not-enforced rule

When a request doesn't match a not-enforced rule, the agent does the following:

* Checks that the user is authenticated with AM, and redirects the user for authentication if not.

* Requests policy information from AM for the request.

* Relays the policy information to the Apache `Require AmAuth` directive.

Apache or IBM HTTP server uses the `Require AmAuth` directive and other `Require` directives to allow or deny access to resources.

The following image shows the flow of requests:

![Flow of a request when \`AmAuthProvider\` is \`On\` and a request doesn't match a not-enforced rule in the agent configuration.](_images/directives.svg)

#### When `AmAuthProvider` is `On` and the request matches a not-enforced rule

When a request matches a not-enforced rule, the agent doesn't require the user to be authenticated with AM or request policy information from AM. The `Require AmAuth` directive returns a neutral value.

Apache or IBM HTTP server uses the other `Require` directives to allow or deny access to resources.

The following image shows the flow of requests:

![Flow of a request when \`AmAuthProvider\` is \`On\` and a request matches a not-enforced rule in the agent configuration.](_images/directives-nenf-match.svg)

Consider the following for using not-enforced rules when `AmAuthProvider` is `On`:

* Instead of using not-enforced rules to provide caveats to AM policy enforcement, use Apache `Require` directives.

* In server locations where the agent is configured with not-enforced rules, set `AmAuthProvider` to `Off` to let the agent do the enforcement.

* If you use not-enforced rules when `AmAuthProvider` is `On`, remember that the agent drops out of authorisation decisions for requests that match a rule. Apache `Require` directives are used to allow or deny requests.

#### When `AmAuthProvider` is `On` and `Require AmAuth` isn't specified

When `AmAuthProvider` is `On`, the `Require AmAuth` directive should always be specified. If `AmAuthProvider` is `On`, but the `Require AmAuth` directive isn't specified, users are still required to authenticate with AM but Apache doesn't use policy information from AM in its decision.

The following image shows the flow of requests:

![Flow of a request when \`AmAuthProvider\` is \`On\` and \`Require AmAuth\` directive is not specified.](_images/directives-no-amauth.svg)

The following example has this configuration:

* The request doesn't match a not-enforced rule.

* `AmAuthProvider` is `On` for the `/var/www/transaction` directory.

* `Require AmAuth` isn't specified

```
//Not a recommended configuration

<Directory /var/www/>
    Options Indexes FollowSymLinks
    AllowOverride None
    Require all granted
</Directory>

<Directory /var/www/transaction>
    AmAuthProvider On
    Options Indexes FollowSymLinks
    AllowOverride None
    <RequireAll>
        Require ip 19.168.2
    </RequireAll>
</Directory>

AmAgent On
AmAgentConf /opt/web_agents/apache24_agent/instances/agent_1/config/agent.conf
AmAuthProvider Off
```

* Accessing a resource in `/var/www/transaction`

  Apache or IBM HTTP server uses the `Require ip` directive to allow or deny the request. The user must be authenticated with AM and a valid user must be set, but AM policy information is ignored.

#### Example where `AmAuthProvider` is `Off` globally and `On` for specific directories

The example is configured as follows:

* The request doesn't match a not-enforced rule

* `AmAuthProvider` is `Off` globally

* `AmAuthProvider` is `On` for the `/var/www/transaction` directory:

* `Require AmAuth` is specified

```
<Directory /var/www/>
    Options Indexes FollowSymLinks
    AllowOverride None
    Require all granted
</Directory>

<Directory /var/www/transaction>
    AmAuthProvider On
    Options Indexes FollowSymLinks
    AllowOverride None
    <RequireAll>
        Require AmAuth
        Require ip 19.168.2
    </RequireAll>
</Directory>

AmAgent On
AmAgentConf /opt/web_agents/apache24_agent/instances/agent_1/config/agent.conf
AmAuthProvider Off
```

* Accessing a resource in `/var/www/`

  The agent acts as the enforcement point, allowing or denying requests based on not-enforced rules and AM policies.

* Accessing a resource in `/var/www/transaction`

  The agent provides AM policy information to the `Require AmAuth` directive. Apache uses that and the `Require ip` directive to allow or deny the request.

  To access the resource, the user must be authenticated with AM, and the request must meet AM policy requirements and come from the specified IP address.

### `AmAuthErrorDocument` directive to authorize ErrorDocument internal redirects

Switch authorization on or off for ErrorDocument internal file or CGI redirects either at the Server or VirtualHost level, or at the Directory level.

|   |                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------- |
|   | This setting doesn't apply to external redirects or simple text based responses for the ErrorDocument directive. |

Use the following settings:

* `AmAuthErrorDocument On`

  The agent performs authorization on ErrorDocument internal file or CGI redirects.

  Use this setting when you have ErrorDocuments that use CGI scripts and require authorization. For example:

  ```
  ErrorDocument 400 /cgi/bin/cgi-error-script
  ```

  When this directive is set to `On`, it lets the CGI script read user attributes from headers or cookies to make decisions.

  For example, if a user attempts to access a page they're not authorized to access, the CGI helper can allow them to request access to that page.

  The CGI script must be in an AM policy to be authorized. If a policy denies access to the CGI script, Apache displays a default error response page and informs you that an error occurred while trying to display the custom response.

* `AmAuthErrorDocument Off`

  The ErrorDocument internal redirects are allowed and the agent doesn't perform any authorization.

Default: `AmAuthErrorDocument` is `Off`.

The `AmAuthErrorDocument` configuration is hierarchical. When it's `On` or `Off` at the Server level, it's set for all server locations except those explicitly specified otherwise.

If authorization is needed for ErrorDocument internal redirects, the simplest configuration is to set `AmAuthErrorDocument` to `On` at the Server level.

### `AmBypassPreflightChecks` directive to skip preflight permission checks on startup

Controls whether the Web Agent runs preflight permission checks on startup.

Use the following settings:

* `AmBypassPreflightChecks Off`

  The agent runs preflight permission checks on startup. If the Apache user doesn't have the required access to agent directories, Apache fails to start and the agent logs errors similar to the following in the Apache logs:

  ```bash
  [amagent:error] validate_necessary_file_permissions: FATAL startup error: no access to /opt/web_agents/apache24_agent/lib/../log error: 13 (Permission denied)
  [amagent:error] validate_necessary_file_permissions: [ACTION] Please ensure that the user: [www-data (uid:33)] has access to: /opt/web_agents/apache24_agent/lib/../log/
  [amagent:error] amagent_init_servers server: 127.0.1.1:0 FAILED Agent Preflight validation, result: (13) Permission denied
  [:emerg] AH00020: Configuration Failed, exiting
  ```

* `AmBypassPreflightChecks On`

  The agent skips the preflight checks on startup and logs the following warning in the Apache logs:

  ```bash
  [amagent:warn] amagent_validate_server_agent_config: server: 127.0.1.1:0 AmBypassPreflightChecks is ON, preflight checks bypassed per configuration
  ```

  Use this setting only if you need to bypass the checks temporarily, for example to diagnose a startup problem. Leaving preflight checks bypassed means permission errors won't be caught on startup and can be harder to diagnose later.

Default: `AmBypassPreflightChecks` is `Off`.

### Apache as a reverse proxy

This section has an example configuration of Apache HTTP Server as a reverse proxy between AM and Web Agent. You can use any reverse proxy that supports the WebSocket protocol.

For information about how to configure Apache for load balancing, and other requirements for your environment, refer to the Apache documentation.

![Simplified diagram showing an Apache HTTP Server configured as a reverse proxy between AM and the agent.](_images/apache-proxy.svg)Figure 1. Apache HTTP Server reverse proxy configured between the agent and AM

1. Locate the `httpd.conf` file in your deployed reverse proxy instance.

2. Add the modules required for a proxy configuration, as follows:

   ```bash
   # Modules required for proxy
   LoadModule proxy_module modules/mod_proxy.so
   LoadModule proxy_http_module modules/mod_proxy_http.so
   LoadModule proxy_wstunnel_module modules/mod_proxy_wstunnel.so
   ```

   The `mod_proxy_wstunnel.so` module is required to support the WebSocket protocol used for communication between AM and the agents.

3. Add the proxy configuration inside the `VirtualHost` context. Consider the following directives:

   ```bash
   <VirtualHost 192.168.1.1>
   ...
   # Proxy Config
   RequestHeader set X-Forwarded-Proto "https" (1)
   ProxyPass "/am/notifications" "ws://am.example.com:8080/am/notifications" Upgrade=websocket (2)
   ProxyPass "/am" "http://am.example.com:8080/am" (3)
   ProxyPassReverseCookieDomain "am.internal.example.com" "proxy.example.com" (4)
   ProxyPassReverse "/am" "http://am.example.com:8080/am" (5)
   ...
   </VirtualHost>
   ```

   (1) RequestHeader: Set to `https` or `http`, depending on the proxy configuration. If the proxy is configured for https, as in the above example, set to `https`. Otherwise, set `http`. In a later step, you configure AM to recognize the forwarded header and use it in the `goto` parameter for redirecting back to the agent after authentication.

   (2) ProxyPass: Set to allow WebSocket traffic between AM and the agent. If HTTPS is configured between the proxy and AM, set to use the `wss` protocol instead of `ws`.

   (3) ProxyPass: Set to allow HTTP traffic between AM and the agent.

   (4) ProxyPassReverseCookieDomain: Set to rewrite the domain string in \`Set-Cookie\`headers in the format *internal domain* (AM's domain) *public domain* (proxy's domain).

   (5) ProxyPassReverse: Set to the same value configured for the `ProxyPass` directive.

   For more information about configuring Apache HTTP Server as a reverse proxy, refer to the [Apache documentation](https://httpd.apache.org/docs/2.4/howto/reverse_proxy.html).

4. Restart the reverse proxy instance.

5. Configure AM to recover the forwarded header you configured in the reverse proxy. Also, review other configurations that may be required in an environment that uses reverse proxies. Learn more in [Agent connection to AM through a load balancer/reverse proxy](../user-guide/load-balancers-proxies.html#comms-am-agents)

***

[1](#_footnoteref_1). The root agent profile refers to the agent installation performed in [Install Apache or IBM HTTP Web Agent](#install-apache-web-agent) and required for installation on virtual hosts.[2](#_footnoteref_2). The root agent profile refers to the agent installation performed in [Install Apache or IBM HTTP Web Agent](#install-apache-web-agent) and required for installation on virtual hosts.

---

---
title: Deploy Web Agent with Docker
description: Deploy PingAM Web Agent in a Docker container using a Dockerfile example, including build arguments, upgrade, and rollback steps.
component: web-agents
version: 2026
page_id: web-agents:installation-guide:docker
canonical_url: https://docs.pingidentity.com/web-agents/2026/installation-guide/docker.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  deploy_apache_web_agent_example: Deploy Apache Web Agent example
  upgrade_and_rollback: Upgrade and rollback
---

# Deploy Web Agent with Docker

The example in this section provides a Dockerfile and instructions to deploy Apache Web Agent to extend and protect an application. Adapt the information for other agent containers.

Consider the following limitations:

* The Dockerfile doesn't manage logs, so agent logs are lost when the Docker container is killed. Manage logs independently of the Dockerfile in the following ways, according to your environment:

  * Store logs persistently to a volume

  * Store logs to a host machine

  * Tail logs into STDOUT or STDERR so that Docker can collect the data

* The Dockerfile isn't suitable for local configuration mode and doesn't update bootstrap properties. The agent must be configured to operate in the default [Centralized configuration](../user-guide/about.html#configuration-location) mode. Learn more in [Location of Agent Configuration Repository](../properties-reference/com.sun.identity.agents.config.repository.location.html).

## Deploy Apache Web Agent example

1. Build a Docker image of your application. This example uses a sample application called `fr-sample-app:1.0`.

2. In Advanced Identity Cloud or AM, set up an agent profile and policy. For more information, refer to Advanced Identity Cloud's [Prepare for installation](../identity-cloud-guide/installation.html#pre-installation) or AM's [Prepare for installation](pre-installation.html).

   This example uses the following configuration:

   * AM URL: `https://am.example.com:8443/am`

   * AM realm: `/`

   * Agent URL: `https://agent.example.com:443`

   * Agent profile name: `web-agent`

   * Agent profile password: `password`

   * Policy set and policy: Allow HTTP `GET` and `POST` for all authenticated users.

3. Create a local folder for the agent .zip file, the Dockerfile, and the agent profile password—they must be in the same folder. This example uses `/path/to/docker`.

4. Download the agent .zip file to the local folder.

5. Create a file containing the agent profile password. The filename in this example is `agent_secret` and the password is `password`.

   ```bash
   /path/to/docker$ cat > agent_secret
   password
   CTRL+D 
   ```

   |   |                                                                                                                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Although the agent accepts any password length and content, you are strongly encouraged to generate secure passwords. This can be achieved in various ways, for example, by using a password manager. |

6. Create the following Dockerfile in `/path/to/docker/Dockerfile`. Arguments are provided by the build command.

   ```txt
   # Application Docker image
   ARG BASE_DOCKER_IMAGE
   FROM ${BASE_DOCKER_IMAGE}

   # Install and unzip the application, required for unpacking the agent build.
   # Not required if the base image is already unzipped.
   # For non-Debian Linux distributions, use the appropriate package manager.
   RUN apt-get update && \
   	apt-get install unzip --no-install-recommends -y && \
   	apt-get clean

   # Define the build arguments.
   # Arguments without default values must be specified in the build command.
   ARG AGENT_VERSION
   ARG AGENT_ZIP_FILE=web-agent-${AGENT_VERSION}-Apache_v24_Linux_x86_64.zip
   ARG AGENT_HOME=/opt
   ARG AM_URL
   ARG APACHE_CONF=/usr/local/apache2/conf/httpd.conf
   ARG AGENT_URL=http://agent.dummy.url:80
   ARG AGENT_REALM=/
   ARG AGENT_PROFILE

   # Copy the agent .zip file to the Docker directory where the agent is installed.
   COPY ${AGENT_ZIP_FILE} ${AGENT_HOME}/${AGENT_ZIP_FILE}

   # Unzip the agent and delete the .zip file
   RUN cd ${AGENT_HOME} && \
   	unzip ./${AGENT_ZIP_FILE} && \
   	rm -rf ./${AGENT_ZIP_FILE}

   # Install the agent and mount the file containing the agent password
   RUN --mount=type=secret,id=agent_secret,required=true \
   	"${AGENT_HOME}"/web_agents/apache24_agent/bin/agentadmin --s \
   	"${APACHE_CONF}" \
   	"${AM_URL}" \
   	"${AGENT_URL}" \
   	"${AGENT_REALM}" \
   	"${AGENT_PROFILE}" \
   	"/run/secrets/agent_secret" \
   	--changeOwner \
   	--forceInstall
   ```

7. Find values for the following arguments that correspond to your application and environment:

   * `agent_secret`: The name of the file containing the agent profile password.

   * `BASE_DOCKER_IMAGE`: The name and path to the base image of your application.

   * `AGENT_VERSION`: The agent version in the Docker image.

   * `AGENT_ZIP_FILE`: Name of the agent .zip file. Default: Derived from `AGENT_VERSION`.

   * `AGENT_HOME`: Docker directory where the agent is installed. Default: `/opt`.

   * `AM_URL`: Advanced Identity Cloud or AM server URL including port number.

   * `AGENT_URL`: Agent URL. Default: `http://agent.dummy.url:80`.

   * `APACHE_CONF`: Path to the Apache server configuration. Default: `/usr/local/apache2/conf/httpd.conf`.

   * `AGENT_REALM`: Advanced Identity Cloud or AM realm containing the agent profile.

   * `AGENT_PROFILE`: Agent profile name. Default `/`.

8. With a Docker daemon running, build the Docker image with the following command, replacing the example values with your own values:

   ```bash
   /path/to/docker$ docker build --secret id=agent_secret \
     --build-arg BASE_DOCKER_IMAGE=fr-sample-app:1.0 \
     --build-arg AGENT_VERSION=2026.6 \
     --build-arg AGENT_ZIP_FILE=web-agent-2026.6-Apache_v24_Linux_x86_64.zip \
     --build-arg AGENT_HOME=/opt \
     --build-arg AM_URL=https://am.example.com:8443/am \
     --build-arg AGENT_URL=https://agent.example.com:443 \
     --build-arg APACHE_CONF=/etc/httpd/conf/httpd.conf \
     --build-arg AGENT_REALM=/ \
     --build-arg AGENT_PROFILE=web-agent \
     --tag agent-image:2026.6 .

   ...
    => => writing image sha256:803...ada  0.0s
    => => naming to docker.io/library/web-agent:2026.6
   ```

9. Run the container:

   ```bash
   /path/to/docker$ docker run -it --name apache24-agent -p 80:80 web-agent:2026.6

   ... Apache/2.4.58 (Unix) AM Web Agent/2026.6 configured -- resuming normal operations
   ... Command line: 'httpd -D FOREGROUND'
   ```

10. Access your application through the agent at `https://agent.example.com:443`. Access is managed by Advanced Identity Cloud or AM according to the policy configured for the agent profile.

    This example displays the Advanced Identity Cloud or AM login in page. When you log in as a user, you access the sample application.

## Upgrade and rollback

To upgrade or roll back an agent Docker container to a different agent version:

1. Build a new Docker container with the different agent version, using a tag name that corresponds to the version.

2. Replace the Docker image tag in your environment.

---

---
title: IIS and ISAPI Web Agent
description: Install, configure, enable, and disable PingAM Web Agent on IIS and ISAPI, including basic authentication, password replay, and child application protection.
component: web-agents
version: 2026
page_id: web-agents:installation-guide:install-iis
canonical_url: https://docs.pingidentity.com/web-agents/2026/installation-guide/install-iis.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  install-iis-web-agent: Install IIS or ISAPI Web Agent interactively
  silent-iis-agent-installation: Install IIS or ISAPI Web Agent silently
  manage-iis-agents: Enable and disable IIS Web Agent
  proc-enable-disable-iis-web-policy-agent: Disable and enable Web Agent on an IIS site or application
  proc-disabling-enabling-child-protection: Disable and enable agent protection for child applications
  iis-enable-basic-auth: Enable support for basic authentication and password replay
  microsoft_issues: Microsoft issues
  configure-iis-basic-auth: Configure basic authentication and password replay support
  install_in_a_subrealm: Install in a subrealm
---

# IIS and ISAPI Web Agent

IIS and ISAPI Web Agent instances can be configured to operate with multiple websites. Each configuration instance is independent and has its own configuration file, debug logs, and audit logs. Each instance can connect to a different AM realm, or even different AM servers.

Consider the following for IIS and ISAPI Web Agent:

* IIS agents must run in Integrated mode.

* IIS and ISAPI agents can't run in the same Windows Server instance.

* ISAPI agent handles the POST method for form data but not for other data types.

* An agent configured for a site or parent application protects any application configured in the site or parent application.

* A protected application configured for a site or parent application protects any application configured in the site or parent application.

* Agents configured in a site or parent application protect only the child applications that inherit their parent IIS or ISAPI configuration.

* Because of architectural differences, agents configured for a site or parent application running in a 64-bit pool *don't* protect child applications running in a 32-bit pool. 32-bit applications can't load 64-bit web agent libraries.

  Similarly, agents configured for a site or parent application running in a 32-bit pool *don't* protect child applications running in a 64-bit pool.

  In this case, child applications require their own agent installation, as explained in the next item of this list. Both 32-bit and 64-bit agent libraries are supplied with the IIS and ISAPI Web Agent binaries.

* If an application requires a specific agent configuration or, for example, the application is a 32-bit application configured within a 64-bit site, follow the procedures in this section to create a new agent instance for it. Configuring an agent on an application overrides the application's parent web agent configuration, if any.

  |   |                                                                                                                                                                 |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Install Web Agent on the child application before installing it in the parent. Trying to install an agent on a child that is already protected causes an error. |

* (IIS agent) You can disable the agent protection at any level of the IIS hierarchy, with the following constraints:

  * Disabling the agent in a parent application disables protection on all child applications that don't have a specific agent instance installed on them.

  * Disabling the agent in a child application doesn't disable protection on its parent application.

* (ISAPI agent) You can't disable the agent protection. ISAPI agent is either installed and running or not installed.

* Agents require the *Application Development* component to be installed alongside the core IIS or ISAPI services. Application Development is an optional component of the IIS and ISAPI web server. The component provides required infrastructure for hosting web applications.

  ![Web agents require that the Application Development component is installed alongside the core IIS services.](_images/iis-application-development-role.png)Figure 1. Adding the application development component to IIS and ISAPI

* The following properties don't work with ISAPI agent:

  * [Ignore Path Info in Request URLs](../properties-reference/com.sun.identity.agents.config.ignore.path.info.html)

  * [Authorization flow for applications using Javascript](../properties-reference/com.forgerock.agents.config.auth.flow.callback.html)

## Install IIS or ISAPI Web Agent interactively

|   |                                                                                                                                                                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The IIS Web Agent installer doesn't support custom namespace elements in the `web.config` file. If any exist, they're removed from the `web.config` file during the installation process.If you require custom namespace elements, back up the `web.config` file before installing the agent and manually restore them once the agent is installed. |

1. Review the information in [Before you install](pre-installation.html#before-install) and complete the [pre-installation tasks](pre-installation.html#preinstall-tasks).

2. Log on to Windows as a user with administrator privileges.

3. Make sure AM is running.

4. Run the [agentadmin --i](agentadmin.html) command to install the agent.

   ```
   c:\> cd web_agents\iis_agent\bin
   c:\web_agents\iis_agent\bin> agentadmin.exe --i
   ```

5. When prompted, enter information for your deployment.

   |   |                                                       |
   | - | ----------------------------------------------------- |
   |   | To cancel the installation at any time, press Ctrl+C. |

   1. Choose the site and application in which to install the web agent.

      The `agentadmin` command reads the IIS or ISAPI server configuration and converts hierarchy as follows:

      * (ISAPI agent) Into a single value ID.

      * (IIS agent) Into an ID composed of three values separated by the dot (`.`) character:

        The first value specifies an IIS site. The number `1` specifies the first site in the server.

        The second value specifies an application configured in an IIS site. The number `1` specifies the first application in the site.

        The third value specifies an internal value for the web agent.

        The following is an example IIS server configuration read by the `agentadmin` command:

        ```
        IIS Server Site configuration:
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
        2.2.1    virtualDirectory path:/  configuration C:\inetpub\MySite\MyApp1\web.config
                 application path:/MyApp1/MyApp2, pool: MySite
        2.3.1    virtualDirectory path:/  configuration C:\inetpub\MySite\MyApp1\MyApp2\web.config

        Enter IIS Server Site identification number.
        [ q or 'ctrl+c' to exit ]
        Site id: 2.1.1
        ```

        * ID `2.1.1` corresponds to the first application, `/` configured in a second IIS site, `MySite`. You would choose this ID to install the web agent at the root of the site.

        * ID `2.2.1` corresponds to a second application, `MyApp1`, configured in a second IIS site, `MySite`. You would choose this ID to install the web agent in the `MyApp1` application.

        * ID `2.3.1` corresponds to a child application, `MyApp1/MyApp2`, configured in the second application, `MyApp1`, configured in a second IIS site, `MySite`. You would choose this ID to install the web agent in the sub-application, `MyApp1/MyApp2`.

   2. The installer can import settings from an existing web agent on the new installation and skips prompts for any values present in the existing configuration file. You will be required to re-enter the agent profile password.

      Enter the full path to an existing agent configuration file to import the settings, or press Enter to skip the import.

      ```
      To set properties from an existing configuration enter path to file
      [ q or 'ctrl+c' to exit, return to ignore ]
      Existing agent.conf file:
      ```

   3. Enter the full URL of the AM instance the agent will use. Make sure the deployment URI is specified.

      |   |                                                                                                                                                                                                                                                                                                |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | If a reverse proxy is configured between AM and the agent, set the AM URL to the proxy URL, for example, `https://proxy.example.com:443/am`. You can find information about setting up an environment for reverse proxies in [Apache as a reverse proxy](apache.html#configure-apache-server). |

      ```
      Enter the URL where the AM server is running. Please include the
      deployment URI also as shown below:
      (http://am.sample.com:58080/am)
      [ q or 'ctrl+c' to exit ]
      AM server URL: https://am.example.com:8443/am
      ```

   4. Enter the full URL of the site the agent will run in.

      ```
      Enter the Agent URL as shown below:
      (http://agent.sample.com:1234)
      [ q or 'ctrl+c' to exit ]
      Agent URL: http://customers.example.com:80
      ```

   5. Enter the name given to the agent profile created in AM.

      ```
      Enter the Agent profile name
      [ q or 'ctrl+c' to exit ]
      Agent Profile name: iisagent
      ```

   6. Enter the [agent profile realm](../user-guide/glossary.html#def-agent-profile-realm). Realms are case-sensitive.

      ```
      Enter the Agent realm/organization
      [ q or 'ctrl+c' to exit ]
      Agent realm/organization name: [/]: /
      ```

   7. Enter the full path to the file containing the agent profile password created earlier.

      ```
      Enter the path to a file that contains the password to be used
      for identifying the Agent
      [ q or 'ctrl+c' to exit ]
      The path to the password file: c:\pwd.txt
      ```

   8. The installer displays a summary of the configuration settings you specified.

      If a setting is incorrect, enter `no` or press Enter. The installer loops through the configuration prompts using your provided settings as the default. Press Enter to accept each one or enter a replacement setting.

      If the settings are correct, enter `yes` to proceed with installation.

      ```
      Installation parameters:
         AM URL: https://am.example.com:8443/am
         Agent URL: https://customers.example.com:443
         Agent Profile name: iisagent
         Agent realm/organization name: /
         Agent Profile password source: c:\pwd.txt

      Confirm configuration (yes/no): [no]: yes Validating…​
      Validating…​ Success.
      Cleaning up validation data…​
      Creating configuration…​
      Installation complete.
      ```

      On successful completion, the installer adds the agent as a module to the IIS or ISAPI site configuration.

      |   |                                                                                                         |
      | - | ------------------------------------------------------------------------------------------------------- |
      |   | To ease logging, the installer grants full user access permissions on the IIS or ISAPI instance folder. |

      Each agent instance has a numbered configuration and logs directory.

      * For IIS, the first agent configuration and logs are located in `web_agents\iis_agent\instances\agent_1\`.

      * For ISAPI, the agent ID corresponds to the site ID. If site 5 is used, the agent configuration and logs are located in `web_agents\iis_agent\instances\agent_5\`.

6. Make sure the application pool identity related to the IIS site has the appropriate permissions on the following agent installation folders:

   * `\web_agents\iis_agent\lib`

   * `\web_agents\iis_agent\log`

   * `\web_agents\iis_agent\instances\agent_nnn`

     To change the ACLs for files and folders related to the agent instance, run the `agentadmin --o` command. For example:

     ```
     C:\web_agents\iis_agent\bin>agentadmin.exe --o "ApplicationPoolIdentity1" "C:\web_agents\iis_agent\lib"
     ```

     Learn more in [agentadmin command](agentadmin.html).

     When permissions aren't set correctly, errors such as getting a blank page when accessing a protected resource can occur.

7. If you installed Web Agent in an application, set [CDSSO Redirect URI](../properties-reference/com.sun.identity.agents.config.cdsso.redirect.uri.html) to the application path, as follows:

   1. Go to Realms > *Realm Name* > Agents > Web > *Agent Name* > SSO > Cross Domain SSO.

   2. Add the application path to the default value of [CDSSO Redirect URI](../properties-reference/com.sun.identity.agents.config.cdsso.redirect.uri.html). For example, if you installed Web Agent in an application such as `MyApp1/MyApp2`, set the property to `MyApp1/MyApp2/agent/cdsso-oauth2`.

   3. Save your changes.

## Install IIS or ISAPI Web Agent silently

|   |                                                                                                                                                                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The IIS Web Agent installer doesn't support custom namespace elements in the `web.config` file. If any exist, they're removed from the `web.config` file during the installation process.If you require custom namespace elements, back up the `web.config` file before installing the agent and manually restore them once the agent is installed. |

1. Review the information in [Before you install](pre-installation.html#before-install) and complete the [pre-installation tasks](pre-installation.html#preinstall-tasks).

2. Make sure AM is running.

3. Run the [agentadmin --s](agentadmin.html) command with the required arguments. For example:

   ```
   c:\web_agents\iis_agent\bin> agentadmin.exe --s ^
     "2.1.1" ^
     "https://am.example.com:8443/am" ^
     "http://iis.example.com:80" ^
     "/" ^
     "iisagent" ^
     "c:\pwd.txt" ^

   AM Web Agent for IIS Server installation.

   Validating…​
   Validating…​ Success.
   Cleaning up validation data…​
   Creating configuration…​
   Installation complete.
   ```

4. Make sure the application pool identity related to the IIS site has the appropriate permissions on the following agent installation folders:

   * `\web_agents\iis_agent\lib`

   * `\web_agents\iis_agent\log`

   * `\web_agents\iis_agent\instances\agent_nnn`

     To change the ACLs for files and folders related to the agent instance, run the `agentadmin --o` command. For example:

     ```
     C:\web_agents\iis_agent\bin>agentadmin.exe --o "ApplicationPoolIdentity1" "C:\web_agents\iis_agent\lib"
     ```

     Learn more in [agentadmin command](agentadmin.html).

     When permissions aren't set correctly, errors such as getting a blank page when accessing a protected resource can occur.

5. (Optional) If you installed the agent in a parent application, enable it for its child applications, as described in [Disable and enable agent protection for child applications](#proc-disabling-enabling-child-protection).

## Enable and disable IIS Web Agent

|   |                                                                                                    |
| - | -------------------------------------------------------------------------------------------------- |
|   | ISAPI Web Agent can't be enabled or disabled; it is either installed and running or not installed. |

### Disable and enable Web Agent on an IIS site or application

The `agentadmin` command shows only instances of the agent. Learn about how to enable or disable the protection of child applications in [Disable and enable agent protection for child applications](#proc-disabling-enabling-child-protection).

1. Log on to Windows as a user with administrator privileges.

2. Run the [agentadmin --l](agentadmin.html) command to list the installed agent configuration instances.

   ```
   c:\web_agents\iis_agent\bin> agentadmin.exe --l

   AM Web Agent configuration instances:

      id:            agent_1
      configuration: c:\web_agents\iis_agent\bin\..\instances\agent_1
      server/site:   2.2.1
   ```

   Make a note of the ID value of the configuration instance you want to disable or enable.

3. Perform one of the following steps:

   * To disable the agent in a site, run the [agentadmin --d](agentadmin.html) command and specify the ID of the agent configuration instance to disable.

     ```
     c:\web_agents\iis_agent\bin> agentadmin.exe --d agent_1

     Disabling agent_1 configuration…​
     Disabling agent_1 configuration…​ Done.
     ```

   * To enable the agent in a site, run the [agentadmin --e](agentadmin.html) command and specify the ID of the agent configuration instance to enable.

     ```
     c:\web_agents\iis_agent\bin> agentadmin.exe --e agent_1

     Enabling agent_1 configuration…​
     Enabling agent_1 configuration…​ Done.
     ```

### Disable and enable agent protection for child applications

1. Edit the child application's `web.config` configuration.

2. Decide whether to enable or disable agent protection:

   * To disable agent protection, add the following lines to the child application's `web.config` file:

     ```xml
     <OpenAmModule enabled="false" configFile="C:\web_agents\iis_agent\instances\agent_1\config\agent.conf" />
     <modules>
        <add name="OpenAmModule64" preCondition="bitness64" />
     </modules>
     ```

     Note that the path specified in `configFile` may be different for your environment.

   * To enable agent protection, understand that agents configured in a site or parent application also protect any applications that inherit the IIS configuration from that site or parent.

     If you have disabled the agent's protection for a child application by following the steps in this procedure, remove the lines added to the `web.config` file to enable protection again.

## Enable support for basic authentication and password replay

|   |                                                  |
| - | ------------------------------------------------ |
|   | ISAPI Web Agent doesn't support password replay. |

The IIS Web Agent supports basic authentication and password replay. Use the appropriate software versions.

Given the proper configuration and with Active Directory as a user data store for AM, the IIS agent can provide access to IIS server variables. The instructions for configuring the capability follow in this section, though you should read the section in full, also paying attention to the required workarounds for Microsoft issues.

When configured as described, the agent requests IIS server variable values from AM, which gets them from Active Directory. The agent then sets the values in HTTP headers so that they can be accessed by your application.

The following IIS server variables all take the same value when set: `REMOTE_USER`, `AUTH_USER`, and `login_USER`. The agent either sets all three, or doesn't set any of them.

When [Logon and Impersonation](../properties-reference/com.sun.identity.agents.config.iis.logonuser.html) is enabled, the agent performs Windows login and sets the user impersonation token in the agent session context.

When [Show Password in HTTP Header](../properties-reference/com.sun.identity.agents.config.iis.password.header.html) is enabled, the agent adds the password in the `USER_PASSWORD` header.

The agent doesn't modify any other IIS server variables related to the authenticated user's session.

The agent requires IIS to run in Integrated mode.

### Microsoft issues

Apply workarounds for the following Microsoft issues:

* [Prompt for credentials when you access WebDav-based FQDN sites in Windows](https://learn.microsoft.com/troubleshoot/windows-server/networking/credentials-prompt-access-webdav-fqdn-sites)

* [Office applications open blank from SharePoint WebDAV or sites](https://learn.microsoft.com/office/troubleshoot/powerpoint/office-opens-blank-from-sharepoint)

### Configure basic authentication and password replay support

1. Use the `openssl` tool to generate a suitable encryption key:

   ```
   $ openssl rand -base64 32
   e63…​sw=
   ```

2. In the AM admin UI, go to Deployment > Servers > *Server Name* > Advanced, and then add a property `com.sun.am.replaypasswd.key` with the encryption key you generated in a previous step as the value.

3. Go to Realms > *Realm Name* > Authentication > Settings > Post Authentication Processing, and in Authentication Post Processing Classes, add the class `com.sun.identity.authentication.spi.JwtReplayPassword`.

4. Restart AM.

5. In the AM admin UI go to Realms > *Realm Name* > Applications > Agents > Web > *Agent Name* > Advanced

   1. (AM 7.4.x and earlier versions) In Replay Password Key, enter the encryption key generated in a previous step. The field corresponds to [Replay Password Key](../properties-reference/com.sun.identity.agents.config.replaypasswd.key.html).

      |   |                                                                                                                                                                                                                                                           |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | From AM 7.5, setting this property in the AM admin UI is deprecated. Values set in this field of the AM admin UI are ignored. The value of the DES key is inherited from the secret mapped to the AM secret label `am.authentication.replaypassword.key`. |

   2. For Windows login for user token impersonation, enable [Logon and Impersonation](../properties-reference/com.sun.identity.agents.config.iis.logonuser.html).

   3. Save your changes.

6. (Optional) To set the encrypted password in the IIS `AUTH_PASSWORD` server variable, go to Realms > *Realm Name* > Applications > Agents > Web > *Agent Name* > Advanced, and enable [Show Password in HTTP Header](../properties-reference/com.sun.identity.agents.config.iis.password.header.html).

7. (Optional) If you require Windows login, or you need to use basic authentication with SharePoint or OWA, then you must do the following so that the agent requests AM to provide the appropriate account information from Active Directory in its policy response:

   * Configure Active Directory as a user data store

   * Configure the IIS or ISAPI agent profile User ID Parameter and User ID Parameter Type.

     Skip this step if you don't use SharePoint or OWA and no Windows login is required.

     Make sure the AM data store is configured to use Active Directory as the user data store.

     In the AM admin UI under Realms > *Realm Name* > Applications > Agents > Web > *Agent Name* > AM Services, set [User ID Parameter](../properties-reference/com.sun.identity.agents.config.userid.param.html) and [User ID Parameter Type](../properties-reference/com.sun.identity.agents.config.userid.param.type.html).

     For example, if the real username for Windows domain login in Active Directory is stored on the `sAMAccountName` attribute, then set the User ID Parameter to `sAMAccountName`, and the User ID Parameter Type to `LDAP`.

     Setting [User ID Parameter Type](../properties-reference/com.sun.identity.agents.config.userid.param.type.html) to `LDAP` causes the web agent to request that AM get the value of the User ID Parameter attribute from the data store, in this case, Active Directory. Given that information, the agent can set the HTTP headers `REMOTE_USER`, `AUTH_USER`, or `login_USER` and `USER_PASSWORD` with Active Directory attribute values suitable for Windows login, setting the remote user, and so forth.

8. (Optional) To access Microsoft Office from SharePoint pages, configure AM to persist the authentication cookie. Learn more in [Persistent cookie decision node](https://docs.pingidentity.com/auth-node-ref/8.1/persistent-cookie-decision.html).

## Install in a subrealm

Examples in this document install the agent in the top-level realm. To install the agent in a subrealm during interactive or silent installation, use the subrealm during the installation or in the response file.

For example, instead of:

```bash
Agent realm/organization name: [/]: /
```

specify:

```bash
Agent realm/organization name: [/]: /myrealm
```

Even though the agent is installed in a subrealm, the default login redirect requires the [user realm](../user-guide/glossary.html#def-user-realm) to be the top-level realm. You can find information about changing the user realm in [Login redirect](../user-guide/login-redirect.html).

---

---
title: Installation
description: Installation guide for PingAM Web Agent, covering setup on Apache HTTP Server, IIS, NGINX Plus, and Docker.
component: web-agents
version: 2026
page_id: web-agents:installation-guide:preface
canonical_url: https://docs.pingidentity.com/web-agents/2026/installation-guide/preface.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["index.adoc", "release-notes:preface.adoc"]
section_ids:
  preface-examples: Example installation for this guide
---

# Installation

This guide describes how to install Web Agent.

## Example installation for this guide

Unless otherwise stated, the examples in this guide assume the following installation:

* Web Agent installed on `https://agent.example.com:443`.

* AM installed on `https://am.example.com:8443/am`.

* Work in the top-level realm `/`.

If you use a different configuration, substitute in the procedures accordingly.

---

---
title: Installation environment variables
description: Reference for PingAM Web Agent installation environment variables, including proxy settings, TLS configuration, and authentication mode options.
component: web-agents
version: 2026
page_id: web-agents:installation-guide:installer-env-vars
canonical_url: https://docs.pingidentity.com/web-agents/2026/installation-guide/installer-env-vars.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Installation environment variables

This section describes Web Agent properties that are configured by environment variables and set during installation.

Use installation environment variables as follows:

* Add environment variables to the command line when you install the agent. For example:

  * Linux

  * Windows

  ```none
  $ AM_AGENT_AUTH_MODE=1 ./agentadmin --i
  ```

  ```
  C:\>set AM_AGENT_AUTH_MODE=1
  C:\>agentadmin.exe --i agent_1
  ```

* Use installation environment variables with the `agentadmin -V[i]` command to validate the installation with different parameters. For example:

  * Linux

  * Windows

  ```bash
  $ AM_PROXY_HOST=proxy.host.net AM_PROXY_PORT=8080 AM_PROXY_USER=user AM_PROXY_PASSWORD=pass ./agentadmin --Vi
  ```

  ```
  C:\>set AM_PROXY_HOST=proxy.host.net
  C:\>set AM_PROXY_PORT=8080
  C:\>set AM_PROXY_USER=user
  C:\>set AM_PROXY_PASSWORD=pass
  C:\>agentadmin.exe --Vi agent_1
  ```

You can find details about other environment variables in [Environment variables](../user-guide/configure-envvars.html).

* `AM_AGENT_AUTH_MODE`

  A flag to determine which method the agent uses to authenticate to Advanced Identity Cloud and AM:

  * `1` (default): The agent always authenticates using the `Agent` journey. If this fails, the agent doesn't try to authenticate using the authentication module.

    Make sure the `Agent` journey exists. Learn more in [Authenticate agents to the identity provider](pre-installation.html#authenticate_agents_to_the_identity_provider).

  * `2`: The agent always authenticates using the authentication module. Modules are deprecated and will be removed in a future release.

    If you use PingAM 7.3 or 7.4 and experience issues with session quotas, set this environment variable to `2` to always authenticate using the authentication module.

* `AM_PROXY_HOST`

  The proxy FQDN, when AM and the agent communicate through a proxy configured in forward proxy mode.

* `AM_PROXY_PASSWORD`

  The agent password, when AM and the agent communicate through a proxy configured in forward proxy mode, and the proxy requires that the agent authenticates using Basic Authentication.

* `AM_PROXY_USER`

  The agent username, when AM and the agent communicate through a proxy configured in forward proxy mode, and the proxy requires that the agent authenticates using Basic Authentication.

* `AM_PROXY_PORT`

  The proxy port number, when AM and the agent communicate through a proxy configured in forward proxy mode.

- `AM_SSL_KEYLOG_ENABLE`

  A flag to enable TLS key logging during the agent installation process:

  * `0` (default): Disable TLS key logging.

  * `1`: Enable TLS key logging to troubleshoot TLS issues between the agent and AM.

    If you enable TLS key logging, you must specify the name of the SSL key log file in the [AM\_SSL\_KEYLOG\_FILE](../user-guide/configure-envvars.html#am-ssl-keylog-file) environment variable.

    |   |                                                                                                                                  |
    | - | -------------------------------------------------------------------------------------------------------------------------------- |
    |   | Only enable TLS key logging when advised by Support. After troubleshooting, disable key logging and remove the SSL key log file. |

  Learn more in [TLS key logging](../maintenance-guide/troubleshooting.html#tls-key-logging).

- `APACHE_RUN_USER`

  The user running the Apache HTTP or IBM HTTP Server. Set this variable before installation when an Apache user is not defined in `httpd.conf`. This can be the case in non-Red Hat Enterprise Linux-based distributions.

- `APACHE_RUN_GROUP`

  The group to which the user running the Apache HTTP Server or IBM HTTP Server belongs. Set this variable before installation when an Apache group is not defined in `httpd.conf`. This can be the case in non-Red Hat Enterprise Linux-based distributions.

- `AM_SSL_SCHANNEL`

  Use for Windows only, when TLS/SSL is configured in AM or the agent web server.

  A flag for whether the agent installation process should use the Windows Secure Channel API (Schannel):

  * `0`: Disable Schannel support. The agent uses OpenSSL libraries instead.

    Make sure the [OpenSSL libraries](pre-installation.html#pre-SSL-configuration) are in the correct location.

  * `1`: Enable Schannel support.

- `AM_SSL_KEY`

  Use for OpenSSL only, when TLS/SSL is configured in AM or the agent web server.

  When AM is configured to perform client authentication, this environment variable specifies a PEM file that contains the private key corresponding to the certificate specified in the `AM_SSL_CERT` environment variable.

  For example:

  * Unix

  * Windows

  ```bash
  /opt/certificates/client-private-key.pem
  ```

  ```windows
  C:\Certificates\client-private-key.pem
  ```

- `AM_SSL_PASSWORD`

  Use for OpenSSL only, when TLS/SSL is configured in AM or the agent web server.

  When AM is configured to perform client authentication, this environment variable specifies the obfuscated password of the private key configured in the `AM_SSL_KEY` variable. Configure this variable only if the private key is password-protected.

  To obfuscate the password, use the `agentadmin --p` command:

  * Unix

  * Windows

  ```bash
  $ /path/to/web_agents/agent_type/bin/> agentadmin --p "Encryption Key" "cat certificate_password.file"

  Encrypted password value: zck...jtc=com.forgerock.agents.config.cert.key.password = zck+6RKqjtc=
  ```

  ```windows
  C:\path\to\web_agents\agent_type\bin> agentadmin.exe --p "Encryption_Key" "Certificate_File_Password"
  Encrypted password value: zck+6RKqjtc=
  ```

- `AM_SSL_CIPHERS`

  Use for OpenSSL only, when TLS/SSL is configured in AM or the agent web server.

  The list of ciphers to support. The list consists of one or more cipher strings separated by colons, as defined in the man page for ciphers at <http://www.openssl.org>.

  For example, `HIGH:MEDIUM`.

- `AM_SSL_CERT`

  Use when TLS/SSL is configured in AM or the agent web server.

  When AM is configured to perform client authentication, this environment variable specifies a PEM file that contains the certificate chain for the agent.

  For example, `/opt/certificates/client-cert.pem`, `C:\Certificates\client-cert.pem` (Windows with OpenSSL), or `Cert:\LocalMachine\My location` (Windows with Schannel).

- `AM_SSL_CA`

  When configuring the agent to validate AM's certificate, this environment variable specifies a PEM file that contains the certificates required to validate AM's server certificate. For example, `/opt/certificates/ca.pem`, `C:\Certificates\ca.pem` (Windows with OpenSSL), or `Cert:\LocalMachine\Ca` (Windows with Schannel).

---

---
title: NGINX Plus Web Agent
description: Install and configure PingAM Web Agent on NGINX Plus.
component: web-agents
version: 2026
page_id: web-agents:installation-guide:nginx
canonical_url: https://docs.pingidentity.com/web-agents/2026/installation-guide/nginx.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  install-nginx: Install NGINX Plus Web Agent
  install-nginx-web-agent: Install NGINX Plus Web Agent interactively
  silent-nginx-agent-installation: Install NGINX Plus Web Agent silently
  complete-nginx-install: Complete the NGINX Plus Web Agent installation
  check_the_nginx_web_agent_installation: Check the NGINX Web Agent installation
  install_in_a_subrealm: Install in a subrealm
  configure-nginx: Configure NGINX Plus Web Agent
  NGINX_directives: NGINX directives
  openam_agent: openam_agent
  openam_configuration: openam_configuration
  openam_threadpool: openam_threadpool
  openam_agent_instance: openam_agent_instance
  examples: Examples
  nginx-reverse-proxy-server: NGINX as a reverse proxy
---

# NGINX Plus Web Agent

## Install NGINX Plus Web Agent

Examples use the NGINX Plus R36 agent path. For other supported versions, replace the R36 agent path with the required version. Learn more about supported versions of NGINX in [Other requirements](https://docs.pingidentity.com/web-agents/release-notes/before-you-install.html#web-pa-other-requirements).

Consider the following for NGINX Plus Web Agent:

* SELinux can prevent the web server from accessing agent libraries and the agent from being able to write to audit and debug logs. Learn more in [Troubleshoot](../maintenance-guide/troubleshooting.html).

* The agent and NGINX must load the same version of the OpenSSL libraries. If you have multiple supported versions of OpenSSL installed, you could experience stability issues when using the Web Agent.

  Use the standard `ldconfig` utility to configure the dynamic linker, or set the `LD_LIBRARY_PATH` variable in NGINX to ensure the same version is loaded.

### Install NGINX Plus Web Agent interactively

1. Review the information in [Before you install](pre-installation.html#before-install) and complete the [pre-installation tasks](pre-installation.html#preinstall-tasks).

2. Shut down the server where you plan to install the agent.

3. Make sure AM is running.

4. Run the `agentadmin --i` command to install the agent:

   ```
   $ cd /web_agents/nginx36_agent/bin/
   $ ./agentadmin --i
   ```

5. When prompted, enter information for your deployment.

   |   |                                                       |
   | - | ----------------------------------------------------- |
   |   | To cancel the installation at any time, press Ctrl+C. |

   1. Enter the full path to the NGINX Plus server configuration file, `nginx.conf` :

      ```
      Enter the complete path to your NGINX server configuration file
       [ q or 'ctrl+c' to exit ]
       [nginx.conf]:/etc/nginx/nginx.conf
      ```

   2. The installer can import settings from an existing web agent to the new installation and skips prompts for any values present in the existing configuration file. You will be required to re-enter the agent profile password.

      Enter the full path to an existing agent configuration file to import the settings or press Enter to skip the import:

      ```
      To set properties from an existing configuration enter path to file
       [ q or Ctrl+C to exit, return to ignore ]
       Existing agent.conf file:
      ```

   3. Enter the full URL of the AM instance that the agent should connect to:

      |   |                                                                                                                                                                                                                                                                                                |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | If a reverse proxy is configured between AM and the agent, set the AM URL to the proxy URL, for example, `https://proxy.example.com:443/am`. You can find information about setting up an environment for reverse proxies in [Apache as a reverse proxy](apache.html#configure-apache-server). |

      ```
      Enter the URL where the AM server is running. Please include the
       deployment URI also as shown below:
       (http://am.sample.com:58080/am)
       [ q or 'ctrl+c' to exit ]
       AM server URL: https://am.example.com:8443/am
      ```

   4. Enter the full URL of the server the agent is running on.

      ```
      Enter the Agent URL as shown below:
       (http://agent.sample.com:1234)
       [ q or 'ctrl+c' to exit ]
       Agent URL: https://agent.example.com:443
      ```

   5. Enter the name of the agent profile created in AM:

      ```
      Enter the Agent profile name
       [ q or 'ctrl+c' to exit ]
       Agent Profile name:nginx_agent
      ```

   6. Enter the [agent profile realm](../user-guide/glossary.html#def-agent-profile-realm). Realms are case-sensitive:

      ```
      Enter the Agent realm/organization
       [ q or 'ctrl+c' to exit ]
       Agent realm/organization name: [/]:/
      ```

   7. Enter the full path to the file containing the agent profile password created in the prerequisites:

      ```
      Enter the path to a file that contains the password to be used
       for identifying the Agent
       [ q or 'ctrl+c' to exit ]
       The path to the password file:/secure-directory/pwd.txt
      ```

   8. The installer displays a summary of the configuration settings you specified.

      If a setting is incorrect, enter `no` or press Enter. The installer loops through the configuration prompts again, using your provided settings as the default. Press Enter to accept each one or enter a replacement setting.

      If the setting is correct, enter `yes` to proceed with installation:

      ```
      Installation parameters:
       AM URL: https://am.example.com:8443/am
       Agent URL: https://agent.example.com:443
       Agent Profile name: nginx_agent
       Agent realm/organization name: /
       Agent Profile password source: /secure-directory/pwd.txt

       Confirm configuration (yes/no): [no]: yes
       Validating…​
       Validating…​ Success.

       Cleaning up validation data…​

       Creating configuration…​

       In order to complete the installation of the agent, update the configuration file /etc/nginx/nginx.conf

       if this is the first agent in the installation, please insert the following directives into the top section of the NGINX configuration
       load_module /web_agents/nginx36_agent/lib/openam_ngx_auth_module.so;

       then insert the following directives into the server or location NGINX configuration sections that you wish this agent to protect:
       openam_agent on;
       openam_agent_configuration /web_agents/nginx36_agent/instances/agent_1/config/agent.conf;

       Please ensure that the agent installation files have read/write permissions for the NGINX server's user

       Please press any key to continue.

       Installation complete.
      ```

      Each agent instance has a numbered configuration and logs directory. The first agent configuration and logs are located in `/web_agents/nginx36_agent/instances/agent_1/`.

6. Finish installation as described in [Complete the NGINX Plus Web Agent Installation](#complete-nginx-install).

### Install NGINX Plus Web Agent silently

Use the `agentadmin --s` command for silent installation. You can find details about the options in [agentadmin command](agentadmin.html).

1. Review the information in [Before you install](pre-installation.html#before-install) and complete the [pre-installation tasks](pre-installation.html#preinstall-tasks).

2. Shut down the server where you plan to install the agent.

3. Make sure AM is running.

4. Run the `agentadmin --s` command with the required arguments. For example:

   ```
   $ agentadmin --s \
    "/etc/nginx/nginx.conf" \
    "https://am.example.com:8443/am" \
    "https://agent.example.com:443" \
    "/" \
    "nginx_agent" \
    "/secure-directory/pwd.txt" 
   Web Agent for NGINX Server installation.

   Validating…​

   Validating…​ Success.

   Cleaning up validation data…​

   Creating configuration…​

   In order to complete the installation of the agent, update the configuration file /etc/nginx/nginx.conf

   if this is the first agent in the installation, please insert the following directives into the top section of the NGINX configuration
   load_module /web_agents/nginx36_agent/lib/openam_ngx_auth_module.so;

   then insert the following directives into the server or location NGINX configuration sections that you wish this agent to protect:
   openam_agent on;
   openam_agent_configuration /web_agents/nginx36_agent/instances/agent_3/config/agent.conf;

   Please ensure that the agent installation files have read/write permissions for the NGINX server's user

   Please press any key to continue.
   ```

5. Finish the installation as described in [Complete the NGINX Plus Web Agent Installation](#complete-nginx-install).

### Complete the NGINX Plus Web Agent installation

After [interactive](#install-nginx-web-agent) or [silent](#silent-nginx-agent-installation) installation, follow these steps to complete the installation.

1. Edit the NGINX Plus server configuration file `nginx.conf` to load the agent module `openam_ngx_auth_module.so`:

   ```
   $ vi nginx.conf
   user  nginx;
   worker_processes  auto;

   error_log     /var/log/nginx/error.log notice;
   pid           /var/run/nginx.pid;
   load_module   /web_agents/nginx36_agent/lib/openam_ngx_auth_module.so;
   …​
   ```

2. Add and `openam_agent` directive at the global level of `nginx.conf` to set the agent as `on`. Learn more in [openam\_agent](#NGINX-amagent).

3. Give the user or group running the NGINX Plus server appropriate permissions for the following directories:

   * Read permission: `/web_agents/nginx36_agent/lib`

   * Read and write permission:

     * `/web_agents/nginx36_agent/instances/agent_nnn`

     * `/web_agents/nginx36_agent/log`

   Apply execute permissions on the folders listed above, recursively, for the user that runs the NGINX Plus server.

   To determine which user or group is running the NGINX Plus server, check the `User` directive in the NGINX Plus server configuration file.

   Failure to set permissions causes issues, such as the NGINX Plus server not starting up, getting a blank page when accessing a protected resource, or the web agent generating errors during log file rotation.

   |   |                                                                                                                                                                                                                       |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You could encounter the same issues if SELinux is enabled in `enforcing` mode and it is not configured to allow access to agent directories. Learn more in [Troubleshoot](../maintenance-guide/troubleshooting.html). |

4. Start the server.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The NGINX Plus server only sets the `REMOTE_USER` variable if the request contains an HTTP Authorization header, but the NGINX agent does not set an an HTTP Authorization header after the user has authenticated. Therefore, if you need to set the variable so CGI scripts can use it, configure the agent to create a custom header with the required attribute and then configure the NGINX Plus server to capture that header and convert it into the `REMOTE_USER` variable. |

### Check the NGINX Web Agent installation

1. After you start the server, check the server error log to make sure startup completed successfully:

   ```
   2021…​ [info] 31#31: agent worker startup complete
   ```

2. Make an HTTP request to a resource protected by the agent, then check the `/web_agents/nginx36_agent/log/system_0.log` file to verify that no startup errors occurred:

   ```
   Web Agent Version: 2026.6
   Revision: ab12cde, Container: NGINX Plus R36 Linux 64bit (Ubuntu24),
   Build date: …​
   ```

3. (Optional) If you have a policy configured, test that the agent is processing requests. For example, make an HTTP request to a resource protected by the agent, and check that you are redirected to AM to authenticate. After authentication, AM redirects you back to the resource you tried to access.

### Install in a subrealm

Examples in this document install the agent in the top-level realm. To install the agent in a subrealm during interactive or silent installation, use the subrealm during the installation or in the response file.

For example, instead of:

```bash
Agent realm/organization name: [/]: /
```

specify:

```bash
Agent realm/organization name: [/]: /myrealm
```

Even though the agent is installed in a subrealm, the default login redirect requires the [user realm](../user-guide/glossary.html#def-user-realm) to be the top-level realm. You can find information about changing the user realm in [Login redirect](../user-guide/login-redirect.html).

## Configure NGINX Plus Web Agent

### NGINX directives

Add NGINX directives to the `nginx.conf` configuration file to configure the global environment or individual HTTP servers and HTTP locations.

Directives are applied hierarchically. When set at the global level in `nginx.conf`, they apply to all HTTP servers and HTTP locations except those explicitly specified otherwise. Similarly, when set for an HTTP server or HTTP location, they are set for all child locations except those explicitly specified otherwise.

#### `openam_agent`

A flag to set the agent on or off:

* `openam_agent on`

  The agent protects the resource. It allows or denies requests based on AM policy configuration and not-enforced rules.

* `openam_agent off`

  NGINX protects the resource. The agent plays no part in protecting the server locations.

Default: None.

After installation, add `openam_agent on` to `nginx.conf` at the global level.

```
user  nginx;
worker_processes  auto;

error_log  /var/log/nginx/error.log notice;
openam_agent on
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Consider setting `openam_agent` to `off` for the following situations:- For HTTP servers or HTTP locations that need no AM authentication or policy, such as the public face of a website, `/css` directories, or `/images` directories.

- When an NGINX HTTP Server is acting as a reverse proxy to AM or Advanced Identity Cloud, if you don't want the agent to take part in protecting URLs in AM or Advanced Identity Cloud. |

#### `openam_configuration`

The path to the local bootstrap file for the agent:

`openam_configuration <path to nginx.conf>`

Default: None, but during agent installation you must provide the path to `/etc/nginx/nginx.conf`.

#### `openam_threadpool`

The name of the AM threadpool:

`openam_threadpool <name>`

Default: The NGINX default threadpool

|   |                                                                                          |
| - | ---------------------------------------------------------------------------------------- |
|   | Before setting this directive, consider the consequence of changing the threadpool name. |

#### openam\_agent\_instance

A number to identify an instance of NGINX Plus:

`openam_agent_instance <number>`

Default: `1`

In deployments with multiple instances of NGINX Plus, use a unique number for each instance.

#### Examples

* `openam_agent` is `on` globally but off\` for one HTTP location

  |   |                                                                                                                                                                                |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | When `openam_agent` configuration is `off`, configure the server location `/agent` as `on`. This allows AM to redirect requests to the `/agent` endpoint after authentication. |

  In the following example `nginx.conf`:

  * `agent_1` in the `server` context protects the `/` and ``/marketplace`location`` contexts

  * No agent instance protects the ``/customers`location`` context.

  ```
  server {
    listen       80 default_server;
    server_name  localhost;
    openam_agent on;
    openam_agent_configuration /web_agents/nginx36_agent/instances/agent_1/config/agent.conf;
    #charset koi8-r;
    #access_log  /var/log/nginx/log/host.access.log  main;

      location / {
        root   /www/;
        index  index.html index.htm;
      }

      location /customers {
        openam_agent  off
        root   /www/customers
        index  index.html
      }

      location /market {
      root   /www/marketplace
      index  index.html
    }
  }
  ```

* Different agent instances protect different parts of the deployment

  In the following example `nginx.conf`:

  * `agent_1` at the `server` context protects the `/` and ``/marketplace`location`` contexts

  * `agent_2` protects the ``/customers`location`` context

  ```
  server {
    listen       80 default_server;
    server_name  localhost;
    openam_agent on;
    openam_agent_configuration /web_agents/nginx36_agent/instances/agent_1/config/agent.conf;
    #charset koi8-r;
    #access_log  /var/log/nginx/log/host.access.log  main;

      location / {
        root   /www/;
        index  index.html index.htm;
      }

      location /customers {
        openam_agent on;
        openam_agent_configuration /web_agents/nginx36_agent/instances/agent_2/config/agent.conf;
        root   /www/customers
        index  index.html
      }

      location /market {
        root   /www/marketplace
        index  index.html
    }
  }
  ```

### NGINX as a reverse proxy

This section contains an example configuration of NGINX as a reverse proxy between AM and Web Agent. You can use any reverse proxy that supports the WebSocket protocol.

![Simplified diagram showing an NGINX configured as a reverse proxy between AM and the agent.](_images/apache-proxy.svg)Figure 1. NGINX reverse proxy configured between the agent and AM

Find information on configuring NGINX for load balancing and other environment requirements in [NGINX as a WebSocket Proxy](https://www.f5.com/company/blog/nginx/websocket-nginx) in the NGINX documentation.

After [interactive](#install-nginx-web-agent) or [silent](#silent-nginx-agent-installation) installation, follow these steps to configure NGINX as a reverse proxy.

1. Locate the NGINX Plus server configuration file `nginx.conf`.

2. Edit `nginx.conf` to add directives to the context you want to protect:

   ```bash
   server {
     ...
     location /am
       {
         proxy_set_header Host $host;
         proxy_pass http://hostname:port/am;
         proxy_http_version 1.1;
         proxy_set_header Connection ""; # to allow keep alives to work #
       }
     location /am/notifications
       {
         proxy_pass http://hostname:port/am/notifications;
         proxy_http_version 1.1;
         proxy_set_header Upgrade $http_upgrade;
         proxy_set_header Connection "Upgrade";
         proxy_set_header Host $host;
       }
     ...
   }
   ```

3. Ensure the user or group running the NGINX Plus server has the appropriate permissions over the following directories:

   * Read Permission: `/web_agents/nginx36_agent/lib`

   * Read and Write Permission:

     * `/web_agents/nginx36_agent/instances/agent_nnn`

     * `/web_agents/nginx36_agent/log`

4. Restart the reverse proxy instance.

5. Configure AM to recover the forwarded header configured in the reverse proxy.

6. Review other configuration that a reverse proxy environment can require. Learn more in [Agent connection to AM through a load balancer/reverse proxy](../user-guide/load-balancers-proxies.html#comms-am-agents)

---

---
title: Post-installation
description: "Post-installation steps for PingAM Web Agent: review logs, validate the instance, configure shared memory, and support load balancers and reverse proxies."
component: web-agents
version: 2026
page_id: web-agents:installation-guide:post-installation
canonical_url: https://docs.pingidentity.com/web-agents/2026/installation-guide/post-installation.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  review_directories_for_configuration_and_logs: Review directories for configuration and logs
  validate-instance: Validate the agent instance
  configuring-shared-memory: Configure shared runtime resources and memory
  choosing-agent-groups: Choose whether to share resources
  configure_apache_agent_groups: Configure Apache agent groups
  configure_nginx_plus_agent_groups: Configure NGINX Plus agent groups
  post-LB-proxies: Support load balancers and reverse proxies between clients and agents
  configuring-audit-logging: Configure audit logging
  configure_audit_logging_for_the_agent: Configure audit logging for the agent
  configuring-agent-communication: Configure AM to sign authentication information
  proc-agents-secret-IDs-am65: "Configure AM secret labels for the agents' OAuth 2.0 provider"
---

# Post-installation

## Review directories for configuration and logs

Each agent instance has a numbered configuration and logs directory, starting with `agent_1`. The first agent configuration and logs are located at `web_agents/agent_type/instances/agent_1/`.

The following configuration files and logs are created:

* `web_agents/agent_type/instances/agent_1/config/`: Bootstrap properties to connect to AM and download the configuration. This directory contains properties that are used only in [local configuration mode](../user-guide/glossary.html#def-local-configuration-mode).

* `web_agents/agent_type/instances/agent_1/logs/audit/`: Audit log directory. Used only if [Audit Log Location](../properties-reference/com.sun.identity.agents.config.log.disposition.html) is `LOCAL` or `ALL`.

* `web_agents/agent_type/instances/agent_1/logs/debug/`: The directory where the agent writes debug log files after startup.

During agent startup, the location of the logs can be based on the agent web server, or defined in the site configuration file for the server. For example, bootstrap logs for NGINX Plus Web Agent can be written to `/var/log/nginx/error.log`.

## Validate the agent instance

Validate the agent instance by using the `agentadmin --V[i]` command. For information about the options and requirements for this command, refer to [agentadmin](agentadmin.html#vi).

* Linux

* Windows

```
$ sudo -u web-server-user
$ cd /web_agents/agent_type/bin/
$ ./agentadmin --Vi agent_name am_identity_name .var]/path/to/am_identity_password
```

```
C:\web_agents\agent-type\bin> agentadmin --Vi ^
agent_name am_identity_name C:/path/to/am_identity_password /
```

A result similar to this is displayed:

```
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

If `validate_websocket_connection` is `not ok`, make sure the web server and the network infrastructure between the web server and the AM servers support WebSockets.

## Configure shared runtime resources and memory

Consider using agent resource groups in atypical deployments, where multiple independent web servers are deployed on the same machine. Agent resource groups apply only to Apache HTTP server or NGNIX, because IIS and ISAPI runs only as a single instance.

Agent resource groups allow server processes to share resources and memory, such as background tasks, log files, runtime resources including pipes, caches, and notification channels to AM.

An agent resource group is determined by the AmAgentID directive in a web server configuration. The value is numeric and defaults to 0 for a typical, single-server deployment. By default, up to 32 agent instances can be in a single installation. For information about changing this limit, refer to *AM\_MAX\_AGENTS* in [Environment variables](../user-guide/configure-envvars.html).

### Choose whether to share resources

Consider the information in the following table before configuring your agent resource groups:

| Impact                                                                                      | Advantage                                                                            | Caution                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Shared agent policy and session cache                                                       | Potentially reduces overhead of requests to AM for authentication and authorization. | Cache may fill with irrelevant entries.                                                                                                                                                                                                                                                                      |
|                                                                                             | Reduced memory consumption.                                                          | Sharing the cache among different locations or virtual hosts may not be desirable.                                                                                                                                                                                                                           |
|                                                                                             | -                                                                                    | Agent instances that are members of the same agent group must be configured in the same Apache or NGINX Plus installation.                                                                                                                                                                                   |
| Reduced number of background threads. (Single WebSocket connection to AM for notifications) | Reduced system resource usage.                                                       | Ensure that the `AM_MAX_AGENTS` environment variable is set to, at least, the total number of agent instances in the installation.                                                                                                                                                                           |
| Agent instances share runtime files and semaphores                                          | Reduced system resource usage.                                                       | Ensure that files and resources can be accessed by all agent instances.For example, add the users running the instances to the same group and configure the resources to have `660` permissions. Learn more in *AM\_RESOURCE\_PERMISSIONS* in [Environment variables](../user-guide/configure-envvars.html). |

### Configure Apache agent groups

To create a group in an Apache agent installation, add an `AmAgentId` directive to the Apache configuration file, `httpd.conf`.

To create multiple agent groups in an installation, set `AmAgentId` to a different value in each Apache configuration file. Set only one `AmAgentId` directive in each `httpd.conf`. If more than one value is set, the agent uses the last set value.

When `AmAgentId` isn't specified in `httpd.conf`, it takes the default value of `0`.

The following example `httpd.conf` file configures a group with `AmAgentId 1`. The group includes two virtual hosts, each protected by a different instance of the agent. Both agent instances belong to the agent group `1`.

|   |                                                                          |
| - | ------------------------------------------------------------------------ |
|   | The `AmAgentId` configuration must be outside the `VirtualHost` section. |

```
AmAgentId 1
<VirtualHost *:80>
ServerName www.site1.com
DocumentRoot /home/www/site1.com
AssignUserID site1 www-data
AmAgent On
AmAgentConf /web_agents/apache24_agent/bin/../instances/agent_1/config/agent.conf
…​
</VirtualHost>

<VirtualHost *:8080>
ServerName www.site2.com
DocumentRoot /home/www/site3.com
AssignUserID site2 www-data
AmAgent On
AmAgentConf /web_agents/apache24_agent/bin/../instances/agent_2/config/agent.conf
…​
</VirtualHost>
```

The following table shows an example of six Apache agent instances split into three agent groups:

| Agent instances                     | Directive configuration | Description                                                                                                 |
| ----------------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------- |
| `Agent_1` and `Agent_2`             | Not set (default 0)     | `Agent_1` and `Agent_2` instances share runtime resources and the policy cache with each other.             |
| `Agent_3`, `Agent_4`, and `Agent_5` | 1                       | `Agent_3`, `Agent_4`, and `Agent_5` instances share runtime resources and the policy cache with each other. |
| `Agent_6`                           | 2                       | `Agent_6` instance doesn't share runtime resources or the policy cache with any other instance.             |

### Configure NGINX Plus agent groups

To add NGINX Plus agent instances to a group, add the `openam_agent_instance` directive to each instance in the NGINX Plus server configuration file `nginx.conf`.

The following example `nginx.conf` file configures one agent group, **openam\_agent\_instance 2**, containing `agent_3` and `agent_4`:

```
server {
  listen       80 default_server;
  server_name  localhost;
  openam_agent on;
  openam_agent_configuration /web_agents/nginx36_agent/bin/../instances/agent_3/config/agent.conf; openam_agent_instance 2
  …​
  location /customers {
    openam_agent on;
    openam_agent_configuration /web_agents/nginx36_agent/bin/../instances/agent_4/config/agent.conf; openam_agent_instance 2
    root   /www/customers
    index  index.html
  }
…​
```

When `openam_agent_instance` is not specified for an agent instance, the instance uses the default value of `1`.

To create multiple agent groups in an NGINX Plus agent installation, use different values for `openam_agent_instance`. In the previous example, you could specify two groups by using `openam_agent_instance 2` and `openam_agent_instance 3`.

## Support load balancers and reverse proxies between clients and agents

When your environment has reverse proxies or load balancers configured between agents and clients, you must perform additional configuration in the agents to account for the anonymization of both the clients and the agents.

Failure to do so may cause policy evaluation and other agent features to fail.

Learn more in [Configure load balancers and reverse proxies](../user-guide/load-balancers-proxies.html).

## Configure audit logging

Web Agent supports the logging of audit events for security, troubleshooting, and regulatory compliance. Store agent audit event logs in the following ways:

* Remotely

  Log audit events to the audit event handler configured in the AM realm. In a site comprised of several AM servers, agents write audit logs to the AM server that satisfies the agent request for client authentication or resource authorization.

  Agents cannot log audit events remotely if:

  * AM's audit logging service is disabled.

  * No audit event handler is configured in the [agent profile realm](../user-guide/glossary.html#def-agent-profile-realm).

  * All audit event handlers configured in the [agent profile realm](../user-guide/glossary.html#def-agent-profile-realm) are disabled.

    For more information about audit logging in AM, refer to [Audit logging](https://docs.pingidentity.com/pingam/8.1/monitoring/audit-logging.html) in AM's *Security guide*.

* Locally

  Log audit events in JSON format to a file in the agent installation directory, `/web_agents/agent_type/logs/audit/`.

* Locally and remotely

  Log audit events:

  * To a file in the agent installation directory.

  * To the audit event handler configured in the [agent profile realm](../user-guide/glossary.html#def-agent-profile-realm).

The example is an agent log record:

```json
{
   "timestamp":"2017-10-30T11:56:57Z",
   "eventName":"AM-ACCESS-OUTCOME",
   "transactionId":"608831c4-7351-4277-8a5f-b1a83fe2277e",
   "userId":"id=bjensen,ou=user,dc=am,dc=example,dc=com",
   "trackingIds":[
      "fd5c8ccf-7d97-49ba-a775-76c3c06eb933-82095",
      "fd5c8ccf-7d97-49ba-a775-76c3c06eb933-82177"
   ],
   "component":"Web Policy Agent",
   "realm":"/",
   "server":{
      "ip":"127.0.0.1",
      "port":8020
   },
   "request":{
      "protocol":"HTTP/1.1",
      "operation":"GET"
   },
   "http":{
      "request":{
         "secure":false,
         "method":"GET",
         "path":"http://my.example.com:8020/examples/",
         "cookies":{
            "am-auth-jwt":"eyJ0eXAiOiJKV1QiLCJhbGciOi[...]"
            "i18next":"en",
            "amlbcookie":"01",
            "iPlanetDirectoryPro":"Ts2zDkGUqgtkoxR[...]"
         }
      }
   },
   "response":{
      "status":"DENIED"
   },
   "_id":"fd5c8ccf-7d97-49ba-a775-76c3c06eb933-81703"
}
```

|   |                                                                              |
| - | ---------------------------------------------------------------------------- |
|   | Local audit logs do not have an `_id` attribute, which is an internal AM id. |

The audit log format adheres to the log structure shared across the Ping Advanced Identity Software. For more information about the audit log format, refer to [Audit log format](https://docs.pingidentity.com/pingam/8.1/monitoring/audit-logging-ref.html#audit-log-format) in AM's *Security guide*.

Web Agent supports propagation of the transaction ID across the Ping Advanced Identity Software using the HTTP header `X-ForgeRock-TransactionId`. For more information about configuring the header, refer to [Trust transaction headers](https://docs.pingidentity.com/pingam/8.1/monitoring/implementing-audit.html#configuring-trusttransactionheader-system-property) in AM's *Security guide*.

By default, the Web Agent does not write audit log records. To configure audit logging, perform the following procedure:

### Configure audit logging for the agent

This procedure assumes the Web Agent is in [centralized configuration mode](../user-guide/glossary.html#def-central-configuration-mode). Property names are provided for [local configuration mode](../user-guide/glossary.html#def-local-configuration-mode).

1. In the AM admin UI, go to Realms > *Realm Name* > Applications > Agents > Web > *Agent Name* > Global > Audit.

2. In [Audit Access Types](../properties-reference/com.sun.identity.agents.config.audit.accesstype.html), select the type of messages to log. For example, select `LOG_ALL` to log access allowed and access denied events.

3. In [Audit Log Location](../properties-reference/com.sun.identity.agents.config.log.disposition.html), select whether to write the audit logs locally to the agent installation (`LOCAL`), remotely to AM (`REMOTE`), or to both places (`ALL`). For example, keep `REMOTE` to log audit events to the AM instances.

4. In [Local Audit Log Rotation Size](../properties-reference/com.sun.identity.agents.config.local.log.size.html), specify the maximum size, in bytes, of the audit log files.

   This is a bootstrap property. After changing this property, restart the web server where the agent runs.

## Configure AM to sign authentication information

AM communicates all authentication and authorization information to Web Agent, using OpenID Connect ID tokens. For security, configure AM and the agent to use signed tokens. Learn more in [RFC 7518: JSON Web Algorithms (JWA)](https://www.rfc-editor.org/rfc/rfc7518).

AM also uses an HMAC signing key to protect requested `ACR` claims values between sending the user to the authentication endpoint, and returning from successful authentication.

By default, AM uses a demo key and an autogenerated secret for these purposes. For production environments, perform one of the following procedures to create new key aliases and configure them in AM.

### Configure AM secret labels for the agents' OAuth 2.0 provider

By default, AM configured to:

* Sign the session ID tokens with the secret mapped to the `am.global.services.oauth2.oidc.agent.idtoken.signing` secret label. The label defaults to the `rsajwtsigningkey` key alias provided in AM's JCEKS keystore.

* Sign the claims with the secret mapped to the `am.services.oauth2.jwt.authenticity.signing` secret label. The label defaults to the `hmacsigningtest` key alias available in AM's JCEKS keystore.

  1. Create the following aliases in one of the secret stores configured in AM, for example, the default JCEKS keystore:

     1. Create an RSA key pair.

     2. Create an HMAC secret.

  2. In the AM admin UI, go to Configure > Secret Stores > *Keystore Secret Store Name* > Mappings.

  3. Configure the following secret labels:

     1. Configure the new RSA key alias in the `am.global.services.oauth2.oidc.agent.idtoken.signing` secret label.

     2. Configure the new HMAC secret in the `am.services.oauth2.jwt.authenticity.signing` secret label.

        Note that you may already have a secret configured for this secret label, because it is also used for signing certain OpenID Connect ID tokens and remote consent requests. Learn more in [Secret label default mappings](https://docs.pingidentity.com/pingam/8.1/security/secret-mapping.html#secret-mapping.html#secret-label-mappings) in AM's *Security guide*.

     3. Save your changes.

     For more information about secret stores, refer to [Secret stores](https://docs.pingidentity.com/pingam/8.1/security/secret-stores.html) in AM's *Security guide*.

  No further configuration is required in the agents.

---

---
title: Prepare for installation
description: "Prerequisites and setup steps before installing PingAM Web Agent: system requirements, OpenSSL libraries, downloading the agent, creating agent profiles, and verifying connectivity."
component: web-agents
version: 2026
page_id: web-agents:installation-guide:pre-installation
canonical_url: https://docs.pingidentity.com/web-agents/2026/installation-guide/pre-installation.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  before-install: Before you install
  pre-SSL-configuration: OpenSSL libraries
  downloading-agent: Download and unzip Web Agent
  preinstall-tasks: Pre-installation tasks
  create-agent-profiles: Create agent profiles
  create-agent-profile: Create an agent profile for a single agent instance
  create-agent-profile-mult-instances: Create an agent profile for multiple agent instances when post data preservation is enabled
  create-agent-group: Create an agent profile group
  agent-group-inherit: Inherit properties from an agent profile group
  authenticate_agents_to_the_identity_provider: Authenticate agents to the identity provider
  authenticate-agent-idc: Authenticate agents to Advanced Identity Cloud
  authenticate-agent-am: Authenticate agents to AM
  create-agent-tree: Create an Agent authentication tree
  check-agents-can-connect: Check agents can connect to the identity provider
---

# Prepare for installation

## Before you install

Consider the following before you install:

* Install AM and Web Agent in different servers.

* Make sure AM is running so that you can contact AM from the agent web server.

* Install the web server before you install the agent.

* Make sure OpenSSL or the Windows Secure Channel API (Schannel) is available before installing the agent. Unix-based agents support OpenSSL. Windows-based agents support OpenSSL and Schannel.

  Learn more about SSL requirements in [SSL requirements](https://docs.pingidentity.com/web-agents/release-notes/requirements.html#ssl_requirements) and required OpenSSL libraries in [OpenSSL libraries](#pre-SSL-configuration).

* Install only one Web Agent for each web server and configure as many agent instances as necessary.

* For environments with load balancers or reverse proxies, consider the communication between the agent and AM servers, and between the agent and the client. Configure both AM and the environment **before** you install the agent.

  Learn more in [Configure load balancers and reverse proxies](../user-guide/load-balancers-proxies.html).

### OpenSSL libraries

Before installing, make sure the OpenSSL libraries are located or referenced as follows:

| Operating System  | OpenSSL 3.x Library                           | Location or Variable                     |
| ----------------- | --------------------------------------------- | ---------------------------------------- |
| Linux             | * `libcrypto.so.3`(1)

* `libssl.so.3`(1)     | `$LD_LIBRARY_PATH` `$LD_LIBRARY_PATH_64` |
| Windows 32-bit    | - `libcrypto-3.dll`

- `libssl-3.dll`         | `%SYSTEM32%`                             |
| Windows 64-bit(2) | * `libcrypto-3.dll`

* `libssl-3.dll`         | `\windows\syswow64`                      |
|                   | - `libcrypto-3-x64.dll`

- `libssl-3-x64.dll` | `%SYSTEM32%`                             |

(1) The unversioned file (`libcrypto.so` or `libssl.so`) is used if the versioned file isn't found.\
(2) Windows 64-bit servers require both 32-bit and 64-bit OpenSSL libraries.

## Download and unzip Web Agent

Go to [Ping Identity Product Downloads](https://product-downloads.pingidentity.com) and download an agent based on your architecture and operating system requirements. Verify the checksum of the downloaded file against the checksum posted on the download page.

Unzip the file in the directory where you plan to store the agent configuration and log files. The following directories are extracted:

**Installation directories**

| Directory    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bin/`       | The installation and configuration program `agentadmin`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `config/`    | Configuration templates used by the `agentadmin` command during installation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `instances/` | Configuration files, and audit and debug logs for individual instances of the agents. The directory is empty when first extracted.&#xA;&#xA;Make sure the directory path, including the parent path, doesn't exceed 260 characters.                                                                                                                                                                                                                                                                                                                       |
| `legal/`     | Licensing information including third-party licenses.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `lib/`       | Shared libraries used by the agent.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `log/`       | Log files written during installation. The directory is empty when first extracted.When the agent is running, the directory can contain the following files:- The `system_n.log` file, where the agent logs information related to agent tasks running in the background. Web Agent timestamps events in coordinated universal time (UTC).

- (IIS and ISAPI agents only) The backup of the site and application configuration files created after running the `agentadmin -g` command.

- (IIS and ISAPI agents only) Files related to the agent caches. |
| `pdp-cache/` | POST data preservation cache. The agent stores POST data preservation files temporarily. To change the directory, configure [POST Data Storage Directory](../properties-reference/org.forgerock.agents.config.postdata.preserve.dir.html).                                                                                                                                                                                                                                                                                                                |

## Pre-installation tasks

1. In AM, add an agent profile as described in [Create agent profiles](#create-agent-profiles). The example in this guide uses an agent profile in the top-level realm, with the following values:

   * Agent ID: `web-agent`

   * Agent URL: `https://agent.example.com:443`

   * Server URL: `https://am.example.com:8443/am`

   * Password: `password`

2. In AM, add a policy set and policy as described in [Policies](https://docs.pingidentity.com/pingam/8.1/am-authorization/policies.html) in AM's *Authorization guide*. The example in this guide uses a policy set and policy in the top-level realm, with the following values:

   * Policy set:

     * Name: `PEP`

     * Resource Types: `URL`

   * Policy:

     * Name: `PEP-policy`

     * Resource Type: `URL`

     * Resource pattern: `*://*:*/*`

     * Resource value: `*://*:*/*`

     * Actions tab: Allow HTTP `GET` and `POST`

     * Subjects tab: All Authenticated Users.

   |   |                                                                                                                                                                                                                                                                                                                                                                                          |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When you use your own policy set instead of the default policy set, `iPlanetAMWebAgentService`, update the following properties in the agent profile:* [Policy Set](../properties-reference/org.forgerock.openam.agents.config.policy.evaluation.application.html)

   * [Policy Evaluation Realm](../properties-reference/org.forgerock.openam.agents.config.policy.evaluation.realm.html) |

3. Configure AM to protect the CDSSO cookie from hijacking. For more information, refer to [Restrict tokens for CDSSO session cookies](https://docs.pingidentity.com/pingam/8.1/security/enable-cdsso-cookie-hijacking-protection.html) in AM's *Security guide*.

4. Create a text file for the agent password, and protect it. For example, use commands similar to these, but use a strong password and store it in a secure place:

   * Unix

   * Windows

   ```
   $ cat > /secure-directory/pwd.txt
   password
   CTRL+D

   $ chmod 400 /secure-directory/pwd.txt
   ```

   ```
   C:> type > pwd.txt
   password
   CTRL+Z
   ```

   In Windows Explorer, right-click the password file, select Read-Only, and then click OK.

   |   |                                                                                                                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Although the agent accepts any password length and content, you are strongly encouraged to generate secure passwords. This can be achieved in various ways, for example, by using a password manager. |

5. If either of the following is true, set up the required environment variables:

   * AM is configured to perform client authentication

   * The agent web server is configured to validate AM's server certificate

   Learn more in [Environment variables](../user-guide/configure-envvars.html).

## Create agent profiles

Use Web Agent profiles to connect to and communicate with Advanced Identity Cloud or AM.

|   |                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can find additional details about creating an agent profile in Advanced Identity Cloud in [Create an agent profile in Advanced Identity Cloud](../identity-cloud-guide/installation.html#create-agent-profile). |

### Create an agent profile for a single agent instance

This section describes how to create an agent profile in the AM admin UI. Alternatively, create agent profiles by using the `/realm-config/agents/WebAgent/{id}` endpoint in the REST API. Learn more in [REST API explorer](https://docs.pingidentity.com/pingam/8.1/am-rest/about-api-explorer.html) in AM's *REST guide*.

1. In the AM admin UI, select Realms > *Realm Name* > Applications > Agents > Web, and add an agent using the following hints:

   * Agent ID

     The ID of the agent profile. This ID resembles a username and is used during the agent installation. For example, `MyAgent`.

     |   |                                                                                                                                          |
     | - | ---------------------------------------------------------------------------------------------------------------------------------------- |
     |   | When AM is not available, the related error message contains the agent profile name. Consider this in your choice of agent profile name. |

   * Agent URL

     The URL where the agent resides. Learn more in [Example installation for this guide](preface.html#preface-examples).

     In [centralized configuration mode](../user-guide/glossary.html#def-central-configuration-mode), the Agent URL populates the agent profile for services, such as notifications.

   * Server URL

     The full URL to an authorization server, such as AM. Learn more in [Example installation for this guide](preface.html#preface-examples).

     If the authorization server is deployed in a site configuration (behind a load balancer), enter the site URL.

     In [centralized configuration mode](../user-guide/glossary.html#def-central-configuration-mode), the Server URL populates the agent profile for use with login, logout, naming, and cross-domain SSO.

   * Password

     The password the agent uses to authenticate to an authorization server, such as AM. Use this password when installing an agent.

     |   |                                                                                                                                                                                                       |
     | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | Although the agent accepts any password length and content, you are strongly encouraged to generate secure passwords. This can be achieved in various ways, for example, by using a password manager. |

2. (Optional - From AM 7.5) Use AM's secret service to manage the agent profile password. If AM finds a matching secret in a secret store, it uses that secret instead of the agent password configured in Step 1.

   1. In the agent profile page, set a label for the agent password in Secret Label Identifier.

      AM uses the identifier to generate a secret label for the agent.

      The secret label has the format `am.application.agents.identifier.secret`, where *identifier* is the Secret Label Identifier.

      The Secret Label Identifier can contain only characters `a-z`, `A-Z`, `0-9`, and periods (`.`). It can't start or end with a period.

   2. Select Secret Stores and configure a secret store.

   3. Map the label to the secret. Learn more in AM's [Map and rotate secrets](https://docs.pingidentity.com/pingam/8.1/security/secret-mapping.html).

   Note the following points for using AM's secret service:

   * Set a Secret Label Identifier that clearly identifies the agent.

   * If you update the Secret Label Identifier:

     * If no other agent shares that secret mapping, AM updates any corresponding secret mapping for the previous identifier.

     * If another agent shares that secret mapping, AM creates a new secret mapping for the updated identifier and copies its aliases from the previously shared secret mapping.

   * If you delete the Secret Label Identifier, AM deletes any corresponding secret mapping for the previous identifier, provided no other agent shares that secret mapping.

   * When you rotate a secret, update the corresponding mapping.

### Create an agent profile for multiple agent instances when post data preservation is enabled

By default, the POST data preservation load balancer cookie name and value is set by the agent profile. Therefore, each agent instance behind a load balancer requires its own agent profile.

In scalable environments, such as deployments with load balancing, or environments that run Kubernetes, resources are dynamically created and destroyed.

To facilitate the rapid creation and destruction of agent instances when post data preservation is enabled, set the POST data preservation configuration in `agent.conf` to map one agent profile to multiple agent instances.

The configuration in `agent.conf` overrides the configuration in AM for the following properties:

* [POST Data Sticky Load Balancing Mode](../properties-reference/com.sun.identity.agents.config.postdata.preserve.stickysession.mode.html)

* [POST Data Sticky Load Balancing Value](../properties-reference/com.sun.identity.agents.config.postdata.preserve.stickysession.value.html)

You can find an example in [Map one agent profile to multiple agent instances when POST data preservation is enabled](../user-guide/load-balancers-proxies.html#lb-POST-data-12all).

### Create an agent profile group

Use agent profile groups when you set up multiple agents, and want to inherit settings from the group.

1. In the AM admin UI, go to Realms > *Realm Name* > Applications > Agents > Web.

2. Select the Groups tab, and add a group with the following settings:

   * Group ID: A name for the profile group.

   * Server URL: The URL of the AM server in which to store the profile.

### Inherit properties from an agent profile group

1. Set up an agent profile and agent profile group, as described in [Create an agent profile for a single agent instance](#create-agent-profile) and [Create an agent profile group](#create-agent-group).

2. In the AM admin UI, select your agent profile.

3. On the Global tab, select Group, and select a group from the drop-down menu. The agent profile is added to the group.

4. For each setting in the Global tab, select or deselect the [icon: lock, set=fa]icon:

   * [icon: lock, set=fa]: Inherit this setting from the group

   * [icon: unlock, set=fa]: Do not inherit this setting from the group

## Authenticate agents to the identity provider

### Authenticate agents to Advanced Identity Cloud

Advanced Identity Cloud provides a [journey](https://docs.pingidentity.com/pingoneaic/realms/journeys.html) called `Agent`. The `Agent` journey validates the agent credentials with an [Agent Data Store Decision](https://docs.pingidentity.com/auth-node-ref/latest/agent-data-store-decision.html) node.

All Web Agent, Java Agent and PingGateway profiles use the `Agent` tree. Don't change its configuration.

### Authenticate agents to AM

* AM 8 and later

  AM 8 and later provide an [authentication tree](https://docs.pingidentity.com/pingam/8.1/am-authentication/authn-introduction-authn.html#default-trees) called `Agent` (unless you upgrade from an earlier version using the file-based configuration). The `Agent` tree validates the agent credentials with an [Agent Data Store Decision](https://docs.pingidentity.com/auth-node-ref/8.1/agent-data-store-decision.html) node.

  All Web Agent, Java Agent and PingGateway profiles use the `Agent` tree. Don't change its configuration.

* AM 7.2, 7.3, 7.4, and 7.5

  With earlier versions of AM, you have the choice of authenticating to AM using the `Agent` tree (default) or the deprecated authentication module. To change how the agent authenticates to AM, set the [Agent Authentication Mode](../properties-reference/com.forgerock.agents.config.agent.auth.mode.html) property.

  If you use the `Agent` tree, you must create it as explained in the following section.

#### Create an `Agent` authentication tree

The `Agent` tree must pass the agent credentials to the Agent Data Store Decision node.

When you define a tree in AM, that same tree is used for all instances of Web Agent, Java Agent and PingGateway. Consider this point if you change the tree configuration.

1. On the Realms page of the AM admin UI, choose the realm in which to create the authentication tree.

2. On the Realm Overview page, click Authentication > Trees > Create tree.

3. Create a tree named `Agent`.

   The authentication tree designer is displayed, with the `Start` entry point connected to the `Failure` exit point, and a `Success` node.

   The authentication tree designer provides the following features on the toolbar:

   | Button                                                   | Usage                                                               |
   | -------------------------------------------------------- | ------------------------------------------------------------------- |
   | ![Trees auto layout](_images/icon-trees-auto-layout.png) | Lay out and align nodes according to the order they are connected.  |
   | ![Trees full screen](_images/icon-trees-full-screen.png) | Toggle the designer window between normal and full-screen layout.   |
   | ![Trees delete node](_images/icon-trees-delete-node.png) | Remove the selected node. The `Start` entry point can't be deleted. |

4. Using the Filter bar, find and then drag the following nodes from the Components panel into the designer area:

   * [Zero Page Login Collector](https://docs.pingidentity.com/auth-node-ref/8.1/zero-page-login-collector.html) node to check whether the agent credentials are provided in the incoming authentication request and use their values in the following nodes.

     This node is required for compatibility with Java Agent and Web Agent.

   * [Page](https://docs.pingidentity.com/auth-node-ref/8.1/page.html) node to collect the agent credentials if they aren't provided in the incoming authentication request and use their values in the following nodes.

   * [Agent Data Store Decision](https://docs.pingidentity.com/auth-node-ref/8.1/agent-data-store-decision.html) node to verify that the agent credentials match the registered Web Agent profile.

   |   |                                                                                                                                                              |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Many nodes can be configured in the panel on the right side of the page. Unless otherwise stated, don't configure the nodes and use only the default values. |

5. Drag the following nodes from the Components panel into the Page node:

   * Username Collector node, to prompt the user to enter their username

   * Password Collector node,to prompt the user to enter their password

6. Connect the nodes as follows and save the tree:

   ![A tree that can be used to authenticate an agent to AM.](_images/agenttree-am.png)

## Check agents can connect to the identity provider

You can authenticate as the agent you created a profile for in Advanced Identity Cloud or AM to check the agent can connect successfully. A successful connection proves the agent can connect to Advanced Identity Cloud or AM, their credentials are correct, and a valid agent profile exists.

Authenticate as follows:

```none
$ curl \
--request POST \
--header "X-OpenAM-Username: agent-id" \ (1)
--header "X-OpenAM-Password: password" \ (2)
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=2.1" \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/authenticate?auth-service' (3)
```

|       |                                                                                                                                                                                                                                                                                             |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1** | Replace *agent-id* with the ID of the agent profile you created.                                                                                                                                                                                                                            |
| **2** | Replace *password* with the agent password.                                                                                                                                                                                                                                                 |
| **3** | Replace *auth-service* with either `authIndexType=module&authIndexValue=Application` or `authIndexType=service&authIndexValue=Agent` depending on whether you [authenticate](#authenticate-agent-idc) using the default non-configurable authentication module or a journey called `Agent`. |

If authentication is successful, the response includes the `tokenId` that corresponds to the agent session and the URL to which the agent would normally be redirected. For example:

```json
{
     "tokenId":"AQIC5wM...​TU3OQ*",
     "successUrl":"/am/console",
     "realm":"/alpha"
}
```

---

---
title: Remove Web Agent
description: Remove PingAM Web Agent instances from Apache HTTP Server, IIS, ISAPI, and NGINX Plus using the agentadmin command.
component: web-agents
version: 2026
page_id: web-agents:installation-guide:uninstallation
canonical_url: https://docs.pingidentity.com/web-agents/2026/installation-guide/uninstallation.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  uninstall-apache-agent: Remove Apache Web Agent
  uninstall-iis-agent: Remove IIS or ISAPI Web Agent
  remove-iis-single: Remove a single instance of IIS or ISAPI Web Agent
  remove-iis-all: Remove all instances of IIS or ISAPI Web Agent
  uninstall-nginx-agent: Remove NGINX Plus Web Agent
---

# Remove Web Agent

## Remove Apache Web Agent

1. Shut down Apache HTTP Server where the agent is installed.

2. Run `agentadmin --l` to output a list of the installed web agent configuration instances.

   Note the ID of the Web Agent instance to remove.

3. Run `agentadmin --r`, and specify the ID of the web agent configuration instance to remove. A warning is displayed. Enter `yes` to proceed with removing the configuration instance.

   ```
   $ ./agentadmin --r agent_1

   Warning! This procedure will remove all Web Agent references from
   a Web server configuration. In case you are running Web Agent in a
   multi-virtualhost mode, an uninstallation must be carried out manually.

   Continue (yes/no): [no]: yes

   Removing agent_1 configuration…​
   Removing agent_1 configuration…​ Done.
   ```

   |   |                                                                                                                                                                  |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To silently remove the agent, you can echo the answer and pipe it to the `agentadmin --r` command. For example:```bash
   $ echo yes | ./agentadmin --r agent_1
   ``` |

4. Start the Apache HTTP Server.

## Remove IIS or ISAPI Web Agent

### Remove a single instance of IIS or ISAPI Web Agent

Perform the steps in this procedure to remove :

1. Log on to Windows as a user with administrator privileges.

2. Run `agentadmin.exe --l` to output a list of the installed agent configuration instances.

   ```
   c:\web_agents\iis_agent\bin> agentadmin.exe --l
   agentadmin.exe --l
   Web Agent configuration instances:

   id:            agent_1
   configuration: c:\web_agents\iis_agent\bin\..\instances\agent_1
   server/site:   2.2.1
   ```

   Note the ID of the Web Agent instance to remove.

3. Run `agentadmin.exe --r`, specifying the ID of the Web Agent instance to remove.

   ```
   c:\web_agents\iis_agent\bin> agentadmin.exe --r agent_1
   Removing agent_1 configuration…​
   Removing agent_1 configuration…​ Done.
   ```

   |   |                                                                                                                                                                                |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | The `--r` option does not remove the agent libraries. To remove all agent instances and libraries, refer to [Remove all instances of IIS or ISAPI Web Agent](#remove-iis-all). |

   |   |                                                                                                                                                                                               |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To silently remove the agent, you can echo the answer and pipe it to the `agentadmin --r` command. For example:```bash
   c:\web_agents\iis_agent\bin> echo yes | agentadmin.exe --r agent_1
   ``` |

### Remove all instances of IIS or ISAPI Web Agent

1. Log on to Windows as a user with administrator privileges.

2. Run `agentadmin --g`. A warning is displayed. Enter `yes` to proceed with removing the configuration instance.

   ```
   c:\web_agents\iis_agent\bin> agentadmin.exe --g

   Warning! This procedure will remove all Web Agent references from
   IIS Server configuration.

   Continue (yes/no): [no]: yes
   Removing agent module from IIS Server configuration…​
   Removing agent module from IIS Server configuration…​ Done.
   ```

## Remove NGINX Plus Web Agent

1. Shut down the NGINX Plus server where the agent is installed.

2. Run the `agentadmin --l` command to output a list of installed agent instances. For example:

   ```
   $ ./agentadmin --l
   OpenAM Web Agent configuration instances:

   id:            agent_1
   configuration: /web_agents/nginx36_agent/instances/agent_1
   server/site:   /etc/nginx/nginx.conf

   id:            agent_2
   configuration: /web_agents/nginx36_agent/instances/agent_2
   server/site:   /etc/nginx/nginx.conf

   id:            agent_3
   configuration: /web_agents/nginx36_agent/instances/agent_3
   server/site:   /etc/nginx/nginx.conf
   ```

   Note the ID of the Web Agent instance to remove.

3. Run the `agentadmin --r` command, specifying the ID of the agent instance to remove. A warning is displayed. Enter `yes` to remove the instance.

   ```
   $ ./agentadmin --r agent_1
   Warning! This procedure will remove the Web Agent configuration for agent_1
   but not references to it your NGINX server configuration file: /etc/nginx/nginx.conf.

   Continue (yes/no): [no]: yes

   In order to complete the removal of the agent from your NGINX installation,
   remove the openam_agent_ directives for this agent
   from your NGINX configuration file: /etc/nginx/nginx.conf
   and, if this is the only agent in the installation,
   remove the load_module directive for the openam_agent_auth_module
   in the NGINX configuration file.

   Please press any key to continue.


   Removing agent_1 configuration…​ Done.
   ```

   |   |                                                                                                                                                                  |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To silently remove the agent, you can echo the answer and pipe it to the `agentadmin --r` command. For example:```bash
   $ echo yes | ./agentadmin --r agent_1
   ``` |

4. Edit the NGINX Plus configuration file that contains the context protected by the removed web agent instance.

5. Delete the `openam_agent_` directives from the context.

   If this is the last agent in the NGINX Plus server, remove the directive that loads the `openam_ngx_auth_module.so` library.

6. Restart the NGINX Plus server.

---

---
title: Secure connections
description: Configure TLS for PingAM Web Agent using OpenSSL or Windows Schannel, including server certificate validation, client certificate authentication, and FIPS 140 compliance.
component: web-agents
version: 2026
page_id: web-agents:installation-guide:secure-connections
canonical_url: https://docs.pingidentity.com/web-agents/2026/installation-guide/secure-connections.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  securing-agent-am-communication: Secure communication between the agent and AM
  openssl-config: Secure communication with OpenSSL
  configure-server-validation-openssl: Configure server certificate validation using OpenSSL
  configure-client-cert-auth-openssl: Configure client certificate authentication using OpenSSL
  native-win-ssl-config: Secure communication with Schannel
  configure-server-validation-schannel: Configure server certificate validation using Schannel
  configure-client-cert-auth-schannel: Configure client certificate authentication using Schannel
  fips: FIPS 140 compliance
  fips-unix: Unix-based agents
  fips-windows: Windows-based agents
---

# Secure connections

## Secure communication between the agent and AM

|   |                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Be aware of security breaches and vulnerabilities. Make sure your environment isn't using outdated, insecure protocols, such as SSL 3.0, TLS 1.0, and others. |

To secure communications, configure the agent to validate server certificates installed in the server where AM runs and to present a client certificate to AM. Learn more in AM's [Secure HTTP and LDAP connections](https://docs.pingidentity.com/pingam/8.1/security/secure-connections.html).

To facilitate integration and test, Web Agent is configured by default to trust any server certificate. Test client certificates aren't provided or configured.

To send cookies only when the communication channel is secure, set [Enable Cookie Security](../properties-reference/com.sun.identity.agents.config.cookie.secure.html) to `true`.

## Secure communication with OpenSSL

Unix-based agents support OpenSSL libraries. Windows-based agents can use OpenSSL or the [Windows Secure Channel API (Schannel)](post-installation.html#native-win-ssl-config).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you want to use OpenSSL for the IIS, ISAPI, or Windows Apache agent, configure the agent to use OpenSSL before continuing:- Make sure the [OpenSSL libraries](pre-installation.html#pre-SSL-configuration) are in the correct location.

- Disable Schannel by setting the [Enable OpenSSL to Secure Internal Communications](../properties-reference/org.forgerock.agents.config.secure.channel.disable.html) property to `true`. |

### Configure server certificate validation using OpenSSL

Perform the following steps to configure the agent to validate AM's or Advanced Identity Cloud's server certificate:

1. Set the [Server Certificate Trust](../properties-reference/com.sun.identity.agents.config.trust.server.certs.html) property to `false`.

   |   |                                                                                                                                                                 |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The [Server Certificate Trust](../properties-reference/com.sun.identity.agents.config.trust.server.certs.html) property should always be `false` in production. |

2. Set the [CA Certificate File Name](../properties-reference/com.forgerock.agents.config.cert.ca.file.html) property to the filename of the CA bundle for your system. The exact location and name of the CRT file varies by operating system. For example, for Ubuntu, it's `/etc/ssl/certs/ca-certificates.crt`.

3. Set the [OpenSSL Certificate Verification Depth](../properties-reference/org.forgerock.agents.config.cert.verify.depth.html) property to the level of certificate validation required in your environment.

4. Restart the agent.

### Configure client certificate authentication using OpenSSL

When AM or Advanced Identity Cloud are configured to perform client authentication, you must configure the agent to present its client certificates as follows:

1. Create a PEM file that contains the certificate chain for the agent. For example, `client-cert.pem`.

2. Create a PEM file that contains the private key corresponding to the certificate. For example, `client-private-key.pem`.

3. Set the [Public Client Certificate File Name](../properties-reference/com.forgerock.agents.config.cert.file.html) property to the file containing the certificate chain. For example:

   * Unix

   * Windows

   ```
   com.forgerock.agents.config.cert.file = /opt/certificates/client-cert.pem
   ```

   ```
   com.forgerock.agents.config.cert.file = C:\Certificates\client-cert.pem
   ```

4. Set the [Private Client Certificate File Name](../properties-reference/com.forgerock.agents.config.cert.key.html) property to the file containing the client certificate private key. For example:

   * Unix

   * Windows

   ```
   com.forgerock.agents.config.cert.key = /opt/certificates/client-private-key.pem
   ```

   ```
   com.forgerock.agents.config.cert.key = C:\Certificates\client-private-key.pem
   ```

5. If the private key is password-protected:

   1. Obfuscate the password using the `agentadmin --p` command. For example:

      * Unix

      * Windows

      ```
      $ /path/to/web_agents/agent_type/bin/> agentadmin --p encryption-Key "cat certificate_password.file"
      Encrypted password value: zck+6RKqjtc=
      ```

      ```
      C:\path\to\web_agents\agent_type\bin> agentadmin.exe --p encryption-Key "Certificate_File_Password"
      Encrypted password value: zck+6RKqjtc=
      ```

      Where encryption-Key is the value of the [Agent Profile Password Encryption Key](../properties-reference/com.sun.identity.agents.config.key.html) property.

   2. Set the [Private Key Password](../properties-reference/com.forgerock.agents.config.cert.key.password.html) property to the encrypted password value. For example:

      ```none
      com.forgerock.agents.config.cert.key.password = zck+6RKqjtc=
      ```

6. Restart the agent.

|   |                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Use the [`agentadmin --Vi` command](agentadmin.html#vi) to validate the TLS connection settings between the agent and AM or Advanced Identity Cloud. |

## Secure communication with Schannel

By default, IIS, ISAPI, and Apache for Windows agents use the Windows built-in Secure Channel API (Schannel). Alternatively, you can use OpenSSL as described in [Secure internal communication with OpenSSL](post-installation.html#openssl-config).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Before continuing, make sure the agent is configured to use Schannel:- If this is a new installation, Windows-based agents use Schannel by default.

- If you've previously configured the IIS, ISAPI, or Apache agent to use OpenSSL libraries, set the [Enable OpenSSL to Secure Internal Communications](../properties-reference/org.forgerock.agents.config.secure.channel.disable.html) property to `false`. |

### Configure server certificate validation using Schannel

Perform the following steps to configure the agent to validate AM's or Advanced Identity Cloud's server certificate:

1. Set the [Server Certificate Trust](../properties-reference/com.sun.identity.agents.config.trust.server.certs.html) property to `false`.

   |   |                                                                                                                                                                 |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The [Server Certificate Trust](../properties-reference/com.sun.identity.agents.config.trust.server.certs.html) property should always be `false` in production. |

2. If you're using self-signed certificates or the server certificate is issued from a new CA, add the certificates required to validate AM's or Advanced Identity Cloud's server certificate to the Windows certificate store. For example, to use PowerShell, add certificates to the following locations:

   * **Root CA certificates**: add them to the `Cert:\LocalMachine\Root` location.

   * **Intermediate CA certificates**: add them to the `Cert:\LocalMachine\Ca` location.

3. Restart the agent.

### Configure client certificate authentication using Schannel

When AM or Advanced Identity Cloud are configured to perform client authentication, you must configure the agent to present its client certificates using one of the following methods.

The method you use depends on whether you are loading the client certificate through the Windows certificate store or through a PFX certificate:

* Agent authenticates using a client certificate stored in the Windows Certificate store

  Configure the agent to present its client certificate as follows:

  1. Import the client certificate chain and private key into the Windows certificate store. For example, for PowerShell, import them to `Cert:\LocalMachine\My`.

  2. Set the [Public Client Certificate Friendly Name](../properties-reference/com.forgerock.agents.config.win.clientcert.friendly.name.html) property to the friendly name of the client certificate chain. For example:

     ```none
     com.forgerock.agents.config.win.clientcert.friendly.name = agent.example.com
     ```

     ![Friendly name of the client certificate imported into the Windows certificate store.](_images/windows-cert-friendly-name.png)

  3. Restart the agent.

* Agent authenticates using a PFX file that contains the certificate chain

  Configure the agent to present its client certificate as follows:

  1. Create a Personal Information Exchange (PFX) file that contains the certificate chain for the agent and its private key. For example, `client.pfx` .

  2. Set the [Public Client Certificate File Name](../properties-reference/com.forgerock.agents.config.cert.file.html) property to the PFX file you just created. For example:

     ```none
     com.forgerock.agents.config.cert.file = C:\Certificates\client.pfx
     ```

  3. Obfuscate the certificate password using the `agentadmin --p` command. For example:

     ```
     C:\path\to\web_agents\agent_type\bin> agentadmin.exe --p encryption-Key "Certificate_File_Password"
     Encrypted password value: zck+6RKqjtc=
     ```

     Where encryption-Key is the value of the [Agent Profile Password Encryption Key](../properties-reference/com.sun.identity.agents.config.key.html) property.

  4. Set the [Private Key Password](../properties-reference/com.forgerock.agents.config.cert.key.password.html) property to the encrypted password value. For example:

     ```none
     com.forgerock.agents.config.cert.key.password = zck+6RKqjtc=
     ```

  5. Restart the agent.

|   |                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Use the [`agentadmin --Vi` command](agentadmin.html#vi) to validate the TLS connection settings between the agent and AM or Advanced Identity Cloud. |

## FIPS 140 compliance

Managing FIPS is a complicated process that requires specialist knowledge. Unless you have to be FIPS compliant, it's best not to use FIPS mode.

### Unix-based agents

|   |                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The OpenSSL version is important. Web Agents operating in FIPS mode only work with OpenSSL 3.x. Currently, OpenSSL 3.1.2 is the only FIPS module that's FIPS 140-3 validated. All other OpenSSL FIPS modules are FIPS 140-2 validated. |

To achieve [FIPS 140–3](https://csrc.nist.gov/publications/detail/fips/140/3/final) compliance, configure the FIPS module using OpenSSL 3.1.2, which is a FIPS 140-3 compliant security provider. The FIPS 140-3 security provider can then be used with any OpenSSL 3.x version. Learn more in [OpenSSL Downloads](https://openssl-library.org/source/) and [OpenSSL 3.1.2 security policy](https://openssl-library.org/source/fips-doc/openssl-3.1.2-security-policy-2023-12-29.pdf).

The agent automatically enables FIPS mode when it detects that the OpenSSL FIPS security provider is configured.

You can configure the FIPS module in OpenSSL or in your operating system if your vendor provides OpenSSL 3.x and supports FIPS mode.

Find more information in these links:

* [fips\_module](https://docs.openssl.org/master/man7/fips_module) in the OpenSSL documentation

* [FIPS README](https://github.com/openssl/openssl/blob/master/README-FIPS.md) in the OpenSSL repository

* [Switching RHEL to FIPS mode](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/switching-rhel-to-fips-mode_security-hardening#switching-rhel-to-fips-mode_security-hardening) in the RHEL documentation

* [FIPS 140-3 Compliance in Oracle Linux 9](https://docs.oracle.com/en/operating-systems/oracle-linux/9/security/fips_compliance.html) in the Oracle documentation

* [FIPS for Ubuntu 22.04](https://ubuntu.com/security/certifications/docs/2204/fips) in the Ubuntu documentation

* [Enabling compliance with FIPS 140-3](https://documentation.suse.com/sles/15-SP6/html/SLES-all/cha-security-fips.html) in the SUSE Linux documentation

### Windows-based agents

|   |                                                          |
| - | -------------------------------------------------------- |
|   | Windows Servers are currently only FIPS 140-2 compliant. |

To achieve [FIPS 140–2](https://csrc.nist.gov/pubs/fips/140-2/upd2/final) compliance, enable FIPS compliant algorithms.

The agent automatically enables FIPS mode when it detects the use of FIPS compliant algorithms.

You can configure Windows to use FIPS compliant algorithms by setting the Local Security Policy:

1. Go to Local Security Policy > Local Policies > Security Options > System cryptography > Use FIPS compliant algorithms for encryption, hashing, and signing and select the `Enabled` option.

2. Click Apply.

This enables FIPS mode using Schannel.

|   |                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------- |
|   | Use the [`agentadmin --Vi` command](agentadmin.html#vi) to verify that the agent is running in FIPS mode. |