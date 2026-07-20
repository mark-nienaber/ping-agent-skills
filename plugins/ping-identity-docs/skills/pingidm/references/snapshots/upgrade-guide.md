---
title: About upgrades
description: Overview of the manual PingIDM upgrade process, including supported upgrade paths, installation, configuration migration, and repository updates
component: pingidm
version: 8.1
page_id: pingidm:upgrade-guide:about-upgrades
canonical_url: https://docs.pingidentity.com/pingidm/8.1/upgrade-guide/about-upgrades.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Upgrade", "Migration"]
section_ids:
  supported-upgrade-paths: Supported upgrade paths
---

# About upgrades

The automated update process available with previous IDM versions is no longer supported. This chapter describes the manual process required to upgrade an existing IDM deployment. At a high level, the manual update process involves the following steps:

1. Install IDM 8.1.

2. Migrate your existing IDM configuration to the new installation.

3. Update your repository.

4. Test your scripts and customizations work as expected.

5. Migrate existing data to the new installation.

## Supported upgrade paths

The following table contains information about the supported upgrade paths to IDM 8.1:

**Upgrade Paths**

| Version   | Upgrade Supported to IDM 8.1 |
| --------- | ---------------------------- |
| IDM 8.0.x | YES                          |
| IDM 7.5.x | YES                          |
| IDM 7.4.x | YES                          |
| IDM 7.3.x | YES                          |
| IDM 7.2.x | YES                          |
| IDM 7.1.x | YES                          |
| IDM 7.0.x | YES                          |
| IDM 6.5.x | YES                          |
| IDM 6.0.x | YES                          |
| IDM 5.5.x | YES                          |
| IDM 5.0.x | YES                          |

|   |                                                                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Depending on how you have customized your deployment, there might be incompatible configuration changes when you upgrade from versions prior to IDM 6.5.x. Read the upgrade documentation for each interim release and apply all required script and configuration changes. |

---

---
title: Before you upgrade
description: Fulfill prerequisites before upgrading PingIDM, including verifying the Java version, backing up data, and reviewing changed functionality
component: pingidm
version: 8.1
page_id: pingidm:upgrade-guide:before-you-upgrade
canonical_url: https://docs.pingidentity.com/pingidm/8.1/upgrade-guide/before-you-upgrade.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Upgrade", "Migration"]
---

# Before you upgrade

Fulfill these requirements before you upgrade IDM, especially before upgrading the software in a production environment. Also refer to the requirements listed in [Before you install](../release-notes/before-you-install.html) and the changes listed in [Changed functionality](../release-notes/changed-functionality.html).

Before you start, verify that you have a supported Java version installed:

**Supported Java Versions**

| Vendor                                                                                                                                                                                                                                 | Versions |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| OpenJDK, including OpenJDK-based distributions:- AdoptOpenJDK/Eclipse Temurin

- Amazon Corretto

- Azul Zulu

- Red Hat OpenJDK	Ping tests most extensively with AdoptOpenJDK/Eclipse Temurin. Ping recommends using the HotSpot JVM. | 21       |
| Oracle Java                                                                                                                                                                                                                            | 21       |

If the server uses an older version that is no longer supported, install a newer Java version before you update, and follow the instructions in [Java requirements](../install-guide/verify-java.html).

Then, follow these steps:

1. Back up your existing deployment by archiving the `openidm` directory and creating a backup of the repository and all other applicable databases.

   |   |                                                                                                                                                                                                                                                                                                                                 |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you use workflow, you must manually dump the workflow database tables, and then import them *before* you start the new instance of IDM for the first time. The workflow database tables start with the prefix `ACT_`. For information on how to dump/import individual tables, refer to the documentation for your database. |

2. To save a record of the audit logs from your existing IDM installation, manually copy [the log files](../audit-guide/audit-log-topics.html#default-audit-topics) from the `/path/to/openidm/audit/` directory, before you start the upgrade.

3. Download and extract `IDM-8.1.1.zip` from the [Backstage download site](https://backstage.forgerock.com/downloads).

---

---
title: Migrate data
description: Use the PingIDM data migration service to move repository data to a new deployment when upgrading or switching to a different repository type
component: pingidm
version: 8.1
page_id: pingidm:upgrade-guide:data-migration
canonical_url: https://docs.pingidentity.com/pingidm/8.1/upgrade-guide/data-migration.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Migration", "Data"]
section_ids:
  configure-data-migration: Configure the Migration Service
  running-data-migration: Run the Data Migration
---

# Migrate data

The data migration service helps you move information stored in an IDM repository to a new deployment. You can use this service when you are upgrading to a new version, or when you are migrating to a different repository type. The migration service is off by default. To enable it, copy `migration.json` from `samples/example-configurations/conf/` into your `conf/` directory, and set `"enabled": true`.

Migration is run from your new installation through IDM's recon service, using your previous deployment as a data source. The data migration service supports importing information from IDM instances back to version 4. If you are migrating from a version of IDM earlier than that, you will need to follow previous update instructions to get your deployment into a state where it can be migrated using this service.

|   |                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Because the migration service migrates information that may be encrypted, such as passwords, you must make sure you have copied the `truststore` and `keystore` files from your previous deployment *before* you start the migration. |

The following data is imported by the migration service by default:

* Internal Roles

* Internal Users

* Internal User Metadata

* Managed Roles

* Managed Users

* Managed Assignments

* Links and Relationships

* Scheduler jobs

  |   |                                                                                                                                                                                                 |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If you are migrating scheduler jobs from IDM 4.0 or 4.5, you will need to modify the entry in `migration.json` to be:```json
  {
      "source" : "scheduler",
      "target" : "scheduler/job"
  }
  ``` |

|   |                                                                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The migration service migrates IDM repository data from one instance to a new one. If you need to migrate system objects, [define a mapping](../synchronization-guide/mappings.html) and [use reconciliation](../synchronization-guide/sync-types.html). |

If you have additional object types (for example, managed devices), modify `migration.json` to include these objects.

## Configure the Migration Service

The data migration service is configured through `migration.json`. The default file assumes a default schema; modify the file if you have added custom managed data. The `migration.json` file can have the following properties:

* enabled

  Boolean, `true` or `false`. Enables the migration service.

* connection

  Configures the connection to the source IDM instance you are migrating from. Available properties:

  * instanceUrl

    The URI for the source IDM instance.

  * authType

    The authentication mechanism to the source IDM instance. Can be `basic` (username/password) or `bearer` (authentication using AM bearer tokens).

  * userName

    Used for authenticating to the source IDM instance, if the `authType` is `basic`.

  * password

    Used for authenticating to the source IDM instance, if the `authType` is `basic`.

  * clientId

    Used for authenticating to the source IDM instance, if the `authType` is `bearer`.

  * clientSecret

    Used for authenticating to the source IDM instance, if the `authType` is `bearer`.

  * tokenEndpoint

    Used for authenticating to the source IDM instance, if the `authType` is `bearer`.

  * scope (optional)

    List of OAuth scopes.

  * scopeDelimiter (optional)

    Delimiter for the list of OAuth scopes.

  * tlsVersion (optional)

    Lets you override the default TLS version.

  * connectionTimeout (optional)

    Timeout for connecting to the source IDM instance (defaults to `10s`).

  * reuseConnections (optional)

    Lets you override the default setting (defaults to `true`).

  * retryRequests (optional)

    Lets you override the default setting (defaults to `true`).

  * hostnameVerifier (optional)

    The SSL hostname verification policy. Specifies whether the host name presented by the remote server certificate is verified upon establishing new SSL connections (defaults to `STRICT`). Possible values:

    * `STRICT` : Requires that the host name match the host name presented in the certificate. Wild-cards only match a single domain.

    * `ALLOW_ALL` : Accepts any host name (disables host name verification).

  * maxConnections (optional)

    Lets you override the default maximum number of connections (default is `64`).

  * proxy (optional)

    Lets you specify connection through a proxy server. Includes the following properties:

    * `proxyUri`

      The proxy host and port to which IDM should connect.

    * `userName`

      The user account to connect to the remote proxy.

    * `password`

      The password of the proxy user.

  * socketTimeout

    The TCP socket timeout, when waiting for HTTP responses. If you do not set a duration, the default is no timeout.

    Example valid duration values:

    * 4 days

    * 59 minutes and 1 millisecond

    * 1 minute and 10 seconds

    * 42 millis

    * unlimited

    * none

    * zero

* mappings

  A list of the endpoints that will be migrated from your old IDM instance to your new instance, expressed as mappings between the old and new instances. The complete list of mapping properties is the same as any regular [synchronization mapping](../synchronization-guide/synchronization-ref.html#sync-object-mapping). Properties with particular significance for data migration include the following:

  * allowEmptySourceSet

    Specifies whether the migration service should continue if it encounters an empty source mapping. This is enabled by default.

  * correlationQuery

    You can specify a custom correlation query. By default, this is:

    ```javascript
    "var map = {'_queryFilter': '_id eq \"' + source._id + '\"'}; map;"
    ```

    For more information about writing correlation queries, refer to [Correlate source objects with existing target objects](../synchronization-guide/chap-correlation.html).

  * enableLinking

    Specifies whether links are maintained between source and target objects. If `enableLinking` is set to `false`, links are not maintained. This is the default behavior for the migration service, where it is expected that you will run the migration only once. If you intend to run the migration more than once, set this parameter to `true`.

  * onCreate

    The script used by the migration service for creating the data that is being migrated to the new installation. By default, this points to a Groovy script: `update/mapLegacyObject.groovy`.

  * onUpdate

    The script used by the migration service for updating the data that is being migrated in the new installation. By default, this points to a Groovy script: `update/mapLegacyObject.groovy`.

  * policies

    An array of policies to apply to the data being migrated.

  * properties

    An array of properties to perform additional actions on, such as modifying the contents of a property during the migration. This follows the pattern you would find in a standard reconciliation. For more information about transforming data during a reconciliation, refer to [Transform Attributes in a Mapping](../synchronization-guide/mapping-transforming-attributes.html).

  * reconSourceQueryPageSize

    Specifies the number of results to return per page, if paging is turned on. By default, 1000 results per page are returned.

  * reconSourceQueryPaging

    Specifies whether the migration service should use paging when querying the source IDM instance. By default, this is set to `false`. Turn paging on if you have a large data set and are concerned about memory usage.

    For large data sets, you might be able to improve migration performance by turning paging on and increasing the query page size (using `reconSourceQueryPageSize`). The most effective page size will vary, depending on the available resources.

  * runTargetPhase

    Specifies whether the migration should run the target phase of reconciliation. By default, this is set to `false` as there is no data in the target repository.

  * source

    This is the only property that is *required* for data migration. The source should be the path to the resource within the repo; for example, `repo/managed/user`.

    |   |                                                                                                                                                                                                                                                                   |
    | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | By default, the migration services use the `repo` endpoint, rather than the `managed` endpoint for both the `source` and the `target`. Create, read, update, and delete operations will therefore not trigger an implicit synchronization to the target resource. |

  * sourceQuery

    The query on the source system, used to find all objects to be migrated. Defaults to `"_queryFilter" : "true&fields=_id"`, which returns the IDs of all source objects.

    You can improve migration performance by returning the whole source entry (setting the `sourceQuery` to `"_queryFilter" : "true"`).

    |   |                                                                                                                                                                                              |
    | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | If you are migrating from IDM 6.5.xAny explicitly mapped resource coming from `repo/<mappingName>` must include:```json
    "sourceQuery": {
        "_queryFilter": "true",
        "_fields": ""
    }
    ``` |

  * sourceQueryFullEntry

    (Optional). Specifies whether the defined source query returns full object data (`true`) or IDs only (`false`). Defaults to `true`.

    If you do not set this parameter, IDM attempts to detect whether the full object is returned, based on the query results.

  * target

    The path to the resource within the target repository. By default, this will be the same as the source path.

  * validSource

    You can specify a script to validate the source object prior to migration. By default, this property is empty.

* endpoint

  By default, the migration service endpoint is `migration`. You can use the `endpoint` property to change this if needed.

|   |                                                                                                                                                                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Because the data migration service performs a reconciliation between your old installation and your new installation, the general reconciliation optimizations also apply to the data migration service. For more information about reconciliation optimization, refer to [Tuning reconciliation performance](../synchronization-guide/chap-performance.html). |

## Run the Data Migration

Before you run your migration, make sure that you have done the following:

* Paused any scheduled jobs on the source deployment.

* Configured your `conf/migration.json` and `update/mapLegacyObject.groovy` files on the new IDM installation.

* Moved your configuration files from the old deployment to the new one.

* If you use workflow, you must manually dump the workflow database tables, and then import them *before* you start the new instance of IDM for the first time. The workflow database tables start with the prefix `ACT_`. For information on how to dump/import individual tables, refer to the documentation for your database.

When you launch the new IDM installation, a new `migration` endpoint should be available. This endpoint supports the following actions:

* `migrate`: Triggers a migration of all legacy objects from the remote system. Optionally takes a `mapping` parameter in order to specify a specific mapping to migrate. For example:

  ```
  curl \
  --header "X-OpenIDM-Username: openidm-admin" \
  --header "X-OpenIDM-Password: openidm-admin" \
  --header "Accept-API-Version: resource=1.0" \
  --request POST \
  "http://localhost:8080/openidm/migration?_action=migrate&mapping=repoManagedUser_repoManagedUser"
  ```

* `status`: Returns the last status for all reconciliations triggered by the migration service.

* `mappingConfigurations`: Returns the full list of migration mapping configurations.

* `mappingNames`: Returns the list of migration mapping names.

The period of time a migration takes will depend on the amount of information being migrated. Migrated data will retain the same object IDs they had in the previous deployment.

|   |                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------ |
|   | If requests sent to the source server include an `X-Requested-With` header, the value of the header will be set to `RemoteIDMProxy`. |

---

---
title: Migrate your configuration
description: Manually migrate PingIDM configuration files, scripts, security settings, and property files to a new installation
component: pingidm
version: 8.1
page_id: pingidm:upgrade-guide:migrate-config
canonical_url: https://docs.pingidentity.com/pingidm/8.1/upgrade-guide/migrate-config.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Migration", "Configuration", "Security", "Scripts", "Property Files"]
section_ids:
  migrate-config-files: Migrate configuration files
  update-boot-properties: Migrate boot.properties
  update-security: Migrate security settings
  update-scripts: Migrate custom scripts
  migrate-bundles: Migrate custom bundles
  update-provisioner-files: Migrate provisioner files
  updating-custom-ui: Migrate UI customizations
  updating-logback: Migrate logging functionality
  updating-jetty: Migrate Jetty configuration files
  updating-workflow-vue3: Migrate workflows to Vue 3
---

# Migrate your configuration

This chapter covers the steps required to migrate your IDM configuration to IDM 8.1.

There is no automated way to migrate a customized configuration to IDM 8.1, so you must migrate customized configuration files manually. If you're upgrading from IDM 8.0.x, there are three ways to do this:

* Use the new IDM 8.1 configuration files as a base, and copy any customizations you have made to the new files.

  This is the preferred option, particularly if you have used version control on your configuration and can determine the exact changes you have applied.

* Use your existing configuration files as a base, and add any new IDM 8.1 configuration to your existing files.

* Use your existing configuration as is with no IDM 8.1 changes.

Usually, a customized IDM 8.0.x configuration will work without further modification on IDM 8.1.

## Migrate configuration files

For customized files in your project's `conf/` directory, check that the customizations are compatible with the changes outlined in [Changed functionality](../release-notes/changed-functionality.html). If there are no incompatible changes, either copy your old configuration files to your IDM 8.1 installation, or copy any customization into the corresponding new configuration files.

|   |                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you create custom configuration files, don't use spaces or special characters in the filenames, in accordance with the [OSGi specification](https://docs.osgi.org/specification/osgi.core/8.0.0/framework.service.html#i3043166). |

## Migrate `boot.properties`

On the IDM 8.1 installation, edit the `resolver/boot.properties` file to match any customizations that you made on your IDM 8.0.x server. Specifically, check the following elements:

* The HTTP, HTTPS, and mutual authentication ports.

  If you changed the default ports in your IDM 8.0.x deployment, make those same changes in the new `boot.properties` file.

* Check that the keystore and truststore passwords match the current passwords for the keystore and truststore of your existing IDM deployment.

## Migrate security settings

Copy the contents of your IDM 8.0.x `security/` folder to the IDM 8.1 installation.

|   |                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you don't copy your old truststore and keystore files to your new instance, you cannot decrypt anything that was encrypted by your old instance of IDM. |

## Migrate custom scripts

Migrate any custom scripts or default scripts *that you have modified* to the `script` directory of your IDM 8.1 instance. In general, custom and customized scripts should be located in the `openidm/script` directory of your existing IDM deployment.

For custom scripts, review [Changed functionality](../release-notes/changed-functionality.html). If you're confident that the scripts will work as intended on IDM 8.1, copy these scripts to the new instance.

If you modified a default IDM script, compare the default versions of the IDM 8.0.x and IDM 8.1 scripts. If nothing has changed between the default versions, review your customizations against [Changed functionality](../release-notes/changed-functionality.html). If a default script has changed since the IDM 8.0.x release, test that your customizations work with the new default script. If you are confident that your changes will work as intended on the new version, copy the customized scripts to the new `script` directory.

|   |                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------- |
|   | If you modify any shell scripts, such as `startup.sh`, you must migrate your changes manually to the new version of the script. |

## Migrate custom bundles

If your existing deployment includes any custom JAR files in the `bundles` directory, migrate these to the new deployment. Pay particular attention to any files that support JDBC database drivers.

## Migrate provisioner files

Change any customized provisioner configurations in your existing deployment to point to the connectors that are provided with IDM 8.1. Specifically, make sure that the `connectorRef` properties reflect the new connector versions, where applicable. For example:

```json
"connectorRef" : {
    "bundleName": "org.forgerock.openicf.connectors.ldap-connector",
    "bundleVersion": "[1.4.0.0,1.6.0.0)",
    "connectorName": "org.identityconnectors.ldap.LdapConnector"
},
```

Alternatively, copy the connector .jar files from your existing deployment into the `openidm/connectors` directory of the new installation.

## Migrate UI customizations

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Starting with IDM 8.1, the [legacy admin UI is deprecated](../release-notes/deprecated-functionality.html#legacy-admin-ui-deprecated) and is no longer bundled with IDM. New deployments should use the [Platform admin UI](../setup-guide/platform-admin-ui.html), which is the replacement for the legacy admin UI.Both UIs are available as separate downloads from the [Backstage download site](https://backstage.forgerock.com/downloads):- To install the Platform admin UI, follow the steps in [Install the Platform admin UI for standalone IDM](../setup-guide/platform-admin-ui.html).

- To continue using the legacy admin UI, follow the steps in [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html). |

If you have customized the admin UI, review any custom UI files from your previous IDM deployment (generally in the `openidm/ui/admin/extension` directory), and compare them against the corresponding IDM 8.1.1 files from the legacy admin UI artifact, and make changes, as needed.

Learn more in [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html).

## Migrate logging functionality

For customized logging behavior in your project, check that the customizations are compatible with the changes outlined in [Server logs](../monitoring-guide/server-logs.html). Update your `conf/logback.xml` file with any necessary changes.

If you want to preserve the JUL style logs, learn more in [pattern layout encoder](../monitoring-guide/server-logs.html#pattern-layout-encoder).

## Migrate Jetty configuration files

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In IDM 8.0, `jetty.xml` is no longer supported.When serving SSL requests, Jetty 12 checks that the incoming host header matches the server certificate's subject and returns a `400 Bad Request` error on a mismatch. If you're upgrading to IDM 8.0, you must ensure your IDM server certificate subject matches the host name used by your deployment.Learn more in [Jetty 12 support](../release-notes/whats-new.html#jetty_12_support). |

If you haven't modified your `jetty.xml` configuration file, you don't need to make changes for Jetty 12 because the current configuration replicates the `jetty.xml` default settings. However, if you've made changes, you might need to adjust the `webserver.listener-*json` files as needed.

For example, the `webserver.listener-mutualAuth.json` file duplicates the `8444` port configuration in `jetty.xml`. You can enable mutual authentication on any listener by setting the `secure` and `mutualAuth` flags to `true`.

Learn more in [Embedded Jetty configuration](../install-guide/appendix-jetty.html) and in [Secure network connections](../security-guide/chap-connections.html).

## Migrate workflows to Vue 3

If you have custom workflow form templates, review them for compatibility with Vue 3. The end-user UI no longer registers `ValidationObserver`, `ValidationProvider`, or the `$set()` reactivity API globally. You must update any templates that depend on these.

Learn more in [Update custom workflow templates for Vue 3](../workflow-guide/custom-workflow-template.html#vue3-workflow-migration).

---

---
title: Update the repository
description: Update the PingIDM repository after a configuration migration by upgrading the existing repository in place or creating and migrating to a new one
component: pingidm
version: 8.1
page_id: pingidm:upgrade-guide:update-repo
canonical_url: https://docs.pingidentity.com/pingidm/8.1/upgrade-guide/update-repo.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Upgrade", "Repository"]
section_ids:
  upgrade-existing-repository: Upgrade an existing repository
  create-new-repository: Create a new repository
---

# Update the repository

When you have migrated your configuration to the new IDM installation, you need to handle the data that is stored in your repository. There are two options to update a repository:

* [Upgrade your existing IDM repository](#upgrade-existing-repository).

* [Create a new IDM 8.1 repository](#create-new-repository), then migrate your data to the new repository.

When you have upgraded the repository, or created a new repository, start the IDM server and test that all your scripts are working as expected, before migrating your data.

## Upgrade an existing repository

Upgrading an existing repository means that you do not need to migrate data. However, you must run a series of scripts that modify the repository, to use the new features in IDM 8.1. You should also review [Changed functionality](../release-notes/changed-functionality.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Because the repository upgrade scripts are incremental, you must review each major version upgrade after your current release. For example, when upgrading from 6.5.x to 8.1.x, review the upgrade process and scripts for 7.0.x, 7.1.x, 7.2.x, 7.3.x, 7.4.x, 7.5.x, 8.0.x, and 8.1.x (this version).Repository upgrade procedures:- [Upgrade an existing repository (7.0.x)](https://backstage.forgerock.com/docs/idm/7/upgrade-guide/update-repo.html#upgrade-existing-repository)

- [Upgrade an existing repository (7.1.x)](https://backstage.forgerock.com/docs/idm/7.1/upgrade-guide/update-repo.html#upgrade-existing-repository)

- [Upgrade an existing repository (7.2.x)](https://docs.pingidentity.com/pingidm/7.2/upgrade-guide/update-repo.html#upgrade-existing-repository)

- [Upgrade an existing repository (7.3.x)](https://docs.pingidentity.com/pingidm/7.3/upgrade-guide/update-repo.html#upgrade-existing-repository)

- [Upgrade an existing repository (7.4.x)](https://docs.pingidentity.com/pingidm/7.4/upgrade-guide/update-repo.html#upgrade-existing-repository)

- [Upgrade an existing repository (7.5.x)](https://docs.pingidentity.com/pingidm/7.5/upgrade-guide/update-repo.html#upgrade-existing-repository)

- [Upgrade an existing repository (8.0.x)](https://docs.pingidentity.com/pingidm/8/upgrade-guide/update-repo.html#upgrade-existing-repository) |

Prepare an existing repository for IDM 8.1 as follows:

1. Shut down IDM, if it is running.

2. Clear all `configobjects` related tables. For example, in MySQL run:

   ```sql
   DELETE FROM openidm.configobjects;
   DELETE FROM openidm.configobjectproperties;
   ```

3. If you are using workflow, you must run the Flowable upgrade scripts for your database type. These upgrade scripts are incremental and must be run in order, starting with the correct script based on your current Flowable version.

   1. To determine your current Flowable version, check the `/path/to/openidm/bundle/flowable-engine-versionNumber.jar` file in your old IDM installation.

      |   |                                                                                                  |
      | - | ------------------------------------------------------------------------------------------------ |
      |   | If your current Flowable version is `7.2.0`, you don't need to run any Flowable upgrade scripts. |

   2. Run the upgrade scripts from `/path/to/openidm/db/database-type/scripts/updates/` in order, starting with your current Flowable version:

      1. `flowable.database-type.upgradestep.6.6.0.to.6.7.0.all.sql`

      2. `flowable.database-type.upgradestep.6.7.0.to.6.7.1.all.sql`

      3. `flowable.database-type.upgradestep.6.7.1.to.6.7.2.all.sql`

      4. `flowable.database-type.upgradestep.6.7.2.to.6.8.0.all.sql`

      5. `flowable.database-type.upgradestep.6.8.0.to.7.0.0.all.sql`

      6. `flowable.database-type.upgradestep.7.0.0.to.7.0.1.all.sql`

      7. `flowable.database-type.upgradestep.7.0.1.to.7.1.0.all.sql`

      8. `flowable.database-type.upgradestep.7.1.0.to.7.2.0.all.sql`

4. Optionally, for PostgreSQL repositories only, you can activate database-level protection against duplicate relationship table entries:

   1. Run the upgrade script `/path/to/openidm/db/postgresql/scripts/updates/00-relationship-uniqueness.pgsql`.

   2. If the script returns an error, you must locate and remove existing duplicate entries. For example:

      Locate duplicates

      ```sql
      WITH ids_and_properties AS (
          SELECT
              id,
              jsonb_extract_path(fullobject, 'properties') AS properties
          FROM
              relationships
      )
      SELECT
          MIN(r.id) AS first_relationship_id,
          r.firstresourcecollection,
          r.firstresourceid,
          r.firstpropertyname,
          r.secondresourcecollection,
          r.secondresourceid,
          r.secondpropertyname,
          iap.properties
      FROM
          relationships r
          JOIN ids_and_properties iap ON iap.id = r.id
      GROUP BY
          r.firstresourcecollection,
          r.firstresourceid,
          r.firstpropertyname,
          r.secondresourcecollection,
          r.secondresourceid,
          r.secondpropertyname,
          iap.properties
      HAVING
          COUNT(*) > 1;
      ```

   3. Delete the duplicate entries. Refer to your [database documentation](https://www.postgresql.org/docs/17/sql-delete.html) to learn more about deleting table entries.

   4. Run the upgrade script `/path/to/openidm/db/postgresql/scripts/updates/00-relationship-uniqueness.pgsql` again.

5. For Oracle UCP only, make the following changes to your `conf/datasource.jdbc-ucp-oracle.json` file:

   1. Update the JDBC URL format from the deprecated SID format (`@host:port:SID`) to the service name format (`@//host:port/service_name`).

   2. Replace the property `connectionTimeout` (in milliseconds) with `connectionWaitTimeout` (in seconds).

   Learn more in [Set up Oracle as an IDM repository](../install-guide/repository-oracledb.html#oracle-ucp-datasource).

6. Optionally, for DB2 explicit mappings only, you can increase the column size for `activedate` and `inactivedate` in the managed user table. Run the upgrade script `/path/to/openidm/db/db2/scripts/updates/00-explicit-table-increase-date-column-size.sql`.

   This script alters the `activedate` and `inactivedate` columns in the `MANAGED_USER` table from `VARCHAR(29)` to `VARCHAR(35)`, increasing compatibility with certain long date formats.

7. Launch IDM and run the following Groovy script to clear the `reconprogressstate` data in your repository:

   ```groovy
   def result = openidm.query(
     "repo/reconprogressstate", [ "_queryFilter" : "true", "_fields" : "_id" ]).result;
   for ( item in result ) {
     openidm.delete("repo/reconprogressstate/" + item["_id"], null);
   }
   return result.size() + " reconprogressstate records deleted";
   ```

   This script works for all repository types and can be sent as a REST call. For example:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Content-Type: application/json" \
   --request POST \
   --data '{
     "type":"groovy",
     "source":"def result = openidm.query(\"repo/reconprogressstate\", [ \"_queryFilter\" : \"true\", \"_fields\" : \"_id\" ]).result; for ( item in result ) { openidm.delete(\"repo/reconprogressstate/\" + item[\"_id\"], null); }; return result.size() + \" reconprogressstate records deleted\";"
   }' \
   "http://localhost:8080/openidm/script?_action=eval"
   "1 reconprogressstate records deleted"
   ```

8. Verify that all scripts and functions behave as expected.

## Create a new repository

1. Set up a new repository, following the steps in [Select a repository](../install-guide/chap-repository.html). A new repository is already configured for all the new capabilities in IDM, but does require migrating existing data to that repository.

   If you create a new repository, you must still update your configuration files to use the new features.

2. After you have set up the new repository, [migrate your data](data-migration.html) to that repository.

---

---
title: Update to a maintenance release
description: Upgrade a PingIDM 8.1.x deployment to the latest maintenance release
component: pingidm
version: 8.1
page_id: pingidm:upgrade-guide:update-maintenance-release
canonical_url: https://docs.pingidentity.com/pingidm/8.1/upgrade-guide/update-maintenance-release.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Upgrade", "Maintenance"]
---

# Update to a maintenance release

The [maintenance releases](../release-notes/whats-new.html#maintenance-releases) incorporate a collection of fixes and minor enhancements. IDM 8.1.1 is the latest maintenance release for IDM 8.1. To upgrade an existing IDM 8.1.x deployment, follow these steps:

1. Download and extract the IDM 8.1.1 binary from the [Backstage download site](https://backstage.forgerock.com/downloads).

2. Copy any customized configuration files, scripts, or workflow definitions from your existing deployment to the comparable directory in your 8.1.1 deployment.

3. If you're still running an earlier version of IDM 8.1.x, copy the `conf/authentication.json` file from your existing deployment to the `conf/` directory in your 8.1.1 deployment.

4. Copy the keystore and truststore from your existing deployment to the 8.1.1 deployment. For example:

   ```bash
   cp -r /path/to/openidm81x/security /path/to/openidm811
   ```

5. Configure the IDM 8.1.1 server to point to your existing repository:

   * If you're using an external DS repository, verify the accuracy of the `conf/repo.ds.json` file in your new deployment.

   * If you're using a JDBC repository, verify the accuracy of the following files in your new deployment:

     * `conf/repo.jdbc.json`

     * `conf/datasource.jdbc-default.json`

     * `resolver/boot.properties` (particularly the values for `openidm.repo.host` and `openidm.repo.port`)

6. If you're using workflow, you must run the Flowable upgrade scripts for your database type. These upgrade scripts are incremental and must be run in order, starting with the correct script based on your current Flowable version.

   1. To determine your current Flowable version, check the `/path/to/openidm/bundle/flowable-engine-versionNumber.jar` file in your old IDM installation.

      |   |                                                                                                  |
      | - | ------------------------------------------------------------------------------------------------ |
      |   | If your current Flowable version is `7.2.0`, you don't need to run any Flowable upgrade scripts. |

   2. Run the upgrade scripts from `/path/to/openidm/db/database-type/scripts/updates/` in order, starting with your current Flowable version:

      1. `flowable.database-type.upgradestep.6.6.0.to.6.7.0.all.sql`

      2. `flowable.database-type.upgradestep.6.7.0.to.6.7.1.all.sql`

      3. `flowable.database-type.upgradestep.6.7.1.to.6.7.2.all.sql`

      4. `flowable.database-type.upgradestep.6.7.2.to.6.8.0.all.sql`

      5. `flowable.database-type.upgradestep.6.8.0.to.7.0.0.all.sql`

      6. `flowable.database-type.upgradestep.7.0.0.to.7.0.1.all.sql`

      7. `flowable.database-type.upgradestep.7.0.1.to.7.1.0.all.sql`

      8. `flowable.database-type.upgradestep.7.1.0.to.7.2.0.all.sql`

7. Shut down your existing IDM 8.1.x server.

8. Start your IDM 8.1.1 server.

---

---
title: Upgrade
description: This guide shows you how to upgrade an existing deployment to the latest PingIDM release
component: pingidm
version: 8.1
page_id: pingidm:upgrade-guide:preface
canonical_url: https://docs.pingidentity.com/pingidm/8.1/upgrade-guide/preface.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Upgrade"]
page_aliases: ["index.adoc"]
---

# Upgrade

> This guide shows you how to upgrade an existing deployment to the latest PingIDM release.

Quick Start

[icon: cogs, set=fad, size=3x]

#### [Migrate Configuration](migrate-config.html)

Migrate an existing IDM configuration to IDM 8.1.

[icon: database, set=fad, size=3x]

#### [Update Repository](update-repo.html)

Update an existing repository or install a new repository for IDM 8.1.

[icon: users, set=fad, size=3x]

#### [Migrate Data](data-migration.html)

Move the data in an existing IDM repository to an updated deployment.

The upgrade process is largely dependent on your deployment and on the extent to which you have customized IDM. Engage [Ping Support Services](https://www.forgerock.com/support/support-services) for help in upgrading an existing deployment. Also, read the [Release notes](../release-notes/preface.html) before you start an upgrade; specifically, [Changed functionality](../release-notes/changed-functionality.html).

---

---
title: Upgrade a clustered deployment
description: Upgrade a PingIDM clustered deployment by redirecting traffic, shutting down nodes, updating one node, and cloning it to remaining cluster nodes
component: pingidm
version: 8.1
page_id: pingidm:upgrade-guide:upgrade-cluster
canonical_url: https://docs.pingidentity.com/pingidm/8.1/upgrade-guide/upgrade-cluster.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Upgrade", "Cluster"]
---

# Upgrade a clustered deployment

Follow these general steps when you are updating servers in a cluster:

1. Redirect client traffic to a different IDM system or cluster.

2. Shut down every node in the cluster.

3. Update one node in the cluster.

4. Clone the first node to the other nodes in that cluster.