---
title: .NET RCS release notes
description: Release notes for the .NET Remote Connector Server, covering fixes, connection improvements, and dependency updates by version
component: openicf
page_id: openicf:connector-release-notes:dotnet-server-release
canonical_url: https://docs.pingidentity.com/openicf/connector-release-notes/dotnet-server-release.html
section_ids:
  1_5_7_0_net_rcs: 1.5.7.0 .NET RCS
---

# .NET RCS release notes

Subscribe for automatic updates: [icon: rss-square, set=fa][ICF release notes RSS Feed](./feed.xml)

Refer to [Connector framework release notes](framework.html) for details regarding any changes to the ICF Connector Framework that can affect Remote Connector Server (RCS) behavior.

Downloads are available on [Backstage](https://backstage.forgerock.com/downloads/browse/idm/featured/connectors).

|   |                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Unless you have a specific need for the .NET version of the RCS, such as needing the [PowerShell connector toolkit](../connector-reference/powershell.html), we recommend using the [Java RCS](connector-server.html) instead. |

## 1.5.7.0 .NET RCS

* Connection improvements

  * .NET RCS should be able to initiate connection to IDM (OPENICF-731)

  * Client mode should support IDM authentication (OPENICF-1311)

  * Unable to start in client mode when no intervals used (OPENICF-1314)

  * When we attempt to stop in client mode, the connection is re-initiated (OPENICF-1315)

  * ConnectorObject should default the Name to Uid if Name is not present (OPENICF-1318)

  * Add the ability to connect to multiple IDM endpoints (OPENICF-1376)

  * Connection TTL should be in seconds (OPENICF-1626)

  * ConnectionGroup fixes for improved connection handling (OPENICF-1630)

  * Handle failure HTTP status codes when requesting OAuth 2.0 tokens (OPENICF-1631)

  * Fix handshake timing problem (OPENICF-1682)

  * Prevent use of websockets that are about to be closed (OPENICF-1685)

  * Ensure that IDM gets notification that a websocket is about to be closed (OPENICF-1700)

  * Stagger connection starts if webSocketConnections > 1 (OPENICF-1706)

  * SocketClosingSoonException introduces null values that break protobuf3 (OPENICF-2001)

  * Improve stability of RCS WebSocket connection management (OPENICF-2008)

  * If OAuth token endpoint is defined, .NET RCS still tries to use Basic Auth to connect to ID Cloud (OPENICF-2188)

  * Support for HTTP proxy authentication (OPENICF-2197)

  * Closing WebSockets are not handled properly (OPENICF-2217)

* Configuration improvements

  * Separate config properties in the ConnectorServerService.exe.Config (OPENICF-1313)

  * Make Pong interval configurable (OPENICF-1362)

  * Update default properties values (OPENICF-1628)

  * Support for hostId (OPENICF-1512)

  * Align HTTP proxy property names with Java RCS (OPENICF-2204)

* PowerShell connector now included with .NET connector server

  * Embed the PowerShell connector with the .NET connector server (OPENICF-1906)

  * Align PowerShell connector version number with the .NET RCS version (OPENICF-1962)

  * Integrate the PowerShell samples in the project (OPENICF-1970)

  * PowerShell connector: Query might return HTTP 500 when sorting by some properties (OPENICF-2205)

  * AD PowerShell samples should filter \_\_NAME\_\_ as a sort key (OPENICF-2172)

* Dependency updates and cleanup

  * Update and cleanup some dependencies. (OPENICF-1963, OPENICF-1971)

  * Upgrade protocol buffer version and package (OPENICF-1836, OPENICF-2173)

  * Upgrade .NET framework (OPENICF-1707)

  * Fix the Wix project, get rid of legacy dlls (OPENICF-1913)

  * Exception upon start due to a missing dependency (OPENICF-1951)

* General fixes and improvements

  * Sporadic issues managing RCS-hosted connectors through IDM Native Admin Console (OPENICF-2011)

  * Query filter on name attribute with pageSize and pagedResultsCookie returns HTTP 500 (OPENICF-1954)

  * PagedResultsCookie should be set to null if empty when deserialized from protobuf message (OPENICF-1679)

---

---
title: Changed functionality
description: Breaking changes and changed functionality across ICF connectors, the Remote Connector Server, and the connector framework, organized by release version
component: openicf
page_id: openicf:connector-release-notes:changed-functionality
canonical_url: https://docs.pingidentity.com/openicf/connector-release-notes/changed-functionality.html
keywords: ["Compatibility"]
section_ids:
  connectors: Connectors
  _1-5-20-33-changed-fx: 1.5.20.33
  ldap_connector: LDAP connector
  oracle_ebs_connector: Oracle EBS connector
  scim_connector: SCIM connector
  _1-5-20-31-changed-fx: 1.5.20.31
  _1-5-20-31-removed-props: Removed properties
  1_5_20_29: 1.5.20.29
  _1-5-20-29-min-versions-map-config: Minimum RCS and framework versions
  _1-5-20-29-removed-props: Removed properties
  1_5_20_22: 1.5.20.22
  database_table_connector: Database Table connector
  docusign_connector: DocuSign connector
  rcs: RCS
  1_5_20_32: 1.5.20.32
  1_5_20_24: 1.5.20.24
  1_5_20_23: 1.5.20.23
  java_17_required: Java 17 required
  1_5_20_21: 1.5.20.21
  logback-relocation: Logging configuration file
  framework: Framework
  1_5_20_24_2: 1.5.20.24
---

# Changed functionality

The following changes may impact existing deployments when you update. Adjust existing scripts, files, configurations, and so on, as necessary.

## Connectors

### 1.5.20.33

#### [LDAP connector](../connector-reference/ldap.html)

We removed the non-functional, obsolete property `respectResourcePasswordPolicyChangeAfterReset` from the LDAP connector configuration.

#### [Oracle EBS connector](../connector-reference/ebs.html)

* OPENICF-3379: The connector now doesn't require the `__NAME__` attribute in `__ACCOUNT__` attribute updates.

* OPENICF-3389: The connector now supports the delete operation on the `__ACCOUNT__` object type.

* OPENICF-3389: The connector now includes a new boolean configuration property to enable queries to return only active accounts or all accounts.

* OPENICF-3394: The connector now handles updates on the `__ENABLE__` attribute based on the UID of the updated user instead of in the content of the payload `__NAME__` attribute.

#### [SCIM connector](../connector-reference/scim.html)

* OPENICF-3360: The SCIM connector now supports finer rate-limiter granularity to control the operation execution rate. For example, you can configure the rate limiter to any positive rational number, such as `0.5/sec` or `30/min`.

* OPENICF-3377: The connector now supports the `filterAttributesToGet` boolean configuration property that determines if the SCIM `attributes` parameter should be included when reading resources using the SCIM endpoint.

### 1.5.20.31

#### Removed properties

We removed the following runtime configuration properties:

| Connector                                               | Removed configuration properties |
| ------------------------------------------------------- | -------------------------------- |
| [SaaS REST Connector](../connector-reference/rest.html) | `accessToken``tokenExpiration`   |

### 1.5.20.29

#### Minimum RCS and framework versions

The following connectors now use map objects in their configuration and require RCS and framework versions 1.5.20.24 or later:

* [Multiple CSV connector](../connector-reference/multicsv.html)

* [SaaS REST Connector](../connector-reference/rest.html)

* [Workday connector](../connector-reference/workday.html)

#### Removed properties

We removed the following runtime configuration properties:

| Connector                                                            | Removed configuration properties |
| -------------------------------------------------------------------- | -------------------------------- |
| [Adobe Marketing Cloud connector](../connector-reference/adobe.html) | `accessToken`                    |
| [Epic connector](../connector-reference/epic.html)                   | `accessToken``tokenValidity`     |
| [Marketo connector](../connector-reference/marketo.html)             | `accessToken``tokenExpiration`   |

### 1.5.20.22

#### [Database Table connector](../connector-reference/dbtable.html)

* OPENICF-2679: Reduce log level of many operations.

#### [DocuSign connector](../connector-reference/docusign.html)

* OPENICF-2557: DocuSign connector v2 causes incompatibility with the [Synchronize data between IDM and DocuSign sample](https://docs.pingidentity.com/pingidm/7.5/samples-guide/sync-with-docusign.html).

## RCS

### 1.5.20.32

* OPENICF-3369: The Java RCS now supports Java 21. Learn more in [Install Java RCS](../connector-reference/java-server.html).

* OPENICF-3275: The `connectorserver.loggingConfigFile` property has been removed from `ConnectorServer.properties`. To specify a custom logback configuration file, set the `LOGGING_CONFIG` system property to the location of your `logback.xml` file.

  Learn more in [Logging configuration file](../connector-reference/icf-logs.html#icf-logging-config-file).

### 1.5.20.24

* OPENICF-2882: Support for nested objects (map objects) in the provisioner `configurationProperties`. Any connector that supports map objects must use this RCS version or later.

### 1.5.20.23

#### Java 17 required

Running Java RCS requires Java 17.

### 1.5.20.21

#### Logging configuration file

The default location for `logback.xml` was moved from `lib/framework/` to `conf/`. You can now edit the path and filename, refer to [Logging configuration file](../connector-reference/icf-logs.html#icf-logging-config-file).

## Framework

### 1.5.20.24

* OPENICF-2882: The connector framework lets you define nested objects (map objects) in the provisioner `configurationProperties`. Any connector that supports map objects must use this framework version or later.

---

---
title: Connector framework release notes
description: Release notes for the ICF connector framework, covering changes, bug fixes, and enhancements across all framework versions
component: openicf
page_id: openicf:connector-release-notes:framework
canonical_url: https://docs.pingidentity.com/openicf/connector-release-notes/framework.html
section_ids:
  1_5_20_35_framework: 1.5.20.35 Framework
  1_5_20_34_framework: 1.5.20.34 Framework
  1_5_20_33_framework: 1.5.20.33 Framework
  1_5_20_32_framework: 1.5.20.32 Framework
  1_5_20_31_framework: 1.5.20.31 Framework
  1_5_20_30_framework: 1.5.20.30 Framework
  1_5_20_29_framework: 1.5.20.29 Framework
  1_5_20_28_framework: 1.5.20.28 Framework
  1_5_20_26_framework: 1.5.20.26 Framework
  1_5_20_25_framework: 1.5.20.25 Framework
  1_5_20_24_framework: 1.5.20.24 Framework
  1_5_20_23_framework: 1.5.20.23 Framework
  1_5_20_22_framework: 1.5.20.22 Framework
  1_5_20_21_framework: 1.5.20.21 Framework
  1_5_20_18_framework: 1.5.20.18 Framework
  1_5_20_15_framework: 1.5.20.15 Framework
  1_5_20_11_framework: 1.5.20.11 Framework
  1_5_20_8_framework: 1.5.20.8 Framework
  1_5_20_7_framework: 1.5.20.7 Framework
  1_5_20_6_framework: 1.5.20.6 Framework
  1_5_20_5_framework: 1.5.20.5 Framework
  1_5_20_4_framework: 1.5.20.4 Framework
  1_5_20_3_framework: 1.5.20.3 Framework
  1_5_20_0_framework: 1.5.20.0 Framework
  1_5_19_6_framework: 1.5.19.6 Framework
  1_5_19_5_framework: 1.5.19.5 Framework
  1_5_19_4_framework: 1.5.19.4 Framework
  1_5_19_3_framework: 1.5.19.3 Framework
  1_5_19_2_framework: 1.5.19.2 Framework
  1_5_19_1_framework: 1.5.19.1 Framework
  1_5_19_0_framework: 1.5.19.0 Framework
  1_5_18_0_framework: 1.5.18.0 Framework
---

# Connector framework release notes

Subscribe for automatic updates: [icon: rss-square, set=fa][ICF release notes RSS Feed](./feed.xml)

|   |                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------- |
|   | Updates to the connector framework can also include security, formatting, and other internal-facing fixes. |

## 1.5.20.35 Framework

* OPENICF-3510: Prevent the Framework from attempting to dispatch requests through WebSockets in the process of completing the IDM< - >RCS handshake.

## 1.5.20.34 Framework

No public changes were made to the framework, though a new version was released.

## 1.5.20.33 Framework

* OPENICF-3349: The RCS resolves DNS names each time it establishes a new WebSocket connection.

## 1.5.20.32 Framework

No public changes were made to the framework, though a new version was released.

## 1.5.20.31 Framework

* OPENICF-2939: The default ICF operation timeout for all connector operations has changed from no timeout (`-1`) to 15 seconds. This update applies to new connector configurations generated using the `createCoreConfig` action.

## 1.5.20.30 Framework

No public changes were made to the framework, though a new version was released.

## 1.5.20.29 Framework

No public changes were made to the framework, though a new version was released.

## 1.5.20.28 Framework

No public changes were made to the framework, though a new version was released.

## 1.5.20.26 Framework

* OPENICF-2973: Resolves a race condition within the Java Framework that could result in Groovy `ClassLoader` failures at runtime.

* OPENICF-2751: You can configure global operation rate limits on a per-operation basis for any connector. Learn more in [Operation rate limits](../connector-reference/configure-connector.html#operation-rate-limits).

## 1.5.20.25 Framework

No public changes were made to the framework, though a new version was released.

## 1.5.20.24 Framework

* OPENICF-2882: The connector framework lets you define nested objects (map objects) in the provisioner `configurationProperties`.

## 1.5.20.23 Framework

No public changes were made to the framework, though a new version was released.

## 1.5.20.22 Framework

No public changes were made to the framework, though a new version was released.

## 1.5.20.21 Framework

* OPENICF-2642: Align Jetty servlet WebSocketConnectionGroup check interval with default Java RCS value.

## 1.5.20.18 Framework

No public changes were made to the framework, though a new version was released.

## 1.5.20.15 Framework

* OPENICF-2384: Java Framework: Allow \_\_PASSWORD\_\_ removal via null values.

## 1.5.20.11 Framework

No public changes were made to the framework, though a new version was released.

## 1.5.20.8 Framework

* OPENICF-1998: Local/RemoteRequest congruence checks should throw a retryable exception upon failure.

## 1.5.20.7 Framework

* OPENICF-1883: Java RCS: Improve stability of RCS WebSocket connection management.

## 1.5.20.6 Framework

* OPENIDM-17535: IDM stack releases that include bundled connectors should continue to work with existing provisioner configuration.

## 1.5.20.5 Framework

* OPENICF-1855: Investigate handling query 'poison pill' termination via recon automatic retry upon exception receipt.

## 1.5.20.4 Framework

No public changes were made to the framework, though a new version was released.

## 1.5.20.3 Framework

* OPENICF-1704: Framework: resetConnectorInfos does not implement intent.

* OPENICF-1730: Client ConnectorInfos cache not refreshed upon RCS instance restart when using RCS Agent.

* OPENICF-1735: Upgrade to groovy 3.0.9.

## 1.5.20.0 Framework

|   |                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For a list of security issues addressed in this release, refer to the related [Security Advisory](https://backstage.forgerock.com/knowledge/kb/article/a40346022) in the Knowledge Base. |

* OPENICF-1566: Framework: ICF Jetty servlet default maxMessageSize is too small.

## 1.5.19.6 Framework

No issues specific to the ICF Connector Framework were addressed in this release.

## 1.5.19.5 Framework

No issues specific to the ICF Connector Framework were addressed in this release.

## 1.5.19.4 Framework

No issues specific to the ICF Connector Framework were addressed in this release.

## 1.5.19.3 Framework

No issues specific to the ICF Connector Framework were addressed in this release.

## 1.5.19.2 Framework

No issues specific to the ICF Connector Framework were addressed in this release.

## 1.5.19.1 Framework

No issues specific to the ICF Connector Framework were addressed in this release.

## 1.5.19.0 Framework

|   |                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Starting in version 1.5.19.0, ICF connectors that previously had external library dependencies now have those dependencies bundled inside the connector. |

* OPENICF-1413: Use framework version 1.5.11.0 for ldap-connector to support Java8-compatible release.

* OPENICF-1414: Scripted Groovy (v3) based connectors fail to load with IDM releases prior to 7.0.

## 1.5.18.0 Framework

|   |                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------- |
|   | Starting in version 1.5.18.0, the ICF Connector Framework and all connectors bundled with IDM share a unified version number. |

No issues specific to the ICF Connector Framework were addressed in this release.

---

---
title: Connector release notes
description: Per-version release notes for ICF connectors, covering new connectors, bug fixes, and feature updates across all connector releases
component: openicf
page_id: openicf:connector-release-notes:connectors
canonical_url: https://docs.pingidentity.com/openicf/connector-release-notes/connectors.html
section_ids:
  _1_5_20_35_connectors: 1.5.20.35 Connectors
  updated_connectors_with_change_details: Updated connectors with change details
  ms_graph_api: MS Graph API
  multiple_csv_connector: Multiple CSV connector
  pingone_connector: PingOne connector
  _1.5.20.35_saascommon: SaaS Common
  snowflake_connector: Snowflake connector
  updated_connectors_without_change_details: Updated connectors without change details
  1_5_20_34_connectors: 1.5.20.34 Connectors
  updated_connectors_with_change_details_2: Updated connectors with change details
  ldap_connector: LDAP connector
  microsoft_graph_api_connector: Microsoft Graph API connector
  updated_connectors_without_change_details_2: Updated connectors without change details
  1_5_20_33_connectors: 1.5.20.33 Connectors
  new_connectors: New connectors
  snowflake_connector_2: Snowflake connector
  updated_connectors_with_change_details_3: Updated connectors with change details
  google_apps_connector: Google Apps connector
  ldap_connector_2: LDAP connector
  oracle_ebs_connector: Oracle EBS connector
  _1.5.20.33_saascommon: SaaS Common
  sap_successfactors_connector: SAP SuccessFactors connector
  scim_connector: SCIM connector
  workday_connector: Workday connector
  updated_connectors_without_change_details_3: Updated connectors without change details
  1_5_20_32_connectors: 1.5.20.32 Connectors
  updated_connectors_with_change_details_4: Updated connectors with change details
  dropbox_connector_saas_common: Dropbox connector (SaaS common)
  ldap_connector_3: LDAP connector
  _1.5.20.32_saascommon: SaaS Common
  saas_rest_connector_saas_common: SaaS REST Connector (SaaS common)
  sap_hana_database_connector: SAP HANA Database connector
  updated_connectors_without_change_details_4: Updated connectors without change details
  1_5_20_31_connectors: 1.5.20.31 Connectors
  updated_connectors_with_change_details_5: Updated connectors with change details
  docusign_connector: DocuSign connector
  multiple_csv_connector_2: Multiple CSV connector
  multiple_csv_cloud_connector: Multiple CSV Cloud connector
  sap_successfactors_connector_2: SAP SuccessFactors connector
  saas_rest_connector: SaaS REST Connector
  scim_connector_2: SCIM connector
  updated_connectors_without_change_details_5: Updated connectors without change details
  1_5_20_30_connectors: 1.5.20.30 Connectors
  updated_connectors_with_change_details_6: Updated connectors with change details
  database_table_connector: Database Table connector
  google_apps_connector_2: Google Apps connector
  kerberos_connector: Kerberos connector
  ldap_connector_4: LDAP connector
  microsoft_graph_api_connector_2: Microsoft Graph API connector
  _1.5.20.30_saascommon: SaaS Common
  saas_rest_connector_2: SaaS REST Connector
  salesforce_connector: Salesforce connector
  scim_connector_3: SCIM connector
  servicenow_connector: ServiceNow connector
  updated_connectors_without_change_details_6: Updated connectors without change details
  1_5_20_29_connectors: 1.5.20.29 Connectors
  new_connectors_2: New connectors
  saas_rest_connector_3: SaaS REST Connector
  updated_connectors_with_change_details_7: Updated connectors with change details
  adobe_marketing_cloud_connector: Adobe Marketing Cloud connector
  box_connector: Box connector
  epic_connector: Epic connector
  google_cloud_platform_connector: Google Cloud Platform connector
  hubspot_connector: HubSpot connector
  ldap_connector_5: LDAP connector
  marketo_connector: Marketo connector
  _1.5.20.29_saascommon: SaaS Common
  salesforce_connector_2: Salesforce connector
  sap_successfactors_connector_3: SAP SuccessFactors connector
  scim_connector_4: SCIM connector
  servicenow_connector_2: ServiceNow connector
  1_5_20_28_connectors: 1.5.20.28 Connectors
  new_connectors_3: New connectors
  updated_connectors_with_change_details_8: Updated connectors with change details
  microsoft_graph_api_connector_3: Microsoft Graph API connector
  updated_connectors_without_change_details_7: Updated connectors without change details
  1_5_20_27_connectors: 1.5.20.27 Connectors
  updated_connectors_with_change_details_9: Updated connectors with change details
  google_apps_connector_3: Google Apps connector
  ldap_connector_6: LDAP connector
  1_5_20_26_connectors: 1.5.20.26 Connectors
  new_connectors_4: New connectors
  updated_connectors_with_change_details_10: Updated connectors with change details
  aws_iam_identity_center_connector: AWS IAM Identity Center connector
  epic_connector_2: Epic connector
  ldap_connector_7: LDAP connector
  microsoft_graph_api_connector_4: Microsoft Graph API connector
  mongodb_connector_scripted_groovy: MongoDB connector (Scripted Groovy)
  sap_s4hana_connector: SAP S/4HANA connector
  scim_connector_5: SCIM connector
  _1.5.20.26_scriptedgroovy: Scripted Groovy
  workday_connector_2: Workday connector
  updated_connectors_without_change_details_8: Updated connectors without change details
  1_5_20_23_connectors: 1.5.20.23 Connectors
  new_connectors_5: New connectors
  updated_connectors_with_change_details_11: Updated connectors with change details
  adobe_admin_console_connector_saas_common: Adobe Admin Console connector (SaaS common)
  amazon_web_services_aws_connector: Amazon Web Services (AWS) connector
  ldap_connector_8: LDAP connector
  microsoft_graph_api_connector_5: Microsoft Graph API connector
  _1.5.20.23_saascommon: SaaS Common
  sap_successfactors_connector_4: SAP SuccessFactors connector
  webex_connector_saas_common: Webex Connector (SaaS common)
  workday_connector_3: Workday connector
  updated_connectors_without_change_details_9: Updated connectors without change details
  1_5_20_22_connectors: 1.5.20.22 Connectors
  updated_connectors_with_change_details_12: Updated connectors with change details
  adobe_admin_console_connector: Adobe Admin Console connector
  database_table_connector_2: Database Table connector
  docusign_connector_2: DocuSign connector
  ibm_racf_connector: IBM RACF connector
  mongodb_connector: MongoDB connector
  oracle_ebs_connector_2: Oracle EBS connector
  pingone_connector_2: PingOne connector
  sap_successfactors_connector_5: SAP SuccessFactors connector
  scim_connector_6: SCIM connector
  workday_connector_4: Workday connector
  updated_connectors_without_change_details_10: Updated connectors without change details
  1_5_20_21_connectors: 1.5.20.21 Connectors
  updated_connectors_with_change_details_13: Updated connectors with change details
  dropbox_connector: Dropbox connector
  epic_connector_3: Epic connector
  google_apps_connector_4: Google Apps connector
  ldap_connector_9: LDAP connector
  pingone_connector_3: PingOne connector
  sap_connector: SAP connector
  scripted_rest_connector: Scripted REST connector
  webex_connector: Webex Connector
  updated_connectors_without_change_details_11: Updated connectors without change details
  1_5_20_20_connectors: 1.5.20.20 Connectors
  updated_connectors_with_change_details_14: Updated connectors with change details
  database_table_connector_3: Database Table connector
  google_apps_connector_5: Google Apps connector
  microsoft_graph_api_connector_6: Microsoft Graph API connector
  salesforce_connector_3: Salesforce connector
  scim_connector_7: SCIM connector
  updated_connectors_without_change_details_12: Updated connectors without change details
  1_5_20_19_connectors: 1.5.20.19 Connectors
  updated_connectors_with_change_details_15: Updated connectors with change details
  scim_connector_8: SCIM connector
  updated_connectors_without_change_details_13: Updated connectors without change details
  1_5_20_18_connectors: 1.5.20.18 Connectors
  updated_connectors_with_change_details_16: Updated connectors with change details
  dropbox_connector_2: Dropbox connector
  google_apps_connector_6: Google Apps connector
  ldap_connector_10: LDAP connector
  microsoft_graph_api_connector_7: Microsoft Graph API connector
  salesforce_connector_4: Salesforce connector
  sap_connector_2: SAP connector
  sap_hana_database_connector_2: SAP HANA Database connector
  scim_connector_9: SCIM connector
  updated_connectors_without_change_details_14: Updated connectors without change details
  1_5_20_17_connectors: 1.5.20.17 Connectors
  1_5_20_16_connectors: 1.5.20.16 Connectors
  1_5_20_15_connectors: 1.5.20.15 Connectors
  1_5_20_14_connectors: 1.5.20.14 Connectors
  1_5_20_12_connectors: 1.5.20.12 Connectors
  1_5_20_11_connectors: 1.5.20.11 Connectors
  1_5_20_9_connectors: 1.5.20.9 Connectors
  1_5_20_8_connectors: 1.5.20.8 Connectors
  1_5_20_7_connectors: 1.5.20.7 Connectors
  1_5_20_6_connectors: 1.5.20.6 Connectors
  1_5_20_5_connectors: 1.5.20.5 Connectors
  1_5_20_4_connectors: 1.5.20.4 Connectors
  1_5_20_3_connectors: 1.5.20.3 Connectors
  1_5_20_2_connectors: 1.5.20.2 Connectors
  1_5_20_1_connectors: 1.5.20.1 Connectors
  1_5_20_0_connectors: 1.5.20.0 Connectors
  1_5_19_6_connectors: 1.5.19.6 Connectors
  1_5_19_5_connectors: 1.5.19.5 Connectors
  1_5_19_4_connectors: 1.5.19.4 Connectors
  1_5_19_3_connectors: 1.5.19.3 Connectors
  1_5_19_2_connectors: 1.5.19.2 Connectors
  1_5_19_1_connectors: 1.5.19.1 Connectors
  1_5_19_0_connectors: 1.5.19.0 Connectors
  1_5_18_0_connectors: 1.5.18.0 Connectors
---

# Connector release notes

Subscribe for automatic updates: [icon: rss-square, set=fa][ICF release notes RSS Feed](./feed.xml)

Refer to [Connector framework release notes](framework.html) for details regarding any changes to the ICF Connector Framework that can affect connector behavior.

Downloads are available on [Backstage](https://backstage.forgerock.com/downloads/browse/idm/featured/connectors).

|   |                                                                                           |
| - | ----------------------------------------------------------------------------------------- |
|   | All updated connectors can include security, formatting, and other internal-facing fixes. |

## 1.5.20.35 Connectors

### Updated connectors with change details

#### [MS Graph API](../connector-reference/ms-graph-api.html)

* OPENICF-2961: The connector now supports [custom user extension attributes](../connector-reference/msgraph-conf.html#msgraph-api-extension-attributes). Configure `extensionPropertySourceAppIds` to discover and expose custom extension properties registered to your Azure applications.

* OPENICF-3473: The connector now surfaces more specific error details when health checks or connector operations fail, making it easier to distinguish proxy, Microsoft Graph API, and OAuth authentication failures.

#### [Multiple CSV connector](../connector-reference/multicsv.html)

* OPENICF-3470: The connector no longer throws an `OutOfMemoryError` during initialization when CSV files contain large field values.

* OPENICF-3472: Write operations no longer load entire CSV files into heap memory for single-row modifications, reducing memory pressure in large deployments.

#### [PingOne connector](../connector-reference/pingone.html)

* OPENICF-3506: Fixed encoding for spaces and special characters in filter values.

#### [SaaS Common](../connector-reference/preface.html#saas-common)

* OPENICF-3456: The HTTP Client User-Agent is now configurable. It defaults to `PingIdentityConnector`.

* OPENICF-3459: The `jwtPem`, `jwtCert`, and `jwtKey` configuration properties are now treated as secured (GuardedString) values.

* OPENICF-3496: The connector schema is no longer overwritten on every schema request.

#### [Snowflake connector](../connector-reference/snowflake.html)

* OPENICF-3488: Fixed a null pointer exception when a transient connectivity failure occurs while querying a remote Snowflake instance.

### Updated connectors without change details

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | Connectors without change details can include security, formatting, and other internal-facing fixes. |

* Adobe Admin Console connector ([SaaS common](#_1.5.20.35_saascommon))

* Adobe Marketing Cloud connector

* AWS IAM Identity Center connector

* Box connector ([SaaS common](#_1.5.20.35_saascommon))

* DocuSign connector ([SaaS common](#_1.5.20.35_saascommon))

* Dropbox connector ([SaaS common](#_1.5.20.35_saascommon))

* LDAP connector

* MongoDB connector

* Multiple CSV Cloud connector

* Oracle EBS connector

* RACF connector

* SaaS REST connector ([SaaS common](#_1.5.20.35_saascommon))

* SAP connector

* SCIM connector

* ServiceNow connector

* SuccessFactors connector

* Webex connector ([SaaS common](#_1.5.20.35_saascommon))

* Workday connector

## 1.5.20.34 Connectors

### Updated connectors with change details

#### [LDAP connector](../connector-reference/ldap.html)

* OPENICF-3437: Improved LDAP server discovery for PingDS and PingDirectory.

* OPENICF-3438: The LDAP connector correctly populates LDAP modify operation context, preventing accumulation of replicated control requests.

#### [Microsoft Graph API connector](../connector-reference/ms-graph-api.html)

* OPENICF-3435: The Microsoft Graph API connector now correctly handles adding passwords to application objects.

### Updated connectors without change details

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | Connectors without change details can include security, formatting, and other internal-facing fixes. |

* Adobe Admin Console connector

* Adobe Marketing Cloud connector

* AWS connector

* Box connector

* Cerner connector

* DocuSign connector

* Dropbox connector

* Duo connector

* Epic connector

* Google Cloud Platform connector

* HubSpot connector

* Marketo connector

* Multiple CSV Cloud connector

* Oracle EBS connector

* Peoplesoft connector

* PingOne connector

* RACF connector

* SaaS REST connector

* Salesforce connector

* SAP S/4HANA connector

* SCIM connector

* Scripted REST connector

* Snowflake connector

* SuccessFactors connector

* Webex connector

## 1.5.20.33 Connectors

### New connectors

#### [Snowflake connector](../connector-reference/snowflake.html)

### Updated connectors with change details

#### [Google Apps connector](../connector-reference/google.html)

* OPENICF-3302: The connector now clears the user `aliases` field through patch actions.

* OPENICF-3332: The connector now uses the Equals (`EQ`) filter on the new `parentOrgUnitPath` attribute to allow querying an `OrgUnits` object. Learn more in [Deprecated functionality](deprecated-functionality.html#_1_5_20_33) and in [Supported search filters](../connector-reference/google.html#google-apps-search-filters).

#### [LDAP connector](../connector-reference/ldap.html)

* OPENICF-3320: The connector configuration no longer includes the obsolete property `respectResourcePasswordPolicyChangeAfterReset`. Learn more in [Changed functionality](changed-functionality.html#_1-5-20-33-changed-fx).

#### [Oracle EBS connector](../connector-reference/ebs.html)

* OPENICF-3379: The connector now doesn't require the `__NAME__` attribute in `__ACCOUNT__` attribute updates. Learn more in [Changed functionality](changed-functionality.html#_1-5-20-33-changed-fx).

* OPENICF-3389: The connector now supports the delete operation on the `__ACCOUNT__` object type. Learn more in [Changed functionality](changed-functionality.html#_1-5-20-33-changed-fx).

* OPENICF-3389: The connector now includes a new boolean configuration property to enable queries to return only active accounts or all accounts. Learn more in [Changed functionality](changed-functionality.html#_1-5-20-33-changed-fx).

* OPENICF-3394: The connector now handles updates on the `__ENABLE__` attribute based on the UID of the updated user instead of in the content of the payload `__NAME__` attribute. Learn more in [Changed functionality](changed-functionality.html#_1-5-20-33-changed-fx).

#### [SaaS Common](../connector-reference/preface.html#saas-common)

* OPENICF-3371: OAuth access tokens are now renewed at a minimum of 60 seconds before their expiration.

#### [SAP SuccessFactors connector](../connector-reference/successfactors.html)

* OPENICF-3412: The SuccessFactors connector now correctly stores the schema caching mechanism in the connector configuration.

#### [SCIM connector](../connector-reference/scim.html)

* OPENICF-3360: The SCIM connector now supports finer rate-limiter granularity to control the operation execution rate. For example, you can configure the rate limiter to any positive rational number, such as `0.5/sec` or `30/min`. Learn more in [Changed functionality](changed-functionality.html).

* OPENICF-3377: The connector now supports the `filterAttributesToGet` boolean configuration property that determines if the SCIM `attributes` parameter should be included when reading resources using the SCIM endpoint. Learn more in [Changed functionality](changed-functionality.html) and in [SCIM connector configuration](../connector-reference/scim.html#scim).

#### [Workday connector](../connector-reference/workday.html)

* OPENICF-3324: Fixed the XPath transformation logic that could incorrectly alter expressions and lead to invalid results.

### Updated connectors without change details

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | Connectors without change details can include security, formatting, and other internal-facing fixes. |

* Adobe Admin Console connector ([SaaS common](#_1.5.20.33_saascommon))

* Adobe Marketing Cloud connector

* AS400 connector

* AWS IAM Identity Center connector

* Box connector ([SaaS common](#_1.5.20.33_saascommon))

* Database table connector

* DocuSign connector([SaaS common](#_1.5.20.33_saascommon))

* Dropbox connector ([SaaS common](#_1.5.20.33_saascommon))

* Groovy connector ([Scripted Groovy](../connector-reference/preface.html#scripted-groovy))

* HubSpot connector

* Microsoft (MS) Graph API connector

* MongoDB connector ([Scripted Groovy](../connector-reference/preface.html#scripted-groovy))

* Multiple CSV Cloud connector

* Multiple CSV connector

* PingOne connector ([SaaS common](#_1.5.20.33_saascommon))

* SaaS REST connector ([SaaS common](#_1.5.20.33_saascommon))

* Salesforce connector

* SAP connector ([Scripted Groovy](../connector-reference/preface.html#scripted-groovy))

* SAP Hana DB connector

* Scripted REST connector ([Scripted Groovy](../connector-reference/preface.html#scripted-groovy))

* Scripted SQL connector ([Scripted Groovy](../connector-reference/preface.html#scripted-groovy))

* ServiceNow connector

* SSH connector ([Scripted Groovy](../connector-reference/preface.html#scripted-groovy))

* Webex connector ([SaaS common](#_1.5.20.33_saascommon))

## 1.5.20.32 Connectors

### Updated connectors with change details

#### [Dropbox connector](../connector-reference/dropbox.html) ([SaaS common](#_1.5.20.32_saascommon))

* OPENICF-3266: The connector throws a proper error when attempting to perform an unsupported PATCH operation.

#### [LDAP connector](../connector-reference/ldap.html)

* OPENICF-3048: New `enforceADPasswordPolicyOnReset` configuration property specific for Active Directory to enable the enforcement of password policies on password resets.

  |   |                                                                                                                               |
  | - | ----------------------------------------------------------------------------------------------------------------------------- |
  |   | You can't set `enforceADPasswordPolicyOnReset` using the UI. You must edit the provisioner file directly or use the REST API. |

* OPENICF-3273: Ensure proper decoding of LDAP referral URLs.

* OPENICF-3284: Improved password policy validation error feedback for PingDS and Active Directory.

* OPENICF-3286: Fixes LDAP change log sync strategy for IBM Security Directory Server type to correctly skip changes.

* OPENICF-3287: You can't set port 0 in the connector configuration.

* OPENICF-3288: Port 3268 and 3269 (SSL) are now enforced for Active Directory Global Catalog detection.

#### [SaaS Common](../connector-reference/preface.html#saas-common)

* OPENICF-3263: JWT bearer flow no longer requires the `client_secret` to obtain an access token.

#### [SaaS REST Connector](../connector-reference/rest.html) ([SaaS common](#_1.5.20.32_saascommon))

* OPENICF-3272: Fixes an issue where `__UID__` resources that contained a space weren't properly URL-encoded when injected within the request URL.

* OPENICF-3277: Fixes a `NullPointerException` that can occur when attempting to unflatten attributes not present in the request payload.

#### [SAP HANA Database connector](../connector-reference/saphanadb.html)

* OPENICF-3241: The connector no longer uses the cascade option when dropping users.

### Updated connectors without change details

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | Connectors without change details can include security, formatting, and other internal-facing fixes. |

* Adobe Admin Console connector ([SaaS common](#_1.5.20.32_saascommon))

* AWS IAM IC connector

* Box connector ([SaaS common](#_1.5.20.32_saascommon))

* Database table connector

* DocuSign connector ([SaaS common](#_1.5.20.32_saascommon))

* MS Graph API connector

* Multiple CSV Cloud connector

* Oracle EBS connector

* PingOne connector ([SaaS common](#_1.5.20.32_saascommon))

* ScriptedSQL connector

* Webex Connector ([SaaS common](#_1.5.20.32_saascommon))

* Workday connector

## 1.5.20.31 Connectors

### Updated connectors with change details

#### [DocuSign connector](../connector-reference/docusign.html)

* OPENICF-3150: The connector now returns an empty query result instead of throwing an `UnknownUidException` when it cannot find a resource for queries using the UID.

#### [Multiple CSV connector](../connector-reference/multicsv.html)

* OPENICF-3270: Fixes complex queries against multiple special attributes such as `_id` and `__NAME__`.

#### [Multiple CSV Cloud connector](../connector-reference/multicsvcloud.html)

* Initial release of the [Multiple CSV Cloud connector](../connector-reference/multicsvcloud.html).

#### [SAP SuccessFactors connector](../connector-reference/successfactors.html)

* OPENICF-3139: The connector now uses a OpenSAML to generate SAML assertions locally.

#### [SaaS REST Connector](../connector-reference/rest.html)

* OPENICF-3157: Support for dynamic ICF resource filtering.

* OPENICF-3158: Support for restricting fields using `OP_ATTRIBUTES_TO_GET`.

* OPENICF-3233: Fixes invalid `__ACCOUNT__` object type definition when using the `createCoreConfig` action.

* OPENICF-3253: Fixes issue when a DELETE request requires a `requestBody`.

#### [SCIM connector](../connector-reference/scim.html)

* OPENICF-3260: The connector could incorrectly inject a `multiValuedAttributes` attribute into Create and Update payloads sent to the remote SCIM Provider.

### Updated connectors without change details

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | Connectors without change details can include security, formatting, and other internal-facing fixes. |

* AWS IAM IC connector

* Box connector

* CSV File connector

* Kerberos connector

* MongoDB connector

* MS Graph API connector

* SAP connector

* SAP HANA DB connector

* Scripted REST connector

* Webex connector

* Workday connector

## 1.5.20.30 Connectors

### Updated connectors with change details

#### [Database Table connector](../connector-reference/dbtable.html)

* OPENICF-2250: Connector attributes with the configuration property `changeLogColumn` can pass to the connector object.

#### [Google Apps connector](../connector-reference/google.html)

* OPENICF-3081: Use the `passwordHashAlgorithm` property to hash the connector `__PASSWORD__` attribute during transport.

* OPENICF-3088: Bug fix preventing update for `__ACCOUNT__` and `__GROUP__` secondary objects when the payload didn't include changes for the primary Google object.

#### [Kerberos connector](../connector-reference/kerberos.html)

* OPENICF-3170: The `scriptRoots` value returned by the `createCoreConfig` action was invalid.

#### [LDAP connector](../connector-reference/ldap.html)

* OPENICF-3101: The LDAP connector can read the Novell eDirectory GUID attribute.

#### [Microsoft Graph API connector](../connector-reference/ms-graph-api.html)

* OPENICF-1911: Support for the ability to use environment variables when authenticating with Azure.

#### [SaaS Common](../connector-reference/preface.html#saas-common)

* OPENICF-3097: JWT auth flow now supports PEM-formatted private keys.

#### [SaaS REST Connector](../connector-reference/rest.html)

* OPENICF-3114: Ability to send a payload in a delete request.

* OPENICF-3167: Fixes a Gson serialization issue preventing the SaaS REST connector from working with an RCS.

#### [Salesforce connector](../connector-reference/salesforce.html)

* OPENICF-3122: Adds the `initialSyncTokenOffset` configuration property. Use this property to define a period, in hours, to subtract from the current time when generating the initial Salesforce sync token. Default value is `0` hours.

#### [SCIM connector](../connector-reference/scim.html)

* OPENICF-3091: When generating the ICF Schema, the ICF ObjectClass type was incorrectly set to the SCIM Schema name instead of the ResourceType name.

#### [ServiceNow connector](../connector-reference/servicenow.html)

* OPENICF-2422: The connector supports the ServiceNow user object property `cost_center`.

### Updated connectors without change details

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | Connectors without change details can include security, formatting, and other internal-facing fixes. |

* Box connector

* CSV connector

* Scripted REST connector

* Hubspot connector

* Webex connector

## 1.5.20.29 Connectors

### New connectors

#### [SaaS REST Connector](../connector-reference/rest.html)

### Updated connectors with change details

#### [Adobe Marketing Cloud connector](../connector-reference/adobe.html)

* OPENICF-2983: Connector invalidates access token on authentication failure.

* OPENICF-3044: Removed runtime configuration properties. Learn more in [Changed functionality](changed-functionality.html#_1-5-20-29-removed-props).

#### [Box connector](../connector-reference/box.html)

* OPENICF-2978: Connector invalidates access token on authentication failure.

#### [Epic connector](../connector-reference/epic.html)

* OPENICF-2982: Connector invalidates access token on authentication failure.

* OPENICF-3046: Removed runtime configuration properties. Learn more in [Changed functionality](changed-functionality.html#_1-5-20-29-removed-props).

#### [Google Cloud Platform connector](../connector-reference/gcp.html)

* OPENICF-2980: Connector invalidates access token on authentication failure.

#### [HubSpot connector](../connector-reference/hubspot.html)

* OPENICF-2979: Connector invalidates access token on authentication failure.

#### [LDAP connector](../connector-reference/ldap.html)

* OPENICF-3018: For DS 8.0 or later LDAP servers, the connector pages the change log with a search control cookie instead of filtering against change numbers. Change numbers are no longer required to set up and use the sync action.

#### [Marketo connector](../connector-reference/marketo.html)

* OPENICF-2984: Connector invalidates access token on authentication failure.

* OPENICF-3045: Removed runtime configuration properties. Learn more in [Changed functionality](changed-functionality.html#_1-5-20-29-removed-props).

#### [SaaS Common](../connector-reference/preface.html#saas-common)

* OPENICF-2967: Support for JWT authentication flow with framework 1.5.20.24 or later and RCS 1.5.20.24 or later.

* OPENICF-2985: Connector invalidates access token on authentication failure.

#### [Salesforce connector](../connector-reference/salesforce.html)

* OPENICF-2977: Connector invalidates access token on authentication failure.

#### [SAP SuccessFactors connector](../connector-reference/successfactors.html)

* OPENICF-2981: Connector invalidates access token on authentication failure.

#### [SCIM connector](../connector-reference/scim.html)

* OPENICF-2975: Connector invalidates access token on authentication failure.

#### [ServiceNow connector](../connector-reference/servicenow.html)

* OPENICF-2976: Connector invalidates access token on authentication failure.

## 1.5.20.28 Connectors

### New connectors

* [Multiple CSV connector](../connector-reference/multicsv.html)

### Updated connectors with change details

#### [Microsoft Graph API connector](../connector-reference/ms-graph-api.html)

* OPENICF-2910: You can now read the following [Contacts](../connector-reference/msgraph-contacts.html) attributes:

  * `directReports`

  * `memberOf`

  * `transitiveMemberOf`

  * `manager`

  |   |                                               |
  | - | --------------------------------------------- |
  |   | These attributes are not returned by default. |

* OPENICF-3005: You can now read the following [`servicePrincipal`](../connector-reference/msgraph-servicePrincipal.html) attributes:

  * `owners`

  * `memberOf`

  * `transitiveMemberOf`

  * `oauth2PermissionGrants`

  |   |                                               |
  | - | --------------------------------------------- |
  |   | These attributes are not returned by default. |

### Updated connectors without change details

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | Connectors without change details can include security, formatting, and other internal-facing fixes. |

* AWS IAM Identity Center connector

* LDAP connector

* [SaaS Common](../connector-reference/preface.html#saas-common) connectors

* [Scripted Groovy](../connector-reference/preface.html#scripted-groovy) connectors

* Workday connector

## 1.5.20.27 Connectors

### Updated connectors with change details

#### [Google Apps connector](../connector-reference/google.html)

* OPENICF-2996: Correctly maps License Assignment read operation parameters to Google API calls.

#### [LDAP connector](../connector-reference/ldap.html)

* OPENICF-2992: Improved support for IBM directory changelog "changes" binary attribute.

## 1.5.20.26 Connectors

### New connectors

* [Duo connector](../connector-reference/duo.html)

### Updated connectors with change details

#### [AWS IAM Identity Center connector](../connector-reference/aws-iam-identity-center.html)

* OPENICF-2968: Error when renewing access token.

#### [Epic connector](../connector-reference/epic.html)

* OPENICF-2941: Querying Epic accounts could fail.

#### [LDAP connector](../connector-reference/ldap.html)

* OPENICF-2931: PingDirectory is now a recognized LDAP directory.

#### [Microsoft Graph API connector](../connector-reference/ms-graph-api.html)

* OPENICF-2900: Added a user resource attribute `authenticationMethods` that is a read-only list of objects containing the authentication methods associated with a user.

* OPENICF-2901: User email authentication methods can be added/updated/deleted using a new String attribute `__emailAuthenticationMethod__` that contains the email associated with the user's authentication preference.

* OPENICF-2902: The connector can now manage phone authentication methods on a user using a new virtual multivalued String attribute `__phoneAuthenticationMethods__` that contains a definitive list of concatenated `"{phoneNumber}:{phoneType}"`.

* OPENICF-2903: Adds multivalued string attribute `__removeFido2Methods__` to the user schema. This attribute takes a list of String GUIDs to be deleted as Fido2 auth method IDs associated with a user.

* OPENICF-2912: Adds multivalued string attribute `__removeMicrosoftAuthenticatorMethods__` to the user schema. This attribute holds a list of GUIDs associated with MicrosoftAuthenticator authentication method IDs to be removed from a user.

* OPENICF-2913: Adds multivalued string attribute `__removeSoftwareOathMethods__` to the user schema. This attribute holds a list of GUIDs associated with Software Oath authentication method IDs to be removed from a user.

#### [MongoDB connector](../connector-reference/mongodb.html) ([Scripted Groovy](#_1.5.20.26_scriptedgroovy))

* OPENICF-2987: Update MongoDB driver to version 4.11.4.

#### [SAP S/4HANA connector](../connector-reference/sap-hana.html)

* OPENICF-2915: You can specify the `instanceUrl` of the SAP Hana instance in the connector configuration properties.

* OPENICF-2934: Query paging fixes.

#### [SCIM connector](../connector-reference/scim.html)

* OPENICF-2880: Reduce logging noise when a schema extension overrides a core schema attribute.

#### [Scripted Groovy](../connector-reference/preface.html#scripted-groovy)

* OPENICF-2955: The Scripted Groovy `scriptRoots` configuration property can now reference Groovy scripts embedded within the connector JAR file using the `!` prefix.

#### [Workday connector](../connector-reference/workday.html)

* OPENICF-1148: Support for updating the primary work phone number using the `primaryWorkPhone` connector attribute.

* OPENICF-2622: You can use [XPath transformations](../connector-reference/workday.html#workday-xpath-transformations) to simplify and map Workday attributes directly to read-only connector object type properties.

  |   |                                                          |
  | - | -------------------------------------------------------- |
  |   | Requires connector framework version 1.5.20.24 or later. |

* OPENICF-2891: Deprecate Workday connector schema attribute `mobile`.

### Updated connectors without change details

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | Connectors without change details can include security, formatting, and other internal-facing fixes. |

* Adobe Admin Console connector

* Adobe Marketing Cloud connector

* AS400 connector

* AWS connector

* Box connector

* Cerner connector

* CSV connector

* Database table connector

* DocuSign connector

* Dropbox connector

* Google Apps connector

* Google Cloud Platform (GCP) connector

* HubSpot connector

* IBM RACF connector

* Kerberos connector

* Marketo connector ([Scripted Groovy](#_1.5.20.26_scriptedgroovy))

* Oracle EBS

* Peoplesoft connector

* PingOne connector

* Powershell connector toolkit

* Salesforce connector

* SAP connector ([Scripted Groovy](#_1.5.20.26_scriptedgroovy))

* SAP HANA Database connector

* SAP SuccessFactors connector

* ScriptedREST connector ([Scripted Groovy](#_1.5.20.26_scriptedgroovy))

* ScriptedSQL connector ([Scripted Groovy](#_1.5.20.26_scriptedgroovy))

* ServiceNow connector

* SSH connector ([Scripted Groovy](#_1.5.20.26_scriptedgroovy))

* Webex connector

## 1.5.20.23 Connectors

### New connectors

* [AWS IAM Identity Center connector](../connector-reference/aws-iam-identity-center.html)

* [Box connector](../connector-reference/box.html) ([SaaS common](#_1.5.20.23_saascommon))

### Updated connectors with change details

#### [Adobe Admin Console connector](../connector-reference/adobe-admin-console.html) ([SaaS common](#_1.5.20.23_saascommon))

* OPENICF-2792: Set the type for the `orgSpecific` and `businessAccount` schema attributes to boolean.

* OPENICF-2845: Ability to update the user's email address.

* OPENICF-2851: Updating group memberships for an Adobe account may result in excessive email notifications.

#### [Amazon Web Services (AWS) connector](../connector-reference/aws-iam.html)

* OPENICF-2755: Support for groups, roles, managed policy, inline policy, service control policy, and org unit object types.

#### [LDAP connector](../connector-reference/ldap.html)

* OPENICF-2805: SASL-EXTERNAL (mTLS) is now available with the LDAP connector.

#### [Microsoft Graph API connector](../connector-reference/ms-graph-api.html)

* OPENICF-2834: The virtual resource displaying service plans as their own object now includes the `skuPartNumber` as a readable attribute. Additionally, the display name of service plans is now a combination of the `skuPartNumber` and the `servicePlanName`.

#### [SaaS Common](../connector-reference/preface.html#saas-common)

* OPENICF-2781: During token renewal, properly cache new refresh token in the connector configuration.

#### [SAP SuccessFactors connector](../connector-reference/successfactors.html)

* OPENICF-2847: Resolve `ArrayIndexOutOfBoundsException` when consuming older connector configuration.

#### [Webex Connector](../connector-reference/webex.html) ([SaaS common](#_1.5.20.23_saascommon))

* OPENICF-2619: Properly handle HTTP 400 error responses during Webex user creation.

#### [Workday connector](../connector-reference/workday.html)

* OPENICF-2524: Paged queries with no results throw an internal server error.

### Updated connectors without change details

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | Connectors without change details can include security, formatting, and other internal-facing fixes. |

* Adobe Marketing Cloud connector

* AS400 connector

* Cerner connector

* CSV connector

* Database table connector

* DocuSign connector ([SaaS common](#_1.5.20.23_saascommon))

* Dropbox connector ([SaaS common](#_1.5.20.23_saascommon))

* Epic connector

* Google Apps connector

* Google Cloud Platform (GCP) connector

* Groovy connector toolkit

* HubSpot connector

* IBM RACF connector

* Kerberos connector

* Marketo connector

* MongoDB connector

* Oracle EBS

* Peoplesoft connector

* PingOne connector ([SaaS common](#_1.5.20.23_saascommon))

* Powershell connector toolkit

* Salesforce connector

* SAP connector

* SAP HANA Database connector

* SAP S/4HANA connector

* SAP SuccessFactors connector

* SCIM connector

* ScriptedREST connector

* ScriptedSQL connector

* ServiceNow connector

* SSH connector

## 1.5.20.22 Connectors

### Updated connectors with change details

#### [Adobe Admin Console connector](../connector-reference/adobe-admin-console.html)

* OPENICF-2559: Initial release of the Adobe Admin Console connector. Refer to [Adobe Admin Console connector](../connector-reference/adobe-admin-console.html) for more information.

#### [Database Table connector](../connector-reference/dbtable.html)

* OPENICF-2679: Reduce log level of many operations

#### [DocuSign connector](../connector-reference/docusign.html)

* OPENICF-2557: DocuSign connector v2

  * OPENICF-2583: Add ObjectClass UserGroups

  * OPENICF-2587: Add filter support for Users ObjectClass

  * OPENICF-2588: Add filter support for the UserGroups ObjectClass

  * OPENICF-2766: Wrong exception message when the connector is configured incorrectly

#### [IBM RACF connector](../connector-reference/racf.html)

* OPENICF-2757: Support for new object types, segments, and attributes

#### [MongoDB connector](../connector-reference/mongodb.html)

* OPENICF-2784: Update MongoDB driver to version 4.11.2

#### [Oracle EBS connector](../connector-reference/ebs.html)

* OPENICF-1760: EBS Connector v2, support responsibilities

#### [PingOne connector](../connector-reference/pingone.html)

* OPENICF-2740: Enhance user password to accept external password assignments

#### [SAP SuccessFactors connector](../connector-reference/successfactors.html)

* OPENICF-2428: Account Object: Group Name not required

* OPENICF-2528: Support schema discovery and writeback

#### [SCIM connector](../connector-reference/scim.html)

* OPENICF-1617: Ability to assign groups to users

* OPENICF-2669: The read rate limit may be exceeded during queries

* OPENICF-2672: Reconciliation after patch remove on managed user throws NPE and full updates omit remove operations

* OPENICF-2682: Using dynamic schema, multivalued attributes of schema extensions are improperly handled

* OPENICF-2710: Creating users/groups with multivalued extension attributes fails

* OPENICF-2726: Do not fail on unknown Enum values when deserializing schemas

* OPENICF-2735: The endpoint in use for a given ResourceType was incorrectly derived from the objectClass defined by the IDM provisioner configuration instead of from the endpoint specified by the ResourceTypes response from the SCIM Provider

#### [Workday connector](../connector-reference/workday.html)

* OPENICF-2524: liveSync on Workday custom fields now works

### Updated connectors without change details

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | Connectors without change details can include security, formatting, and other internal-facing fixes. |

* Adobe Marketing Cloud connector

* AS400 connector

* AWS connector

* Cerner connector

* CSV connector

* Dropbox connector

* Epic connector

* Google Apps connector

* Google Cloud Platform (GCP) connector

* Groovy connector toolkit

* HubSpot connector

* Kerberos connector

* LDAP connector

* Marketo connector

* MS Graph API connector

* Peoplesoft connector

* Powershell connector toolkit

* Salesforce connector

* SAP connector

* SAP HANA Database connector

* SAP S/4HANA connector

* ScriptedREST connector

* ScriptedSQL connector

* ServiceNow connector

* SSH connector

* Webex connector

## 1.5.20.21 Connectors

### Updated connectors with change details

#### [Dropbox connector](../connector-reference/dropbox.html)

* OPENICF-2664: SaaS Client Initializer should not automatically add default HTTP headers

* OPENICF-2655: Logging levels in use by generated connector class are too verbose

#### [Epic connector](../connector-reference/epic.html)

* OPENICF-2233: Add support for managing SER resources

* OPENICF-2492: EMP Enhancements

#### [Google Apps connector](../connector-reference/google.html)

* OPENICF-2617: Deprecate \_\_SECONDARY\_EMAIL\_\_ in favor of \_\_SECONDARY\_EMAILS\_\_ attribute

#### [LDAP connector](../connector-reference/ldap.html)

* OPENICF-2544: LiveSync timestamp strategy may lose changes when remote handler returns `false`

#### [PingOne connector](../connector-reference/pingone.html)

* OPENICF-2507: Initial release of the PingOne connector. Refer to [PingOne connector](../connector-reference/pingone.html) for more information.

#### [SAP connector](../connector-reference/sap.html)

* OPENICF-2410: Additional attributes in the Profile Object Type

* OPENICF-2411: Additional attributes in the Activity Groups Object Type

#### [Scripted REST connector](../connector-reference/scripted-rest.html)

* OPENICF-1917: Support for throttling

#### [Webex Connector](../connector-reference/webex.html)

* OPENICF-2047: Initial release of the Webex connector. Refer to [Webex Connector](../connector-reference/webex.html) for more information.

### Updated connectors without change details

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | Connectors without change details can include security, formatting, and other internal-facing fixes. |

* AWS connector

* Kerberos connector

## 1.5.20.20 Connectors

### Updated connectors with change details

#### [Database Table connector](../connector-reference/dbtable.html)

* OPENICF-2606: Schema is unnecessarily regenerated for every operation.

#### [Google Apps connector](../connector-reference/google.html)

* OPENICF-2194: PATCH remove operation doesn't update the object when both the field and value are provided.

* OPENICF-2351: Include 503 errors in the retry logic for GoogleApps connector.

* OPENICF-2490: Requests hang if the Google Admin SDK API has not been enabled within the configured Google Project.

#### [Microsoft Graph API connector](../connector-reference/ms-graph-api.html)

* OPENICF-2593: Upgrade azure-identity dependency to latest version.

#### [Salesforce connector](../connector-reference/salesforce.html)

* OPENICF-2626: A duplicate header sent by the connector prevents successful OAuth flow.

#### [SCIM connector](../connector-reference/scim.html)

* OPENICF-2575: Running liveSync for object classes other than the Account object results in an error.

* OPENICF-2601: Inject common attributes within dynamically generated schemas for all resource types.

### Updated connectors without change details

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | Connectors without change details can include security, formatting, and other internal-facing fixes. |

* Adobe Marketing Cloud connector

* Marketo connector

* ScriptedREST connector

* ScriptedSQL connector

## 1.5.20.19 Connectors

### Updated connectors with change details

#### [SCIM connector](../connector-reference/scim.html)

* OPENICF-1296: HTTP Status and Error Response Handling.

* OPENICF-2574: Authorization header contains an extra space which breaks client\_credentials flow.

* OPENICF-2579: TestOp should catch all exceptions thrown by the initial attempt to read the alternate ServiceProviderConfig endpoint.

### Updated connectors without change details

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | Connectors without change details can include security, formatting, and other internal-facing fixes. |

* Microsoft Graph API connector

## 1.5.20.18 Connectors

### Updated connectors with change details

#### [Dropbox connector](../connector-reference/dropbox.html)

* OPENICF-2354 Missing property messages.

#### [Google Apps connector](../connector-reference/google.html)

* OPENICF-2487 License assignment account attribute should be an array of strings.

#### [LDAP connector](../connector-reference/ldap.html)

* OPENICF-2296: Bad IP address for the LDAP host should be caught, and a 503 error code should be returned by IDM.

* OPENICF-2401: `queryFilter` true or false against isActive attribute returns all results.

* OPENICF-2526: Specify a negative offset (in seconds) to be applied to the timestamp token when querying for changes on the remote LDAP server using the `timestampSyncOffset` configuration property.

* OPENICF-2555: Ability to define custom octet string attributes using the `customOctetStringAttributes` configuration property.

#### [Microsoft Graph API connector](../connector-reference/ms-graph-api.html)

* OPENICF-2006: Clicking on Azure AD connector for the first time throws a 500 error.

* OPENICF-2027: Support single quotation marks in query filters.

* OPENICF-2140: Info level logging is overused for this connector.

#### [Salesforce connector](../connector-reference/salesforce.html)

* OPENICF-1527: Returns a generic ConnectorException 'Error: 400' on expired/revoked refresh\_token.

* OPENICF-2246: Implement support for Client Credentials Grant type. Refer to [Configure the Salesforce connector](../connector-reference/salesforce.html#salesforce-provisioner).

* OPENICF-2266: User schema is not cached.

* OPENICF-2505: createFullConfig NPEs when supportedObjectTypes contains FeatureLicense.

#### [SAP connector](../connector-reference/sap.html)

* OPENICF-2371: Scripts for SAP HR searching and filtering.

* OPENICF-2465: Prevent activity group assignment from being deleted when the assignment is end-dated.

* OPENICF-2480: SAP Central User Administration (CUA) support.

#### [SAP HANA Database connector](../connector-reference/saphanadb.html)

Initial release of the SAP HANA Database connector. Refer to [SAP HANA Database connector](../connector-reference/saphanadb.html) for more information.

* OPENICF-2368: SAP HANA Database connector.

#### [SCIM connector](../connector-reference/scim.html)

* OPENICF-1528: Salesforce returns a generic ConnectorException 'Error: 400' on expired/revoked refresh\_token.

* OPENICF-2472: access\_token validation checked on `issued_at` claim instead of `expires_in` for refresh\_token grant.

* OPENICF-2500: Extension attributes not flattened when converted to ConnectorObject.

* OPENICF-2504: Map JSON integer type to Java Long.

### Updated connectors without change details

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | Connectors without change details can include security, formatting, and other internal-facing fixes. |

* Adobe Marketing Cloud connector

* AS400 connector

* AWS connector

* Box connector

* Cerner connector

* CSV connector

* Database Table connector

* DocuSign connector

* Epic connector

* GCP connector

* HubSpot connector

* IBM RACF connector

* Oracle EBS connector

* Peoplesoft connector

* SAP S/4HANA connector

* SAP SuccessFactors connector

* ScriptedREST connector

* ScriptedSQL connector

* ServiceNow connector

* Workday connector

## 1.5.20.17 Connectors

> **Collapse: Database Table Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Microsoft Graph API Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Oracle EBS connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Salesforce connector**
>
> * OPENICF-1723: Clarify usage of `proxyUri` configuration property

> **Collapse: SCIM connector**
>
> * OPENICF-900: Implement the `/Schemas` endpoint discovery
>
> * OPENICF-2297: Roles attribute should be a list of Strings, not a list of Objects
>
> * OPENICF-2482: Dynamic schema does not default to static schema on all exceptions
>
> * OPENICF-2483: Creating a user with special attributes fails with dynamically generated schema
>
> * OPENICF-2484: PUT w/schemas attribute fails for Providers that support Patch
>
> * OPENICF-2448: HTTP Client fails to handle OAuth errors
>
> * OPENICF-2453: Persist optional refresh\_token issued upon successful access\_token renewal

> **Collapse: ScriptedSQL Connector**
>
> No public changes were made specific to this connector, though a new version was released.

## 1.5.20.16 Connectors

> **Collapse: Dropbox connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: DocuSign connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Google Apps connector**
>
> * OPENICF-2356: GoogleApps Connector doesn't allow listing of licenses

> **Collapse: Groovy connector toolkit**
>
> * OPENICF-2394: Align Scripted Connector templates

> **Collapse: HubSpot connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Kerberos Apps connector**
>
> * OPENICF-2400: Kerberos Search operation logs incorrect operation type
>
> * OPENICF-2394: Align Scripted Connector templates

> **Collapse: Marketo Connector**
>
> * OPENICF-2394: Align Scripted Connector templates

> **Collapse: Microsoft Graph API connector**
>
> * OPENICF-2355: MSGraphAPI Connector doesn't support assigning `servicePlans` to an Azure user

> **Collapse: MongoDB Connector**
>
> * OPENICF-2394: Align Scripted Connector templates

> **Collapse: Salesforce connector**
>
> * OPENICF-2357: Salesforce Connector doesn't allow listing of licenses

> **Collapse: SAP connector**
>
> * OPENICF-2035: SAP Account Object Type attributes
>
> * OPENICF-2036: SAP Role Object Type Attributes
>
> * OPENICF-2037: SAP UM Profile Object Type Attributes
>
> * OPENICF-2292: Group Object Type attributes
>
> * OPENICF-2350: R3 script uses deprecated methods to parse date
>
> * OPENICF-2360: NPE getting SAP configuration
>
> * OPENICF-2377: Active Group memberships should not sync activity group name
>
> * OPENICF-2379: Should not retrieve, display, or allow manipulation of password hashing attributes
>
> * OPENICF-2386: Router should not be a required attribute
>
> * OPENICF-2388: Must throw an error upon user create/update/delete error
>
> * OPENICF-2394: Align Scripted Connector templates
>
> * OPENICF-2397: Add pagination
>
> * OPENICF-2419: Timestamp filtering support
>
> * OPENICF-2432: Default location for the ScriptRoots is incorrect
>
> * OPENICF-2435: Respect boolean response from search result handler
>
> * OPENICF-2452: Filter CODVN, CODVC, and CODVS from User LOGONDATA
>
> * OPENICF-2459: Query with `_queryFilter=true` no longer returns full user object

> **Collapse: ScriptedREST Connector**
>
> * OPENICF-2430: Search and Sync operations do not respect handler result
>
> * OPENICF-2394: Align Scripted Connector templates

> **Collapse: ScriptedSQL Connector**
>
> * OPENICF-2429: Search and Sync operations do not respect handler result
>
> * OPENICF-2394: Align Scripted Connector templates

> **Collapse: SSH Connector**
>
> * OPENICF-2394: Align Scripted Connector templates

> **Collapse: Workday connector**
>
> * OPENICF-2438: `externalFieldAndParameterCriteria` config parameter should not be set to null by default

## 1.5.20.15 Connectors

> **Collapse: Adobe Marketing Cloud connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Database Table Connector**
>
> * OPENICF-2308: Database Table Connector - Possible regression of OPENICF-903
>
> * OPENICF-1987: ORA-00933 - SQL command not properly ended error using Database Table Connector

> **Collapse: Dropbox Connector**
>
> Initial release of the Dropbox connector. Refer to [Dropbox connector](../connector-reference/dropbox.html) for more information.
>
> * OPENICF-2051: Dropbox connector

> **Collapse: Microsoft Graph API connector**
>
> * OPENICF-2306: MS Graph API Connector: Creating and updating applications with certificates fails
>
> * OPENICF-2269: MS Graph API Connector: Implement application role assignments
>
> * OPENICF-1964: MS Graph API Connector: Add the ability to handle User's Contacts object
>
> * OPENICF-2315: MS Graph API Connector: otherMails attribute should be an array of strings

> **Collapse: Salesforce connector**
>
> * OPENICF-2343: Cannot delete a list of PermissionSetAssignments

> **Collapse: SCIM connector**
>
> * OPENICF-2320: SCIM Connector: totalResults is not used when query is using paging
>
> * OPENICF-2321: SCIM Connector: pagedResultsOffset is not used properly
>
> * OPENICF-2325: SCIM Connector: HTTP error 429 should have a more explicit message
>
> * OPENICF-2323: SCIM Connector: prevent query with sorting when the Service Provider does not accept sorting
>
> * OPENICF-1916: SCIM Connector: Support for throttling

> **Collapse: ScriptedSQL Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: ServiceNow connector**
>
> No public changes were made specific to this connector, though a new version was released.

## 1.5.20.14 Connectors

> **Collapse: AS400 Connector**
>
> * OPENICF-2236 - AS400 Connector: does not expose all the AS400ConnectionPool configuration properties

> **Collapse: Google Apps connector**
>
> * OPENICF-2252: GoogleApps Connector: Unable to configure connector via UI

> **Collapse: LDAP connector**
>
> * OPENICF-2225: LDAP Connector: syncToken nativeType to be configurable / updated - mismatch with DS type stops livesync

> **Collapse: Marketo connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Microsoft Graph API connector**
>
> * OPENICF-1976: MS Graph API Connector: Ability to create guest users
>
> * OPENICF-2208: MS Graph API Connector: add the ability to read "application" and "servicePrincipal" object
>
> * OPENICF-2238: MS Graph API Connector: unable to retrieve roles
>
> * OPENICF-2247: MS Graph API Connector: Query filters on collections and filters requiring advanced query parameters cause errors
>
> * OPENICF-2248: MS Graph API Connector: Implement role assignment and role eligibility schedules
>
> * OPENICF-2251: MS Graph API Connector: \_\_ACCOUNT\_\_ data listing fails in native console for assignedLicenses
>
> * OPENICF-2257: MS Graph API Connector: Clicking Role Assignment in Data tab throws a Graph API error
>
> * OPENICF-2267: MS Graph API Connector: Proxy -→ Java.lang.ClassCastException: class okhttp3.OkHttpClient cannot be cast to class com.azure.core.http.HttpClient (okhttp3.OkHttpClient and com.azure.core.http.HttpClient are in unnamed module of loader
>
> * OPENICF-2270: MS Graph API Connector: Adding API permissions to applications fails
>
> * OPENICF-2271: MS Graph API Connector: proxy basic auth not implemented but referenced
>
> * OPENICF-2275: MS Graph API Connector: Refactor connector new object handlers and UnsupportedOperationException handling

> **Collapse: Oracle EBS connector**
>
> Initial release of the EBS connector. Refer to [Oracle EBS connector](../connector-reference/ebs.html) for more information.
>
> * OPENICF-1781: EBS Connector V1.0

> **Collapse: Peoplesoft connector**
>
> * OPENICF-2311: PeopleSoft Connector: Remove embedded `psft-2.0` and `psjoa-1.0` Jar files

> **Collapse: Salesforce connector**
>
> * OPENICF-2176 - Salesforce Connector: Support Feature License Elements as List on User Object

> **Collapse: SCIM connector**
>
> * OPENICF-1922 SCIM Connector: PATCH operation should use `path` attribute for "add" and "replace"
>
> * OPENICF-2241: SCIM Connector: Service Provider Config settings don't work for Salesforce

## 1.5.20.12 Connectors

> **Collapse: AS400 Connector**
>
> Initial release of the AS400 connector. Refer to [AS400 connector](../connector-reference/as400.html) for more information.

> **Collapse: Google Apps connector**
>
> * OPENICF-2192: NPE when updating LicenseAssignments through a user update
>
> * OPENICF-2117: Hide Alternate Emails from the schema
>
> * OPENICF-2195: Intermittent NPE when we try to read newly created user

> **Collapse: LDAP connector**
>
> * OPENICF-400: LDAP connector should be able to properly handle reading the AD tokenGroups attribute

> **Collapse: PeopleSoft connector**
>
> * OPENICF-2033: PeopleSoft Connector v2.0

> **Collapse: SAP connector**
>
> * OPENICF-2183: Exception when SAP connector is running in OpenIDM

> **Collapse: SAP SuccessFactors connector**
>
> * OPENICF-2007: SAP SuccessFactors v2

> **Collapse: SCIM connector**
>
> * OPENICF-1916: Support for throttling
>
> * OPENICF-2207: Ability to define Accept: and Content-Type: HTTP headers

> **Collapse: Workday connector**
>
> * OPENICF-2030: Connector breaks when workerID is empty when using RCS
>
> * OPENICF-2150: Ability to add field and parameter to the request criteria

## 1.5.20.11 Connectors

> **Collapse: Adobe Marketing Cloud connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: AWS connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Box connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Cerner connector**
>
> * OPENICF-1960: Cerner Connector v2

> **Collapse: CSV connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: DocuSign connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Epic connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: GCP connector**
>
> Initial release of the GCP connector. Refer to [Google Cloud Platform connector](../connector-reference/gcp.html) for more information.
>
> * OPENICF-1749: GCP Connector

> **Collapse: Google Apps connector**
>
> * OPENICF-2039: GoogleApps Connector: missing some user attributes
>
> * OPENICF-2040: GoogleApps Connector: Manage role attributes
>
> * OPENICF-2041: GoogleApps Connector: Group attributes
>
> * OPENICF-2064: Google Apps Connector: Query the Google Workspace instance for Licenses
>
> * OPENICF-2066: GoogleApps Connector: Ability to query Roles and RoleAssignments
>
> * OPENICF-2136: Google Apps Connector: Exponential Back off for reading google objects required

> **Collapse: HubSpot connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: IBM RACF connector**
>
> * OPENICF-1762: IBM RACF API Connector
>
> |   |                                                                                                                                     |
> | - | ----------------------------------------------------------------------------------------------------------------------------------- |
> |   | There was a previous RACF connector, which is deprecated. Users of the previous RACF connector should migrate to the new connector. |

> **Collapse: LDAP connector**
>
> * OPENICF-1856: LDAP Connector: Assignment of static group to IDM User fails to assign it on LDAP side if user is already a member of a Dynamic Group on LDAP side
>
> * OPENICF-2089: LDAP Connector: ldapGroups membership does not take into account nested membership of other groups
>
> * OPENICF-2108: LDAP Connector: slow group membership updates with unindexed member/uniqueMember attributes in DS
>
> * OPENICF-2126: Assignment Issue: Managed User to DS Groups Failure to Select Target Group

> **Collapse: Marketo connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Microsoft Graph API connector**
>
> * OPENICF-2068: MSGraphAPI Connector: Implement Azure AD Directory Roles support
>
> * OPENICF-2088: MSGraphAPI Connector: Implement Azure AD custom role creation

> **Collapse: PeopleSoft connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Salesforce connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: SAP S/4HANA connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: SAP SuccessFactors connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: SCIM connector**
>
> * OPENICF-2112: SCIM Connector: caseSensitive
>
> * OPENICF-2113: SCIM Connector: problem with "issuedAt" from OAuth neg
>
> * OPENICF-2114: SCIM Connector: use authenticationBasic as an option for OAuth neg
>
> * OPENICF-2125: SCIM Connector: Fix Filter

> **Collapse: Scripted REST connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: ServiceNow connector**
>
> * OPENICF-2130: ServiceNow connector query results do not match what is returned from API

> **Collapse: Workday connector**
>
> No public changes were made specific to this connector, though a new version was released.

## 1.5.20.9 Connectors

> **Collapse: LDAP Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Microsoft Graph API Connector**
>
> * OPENICF-1614: MS Graph API Connector: Livesync on user/group does not populate membership
>
> * OPENICF-1858: MS Graph API Connector: Add Group Owners management

> **Collapse: SAP Connector**
>
> * OPENICF-1675: SAP Connector: Groovy deps should be embedded
>
> * OPENICF-2071: SAP Connector: Cannot update ACTIVITY GROUPS for users

## 1.5.20.8 Connectors

> **Collapse: CSV File Connector**
>
> * OPENICF-1935: CSV Connector: generates a stacktrace for Read Only permission files
>
> * OPENICF-1969: CSV Connector: Update csv connector parsing library
>
> * OPENICF-1258: CSV Connector: stripping empty strings, replacing with nulls.

> **Collapse: DatabaseTable Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Google Apps Connector**
>
> * OPENICF-2038: Google Apps Connector: Updating user's group membership may return NPE

> **Collapse: LDAP Connector**
>
> * OPENICF-1977: LDAP Connector: Detect CA LDAP directory server

> **Collapse: Microsoft Graph API Connector**
>
> * OPENICF-1606: MS Graph API Connector: Upgrade to MS Graph Java SDK v3
>
> * OPENICF-1807: MS Graph API Connector: Better handle failure of hard delete
>
> * OPENICF-1819: MS Graph API Connector: "performHardDelete" should be set to false by default

> **Collapse: PeopleSoft Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Salesforce Connector**
>
> * OPENICF-2002: Salesforce Connector: syncFailureHandler can exceed maxRetries

> **Collapse: ScriptedSQL Connector**
>
> No public changes were made specific to this connector, though a new version was released.

## 1.5.20.7 Connectors

> **Collapse: AWS Connector**
>
> Initial release of the AWS IAM connector. Refer to [Amazon Web Services (AWS) connector](../connector-reference/aws-iam.html) for more information.
>
> * OPENICF-1780: AWS IAM Connector

> **Collapse: DatabaseTable Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Google Apps Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: LDAP Connector**
>
> * OPENICF-1897: LDAP Connector: Add support for nested AD groups

> **Collapse: MongoDB Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: PeopleSoft Connector**
>
> Initial release of the Oracle PeopleSoft connector. Refer to [PeopleSoft connector](../connector-reference/peoplesoft.html) for more information.
>
> * OPENICF-1748: PeopleSoft Connector

> **Collapse: Salesforce Connector**
>
> * OPENICF-1812: SalesForce Connector: syncFailureHandler maxRetries is not working

> **Collapse: SAP S/4HANA Connector**
>
> Initial release of the SAP S/4HANA connector. Refer to [SAP S/4HANA connector](../connector-reference/sap-hana.html) for more information.
>
> * OPENICF-1782: SAP Hana Connector

> **Collapse: ScriptedSQL Connector**
>
> No public changes were made specific to this connector, though a new version was released.

## 1.5.20.6 Connectors

> **Collapse: Cerner Connector**
>
> Initial release of the Cerner connector. Refer to [Cerner connector](../connector-reference/cerner.html) for more information.
>
> * OPENICF-1737: Cerner Connector

> **Collapse: Epic Connector**
>
> * OPENICF-1818: Epic V2 Connector
>
> * OPENICF-1878: Epic Connector: Query filter not matching uid returns HTTP 404

> **Collapse: Google Apps Connector**
>
> * OPENICF-1181: Google Apps Connector: Unable to delete custom attributes

> **Collapse: LDAP Connector**
>
> * OPENICF-1901: LDAP Connector: Reduce JVM garbage from ConnectorObjectBuilder and AttributeBuilder

> **Collapse: MongoDB Connector**
>
> * OPENICF-1833: Update MongoDB driver to the latest for compatibility with newer versions of MongoDB

## 1.5.20.5 Connectors

> **Collapse: Adobe Marketing Cloud Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Database Table Connector**
>
> * OPENICF-1711: Database Table Connector - ORA-22816 error when using Oracle trigger

> **Collapse: Epic Connector**
>
> Initial release of the Epic connector. Refer to [Epic connector](../connector-reference/epic.html) for more information.
>
> * OPENICF-1750: Epic Connector

> **Collapse: Google Apps Connector**
>
> * OPENICF-1808: Google Apps Connector: when user is provisioned using a role assignment, group isn't set correctly

> **Collapse: LDAP Connector**
>
> * OPENICF-1859: LDAP Connector: \_memberId is not returned with AD & liveSync if attribute range is used

> **Collapse: Marketo Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Salesforce Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: SCIM Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Scripted REST Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Scripted SQL Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: SAP SuccessFactors Connector**
>
> * OPENICF-1822: SuccessFactors should not require PEM formatted file on disk

## 1.5.20.4 Connectors

> **Collapse: Google Apps Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Microsoft Graph API Connector**
>
> No public changes were made specific to this connector, though a new version was released.

## 1.5.20.3 Connectors

> **Collapse: Database Table Connector**
>
> * OPENICF-1692: Database Table Connector: throwing a null pointer exception

> **Collapse: Google Apps Connector**
>
> * OPENICF-1716: Google Apps Connector: Add recoveryEmail and recoveryPhone attributes for User

> **Collapse: LDAP Connector**
>
> * OPENICF-1731: LDAP Connector: Escape characters (\\) not properly handled on delete and updates ops

> **Collapse: Scripted SQL Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: ServiceNow Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Workday Connector**
>
> No public changes were made specific to this connector, though a new version was released.

## 1.5.20.2 Connectors

> **Collapse: CSV File Connector**
>
> * OPENICF-1677: CSV Connector returns pagedResultsCookie for queries with \_pageSize=0.

> **Collapse: LDAP Connector**
>
> * OPENICF-1666: LDAP Connector: ldapGroups should restrict membership to the specified contexts.

> **Collapse: Microsoft Graph API Connector**
>
> * OPENICF-1656: MS Graph API Connector: Unable to update onPremisesExtensionAttributes.
>
> * OPENICF-1687: MS Graph API Connector: Should be able to work behind an HTTP Proxy.
>
> * OPENICF-1698: MS Graph API Connector: get the cause of exception if test() fails.

> **Collapse: Workday Connector**
>
> * OPENICF-1689: Workday Connector: Workers transaction logs are filtered.
>
> * OPENICF-1691: Workday Connector: Reduce Garbage collection when building connector objects.

## 1.5.20.1 Connectors

|   |                                                                                                   |
| - | ------------------------------------------------------------------------------------------------- |
|   | 1.5.20.1 is a limited release, where only the Database Table Connector was released to Backstage. |

> **Collapse: Database Table Connector**
>
> * OPENICF-1477: Database Table Connector: ORA-01000: maximum open cursors exceeded
>
> * OPENICF-1596: PSQLException: FATAL: terminating connection due to idle-in-transaction timeout

## 1.5.20.0 Connectors

> **Collapse: Generic LDAP Connector**
>
> * OPENICF-1560: LDAP Connector: RFE Disable Paged Results Control
>
> * OPENICF-1586: LDAP Connector: Timestamp sync strategy: Synchronization filters are not used properly

> **Collapse: MongoDB Connector**
>
> * OPENICF-1553: MongoDB Connector: convertBSONtoICF() does not traverse Arrays.

> **Collapse: Microsoft Graph API Connector**
>
> * OPENICF-1538: MS Graph API Connector: Sync() does not work
>
> * OPENICF-1541: MS Graph API Connector: Add ConsistencyLevel: eventual' header and $count=true for endsWith filter
>
> * OPENICF-1557: MS Graph API Connector: Handle user employeeHireDate attribute and Calendar data type
>
> * OPENICF-1558: MS Graph API Connector: Make sure sortKey is supported by the objectClass
>
> * OPENICF-1559: MS Graph API Connector: Implement Authenticate() call
>
> * OPENICF-1595: MS Graph API Connector: test() should connect to the MS Graph endpoint to validate the connectionThe following known issues will be addressed in a later release:
>
> * OPENICF-1614: MS Graph API Connector: Livesync on user/group does not populate membership
>
> * OPENICF-1615: MS Graph API Connector: Deleting Azure AD group works but throws HTTP 500

> **Collapse: SCIM Connector**
>
> * OPENICF-1589: SCIM Connector: NPE caused by exception not properly handled
>
> * OPENICF-1591: SCIM Connector: Parsing OAuth response should not fail on unknown properties
>
> * OPENICF-1598: SCIM Connector: NPE when updating attribute with null value
>
> * OPENICF-1600: SCIM Connector: unknown attributes in a query result should not throw parsing exception
>
> * OPENICF-1601: SCIM Connector: Implement a global connection timeout property

## 1.5.19.6 Connectors

No issues specific any connectors were addressed in this release.

## 1.5.19.5 Connectors

> **Collapse: CSV File Connector**
>
> * OPENICF-1530: system?\_action=createFullConfig validation does not return consistent errors

> **Collapse: Database Table Connector**
>
> * OPENICF-1510: Errors in Database Table Connector docs

> **Collapse: Groovy connector toolkit**
>
> * OPENICF-1523: ScriptedGroovy connectors fail to load in IDM 7.x when embedded Groovy version does not match IDM Groovy version

> **Collapse: Microsoft Graph API Connector**
>
> * OPENICF-1493: MS Graph API Connector: add the ability to read/assign license for the user
>
> * OPENICF-1499: MS Graph API Connector: remove the maximumConnections property
>
> * OPENICF-1507: MS Graph API Connector: add the ability to read subscribedSku object
>
> * OPENICF-1525: MS Graph API Connector: replace the default Graph SDK logger
>
> * OPENICF-1526: MS Graph API Connector: add the ability to read Team objects

> **Collapse: Salesforce Connector**
>
> * OPENICF-1522: Salesforce Connector : implement StatefulConfiguration to allow persistence of accessToken in memory

> **Collapse: SCIM Connector**
>
> * OPENICF-1518: SCIM connector: Http client ConnectionManager is not set properly

> **Collapse: Workday Connector**
>
> * OPENICF-1504: Workday Connector: SyncToken should be updated even if no events
>
> * OPENICF-1506: Workday Connector: SyncToken should be set to tenant timestamp after call to sync()
>
> * OPENICF-1508: Workday Connector: Query on SCR objects should not include date range as a search criteria

## 1.5.19.4 Connectors

No issues specific any connectors were addressed in this release.

## 1.5.19.3 Connectors

> **Collapse: Microsoft Graph API Connector**
>
> * OPENICF-1475: MS Graph API Connector: the 'manager' only returns the id and not the full object
>
> * OPENICF-1481: MS Graph API Connector: add the ability to assign/remove user's manager
>
> * OPENICF-1483: MS Graph API Connector: can't remove all groups a user belongs to

> **Collapse: Salesforce Connector**
>
> * OPENICF-1471: SalesForce Connector: should not implement PoolableConnector interface

## 1.5.19.2 Connectors

> **Collapse: Generic LDAP Connector**
>
> * OPENICF-1448: LDAP Connector: Enabling changelog livesync for oracle unified directory (OUD)
>
> * OPENICF-1466: LDAP Connector: Update filterWithOrInsteadOfAnd to apply to timestamp and Active Directory liveSync
>
> * OPENICF-1470: LDAP Connector: Null Check in ADUserAccounControl.addControl
>
> * OPENICF-1472: LDAP Connector: Data not synced from AD to IDM via livesync on \_\_ALL\_\_ object

> **Collapse: Microsoft Graph API Connector**
>
> * OPENICF-1469: MS Graph API Connector: implement a read/write rate limiter

> **Collapse: SCIM Connector**
>
> * OPENICF-1401: SCIM Connector: Align exceptions for not configured (blank/null) configurationProperties

## 1.5.19.1 Connectors

> **Collapse: Microsoft Graph API Connector**
>
> * OPENICF-1446: MS Graph API Connector: implement PoolableConnector

> **Collapse: Salesforce Connector**
>
> * OPENICF-1352: Salesforce connector: pagination and cookies not working properly

> **Collapse: SCIM Connector**
>
> * OPENICF-1444: SCIM connector - provide support for 'scope'

> **Collapse: SSH Connector**
>
> * OPENICF-1433: SSH connector: Kerberos username prompt for public key and password auth
>
> * OPENICF-1445: SSH connector: Stale or disconnected SSH sessions are not detected when borrowing from the pool

> **Collapse: Workday Connector**
>
> * OPENICF-1383: Workday Connector: Upgrade to API v35.0
>
> * OPENICF-1419: Workday Connector: Implement Service Center Representative object type
>
> * OPENICF-1426: Workday Connector: Ability to update email for Service Center Representative object
>
> * OPENICF-1432: Workday Connector: Implement OR filter
>
> * OPENICF-1447: Workday Connector: add the Contingent\_Worker\_ID as a search criteria

## 1.5.19.0 Connectors

|   |                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Starting in version 1.5.19.0, ICF connectors that previously had external library dependencies now have those dependencies bundled inside the connector. |

Initial release of the MS Graph API Connector.

> **Collapse: Generic LDAP Connector**
>
> * OPENICF-1388: LDAP Connector 1.5.5.0 throws java.lang.NoSuchMethodError on Java 8
>
> * OPENICF-1396: OPENIDM-15448 changes seemingly broke querying ldap via the data tab

> **Collapse: Groovy connector toolkit**
>
> * OPENICF-1414: Scripted Groovy (v3) based connectors fail to load with IDM releases prior to 7.0

## 1.5.18.0 Connectors

|   |                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------- |
|   | Starting in version 1.5.18.0, the ICF Connector Framework and all connectors bundled with IDM share a unified version number. |

No issues specific any connectors were addressed in this release.

---

---
title: Deprecation
description: Release notes tracking deprecated ICF connector functionality across versions, with migration guidance for replaced attributes and object types
component: openicf
page_id: openicf:connector-release-notes:deprecated-functionality
canonical_url: https://docs.pingidentity.com/openicf/connector-release-notes/deprecated-functionality.html
section_ids:
  1_5_20_33: 1.5.20.33
  google_apps_connector: Google Apps connector
  1_5_20_30: 1.5.20.30
  servicenow_connector: ServiceNow connector
  1_5_20_21: 1.5.20.21
  google_apps_connector_2: Google Apps connector
  earlier_than_1_5_18_0: Earlier than 1.5.18.0
  deprecated-java-date: JAVA_TYPE_DATE attribute type
---

# Deprecation

The following functionality is deprecated and likely to be removed in a future release.

## 1.5.20.33

### [Google Apps connector](../connector-reference/google.html)

* Using the StartsWith (`SW`) filter on the `orgUnitPath` attribute to query the `OrgUnit` object is deprecated. Use the Equals (`EQ`) filter on the new `parentOrgUnitPath` attribute.

  Learn more in [Supported search filters](../connector-reference/google.html#google-apps-search-filters).

## 1.5.20.30

### [ServiceNow connector](../connector-reference/servicenow.html)

* The `sys_id` ServiceNow connector attribute is deprecated and replaced with the `__NAME__` attribute.

- The `user` object type in the ServiceNow schema is deprecated. Use the native `__ACCOUNT__` object type instead.

## 1.5.20.21

### [Google Apps connector](../connector-reference/google.html)

The `__SECONDARY_EMAIL__` user attribute is deprecated. Use the newer attribute `__SECONDARY_EMAILS__`. These two attributes are mutually exclusive.

## Earlier than 1.5.18.0

### `JAVA_TYPE_DATE` attribute type

Support for the native attribute type `JAVA_TYPE_DATE` is deprecated and will be removed in a future release. This property-level extension is an alias for `string`. Any dates assigned to this extension should be formatted per ISO 8601.

---

---
title: ICF release notes
description: Release notes for the connectors that are supported with PingIDM and Advanced Identity Cloud and covers changes to connectors since ICF 1.5.18.0
component: openicf
page_id: openicf:connector-release-notes:feed
canonical_url: https://docs.pingidentity.com/openicf/connector-release-notes/feed.html
revdate: March 20, 2026
section_ids:
  framework: Connector framework release notes
  1_5_20_35_framework: 1.5.20.35 Framework
  1_5_20_34_framework: 1.5.20.34 Framework
  1_5_20_33_framework: 1.5.20.33 Framework
  1_5_20_32_framework: 1.5.20.32 Framework
  1_5_20_31_framework: 1.5.20.31 Framework
  1_5_20_30_framework: 1.5.20.30 Framework
  1_5_20_29_framework: 1.5.20.29 Framework
  1_5_20_28_framework: 1.5.20.28 Framework
  1_5_20_26_framework: 1.5.20.26 Framework
  1_5_20_25_framework: 1.5.20.25 Framework
  1_5_20_24_framework: 1.5.20.24 Framework
  1_5_20_23_framework: 1.5.20.23 Framework
  1_5_20_22_framework: 1.5.20.22 Framework
  1_5_20_21_framework: 1.5.20.21 Framework
  1_5_20_18_framework: 1.5.20.18 Framework
  1_5_20_15_framework: 1.5.20.15 Framework
  1_5_20_11_framework: 1.5.20.11 Framework
  1_5_20_8_framework: 1.5.20.8 Framework
  1_5_20_7_framework: 1.5.20.7 Framework
  1_5_20_6_framework: 1.5.20.6 Framework
  1_5_20_5_framework: 1.5.20.5 Framework
  1_5_20_4_framework: 1.5.20.4 Framework
  1_5_20_3_framework: 1.5.20.3 Framework
  1_5_20_0_framework: 1.5.20.0 Framework
  1_5_19_6_framework: 1.5.19.6 Framework
  1_5_19_5_framework: 1.5.19.5 Framework
  1_5_19_4_framework: 1.5.19.4 Framework
  1_5_19_3_framework: 1.5.19.3 Framework
  1_5_19_2_framework: 1.5.19.2 Framework
  1_5_19_1_framework: 1.5.19.1 Framework
  1_5_19_0_framework: 1.5.19.0 Framework
  1_5_18_0_framework: 1.5.18.0 Framework
  connectors: Connector release notes
  _1_5_20_35_connectors: 1.5.20.35 Connectors
  updated_connectors_with_change_details: Updated connectors with change details
  ms_graph_api: MS Graph API
  multiple_csv_connector: Multiple CSV connector
  pingone_connector: PingOne connector
  _1.5.20.35_saascommon: SaaS Common
  snowflake_connector: Snowflake connector
  updated_connectors_without_change_details: Updated connectors without change details
  1_5_20_34_connectors: 1.5.20.34 Connectors
  updated_connectors_with_change_details_2: Updated connectors with change details
  ldap_connector: LDAP connector
  microsoft_graph_api_connector: Microsoft Graph API connector
  updated_connectors_without_change_details_2: Updated connectors without change details
  1_5_20_33_connectors: 1.5.20.33 Connectors
  new_connectors: New connectors
  snowflake_connector_2: Snowflake connector
  updated_connectors_with_change_details_3: Updated connectors with change details
  google_apps_connector: Google Apps connector
  ldap_connector_2: LDAP connector
  oracle_ebs_connector: Oracle EBS connector
  _1.5.20.33_saascommon: SaaS Common
  sap_successfactors_connector: SAP SuccessFactors connector
  scim_connector: SCIM connector
  workday_connector: Workday connector
  updated_connectors_without_change_details_3: Updated connectors without change details
  1_5_20_32_connectors: 1.5.20.32 Connectors
  updated_connectors_with_change_details_4: Updated connectors with change details
  dropbox_connector_saas_common: Dropbox connector (SaaS common)
  ldap_connector_3: LDAP connector
  _1.5.20.32_saascommon: SaaS Common
  saas_rest_connector_saas_common: SaaS REST Connector (SaaS common)
  sap_hana_database_connector: SAP HANA Database connector
  updated_connectors_without_change_details_4: Updated connectors without change details
  1_5_20_31_connectors: 1.5.20.31 Connectors
  updated_connectors_with_change_details_5: Updated connectors with change details
  docusign_connector: DocuSign connector
  multiple_csv_connector_2: Multiple CSV connector
  multiple_csv_cloud_connector: Multiple CSV Cloud connector
  sap_successfactors_connector_2: SAP SuccessFactors connector
  saas_rest_connector: SaaS REST Connector
  scim_connector_2: SCIM connector
  updated_connectors_without_change_details_5: Updated connectors without change details
  1_5_20_30_connectors: 1.5.20.30 Connectors
  updated_connectors_with_change_details_6: Updated connectors with change details
  database_table_connector: Database Table connector
  google_apps_connector_2: Google Apps connector
  kerberos_connector: Kerberos connector
  ldap_connector_4: LDAP connector
  microsoft_graph_api_connector_2: Microsoft Graph API connector
  _1.5.20.30_saascommon: SaaS Common
  saas_rest_connector_2: SaaS REST Connector
  salesforce_connector: Salesforce connector
  scim_connector_3: SCIM connector
  servicenow_connector: ServiceNow connector
  updated_connectors_without_change_details_6: Updated connectors without change details
  1_5_20_29_connectors: 1.5.20.29 Connectors
  new_connectors_2: New connectors
  saas_rest_connector_3: SaaS REST Connector
  updated_connectors_with_change_details_7: Updated connectors with change details
  adobe_marketing_cloud_connector: Adobe Marketing Cloud connector
  box_connector: Box connector
  epic_connector: Epic connector
  google_cloud_platform_connector: Google Cloud Platform connector
  hubspot_connector: HubSpot connector
  ldap_connector_5: LDAP connector
  marketo_connector: Marketo connector
  _1.5.20.29_saascommon: SaaS Common
  salesforce_connector_2: Salesforce connector
  sap_successfactors_connector_3: SAP SuccessFactors connector
  scim_connector_4: SCIM connector
  servicenow_connector_2: ServiceNow connector
  1_5_20_28_connectors: 1.5.20.28 Connectors
  new_connectors_3: New connectors
  updated_connectors_with_change_details_8: Updated connectors with change details
  microsoft_graph_api_connector_3: Microsoft Graph API connector
  updated_connectors_without_change_details_7: Updated connectors without change details
  1_5_20_27_connectors: 1.5.20.27 Connectors
  updated_connectors_with_change_details_9: Updated connectors with change details
  google_apps_connector_3: Google Apps connector
  ldap_connector_6: LDAP connector
  1_5_20_26_connectors: 1.5.20.26 Connectors
  new_connectors_4: New connectors
  updated_connectors_with_change_details_10: Updated connectors with change details
  aws_iam_identity_center_connector: AWS IAM Identity Center connector
  epic_connector_2: Epic connector
  ldap_connector_7: LDAP connector
  microsoft_graph_api_connector_4: Microsoft Graph API connector
  mongodb_connector_scripted_groovy: MongoDB connector (Scripted Groovy)
  sap_s4hana_connector: SAP S/4HANA connector
  scim_connector_5: SCIM connector
  _1.5.20.26_scriptedgroovy: Scripted Groovy
  workday_connector_2: Workday connector
  updated_connectors_without_change_details_8: Updated connectors without change details
  1_5_20_23_connectors: 1.5.20.23 Connectors
  new_connectors_5: New connectors
  updated_connectors_with_change_details_11: Updated connectors with change details
  adobe_admin_console_connector_saas_common: Adobe Admin Console connector (SaaS common)
  amazon_web_services_aws_connector: Amazon Web Services (AWS) connector
  ldap_connector_8: LDAP connector
  microsoft_graph_api_connector_5: Microsoft Graph API connector
  _1.5.20.23_saascommon: SaaS Common
  sap_successfactors_connector_4: SAP SuccessFactors connector
  webex_connector_saas_common: Webex Connector (SaaS common)
  workday_connector_3: Workday connector
  updated_connectors_without_change_details_9: Updated connectors without change details
  1_5_20_22_connectors: 1.5.20.22 Connectors
  updated_connectors_with_change_details_12: Updated connectors with change details
  adobe_admin_console_connector: Adobe Admin Console connector
  database_table_connector_2: Database Table connector
  docusign_connector_2: DocuSign connector
  ibm_racf_connector: IBM RACF connector
  mongodb_connector: MongoDB connector
  oracle_ebs_connector_2: Oracle EBS connector
  pingone_connector_2: PingOne connector
  sap_successfactors_connector_5: SAP SuccessFactors connector
  scim_connector_6: SCIM connector
  workday_connector_4: Workday connector
  updated_connectors_without_change_details_10: Updated connectors without change details
  1_5_20_21_connectors: 1.5.20.21 Connectors
  updated_connectors_with_change_details_13: Updated connectors with change details
  dropbox_connector: Dropbox connector
  epic_connector_3: Epic connector
  google_apps_connector_4: Google Apps connector
  ldap_connector_9: LDAP connector
  pingone_connector_3: PingOne connector
  sap_connector: SAP connector
  scripted_rest_connector: Scripted REST connector
  webex_connector: Webex Connector
  updated_connectors_without_change_details_11: Updated connectors without change details
  1_5_20_20_connectors: 1.5.20.20 Connectors
  updated_connectors_with_change_details_14: Updated connectors with change details
  database_table_connector_3: Database Table connector
  google_apps_connector_5: Google Apps connector
  microsoft_graph_api_connector_6: Microsoft Graph API connector
  salesforce_connector_3: Salesforce connector
  scim_connector_7: SCIM connector
  updated_connectors_without_change_details_12: Updated connectors without change details
  1_5_20_19_connectors: 1.5.20.19 Connectors
  updated_connectors_with_change_details_15: Updated connectors with change details
  scim_connector_8: SCIM connector
  updated_connectors_without_change_details_13: Updated connectors without change details
  1_5_20_18_connectors: 1.5.20.18 Connectors
  updated_connectors_with_change_details_16: Updated connectors with change details
  dropbox_connector_2: Dropbox connector
  google_apps_connector_6: Google Apps connector
  ldap_connector_10: LDAP connector
  microsoft_graph_api_connector_7: Microsoft Graph API connector
  salesforce_connector_4: Salesforce connector
  sap_connector_2: SAP connector
  sap_hana_database_connector_2: SAP HANA Database connector
  scim_connector_9: SCIM connector
  updated_connectors_without_change_details_14: Updated connectors without change details
  1_5_20_17_connectors: 1.5.20.17 Connectors
  1_5_20_16_connectors: 1.5.20.16 Connectors
  1_5_20_15_connectors: 1.5.20.15 Connectors
  1_5_20_14_connectors: 1.5.20.14 Connectors
  1_5_20_12_connectors: 1.5.20.12 Connectors
  1_5_20_11_connectors: 1.5.20.11 Connectors
  1_5_20_9_connectors: 1.5.20.9 Connectors
  1_5_20_8_connectors: 1.5.20.8 Connectors
  1_5_20_7_connectors: 1.5.20.7 Connectors
  1_5_20_6_connectors: 1.5.20.6 Connectors
  1_5_20_5_connectors: 1.5.20.5 Connectors
  1_5_20_4_connectors: 1.5.20.4 Connectors
  1_5_20_3_connectors: 1.5.20.3 Connectors
  1_5_20_2_connectors: 1.5.20.2 Connectors
  1_5_20_1_connectors: 1.5.20.1 Connectors
  1_5_20_0_connectors: 1.5.20.0 Connectors
  1_5_19_6_connectors: 1.5.19.6 Connectors
  1_5_19_5_connectors: 1.5.19.5 Connectors
  1_5_19_4_connectors: 1.5.19.4 Connectors
  1_5_19_3_connectors: 1.5.19.3 Connectors
  1_5_19_2_connectors: 1.5.19.2 Connectors
  1_5_19_1_connectors: 1.5.19.1 Connectors
  1_5_19_0_connectors: 1.5.19.0 Connectors
  1_5_18_0_connectors: 1.5.18.0 Connectors
  java-rcs-release-notes: Java RCS release notes
  1_5_20_35_java_rcs: 1.5.20.35 Java RCS
  1_5_20_34_java_rcs: 1.5.20.34 Java RCS
  1_5_20_33_java_rcs: 1.5.20.33 Java RCS
  1_5_20_32_java_rcs: 1.5.20.32 Java RCS
  1_5_20_31_java_rcs: 1.5.20.31 Java RCS
  1_5_20_30_java_rcs: 1.5.20.30 Java RCS
  1_5_20_29_java_rcs: 1.5.20.29 Java RCS
  1_5_20_28_java_rcs: 1.5.20.28 Java RCS
  1_5_20_27_java_rcs: 1.5.20.27 Java RCS
  1_5_20_26_java_rcs: 1.5.20.26 Java RCS
  1_5_20_23_java_rcs: 1.5.20.23 Java RCS
  java_17_required: Java 17 required
  more_bundled_connectors: More bundled connectors
  1_5_20_22_java_rcs: 1.5.20.22 Java RCS
  1_5_20_21_java_rcs: 1.5.20.21 Java RCS
  1_5_20_18_java_rcs: 1.5.20.18 Java RCS
  1_5_20_15_java_rcs: 1.5.20.15 Java RCS
  1_5_20_14_java_rcs: 1.5.20.14 Java RCS
  1_5_20_12_java_rcs: 1.5.20.12 Java RCS
  1_5_20_11_java_rcs: 1.5.20.11 Java RCS
  1_5_20_9_java_rcs: 1.5.20.9 Java RCS
  1_5_20_8_java_rcs: 1.5.20.8 Java RCS
  1_5_20_7_java_rcs: 1.5.20.7 Java RCS
  1_5_20_6_java_rcs: 1.5.20.6 Java RCS
  1_5_20_5_java_rcs: 1.5.20.5 Java RCS
  1_5_20_4_java_rcs: 1.5.20.4 Java RCS
  1_5_20_3_java_rcs: 1.5.20.3 Java RCS
  1_5_20_2_java_rcs: 1.5.20.2 Java RCS
  1_5_20_0_java_rcs: 1.5.20.0 Java RCS
  1_5_19_6_java_rcs: 1.5.19.6 Java RCS
  1_5_19_5_java_rcs: 1.5.19.5 Java RCS
  1_5_19_4_java_rcs: 1.5.19.4 Java RCS
  1_5_19_3_java_rcs: 1.5.19.3 Java RCS
  1_5_19_2_java_rcs: 1.5.19.2 Java RCS
  1_5_19_1_java_rcs: 1.5.19.1 Java RCS
  1_5_19_0_java_rcs: 1.5.19.0 Java RCS
  1_5_18_0_java_rcs: 1.5.18.0 Java RCS
  net_rcs_release_notes: .NET RCS release notes
  1_5_7_0_net_rcs: 1.5.7.0 .NET RCS
---

# ICF release notes

## Connector framework release notes

Subscribe for automatic updates: [icon: rss-square, set=fa][ICF release notes RSS Feed](./feed.xml)

|   |                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------- |
|   | Updates to the connector framework can also include security, formatting, and other internal-facing fixes. |

### 1.5.20.35 Framework

* OPENICF-3510: Prevent the Framework from attempting to dispatch requests through WebSockets in the process of completing the IDM< - >RCS handshake.

### 1.5.20.34 Framework

No public changes were made to the framework, though a new version was released.

### 1.5.20.33 Framework

* OPENICF-3349: The RCS resolves DNS names each time it establishes a new WebSocket connection.

### 1.5.20.32 Framework

No public changes were made to the framework, though a new version was released.

### 1.5.20.31 Framework

* OPENICF-2939: The default ICF operation timeout for all connector operations has changed from no timeout (`-1`) to 15 seconds. This update applies to new connector configurations generated using the `createCoreConfig` action.

### 1.5.20.30 Framework

No public changes were made to the framework, though a new version was released.

### 1.5.20.29 Framework

No public changes were made to the framework, though a new version was released.

### 1.5.20.28 Framework

No public changes were made to the framework, though a new version was released.

### 1.5.20.26 Framework

* OPENICF-2973: Resolves a race condition within the Java Framework that could result in Groovy `ClassLoader` failures at runtime.

* OPENICF-2751: You can configure global operation rate limits on a per-operation basis for any connector. Learn more in [Operation rate limits](../connector-reference/configure-connector.html#operation-rate-limits).

### 1.5.20.25 Framework

No public changes were made to the framework, though a new version was released.

### 1.5.20.24 Framework

* OPENICF-2882: The connector framework lets you define nested objects (map objects) in the provisioner `configurationProperties`.

### 1.5.20.23 Framework

No public changes were made to the framework, though a new version was released.

### 1.5.20.22 Framework

No public changes were made to the framework, though a new version was released.

### 1.5.20.21 Framework

* OPENICF-2642: Align Jetty servlet WebSocketConnectionGroup check interval with default Java RCS value.

### 1.5.20.18 Framework

No public changes were made to the framework, though a new version was released.

### 1.5.20.15 Framework

* OPENICF-2384: Java Framework: Allow \_\_PASSWORD\_\_ removal via null values.

### 1.5.20.11 Framework

No public changes were made to the framework, though a new version was released.

### 1.5.20.8 Framework

* OPENICF-1998: Local/RemoteRequest congruence checks should throw a retryable exception upon failure.

### 1.5.20.7 Framework

* OPENICF-1883: Java RCS: Improve stability of RCS WebSocket connection management.

### 1.5.20.6 Framework

* OPENIDM-17535: IDM stack releases that include bundled connectors should continue to work with existing provisioner configuration.

### 1.5.20.5 Framework

* OPENICF-1855: Investigate handling query 'poison pill' termination via recon automatic retry upon exception receipt.

### 1.5.20.4 Framework

No public changes were made to the framework, though a new version was released.

### 1.5.20.3 Framework

* OPENICF-1704: Framework: resetConnectorInfos does not implement intent.

* OPENICF-1730: Client ConnectorInfos cache not refreshed upon RCS instance restart when using RCS Agent.

* OPENICF-1735: Upgrade to groovy 3.0.9.

### 1.5.20.0 Framework

|   |                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For a list of security issues addressed in this release, refer to the related [Security Advisory](https://backstage.forgerock.com/knowledge/kb/article/a40346022) in the Knowledge Base. |

* OPENICF-1566: Framework: ICF Jetty servlet default maxMessageSize is too small.

### 1.5.19.6 Framework

No issues specific to the ICF Connector Framework were addressed in this release.

### 1.5.19.5 Framework

No issues specific to the ICF Connector Framework were addressed in this release.

### 1.5.19.4 Framework

No issues specific to the ICF Connector Framework were addressed in this release.

### 1.5.19.3 Framework

No issues specific to the ICF Connector Framework were addressed in this release.

### 1.5.19.2 Framework

No issues specific to the ICF Connector Framework were addressed in this release.

### 1.5.19.1 Framework

No issues specific to the ICF Connector Framework were addressed in this release.

### 1.5.19.0 Framework

|   |                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Starting in version 1.5.19.0, ICF connectors that previously had external library dependencies now have those dependencies bundled inside the connector. |

* OPENICF-1413: Use framework version 1.5.11.0 for ldap-connector to support Java8-compatible release.

* OPENICF-1414: Scripted Groovy (v3) based connectors fail to load with IDM releases prior to 7.0.

### 1.5.18.0 Framework

|   |                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------- |
|   | Starting in version 1.5.18.0, the ICF Connector Framework and all connectors bundled with IDM share a unified version number. |

No issues specific to the ICF Connector Framework were addressed in this release.

## Connector release notes

Subscribe for automatic updates: [icon: rss-square, set=fa][ICF release notes RSS Feed](./feed.xml)

Refer to [Connector framework release notes](framework.html) for details regarding any changes to the ICF Connector Framework that can affect connector behavior.

Downloads are available on [Backstage](https://backstage.forgerock.com/downloads/browse/idm/featured/connectors).

|   |                                                                                           |
| - | ----------------------------------------------------------------------------------------- |
|   | All updated connectors can include security, formatting, and other internal-facing fixes. |

### 1.5.20.35 Connectors

#### Updated connectors with change details

##### [MS Graph API](../connector-reference/ms-graph-api.html)

* OPENICF-2961: The connector now supports [custom user extension attributes](../connector-reference/msgraph-conf.html#msgraph-api-extension-attributes). Configure `extensionPropertySourceAppIds` to discover and expose custom extension properties registered to your Azure applications.

* OPENICF-3473: The connector now surfaces more specific error details when health checks or connector operations fail, making it easier to distinguish proxy, Microsoft Graph API, and OAuth authentication failures.

##### [Multiple CSV connector](../connector-reference/multicsv.html)

* OPENICF-3470: The connector no longer throws an `OutOfMemoryError` during initialization when CSV files contain large field values.

* OPENICF-3472: Write operations no longer load entire CSV files into heap memory for single-row modifications, reducing memory pressure in large deployments.

##### [PingOne connector](../connector-reference/pingone.html)

* OPENICF-3506: Fixed encoding for spaces and special characters in filter values.

##### [SaaS Common](../connector-reference/preface.html#saas-common)

* OPENICF-3456: The HTTP Client User-Agent is now configurable. It defaults to `PingIdentityConnector`.

* OPENICF-3459: The `jwtPem`, `jwtCert`, and `jwtKey` configuration properties are now treated as secured (GuardedString) values.

* OPENICF-3496: The connector schema is no longer overwritten on every schema request.

##### [Snowflake connector](../connector-reference/snowflake.html)

* OPENICF-3488: Fixed a null pointer exception when a transient connectivity failure occurs while querying a remote Snowflake instance.

#### Updated connectors without change details

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | Connectors without change details can include security, formatting, and other internal-facing fixes. |

* Adobe Admin Console connector ([SaaS common](#_1.5.20.35_saascommon))

* Adobe Marketing Cloud connector

* AWS IAM Identity Center connector

* Box connector ([SaaS common](#_1.5.20.35_saascommon))

* DocuSign connector ([SaaS common](#_1.5.20.35_saascommon))

* Dropbox connector ([SaaS common](#_1.5.20.35_saascommon))

* LDAP connector

* MongoDB connector

* Multiple CSV Cloud connector

* Oracle EBS connector

* RACF connector

* SaaS REST connector ([SaaS common](#_1.5.20.35_saascommon))

* SAP connector

* SCIM connector

* ServiceNow connector

* SuccessFactors connector

* Webex connector ([SaaS common](#_1.5.20.35_saascommon))

* Workday connector

### 1.5.20.34 Connectors

#### Updated connectors with change details

##### [LDAP connector](../connector-reference/ldap.html)

* OPENICF-3437: Improved LDAP server discovery for PingDS and PingDirectory.

* OPENICF-3438: The LDAP connector correctly populates LDAP modify operation context, preventing accumulation of replicated control requests.

##### [Microsoft Graph API connector](../connector-reference/ms-graph-api.html)

* OPENICF-3435: The Microsoft Graph API connector now correctly handles adding passwords to application objects.

#### Updated connectors without change details

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | Connectors without change details can include security, formatting, and other internal-facing fixes. |

* Adobe Admin Console connector

* Adobe Marketing Cloud connector

* AWS connector

* Box connector

* Cerner connector

* DocuSign connector

* Dropbox connector

* Duo connector

* Epic connector

* Google Cloud Platform connector

* HubSpot connector

* Marketo connector

* Multiple CSV Cloud connector

* Oracle EBS connector

* Peoplesoft connector

* PingOne connector

* RACF connector

* SaaS REST connector

* Salesforce connector

* SAP S/4HANA connector

* SCIM connector

* Scripted REST connector

* Snowflake connector

* SuccessFactors connector

* Webex connector

### 1.5.20.33 Connectors

#### New connectors

##### [Snowflake connector](../connector-reference/snowflake.html)

#### Updated connectors with change details

##### [Google Apps connector](../connector-reference/google.html)

* OPENICF-3302: The connector now clears the user `aliases` field through patch actions.

* OPENICF-3332: The connector now uses the Equals (`EQ`) filter on the new `parentOrgUnitPath` attribute to allow querying an `OrgUnits` object. Learn more in [Deprecated functionality](deprecated-functionality.html#_1_5_20_33) and in [Supported search filters](../connector-reference/google.html#google-apps-search-filters).

##### [LDAP connector](../connector-reference/ldap.html)

* OPENICF-3320: The connector configuration no longer includes the obsolete property `respectResourcePasswordPolicyChangeAfterReset`. Learn more in [Changed functionality](changed-functionality.html#_1-5-20-33-changed-fx).

##### [Oracle EBS connector](../connector-reference/ebs.html)

* OPENICF-3379: The connector now doesn't require the `__NAME__` attribute in `__ACCOUNT__` attribute updates. Learn more in [Changed functionality](changed-functionality.html#_1-5-20-33-changed-fx).

* OPENICF-3389: The connector now supports the delete operation on the `__ACCOUNT__` object type. Learn more in [Changed functionality](changed-functionality.html#_1-5-20-33-changed-fx).

* OPENICF-3389: The connector now includes a new boolean configuration property to enable queries to return only active accounts or all accounts. Learn more in [Changed functionality](changed-functionality.html#_1-5-20-33-changed-fx).

* OPENICF-3394: The connector now handles updates on the `__ENABLE__` attribute based on the UID of the updated user instead of in the content of the payload `__NAME__` attribute. Learn more in [Changed functionality](changed-functionality.html#_1-5-20-33-changed-fx).

##### [SaaS Common](../connector-reference/preface.html#saas-common)

* OPENICF-3371: OAuth access tokens are now renewed at a minimum of 60 seconds before their expiration.

##### [SAP SuccessFactors connector](../connector-reference/successfactors.html)

* OPENICF-3412: The SuccessFactors connector now correctly stores the schema caching mechanism in the connector configuration.

##### [SCIM connector](../connector-reference/scim.html)

* OPENICF-3360: The SCIM connector now supports finer rate-limiter granularity to control the operation execution rate. For example, you can configure the rate limiter to any positive rational number, such as `0.5/sec` or `30/min`. Learn more in [Changed functionality](changed-functionality.html).

* OPENICF-3377: The connector now supports the `filterAttributesToGet` boolean configuration property that determines if the SCIM `attributes` parameter should be included when reading resources using the SCIM endpoint. Learn more in [Changed functionality](changed-functionality.html) and in [SCIM connector configuration](../connector-reference/scim.html#scim).

##### [Workday connector](../connector-reference/workday.html)

* OPENICF-3324: Fixed the XPath transformation logic that could incorrectly alter expressions and lead to invalid results.

#### Updated connectors without change details

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | Connectors without change details can include security, formatting, and other internal-facing fixes. |

* Adobe Admin Console connector ([SaaS common](#_1.5.20.33_saascommon))

* Adobe Marketing Cloud connector

* AS400 connector

* AWS IAM Identity Center connector

* Box connector ([SaaS common](#_1.5.20.33_saascommon))

* Database table connector

* DocuSign connector([SaaS common](#_1.5.20.33_saascommon))

* Dropbox connector ([SaaS common](#_1.5.20.33_saascommon))

* Groovy connector ([Scripted Groovy](../connector-reference/preface.html#scripted-groovy))

* HubSpot connector

* Microsoft (MS) Graph API connector

* MongoDB connector ([Scripted Groovy](../connector-reference/preface.html#scripted-groovy))

* Multiple CSV Cloud connector

* Multiple CSV connector

* PingOne connector ([SaaS common](#_1.5.20.33_saascommon))

* SaaS REST connector ([SaaS common](#_1.5.20.33_saascommon))

* Salesforce connector

* SAP connector ([Scripted Groovy](../connector-reference/preface.html#scripted-groovy))

* SAP Hana DB connector

* Scripted REST connector ([Scripted Groovy](../connector-reference/preface.html#scripted-groovy))

* Scripted SQL connector ([Scripted Groovy](../connector-reference/preface.html#scripted-groovy))

* ServiceNow connector

* SSH connector ([Scripted Groovy](../connector-reference/preface.html#scripted-groovy))

* Webex connector ([SaaS common](#_1.5.20.33_saascommon))

### 1.5.20.32 Connectors

#### Updated connectors with change details

##### [Dropbox connector](../connector-reference/dropbox.html) ([SaaS common](#_1.5.20.32_saascommon))

* OPENICF-3266: The connector throws a proper error when attempting to perform an unsupported PATCH operation.

##### [LDAP connector](../connector-reference/ldap.html)

* OPENICF-3048: New `enforceADPasswordPolicyOnReset` configuration property specific for Active Directory to enable the enforcement of password policies on password resets.

  |   |                                                                                                                               |
  | - | ----------------------------------------------------------------------------------------------------------------------------- |
  |   | You can't set `enforceADPasswordPolicyOnReset` using the UI. You must edit the provisioner file directly or use the REST API. |

* OPENICF-3273: Ensure proper decoding of LDAP referral URLs.

* OPENICF-3284: Improved password policy validation error feedback for PingDS and Active Directory.

* OPENICF-3286: Fixes LDAP change log sync strategy for IBM Security Directory Server type to correctly skip changes.

* OPENICF-3287: You can't set port 0 in the connector configuration.

* OPENICF-3288: Port 3268 and 3269 (SSL) are now enforced for Active Directory Global Catalog detection.

##### [SaaS Common](../connector-reference/preface.html#saas-common)

* OPENICF-3263: JWT bearer flow no longer requires the `client_secret` to obtain an access token.

##### [SaaS REST Connector](../connector-reference/rest.html) ([SaaS common](#_1.5.20.32_saascommon))

* OPENICF-3272: Fixes an issue where `__UID__` resources that contained a space weren't properly URL-encoded when injected within the request URL.

* OPENICF-3277: Fixes a `NullPointerException` that can occur when attempting to unflatten attributes not present in the request payload.

##### [SAP HANA Database connector](../connector-reference/saphanadb.html)

* OPENICF-3241: The connector no longer uses the cascade option when dropping users.

#### Updated connectors without change details

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | Connectors without change details can include security, formatting, and other internal-facing fixes. |

* Adobe Admin Console connector ([SaaS common](#_1.5.20.32_saascommon))

* AWS IAM IC connector

* Box connector ([SaaS common](#_1.5.20.32_saascommon))

* Database table connector

* DocuSign connector ([SaaS common](#_1.5.20.32_saascommon))

* MS Graph API connector

* Multiple CSV Cloud connector

* Oracle EBS connector

* PingOne connector ([SaaS common](#_1.5.20.32_saascommon))

* ScriptedSQL connector

* Webex Connector ([SaaS common](#_1.5.20.32_saascommon))

* Workday connector

### 1.5.20.31 Connectors

#### Updated connectors with change details

##### [DocuSign connector](../connector-reference/docusign.html)

* OPENICF-3150: The connector now returns an empty query result instead of throwing an `UnknownUidException` when it cannot find a resource for queries using the UID.

##### [Multiple CSV connector](../connector-reference/multicsv.html)

* OPENICF-3270: Fixes complex queries against multiple special attributes such as `_id` and `__NAME__`.

##### [Multiple CSV Cloud connector](../connector-reference/multicsvcloud.html)

* Initial release of the [Multiple CSV Cloud connector](../connector-reference/multicsvcloud.html).

##### [SAP SuccessFactors connector](../connector-reference/successfactors.html)

* OPENICF-3139: The connector now uses a OpenSAML to generate SAML assertions locally.

##### [SaaS REST Connector](../connector-reference/rest.html)

* OPENICF-3157: Support for dynamic ICF resource filtering.

* OPENICF-3158: Support for restricting fields using `OP_ATTRIBUTES_TO_GET`.

* OPENICF-3233: Fixes invalid `__ACCOUNT__` object type definition when using the `createCoreConfig` action.

* OPENICF-3253: Fixes issue when a DELETE request requires a `requestBody`.

##### [SCIM connector](../connector-reference/scim.html)

* OPENICF-3260: The connector could incorrectly inject a `multiValuedAttributes` attribute into Create and Update payloads sent to the remote SCIM Provider.

#### Updated connectors without change details

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | Connectors without change details can include security, formatting, and other internal-facing fixes. |

* AWS IAM IC connector

* Box connector

* CSV File connector

* Kerberos connector

* MongoDB connector

* MS Graph API connector

* SAP connector

* SAP HANA DB connector

* Scripted REST connector

* Webex connector

* Workday connector

### 1.5.20.30 Connectors

#### Updated connectors with change details

##### [Database Table connector](../connector-reference/dbtable.html)

* OPENICF-2250: Connector attributes with the configuration property `changeLogColumn` can pass to the connector object.

##### [Google Apps connector](../connector-reference/google.html)

* OPENICF-3081: Use the `passwordHashAlgorithm` property to hash the connector `__PASSWORD__` attribute during transport.

* OPENICF-3088: Bug fix preventing update for `__ACCOUNT__` and `__GROUP__` secondary objects when the payload didn't include changes for the primary Google object.

##### [Kerberos connector](../connector-reference/kerberos.html)

* OPENICF-3170: The `scriptRoots` value returned by the `createCoreConfig` action was invalid.

##### [LDAP connector](../connector-reference/ldap.html)

* OPENICF-3101: The LDAP connector can read the Novell eDirectory GUID attribute.

##### [Microsoft Graph API connector](../connector-reference/ms-graph-api.html)

* OPENICF-1911: Support for the ability to use environment variables when authenticating with Azure.

##### [SaaS Common](../connector-reference/preface.html#saas-common)

* OPENICF-3097: JWT auth flow now supports PEM-formatted private keys.

##### [SaaS REST Connector](../connector-reference/rest.html)

* OPENICF-3114: Ability to send a payload in a delete request.

* OPENICF-3167: Fixes a Gson serialization issue preventing the SaaS REST connector from working with an RCS.

##### [Salesforce connector](../connector-reference/salesforce.html)

* OPENICF-3122: Adds the `initialSyncTokenOffset` configuration property. Use this property to define a period, in hours, to subtract from the current time when generating the initial Salesforce sync token. Default value is `0` hours.

##### [SCIM connector](../connector-reference/scim.html)

* OPENICF-3091: When generating the ICF Schema, the ICF ObjectClass type was incorrectly set to the SCIM Schema name instead of the ResourceType name.

##### [ServiceNow connector](../connector-reference/servicenow.html)

* OPENICF-2422: The connector supports the ServiceNow user object property `cost_center`.

#### Updated connectors without change details

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | Connectors without change details can include security, formatting, and other internal-facing fixes. |

* Box connector

* CSV connector

* Scripted REST connector

* Hubspot connector

* Webex connector

### 1.5.20.29 Connectors

#### New connectors

##### [SaaS REST Connector](../connector-reference/rest.html)

#### Updated connectors with change details

##### [Adobe Marketing Cloud connector](../connector-reference/adobe.html)

* OPENICF-2983: Connector invalidates access token on authentication failure.

* OPENICF-3044: Removed runtime configuration properties. Learn more in [Changed functionality](changed-functionality.html#_1-5-20-29-removed-props).

##### [Box connector](../connector-reference/box.html)

* OPENICF-2978: Connector invalidates access token on authentication failure.

##### [Epic connector](../connector-reference/epic.html)

* OPENICF-2982: Connector invalidates access token on authentication failure.

* OPENICF-3046: Removed runtime configuration properties. Learn more in [Changed functionality](changed-functionality.html#_1-5-20-29-removed-props).

##### [Google Cloud Platform connector](../connector-reference/gcp.html)

* OPENICF-2980: Connector invalidates access token on authentication failure.

##### [HubSpot connector](../connector-reference/hubspot.html)

* OPENICF-2979: Connector invalidates access token on authentication failure.

##### [LDAP connector](../connector-reference/ldap.html)

* OPENICF-3018: For DS 8.0 or later LDAP servers, the connector pages the change log with a search control cookie instead of filtering against change numbers. Change numbers are no longer required to set up and use the sync action.

##### [Marketo connector](../connector-reference/marketo.html)

* OPENICF-2984: Connector invalidates access token on authentication failure.

* OPENICF-3045: Removed runtime configuration properties. Learn more in [Changed functionality](changed-functionality.html#_1-5-20-29-removed-props).

##### [SaaS Common](../connector-reference/preface.html#saas-common)

* OPENICF-2967: Support for JWT authentication flow with framework 1.5.20.24 or later and RCS 1.5.20.24 or later.

* OPENICF-2985: Connector invalidates access token on authentication failure.

##### [Salesforce connector](../connector-reference/salesforce.html)

* OPENICF-2977: Connector invalidates access token on authentication failure.

##### [SAP SuccessFactors connector](../connector-reference/successfactors.html)

* OPENICF-2981: Connector invalidates access token on authentication failure.

##### [SCIM connector](../connector-reference/scim.html)

* OPENICF-2975: Connector invalidates access token on authentication failure.

##### [ServiceNow connector](../connector-reference/servicenow.html)

* OPENICF-2976: Connector invalidates access token on authentication failure.

### 1.5.20.28 Connectors

#### New connectors

* [Multiple CSV connector](../connector-reference/multicsv.html)

#### Updated connectors with change details

##### [Microsoft Graph API connector](../connector-reference/ms-graph-api.html)

* OPENICF-2910: You can now read the following [Contacts](../connector-reference/msgraph-contacts.html) attributes:

  * `directReports`

  * `memberOf`

  * `transitiveMemberOf`

  * `manager`

  |   |                                               |
  | - | --------------------------------------------- |
  |   | These attributes are not returned by default. |

* OPENICF-3005: You can now read the following [`servicePrincipal`](../connector-reference/msgraph-servicePrincipal.html) attributes:

  * `owners`

  * `memberOf`

  * `transitiveMemberOf`

  * `oauth2PermissionGrants`

  |   |                                               |
  | - | --------------------------------------------- |
  |   | These attributes are not returned by default. |

#### Updated connectors without change details

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | Connectors without change details can include security, formatting, and other internal-facing fixes. |

* AWS IAM Identity Center connector

* LDAP connector

* [SaaS Common](../connector-reference/preface.html#saas-common) connectors

* [Scripted Groovy](../connector-reference/preface.html#scripted-groovy) connectors

* Workday connector

### 1.5.20.27 Connectors

#### Updated connectors with change details

##### [Google Apps connector](../connector-reference/google.html)

* OPENICF-2996: Correctly maps License Assignment read operation parameters to Google API calls.

##### [LDAP connector](../connector-reference/ldap.html)

* OPENICF-2992: Improved support for IBM directory changelog "changes" binary attribute.

### 1.5.20.26 Connectors

#### New connectors

* [Duo connector](../connector-reference/duo.html)

#### Updated connectors with change details

##### [AWS IAM Identity Center connector](../connector-reference/aws-iam-identity-center.html)

* OPENICF-2968: Error when renewing access token.

##### [Epic connector](../connector-reference/epic.html)

* OPENICF-2941: Querying Epic accounts could fail.

##### [LDAP connector](../connector-reference/ldap.html)

* OPENICF-2931: PingDirectory is now a recognized LDAP directory.

##### [Microsoft Graph API connector](../connector-reference/ms-graph-api.html)

* OPENICF-2900: Added a user resource attribute `authenticationMethods` that is a read-only list of objects containing the authentication methods associated with a user.

* OPENICF-2901: User email authentication methods can be added/updated/deleted using a new String attribute `__emailAuthenticationMethod__` that contains the email associated with the user's authentication preference.

* OPENICF-2902: The connector can now manage phone authentication methods on a user using a new virtual multivalued String attribute `__phoneAuthenticationMethods__` that contains a definitive list of concatenated `"{phoneNumber}:{phoneType}"`.

* OPENICF-2903: Adds multivalued string attribute `__removeFido2Methods__` to the user schema. This attribute takes a list of String GUIDs to be deleted as Fido2 auth method IDs associated with a user.

* OPENICF-2912: Adds multivalued string attribute `__removeMicrosoftAuthenticatorMethods__` to the user schema. This attribute holds a list of GUIDs associated with MicrosoftAuthenticator authentication method IDs to be removed from a user.

* OPENICF-2913: Adds multivalued string attribute `__removeSoftwareOathMethods__` to the user schema. This attribute holds a list of GUIDs associated with Software Oath authentication method IDs to be removed from a user.

##### [MongoDB connector](../connector-reference/mongodb.html) ([Scripted Groovy](#_1.5.20.26_scriptedgroovy))

* OPENICF-2987: Update MongoDB driver to version 4.11.4.

##### [SAP S/4HANA connector](../connector-reference/sap-hana.html)

* OPENICF-2915: You can specify the `instanceUrl` of the SAP Hana instance in the connector configuration properties.

* OPENICF-2934: Query paging fixes.

##### [SCIM connector](../connector-reference/scim.html)

* OPENICF-2880: Reduce logging noise when a schema extension overrides a core schema attribute.

##### [Scripted Groovy](../connector-reference/preface.html#scripted-groovy)

* OPENICF-2955: The Scripted Groovy `scriptRoots` configuration property can now reference Groovy scripts embedded within the connector JAR file using the `!` prefix.

##### [Workday connector](../connector-reference/workday.html)

* OPENICF-1148: Support for updating the primary work phone number using the `primaryWorkPhone` connector attribute.

* OPENICF-2622: You can use [XPath transformations](../connector-reference/workday.html#workday-xpath-transformations) to simplify and map Workday attributes directly to read-only connector object type properties.

  |   |                                                          |
  | - | -------------------------------------------------------- |
  |   | Requires connector framework version 1.5.20.24 or later. |

* OPENICF-2891: Deprecate Workday connector schema attribute `mobile`.

#### Updated connectors without change details

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | Connectors without change details can include security, formatting, and other internal-facing fixes. |

* Adobe Admin Console connector

* Adobe Marketing Cloud connector

* AS400 connector

* AWS connector

* Box connector

* Cerner connector

* CSV connector

* Database table connector

* DocuSign connector

* Dropbox connector

* Google Apps connector

* Google Cloud Platform (GCP) connector

* HubSpot connector

* IBM RACF connector

* Kerberos connector

* Marketo connector ([Scripted Groovy](#_1.5.20.26_scriptedgroovy))

* Oracle EBS

* Peoplesoft connector

* PingOne connector

* Powershell connector toolkit

* Salesforce connector

* SAP connector ([Scripted Groovy](#_1.5.20.26_scriptedgroovy))

* SAP HANA Database connector

* SAP SuccessFactors connector

* ScriptedREST connector ([Scripted Groovy](#_1.5.20.26_scriptedgroovy))

* ScriptedSQL connector ([Scripted Groovy](#_1.5.20.26_scriptedgroovy))

* ServiceNow connector

* SSH connector ([Scripted Groovy](#_1.5.20.26_scriptedgroovy))

* Webex connector

### 1.5.20.23 Connectors

#### New connectors

* [AWS IAM Identity Center connector](../connector-reference/aws-iam-identity-center.html)

* [Box connector](../connector-reference/box.html) ([SaaS common](#_1.5.20.23_saascommon))

#### Updated connectors with change details

##### [Adobe Admin Console connector](../connector-reference/adobe-admin-console.html) ([SaaS common](#_1.5.20.23_saascommon))

* OPENICF-2792: Set the type for the `orgSpecific` and `businessAccount` schema attributes to boolean.

* OPENICF-2845: Ability to update the user's email address.

* OPENICF-2851: Updating group memberships for an Adobe account may result in excessive email notifications.

##### [Amazon Web Services (AWS) connector](../connector-reference/aws-iam.html)

* OPENICF-2755: Support for groups, roles, managed policy, inline policy, service control policy, and org unit object types.

##### [LDAP connector](../connector-reference/ldap.html)

* OPENICF-2805: SASL-EXTERNAL (mTLS) is now available with the LDAP connector.

##### [Microsoft Graph API connector](../connector-reference/ms-graph-api.html)

* OPENICF-2834: The virtual resource displaying service plans as their own object now includes the `skuPartNumber` as a readable attribute. Additionally, the display name of service plans is now a combination of the `skuPartNumber` and the `servicePlanName`.

##### [SaaS Common](../connector-reference/preface.html#saas-common)

* OPENICF-2781: During token renewal, properly cache new refresh token in the connector configuration.

##### [SAP SuccessFactors connector](../connector-reference/successfactors.html)

* OPENICF-2847: Resolve `ArrayIndexOutOfBoundsException` when consuming older connector configuration.

##### [Webex Connector](../connector-reference/webex.html) ([SaaS common](#_1.5.20.23_saascommon))

* OPENICF-2619: Properly handle HTTP 400 error responses during Webex user creation.

##### [Workday connector](../connector-reference/workday.html)

* OPENICF-2524: Paged queries with no results throw an internal server error.

#### Updated connectors without change details

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | Connectors without change details can include security, formatting, and other internal-facing fixes. |

* Adobe Marketing Cloud connector

* AS400 connector

* Cerner connector

* CSV connector

* Database table connector

* DocuSign connector ([SaaS common](#_1.5.20.23_saascommon))

* Dropbox connector ([SaaS common](#_1.5.20.23_saascommon))

* Epic connector

* Google Apps connector

* Google Cloud Platform (GCP) connector

* Groovy connector toolkit

* HubSpot connector

* IBM RACF connector

* Kerberos connector

* Marketo connector

* MongoDB connector

* Oracle EBS

* Peoplesoft connector

* PingOne connector ([SaaS common](#_1.5.20.23_saascommon))

* Powershell connector toolkit

* Salesforce connector

* SAP connector

* SAP HANA Database connector

* SAP S/4HANA connector

* SAP SuccessFactors connector

* SCIM connector

* ScriptedREST connector

* ScriptedSQL connector

* ServiceNow connector

* SSH connector

### 1.5.20.22 Connectors

#### Updated connectors with change details

##### [Adobe Admin Console connector](../connector-reference/adobe-admin-console.html)

* OPENICF-2559: Initial release of the Adobe Admin Console connector. Refer to [Adobe Admin Console connector](../connector-reference/adobe-admin-console.html) for more information.

##### [Database Table connector](../connector-reference/dbtable.html)

* OPENICF-2679: Reduce log level of many operations

##### [DocuSign connector](../connector-reference/docusign.html)

* OPENICF-2557: DocuSign connector v2

  * OPENICF-2583: Add ObjectClass UserGroups

  * OPENICF-2587: Add filter support for Users ObjectClass

  * OPENICF-2588: Add filter support for the UserGroups ObjectClass

  * OPENICF-2766: Wrong exception message when the connector is configured incorrectly

##### [IBM RACF connector](../connector-reference/racf.html)

* OPENICF-2757: Support for new object types, segments, and attributes

##### [MongoDB connector](../connector-reference/mongodb.html)

* OPENICF-2784: Update MongoDB driver to version 4.11.2

##### [Oracle EBS connector](../connector-reference/ebs.html)

* OPENICF-1760: EBS Connector v2, support responsibilities

##### [PingOne connector](../connector-reference/pingone.html)

* OPENICF-2740: Enhance user password to accept external password assignments

##### [SAP SuccessFactors connector](../connector-reference/successfactors.html)

* OPENICF-2428: Account Object: Group Name not required

* OPENICF-2528: Support schema discovery and writeback

##### [SCIM connector](../connector-reference/scim.html)

* OPENICF-1617: Ability to assign groups to users

* OPENICF-2669: The read rate limit may be exceeded during queries

* OPENICF-2672: Reconciliation after patch remove on managed user throws NPE and full updates omit remove operations

* OPENICF-2682: Using dynamic schema, multivalued attributes of schema extensions are improperly handled

* OPENICF-2710: Creating users/groups with multivalued extension attributes fails

* OPENICF-2726: Do not fail on unknown Enum values when deserializing schemas

* OPENICF-2735: The endpoint in use for a given ResourceType was incorrectly derived from the objectClass defined by the IDM provisioner configuration instead of from the endpoint specified by the ResourceTypes response from the SCIM Provider

##### [Workday connector](../connector-reference/workday.html)

* OPENICF-2524: liveSync on Workday custom fields now works

#### Updated connectors without change details

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | Connectors without change details can include security, formatting, and other internal-facing fixes. |

* Adobe Marketing Cloud connector

* AS400 connector

* AWS connector

* Cerner connector

* CSV connector

* Dropbox connector

* Epic connector

* Google Apps connector

* Google Cloud Platform (GCP) connector

* Groovy connector toolkit

* HubSpot connector

* Kerberos connector

* LDAP connector

* Marketo connector

* MS Graph API connector

* Peoplesoft connector

* Powershell connector toolkit

* Salesforce connector

* SAP connector

* SAP HANA Database connector

* SAP S/4HANA connector

* ScriptedREST connector

* ScriptedSQL connector

* ServiceNow connector

* SSH connector

* Webex connector

### 1.5.20.21 Connectors

#### Updated connectors with change details

##### [Dropbox connector](../connector-reference/dropbox.html)

* OPENICF-2664: SaaS Client Initializer should not automatically add default HTTP headers

* OPENICF-2655: Logging levels in use by generated connector class are too verbose

##### [Epic connector](../connector-reference/epic.html)

* OPENICF-2233: Add support for managing SER resources

* OPENICF-2492: EMP Enhancements

##### [Google Apps connector](../connector-reference/google.html)

* OPENICF-2617: Deprecate \_\_SECONDARY\_EMAIL\_\_ in favor of \_\_SECONDARY\_EMAILS\_\_ attribute

##### [LDAP connector](../connector-reference/ldap.html)

* OPENICF-2544: LiveSync timestamp strategy may lose changes when remote handler returns `false`

##### [PingOne connector](../connector-reference/pingone.html)

* OPENICF-2507: Initial release of the PingOne connector. Refer to [PingOne connector](../connector-reference/pingone.html) for more information.

##### [SAP connector](../connector-reference/sap.html)

* OPENICF-2410: Additional attributes in the Profile Object Type

* OPENICF-2411: Additional attributes in the Activity Groups Object Type

##### [Scripted REST connector](../connector-reference/scripted-rest.html)

* OPENICF-1917: Support for throttling

##### [Webex Connector](../connector-reference/webex.html)

* OPENICF-2047: Initial release of the Webex connector. Refer to [Webex Connector](../connector-reference/webex.html) for more information.

#### Updated connectors without change details

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | Connectors without change details can include security, formatting, and other internal-facing fixes. |

* AWS connector

* Kerberos connector

### 1.5.20.20 Connectors

#### Updated connectors with change details

##### [Database Table connector](../connector-reference/dbtable.html)

* OPENICF-2606: Schema is unnecessarily regenerated for every operation.

##### [Google Apps connector](../connector-reference/google.html)

* OPENICF-2194: PATCH remove operation doesn't update the object when both the field and value are provided.

* OPENICF-2351: Include 503 errors in the retry logic for GoogleApps connector.

* OPENICF-2490: Requests hang if the Google Admin SDK API has not been enabled within the configured Google Project.

##### [Microsoft Graph API connector](../connector-reference/ms-graph-api.html)

* OPENICF-2593: Upgrade azure-identity dependency to latest version.

##### [Salesforce connector](../connector-reference/salesforce.html)

* OPENICF-2626: A duplicate header sent by the connector prevents successful OAuth flow.

##### [SCIM connector](../connector-reference/scim.html)

* OPENICF-2575: Running liveSync for object classes other than the Account object results in an error.

* OPENICF-2601: Inject common attributes within dynamically generated schemas for all resource types.

#### Updated connectors without change details

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | Connectors without change details can include security, formatting, and other internal-facing fixes. |

* Adobe Marketing Cloud connector

* Marketo connector

* ScriptedREST connector

* ScriptedSQL connector

### 1.5.20.19 Connectors

#### Updated connectors with change details

##### [SCIM connector](../connector-reference/scim.html)

* OPENICF-1296: HTTP Status and Error Response Handling.

* OPENICF-2574: Authorization header contains an extra space which breaks client\_credentials flow.

* OPENICF-2579: TestOp should catch all exceptions thrown by the initial attempt to read the alternate ServiceProviderConfig endpoint.

#### Updated connectors without change details

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | Connectors without change details can include security, formatting, and other internal-facing fixes. |

* Microsoft Graph API connector

### 1.5.20.18 Connectors

#### Updated connectors with change details

##### [Dropbox connector](../connector-reference/dropbox.html)

* OPENICF-2354 Missing property messages.

##### [Google Apps connector](../connector-reference/google.html)

* OPENICF-2487 License assignment account attribute should be an array of strings.

##### [LDAP connector](../connector-reference/ldap.html)

* OPENICF-2296: Bad IP address for the LDAP host should be caught, and a 503 error code should be returned by IDM.

* OPENICF-2401: `queryFilter` true or false against isActive attribute returns all results.

* OPENICF-2526: Specify a negative offset (in seconds) to be applied to the timestamp token when querying for changes on the remote LDAP server using the `timestampSyncOffset` configuration property.

* OPENICF-2555: Ability to define custom octet string attributes using the `customOctetStringAttributes` configuration property.

##### [Microsoft Graph API connector](../connector-reference/ms-graph-api.html)

* OPENICF-2006: Clicking on Azure AD connector for the first time throws a 500 error.

* OPENICF-2027: Support single quotation marks in query filters.

* OPENICF-2140: Info level logging is overused for this connector.

##### [Salesforce connector](../connector-reference/salesforce.html)

* OPENICF-1527: Returns a generic ConnectorException 'Error: 400' on expired/revoked refresh\_token.

* OPENICF-2246: Implement support for Client Credentials Grant type. Refer to [Configure the Salesforce connector](../connector-reference/salesforce.html#salesforce-provisioner).

* OPENICF-2266: User schema is not cached.

* OPENICF-2505: createFullConfig NPEs when supportedObjectTypes contains FeatureLicense.

##### [SAP connector](../connector-reference/sap.html)

* OPENICF-2371: Scripts for SAP HR searching and filtering.

* OPENICF-2465: Prevent activity group assignment from being deleted when the assignment is end-dated.

* OPENICF-2480: SAP Central User Administration (CUA) support.

##### [SAP HANA Database connector](../connector-reference/saphanadb.html)

Initial release of the SAP HANA Database connector. Refer to [SAP HANA Database connector](../connector-reference/saphanadb.html) for more information.

* OPENICF-2368: SAP HANA Database connector.

##### [SCIM connector](../connector-reference/scim.html)

* OPENICF-1528: Salesforce returns a generic ConnectorException 'Error: 400' on expired/revoked refresh\_token.

* OPENICF-2472: access\_token validation checked on `issued_at` claim instead of `expires_in` for refresh\_token grant.

* OPENICF-2500: Extension attributes not flattened when converted to ConnectorObject.

* OPENICF-2504: Map JSON integer type to Java Long.

#### Updated connectors without change details

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | Connectors without change details can include security, formatting, and other internal-facing fixes. |

* Adobe Marketing Cloud connector

* AS400 connector

* AWS connector

* Box connector

* Cerner connector

* CSV connector

* Database Table connector

* DocuSign connector

* Epic connector

* GCP connector

* HubSpot connector

* IBM RACF connector

* Oracle EBS connector

* Peoplesoft connector

* SAP S/4HANA connector

* SAP SuccessFactors connector

* ScriptedREST connector

* ScriptedSQL connector

* ServiceNow connector

* Workday connector

### 1.5.20.17 Connectors

> **Collapse: Database Table Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Microsoft Graph API Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Oracle EBS connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Salesforce connector**
>
> * OPENICF-1723: Clarify usage of `proxyUri` configuration property

> **Collapse: SCIM connector**
>
> * OPENICF-900: Implement the `/Schemas` endpoint discovery
>
> * OPENICF-2297: Roles attribute should be a list of Strings, not a list of Objects
>
> * OPENICF-2482: Dynamic schema does not default to static schema on all exceptions
>
> * OPENICF-2483: Creating a user with special attributes fails with dynamically generated schema
>
> * OPENICF-2484: PUT w/schemas attribute fails for Providers that support Patch
>
> * OPENICF-2448: HTTP Client fails to handle OAuth errors
>
> * OPENICF-2453: Persist optional refresh\_token issued upon successful access\_token renewal

> **Collapse: ScriptedSQL Connector**
>
> No public changes were made specific to this connector, though a new version was released.

### 1.5.20.16 Connectors

> **Collapse: Dropbox connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: DocuSign connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Google Apps connector**
>
> * OPENICF-2356: GoogleApps Connector doesn't allow listing of licenses

> **Collapse: Groovy connector toolkit**
>
> * OPENICF-2394: Align Scripted Connector templates

> **Collapse: HubSpot connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Kerberos Apps connector**
>
> * OPENICF-2400: Kerberos Search operation logs incorrect operation type
>
> * OPENICF-2394: Align Scripted Connector templates

> **Collapse: Marketo Connector**
>
> * OPENICF-2394: Align Scripted Connector templates

> **Collapse: Microsoft Graph API connector**
>
> * OPENICF-2355: MSGraphAPI Connector doesn't support assigning `servicePlans` to an Azure user

> **Collapse: MongoDB Connector**
>
> * OPENICF-2394: Align Scripted Connector templates

> **Collapse: Salesforce connector**
>
> * OPENICF-2357: Salesforce Connector doesn't allow listing of licenses

> **Collapse: SAP connector**
>
> * OPENICF-2035: SAP Account Object Type attributes
>
> * OPENICF-2036: SAP Role Object Type Attributes
>
> * OPENICF-2037: SAP UM Profile Object Type Attributes
>
> * OPENICF-2292: Group Object Type attributes
>
> * OPENICF-2350: R3 script uses deprecated methods to parse date
>
> * OPENICF-2360: NPE getting SAP configuration
>
> * OPENICF-2377: Active Group memberships should not sync activity group name
>
> * OPENICF-2379: Should not retrieve, display, or allow manipulation of password hashing attributes
>
> * OPENICF-2386: Router should not be a required attribute
>
> * OPENICF-2388: Must throw an error upon user create/update/delete error
>
> * OPENICF-2394: Align Scripted Connector templates
>
> * OPENICF-2397: Add pagination
>
> * OPENICF-2419: Timestamp filtering support
>
> * OPENICF-2432: Default location for the ScriptRoots is incorrect
>
> * OPENICF-2435: Respect boolean response from search result handler
>
> * OPENICF-2452: Filter CODVN, CODVC, and CODVS from User LOGONDATA
>
> * OPENICF-2459: Query with `_queryFilter=true` no longer returns full user object

> **Collapse: ScriptedREST Connector**
>
> * OPENICF-2430: Search and Sync operations do not respect handler result
>
> * OPENICF-2394: Align Scripted Connector templates

> **Collapse: ScriptedSQL Connector**
>
> * OPENICF-2429: Search and Sync operations do not respect handler result
>
> * OPENICF-2394: Align Scripted Connector templates

> **Collapse: SSH Connector**
>
> * OPENICF-2394: Align Scripted Connector templates

> **Collapse: Workday connector**
>
> * OPENICF-2438: `externalFieldAndParameterCriteria` config parameter should not be set to null by default

### 1.5.20.15 Connectors

> **Collapse: Adobe Marketing Cloud connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Database Table Connector**
>
> * OPENICF-2308: Database Table Connector - Possible regression of OPENICF-903
>
> * OPENICF-1987: ORA-00933 - SQL command not properly ended error using Database Table Connector

> **Collapse: Dropbox Connector**
>
> Initial release of the Dropbox connector. Refer to [Dropbox connector](../connector-reference/dropbox.html) for more information.
>
> * OPENICF-2051: Dropbox connector

> **Collapse: Microsoft Graph API connector**
>
> * OPENICF-2306: MS Graph API Connector: Creating and updating applications with certificates fails
>
> * OPENICF-2269: MS Graph API Connector: Implement application role assignments
>
> * OPENICF-1964: MS Graph API Connector: Add the ability to handle User's Contacts object
>
> * OPENICF-2315: MS Graph API Connector: otherMails attribute should be an array of strings

> **Collapse: Salesforce connector**
>
> * OPENICF-2343: Cannot delete a list of PermissionSetAssignments

> **Collapse: SCIM connector**
>
> * OPENICF-2320: SCIM Connector: totalResults is not used when query is using paging
>
> * OPENICF-2321: SCIM Connector: pagedResultsOffset is not used properly
>
> * OPENICF-2325: SCIM Connector: HTTP error 429 should have a more explicit message
>
> * OPENICF-2323: SCIM Connector: prevent query with sorting when the Service Provider does not accept sorting
>
> * OPENICF-1916: SCIM Connector: Support for throttling

> **Collapse: ScriptedSQL Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: ServiceNow connector**
>
> No public changes were made specific to this connector, though a new version was released.

### 1.5.20.14 Connectors

> **Collapse: AS400 Connector**
>
> * OPENICF-2236 - AS400 Connector: does not expose all the AS400ConnectionPool configuration properties

> **Collapse: Google Apps connector**
>
> * OPENICF-2252: GoogleApps Connector: Unable to configure connector via UI

> **Collapse: LDAP connector**
>
> * OPENICF-2225: LDAP Connector: syncToken nativeType to be configurable / updated - mismatch with DS type stops livesync

> **Collapse: Marketo connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Microsoft Graph API connector**
>
> * OPENICF-1976: MS Graph API Connector: Ability to create guest users
>
> * OPENICF-2208: MS Graph API Connector: add the ability to read "application" and "servicePrincipal" object
>
> * OPENICF-2238: MS Graph API Connector: unable to retrieve roles
>
> * OPENICF-2247: MS Graph API Connector: Query filters on collections and filters requiring advanced query parameters cause errors
>
> * OPENICF-2248: MS Graph API Connector: Implement role assignment and role eligibility schedules
>
> * OPENICF-2251: MS Graph API Connector: \_\_ACCOUNT\_\_ data listing fails in native console for assignedLicenses
>
> * OPENICF-2257: MS Graph API Connector: Clicking Role Assignment in Data tab throws a Graph API error
>
> * OPENICF-2267: MS Graph API Connector: Proxy -→ Java.lang.ClassCastException: class okhttp3.OkHttpClient cannot be cast to class com.azure.core.http.HttpClient (okhttp3.OkHttpClient and com.azure.core.http.HttpClient are in unnamed module of loader
>
> * OPENICF-2270: MS Graph API Connector: Adding API permissions to applications fails
>
> * OPENICF-2271: MS Graph API Connector: proxy basic auth not implemented but referenced
>
> * OPENICF-2275: MS Graph API Connector: Refactor connector new object handlers and UnsupportedOperationException handling

> **Collapse: Oracle EBS connector**
>
> Initial release of the EBS connector. Refer to [Oracle EBS connector](../connector-reference/ebs.html) for more information.
>
> * OPENICF-1781: EBS Connector V1.0

> **Collapse: Peoplesoft connector**
>
> * OPENICF-2311: PeopleSoft Connector: Remove embedded `psft-2.0` and `psjoa-1.0` Jar files

> **Collapse: Salesforce connector**
>
> * OPENICF-2176 - Salesforce Connector: Support Feature License Elements as List on User Object

> **Collapse: SCIM connector**
>
> * OPENICF-1922 SCIM Connector: PATCH operation should use `path` attribute for "add" and "replace"
>
> * OPENICF-2241: SCIM Connector: Service Provider Config settings don't work for Salesforce

### 1.5.20.12 Connectors

> **Collapse: AS400 Connector**
>
> Initial release of the AS400 connector. Refer to [AS400 connector](../connector-reference/as400.html) for more information.

> **Collapse: Google Apps connector**
>
> * OPENICF-2192: NPE when updating LicenseAssignments through a user update
>
> * OPENICF-2117: Hide Alternate Emails from the schema
>
> * OPENICF-2195: Intermittent NPE when we try to read newly created user

> **Collapse: LDAP connector**
>
> * OPENICF-400: LDAP connector should be able to properly handle reading the AD tokenGroups attribute

> **Collapse: PeopleSoft connector**
>
> * OPENICF-2033: PeopleSoft Connector v2.0

> **Collapse: SAP connector**
>
> * OPENICF-2183: Exception when SAP connector is running in OpenIDM

> **Collapse: SAP SuccessFactors connector**
>
> * OPENICF-2007: SAP SuccessFactors v2

> **Collapse: SCIM connector**
>
> * OPENICF-1916: Support for throttling
>
> * OPENICF-2207: Ability to define Accept: and Content-Type: HTTP headers

> **Collapse: Workday connector**
>
> * OPENICF-2030: Connector breaks when workerID is empty when using RCS
>
> * OPENICF-2150: Ability to add field and parameter to the request criteria

### 1.5.20.11 Connectors

> **Collapse: Adobe Marketing Cloud connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: AWS connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Box connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Cerner connector**
>
> * OPENICF-1960: Cerner Connector v2

> **Collapse: CSV connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: DocuSign connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Epic connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: GCP connector**
>
> Initial release of the GCP connector. Refer to [Google Cloud Platform connector](../connector-reference/gcp.html) for more information.
>
> * OPENICF-1749: GCP Connector

> **Collapse: Google Apps connector**
>
> * OPENICF-2039: GoogleApps Connector: missing some user attributes
>
> * OPENICF-2040: GoogleApps Connector: Manage role attributes
>
> * OPENICF-2041: GoogleApps Connector: Group attributes
>
> * OPENICF-2064: Google Apps Connector: Query the Google Workspace instance for Licenses
>
> * OPENICF-2066: GoogleApps Connector: Ability to query Roles and RoleAssignments
>
> * OPENICF-2136: Google Apps Connector: Exponential Back off for reading google objects required

> **Collapse: HubSpot connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: IBM RACF connector**
>
> * OPENICF-1762: IBM RACF API Connector
>
> |   |                                                                                                                                     |
> | - | ----------------------------------------------------------------------------------------------------------------------------------- |
> |   | There was a previous RACF connector, which is deprecated. Users of the previous RACF connector should migrate to the new connector. |

> **Collapse: LDAP connector**
>
> * OPENICF-1856: LDAP Connector: Assignment of static group to IDM User fails to assign it on LDAP side if user is already a member of a Dynamic Group on LDAP side
>
> * OPENICF-2089: LDAP Connector: ldapGroups membership does not take into account nested membership of other groups
>
> * OPENICF-2108: LDAP Connector: slow group membership updates with unindexed member/uniqueMember attributes in DS
>
> * OPENICF-2126: Assignment Issue: Managed User to DS Groups Failure to Select Target Group

> **Collapse: Marketo connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Microsoft Graph API connector**
>
> * OPENICF-2068: MSGraphAPI Connector: Implement Azure AD Directory Roles support
>
> * OPENICF-2088: MSGraphAPI Connector: Implement Azure AD custom role creation

> **Collapse: PeopleSoft connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Salesforce connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: SAP S/4HANA connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: SAP SuccessFactors connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: SCIM connector**
>
> * OPENICF-2112: SCIM Connector: caseSensitive
>
> * OPENICF-2113: SCIM Connector: problem with "issuedAt" from OAuth neg
>
> * OPENICF-2114: SCIM Connector: use authenticationBasic as an option for OAuth neg
>
> * OPENICF-2125: SCIM Connector: Fix Filter

> **Collapse: Scripted REST connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: ServiceNow connector**
>
> * OPENICF-2130: ServiceNow connector query results do not match what is returned from API

> **Collapse: Workday connector**
>
> No public changes were made specific to this connector, though a new version was released.

### 1.5.20.9 Connectors

> **Collapse: LDAP Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Microsoft Graph API Connector**
>
> * OPENICF-1614: MS Graph API Connector: Livesync on user/group does not populate membership
>
> * OPENICF-1858: MS Graph API Connector: Add Group Owners management

> **Collapse: SAP Connector**
>
> * OPENICF-1675: SAP Connector: Groovy deps should be embedded
>
> * OPENICF-2071: SAP Connector: Cannot update ACTIVITY GROUPS for users

### 1.5.20.8 Connectors

> **Collapse: CSV File Connector**
>
> * OPENICF-1935: CSV Connector: generates a stacktrace for Read Only permission files
>
> * OPENICF-1969: CSV Connector: Update csv connector parsing library
>
> * OPENICF-1258: CSV Connector: stripping empty strings, replacing with nulls.

> **Collapse: DatabaseTable Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Google Apps Connector**
>
> * OPENICF-2038: Google Apps Connector: Updating user's group membership may return NPE

> **Collapse: LDAP Connector**
>
> * OPENICF-1977: LDAP Connector: Detect CA LDAP directory server

> **Collapse: Microsoft Graph API Connector**
>
> * OPENICF-1606: MS Graph API Connector: Upgrade to MS Graph Java SDK v3
>
> * OPENICF-1807: MS Graph API Connector: Better handle failure of hard delete
>
> * OPENICF-1819: MS Graph API Connector: "performHardDelete" should be set to false by default

> **Collapse: PeopleSoft Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Salesforce Connector**
>
> * OPENICF-2002: Salesforce Connector: syncFailureHandler can exceed maxRetries

> **Collapse: ScriptedSQL Connector**
>
> No public changes were made specific to this connector, though a new version was released.

### 1.5.20.7 Connectors

> **Collapse: AWS Connector**
>
> Initial release of the AWS IAM connector. Refer to [Amazon Web Services (AWS) connector](../connector-reference/aws-iam.html) for more information.
>
> * OPENICF-1780: AWS IAM Connector

> **Collapse: DatabaseTable Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Google Apps Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: LDAP Connector**
>
> * OPENICF-1897: LDAP Connector: Add support for nested AD groups

> **Collapse: MongoDB Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: PeopleSoft Connector**
>
> Initial release of the Oracle PeopleSoft connector. Refer to [PeopleSoft connector](../connector-reference/peoplesoft.html) for more information.
>
> * OPENICF-1748: PeopleSoft Connector

> **Collapse: Salesforce Connector**
>
> * OPENICF-1812: SalesForce Connector: syncFailureHandler maxRetries is not working

> **Collapse: SAP S/4HANA Connector**
>
> Initial release of the SAP S/4HANA connector. Refer to [SAP S/4HANA connector](../connector-reference/sap-hana.html) for more information.
>
> * OPENICF-1782: SAP Hana Connector

> **Collapse: ScriptedSQL Connector**
>
> No public changes were made specific to this connector, though a new version was released.

### 1.5.20.6 Connectors

> **Collapse: Cerner Connector**
>
> Initial release of the Cerner connector. Refer to [Cerner connector](../connector-reference/cerner.html) for more information.
>
> * OPENICF-1737: Cerner Connector

> **Collapse: Epic Connector**
>
> * OPENICF-1818: Epic V2 Connector
>
> * OPENICF-1878: Epic Connector: Query filter not matching uid returns HTTP 404

> **Collapse: Google Apps Connector**
>
> * OPENICF-1181: Google Apps Connector: Unable to delete custom attributes

> **Collapse: LDAP Connector**
>
> * OPENICF-1901: LDAP Connector: Reduce JVM garbage from ConnectorObjectBuilder and AttributeBuilder

> **Collapse: MongoDB Connector**
>
> * OPENICF-1833: Update MongoDB driver to the latest for compatibility with newer versions of MongoDB

### 1.5.20.5 Connectors

> **Collapse: Adobe Marketing Cloud Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Database Table Connector**
>
> * OPENICF-1711: Database Table Connector - ORA-22816 error when using Oracle trigger

> **Collapse: Epic Connector**
>
> Initial release of the Epic connector. Refer to [Epic connector](../connector-reference/epic.html) for more information.
>
> * OPENICF-1750: Epic Connector

> **Collapse: Google Apps Connector**
>
> * OPENICF-1808: Google Apps Connector: when user is provisioned using a role assignment, group isn't set correctly

> **Collapse: LDAP Connector**
>
> * OPENICF-1859: LDAP Connector: \_memberId is not returned with AD & liveSync if attribute range is used

> **Collapse: Marketo Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Salesforce Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: SCIM Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Scripted REST Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Scripted SQL Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: SAP SuccessFactors Connector**
>
> * OPENICF-1822: SuccessFactors should not require PEM formatted file on disk

### 1.5.20.4 Connectors

> **Collapse: Google Apps Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Microsoft Graph API Connector**
>
> No public changes were made specific to this connector, though a new version was released.

### 1.5.20.3 Connectors

> **Collapse: Database Table Connector**
>
> * OPENICF-1692: Database Table Connector: throwing a null pointer exception

> **Collapse: Google Apps Connector**
>
> * OPENICF-1716: Google Apps Connector: Add recoveryEmail and recoveryPhone attributes for User

> **Collapse: LDAP Connector**
>
> * OPENICF-1731: LDAP Connector: Escape characters (\\) not properly handled on delete and updates ops

> **Collapse: Scripted SQL Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: ServiceNow Connector**
>
> No public changes were made specific to this connector, though a new version was released.

> **Collapse: Workday Connector**
>
> No public changes were made specific to this connector, though a new version was released.

### 1.5.20.2 Connectors

> **Collapse: CSV File Connector**
>
> * OPENICF-1677: CSV Connector returns pagedResultsCookie for queries with \_pageSize=0.

> **Collapse: LDAP Connector**
>
> * OPENICF-1666: LDAP Connector: ldapGroups should restrict membership to the specified contexts.

> **Collapse: Microsoft Graph API Connector**
>
> * OPENICF-1656: MS Graph API Connector: Unable to update onPremisesExtensionAttributes.
>
> * OPENICF-1687: MS Graph API Connector: Should be able to work behind an HTTP Proxy.
>
> * OPENICF-1698: MS Graph API Connector: get the cause of exception if test() fails.

> **Collapse: Workday Connector**
>
> * OPENICF-1689: Workday Connector: Workers transaction logs are filtered.
>
> * OPENICF-1691: Workday Connector: Reduce Garbage collection when building connector objects.

### 1.5.20.1 Connectors

|   |                                                                                                   |
| - | ------------------------------------------------------------------------------------------------- |
|   | 1.5.20.1 is a limited release, where only the Database Table Connector was released to Backstage. |

> **Collapse: Database Table Connector**
>
> * OPENICF-1477: Database Table Connector: ORA-01000: maximum open cursors exceeded
>
> * OPENICF-1596: PSQLException: FATAL: terminating connection due to idle-in-transaction timeout

### 1.5.20.0 Connectors

> **Collapse: Generic LDAP Connector**
>
> * OPENICF-1560: LDAP Connector: RFE Disable Paged Results Control
>
> * OPENICF-1586: LDAP Connector: Timestamp sync strategy: Synchronization filters are not used properly

> **Collapse: MongoDB Connector**
>
> * OPENICF-1553: MongoDB Connector: convertBSONtoICF() does not traverse Arrays.

> **Collapse: Microsoft Graph API Connector**
>
> * OPENICF-1538: MS Graph API Connector: Sync() does not work
>
> * OPENICF-1541: MS Graph API Connector: Add ConsistencyLevel: eventual' header and $count=true for endsWith filter
>
> * OPENICF-1557: MS Graph API Connector: Handle user employeeHireDate attribute and Calendar data type
>
> * OPENICF-1558: MS Graph API Connector: Make sure sortKey is supported by the objectClass
>
> * OPENICF-1559: MS Graph API Connector: Implement Authenticate() call
>
> * OPENICF-1595: MS Graph API Connector: test() should connect to the MS Graph endpoint to validate the connectionThe following known issues will be addressed in a later release:
>
> * OPENICF-1614: MS Graph API Connector: Livesync on user/group does not populate membership
>
> * OPENICF-1615: MS Graph API Connector: Deleting Azure AD group works but throws HTTP 500

> **Collapse: SCIM Connector**
>
> * OPENICF-1589: SCIM Connector: NPE caused by exception not properly handled
>
> * OPENICF-1591: SCIM Connector: Parsing OAuth response should not fail on unknown properties
>
> * OPENICF-1598: SCIM Connector: NPE when updating attribute with null value
>
> * OPENICF-1600: SCIM Connector: unknown attributes in a query result should not throw parsing exception
>
> * OPENICF-1601: SCIM Connector: Implement a global connection timeout property

### 1.5.19.6 Connectors

No issues specific any connectors were addressed in this release.

### 1.5.19.5 Connectors

> **Collapse: CSV File Connector**
>
> * OPENICF-1530: system?\_action=createFullConfig validation does not return consistent errors

> **Collapse: Database Table Connector**
>
> * OPENICF-1510: Errors in Database Table Connector docs

> **Collapse: Groovy connector toolkit**
>
> * OPENICF-1523: ScriptedGroovy connectors fail to load in IDM 7.x when embedded Groovy version does not match IDM Groovy version

> **Collapse: Microsoft Graph API Connector**
>
> * OPENICF-1493: MS Graph API Connector: add the ability to read/assign license for the user
>
> * OPENICF-1499: MS Graph API Connector: remove the maximumConnections property
>
> * OPENICF-1507: MS Graph API Connector: add the ability to read subscribedSku object
>
> * OPENICF-1525: MS Graph API Connector: replace the default Graph SDK logger
>
> * OPENICF-1526: MS Graph API Connector: add the ability to read Team objects

> **Collapse: Salesforce Connector**
>
> * OPENICF-1522: Salesforce Connector : implement StatefulConfiguration to allow persistence of accessToken in memory

> **Collapse: SCIM Connector**
>
> * OPENICF-1518: SCIM connector: Http client ConnectionManager is not set properly

> **Collapse: Workday Connector**
>
> * OPENICF-1504: Workday Connector: SyncToken should be updated even if no events
>
> * OPENICF-1506: Workday Connector: SyncToken should be set to tenant timestamp after call to sync()
>
> * OPENICF-1508: Workday Connector: Query on SCR objects should not include date range as a search criteria

### 1.5.19.4 Connectors

No issues specific any connectors were addressed in this release.

### 1.5.19.3 Connectors

> **Collapse: Microsoft Graph API Connector**
>
> * OPENICF-1475: MS Graph API Connector: the 'manager' only returns the id and not the full object
>
> * OPENICF-1481: MS Graph API Connector: add the ability to assign/remove user's manager
>
> * OPENICF-1483: MS Graph API Connector: can't remove all groups a user belongs to

> **Collapse: Salesforce Connector**
>
> * OPENICF-1471: SalesForce Connector: should not implement PoolableConnector interface

### 1.5.19.2 Connectors

> **Collapse: Generic LDAP Connector**
>
> * OPENICF-1448: LDAP Connector: Enabling changelog livesync for oracle unified directory (OUD)
>
> * OPENICF-1466: LDAP Connector: Update filterWithOrInsteadOfAnd to apply to timestamp and Active Directory liveSync
>
> * OPENICF-1470: LDAP Connector: Null Check in ADUserAccounControl.addControl
>
> * OPENICF-1472: LDAP Connector: Data not synced from AD to IDM via livesync on \_\_ALL\_\_ object

> **Collapse: Microsoft Graph API Connector**
>
> * OPENICF-1469: MS Graph API Connector: implement a read/write rate limiter

> **Collapse: SCIM Connector**
>
> * OPENICF-1401: SCIM Connector: Align exceptions for not configured (blank/null) configurationProperties

### 1.5.19.1 Connectors

> **Collapse: Microsoft Graph API Connector**
>
> * OPENICF-1446: MS Graph API Connector: implement PoolableConnector

> **Collapse: Salesforce Connector**
>
> * OPENICF-1352: Salesforce connector: pagination and cookies not working properly

> **Collapse: SCIM Connector**
>
> * OPENICF-1444: SCIM connector - provide support for 'scope'

> **Collapse: SSH Connector**
>
> * OPENICF-1433: SSH connector: Kerberos username prompt for public key and password auth
>
> * OPENICF-1445: SSH connector: Stale or disconnected SSH sessions are not detected when borrowing from the pool

> **Collapse: Workday Connector**
>
> * OPENICF-1383: Workday Connector: Upgrade to API v35.0
>
> * OPENICF-1419: Workday Connector: Implement Service Center Representative object type
>
> * OPENICF-1426: Workday Connector: Ability to update email for Service Center Representative object
>
> * OPENICF-1432: Workday Connector: Implement OR filter
>
> * OPENICF-1447: Workday Connector: add the Contingent\_Worker\_ID as a search criteria

### 1.5.19.0 Connectors

|   |                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Starting in version 1.5.19.0, ICF connectors that previously had external library dependencies now have those dependencies bundled inside the connector. |

Initial release of the MS Graph API Connector.

> **Collapse: Generic LDAP Connector**
>
> * OPENICF-1388: LDAP Connector 1.5.5.0 throws java.lang.NoSuchMethodError on Java 8
>
> * OPENICF-1396: OPENIDM-15448 changes seemingly broke querying ldap via the data tab

> **Collapse: Groovy connector toolkit**
>
> * OPENICF-1414: Scripted Groovy (v3) based connectors fail to load with IDM releases prior to 7.0

### 1.5.18.0 Connectors

|   |                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------- |
|   | Starting in version 1.5.18.0, the ICF Connector Framework and all connectors bundled with IDM share a unified version number. |

No issues specific any connectors were addressed in this release.

## Java RCS release notes

Subscribe for automatic updates: [icon: rss-square, set=fa][ICF release notes RSS Feed](./feed.xml)

Refer to [Connector framework release notes](framework.html) for details regarding any changes to the ICF Connector Framework that can affect RCS behavior.

Downloads are available on [Backstage](https://backstage.forgerock.com/downloads/browse/idm/featured/connectors).

|   |                                                                                                 |
| - | ----------------------------------------------------------------------------------------------- |
|   | Updates to the Java RCS can also include security, formatting, and other internal-facing fixes. |

### 1.5.20.35 Java RCS

* OPENICF-3442: The RCS default truststore format has changed from JKS to PKCS12, aligning with IDM.

### 1.5.20.34 Java RCS

No public changes were made to Java RCS, though a new version was released.

### 1.5.20.33 Java RCS

* OPENICF-3349: The RCS resolves DNS names each time it establishes a new WebSocket connection.

* OPENICF-3366: The `pingpongInterval` and `groupCheckInterval` can now be set to `0`. Learn more in [RCS configuration properties](../connector-reference/configure-server.html#rcs-properties).

### 1.5.20.32 Java RCS

* OPENICF-3369: The Java RCS now supports Java 21. Learn more in [Install Java RCS](../connector-reference/java-server.html).

* OPENICF-3275: The `connectorserver.loggingConfigFile` property has been removed from `ConnectorServer.properties`. To specify a custom logback configuration file, set the `LOGGING_CONFIG` system property to the location of your `logback.xml` file.

  Learn more in [Logging configuration file](../connector-reference/icf-logs.html#icf-logging-config-file).

### 1.5.20.31 Java RCS

* OPENICF-3255: The Java RCS now sets and uses a default temp directory location within the RCS installation folder.

### 1.5.20.30 Java RCS

* OPENICF-2272: The Java RCS download now includes a sample dockerfile at `path/to/openicf/docker/Dockerfile`. Learn more in [Deploy Java RCS in a Docker container](../connector-reference/rcs-docker.html).

### 1.5.20.29 Java RCS

* OPENICF-1724: Fixed error message when uninstalling non-existent Java RCS Windows service.

### 1.5.20.28 Java RCS

* OPENICF-2153: Ability to output `CAUD_TRANSACTION_ID` in the RCS logs.

* OPENICF-2616: The default truststore is now the RCS security/trustStore previously introduced by OPENICF-2152.

* OPENICF-2970: Simplified default `ConnectorServer.properties` and added sample configurations available in `conf/samples`:

  * `ConnectorServer.properties.cloud-client`

  * `ConnectorServer.properties.default-parameters`

  * `ConnectorServer.properties.onprem-client`

  * `ConnectorServer.properties.onprem-server`

* OPENICF-2972: Removed the `/setDefaults` command.

### 1.5.20.27 Java RCS

* OPENICF-2969: The default RCS `webSocketConnections` are reduced from `3` to `2`.

### 1.5.20.26 Java RCS

* OPENICF-2942: You can launch Java RCS in a [Docker container](../connector-reference/rcs-docker.html) with multiple values (comma-separated) defined for `connectorserver.url` in `OPENICF_OPTS`.

### 1.5.20.23 Java RCS

#### Java 17 required

Running Java RCS requires Java 17.

#### More bundled connectors

Java RCS now bundles the following additional connectors:

* AS400

* Cerner

* Epic

* IBM RACF

* MongoDB

* Oracle EBS

* Peoplesoft

* SAP

* SAP HANA DB

### 1.5.20.22 Java RCS

* OPENICF-2640: If remote IDM process is stopped, Websocket connections increase until IDM process is back.

### 1.5.20.21 Java RCS

* OPENICF-2228: `logback.xml` moved to `conf/` directory.

* OPENICF-2152: Provide a default SSL truststore file.

* OPENICF-2511: Connection to IDM becomes dysfunctional after a period of inactivity in RCS.

* OPENICF-2643: Timeout waiting to acquire a websocket to send a message has been decreased from 2 minutes to 30 seconds.

* OPENICF-2644: NPE may be thrown on WebSocketConnectionGroup shutdown.

* OPENICF-2154: RCS now logs any connector exception to the log file and console.

### 1.5.20.18 Java RCS

* OPENICF-1638: The default `logback.xml` logging configuration rolls log files daily. Refer to [Rolling log policy](../connector-reference/icf-logs.html#icf-rolling-log-policy).

* OPENICF-2547: New local connector facade created --> Method: newConnectorFacadeInstance.

### 1.5.20.15 Java RCS

* OPENICF-2336: Java RCS: Change the default connector.groupCheckInterval=900 seconds to 60 seconds.

### 1.5.20.14 Java RCS

* OPENICF-1418: Java RCS: Invalid interval properties not handled properly for client mode.

* OPENICF-2181: Java RCS: Housekeeping task should log which endpoint/instance it is working with.

* OPENICF-2274: Java RCS: Response to unknown protobuf request should contain RCS version.

### 1.5.20.12 Java RCS

* OPENICF-1473: Java RCS: ConnectorServer.properties template should include config for FRAAS.

* OPENICF-1889: Java RCS: Include relevant defaults for RCS config.

### 1.5.20.11 Java RCS

* OPENICF-2132: Java RCS: docker-entrypoint.sh uses -run instead of -service to start the RCS.

* OPENICF-2137: Java RCS: When running in -service mode, version is not displayed at startup.

* OPENICF-2174: Java RCS: Incompatible with AM macaroons: Unrecognized field "expireTime".

### 1.5.20.9 Java RCS

Bundled connectors were updated, though no changes to the remote connector server were made.

### 1.5.20.8 Java RCS

* OPENICF-2000: potential log flooding resulting from operation cancel request messages for LocalOperations which have already completed.

### 1.5.20.7 Java RCS

* OPENICF-1883: Java RCS: Improve stability of RCS WebSocket connection management.

* OPENICF-1975: Java RCS: Increase default heap size from 512m to 1g.

* OPENICF-1925: Java RCS: require explicitly set property to enable agent deployment.

### 1.5.20.6 Java RCS

* OPENICF-1832: Java RCS: High CPU usage when running as a service.

### 1.5.20.5 Java RCS

* OPENICF-1855: Investigate handling query 'poison pill' termination via recon automatic retry upon exception receipt.

### 1.5.20.4 Java RCS

* OPENICF-1726: Java RCS: OAuth access token should be cached and reused till expired.

* OPENICF-1744: Java RCS: Unable to run RCS with Marketo connector using a different groovy version.

* OPENICF-1796: Java RCS: NPE if connectorserver.url has a bad hostname

### 1.5.20.3 Java RCS

* OPENICF-1725: Java RCS: classPath issue in JAVA\_DLL when running as a service on Windows.

* OPENICF-1730: Client ConnectorInfos cache not refreshed upon RCS instance restart when using RCS Agent.

* OPENICF-1743: Java RCS: windows service starts up and stops abruptly.

* OPENICF-1751: Sporadic issues managing RCS-hosted connectors through IDM Native Admin Console.

* OPENICF-1783: Java RCS: Rename the windows service name.

* OPENICF-1792: Java RCS: message hostId missing and causing a connection drop.

* OPENICF-1746: Java RCS: Should display its current version in console and jar files should have their version in file name.

* OPENICF-1764: Java RCS: on Windows, ConnectorServer.bat /setKey does not work.

* OPENICF-1774: Java RCS: upgrade Procrun to latest version for RCS as a Windows service.

### 1.5.20.2 Java RCS

* OPENICF-1655: Java RCS: When using TLS, the RCS does not work behind a proxy.

### 1.5.20.0 Java RCS

* OPENICF-1366: Java Connector Server: /setDefaults does not revert config to default properly.

* OPENICF-1502: RCS: requests not cancelled when websocket closes.

* OPENICF-1540: RCS: requests bearer token from AM, but doesn't look for error status code in response.

* OPENICF-1544: Fix double-checked locking in WebSocketConnectionGroup.

* OPENICF-1549: Update default ConnectorServer.properties.

* OPENICF-1555: Clarify locking behavior in ConnectorServer for Grizzly server lifecycle.

* OPENICF-1561: RCS: Reduce log level for common debug messages.

### 1.5.19.6 Java RCS

* OPENIDM-16178: IDM recon would fail w/ remote Java connector server.

### 1.5.19.5 Java RCS

* OPENICF-1516: Failed ICF Search Query confuses total number of search results.

* OPENICF-1520: Java RCS: Connection groups can accumulate many more websockets than they should have.

### 1.5.19.4 Java RCS

* OPENICF-1485: Java RCS: Non operational ConnectionGroup should be closed and removed.

* OPENICF-1486: Java RCS: Connection housekeeping task may stop running.

* OPENICF-1494: Java RCS: Housekeeping task gets blocked.

* OPENICF-1500: Java RCS: Improve default logging.

### 1.5.19.3 Java RCS

* OPENICF-1482: Java RCS: fails to reestablish connections to IDM after IDM is restarted.

### 1.5.19.2 Java RCS

* OPENICF-1467: RCS: endless loops on connection loss and shutdown.

### 1.5.19.1 Java RCS

No issues specific to the Remote Connector Server were addressed in this release.

### 1.5.19.0 Java RCS

* OPENICF-1393: Java Connector Server: useSSL property use should be clarified.

* OPENICF-1394: missing connectorserver.scope in connectorserver property file.

* OPENICF-1395: Investigate and clean up the following start up error message.

* OPENICF-1397: Java Connector Server: javax.net.ssl trustStore and keyStore properties should be set.

* OPENICF-1399: restarting IDM with active RCS causes RCS to decrement websocket connection count.

* OPENICF-1400: Java Connector Server: Property name usessl should match docs and code.

* OPENICF-1404: Java connector server proxy config for port is incorrect.

* OPENICF-1407: Java RCS: Incorrect url in Debug message of HttpRequestPacket header for non-SSL.

* OPENICF-1408: Java RCS: NPE when we set proxyHost for client mode.

### 1.5.18.0 Java RCS

* OPENICF-1371: Java Connector server does not always reestablish closed websockets.

* OPENICF-1390: Java RCS: Prevent use of websockets that are about to be closed.

* OPENICF-1392: Java Connector Server: TTL should be in seconds.

## .NET RCS release notes

Subscribe for automatic updates: [icon: rss-square, set=fa][ICF release notes RSS Feed](./feed.xml)

Refer to [Connector framework release notes](framework.html) for details regarding any changes to the ICF Connector Framework that can affect Remote Connector Server (RCS) behavior.

Downloads are available on [Backstage](https://backstage.forgerock.com/downloads/browse/idm/featured/connectors).

|   |                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Unless you have a specific need for the .NET version of the RCS, such as needing the [PowerShell connector toolkit](../connector-reference/powershell.html), we recommend using the [Java RCS](connector-server.html) instead. |

### 1.5.7.0 .NET RCS

* Connection improvements

  * .NET RCS should be able to initiate connection to IDM (OPENICF-731)

  * Client mode should support IDM authentication (OPENICF-1311)

  * Unable to start in client mode when no intervals used (OPENICF-1314)

  * When we attempt to stop in client mode, the connection is re-initiated (OPENICF-1315)

  * ConnectorObject should default the Name to Uid if Name is not present (OPENICF-1318)

  * Add the ability to connect to multiple IDM endpoints (OPENICF-1376)

  * Connection TTL should be in seconds (OPENICF-1626)

  * ConnectionGroup fixes for improved connection handling (OPENICF-1630)

  * Handle failure HTTP status codes when requesting OAuth 2.0 tokens (OPENICF-1631)

  * Fix handshake timing problem (OPENICF-1682)

  * Prevent use of websockets that are about to be closed (OPENICF-1685)

  * Ensure that IDM gets notification that a websocket is about to be closed (OPENICF-1700)

  * Stagger connection starts if webSocketConnections > 1 (OPENICF-1706)

  * SocketClosingSoonException introduces null values that break protobuf3 (OPENICF-2001)

  * Improve stability of RCS WebSocket connection management (OPENICF-2008)

  * If OAuth token endpoint is defined, .NET RCS still tries to use Basic Auth to connect to ID Cloud (OPENICF-2188)

  * Support for HTTP proxy authentication (OPENICF-2197)

  * Closing WebSockets are not handled properly (OPENICF-2217)

* Configuration improvements

  * Separate config properties in the ConnectorServerService.exe.Config (OPENICF-1313)

  * Make Pong interval configurable (OPENICF-1362)

  * Update default properties values (OPENICF-1628)

  * Support for hostId (OPENICF-1512)

  * Align HTTP proxy property names with Java RCS (OPENICF-2204)

* PowerShell connector now included with .NET connector server

  * Embed the PowerShell connector with the .NET connector server (OPENICF-1906)

  * Align PowerShell connector version number with the .NET RCS version (OPENICF-1962)

  * Integrate the PowerShell samples in the project (OPENICF-1970)

  * PowerShell connector: Query might return HTTP 500 when sorting by some properties (OPENICF-2205)

  * AD PowerShell samples should filter \_\_NAME\_\_ as a sort key (OPENICF-2172)

* Dependency updates and cleanup

  * Update and cleanup some dependencies. (OPENICF-1963, OPENICF-1971)

  * Upgrade protocol buffer version and package (OPENICF-1836, OPENICF-2173)

  * Upgrade .NET framework (OPENICF-1707)

  * Fix the Wix project, get rid of legacy dlls (OPENICF-1913)

  * Exception upon start due to a missing dependency (OPENICF-1951)

* General fixes and improvements

  * Sporadic issues managing RCS-hosted connectors through IDM Native Admin Console (OPENICF-2011)

  * Query filter on name attribute with pageSize and pagedResultsCookie returns HTTP 500 (OPENICF-1954)

  * PagedResultsCookie should be set to null if empty when deserialized from protobuf message (OPENICF-1679)

---

---
title: ICF release notes
description: Release notes for the connectors that are supported with PingIDM and Advanced Identity Cloud and covers changes to connectors since ICF 1.5.18.0
component: openicf
page_id: openicf:connector-release-notes:preface
canonical_url: https://docs.pingidentity.com/openicf/connector-release-notes/preface.html
page_aliases: ["index.adoc"]
---

# ICF release notes

These release notes cover the ICF releases that are supported in a deployment of PingIDM, Remote Connector Server (RCS), or PingOne Advanced Identity Cloud.

Subscribe for automatic updates: [icon: rss-square, set=fa][ICF release notes RSS Feed](./feed.xml)

Downloads are available on [Backstage](https://backstage.forgerock.com/downloads/browse/idm/featured/connectors).

**Recent updates**

| Version   | Product                                                                                                                                                                                                                                                                                                                                     | Date       |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 1.5.20.35 | * [ICF Connector Framework](framework.html#_1_5_20_35_framework)

* [Remote Connector Server](connector-server.html#_1_5_20_35_java_rcs)

* [ICF Connectors](connectors.html#_1_5_20_35_connectors)                                                                                                                                         | 2026/06/09 |
| 1.5.20.34 | - [ICF Connector Framework](framework.html#_1_5_20_34_framework)

- [Remote Connector Server](connector-server.html#_1_5_20_34_java_rcs)

- [ICF Connectors](connectors.html#_1_5_20_34_connectors)                                                                                                                                         | 2026/03/20 |
| 1.5.20.33 | * [ICF Connector Framework](framework.html#_1_5_20_33_framework)

* [Remote Connector Server](connector-server.html#_1_5_20_33_java_rcs)

* [ICF Connectors](connectors.html#_1_5_20_33_connectors)

* [Changed functionality](changed-functionality.html#_1-5-20-33-changed-fx)

* [Deprecation](deprecated-functionality.html#_1_5_20_33) | 2026/03/10 |
| 1.5.20.32 | - [ICF Connector Framework](framework.html#_1_5_20_32_framework)

- [Remote Connector Server](connector-server.html#_1_5_20_32_java_rcs)

- [ICF Connectors](connectors.html#_1_5_20_32_connectors)                                                                                                                                         | 2025/09/30 |
| 1.5.20.31 | * [ICF Connector Framework](framework.html#_1_5_20_31_framework)

* [Remote Connector Server](connector-server.html#_1_5_20_31_java_rcs)

* [ICF Connectors](connectors.html#_1_5_20_31_connectors)

* [Changed functionality](changed-functionality.html#_1-5-20-31-changed-fx)                                                            | 2025/09/02 |
| 1.5.20.30 | - [ICF Connector Framework](framework.html#_1_5_20_30_framework)

- [Remote Connector Server](connector-server.html#_1_5_20_30_java_rcs)

- [ICF Connectors](connectors.html#_1_5_20_30_connectors)

- [Deprecation](deprecated-functionality.html#_1_5_20_30)                                                                              | 2025/07/07 |
| 1.5.20.29 | * [ICF Connector Framework](framework.html#1_5_20_29)

* [Remote Connector Server](connector-server.html#1_5_20_29)

* [ICF Connectors](connectors.html#1_5_20_29)

* [Changed functionality](changed-functionality.html#1_5_20_29)                                                                                                         | 2025/04/23 |
| 1.5.20.28 | - [ICF Connector Framework](framework.html#1_5_20_28)

- [Remote Connector Server](connector-server.html#1_5_20_28)

- [ICF Connectors](connectors.html#1_5_20_28)                                                                                                                                                                          | 2025/02/27 |
| 1.5.20.27 | * [Remote Connector Server](connector-server.html#1_5_20_27)

* [ICF Connectors](connectors.html#1_5_20_27)                                                                                                                                                                                                                                 | 2025/01/09 |
| 1.5.20.26 | - [ICF Connector Framework](framework.html#1_5_20_26)

- [Remote Connector Server](connector-server.html#1_5_20_26)

- [ICF Connectors](connectors.html#1_5_20_26)                                                                                                                                                                          | 2024/12/06 |
| 1.5.20.25 | * [ICF Connector Framework](framework.html#1_5_20_25)                                                                                                                                                                                                                                                                                       | 2024/10/18 |
| 1.5.20.24 | - [ICF Connector Framework](framework.html#1_5_20_24)                                                                                                                                                                                                                                                                                       | 2024/10/02 |
| 1.5.20.23 | * [ICF Connector Framework](framework.html#1_5_20_23)

* [Remote Connector Server](connector-server.html#1_5_20_23)

* [ICF Connectors](connectors.html#1_5_20_23)

* [Changed functionality](changed-functionality.html#1_5_20_23)                                                                                                         | 2024/08/01 |
| 1.5.20.22 | - [ICF Connector Framework](framework.html#1_5_20_22)

- [Remote Connector Server](connector-server.html#1_5_20_22)

- [ICF Connectors](connectors.html#1_5_20_22)

- [Changed functionality](changed-functionality.html#1_5_20_22)                                                                                                         | 2024/06/21 |
| 1.5.20.21 | * [ICF Connector Framework](framework.html#1_5_20_21)

* [Remote Connector Server](connector-server.html#1_5_20_21)

* [ICF Connectors](connectors.html#1_5_20_21)

* [Changed functionality](changed-functionality.html#1_5_20_21)

* [Deprecation](deprecated-functionality.html#1_5_20_21)                                               | 2024/03/19 |
| 1.5.20.20 | - [ICF Connectors](connectors.html#1_5_20_20)                                                                                                                                                                                                                                                                                               | 2024/02/06 |
| 1.5.20.19 | * [ICF Connectors](connectors.html#1_5_20_19)                                                                                                                                                                                                                                                                                               | 2023/11/17 |
| 1.5.20.18 | - [ICF Connector Framework](framework.html#1_5_20_18)

- [Remote Connector Server](connector-server.html#1_5_20_18)

- [ICF Connectors](connectors.html#1_5_20_18)                                                                                                                                                                          | 2023/11/17 |
| 1.5.20.17 | * [ICF Connectors](connectors.html#1_5_20_17)                                                                                                                                                                                                                                                                                               | 2023/09/07 |
| 1.5.20.16 | - [ICF Connectors](connectors.html#1_5_20_16)                                                                                                                                                                                                                                                                                               | 2023/08/02 |
| 1.5.20.15 | * [ICF Connector Framework](framework.html#1_5_20_15)

* [Remote Connector Server](connector-server.html#1_5_20_15)

* [ICF Connectors](connectors.html#1_5_20_15)                                                                                                                                                                          | 2023/05/12 |
| 1.5.20.14 | - [Remote Connector Server](connector-server.html#1_5_20_14)

- [ICF Connectors](connectors.html#1_5_20_14)                                                                                                                                                                                                                                 | 2023/03/20 |
| 1.5.7.0   | * [.NET remote connector server](dotnet-server-release.html#1_5_7_0)                                                                                                                                                                                                                                                                        | 2023/02/02 |
| 1.5.20.12 | - [Remote Connector Server](connector-server.html#1_5_20_12)

- [ICF Connectors](connectors.html#1_5_20_12)                                                                                                                                                                                                                                 | 2022/12/09 |
| 1.5.20.11 | * [ICF Connector Framework](framework.html#1_5_20_11)

* [Remote Connector Server](connector-server.html#1_5_20_11)

* [ICF Connectors](connectors.html#1_5_20_11)                                                                                                                                                                          | 2022/11/01 |
| 1.5.20.9  | - [Remote Connector Server](connector-server.html#1_5_20_9)

- [ICF Connectors](connectors.html#1_5_20_9)                                                                                                                                                                                                                                   | 2022/09/09 |
| 1.5.20.8  | * [ICF Connector Framework](framework.html#1_5_20_8)

* [Remote Connector Server](connector-server.html#1_5_20_8)

* [ICF Connectors](connectors.html#1_5_20_8)                                                                                                                                                                             | 2022/08/08 |
| 1.5.20.7  | - [ICF Connector Framework](framework.html#1_5_20_7)

- [Remote Connector Server](connector-server.html#1_5_20_7)

- [ICF Connectors](connectors.html#1_5_20_7)                                                                                                                                                                             | 2022/06/06 |
| 1.5.20.6  | * [ICF Connector Framework](framework.html#1_5_20_6)

* [Remote Connector Server](connector-server.html#1_5_20_6)

* [ICF Connectors](connectors.html#1_5_20_6)                                                                                                                                                                             | 2022/05/05 |
| 1.5.20.5  | - [ICF Connector Framework](framework.html#1_5_20_5)

- [Remote Connector Server](connector-server.html#1_5_20_5)

- [ICF Connectors](connectors.html#1_5_20_5)                                                                                                                                                                             | 2022/02/14 |
| 1.5.20.4  | * [ICF Connector Framework](framework.html#1_5_20_4)

* [Remote Connector Server](connector-server.html#1_5_20_4)

* [ICF Connectors](connectors.html#1_5_20_4)                                                                                                                                                                             | 2021/12/08 |
| 1.5.20.3  | - [ICF Connector Framework](framework.html#1_5_20_3)

- [Remote Connector Server](connector-server.html#1_5_20_3)

- [ICF Connectors](connectors.html#1_5_20_3)                                                                                                                                                                             | 2021/11/22 |
| 1.5.20.2  | * [Remote Connector Server](connector-server.html#1_5_20_2)

* [ICF Connectors](connectors.html#1_5_20_2)                                                                                                                                                                                                                                   | 2021/07/27 |
| 1.5.20.1  | - [Database Table Connector](connectors.html#1_5_20_1)                                                                                                                                                                                                                                                                                      | 2021/05/28 |
| 1.5.20.0  | * [ICF Connector Framework](framework.html#1_5_20_0)

* [ICF Connectors](connectors.html#1_5_20_0)

* [Remote Connector Server](connector-server.html#1_5_20_0)                                                                                                                                                                             | 2021/04/16 |
| 1.5.19.6  | - [ICF Connector Framework](framework.html#1_5_19_6)

- [ICF Connectors](connectors.html#1_5_19_6)

- [Remote Connector Server](connector-server.html#1_5_19_6)                                                                                                                                                                             | 2021/02/26 |
| 1.5.19.5  | * [ICF Connector Framework](framework.html#1_5_19_5)

* [ICF Connectors](connectors.html#1_5_19_5)

* [Remote Connector Server](connector-server.html#1_5_19_5)                                                                                                                                                                             | 2021/02/12 |
| 1.5.19.4  | - [ICF Connector Framework](framework.html#1_5_19_4)

- [ICF Connectors](connectors.html#1_5_19_4)

- [Remote Connector Server](connector-server.html#1_5_19_4)                                                                                                                                                                             | 2021/01/22 |
| 1.5.19.3  | * [ICF Connector Framework](framework.html#1_5_19_3)

* [ICF Connectors](connectors.html#1_5_19_3)

* [Remote Connector Server](connector-server.html#1_5_19_3)                                                                                                                                                                             | 2020/12/13 |
| 1.5.19.2  | - [ICF Connector Framework](framework.html#1_5_19_2)

- [ICF Connectors](connectors.html#1_5_19_2)

- [Remote Connector Server](connector-server.html#1_5_19_2)                                                                                                                                                                             | 2020/11/30 |
| 1.5.19.1  | * [ICF Connector Framework](framework.html#1_5_19_1)

* [ICF Connectors](connectors.html#1_5_19_1)

* [Remote Connector Server](connector-server.html#1_5_19_1)                                                                                                                                                                             | 2020/11/18 |
| 1.5.19.0  | - [ICF Connector Framework](framework.html#1_5_19_0)

- [ICF Connectors](connectors.html#1_5_19_0)

- [Remote Connector Server](connector-server.html#1_5_19_0)                                                                                                                                                                             | 2020/10/20 |
| 1.5.18.0  | * [ICF Connector Framework](framework.html#1_5_18_0)

* [ICF Connectors](connectors.html#1_5_18_0)

* [Remote Connector Server](connector-server.html#1_5_18_0)                                                                                                                                                                             | 2020/09/14 |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | IDM supportThe releases listed in this document cover the connector releases since ICF 1.5.18.0. In most cases, these releases are backwards compatible with previous versions of IDM. Check the [IDM / ICF Compatibility Matrix](https://docs.pingidentity.com/pingidm/8/release-notes/before-you-install.html#connector-matrix) for your version of IDM for compatibility before installing a new version of a connector. |

---

---
title: Java RCS release notes
description: Release notes for the Java Remote Connector Server, covering changes, bug fixes, and improvements across all versions
component: openicf
page_id: openicf:connector-release-notes:connector-server
canonical_url: https://docs.pingidentity.com/openicf/connector-release-notes/connector-server.html
section_ids:
  1_5_20_35_java_rcs: 1.5.20.35 Java RCS
  1_5_20_34_java_rcs: 1.5.20.34 Java RCS
  1_5_20_33_java_rcs: 1.5.20.33 Java RCS
  1_5_20_32_java_rcs: 1.5.20.32 Java RCS
  1_5_20_31_java_rcs: 1.5.20.31 Java RCS
  1_5_20_30_java_rcs: 1.5.20.30 Java RCS
  1_5_20_29_java_rcs: 1.5.20.29 Java RCS
  1_5_20_28_java_rcs: 1.5.20.28 Java RCS
  1_5_20_27_java_rcs: 1.5.20.27 Java RCS
  1_5_20_26_java_rcs: 1.5.20.26 Java RCS
  1_5_20_23_java_rcs: 1.5.20.23 Java RCS
  java_17_required: Java 17 required
  more_bundled_connectors: More bundled connectors
  1_5_20_22_java_rcs: 1.5.20.22 Java RCS
  1_5_20_21_java_rcs: 1.5.20.21 Java RCS
  1_5_20_18_java_rcs: 1.5.20.18 Java RCS
  1_5_20_15_java_rcs: 1.5.20.15 Java RCS
  1_5_20_14_java_rcs: 1.5.20.14 Java RCS
  1_5_20_12_java_rcs: 1.5.20.12 Java RCS
  1_5_20_11_java_rcs: 1.5.20.11 Java RCS
  1_5_20_9_java_rcs: 1.5.20.9 Java RCS
  1_5_20_8_java_rcs: 1.5.20.8 Java RCS
  1_5_20_7_java_rcs: 1.5.20.7 Java RCS
  1_5_20_6_java_rcs: 1.5.20.6 Java RCS
  1_5_20_5_java_rcs: 1.5.20.5 Java RCS
  1_5_20_4_java_rcs: 1.5.20.4 Java RCS
  1_5_20_3_java_rcs: 1.5.20.3 Java RCS
  1_5_20_2_java_rcs: 1.5.20.2 Java RCS
  1_5_20_0_java_rcs: 1.5.20.0 Java RCS
  1_5_19_6_java_rcs: 1.5.19.6 Java RCS
  1_5_19_5_java_rcs: 1.5.19.5 Java RCS
  1_5_19_4_java_rcs: 1.5.19.4 Java RCS
  1_5_19_3_java_rcs: 1.5.19.3 Java RCS
  1_5_19_2_java_rcs: 1.5.19.2 Java RCS
  1_5_19_1_java_rcs: 1.5.19.1 Java RCS
  1_5_19_0_java_rcs: 1.5.19.0 Java RCS
  1_5_18_0_java_rcs: 1.5.18.0 Java RCS
---

# Java RCS release notes

Subscribe for automatic updates: [icon: rss-square, set=fa][ICF release notes RSS Feed](./feed.xml)

Refer to [Connector framework release notes](framework.html) for details regarding any changes to the ICF Connector Framework that can affect RCS behavior.

Downloads are available on [Backstage](https://backstage.forgerock.com/downloads/browse/idm/featured/connectors).

|   |                                                                                                 |
| - | ----------------------------------------------------------------------------------------------- |
|   | Updates to the Java RCS can also include security, formatting, and other internal-facing fixes. |

## 1.5.20.35 Java RCS

* OPENICF-3442: The RCS default truststore format has changed from JKS to PKCS12, aligning with IDM.

## 1.5.20.34 Java RCS

No public changes were made to Java RCS, though a new version was released.

## 1.5.20.33 Java RCS

* OPENICF-3349: The RCS resolves DNS names each time it establishes a new WebSocket connection.

* OPENICF-3366: The `pingpongInterval` and `groupCheckInterval` can now be set to `0`. Learn more in [RCS configuration properties](../connector-reference/configure-server.html#rcs-properties).

## 1.5.20.32 Java RCS

* OPENICF-3369: The Java RCS now supports Java 21. Learn more in [Install Java RCS](../connector-reference/java-server.html).

* OPENICF-3275: The `connectorserver.loggingConfigFile` property has been removed from `ConnectorServer.properties`. To specify a custom logback configuration file, set the `LOGGING_CONFIG` system property to the location of your `logback.xml` file.

  Learn more in [Logging configuration file](../connector-reference/icf-logs.html#icf-logging-config-file).

## 1.5.20.31 Java RCS

* OPENICF-3255: The Java RCS now sets and uses a default temp directory location within the RCS installation folder.

## 1.5.20.30 Java RCS

* OPENICF-2272: The Java RCS download now includes a sample dockerfile at `path/to/openicf/docker/Dockerfile`. Learn more in [Deploy Java RCS in a Docker container](../connector-reference/rcs-docker.html).

## 1.5.20.29 Java RCS

* OPENICF-1724: Fixed error message when uninstalling non-existent Java RCS Windows service.

## 1.5.20.28 Java RCS

* OPENICF-2153: Ability to output `CAUD_TRANSACTION_ID` in the RCS logs.

* OPENICF-2616: The default truststore is now the RCS security/trustStore previously introduced by OPENICF-2152.

* OPENICF-2970: Simplified default `ConnectorServer.properties` and added sample configurations available in `conf/samples`:

  * `ConnectorServer.properties.cloud-client`

  * `ConnectorServer.properties.default-parameters`

  * `ConnectorServer.properties.onprem-client`

  * `ConnectorServer.properties.onprem-server`

* OPENICF-2972: Removed the `/setDefaults` command.

## 1.5.20.27 Java RCS

* OPENICF-2969: The default RCS `webSocketConnections` are reduced from `3` to `2`.

## 1.5.20.26 Java RCS

* OPENICF-2942: You can launch Java RCS in a [Docker container](../connector-reference/rcs-docker.html) with multiple values (comma-separated) defined for `connectorserver.url` in `OPENICF_OPTS`.

## 1.5.20.23 Java RCS

### Java 17 required

Running Java RCS requires Java 17.

### More bundled connectors

Java RCS now bundles the following additional connectors:

* AS400

* Cerner

* Epic

* IBM RACF

* MongoDB

* Oracle EBS

* Peoplesoft

* SAP

* SAP HANA DB

## 1.5.20.22 Java RCS

* OPENICF-2640: If remote IDM process is stopped, Websocket connections increase until IDM process is back.

## 1.5.20.21 Java RCS

* OPENICF-2228: `logback.xml` moved to `conf/` directory.

* OPENICF-2152: Provide a default SSL truststore file.

* OPENICF-2511: Connection to IDM becomes dysfunctional after a period of inactivity in RCS.

* OPENICF-2643: Timeout waiting to acquire a websocket to send a message has been decreased from 2 minutes to 30 seconds.

* OPENICF-2644: NPE may be thrown on WebSocketConnectionGroup shutdown.

* OPENICF-2154: RCS now logs any connector exception to the log file and console.

## 1.5.20.18 Java RCS

* OPENICF-1638: The default `logback.xml` logging configuration rolls log files daily. Refer to [Rolling log policy](../connector-reference/icf-logs.html#icf-rolling-log-policy).

* OPENICF-2547: New local connector facade created --> Method: newConnectorFacadeInstance.

## 1.5.20.15 Java RCS

* OPENICF-2336: Java RCS: Change the default connector.groupCheckInterval=900 seconds to 60 seconds.

## 1.5.20.14 Java RCS

* OPENICF-1418: Java RCS: Invalid interval properties not handled properly for client mode.

* OPENICF-2181: Java RCS: Housekeeping task should log which endpoint/instance it is working with.

* OPENICF-2274: Java RCS: Response to unknown protobuf request should contain RCS version.

## 1.5.20.12 Java RCS

* OPENICF-1473: Java RCS: ConnectorServer.properties template should include config for FRAAS.

* OPENICF-1889: Java RCS: Include relevant defaults for RCS config.

## 1.5.20.11 Java RCS

* OPENICF-2132: Java RCS: docker-entrypoint.sh uses -run instead of -service to start the RCS.

* OPENICF-2137: Java RCS: When running in -service mode, version is not displayed at startup.

* OPENICF-2174: Java RCS: Incompatible with AM macaroons: Unrecognized field "expireTime".

## 1.5.20.9 Java RCS

Bundled connectors were updated, though no changes to the remote connector server were made.

## 1.5.20.8 Java RCS

* OPENICF-2000: potential log flooding resulting from operation cancel request messages for LocalOperations which have already completed.

## 1.5.20.7 Java RCS

* OPENICF-1883: Java RCS: Improve stability of RCS WebSocket connection management.

* OPENICF-1975: Java RCS: Increase default heap size from 512m to 1g.

* OPENICF-1925: Java RCS: require explicitly set property to enable agent deployment.

## 1.5.20.6 Java RCS

* OPENICF-1832: Java RCS: High CPU usage when running as a service.

## 1.5.20.5 Java RCS

* OPENICF-1855: Investigate handling query 'poison pill' termination via recon automatic retry upon exception receipt.

## 1.5.20.4 Java RCS

* OPENICF-1726: Java RCS: OAuth access token should be cached and reused till expired.

* OPENICF-1744: Java RCS: Unable to run RCS with Marketo connector using a different groovy version.

* OPENICF-1796: Java RCS: NPE if connectorserver.url has a bad hostname

## 1.5.20.3 Java RCS

* OPENICF-1725: Java RCS: classPath issue in JAVA\_DLL when running as a service on Windows.

* OPENICF-1730: Client ConnectorInfos cache not refreshed upon RCS instance restart when using RCS Agent.

* OPENICF-1743: Java RCS: windows service starts up and stops abruptly.

* OPENICF-1751: Sporadic issues managing RCS-hosted connectors through IDM Native Admin Console.

* OPENICF-1783: Java RCS: Rename the windows service name.

* OPENICF-1792: Java RCS: message hostId missing and causing a connection drop.

* OPENICF-1746: Java RCS: Should display its current version in console and jar files should have their version in file name.

* OPENICF-1764: Java RCS: on Windows, ConnectorServer.bat /setKey does not work.

* OPENICF-1774: Java RCS: upgrade Procrun to latest version for RCS as a Windows service.

## 1.5.20.2 Java RCS

* OPENICF-1655: Java RCS: When using TLS, the RCS does not work behind a proxy.

## 1.5.20.0 Java RCS

* OPENICF-1366: Java Connector Server: /setDefaults does not revert config to default properly.

* OPENICF-1502: RCS: requests not cancelled when websocket closes.

* OPENICF-1540: RCS: requests bearer token from AM, but doesn't look for error status code in response.

* OPENICF-1544: Fix double-checked locking in WebSocketConnectionGroup.

* OPENICF-1549: Update default ConnectorServer.properties.

* OPENICF-1555: Clarify locking behavior in ConnectorServer for Grizzly server lifecycle.

* OPENICF-1561: RCS: Reduce log level for common debug messages.

## 1.5.19.6 Java RCS

* OPENIDM-16178: IDM recon would fail w/ remote Java connector server.

## 1.5.19.5 Java RCS

* OPENICF-1516: Failed ICF Search Query confuses total number of search results.

* OPENICF-1520: Java RCS: Connection groups can accumulate many more websockets than they should have.

## 1.5.19.4 Java RCS

* OPENICF-1485: Java RCS: Non operational ConnectionGroup should be closed and removed.

* OPENICF-1486: Java RCS: Connection housekeeping task may stop running.

* OPENICF-1494: Java RCS: Housekeeping task gets blocked.

* OPENICF-1500: Java RCS: Improve default logging.

## 1.5.19.3 Java RCS

* OPENICF-1482: Java RCS: fails to reestablish connections to IDM after IDM is restarted.

## 1.5.19.2 Java RCS

* OPENICF-1467: RCS: endless loops on connection loss and shutdown.

## 1.5.19.1 Java RCS

No issues specific to the Remote Connector Server were addressed in this release.

## 1.5.19.0 Java RCS

* OPENICF-1393: Java Connector Server: useSSL property use should be clarified.

* OPENICF-1394: missing connectorserver.scope in connectorserver property file.

* OPENICF-1395: Investigate and clean up the following start up error message.

* OPENICF-1397: Java Connector Server: javax.net.ssl trustStore and keyStore properties should be set.

* OPENICF-1399: restarting IDM with active RCS causes RCS to decrement websocket connection count.

* OPENICF-1400: Java Connector Server: Property name usessl should match docs and code.

* OPENICF-1404: Java connector server proxy config for port is incorrect.

* OPENICF-1407: Java RCS: Incorrect url in Debug message of HttpRequestPacket header for non-SSL.

* OPENICF-1408: Java RCS: NPE when we set proxyHost for client mode.

## 1.5.18.0 Java RCS

* OPENICF-1371: Java Connector server does not always reestablish closed websockets.

* OPENICF-1390: Java RCS: Prevent use of websockets that are about to be closed.

* OPENICF-1392: Java Connector Server: TTL should be in seconds.

---

---
title: Known issues
description: Open known bugs across ICF connectors, including LDAP, SCIM, MS Graph API, SAP, and others, that remain unresolved at release time
component: openicf
page_id: openicf:connector-release-notes:known-issues
canonical_url: https://docs.pingidentity.com/openicf/connector-release-notes/known-issues.html
---

# Known issues

This topic lists issues that remain open at the time of release.

* OPENICF-1365: LDAP Connector: Triggered livesync using timestamps on a custom object returns HTTP 500

* OPENICF-1905: Database Table Connector: Error when using \_\_NAME\_\_ and pr operator in queryFilter

* OPENICF-2223: MSGraphAPI Connector: query filter using `pr` doesn't work

* OPENICF-2234: ScriptedSQL Connector: Throws "Unable to load FastStringService"

* OPENICF-2235: AS400 Connector: connectionTimeout setting is incorrectly applied to the maxLifetime pooled connections

* OPENICF-2258: MSGraphAPI Connector: Clicking on Directory Role Template gives oData error

* OPENICF-2265: MS Graph API Connector: Invalid filter clause when paging certain filtered results

* OPENICF-2289: SCIM Connector: Update operation fails on Salesforce using scimv2

* OPENICF-2302: LDAP Connector: createFullConfig doesn't throw a uniform error when invalid connection details provided

* OPENICF-2319: SCIM Connector: GoTo system returns non-404 code when trying to read a deleted record

* OPENICF-2349: ServiceNow Connector: query filter with complex expression including negation `!` doesn't work

* OPENICF-2369: MSGraphAPI Connector: Attributes embedded in the additionalDataManager should be exposed upon request

* OPENICF-2399: HubSpot Connector: can return wrong OWNER when single querying

* OPENICF-2403: Marketo Connector: cannot get the list of all leads when the result set is paged by the external system

* OPENICF-2416: SAP Connector: InternalServerError thrown when requesting \_pagedResultsOffset which exceeds number of available records

* OPENICF-2495: SCIM Connector: Do not log failure to retrieve AccessToken issued\_at time at SEVERE level

* OPENICF-2516: SAP Connector: Unsupported Filter operators are not rejected by the connector

* OPENICF-2518: SAP Connector: Info level logging is overused in this connector

* OPENICF-2539: Dropbox connector: improve error handling that throws java.lang.IllegalStateException

* OPENICF-2541: LDAP Connector: switching between changelog and timestamp livesync throws HTTP 500

* OPENICF-2629: SaasCommon: HTTP client default headers need to be defined per operation basis

* OPENICF-2670: SaaS Common: Admin UI allows saving bad configuration values

* OPENICF-2677: SCIM Connector: attribute duplication on PATCH caused by presence of \_\_NAME\_\_ and `userName` or `displayName` on provisioner file for V2

* OPENICF-2686: SuccessFactors Connector: default headers should not be defined at HTTP client level

* OPENICF-2763: MSGraphAPI Connector: Reconciliation on repo user fails to update target

* OPENICF-2775: SCIM Connector: Query on Salesforce displayName attribute throws an error

* OPENICF-2793: Adobe Admin Console Connector: Schema incorrectly contains both the ICF \_\_NAME\_\_ attribute and it's associated native source attribute

* OPENICF-2794: DocuSign Connector: Schema incorrectly contains both the ICF \_\_NAME\_\_ attribute and it's associated native source attribute

* OPENICF-2884: Framework: remove `Script` as valid connectorConfiguration property type

* OPENICF-2917: AWS Connector: List on Inline Policy throws an error

* OPENICF-2974: Groovy Connector: An invalid path containing multiple slash characters in the scriptRoots is not properly validated

* OPENICF-2997: SCIM Connector: Doesn't detect custom resourceType when used against scim.dev

* OPENICF-3043: GoogleApps Connector: Test operation should test connectivity to Google via supplied config

* OPENICF-3080: Box Connector: Consolidate HTTP client initializer with SaaSCommon

* OPENICF-3087: Java RCS: A runtime exception in the Main thread upon RCS startup is not being logged

* OPENICF-3089: Remove connector reference to test code on several connectors

* OPENICF-3094: Consolidate and improve configuration validation exceptions and handling

* OPENICF-3096: SCIM Connector: BeyondTrust patch remove on multivalued map throws 400 \[invalidFilter]

* OPENICF-3150: DocuSign Connector: Query filter on non-existing id returns HTTP 404

* OPENICF-3151: Duo Connector: Query filter on non-existing id returns HTTP 404

* OPENICF-3152: PingOne Connector: Query filter on non-existing id returns HTTP 404

* OPENICF-3154: Salesforce Connector: Query filter on non-existing id returns HTTP 404

* OPENICF-3164: CSV Connector: Validate newlineString property

* OPENICF-3262: SaaS REST Connector: Update operation via PATCH fails

* OPENICF-3382: Oracle EBS Connector: replace `__NAME__` attribute by USERNAME from connector schema or add as fallback