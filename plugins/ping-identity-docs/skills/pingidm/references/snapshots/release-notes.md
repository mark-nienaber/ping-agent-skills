---
title: Before you install
description: Hardware, OS, Java, repository, browser, and connector requirements for running PingIDM in production
component: pingidm
version: 8.1
page_id: pingidm:release-notes:before-you-install
canonical_url: https://docs.pingidentity.com/pingidm/8.1/release-notes/before-you-install.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Deployment", "Identities", "Compatibility", "Security", "Java", "Browser", "Connectors"]
section_ids:
  prerequisites-hardware: Hardware and memory requirements
  change-jvm-heap: Change the JVM heap size
  prerequisites-os: Operating System requirements
  prerequisites-java: Java requirements
  prerequisites-container: Supported web application containers
  prerequisites-repositories: Supported repositories
  prerequisites-clients: Supported browsers
  prerequisites-connectors: Supported connectors
  prerequisites-plugins: Supported password synchronization plugins
---

# Before you install

This topic covers requirements before you run PingIDM software.

## Hardware and memory requirements

Due to the underlying Java platform, IDM software runs well on a variety of processor architectures.

To run IDM for evaluation, you need at least:

* 256 MB memory (32-bit) or 1 GB memory (64-bit) available.

* 10 GB free disk space for the software and sample data.

|   |                                                                                                                                                                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | A DS repository requires free disk space of 5% of the filesystem size, plus 1 GB by default. To change this requirement, set the `disk-full-threshold` in the DS configuration. Learn more about [Disk Space Thresholds](https://docs.pingidentity.com/pingds/8.1/config-guide/import-export.html#set-database-backend-disk-thresholds) in the DS documentation. |

In production, disk space and memory requirements depend on the size of your external repository, as well as the size of the audit and service log files that IDM creates.

The amount of memory that IDM consumes is highly dependent on the data that it holds. Queries that return large data sets will have a significant impact on heap requirements, particularly if they are run in parallel with other large data requests. To avoid out-of-memory errors, analyze your data requirements, set the heap configuration appropriately, and modify access controls to restrict requests on large data sets.

IDM exposes many JVM metrics to help you analyze the amount of memory that it is consuming. For more information on analyzing hardware and memory performance, see [Load testing](../monitoring-guide/load-testing.html).

### Change the JVM heap size

Changing the JVM heap size can improve performance and reduce the time it takes to run reconciliations.

You can set the JVM heap size via the `OPENIDM_OPTS` environment variable. If `OPENIDM_OPTS` is undefined, the JVM maximum heap size defaults to 2GB. For example, to set the minimum and maximum heap sizes to 4GB, enter the following before starting IDM:

* Unix/Linux

* Windows

```
cd /path/to/openidm/
export OPENIDM_OPTS="-Xms4096m -Xmx4096m"
./startup.sh
Using OPENIDM_HOME:   /path/to/openidm
Using PROJECT_HOME:   /path/to/openidm
Using OPENIDM_OPTS:   -Xms4096m -Xmx4096m
...
OpenIDM ready
```

```
cd \path\to\openidm
set OPENIDM_OPTS=-Xms4096m -Xmx4096m
startup.bat
"Using OPENIDM_HOME:   \path\to\openidm"
"Using PROJECT_HOME:   \path\to\openidm"
"Using OPENIDM_OPTS:   -Xms4096m -Xmx4096m -Dfile.encoding=UTF-8"
...
OpenIDM ready
```

You can also edit the `OPENIDM_OPTS` values in `startup.sh` or `startup.bat`.

|   |                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------ |
|   | For more information about tuning and load testing, refer to [Load testing](../monitoring-guide/load-testing.html) |

## Operating System requirements

IDM 8.1 software is supported on actively maintained versions of the following operating systems:

* Amazon Linux

* Debian

* Red Hat Enterprise Linux

* Rocky Linux

* SUSE Linux Enterprise

* Ubuntu Linux

* Windows Server 2019 and 2022

## Java requirements

IDM software supports the following Java environments:

**Supported Java Versions**

| Vendor                                                                                                                                                                                                                                 | Versions |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| OpenJDK, including OpenJDK-based distributions:- AdoptOpenJDK/Eclipse Temurin

- Amazon Corretto

- Azul Zulu

- Red Hat OpenJDK	Ping tests most extensively with AdoptOpenJDK/Eclipse Temurin. Ping recommends using the HotSpot JVM. | 21       |
| Oracle Java                                                                                                                                                                                                                            | 21       |

|   |                                                                                            |
| - | ------------------------------------------------------------------------------------------ |
|   | Ping recommends you keep your Java installation up-to-date with the latest security fixes. |

## Supported web application containers

You must install IDM as a standalone service, using the bundled Apache Felix framework and Jetty web application container. Alternate containers are not supported. IDM bundles Jetty version 12.0.25.

## Supported repositories

The following repositories are supported for use in production:

| Repository                                                                                                    | Supported versions                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| PingDS (DS)                                                                                                   | 8.1                                                                                  |
| MySQL                                                                                                         | 8.4, 9.6Requires MySQL JDBC Driver Connector/J 8.0[\*](#connector-j-version-note).   |
| MariaDB                                                                                                       | 11.4, 11.8Requires MySQL JDBC Driver Connector/J 8.0[\*](#connector-j-version-note). |
| Microsoft SQL Server                                                                                          | 2022, 2025                                                                           |
| Oracle Database                                                                                               | 19c, 26ai                                                                            |
| PostgreSQL                                                                                                    | 17, 18                                                                               |
| IBM DB2                                                                                                       | 11.5, 12.1                                                                           |
| \* []()Don't use Connector/J versions 8.0.23 through 8.0.25. [Why?](https://bugs.mysql.com/bug.php?id=102372) |                                                                                      |

IDM supports repositories in cloud-hosted environments, such as AWS and GKE Cloud, as long as the underlying repository is supported.

|   |                                                                                                                                                                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | These repositories might not be supported on all operating system platforms. Refer to the specific repository documentation for more information.Do not mix and match versions. For example, if you are running Oracle Database 21c, and want to take advantage of the support for Oracle UCP, download driver and companion JARs for Oracle version 21c. |

## Supported browsers

The IDM UI has been tested with the latest, stable versions of the following browsers:

* Chrome and Chromium

* Edge

* Firefox

* Safari

## Supported connectors

For a complete list of IDM bundled connectors, check out [Available connectors](https://docs.pingidentity.com/openicf/index.html#available_connectors).

The Java RCS is supported on the following Java versions:

**Java version support**

| Java RCS version            | Supported Java version |
| --------------------------- | ---------------------- |
| 1.5.20.22 and earlier       | Java 11 or 17          |
| 1.5.20.23 through 1.5.20.31 | Java 17                |
| 1.5.20.32 and later         | Java 17 or 21          |

|   |                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Although the scripted connector toolkits are supported, connectors that you build with these toolkits are not supported. You can find examples of how to build connectors with these toolkits in [Samples](../samples-guide/preface.html). |

Check out the [ICF release notes](https://docs.pingidentity.com/openicf/connector-release-notes/preface.html) for the latest connector and RCS updates.

**IDM / ICF Compatibility Matrix**

| IDM Version | RCS Version | Java Connectors               | Scripted Groovy Connectors                                           | .NET Connectors            |
| ----------- | ----------- | ----------------------------- | -------------------------------------------------------------------- | -------------------------- |
| 7.x         | 1.5.x       | Java connectors version 1.5.x | Scripted REST, Scripted SQL, SSH, Kerberos connectors version 1.5.x. | PowerShell Connector 1.5.x |
| 8.x         | 1.5.x       | Java connectors version 1.5.x | Scripted REST, Scripted SQL, SSH, Kerberos connectors version 1.5.x. | PowerShell Connector 1.5.x |

|   |                                                                                                    |
| - | -------------------------------------------------------------------------------------------------- |
|   | Ping recommends you keep your RCS installation and connectors up-to-date with the latest versions. |

## Supported password synchronization plugins

The following table lists the supported password synchronization plugins:

| Plugin                                           | Supported Version                            |
| ------------------------------------------------ | -------------------------------------------- |
| DS Password Synchronization Plugin               | 8.1.x, supported with DS 8.1.x and IDM 8.1.x |
| Active Directory Password Synchronization Plugin | 1.8.0 supported on Windows Server 2022       |

---

---
title: Changed functionality
description: Compatibility-breaking changes across PingIDM releases to review before upgrading an existing deployment
component: pingidm
version: 8.1
page_id: pingidm:release-notes:changed-functionality
canonical_url: https://docs.pingidentity.com/pingidm/8.1/release-notes/changed-functionality.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Deployment", "Identities", "Compatibility", "Security", "JSON"]
section_ids:
  changes_between_idm_8_1_0_and_8_1_1: Changes between IDM 8.1.0 and 8.1.1
  changes_between_idm_8_0_x_and_8_1_0: Changes between IDM 8.0.x and 8.1.0
  changed-admin-ui-removed-from-zip-810: Legacy admin UI and API Explorer removed
  changed-workflow-vue3-810: Custom workflow templates require Vue 3 updates
  changed-oracle-ucp-template-810: Oracle UCP datasource changes
  changed-workflow-upgrade-720-810: Workflow engine upgrade
  java_21_support: Java 21 support
  queued_synchronization_property_changes: Queued synchronization property changes
  default_api_version_for_unversioned_requests: Default API version for unversioned requests
  deprecated_metric_collection: Deprecated metric collection
  router_filter_metric_names: Router filter metric names
  jetty_metrics_for_number_of_queued_requests: Jetty metrics for number of queued requests
  scripted_endpoint_metric_names: Scripted endpoint metric names
  livesync_metric_tag_and_naming_updates: liveSync metric tag and naming updates
  managed_object_script_hook_naming_updates: Managed object script hook naming updates
  changes_between_idm_8_0_1_and_8_0_2: Changes between IDM 8.0.1 and 8.0.2
  changed-oracle-ucp-template-802: Oracle UCP datasource changes
  changes_between_idm_8_0_0_and_8_0_1: Changes between IDM 8.0.0 and 8.0.1
  default_api_version_for_unversioned_requests_2: Default API version for unversioned requests
  changes_between_idm_7_5_x_and_8_0_0: Changes between IDM 7.5.x and 8.0.0
  launcher_json_configuration: launcher.json configuration
  embedded_jetty_web_server_upgrade: Embedded Jetty web server upgrade
  felix_http_jetty_upgrade: Felix HTTP Jetty upgrade
  servlet_specification_upgrade: Servlet Specification upgrade
  jetty_thread_pool_settings: Jetty thread pool settings
  gzip_compression_settings: Gzip compression settings
  secure_protocol_configuration: Secure protocol configuration
  embedded_ds_repository: Embedded DS repository
  logback: Logback
  standalone_end_user_ui_not_bundled_with_pingidm: Standalone end-user UI not bundled with PingIDM
  changed-parameter-authorization-80: _api parameter requires authorization
  changed-array-comparison-80: Array comparison
  java_21_support_2: Java 21 support
  changes_between_idm_7_5_2_and_7_5_3: Changes between IDM 7.5.2 and 7.5.3
  changed-oracle-ucp-template-753: Oracle UCP datasource changes
  changes_between_idm_7_5_1_and_7_5_2: Changes between IDM 7.5.1 and 7.5.2
  default_api_version_for_unversioned_requests_3: Default API version for unversioned requests
  changes_between_idm_7_5_0_and_7_5_1: Changes between IDM 7.5.0 and 7.5.1
  changed-parameter-authorization-751: _api parameter requires authorization
  changed-array-comparison-751: Array comparison
  changes_between_idm_7_4_x_and_7_5_0: Changes between IDM 7.4.x and 7.5.0
  changed-fx-flowable-upgrade-680-75: Workflow engine upgrade
  array_schema_fields_default_to_item_type_string: Array schema fields default to item type string
  populatedefaults_flag_removed_from_secrets_configuration: populateDefaults flag removed from secrets configuration
  java_17_required: Java 17 required
  legacy_hashing_algorithms_removed_from_the_admin_ui: Legacy hashing algorithms removed from the Admin UI
  secret_store_class_renamed: Secret store class renamed
  changes_between_idm_7_4_2_and_7_4_3: Changes between IDM 7.4.2 and 7.4.3
  default_api_version_for_unversioned_requests_4: Default API version for unversioned requests
  changes_between_idm_7_4_1_and_7_4_2: Changes between IDM 7.4.1 and 7.4.2
  changed-parameter-authorization-74: _api parameter requires authorization
  changed-array-comparison-742: Array comparison
  changed-java-support: Java upgrade
  changes_between_idm_7_4_0_and_7_4_1: Changes between IDM 7.4.0 and 7.4.1
  changed-fx-flowable-upgrade-680-74: Workflow engine upgrade
  changes_between_idm_7_3_x_and_7_4_0: Changes between IDM 7.3.x and 7.4.0
  jdk-keystore-creation: IDM requires JDK 11.0.20 or higher
  db2-driver-osgi: The DB2 driver is now OSGi-compliant
  changes_between_idm_7_3_2_and_7_3_3: Changes between IDM 7.3.2 and 7.3.3
  default_api_version_for_unversioned_requests_5: Default API version for unversioned requests
  changes_between_idm_7_3_1_and_7_3_2: Changes between IDM 7.3.1 and 7.3.2
  changed-parameter-authorization-73: _api parameter requires authorization
  changed-array-comparison-732: Array comparison
  changed-java-upgrade-732: Java upgrade
  changes_between_idm_7_3_0_and_7_3_1: Changes between IDM 7.3.0 and 7.3.1
  changed-fx-flowable-upgrade-680-73: Workflow engine upgrade
  changes_between_idm_7_2_x_and_7_3_0: Changes between IDM 7.2.x and 7.3.0
  array-order-agnostic-sync: Synchronization JSON array comparison is order-agnostic
  attribute_encryption_on_assignments: Attribute encryption on assignments
  changes_between_idm_7_1_x_and_7_2_0: Changes between IDM 7.1.x and 7.2.0
  onDelete-default-bahavior: Default onDelete behavior
  felix-osgi-upgrade: Felix and OSGi upgrades
  jms-20-upgrade: JMS 2.0 upgrade
  json-patch-exceptions: PATCH request exceptions
  policy-enforcement-on-role-name: Policy enforcement on role name
  preferredLocales-precedence: Precedence in locales in the self-registration email template
  paused-queued-sync-changed: Paused queued synchronization for unavailable routes
  embedded_workflow_database: Embedded workflow database
  default_mysql_connection_driver: Default MySQL connection driver
  changes_between_idm_7_1_4_and_7_1_6: Changes between IDM 7.1.4 and 7.1.6
  changes_between_idm_7_1_2_and_7_1_4: Changes between IDM 7.1.2 and 7.1.4
  changes_between_idm_7_1_0_and_7_1_2: Changes between IDM 7.1.0 and 7.1.2
  embedded_workflow_database_2: Embedded workflow database
  workflow_version_update: Workflow version update
  changes_between_idm_7_0_x_and_7_1_0: Changes between IDM 7.0.x and 7.1.0
  data_format_change_for_external_ds_repositories: Data format change for external DS repositories
  audit_handler_changes: Audit handler changes
  parameterized_http_and_https_enablement: Parameterized HTTP and HTTPS enablement
  parameterized_felix_web_console_credentials: Parameterized Felix web console credentials
  notification_changes: Notification changes
  moved_configuration_files: Moved configuration files
  improved_validateproperty_error_handling: Improved validateProperty error handling
  changes_to_router_json: Changes to router.json
  changes_between_idm_6_5_x_and_7_0_0: Changes between IDM 6.5.x and 7.0.0
  embedded_workflow_database_3: Embedded workflow database
  new_workflow_engine: New workflow engine
  changes_to_boot_properties: Changes to boot.properties
  changes_to_logging_properties: Changes to logging.properties
  change_to_how_authorization_roles_are_assigned: Change to how authorization roles are assigned
  schema_change_to_authzroles: Schema change to authzRoles
  change_to_the_internal_user_authentication_module: Change to the INTERNAL_USER authentication module
  change_to_prometheus_monitoring: Change to Prometheus monitoring
  change_in_how_boolean_values_are_assessed: Change in how boolean values are assessed
  queued_sync_changes: Queued sync changes
  virtual_property_calculation_for_effectiveroles_and_effectiveassignments: Virtual property calculation for effectiveRoles and effectiveAssignments
  gzip_compression_for_http_responses: Gzip compression for HTTP responses
  configurable_hashing: Configurable hashing
  temporal_constraint_enforcement_on_roles: Temporal constraint enforcement on roles
  change_to_jms_audit_handler: Change to JMS audit handler
  change_to_default_audit_configuration: Change to default audit configuration
  datatype_of_userpassword_property_in_provisioner_files: Datatype of userPassword property in provisioner files
  removal_of_the_global_consent_setting: Removal of the global consent setting
  support_for_mysql_connectorj_version_8_0: Support for MySQL Connector/J version 8.0
  default_security_protocols_for_inbound_connections: Default security protocols for inbound connections
  removal_of_address2_from_the_managed_object_schema: Removal of address2 from the managed object schema
  icf_and_connector_changes: ICF and connector changes
  archive: Archive
---

# Changed functionality

When you update to IDM 8.1.1 from the last major version, the following changes could affect existing deployments. Adjust existing scripts, files, clients, and so on, as necessary. You should also review [Deprecation](deprecated-functionality.html) notices.

If you're upgrading from an older release, review the changed functionality from all releases after your current version of IDM.

For previous releases, the information could be outdated or superseded.

## Changes between IDM 8.1.0 and 8.1.1

No additional incompatible changes were made between 8.1.0 and 8.1.1.

## Changes between IDM 8.0.x and 8.1.0

### Legacy admin UI and API Explorer removed

The legacy admin UI (`/admin`) and API Explorer (`/api`) are no longer included in the IDM `.zip` distribution. Requests to the `/admin` or `/api` endpoints on the IDM server return a `404` response.

New deployments should use the [Platform admin UI](../setup-guide/platform-admin-ui.html), which is the replacement for the legacy admin UI.

Although the legacy admin UI and API Explorer are [deprecated](deprecated-functionality.html#legacy-admin-ui-deprecated), you can still download and install the artifact separately. Learn more in [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html).

### Custom workflow templates require Vue 3 updates

The end-user UI has been upgraded from Vue 2 to Vue 3. If you have custom workflow form templates, they might require changes to work correctly.

The `ValidationObserver` and `ValidationProvider` components from `vee-validate`, which the previous UI registered globally, are no longer available. Replace them with component-local validation. The `$set()` reactivity API has also been removed in Vue 3. Use direct property assignment instead.

The sample workflow template has been updated as a reference. Learn more in [Update custom workflow templates for Vue 3](../workflow-guide/custom-workflow-template.html#vue3-workflow-migration).

### Oracle UCP datasource changes

The default Oracle UCP datasource template (`datasource.jdbc-ucp-oracle.json`) has changed:

* The JDBC URL format changed from the deprecated SID format (`@host:port:SID`) to the service name format (`@//host:port/service_name`).

* The `connectionTimeout` (in milliseconds) property is replaced with `connectionWaitTimeout` (in seconds). The old property was silently ignored by UCP.

Update your existing `conf/datasource.jdbc-ucp-oracle.json` file for these changes. Learn more in [Set up Oracle as an IDM repository](../install-guide/repository-oracledb.html#oracle-ucp-datasource).

### Workflow engine upgrade

The Flowable embedded workflow engine has been upgraded to [version 7.2.0](https://github.com/flowable/flowable-engine/releases/tag/flowable-7.2.0).

If you're upgrading from a previous version of IDM and use workflow, this upgrade requires one or more incremental [upgrade scripts](../upgrade-guide/update-repo.html#upgrade-existing-repository).

### Java 21 support

Previously, IDM supported Java 17 and Java 21. Now, running IDM requires Java 21. Learn more in [Java requirements](before-you-install.html#prerequisites-java).

### Queued synchronization property changes

The `maxQueueSize` for [queued synchronization](../synchronization-guide/chap-implicit-live-sync.html#configure-queued-sync) now defaults to `1000` and can't be configured to a value higher than `1000` or lower than `100`. The previous default was `20000`.

The `pageSize` defaults to `100` (unchanged) and can't be configured to a value higher than `100` or lower than `10`. If the configured `pageSize` is greater than `maxQueueSize / 10`, IDM uses `maxQueueSize / 10` for the page size.

If you have any configuration outside of these bounds, IDM automatically adjusts the values to the nearest bound.

### Default API version for unversioned requests

Previously, REST API requests without an `Accept-API-Version` header used the latest available API version for the resource. These requests now default to API version `1.0`. The `consent`, `scheduler/job`, `scheduler/trigger`, and `schema` endpoints default to API version `2.0`.

### Deprecated metric collection

Deprecated metric names are now generated along with the replacement metric names only when the `deprecatedMetricsEnabled` property is set to `true` (default) in `conf/metrics.json`. To generate only the replacement metric names, set the property to `false`. Learn more in [Deprecated metric collection](../monitoring-guide/monitoring.html#deprecated-metric-collection).

### Router filter metric names

Router filter metrics now use the `router-filter` ([API](../monitoring-guide/api-metrics.html#api-metric-names)) and `idm_router_filter_seconds` ([Prometheus](../monitoring-guide/prometheus-metrics.html#prometheus-metric-names)) metric names that replace the `filter` (API) and `idm_filter_seconds` (Prometheus) metric names. This metric also specifies a `name` and `system` label. If no name label is specified, it defaults to "unknown". The `system` label is always `system="false"`.

|   |                                                                                                                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The deprecated metric names are still available and are generated along with the new metric names unless `deprecatedMetricsEnabled` is set to `false` in `conf/metrics.json`. Learn more in [Deprecated metric collection](../monitoring-guide/monitoring.html#deprecated-metric-collection). |

### Jetty metrics for number of queued requests

The [Jetty QoSHandler](../install-guide/idm-config-properties-jetty.html#config-jetty-qos-handler) metrics, `jetty.qos.queue.count` (API) and `idm_jetty_qos_queue_count` (Prometheus), now contain an accurate count of queued requests and replace `jetty.thread.queue` (API) and `idm_jetty_thread_queue` (Prometheus).

### Scripted endpoint metric names

Scripted endpoint metric names are more consistent and no longer use randomly generated GUIDs for inline scripts.

* API metrics:

  The metric `script.{script-name}.{request-type}` is now `custom-endpoint.{endpoint-name}.{request-type}`.

* Prometheus metrics:

  The metric `idm_script_{script-name}_{request-type}` is now `idm_custom_endpoint_seconds{name="{endpoint-name}",request_type="{request-type}"}`.

For both metric types, `{endpoint-name}` is determined by the endpoint's configuration file name. For example, `endpoint-myendpoint.json` results in the name `myendpoint`.

|   |                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------- |
|   | If you have monitoring dashboards or other tools that rely on the old metric names, update them to use the new names. |

### liveSync metric tag and naming updates

The liveSync metric includes updated tag and naming conventions.

* [API metric](../monitoring-guide/api-metrics.html#new-livesync-metric):

  The metric `live-sync.{system-name}.{object-type}` is now `icf.{connector-type}.{system-identifier}.{bundle-version}.{location}.{object-class}.liveSync`.

* [Prometheus metric](../monitoring-guide/prometheus-metrics.html#new-live-sync-prom-metric):

  The metric `idm_live_sync_seconds{object_type="{object_type}",system_name="{system_name}",quantile="{quantile}"` is now `idm_icf_seconds{action="liveSync",bundle_version="{bundle_version}",connector="{connector}",connector_type="{connector_type}",location="{location}",object_class="{object_class}",operation="action",system_identifier="{system_identifier}",quantile="{quantile}"}`.

### Managed object script hook naming updates

The managed object script hook metrics include an updated naming convention and optional "object" and "script hook" tags.

* [API metric](../monitoring-guide/api-metrics.html#changed-managed-object-script-hook-metric):

  []()The metric `managed.{managed-object}.script.{script-name}` is now `managed-script-hook.{object}.{script-hook}`.

* [Prometheus metric](../monitoring-guide/prometheus-metrics.html#changed-managed-object-script-hook-metric-prom):

  []()The metric `idm_managed_seconds{managed_object="managed_object",operation="operation_name",script="script_name"}` is now `idm_managed_script_hook_seconds{object="object",script_hook="script_hook"}`.

|   |                                                                                                                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The deprecated metric names are still available and are generated along with the new metric names unless `deprecatedMetricsEnabled` is set to `false` in `conf/metrics.json`. Learn more in [Deprecated metric collection](../monitoring-guide/monitoring.html#deprecated-metric-collection). |

## Changes between IDM 8.0.1 and 8.0.2

### Oracle UCP datasource changes

The default Oracle UCP datasource template (`datasource.jdbc-ucp-oracle.json`) has changed:

* The JDBC URL format changed from the deprecated SID format (`@host:port:SID`) to the service name format (`@//host:port/service_name`).

* The `connectionTimeout` (in milliseconds) property is replaced with `connectionWaitTimeout` (in seconds). The old property was silently ignored by UCP.

Update your existing `conf/datasource.jdbc-ucp-oracle.json` file for these changes. Learn more in [Set up Oracle as an IDM repository](../install-guide/repository-oracledb.html#oracle-ucp-datasource).

## Changes between IDM 8.0.0 and 8.0.1

### Default API version for unversioned requests

Previously, REST API requests without an `Accept-API-Version` header used the latest available API version for the resource. These requests now default to API version `1.0`. The `consent`, `scheduler/job`, `scheduler/trigger`, and `schema` endpoints default to API version `2.0`.

## Changes between IDM 7.5.x and 8.0.0

### `launcher.json` configuration

Logging changes require new bundles and a specific `start-level` order. If you're copying `launcher.json` from a previous version of IDM, review the 8.0.0 version of `launcher.json` and integrate the changes and additions:

```json
{
  "bundle": {
    "containers": [
      {
        "location": "bundle",
        "includes": [
          "*.jar"
        ],
        "start-level": 1,
        "action": "install"
      },
      {
        "location": "bundle",
        "includes": [
          "**/org.apache.aries.spifly.dynamic.bundle*.jar",
          "**/asm-*.jar",
          "**/slf4j-*.jar"
        ],
        "start-level": 2,
        "action": "start"
      },
      {
        "location": "bundle",
        "includes": [
          "**/openidm-system-*.jar",
          "**/org.apache.felix.log*.jar"
        ],
        "start-level": 3,
        "action": "start"
      },
      {
        "location": "bundle",
        "includes": [
          "**/openidm-infoservice-*.jar",
          "**/openidm-datasource*.jar",
          "**/openidm-scr-starter-*.jar"
        ],
        "start-level": 4,
        "action": "start"
      },
      ...
    ]
  }
}
```

|   |                                               |
| - | --------------------------------------------- |
|   | Logging won't function without these changes. |

### Embedded Jetty web server upgrade

The embedded Jetty web server has been upgraded to Jetty 12, and `jetty.xml` is no longer supported in this IDM release. Learn more in [Embedded Jetty configuration](../install-guide/appendix-jetty.html) and in [Migrate Jetty configuration files](../upgrade-guide/migrate-config.html#updating-jetty).

|   |                                                                                                                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When serving SSL requests, Jetty 12 checks that the incoming host header matches the server certificate's subject and returns a `400 Bad Request` error on a mismatch. If you're upgrading to IDM 8.0, you must ensure your IDM server certificate subject matches the host name used by your deployment. |

### Felix HTTP Jetty upgrade

Felix HTTP Jetty has been upgraded to Jetty 12.

### Servlet Specification upgrade

Servlet Specification has been upgraded to 6.0.

### Jetty thread pool settings

You can now configure [Jetty thread pool settings](../install-guide/idm-config-properties-jetty.html#config-jetty-thread-settings-gzip-compression) in `conf/webserver.json`.

### Gzip compression settings

You can now configure [Gzip compression for HTTP responses](../install-guide/idm-config-properties-jetty.html#config-jetty-thread-settings-gzip-compression) in `conf/webserver.json`.

### Secure protocol configuration

You can now configure [Secure protocol settings](../install-guide/idm-config-properties-jetty.html#jetty-property-reference) in `conf/webserver.listener-*json`.

### Embedded DS repository

The embedded DS repository is no longer included with IDM. Before you can use IDM, you must [select and configure a repository](../install-guide/chap-repository.html).

### Logback

PingIDM now uses Logback to generate its server logs. You will need to add `logback.xml` to your configuration when updating. Learn more in [Server logs](../monitoring-guide/server-logs.html).

### Standalone end-user UI not bundled with PingIDM

The end-user UI is no longer bundled with PingIDM. You can download and install it separately from the [Backstage download site](https://backstage.forgerock.com/downloads). Learn more in [Install the end-user UI](../setup-guide/idm-enduser-ui.html).

### `_api` parameter requires authorization

Requests passing the `_api` parameter now require authorization. Learn more in [Common REST](../crest/about-crest.html#api-authorize-example).

### Array comparison

Starting with IDM 7.3, unordered array comparison became the default behavior. For this release of IDM, ordered array comparison is the default behavior, restoring the default behavior prior to IDM 7.3.

You can now use the `comparison` managed object schema configuration property to choose how JSON array comparisons are made with regard to array order.

Learn more about [managed object schema properties](../objects-guide/appendix-managed-objects.html#managed-object-property-config-properties) and [array comparison](../synchronization-guide/chap-implicit-live-sync.html#array-comparison).

### Java 21 support

Previously, running IDM required Java 17. You can now use Java 17 or Java 21. Learn more in [Java requirements](before-you-install.html#prerequisites-java).

## Changes between IDM 7.5.2 and 7.5.3

### Oracle UCP datasource changes

The default Oracle UCP datasource template (`datasource.jdbc-ucp-oracle.json`) has changed:

* The JDBC URL format changed from the deprecated SID format (`@host:port:SID`) to the service name format (`@//host:port/service_name`).

* The `connectionTimeout` (in milliseconds) property is replaced with `connectionWaitTimeout` (in seconds). The old property was silently ignored by UCP.

Update your existing `conf/datasource.jdbc-ucp-oracle.json` file for these changes. Learn more in [Set up Oracle as an IDM repository](../install-guide/repository-oracledb.html#oracle-ucp-datasource).

## Changes between IDM 7.5.1 and 7.5.2

### Default API version for unversioned requests

Previously, REST API requests without an `Accept-API-Version` header used the latest available API version for the resource. These requests now default to API version `1.0`. The `consent`, `scheduler/job`, `scheduler/trigger`, and `schema` endpoints default to API version `2.0`.

## Changes between IDM 7.5.0 and 7.5.1

### `_api` parameter requires authorization

Requests passing the `_api` parameter now require authorization. Learn more in [Common REST](../crest/about-crest.html#api-authorize-example).

### Array comparison

Starting with IDM 7.3.0, unordered array comparison became the default behavior. For this release of IDM, ordered array comparison is the default behavior, restoring the default behavior from prior to IDM 7.3.0.

You can now use the `comparison` managed object schema configuration property to choose how JSON array comparisons are made with regard to array order.

Learn more about [managed object schema properties](../objects-guide/appendix-managed-objects.html#managed-object-property-config-properties) and [array comparison](../synchronization-guide/chap-implicit-live-sync.html#array-comparison).

## Changes between IDM 7.4.x and 7.5.0

### Workflow engine upgrade

The Flowable embedded workflow engine has been upgraded to [version 6.8.0](https://github.com/flowable/flowable-engine/releases/tag/flowable-6.8.0). If you are upgrading from a previous version of IDM and use workflow, this upgrade requires one or more incremental upgrade scripts. For more information, refer to [Upgrade an existing repository](../upgrade-guide/update-repo.html#upgrade-existing-repository).

### Array schema fields default to item type `string`

Schema fields defined as type *array* are required to have an item type defined as of IDM 7.4.0. IDM 7.5.0 defaults the item type to `string` to avoid startup issues if the type is not defined.

### `populateDefaults` flag removed from secrets configuration

The sample secrets configuration (`secrets.json`) no longer includes the `populateDefaults` flag. It is safe to remove this from your secrets configuration.

### Java 17 required

Running IDM requires Java 17. For more information, refer to [Java requirements](before-you-install.html#prerequisites-java).

### Legacy hashing algorithms removed from the Admin UI

MD5 and SHA-1 are supported for legacy reasons, but should not be used in production environments and have been removed from the Admin UI. For more information, refer to [Salted hash algorithms](../security-guide/encoding-attribute-values.html#encoding-salted-hash).

### Secret store class renamed

The `org.forgerock.openidm.secrets.config.FileBasedStore` class has been deprecated and replaced by `org.forgerock.openidm.secrets.config.KeyStoreSecretStore`. The old class is currently an alias.

## Changes between IDM 7.4.2 and 7.4.3

### Default API version for unversioned requests

Previously, REST API requests without an `Accept-API-Version` header used the latest available API version for the resource. These requests now default to API version `1.0`. The `consent`, `scheduler/job`, `scheduler/trigger`, and `schema` endpoints default to API version `2.0`.

## Changes between IDM 7.4.1 and 7.4.2

### `_api` parameter requires authorization

Requests passing the `_api` parameter now require authorization. Learn more in [Common REST](../crest/about-crest.html#api-authorize-example).

### Array comparison

Starting with IDM 7.3.0, unordered array comparison became the default behavior. For this release of IDM, ordered array comparison is the default behavior, restoring the default behavior from prior to IDM 7.3.0.

You can now use the `comparison` managed object schema configuration property to choose how JSON array comparisons are made with regard to array order.

Learn more about [managed object schema properties](../objects-guide/appendix-managed-objects.html#managed-object-property-config-properties) and [array comparison](../synchronization-guide/chap-implicit-live-sync.html#array-comparison).

### Java upgrade

You must upgrade to Java 17, which is required by Jetty 12, to run IDM 7.4.2. Learn more in [Embedded Jetty configuration](../install-guide/appendix-jetty.html).

## Changes between IDM 7.4.0 and 7.4.1

### Workflow engine upgrade

The Flowable embedded workflow engine has been upgraded to [version 6.8.0](https://github.com/flowable/flowable-engine/releases/tag/flowable-6.8.0). If you're upgrading from a previous version of IDM and use workflow, this upgrade requires one or more incremental upgrade scripts. For more information, refer to [Upgrade an existing repository](../upgrade-guide/update-repo.html#upgrade-existing-repository).

## Changes between IDM 7.3.x and 7.4.0

### IDM requires JDK 11.0.20 or higher

If you try to run this version of IDM using an older release of JDK, the following error displays:

```console
SEVERE: Error loading keystore
java.io.IOException: Invalid keystore format
at java.base/sun.security.provider.JavaKeyStore.engineLoad(JavaKeyStore.java:667)
at java.base/sun.security.util.KeyStoreDelegator.engineLoad(KeyStoreDelegator.java:222)
at java.base/java.security.KeyStore.load(KeyStore.java:1479)
at org.forgerock.security.keystore.KeyStoreBuilder.build(KeyStoreBuilder.java:228)
at org.forgerock.openidm.secrets.keystore.KeyStoreRepository.load(KeyStoreRepository.java:59)
at org.forgerock.openidm.secrets.config.ConfigSupport.asKeyStoreHolder(ConfigSupport.java:95)
at org.forgerock.openidm.secrets.config.StoreSupport.asKeyStoreHolder(StoreSupport.java:61)
at org.forgerock.openidm.secrets.config.FileBasedStore.asKeyStoreHolder(FileBasedStore.java:18)
...
```

For a complete list of supported Java versions, refer to [Java requirements](before-you-install.html#prerequisites-java).

### The DB2 driver is now OSGi-compliant

When using IDM with a DB2 database, you previously had to create an OSGi-compliant driver. The driver included with DB2 is now compliant.

For more information, refer to:

* [IBM DB2 repository](../install-guide/repository-db2.html)

* [Supported repositories](before-you-install.html#prerequisites-repositories)

## Changes between IDM 7.3.2 and 7.3.3

### Default API version for unversioned requests

Previously, REST API requests without an `Accept-API-Version` header used the latest available API version for the resource. These requests now default to API version `1.0`. The `consent`, `scheduler/job`, `scheduler/trigger`, and `schema` endpoints default to API version `2.0`.

## Changes between IDM 7.3.1 and 7.3.2

### `_api` parameter requires authorization

Requests passing the `_api` parameter now require authorization. Learn more in [Common REST](../crest/about-crest.html#api-authorize-example).

### Array comparison

Starting with IDM 7.3.0, unordered array comparison became the default behavior. For this release of IDM, ordered array comparison is the default behavior, restoring the default behavior from prior to IDM 7.3.0.

You can now use the `comparison` managed object schema configuration property to choose how JSON array comparisons are made with regard to array order.

Learn more about [managed object schema properties](../objects-guide/appendix-managed-objects.html#managed-object-property-config-properties) and [array comparison](../synchronization-guide/chap-implicit-live-sync.html#array-comparison).

### Java upgrade

You must upgrade to Java 17, which is required by Jetty 12, to run IDM 7.3.2. Learn more in [Embedded Jetty configuration](../install-guide/appendix-jetty.html).

## Changes between IDM 7.3.0 and 7.3.1

### Workflow engine upgrade

The Flowable embedded workflow engine has been upgraded to [version 6.8.0](https://github.com/flowable/flowable-engine/releases/tag/flowable-6.8.0). If you're upgrading from a previous version of IDM and use workflow, this upgrade requires one or more incremental upgrade scripts. For more information, refer to [Upgrade an existing repository](../upgrade-guide/update-repo.html#upgrade-existing-repository).

## Changes between IDM 7.2.x and 7.3.0

### Synchronization JSON array comparison is order-agnostic

JSON array comparison during sync is now *order-agnostic*. This change may negate the need for certain custom scripts within mappings. For example, scripts that were previously required to sort `ldapGroups` values to avoid unnecessary target object updates.

### Attribute encryption on assignments

Assignment attributes are now encrypted if the corresponding connector attribute indicates confidentiality, based on the attribute's `nativeType` (such as `JAVA_TYPE_GUARDEDSTRING` or `JAVA_TYPE_GUARDED_BYTE_ARRAY`). As part of this change, the managed assignment object now includes the following property:

```json
"attributeEncryption" : { }
```

If `attributeEncryption` is not present, the assignment attributes are not encrypted. If the property is present but empty, it will default to IDM's default [encryption cipher](../security-guide/encoding-attribute-values.html). To specify a different cipher, add the `cipher` property. For example:

```json
"attributeEncryption" : {
  "cipher" : "AES/CBC/PKCS5Padding"
}
```

Additionally, `secrets.json` has a new secret: `idm.assignment.attribute.encryption`.

## Changes between IDM 7.1.x and 7.2.0

### Default `onDelete` behavior

The default `onDelete` behavior previously called a file-based script, `onDelete-roles.js`. This has been removed from the managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint, or directly in the conf/managed.json file.)*.

### Felix and OSGi upgrades

IDM has upgraded to OSGi Core 8.0 and Felix Framework 7.0.0.

### JMS 2.0 upgrade

The samples that use the Java Message Service (JMS) have been upgraded to use the 2.0 API and Apache ActiveMQ Artemis:

* [Subscribe to JMS messages](../samples-guide/scripted-jms-subscriber.html)

* [Direct audit information to a JMS broker](../samples-guide/audit-jms.html)

### PATCH request exceptions

Previously, illegal PATCH requests could return a `400` *or* `500` exception. In such cases, IDM now returns a `400` status.

### Policy enforcement on role name

The `name` property of a [managed role](../objects-guide/managed-roles.html) is now subject to the uniqueness policy by default. This means that you cannot create multiple roles with the same `name`. To change this behavior, adjust the policy validation on the `role` property in your managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint, or directly in the conf/managed.json file.)*.

### Precedence in locales in the self-registration email template

Previously, the `defaultLocale` specified in the Self-Registration Email Template configuration took precedence. As of IDM 7.2, locales specified as `preferredLocales` in the `Accept-Language` header take precedence over the `defaultLocale`.

### Paused queued synchronization for unavailable routes

Synchronization queue processing for a mapping is now *paused* if either the source or target system route are *unregistered*. For more information, see [Configure queued synchronization](../synchronization-guide/chap-implicit-live-sync.html#configure-queued-sync).

### Embedded workflow database

Previously, you could use the Flowable workflow engine's embedded H2 database for demo and testing purposes. IDM no longer includes this database. Before you use workflow, you must [install a JDBC repository](../install-guide/chap-repository.html).

Learn more in [Enable workflows](../workflow-guide/enable-workflows.html).

### Default MySQL connection driver

The default [JDBC Connection Configuration](../objects-guide/repo-config.html#datasource-jdbc-json) now uses the connection driver from MySQL 8.1 (`com.mysql.cj.jdbc.Driver`).

## Changes between IDM 7.1.4 and 7.1.6

No additional incompatible changes were made between 7.1.4 and 7.1.6.

## Changes between IDM 7.1.2 and 7.1.4

No additional incompatible changes were made between 7.1.2 and 7.1.4.

## Changes between IDM 7.1.0 and 7.1.2

### Embedded workflow database

Previously, you could use the Flowable workflow engine's embedded H2 database for demo and testing purposes. IDM no longer includes this database. Before you use workflow, you must [install a JDBC repository](../install-guide/chap-repository.html).

Learn more in [Enable workflows](../workflow-guide/enable-workflows.html).

### Workflow version update

Previously, workflows would break when upgrading from version 7.0.2 to 7.1.0 of IDM, because of out-of-sync versions of the Flowable workflow engine. This is fixed in version 7.1.2 of IDM. If you're upgrading IDM from version 7.0, please use IDM version 7.1.2 or higher.

## Changes between IDM 7.0.x and 7.1.0

### Data format change for external DS repositories

For external DS repositories with explicitly mapped managed objects, the stored data format has changed for certain data types.

In IDM versions prior to 7.1, certain property values were always considered as strings, so the returned JSON format of a managed object would look something like this:

```json
{
  "boolean": "true",
  "integer": "12345",
  "timestamp": "20210315010101Z",
  "json": "{\"key\":\"value\"}"
}
```

In IDM 7.1, these properties are returned with the correct data type, so a similar object in IDM 7.1 looks something like this:

```json
{
  "boolean": true,
  "integer": 12345,
  "timestamp": "2021-03-15T01:01:01Z",
  "json": { "key": "value" }
}
```

This change doesn't affect new deployments. If you're upgrading an existing deployment with an external DS repository with explicit object mappings, you should test this change and adapt your scripts and REST API calls, as necessary.

This change affects the following data types:

* Booleans: from string to JSON boolean

  Affected OIDs: `1.3.6.1.4.1.1466.115.121.1.7` and `1.3.6.1.4.1.36733.2.1.3.3.7`

* Integers: from string to JSON integer

  Affected OIDs: `1.3.6.1.4.1.1466.115.121.1.27` and `1.3.6.1.4.1.36733.2.1.3.3.27`

* Generalized time: from string in LDAP generalized time format, to string in ISO 8601 format

  Affected OIDs: `1.3.6.1.4.1.1466.115.121.1.24` and `1.3.6.1.4.1.36733.2.1.3.3.24`

* JSON: from JSON embedded in a string to structured JSON

  Affected OIDs: `1.3.6.1.4.1.36733.2.1.3.1`

|   |                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you want to retain the legacy behavior, set the following property in `conf/system.properties`:```properties
openidm.ds.rest2ldap.ignoreSchema.enabled=true
```This is not recommended in a production deployment and should be used only temporarily, as part of a plan to adapt to these changes. |

### Audit handler changes

The `JsonStdoutAuditEventHandler` is now pre-configured in the standard audit configuration, but is disabled by default.

Previously, to enable or disable audit handlers, you needed to modify `conf/audit.json` directly. Now, you can set the following properties in the `resolver/boot.properties` file to `true` or `false`:

* `openidm.audit.handler.json.enabled`

* `openidm.audit.handler.stdout.enabled`

* `openidm.audit.handler.repo.enabled`

Learn more in:

* [Choose audit event handlers](../audit-guide/configuring-topic-handlers.html)

* [Property value substitution](../setup-guide/using-property-substitution.html)

### Parameterized HTTP and HTTPS enablement

Previously, to enable or disable HTTP or HTTPS, you could modify `conf/config.properties` directly. Now, you can set the following properties in the `resolver/boot.properties` file to `true` or `false`:

* `openidm.https.enabled`

* `openidm.http.enabled`

Learn more in [Property value substitution](../setup-guide/using-property-substitution.html).

### Parameterized Felix web console credentials

Previously, to change the Felix web console credentials, you could modify the `conf/felix.webconsole.json` file directly. Now, you can set the following properties in the `resolver/boot.properties` file:

* `openidm.felix.webconsole.username`

* `openidm.felix.webconsole.password`

### Notification changes

Notifications are now disabled by default. Previously, to enable or disable notifications, you could modify the applicable `conf/notificationType.json` file directly. Now, you can set the following properties in the `resolver/boot.properties` file to `true` or `false`:

* `openidm.notifications.passwordUpdate`

* `openidm.notifications.profileUpdate`

* `openidm.notifications`

Learn more in [Configure notifications](../audit-guide/notification-config.html).

### Moved configuration files

The following files have been moved from the `/path/to/openidm/conf/` directory:

* `auth.profile.json` moved to `/path/to/openidm/samples/example-configurations/self-service/`.

* `jsonstore.json` moved to `/path/to/openidm/samples/example-configurations/self-service/`.

* `identityProviders.json` moved to `/path/to/openidm/samples/example-configurations/self-service/`.

### Improved `validateProperty` error handling

Previously, API requests containing the `validateProperty` action to unknown resources or those with invalid POST body content could result in an invalid `true` response, or a generic *500 Internal Server Error*. Both of these situations now return a *400 Bad Request Error* with an explanation.

Error comparison

* BEFORE

* AFTER

```json
{
  "code": 500,
  "reason": "Internal Server Error",
  "message": "TypeError: Cannot call method "hasOwnProperty" of null",
  "detail": {}
}
```

```json
{
  "code": 400,
  "reason": "Bad Request",
  "message": "object and properties were not provided in request content, and they are unable to be retrieved.",
  "detail": {}
}
```

### Changes to `router.json`

The default `router.json` file no longer includes `system` in the matching pattern.

## Changes between IDM 6.5.x and 7.0.0

### Embedded workflow database

Previously, you could use the Flowable workflow engine's embedded H2 database for demo and testing purposes. IDM no longer includes this database. Before you use workflow, you must [install a JDBC repository](../install-guide/chap-repository.html).

Learn more in [Enable workflows](../workflow-guide/enable-workflows.html).

### New workflow engine

The Activiti workflow engine has been replaced with [Flowable](https://www.flowable.com/open-source/docs/). Current workflow definitions will continue to work with the new engine in compatibility mode, but all new workflow definitions must be written for Flowable. Learn more in [Workflow definition comparison^](../../8/workflow-guide/workflow-def-comp.html).

If you're using MySQL for the workflow database, the following apply:

* You must use MySQL version 5.6.4 or later. If you're using an older version, perform the MySQL upgrade before upgrading to IDM 7 or later. For additional information, see the [Flowable Note for MySQL users](https://flowable.com/open-source/docs/bpmn/ch03-Configuration/#creating-the-database-tables).

* Flowable automatically upgrades the database schema and can encounter non-recoverable errors related to date settings. Before you start IDM 7 or later for the first time, remove the `SQL_MODE` settings `NO_ZERO_IN_DATE` and `NO_ZERO_DATE`. Example SQL command:

  ```sql
  mysql -uroot -ppassword

  set GLOBAL SQL_MODE='';

  use openidm;
  set SQL_MODE='';
  ```

  After you complete the upgrade process, you can restart MySQL and your original settings should be restored.

### Changes to `boot.properties`

* Prometheus monitoring

  Monitoring using Prometheus is no longer achieved with a specific access role. The `openidm/metrics/prometheus` endpoint is now protected by a basic authentication filter, using credentials set in the `resolver/boot.properties` file. Learn more in [Prometheus endpoint](../monitoring-guide/monitoring.html#prometheus).

* Debugging information for Groovy scripts

  In previous releases, setting `javascript.exception.debug.info=true` in the `boot.properties` file enabled additional debug information, including line numbers and file names for JavaScript exceptions. In this release, setting `groovy.exception.debug.info=true` lets you gather comparable debug information for Groovy scripts.

* Added properties

  These properties have been added to `resolver/boot.properties`:

  * `openidm.servlet.upload.alias=/upload` and `openidm.servlet.export.alias=/export`: Sets the REST endpoints for the bulk import feature.

  * `openidm.admin.password=openidm-admin`: Lets you change the password of the administrative user before startup.

* Removed properties

  These properties have been removed from `resolver/boot.properties`:

  * openidm.script.javascript.debug

  * openidm.script.javascript.sources

  * openidm.ssl.host.aliases

  * com.iplanet.am.cookie.name

  * com.sun.identity.auth.cookieName

### Changes to `logging.properties`

The default log message formatter has changed from `ThreadIdLogFormatter` to `SanitizedThreadIdLogFormatter`. The new default encodes control characters (such as newline characters) using URL-encoding, to protect against log forgery. Control characters in stack traces are not encoded. Learn more in [Log message format](../monitoring-guide/server-logs.html#log-message-format).

### Change to how authorization roles are assigned

In previous IDM releases, managed users were granted the `openidm-authorized` role as a relationship during user creation as part of the `onCreateUser.js` script. In IDM 7, users are granted the `openidm-authorized` role statically when they authenticate. Learn more in [Authentication and roles](../auth-guide/authentication-and-roles.html).

|   |                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This way of granting internal authentication roles is considered a best practice and is recommended for performance reasons. However, if your deployment relies on the old way of granting the `openidm-authorized` role, that configuration is still supported, and you can use your existing `onCreateUser.js` script to grant the role on creation. |

### Schema change to `authzRoles`

The default relationship model for `authzRoles` and `authzMembers` has changed in this release. In the default configuration, a user's `authzRoles` now references only the `internal/role` resource collection and not the `managed/role`. Conversely, an internal role's `authzMembers` property now references only the `managed/user` resource collection.

The default schema configuration files have been amended to support this change. The `managed/role` collection has been removed from the `authzRoles` property on a managed user object and the `internal/user` collection has been removed from the `authzMembers` property on an internal role object.

Multiple resource collections for a single relationship field are not currently supported with a DS repository. For legacy reasons, Multiple resource collections will still work with a JDBC repository.

### Change to the `INTERNAL_USER` authentication module

The INTERNAL\_USER authentication module is no longer provided in the default authentication configuration.

This change means that any scripts you used previously to update internal user passwords in the IDM repository will need to be modified.

### Change to Prometheus monitoring

Monitoring using Prometheus is no longer achieved with a specific access role. The `openidm/metrics/prometheus` endpoint is now protected by a basic authentication filter, using credentials set in the `resolver/boot.properties` file. Learn more in [Prometheus endpoint](../monitoring-guide/monitoring.html#prometheus).

### Change in how boolean values are assessed

Properties stored in the repository with boolean (`true/false`) values are processed differently from this release. A property value is now considered `false` if its value is `false` or `null`. The value is considered `true` only if it is `true`, not if it is `null`. If you're migrating from a previous IDM release, you might need to adjust your scripts to take this change into account.

### Queued sync changes

* Processing order of queued synchronization mappings

  In previous IDM releases, mappings for which queued synchronization was enabled were processed first. The synchronization engine would then process the non-queued mappings in order. In IDM 7, all mappings are processed in the order in which they are listed, regardless of whether queued synchronization is enabled.

  If you want to retain the pre-7.0 behavior, place your queued synchronization mappings first in your list of mappings.

* Removal of `remainingRetries` from queued synchronization

  This release lets you configure an infinite number of queued synchronization retries. As part of this change, the `remainingRetries` property has been removed from the queued synchronization object.

  Learn more in [Configure queued synchronization](../synchronization-guide/chap-implicit-live-sync.html#configure-queued-sync).

### Virtual property calculation for `effectiveRoles` and `effectiveAssignments`

`effectiveRoles` and `effectiveAssignments` are now calculated in IDM by default, using the new `queryConfig` property. The old method of using `onRetrieve` scripts will still work. The new `queryConfig` property is also available for use with other virtual properties. Learn more in [Effective roles and effective assignments](../objects-guide/effective-roles-and-assignments.html) and [Virtual properties](../objects-guide/managed-object-virtual-properties.html).

### Gzip compression for HTTP responses

You can now configure Gzip compression for HTTP responses in `conf/jetty.xml`. In previous IDM releases, compression was configured in `conf/servletfilter-gzip.json`. This file has been removed.

### Configurable hashing

IDM 7 supports [configurable hashing algorithms](../security-guide/encoding-attribute-values.html#encoding-salted-hash).

### Temporal constraint enforcement on roles

Enforcing temporal constraints on roles is now achieved through Java, rather than through the `onSync-roles.js` and `postOperation-roles.js` scripts. These scripts are still provided in `openidm/bin/defaults/script/roles` for backward compatibility.

To use the new Java-based functionality in existing deployments, change the `role` object in your managed object schema (`conf/managed.json`) by adding `"isTemporalConstraint" : true` to the `"temporalConstraints"` object. For example:

```json
"temporalConstraints" : {
    "description" : "An array of temporal constraints for a role",
    "title" : "Temporal Constraints",
    "viewable" : false,
    "returnByDefault" : true,
    "isTemporalConstraint" : true,
    "type" : "array",
    ...
}
```

Learn more in [Use temporal constraints to restrict effective roles](../objects-guide/roles-temporal-constraints.html).

### Change to JMS audit handler

The `batch` configuration for the JMS common audit handler for access logs has changed to support reconnection if the broker becomes unavailable.

This change adds a `batch.writeInterval` setting. It removes the following settings:

* `batch.batchEnabled`

* `batch.insertTimeoutSec`

* `batch.pollTimeoutSec`

* `batch.shutdownTimeoutSec`

* `batch.threadCount`

Learn more in [Configure the JMS audit event handler](../audit-guide/configuring-topic-handlers.html#audit-jms-config).

### Change to default audit configuration

The default audit configuration no longer includes the `recon` audit topic. You can enable it by adding the `recon` audit topic to the `topics` list in `conf/audit.json` for the event handlers you choose.

This change does not affect how auditing reconciliations works, just what the default configuration includes. No action is necessary unless you wish to have auditing on reconciliations enabled on a new installation. Learn more in [Query the reconciliation audit log](../audit-guide/querying-audit-over-rest.html#querying-recon-logs).

### Datatype of `userPassword` property in provisioner files

As a security precaution, the `nativeType` for `userPassword` properties has been changed to `JAVA_TYPE_GUARDEDSTRING` in all sample provisioner files for the LDAP connector. If you have customized provisioner files, you should change this property. For example, change:

Example provisioner update

* BEFORE

* AFTER

```json
"userPassword" : {
    "type" : "string",
    "nativeName" : "userPassword",
    "nativeType" : "string",
    ...
```

```json
"userPassword" : {
    "type" : "string",
    "nativeName" : "__PASSWORD__",
    "nativeType" : "JAVA_TYPE_GUARDEDSTRING",
    ...
```

### Removal of the global consent setting

Previous IDM versions included a global consent setting in `conf/consent.json`. This file included a single configuration property, `enabled`, which determined whether IDM should check any mappings where consent was enabled and prompt end users for consent.

This global consent setting and the corresponding `consent.json file` have been removed. If you have an existing `consent.json` file in your configuration, it will be ignored.

Consent is now assessed only on a per-mapping, per-object basis.

### Support for MySQL Connector/J version 8.0

IDM 7 adds support for the latest version of MySQL Connector/J. If you're using MySQL Connector/J version 8.0 or later, make sure your `datasource.jdbc-default.json` file includes a setting for the time zone in your `jdbcUrl` property:

```json
"jdbcUrl" : "jdbc:mysql://&{openidm.repo.host}:&{openidm.repo.port}/openidm?allowMultiQueries=true&characterEncoding=utf8&serverTimezone=UTC",
```

Also, note the `driverClass` changed in MySQL Connector/J version 8.0, from `com.mysql.jdbc.Driver` to `com.mysql.cj.jdbc.Driver`. The previous `driverClass` name will still work for now, but should be updated to avoid it displaying a warning when starting up IDM.

### Default security protocols for inbound connections

The default security protocols for inbound connections to IDM are `TLSv1.2` and `TLSv1.3`. Learn more in [Jetty property reference](../install-guide/idm-config-properties-jetty.html#jetty-property-reference).

Support for the `TLSv1.1` protocol has been removed by default.

### Removal of `address2` from the managed object schema

The `address2` attribute has been removed from the managed object schema (`conf/managed.json`).

### ICF and connector changes

The following ICF and connector changes will have an impact on existing IDM deployments that use those connectors:

* Workday connector

  The Workday connector is no longer bundled with IDM. Download the connector and its dependencies from the [Backstage](https://backstage.forgerock.com/downloads/) download site.

* Database Table connector

  The configuration requirements for the Database Table connector have changed:

  * The `jdbcDriver` and `jdbcUrlTemplate` properties have been removed. Use `driverClassName` and `url` instead.

  * The `database` property has been removed. The database should now be specified in the JDBC address in `url`.

  * Additional (optional) configuration properties are now available. For a full list, refer to [Database table connector](https://docs.pingidentity.com/openicf/connector-reference/dbtable.html).

  Additionally, the Database Table connector example configurations have changed:

  * samples/example-configurations/provisioners/provisioner.openicf-contractordb.json

    * Removed `required : true` from the `__NAME__` property.

    * Added `required : true` to the `EMAIL` property.

    * Removed `"keyColumn" : "UNIQUE_ID"`.

  * samples/example-configurations/provisioners/provisioner.openicf-contractordb.sql

    Set `EMAIL` as the `PRIMARY KEY`.

## Archive

For documentation and release information prior to IDM 7.0, check out the [Documentation Archive](https://docs.pingidentity.com/archive/).

---

---
title: Deprecation
description: PingIDM features marked as deprecated and scheduled for removal in a future release, with replacement options where available
component: pingidm
version: 8.1
page_id: pingidm:release-notes:deprecated-functionality
canonical_url: https://docs.pingidentity.com/pingidm/8.1/release-notes/deprecated-functionality.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Compatibility"]
section_ids:
  api-explorer-ui-deprecated: Legacy API Explorer
  legacy-admin-ui-deprecated: Legacy admin UI
  deprecation-managed-object-script-metrics: Managed object script metric names
  deprecation-router-filter-metrics: Router filter metrics
  deprecation-non-persisted-schedules: Non-persisted schedules
  deprecation-openidm-health-endpoint: openidm/health endpoint
  deprecation-ping-info-endpoint: openidm/info/ping endpoint
  deprecation-pax-web-properties: Pax Web properties
  deprecation-audit-event-handlers: Audit event handlers
  deprecation-read-query-audit-endpoint: Read and query the audit endpoint
  deprecation-proxy-properties-purpose: Proxy properties and password purpose
  deprecation-prometheus-properties-purpose: Prometheus properties and password purpose
  deprecation-java-util-logging: Java.util.logging
  deprecation-info-features-endpoint: info/features endpoint
  deprecation-jvm-mem-usage-metrics: Memory usage ratio metrics
  deprecation-secrets-in-config: Secrets and passwords stored in configuration
  deprecation-widgets: Widgets
  relationship_schema_query_filter: Relationship schema query filter
  secret_store_class_renamed: Secret store class renamed
  deprecated-access.js: Access configuration in access.js
  deprecated-scheduler-action: Actions on scheduler endpoint
  deprecated-health-endpoints: Health endpoints
  deprecated-conditional-queries: Conditional query filters
  deprecated-oauthReturn-endpoint: oauthReturn endpoint
  deprecated-timezone-schedules: timeZone in schedules
  deprecated-hash-algorithms: MD5 and SHA-1 hash algorithms
  deprecated-java-date: JAVA_TYPE_DATE attribute type
  deprecated-action-patch: POST request with ?_action=patch
  deprecated-minlength-patch: minLength property
  deprecated-top-level-read-on-config: Read requests at top of /config
  deprecated-array-of-types: Defining object schema type attribute in an array when it is a single type
---

# Deprecation

The following features are deprecated and likely to be discontinued in a future release.

## Legacy API Explorer

The legacy IDM API Explorer is deprecated and will be removed in a future release.

Starting with IDM 8.1, the API Explorer is no longer bundled with the IDM distribution. It's available as a separate downloadable artifact from the [Backstage download site](https://backstage.forgerock.com/downloads).

Learn more in [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html).

## Legacy admin UI

The legacy IDM admin UI is deprecated and will be removed in a future release. Use the [Platform admin UI](../setup-guide/platform-admin-ui.html) instead.

Starting with IDM 8.1, the legacy admin UI is no longer bundled with the IDM distribution. It's available as a separate downloadable artifact from the [Backstage download site](https://backstage.forgerock.com/downloads).

|   |                                                                                                                                                                                                                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The Platform admin UI and the legacy admin UI are independent artifacts. You can install one or both on different Nginx servers or different ports. New deployments should use the Platform admin UI.Learn more:- [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html)

- [Install the Platform admin UI for standalone IDM](../setup-guide/platform-admin-ui.html) |

## Managed object script metric names

The following [API](../monitoring-guide/api-metrics.html#changed-managed-object-script-hook-metric) and [Prometheus](../monitoring-guide/prometheus-metrics.html#changed-managed-object-script-hook-metric-prom) metric names are deprecated:

* `managed.managed-object.script.script-name`

* `idm_managed_seconds{managed_object="managed_object",operation="operation_name",script="script_name"}`

Use the following replacement metric names:

* `managed-script-hook.object.script-hook`

* `idm_managed_script_hook_seconds{object="object",script_hook="script_hook"}`

All previous metric names will continue to function until removed. Learn more in [Deprecated metric collection](../monitoring-guide/monitoring.html#deprecated-metric-collection).

## Router filter metrics

The following [API](../monitoring-guide/api-metrics.html#changed-router-filter-metrics) and [Prometheus](../monitoring-guide/prometheus-metrics.html#changed-router-filter-metrics-prom) metric names are deprecated:

* `filter.filter-type.action.script-name`

* `idm_filter_seconds{action=action,filter_type=filter_type,script_name=script_name}`

Use the following replacement metric names:

* `router-filter.name.action.script-name.quantile.system`

* `idm_router_filter_seconds{action=action,name=name,script_name=script_name,quantile=quantile,system=system}`

All previous metric names will continue to function until removed. Learn more in [Deprecated metric collection](../monitoring-guide/monitoring.html#deprecated-metric-collection).

## Non-persisted schedules

Non-persisted (in memory) schedules are deprecated. Use the default, [persisted schedules](../schedules-guide/persistent-schedules.html).

## `openidm/health` endpoint

The `openidm/health` endpoint is deprecated. Use the [`openidm/health/live` and `openidm/health/ready` endpoints](../install-guide/system-healthcheck.html#audit-free-health-check) instead.

## `openidm/info/ping` endpoint

The `openidm/info/ping` endpoint is deprecated. Use the [`openidm/health/live` and `openidm/health/ready` endpoints](../install-guide/system-healthcheck.html#audit-free-health-check) instead.

## Pax Web properties

The following Pax Web properties are deprecated and will be removed in a future release of IDM:

* `org.ops4j.pax.web.server.maxThreads`

  Set the `maxThreads` field directly in the webserver config or use `openidm.webserver.max.threads`.

* `org.ops4j.pax.web.server.minThreads`

  There is no replacement for this setting and the minimum thread count is always set to `8`.

* `org.ops4j.pax.web.server.jetty.io.idleTimeout`

  There is no replacement for this setting and the thread idle timeout is always set to `60000` ms.

## Audit event handlers

The [JMS](../audit-guide/configuring-topic-handlers.html#audit-jms-handler), [Repository](../audit-guide/configuring-topic-handlers.html#audit-repo-handler), [Router](../audit-guide/configuring-topic-handlers.html#audit-router-handler), and [Syslog](../audit-guide/configuring-topic-handlers.html#audit-syslog-handler) audit event handlers are deprecated and will be removed in a future release of IDM. Use the [JSON audit event handler](../audit-guide/configuring-topic-handlers.html#audit-json-handler) or similar to export your data to a third-party audit framework, such as [Elastic Stack](https://www.elastic.co/elastic-stack).

## Read and query the audit endpoint

Query and read operations on the `/audit` API endpoint are deprecated and will be removed in a future release of IDM. Use the [JSON audit event handler](../audit-guide/configuring-topic-handlers.html#audit-json-handler) or similar to export your data to a third-party audit framework, such as [Elastic Stack](https://www.elastic.co/elastic-stack).

## Proxy properties and password purpose

The following proxy properties and purpose are deprecated and will be removed in a future release of IDM:

* `openidm.http.client.proxy.userName`

* `openidm.http.client.proxy.password`

* `idm.http.client.proxy.password`

Use the `idm.http.client.proxy.credentials` purpose to store the proxy username and password instead.

## Prometheus properties and password purpose

The following Prometheus properties and purpose are deprecated and will be removed in a future release of IDM:

* `openidm.prometheus.username`

* `openidm.prometheus.password`

* `idm.prometheus.password`

Use the `idm.prometheus.credentials` secret to store the Prometheus username and password instead.

## Java.util.logging

PingIDM now uses [Logback](../monitoring-guide/server-logs.html) to generate its logs. JUL logs are deprecated. You can generate logs in the old format by configuring Logback to use the [pattern layout encoder](../monitoring-guide/server-logs.html#pattern-layout-encoder).

## `info/features` endpoint

The `info/features` endpoint is deprecated and will be removed in a future release of IDM.

## Memory usage ratio metrics

Most of the existing [JVM metrics](../monitoring-guide/api-metrics.html#api-jvm-metric-names) have been deprecated and will be removed in a future release of IDM. All previous metrics will continue to function until their removal. The metrics are classified into these categories:

* The metric name has changed.

* The metric type has changed.

* The metric has no replacement, but you might be able to calculate the value on your own.

* Three metrics remain unchanged:

  * jvm.max-memory

  * jvm.available-cpus

  * jvm.used-memory

Use the following table to compare old and new metric names, removed metrics, and type changes:

| Deprecated Metric                                                 | New Metric                                                         | Notes                           |
| ----------------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------- |
| jvm.memory-usage.pools.G1-Old-Gen.committed                       | jvm.memory-usage.pools.committed\_G1-Old-Gen                       |                                 |
| jvm.memory-usage.pools.CodeHeap-'profiled-nmethods'.init          | jvm.memory-usage.pools.init\_CodeHeap-'profiled-nmethods'          |                                 |
| jvm.memory-usage.pools.G1-Old-Gen.init                            | jvm.memory-usage.pools.init\_G1-Old-Gen                            |                                 |
| jvm.memory-usage.total.max                                        | N/A                                                                | Removed                         |
| jvm.memory-usage.total.committed                                  | N/A                                                                | Removed                         |
| jvm.memory-usage.heap.init                                        | jvm.memory-usage.init\_heap                                        |                                 |
| jvm.memory-usage.pools.CodeHeap-'non-nmethods'.usage              | N/A                                                                | Removed                         |
| jvm.memory-usage.pools.Metaspace.init                             | jvm.memory-usage.pools.init\_Metaspace                             |                                 |
| jvm.memory-usage.pools.G1-Survivor-Space.committed                | jvm.memory-usage.pools.committed\_G1-Survivor-Space                |                                 |
| jvm.memory-usage.heap.usage                                       | N/A                                                                | Removed                         |
| jvm.garbage-collector.G1-Old-Generation.count                     | jvm.garbage-collector.count.total\_G1-Old-Generation               | Type was "gauge", now "counter" |
| jvm.thread-state.waiting.count                                    | jvm.thread-state\_waiting                                          |                                 |
| jvm.class-loading.loaded                                          | jvm.class-loading.loaded.total                                     | Type was "gauge", now "counter" |
| jvm.memory-usage.pools.CodeHeap-'non-profiled-nmethods'.committed | jvm.memory-usage.pools.committed\_CodeHeap-'non-profiled-nmethods' |                                 |
| jvm.memory-usage.total.init                                       | N/A                                                                | Removed                         |
| jvm.memory-usage.pools.CodeHeap-'non-nmethods'.used               | jvm.memory-usage.pools.used\_CodeHeap-'non-nmethods'               |                                 |
| jvm.memory-usage.pools.G1-Eden-Space.init                         | jvm.memory-usage.pools.init\_G1-Eden-Space                         |                                 |
| jvm.memory-usage.pools.Metaspace.usage                            | N/A                                                                | Removed                         |
| jvm.memory-usage.pools.G1-Eden-Space.max                          | jvm.memory-usage.pools.max\_G1-Eden-Space                          |                                 |
| jvm.memory-usage.pools.G1-Old-Gen.max                             | jvm.memory-usage.pools.max\_G1-Old-Gen                             |                                 |
| jvm.memory-usage.total.used                                       | N/A                                                                | Removed                         |
| jvm.memory-usage.pools.CodeHeap-'profiled-nmethods'.used          | jvm.memory-usage.pools.used\_CodeHeap-'profiled-nmethods'          |                                 |
| jvm.memory-usage.pools.G1-Survivor-Space.init                     | jvm.memory-usage.pools.init\_G1-Survivor-Space                     |                                 |
| jvm.memory-usage.non-heap.max                                     | jvm.memory-usage.max\_non-heap                                     |                                 |
| jvm.memory-usage.pools.G1-Survivor-Space.max                      | jvm.memory-usage.pools.max\_G1-Survivor-Space                      |                                 |
| jvm.memory-usage.pools.CodeHeap-'profiled-nmethods'.max           | jvm.memory-usage.pools.max\_CodeHeap-'profiled-nmethods'           |                                 |
| jvm.thread-state.daemon.count                                     | jvm.thread-state.daemon                                            |                                 |
| jvm.memory-usage.pools.G1-Eden-Space.used-after-gc                | jvm.memory-usage.pools.used-after-gc\_G1-Eden-Space                |                                 |
| jvm.thread-state.new\.count                                       | jvm.thread-state\_new                                              |                                 |
| jvm.memory-usage.pools.G1-Eden-Space.used                         | jvm.memory-usage.pools.used\_G1-Eden-Space                         |                                 |
| jvm.garbage-collector.G1-Young-Generation.time                    | jvm.garbage-collector.time.total\_G1-Young-Generation              | Type was "gauge", now "counter" |
| jvm.memory-usage.pools.CodeHeap-'non-profiled-nmethods'.max       | jvm.memory-usage.pools.max\_CodeHeap-'non-profiled-nmethods'       |                                 |
| jvm.memory-usage.heap.used                                        | jvm.memory-usage.used\_heap                                        |                                 |
| jvm.class-loading.unloaded                                        | jvm.class-loading.unloaded.total                                   | Type was "gauge", now "counter" |
| jvm.memory-usage.pools.G1-Eden-Space.committed                    | jvm.memory-usage.pools.committed\_G1-Eden-Space                    |                                 |
| jvm.memory-usage.heap.max                                         | jvm.memory-usage.max\_heap                                         |                                 |
| jvm.memory-usage.pools.Metaspace.used                             | jvm.memory-usage.pools.used\_Metaspace                             |                                 |
| jvm.memory-usage.non-heap.used                                    | jvm.memory-usage.used\_non-heap                                    |                                 |
| jvm.memory-usage.pools.Compressed-Class-Space.usage               | N/A                                                                | Removed                         |
| jvm.memory-usage.non-heap.usage                                   | N/A                                                                | Removed                         |
| jvm.memory-usage.pools.CodeHeap-'non-profiled-nmethods'.init      | jvm.memory-usage.pools.init\_CodeHeap-'non-profiled-nmethods'      |                                 |
| jvm.memory-usage.pools.Compressed-Class-Space.init                | jvm.memory-usage.pools.init\_Compressed-Class-Space                |                                 |
| jvm.memory-usage.pools.G1-Old-Gen.used                            | jvm.memory-usage.pools.used\_G1-Old-Gen                            |                                 |
| jvm.thread-state.timed\_waiting.count                             | jvm.thread-state\_timed\_waiting                                   |                                 |
| jvm.memory-usage.pools.G1-Old-Gen.usage                           | N/A                                                                | Removed                         |
| jvm.memory-usage.pools.CodeHeap-'non-profiled-nmethods'.usage     | N/A                                                                | Removed                         |
| jvm.garbage-collector.G1-Young-Generation.count                   | jvm.garbage-collector.count.total\_G1-Young-Generation             | Type was "gauge", now "counter" |
| jvm.thread-state.terminated.count                                 | jvm.thread-state\_terminated                                       |                                 |
| jvm.garbage-collector.G1-Old-Generation.time                      | jvm.garbage-collector.time.total\_G1-Old-Generation                | Type was "gauge", now "counter" |
| jvm.memory-usage.heap.committed                                   | jvm.memory-usage.committed\_heap                                   |                                 |
| jvm.memory-usage.pools.Metaspace.committed                        | jvm.memory-usage.pools.committed\_Metaspace                        |                                 |
| jvm.memory-usage.pools.CodeHeap-'non-nmethods'.committed          | jvm.memory-usage.pools.committed\_CodeHeap-'non-nmethods'          |                                 |
| jvm.memory-usage.non-heap.committed                               | jvm.memory-usage.committed\_non-heap                               |                                 |
| jvm.memory-usage.pools.G1-Survivor-Space.usage                    | N/A                                                                | Removed                         |
| jvm.thread-state.blocked.count                                    | jvm.thread-state\_blocked                                          |                                 |
| jvm.memory-usage.pools.G1-Survivor-Space.used-after-gc            | jvm.memory-usage.pools.used-after-gc\_G1-Survivor-Space            |                                 |
| jvm.memory-usage.pools.G1-Eden-Space.usage                        | N/A                                                                | Removed                         |
| jvm.memory-usage.pools.CodeHeap-'non-profiled-nmethods'.used      | jvm.memory-usage.pools.used\_CodeHeap-'non-profiled-nmethods'      |                                 |
| jvm.memory-usage.pools.G1-Survivor-Space.used                     | jvm.memory-usage.pools.used\_G1-Survivor-Space                     |                                 |
| jvm.memory-usage.pools.Compressed-Class-Space.committed           | jvm.memory-usage.pools.committed\_Compressed-Class-Space           |                                 |
| jvm.memory-usage.pools.CodeHeap-'non-nmethods'.init               | jvm.memory-usage.pools.init\_CodeHeap-'non-nmethods'               |                                 |
| jvm.thread-state.count                                            | N/A                                                                | Removed                         |
| jvm.memory-usage.non-heap.init                                    | jvm.memory-usage.init\_non-heap                                    |                                 |
| jvm.thread-state.runnable.count                                   | jvm.thread-state\_runnable                                         |                                 |
| jvm.memory-usage.pools.CodeHeap-'profiled-nmethods'.committed     | jvm.memory-usage.pools.committed\_CodeHeap-'profiled-nmethods'     |                                 |
| jvm.memory-usage.pools.Metaspace.max                              | jvm.memory-usage.pools.max\_Metaspace                              |                                 |
| jvm.memory-usage.pools.G1-Old-Gen.used-after-gc                   | jvm.memory-usage.pools.used-after-gc\_G1-Old-Gen                   |                                 |
| jvm.memory-usage.pools.Compressed-Class-Space.max                 | jvm.memory-usage.pools.max\_Compressed-Class-Space                 |                                 |
| jvm.memory-usage.pools.CodeHeap-'non-nmethods'.max                | jvm.memory-usage.pools.max\_CodeHeap-'non-nmethods'                |                                 |
| jvm.memory-usage.pools.CodeHeap-'profiled-nmethods'.usage         | N/A                                                                | Removed                         |
| jvm.memory-usage.pools.Compressed-Class-Space.used                | jvm.memory-usage.pools.used\_Compressed-Class-Space                |                                 |
| jvm.free-used-memory                                              | jvm.free-memory                                                    |                                 |

## Secrets and passwords stored in configuration

Storing secrets and passwords directly in configuration and property files is deprecated and will be removed in a future release of IDM. Use [Secret stores](../security-guide/secret-stores.html) for secret resolution.

## Widgets

Widgets are deprecated and will be removed in a future release of IDM.

## Relationship schema query filter

The Query Filter field in the Edit Resource window of relationship schema properties has been deprecated.

Use cases requiring a delegated admin to see a subset of users or other objects can use a query filter on the role privilege to limit the users returned by the query.

## Secret store class renamed

The `org.forgerock.openidm.secrets.config.FileBasedStore` class has been deprecated and replaced by `org.forgerock.openidm.secrets.config.KeyStoreSecretStore`. The old class is currently an alias.

## Access configuration in access.js

In previous releases, access rules were configured in the `access.js` script. This script has been replaced by an `access.json` configuration file, that performs the same function. Existing deployments that use customized `access.js` files are still supported for backward compatibility. However, support for access rules defined in `access.js` is deprecated, and will be removed in a future release. You should move these access rules to a `conf/access.json` file. For more information, refer to [Authorization and roles](../auth-guide/authorization-and-roles.html).

## Actions on scheduler endpoint

The `action` parameter on the `scheduler` endpoint was deprecated in Version 1 of the endpoint and is not supported in Version 2.

To validate a cron expression, use the `validateQuartzCronExpression` action on the `scheduler/job` endpoint, as described in [Validate Cron Trigger Expressions](../schedules-guide/configure-schedules.html#validating-schedule-syntax).

## Health endpoints

The `health` endpoints, used to monitor system activity have been deprecated in this release, as their functionality was not considered to be of much use.

The information available on `health/recon` was node-specific. Instead, you can retrieve cluster-wide reconciliation details with a GET on the `recon` endpoint.

The information available on the `health/os` and `health/memory` endpoints can be retrieved by inspecting the [JVM metrics](../monitoring-guide/api-metrics.html#api-jvm-metric-names).

## Conditional query filters

The syntax of conditional query filters and scripts within notification filters has changed in this release. In previous IDM releases, request properties such as `content` in create and update requests or `patchOperations` in patch requests were referenced directly. For example, a previous configuration might have used the following query filter:

```json
"condition" : "content/manager pr"
```

In IDM 7 and later, query filters and scripts should reference the `request` object to obtain any request properties. Sample query filters have been changed accordingly. The previous example would be changed to the following:

```json
"condition" : "request/content/manager pr",
```

This syntax is more verbose, but it lets script implementations use request visitors logic based on the request type, and is more consistent with generic router filters.

The old request syntax will still work in IDM 7.0, but is considered deprecated. Support for the old syntax will be removed in a future release. Note that this change is limited to notification filters. Filters such as those used with scripted endpoints have never supported direct access to request properties, and are therefore not changing. For more information on notification filters, refer to [Configure notifications](../audit-guide/notification-config.html).

## oauthReturn endpoint

Support for `oauthReturn` as an endpoint for OAuth2 and OpenID Connect standards has been deprecated for interactions with AM and will be removed in a future release. Support for interactions with social identity providers was [removed in IDM 6.5.0](https://backstage.forgerock.com/docs/idm/6.5/release-notes/#removed-6.5.0).

Default versions of relevant configuration files no longer include `oauthReturn` in the `redirectUri` setting. However, for IDM 8.1, these configuration files should still work both with and without `oauthReturn` in the endpoint.

## `timeZone` in schedules

In [Configure schedules](../schedules-guide/configure-schedules.html), setting a time zone using the `timeZone` field is deprecated. To specify a time zone for schedules, use the `startTime` and `endTime` fields.

## MD5 and SHA-1 hash algorithms

Support for the `MD5` and `SHA-1` hash algorithms is deprecated and will be removed in a future release. You should use more secure algorithms in a production environment. For a list of supported hash algorithms, refer to [Salted Hash Algorithms](../security-guide/encoding-attribute-values.html#encoding-salted-hash).

## `JAVA_TYPE_DATE` attribute type

Support for the native attribute type, `JAVA_TYPE_DATE`, is deprecated and will be removed in a future release. This property-level extension is an alias for `string`. Any dates assigned to this extension should be formatted per ISO 8601.

## POST request with `?_action=patch`

Support for a POST request with `?_action=patch` is deprecated, when patching a specific resource. You can still use `?_action=patch` when patching by query on a collection.

Clients that do not support the regular PATCH verb should use the `X-HTTP-Method-Override` header instead.

For example, the following POST request uses the `X-HTTP-Method-Override` header to patch user jdoe's entry:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request POST \
--header "X-HTTP-Method-Override: PATCH" \
--data '[
    {
        "operation":"replace",
        "field":"/description",
        "value":"The new description for Jdoe"
    }
]' \
"http://localhost:8080/openidm/managed/user/jdoe"
```

## `minLength` property

The managed object property `minLength` is deprecated. When you need to specify a minimum length for a property, use the `minimum-length` policy:

```json
{
    "policyId" : "minimum-length",
    "params" : {
        "minLength" : 8
    }
}
```

## Read requests at top of `/config`

Support for top-level read requests to the `/config` endpoint is deprecated. You can still retrieve a list of config IDs by querying the `/config` endpoint.

## Defining object schema `type` attribute in an array when it is a single type

Support for specifying an object's schema `type` attribute in an array when there is only a single type is deprecated and will be removed in a later release.

This affects schemas with `type` attribute definitions in the form:

```json
{
    "type" : ["string"]
}
```

`type` attribute definitions in this form should be updated to:

```json
{
    "type" : "string"
}
```

For additional information, refer to the [JSON schema `type` attribute definition](https://datatracker.ietf.org/doc/html/draft-zyp-json-schema-03#anchor9).

---

---
title: Discontinued
description: Functionality removed from PingIDM across releases, including discontinued APIs, connectors, authentication modules, and configuration options
component: pingidm
version: 8.1
page_id: pingidm:release-notes:removed-functionality
canonical_url: https://docs.pingidentity.com/pingidm/8.1/release-notes/removed-functionality.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Compatibility"]
section_ids:
  idm_8_1_1: IDM 8.1.1
  idm_8_1: IDM 8.1
  java_17_support: Java 17 support
  idm_8_0: IDM 8.0
  removed-jettyxml: Jetty configuration
  removed-custom-servlet-filters-80: Custom servlet filters
  removed-trusted-attribute-auth-module: TRUSTED_ATTRIBUTE authentication module
  removed-tamper-evident-csv-audit: Embedded DS repository
  removed-felix-webconsole-80: Apache Felix web console
  removed-tamper-evident-csv-audit-80: Tamper protection for CSV audit logs
  removed-IWA-auth-80: Integrated Windows Authentication (IWA)
  removed-self-service-80: Standalone self-service
  removed-standalone-socialid-auth-80: Social authentication
  removed-standalone-prog-profile-80: Progressive profile
  samples: Samples
  getting_started_sample: Getting started sample
  synchronize_data_between_idm_and_docusign_sample: Synchronize data between IDM and DocuSign sample
  example_configurations: Example configurations
  idm_7_5: IDM 7.5
  java_11_support: Java 11 support
  idm_7_4: IDM 7.4
  sample_notification_configuration_files: Sample notification configuration files
  splunk_and_elasticsearch_audit_handlers: Splunk and Elasticsearch audit handlers
  idm_7_3: IDM 7.3
  idm_7_2: IDM 7.2
  oauth_client_authentication_module: OAUTH_CLIENT authentication module
  cli_update_command: CLI update command
  idm_7_1: IDM 7.1
  idm_7_0: IDM 7.0
  native_queries_using_queryexpression: Native queries using _queryExpression
  reloadscriptonexecution_for_scripted_groovy_connectors: reloadScriptOnExecution for Scripted Groovy connectors
  properties_from_boot_properties: Properties from boot.properties
  custom_aliases_for_default_keys: Custom aliases for default keys
  communication_protocol_for_connector_servers: Communication protocol for connector servers
  full_stack_sample: Full Stack sample
  obfuscating_and_encrypting_property_values: Obfuscating and encrypting property values
  self_service_registration_with_the_legacy_ui: Self-service registration with the legacy UI
  scriptedcrest_connector_and_sample: ScriptedCREST Connector and Sample
  office_365_connector: Office 365 Connector
  active_directory_connector: Active Directory Connector
  archive: Archive
---

# Discontinued

We've removed the following functionality. For previous releases, the information could be outdated or superseded.

## IDM 8.1.1

No features or functionality were removed in this release.

## IDM 8.1

### Java 17 support

Running IDM requires Java 21. Learn more in [Java requirements](before-you-install.html#prerequisites-java).

## IDM 8.0

### Jetty configuration

We've removed `jetty.xml` configuration in this release of IDM. The updated Jetty 12 configuration is replaced with a `webserver.json` file for global settings and a `webserver.listener-*.json` file to detect changes. Learn more in [Embedded Jetty configuration](../install-guide/appendix-jetty.html).

### Custom servlet filters

[Custom servlet filters](../install-guide/register-servlet-filters.html) aren't supported in IDM 8.0 and later. The only `servletfilter-*` configurations you can continue to use are `CrossOriginFilter` and `LargePayloadServletFilter`.

### TRUSTED\_ATTRIBUTE authentication module

We've removed the TRUSTED\_ATTRIBUTE authentication module in this release of IDM. This module depended on custom servlet filters, which are no longer supported. To achieve similar functionality, use PingGateway or the [rsFilter configuration](../auth-guide/rsfilter-auth.html) with bearer tokens.

### Embedded DS repository

The embedded DS repository is no longer included with IDM. Before you can use IDM, you must [select and configure a repository](../install-guide/chap-repository.html).

### Apache Felix web console

We've removed the Apache Felix web console in this release of IDM.

### Tamper protection for CSV audit logs

We've removed tamper protection for CSV audit logs in this release of IDM.

### Integrated Windows Authentication (IWA)

We've removed the IWA authentication module in this release of IDM. This feature is a function of PingAM.

### Standalone self-service

We've removed IDM standalone self-service and all self-service stages in this release. From IDM 7 onwards, this functionality is replaced by [AM Authentication Trees](https://docs.pingidentity.com/pingam/8.1/authentication-guide/about-authentication-trees.html).

|   |                                                                              |
| - | ---------------------------------------------------------------------------- |
|   | The admin UI link to self-service resulting in a 404 error is a known issue. |

### Social authentication

We've removed social authentication in this release of IDM. The feature is a function of AM. Once a user has logged in through AM (using a social provider or some other way), they can obtain an access token with that session and use the access token to interact with IDM through the [rsFilter configuration](../auth-guide/rsfilter-auth.html).

Additionally, Microsoft has deprecated the "Sign In with LinkedIn" functionality as of August 1, 2023. Refer to [Sign In with LinkedIn](https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/sign-in-with-linkedin).

### Progressive profile

We've removed progressive profile data collection in this release of IDM. This functionality is already supported by PingOne Advanced Identity Cloud and AM in a platform deployment. Learn more in:

* [Progressive profile](https://backstage.forgerock.com/docs/platform/7.2/platform-self-service/progressive-profile.html) in the Ping Identity Platform documentation.

* [Progressive profile](https://docs.pingidentity.com/pingoneaic/latest/self-service/progressive-profile.html) in the PingOne Advanced Identity Cloud documentation.

### Samples

We've removed the following samples and example configurations in this release.

#### Getting started sample

The `getting-started` sample is no longer included with IDM. Use [Synchronize data from a CSV file to IDM](../samples-guide/sync-with-csv.html) instead.

#### Synchronize data between IDM and DocuSign sample

The `sync-with-docusign` sample is no longer included with IDM. You can find more information in the [ICF documentation](https://docs.pingidentity.com/openicf/connector-release-notes/changed-functionality.html#1_5_20_22).

#### Example configurations

* `provisioner.openicf-engineering.json`

## IDM 7.5

### Java 11 support

Running IDM requires Java 17. Learn more in [Java requirements](before-you-install.html#prerequisites-java).

## IDM 7.4

### Sample notification configuration files

We've removed the following sample notification configuration files from the `/path/to/openidm/samples/example-configurations/conf` directory:

* `notification-newReport.json`

* `notification-termsUpdate.json`

### Splunk and Elasticsearch audit handlers

We've removed the Splunk and Elasticsearch audit event handlers in this release.

IDM 7.4 supports file-based audit handlers and logging to standard output, both of which Elasticsearch and Splunk can consume.

## IDM 7.3

No features or functionality were removed in this release.

## IDM 7.2

### `OAUTH_CLIENT` authentication module

The `OAUTH_CLIENT` authentication module has been removed. Using OAuth2 for authentication through AM is available with the [resource server filter](../auth-guide/rsfilter-auth.html) (`rsFilter`).

### CLI `update` command

The `cli.sh update` command (used in older releases to apply maintenance updates) has been removed in this release. Learn more about upgrading to the latest IDM release in the [Upgrade Guide](../upgrade-guide/preface.html). The ability to place a server in maintenance mode has also been removed.

## IDM 7.1

No features or functionality were removed in this release.

## IDM 7.0

### Native queries using `_queryExpression`

Native query expressions using the `_queryExpression` keyword are no longer supported on managed objects. You must rewrite any custom queries that use `_queryExpression` as regular [filtered queries](../objects-guide/queries.html#query-filters) or as [parameterized queries](../objects-guide/queries.html#parameterized-queries). Native query expressions are still supported for system objects.

### reloadScriptOnExecution for Scripted Groovy connectors

For scripted Groovy connectors, the `reloadScriptOnExecution` property has been removed from all sample provisioner files, as the property is not used by the connectors. To learn more about how scripts are loaded, refer to [Script compilation and caching](https://docs.pingidentity.com/openicf/connector-reference/groovy.html).

|   |                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | [Scripted PowerShell connectors](https://docs.pingidentity.com/openicf/connector-reference/powershell.html) still use the `ReloadScriptOnExecution` property to determine when a script is reloaded from disk. |

### Properties from `boot.properties`

The following properties have been removed from \<filename>resolver/boot.properties\</filename>:

* `openidm.script.javascript.debug`

* `openidm.script.javascript.sources`

* `openidm.ssl.host.aliases`

* `com.iplanet.am.cookie.name`

* `com.sun.identity.auth.cookieName`

### Custom aliases for default keys

You can no longer specify custom aliases for the default keys that IDM generates on startup. Learn more in [The IDM keystore](../security-guide/default-keystore.html).

### Communication protocol for connector servers

In previous IDM releases, the `protocol` property of a connector server configuration specified the communication protocol to the remote connector server. This property existed for legacy purposes and was set to `websocket` by default. The property has now been removed and connections to the remote connector server always use the `websocket` protocol.

### Full Stack sample

The "full stack sample" (*Integrating IDM With the ForgeRock Identity Platform*) has been removed. The only supported method of authentication through AM is by using AM bearer tokens and the `rsFilter` authentication module. Learn more in the [Platform Setup Guide](https://backstage.forgerock.com/docs/platform/7.5/platform-setup-guide/index.html).

### Obfuscating and encrypting property values

The ability to generate obfuscated and encrypted property values by using the crypto bundle has been removed. The secrets service replaces this functionality. Learn more in [Secret stores](../security-guide/secret-stores.html).

### Self-service registration with the legacy UI

When configuring self-service registration, the `idmUserDetails` stage had previously used the `identityResourceUrl` property instead of `identityServiceUrl`. This stage now correctly uses the `identityServiceUrl` property. `identityResourceUrl` has been removed.

### ScriptedCREST Connector and Sample

The ScriptedCREST connector and the corresponding sample have been removed in this release. Migrate any deployments that use this connector to the [Scripted REST connector](https://docs.pingidentity.com/openicf/connector-reference/scripted-rest.html).

### Office 365 Connector

Support for the Office 365 connector has been removed in this release. Instead of the Office 365 connector, use the [Microsoft Graph API connector](https://docs.pingidentity.com/openicf/connector-reference/ms-graph-api.html).

### Active Directory Connector

Support for the Active Directory (AD) .NET Connector has been removed.

* For simple Active Directory and Active Directory LDS deployments, use the [LDAP connector](https://docs.pingidentity.com/openicf/connector-reference/ldap.html).

* For more complex Active Directory deployments, use the [PowerShell connector toolkit](https://docs.pingidentity.com/openicf/connector-reference/powershell.html).

## Archive

For documentation and release information prior to IDM 7.0, check out the [Documentation Archive](https://docs.pingidentity.com/archive/).

---

---
title: Fixed issues
description: Highlighted fixes in PingIDM releases
component: pingidm
version: 8.1
page_id: pingidm:release-notes:fixes
canonical_url: https://docs.pingidentity.com/pingidm/8.1/release-notes/fixes.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Deployment", "Identities", "Compatibility", "Security"]
section_ids:
  idm_8_1_1: IDM 8.1.1
  idm_8_1: IDM 8.1
---

# Fixed issues

## IDM 8.1.1

The following highlighted issues were fixed in this release:

* OPENIDM-22101: Fixed an issue where the Jetty servlet WebSocket `idleTimeout` was set with an incorrect duration.

* OPENIDM-22524: Fixed a user enumeration vulnerability in the managed object `?_action=patch` endpoint that did not enforce authorization before evaluating query filters. Query authorization on the target resource collection is now required and is granted through access rules or delegated admin rules.

## IDM 8.1

The following highlighted bugs were fixed in this release:

* OPENIDM-20345: Managed objects no longer create a relationship for a valid property when an invalid property is provided.

* OPENIDM-20533: OpenICF Provisioner Service activation no longer fails permanently if a connector validate operation timeout occurs.

* OPENIDM-20863: Fixed an issue where non-primitive default values for mapping properties were passed by reference, allowing unintended mutation across sync invocations.

* OPENIDM-20995: Fixed a large increase in the volume of data fetched for static group patch operations to add a user.

* OPENIDM-21106: Fixed a task scanner failure on DB2 explicit tables caused by undersized VARCHAR(29) date columns.

* OPENIDM-21363: The webserver.listener-\*.json fields inputBufferSize and outputBufferSize now configure their intended Jetty buffers.

* OPENIDM-21421: Prevent IllegalStateException when updating provisioner config for inactive provisioners.

* OPENIDM-21454: Fixed an issue where the sync retry handler could exceed the configured retry limit.

* OPENIDM-21493: Clustered reconciliation now terminates properly when the connector is unavailable.

* OPENIDM-21675: Fixed a NullPointerException in ConnectorInfoProviderService during testConnectorServers when an RCS cluster group has an empty serversList.

* OPENIDM-21776: Fixed "Connection is closed" errors during large reconciliation operations between tenants via IDM external proxy.

---

---
title: Limitations
description: Known limitations in PingIDM, including Bouncy Castle FIPS, workflow, query filter, connector, and If-Match constraints
component: pingidm
version: 8.1
page_id: pingidm:release-notes:limitations
canonical_url: https://docs.pingidentity.com/pingidm/8.1/release-notes/limitations.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Deployment", "Identities", "Compatibility", "Security", "Query"]
section_ids:
  limitations-bouncy-castle-fips: Bouncy Castle FIPS with custom JVM
  limitations-workflow: Workflow limitations
  limitations-ds-repo: Queries with a DS repository
  limitations-oracle-repo: Queries with an OracleDB repository
  limitations-privileges: Queries with privileges
  limitations-connectors: Connector limitations
  limitations-if-match: If-Match requests
---

# Limitations

PingIDM 8.1 has the following known limitations:

## Bouncy Castle FIPS with custom JVM

You can't use the [Bouncy Castle FIPS](../security-guide/security-bouncy-castle-fips.html) provider with a custom JVM.

## Workflow limitations

* Workflows are not supported with a DS repository. If you are using a DS repository for IDM data, you must configure a separate JDBC repository as the [workflow datasource](../workflow-guide/enable-workflows.html#workflow-datasource).

* The embedded workflow and business process engine is based on Flowable and the Business Process and Notation (BPMN) 2.0 standard. As an embedded system, local integration is supported. Remote integration is not currently supported.

## Queries with a DS repository

For DS repositories, relationships must be defined in the repository configuration (`repo.ds.json`). If you do not explicitly define relationships in the repository configuration, you will be able to query those relationships, but filtering and sorting on those queries will not work. For more information, refer to [Relationship Properties in a DS Repository](../objects-guide/explicit-generic-mapping-ds.html#relationship-properties-ds).

## Queries with an OracleDB repository

For OracleDB repositories, queries that use the `queryFilter` syntax do not work on CLOB columns in explicit tables.

## Queries with privileges

Query filters used for privileges can only reference *direct* attributes of the object. For example, relationship fields cannot be referenced in a privilege filter.

## Connector limitations

When you add or edit a connector through the admin UI, the list of required `Base Connector Details` is not necessarily accurate for your deployment. Some of these details might be required for specific deployment scenarios only. If you need a connector configuration where not all the Base Connector Details are required, you must create your connector configuration file over REST or by editing the provisioner file. For more information, refer to [Configure connectors](https://docs.pingidentity.com/openicf/connector-reference/configure-connector.html).

## `If-Match` requests

A conditional GET request, with the `If-Match` request header, is not supported.

---

---
title: New features
description: New features and enhancements in PingIDM releases, including UI improvements, metrics, security, workflow, and infrastructure updates
component: pingidm
version: 8.1
page_id: pingidm:release-notes:whats-new
canonical_url: https://docs.pingidentity.com/pingidm/8.1/release-notes/whats-new.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Deployment", "Identities", "Compatibility", "Security"]
section_ids:
  maintenance-releases: Maintenance releases
  wn-related-releases: Related component releases
  wn-ad-pw-plugin-180: AD password synchronization plugin 1.8.0
  idm_8_1_1: IDM 8.1.1
  idm_8_1: IDM 8.1
  wn-end-user-ui-810: IDM end-user UI
  wn-platform-admin-ui-810: Platform admin UI for standalone IDM
  wn-cluster-standby-mode: Cluster standby mode
  wn-user-agent-property-810: openidm.http.client.userAgent property
  wn-flowable-upgrade-720-810: Workflow engine upgrade
  wn-quartz-scheduler252-810: Quartz Scheduler upgraded to 2.5.2
  wn-want-client-auth-810: wantClientAuth support for Jetty listeners
  enum_support: enum support
  wn-otel-logging-810: OpenTelemetry logging
  wn-otel-log-appender-810: OpenTelemetryAppender in logback.xml
  wn-sync-mappings-paging-810: Paging for the sync/mappings endpoint
  wn-task-scanner-exception-810: Improved task scanner exception handling
  wn-bc-fips-upgrade-810: Bouncy Castle FIPS upgrade
  wn-jetty-qos-handler-810: Jetty QoSHandler and configuration properties
  wn-jetty-qos-handler-metrics-810: Jetty QoSHandler metrics
  wn-sni-host-check-810: Jetty Server Name Indication (SNI) host check
  wn-jetty-metrics-810: Jetty thread pool and request metrics
  wn-atob-btoa-global-scripts-81: Base64 atob and btoa global script bindings
  wn-liveness-endpoint-810: Liveness endpoint
  wn-health-ready-endpoint-810: Readiness endpoint
  wn-connector-server-status-metric-810: Connector server status metric
  wn-pending-connector-request-metric-provisioner-tags-810: Pending connector request metric and provisioner metric tags
  idm_8_0_2: IDM 8.0.2
  wn-quartz-scheduler252-802: Quartz Scheduler upgraded to 2.5.2
  wn-user-agent-property-802: openidm.http.client.userAgent property
  wn-ds-81-supported-repo-802: DS 8.1 repository support
  wn-want-client-auth-802: wantClientAuth support for Jetty listeners
  wn-task-scanner-exception-handling-802: Improved task scanner exception handling
  idm_8_0_1: IDM 8.0.1
  wn-enduser-ui-801: End-user UI install guide
  wn-bc-fips-upgrade-801: Bouncy Castle FIPS upgrade
  wn-sni-host-check-801: Jetty Server Name Indication (SNI) host check
  idm_8_0: IDM 8.0
  wn-audit-watchedfields-wildcard-80: Wildcard support for activity audit watchedFields
  secure_rcs_access: Secure RCS access
  bouncy-castle-fips-1403-compliance: Bouncy Castle FIPS 140-3 compliance
  distributed-tracing-ot-80: Distributed tracing with OpenTelemetry
  jetty-12-support-80: Jetty 12 support
  new-array-comparison-80: Array comparison
  wn-logback: Logback
  java_21_support: Java 21 support
  new-health-endpoint-80: Audit-free health check
  new-icf-metrics-80: Additional metrics
  new-fs-automatic-encryption: Filesystem secret store automatic encryption
  secret-rotation-80: Store credentials as secrets
  wn-parameter-authorization-80: _api parameter requires authorization
  idm_7_5_3: IDM 7.5.3
  wn-quartz-scheduler252-753: Quartz Scheduler upgraded to 2.5.2
  wn-user-agent-property-753: openidm.http.client.userAgent property
  idm_7_5_2: IDM 7.5.2
  improved_task_scanner_exception_handling: Improved task scanner exception handling
  idm_7_5_1: IDM 7.5.1
  wn-parameter-authorization-751: _api parameter requires authorization
  secure_rcs_access_2: Secure RCS access
  new-array-comparison-751: Array comparison
  jetty-12-support-751: Jetty 12 support
  idm_7_5_0: IDM 7.5.0
  connectors: Connectors
  whats-new-international-email: International email addresses
  custom-relationships: Custom relationship properties
  secret-rotation: Store credentials as secrets
  secret-versioning: Version file system secrets
  enhanced-signal-propagation: Enhanced signal propagation
  whats-new-flowable-upgrade-680-75: Workflow engine upgrade
  connect_to_ds_with_scriptedrest_sample_supports_client_credentials_grant_type: Connect to DS with ScriptedREST sample supports client_credentials grant type
  end_user_ui_supports_array_properties: End User UI supports array properties
  idm_7_4_3: IDM 7.4.3
  improved_task_scanner_exception_handling_2: Improved task scanner exception handling
  idm_7_4_2: IDM 7.4.2
  international_email_addresses: International email addresses
  secure_rcs_access_3: Secure RCS access
  new-array-comparison-742: Array comparison
  wn-parameter-authorization-74: _api parameter requires authorization
  jetty-12-support-74: Jetty 12 support
  java-17-support-74: Java 17 support
  idm_7_4_1: IDM 7.4.1
  idm_7_4_0: IDM 7.4.0
  whats-new-filesystem-secrets: Filesystem secret stores
  whats-new-msgraph-email-client: Microsoft Graph API email client
  whats-new-metrics: Additional metrics
  new-script-countonly: Script support for countOnly queries
  mtls-auth-to-ds: mTLS for authentication to DS
  idm_7_3_3: IDM 7.3.3
  improved_task_scanner_exception_handling_3: Improved task scanner exception handling
  idm_7_3_2: IDM 7.3.2
  international_email_addresses_2: International email addresses
  secure_rcs_access_4: Secure RCS access
  new-array-comparison-732: Array comparison
  wn-parameter-authorization-73: _api parameter requires authorization
  jetty-12-support-73: Jetty 12 support
  java-17-support-73: Java 17 support
  idm_7_3_1: IDM 7.3.1
  whats-new-flowable-upgrade-680-73: Workflow engine upgrade
  end_user_ui_supports_array_properties_2: End User UI supports array properties
  idm_7_3_0: IDM 7.3.0
  whats-new-bouncy-castle-fips: Support for Bouncy Castle FIPS
  whats-new-prop-based-secret-stores: Support for UTF-8 email addresses
  disable_delegated_administrator_sort_and_filter_while_searching: Disable delegated administrator sort and filter while searching
  workflows_now_support_javascript: Workflows now support JavaScript
  patch_operation_improvements: Patch operation improvements
  improvements_to_the_system_endpoint: Improvements to the /system endpoint
  new_sync_mapping_configuration_fields: New sync mapping configuration fields
  idm_7_2_2: IDM 7.2.2
  support_for_upgrading_ds_to_later_version_than_idm: Support for upgrading DS to later version than IDM
  idm_7_2_1: IDM 7.2.1
  idm_7_2_0: IDM 7.2.0
  property_based_secret_stores: Property-based secret stores
  activate-deactivate-tasks: Scanning tasks to activate and deactivate accounts
  whats-new-sendTemplate-cc-bcc: external/email endpoint improvements
  whats-new-workflow: Workflow improvements
  policy_validation_for_field_removal: Policy validation for field removal
  relationship_derived_virtual_properties_rdvp_improvements: Relationship-derived Virtual Properties (RDVP) improvements
  ad_password_synchronization_plugin_utc_timestamps: AD Password Synchronization Plugin UTC timestamps
  bootstrap_idm_without_stored_configuration: Bootstrap IDM without stored configuration
  api_version_header_warnings: API version header warnings
  reconciliation_enhancements: Reconciliation enhancements
  assignment_synchronization_optimization: Assignment synchronization optimization
  query_filtering_on_arrays: Query filtering on arrays
  additional_metrics: Additional metrics
  idm_7_1_6: IDM 7.1.6
  idm_7_1_4: IDM 7.1.4
  idm_7_1_2: IDM 7.1.2
  idm_7_1: IDM 7.1
  sample_connection_to_azure_ad_with_the_ms_graph_api_connector: Sample connection to Azure AD with the MS Graph API connector
  password_sync_plugins: Password sync plugins
  active_directory_password_synchronization_plugin_utc_timestamps: Active Directory Password Synchronization Plugin UTC timestamps
  active_directory_password_synchronization_plugin_infinite_loop_prevention: Active Directory Password Synchronization Plugin infinite loop prevention
  active_directory_password_synchronization_plugin_configurable_max_retries: Active Directory Password Synchronization Plugin configurable max retries
  active_directory_password_synchronization_plugin_search_filter: Active Directory Password Synchronization Plugin search filter
  support_for_am_bearer_tokens_in_the_ds_and_active_directory_password_synchronization_plugins: Support for AM Bearer Tokens in the DS and Active Directory Password Synchronization Plugins
  support_for_alternative_kba_answer_hashing: Support for alternative KBA answer hashing
  managed_object_default_values: Managed object default values
  support_for_rest_queries_on_array_properties_jdbc: Support for REST queries on array properties (JDBC)
  waitforcompletion_property_added_to_the_config_endpoint: waitForCompletion property added to the config endpoint
  api_endpoint_requires_admin_authentication: API endpoint requires admin authentication
  additional_query_types_in_jdbc_explicit_tables: Additional query types in JDBC explicit tables
  idm_7_0_4: IDM 7.0.4
  idm_7_0_3: IDM 7.0.3
  idm_7_0_2: IDM 7.0.2
  idm_7_0_1: IDM 7.0.1
  idm_7: IDM 7
  password_sync_plugins_2: Password sync plugins
  active_directory_password_synchronization_plugin_utc_timestamps_2: Active Directory Password Synchronization Plugin UTC timestamps
  active_directory_password_synchronization_plugin_infinite_loop_prevention_2: Active Directory Password Synchronization Plugin infinite loop prevention
  active_directory_password_synchronization_plugin_configurable_max_retries_2: Active Directory Password Synchronization Plugin configurable max retries
  active_directory_password_synchronization_plugin_search_filter_2: Active Directory Password Synchronization Plugin search filter
  support_for_am_bearer_tokens_in_the_ds_and_active_directory_password_synchronization_plugins_2: Support for AM Bearer Tokens in the DS and Active Directory Password Synchronization Plugins
  access_configuration_over_rest: Access configuration over REST
  privilege_dynamic_filters: Privilege dynamic filters
  configurable_http_io_request_buffer: Configurable HTTP I/O request buffer
  filter_expanded_relationships: Filter expanded relationships
  deterministic_ecdsa_signatures_for_jwt: Deterministic ECDSA signatures for JWT
  debugging_information_for_groovy_scripts: Debugging information for Groovy scripts
  rest_api_versioning: REST API Versioning
  support_for_am_bearer_tokens: Support for AM bearer tokens
  notification_property_now_configurable: Notification property now configurable
  reconciliation_association_information: Reconciliation Association Information
  profile_completeness_endpoint: Profile completeness endpoint
  audit_logging_safelist: Audit logging safelist
  in_clause_for_queries: in clause for queries
  disposal_of_idle_poolable_connector_instances_icf: Disposal of idle poolable connector instances (ICF)
  separate_mapping_configuration_files: Separate mapping configuration files
  queued_sync_retry: Queued sync retry
  material_design_icon_added_to_managed_object_configuration: Material Design Icon added to managed object configuration
  additional_query_types_in_jdbc_explicit_tables_2: Additional query types in JDBC explicit tables
  config_properties_additions: config.properties additions
  archive: Archive
  security-advisories: Security advisories
---

# New features

## Maintenance releases

Ping Identity maintenance releases contain a collection of fixes and minor enhancements grouped together and released as part of our commitment to support our customers.

IDM 8.1.1 is the latest release targeted for IDM 8.1 deployments and can be downloaded from the [Backstage Download Center](https://backstage.forgerock.com/downloads/browse/idm/latest).

|   |                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can deploy the release as an initial deployment or as an update from an existing 8.1.x deployment. Learn more about updating from 8.1.x in [Update to a maintenance release](../upgrade-guide/update-maintenance-release.html). |

For previous releases, the information could be outdated or superseded.

## Related component releases

The following component, distributed separately from IDM, has a new version available:

### AD password synchronization plugin 1.8.0

[AD password synchronization plugin 1.8.0](https://product-downloads.pingidentity.com/browse/idm/featured/get/familyId:idm/productId:idm-password-sync-plugins/minorVersion:1.8/version:1.8.0/releaseType:full/distribution:exe) is available as a separate download from the [Backstage download site](https://backstage.forgerock.com/downloads). This release fixes an issue that could cause the domain controller to restart unexpectedly during consecutive password changes. Learn more about the [AD password synchronization plugin](../pwd-plugin-guide/install-ad-pwd-sync.html).

## IDM 8.1.1

This release includes updates to ICF connectors, updates to dependency libraries, and bug fixes.

## IDM 8.1

### IDM end-user UI

A new IDM end-user UI is available from the [Backstage download site](https://backstage.forgerock.com/downloads). Deploy it behind a standalone Nginx server or as a Docker container built from the included `Dockerfile`.

Learn more in [Install the end-user UI](../setup-guide/idm-enduser-ui.html).

### Platform admin UI for standalone IDM

Standalone IDM now supports the Platform admin UI, the same UI used in Ping Identity Platform and PingOne Advanced Identity Cloud deployments. Download it as a separate artifact from the [Backstage download site](https://backstage.forgerock.com/downloads) and deploy it behind a standalone Nginx server or as a Docker container built from the included `Dockerfile`.

Learn more in [Install the Platform admin UI for standalone IDM](../setup-guide/platform-admin-ui.html).

### Cluster standby mode

You can configure IDM instances to boot in standby mode, where they don't process schedules, clustered reconciliation, or queued sync operations. Use the `openidm/cluster/active` endpoint to transition nodes between active and standby states on demand.

Learn more in:

* [Cluster standby mode](../install-guide/cluster-standby.html)

* [Cluster activation endpoint](../rest-api-reference/endpoints/rest-cluster-active.html)

### `openidm.http.client.userAgent` property

The `openidm.http.client.userAgent` property lets you customize the `User-Agent` header sent with [HTTP client](../setup-guide/http-client-config.html#new-user-agent-property) requests. If not specified, the default `"PingIdentity"` value is used. Request-level headers take precedence over both the IDM configuration and the default value. Learn more in [External REST configuration properties](../external-services-guide/external-rest.html#external-rest-properties-user-agent).

### Workflow engine upgrade

The Flowable embedded workflow engine has been upgraded to [version 7.2.0](https://github.com/flowable/flowable-engine/releases/tag/flowable-7.2.0).

If you're upgrading from a previous version of IDM and use workflow, this upgrade requires one or more incremental [upgrade scripts](../upgrade-guide/update-repo.html#upgrade-existing-repository).

### Quartz Scheduler upgraded to 2.5.2

The embedded Quartz Scheduler has been upgraded from version 2.3.2 to 2.5.2. This upgrade doesn't require any configuration change.

### `wantClientAuth` support for Jetty listeners

A new setting, `wantClientAuth`, is available for `webserver.listener-*.json` configuration files to allow the server to request a client certificate during the TLS handshake without requiring it. This enables support for mixed traffic, allowing clients with or without certificates to connect on the same port. If a client provides a certificate, it must be valid; otherwise, the handshake fails.

Learn more:

* [Enable mixed client authentication](../security-guide/chap-connections.html#mixed-client-auth)

* [Jetty property reference](../install-guide/idm-config-properties-jetty.html#jetty-property-reference)

### `enum` support

Support for [managed object schema enumerations](../objects-guide/creating-modifying-managed-objects.html#enum-managed-object) in string and number attributes. To make an attribute an enumeration, add `"enum" : [ "one", "two", "three" ]` to the attribute.

### OpenTelemetry logging

IDM now supports OpenTelemetry logging, which allows you to export logs in the [OpenTelemetry Protocol (OTLP)](https://github.com/open-telemetry/opentelemetry-proto/tree/main/docs) to an [OpenTelemetry collector](https://opentelemetry.io/docs/collector/). This is an evolving feature ([1](appendix-interface-stability.html#interface-stability)). Learn more in [OpenTelemetry logging](../monitoring-guide/opentelemetry-logging.html).

### `OpenTelemetryAppender` in `logback.xml`

IDM now supports the `OpenTelemetryAppender` in the `logback.xml` configuration file. This appender writes formatted JSON logs to a collector using the OTLP protocol. Learn more in [Log appenders](../monitoring-guide/server-logs.html#log-appenders).

### Paging for the `sync/mappings` endpoint

The `sync/mappings` endpoint now supports paging to better display large numbers of mappings. You can retrieve results in manageable chunks by using the `_pageSize` parameter with either cookie-based (`_pagedResultsCookie`) or offset-based (`_pagedResultsOffset`) paging.

Learn more in [Paging synchronization mapping results](../synchronization-guide/mappings.html#sync-mapping-paging).

### Improved task scanner exception handling

If the task scanner encounters a task that results in an exception, it now aborts only that task and continues processing the remaining tasks. Previously, the scanner would abort the entire process when any task caused an exception.

### Bouncy Castle FIPS upgrade

The `bc-fips-2.1.2` library is now available. Learn more in [Download the Bouncy Castle libraries](../security-guide/security-bouncy-castle-fips.html#download-bouncy-castle-libraries).

### Jetty QoSHandler and configuration properties

IDM now includes the [Jetty QoSHandler](https://jetty.org/docs/jetty/12/programming-guide/server/http.html#handler-use-qos) to limit the number of active concurrent requests. The handler is configured to use all but two threads to ensure requests to critical endpoints are always handled.

New QoSHandler configuration properties are available in `webserver.json` to control the maximum number of requests and the amount of time a request can remain in the handler's queue: `maxQueueSize` and `maxRequestSuspendTime`.

Learn more in [Jetty QoSHandler](../install-guide/idm-config-properties-jetty.html#config-jetty-qos-handler) and in [Jetty property reference](../install-guide/idm-config-properties-jetty.html#jetty-property-reference).

### Jetty QoSHandler metrics

IDM's [metric collection endpoints](../monitoring-guide/metrics.html) now include [Jetty QoSHandler](../install-guide/idm-config-properties-jetty.html#config-jetty-qos-handler) metrics. Learn more about the [API](../monitoring-guide/api-metrics.html#api-jetty-qos-queue-count) and [Prometheus](../monitoring-guide/prometheus-metrics.html#prometheus-jetty-qos-queue-count) metrics that track the QoSHandler queue.

### Jetty Server Name Indication (SNI) host check

A new setting, `sniHostCheckEnabled`, is available in the `webserver.listener-*.json` configuration files to control the Jetty SNI host check. Although not recommended for security reasons, disabling this check might be necessary in certain proxy configurations, such as SSL pass-through.

Learn more in [Disable SNI host check](../security-guide/chap-connections.html#sni-host-check).

### Jetty thread pool and request metrics

IDM's [metric collection endpoints](../monitoring-guide/metrics.html) now include Jetty thread pool and request metrics. Learn more in [API Jetty metrics](../monitoring-guide/api-metrics.html#api-jetty-metric-names) and [Prometheus Jetty metrics](../monitoring-guide/prometheus-metrics.html#prometheus-jetty-metric-names).

### Base64 `atob` and `btoa` global script bindings

IDM now includes `atob` (Base64-decode) and `btoa` (Base64-encode) as global script bindings. This update provides common JavaScript utilities for Base64 operations, mitigating potential class-loading issues associated with using native Java packages or classes for these functions.

Learn more in:

* [Global utility functions](../scripting-guide/scripting-func-ref.html#global-utility-functions)

* [Example script eval Base64 encode/decode](../rest-api-reference/endpoints/rest-scripts.html#script-base64-example)

### Liveness endpoint

A new liveness endpoint, `openidm/health/live`, is available to indicate whether the IDM instance is running. This endpoint can be used in containerized environments, such as Kubernetes, to determine when to restart a container.

The endpoint returns a `200 OK` status when IDM's required bundles are installed and started. Otherwise, it returns a `503 Service Unavailable` status.

Learn more in [Liveness probe](../install-guide/system-healthcheck.html#liveness-probe).

### Readiness endpoint

A new [readiness endpoint](../install-guide/system-healthcheck.html#readiness-probe), `openidm/health/ready`, is available to indicate whether the IDM instance is ready. This endpoint can be used in containerized environments, such as Kubernetes, to determine when a container is ready to accept traffic.

The endpoint returns an HTTP `503` status code when the health check readiness state is `TEMPORARILY_UNAVAILABLE`, `CRITICAL`, or `HEALTHCHECK_UNKNOWN`.

### Connector server status metric

A new metric is available to monitor the status of connector servers. This metric indicates whether a connector server is running (`1`) or not running (`0`), providing a way to track connector server health without making a POST call to the `system?_action=testConnectorServers` endpoint.

* [API metric](../monitoring-guide/prometheus-metrics.html#prometheus-metric-names): `icf_connector_server_availability.rcsName.rcsType`

* [Prometheus metric](../monitoring-guide/prometheus-metrics.html#prometheus-metric-names): `idm_icf_connector_server_availability`

### Pending connector request metric and provisioner metric tags

IDM's [metric collection endpoints](../monitoring-guide/metrics.html) include a new metric to monitor the number of pending connector requests over the configured limit. The provisioner service also includes `connector_type`, `bundle_version`, and `location` metric tags.

|   |                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------ |
|   | Pending request gauges won't register until the associated `RequestType` has been invoked at least one time. |

* [API metric](../monitoring-guide/api-metrics.html#icf-pending-provisioner-metric): `icf_pending.{connector-type}.{bundle-version}.{location}`

* [Prometheus metric](../monitoring-guide/prometheus-metrics.html#idm-icf-pending-metric): `idm_icf_pending{bundle_version="{bundle_version}",connector="{connector}",connector_type="{connector_type}",location="{location}",operation="{operation}",system_identifier="{system_identifier}"}`

## IDM 8.0.2

### Quartz Scheduler upgraded to 2.5.2

The embedded Quartz Scheduler has been upgraded from version 2.3.2 to 2.5.2. This upgrade doesn't require any configuration change.

### `openidm.http.client.userAgent` property

The `openidm.http.client.userAgent` property lets you customize the `User-Agent` header sent with [HTTP client](../setup-guide/http-client-config.html#new-user-agent-property) requests. If not specified, the default `"PingIdentity"` value is used. Request-level headers take precedence over both the IDM configuration and the default value. Learn more in [External REST configuration properties](../external-services-guide/external-rest.html#external-rest-properties-user-agent).

### DS 8.1 repository support

DS 8.1 is now a supported repository for IDM 8.0.2. This lets you upgrade DS to 8.1 while continuing to run IDM 8.0.x, easing the transition to IDM 8.1.

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | DS 8.1 compatibility lets you upgrade DS before upgrading IDM to 8.1. Don't mix and match IDM and DS versions long term. |

Learn more in [Supported repositories](before-you-install.html#prerequisites-repositories).

### `wantClientAuth` support for Jetty listeners

A new setting, `wantClientAuth`, is available for `webserver.listener-*.json` configuration files to allow the server to request a client certificate during the TLS handshake without requiring it. This enables support for mixed traffic, allowing clients with or without certificates to connect on the same port. If a client provides a certificate, it must be valid; otherwise, the handshake fails.

Learn more:

* [Enable mixed client authentication](../security-guide/chap-connections.html#mixed-client-auth)

* [Jetty property reference](../install-guide/idm-config-properties-jetty.html#jetty-property-reference)

### Improved task scanner exception handling

If the task scanner encounters a task that results in an exception, it now aborts only that task and continues processing the remaining tasks. Previously, the scanner would abort the entire process when any task caused an exception.

## IDM 8.0.1

### End-user UI install guide

The IDM end-user UI is available as a standalone downloadable artifact (`PingIDM-Enduser-UI-8.1.0.zip`) from the [Backstage download site](https://backstage.forgerock.com/downloads). For IDM 8.0.x deployments, use the end-user UI 8.1.0 artifact.

Learn more in [Install the end-user UI](../setup-guide/idm-enduser-ui.html).

### Bouncy Castle FIPS upgrade

The `bc-fips-2.1.2` library is now available. Learn more in [Download the Bouncy Castle libraries](../security-guide/security-bouncy-castle-fips.html#download-bouncy-castle-libraries).

### Jetty Server Name Indication (SNI) host check

A new setting, `sniHostCheckEnabled`, is available in the `webserver.listener-*.json` configuration files to control Jetty's SNI host check. Although not recommended for security reasons, disabling this check might be necessary in certain proxy configurations, such as SSL pass-through.

Learn more in [Disable SNI host check](../security-guide/chap-connections.html#sni-host-check).

## IDM 8.0

### Wildcard support for activity audit `watchedFields`

The `watchedFields` property in `conf/audit.json` now accepts a wildcard value (`["*"]`), which tells IDM to track changes to all managed object fields without listing them individually. Learn more in [Monitor specific activity log changes](../audit-guide/activity-log-watch-fields.html).

### Secure RCS access

You can create stricter RCS authorization and access rules. To enable authorization for RCS, add an appropriate role to the static-user mapping used for the RCS subject and write the appropriate access rules to permit this role to be granted access to the `openicf` servlet on the path (pattern) corresponding to the RCS name used in the RCS configuration.

Learn more in [Secure RCS access](../auth-guide/authorization-and-roles.html#secure-openicf-access).

### Bouncy Castle FIPS 140-3 compliance

You can configure PingIDM to meet Federal Information Processing Standard (FIPS) 140-3 compliance standards. Learn more in [FIPS 140-3 compliance](../security-guide/security-bouncy-castle-fips.html).

### Distributed tracing with OpenTelemetry

You can run a distributed trace in PingIDM using OpenTelemetry and export the data to an external trace collector for telemetry storage and visualization.

Learn more in [Distributed tracing](../monitoring-guide/distributed-tracing.html).

### Jetty 12 support

The embedded Jetty web server supports Jetty 12. Instead of `jetty.xml`, the updated configuration uses a `webserver.json` for global settings and a `webserver.listener-*.json` to detect changes. Learn more in [Embedded Jetty configuration](../install-guide/appendix-jetty.html).

|   |                                                                                                                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When serving SSL requests, Jetty 12 checks that the incoming host header matches the server certificate's subject and returns a `400 Bad Request` error on a mismatch. If you're upgrading to IDM 8.0, you must ensure your IDM server certificate subject matches the host name used by your deployment. |

### Array comparison

You can choose how synchronization detects managed object array changes using *unordered* or *ordered* comparison using the configuration property `comparison` in the schema. Unordered JSON array comparison ignores the order of elements and can negate the need for certain custom scripts within mappings.

Learn more about [managed object schema properties](../objects-guide/appendix-managed-objects.html#managed-object-property-config-properties) and [array comparison](../synchronization-guide/chap-implicit-live-sync.html#array-comparison).

### Logback

IDM now uses Logback to generate server logs. Learn more in [Server logs](../monitoring-guide/server-logs.html).

### Java 21 support

You can run IDM with Java 21. Learn more in [Java requirements](before-you-install.html#prerequisites-java).

### Audit-free health check

To verify the current server state without generating audit logs, use the new `openidm/health` endpoint. Learn more in [Audit-free health check](../install-guide/system-healthcheck.html#audit-free-health-check).

### Additional metrics

New metrics are available for [ICF operations](../monitoring-guide/api-metrics.html#new-icf-metrics).

### Filesystem secret store automatic encryption

You can [configure automatic encryption](../security-guide/secret-stores-filesystem.html#fs-automatic-encryption) of your filesystem secret store.

### Store credentials as secrets

You can store credentials for many services as secrets. The list of supported services has been expanded to include:

* [Prometheus](../security-guide/secret-stores.html#secret-rotation-prometheus)

* [Hikari connection pooling datasource](../security-guide/secret-stores.html#secret-rotation-hikari)

* [External email services that use the MS Graph API](../external-services-guide/email.html#secret-rotation-email)

* [HTTP client proxy](../setup-guide/http-client-config.html)

Learn more in [Secret stores](../security-guide/secret-stores.html).

### `_api` parameter requires authorization

Requests passing the `_api` parameter now require authorization. Learn more in [Common REST](../crest/about-crest.html#api-authorize-example).

## IDM 7.5.3

### Quartz Scheduler upgraded to 2.5.2

The embedded Quartz Scheduler has been upgraded from version 2.3.2 to 2.5.2. This upgrade doesn't require any configuration change.

### `openidm.http.client.userAgent` property

The `openidm.http.client.userAgent` property lets you customize the `User-Agent` header sent with [HTTP client](../setup-guide/http-client-config.html#new-user-agent-property) requests. If not specified, the default `"PingIdentity"` value is used. Request-level headers take precedence over both the IDM configuration and the default value. Learn more in [External REST configuration properties](../external-services-guide/external-rest.html#external-rest-properties-user-agent).

## IDM 7.5.2

This release includes updates to ICF connectors, updates to dependency libraries, bug fixes, and the following feature:

### Improved task scanner exception handling

If the task scanner encounters a task that results in an exception, it now aborts only that task and continues processing the remaining tasks. Previously, the scanner would abort the entire process when any task caused an exception.

## IDM 7.5.1

### `_api` parameter requires authorization

Requests passing the `_api` parameter now require authorization. Learn more in [Common REST](../crest/about-crest.html#api-authorize-example).

### Secure RCS access

You can create stricter RCS authorization and access rules. To enable authorization for RCS, add an appropriate role to the static-user mapping used for the RCS subject and write the appropriate access rules to permit this role to be granted access to the `openicf` servlet on the path (pattern) corresponding to the RCS name used in the RCS configuration.

Learn more in [Secure RCS access](../auth-guide/authorization-and-roles.html#secure-openicf-access).

### Array comparison

You can choose how synchronization detects managed object array changes using *unordered* or *ordered* comparison using the configuration property `comparison` in the schema. Unordered JSON array comparison ignores the order of elements and can negate the need for certain custom scripts within mappings.

Learn more about [managed object schema properties](../objects-guide/appendix-managed-objects.html#managed-object-property-config-properties) and [array comparison](../synchronization-guide/chap-implicit-live-sync.html#array-comparison).

### Jetty 12 support

The embedded Jetty web server supports Jetty 12.

## IDM 7.5.0

### Connectors

Connectors continue to be updated and released outside of IDM. To stay up-to-date with new features and versions, check out the [ICF Release notes](https://docs.pingidentity.com/openicf/connector-release-notes/preface.html).

Although not bundled in this release of IDM, the two newest connectors are available to download from [Backstage](https://backstage.forgerock.com/downloads/):

* [PingOne connector documentation](https://docs.pingidentity.com/openicf/connector-reference/pingone.html)

* [Webex connector documentation](https://docs.pingidentity.com/openicf/connector-reference/webex.html)

### International email addresses

IDM now supports [international email addresses](https://en.wikipedia.org/wiki/International_email). This feature is only available for supporting SMTP providers.

For more information, refer to [International email addresses](../external-services-guide/email.html#international-email-address).

### Custom relationship properties

You can create custom relationship properties in the [admin UI](../objects-guide/relationships-custom.html) or with the [REST API](../rest-api-reference/endpoints/rest-schema.html).

### Store credentials as secrets

You can store credentials for a number of services as secrets. The supported services include:

* [DS using mTLS](../install-guide/external-ds.html#secret-rotation-mtls)

* [rsFilter](../security-guide/secret-stores.html#secret-rotation-rsfilter)

* [Email service](../security-guide/secret-stores.html#secret-rotation-email)

* [Connectors with encrypted credentials](../security-guide/secret-stores.html#secret-rotation-connectors)

For more information, refer to [Secret stores](../security-guide/secret-stores.html).

### Version file system secrets

You can have multiple versions of secrets stored in a file system secret store.

For more information, refer to [Filesystem secret stores](../security-guide/secret-stores-filesystem.html).

### Enhanced signal propagation

Managed objects can now receive relationship graph topology change signals through the `SignalPropagationCalculator` class that is active by default.

Learn more in [Enhanced signal propagation](../objects-guide/managed-object-virtual-properties.html#virtual-properties-enhanced-signal-propagation).

### Workflow engine upgrade

The Flowable embedded workflow engine has been upgraded to [version 6.8.0](https://github.com/flowable/flowable-engine/releases/tag/flowable-6.8.0). If you are upgrading from a previous version of IDM and use workflow, this upgrade requires one or more incremental upgrade scripts. For more information, refer to [Upgrade an existing repository](../upgrade-guide/update-repo.html#upgrade-existing-repository).

### [Connect to DS with ScriptedREST](../samples-guide/scripted-rest-with-dj.html) sample supports `client_credentials` grant type

The customizer script for the [Connect to DS with ScriptedREST](../samples-guide/scripted-rest-with-dj.html) sample now includes OAuth capabilities for the `client_credentials` grant type.

### End User UI supports array properties

Array properties now display in the End User UI.

## IDM 7.4.3

This release includes updates to ICF connectors, updates to dependency libraries, bug fixes, and the following feature:

### Improved task scanner exception handling

If the task scanner encounters a task that results in an exception, it now aborts only that task and continues processing the remaining tasks. Previously, the scanner would abort the entire process when any task caused an exception.

## IDM 7.4.2

### International email addresses

IDM now supports [international email addresses](https://en.wikipedia.org/wiki/International_email). This feature is available only for supporting SMTP providers.

For more information, refer to [International email addresses](../external-services-guide/email.html#international-email-address).

### Secure RCS access

You can create stricter RCS authorization and access rules. To enable authorization for RCS, add an appropriate role to the static-user mapping used for the RCS subject and write the appropriate access rules to permit this role to be granted access to the `openicf` servlet on the path (pattern) corresponding to the RCS name used in the RCS configuration.

Learn more in [Secure RCS access](../auth-guide/authorization-and-roles.html#secure-openicf-access).

### Array comparison

You can choose how synchronization detects managed object array changes using *unordered* or *ordered* comparison using the configuration property `comparison` in the schema. Unordered JSON array comparison ignores the order of elements and can negate the need for certain custom scripts within mappings.

Learn more about [managed object schema properties](../objects-guide/appendix-managed-objects.html#managed-object-property-config-properties) and [array comparison](../synchronization-guide/chap-implicit-live-sync.html#array-comparison).

### `_api` parameter requires authorization

Requests passing the `_api` parameter now require authorization. Learn more in [Common REST](../crest/about-crest.html#api-authorize-example).

### Jetty 12 support

The embedded Jetty web server supports Jetty 12.

### Java 17 support

This IDM release requires Java 17. Learn more in [Embedded Jetty configuration](../install-guide/appendix-jetty.html).

## IDM 7.4.1

* The Flowable embedded workflow engine has been upgraded to version 6.8.0.

* End user UI supports array properties.

* SalesForce connector supports `client_credentials` and `refresh_token` grant types.

## IDM 7.4.0

### Filesystem secret stores

You can now configure secret stores to use filesystem secret stores. Filesystem secret stores use a directory containing many files, each storing a single secret. For more information, refer to [Filesystem secret stores](../security-guide/secret-stores-filesystem.html).

### Microsoft Graph API email client

In addition to the SMTP client, you can now configure the outbound email service to use the new MS Graph API Client.

|   |                                                                                    |
| - | ---------------------------------------------------------------------------------- |
|   | Use of the new email client requires a properly configured Microsoft Azure tenant. |

For more information, refer to [Outbound email service](../external-services-guide/email.html).

### Additional metrics

New metrics are available for [livesync](../monitoring-guide/api-metrics.html#new-livesync-metric) and [scheduler functions](../monitoring-guide/api-metrics.html#api-scheduler-metric-names). For example requests, refer to [Scheduler metrics](../schedules-guide/schedule-metrics.html).

### Script support for `countOnly` queries

Queries within scripts now support the `_countOnly` parameter.

### mTLS for authentication to DS

If you're using IDM with a DS repository, ForgeRock recommends using mTLS to authenticate to DS to better facilitate credential rotation. Refer to [Configure mTLS](../install-guide/external-ds.html#external-ds-mtls).

## IDM 7.3.3

This release includes updates to ICF connectors, updates to dependency libraries, bug fixes, and the following feature:

### Improved task scanner exception handling

If the task scanner encounters a task that results in an exception, it now aborts only that task and continues processing the remaining tasks. Previously, the scanner would abort the entire process when any task caused an exception.

## IDM 7.3.2

### International email addresses

IDM now supports [international email addresses](https://en.wikipedia.org/wiki/International_email). This feature is available only for supporting SMTP providers.

For more information, refer to [International email addresses](../external-services-guide/email.html#international-email-address).

### Secure RCS access

You can create stricter RCS authorization and access rules. To enable authorization for RCS, add an appropriate role to the static-user mapping used for the RCS subject and write the appropriate access rules to permit this role to be granted access to the `openicf` servlet on the path (pattern) corresponding to the RCS name used in the RCS configuration.

Learn more in [Secure RCS access](../auth-guide/authorization-and-roles.html#secure-openicf-access).

### Array comparison

You can choose how synchronization detects managed object array changes using *unordered* or *ordered* comparison using the configuration property `comparison` in the schema. Unordered JSON array comparison ignores the order of elements and can negate the need for certain custom scripts within mappings.

Learn more about [managed object schema properties](../objects-guide/appendix-managed-objects.html#managed-object-property-config-properties) and [array comparison](../synchronization-guide/chap-implicit-live-sync.html#array-comparison).

### `_api` parameter requires authorization

Requests passing the `_api` parameter now require authorization. Learn more in [Common REST](../crest/about-crest.html#api-authorize-example).

### Jetty 12 support

The embedded Jetty web server supports Jetty 12.

### Java 17 support

This IDM release requires Java 17. Learn more in [Embedded Jetty configuration](../install-guide/appendix-jetty.html).

## IDM 7.3.1

### Workflow engine upgrade

The Flowable embedded workflow engine has been upgraded to [version 6.8.0](https://github.com/flowable/flowable-engine/releases/tag/flowable-6.8.0). If you're upgrading from a previous version of IDM and use workflow, this upgrade requires one or more incremental upgrade scripts. For more information, refer to [Upgrade an existing repository](../upgrade-guide/update-repo.html#upgrade-existing-repository).

### End User UI supports array properties

Array properties now display in the End User UI.

## IDM 7.3.0

### Support for Bouncy Castle FIPS

IDM now supports the use of Bouncy Castle FIPS as a security provider. Bouncy Castle FIPS is useful when dealing with government data, where meeting the FIPS 140-2 security requirement is necessary for regulatory compliance.

For information on how to configure Bouncy Castle, refer to [FIPS 140-3 compliance](../security-guide/security-bouncy-castle-fips.html).

### Support for UTF-8 email addresses

IDM now supports UTF-8 (non-ASCII/international) characters in email addresses, such as **zoë@example.com**. When sending emails to these type of addresses, the configured SMTP server must also support UTF-8.

### Disable delegated administrator sort and filter while searching

You can now disable delegated administrator sort and filter while searching resource collections in the End User UI. For more information, refer to [Disable sort and filter for resource collections](../auth-guide/delegated-admin.html#disable_sort_and_filter_for_resource_collections).

### Workflows now support JavaScript

IDM workflows now support JavaScript in addition to Groovy. For more information about scripting workflows, refer to [BPMN 2.0 and workflow tools](../workflow-guide/about-workflow-tools.html).

### Patch operation improvements

It is now possible to patch the root of an object. The only supported patch operations on the root of an object are `remove` and `replace`.

### Improvements to the /system endpoint

`/system` endpoints now support specifying additional fields when also using `*`. This allows callers to get fields that are not returned by default.

### New sync mapping configuration fields

New sync mapping configuration fields, `defaultSourceFields` and `defaultTargetFields`, allow specifying which fields to use for read and query requests made on source and target resource collections.

## IDM 7.2.2

This release includes updates to ICF connectors, updates to dependency libraries, bug fixes, and the following new feature:

### Support for upgrading DS to later version than IDM

Upgrading to DS 7.3 is now supported. For more information, refer to [Supported repositories](before-you-install.html#prerequisites-repositories).

## IDM 7.2.1

This release includes updates to ICF connectors, updates to dependency libraries, and bug fixes.

## IDM 7.2.0

This release of PingIDM software includes the following new features:

### Property-based secret stores

IDM now supports *property-based secret stores* and can read keys and trusted certificates from properties that contain keys in Privacy-Enhanced Mail (PEM) format.

For more information, see [Property secret stores](../security-guide/secret-stores-property.html).

### Scanning tasks to activate and deactivate accounts

The default IDM configuration now includes two scanning tasks that *activate* and *deactivate* a user's `accountStatus`, based on their `activeDate` and `inactiveDate`. For more information, see [Activate and deactivate accounts](../schedules-guide/activate-deactivate-tasks.html).

### `external/email` endpoint improvements

You can now use `cc` and `bcc` parameters with the `sendTemplate` action. For more information, see:

* [openidm.action](../scripting-guide/scripting-func-ref.html#function-action)

* [Outbound email service](../external-services-guide/email.html)

### Workflow improvements

The Flowable embedded workflow engine has been upgraded to version 6.6.0. This upgrade fixes the issue with [native email tasks](https://github.com/flowable/flowable-engine/issues/2343) previously mentioned in the [Workflow Guide](../workflow-guide/preface.html).

### Policy validation for field removal

You can now [validate field removal](../objects-guide/policies-over-REST.html#_validate_field_removal) using the policy action `validateProperty`.

### Relationship-derived Virtual Properties (RDVP) improvements

[Relationship-derived Virtual Properties](../objects-guide/managed-object-virtual-properties.html#relationship-derived-virtual-properties) now include reference fields with details of the referenced relationship.

### AD Password Synchronization Plugin UTC timestamps

The latest version of the Active Directory password synchronization plugin (v1.7.0) uses UTC timestamps for logs.

### Bootstrap IDM without stored configuration

Previously, the property `openidm.fileinstall.enabled` also controlled the configs being loaded on startup. Therefore, to disable file monitoring, you had to first start IDM with it enabled in order to load the configs into the repository, and then restart IDM with it disabled. The new setting `openidm.config.bootstrap.enabled` (which defaults to `true`), allows file monitoring to be disabled, and the bootstrap process will load the configuration into the repository.

For more information, see [Disable automatic configuration updates](../security-guide/disabling-auto-config-updates.html).

### API version header warnings

IDM can now [log warnings](../rest-api-reference/rest-api-versioning.html#_api_version_header_warnings) when API version headers are not specified.

### Reconciliation enhancements

Reconciliation has been enhanced in the following ways:

* Previously, if one node in the cluster went down or offline during a clustered reconciliation run, the reconciliation was canceled. This limitation no longer exists. For more information, see [Clustered reconciliation](../synchronization-guide/clustered-recon.html).

* Addition of the properties:

  * `reconTargetQueryPaging`

  * `reconTargetQueryPageSize`

  Learn more in the [Synchronization reference](../synchronization-guide/synchronization-ref.html#sync-object-mapping).

### Assignment synchronization optimization

A new property has been added to synchronization mappings, `optimizeAssignmentSync`, which determines whether modifications to an assignment's attributes or relationships should be treated as a synchronization event for members of that assignment or role, or if it should only be treated as a synchronization event for members if the modified assignment is directly relevant to that mapping, or if `effectiveAssignments` is included in `triggerSyncProperties`.

Learn more in the [Synchronization reference](../synchronization-guide/synchronization-ref.html#sync-object-mapping).

### Query filtering on arrays

For versions of IDM running DS or PostgreSQL as a repository, `queryFilter` now supports filtering on the contents of arrays. For more information, see [Filter objects in arrays](../objects-guide/queries.html#_filter_objects_in_arrays).

### Additional metrics

New metrics are available for [workflow](../monitoring-guide/api-metrics.html#api-workflow-metric-names) and [JVM](../monitoring-guide/api-metrics.html#api-jvm-metric-names).

## IDM 7.1.6

This release includes updates to ICF connectors, updates to dependency libraries, bug fixes, and the following new feature:

* The SalesForce connector template supports `client_credentials` grant type.

## IDM 7.1.4

This release includes updates to ICF connectors, updates to dependency libraries, bug fixes, and the following new feature:

* Upgrading to DS 7.3 is now supported. For more information, refer to [Supported repositories](before-you-install.html#prerequisites-repositories).

## IDM 7.1.2

This release includes updates to ICF connectors, updates to dependency libraries, bug fixes, and the following new feature:

* The Flowable embedded workflow engine has been upgraded to version 6.6.0. This upgrade fixes the issue with [native email tasks](https://github.com/flowable/flowable-engine/issues/2343) previously mentioned in the [Workflow Guide](../workflow-guide/preface.html).

## IDM 7.1

### Sample connection to Azure AD with the MS Graph API connector

The [Synchronize data between IDM and Azure Active Directory](../samples-guide/sync-with-azuread.html) sample uses the MS Graph API connector to synchronize users between IDM and Azure AD.

### Password sync plugins

#### Active Directory Password Synchronization Plugin UTC timestamps

The latest version of the Active Directory password synchronization plugin uses UTC timestamps for logs.

#### Active Directory Password Synchronization Plugin infinite loop prevention

The latest version of the Active Directory Password Synchronization Plugin supports a new registry key that helps prevent infinite password update loops. Learn more about the registry key, [pwdChangeInterval](../pwd-plugin-guide/conf-ad-pwd-sync.html#ad-sync-keys-infinite-loop).

#### Active Directory Password Synchronization Plugin configurable max retries

The latest version of the Active Directory Password Synchronization Plugin supports a new registry key to configure the maximum retry attempts for password changes. Learn more about the registry key, [maxFileRetry](../pwd-plugin-guide/conf-ad-pwd-sync.html#ad-sync-keys-noidm).

#### Active Directory Password Synchronization Plugin search filter

The latest version of the Active Directory Password Synchronization Plugin supports a new registry key to configure a search filter to omit users/groups from password syncing. Learn more about the registry key, [userSearchFilterStrict](../pwd-plugin-guide/conf-ad-pwd-sync.html#userSearchFilterStrict).

#### Support for AM Bearer Tokens in the DS and Active Directory Password Synchronization Plugins

The latest versions of the DS and Active Directory password synchronization plugins now support the use of AM bearer tokens as an authentication method. Learn more:

* [Configure the plugin for AM bearer tokens](../pwd-plugin-guide/chap-sync-dj.html#pwd-sync-am-tokens)

* [Install the Active Directory password synchronization plugin](../pwd-plugin-guide/install-ad-pwd-sync.html)

### Support for alternative KBA answer hashing

Previously, KBA answers were always hashed as SHA-256 upon save, which is still the default setting. However, you can now specify an alternative hashing algorithm.

### Managed object default values

You can now specify default values for properties in the managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint, or directly in the conf/managed.json file.)*. For example, the default managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint, or directly in the conf/managed.json file.)* includes a default value that makes `accountStatus:active`, which effectively replaces the `onCreate` script that was previously used to achieve the same result.

|   |                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | IDM assumes all default values are valid for the schema. Although IDM skips policy validation for objects with default values, you can force validation on property values |

### Support for REST queries on array properties (JDBC)

You can now perform REST queries on properly configured array fields. Learn more:

* [Queries on object array properties (JDBC)](../objects-guide/queries.html#query-array-reqs)

* [Configure array fields](../install-guide/repository-postgresql.html#postgres-conf-search-array)

* [Convert an explicit mapped object to a hybrid mapped object (JDBC)](../objects-guide/explicit-generic-mapping-jdbc.html#convert-explicit-to-hybrid-jdbc)

### `waitForCompletion` property added to the `config` endpoint

The optional `waitForCompletion` parameter is now available to the `config` endpoint for create, update, and patch requests. Learn more:

* [Configure the server over REST](../setup-guide/configuring-over-rest.html)

* [Server configuration](../rest-api-reference/endpoints/rest-server-config.html)

### API endpoint requires admin authentication

To protect production servers from unauthorized API descriptor requests, IDM now requires admin authentication for the API endpoint.

### Additional query types in JDBC explicit tables

Queries on explicit tables in JDBC now support `bool:`, `num:`, and `long:` in addition to the previously supported query parameters (`strings`, `list:`, and `int:`).

## IDM 7.0.4

This release includes updates to ICF connectors, updates to dependency libraries, and bug fixes.

## IDM 7.0.3

This release includes bug fixes.

## IDM 7.0.2

* You can now [validate field removal](../objects-guide/policies-over-REST.html#_validate_field_removal) using the policy action `validateProperty`.

* The Flowable embedded workflow engine has been upgraded to version 6.6.0. This upgrade fixes the issue with [native email tasks](https://github.com/flowable/flowable-engine/issues/2343) previously mentioned in the [Workflow Guide](../workflow-guide/preface.html).

## IDM 7.0.1

This release includes bug fixes.

## IDM 7

### Password sync plugins

#### Active Directory Password Synchronization Plugin UTC timestamps

The latest version of the Active Directory password synchronization plugin uses UTC timestamps for logs.

#### Active Directory Password Synchronization Plugin infinite loop prevention

The latest version of the Active Directory Password Synchronization Plugin supports a new registry key that helps prevent infinite password update loops. Learn more about the registry key, [pwdChangeInterval](../pwd-plugin-guide/conf-ad-pwd-sync.html#ad-sync-keys-infinite-loop).

#### Active Directory Password Synchronization Plugin configurable max retries

The latest version of the Active Directory Password Synchronization Plugin supports a new registry key to configure the maximum retry attempts for password changes. Learn more about the registry key, [maxFileRetry](../pwd-plugin-guide/conf-ad-pwd-sync.html#ad-sync-keys-noidm).

#### Active Directory Password Synchronization Plugin search filter

The latest version of the Active Directory Password Synchronization Plugin supports a new registry key to configure a search filter to omit users/groups from password syncing. Learn more about the registry key, [userSearchFilterStrict](../pwd-plugin-guide/conf-ad-pwd-sync.html#userSearchFilterStrict).

#### Support for AM Bearer Tokens in the DS and Active Directory Password Synchronization Plugins

The latest versions of the DS and Active Directory password synchronization plugins now support the use of AM bearer tokens as an authentication method. Learn more:

* [Configure the plugin for AM bearer tokens](../pwd-plugin-guide/chap-sync-dj.html#pwd-sync-am-tokens)

* [Install the Active Directory password synchronization plugin](../pwd-plugin-guide/install-ad-pwd-sync.html)

### Access configuration over REST

You can now configure access rules over REST, at the `openidm/config/access` endpoint. In previous releases, access rules were configured in the `access.js` file. This script file has been replaced by an `access.json` configuration file, that performs the same function. Learn more in [Authorization and roles](../auth-guide/authorization-and-roles.html).

### Privilege dynamic filters

You can now create privilege [dynamic filters](../auth-guide/delegated-admin.html#dynamic-filter-da) for delegated administrators.

### Configurable HTTP I/O request buffer

You can now configure the [temporary storage file size](../setup-guide/temp-storage.html) for HTTP I/O requests.

### Filter expanded relationships

You can use `_queryFilter` to directly filter expanded relationships from a collection, such as `authzRoles`. Learn more in [Filter expanded relationships](../objects-guide/queries.html#filter-expand-relation).

### Deterministic ECDSA signatures for JWT

By default, JWTs are now signed with deterministic Elliptic Curve Digital Signature Algorithm (ECDSA). In order to use this more secure signing method, Bouncy Castle, which is included in the default IDM installation, must be installed. If Bouncy Castle is unavailable or the key is incompatible, IDM falls back to normal ECDSA.

|   |                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you need to turn off the use of deterministic ECDSA, add the following line to `conf/system.properties`:```properties
org.forgerock.secrets.preferDeterministicEcdsa=false
``` |

### Debugging information for Groovy scripts

In previous releases, setting `javascript.exception.debug.info=true` in the `boot.properties` file enabled additional debug information, including line numbers and file names for JavaScript exceptions. In this release, setting `groovy.exception.debug.info=true` lets you gather comparable debug information for Groovy scripts.

### REST API Versioning

IDM now supports the ability to specify the REST API version in HTTP calls and scripts. For more information, see REST API Versioning.

The following APIs have been updated in this release:

* openidm/scheduler

  Version 2 of this endpoint adds a `previousRunDate` property to the output of REST calls on specific scheduled tasks.

  Version 2 also lets you [trigger a scheduled task manually](../schedules-guide/configure-schedules.html#trigger-scheduled-task) and [pause and resume a scheduled task](../schedules-guide/configure-schedules.html#pause-scheduled-job).

  |   |                                                                                                                                   |
  | - | --------------------------------------------------------------------------------------------------------------------------------- |
  |   | The `action` parameter on the `scheduler` endpoint was deprecated in Version 1 of the endpoint and is not supported in Version 2. |

### Support for AM bearer tokens

IDM now supports using AM bearer tokens for authentication, with the `rsFilter` authentication module. Going forward, this is the only supported method for integrating AM and IDM. Learn more in [Authenticate through AM](../auth-guide/rsfilter-auth.html).

### Notification property now configurable

Notifications of changes to managed objects are injected into a property in that object type. Previously, the name of this property was always `_notifications`. In this IDM release, you can customize the name of the notifications property. Learn more in [Configure notifications](../audit-guide/notification-config.html).

### Reconciliation Association Information

The new `recon/assoc` endpoint can be used to gather detailed information about the associations created between a source and a target object during a reconciliation. This endpoint requires the following tables and views to be added to your repository: `reconassoc`, `reconassocentry`, and `reconassocentryview`. Learn more about [reconciliation association details](../synchronization-guide/manage-recon.html#recon-assoc).

For instructions on updating your existing repositories to enable this feature, refer to [Upgrade an Existing Repository](https://backstage.forgerock.com/docs/idm/7/upgrade-guide/update-repo.html#upgrade-existing-repository) in the IDM 7.0 documentation.

### Profile completeness endpoint

A new endpoint has been added to self-service, which lets you get a percentage value regarding the completeness of a specified user's profile.

### Audit logging safelist

By default, IDM now safelists fields that are safe to log. Learn more in [Use policies to filter audit data](../audit-guide/filtering-audit-policies.html).

### `in` clause for queries

The [`in` expression clause](../objects-guide/queries.html#query-in) provides limited support for queries on singleton string properties.

### Disposal of idle poolable connector instances (ICF)

In version 1.5.20.11 of the ICF framework, the framework disposes of idle connector instances in the connection pool (for poolable connectors such as the LDAP connector and the Database Table connector).

A connection pool cleaner thread now runs every minute and removes connections whose `lastUsed` time is larger than the `minEvictableIdleTimeMillis`.

This behavior is an improvement on previous releases, where a connection that had been used then returned to the connection pool remained there until the next connector operation. The previous behavior could result in several connections in the pool, that were idle but still connected to the target resource.

### Separate mapping configuration files

This release lets you configure mappings in separate mapping files, instead of, or in addition to one `sync.json` file. You cannot manage separate mapping configurations through the Admin UI. Learn more in [Resource mapping](../synchronization-guide/mappings.html).

### Queued sync retry

This release provides the ability to configure an infinite number of queued synchronization retries. Learn more in [Configure queued synchronization](../synchronization-guide/chap-implicit-live-sync.html#configure-queued-sync).

### Material Design Icon added to managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint, or directly in the conf/managed.json file.)*

[`mat-icon`](../objects-guide/appendix-managed-objects.html) has been added to the `schema` property of the managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint, or directly in the conf/managed.json file.)*.

### Additional query types in JDBC explicit tables

Queries on explicit tables in JDBC now support `bool:`, `num:`, and `long:` in addition to the previously supported query parameters (`strings`, `list:`, and `int:`).

### `config.properties` additions

The following content was added to the default `config.properties` file:

```properties
# The name of the PersistenceManager to be used by the framework
# when persisting component configurations.
felix.cm.pm=repo
```

## Archive

For documentation and release information prior to IDM 7.0, check out the [Documentation Archive](https://docs.pingidentity.com/archive/).

## Security advisories

Ping Identity issues security advisories in collaboration with our customers to address any security vulnerabilities transparently and rapidly.

Ping Identity's security advisory policy governs the process on how security issues are submitted, received, and evaluated as well as the timeline for the issuance of security advisories and patches.

Learn how to find security advisories in the Ping Identity [support portal](https://support.pingidentity.com/s/article/Support-Portal-Guide#SecurityAdvisories) (requires sign-on).

---

---
title: Release levels and interface stability
description: Describes PingIDM release levels and interface stability classifications to help you assess upgrade impact and compatibility
component: pingidm
version: 8.1
page_id: pingidm:release-notes:appendix-interface-stability
canonical_url: https://docs.pingidentity.com/pingidm/8.1/release-notes/appendix-interface-stability.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Documentation", "ForgeRock Support"]
section_ids:
  release-levels: Ping product release levels
  interface-stability: Ping product stability labels
---

# Release levels and interface stability

## Ping product release levels

Ping defines Major, Minor, Maintenance, and Patch product release levels. The release level is reflected in the version number. The release level tells you what sort of compatibility changes to expect.

**Release Level Definitions**

| Release Label      | Version Numbers                                                | Characteristics                                                                                                                                                                                                                                                                                                             |
| ------------------ | -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Major              | Version: x\[.0.0] (trailing 0s are optional)                   | * Bring major new features, minor features, and bug fixes

* Can include changes even to Stable interfaces

* Can remove previously Deprecated functionality, and in rare cases remove Evolving functionality that has not been explicitly Deprecated

* Include changes present in previous Minor and Maintenance releases |
| Minor              | Version: x.y\[.0] (trailing 0s are optional)                   | - Bring minor features, and bug fixes

- Can include backwards-compatible changes to Stable interfaces in the same Major release, and incompatible changes to Evolving interfaces

- Can remove previously Deprecated functionality

- Include changes present in previous Minor and Maintenance releases                   |
| Maintenance, Patch | Version: x.y.z\[.p]The optional `.p` reflects a Patch version. | * Bring bug fixes

* Are intended to be fully compatible with previous versions from the same Minor release                                                                                                                                                                                                                 |

## Ping product stability labels

Ping products support many features, protocols, APIs, GUIs, and command-line interfaces. Some of these are standard and very stable. Others offer new functionality that is continuing to evolve.

Ping acknowledges you invest in these features and interfaces, and therefore must know when and how Ping expects them to change. For that reason, Ping defines stability labels and uses these definitions in Ping products.

**Ping Stability Label Definitions**

| Stability Label       | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Stable                | This documented feature or interface is expected to undergo backwards-compatible changes only for major releases. Changes may be announced at least one minor release before they take effect.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Evolving              | This documented feature or interface is continuing to evolve and so is expected to change, potentially in backwards-incompatible ways even in a minor release. Changes are documented at the time of product release.While new protocols and APIs are still in the process of standardization, they are Evolving. This applies for example to recent Internet-Draft implementations, and also to newly developed functionality.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Legacy                | This feature or interface has been replaced with an improved version, and is no longer receiving development effort from Ping.You should migrate to the newer version, however the existing functionality will remain.Legacy features or interfaces will be marked as *Deprecated* if they are scheduled to be removed from the product.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Deprecated            | This feature or interface is deprecated and likely to be removed in a future release. For previously stable features or interfaces, the change was likely announced in a previous release. Deprecated features or interfaces will be removed from Ping products.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Removed               | This feature or interface was deprecated in a previous release and has now been removed from the product.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Technology Preview    | Technology previews provide access to new features that are considered as new technology that is not yet supported. Technology preview features may be functionally incomplete and the function as implemented is subject to change without notice. DO NOT DEPLOY A TECHNOLOGY PREVIEW INTO A PRODUCTION ENVIRONMENT.Customers are encouraged to test drive the technology preview features in a non-production environment and are welcome to make comments and suggestions about the features in the associated forums.Ping does not guarantee that a technology preview feature will be present in future releases, the final complete version of the feature is liable to change between preview and the final version. Once a technology preview moves into the completed version, said feature will become part of the Ping platform. Technology previews are provided on an "AS-IS" basis for evaluation purposes only and Ping accepts no liability or obligations for the use thereof. |
| Internal/Undocumented | Internal and undocumented features or interfaces can change without notice. If you depend on one of these features or interfaces, contact Ping support.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

---

---
title: Release notes
description: Overview of PingIDM release notes covering new features, requirements, compatibility, bug fixes, deprecations, and discontinued functionality
component: pingidm
version: 8.1
page_id: pingidm:release-notes:preface
canonical_url: https://docs.pingidentity.com/pingidm/8.1/release-notes/preface.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Deployment", "Identities", "Compatibility", "Security"]
page_aliases: ["index.adoc", "_@pingidm::index.adoc"]
---

# Release notes

PingIDM (IDM) software provides centralized, simple management and synchronization of identities for users, devices, and things. IDM software is highly flexible and therefore able to fit almost any use case and workflow.

These release notes are written for anyone using the IDM 8.1 release. Read these notes before you install or upgrade IDM software.

[icon: newspaper, set=fad, size=3x]

#### [What's New](whats-new.html)

New features and improvements.

[icon: ship, set=fad, size=3x]

#### [Prepare for Deployment](before-you-install.html)

The requirements for running IDM software in production.

[icon: clipboard-list, set=fad, size=3x]

#### [Compatibility](changed-functionality.html)

Key changes and compatibility with previous deployments.

[icon: spider-black-widow, set=fad, size=3x]

#### [Bug Fixes](fixes.html)

Bug fixes, limitations, and open issues.

[icon: scroll-old, set=fad, size=3x]

#### [Deprecation](deprecated-functionality.html)

Functionality marked for future removal.

[icon: cassette-betamax, set=fad, size=3x]

#### [Discontinued](removed-functionality.html)

Removed functionality.

---

---
title: Third-Party software
description: Third-party software supported for Ping Common Audit event logging and server monitoring, including JMS, Splunk, Graphite, Prometheus, and Grafana
component: pingidm
version: 8.1
page_id: pingidm:release-notes:commons-third-party
canonical_url: https://docs.pingidentity.com/pingidm/8.1/release-notes/commons-third-party.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Deployment", "Identities", "Compatibility", "Security"]
---

# Third-Party software

Ping provides support for using the following third-party software when logging Ping Common Audit events:

| Software                      | Version                                                                         |
| ----------------------------- | ------------------------------------------------------------------------------- |
| Java Message Service (JMS)    | 2.0 API                                                                         |
| MySQL JDBC Driver Connector/J | 8 (at least 8.0.19)	Do not use Connector/J versions 8.0.23 through 8.0.25. Why? |
| Splunk                        | 8.0 (at least 8.0.2)                                                            |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Elasticsearch and Splunk have native or third-party tools to collect, transform, and route logs. Examples include [Logstash](https://www.elastic.co/logstash) and [Fluentd](https://www.fluentd.org/).Ping recommends that you consider these alternatives. These tools have advanced, specialized features focused on getting log data into the target system. They decouple the solution from the Ping Identity Platform systems and version, and provide inherent persistence and reliability. You can configure the tools to avoid losing audit messages if a Ping Identity Platform service goes offline, or delivery issues occur.These tools can work with common audit logging:- Configure the server to log messages to standard output, and route from there.

- Configure the server to log to files, and use log collection and routing for the log files. |

Although Ping does not provide support for these tools, you can any use of the following third-party software to monitor Ping servers:

| Software   | Version            |
| ---------- | ------------------ |
| Grafana    | 7 (at least 7.4.3) |
| Graphite   | 1                  |
| Prometheus | 2.36               |

For Hardware Security Module (HSM) support, Ping software requires a client library that conforms to the PKCS#11 standard v2.20 or later.