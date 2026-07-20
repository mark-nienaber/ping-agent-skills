---
title: Configure secret stores after upgrade
description: Configure secret stores on all servers in your site after upgrading PingAM to ensure all cryptographic keys and credentials are available across instances
component: pingam
version: 8.1
page_id: pingam:upgrade:upgrade-create-secret-stores
canonical_url: https://docs.pingidentity.com/pingam/8.1/upgrade/upgrade-create-secret-stores.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Upgrade", "Security"]
page_aliases: ["upgrade-guide:upgrade-create-secret-stores.adoc"]
section_ids:
  upgrade-secret-stores: Redeploy secret stores to a site after upgrade
---

# Configure secret stores after upgrade

Secret stores are repositories of cryptographic keys, key pairs, and credentials.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * The upgrade process doesn't create all the demo key aliases created during a fresh install. This includes, for example, the aliases required for the [IoT service](../security/secret-mapping.html#iot-default-secret-IDs). If you want to use services that require these demo aliases, add the corresponding keys and mappings after you have upgraded.

* Although the configuration for secret stores is available to any upgraded server in the site, **the upgrade process only creates the relevant secret store files on the AM instance where you run the upgrade process**. |

Follow these steps to make the secret stores available to other servers in the site:

## Redeploy secret stores to a site after upgrade

You can reconfigure the secret stores and their mappings after upgrade. However, we recommend that you follow the steps in this procedure to ensure all secrets are available to all the instances in the site, and later on, you make additional changes to your environment.

The upgrade process creates several secret stores, globally and by realm, depending on the features configured in AM:

1. Go to Configuration > Secret Stores, and review the global secret stores created for your environment.

   * Make sure the keystores configured exist on the other servers within the site. You might need to copy the keystores across or make them available in some other way.

   * Make sure directories configured in file system secret stores and their content exist on the other servers within the site. You might need to copy the directories across or make them available in some other way.

2. Go to Realms > *realm name* > Secret Stores, and perform the same actions you took for the global secret stores.

   Realm-based secret stores are created for those features that support different keystore configurations by realm. For example, SAML 2.0, or the persistent cookie decision node.

   To find the realm-based secret stores, go to Realms > *realm name* > Secret Stores. The secrets themselves are stored in the `/path/to/am/security/secrets/realms/root/realm-name/secret-store-name` directory.

   Repeat this step for each of the realms you have configured.

3. Deploy the new AM `.war` file on the rest of the AM servers.

4. When the site is up, and before opening the service to end users, review the secret label mappings of the new secret stores and change them as required.

   For example, the upgrade process could have created secret stores for features you aren't using. These secret stores could have mappings to secrets that don't exist. It's advisable to remove unused secret mappings in production environments.

   Learn more about available secret labels in [Secret label default mappings](../security/secret-mapping.html#secret-label-mappings).

   > **Collapse: Reference: SAML 2.0 mappings after upgrade**
   >
   > AM is flexible regarding the configuration of secrets for SAML 2.0. Therefore, migrating the different combinations may create a high number of secret labels in your environment.
   >
   > As a rule of thumb, AM configures providers that were using the same key aliases *in the same order*, to use the same secret labels. If this rule can't be satisfied, the upgrade process creates new secret labels for the provider by assigning it a secret label identifier.

---

---
title: Configure the user profile allowlist
description: Configure PingIDM to allowlist user profile attributes in self-service flows
component: pingam
version: 8.1
page_id: pingam:upgrade:upgrade-profile-whitelist
canonical_url: https://docs.pingidentity.com/pingam/8.1/upgrade/upgrade-profile-whitelist.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Upgrade"]
page_aliases: ["upgrade-guide:upgrade-profile-whitelist.adoc"]
---

# Configure the user profile allowlist

The profile attribute allowlist controls the information returned to non-administrative users when they access `json/user` endpoints. For example, the allowlist controls the attributes shown in the user profile page.

Common profile attributes are allowlisted by default. You must add any custom attributes that you want non-administrative users to see.

The allowlist can be set globally, or per realm, in the user self-service service. To modify the list:

* **Globally**: Go to Configure > Global Services > User Self-Service > Profile Management, and edit the Self readable attributes field.

* **By realm**: Go to Realms > *realm name* > Services > User Self-Service > Profile Management, and edit the Self readable attributes field.

  You must add the user self-service service to the realm if you've not done so already but you don't need to configure anything other than the allowlist.

|   |                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------- |
|   | You must allowlist the `kbainfo` attribute for users to manage their KB questions and answers in user self-service flows. |

---

---
title: Migrate legacy instances
description: Migrate from legacy PingAM deployments by creating a new deployment and redirecting client traffic to replace your unsupported installation
component: pingam
version: 8.1
page_id: pingam:upgrade:upgrade-legacy
canonical_url: https://docs.pingidentity.com/pingam/8.1/upgrade/upgrade-legacy.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Upgrade"]
page_aliases: ["upgrade-guide:upgrade-legacy.adoc"]
section_ids:
  proc-upgrade-legacy: Upgrade a legacy deployment
---

# Migrate legacy instances

Rather than upgrade legacy instances (running an [AM version that's no longer supported](https://support.pingidentity.com/s/article/Ping-Identity-EOL-Tracker#pam)), you must instead manually migrate from your existing deployment to a new deployment.

For complex legacy deployments, Ping Identity can help you with the migration process.

## Upgrade a legacy deployment

1. Prepare your customized AM `.war` file.

2. Prepare a new deployment, installing servers from the new, customized `.war` file, starting with the instructions in [Install AM](../installation/installing-instances.html).

3. After installation, configure the new servers in the same way as the old servers, adapting as necessary.

4. Validate that the new service is performing as expected.

5. Redirect client application traffic from the old deployment to the new deployment.

---

---
title: Migrate to file-based configuration
description: Migrate your PingAM configuration from LDAP directories to file-based configuration after upgrading to PingAM 8.0
component: pingam
version: 8.1
page_id: pingam:upgrade:migrate-to-fbc
canonical_url: https://docs.pingidentity.com/pingam/8.1/upgrade/migrate-to-fbc.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Migrate", "FBC", "File-based configuration"]
page_aliases: ["upgrade-guide:migrate-to-fbc.adoc"]
section_ids:
  separate-config: Separate dynamic data from configuration data
  export-existing-config: Export existing configuration data
  migrate-config: Migrate exported configuration to FBC
  copy-fbc-to-am: Provide configuration files to AM
  start-am-fbc: Start AM in FBC mode
  migrate-fbc-troubleshooting: Troubleshoot your FBC migration
---

# Migrate to file-based configuration

Prior to AM 8.0, all information (configuration *and* data) was stored in LDAP directories. AM 8.1 can read its configuration from JSON files instead of directory servers.

File-based configuration (FBC) is best-suited to a DevOps-style deployment, with the associated tools and practices of that approach.

Static FBC data is written to configuration files in the file system and checked into a source control system, such as Git.

AM instances are created as Docker images, with the FBC incorporated into the image.

![Kubernetes deployment using file-based configuration.](../_images/docker-deployment.png)

You can insert variables into these configuration files before you check them into source control. The variables are substituted with the appropriate values at runtime when you start the Docker container. Using variables lets you reuse the same base configuration files for multiple instances, and different staging environments. For example, development, QA, or pre-production, which are then promoted to production.

In an existing deployment, you can migrate your configuration to FBC *after you've upgraded* the configuration to AM 8.1.

|   |                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Before you start, read [How AM reads FBC](../installation/fbc.html#how-am-reads-FBC) to understand the file-based configuration layers and their order of precedence. |

These topics assume you've already upgraded to AM 8.1 using the [upgrade wizard](upgrade-servers.html#upgrade-wizard). If you upgraded using, [amupgrade and Amster](upgrade-servers.html#upgrade-amupgrade), first deploy AM 8.1 and import the upgraded `amster` configuration. Then continue with the migration to FBC.

Migrating to FBC involves the following high-level steps:

1. [Separate dynamic data from configuration data](#separate-config)

2. [Export existing configuration data](#export-existing-config)

3. [Migrate exported configuration to FBC](#migrate-config)

4. [Provide configuration files to AM](#copy-fbc-to-am)

5. [Start AM in FBC mode](#start-am-fbc)

## Separate dynamic data from configuration data

Most deployments have one or more LDAP directories to store static configuration *and* data (identities, CTS tokens, policies, agents, and applications). If you store configuration and data in a single LDAP directory, you must separate the dynamic data first.

This section assumes you have stored identities in a separate datastore and focuses on CTS tokens, policies, agents, and applications. Export the data from your existing DS server and import it into one or more DS servers specifically for that data.

|   |                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You can use your existing directory to store your policies and applications, to avoid the overhead of setting up and managing additional DS instances during the migration. In this case, overwrite the contents of the directory with only the dynamic data. If you do use the existing instance, backup directory so that you can restore it if issues occur during the migration. |

To assist with the export, this table shows the default backend IDs and base DNs for AM data stored in DS directories. The table assumes you installed DS with the appropriate setup profiles. Adjust the values to reflect how you configured your DS server to store this data.

|   |                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | There is no DS setup profile for UMA-related data. This table therefore shows the values suggested in [Prepare external UMA datastores](../uma/prepare-uma-store.html). |

| Data type                         | Backend ID   | Base DN                                     |
| --------------------------------- | ------------ | ------------------------------------------- |
| CTS tokens                        | `amCts`      | `ou=famrecords,ou=openam-session,ou=tokens` |
| Policies, applications and agents | `cfgStore`   | `ou=services,ou=am-config`                  |
| UMA-related data                  | `umaRsStore` | `dc=uma-resources,dc=example,dc=com`        |

1. Set up at least one external PingDS instance for your exported data, following these instructions:

   * [Prepare policy and application stores](../setup/prepare-policy-and-application-store.html)

   * [Configure CTS token stores](../cts/cts-openam-config.html)

   * [Prepare external UMA datastores](../uma/prepare-uma-store.html)

2. Use the `export-ldif` command on your current DS server instance to export the policies, applications, agents, CTS tokens and any UMA-related data from your existing configuration store.

   * This command exports the CTS tokens to an LDIF file named `output-cts.ldif`:

     ```bash
     $ /path/to/opendj/bin/export-ldif \
       --hostname ds.example.com \
       --port 1636 \
       --useSsl \
       --usePkcs12TrustStore ~/path/to/opendj/config/keystore \
       --trustStorePassword:file ~/path/to/opendj/config/keystore.pin \
       --bindDn uid=admin \
       --bindPassword str0ngAdm1nPa55word \
       --backendId amCts \
       --ldifFile output-cts.ldif
     Export task ExportTask-16a9dce5-ceb1-41f0-a94d-154246ba7393 scheduled to start immediately
     …​
     Export task ExportTask-16a9dce5-ceb1-41f0-a94d-154246ba7393 has been successfully completed
     ```

   * This command exports UMA-related data to an LDIF file named `output-uma.ldif`:

     ```bash
     $ /path/to/opendj/bin/export-ldif \
       --hostname ds.example.com \
       --port 1636 \
       --useSsl \
       --usePkcs12TrustStore ~/path/to/opendj/config/keystore \
       --trustStorePassword:file ~/path/to/opendj/config/keystore.pin \
       --bindDn uid=admin \
       --bindPassword str0ngAdm1nPa55word \
       --backendId umaRsStore \
       --ldifFile output-uma.ldif
     Export task ExportTask-16a9dce5-ceb1-41f0-a94d-154246ba7393 scheduled to start immediately
     …​
     Export task ExportTask-16a9dce5-ceb1-41f0-a94d-154246ba7393 has been successfully completed
     ```

   * Follow the steps in [Migrate policy or application data to DS](../setup/prepare-policy-and-application-store.html#migrate-policy-and-application-data) to export the policy and application data.

   You can find more information about this command in [export-ldif](https://docs.pingidentity.com/pingds/8.1/tools-reference/export-ldif.html).

3. Import the dynamic data into the new DS server or servers you've installed for this purpose.

   * This command imports the CTS tokens into a DS server instance at `ds-cts.example.com`:

     ```bash
     $ /path/to/opendj/bin/import-ldif \
       --hostname ds-cts.example.com \
       --port 1636 \
       --useSsl \
       --usePkcs12TrustStore ~/path/to/opendj/config/keystore \
       --trustStorePassword:file ~/path/to/opendj/config/keystore.pin \
       --bindDn uid=admin \
       --bindPassword str0ngAdm1nPa55word \
       --backendId amCts \
       --ldifFile output-cts.ldif
     Import task ImportTask-2f93d32f-0599-4215-8d3e-ecb77164d64b scheduled to start immediately
     …​
     Import task ImportTask-2f93d32f-0599-4215-8d3e-ecb77164d64b has been successfully completed
     ```

   * This command imports the UMA-related data into a DS server instance at `ds-uma.example.com`:

     ```bash
     $ /path/to/opendj/bin/import-ldif \
       --hostname ds-uma.example.com \
       --port 1636 \
       --useSsl \
       --usePkcs12TrustStore ~/path/to/opendj/config/keystore \
       --trustStorePassword:file ~/path/to/opendj/config/keystore.pin \
       --bindDn uid=admin \
       --bindPassword str0ngAdm1nPa55word \
       --backendId umaRsStore \
       --ldifFile output-uma.ldif
     Import task ImportTask-2f93d32f-0599-4215-8d3e-ecb77164d64b scheduled to start immediately
     …​
     Import task ImportTask-2f93d32f-0599-4215-8d3e-ecb77164d64b has been successfully completed
     ```

   * Follow the steps in [Migrate policy or application data to DS](../setup/prepare-policy-and-application-store.html#migrate-policy-and-application-data) to import the policy and application data to the DS server you've set up for that purpose.

   You can find more information about this command in [import-ldif](https://docs.pingidentity.com/pingds/8.1/tools-reference/import-ldif.html).

4. On your AM configuration server, delete the dynamic data you've exported.

   |   |                                                                                                                                                                                                                                                                         |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Although you don't *have* to do this, it does result in a cleaner migration of static configuration. You must have a clear understanding of how your data is stored in the underlying LDAP directory before you delete the dynamic data you don't want to store in FBC. |

   To delete all policy definitions and applications:

   1. Create a text file that includes the following subtrees:

      ```bash
      $ cat subtrees-to-delete.txt
      ```

      Output

      ```bash
      o=sunamhiddenrealmdelegationservicepermissions,ou=services,ou=am-config
      ou=AgentService,ou=services,ou=am-config
      ou=sunEntitlementService,ou=services,ou=am-config
      ou=sunEntitlementIndexes,ou=services,ou=am-config
      ou=sunFMCOTConfigService,ou=services,ou=am-config
      ou=sunFMIDFFMetadataService,ou=services,ou=am-config
      ou=sunFMSAML2MetadataService,ou=services,ou=am-config
      ou=sunFMWSFederationMetadataService,ou=services,ou=am-config
      ```

   2. Send this list to the `ldapdelete` command on standard input:

      ```bash
      $ cat subtrees-to-delete.txt | /path/to/opendj/bin/ldapdelete \
      --hostname ds.example.com \
      --port 1636 \
      --useSsl \
      --usePkcs12TrustStore ~/path/to/opendj/config/keystore \
      --trustStorePassword:file ~/path/to/opendj/config/keystore.pin \
      --bindDN "uid=admin" \
      --bindPassword str0ngAdm1nPa55word \
      --deleteSubtree
      # DELETE operation successful for DN o=sunamhiddenrealmdelegationservicepermissions,ou=services,ou=am-config
      …​
      ```

## Export existing configuration data

The migration utility consumes an LDIF export of the existing configuration.

Use the `export-ldif` command to export the data, supplying the following parameters:

* The backend ID of the configuration store, `cfgStore` by default.

* The base DN of the branch containing the configuration, `ou=am-config` by default.

* An LDIF file to store the exported configuration.

The following example, run on the DS server, assumes the default parameters when DS is [installed for AM configuration](https://docs.pingidentity.com/pingds/8.1/install-guide/profile-am-config.html):

```bash
$ /path/to/opendj/bin/export-ldif \
--backendId cfgStore \
--includeBranch ou=am-config \
--ldifFile /path/to/export-config/exported-configuration.ldif \
--offline
…​
 category=BACKEND severity=INFO seq=34 msg=Exported 1528 entries and skipped 0 in 0 seconds (average rate 24254.0/sec)
```

The exported file contains the existing configuration under `ou=am-config`:

```bash
$ more /path/to/export-config/exported-configuration.ldif
dn: ou=am-config
objectClass: top
objectClass: untypedObject
ou: am-config
…​
```

## Migrate exported configuration to FBC

The migration utility is an enhanced version of the AM `amupgrade` command, available in the AM `.zip` file.

1. If you don't already have it, download `AM-8.1.1.zip` from the [Ping Identity Download Center](https://backstage.pingidentity.com/downloads).

2. Extract the contents of the `.zip` archive.

3. In the extracted directory, locate and extract the `Config-Upgrader-8.1.1.zip` archive.

4. To migrate the LDAP configuration, run the `amupgrade` command with the `migrationMode` argument:

   ```bash
   $ /path/to/amupgrade \
   --migrationMode \
   --inputConfig input-directory \
   --output output-directory \
   /path/to/amupgrade/rules/fbc/migrate-to-fbc.groovy
   ```

   > **Collapse: command-line arguments**
   >
   > * `--amsterVersion, -a`
   >
   >   The version of Amster that will be used to import the configuration (for example 8.0.0). This parameter is required unless you provide the `--migrationMode` or `--fileBasedMode` arguments.
   >
   > * `--baseDn, -d`
   >
   >   Lets you set a custom base DN.
   >
   > * `--clean`
   >
   >   The migration should remove all existing files from the output location directory.
   >
   >   Default: true
   >
   > * `--fileBasedMode, -m`
   >
   >   The configuration to be upgraded is file-based configuration (not Amster-exported configuration).
   >
   >   Default: false
   >
   > * `--ignoreNoRuleTracking`
   >
   >   Don't check for the existence of the Configuration Version Service. This lets you run the migration tool against individual files. However, it means that rules can be run multiple times against those files. Most rules don't support this. Use with caution.
   >
   >   Default: false
   >
   > * `--ignoreRequiredSecretMapping`
   >
   >   Prevents the upgrade from terminating due to missing required secret label mappings. Use with caution.
   >
   >   Default: false
   >
   > * `-i, --inputConfig`
   >
   >   The directory containing the LDIF configuration files that you're migrating.
   >
   > * `--log-output, -l`
   >
   >   The logging output file; logs at FINE by default and FINEST in verbose mode.
   >
   > * `--migration-mode`
   >
   >   The upgrade command should *migrate* the configuration from LDIF data to file-based (JSON) data.
   >
   > * `--prettyArrays`
   >
   >   Whether to print each JSON array value on a new line.
   >
   >   Default: false
   >
   > * `-o | --output directory`
   >
   >   The directory on the file system to which the migration utility writes the generated FBC.
   >
   > * `--secretsConfigFile, -f`
   >
   >   The properties file that contains settings necessary to migrate credentials to secrets. This file is required if your rules contain secrets upgrades. Read the `sampleconfig.properties` file for more details.
   >
   > * `--sectionsSource, -s`
   >
   >   A file that specifies the structure (*section* details) of the output configuration.
   >
   >   Without this option, the migration utility generates the configuration properties as flat files.
   >
   >   This file can be a `section.properties` file for a specific service or an `AM.war` file that includes the structure for all services.
   >
   >   > **Collapse: Example  file for JSON audit handler**
   >   >
   >   > ```properties
   >   > ########################################################################################################################
   >   > # Common handler section properties
   >   > ########################################################################################################################
   >   > commonHandler=enabled
   >   > commonHandler=topics
   >   >
   >   > ########################################################################################################################
   >   > # Common handler plugin section properties
   >   > ########################################################################################################################
   >   > commonHandlerPlugin=handlerFactory
   >   >
   >   > ########################################################################################################################
   >   > # JSON handler section properties
   >   > ########################################################################################################################
   >   > jsonConfig=location
   >   > jsonConfig=elasticsearchCompatible
   >   > jsonConfig=rotationRetentionCheckInterval
   >   > jsonFileRotation=rotationEnabled
   >   > jsonFileRotation=rotationMaxFileSize
   >   > jsonFileRotation=rotationFilePrefix
   >   > jsonFileRotation=rotationFileSuffix
   >   > jsonFileRotation=rotationInterval
   >   > jsonFileRotation=rotationTimes
   >   > jsonFileRetention=retentionMaxNumberOfHistoryFiles
   >   > jsonFileRetention=retentionMaxDiskSpaceToUse
   >   > jsonFileRetention=retentionMinFreeSpaceRequired
   >   > jsonBuffering=bufferingMaxSize
   >   > jsonBuffering=bufferingWriteInterval
   >   > ```
   >
   > * `rules-file-path`
   >
   >   The path to the upgrade rules file.
   >
   >   Although you're not using this command to upgrade to a new version, the `amupgrade` command requires an upgrade rules file.
   >
   >   Use the `noop.groovy` file (located in (`/path/to/amupgrade/rules/fbc/noop.groovy`) to migrate the configuration without applying any rules.
   >
   > * `--version, -V`
   >
   >   Prints the version of this configuration upgrader tool and exits.
   >
   > * `--verbose, -v`
   >
   >   Logs verbose output; outputs at FINE level to the console and FINEST level to files.

   For example:

   ```bash
   $ /path/to/amupgrade \
   --migrationMode \
   --inputConfig /path/to/export-config/ \
   --output /path/to/fbc/config/ \
   /path/to/amupgrade/rules/fbc/migrate-to-fbc.groovy
   ```

   In this example, the new JSON configuration files are generated in `/path/to/fbc/config/`.

   A sample `alpha` realm configuration might look like the following:

   ```json
   $ more /path/to/am/config/services/global/realms/root-alpha.json
   {
     "metadata": {
       "realm": "/alpha",
       "entityType": "",
       "entityId": "L2FscGhh",
       "uid": "o=alpha,ou=services,ou=am-config",
       "sunServiceID": null,
       "objectClass": [
         "sunRealmService",
         "top"
       ],
       "pathParams": {},
       "ou": []
     },
     "data": {
       "_id": "root-alpha",
       "_type": {
         "_id": "",
         "name": "",
         "collection": false
       },
       "active": true,
       "aliases": [
         "alpha"
       ],
       "parentPath": "/",
       "name": "alpha"
     }
   }
   ```

## Provide configuration files to AM

1. Stop AM or the container where it runs.

2. Copy the FBC files to the location of the *deployment layer* of your AM 8.0 configuration, by default, `/path/to/am/config/services`.

   Learn more about the deployment layer in [How AM reads FBC](../installation/fbc.html#how-am-reads-FBC).

   AM reads FBC from its home directory. You'll need access to this directory on your local host or in your Docker container.

   For local hosts, change to the $AM\_HOME/config/services directory:

   ```bash
   $ cd $AM_HOME/config/services
   ```

3. Copy the migrated configuration into the `services` directory.

   ```bash
   $ cp /path/to/fbc/config/ $AM_HOME/config/services
   ```

   If the directory contains default configuration, delete it before copying in your migrated configuration.

## Start AM in FBC mode

When you've migrated your configuration to JSON files, you can point your upgraded AM instances to the FBC, and to the new policy and application datastores.

These instructions assume a local AM server running in an Apache Tomcat container. Adjust the instructions to suit your environment.

1. Set the following Java variable to `true`:

   `com.sun.identity.sm.sms_object_filebased_enabled=true`

2. Pass that variable to AM in some way. For example, for Tomcat you can set the variable in the `CATALINA_OPTS` options:

   ```bash
   export CATALINA_OPTS="$CATALINA_OPTS -Dcom.sun.identity.sm.sms_object_filebased_enabled=true"
   ```

3. Restart AM or the container where it runs.

4. Start up and test your environment.

   Check that AM has the configuration you expect. You can also make changes to your configuration through the AM admin UI and check that those changes are made in the JSON configuration files.

## Troubleshoot your FBC migration

Use these sections to help you troubleshoot if you encounter the following errors during a migration to FBC:

> **Collapse: Failed to import /etc/am/configuration/global/DataStoreService.json**
>
> * Upgrade scenario
>
>   FBC import after an Amster export
>
> * Error
>
>   `user-data: [main] ERROR org.forgerock.amster.org.forgerock.openam.sdk.http.DefaultErrorHandler - Unhandled client error: [Status: 400 Bad Request] user-data: Failed to import /etc/am/configuration/global/DataStoreService.json`
>
> * Explanation
>
>   The order of imported files causes the import of `DataStoreService.json` to fail because the datastore instances that it references (for external application and policy stores) have not yet been created.
>
> * Solution
>
>   Import the `global/DataStoreInstance` path first, then import the remaining configuration.

> **Collapse: Invalid SSO Token**
>
> * Upgrade scenario
>
>   FBC import after an Amster export
>
> * Error
>
>   `ERROR: Error updating properties for server null and tab sdk com.sun.identity.sm.SMSException: Invalid SSO Token: Invalid SSO Token`
>
> * Explanation
>
>   Importing the CTS store properties when moving to an external CTS store fails for any subsequent import files because the CTS session is no longer valid.
>
> * Solution
>
>   Import the `global/Servers` path first, then import `global/DefaultCtsDataStoreStoreProperties` and finally import the remaining configuration.

> **Collapse: Data validation failed for the attribute, Secret Label**
>
> * Upgrade scenario
>
>   FBC import after an Amster export of configuration prior to 7.5.0
>
> * Error
>
>   `Failed to import …​output/global/KeyStoreSecretStore/default-keystore/KeyStoreMappings/am.default.authentication.nodes.persistentcookie.encryption.json ERROR org.forgerock.openam.sdk.http.ClientErrorException: 400 Bad Request: Data validation failed for the attribute, Secret Label`
>
> * Explanation
>
>   The secret mapping labels for persistent cookies changed in 7.5. As a result an attempt to import previous names fails.
>
> * Solution
>
>   Before performing the import:
>
>   1. Remove any instances of `global/KeyStoreSecretStore/…/am.default.authentication.modules.persistentcookie.encryption.json`
>
>   2. Remove any instances of `global/KeyStoreSecretStore/…/am.default.authentication.modules.persistentcookie.signing.json`
>
>   3. Rename any instances of `global/KeyStoreSecretStore/…/am.default.authentication.nodes.persistentcookie.encryption to am.authentication.nodes.persistentcookie.encryption`. Modify the contents of each renamed file and perform the same search and replace.
>
>   4. When the import is complete, optionally add encryption and signing secrets in the realms in which the `PersistentCookieAuthModule` is used. The new secret mapping format is:
>
>      `am.authentication.modules.persistentcookie.persistent-cookie-instance-name.encryption`
>
>      `am.authentication.modules.persistentcookie.persistent-cookie-instance-name.signing`

> **Collapse: services/customusernamecollector': Trying to redefine version 0.0 for path**
>
> * Upgrade scenario
>
>   FBC import after an Amster export
>
> * Error
>
>   `ERROR o.f.a.CrestApiProducer - ApiDescription 'frapi:openam/realm-config:2.0//services/customusernamecollector': Trying to redefine version 0.0 for path ''`
>
> * Explanation
>
>   The `CustomUsernameCollectorAuth` module isn't recognized as an authentication module after the Amster import causing a failure to access the global service configuration.
>
> * Solution
>
>   Before importing the upgraded Amster configuration, make sure the `'com.example.custom.CustomUsernameCollectorAuth'` is included in the list of authenticators in the `global/Authentication.json file`. Edit that file and add it as follows:
>
>   ```json
>   "authenticators" : [ "com.sun.identity.authentication.modules.ad.AD",
>   ...
>   "org.forgerock.openam.authentication.modules.amster.Amster",
>   "org.forgerock.openam.authentication.modules.CustomUsernameCollectorAuth" ]
>   ```
>
>   |   |                                                                                                             |
>   | - | ----------------------------------------------------------------------------------------------------------- |
>   |   | This example includes line breaks for legibility. In your file, the modules should all be on a single line. |

> **Collapse: UMA settings aren't applied**
>
> * Upgrade scenario
>
>   FBC import after an Amster export
>
> * Error
>
>   `Could not create token in token data store: Operation failed: Result Code: Insufficient Access Rights`
>
> * Explanation
>
>   Amster doesn't export the default server settings for UMA. It only exports specific server settings, which inherit from the default server settings.
>
> * Solution
>
>   Before you import the `global/Servers/01/UmaDataStoreProperties.json` file:
>
>   * If your deployment includes UMA configuration that is inherited from the server defaults (for example, the configuration for UMA to use external datastores), modify the inherited property to be `false` so that the specific server settings override the server defaults.
>
>   * Alternatively, remove the specific server file so that it's not imported and doesn't override the server defaults.

> **Collapse: Amster import fails for  file**
>
> * Upgrade scenario
>
>   FBC import after an Amster export
>
> * Error
>
>   \`ERROR o.f.o.c.s.SmsJsonConverter - Invalid attribute named snmpPort specified.
>
> * WARN o.f.o.c.r.s.SmsSingletonProvider - ::SmsSingletonProvider
>
>   InvalidAttributeException on Update org.forgerock.openam.core.sms.InvalidAttributeException: Invalid attribute specified.\`
>
> * Explanation
>
>   Performing an Amster import from an upgraded previous version export fails for `global/Monitoring.json` because the `snmpPort` and `snmpEnabled` attributes aren't recognized.
>
> * Solution
>
>   Before importing the `Monitoring.json` file, remove the `snmpPort` and `snmpEnabled` attributes and values.

> **Collapse: Errors related to the keystore**
>
> * Upgrade scenario
>
>   Server startup with FBC
>
> * Errors
>
>   `ERROR: Unable to read private key password file` `ERROR: mapPk2Cert.JKSKeyProvider: java.io.FileNotFoundException` `ERROR: EventService.restartPSearches() Unable to start listener class com.sun.identity.sm.ldap.LDAPEventManager for data store DataStoreId…​ [CONTINUED]Unable to retrieve a connection`
>
> * Explanation
>
>   These errors can be thrown when AM is unable to find the required keystores.
>
> * Solution
>
>   Make sure your secret stores are configured correctly after the migration.

---

---
title: Plan the upgrade
description: Plan your PingAM upgrade by reviewing release notes, testing changes, and backing up your deployment before upgrading to a new major or minor version
component: pingam
version: 8.1
page_id: pingam:upgrade:upgrade-planning
canonical_url: https://docs.pingidentity.com/pingam/8.1/upgrade/upgrade-planning.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Upgrade"]
page_aliases: ["upgrade-guide:upgrade-planning.adoc"]
section_ids:
  plan-upgrade-downtime: Route around servers during downtime
  pre-upgrade-backup: Back up the deployment
  review-REST-API-versions: Review REST API versions before upgrading
  pre-upgrade-certificates: Review PingDS certificates before upgrading
  pre-upgrade-customization: Customize before upgrading
  post-upgrade-rollback: Plan for rollback
  testing-upgrade: Upgrade in a test environment first
---

# Plan the upgrade

The work involved in upgrading AM software depends on the magnitude of change between your current version and the new version:

* Maintenance releases have a limited effect on current functionality but contain necessary bug and security fixes. Keep up to date with maintenance releases, as the fixes are important and the risk of affecting service is minimal.

* When upgrading to a new major or minor release, always plan and test the changes before carrying out the upgrade in production. Make sure you read the [Release notes](https://docs.pingidentity.com/pingam/release-notes/preface.html) for intervening versions with care. Identify any changes likely to affect your deployment and then plan accordingly.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Authentication modules and chains have been removed in AM 8.0. If you're still using modules and chains for authentication, you must migrate to [nodes and trees](../am-authentication/migrate-to-auth-trees.html) as soon as possible.It's recommended that you migrate to nodes and trees *before* upgrading to AM 8.If that's not possible, and you need access to modules and chains for migration purposes, you can temporarily re-enable modules and chains in AM 8.0.> **Collapse: Re-enable modules and chains**
>
> 1. Go to Configure > Server Defaults > Advanced in the AM admin UI.
>
> 2. Add the `org.forgerock.am.authentication.chains.enabled` property and set it to `true`.
>
> 3. Save your changes.
>
> 4. Restart AM or the container where it runs.
>
> You can now access modules and chains through the REST endpoints. Modules and chains aren't accessible through the AM admin UI.The option to re-enable modules and chains is only for migration purposes in AM 8.0. Authentication modules and chains will be removed completely in an upcoming release. |

Review the following best practices before you upgrade AM:

* [Route around servers during downtime](#plan-upgrade-downtime)

* [Back up the deployment](#pre-upgrade-backup)

* [Review REST API versions before upgrading](#review-REST-API-versions)

* [Review PingDS certificates before upgrading](#pre-upgrade-certificates)

* [Customize before upgrading](#pre-upgrade-customization)

* [Plan for rollback](#post-upgrade-rollback)

* [Upgrade in a test environment first](#testing-upgrade)

## Route around servers during downtime

Upgrading servers takes at least one of your AM sites down while you update the server configurations to the new version. Plan for this site to be down. Route client applications to another site until the upgrade process is complete, and you have validated the result. Make sure client application owners are aware of the change, and let them know what to expect.

If you only have a single AM site, make sure the downtime happens in a low-usage window, and make sure you let client application owners plan accordingly.

|   |                                                                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | During an upgrade, restrict access to the AM admin UI. The Upgrade Wizard doesn't require authorization. Immediately after you deploy the new `.war` file, any user with access to the AM admin UI can start the upgrade process. |

## Back up the deployment

Always back up your deployment before you upgrade. If something goes wrong during the upgrade process, you can then roll back to the previous version.

* In production environments, back up your configuration as described in [Back up configurations](../maintenance/backup-restore.html).

* In preparation for upgrading AM servers and their configurations, also take LDIF backups of the configuration store data in the directory servers. If possible, stop servers before upgrading and take a file system backup of the deployed servers and also of their configuration directories. This can make it easier to roll back from a failed upgrade.

  For example, if you deploy AM in Apache Tomcat under `/am`, you might take a file system backup of the following directories for each AM server:

  * `/path/to/tomcat/webapps/am/`

  * `~/am/`

  * `~/.openamcfg/`

* When upgrading tools, keep copies of any customized scripts.

* Back up the key stores and trust stores you use to connect securely.

* Record any custom advanced server properties configured under Configure > Server Defaults > Advanced or Deployment > Servers > *server name* > Advanced in the AM admin UI. These properties are lost during the upgrade and must be re-added after the upgrade is complete.

## Review REST API versions before upgrading

Upgrading AM can update the default API version of several AM endpoints. After an upgrade, your applications might experience issues connecting to endpoints if they don't specify the API version in REST calls.

By default, an upgraded AM instance responds to REST calls that don't specify version information with the oldest version available for the endpoint. However, the oldest supported version might not be the one required by the application, as API versions become deprecated or unsupported.

To avoid version conflicts between application calls and REST endpoint APIs, consider specifying the protocol and resource version required by the application in the `Accept-API-Version` header when making requests to REST endpoints. Learn more in [Specify REST API versions](../am-rest/rest-api-versioning.html#rest-api-explicit-version).

|   |                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | AM includes a CSRF protection filter that's enabled by default. REST requests other than GET, HEAD, and OPTIONS made to endpoints under the `json/` root return 403 Forbidden messages unless they include the `X-Requested-With` or `Accept-API-Version` headers.Learn more in [Protect against CSRF attacks](../security/rest-CSRF.html). |

You can configure AM's default REST API behavior. Learn more in [Configure versioning behavior](../am-rest/rest-api-versioning.html#configure-default-version).

## Review PingDS certificates before upgrading

Before you upgrade, review the certificates used to establish secure connections between AM and the DS stores.

If the FQDN value from the `subject` field of a non-wildcard certificate doesn't match the FQDN obtained from DNS for the DS instance, AM can't establish a secure connection with DS. Additionally, if the DS instance responds to multiple FQDNs, you must also specify them in the certificate.

This step is critical for the configuration store. If AM can't establish communication with the configuration store, it fails to start up.

You can find more information about setting up DS server certificates in [Key management](https://docs.pingidentity.com/pingds/8.1/security-guide/key-management.html) in the DS documentation.

## Customize before upgrading

Prepare a `.war` file that contains any customizations you require.

Customizations include any changes you've made to the AM server installation, such as the following:

* Custom plugins and extensions, for example:

  * Custom authentication nodes.

  * Custom SAML 2.0 attribute mappers.

  * Custom OAuth 2.0 scope validators.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | New functionality often changes the samples provided with AM.Don't copy custom plugins or extensions from a previous version of AM to the `.war` file.You must customize the samples of the version you're upgrading to before adding them to the `.war` file. For example, download the custom scope validator sample of the version you're upgrading to, customize it, recompile it, then add the resulting `.jar` file to the `.war` file.Failure to use the new version's samples as the base for your customizations can result in unexpected behavior. |

* Customized JSPs, redesigned login or service pages and additional CSS and visual content.

* Any changes to AM classes or APIs.

  |   |                                                                                                                                                                                    |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Recompile any custom implementations you have created with each release of AM, because the method signature or imports for supported and evolving APIs can change in each version. |

* Any changes or additional Java class libraries (such as `.jar` files in `WEB-INF/lib` ).

## Plan for rollback

Sometimes even a well-planned upgrade operation fails. In such cases, you need a plan to roll back to the pre-upgrade version.

For AM servers, you can roll back by restoring from a file system backup. Restore the old configuration directory service from LDIF before you restart the old servers. Learn more in [Back up configurations](../maintenance/backup-restore.html).

|   |                                                                                                                                                                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you upgraded using the [upgrade wizard](upgrade-servers.html#upgrade-wizard) and need to roll back the upgrade to a version earlier than AM 7.4, you must restore the *default keystore*. The upgrade wizard removes a default alias that AM versions before AM 7.4 need to start. If you don't restore this alias, the rolled back instance of AM won't start up. |

## Upgrade in a test environment first

Always try upgrading AM in a test environment before applying the upgrade in your production environment.

This helps you assess the volume of work required without affecting your production environment, and can circumvent unforeseen problems.

---

---
title: Supported upgrade paths
description: Upgrade to PingAM from any supported 7.x or 8.x version, or through intermediate versions if upgrading from unsupported releases
component: pingam
version: 8.1
page_id: pingam:upgrade:supported-upgrades
canonical_url: https://docs.pingidentity.com/pingam/8.1/upgrade/supported-upgrades.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Upgrade"]
page_aliases: ["upgrade-guide:supported-upgrades.adoc"]
---

# Supported upgrade paths

You can upgrade to AM 8.1 from any AM 7.x or 8.x version.

If you're upgrading to AM 8.1 from an *unsupported* version of AM, you must upgrade to a supported version first, and then to AM 8.1.

Find information about supported versions in the [Ping Identity End of Life (EOL) Software Tracker](https://support.pingidentity.com/s/article/Ping-Identity-EOL-Tracker#pam).

---

---
title: Upgrade
description: Learn how to upgrade PingAM deployments across maintenance, minor, and major releases, including planning, core services, components, and migration to file-based configuration
component: pingam
version: 8.1
page_id: pingam:upgrade:preface
canonical_url: https://docs.pingidentity.com/pingam/8.1/upgrade/preface.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Upgrade"]
page_aliases: ["index.adoc", "upgrade-guide:preface.adoc"]
---

# Upgrade

This guide covers common aspects of upgrading an AM deployment, whether you are moving to a new maintenance release, upgrading to a new major release, or migrating from a legacy release to a newer AM release.

Release levels, and how much change to expect in a maintenance, minor, or major release, are defined in [Product Release Levels](https://docs.pingidentity.com/pingam/release-notes/stability.html#release-levels). Release levels are identified by version number.

[icon: check-square, set=fad, size=3x]

#### [Before you upgrade](upgrade-planning.html)

Review the tasks you need to complete before upgrading AM.

[icon: server, set=fad, size=3x]

#### [Upgrade servers](upgrade-servers.html)

Learn, step by step, how to upgrade the AM core services.

[icon: circle-arrow-up, set=fad, size=3x]

#### [Upgrade components](upgrade-components.html)

Review components and services that you might need to upgrade or reconfigure.

[icon: files, set=fad, size=3x]

#### [Migrate to FBC](migrate-to-fbc.html)

Migrate from an LDAP configuration store to file-based configuration.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | AM supports several versions of the web and Java agents, so you don't usually need to upgrade your agents when you upgrade AM.You can find information on the supported AM versions in [Web Agents](https://docs.pingidentity.com/web-agents/latest/release-notes/before-you-install.html#am-requirements) or [Java Agents](https://docs.pingidentity.com/java-agents/latest/release-notes/before-you-install.html#am-requirements).Learn more about upgrading web and Java agents in the [Web Agents documentation](https://docs.pingidentity.com/web-agents/2025.3/upgrade/preface.html) or the [Java Agents documentation](https://docs.pingidentity.com/java-agents/2025.3/upgrade/preface.html). |

---

---
title: Upgrade AM instances
description: Upgrade PingAM server instances by deploying new software on each server and updating the configuration on one server in your site
component: pingam
version: 8.1
page_id: pingam:upgrade:upgrade-servers
canonical_url: https://docs.pingidentity.com/pingam/8.1/upgrade/upgrade-servers.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Upgrade"]
page_aliases: ["upgrade-guide:upgrade-servers.adoc"]
section_ids:
  high_level_upgrade_steps: High-level upgrade steps
  before-you-upgrade: Before you upgrade
  upgrade-tomcat: Upgrade Tomcat
  upgrade-config: Upgrade the server and configuration
  upgrade-amupgrade: amupgrade
  amupgrade_rules: amupgrade rules
  before_you_start: Before you start
  upgrade_from_an_amster_configuration_export: Upgrade from an Amster configuration export
  upgrade_from_a_file_based_configuration: Upgrade from a file-based configuration
  upgrade-wizard: Upgrade wizard
  upgrade-rest: Upgrade over REST
  update_tools_scripts_and_components: Update tools, scripts, and components
  update-schema: Update the schema
  configuration_store: Configuration store
  identity_store: Identity store
  after_upgrade: After upgrade
---

# Upgrade AM instances

To upgrade an AM deployment, you must upgrade each *server instance* in your site by upgrading the AM software on each server. You only need to upgrade the configuration on *one* server in the site.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | * AM 8.1 supports Apache Tomcat 10 as a web application container. If you use Apache Tomcat, you *must* upgrade to at least version 10 before you upgrade to AM 8.1.

* AM 8.1 supports a file-based configuration store (FBC) in production deployments. If you migrate your configuration to FBC, there is no longer the concept of separate *sites*. Each server has its own ID and its own local configuration. Learn more in [FBC and AM sites](../installation/fbc.html#fbc-and-am-sites). |

## High-level upgrade steps

Upgrading AM involves the following high-level steps:

* On one server in your site

  1. If you use Apache Tomcat as an application container:

     1. Stop AM or the container where it runs.

     2. [Upgrade Tomcat](#upgrade-tomcat) if needed.

  2. Upgrade the AM server software.

     The server is upgraded when you deploy the `.war` file of the new version. You must deploy the new `.war` file on each server in the site.

  3. Upgrade the configuration.

     Use one of the following methods:

     * [`amupgrade`](#upgrade-amupgrade)

       This utility is provided in the `AM-8.1.1.zip` file and upgrades a file-based configuration (FBC) or a configuration exported using Amster. This is the recommended way to update the configuration.

     * [Upgrade wizard](#upgrade-wizard)

       The upgrade wizard is launched when you replace a deployed AM `.war` file with a newer version, then go to the deployment URL.

     * [Upgrade over REST](#upgrade-rest)

       Send a `GET` request to the `config/upgrade/upgrade.htm` endpoint to initiate the upgrade over REST.

  4. Update the schema

     Generally, the configuration store schema is updated when you update the configuration. From time to time, updates are required to the schema of other datastores, such as the identity store or the CTS store. You must make these updates manually.

     Learn more in [Update the schema](#update-schema).

  5. Update tools and scripts.

     Read the [Release notes](https://docs.pingidentity.com/pingam/release-notes) to understand the changes introduced in each version before you update AM tools and scripts.

  6. Restart AM or the container where it runs.

* On the remaining servers in your site

  1. If you use Apache Tomcat as an application container:

     1. Stop AM or the container where it runs.

     2. [Upgrade Tomcat](#upgrade-tomcat) if needed.

  2. Upgrade the AM server software.

     The server is upgraded when you deploy the `.war` file of the new version. You must deploy the new `.war` file on each server in the site.

  3. Restart AM or the container where it runs.

|   |                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you're upgrading to AM 8.1 from an *unsupported* version of AM, you might need to upgrade to a supported version first, and then to AM 8.1. |

## Before you upgrade

You *must* follow these steps before you start an upgrade.

1. [Plan your upgrade](upgrade-planning.html).

2. [Prepare a customized AM `.war` file](upgrade-planning.html#pre-upgrade-customization).

3. [Back up your deployment](upgrade-planning.html#pre-upgrade-backup).

4. [Route client application traffic to another site](upgrade-planning.html#plan-upgrade-downtime) during the upgrade.

5. Make the transient state encryption key available to *all instances* in the site.

   An AES 256-bit key called `directenctest` must be available to all instances in the site. This might mean, for example, copying the keystore across the site.

   This key doesn't need to be the same key that AM provides in the default keystore.

   If you don't provide this key, AM won't start up after the upgrade.

   > **Collapse: What is the  key for?**
   >
   > AM uses the `directenctest` key to encrypt information stored in the [transient state](../auth-nodes/store-values-shared-state.html#store-values-in-transient-state) of authentication trees.
   >
   > The upgrade process maps this key to the `am.authn.trees.transientstate.encryption` secret label.

   > **Collapse: How do I make the  key available?**
   >
   > The alias must exist in a secret store configured globally, so that all realms can access it. You can configure additional secrets by realm, if required, after the upgrade.
   >
   > \+ You can create a new secret store to house this secret, or you can add it to one of your existing stores.
   >
   > \+ The following example creates the key alias in the AM keystore, or in a keystore configured in a secret store:
   >
   > \+
   >
   > ```bash
   > $ keytool \
   > -genseckey \
   > -alias directenctest \
   > -keyalg AES \
   > -keysize 256 \
   > -storetype JCEKS \
   > -keystore /path/to/keystore.jceks
   > ```

   > **Collapse: Where do I find the keystore passwords?**
   >
   > The passwords are stored as secrets in a separate secret store. For example, a file system volume secret store.

   After the upgrade, you can rename the key alias or set a different key in the secret label mapping. Make sure the secret label is always mapped to an existing, resolvable secret or key alias.

## Upgrade Tomcat

From AM 8.0 Apache Tomcat 10.x is supported. Support for earlier Tomcat versions is removed. If you use Apache Tomcat as an application container, you must install Apache Tomcat 10.x and deploy AM 8.1 into that container. Running AM 8 in an Apache Tomcat 8.5 or 9 container *does not work*.

In addition to downloading and installing Apache Tomcat 10.x, make the following changes before you deploy AM:

* Update any custom scripts, configurations, and allowlist entries to reflect the change to Jakarta EE 9 (Servlet API 5.0). In particular, change the following references:

  * `javax.servlet` → `jakarta.servlet`

  * `javax.websocket` → `jakarta.websocket`

  You don't need to change other `javax` references, such as `javax.xml` and `javax.inject`.

* The Tomcat system property to manage encoded slash (`/`) characters in requests has changed.

  The `org.apache.tomcat.util.buf.UDecoder.ALLOW_ENCODED_SLASH` property has been removed in Tomcat 10 and replaced with the `encodedSolidusHandling` property.

  Update references to the old property in the `Connector` element in your Tomcat `server.xml` file.

  |   |                                                                                |
  | - | ------------------------------------------------------------------------------ |
  |   | In production environments, avoid resource names that contain forward slashes. |

## Upgrade the server and configuration

Use one of the following methods to upgrade the AM server software and configuration:

### `amupgrade`

The `amupgrade` utility converts AM configuration files so that the configuration can be used with the latest AM version. Use this utility with `Amster` and to upgrade file-based configurations. The utility has the same Java requirements as AM. Learn more about these [requirements](https://docs.pingidentity.com/pingam/release-notes/requirements.html) in the Release notes.

#### `amupgrade` rules

The `amupgrade` utility uses *upgrade rules* to convert configuration between versions.

The upgrade rules are *sequential*, that is, they upgrade configuration from one version to the next [minor](https://docs.pingidentity.com/pingam/release-notes/stability.html#release-levels) consecutive version. If you're upgrading to a version greater than the next minor consecutive version, you must run multiple `amupgrade` commands sequentially until you reach the required configuration.

In other words, if you're upgrading your configuration from version 7.2.x to version 8.0.x:

1. Run `amupgrade` with the `7.2.x-to-7.3.x.groovy` rules file to get a 7.3 configuration.

2. Run `amupgrade` on the 7.3 configuration with `7.3.x-to-7.4.x.groovy` rules file to get a 7.4 configuration.

3. Continue running successive upgrades until you have an 8.0 configuration.

|   |                                                             |
| - | ----------------------------------------------------------- |
|   | You can't use `amupgrade` to upgrade a running AM instance. |

#### Before you start

1. Download the AM `.zip` file from the [Ping Identity Download Center](https://backstage.pingidentity.com/downloads).

2. Extract the contents of the `.zip` file.

3. In the extracted directory, locate the `Config-Upgrader-8.1.1.zip` file.

4. Extract the `Config-Upgrader-8.1.1.zip` file.

#### Upgrade from an `Amster` configuration export

1. [Export configuration data](../amster/export-config.html).

2. Upgrade the exported configuration to the new version:

   ```bash
   $ amupgrade \
   -i exported configuration \
   -o output directory \
   -a amster version \
   rules/amster/from-to-to.groovy
   ```

   Where:

   * exported configuration is the path to the configuration directory you generated in step 1

   * output directory is the directory to which the command writes the upgraded configuration

   * amster version is the version of Amster you will use to import the configuration

   * from is the AM version from which you're upgrading

   * to is the AM version to which you're upgrading

   * *rules* specifies the path to a configuration rules file in the `/path/to/amupgrade/rules` directory

   For example:

   ```bash
   $ amupgrade \
   -i /path/to/AM7.5Config/ \
   -o /path/to/AM8Config \
   -a 8.1.1 \
   rules/amster/7.5.x-to-8.1.x.groovy
   Reading existing configuration from files in /path/to/AM7.5-config/…​
   Modifying configuration based on rules in [rules/amster/7.5.x-to-8.1.x.groovy]…​
   reading configuration from Amster json files
   Writing configuration to new location at /path/to/AM8Config…​
   Upgrade Completed, modified configuration saved to /path/to/AM8Config
   ```

3. Install a new version of DS with an [`am-config` profile](https://docs.pingidentity.com/pingds/8.1/install-guide/profile-am-config.html).

   Don't upgrade or use an existing DS configuration store because configuration associated with the older DS version can cause conflicts.

4. Stop AM or the container where it runs.

5. Unconfigure AM by removing the configuration files in the $HOME directory of the user running the web application container.

   For example:

   ```bash
   $ rm -rf $HOME/am $HOME/.openamcfg
   ```

   To uninstall AM and its associated configuration files, delete the following directories:

   * *The configuration directory*.

     If you didn't use the default configuration location (`$HOME/am`), check the value of the `Base installation directory` property under Deployment > Servers > *server name* > General > System.

   * *The hidden directory that holds a file pointing to the configuration directory*.

     For example, if you are using Apache Tomcat as the web container, this file could be `$HOME/.openamcfg/AMConfig_path_to_tomcat_webapps_am_`.

6. Undeploy the AM web application.

   For example, if you are using Apache Tomcat as the web container, remove the `.war` file and expanded web application from the container:

   ```bash
   $ cd /path/to/tomcat/webapps/
   $ rm -rf am.war am/
   ```

7. [Upgrade Tomcat](#upgrade-tomcat).

8. [Install](../installation/interactive-install.html) the new version of AM using the new DS server for your configuration store.

9. [Import configuration data](../amster/import-config.html).

10. Restart AM or the container where it runs.

#### Upgrade from a file-based configuration

1. Run `amupgrade` to upgrade the configuration:

   ```bash
   $ amupgrade \
   -i existing-config \
   -o output-directory \
   --fileBasedMode \
   /path/to/amupgrade/rules/fbc/latest.groovy \
   --ignoreNoRuleTracking
   ```

   Where:

   * *existing-config* is the path to your existing FBC directory

   * *output-directory* is the directory to which the command writes the upgraded configuration

   * `--fileBasedMode` indicates that you're upgrading file-based configuration (FBC) rather than configuration exported with Amster

   * `rules` specifies the path to an upgrade rules file in the `/path/to/amupgrade/rules` directory

   * `--ignoreNoRuleTracking` lets you upgrade without specifying a configuration version

   For example:

   ```bash
   $ amupgrade \
   -i /path/to/am/config/services/ \
   -o /tmp/upgraded-services \
   --fileBasedMode \
   /path/to/amupgrade/rules/fbc/latest.groovy \
   --ignoreNoRuleTracking
   ```

2. Stop AM or the container in which it runs.

3. Move the existing configuration from the AM configuration directory to a temporary location:

   ```bash
   $ mv /path/to/am/config/services/* /tmp/old-services/
   ```

4. Move the upgraded configuration into the AM configuration directory:

   ```bash
   $ mv /tmp/upgraded-services/* /path/to/am/config/services/
   ```

5. Copy the `noninteractive-install.properties` from the old services directory to the AM configuration directory:

   ```bash
   $ cp /tmp/old-services/noninteractive-install.properties /path/to/am/config/services/
   ```

   |   |                                                                                                                                                                         |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can also set the startup properties as environment variables. Find more information in [FBC initial startup](../installation/passive-install-fbc.html#fbc-startup). |

6. Deploy your customized AM `.war` file.

   When you deploy the new `.war` file, you might need to delete working files left by the old deployment.

   For example, if you deploy on Apache Tomcat, replace `/path/to/tomcat/webapps/am.war` with the customized `.war` file, then recursively delete the `/path/to/tomcat/webapps/am/` and `/path/to/tomcat/work/Catalina/localhost/am/` directories before restarting the server.

7. Restart AM or the container where it runs.

### Upgrade wizard

The upgrade wizard brings the AM configuration, including the version number, up to date with the new version.

1. Stop AM or the container where it runs.

2. Deploy your customized AM `.war` file.

   When you deploy the new `.war` file, you might need to delete working files left by the old deployment.

   For example, if you deploy on Apache Tomcat, replace `/path/to/tomcat/webapps/am.war` with the customized `.war` file, then recursively delete the `/path/to/tomcat/webapps/am/` and `/path/to/tomcat/work/Catalina/localhost/am/` directories before restarting the server.

3. Restart AM or the container where it runs.

4. After deploying AM, but before upgrading, your application container serves AM's upgrader user interface.

   Suspend any external network access to the application container until the upgrade is complete. After the upgrade is complete, AM prevents access to the upgrader UI.

5. Go to the deployment URL and follow the prompts to upgrade.

6. Restart AM or the container where it runs.

7. Update the identity store schema:

   1. Log into AM.

   2. Go to Realms > *realm name* > Identity Stores.

   3. Select your external identity store and toggle Load Schema to ON.

   4. Click Save to apply your changes.

   5. If you have additional identity stores, repeat the previous steps for each store.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * The AM upgrade wizard uses three libraries that should be removed after upgrade, for security reasons.

  When your upgrade is complete, remove the following .jar files from the `WEB-INF/lib` directory:

  * `click-extras-2.3.0.jar`

  * `click-nodeps-2.3.0.jar`

  * `velocity-1.7-p1.jar`

  These files are used *only* by the install and upgrade wizards. Removing them won't affect your installed instance.

  You must also remove the references to `click-servlet` from the deployment descriptor file. Edit `/path/to/tomcat/webapps/am/WEB-INF/web.xml` to remove the following mappings:

  ```xml
  <servlet>
      <servlet-name>click-servlet</servlet-name>
      <servlet-class>org.apache.click.ClickServlet</servlet-class>
  </servlet>

  ...

  <servlet-mapping>
      <servlet-name>click-servlet</servlet-name>
      <url-pattern>*.htm</url-pattern>
  </servlet-mapping>
  ``` |

### Upgrade over REST

Sending a `GET` request to the `config/upgrade/upgrade.htm` endpoint initiates the same upgrade process as the upgrade wizard, and brings the AM configuration, including the version number, up to date with the new version.

1. Stop AM or the container where it runs.

2. Deploy your customized AM `.war` file.

   When you deploy the new `.war` file, you might need to delete working files left by the old deployment.

   For example, if you deploy on Apache Tomcat, replace `/path/to/tomcat/webapps/am.war` with the customized `.war` file, then recursively delete the `/path/to/tomcat/webapps/am/` and `/path/to/tomcat/work/Catalina/localhost/am/` directories before restarting the server.

3. Restart AM or the container where it runs.

4. Send an HTTP GET request as follows:

   ```bash
   $ curl "https://am.example.com:8443/am/config/upgrade/upgrade.htm?actionLink=doUpgrade&actionLink=saveReport&acceptLicense=true"
   true
   ```

5. Restart AM or the container where it runs.

6. Update the identity store schema:

   1. Log into AM.

   2. Go to Realms > *realm name* > Identity Stores.

   3. Select your external identity store and toggle Load Schema to ON.

   4. Click Save to apply your changes.

   5. If you have additional identity stores, repeat the previous steps for each store.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * The AM upgrade wizard uses three libraries that should be removed after upgrade, for security reasons.

  When your upgrade is complete, remove the following .jar files from the `WEB-INF/lib` directory:

  * `click-extras-2.3.0.jar`

  * `click-nodeps-2.3.0.jar`

  * `velocity-1.7-p1.jar`

  These files are used *only* by the install and upgrade wizards. Removing them won't affect your installed instance.

  You must also remove the references to `click-servlet` from the deployment descriptor file. Edit `/path/to/tomcat/webapps/am/WEB-INF/web.xml` to remove the following mappings:

  ```xml
  <servlet>
      <servlet-name>click-servlet</servlet-name>
      <servlet-class>org.apache.click.ClickServlet</servlet-class>
  </servlet>

  ...

  <servlet-mapping>
      <servlet-name>click-servlet</servlet-name>
      <url-pattern>*.htm</url-pattern>
  </servlet-mapping>
  ``` |

## Update tools, scripts, and components

1. Update Amster.

   Follow [Install Amster](../amster/install-amster.html) to install an updated version of Amster.

   When you have confirmed the new tools are working, delete the old tools.

2. Make sure the AM scripts are current and contain the modifications your environment requires.

   To avoid overwriting changes made in customized scripts, the upgrade process doesn't update scripts from earlier versions of AM.

   Check the scripts in your environment are compatible with the version of AM you're upgrading to by following these steps:

   1. Read the [Release notes](https://docs.pingidentity.com/pingam/release-notes) for information about possible changes.

   2. Install an AM 8.1.1 test environment, and compare the scripts.

      New installations always have the current scripts.

3. Review the information in [Upgrade components and services](upgrade-components.html) and decide if you need to reconfigure any of AM's services or features.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Reconfigure any custom advanced properties if necessary. These properties are lost during the upgrade, and you'll need to re-add them in the AM admin UI.> **Collapse: How do I configure advanced server properties?**
   >
   > * To configure advanced server properties for all instances of the AM environment, go to Configure > Server Defaults > Advanced in the AM admin UI.
   >
   > * To configure advanced server properties for a particular instance, go to Deployment > Servers > *server name* > Advanced.
   >
   > If the property you want to add or edit is already configured, click on the pencil ([icon: pencil-alt, set=fas]) button to edit it. When you are finished, click on the tick ([icon: check, set=fas]) button.
   >
   > Click Save Changes. |

## Update the schema

You might need to update the schema for specific datastores, depending on the version from which you are upgrading and the datastore type.

### Configuration store

Generally, updating your configuration makes the required schema updates to the configuration store.

After you've updated the configuration, add an access control instruction (ACI) to the configuration store directory to give the AM administrative user server-side sorting privileges.

The ACI should be similar to the following:

```ldif
aci: (targetcontrol="1.2.840.113556.1.4.473")(version 3.0;
acl "Allow server-side sorting"; allow (read)
 (userdn = "ldap:///uid=am,ou=admins,dc=example,dc=com");)
```

You can find more information about configuring AM configuration stores in [Prepare configuration stores](../installation/prepare-configuration-store.html).

### Identity store

Depending on the version you're upgrading from, and the features you've configured, you might need to update your identity store schema manually.

* Upgrade from AM 7.0 with a PingDS identity store

  1. In the path where you deployed the `am.war` file (for example, `/path/to/tomcat/webapps/am`) locate the following file in the `WEB-INF/template/ldif/opendj` directory:

     `opendj_retry_limit_node_count.ldif`

  2. Update the identity store schema as follows:

     ```bash
     $ /path/to/opendj/bin/ldapmodify \
     --hostname 'ds.example.com' \
     --port 1636 \
     --useSsl \
     --usePkcs12TrustStore /path/to/opendj/config/keystore \
     --truststorepassword:file /path/to/opendj/config/keystore.pin \
     --continueOnError \
     --bindDN uid=admin \
     --bindPassword str0ngAdm1nPa55word \
     /path/to/tomcat/webapps/am/WEB-INF/template/ldif/opendj/opendj_retry_limit_node_count.ldif
     ```

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | This schema update is required for the Save Retry Limit to User feature in the [Retry Limit Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/retry-limit-decision.html). The feature is enabled by default.Even if you aren't currently using the Retry Limit Decision node, you *should* make this schema update, in case you decide to use the node in the future. If you can't update the identity store schema at this point, you *must* disable the feature. |

* Using push or web authentication, or using the Ping SDKs for device profiling

  Apply the following LDIF files:

  * `/path/to/tomcat/webapps/am/WEB-INF/template/ldif/opendj/opendj_webauthndevices.ldif`

  * `/path/to/tomcat/webapps/am/WEB-INF/template/ldif/opendj/opendj_deviceprofiles.ldif`

  * `/path/to/tomcat/webapps/am/WEB-INF/template/ldif/opendj/opendj_bounddevices.ldif`

  For example:

  ```bash
  $ /path/to/opendj/bin/ldapmodify \
  --hostname 'ds.example.com' \
  --port 1636 \
  --useSsl \
  --usePkcs12TrustStore /path/to/opendj/config/keystore \
  --truststorepassword:file /path/to/opendj/config/keystore.pin \
  --continueOnError \
  --bindDN uid=admin \
  --bindPassword str0ngAdm1nPa55word \
  /path/to/tomcat/webapps/am/WEB-INF/template/ldif/opendj/opendj_webauthndevices.ldif \
  /path/to/tomcat/webapps/am/WEB-INF/template/ldif/opendj/opendj_deviceprofiles.ldif \
  /path/to/tomcat/webapps/am/WEB-INF/template/ldif/opendj/opendj_bounddevices.ldif
  ```

  If you don't make this schema change, you *must* remove the `webauthnDeviceProfilesContainer` object class from the user configuration after the upgrade:

  1. In the AM admin UI, go to Realms > *realm name* > Identity Stores > *identity store name*.

  2. On the User Configuration tab, remove `webauthnDeviceProfilesContainer` from the LDAP User Object Class.

  3. Save your changes.

  Make the same change for each identity store that doesn't have the schema change, and in each realm that uses the identity store.

## After upgrade

1. Validate the service is performing as expected.

2. Allow client application traffic to flow to the upgraded site.

---

---
title: Upgrade components and services
description: Plan your upgrade by reviewing component changes in later PingAM versions and performing additional configuration tasks beyond standard upgrade steps
component: pingam
version: 8.1
page_id: pingam:upgrade:upgrade-components
canonical_url: https://docs.pingidentity.com/pingam/8.1/upgrade/upgrade-components.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Upgrade"]
page_aliases: ["upgrade-guide:upgrade-components.adoc"]
---

# Upgrade components and services

As part of planning your upgrade, consider that some changes in later AM versions will have an impact on your environment. Usually, these changes are driven by changes in specification, security policies, or performance.

Wherever possible, the upgrade process makes the appropriate changes to your AM configuration. However, sometimes you'll need to perform additional configuration based on your environment.

In addition to the mandatory upgrade steps outlined in [Upgrade AM instances](upgrade-servers.html), if you're using features described in [these lists](https://docs.pingidentity.com/pingam/release-notes/changes.html), you'll need to perform further upgrade tasks.