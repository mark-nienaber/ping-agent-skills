---
title: Restoring a PingAccess configuration backup
description: If an upgrade fails, restore your PingAccess configuration using an automatically generated backup.
component: pingaccess
version: 9.1
page_id: pingaccess:upgrading_pingaccess:pa_restoring_a_pa_configuration_backup
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/upgrading_pingaccess/pa_restoring_a_pa_configuration_backup.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
---

# Restoring a PingAccess configuration backup

If an upgrade fails, restore your PingAccess configuration using an automatically generated backup.

## About this task

PingAccess automatically creates a backup `.zip` file each time an administrative user authenticates to the administrative console. These backups are stored in `<PA_HOME>/data/archive`, with a maximum number of backups configurable using the `pa.backup.filesToKeep` configuration parameter in `run.properties`.

|   |                                                                  |
| - | ---------------------------------------------------------------- |
|   | This operation will replace your current configuration settings. |

## Steps

1. Stop PingAccess.

2. Extract the backup file to `<PA_HOME>`.

3. Restart PingAccess.

   ### Result:

   Your PingAccess configuration is reverted to the state in the backup archive that was restored.

---

---
title: Upgrade considerations
description: The following changes between PingAccess versions might require additional steps during an upgrade.
component: pingaccess
version: 9.1
page_id: pingaccess:upgrading_pingaccess:pa_upgrade_considerations
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/upgrading_pingaccess/pa_upgrade_considerations.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 1, 2026
section_ids:
  considerations-when-upgrading-to-6-0-or-later: Considerations when upgrading to 6.0 or later
  new-templates-for-error-and-logout-pages: New templates for error and logout pages
  using-a-proxied-pingfederate-deployment: Using a proxied PingFederate deployment
  spa-support: SPA support
  considerations-when-upgrading-to-7-0-or-later: Considerations when upgrading to 7.0 or later
  runtime-state-clustering-removal: Runtime state clustering removal
  upgrading-to-or-past-version-7-3-with-a-customized-log4j2-xml-file: Upgrading to or past version 7.3 with a customized log4j2.xml file
  elliptic-curve-key-pair-issues-with-aws-cloudhsm-client-sdk-5: Elliptic Curve key pair issues with AWS CloudHSM Client SDK 5
  improved-configuration-replication-compatibility: Improved configuration replication compatibility
  considerations-when-upgrading-to-8-0-or-later: Considerations when upgrading to 8.0 or later
  upgrading-to-or-past-version-8-0-from-version-6-2-or-below: Upgrading to or past version 8.0 from version 6.2 or below
  pa-keystore-pw-encryption-enforcement: pa.keystore.pw encryption enforcement
  considerations-when-upgrading-to-9-0-or-later: Considerations when upgrading to 9.0 or later
  java-11-removal: Java 11 removal
  rsa-1-5-with-pkcs1-removal: RSA 1.5 with PKCS#1 removal
  rotate: Automatically rotate the admin config query certificate
---

# Upgrade considerations

The following changes between PingAccess versions might require additional steps during an upgrade.

## Considerations when upgrading to 6.0 or later

### New templates for error and logout pages

In PingAccess 6.1, we updated several error and logout page template files to modernize their appearance and remove Ping branding:

* `general.loggedout.page.template.html`

* `general.error.page.template.html`

* `admin.error.page.template.html`

* `policy.error.page.template.html`

You can find more information about the templates in [User-facing page customization reference](../configuring_and_customizing_pingaccess/pa_user_facing_page_customization_ref.html). If you customized the template files previously, recustomize the new files.

### Using a proxied PingFederate deployment

PingAccess 6.2 introduced the ability to configure a proxied PingFederate deployment through PingAccess. If you configured a similar deployment in an earlier version of PingAccess manually, you can continue to use it.

However, if you plan to switch from a deployment that you configured manually to a proxied PingFederate deployment through PingAccess:

* Review the configuration options in the proxied PingFederate deployment admin console. Verify that it can support your current configuration's use cases.

* Remove any PingFederate-related applications before migrating the configuration.

### SPA support

We removed the single-page application (SPA) support checkbox from the admin UI for **Web** applications in PingAccess 6.2. Consequently, all **Web** applications created in PingAccess 6.2 and later have SPA support enabled by default.

The SPA support checkbox is still available for **API** applications and **Web + API** applications. You can find more information in [Application field descriptions](../pingaccess_user_interface_reference_guide/pa_application_field_descriptions.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If the default settings for SPA support with **Web** applications aren't compatible with your environment or with a specific application, you can [change the default authentication policy](../pingaccess_user_interface_reference_guide/pa_changing_the_default_authentication_challenge_policy.html) or [create a new authentication challenge policy](../pingaccess_user_interface_reference_guide/pa-managing-acps.html). |

PingAccess 7.1 added a system-provided authentication challenge policy that disables SPA support by default. This policy is useful if you aren't onboarding any new SPAs and don't have many SPAs in your current environment. Learn more in [Authentication](../pingaccess_user_interface_reference_guide/pa_authentication.html).

## Considerations when upgrading to 7.0 or later

### Runtime state clustering removal

Support for runtime state clustering was removed in PingAccess 7.0. However, one benefit of runtime state clustering was that it enabled [rate limiting rules](../pingaccess_user_interface_reference_guide/pa_adding_rate_limiting_rules.html) to behave more consistently in a clustered environment. This was because runtime state clustering enabled all of the engines in a cluster to know the total number of requests for a resource, not just the requests which that engine received.

If you're using runtime state clustering with rate limiting rules, before upgrading to PingAccess 7.0 or later, you should either:

* Configure a load balancer sitting in front of a PingAccess cluster to stick the session to a specific engine. This ensures that a single PingAccess engine node applies the rate limiting rule. Learn more in [Managing load balancing strategies](../pingaccess_user_interface_reference_guide/pa_load_balancing_strategies.html).

* Tune down the **Max Burst Requests** interval on the rate limiting rule, following the *\<current max burst requests interval>*/*\<number of engines in cluster>* ratio.

### Upgrading to or past version 7.3 with a customized `log4j2.xml` file

PingAccess 7.3 introduced a new `log4j-categories.xml` file to enable adjustment of the amount of detail included in PingAccess's logs. Learn more in [Configuring verbose logging in the admin console](../pingaccess_user_interface_reference_guide/pa_configuring_verbose_logging.html).

If you have customized your `log4j2.xml` file, you must merge this file with the `log4j-categories.xml` file the first time you upgrade to PingAccess 7.3 or a later version.

### Elliptic Curve key pair issues with AWS CloudHSM Client SDK 5

As of PingAccess 7.3, PingAccess offers support for Amazon Web Services (AWS) *(tooltip: \<div class="paragraph">
\<p>An Amazon subsidiary providing cloud computing platforms.\</p>
\</div>)* CloudHSM Client SDK 5 instead of Client SDK 3.

Client SDK 5 introduces an issue with elliptic curve (EC) key pairs for all TLS handshakes, similar to the extant issue with TLS 1.3 for EC and RSA keys. As a result, you can create EC key pairs in PingAccess, but you can't assign them to a listener.

### Improved configuration replication compatibility

PingAccess 7.3 introduced the ability for engine nodes and the replica administrative node to connect to an administrative node that's running a later version of PingAccess. This ability was backported to PingAccess 7.2.2 as well.

Nodes running PingAccess 7.2.2 or later can replicate data that's relevant for the version of PingAccess that they're running from the administrative node. You can find more information on clustering and configuration data replication in [Clustering in PingAccess](../reference_guides/pa_clustering_ref_guide.html).

This ability to maintain compatibility reduces the possibility for outages caused by outdated information, providing more flexibility during the upgrade process for those with large scale or hybrid environments. It also improves stability for containerized deployments because clustered engine nodes don't need to maintain their replication data throughout a restart.

|   |                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You should still finish upgrading the engine nodes as soon as possible and avoid making configuration changes until all engines have been upgraded. |

## Considerations when upgrading to 8.0 or later

### Upgrading to or past version 8.0 from version 6.2 or below

If you have PingAccess 6.2 or below, you cannot upgrade directly to PingAccess 8.0. You must upgrade to a version above 6.2 first, and then upgrade to 8.0.

This is because in PingAccess 8.0, an outdated H2 JAR file was removed, and PingAccess 6.2 and below use an H2 embedded database.

### `pa.keystore.pw` encryption enforcement

PingAccess 8.3 and later enforce encryption of the `pa.keystore.pw` property in the `run.properties` file as follows:

* In non-FIPS mode, if you don't obfuscate `pa.keystore.pw`, PingAccess logs a warning during startup.

* If you try to enable FIPS mode without obfuscating `pa.keystore.pw`, PingAccess terminates startup and logs an error message.

## Considerations when upgrading to 9.0 or later

### Java 11 removal

Ping Identity removed Java 11 support from PingAccess in December 2025. You must upgrade to a supported Java version before installing PingAccess 9.0 or later. Learn more about supported java versions in [PingAccess system requirements](../installing_and_uninstalling_pingaccess/pa_installation_requirements.html#system-reqs).

### RSA 1.5 with PKCS#1 removal

Ping Identity removed support for RSA 1.5 with PKCS#1 in PingAccess 9.0.

### Automatically rotate the admin config query certificate

PingAccess 9.1 now uses a two-port certificate rotation approach for the admin config query listener. Engine nodes poll the [`/engines/rest/config-query-certificate` endpoint](../reference_guides/pa_api_endpoints.html) to retrieve new certificates and add them to the engine node's truststore.

After upgrading to PingAccess 9.1 or later:

* Consider whether you need to change the rotation window or the temporary rotation port. Learn more in the [PingAccess configuration file reference](../reference_guides/pa_config_file_ref.html#pa-cluster-config-settings) and [Port requirements](../installing_and_uninstalling_pingaccess/pa_installation_requirements.html#port-reqs).

* If using Linux, make sure any clustered PingAccess engine nodes have the write permission so they can modify the `bootstrap.properties` file. If these nodes don't have the correct file permissions, making updates to the config query listener can cause unexpected behavior.

---

---
title: Upgrade Troubleshooting
description: This table lists some potential problems and resolutions you might encounter while upgrading PingAccess.
component: pingaccess
version: 9.1
page_id: pingaccess:upgrading_pingaccess:pa_upgrade_troubleshooting
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/upgrading_pingaccess/pa_upgrade_troubleshooting.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
---

# Upgrade Troubleshooting

This table lists some potential problems and resolutions you might encounter while upgrading PingAccess.

| Issue                                                                 | Resolution                                                                                                                                                                                                              |
| --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Upgrade from version 4.3 or earlier fails due to Groovy rule changes. | To verify your Groovy scripts are prepared for the upgrade, review the [Groovy development reference guide](../reference_guides/pa_groovy_in_pa.html) and the [Upgrade considerations](pa_upgrade_considerations.html). |
| Custom plugins are missing after upgrade.                             | Manually add the custom plugins to the `<PA Home>/deploy` directory.                                                                                                                                                    |

---

---
title: Upgrade utility configuration file reference
description: This configuration file reference provides an overview of configurable parameters used by the upgrade utility. These parameters are configured in the <UU_HOME>/conf/run.properties file.
component: pingaccess
version: 9.1
page_id: pingaccess:upgrading_pingaccess:pa_upgrade_utility_config_file_ref
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/upgrading_pingaccess/pa_upgrade_utility_config_file_ref.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
---

# Upgrade utility configuration file reference

This configuration file reference provides an overview of configurable parameters used by the upgrade utility. These parameters are configured in the `<UU_HOME>/conf/run.properties` file.

* pa.upgrade.source.ssl.ciphers

  Defines the type of cryptographic ciphers available for use with the source PingAccess

* pa.upgrade.source.ssl.protocols

  Defines the protocols available for use with the source PingAccess

* pa.upgrade.target.ssl.ciphers

  Defines the type of cryptographic ciphers available for use with the target PingAccess. If not specified, the Java Virtual Machine (JVM) *(tooltip: \<div class="paragraph">
  \<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>
  \</div>)* default values are used.

* pa.upgrade.target.ssl.protocols

  Defines the protocols available for use with the target PingAccess. If not specified, the JVM default values are used.

* pa.upgrade.http.client.connection.timeout.ms

  Defines, in milliseconds, the amount of time to wait before timing out the connection to the HTTP client. The default value is 3600000.

* pa.upgrade.http.client.socket.timeout.ms

  Defines, in milliseconds, the HTTP client socket timeout. The default value is 3600000.

---

---
title: Upgrading a PingAccess cluster using the incremental update package
description: Upgrade a PingAccess cluster to a newer version using the incremental update package.
component: pingaccess
version: 9.1
page_id: pingaccess:upgrading_pingaccess:pa_upgrading_a_pa_cluster_using_the_incremental_upgrade_package
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/upgrading_pingaccess/pa_upgrading_a_pa_cluster_using_the_incremental_upgrade_package.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 5, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Upgrading a PingAccess cluster using the incremental update package

Upgrade a PingAccess cluster to a newer version using the incremental update package.

## Before you begin

* Make a backup copy of the PingAccess home directory. If the upgrade fails, use the backup copy to restore PingAccess.

* Review the release notes for every version between your current version and the target version.

* Verify that each node is using the same PingAccess version. You can check the version by viewing the `<PA_HOME>/lib/pingaccess-admin-ui-<version number>.jar` file.

* Verify that the PingAccess administrative node is running.

* Verify that basic authentication is configured and enabled for the running PingAccess administrative node.

* Download the PingAccess incremental update `.zip` file for the target version.

## About this task

Use the PingAccess incremental update bundle to upgrade a cluster from PingAccess 6.3 or later, the source version, to the most recent maintenance release for that version of PingAccess, the target version. For example, upgrade PingAccess 6.3 to the most recent maintenance release for 6.3.

|   |                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This upgrade procedure causes some downtime. To upgrade a cluster with no downtime, see the [Zero Downtime Upgrade](../pingaccess_zero_downtime_upgrade/pa_zero_downtime_upgrade.html) guide. |

## Steps

1. Upgrade the administrative node.

   1. Extract the `.zip` file for the target version of PingAccess.

   2. Open the `readme` file included in the extracted `.zip` bundle.

   3. Make the file changes specified in the `readme` file.

2. Upgrade the replica administrative node.

   1. Extract the `.zip` file for the target version of PingAccess.

   2. Open the `readme` file included in the extracted `.zip` bundle.

   3. Make the file changes specified in the `readme` file.

3. Upgrade each engine node.

   1. Extract the `.zip` file for the target version of PingAccess.

   2. Open the `readme` file included in the extracted `.zip` bundle.

   3. Make the file changes specified in the `readme` file.

4. Shut down the entire cluster.

5. Start the upgraded administrative node.

6. Start the upgraded replica administrative node.

7. Start each upgraded engine node.

## Next steps

After you complete the upgrade, see [Performing post-upgrade tasks](pa_performing_post_upgrade_tasks.html).

---

---
title: Upgrading a PingAccess cluster using the upgrade utility
description: Upgrade a PingAccess cluster to a newer version.
component: pingaccess
version: 9.1
page_id: pingaccess:upgrading_pingaccess:pa_upgrading_a_pa_cluster_using_the_upgrade_utility
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/upgrading_pingaccess/pa_upgrading_a_pa_cluster_using_the_upgrade_utility.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  choose-from-3: Choose from:
  next-steps: Next steps
  pingaccess-cluster-upgrade-parameters: PingAccess cluster upgrade parameters
  parameter-definitions: Parameter definitions
  environment-variables: Environment variables
  java-virtual-machine-jvm-memory-options: Java virtual machine (JVM) memory options
  example: Example
---

# Upgrading a PingAccess cluster using the upgrade utility

Upgrade a PingAccess cluster to a newer version.

## Before you begin

* If you are using PingAccess 3.2 or earlier, upgrade to PingAccess 4.3 or 5.3 before upgrading to the latest version.

* Create a backup of your existing PingAccess configuration. If the upgrade fails, you can restore your environment from this backup.

* Review the release notes for every version between your current version and the target version.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | In PingAccess 5.0 or later, there are potentially breaking changes to the Software Development Kit (SDK) *(tooltip: \<div class="paragraph">&#xA;\<p>A set of tools that allows a developer to build a custom application that integrates with or connects to a platform or service.\</p>&#xA;\</div>)* for Java, Groovy scripts, and the administrative SDK. For information on these changes and the actions administrators might need to take, see the [Upgrade considerations](pa_upgrade_considerations.html) and the [PingAccess 5.0](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-50.pdf#page=263) release notes. |

* Verify the following:

  * Each node is using the same PingAccess version. You can check the version by viewing the `<PA_HOME>/lib/pingaccess-admin-ui-<version number>.jar` file.

  * The PingAccess administrative node is running.

  * Basic authentication is configured and enabled for the running PingAccess administrative node.

  * You have the `.zip` bundle for the target version of PingAccess.

* Verify that you are using the same account normally used to run PingAccess.

## About this task

Use the PingAccess upgrade utility to upgrade a cluster from PingAccess 4.0 or later, the source version, to the most recent version, the target version.

|   |                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The upgrade procedure causes some downtime. To upgrade a cluster with no downtime, see the [Zero Downtime Upgrade](../pingaccess_zero_downtime_upgrade/pa_zero_downtime_upgrade.html) guide. |

The upgrade utility starts an instance of PingAccess with an administrative listener on port 9001. You can change this port number using the `upgrade.bat` or `upgrade.sh` `-p` parameter. This port configuration is only used for the upgrade. The configured port is used by the upgraded server when the upgrade is complete.

Any warnings or errors encountered are recorded in `log/upgrade.log`, as well as on-screen while the utility is being run. The upgrade uses an exit code of 0 to indicate a successful upgrade and an exit code of 1 to indicate failure.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you are upgrading from version 4.3 or earlier, and your installation uses custom plugins, they must be rebuilt using the SDK version included in PingAccess 5.0 or later. Run the upgrade utility manually with the new `-i` command-line option to specify a directory containing the custom plugin JAR files and only the custom plugin JAR files. To migrate your custom plugins, see the [PingAccess Addon SDK for Java Migration Guide](../agents_and_integrations/pa_add_on_sdk_for_java_migration_guide.html). |

|   |                                                                                    |
| - | ---------------------------------------------------------------------------------- |
|   | During the upgrade, do not make any changes to the running PingAccess environment. |

## Steps

1. On the administrative node, extract the `.zip` file for the target version of PingAccess.

2. Go to the new version's `/upgrade/bin` directory.

3. Run the PingAccess upgrade utility:

   ### Choose from:

   * On Windows: `upgrade.bat [-p <admin_port>] [-i <directory>] [-j <jvm_memory_options_file>] [-l <newPingAccessLicense>] [-s | --silent] <sourcePingAccessRootDir>`

   * On Linux: `./upgrade.sh [-p <admin_port>] [-i <directory>] [-j <jvm_memory_options_file>] [-l <newPingAccessLicense>] [-s | --silent] <sourcePingAccessRootDir>`

4. Review the upgrade log. If it records any manual post-upgrade tasks:

   1. Stop the source administrative console.

   2. Start the target administrative console using the `<PA_HOME>/bin/run.sh` command on Linux systems or the `<PA_HOME>\bin\run.bat` command on Windows systems.

   3. Perform any manual post-upgrade tasks recorded in the upgrade log.

   4. Shut down the upgraded administrative console.

5. Run the upgrade utility on the replica administrative node.

   ### Choose from:

   * On Windows: `upgrade.bat [-p <admin_port>] [-i <directory>] [-j <jvm_memory_options_file>] [-l <newPingAccessLicense>] [-s | --silent] <sourcePingAccessRootDir>`

   * On Linux: `./upgrade.sh [-p <admin_port>] [-i <directory>] [-j <jvm_memory_options_file>] [-l <newPingAccessLicense>] [-s | --silent] <sourcePingAccessRootDir>`

6. Run the upgrade utility on each engine node.

   ### Choose from:

   * On Windows: `upgrade.bat [-p <admin_port>] [-i <directory>] [-j <jvm_memory_options_file>] [-l <newPingAccessLicense>] [-s | --silent] <sourcePingAccessRootDir>`

   * On Linux: `./upgrade.sh [-p <admin_port>] [-i <directory>] [-j <jvm_memory_options_file>] [-l <newPingAccessLicense>] [-s | --silent] <sourcePingAccessRootDir>`

7. Shut down the entire cluster.

8. Start the upgraded administrative node.

9. Start the upgraded replica administrative node.

10. Start each upgraded engine node.

## Next steps

After you complete the upgrade, see [Performing post-upgrade tasks](pa_performing_post_upgrade_tasks.html).

## PingAccess cluster upgrade parameters

The command-line parameters are the same regardless of the platform, and are defined as follows.

### Parameter definitions

| Parameter                          | Value description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -r \| --disable-config-replication | Disables configuration replication on the admin node. For more information about using this parameter in an upgrade, see the [Zero Downtime Upgrade](../pingaccess_zero_downtime_upgrade/pa_zero_downtime_upgrade.html).                                                                                                                                                                                                                                                                                                                                                                |
| -p *\<admin\_port>*                | Optional port to be used by the temporary PingAccess instance run during the upgrade. The default is 9001.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -i *\<directory>*                  | An optional directory containing additional library JAR files, such as plugins, Java Database Connectivity (JDBC) drivers to be copied into the target installation.Beginning in version 6.0, `JAR` files are stored in the `<PA HOME>/deploy` folder.During an upgrade from versions earlier than 6.0, third-party `JAR` files are migrated from the `lib` folder to the `deploy` folder if no directory is specified.During an upgrade from version 6.0 or later, the contents of the `deploy` folder are migrated to the new `<PA HOME>/deploy` folder if no directory is specified. |
| *\<sourcePingAccessRootDir>*       | The PA\_HOME for the source PingAccess version.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -l *\<newPingAccessLicense>*       | An optional path to the PingAccess license file to use for the target version. If not specified, the existing license is reused.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -j *\<jvm\_memory\_options\_file>* | An optional path to a file with Java Virtual Machine (JVM) *(tooltip: \<div class="paragraph">&#xA;\<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>&#xA;\</div>)* memory options to use for the new PingAccess instance during the upgrade.                                                                                                                                                                                                                                                                      |
| -s \| --silent                     | Run the upgrade with no user input required. To use this option, specify the source version's credentials using environment variables.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

### Environment variables

You can specify the username and password for the source version using these environment variables:

* `PA_SOURCE_API_USERNAME` – The username for the source version's Admin API. This should be set to Administrator.

* `PA_SOURCE_API_PASSWORD` – The basic authorization password for the Administrator in the source version's Admin API.

### Java virtual machine (JVM) memory options

These options can be included in the JVM memory options file. Memory amounts use `m` or `g` to specify the unit.

* `-Xms<amount>` – Minimum heap size.

* `-Xmx<amount>` – Maximum heap size.

* `-XX:NewSize=<amount>` – Minimum size for the Young Gen space.

* `-XX:MaxNewSize=<amount>` – Maximum size for the Young Gen space.

* `-XX:+UseParallelGC` – Specifies that the parallel garbage collector should be used.

You can copy the existing `<PA_HOME>/conf/jvm-memory.options` file to create a JVM memory options file for the upgrade.

### Example

```
#Sample JVM Memory options file
-Xms512m
-Xmx1g
-XX:NewSize=256m
-XX:MaxNewSize=512m
-XX:+UseParallelGC
```

---

---
title: Upgrading a PingAccess standalone version using the incremental update package
description: Upgrade a standalone PingAccess deployment to a newer version using the incremental update package.
component: pingaccess
version: 9.1
page_id: pingaccess:upgrading_pingaccess:pa_upgrading_a_pa_standalone_version_using_the_incremental_update_package
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/upgrading_pingaccess/pa_upgrading_a_pa_standalone_version_using_the_incremental_update_package.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 5, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Upgrading a PingAccess standalone version using the incremental update package

Upgrade a standalone PingAccess deployment to a newer version using the incremental update package.

## Before you begin

* Make a backup copy of the PingAccess home directory. If the upgrade fails, use the backup copy to restore PingAccess.

* Review the release notes for every version between your current version and the target version.

* Verify that you have the following:

  * The PingAccess incremental update `.zip` file for the target version

  * Administrator credentials for the running PingAccess instance

* Verify that basic authentication is configured and enabled for the running PingAccess instance.

* Verify that the PingAccess host is running.

## About this task

Use the PingAccess incremental update bundle to upgrade from PingAccess 6.3 or later, the source version, to the most recent maintenance release for that version of PingAccess, the target version. For example, upgrade PingAccess 6.3 to the most recent maintenance release for 6.3.

## Steps

1. Stop PingAccess.

2. Open the `readme` file included in the extracted `.zip` bundle.

3. Make the file changes specified in the `readme` file.

4. Restart PingAccess.

## Next steps

After you complete the upgrade, see [Performing post-upgrade tasks](pa_performing_post_upgrade_tasks.html).

---

---
title: Upgrading a PingAccess standalone version using the upgrade utility
description: Upgrade a standalone PingAccess deployment to a newer version.
component: pingaccess
version: 9.1
page_id: pingaccess:upgrading_pingaccess:pa_upgrading_a_pa_standalone_version_using_the_upgrade_utility
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/upgrading_pingaccess/pa_upgrading_a_pa_standalone_version_using_the_upgrade_utility.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  example: Example:
  next-steps: Next steps
  pingaccess-standalone-upgrade-parameters: PingAccess standalone upgrade parameters
  environment-variables: Environment variables
  java-virtual-machine-jvm-memory-options: Java virtual machine (JVM) memory options
  example-2: Example
---

# Upgrading a PingAccess standalone version using the upgrade utility

Upgrade a standalone PingAccess deployment to a newer version.

## Before you begin

* If you are using PingAccess 3.2 or earlier, upgrade to PingAccess 4.3 or 5.3 before upgrading to the current version of PingAccess.

* Create a backup of your existing PingAccess configuration. If the upgrade fails, restore your environment from this backup.

* Review the release notes for every version between your current version and the target version.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | In release 5.0, there are potentially breaking changes to the Software Development Kit (SDK) *(tooltip: \<div class="paragraph">&#xA;\<p>A set of tools that allows a developer to build a custom application that integrates with or connects to a platform or service.\</p>&#xA;\</div>)* for Java, Groovy scripts, and the administrative application programming interface (API) *(tooltip: \<div class="paragraph">&#xA;\<p>A specification of interactions available for building software to access an application or service.\</p>&#xA;\</div>)*. For information on these changes and the actions administrators might need to take, review the [Upgrade considerations](pa_upgrade_considerations.html) and the [PingAccess 5.0](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-50.pdf#page=263) release notes. |

* Verify that you have the following:

  * The PingAccess distribution `.zip` file

  * Your new PingAccess license file, if you plan to switch to a new license file

  * Sign on access to the PingAccess host, as the utility is run on the host

  * Administrator credentials for the running PingAccess instance

* Verify that basic authentication is configured and enabled for the running PingAccess instance.

* Verify that the PingAccess host is running.

* Verify that you are using the same account normally used to run PingAccess.

|   |                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you have set `security.overridePropertiesFile=false` in `$JAVA_HOME/jre/lib/java.security`, the upgrade utility might fail because the PingAccess upgrade utility uses an override to enable deprecated ciphers and protocols during the upgrade process. |

## About this task

Use the PingAccess upgrade utility to upgrade from PingAccess 4.0 or later, the source version, to the most recent version, the target version.

The upgrade utility starts an instance of PingAccess with an administrative listener on port 9001. This port number can be changed using the `upgrade.bat` or `upgrade.sh` `-p` parameter. This port configuration is only used for the upgrade. The configured port is used by the upgraded server when the upgrade is complete.

Any warnings or errors encountered are recorded in `log/upgrade.log`, as well as on-screen while the utility is being run. The upgrade uses an exit code of 0 to indicate a successful upgrade and an exit code of 1 to indicate failure.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you are upgrading from version 4.3 or earlier, and your installation uses custom plugins, they must be rebuilt using the SDK version included in PingAccess 5.0 or later. Run the upgrade utility manually with the new `-i` command-line option to specify a directory containing the custom plugin JAR files and only the custom plugin JAR files. To migrate your custom plugins, see the [PingAccess Addon SDK for Java Migration Guide](../agents_and_integrations/pa_add_on_sdk_for_java_migration_guide.html). |

|   |                                                                                    |
| - | ---------------------------------------------------------------------------------- |
|   | During the upgrade, do not make any changes to the running PingAccess environment. |

## Steps

1. Copy the `.zip` file for the new PingAccess version to the PingAccess host and extract it.

2. Change to the new version's `/upgrade/bin` directory.

3. Run the PingAccess upgrade utility:

   ### Choose from:

   * On Windows: `upgrade.bat [-p <admin_port>] [-i <directory>] [-j <jvm_memory_options_file>] [-l <newPingAccessLicense>] [-s | --silent] <sourcePingAccessRootDir>`

   * On Linux: `./upgrade.sh [-p <admin_port>] [-i <directory>] [-j <jvm_memory_options_file>] [-l <newPingAccessLicense>] [-s | --silent] <sourcePingAccessRootDir>`

     ### Example:

     For example: `./upgrade.sh -p 9002 -i MyJARDir pingaccess-5.3`

## Next steps

After you complete the upgrade, see [Performing post-upgrade tasks](pa_performing_post_upgrade_tasks.html).

## PingAccess standalone upgrade parameters

The command-line parameters are the same regardless of the platform and are defined in the following table.

| Parameter                          | Value description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -p *\<admin\_port>*                | Optional port to be used by the temporary PingAccess instance run during the upgrade. The default is 9001.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -i *\<directory>*                  | An optional directory containing additional library JAR files, such as plugins and Java Database Connectivity (JDBC) drivers, to be copied into the target installation.Beginning in version 6.0, JAR files are stored in the `<PA HOME>/deploy` folder.During an upgrade from versions earlier than 6.0, third-party JAR files are migrated from the `lib` folder to the `deploy` folder if no directory is specified.During an upgrade from version 6.0 or later, the contents of the `deploy` folder are migrated to the new `<PA HOME>/deploy` folder if no directory is specified. |
| *\<sourcePingAccessRootDir>*       | The `PA_HOME` for the source PingAccess version.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -l *\<newPingAccessLicense>*       | An optional path to the PingAccess license file to use for the target version. If not specified, the existing license is reused.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -j *\<jvm\_memory\_options\_file>* | An optional path to a file with Java Virtual Machine (JVM) *(tooltip: \<div class="paragraph">&#xA;\<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>&#xA;\</div>)* options to use for the new PingAccess instance during the upgrade.                                                                                                                                                                                                                                                                             |
| -s \| --silent                     | Run the upgrade with no user input required. To use this option, specify the source version's credentials using environment variables.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

### Environment variables

You can specify the username and password for the source version using these environment variables:

* `PA_SOURCE_API_USERNAME` – The username for the source version's Admin API. This should be set to Administrator.

* `PA_SOURCE_API_PASSWORD` – The basic authorization password for the Administrator in the source version's Admin API.

### Java virtual machine (JVM) memory options

You can include these options in the JVM memory options file. Memory amounts use `m` or `g` to specify the unit.

* `-Xms<amount>` – Minimum heap size

* `-Xmx<amount>` – Maximum heap size

* `-XX:NewSize=<amount>` – Minimum size for the Young Gen space

* `-XX:MaxNewSize=<amount>` – Maximum size for the Young Gen space

* `-XX:+UseParallelGC` – Specifies that the parallel garbage collector should be used

You can copy the existing `<PA_HOME>/conf/jvm-memory.options` file to create a JVM memory options file for the upgrade.

### Example

```
#Sample JVM Memory options file
-Xms512m
-Xmx1g
-XX:NewSize=256m
-XX:MaxNewSize=512m
-XX:+UseParallelGC
```

---

---
title: Upgrading PingAccess
description: Learn how to upgrade your PingAccess server to a more recent target version.
component: pingaccess
version: 9.1
page_id: pingaccess:upgrading_pingaccess:pa_upgrading_pa_landing_topic
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/upgrading_pingaccess/pa_upgrading_pa_landing_topic.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 11, 2026
---

# Upgrading PingAccess

Learn how to upgrade your PingAccess server to a more recent target version. After reviewing the [Upgrade considerations](pa_upgrade_considerations.html), complete the procedure relevant to your environment:

* [Upgrading a PingAccess standalone version using the upgrade utility](pa_upgrading_a_pa_standalone_version_using_the_upgrade_utility.html)

* [Upgrading a PingAccess cluster using the upgrade utility](pa_upgrading_a_pa_cluster_using_the_upgrade_utility.html)

* [Upgrading PingAccess using the Windows installer](pa_upgrading_pa_using_the_windows_installer.html)

* [Upgrading a PingAccess standalone version using the incremental update package](pa_upgrading_a_pa_standalone_version_using_the_incremental_update_package.html)

* [Upgrading a PingAccess cluster using the incremental update package](pa_upgrading_a_pa_cluster_using_the_incremental_upgrade_package.html)

|   |                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you have a clustered environment and want to upgrade PingAccess without impacting resource availability, learn more in [PingAccess zero downtime upgrade](../pingaccess_zero_downtime_upgrade/pa_zero_downtime_upgrade.html). |

You can find more information about what to do during or after your upgrade in:

* [Performing post-upgrade tasks](pa_performing_post_upgrade_tasks.html)

* [Restoring a PingAccess configuration backup](pa_restoring_a_pa_configuration_backup.html)

* [Upgrade Troubleshooting](pa_upgrade_troubleshooting.html)

* [Upgrade utility configuration file reference](pa_upgrade_utility_config_file_ref.html)

---

---
title: Upgrading PingAccess using the Windows installer
description: Upgrade PingAccess if you installed PingAccess using the Windows installer.
component: pingaccess
version: 9.1
page_id: pingaccess:upgrading_pingaccess:pa_upgrading_pa_using_the_windows_installer
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/upgrading_pingaccess/pa_upgrading_pa_using_the_windows_installer.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  result: Result:
  next-steps: Next steps
---

# Upgrading PingAccess using the Windows installer

Upgrade PingAccess if you installed PingAccess using the Windows installer.

## Before you begin

* If you are using PingAccess 3.2 or earlier, you must upgrade to PingAccess 4.3 or 5.3 before upgrading to PingAccess 6.0.

* Review the [Upgrade considerations](pa_upgrade_considerations.html).

## About this task

|   |                                                                                                                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If additional JAR files, such as custom plugins and Java database connectivity (JDBC) drivers, have been added to the existing PingAccess `/lib` directory, the 5.0-Beta installer cannot be used to perform the upgrade. Instead, run the upgrade utility manually, using the `-i` command-line option to specify the JAR files to be included. |

## Steps

1. Download the installer.

2. Start the installer.

   ### Result:

   The existing installation is detected.

3. To upgrade the installation, click **Yes**.

4. If you are switching to a new license, select a license file and specify a temporary admin port.

   |   |                                                                         |
   | - | ----------------------------------------------------------------------- |
   |   | The temporary admin port is not required when upgrading a cluster node. |

5. Click **Next**.

6. Specify the administrator credentials. Click **Next**.

   |   |                                                                           |
   | - | ------------------------------------------------------------------------- |
   |   | Administrator credentials are not required when upgrading a cluster node. |

7. Click **Finish**.

## Next steps

After completing the upgrade, [Performing post-upgrade tasks](pa_performing_post_upgrade_tasks.html).