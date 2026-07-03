---
title: Backing up policies
description: Back up Policy Editor policies before upgrading by exporting policy snapshots from Branch Manager.
component: pingauthorize
version: 11.1
page_id: pingauthorize:upgrading_pingauthorize:paz_back_up_policies
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/upgrading_pingauthorize/paz_back_up_policies.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 1, 2026
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
  result-2: Result:
---

# Backing up policies

Back up existing policies before upgrading the Policy Editor. Do this by exporting policy snapshots.

## About this task

Back up policies manually as described below or rely on the automatic backups covered in [Policy database backups](../pingauthorize_server_administration_guide/paz_policy_db_backups.html).

## Steps

1. Sign on to the Policy Editor and choose any existing branch to go to the main landing page.

2. To display your current branches, select Branch Manager → Version Control.

3. From the Branches list, click a branch that you want to export.

   ### Result:

   You should see a list of the commits for that branch, and the most recent version of the branch is named Uncommitted Changes.

4. Identify the commit that represents the snapshot that you want to export and click the hamburger menu in the Options column.

5. Choose Export Snapshot.

   ### Result:

   Your browser downloads the file.

6. Repeat for any additional branches that you want to back up.

---

---
title: Docker upgrades
description: Upgrade PingAuthorize Server and the Policy Editor using Docker.
component: pingauthorize
version: 11.1
page_id: pingauthorize:upgrading_pingauthorize:paz_docker_upgrades
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/upgrading_pingauthorize/paz_docker_upgrades.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 1, 2026
section_ids:
  upgrading-pingauthorize-server-using-docker: Upgrading PingAuthorize Server using Docker
  about-this-task: About this task
  steps: Steps
  upgrading-the-pingauthorize-policy-editor-using-docker: Upgrading the PingAuthorize Policy Editor using Docker
  steps-2: Steps
---

# Docker upgrades

## Upgrading PingAuthorize Server using Docker

When using Docker, instead of upgrading PingAuthorize Server, you deploy a container with the new PingAuthorize version and use the same server profile.

### About this task

If you deployed a container using a server profile, when you want to deploy a newer PingAuthorize Server version, you deploy a container with that version using the same server profile.

### Steps

* For more information, see <https://devops.pingidentity.com/reference/config/>.

  The server profiles for Docker deployments differ from those discussed in [Deployment automation and server profiles](../pingauthorize_server_administration_guide/paz_deploy_auto_server_prof.html).

## Upgrading the PingAuthorize Policy Editor using Docker

If you originally installed the Policy Editor with Docker per [Deploying the Policy Editor using Docker](../installing_and_uninstalling_pingauthorize/paz_install_server_pe_docker.html#pe_install_docker), use this procedure to upgrade the PingAuthorize Policy Editor when a new version is released.

### Steps

1. In your current Policy Editor, complete the steps in [Backing up policies](paz_back_up_policies.html).

2. Stop the old Docker container and start the new one.

   When a new Docker image for the PingAuthorize Policy Editor is available, you stop the existing Docker container and start the new container from the new image while mounting the same volumes.

   |   |                                                                                                                                                            |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you use a shared volume, you should always stop the Docker container running the older version of the Policy Editor before you start the new container. |

   The following commands stop the running container and run a new image named *\<pap\_new>*. This image uses the volumes from *\<pap\_old>* to house the policy database. Also, the command uses the same `PING_H2_FILE` location from [Example: Override the configured policy database location](../pingauthorize_server_administration_guide/paz_start_pe.html#override_policy_db_location).

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | * The Ping Identity DevOps Docker images use the PingAuthorize `setup` tool to update the H2 policy database on the mounted volume. If you store your policies in a PostgreSQL database, follow the instructions in [Deploying the Policy Editor using Docker](../installing_and_uninstalling_pingauthorize/paz_install_server_pe_docker.html#pe_install_docker) to update your policy database.

   * For proper communication between containers, create a Docker network using a command such as `docker network create --driver <network_type> <network_name>`, and then connect to that network with the `--network=<network_name>` option. |

   ```shell
   $ docker container stop  <pap_old>
   $ docker run --network=<network_name>  --name  <pap_new>  \
       -p 443:1443 -d --env-file ~/.pingidentity/config \
       --volumes-from  <pap_old>  \
       --env PING_H2_FILE=/opt/out/Symphonic \
       pingidentity/{PAP_CONTAINER_NAME}:<TAG>
   ```

   The Docker image *\<TAG>* used in the example is only a placeholder. For actual tag values, see Docker Hub (<https://hub.docker.com/r/pingidentity/pingauthorizepap>).

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The `setup` tool uses the default credentials to upgrade the policy database. If the credentials no longer match the default values, the server administrator should pass the correct credentials to the `setup` tool using the `PING_DB_ADMIN_USERNAME`, `PING_DB_ADMIN_PASSWORD`, `PING_DB_APP_USERNAME`, and `PING_DB_APP_PASSWORD` UNIX environment variables.For example, if the old policy database admin credentials have been previously set to admin/Passw0rd, and the application credentials have been set to app/S3cret, the docker `run` command should include those environment variables as shown in this example.```shell
     $ docker container stop  <pap_old>
     $ docker run --network=<network_name>  --name  <pap_new>  \
     -p 443:1443 -d --env-file ~/.pingidentity/config \
     --env PING_H2_FILE=/opt/out/Symphonic \
     --env PING_DB_ADMIN_USERNAME=admin \
     --env PING_DB_ADMIN_PASSWORD=Passw0rd \
     --env PING_DB_APP_USERNAME=app \
     --env PING_DB_APP_PASSWORD=S3cret \
     pingidentity/{PAP_CONTAINER_NAME}:<TAG>
   ```The Docker image *\<TAG>* used in the example is only a placeholder. For actual tag values, see Docker Hub (<https://hub.docker.com/r/pingidentity/pingauthorizepap>).This command ensures that the `setup` tool has the correct credentials to access the policy database, and that it does not reset credentials to their defaults. |

3. In the new Policy Editor, complete the steps in [Upgrading the Trust Framework and policies](paz_upgrade_trust_framework_policies.html).

---

---
title: Manual upgrades
description: Manually upgrade PingAuthorize Server and the Policy Editor, including steps to revert a server update.
component: pingauthorize
version: 11.1
page_id: pingauthorize:upgrading_pingauthorize:paz_manual_upgrades
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/upgrading_pingauthorize/paz_manual_upgrades.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 1, 2026
section_ids:
  upgrading-pingauthorize-server-manually: Upgrading PingAuthorize Server manually
  steps: Steps
  example: Example:
  reverting-an-update: Reverting an update
  about-this-task: About this task
  steps-2: Steps
  upgrade_pe_manually: Upgrading the PingAuthorize Policy Editor manually
  steps-3: Steps
  choose-from: Choose from:
---

# Manual upgrades

## Upgrading PingAuthorize Server manually

Perform the following steps to upgrade a PingAuthorize server.

### Steps

1. Download and unzip the new version of PingAuthorize Server in a location outside the existing server's installation.

   For these steps, assume the existing server installation is in `/opt/pingauthorize/PingAuthorize` and the new server version is extracted into `/home/stage/PingAuthorize`.

2. Provide a copy of the PingAuthorize license file for the version to which you are upgrading in the `/home/stage/PingAuthorize` directory, or give the location of the license file to the tool using the `--licenseKeyFile` option.

3. Run the `update` tool provided with the new server package to update the existing PingAuthorize Server.

   The `update` tool might prompt for confirmation on server configuration changes if it detects customization.

   #### Example:

   ```
   /home/stage/{pingauthorize}/update --serverRoot /opt/pingauthorize/{pingauthorize}
   ```

## Reverting an update

After you've updated PingAuthorize Server, you can revert to the previous version (one level back) using the `revert-update` tool.

### About this task

The `revert-update` tool accesses a log of file actions taken by the updater to put the file system back to its previous state. If you have run multiple updates, you can run the `revert-update` tool multiple times to sequentially revert to each prior update. You can only revert back one level at a time with the `revert-update` tool. For example, if you had to run the update twice since first installing PingAuthorize Server, you can run the `revert-update` tool to revert to its previous state, then run the `revert-update` tool again to return to its original state.

When starting the server for the first time after running a revert, the server displays warnings about "offline configuration changes," but these are not critical and will not appear during subsequent start-ups.

### Steps

* Run `revert-update` in the server root directory to revert back to the most recent previous version of the server, as shown in the following example:

  ```
  /opt/pingauthorize/{pingauthorize}/revert-update
  ```

## Upgrading the PingAuthorize Policy Editor manually

If you originally installed the PingAuthorize Policy Editor using `.zip` files, use this procedure to upgrade the Policy Editor when a new version is released.

### Steps

1. In your current Policy Editor, complete the steps in [Backing up policies](paz_back_up_policies.html).

2. Stop the Policy Editor.

   ```shell
   $ bin/stop-server
   ```

3. Obtain the new version of the PingAuthorize Policy Editor and extract it to a location outside the existing Policy Editor's installation.

4. Prepare the existing policy database.

   |   |                                                                                     |
   | - | ----------------------------------------------------------------------------------- |
   |   | The new server installation might require changes to the policy database structure. |

   #### Choose from:

   * If you store your policies in the H2 policy database, copy the existing database. The server `setup` tool performs these upgrades and generates a new `configuration.xml` file.

     This example assumes the old installation is in `/opt/pingauthorize/PingAuthorize-PAP-previous`, and the new installation is in `/opt/pingauthorize/PingAuthorize-PAP`. Run the following commands to upgrade from each version:

     * Step 8.1 and later

       ```shell
       $ cp /opt/pingauthorize/{pingauthorize}-PAP-previous/Symphonic.mv.db opt/pingauthorize/{pingauthorize}-PAP
       ```

     * Step 8.0 earlier

       ```shell
       $ cp /opt/pingauthorize/{pingauthorize}-PAP-previous/admin-point-application/db/Symphonic.mv.db opt/pingauthorize/{pingauthorize}-PAP
       ```

   * If you store your policies in a PostgreSQL database, follow the instructions for [Upgrading a PostgreSQL policy database](paz_upgrade_postgresql_policy_db.html).

5. Run the `setup` tool.

   |   |                                                                                                                                                                                                            |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Updating PingAuthorize Server uses an `update` tool. However, PingAuthorize Policy Editor does not have this tool. Instead of updating the Policy Editor in-place, you must install the new Policy Editor. |

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | The `setup` tool uses the default credentials to upgrade the database. If the credentials no longer match the default values, provide the correct credentials to the `setup` tool using the appropriate command-line options:- If you are using the default H2 policy database implementation, provide the non-default values using the `--dbAdminUsername`, `--dbAdminPassword`, `--dbAppUsername`, and `--dbAppPassword` command-line options. Otherwise, `setup` fails when it cannot access the H2 policy database, or it might reset credentials to their default values. For more information, see [Manage policy database credentials](../pingauthorize_server_administration_guide/paz_manage_policy_db_creds.html).

   - If you are using a PostgreSQL policy database implementation, provide the server runtime user value through the `--dbAppUsername` command-line option. For the server runtime password, provide this value to the `PING_DB_APP_PASSWORD` environment variable before server start. |

   Follow the instructions in either of the following topics:

   * [Installing the Policy Editor interactively](../installing_and_uninstalling_pingauthorize/paz_install_pe_interactive.html)

   * [Installing the Policy Editor non-interactively](../installing_and_uninstalling_pingauthorize/paz_install_pe_noninteractive.html)

6. Start the new Policy Editor.

   Follow the instructions in [Post-setup steps (manual installation)](../installing_and_uninstalling_pingauthorize/paz_post_setup_manual.html).

7. In the new Policy Editor, complete the steps in [Upgrading the Trust Framework and policies](paz_upgrade_trust_framework_policies.html).

---

---
title: Policy-related upgrades
description: Upgrade Policy Editor components for PingAuthorize, including policies, the Trust Framework, and the PostgreSQL policy database.
component: pingauthorize
version: 11.1
page_id: pingauthorize:upgrading_pingauthorize:paz_policy_related_upgrades
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/upgrading_pingauthorize/paz_policy_related_upgrades.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 1, 2026
---

# Policy-related upgrades

As part of the PingAuthorize upgrade process, you must upgrade specific Policy Editor components and dependencies, including policies, policy databases, and the Trust Framework.

See the following topics for instructions on upgrading Policy Editor components and dependencies:

* [Backing up policies](paz_back_up_policies.html)

* [Upgrading the Trust Framework and policies](paz_upgrade_trust_framework_policies.html)

* [Upgrading a PostgreSQL policy database](paz_upgrade_postgresql_policy_db.html)

---

---
title: Upgrade considerations
description: Review considerations before upgrading PingAuthorize, including Docker and manual requirements, Java versions, and version-specific notes.
component: pingauthorize
version: 11.1
page_id: pingauthorize:upgrading_pingauthorize:paz_upgrade_consids
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/upgrading_pingauthorize/paz_upgrade_consids.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 9, 2026
section_ids:
  general-considerations: General considerations
  considerations-when-upgrading-to-11-1-or-later: Considerations when upgrading to 11.1 or later
  moving-to-java-25: Moving to Java 25
  considerations-when-upgrading-to-11-0-or-later: Considerations when upgrading to 11.0 or later
  url-decoding-behavior-standardization: URL decoding behavior standardization
  aws-java-sdk-upgrade: AWS Java SDK upgrade
  considerations-when-upgrading-to-10-3-or-later: Considerations when upgrading to 10.3 or later
  behavior-change-for-empty-arrays-relative-to-json-attributes: Behavior change for empty arrays relative to JSON attributes
  custom-sdk-extensions-using-java-ee-javax-packages-must-be-migrated-and-recompiled: Custom SDK extensions using Java EE javax packages must be migrated and recompiled
  camel-upgrade: Camel upgrade
  java-considerations: Java considerations
  prerequisites-for-upgrading: Prerequisites for upgrading
  upgrading-from-a-server-running-a-supported-version-of-java: Upgrading from a server running a supported version of Java
  upgrading-from-a-server-running-an-unsupported-version-of-java: Upgrading from a server running an unsupported version of Java
  upgrading-a-policy-editor-instance-running-an-unsupported-version-of-java: Upgrading a Policy Editor instance running an unsupported version of Java
  considerations-when-upgrading-to-10-1-or-later: Considerations when upgrading to 10.1 or later
  resolving-issues-with-copying-policy-elements: Resolving issues with copying policy elements
  upgrade_consids_100: Considerations when upgrading to 10.0 or later
  sni-hostname-checking-disabled-by-default: SNI hostname checking disabled by default
---

# Upgrade considerations

When upgrading, you must consider factors such as the scope of the update, the PingAuthorize version from which you're upgrading, and if you're not using Docker, your installed version of Java.

## General considerations

For Docker deployments, the upgrade process involves downloading and deploying the latest containers.

For manual installations, the upgrade process involves downloading and extracting a new version of the PingAuthorize Server `.zip` file on the server and running the update utility with the `--serverRoot` or `-R` option value from the new root server pointing to the installation.

Consider the following when upgrading:

* The update affects only the server being upgraded. The process does not alter the configuration of other servers, so you must update those servers separately.

* The update tool verifies that the installed version of Java meets the new server requirements. To simplify the process, install the version of Java that is supported by the new server before running the tool.

|   |                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For additional considerations, refer to [Best Practices: Planning your upgrade](https://docs.pingidentity.com/solution-guides/best_practice_guides/htg_plan_software_upgrade.html). |

## Considerations when upgrading to 11.1 or later

### Moving to Java 25

* Changes

  We added Java Runtime Environment (JRE) support for Oracle JDK 25 and OpenJDK 25. However, previous versions of the PingAuthorize `config/java.properties` file contain references to the security manager, which Java 25 doesn't support. This conflict causes the server to fail on startup.

* Required action

  After upgrading a previous PingAuthorize Server version to 11.1, you must complete the following steps to use Java 25:

  1. In the `config/java.properties` file, change the value of `default.java-home` to the correct JRE for Java 25.

  2. Run **bin/dsjavaproperties --initialize**.

     This command overwrites the `java.properties` file and saves the original file as `java.properties.old`.

  3. Update the new `java.properties` file with any custom property changes, using `java.properties.old` as a reference.

  4. Restart the server.

## Considerations when upgrading to 11.0 or later

### URL decoding behavior standardization

* Changes

  We've standardized URL decoding behavior to address a security vulnerability that permitted double-URL-encoded requests to bypass path-based access controls.

  * **Policy evaluation**: The PingAuthorize Server now decodes the incoming request URL, including the path and query parameters, exactly once before policy evaluation.

  * **Request forwarding**: The PingAuthorize Server now forwards the original, unmodified request URL to the backend resource server.

* Required action

  Backend resource servers must now perform their own URL decoding in accordance with [RFC-3986](https://datatracker.ietf.org/doc/html/rfc3986). If your resource servers previously relied on PingAuthorize to forward fully-decoded request URLs, now these servers might fail to process encoded URLs correctly. Update these servers to handle encoded URLs or deploy a proxy to decode traffic before it reaches the server.

### AWS Java SDK upgrade

* Changes

  We've upgraded to AWS Java SDK v2. This upgrade changes the default behavior for Amazon S3 connections to use virtual-hosted-style URLs, disabling legacy path-style access by default.

* Required action

  If your Amazon S3 deployment package stores require path-style access (for example, `https://s3.amazonaws.com/<bucket-name>`), enable the **Use Path Style Access** option in the PingAuthorize S3 store configuration to maintain connectivity.

  Learn more in [Adding an Amazon S3 deployment package store to PingAuthorize](../pingauthorize_server_administration_guide/paz_amazons3_deploy_package.html).

## Considerations when upgrading to 10.3 or later

### Behavior change for empty arrays relative to JSON attributes

If a JSON attribute in a SCIM PATCH request contains or is an empty array, the server now clears the array. In previous versions of PingAuthorize, this request doesn't modify the existing array.

This update might cause behavior changes.

### Custom SDK extensions using Java EE `javax` packages must be migrated and recompiled

Several components were upgraded in version 10.3 of PingAuthorize. If any of your custom Server SDK extensions import `javax.*` packages that are part of the Java EE specification (such as `javax.servlet` or `javax.ws.rs`), you must migrate them to the equivalent `jakarta.*` packages and recompile the extension.

|   |                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------- |
|   | `javax.*` packages that are part of standard Java SE (such as `javax.crypto` or `javax.sql`) are unaffected and don't require migration. |

### Camel upgrade

PingAuthorize 10.3 now supports Apache Camel 4.0. The limitations on using Apache Camel to connect policy information points (PIP) introduced in PingAuthorize 9.3 still apply. You can find more information on working around these limitations in [Enabling Camel service connections](../pingauthorize_policy_administration_guide/paz_camel_enable.html). Learn how to upgrade PingAuthorize versions 10.0-10.2 using Camel 3.x in the Apache Camel 3.x to 4.0 [migration guide](https://camel.apache.org/manual/camel-4-migration-guide.html).

### Java considerations

Support for Java 11 has been removed, and upgrading to Version 10.3 of PingAuthorize will fail unless you are running Java 17 or 21.

#### Prerequisites for upgrading

You must meet one of the following requirements:

* Your default Java installation is a supported version.

* You are pointing one of the following environment variables to a supported version of Java:

  * `UNBOUNDID_JAVA_HOME`

  * `JAVA_HOME`

|   |                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you use environment variables to point to your Java installation, these will override your default Java version. We recommend you set only one variable. If both are set, `UNBOUNDID_JAVA_HOME` takes precedence. |

|   |                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------- |
|   | Java 11 is no longer supported. You can't upgrade a server instance to version 10.3 without first updating Java to a supported version. |

##### Upgrading from a server running a supported version of Java

If you're upgrading a server running Java 17 or 21 to version 10.3, you can [proceed with the server upgrade](paz_upgrade_pingauthorize.html).

##### Upgrading from a server running an unsupported version of Java

Before upgrading the server to version 10.3, you must install either Java 17 or 21. Learn more in [System requirements](../installing_and_uninstalling_pingauthorize/paz_system_requirements.html). Upgrading to version 10.3 after updating Java requires changes to the `java.properties` file.

|   |                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------- |
|   | You must also meet one of the prerequisites listed in the previous section before upgrading the server. |

Select one of the following options for modifying the `java.properties` file. Where a Java version is specified, substitute your installed, supported Java version.

* Option 1: Before upgrading the server, convert the file manually:

  1. Edit the `config/java.properties` file to update the Java version and convert the JVM parameters to be specific to Java 17.

  2. Run the `bin/dsjavaproperties` command to put the changes into effect.

* Option 2: Before upgrading the server, create a new file:

  1. Rename the old `java.properties` file.

  2. Run the `bin/dsjavaproperties` command to initialize a new Java 17 `java.properties` file.

     For this option, run:

     ```
     bin/dsjavaproperties --initialize
     ```

  3. Upgrade the server using the generated `java.properties` file, and then restore your customized settings from the original file.

* Option 3: Allow the upgrade to replace the file:

  1. Upgrade the server to version 10.3.

     The upgrade process will overwrite the `java.properties` file and the original file will be saved as `java.properties.old`. A `java.properties.change` file will also be created, containing the diff output between the new and old `java.properties` files.

  2. Restore or convert the JVM settings that were overwritten during the upgrade process.

##### Upgrading a Policy Editor instance running an unsupported version of Java

If you are upgrading from a Policy Editor instance running an unsupported version of Java, you must export the `JAVA_HOME` environment variable by running the following command:

```
export JAVA_HOME=$JAVA11_HOME
```

You must perform this export before running any scripts in PingAuthorize 10.3, including `bin/setup` and `bin/start-server`.

## Considerations when upgrading to 10.1 or later

### Resolving issues with copying policy elements

After upgrading from a version of PingAuthorize earlier than 10.1 and attempting to delete a copy of a Policy Editor element, that copy might persist in the UI and return an error when selected. To completely remove deleted copies from the Policy Editor, follow the steps in [Deleting persistent copies](../pingauthorize_policy_administration_guide/paz_entity_copy_troubleshooting.html).

## Considerations when upgrading to 10.0 or later

### SNI hostname checking disabled by default

If you're upgrading to PingAuthorize 10.0 or later with an existing configuration that has SNI hostname checks enabled, you might encounter an issue when using a host name not found in the key store. To migrate an existing configuration from an earlier version of PingAuthorize and disable SNI host name checks, add the following to your `configuration.yml` file:

```
server:
  ...
  applicationConnectors:
  - type: "https"
    ...
    disableSniHostCheck: "${PING_DISABLE_SNI_HOSTNAME_CHECKS:-true}"
```

This change also introduces a new `setup` option, `--disableSniHostnameChecks`, that you can set to `false` to enable SNI hostname checks.

---

---
title: Upgrading a PostgreSQL policy database
description: Upgrade a PostgreSQL policy database for the Policy Editor using the policy-db tool.
component: pingauthorize
version: 11.1
page_id: pingauthorize:upgrading_pingauthorize:paz_upgrade_postgresql_policy_db
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/upgrading_pingauthorize/paz_upgrade_postgresql_policy_db.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 1, 2026
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  result: Result
  next-steps: Next steps
---

# Upgrading a PostgreSQL policy database

To upgrade an existing PostgreSQL policy database, use the `policy-db` tool.

## Before you begin

* The PostgreSQL instance must be reachable on the network from the Policy Editor host and listening for connections.

* The Policy Editor uses both a PostgreSQL administration user and a server runtime user. Have a database administrator create both users before providing their credentials to the `policy-db` tool. The administration user must be able to create new databases. When new releases of the Policy Editor become available, continue using the same administration user to prevent database object ownership issues.

  Learn more about creating new database users and configuring PostgreSQL to listen for remote connections securely in the [PostgreSQL documentation](https://www.postgresql.org/docs/).

* The Policy Editor uses Java Database Connectivity (JDBC) to connect to PostgreSQL. Be prepared to provide the JDBC connection string in the following format: `jdbc:postgresql://<host>:<port>/<name>`. For example: `jdbc:postgresql://example.com:5432/pap_db`

## About this task

When a newer version of the Policy Editor is released, it will fail to start when pointing to a PostgreSQL database with older database objects. Running `start-server` will print a message like the following to the console:

```
The policy database at 'jdbc:postgresql://example.com:5432/pap_db' is older than this version of PingAuthorize Policy Editor (9.2.0.0).
Please use the policy-db tool to upgrade the database before running start-server again.
```

This message indicates that you must run the `policy-db` tool for this newer version of the Policy Editor to upgrade the database objects.

Follow these instructions to upgrade a PostgreSQL database for a manual upgrade of the Policy Editor. Be prepared to provide the database administration credentials and server runtime credentials you used to create the PostgreSQL database.

|   |                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | See [Deploying the Policy Editor using Docker](../installing_and_uninstalling_pingauthorize/paz_install_server_pe_docker.html#pe_install_docker) for containerized deployments. |

## Steps

1. Complete steps 1-3 of [Upgrading the PingAuthorize Policy Editor manually](paz_manual_upgrades.html#upgrade_pe_manually).

2. Run the following command:

   ```shell
   $ bin/policy-db \
     --dbConnectionString "jdbc:postgresql://<host>:<port>/<name>" \
     --dbAppUsername  <server-runtime-username>  \
     --dbAppPassword  <server-runtime-password>
   ```

   |   |                                                                                                                     |
   | - | ------------------------------------------------------------------------------------------------------------------- |
   |   | Alternatively, you can provide the server runtime password through the `PING_DB_APP_PASSWORD` environment variable. |

3. Provide the database administration credentials when prompted.

## Result

The `policy-db` tool connects to PostgreSQL and applies the upgrades.

## Next steps

Complete steps 5-7 of [Upgrading the PingAuthorize Policy Editor manually](paz_manual_upgrades.html#upgrade_pe_manually).

|   |                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Provide the Policy Editor with the same `--dbConnectionString`, `--dbAppUsername`, and server runtime password you used to create the PostgreSQL database. |

---

---
title: Upgrading PingAuthorize
description: Upgrade PingAuthorize Server and the Policy Editor in tandem to keep versions in sync.
component: pingauthorize
version: 11.1
page_id: pingauthorize:upgrading_pingauthorize:paz_upgrade_pingauthorize
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/upgrading_pingauthorize/paz_upgrade_pingauthorize.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 1, 2026
---

# Upgrading PingAuthorize

PingAuthorize includes two server applications you must upgrade in tandem—the main PingAuthorize Server and the Policy Editor.

Ping Identity issues software release builds periodically with new features, enhancements, and fixes for improved server performance.

|   |                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingAuthorize Server used in external PDP mode requires a Policy Editor with the same version. When upgrading PingAuthorize Server, you must also upgrade the Policy Editor. |

---

---
title: Upgrading the Trust Framework and policies
description: Upgrade the PingAuthorize Trust Framework and policies by merging the version-specific upgrade snapshot and updating the trust-framework-version.
component: pingauthorize
version: 11.1
page_id: pingauthorize:upgrading_pingauthorize:paz_upgrade_trust_framework_policies
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/upgrading_pingauthorize/paz_upgrade_trust_framework_policies.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 1, 2026
section_ids:
  steps: Steps
  example: Example:
---

# Upgrading the Trust Framework and policies

PingAuthorize ships with a default Trust Framework and policy snapshot that policy writers should use as a starting point when developing their policies. Occasionally, a server upgrade results in changes to the default Trust Framework and policies, and policy writers must upgrade any policies based on `defaultPolicies.SNAPSHOT`.

## Steps

1. Sign on to the Policy Editor and choose any branch to go to the main landing page.

2. Select **Branch Manager** from the navigation bar on the left, and open the **Merge Snapshot** tab.

3. Click the **file selection** option, and go to the `resource/policies/upgrade-snapshots` folder of the new Policy Editor deployment.

4. Select the correct `SNAPSHOT` file based on the version you are upgrading from and the version to which you are upgrading.

   |   |                                                                                                                                                                          |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If you are upgrading from 7.3.0.*x*, use the `7.3.0.x-to-8.0.0.0-SNAPSHOT` and merge that (per the next step) before you select and merge `8.0.0.0-to-8.1.0.0.SNAPSHOT`. |

   ### Example:

   When upgrading from version 8.0.0.0 to version 8.1.0.0, use `resource/policies/upgrade-snapshots/8.0.0.0-to-8.1.0.0.SNAPSHOT`.

5. Merge the partial snapshot.

   |   |                                                                                                                                                          |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Merge conflicts might occur where objects have been updated. If you have not modified the objects in conflict, you can safely select **Keep Snapshots**. |

6. Return to your PingAuthorize Server installation.

7. Run the following `dsconfig` command to configure PingAuthorize Server to use the latest Trust Framework version:

   ```
   dsconfig set-policy-decision-service-prop \
     --set trust-framework-version:{TRUST_FRAMEWORK_VERSION}
   ```