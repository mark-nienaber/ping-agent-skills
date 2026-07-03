---
title: agentadmin command
description: Reference for the agentadmin command-line tool to install, uninstall, list, encrypt, and manage PingAM Java Agent instances.
component: java-agents
version: 2026
page_id: java-agents:installation-guide:agentadmin
canonical_url: https://docs.pingidentity.com/java-agents/2026/installation-guide/agentadmin.html
section_ids:
  agentadmin-install: "--install"
  forceinstall: "--forceInstall"
  custom_install_custom: "--custom-install, --custom"
  uninstall_r: "--uninstall, -r"
  uninstallall: "--uninstallAll"
  version_v: "--version, -v"
  listagents_list_l: "--listAgents, --list, -l"
  agentinfo_info: "--agentInfo, --info"
  encrypt: "--encrypt"
  amadmin-getEncryptKey: "--getEncryptKey, --getKey"
  agentadmin-key: "--key"
  agentadmin-d: "--d, -d, --decryptAgent, --decrypt"
  decryptpassword: "--decryptPassword"
  agentadmin-raw-encrypt: "--raw-encrypt"
---

# agentadmin command

The `agentadmin` command manages Java Agent installation. It requires a Java runtime environment. The command supports the following options:

## `--install`

Installs a new agent instance.

Usage (non-FIPS install): `agentadmin --install [--useResponse | --saveResponse file-name]`

Usage (FIPS install): `agentadmin --fips-only --fips-jar-dir=directory --security-properties=file --key-digest=digest --install`

|   |                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | With the `agentadmin.bat` script, the order of the options is important. The FIPS related options must be specified before the `--install` option or any other options, otherwise they are ignored. |

Before installation, shut down the agent container. If a service on an agent URL is responding, the installer stops with an error.

When the command is used without options, the installation process prompts for the following information:

* Information about the container installation.

* The URL of the AM instance. The agent confirms that it can log in to AM by using the profile name and password provided during installation. If unsuccessful, the installation stops with an error.

* The URL of the agent instance. The agent confirms that it can access the host and port of the URL. If the port is busy, it prompts the user to stop the container.

* The agent profile name in AM.

* The AM realm containing the agent profile.

* The path to the file containing the agent password.

  * `--useResponse`

    Run in silent mode by specifying all the responses in the *file-name* file. When this option is used, `agentadmin` runs in non-interactive mode.

  * `--saveResponse`

    Save all the supplied responses in a response file specified by *file-name*.

  * `--fips-only`

    Sets the `-Dorg.bouncycastle.fips.approved_only=true` property, which means only algorithms approved by FIPS can be used.

  * `--fips-jar-dir`

    Indicates the location of the FIPS `.jar` files in *directory*.

  * `--key-digest`

    Uses the key digest specified by *digest* for FIPS.

    Possible values are `SHA1`, `SHA256`, `SHA384` or `SHA512`.

  * `--security-properties`

    Uses the custom `security-properties` file specified by *file-name* for FIPS instead of the default file.

## `--forceInstall`

Installs a new agent instance, without checking the AM URL or agent URL.

Use this option in deployments with load balancers or reverse proxies, where the URL of the agent and AM can be concealed.

Usage (non-FIPS install): `agentadmin --forceInstall [--useResponse | --saveResponse file-name]`

Usage (FIPS install): `agentadmin --fips-only --fips-jar-dir=directory --security-properties=file --key-digest=digest --forceinstall`

|   |                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | With the `agentadmin.bat` script, the order of the options is important. The FIPS related options must be specified before the `--forceinstall` option or any other options, otherwise they are ignored. |

Before installation, shut down the agent container. If a service on an agent URL is responding, the installer stops with an error.

When the command is used without options, the installation process prompts for the following information:

* Information about the container installation.

* The URL of the AM instance. The agent confirms that it can log in to AM by using the profile name and password provided during installation. If unsuccessful, the installation stops with an error.

* The URL of the agent instance. The agent confirms that it can access the host and port of the URL. If the port is busy, it prompts the user to stop the container.

* The agent profile name in AM.

* The AM realm containing the agent profile.

* The path to the file containing the agent password.

  * `--useResponse`

    Run in silent mode by specifying all the responses in the *file-name* file. When this option is used, `agentadmin` runs in non-interactive mode.

  * `--saveResponse`

    Save all the supplied responses in a response file specified by *file-name*.

  * `--fips-only`

    Sets the `-Dorg.bouncycastle.fips.approved_only=true` property, which means only algorithms approved by FIPS can be used.

  * `--fips-jar-dir`

    Indicates the location of the FIPS `.jar` files in *directory*.

  * `--key-digest`

    Uses the key digest specified by *digest* for FIPS.

    Possible values are `SHA1`, `SHA256`, `SHA384` or `SHA512`.

  * `--security-properties`

    Uses the custom `security-properties` file specified by *file-name* for FIPS instead of the default file.

## `--custom-install`, `--custom`

Installs a new agent instance, specifying advanced configuration options.

Usage (non-FIPS install): `agentadmin --custom-install [--useResponse | --saveResponse file-name]`

Usage (FIPS install): `agentadmin --fips-only --fips-jar-dir=directory --security-properties=file --key-digest=digest --custom-install`

|   |                                                                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | With the `agentadmin.bat` script, the order of the options is important. The FIPS related options must be specified before the `--custom-install` option or any other options, otherwise they are ignored. |

* `--useResponse`

  Run in silent mode by specifying all the responses in the *file-name* file. When this option is used, `agentadmin` runs in non-interactive mode.

* `--saveResponse`

  Save all the supplied responses in a response file specified by *file-name*.

* `--fips-only`

  Sets the `-Dorg.bouncycastle.fips.approved_only=true` property, which means only algorithms approved by FIPS can be used.

* `--fips-jar-dir`

  Indicates the location of the FIPS `.jar` files in *directory*.

* `--key-digest`

  Uses the key digest specified by *digest* for FIPS.

  Possible values are `SHA1`, `SHA256`, `SHA384` or `SHA512`.

* `--security-properties`

  Uses the custom `security-properties` file specified by *file-name* for FIPS instead of the default file.

## `--uninstall`, `-r`

Uninstalls an existing agent instance.

Usage: `agentadmin --uninstall [--useResponse | --saveResponse file-name]`

* `--useResponse`

  Run in silent mode by specifying all the responses in the *file-name* file. When this option is used, `agentadmin` runs in non-interactive mode.

* `--saveResponse`

  Save all the supplied responses in a response file specified by *file-name*.

## `--uninstallAll`

Uninstalls all agent instances.

Usage: `agentadmin --uninstallAll`

## `--version`, `-v`

Displays the agent version.

Usage: `agentadmin --version`

## `--listAgents`, `--list`, `-l`

Displays information about all configured agents.

Usage: `agentadmin --listAgents`

## `--agentInfo`, `--info`

Displays information about the agent corresponding to the specified *agent-id*.

Usage: `agentadmin --agentInfo agent-id`

Example: `agentadmin --agentInfo agent_001`

## `--encrypt`

Encrypts a given string.

Usage: `agentadmin --encrypt agent-instance password-file`

* *agent-instance*

  Agent instance identifier. The encryption functionality requires the use of agent instance specific encryption key present in its configuration file.

* *password-file*

  File containing a password in clear text to encrypt.

## `--getEncryptKey`, `--getKey`

Generates an agent encryption key of 40 characters long.

Usage: `agentadmin --getEncryptKey`

## `--key`

Generates an agent encryption key of the specified length. For security, generate keys that are about 80 characters long.

Usage: `agentadmin --key key-length`

## `--d`, `-d`, `--decryptAgent`, `--decrypt`

Reveals the agent password in clear text, for the agent corresponding to the specified *agent-id*.

Usage: `agentadmin --d [agent-id]`

Example: `agentadmin --d Agent_001`

* *agent-id*

  The agent instance. Default: `Agent_001`.

## `--decryptPassword`

Decrypts the agent password, for the agent corresponding to the specified *agent-id*.

Usage: `agentadmin --decryptPassword encrypted-password encryption-key`

* *encrypted-password*

  Encrypted agent password.

* *encryption-key*

  Key used to encrypt the agent password.

## `--raw-encrypt`

Encrypts the agent password without requiring the agent to be installed first.

Usage: `agentadmin --raw-encrypt --key-file [--password-file] [--out]`

* *\--key-file*

  Path and name of the encryption key.

  To generate a key, use `agentadmin getEncryptKey` or `agentadmin getKey`.

  Required: If the key isn't provided or is too short, an error occurs.

* *\--password-file*

  File containing a password in clear text to encrypt.

  Optional: If not provided, `agentadmin` prompts for the password.

* *\--out*

  Path and name of the file containing the resulting encrypted password.

  Optional: If not provided, the encrypted result is written to the console output.
