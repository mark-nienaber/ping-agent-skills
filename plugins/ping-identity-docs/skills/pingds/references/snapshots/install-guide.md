---
title: File layout
description: Reference for the files and directories that PingDS creates when you install and run the server.
component: pingds
version: 8.1
page_id: pingds:install-guide:file-layout
canonical_url: https://docs.pingidentity.com/pingds/8.1/install-guide/file-layout.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Install", "LDAP"]
---

# File layout

DS software installs and creates the following files and directories. The following table is not meant to be exhaustive.

| File or directory                       | Description                                                                                                                                                                                                                                                                   |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bak`                                   | Directory intended for local backup data.                                                                                                                                                                                                                                     |
| `bat`                                   | Windows command-line tools.                                                                                                                                                                                                                                                   |
| `bin`                                   | Linux command-line tools.                                                                                                                                                                                                                                                     |
| `changelogDb`                           | Backend for replication changelog data.                                                                                                                                                                                                                                       |
| `classes`                               | Directory added to the server classpath, permitting individual classes to be patched.                                                                                                                                                                                         |
| `config`                                | (Optionally) immutable server configuration files.                                                                                                                                                                                                                            |
| `config/audit-handlers`                 | Templates for configuring external Common Audit event handlers.                                                                                                                                                                                                               |
| `config/config.ldif`                    | LDIF representation of current DS server configuration.                                                                                                                                                                                                                       |
| `config/keystore` `config/keystore.pin` | Keystore and password (`.pin`) files for servers using PKI based on a deployment ID and password.                                                                                                                                                                             |
| `config/MakeLDIF`                       | Templates for use with the `makeldif` LDIF generation tool.                                                                                                                                                                                                                   |
| `db`                                    | Default directory for backend database files.For details, refer to [Data storage](../config-guide/import-export.html).                                                                                                                                                        |
| `extlib`                                | Directory for additional .jar files used by your custom plugins.If the instance path is not the same as the binaries, copy additional files into the `instance-path/extlib/` directory.                                                                                       |
| `import-tmp`                            | Working directory used when importing LDIF data.                                                                                                                                                                                                                              |
| `ldif`                                  | Directory for saving LDIF export files.                                                                                                                                                                                                                                       |
| `legal-notices`                         | License information.                                                                                                                                                                                                                                                          |
| `lib`                                   | Scripts and libraries shipped with DS servers.                                                                                                                                                                                                                                |
| `lib/extensions`                        | Directory for custom plugins.                                                                                                                                                                                                                                                 |
| `locks`                                 | Lock files that prevent more than one process from using the same backend.                                                                                                                                                                                                    |
| `logs`                                  | Access, errors, and audit logs.                                                                                                                                                                                                                                               |
| `logs/server.pid`                       | Contains the process ID for a running server.                                                                                                                                                                                                                                 |
| `README`                                | About DS servers.                                                                                                                                                                                                                                                             |
| `samples`(1)                            | Samples for use with DS servers, such as:- A sample `Dockerfile` and related files for building custom DS Docker images.

- A sample Grafana dashboard demonstrating how to graph DS server metrics stored in a Prometheus database.

- Sample server plugins and extensions. |
| `setup`                                 | Linux setup tool.                                                                                                                                                                                                                                                             |
| `setup.bat`                             | Windows setup tool.                                                                                                                                                                                                                                                           |
| `template`                              | Templates for setting up a server instance.                                                                                                                                                                                                                                   |
| `template/setup-profiles`               | Profile scripts to configure directory servers for specific use cases.                                                                                                                                                                                                        |
| `upgrade`                               | Linux upgrade tool.                                                                                                                                                                                                                                                           |
| `upgrade.bat`                           | Windows upgrade tool.                                                                                                                                                                                                                                                         |
| `var`                                   | Files the DS server writes to during operation.Do not modify or move files in the `var` directory.                                                                                                                                                                            |
| `var/archived-configs`                  | Snapshots of the main server configuration file, `config/config.ldif`.The server writes a compressed snapshot file when the configuration is changed.                                                                                                                         |
| `var/config.ldif.startok`               | The most recent version of the main server configuration file that the server successfully started with.                                                                                                                                                                      |

(1) The samples are provided on an "as is" basis. Ping Identity does not guarantee the individual success developers may have in implementing the samples on their development platforms or in production configurations.

For details about how to try the samples, refer to the accompanying `README.md` files.
