---
title: OpenICF
description: Overview of the Identity Connector Framework (ICF) for connecting external resources to Ping Identity products, with available connectors listed
component: openicf
page_id: openicf::index
canonical_url: https://docs.pingidentity.com/openicf/index.html
keywords: ["LDAP", "Connectors"]
section_ids:
  icf-available-connectors: Available connectors
---

# OpenICF

The OpenICF (ICF) is a framework for connecting external resources to the Ping Identity Platform. This allows data to synchronize between Ping Identity products and other resources like LDAP and Active Directory servers, Google Apps, or Marketo, as well as resources like CSV files and database tables. Ping Identity provides connectors for a number of common services and the ability to write your own.

## Available connectors

|   |                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Any available connector works with PingIDM, either directly or using RCS. Advanced Identity Cloud can use any available connector through RCS, while some are available directly or as an [application](https://docs.pingidentity.com/pingoneaic/latest/app-management/app-catalog.html). |

All connectors are available for download from [Backstage](https://backstage.forgerock.com/downloads/browse/idm/featured/connectors), but some connectors are included in the default deployment for Advanced Identity Cloud, IDM, and RCS. The following table identifies which connectors are included in the default deployments:

**Connectors included in default deployment**

| Connector                                                                   | IDM                      | RCS                      |
| --------------------------------------------------------------------------- | ------------------------ | ------------------------ |
| [Adobe Admin Console](connector-reference/adobe-admin-console.html)         | [icon: times, set=fa]No  | [icon: times, set=fa]No  |
| [Adobe Marketing Cloud](connector-reference/adobe.html)                     | [icon: check, set=fa]Yes | [icon: times, set=fa]No  |
| [Amazon Web Services (AWS)](connector-reference/aws-iam.html)               | [icon: times, set=fa]No  | [icon: times, set=fa]No  |
| [AWS IAM Identity Center](connector-reference/aws-iam-identity-center.html) | [icon: times, set=fa]No  | [icon: times, set=fa]No  |
| [AS400](connector-reference/as400.html)                                     | [icon: times, set=fa]No  | [icon: check, set=fa]Yes |
| [Box](connector-reference/box.html)                                         | [icon: times, set=fa]No  | [icon: times, set=fa]No  |
| [Cerner](connector-reference/cerner.html)                                   | [icon: times, set=fa]No  | [icon: check, set=fa]Yes |
| [CSV file](connector-reference/csv.html)                                    | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes |
| [Database table](connector-reference/dbtable.html)                          | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes |
| [DocuSign](connector-reference/docusign.html)                               | [icon: times, set=fa]No  | [icon: times, set=fa]No  |
| [Dropbox](connector-reference/dropbox.html)                                 | [icon: times, set=fa]No  | [icon: times, set=fa]No  |
| [Duo](connector-reference/duo.html)                                         | [icon: times, set=fa]No  | [icon: times, set=fa]No  |
| [Epic](connector-reference/epic.html)                                       | [icon: times, set=fa]No  | [icon: check, set=fa]Yes |
| [Google Apps](connector-reference/google.html)                              | [icon: check, set=fa]Yes | [icon: times, set=fa]No  |
| [Google Cloud Platform (GCP)](connector-reference/gcp.html)                 | [icon: times, set=fa]No  | [icon: times, set=fa]No  |
| [Groovy connector toolkit](connector-reference/groovy.html)                 | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes |
| [HubSpot](connector-reference/hubspot.html)                                 | [icon: times, set=fa]No  | [icon: times, set=fa]No  |
| [IBM RACF](connector-reference/racf.html)                                   | [icon: times, set=fa]No  | [icon: check, set=fa]Yes |
| [Kerberos](connector-reference/kerberos.html)                               | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes |
| [LDAP](connector-reference/ldap.html)                                       | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes |
| [Marketo](connector-reference/marketo.html)                                 | [icon: check, set=fa]Yes | [icon: times, set=fa]No  |
| [Microsoft Graph API](connector-reference/ms-graph-api.html)                | [icon: check, set=fa]Yes | [icon: times, set=fa]No  |
| [MongoDB](connector-reference/mongodb.html)                                 | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes |
| [Multiple CSV](connector-reference/multicsv.html)                           | [icon: times, set=fa]No  | [icon: times, set=fa]No  |
| [Multiple CSV Cloud](connector-reference/multicsvcloud.html)                | [icon: times, set=fa]No  | [icon: times, set=fa]No  |
| [Oracle EBS](connector-reference/ebs.html)                                  | [icon: times, set=fa]No  | [icon: check, set=fa]Yes |
| [PeopleSoft](connector-reference/peoplesoft.html)                           | [icon: times, set=fa]No  | [icon: check, set=fa]Yes |
| [PingOne](connector-reference/pingone.html)                                 | [icon: times, set=fa]No  | [icon: times, set=fa]No  |
| [PowerShell connector toolkit](connector-reference/powershell.html)         | [icon: times, set=fa]No  | [icon: times, set=fa]No  |
| [SaaS REST](connector-reference/rest.html)                                  | [icon: times, set=fa]No  | [icon: times, set=fa]No  |
| [Salesforce](connector-reference/salesforce.html)                           | [icon: check, set=fa]Yes | [icon: times, set=fa]No  |
| [SAP](connector-reference/sap.html)                                         | [icon: times, set=fa]No  | [icon: check, set=fa]Yes |
| [SAP HANA Database](connector-reference/saphanadb.html)                     | [icon: times, set=fa]No  | [icon: check, set=fa]Yes |
| [SAP S/4HANA](connector-reference/sap-hana.html)                            | [icon: times, set=fa]No  | [icon: times, set=fa]No  |
| [SAP SuccessFactors](connector-reference/successfactors.html)               | [icon: times, set=fa]No  | [icon: times, set=fa]No  |
| [SCIM](connector-reference/scim.html)                                       | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes |
| [Scripted REST](connector-reference/scripted-rest.html)                     | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes |
| [Scripted SQL](connector-reference/scripted-sql.html)                       | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes |
| [ServiceNow](connector-reference/servicenow.html)                           | [icon: check, set=fa]Yes | [icon: times, set=fa]No  |
| [Snowflake](connector-reference/snowflake.html)                             | [icon: times, set=fa]No  | [icon: times, set=fa]No  |
| [SSH](connector-reference/ssh.html)                                         | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes |
| [Webex](connector-reference/webex.html)                                     | [icon: times, set=fa]No  | [icon: times, set=fa]No  |
| [Workday](connector-reference/workday.html)                                 | [icon: times, set=fa]No  | [icon: times, set=fa]No  |

Connectors that aren't bundled can be downloaded from the [Connectors download page on Backstage](https://backstage.forgerock.com/downloads/browse/idm/featured/connectors) and installed in the `connectors/` directory of IDM or RCS. For Advanced Identity Cloud, additional connectors must be installed and run through RCS.