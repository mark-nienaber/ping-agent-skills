---
title: An improved index in the database table for OAuth clients
description: PingFederate 8.4 added the value column to an existing index (IDX_FIELD_NAME) in the pingfederate_oauth_clients_ext table as a general improvement.
component: pingfederate
version: 13.1
page_id: pingfederate:upgrading_pingfederate:pf_improv_index_datab_table_oauth_cli
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/upgrading_pingfederate/pf_improv_index_datab_table_oauth_cli.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  related-links: Related links
---

# An improved index in the database table for OAuth clients

PingFederate 8.4 added the `value` column to an existing index (`IDX_FIELD_NAME`) in the `pingfederate_oauth_clients_ext` table as a general improvement.

This information is applicable only to customers who configured PingFederate to store OAuth clients on a database server.

You must modify the index in your existing `pingfederate_oauth_clients_ext` table.

Although there is no alter-table script provided, you can derive the setup from the new table-setup scripts in the `<pf_install>/pingfederate/server/default/conf/oauth-client-management/sql-scripts/oauth-client-management-<databaseServer>.sql` file.

|   |                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------- |
|   | If your initial installation of PingFederate was version 8.4 or later, you don't need to run this script. |

## Related links

* [Configuring external databases for client storage](../administrators_reference_guide/pf_configuring_external_databases_client_storage.html).

---

---
title: Copying customized files or settings
description: After you upgrade PingFederate, you must copy files that were customized in the previous release to the current installation.
component: pingfederate
version: 13.1
page_id: pingfederate:upgrading_pingfederate:pf_copying_custom_files_settings
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/upgrading_pingfederate/pf_copying_custom_files_settings.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  user-facing-windows: User-facing windows
  email-notifications: Email notifications
  jetty-or-jboss-configuration: Jetty or JBoss configuration
  the-size-limits-conf-file: The size-limits.conf file
  cross-origin-resource-sharing-cors-support-for-oauth-endpoints: Cross-origin resource sharing (CORS) support for OAuth endpoints
  configuration-files-in-the-config-store-directory: Configuration files in the config-store directory
  other-configuration-files: Other configuration files
---

# Copying customized files or settings

After you upgrade PingFederate, you must copy files that were customized in the previous release to the current installation.

## User-facing windows

If you modified any Velocity templates for user-facing windows, to preserve the customized user experience, some of your custom changes must be migrated manually to the new installation manually for each server node.

The templates are located in the `<pf_install>/pingfederate/server/default/conf/template` directory.

As of PingFederate 11.0, the Upgrade Utility migrates your modified Velocity HTML templates to the new installation. The default templates in the new installation that correspond to the modified templates are renamed with the following format: `<template_name>-default-<PF-version>.<ext>`.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Supporting CSS and image file names changed as of PingFederate 7.0. For each modified HTML template copied, add `.1` to the base name for each CSS file referenced in the header, for example, `<link rel="…​" href="assets/css/window.1.css"/>`.Add `.1` to any references in the copied templates to the installed image files contained in the `assets/images` directory, for example, `<img src="assets/images/green_check.1.png"/>`. |

## Email notifications

If you modified the email notification templates before PingFederate 9.2, manually migrate your custom changes to the new HTML-based templates for each server node.

The plain text templates (`message-template-*.txt`) are located in `<pf_install>/pingfederate/server/default/conf` in the source installation. The new HTML-based templates are located in `<pf_install>/pingfederate/server/default/conf/template/mail-notifications` with the same file naming convention but an `.html` file extension.

As of PingFederate 11.0, the Upgrade Utility migrates your modified Velocity HTML templates to the new installation. The default templates in the new installation that correspond to the modified templates are renamed with the following format: `<template_name>-default-<PF-version>.<ext>`.

## Jetty or JBoss configuration

If you have modified any Jetty or JBoss settings that need to be carried forward, you must make the corresponding changes manually in the new PingFederate deployment.

If you are upgrading from PingFederate 6.9 or later, merge any changes in `<pf_install>/etc/jetty-runtime.xml` and `<pf_install>/etc/jetty-admin.xml` files into the corresponding files of the new deployment.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If only the values of the `minThreads`, `maxThreads`, and `acceptQueueSize` parameters were modified in those Jetty files, you should set those values in the new deployment's `<pf_install>/bin/run.properties` file instead of merging them into the Jetty files.The advantage of setting those values in `run.properties` is that PingFederate can automatically merge `run.properties`customizations into new deployments, saving you time and preventing errors in future upgrades. For more information, see [Configuring PingFederate properties](../administrators_reference_guide/pf_config_pf_propert.html). |

If you are upgrading from PingFederate 6.0 through 6.8, first identify any changes made to the JBoss configuration, then make corresponding changes for the newer Jetty configuration.

For example, if you modified the `<pf_install>/pingfederate/server/default/deploy/jetty.sar/META-INF/jboss-service.xml` file before 6.9, identify the changes and make the same modifications at corresponding points in either the `jetty-admin.xml` or `jetty-runtime.xml` files located in the new Jetty configuration directory, `<pf_install>/pingfederate/etc`.

## The size-limits.conf file

Before PingFederate 8.4.2, the `InterReqStateMgmtMapImpl.expiry.mins` setting in the `<pf_install>/pingfederate/server/default/conf/size-limits.conf` file defines the lifetime of the Adapter session-state data and Inter-request state information data sets.

* Adapter session-state data

  The state information, along with the associated attributes and any of their values, maintained or used by the adapters.

* Inter-request state information

  The state information between the redirects to complete a request.

PingFederate 8.4.2 and later splits the `InterReqStateMgmtMapImpl.expiry.mins` settings into two settings, one setting for each data type.

| New settings                                     | Data type                       | Default value in minutes |
| ------------------------------------------------ | ------------------------------- | ------------------------ |
| `InterReqStateMgmtMapImpl.expiry.mins.state.map` | Inter-request state information | 30                       |
| `InterReqStateMgmtMapImpl.expiry.mins.attr.map`  | Adapter session-state data      | 1440 (24 hours)          |

The new settings reduce the memory footprint of PingFederate by purging the inter-request state information after 30 minutes and retaining adapter session-state data during the day.

If you previously modified the value of the `InterReqStateMgmtMapImpl.expiry.mins` setting, when migrating your change to the latest version, adjust the value of the new settings based on your requirements.

## Cross-origin resource sharing (CORS) support for OAuth endpoints

If you previously edited the `<pf_install>/pingfederate/etc/webdefault.xml` file to enable CORS support for OAuth endpoints, instead of updating the `webdefault.xml` file, define the allowed origins manually using the PingFederate administrative console after the upgrade.

For more information, see [Configuring authorization server settings](../administrators_reference_guide/help_authorizationserversettingstasklet_oauthauthorizationserversettingsstate.html).

## Configuration files in the config-store directory

If you added or replaced setting values in configuration files stored in the `<pf_install>/pingfederate/server/default/data/config-store` directory, the PingFederate upgrade tools copy these setting values to the new installation.

|   |                                                                                                |
| - | ---------------------------------------------------------------------------------------------- |
|   | The upgrade tools do not copy comments from the existing installation to the new installation. |

If you removed a setting or a block of settings from a configuration file in the `config-store` directory, the upgrade tool preserves your changes by removing the setting or block of settings from the new installation and records the removals in its log file.

To re-add a setting or block of settings to the new installation, compare the configuration file found in the new installation to the file found in the product distribution `.zip` archive and make your changes.

## Other configuration files

As of PingFederate 10.0, the upgrade process copies many files automatically. However, there are still some files that you must copy manually, which you can find in `<pf_install>/pingfederate/server/default/conf`.

The following files are copied automatically:

* Properties files with the `.conf` extension

* The `log4j2.db.properties` file

* The `jmx-remote-config.xml` file

* The `csd_configuration.yaml` file

* Non-default files located in the `template` directory

If you modified the default templates located in `<pf_install>/pingfederate/server/default/conf/template`, you must customize these templates in the new PingFederate installation.

If you modified versions of `tcp.xml`, `udp.xml`, and `log4j2.xml`, they are copied over intact. The default files are saved in the target directory with a different extension. To take advantage of the improvements in the default versions of these files, merge your changes into the current default files and then rename them appropriately.

|   |                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you are upgrading from 8.0 or earlier, PingFederate might not start until you have merged your changes into the current default files because of JGroups errors. |

Other files, such as `jmx.remote.access`, are not copied to the new installation automatically. To preserve any custom settings, create a backup of the current configuration files and merge your changes to the current files.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you previously customized Java virtual machine (JVM) options in the `run.bat` or `run.sh` files, instead of updating these files, manually merge your JVM options to the `<pf_install>/pingfederate/bin/jvm-memory.options` file. For more information, see [Fine-tuning JVM options](../performance_tuning_guide/pf_fine_tuning_jvm_option.html) and [memoryoptions and upgrade](../performance_tuning_guide/pf_memoryoptions_upgrade.html). |

---

---
title: Custom mode in the Upgrade Utility
description: The custom-mode feature in the Upgrade Utility (invoked with the -c option on the command line) allows you to override several default security settings.
component: pingfederate
version: 13.1
page_id: pingfederate:upgrading_pingfederate:pf_custom_mode
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/upgrading_pingfederate/pf_custom_mode.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 21, 2025
section_ids:
  security-defaults: Security defaults
  adapter-upgrade: Adapter upgrade
---

# Custom mode in the Upgrade Utility

The custom-mode feature in the Upgrade Utility (invoked with the `-c` option on the command line) allows you to override several default security settings.

Running the Upgrade Utility in custom mode also allows you to update to the latest version of any integration bundled with PingFederate, such as the [OpenToken Adapter](https://docs.pingidentity.com/integrations/java/pf_java_ik_overview_of_the_opentoken_adapter.html), [Agentless Integration Kit](https://docs.pingidentity.com/integrations/agentless/pf_agentless_ik.html), and [PingID Provisioner](https://docs.pingidentity.com/integrations/pingid/pf_pid_connector.html).

## Security defaults

Using the security defaults shouldn't cause significant issues for most PingFederate installations. The more recent default security settings include:

* Disabling weaker cipher suites for both the SUN and LUNA Java Cryptography Extension (JCE) in PingFederate version 6.2 and later. To see which cipher suites are commented out, choose yes (`y`) when prompted on whether to use the new defaults. After the upgrade is complete, refer to one of the following configuration files in the new installation's `<pf_install>/pingfederate/server/default/data/config-store` directory:

* `com.pingidentity.crypto.SunJCEManager.xml`

* `com.pingidentity.crypto.AWSCloudHSMJCEManager.xml`

* `com.pingidentity.crypto.LunaJCEManager.xml`

* `com.pingidentity.crypto.NcipherJCEManager.xml`

* `com.pingidentity.crypto.BCFIPSJCEManager.xml`

## Adapter upgrade

Upgrading the OpenToken Adapter from an earlier version doesn't normally require any follow-on configuration changes.

* If your existing installation uses a version of the OpenToken Adapter earlier than 2.3, upgrading requires minor configuration modifications in the PingFederate console and redeployment of the agent configuration file.

* If you're upgrading from an OpenToken version earlier than 2.5.1, you should redeploy the agent configuration files, if applicable, as well as any new agent libraries contained in recent versions of PingFederate integration kits and other plugins that use `OpenToken`.

---

---
title: Downloading PingFederate
description: You can download the latest version of PingFederate from the PingFederate Downloads website.
component: pingfederate
version: 13.1
page_id: pingfederate:upgrading_pingfederate:pf_download_pf
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/upgrading_pingfederate/pf_download_pf.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 29, 2025
---

# Downloading PingFederate

You can download the latest version of PingFederate from the [PingFederate Downloads](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) website.

The distribution `.zip` archive can be used to upgrade PingFederate on both Windows and Linux.

|   |                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You must be logged in to PingOne to download PingFederate.If you're a Ping Identity customer, you can use the **Sign On** button at the top right of the **Downloads** page.If you're not yet a Ping Identity customer, you can start a free trial of PingOne. Learn more in [Starting a PingOne trial](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_start_a_p1_trial.html). |

To download the PingFederate product distribution `.zip` archive, click **Product Distribution (ZIP)**.

After you download the PingFederate product distribution `.zip` archive, learn how to complete the upgrade in [Upgrading PingFederate installations](pf_upgrade_pf_installations.html).

---

---
title: Enabling security enhancement in JDBC datastore queries
description: Edit the org.sourceid.common.SqlFilterManager.xml file for stronger security protection in a JDBC datastore.
component: pingfederate
version: 13.1
page_id: pingfederate:upgrading_pingfederate:pf_secur_enhance_jdbc_datastore_queries
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/upgrading_pingfederate/pf_secur_enhance_jdbc_datastore_queries.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 20, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  example: Example:
---

# Enabling security enhancement in JDBC datastore queries

Edit the `org.sourceid.common.SqlFilterManager.xml` file for stronger security protection in a JDBC datastore.

## About this task

|   |                                                                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you are upgrading from PingFederate 8.4.4 or earlier, modify the `<pf_install>/pingfederate/server/default/data/config-store/org.sourceid.common.SqlFilterManager.xml` file to enable the safeguard for JDBC datastore queries against backend SQL injection attacks. |

## Steps

1. Edit the `org.sourceid.common.SqlFilterManager.xml` file.

2. Set the `<item name="enableSqlFilters"/>` element value to `true`.

   ### Example:

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <config xmlns="http://www.sourceid.org/2004/05/config">
       <item name="enableSqlFilters">true</item>
   </config>
   ```

3. Save the file.

4. Restart PingFederate.

5. If you have a clustered PingFederate environment, push this change to all engine nodes:

   1. On the administrative console, go to **System > Server > Cluster Management**.

   2. Click **Replicate**.

6. Verify your use cases to make sure your search filters return the expected results.

---

---
title: Logging configurations
description: PingFederate uses log4j2 to write log messages.
component: pingfederate
version: 13.1
page_id: pingfederate:upgrading_pingfederate:pf_logging_configs
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/upgrading_pingfederate/pf_logging_configs.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  merging-custom-logging-configurations: Merging custom logging configurations
  about-this-task: About this task
  steps: Steps
---

# Logging configurations

PingFederate uses log4j2 to write log messages.

If the configuration file for Log4j 2 (or Log4j) has been modified in the source installation, manually merge the configuration changes into the upgraded environment.

## Merging custom logging configurations

### About this task

The upgrade tools do not support automatic merging of customizations made to the existing logging configuration. Instead, these upgrade tools copy the modified `log4j2.xml` file to the new installation intact and rename the configuration file from the product `.zip` archive using the new PingFederate version number. Both configuration files are located in the same `conf` directory.

|   |                                                                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If the Upgrade Utility or the PingFederate installer for Windows determines that the log4j2 configuration file ( `<pf_install>/pingfederate/server/default/conf/log4j2.xml`) has changed since it was originally installed, new features are not activated. |

To activate new features:

### Steps

1. Review the new features by comparing the renamed log4j2 configuration file against the `log4j2.xml` file.

2. Modify the `log4j2.xml` file to suit your needs.

3. If you have a clustered PingFederate environment, repeat step 2 for all applicable PingFederate nodes in the cluster.

---

---
title: Migrating other components
description: Some custom and integrated components might require additional steps after upgrading PingFederate.
component: pingfederate
version: 13.1
page_id: pingfederate:upgrading_pingfederate:pf_migrate_other_componen
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/upgrading_pingfederate/pf_migrate_other_componen.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  updating-the-custom-authentication-selector: Updating the custom authentication selector
  migrating-to-the-integrated-ldap-username-pcv: Migrating to the integrated LDAP Username PCV
  about-this-task: About this task
  steps: Steps
  related-links: Related links
  migrating-to-the-integrated-username-token-processor: Migrating to the integrated Username Token Processor
  about-this-task-2: About this task
  steps-2: Steps
  related-links-2: Related links
---

# Migrating other components

Some custom and integrated components might require additional steps after upgrading PingFederate.

## Updating the custom authentication selector

Through the use of the PingFederate SDK, you can create a custom authentication selector by implementing the `AuthenticationSelector` interface.

Most implementations return `AuthenticationSelectorContext.ResultType.CONTEXT` as the result type, which requires no further action after an upgrade.

If your implementation returns either:

* `AuthenticationSelectorContext.ResultType.ADAPTER_ID`, an Identity Provider (IdP) adapter instance ID

* `AuthenticationSelectorContext.ResultType.IDP_CONN_ID`, the connection ID of an IdP connection

You must update the descriptor instance of your custom authentication selector to call the `setSelectAuthnSourceResultType` method with an input of `true`. For each authentication policy path that ends with an instance of such custom authentication selector, you must ensure that its action is set to **Done**.

For more information, see the Javadoc for the `AuthenticationSelector` interface and the `AuthenticationSelectorDescriptor` class.

|   |                                                                                               |
| - | --------------------------------------------------------------------------------------------- |
|   | The Javadoc for PingFederate is located in the `<pf_install>/pingfederate/sdk/doc` directory. |

## Migrating to the integrated LDAP Username PCV

### About this task

As of PingFederate 7.3, the integrated LDAP Username Password Credential Validator (PCV) can return additional attribute values upon successful validation.

If you have previously deployed the `LDAPExtendedAttributesPCV-<version>.jar` file from the PingID integration kit and created an instance of the LDAP PCV with Extended Attributes, migrate to the integrated LDAP Username PCV.

### Steps

1. Create an instance of the integrated LDAP Username PCV:

   1. Go to **System > Data & Credential Stores > Password Credential Validators** and click **Create New Instance**.

   2. On the **Type** tab, enter the required information and select **LDAP Username Password Credential Validator** from the list.

   3. On the **Instance Configuration** tab, select an LDAP datastore from the list, enter a search base and a search filter, and select the scope of the search.

      |   |                                                                                             |
      | - | ------------------------------------------------------------------------------------------- |
      |   | You can reuse the information from the existing LDAP PCV with Extended Attributes instance. |

   4. On the **Extended Contract** tab, enter `memberOf` in the **Extend the Contract** section, and click **Add.**

   5. On the **Summary** tab, review the setup and click **Done**.

   6. On the **Manage Credential Validator Instances** page, click **Save**.

2. In the configuration where the LDAP PCV with Extended Attributes instance is used, replace it with the newly created LDAP Username Password Credential Validator instance.

   For example, if you have created an instance of the PingID PCV (with integrated RADIUS server) instance and have selected an instance of the LDAP PCV with Extended Attributes as one of the delegate PCVs, remove the selection and add the newly created LDAP Username Password Credential Validator instance to the list.

3. After replacing the LDAP PCV with Extended Attributes instance, delete it from the **Password Credential Validators** page.

4. Remove the `<pf_install>/pingfederate/server/default/deploy/LDAPExtendedAttributesPCV-<version>.jar` file on all PingFederate servers.

5. Restart PingFederate on all PingFederate servers.

### Related links

* [Configuring the LDAP Username Password Credential Validator](../administrators_reference_guide/pf_configure_ldap_username_pcv.html)

## Migrating to the integrated Username Token Processor

### About this task

As of PingFederate 7.2, the Username Token Translator has been deprecated and replaced with an integrated Username Token Processor. Although the integrated Username Token Processor and the deprecated Username Token Translator can be simultaneously deployed, you should migrate it to the new token processor.

### Steps

1. Go to **Identity Provider > Token Processors**.

2. To create an instance of the integrated Username Token Processor, click **Create New Instance**.

   1. On the **Type** page, select **Username Token Processor** from the list.

      |   |                                                                                                                                                                              |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | If you have multiple WS-Trust STS SP connections, you can reuse the same Username Token Processor instance or create additional instances of the token processors as needed. |

3. Map the new token processor instance to the applicable WS-Trust STS SP connection on the **IdP Token Processor Mapping** page.

   Repeat this step if you have multiple WS-Trust STS SP connections.

4. Test your WS-Trust STS SP connections using the instance of the integrated Username Token Processor.

5. Remove the token processor instance of the deprecated Username Token Translator from all WS-Trust STS SP connections on the **IdP Token Processor Mapping** page.

6. If you have set up token translator mappings, create new entries to replace those using instances of the deprecated Username Token Translator, test the new mapping entries, and delete the entries that use instances of the deprecated Username Token Translator.

7. Delete all token processor instances of the deprecated Username Token Translator on the **Identity Provider > Token Processors** page.

8. Remove the `pf-username-token-translator-<version>.jar` file from the `<pf_install>/pingfederate/server/default/deploy` directory on all PingFederate servers.

9. Restart PingFederate on all PingFederate servers.

### Related links

* [Managing token processors](../administrators_reference_guide/pf_managing_token_processors.html)

* [Managing IdP token processor mappings](../administrators_reference_guide/help_wstrustsptokencreationtasklet_wstrusttokenprocessormappingstate.html)

* [Token translator mappings](../administrators_reference_guide/pf_token_translator_mappings.html)

* [IdP protocol endpoints](../administrators_reference_guide/help_idp_protocol_endpoints.html)

---

---
title: Post-upgrade tasks
description: Confirm your new PingFederate installation configurations and settings.
component: pingfederate
version: 13.1
page_id: pingfederate:upgrading_pingfederate:pf_post_upgrade_tasks
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/upgrading_pingfederate/pf_post_upgrade_tasks.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
---

# Post-upgrade tasks

Confirm your new PingFederate installation configurations and settings.

After upgrading PingFederate, you might need to:

* [Review administrative users](pf_review_admin_tasks.html)

* [Copy customized files or settings](pf_copying_custom_files_settings.html)

* [Review database changes](pf_review_database_change.html)

* [Review the log configuration](pf_logging_configs.html)

* [Migrate other components](pf_migrate_other_componen.html)

* [Reset files and variables for HSM](pf_reset_file_variable_hsm.html)

* [Verify the new installation](pf_verify_new_install.html)

You should also perform runtime tests to ensure the new PingFederate installation fulfills your existing use cases.

---

---
title: Preparing to upgrade PingFederate
description: Prepare to upgrade PingFederate by completing a number of tasks.
component: pingfederate
version: 13.1
page_id: pingfederate:upgrading_pingfederate:pf_prepare_upgrade_pf
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/upgrading_pingfederate/pf_prepare_upgrade_pf.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 13, 2023
section_ids:
  steps: Steps
---

# Preparing to upgrade PingFederate

Prepare to upgrade PingFederate by completing a number of tasks.

## Steps

* Review the PingFederate release notes for enhancements, upgrade considerations, deprecated features, and other known issues and limitations.

* Review the post-upgrade tasks.

* Review potential changes in system and port requirements.

* Obtain a new license key if needed.

* Update the Java runtime environment (JRE) to version 11 or 17 on your PingFederate servers if needed.

  When you upgrade the JRE, modify the previously defined paths for the system *\<JAVA\_HOME>* and *\<PATH>* environment variables.

  |   |                                                                                                                                                                                                                                                                            |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | PingFederate 7.2 and earlier will not start using the currently supported Java runtime. If you need to start the previous PingFederate version on the same server after the upgrade, retain the older Java installation and change environment variables back when needed. |

* Complete any unfinished connections (Drafts) in the administrative console if you want to include them in the migration.

---

---
title: Provisioning datastore reset
description: If you are upgrading from PingFederate 9.0.0 or 9.0.1, reset the provisioning datastore on the upgraded installation.
component: pingfederate
version: 13.1
page_id: pingfederate:upgrading_pingfederate:pf_provis_datastore_reset
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/upgrading_pingfederate/pf_provis_datastore_reset.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Provisioning datastore reset

If you are upgrading from PingFederate 9.0.0 or 9.0.1, reset the provisioning datastore on the upgraded installation.

## About this task

Use the `provmgr` command-line tool to reset the provisioning datastore on the upgraded installation.

The `provmgr` command-line tool is located in the `<pf_install>/pingfederate/bin` directory:

* Windows: `provmgr.bat`

* Linux: `provmgr.sh`

For more information about the `provmgr` command-line tool, see [Outbound provisioning CLI](../administrators_reference_guide/pf_outbound_provision_cli.html).

## Steps

1. To obtain a list of provisioning channel IDs, run the following command:

   ```
   provmgr --show-channels
   ```

2. Reset the provisioning datastore for a given channel by its ID:

   ```
   provmgr -c  <channel_id>  --reset-all
   ```

   |   |                                                                                                                           |
   | - | ------------------------------------------------------------------------------------------------------------------------- |
   |   | If you have multiple provisioning channels, run the command for each channel. The order of the parameters doesn't matter. |

---

---
title: Resetting files and variable for HSM
description: Update your environmental variable in the <pf_install>server/default/data/ncipher-kmdata-local directory to point to the new location.
component: pingfederate
version: 13.1
page_id: pingfederate:upgrading_pingfederate:pf_reset_file_variable_hsm
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/upgrading_pingfederate/pf_reset_file_variable_hsm.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  related-links: Related links
---

# Resetting files and variable for HSM

Update your environmental variable in the `<pf_install>server/default/data/ncipher-kmdata-local` directory to point to the new location.

If your PingFederate installation is configured in a clustered environment with Entrust nShield Connect, you must copy the `<pf_install>server/default/data/ncipher-kmdata-local` directory to the new installation manually and update the environmental variable `NFAST_KMLOCAL` to point to the new location.

## Related links

* [Integrating with Entrust nShield Connect HSM](../getting_started_with_pingfederate/pf_integra_entrus_nshield_connec_hsm.html)

---

---
title: Reviewing administrative users
description: As of PingFederate 10.1, the use of expressions is enabled by default. Additionally, a new administrative role, Expression Admin, has been added.
component: pingfederate
version: 13.1
page_id: pingfederate:upgrading_pingfederate:pf_review_admin_tasks
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/upgrading_pingfederate/pf_review_admin_tasks.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
---

# Reviewing administrative users

As of PingFederate 10.1, the use of expressions is enabled by default. Additionally, a new administrative role, Expression Admin, has been added.

When upgrading to the PingFederate 10.1 or later from a previous version, administrative users who were granted the Admin role in the earlier installation are granted the Expression Admin role automatically. You can achieve the same result by using the `/bulk/import` administrative API endpoint to bulk-import a configuration that was bulk-exported from PingFederate 10.0.

If preferred, administrators can disable the use of expressions by setting `evaluateExpressions` to `false` as described in [Enabling and disabling expressions](../administrators_reference_guide/pf_enable_disable_express.html).

You can also go to **System > Server > Administrative Accounts** and remove the Expression Admin role from all Admin users. Doing this prevents Admin users from entering expressions into PingFederate if the `evaluateExpressions` element is set to `true` at a later time. For more information, see [Administrative accounts](../administrators_reference_guide/help_administrativeaccountstasklet_administrativeaccountsstate.html).

---

---
title: Reviewing database changes
description: Occasionally, PingFederate introduces database-related changes, such as adding a new table, modifying an existing table, or updating the connection pool library, for the purpose of product improvement.
component: pingfederate
version: 13.1
page_id: pingfederate:upgrading_pingfederate:pf_review_database_change
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/upgrading_pingfederate/pf_review_database_change.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 20, 2023
---

# Reviewing database changes

Occasionally, PingFederate introduces database-related changes, such as adding a new table, modifying an existing table, or updating the connection pool library, for the purpose of product improvement.

Neither the Upgrade Utility nor the PingFederate installer for Windows migrates data maintained in the internal HSQLDB database or any external database. For instance, if outbound provisioning is enabled in the new PingFederate instance using the internal database, it's re-initialized from the provisioning source.

|   |                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Use the built-in HSQLDB only for trial or training environments. For testing and production environments, always use a secured external storage solution for proper functioning in a clustered environment.Testing involving HSQLDB is not a valid test. In both testing and production, it might cause various problems due to its limitations and HSQLDB involved cases are not supported by Ping Identity. |

If your PingFederate environment connects to one or more database servers, review the following topics and make changes accordingly:

* [Provisioning datastore reset](pf_provis_datastore_reset.html)

* [Enabling security enhancement in JDBC datastore queries](pf_secur_enhance_jdbc_datastore_queries.html)

* [An improved index in the database table for OAuth clients](pf_improv_index_datab_table_oauth_cli.html)

---

---
title: Updating to the latest maintenance release
description: For PingFederate maintenance releases, you can update your installation using the incremental update package. This in-place update method lets you replace and merge only the files that have changed.
component: pingfederate
version: 13.1
page_id: pingfederate:upgrading_pingfederate:pf_updating_latest_maintenance_release
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/upgrading_pingfederate/pf_updating_latest_maintenance_release.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 26, 2025
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  example: Example:
  example-2: Example:
---

# Updating to the latest maintenance release

For PingFederate maintenance releases, you can update your installation using the incremental update package. This in-place update method lets you replace and merge only the files that have changed.

## Before you begin

* Ensure your installation is running a version of PingFederate that's older than the version you want to upgrade to. To check which version of PingFederate you're running, click the **Question Mark** icon in the navigation bar, then click **About**.

* Make a backup copy of the PingFederate home directory.

## About this task

The in-place update doesn't contain files from Ping Identity integration kits. You can upgrade an integration kit manually by downloading the latest kit from the [PingFederate Downloads](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) page's **Add-ons** tab and following the instructions provided by the kit's documentation.

|   |                                                                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You can't use the in-place update method to upgrade to a newer minor version of PingFederate, such as 10.3.2 or 11.1.4, to version 11.3.x. For those older versions, you must use the standard upgrade method for your platform described in [Upgrading PingFederate](pf_upgrade_pf.html). |

|   |                                                                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The in-place update method involves manual modification of PingFederate files. If you're not comfortable moving and editing these files, you should use the standard upgrade method for your platform described in [Upgrading PingFederate](pf_upgrade_pf.html). |

If your installation includes a cluster, perform the following procedure on each node starting with the administrative console node.

## Steps

1. Go to the [PingFederate Downloads](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) page on the Ping Identity website.

2. In the **Maintenance Update** section, download the **In-place Update (ZIP)** file and extract its contents.

3. Stop PingFederate.

4. Copy the files in the in-place update's `pingfederate` directory and paste them into their corresponding locations in your current PingFederate installation, replacing the old files.

   ### Example:

   If the in-place update contains `pingfederate/server/default/lib/pf-protocolengine.jar`, copy the `pf-protocolengine.jar` file to the same location in your PingFederate installation: `<pf_install>/pingfederate/server/default/lib`.

5. Compare each file in the in-place update's `merge_required` directory with the version of the file in your current PingFederate installation and manually merge the changes into the file in your current installation.

   ### Example:

   If the in-place update contains `merge_required/pingfederate/server/default/conf/language-packs/pingfederate-messages.properties`, copy the changes in the new version into the `pingfederate-messages.properties` file in your PingFederate installation.

6. Start PingFederate.

---

---
title: Upgrade considerations
description: The following modifications since PingFederate 13.0 might affect existing deployments.
component: pingfederate
version: 13.1
page_id: pingfederate:upgrading_pingfederate:pf_upgrade_considerations_13x
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/upgrading_pingfederate/pf_upgrade_considerations_13x.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 5, 2025
---

# Upgrade considerations

The following modifications since PingFederate 13.0 might affect existing deployments.

* OAuth client management service response format

  If you use the in-place method to upgrade to PingFederate 13.0.3 or later, then the OAuth client management service will always return parameters that support multiple values as arrays, even when only a single value is returned.

  To return single values as strings:

  1. Open the `<pingfed-install>/pingfederate/server/default/data/config-store/com.pingidentity.ws.rest.oauth.client_management.model.converter.SerializerUtil.xml` file in a text editor.

  2. Set the `writeSingleItemElementAsArray` parameter to `false`.

  3. Save and close the file.

* Jersey 1.x plugin compatibility

  Older plugins that depend on Jersey 1.x, such as older versions of the **OAuth Playground**, are not compatible with PingFederate. If you have an older version of the **OAuth Playground** installed, upgrade it to a version compatible with PingFederate 13.1, or delete it from your deployment directory before starting PingFederate. For PingFederate 13.1, use OAuthPlayground 6.0.

  If your `server.log` contains an error similar to the following error, review the `server/default/deploy` directory. You must update or remove any plugin that relies on Jersey 1.x libraries.

  Example error

  ```
  java.lang.RuntimeException: java.lang.AbstractMethodError: Receiver class
  com.sun.jersey.api.uri.UriBuilderImpl does not define orinherit an
  implementation of the resolved method 'abstract javax.ws.rs.core.UriBuilder
  uri(java.lang.String)'...
  ```

* Jakarta EE 9 migration and plugin compatibility

  Starting with version 13.1, PingFederate includes Jakarta EE 9 migration updates. If you have deployed other custom or third-party plugins in `<pingfed-install>/pingfederate/server/default/deploy`, update them to versions compatible with PingFederate 13.1 before starting the server.

* `pf.admin.baseurl` must be set

  A defect fix requires the `pf.admin.baseurl` property to be explicitly set in `run.properties`. This prevents admin console URL redirects from failing when PingFederate is accessed through a load balancer with a port that differs from `pf.admin.https.port`.

* Removed support for Java 11

  Starting with version 13.0, PingFederate no longer supports Java 11. Use Java 17 or Java 21 instead. In version 13.1, Java 25 is also supported.

  Learn more in [Java environment](../installing_and_uninstalling_pingfederate/pf_system_requirements.html#java_environment).

* Upgrade from PingFederate 8.x

  Starting with version 13.0, PingFederate no longer supports upgrading from 8.x.

---

---
title: Upgrade considerations introduced in PingFederate 10.x
description: Several specific modifications since PingFederate 10.0 might affect existing deployments.
component: pingfederate
version: 13.1
page_id: pingfederate:upgrading_pingfederate:pf_upgrade_considerations_introduced_pf_10x
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/upgrading_pingfederate/pf_upgrade_considerations_introduced_pf_10x.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
---

# Upgrade considerations introduced in PingFederate 10.x

Several specific modifications since PingFederate 10.0 might affect existing deployments.

* Delayed heartbeat response due to archive import on startup

  Starting with version 10.2, when you place an archive in the `<pf_install>/pingfederate/server/default/data/drop-in-deployer` directory on startup, the heartbeat endpoint will not return `200` until archive import completes. Depending on how long archive import and configuration loading takes, the first successful heartbeat response may be significantly delayed relative to earlier versions. If you have configured a health check or probe that can trigger a restart of the server, crash loop behavior can result. Review the configuration of these checks to ensure time thresholds are set appropriately.

* TLS 1.0 and 1.1 disabled

  Starting with version 10.3, PingFederate disables TLS 1.0 and 1.1 for both inbound and outbound connections by default. As a result, clients using TLS 1.0 or 1.1 will no longer be able to connect to the administrative port or the runtime port. If you must re-enable TLS 1.0 or 1.1, add `TLSv1` or `TLSv1.1` to the `run.properties` file: look for the "TLS Protocol Settings" section and follow the inline instructions. Additionally, you might need to add back the weaker cipher suites, such as TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA, TLS\_ECDH\_RSA\_WITH\_AES\_128\_CBC\_SHA, or TLS\_ECDH\_ECDSA\_WITH\_AES\_128\_CBC\_SHA. For more information, see [Managing cipher suites](../administrators_reference_guide/pf_managing_cipher_suites.html).

* Bouncy Castle FIPS mode

  When upgrading an installation where Bouncy Castle FIPS mode is enabled, it is no longer necessary to place the `bc-fips` jar file in the `JAVA_HOME/jre/lib/ext` directory. It is also no longer necessary to modify the `JAVA_HOME/jre/lib/security/java.security` file. It is recommended to revert these changes to the Java environment.

* SameSite cookie configuration

  As of PingFederate 10.3, the Jetty configuration uses the native servlet SameSite cookie configuration. This moves the SameSite specifier declaration to its own attribute in the Jetty configuration as follows:

  * New format for `jetty-admin.xml` in the DeploymentManager:

    ```
    <Call name="setContextAttribute">
        <Arg>org.eclipse.jetty.cookie.sameSiteDefault</Arg>
        <Arg>None</Arg>
    </Call>
    ```

  * New format for `jetty-runtime.xml` in the WebAppContext:

    ```
    <Call name="setAttribute">
        <Arg>org.eclipse.jetty.cookie.sameSiteDefault</Arg>
        <Arg>None</Arg>
    </Call>
    ```

  * If you want to specify a default value for session management cookies, such as JSESSIONID, in servlets hosted in PingFederate, add a `<comment>` like the one in the following snippet to the existing `session-config` in the `web.xml` file:

    ```
    <session-config>
        <session-timeout>30</session-timeout>
            <cookie-config>
                <http-only>true</http-only>
                <!--
                    The following comment adds a default SameSite value to the JSESSIONID cookie in any servlet context.
                    Available options are:
                        SAME_SITE_NONE
                        SAME_SITE_LAX
                        SAME_SITE_STRICT
                -->
             <comment>SAME_SITE_NONE</comment>
        </cookie-config>
    </session-config>
    ```

* Microsoft Internet Explorer 11

  Ping Identity commits to deliver the best experience for administrators and users. As we continue to improve our products, we encourage our customers to migrate off of Microsoft Internet Explorer 11. We intend to remove Internet Explorer 11 from our qualification process in December 2021.

* Microsoft Windows Server 2012 R2 and Active Directory 2012

  Because Microsoft will end extended support for Windows Server 2012 R2 in late 2023, you should upgrade your Windows servers and Active Directory to a later version, such as Windows Server 2019. For a full list, see [System requirements](../installing_and_uninstalling_pingfederate/pf_system_requirements.html). We intend to remove Windows Server 2012 R2 and Active Directory 2012 from our qualification process in July 2023.

* Authorization endpoint

  Before version 10.2, PingFederate did not validate the `NumericDate` value of `exp` claims in a signed request object's JWT. To ensure the JWT does not expire too far in the future, PingFederate 10.2 and later do validate the value. PingFederate rejects any JWT that expires more than 720 minutes later. You can change that default value in `<pf_install>/pingfederate/server/default/data/config-store/jwt-request-object-options.xml`.

|   |                                                                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingFederate interprets the `NumericDate` value as seconds, not milliseconds. So PingFederate 10.2 will reject a JWT that has the `NumericDate` value based on milliseconds, because PingFederate calculates the JWT to live more than 720 minutes. |

* Configuration change necessary for MFA adapters

  As of PingFederate 10.2, when you define policies using multi-factor authentication (MFA) adapters, you must select the **User ID Authenticated** checkbox in the **Incoming User ID** popup to allow users to register as a new MFA user. You should only select this checkbox if the previous authentication source has verified the **Incoming User ID**. You should not select the checkbox if the MFA adapter is part of a policy used for password reset or password change. For more information, see [Defining authentication policies](../administrators_reference_guide/pf_defining_auth_policies.html).

|   |                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Administrators using the PingID adapter must review existing policies and select this checkbox if appropriate. Otherwise, the adapter will prevent new user registration. |

* Expression Admin role

  When upgrading to PingFederate 10.1 or later from an earlier version, administrative users who were granted the Admin role in the earlier installation are granted the Expression Admin role automatically. You can achieve the same result by using the `/bulk/import` administrative API endpoint to bulk-import a configuration that was bulk-exported from PingFederate 10.0.Additionally, all four administrative roles, namely User Admin, Admin, Expression Admin, and Crypto Admin, are required to access and make changes through the following services:

  * The `/bulk`, `/configArchive`, and `/configStore` administrative API endpoints

  * The **System > Server > Configuration Archive** window in the administrative console

  * The **Connection Management** configuration item on the **Security > System Integration > Service Authentication** window

* Authentication session created after user registration

  As of PingFederate 10.1, an authentication session is automatically created for a user after registration, preventing the user from having to log in again during the next SSO transaction. This feature is enabled by default for all new and existing local identity profiles. However, if needed, you can disable it through the `/localIdentity/identityProfiles` administrative API endpoint by setting the `createAuthnSessionAfterRegistration` attribute to `false`.

* Template `html.form.login.template.html`

  Starting with PingFederate 10.0, the `html.form.login.template.html` template no longer includes the *$forgotPasswordUrl* variable.

---

---
title: Upgrade considerations introduced in PingFederate 11.x
description: The following modifications since PingFederate 11.0 might affect existing deployments.
component: pingfederate
version: 13.1
page_id: pingfederate:upgrading_pingfederate:pf_upgrade_considerations_11x
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/upgrading_pingfederate/pf_upgrade_considerations_11x.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 16, 2025
---

# Upgrade considerations introduced in PingFederate 11.x

The following modifications since PingFederate 11.0 might affect existing deployments.

* Apache Velocity Engine upgrade

  With PingFederate 11.3, we've upgraded the Apache Velocity templating engine from version 1.6 to version 2.3. All out-of-the-box PingFederate HTML templates are backward compatible with this new version of Velocity, but customized templates might require edits to work with version 2.3. For a complete list of changes to the Velocity engine that might require updating customized templates, see [Upgrading](https://velocity.apache.org/engine/2.3/upgrading.html) in the Apache Velocity Engine documentation.

* Replacement of `hivemodule.xml`

  Starting with PingFederate 11.3, the distribution ZIP file no longer contains the `hivemodule.xml` file. Instead, the distribution contains a new file: `service-points.conf` in the `<pf_install>/pingfederate/server/default/conf/` directory. On first startup, PingFederate processes `service-points.conf` and generates a default `hivemodule.xml`.

The advantage of the `service-points.conf` file is that it lets you use environment variables to override hivemodule settings without having to modify an XML file. For more information, see [Overriding configuration settings using environment variables](../administrators_reference_guide/override_configuration_settings_using_environment_variables.html).

When you upgrade a supported version of PingFederate older than 11.3 to version 11.3 or later, the `service-points.conf` file replaces the `hivemodule.xml` file in the `<pf_install>/pingfederate/server/default/conf/META-INF/` directory with a generated default `hivemodule.xml` file in `<pf_install>/pingfederate/server/default/conf/generated-hivemodule/META-INF/` directory.

If you want to continue using `hivemodule.xml` instead of `service-points.conf`, add `hivemodule.xml` to the directory `<pf_install>/pingfederate/server/default/conf/META-INF/` after upgrading PingFederate. During startup, if PingFederate finds `hivemodule.xml` in that directory, it will ignore `service-points.conf`. Later, when you upgrade PingFederate 11.3 or a newer version, the `hivemodule.xml` file won't be replaced.

These changes don't affect your upgrade process in either of the following cases:

* You upgrade to PingFederate 11.3 or later using the upgrade utility, as recommended

* You don't need to modify the default `hivemodule.xml` file

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you start a new instance of PingFederate 11.3 or later using a process that depends on having `hivemodule.xml` in the distribution ZIP file, the process will fail. To prevent this startup failure, do one of the following:* Launch a local instance of the new PingFederate version, which generates the default `hivemodule.xml` in `<pf_install>/pingfederate/server/default/conf/generated-hivemodule/META-INF/`. Copy and, if needed, modify `hivemodule.xml`. Use that file to launch your production PingFederate instance. When you launch PingFederate, your existing process can grab `hivemodule.xml` and work as expected.

* Disable your process that needs to work with `hivemodule.xml` directly. If needed, modify the `service-points.conf` file that comes with PingFederate 11.3 or later. When you launch PingFederate, it generates `hivemodule.xml` and works as expected.

* Disable your process that needs to work with `hivemodule.xml` directly. If needed, configure the PingFederate environment variables. When you launch PingFederate, it uses those environment variables and generates `hivemodule.xml`. |

* Configuration change necessary for MFA adapters

  As of PingFederate 10.2, when you define policies using multi-factor authentication (MFA) adapters, you must select the **User ID Authenticated** checkbox in the **Incoming User ID** popup to allow users to register as a new MFA user. You should only select this checkbox if the previous authentication source has verified the **Incoming User ID**. You should not select the checkbox if the MFA adapter is part of a policy used for password reset or password change. For more information, see [Defining authentication policies](../administrators_reference_guide/pf_defining_auth_policies.html).

|   |                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Administrators using the PingID adapter must review existing policies and select this checkbox if appropriate. Otherwise, the adapter will prevent new user registration. |

* LDAP properties

  Starting with PingFederate 11.3, the `<pf_install>/pingfederate/bin/ldap.properties` file includes the new `ldap.type` field. This mandatory field specifies the LDAP directory server type. If you use [LDAP for administrative console or administrative API authentication](../administrators_reference_guide/pf_enabling_ldap_auth.html), ensure you set this field to a valid value.

* Refresh token rolling grace period

  When upgrading from PingFederate versions later than 11.0.1, if the **Authorization Server Settings** window was never modified, a default value of 0 shall be set for **Refresh Token Rolling Grace Period**. If the **Authorization Server Settings** window was modified, the previously set value shall be retained. For more information, see the Refresh Token Rolling Grace period field in [Configuring authorization server settings](../administrators_reference_guide/help_authorizationserversettingstasklet_oauthauthorizationserversettingsstate.html).

* Metadata response configuration

  Starting with PingFederate 11.2, PingFederate provides an OAuth authorization server metadata endpoint, `/.well-known/oauth-authorization-server`. The new endpoint returns configuration information that OAuth clients need to interface with PingFederate using the OAuth 2.0 protocol. You can customize what information the endpoint returns by editing the `<pf_install>/pingfederate/server/default/conf/openid-configuration.template.json` template file, which also determines what information the OpenID Connect metadata endpoint returns.

  If you previously modified `openid-configuration.template.json` for the OpenID Connect metadata endpoint, merge your modifications into the 11.2 version of the template.

* Processing policy fragments

  Starting with PingFederate 11.2, PingFederate processes policy fragments independently from policies and other fragments. The nodes in a fragment are no longer aware of the exterior policy or fragment invoking it, other than the fragment input values that the input authentication policy contract provides. The inverse is also true. The exterior policy or fragment is no longer aware of the processing that occurred within an interior fragment, only what is mapped to the output authentication policy contract.

* Integration with Amazon Web Services (AWS) CloudHSM

  Starting with PingFederate 11.2, PingFederate's integration with AWS CloudHSM now requires the AWS CloudHSM Java Cryptography Extension (JCE) provider for Client SDK 5. There are a number of new limitations around assertion and token decryption with Client SDK 5. For more information on limitations, see the Hardware security modules (HSM) issue section of the [Release Notes](../release_notes/pf_release_notes.html). In addition, the `java.security` file in the Java Runtime Environment (JRE) no longer needs to be modified and client files do not need to be copied to the `JAVA_HOME/jre/lib/ext` directory. For more information on how to upgrade the HSM client, see the updated setup instructions in [Integrating with AWS CloudHSM](../getting_started_with_pingfederate/pf_integra_aws_cloudhsm.html).

* Verbose logging

  Starting with PingFederate 11.2, you can enable verbose logging with the **Log Settings** window or with the administrative API on nodes that have the updated version of the `<pf_install>/pingfederate/server/default/conf/log4j2.xml` file. If `log4j2.xml` was previously modified, PingFederate will migrate the modified file on upgrade and create a backup of the latest file. To take advantage of the new verbose logging capability, you must merge your modifications into the latest version of `log4j2.xml`.

* Expired passwords and prompts to change passwords

  When using PingDirectory 8.2 or later as the credential store, if a user's password has expired, the following settings ensure PingFederate doesn't direct the user to the Change Password form when they enter an invalid password:

  * Set the **return-password-expiration-controls** setting in the PingDirectory password policy to **always**.

  * Starting with PingFederate 11.1, when configuring an LDAP Username Password Credential Validator, select the **Expect Password Expired Control** checkbox in the advanced fields section of the **Instance Configuration** tab of the **Create Credential Validator Instance** window.

* Device authorization flows using the authentication API

  Starting with PingFederate 11.1, the user code verification steps of the device authorization flow are API-enabled. Existing API applications will need to be updated to support the new API states. To disable the use of the API for the new states, set `enable-authn-api-for-user-code-validation` to `false` in `<pf_install>/pingfederate/server/default/config-store/oauth-device-flow.xml`. This will cause PingFederate to continue to render these states itself using the Velocity templates.

* Java 17

  Starting with PingFederate 11.1, when using Java 17, the following JDKs are supported:

  * Adoptium OpenJDK

  * Oracle JDK

  * Amazon Correto

If you upgrade to Java version 17 after you upgrade PingFederate:

* Remove `-XX:-UseParallelOldGC` from the `jvm-memory.options` file.

* Reinstall the Windows Service.

  * Certificate revocation checking

    Starting with PingFederate 11.1, when configured for certificate revocation list (CRL) or online certificate status protocol (OCSP) revocation checking, PingFederate now performs these checks in a broader range of flows. In particular, outbound TLS calls to retrieve JSON web key sets (JWKS) now perform revocation checks. Also, outbound TLS calls performed by plugins, such as adapters, now perform revocation checks. To revert to the previous behavior where PingFederate doesn't perform these new checks, set `pf.tls.installRevocationCheckerGlobally` to `false` in the `run.properties` file.

|   |                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | CRL-based revocation checks can consume large amounts of memory. If CRL checking is enabled, you should set PingFederate's maximum heap in the `jvm-memory.options` file to at least 4 GB. Alternatively, consider switching to OCSP revocation checking, which demands fewer resources. |

When configured for CRL or OCSP revocation checking, PingFederate's validation of CRLs and OCSP responses is tighter than before. The following settings in the `revocation-checking-config.xml` file control the new validation checks:

* `crl-issuer-allow-any-trust-anchor`

* `crl-verify-issuing-distribution-point`

* `OCSP-enforce-responder-key-usage-check`

Although you should leave the new validation checks enabled, you can disable them for compatibility with existing deployments.

* Custom `MasterKeyEncryptor` implementations

  Starting with PingFederate 11.1, due to the revocation checking enhancements outlined above, a circular initialization dependency can arise if revocation checking is enabled and a custom `MasterKeyEncryptor` implementation makes API calls to an external service. To avoid this risk, you should disable revocation checking for any API calls made by the master key encryptor. Refer to the SDK documentation for more information on how to disable revocation checking in custom `MasterKeyEncryptor` implementations.

* `run.sh` and `run.bat` files

  In PingFederate 11.1, the `run.sh` and `run.bat` files were updated.

  * A `startup` directory was added under the PingFederate installation. Its contents are now added to the classpath using a wildcard.

  * References to `jetty-start.jar` were updated in `run.sh` and `run.bat` because `jetty-start.jar` was moved from the `bin` directory to the `startup` directory.

  * References to `run.jar` were removed from `run.sh` and `run.bat` because `run.jar` was removed from the `bin` directory.

If your `run.sh` or `run.bat` files were customized, you must update your copy of these files accordingly.

* Template `username.recovery.template.html`

  Starting with PingFederate 11.1, the `username.recovery.template.html` template no longer includes the *$forgotPasswordUrl* variable.

|   |                                                                     |
| - | ------------------------------------------------------------------- |
|   | The top of the template file documents which variables you can use. |

* Dynamic discovery settings

  In versions preceding PingFederate 11.0, administrators could only define dynamic discovery settings to discover cluster membership in the `server/default/conf/tcp.xml` file. Now PingFederate provides a new configuration file for these settings, `bin/jgroups.properties`. This new approach streamlines future upgrade experiences. For new installations, we recommend defining dynamic discovery settings in the `jgroups.properties` file. While upgraded environments will continue to look for dynamic discovery settings from the `tcp.xml` file, we recommend performing a one-time migration to ease the upgrade experiences in the future. For more information, see [Migrating cluster discovery settings](../server_clustering_guide/pf_migrate_cluster_discovery_settings.html).

* Velocity HTML templates

  Starting with PingFederate 11.0, if any of the default Velocity HTML templates for user-facing windows were modified, the Upgrade Utility migrates them to the new installation and renames the corresponding default templates in the new installation with the following format: `<template_name>-default-<PF-version>.<ext>`. For more information, see [User-facing windows](pf_copying_custom_files_settings.html#_user_facing_windows).

* Kerberos authentication

  Starting with PingFederate 11.0, when the new **Retain Previous Keys on Password Change** checkbox on the **Manage Domain/Realm** window is selected, PingFederate saves the encryption keys associated with the password of the current Kerberos service account. The checkbox is selected by default.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | PingFederate will not save the encryption keys until you re-save the configuration of the domain or realm. To facilitate seamless rotation of the service account password for existing domains, click **Save** on the **Manage Domain/Realm** window before you update the password in the domain controller. For more information, see [Adding Active Directory domains and Kerberos realms](../administrators_reference_guide/pf_adding_active_directory_domains_kerberos_realms.html). |

* IWA IdP adapter

  PingFederate 11.0 and later no longer support the integrated Windows authentication (IWA) IdP adapter. The IWA integration kit for Kerberos has been replaced with a PingFederate adapter for Kerberos. See [Migrating from the Integrated Windows Authentication Integration Kit to the PingFederate Kerberos adapter](https://support.pingidentity.com/s/article/Migrating-from-the-Integrated-Windows-Authentication-integration-kit-to-the-PingFederate-Kerberos-adapter).

* Private key JSON web token authentication

  When authenticating an OAuth client that uses the private key JSON web token (JWT) authentication scheme, PingFederate now validates that the issuer and subject claims in the JWT have the same value.The following administrative API endpoint exposes the validation on/off switch:

```
https://{{pf_base_host_port}}/pf-admin-api/v1/configStore/oauth-credentials-validator/issuerMustBeEqualToClientId
```

To disable validation, send an HTTP POST request with the following body to the endpoint:

```json
{
  "id": "issuerMustBeEqualToClientId",
  "stringValue": "false",
  "type":"STRING"
}
```

* Authentication API applications

  Starting with PingFederate 11.0, the new **Restrict Access to Redirectless Mode** checkbox on the **Authentication API Applications** window lets you restrict which authentication API applications can use redirectless mode. To avoid impacting existing deployments, this checkbox is not selected on upgrade. However, you should enable this setting. For more information, see [Managing authentication applications](../administrators_reference_guide/help_authenticationapplicationstasklet_authenticationapplicationsstate.html).

* Jetty agent

  Starting with PingFederate 11.0, if your PingFederate server is running on a Java version prior to 8u252, you must modify your `run.sh`, `run.bat`, or `PingFederateService.conf` script to include the new Jetty agent in PingFederate.

Add the following Java argument to the script:

```
-javaagent:/server/default/lib/jetty-alpn-agent.jar
```

Example for `run.sh`:

```
"$JAVA" $JAVA_OPTS \
$ERROR_FILE \
$HEAP_DUMP \
${GC_FILE:+$GC_FLAG"$GC_FILE"$GC_OPTIONS} \
$ENDORSED_DIRS_FLAG \
 -javaagent:$PF_HOME/server/default/lib/jetty-alpn-agent.jar  \
-Dlog4j2.AsyncQueueFullPolicy=Discard \
```

Example for `run.bat`:

```
"%JAVA%" %PF_JAVA_OPTS% %JAVA_OPTS% %GC_OPTION%  -javaagent:%PF_HOME%/server/default/lib/jetty-alpn-agent.jar  -Dlog4j2.AsyncQueueFullPolicy=Discard
```

Example for `PingFederateService.conf` (note the extra `../` because this is located in `pingfederate/sbin/wrapper`):

```
# Java Additional Parameters
wrapper.java.additional.1=-Dlog4j.configurationFile=../../server/default/conf/log4j2.xml

...... (omitted lines 2-13 to save space) ......

wrapper.java.additional.14=-javaagent:../../server/default/lib/jetty-alpn-agent.jar
```

* Specifying a maximum size for inbound runtime requests

  Starting with PingFederate 11.0, if you have previously specified a value for `maxFormContextSize` in `jetty-runtime.xml`, you should now use `pf.runtime.http.maxRequestBodySize` in the `run.properties` file to control the maximum size for inbound runtime requests. For more information, see [Configuring PingFederate properties](../administrators_reference_guide/pf_config_pf_propert.html).

* Java 8

  As we continue to improve our products and hardware security module (HSM) integrations, you should migrate off of Java 8. We intend to remove Java 8 support from our qualification process in May 2023. For more information, including Java 11 support, see [System requirements](../installing_and_uninstalling_pingfederate/pf_system_requirements.html).

* Third-party integrations

  As we continue to improve PingFederate, we intend to remove the following product releases from our qualification process after the release of PingFederate 11.3 in June 2023:

  * Oracle Linux 7.9 (Red Hat-compatible Kernel)

  * Red Hat Enterprise Linux 7.9

  * Microsoft SQL Server 2016 SP2

  * Oracle Database 12c Release 2

  * Microsoft Windows Server 2012 R2

  * Microsoft Active Directory 2012 R2

We encourage you to upgrade these products to more recent versions, such as:

* Oracle Linux 8.5 (Red Hat-compatible Kernel)

* Red Hat Enterprise Linux 8.5

* Microsoft SQL Server 2017

* Oracle Database 19c

* Microsoft Windows Server 2016

* Microsoft Active Directory 2016

For a more complete list of qualified third-party solutions, see [System requirements](../installing_and_uninstalling_pingfederate/pf_system_requirements.html).

---

---
title: Upgrade considerations introduced in PingFederate 12.x
description: The following modifications since PingFederate 12.0 might affect existing deployments.
component: pingfederate
version: 13.1
page_id: pingfederate:upgrading_pingfederate:pf_upgrade_considerations_12x
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/upgrading_pingfederate/pf_upgrade_considerations_12x.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 10, 2024
---

# Upgrade considerations introduced in PingFederate 12.x

The following modifications since PingFederate 12.0 might affect existing deployments.

* OAuth **Resource URIs** must be defined

  Starting with PingFederate 12.1, reusing a previous version's OAuth authentication calls that contain **Resource URIs** will fail if the required **Resource URIs** aren't defined in the **Access Token Manager**. Learn more in [Managing resource URIs](../administrators_reference_guide/help_beareraccesstokenmgmtplugintasklet_atmselectionsettingsstate.html).

* `pf.admin.baseurl` must be set

  A defect fix requires the `pf.admin.baseurl` property to be explicitly set in `run.properties`. This prevents admin console URL redirects from failing when PingFederate is accessed through a load balancer with a port that differs from `pf.admin.https.port`.

* Refresh token MySQL deadlocks

  We've fixed a defect that caused multiple refresh token requests in short succession to result in Java database connectivity (JDBC) *(tooltip: \<div class="paragraph">
  \<p>A Java API that allows Java programs to interact with databases.\</p>
  \</div>)* data source deadlocks and duplicated data entry into the database. The fix can cause significant performance issues if PingFederate or the JDBC data source have insufficient resources.

* HTTP request logging

  Starting with PingFederate 12.3, HTTP requests to the runtime engine and admin console are no longer logged to `request.log` and `request2.log` files.

  HTTP requests are now logged to the `runtime-request.log` and `admin-request.log` files. Like other PingFederate log files, you can configure the output to these files using the `log4j2.xml` and `run.properties` files.

  You can revert to the legacy logging behavior using `useLog4j2Logger` and `format` strings.

  Learn more in [HTTP request logging](../administrators_reference_guide/pf_http_request_loggin.html).

* Resource indicators for OAuth 2.0

  Starting with PingFederate 12.1, we've added support for the `resource` parameter to allow clients to indicate the protected resources to which the client is requesting access.

  If the incoming authorization or token request includes `resource` parameter(s), then you must add the resource(s) to the Resource URIs within an Access Token Manager. Otherwise, the authorization or token request will result in an error.

  Learn more in [Managing resource URIs](../administrators_reference_guide/help_beareraccesstokenmgmtplugintasklet_atmselectionsettingsstate.html).

* Persist users consent decision when revoking `refresh_token`

  Starting with PingFederate 12.0, you can configure your authorization server settings for OAuth and OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
  \<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
  \</div>)* users so that their decisions to grant access can be persisted after a `refresh_token` is revoked.

  If you have a custom implementation of the `AccessGrantManager` interface, you need to add the new methods:

  * Required: `void updateExpiry(AccessGrant accessGrant)`

  * Optional:

    ```
    Collection<AccessGrant>
    getByUserKeyClientIdGrantType(String userKey, String clientId, String grantType)
    ```

    |   |                                                                                                                                                                          |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    |   | If you don't implement these changes, PingFederate will use existing methods in the `AccessGrantManager` interface to perform the same lookup with additional filtering. |

    When you enable this feature, PingFederate creates more records in the external datastore used for Access Grants. It will not necessarily generate more data because OAuth consent records don't retain the same information as access grants.

    |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
    | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | You must manually add the newly-added index to your existing Access Grant external datastore.- JDBC (for all supported JDBC types)

      Create a new index `UNIQUEUSERIDCLIENTIDGRANTTYPEIDX`.

      You can find the create index command in the table-setup scripts for your database server provided in the `<pf_install>/pingfederate/server/default/conf/access-grant/sql-scripts` directory.

    - LDAP

      For PingDirectory, create a new index `accessGrantGrantType` and rebuild your index. |

* Alert and report when approaching `maxThreads`

  Starting with PingFederate 12.0, you can configure your runtime notifications to alert you when the number of threads in use exceeds a set threshold. You can also use this feature to initiate and log a thread dump event that you can use for troubleshooting.

  If you're using a customized log4j.xml file, add the following to your list of Appenders:

  ```
  <!-- Thread Pool Exhaustion thread dump log : A size based file rolling appender -->
  <RollingFile name="ThreadDumpAppender"
               fileName="${sys:pf.log.dir}/thread-pool-exhaustion-dump.log"
               filePattern="${sys:pf.log.dir}/thread-pool-exhaustion-dump.log.%i"
               ignoreExceptions="false">
      <PatternLayout>
          <!-- Uncomment this if you want to use UTF-8 encoding instead
              of system's default encoding.
          <charset>UTF-8</charset> -->
          <pattern>%d %m%n</pattern>
      </PatternLayout>
      <Policies>
        <SizeBasedTriggeringPolicy
                  size="10000 KB" />
      </Policies>
      <DefaultRolloverStrategy max="5" />
  </RollingFile>
  ```

  Also add the following to your list of Loggers:

  ```
  <AsyncLogger name="ThreadDumpLogger" level="INFO" additivity="false" includeLocation="false">
      <appender-ref ref="ThreadDumpAppender" />
  </AsyncLogger>
  ```

* PingID properties file encrypted

  From RADIUS PCV 3.0.4 and later, the PingID properties file is encrypted after it is uploaded to PingFederate.

  |   |                                                                                                                                                                    |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | If you are upgrading from an earlier version, to ensure the properties file is encrypted, you need to upload it to the PingID RADIUS PCV instance in PingFederate. |

* Skip redirect to authentication application if no action is required

  Starting with PingFederate 12.0, API-capable IdP adapters can now prevent a redirect to the authentication application if no user interaction is required.

  If the adapter determines that no authentication action is required—for example when a request parameter is being passed, or because the adapter maintains a valid session—PingFederate will skip the redirect to the authentication application.

  This capability is implemented in the [HTML Form Adapter](../administrators_reference_guide/pf_html_form_adapt.html) and the [Identifier First Adapter](../administrators_reference_guide/pf_identifier_first_adapter.html), and is also available for custom adapters using the `TRY_LOOKUP_AUTHN` metadata key and input parameter.

* Prevent JGroups thread pool exhaustion in large clusters

  Starting with PingFederate 12.0 the default value of *pf.cluster.TCPPING.return\_entire\_cache* in `jgroups.properties` to `false` on fresh installations of PingFederate.

  Setting *pf.cluster.TCPPING.return\_entire\_cache* to `false` avoids an issue where the thread pool for cluster RPCs temporarily runs out of threads and some RPCs get dropped. This issue only occurs in large clusters under heavy load.

  Setting *pf.cluster.TCPPING.return\_entire\_cache* means that all clusters must be listed in *pf.cluster.tcp.discovery.initial.hosts*.

  On upgrade, the existing value of *pf.cluster.TCPPING.return\_entire\_cache* is preserved, but customers using `TCPPING` with large clusters should set it to `false`, provided that all cluster members are listed in *pf.cluster.tcp.discovery.initial.hosts*.

* Removed support for Java 8

  Starting with version 12.0, PingFederate no longer supports Java 8. Use Java 11, Java 17, or Java 21 instead.

  Learn more in [Java environment](../installing_and_uninstalling_pingfederate/pf_system_requirements.html#java_environment).

* Hostname characters

  If you're using PingFederate on Java 17 or 21, your hostname can't include underscores. Only ASCII letters, digits, and hyphens are permitted.

  Learn more in [RFC 3490](https://www.rfc-editor.org/rfc/rfc3490.html).

* Categories for verbose log settings

  Starting with PingFederate 12.0, some information has been moved from the **Core** log category to the new **Protocol Requests and Responses** log category. Learn more in [Log settings](../administrators_reference_guide/help_logsettingstasklet_logsettingsstate.html).

* Properties in `start.ini` moved to `run.properties`

  Starting with PingFederate 12.0, the properties previously in the `start.ini` file are now in the `run.properties` file to facilitate future upgrade of those properties.

* Default port range in `tcp.xml`

  Starting with PingFederate 12.0, the default port range in the `tcp.xml` file has been changed from `10` to `0`.

  As a result, PingFederate will only listen on the configured `pf.cluster.bind.port` and will fail to start up if that port is in use.

* OpenID Connect Front-Channel Logout

  Starting with version 12.0, PingFederate supports OpenID Connect Front-Channel Logout. For this feature to work correctly, if the value for the `exclude-patterns` item in the `X-Frame-Options` map in `<pf_install>/pingfederate/server/default/data/config-store/response-header-runtime-config.xml` has been edited, then you must add `/fc-logout.openid;/resume/sp/fc-logout.ping` to the `exclude-patterns` item.

* SAML IdP Discovery and SAML AP Affiliations

  As of PingFederate 12.0, the SAML IdP Discovery and SAML AP Affiliations features have been deprecated, and will be removed in a future release.

* Text Message SSPR

  Starting with PingFederate 12.0, text message self-service password reset (SSPR) has been removed.

* SAML SP connection configuration

  Existing SAML SP connections that rely on multiple session states in a single transaction will be affected by new session state validation measures introduced in PingFederate 11.2.5 and 11.3 under PF-33168. Learn more in [PingFederate 11.3 (June 2023)](../release_notes/pf_release_notes_113.html).

  You can find more information about how to diagnose and resolve issues caused by this update in [Solicited SAML Response Validation](https://support.pingidentity.com/s/article/Solicited-SAML-Response-Validation) in the Ping Identity Support Portal.

* Upgrade from PingFederate 6.x and 7.x

  Starting with version 12.0, PingFederate no longer supports upgrading from PingFederate 6.x or 7.x.

---

---
title: Upgrade considerations introduced in PingFederate 9.x
description: When integrating with Gemalto SafeNet Luna Network HSM 6 (hardware security module), PingFederate 9.2 requires firmware version of 6.3.0 and client driver version of 6.3. See Integrating with Thales Luna Network HSM for setup information.
component: pingfederate
version: 13.1
page_id: pingfederate:upgrading_pingfederate:pf_upgrade_considerations_introduced_pf_9x
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/upgrading_pingfederate/pf_upgrade_considerations_introduced_pf_9x.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
---

# Upgrade considerations introduced in PingFederate 9.x

* Gemalto SafeNet Luna HSM 6.3

  When integrating with Gemalto SafeNet Luna Network HSM 6 (hardware security module), PingFederate 9.2 requires firmware version of 6.3.0 and client driver version of 6.3. See [Integrating with Thales Luna Network HSM](../getting_started_with_pingfederate/pf_integrating_thales_luna_network_hsm.html) for setup information.

* Weaker cipher suites disabled

  Starting with PingFederate 9.1, weaker cipher suites TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA and TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA are disabled in new installations and upgrades. As a result, the administrative and runtime servers support only TLS 1.2. If you must re-enable these cipher suites for legacy clients, refer to [Managing cipher suites](../administrators_reference_guide/pf_managing_cipher_suites.html) for more information.

* LDAP service accounts on PingDirectory

  If PingFederate 9.3.1 or newer has an LDAP connection with PingDirectory, then add the config-read privilege to its service account in PingDirectory. Otherwise, users will not receive password expiry notifications. Learn more in [Working with privileges](https://docs.pingidentity.com/pingdirectory/latest/managing_access_control/pd_ds_work_with_privileges.html) in the PingDirectory documentation.

* Improved validation for `AudienceRestriction`

  If an IdP connection is configured with multiple virtual server IDs, the `AudienceRestriction` value in a SAML response must now match the virtual server ID information embedded in the protocol endpoint at which PingFederate receives the message. Otherwise the SSO attempt fails. To override this validation on a per-connection basis, see [Configuring validation for the AudienceRestriction element](../administrators_reference_guide/pf_config_validat_for_audiencerestric_element.html).

* Custom authentication selector

  If you have created a custom authentication selector that returns an IdP adapter instance ID or the connection ID of an IdP connection, you must update the associated descriptor instance. Learn more in [Updating the custom authentication selector](pf_migrate_other_componen.html#_updating_the_custom_authentication_selector).

* Provisioning datastore reset

  Upgrading to PingFederate 9.0 or 9.0.1 when using its outbound provisioning capability can result in user records being disabled at SaaS applications. The issue is resolved in version 9.0.2.

If you are upgrading from version 8.4.4 (or earlier) or from version 9.0.2, 9.0.3, and 9.0.4 to version 10.0, the upgrade process automatically resolves this issue. No further action is required.

If you are upgrading from version 9.0 or 9.0.1 to PingFederate 10.0, you must use the `provmgr` command-line tool to reset the provisioning datastore on the upgraded installation. See [Reviewing database changes](pf_review_database_change.html) for more information.

* Security enhancement in JDBC datastore queries

  A security enhancement was made in PingFederate 9.0 to safeguard JDBC datastore queries against back-end SQL injection attacks. This protection is enabled for all new installations. For upgrades, see [Reviewing database changes](pf_review_database_change.html).

* Access token validation response

  Starting with PingFederate 9.2, the access token validation response no longer includes the username and subject elements by default. Responses include them only if they were mapped in the issuing access token management instance.

---

---
title: Upgrade FAQ
description: The following links contain helpful resources to plan your PingFederate upgrade:
component: pingfederate
version: 13.1
page_id: pingfederate:upgrading_pingfederate:pf_upgrade_faq
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/upgrading_pingfederate/pf_upgrade_faq.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  planning-your-upgrade: Planning your upgrade
  downloads: Downloads
  performing-the-upgrade: Performing the upgrade
  licensing: Licensing
  general: General
  issues-and-rolling-back: Issues and Rolling Back
---

# Upgrade FAQ

## Planning your upgrade

* I want to upgrade PingFederate. What resources can help with this?

  The following links contain helpful resources to plan your PingFederate upgrade:

  |   |                                                                                                                            |
  | - | -------------------------------------------------------------------------------------------------------------------------- |
  |   | Use the version selector on the upper left of the page to select the documentation for the target version of PingFederate. |

  * [Release Notes](../release_notes/pf_release_notes.html) for the target version and any versions between your current version and the target

  * [Upgrade guide](pf_upgrade_pf.html) for the target version

  * [Upgrade considerations introduced in PingFederate 12.x](pf_upgrade_considerations_12x.html) for the target version and any major releases between your current version and the target

  * [Post-upgrade tasks](pf_post_upgrade_tasks.html)

  * [Upgrading PingFederate in a DevOps environment](https://developer.pingidentity.com/devops/how-to/upgradePingfederate.html), if you have PingFederate deployed in a DevOps environment

  * [Updating to the latest maintenance release](pf_updating_latest_maintenance_release.html) if you're performing an in-place maintenance upgrade

* I'm upgrading from a legacy version of PingFederate, how do I start?

  If you're running PingFederate 8.4 or older, you should upgrade to version 8.4 first. After you've upgraded and tested your 8.4 deployment, you can upgrade to a later version.

  |   |                                                                                                                             |
  | - | --------------------------------------------------------------------------------------------------------------------------- |
  |   | PingFederate versions 7.x and earlier can't upgrade directly to PingFederate 12.x. You must perform an incremental upgrade. |

* How can I upgrade PingFederate with the least amount of downtime?

  PingFederate doesn't support a fully zero downtime upgrade, but you can perform a [near-zero downtime upgrade](https://docs.pingidentity.com/solution-guides/getting_started_guides/how_to_guides_near_zero_downtime.html).

## Downloads

* I want to upgrade to a specific release that's no longer available on the [Ping Identity downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate/previous-releases.html). How can I download the version I need?

  Submit a support case to request the release you need, and we'll provide you with a link.

* Do I need to download the Upgrade Utility separately?

  All supported releases include the Upgrade Utility in the PingFederate package, so there's no need to download it separately.

  |   |                                                                                                                                                                                                                                                |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Releases prior to 10.x don't include the Upgrade Utility, so you must download that separately.For example, if you want to upgrade to 8.4, you need to download the PingFederate 8.4 package and the PingFederate 8.4 Upgrade Utility package. |

## Performing the upgrade

* How do I perform a major version or minor version upgrade?

  You can upgrade to the next major or minor version using the PingFederate Upgrade Utility or the Windows installer. The Upgrade Utility is generally the preferred method.

* How do I perform a maintenance release upgrade?

  If you're upgrading to a maintenance release for PingFederate 10.x or later, you can upgrade by deploying the in-place maintenance update package. You can also use the PingFederate Upgrade Utility or the Windows installer.

* Can I use the Windows MSI Installer to upgrade?

  Yes, but only if PingFederate was intially installed using this method. If it wasn't, or if you're unsure how PingFederate was installed, use Upgrade Utility.

* Do I have to use the Upgrade Utility to upgrade to major or minor releases in a DevOps environment?

  Yes. In a DevOps environment, you must always use the Upgrade Utility. Learn more in the [DevOps upgrade guide](https://developer.pingidentity.com/devops/how-to/upgradePingfederate.html).

* Can I use a configuration archive or bulk import from a previous release into a newer release?

  **PingFederate 12.1 and earlier:** No. The Upgrade Utility or Windows installer are the only supported upgrade methods for major or minor releases. The Upgrade Utility is generally the preferred method.

**PingFederate 12.2 and later:** A configuration archive from version 11.1 or later will be upgraded automatically when imported. Importing an archive from a version earlier than 11.1 won't be upgraded or supported.

|   |                                                                                                                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This method only imports data stored in the configuration archive, which excludes things like templates, `.properties`, or `.conf` file settings, and other settings that the Upgrade Utility would migrate. As such, we recommend this method only for environments with appropriate automation to merge these configurations post-upgrade. |

Learn more in [Upgrading configuration data](pf_upgrading_config_data.html).

* Do I need to start my upgrade with the Admin Console?

  Yes. The Admin Console is the only interface that inherits the configuration during the upgrade (such as adapter, connections, and datastores). Failing to upgrade and start the Admin Console and perform [cluster replication](../administrators_reference_guide/pf_replicat_config.html) results in upgraded engine nodes missing key configuration changes needed to process transactions.

## Licensing

* Do I need to upgrade my license when performing an upgrade?

  Yes, if you're upgrading to a new major release. You can upgrade your license by following [this guide](https://support.pingidentity.com/s/article/How-to-upgrade-a-PingFederate-License-key-using-the-Customer-Portal).

* Does upgrading my license invalidate my existing license?

  No. Your existing license continues to be valid until the expiration date.

## General

* How do I know if the version I am running or upgrading to is supported?

  You can check the support status and end-of-life dates for PingFederate at the [End of Life tracker](https://support.pingidentity.com/s/article/How-to-upgrade-a-PingFederate-License-key-using-the-Customer-Portal).

  Learn more in Ping Identity's [End of Life Policy](https://www.pingidentity.com/en/legal/end-of-life-policy.html).

* Does PingFederate support a mixed-version cluster?

  You can mix maintenance releases on a cluster but not major and minor releases.

  * PingFederate servers running 12.1.2 and 12.1.4 can exist within the same cluster. This makes it easier to upgrade to a new maintenance release. We recommend upgrading your older versions rather than keeping the mixed-version cluster long term.

  * PingFederate servers running 12.1 and 12.2 won't communicate with each other.

  * PingFederate releases prior to 10.x don't support any form of mixed-version clustering.

* Do I need to update Java when I upgrade PingFederate?

  Possibly. Check the [system requirements](../installing_and_uninstalling_pingfederate/pf_system_requirements.html) for the target version to see whether your current JDK release is supported.

* Does a PingFederate upgrade also upgrade my Adapters and Integration Kits?

  By default, the Upgrade Utility migrates the existing Integration Kit versions from the source version. This is to maintain functionality. You can then upgrade to new Integration Kit versions after your PingFederate upgrade.

  You can use the `-c` custom mode when running the Upgrade Utility. This prompts the administrator to choose to use the existing or new version of the integration, assuming the target PingFederate package includes the newer version of that integration.

  Integration kits not included in the PingFederate package are always migrated from the source version.

* Will my upgrade affect my existing use cases and functionality?

  Possibly. Review the [Upgrade considerations introduced in PingFederate 12.x](pf_upgrade_considerations_12x.html) before upgrading, and perform the upgrade in a test environment so you can test your use cases before upgrading a production environment.

* What happens to state and Authentication Sessions when upgrading?

  When performing a major or minor version upgrade, state and sessions held in memory will be lost. Persistent Sessions are stored in an external database and will be available post-upgrade.

## Issues and Rolling Back

* After running the Upgrade Utility, when I start the Windows Service, the old PingFederate version starts up. Why?

  The Upgrade Utility doesn't upgrade the Windows Service.

  * You can uninstall the existing Windows Service and install the Windows Service for the new version.

  * Alternatively, you can install the new Windows Service with a unique name so that both services are available to start and stop as you need.

* How can I roll back a PingFederate upgrade?

  PingFederate upgrades using the Upgrade Utility are non-destructive, meaning the previous version remains intact alongside the newly upgraded release. As such, you can roll back the upgrade by stopping the new service and starting the old service.

* If I roll back my upgrade, do I have to rerun the Upgrade Utility when we are ready to retry the upgrade?

  If your environment has changed since the last upgrade, you should run the Upgrade Utility again to ensure these chages are carried over.

* How can I get help if I encounter issues with the new version post-upgrade?

  Submit a support case with a description of the problem, along with the `server.log` and `upgrade.log` files and any other relevant details.

  If this is a production environment and the issue is causing a significant impact, you should roll back the upgrade to restore functionality while the case is investigated.

* I attempted to upgrade using an unsupported method but encountered problems. What can I do?

  If you attempted to upgrade using an unsupported method, like importing a configuration archive from an older version into a new version or from an incompatible version into 12.2 or later, you should start by rolling back to the previous version and upgrade using the Upgrade Utility.

  Upgrading using unsupported methods frequently causes problems, which can be difficult to diagnose.

  Ping Support can't assist with problems caused by an unsupported upgrade process.

* After upgrading, I get a warning banner in the PingFederate Admin Console regarding the HyperSQL Database (HSQLDB). What's causing this?

  This banner is expected if you use the unsupported HSQLDB in your environment. Learn more in [Hypersonic database Usage with PingFederate](https://support.pingidentity.com/s/article/Hypersonic-Database-Usage-with-PingFederate).