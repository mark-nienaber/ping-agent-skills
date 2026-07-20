---
title: December 2023
description: "Platform version: 1.18.0.0"
component: pingoneadvancedservices
page_id: pingoneadvancedservices:release_notes:p1as_rel_notes_dec2023
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/release_notes/p1as_rel_notes_dec2023.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 9, 2024
section_ids:
  delegated-admin: Delegated Admin
  prometheus: Prometheus
  pingdirectory: PingDirectory
  pingfederate: PingFederate
  parsing-improvement: Parsing improvement
  elasticsearch: ElasticSearch
  fluent-bit: Fluent Bit
  grafana: Grafana
  storage-class-provisioner-and-ebs-volume-type-changes: Storage class provisioner and EBS volume type changes
  log-file-handling: Log file handling
  kibana-1-18-only: Kibana (1.18 only)
  argo-cd: Argo CD
---

# December 2023

**Platform version: 1.18.0.0**

In this platform version:

* PingFederate deploys with version 11.3.3 instead of 11.1.8. You can find details regarding this release in the PingFederate 11.3.3 release notes.

* The PingDirectory suite of products deploys with version 9.2.0.4 instead of 9.2.0.2. You can find details regarding this release in the PingDirectory 9.2.0.4 release notes.

These applications are also included:

* PingAccess 7.0.5

* PingCentral 1.10

* Delegated Admin 4.10

## Delegated Admin

New

Administrators can now upload and download user reports.

## Prometheus

New

You can now access Prometheus metrics through a private link or VPN.

## PingDirectory

Improved

Several improvements were made to PingDirectory:

* Backend priming no longer occurs when PingDirectory is started, which decreases PingDirectory startup time.

* PingDirectory restarts have also been enhanced with increased health checking to reduce the chance of data inconsistencies within the cluster.

* Backup and restore now occurs within its own `PersistentVolume`. Learn more in [Backing up and restoring data](https://docs.pingidentity.com/pingdirectory/latest/pingdirectory_server_administration_guide/pd_ds_backup_restore_data.html) in the PingDirectory documentation.

## PingFederate

Improved

Kerberos authentication will no longer support RC4 encryption due to the use of the new 11.0.21 JDK version (which does not support this weak cipher). Any use of RC4 will need to be replaced with AES256 encryption.

## Parsing improvement

Improved

Multi-line logs generated from `server.log` (PingFederate) now appear in Kibana as a single document.

## ElasticSearch

Improved

A horizontal pod autoscaler was added and Logstash performance has improved. The number of warm nodes available has also been increased, which has improved performance and survives AZ failures.

## Fluent Bit

Improved

Now leverages IMDSv2 security instead of IMDSv1.

## Grafana

Improved

User authorization now displays in separate customer and internal teams views. Logging and alert metrics are also now available, but only to internal Ping Identity teams.

## Storage class provisioner and EBS volume type changes

Improved

The StorageClass provisioner was changed to CSI, and the EBS volume type was changed to GP3, which will improve performance and stability.

## Log file handling

Info

Our legacy logging mode (sending log files to Cloudwatch) has been removed, and log files are now sent to our internal ELK (Elasticsearch, Logstash, Kibana) stack or to a customer endpoint.

## Kibana (1.18 only)

Info

Kibana logs older than 90 days must be dropped for the migration to the new StorageClass provisioner. However, raw PROD logs from this time period are still available in S3 but can be restored to Kibana via a service request after the upgrade. When searching indexes, results contain the same fields and data, regardless of which index is chosen. For example, `pf-audit*` and`logstash*` return the same results.

## Argo CD

Info

Argo CD is now only deployed to the one per-region customer hub managing the development, staging, testing, and production environments.

---

---
title: July 2022
description: "Platform version: 1.16.1.1."
component: pingoneadvancedservices
page_id: pingoneadvancedservices:release_notes:p1as_rel_notes_july2022
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/release_notes/p1as_rel_notes_july2022.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 9, 2024
section_ids:
  use-pingcentral-to-configure-pingfederate-and-pingaccess-environments: Use PingCentral to configure PingFederate and PingAccess environments
  use-pingfederate-admin-api-to-create-password-credential-validator-and-ldap-client-manager: Use PingFederate Admin API to create password credential validator and LDAP client manager
  hot-and-warm-elasticsearch-index-tiers-added: Hot and warm Elasticsearch index tiers added
  health-check-services-added: Health check services added
  configurable-log-streaming-pipeline-added: Configurable log-streaming pipeline added
---

# July 2022

**Platform version: 1.16.1.1**.

These applications are included:

* PingAccess 7.0.5

* PingCentral 1.10

* PingDataSync 8.2.0.6

* Delegated Admin 4.10

* PingDirectory 9.0.0.2

* PingFederate 11.1

## **Use PingCentral to configure PingFederate and PingAccess environments**

New

PingCentral is now deployed with PingFederate and PingAccess environments. All of your development environments, (development, testing, staging, and production) will be configured for you and accessible from PingCentral.

## **Use PingFederate Admin API to create password credential validator and LDAP client manager**

Fixed

You can now use the PingFederate Admin API to create the PingDirectory password credential validator and the LDAP client manager instead of using static XML. If the credential validator or client manager already exists, they will not be overwritten.

## **Hot and warm Elasticsearch index tiers added**

Improved

Elasticsearch index lifecycle management (ILM) policies have been created, and a hot-warm-cold architecture has been implemented to improve performance and resiliency.

The indexer handles indexed data in a way that ages the data through several states. When the data is first indexed, it's added to a hot data tier and remains there for 90 days. Data nodes that are not actively written to are moved to a warm data tier, where they remain for 180 days. Data not accessed for more than 180 days is not indexed.

## **Health check services added**

Improved

Health check services, which provide operational status and performance data, were recently added to monitor internal APIs and clusters.

## **Configurable log-streaming pipeline added**

Improved

You can now use a variety of different security analytics services and customize the ways log data is streamed. You can filter streamed data by application, log, and keywords, and modify JSON files. Available security analytics services include:

* Customer S3 bucket

* Customer Cloudwatch ingestion

* Syslog

* IBM QRadar

---

---
title: July 2023
description: "Platform version: 1.17.1.0."
component: pingoneadvancedservices
page_id: pingoneadvancedservices:release_notes:p1as_rel_notes_july2023
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/release_notes/p1as_rel_notes_july2023.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 9, 2024
---

# July 2023

**Platform version: 1.17.1.0.**

PingFederate deploys with version 11.1.7 instead of 11.1.5. You can find details regarding this release in the PingFederate 11.1.7 release notes.

These applications are also included:

* PingAccess 7.0.5

* PingCentral 1.10

* PingDataSync 8.2.0.6

* Delegated Admin 4.10

* PingDirectory 9.2

---

---
title: March 2022
description: "Platform version: 1.16.0.1."
component: pingoneadvancedservices
page_id: pingoneadvancedservices:release_notes:p1as_rel_notes_march2022
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/release_notes/p1as_rel_notes_march2022.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 9, 2024
section_ids:
  web-application-firewall-offers-additional-protection: Web application firewall offers additional protection
  log4j-and-log4shell-security-fixes: Log4j and Log4Shell security fixes
  updated-nginx-ingress-controller: Updated NGINX ingress controller
  updated-dashboard-and-monitoring-tools: Updated dashboard and monitoring tools
  added-opentoken-adapter: Added OpenToken Adapter
---

# March 2022

**Platform version: 1.16.0.1**.

These applications are included:

* PingAccess 7.0.5

* PingCentral 1.10

* PingDataSync 8.2.0.6

* Delegated Admin 4.9

* PingFederate 11.1.10

## Web application firewall offers additional protection

Security

A Signal Sciences Web Application Firewall (WAF) was added to the platform to protect environments against vulnerabilities and mitigate DoS and DDoS attacks.

## Log4j and Log4Shell security fixes

Security

This release contains several updates that address and remediate Log4j and Log4Shell vulnerabilities.

## Updated NGINX ingress controller

Improved

The Nginx ingress controller was updated to the latest version, which provides access to the latest network security and performance functionality.

## Updated dashboard and monitoring tools

Improved

NewRelic agent, Kibana, ElasticSearch, Logstash were updated to the latest versions available.

## Added OpenToken Adapter

New

The OpenToken Adapter Kit was added to the PingFederate default profile.

---

---
title: March 2023
description: "Platform version: 1.17.0.0."
component: pingoneadvancedservices
page_id: pingoneadvancedservices:release_notes:p1as_rel_notes_march2023
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/release_notes/p1as_rel_notes_march2023.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 9, 2024
section_ids:
  dashboard-consolidation: Dashboard consolidation
  user-interface-updates: User interface updates
---

# March 2023

**Platform version: 1.17.0.0.**

PingDirectory deploys with version 9.2 instead of 9.0.0.2. You can find details regarding this release in the PingDirectory 9.2 release notes.

These applications are also included:

* PingAccess 7.0.5

* PingCentral 1.10

* PingDataSync 8.2.0.6

* Delegated Admin 4.10

* PingFederate 11.1.5

## Dashboard consolidation

Improved

The PingOne Advanced Services dashboard has been enhanced. Not only does it provide a consolidated view of key indicators, metrics, and data regarding the health of your infrastructure, but you can now access all of your environments from this location instead of using separate URLs.

## User interface updates

Improved

The PingOne Advanced Services user interface has also been updated to more closely match the look and feel of PingOne, which smooths the transition between the two.

---

---
title: March 2024
description: Platform version 1.18.2.0. Updated May 23, 2024.
component: pingoneadvancedservices
page_id: pingoneadvancedservices:release_notes:p1as_rel_notes_march2024
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/release_notes/p1as_rel_notes_march2024.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 11, 2024
---

# March 2024

**Platform version 1.18.2.0**. Updated May 23, 2024.

Product versions:

* In this platform version, PingFederate deploys with version 11.3.6 instead of 11.3.5. You can find details regarding the release in the [PingFederate 11.3.6 release notes](https://docs.pingidentity.com/pingfederate/11.3/release_notes/pf_release_notes.html#pingfederate-11-3-6-april-2024).

* In this platform version, PingAccess deploys with version 7.0.7 instead of 7.0.5. You can find details regarding this release in the [PingAccess 7.0.7 release notes](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-70.pdf).

These applications are also included:

* [PingDirectory 9.2.0.4 suite of products](https://docs.pingidentity.com/archive/#pingdirectory)

* [PingCentral 1.10](https://docs.pingidentity.com/pingcentral/1.11/release_notes/pingcentral_relnotes_home.html#pingcentral-1-10-june-2022)

**Platform version: 1.18.1.0**. Updated March 27, 2024.

In this platform version, PingFederate deploys with version 11.3.5 instead of 11.3.3. You can find details regarding this release in the [PingFederate 11.3.5 release notes](https://docs.pingidentity.com/pingfederate/11.3/release_notes/pf_release_notes.html#pingfederate-11-3-5-february-2024).

These applications are also included:

* PingDirectory 9.2.0.4 suite of products

* PingAccess 7.0.5

* PingCentral 1.10

---

---
title: May 2022
description: "Platform version: 1.16.1.0."
component: pingoneadvancedservices
page_id: pingoneadvancedservices:release_notes:p1as_rel_notes_may2022
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/release_notes/p1as_rel_notes_may2022.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 9, 2024
section_ids:
  synchronize-all-of-your-data-sources-into-one-source-of-truth: Synchronize all of your data sources into one source of truth
  pingone-ldap-gateway-connectivity: PingOne LDAP gateway connectivity
  radius-ports-are-now-configured-by-default: RADIUS ports are now configured by default
  pingfederate-thread-usage-auto-tuning-enhanced: PingFederate thread usage auto-tuning enhanced
  custom-password-policies-are-now-available-through-the-admin-portal: Custom password policies are now available through the admin portal
  jvm-metrics-are-now-available-for-pingfederate-and-pingaccess: JVM metrics are now available for PingFederate and PingAccess
---

# May 2022

**Platform version: 1.16.1.0**.

These applications are included:

* PingAccess 7.0.5

* PingCentral 1.10

* PingDataSync 8.2.0.6

* Delegated Admin 4.10

* PingDirectory 9.0.0.2

* PingFederate 11.1

## Synchronize all of your data sources into one source of truth

New

The PingDataSync Server is now available to synchronize the data from your on-premise and cloud-based data sources into PingDirectory, a high-performance, extensible LDAP directory that serves as the single source of identity truth.

## PingOne LDAP gateway connectivity

New

PingOne LDAP gateway connectivity is now supported in the PingOne Advanced Services Simple Network option, which is significantly less time-consuming to deploy than the Advanced Network option that used to be required for LDAP connectivity.

## RADIUS ports are now configured by default

Improved

Having these ports configured by default eliminates the need for our partners and professional services teams to manually configure them after deployment.

## PingFederate thread usage auto-tuning enhanced

Improved

The PingFederate server thread usage auto-tuning feature has been enhanced to improve the user experience and reduce the need for manual tuning.

## Custom password policies are now available through the admin portal

Improved

Now, not only can you request custom password policies through a service request form, but you can also request them through the admin portal.

## JVM metrics are now available for PingFederate and PingAccess

Improved

The PingFederate and PingAccess tenant dashboards now display Java Virtual Machine (JVM) metrics, which you can use to optimize system performance.

---

---
title: May 2024
description: "Platform version: 1.19.0.0. Updated May 6, 2024."
component: pingoneadvancedservices
page_id: pingoneadvancedservices:release_notes:p1as_rel_notes_may2024
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/release_notes/p1as_rel_notes_may2024.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 11, 2024
section_ids:
  elasticsearch-replaced-by-opensearch: Elasticsearch replaced by OpenSearch
  pingdirectory-improvements: PingDirectory improvements
  onepinglogin: OnePingLogin
---

# May 2024

**Platform version: 1.19.0.0.** Updated May 6, 2024.

In this platform version:

* PingAccess deploys with version 8.0.1 instead of 7.07. You can find details regarding this release in the [PingAccess 8.0.1 release notes](https://docs.pingidentity.com/pingaccess/8.0/release_notes/pa_release_notes.html#pa_801_rn).

* PingDirectory deploys with version 10.0.0.2 instead of 9.2.0.4. You can find details regarding this release in the [PingDirectory 10.0.0.2 release notes](https://docs.pingidentity.com/pingdirectory/10.0/release_notes/pd_release_notes.html#pingdirectory-suite-of-products-10-0-0-2-march-2024).

* PingCentral deploys with version 2.0.1 instead of 1.10.1. You can find details regarding this release in the [PingCentral 2.0.1 release notes](https://docs.pingidentity.com/pingcentral/2.0/release_notes/pingcentral_relnotes_home.html#pingcentral-2-0-1-january-2024).

These applications are also included:

* [PingFederate 11.3.5](https://docs.pingidentity.com/pingfederate/12.0/release_notes/pf_release_notes.html#pingfederate-11-3-5-february-2024)

* PingDataSync 10.0.0.1

* [Delegated Admin 5.0](https://docs.pingidentity.com/pingdirectory/10.0/release_notes/pd_release_notes.html#delegated-admin-5-0-december-2023)

## Elasticsearch replaced by OpenSearch

Improved

After careful consideration over several years, PingOne Advanced Services has replaced Elasticsearch with OpenSearch, an open source branch of Elasticsearch. OpenSearch provides a much larger and innovative feature set that enables a better path forward for continuing to provide log indexing, search, alerting, single sign-on (SSO), custom dashboards, and role-based access.

**Elasticsearch data will not be directly migrated into OpenSearch. Instead, only new logs will be processed during the upgrade to platform version 1.19.0.0 and will be available in your new OpenSearch dashboards**. We retain 13 months worth of raw log files, and can reprocess up to 3 months of these files into OpenSearch to allow indexed searches of limited historical data, upon request.

This change should not affect logs sent to your SIEM systems, such as Splunk. Log processing pipelines for your endpoints will remain the same, and logs sent to these endpoints will remain in a raw format for you to process.

Kibana Data Views have also been expanded. Each log generated by an app will now have its own data view, which makes it much easier to know where your logs are based on the name of the log file generated by the app. Custom dashboards will need to be exported as JSON files before the upgrade, and after the upgrade, imported into OpenSearch Dashboards and updated to reflect the changes in the new data views. The change to the data views might also require that you update the dashboard panels with the name of the new data view that previously contained the logs of interest.

## PingDirectory improvements

Improved

Several improvements were made to PingDirectory:

* You can now enable database cache sharing for deployments with multiple backend databases. You can find details in the [PingDirectory 10.0.0.0 release notes](https://docs.pingidentity.com/pingdirectory/10.0/release_notes/pd_release_notes.html#pingdirectory-suite-of-products-10-0-0-0-december-2023).

* When deployed with multiple backend databases, PingDirectory now performs better than before because preloading has been disabled.

* PingDirectory pod IPs availability and propagation to DNS have been improved for multi-region support.

* PingDirectory pods graceful shutdown has been improved and now uses an on-premise software-aligned stop-server script to terminate pods.

## OnePingLogin

Improved

The PingFederate admin console, PingAccess admin console, ArgoCD, and OpenSearch SSO has been improved to reduce the number of multi-factor authentications.

CAP permissions have also been improved to support additional fine-grained controls over user permissions. Now, users sign on using SSO to access their OpenSearch, PingFederate, or PingAccess environments. The tasks they can perform depend on the administrative roles they are assigned. By default, CAP users will not have any PingFederate or PingAccess roles assigned to them and must submit a [service request](../task_summary_table/p1as_service_requests.html) to request the appropriate roles and permissions.

|   |                                                                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This authentication experience is configured in the PingAccess and PingFederate authentication settings. Changing these settings to use a non-default token provider might delay support because it introduces additional authentication steps for Ping Identity operations resources to review. |

PingFederate and PingAccess administrator roles provide fine-grained access to features that allow them to perform specific tasks.

**PingFederate administrator roles**

* **User Admin**: Those with this role can add and remove users, change and reset passwords, and install replacement license keys.

* **Admin**: Those with this role can configure partner connections and most system settings, but they cannot manage local accounts or handle local keys and certificates.

* **Expression Admin**: Those with this role can map user attributes using Object-Graph Navigation Language (OGNL).

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Only administrators who have both the Admin role and the Expression Admin role can be granted:- The User Admin role. This restriction prevents non-Expression Admins from granting themselves the Expression Admin role.

  - Write access to the file system or directory where PingFederate is installed. This restriction prevents a non-Expression Admin user from placing a `data.zip` file containing expressions into the `<pf_install>/pingfederate/server/default/deploy` directory, which would introduce expressions into PingFederate.] |

* **Crypto Admin**: Those with this role manage local keys and certificates.

* **Auditor**: Those with this role have view-only privileges.

**PingAccess administrator roles**

* **Administrator**: Those with this role can access all features unless someone is assigned the Platform Administrator role. If that role is assigned, the Administrators can't update authorization, user, or environment settings, but can access everything else.

* **Platform Administrator**: Those with this role can access everything that an Administrator can access, but they can also update authorization, user, and environment settings and configurations. Use this role in conjunction with the Administrator role to prevent accidental lockouts.

* **Auditor**: Those with this role have view-only privileges.

---

---
title: November 2022
description: "Platform version: 1.16.5.0."
component: pingoneadvancedservices
page_id: pingoneadvancedservices:release_notes:p1as_rel_notes_nov2022
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/release_notes/p1as_rel_notes_nov2022.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 9, 2024
section_ids:
  provision-and-deprovision-users-for-saas-applications: Provision and deprovision users for SaaS applications
  performance-metrics: Performance metrics
  pingfederate-patches-now-automatically-updated: PingFederate patches now automatically updated
---

# November 2022

**Platform version: 1.16.5.0**.

These applications are included:

* PingAccess 7.0.5

* PingCentral 1.10

* PingDataSync 8.2.0.6

* Delegated Admin 4.10

* PingDirectory 9.0.0.2

* PingFederate 11.1.5

## **Provision and deprovision users for SaaS applications**

New

Using PingOne Advanced Services, PingFederate administrators can now provision and deprovision users to the following software as a service (SaaS) applications:

* Slack

* Udemy

* Zscaler

* SCIM

* PingOne MFA

|   |                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In a multi-region deployment, SaaS provisioning is deployed to a single region, which is your primary region, and will not be deployed to your secondary region. |

## Performance metrics

Improved

You can now access up to 13 months of performance data that will help you better understand the activities occurring within your PingOne Advanced Services environments.

## **PingFederate patches now automatically updated**

Improved

PingFederate patch versions are now automatically updated in PingOne Advanced Services.

---

---
title: November 2024
description: "Platform version: 1.19.2.0. Updated November 21, 2024."
component: pingoneadvancedservices
page_id: pingoneadvancedservices:release_notes:p1as_rel_notes_nov2024
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/release_notes/p1as_rel_notes_nov2024.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 11, 2024
section_ids:
  indexed-log-file-retention-policy-change: Indexed log file retention policy change
---

# November 2024

**Platform version: 1.19.2.0**. Updated November 21, 2024.

In this platform version:

* PingAccess deploys with version 8.0.4 instead of 8.0.3. You can find details regarding this release in the [PingAccess 8.0.4 release notes](https://docs.pingidentity.com/pingaccess/8.0/release_notes/pa_release_notes.html#pa_804_rn).

* PingCentral deploys with version 2.0.2 instead of 2.0.1. You can find details regarding this release in the [PingCentral 2.0.2 release notes](https://docs.pingidentity.com/pingcentral/latest/release_notes/pingcentral_relnotes_home.html#pingcentral-2-0-2-april-2024).

These applications are also included:

* [PingFederate 11.3.8](https://docs.pingidentity.com/pingfederate/11.3/release_notes/pf_release_notes.html#pingfederate-11-3-8-july-2024)

* [PingDirectory 10.0.0.2](https://docs.pingidentity.com/pingdirectory/latest/release_notes/pd_release_notes.html#pingdirectory-suite-of-products-10-0-0-2-march-2024)

* [PingDataSync 10.0.0.2](https://docs.pingidentity.com/pingdirectory/latest/release_notes/pd_release_notes.html#pingdirectory-suite-of-products-10-0-0-2-march-2024)

* [Delegated Admin 5.0.0](https://docs.pingidentity.com/pingdirectory/10.0/release_notes/pd_release_notes.html#delegated-admin-5-0-december-2023)

## Indexed log file retention policy change

Info

With the release of platform version 1.19.0.0, we announced that we've replaced Elasticsearch with OpenSearch because OpenSearch provides a larger and more innovative feature set. As part of the 1.19.2.0 log adjustments, we will now have indexed logs available for a rolling 30-day window. This change will be rolled out to all platform versions of P1AS starting on Feb 1st. Log files older than 30 days will be unavailable and will remain in our internal archive.

Many of you have your own Security Information and Event Management (SIEM) systems and your own ways of storing, indexing, and searching your log files, so you won't be affected by this change. The same is true if you receive a copy of your logs through a customer endpoint. Your log files can remain on your endpoint systems for the amount of time specified in your retention policies.

Otherwise, this change in policy means that:

* If you're upgrading to version 1.19.2.0, your Elasticsearch data will not be directly migrated into OpenSearch. Instead, only new logs will be processed after the upgrade and be available in your new OpenSearch dashboard when the upgrade is complete.

* If you're using platform version 1.19.0.0, this change will occur on February 1, 2025. On that day, you'll notice that your Kibana or OpenSearch dashboards will only display indexed log files for a rolling 30-day window.

If you want to have indexed log files for more than 30 days, we recommend that you add your own customer-managed endpoint, or use your own SIEM system to store and manage your log files.

To have your logs sent to a SIEM system or other customer endpoint, submit a service request through the [Support Portal](https://support.pingidentity.com/s/). Learn more about submitting this type of request in [Platform service requests > SIEM integration.](../task_summary_table/p1as_platform_siem_integration.html)

---

---
title: October 2023
description: "Platform version: 1.17.3.0."
component: pingoneadvancedservices
page_id: pingoneadvancedservices:release_notes:p1as_rel_notes_oct2023
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/release_notes/p1as_rel_notes_oct2023.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 9, 2024
---

# October 2023

**Platform version: 1.17.3.0.**

The PingDirectory suite of products deploys with version 9.2.0.2 instead of 9.2. You can find details regarding this release in the PingDirectory 9.2.0.2 release notes.

These applications are also included:

* PingAccess 7.0.5

* PingCentral 1.10

* Delegated Admin 4.10

* PingFederate 11.1.8

---

---
title: PingOne Advanced Services Release Notes
description: Review release notes for PingOne Advanced Services.
component: pingoneadvancedservices
page_id: pingoneadvancedservices:release_notes:p1as_rel_notes
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/release_notes/p1as_rel_notes.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 16, 2025
section_ids:
  platform-version-2-2-0-march-2026: Platform version 2.2.0 (March 2026)
  pingfederate-2-2-2-june-2026: PingFederate 2.2.2 (June 2026)
  pingaccess-2-2-1-june-2026: PingAccess 2.2.1 (June 2026)
  pingfederate-2-2-1-april-2026: PingFederate 2.2.1 (April 2026)
  pingdirectory-2-2-1-april-2026: PingDirectory 2.2.1 (April 2026)
  enhancements: Enhancements
  support-policy-now-available: Support policy now available
  create-and-update-virtual-hosts-using-the-admin-console: Create and update virtual hosts using the admin console
  ip-allow-list-service-request-form-now-available: IP allow list service request form now available
  pingdirectory-restart-process-improved: PingDirectory restart process improved
  platform-version-2-1-5-june-2026: Platform version 2.1.5 (June 2026)
  enhancements-2: Enhancements
  pingdirectory-restart-process-improved-2: PingDirectory restart process improved
  platform-version-2-1-1-september-2025: Platform version 2.1.1 (September 2025)
  pingfederate-2-1-5-june-2026: PingFederate 2.1.5 (June 2026)
  pingaccess-2-1-5-june-2026: PingAccess 2.1.5 (June 2026)
  pingaccess-2-1-4-april-2026: PingAccess 2.1.4 (April 2026)
  pingaccess-2-1-3-march-2026: PingAccess 2.1.3 (March 2026)
  pingfederate-2-1-4-march-2026: PingFederate 2.1.4 (March 2026)
  pingfederate-2-1-3-january-2026: PingFederate 2.1.3 (January 2026)
  pingfederate-2-1-2-october-2025: PingFederate 2.1.2 (October 2025)
  enhancements-3: Enhancements
  use-oauth-to-access-the-pingfederate-admin-api: Use OAuth to access the PingFederate Admin API
  platform-version-2-1-0-may-2025: Platform version 2.1.0 (May 2025)
  enhancements-4: Enhancements
  use-oauth-to-access-the-pingaccess-admin-api: Use OAuth to access the PingAccess Admin API
  ldaps-custom-domains-now-supported: LDAPS custom domains now supported
  automated-certificates-for-global-dns-domains-now-available: Automated certificates for global DNS domains now available
  logging-improvements: Logging improvements
  platform-version-2-0-1-april-2025: Platform version 2.0.1 (April 2025)
  pingfederate-2-0-2-november-2025: PingFederate 2.0.2 (November 2025)
  pingdirectory-2-0-3-march-2026: PingDirectory 2.0.3 (March 2026)
  platform-version-2-0-0-december-2024: Platform version 2.0.0 (December 2024)
  enhancements-5: Enhancements
  self-service-api-beta-now-available: Self-service API Beta now available
---

# PingOne Advanced Services Release Notes

Review release notes for PingOne Advanced Services.

Subscribe to get automatic updates: [icon: rss-square, set=fa][PingOne Advanced Services release notes RSS feed](p1as_rel_notes.xml)

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * PingOne Advanced Services platform version 2.1 is the final version that supports basic authentication for the PingFederate and PingAccess Admin APIs. After platform version 2.4 releases, 2.1 will move into extended support and six months later will reach its End of Life (EOL) status, as outlined in our [Support policy](../p1as_support_policy.html). Exceptions to this policy will be granted on a case-by-case basis.

* In the upcoming version of PingOne Advanced Services, platform version 2.4, PingOne Advanced Services will start using formatted JSON to improve the logging output, which might require adjustments to custom parsing logic in your SIEM. A sample of logs in the new format is [available to download](../_attachments/JSON-logging-samples.zip). |

## Platform version 2.2.0 (March 2026)

> **Collapse: This platform version deploys with these microservices and applications:**
>
> * PingAccess 2.2.0
>
>   * [PingAccess 9.0.0](https://docs.pingidentity.com/pingaccess/9.0/release_notes/pa_release_notes.html#pa-90)
>
> * PingCentral 2.2.0
>
>   * [PingCentral 2.2.0](https://docs.pingidentity.com/pingcentral/3.0/release_notes/pingcentral_relnotes_home.html#pingcentral-2-2-december-2024)
>
> * PingDirectory 2.2.0
>
>   * [PingDirectory suite of products 10.3.0.1](https://docs.pingidentity.com/pingdirectory/10.3/release_notes/pd_release_notes.html#rn10301)
>
>     * PingDataSync 10.3.0.0
>
>     * Delegated Admin 5.0.0
>
>       |   |                                                                                                                                                                  |
>       | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>       |   | PingDirectory was upgraded from Java 11 to Java 17 in this release, so compatibility testing and validation should be done before integrating with your systems. |
>
> * PingFederate 2.2.0
>
>   * [PingFederate 12.2.6](https://docs.pingidentity.com/pingfederate/12.2/release_notes/pf_release_notes.html#pingfederate-12-2-6-november-2025)

We've also updated these microservices and applications, which are available for platform version 2.2.0:

### PingFederate 2.2.2 (June 2026)

* [PingFederate 12.3.6](https://docs.pingidentity.com/pingfederate/12.3/release_notes/pf_release_notes.html#pingfederate-12-3-6-april-2026)

### PingAccess 2.2.1 (June 2026)

* [PingAccess 9.0.3](https://docs.pingidentity.com/pingaccess/9.0/release_notes/pa_release_notes.html#pa-903)

### PingFederate 2.2.1 (April 2026)

* [PingFederate 12.3.5](https://docs.pingidentity.com/pingfederate/13.0/release_notes/pf_release_notes.html#pingfederate-12-3-5-february-2026)

* New Update PingFederate templates using the admin console or the administrative API. Learn more in [Accessing the PingOne Advanced Services admin console and administrative API](../task_summary_table/p1as_platform_admin_api.html).

### PingDirectory 2.2.1 (April 2026)

* [PingDirectory 10.3.0.3](https://docs.pingidentity.com/pingdirectory/10.3/release_notes/pd_release_notes.html#pingdirectory-suite-of-products-10-3-0-3-march-2026)

### Enhancements

#### Support policy now available

New

Our support policy is now available in our product documentation, which covers the platform versions we support, deprecation timelines, and information regarding upgrades. Learn more about our policy in [Support policy](../p1as_support_policy.html).

#### Create and update virtual hosts using the admin console

New

You and your administrators can now create and update virtual host certificates and TLS configurations yourselves by using either the new PingOne Advanced Services admin console or the administrative API. Learn more about this process in [Creating and updating virtual hosts](../task_summary_table/p1as_platform_virtual_hosts.html).

#### IP allow list service request form now available

New

IP allow lists are designed to restrict access to networks, applications, or services to only authorized, preapproved IP addresses. To request that an IP allow list be added or updated to specific PingOne Advanced Services public endpoints, submit a service request through the [Support Portal](https://support.pingidentity.com/s/). Learn more about submitting this type of request in [Platform service requests > IP allow list](../task_summary_table/p1as_platform_allowlist.html).

#### PingDirectory restart process improved

Improved

This update introduces a simplified deployment and configuration pattern for PingDirectory.

## Platform version 2.1.5 (June 2026)

> **Collapse: This platform version deploys with these microservices and applications:**
>
> * PingAccess 2.1.5
>
>   * [PingAccess 8.3.4](https://docs.pingidentity.com/pingaccess/8.3/release_notes/pa_release_notes.html#pa-834)
>
> * PingCentral 2.1.0
>
>   * [PingCentral 2.2.0](https://docs.pingidentity.com/pingcentral/3.0/release_notes/pingcentral_relnotes_home.html#pingcentral-2-2-december-2024)
>
> * PingDirectory 2.1.5
>
>   * [PingDirectory suite of products 10.2.0.6](https://docs.pingidentity.com/pingdirectory/10.2/release_notes/pd_release_notes.html#pingdirectory-suite-of-products-10-2-0-6-march-2026)
>
>     * PingDataSync 10.2.0.7
>
>     * Delegated Admin 5.0.0
>
>       |   |                                                                                                                                                                  |
>       | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>       |   | PingDirectory was upgraded from Java 11 to Java 17 in this release, so compatibility testing and validation should be done before integrating with your systems. |
>
> * PingFederate 2.1.5
>
>   * [PingFederate 12.2.8](https://docs.pingidentity.com/pingfederate/13.0/release_notes/pf_release_notes.html#pingfederate-12-2-8-may-2026)

### Enhancements

#### PingDirectory restart process improved

Improved

This update introduces a simplified deployment and configuration pattern for PingDirectory.

## Platform version 2.1.1 (September 2025)

> **Collapse: This platform version deploys with these microservices and applications:**
>
> * PingAccess 2.1.0
>
>   * [PingAccess 8.2.0](https://docs.pingidentity.com/pingaccess/8.2/release_notes/pa_release_notes.html#pingaccess-8-2-december-2024)
>
> * PingCentral 2.1.0
>
>   * [PingCentral 2.2.0](https://docs.pingidentity.com/pingcentral/2.2/release_notes/pingcentral_relnotes_home.html#pingcentral-2-2-december-2024)
>
> * PingDirectory 2.1.1
>
>   * [PingDirectory suite of products 10.0.0.6](https://docs.pingidentity.com/pingdirectory/10.2/release_notes/pd_release_notes.html#pingdirectory-suite-of-products-10-0-0-6-june-2025)
>
>     * PingDataSync 10.0.0.2
>
>     * Delegated Admin 5.0.0
>
> * PingFederate 2.1.1
>
>   * [PingFederate 12.2.5](https://docs.pingidentity.com/pingfederate/13.0/release_notes/pf_release_notes.html#pingfederate-12-2-5-august-2025)

We've also updated these microservices and applications, which are available for platform version 2.1.1:

### PingFederate 2.1.5 (June 2026)

* [PingFederate 12.2.8](https://docs.pingidentity.com/pingfederate/12.3/release_notes/pf_release_notes.html#pingfederate-12-2-8-may-2026)

### PingAccess 2.1.5 (June 2026)

* [PingAccess 8.3.4](https://docs.pingidentity.com/pingaccess/8.3/release_notes/pa_release_notes.html#pa-834)

### PingAccess 2.1.4 (April 2026)

* [PingAccess 8.3.3](https://docs.pingidentity.com/pingaccess/8.3/release_notes/pa_release_notes.html#pa-833)

### PingAccess 2.1.3 (March 2026)

* [PingAccess 8.3.2](https://docs.pingidentity.com/pingaccess/8.3/release_notes/pa_release_notes.html#pa-832-rn)

### PingFederate 2.1.4 (March 2026)

* [PingFederate 12.2.7](https://docs.pingidentity.com/pingfederate/12.2/release_notes/pf_release_notes.html#pingfederate-12-2-7-february-2026)

### PingFederate 2.1.3 (January 2026)

* [PingFederate 12.2.6](https://docs.pingidentity.com/pingfederate/12.2/release_notes/pf_release_notes.html#pingfederate-12-2-6-november-2025)

### PingFederate 2.1.2 (October 2025)

* [PingFederate 12.2.5](https://docs.pingidentity.com/pingfederate/12.2/release_notes/pf_release_notes.html#pingfederate-12-2-5-august-2025)

### Enhancements

#### Use OAuth to access the PingFederate Admin API

New

To connect to the PingFederate API, get an access token. This token can be retrieved using an [authorization code flow](../task_summary_table/p1as_platform_admin_api.html#_auth_code_flow) or a [client credentials flow](../task_summary_table/p1as_platform_admin_api.html#_client_cred_flow).

If you choose to use a client credentials flow, connections must be correctly configured for self-managing administrator accounts.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingOne Advanced Services platform version 2.1 is the last version that supports basic authentication for the PingFederate and PingAccess Admin APIs. After platform version 2.4.0 is released, 2.1.0 will move into extended support and six months later will reach its End of Life (EOL) status, as outlined in our [Support policy](https://docs.pingidentity.com/pingoneadvancedservices/p1as_support_policy.html). Exceptions to this policy will be granted on a case-by-case basis. |

## Platform version 2.1.0 (May 2025)

> **Collapse: This platform version deploys with these microservices and applications:**
>
> * PingAccess 2.1.0
>
>   * [PingAccess 8.2.0 release notes](https://docs.pingidentity.com/pingaccess/8.2/release_notes/pa_release_notes.html#pingaccess-8-2-december-2024).
>
>     |   |                                                                                                                                                               |
>     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>     |   | PingAccess was upgraded from Java 11 to Java 17 in this release, so compatibility testing and validation should be done before integrating with your systems. |
>
> * PingCentral 2.1.1
>
>   * PingCentral [PingCentral 2.2.0 release notes](https://docs.pingidentity.com/pingcentral/2.3/release_notes/pingcentral_relnotes_home.html#pingcentral-2-2-december-2024).
>
> * PingDirectory 2.1.0
>
>   * [PingDirectory suite of products 10.0.0.4](https://docs.pingidentity.com/pingdirectory/10.2/release_notes/pd_release_notes.html#pingdirectory-suite-of-products-10-0-0-4-october-2024)
>
>     * PingDataSync 10.0.0.2
>
>     * Delegated Admin 5.0.0
>
> * PingFederate 2.1.0
>
>   * [PingFederate 12.1.6](https://docs.pingidentity.com/pingfederate/12.2/release_notes/pf_release_notes.html#pingfederate-12-1-6-february-2025)

### Enhancements

#### Use OAuth to access the PingAccess Admin API

New

* To connect to the PingAccess API, get an access token. This token can be retrieved using an [authorization code flow](../task_summary_table/p1as_platform_admin_api.html#_auth_code_flow) or a [client credentials flow](../task_summary_table/p1as_platform_admin_api.html#_client_cred_flow).

If you choose to use a client credentials flow, connections must be correctly configured for self-managing administrator accounts.

|   |                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For improved security, basic authentication for the PingAccess Admin API has been deprecated and will be removed in PingOne Advanced Services version 2.2. |

#### LDAPS custom domains now supported

Improved

PingDirectory LDAPS URLs are now routed through NGINX, which has improved system flexibility and supports custom domains.

#### Automated certificates for global DNS domains now available

Improved

Those using Let's Encrypt certificates to ensure that communications between PingOne Advanced Services products and services remain encrypted and secure (used by default), can now create automated certificates for global DNS domains.

#### Logging improvements

Improved

Internal log pipeline stability improvements have been made, which will further help you observe and maintain your system.

## Platform version 2.0.1 (April 2025)

> **Collapse: This platform version deploys with these microservices and applications:**
>
> * PingAccess 2.0.1
>
>   * [PingAccess 8.0.6](https://docs.pingidentity.com/pingaccess/8.0/release_notes/pa_release_notes.html#pingaccess-8-0-6-april-2025)
>
> * PingCentral 2.0.1
>
>   * [PingCentral 2.0.2](https://docs.pingidentity.com/pingcentral/2.0/release_notes/pingcentral_relnotes_home.html#pingcentral-2-0-2-april-2024)
>
> * PingDirectory 2.0.1
>
>   * [PingDirectory suite of products 10.0.0.4](https://docs.pingidentity.com:/pingdirectory/10.1/release_notes/pd_release_notes.html#pingdirectory-suite-of-products-10-0-0-4-october-2024)
>
>     * PingDataSync 10.0.0.2
>
>     * Delegated Admin 5.0.0
>
> * PingFederate 2.0.1
>
>   * [PingFederate 12.1.6](https://docs.pingidentity.com/pingfederate/12.2/release_notes/pf_release_notes.html#pingfederate-12-1-6-february-2025)

We've also updated these microservices and applications, which are available for platform version 2.0.1:

### PingFederate 2.0.2 (November 2025)

* [PingFederate 12.1.9](https://docs.pingidentity.com/pingfederate/12.1/release_notes/pf_release_notes.html#pingfederate-12-1-9-september-2025)

### PingDirectory 2.0.3 (March 2026)

* [PingDirectory 10.2.0.6](https://docs.pingidentity.com/pingdirectory/10.2/release_notes/pd_release_notes.html#pingdirectory-suite-of-products-10-2-0-6-march-2026)

## Platform version 2.0.0 (December 2024)

> **Collapse: This platform version deploys with these microservices and applications:**
>
> * PingAccess 2.0.0
>
>   * [PingAccess 8.0.4](https://docs.pingidentity.com/pingaccess/8.0/release_notes/pa_release_notes.html#pa_804_rn)
>
> * PingCentral 2.0.0
>
>   * [PingCentral 2.0.2](https://docs.pingidentity.com/pingcentral/2.0/release_notes/pingcentral_relnotes_home.html#pingcentral-2-0-2-april-2024)
>
> * PingDirectory 2.0.0
>
>   * [PingDirectory suite of products 10.0.0.2](https://docs.pingidentity.com/pingdirectory/10.1/release_notes/pd_release_notes.html#pingdirectory-suite-of-products-10-0-0-2-march-2024)
>
>     * PingDataSync 10.0.0.2
>
>     * Delegated Admin 5.0.0
>
> * PingFederate 2.0.0
>
>   * [PingFederate 12.1.0](https://docs.pingidentity.com/pingfederate/12.1/release_notes/pf_release_notes.html#pingfederate-12-1-june-2024)

### Enhancements

#### Self-service API Beta now available

New

You and your administrators can now create and update virtual host certificates and TLS configurations yourselves through a self-service API. Configurations are automatically replicated to child regions in PingOne Advanced Services for the following applications:

* PingFederate

* PingFederate Admin API

* PingAccess

* PingAccess Admin API

* PingAccess Agents

* PingDirectory

* Delegated Admin

Learn more in [Creating and updating virtual hosts](../task_summary_table/p1as_platform_virtual_hosts.html).

If you don't want to create or update virtual hosts yourself, you can still submit a service request. Select **Advanced/Other** as your requested capability, provide a detailed description of your needs, and submit your request to the Support team.

You'll need to configure access to the administrative API before you can add or update virtual hosts. Learn more about configuring the API in [Configuring access to the administrative API](../task_summary_table/p1as_platform_admin_api.html#_platform_api_config).

You'll also need to add the **SelfService** attribute. Learn more about these attributes in [Creating custom user attributes](../task_summary_table/p1as_platform_mng_admins.html#p1as_custom_attributes). Then, update the application with the appropriate attribute mappings.

---

---
title: PingOne Advanced Services Release Notes
description: Review release notes for PingOne Advanced Services platform versions 1.19.2.0 and earlier.
component: pingoneadvancedservices
page_id: pingoneadvancedservices:release_notes:p1as_rel_notes_prev_versions
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/release_notes/p1as_rel_notes_prev_versions.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 16, 2026
section_ids:
  november-2024: November 2024
  indexed-log-file-retention-policy-change: Indexed log file retention policy change
  september-2024: September 2024
  administrators-can-self-service-their-administrator-sso-accounts: Administrators can self-service their administrator SSO accounts
  may-2024: May 2024
  elasticsearch-replaced-by-opensearch: Elasticsearch replaced by OpenSearch
  pingdirectory-improvements: PingDirectory improvements
  onepinglogin: OnePingLogin
  march-2024: March 2024
  december-2023: December 2023
  delegated-admin: Delegated Admin
  prometheus: Prometheus
  pingdirectory: PingDirectory
  pingfederate: PingFederate
  parsing-improvement: Parsing improvement
  elasticsearch: ElasticSearch
  fluent-bit: Fluent Bit
  grafana: Grafana
  storage-class-provisioner-and-ebs-volume-type-changes: Storage class provisioner and EBS volume type changes
  log-file-handling: Log file handling
  kibana-1-18-only: Kibana (1.18 only)
  argo-cd: Argo CD
  october-2023: October 2023
  september-2023: September 2023
  july-2023: July 2023
  march-2023: March 2023
  dashboard-consolidation: Dashboard consolidation
  user-interface-updates: User interface updates
  november-2022: November 2022
  provision-and-deprovision-users-for-saas-applications: Provision and deprovision users for SaaS applications
  performance-metrics: Performance metrics
  pingfederate-patches-now-automatically-updated: PingFederate patches now automatically updated
  september-2022: September 2022
  password-policy-added-for-topology-administrators: Password policy added for topology administrators
  pingfederate-dashboard-revisions: PingFederate dashboard revisions
  additional-time-series-data-now-available: Additional time series data now available
  active-user-numbers-now-available: Active user numbers now available
  july-2022: July 2022
  use-pingcentral-to-configure-pingfederate-and-pingaccess-environments: Use PingCentral to configure PingFederate and PingAccess environments
  use-pingfederate-admin-api-to-create-password-credential-validator-and-ldap-client-manager: Use PingFederate Admin API to create password credential validator and LDAP client manager
  hot-and-warm-elasticsearch-index-tiers-added: Hot and warm Elasticsearch index tiers added
  health-check-services-added: Health check services added
  configurable-log-streaming-pipeline-added: Configurable log-streaming pipeline added
  may-2022: May 2022
  synchronize-all-of-your-data-sources-into-one-source-of-truth: Synchronize all of your data sources into one source of truth
  pingone-ldap-gateway-connectivity: PingOne LDAP gateway connectivity
  radius-ports-are-now-configured-by-default: RADIUS ports are now configured by default
  pingfederate-thread-usage-auto-tuning-enhanced: PingFederate thread usage auto-tuning enhanced
  custom-password-policies-are-now-available-through-the-admin-portal: Custom password policies are now available through the admin portal
  jvm-metrics-are-now-available-for-pingfederate-and-pingaccess: JVM metrics are now available for PingFederate and PingAccess
  march-2022: March 2022
  web-application-firewall-offers-additional-protection: Web application firewall offers additional protection
  log4j-and-log4shell-security-fixes: Log4j and Log4Shell security fixes
  updated-nginx-ingress-controller: Updated NGINX ingress controller
  updated-dashboard-and-monitoring-tools: Updated dashboard and monitoring tools
  added-opentoken-adapter: Added OpenToken Adapter
---

# PingOne Advanced Services Release Notes

Review release notes for PingOne Advanced Services platform versions 1.19.2.0 and earlier.

## November 2024

**Platform version: 1.19.2.0**. Updated November 21, 2024.

In this platform version:

* PingAccess deploys with version 8.0.4 instead of 8.0.3. You can find details regarding this release in the [PingAccess 8.0.4 release notes](https://docs.pingidentity.com/pingaccess/8.0/release_notes/pa_release_notes.html#pa_804_rn).

* PingCentral deploys with version 2.0.2 instead of 2.0.1. You can find details regarding this release in the [PingCentral 2.0.2 release notes](https://docs.pingidentity.com/pingcentral/latest/release_notes/pingcentral_relnotes_home.html#pingcentral-2-0-2-april-2024).

These applications are also included:

* [PingFederate 11.3.8](https://docs.pingidentity.com/pingfederate/11.3/release_notes/pf_release_notes.html#pingfederate-11-3-8-july-2024)

* [PingDirectory 10.0.0.2](https://docs.pingidentity.com/pingdirectory/latest/release_notes/pd_release_notes.html#pingdirectory-suite-of-products-10-0-0-2-march-2024)

* [PingDataSync 10.0.0.2](https://docs.pingidentity.com/pingdirectory/latest/release_notes/pd_release_notes.html#pingdirectory-suite-of-products-10-0-0-2-march-2024)

* [Delegated Admin 5.0.0](https://docs.pingidentity.com/pingdirectory/10.0/release_notes/pd_release_notes.html#delegated-admin-5-0-december-2023)

### Indexed log file retention policy change

Info

With the release of platform version 1.19.0.0, we announced that we've replaced Elasticsearch with OpenSearch because OpenSearch provides a larger and more innovative feature set. As part of the 1.19.2.0 log adjustments, we will now have indexed logs available for a rolling 30-day window. This change will be rolled out to all platform versions of P1AS starting on Feb 1st. Log files older than 30 days will be unavailable and will remain in our internal archive.

Many of you have your own Security Information and Event Management (SIEM) systems and your own ways of storing, indexing, and searching your log files, so you won't be affected by this change. The same is true if you receive a copy of your logs through a customer endpoint. Your log files can remain on your endpoint systems for the amount of time specified in your retention policies.

Otherwise, this change in policy means that:

* If you're upgrading to version 1.19.2.0, your Elasticsearch data will not be directly migrated into OpenSearch. Instead, only new logs will be processed after the upgrade and be available in your new OpenSearch dashboard when the upgrade is complete.

* If you're using platform version 1.19.0.0, this change will occur on February 1, 2025. On that day, you'll notice that your Kibana or OpenSearch dashboards will only display indexed log files for a rolling 30-day window.

If you want to have indexed log files for more than 30 days, we recommend that you add your own customer-managed endpoint, or use your own SIEM system to store and manage your log files.

To have your logs sent to a SIEM system or other customer endpoint, submit a service request through the [Support Portal](https://support.pingidentity.com/s/). Learn more about submitting this type of request in [Platform service requests > SIEM integration.](../task_summary_table/p1as_platform_siem_integration.html)

## September 2024

**Platform version: 1.19.1.0**. Updated September 11, 2024.

In this platform version:

* PingFederate deploys with version 11.3.8 instead of 11.3.6. You can find details in the [PingFederate 11.3.8 release notes](https://docs.pingidentity.com/pingfederate/12.3/release_notes/pf_release_notes.html#pingfederate-11-3-8-july-2024).

* PingAccess deploys with version 8.0.3 instead of 8.0.1. You can find details regarding this release in the [PingAccess 8.0.3 release notes](https://docs.pingidentity.com/pingaccess/8.3/release_notes/pa_release_notes.html#pingaccess-8-0-3-may-2024).

* OpenSearch and OpenSearch Dashboards were also upgraded from version 2.8.0 to 2.11.1. You can find details in the [OpenSearch and OpenSearch Dashboards 2.11.1 release notes](https://github.com/opensearch-project/opensearch-build/blob/main/release-notes/opensearch-release-notes-2.11.1.md).

These applications are also included:

* [PingDirectory 10.0.0.2](https://docs.pingidentity.com/pingdirectory/10.0/release_notes/pd_release_notes.html#pingdirectory-suite-of-products-10-0-0-2-march-2024)

* [PingDataSync 10.0.0.2](https://docs.pingidentity.com/pingdirectory/10.0/release_notes/pd_release_notes.html#pingdirectory-suite-of-products-10-0-0-2-march-2024)

* [Delegated Admin 5.0](https://docs.pingidentity.com/pingdirectory/10.0/release_notes/pd_release_notes.html#delegated-admin-5-0-december-2023)

* [PingCentral 2.0.1](https://docs.pingidentity.com/pingcentral/2.0/release_notes/pingcentral_relnotes_home.html#pingcentral-2-0-1-january-2024)

### Administrators can self-service their administrator SSO accounts

New

You can now set up and configure connections between environments that will allow your administrators to use single sign-on (SSO) to access the PingOne Advanced Services platform and the appropriate admin consoles.

You'll need to configure access to the administrative API before you can use SSO. Learn more about this process in [Configuring access to the administrative API](../task_summary_table/p1as_platform_admin_api.html#_platform_api_config).

## May 2024

**Platform version: 1.19.0.0.** Updated May 6, 2024.

In this platform version:

* PingAccess deploys with version 8.0.1 instead of 7.07. You can find details regarding this release in the [PingAccess 8.0.1 release notes](https://docs.pingidentity.com/pingaccess/8.0/release_notes/pa_release_notes.html#pa_801_rn).

* PingDirectory deploys with version 10.0.0.2 instead of 9.2.0.4. You can find details regarding this release in the [PingDirectory 10.0.0.2 release notes](https://docs.pingidentity.com/pingdirectory/10.0/release_notes/pd_release_notes.html#pingdirectory-suite-of-products-10-0-0-2-march-2024).

* PingCentral deploys with version 2.0.1 instead of 1.10.1. You can find details regarding this release in the [PingCentral 2.0.1 release notes](https://docs.pingidentity.com/pingcentral/2.0/release_notes/pingcentral_relnotes_home.html#pingcentral-2-0-1-january-2024).

These applications are also included:

* [PingFederate 11.3.5](https://docs.pingidentity.com/pingfederate/12.0/release_notes/pf_release_notes.html#pingfederate-11-3-5-february-2024)

* PingDataSync 10.0.0.1

* [Delegated Admin 5.0](https://docs.pingidentity.com/pingdirectory/10.0/release_notes/pd_release_notes.html#delegated-admin-5-0-december-2023)

### Elasticsearch replaced by OpenSearch

Improved

After careful consideration over several years, PingOne Advanced Services has replaced Elasticsearch with OpenSearch, an open source branch of Elasticsearch. OpenSearch provides a much larger and innovative feature set that enables a better path forward for continuing to provide log indexing, search, alerting, single sign-on (SSO), custom dashboards, and role-based access.

**Elasticsearch data will not be directly migrated into OpenSearch. Instead, only new logs will be processed during the upgrade to platform version 1.19.0.0 and will be available in your new OpenSearch dashboards**. We retain 13 months worth of raw log files, and can reprocess up to 3 months of these files into OpenSearch to allow indexed searches of limited historical data, upon request.

This change should not affect logs sent to your SIEM systems, such as Splunk. Log processing pipelines for your endpoints will remain the same, and logs sent to these endpoints will remain in a raw format for you to process.

Kibana Data Views have also been expanded. Each log generated by an app will now have its own data view, which makes it much easier to know where your logs are based on the name of the log file generated by the app. Custom dashboards will need to be exported as JSON files before the upgrade, and after the upgrade, imported into OpenSearch Dashboards and updated to reflect the changes in the new data views. The change to the data views might also require that you update the dashboard panels with the name of the new data view that previously contained the logs of interest.

### PingDirectory improvements

Improved

Several improvements were made to PingDirectory:

* You can now enable database cache sharing for deployments with multiple backend databases. You can find details in the [PingDirectory 10.0.0.0 release notes](https://docs.pingidentity.com/pingdirectory/10.0/release_notes/pd_release_notes.html#pingdirectory-suite-of-products-10-0-0-0-december-2023).

* When deployed with multiple backend databases, PingDirectory now performs better than before because preloading has been disabled.

* PingDirectory pod IPs availability and propagation to DNS have been improved for multi-region support.

* PingDirectory pods graceful shutdown has been improved and now uses an on-premise software-aligned stop-server script to terminate pods.

### OnePingLogin

Improved

The PingFederate admin console, PingAccess admin console, ArgoCD, and OpenSearch SSO has been improved to reduce the number of multi-factor authentications.

CAP permissions have also been improved to support additional fine-grained controls over user permissions. Now, users sign on using SSO to access their OpenSearch, PingFederate, or PingAccess environments. The tasks they can perform depend on the administrative roles they are assigned. By default, CAP users will not have any PingFederate or PingAccess roles assigned to them and must submit a [service request](../task_summary_table/p1as_service_requests.html) to request the appropriate roles and permissions.

|   |                                                                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This authentication experience is configured in the PingAccess and PingFederate authentication settings. Changing these settings to use a non-default token provider might delay support because it introduces additional authentication steps for Ping Identity operations resources to review. |

PingFederate and PingAccess administrator roles provide fine-grained access to features that allow them to perform specific tasks.

**PingFederate administrator roles**

* **User Admin**: Those with this role can add and remove users, change and reset passwords, and install replacement license keys.

* **Admin**: Those with this role can configure partner connections and most system settings, but they cannot manage local accounts or handle local keys and certificates.

* **Expression Admin**: Those with this role can map user attributes using Object-Graph Navigation Language (OGNL).

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Only administrators who have both the Admin role and the Expression Admin role can be granted:- The User Admin role. This restriction prevents non-Expression Admins from granting themselves the Expression Admin role.

  - Write access to the file system or directory where PingFederate is installed. This restriction prevents a non-Expression Admin user from placing a `data.zip` file containing expressions into the `<pf_install>/pingfederate/server/default/deploy` directory, which would introduce expressions into PingFederate.] |

* **Crypto Admin**: Those with this role manage local keys and certificates.

* **Auditor**: Those with this role have view-only privileges.

**PingAccess administrator roles**

* **Administrator**: Those with this role can access all features unless someone is assigned the Platform Administrator role. If that role is assigned, the Administrators can't update authorization, user, or environment settings, but can access everything else.

* **Platform Administrator**: Those with this role can access everything that an Administrator can access, but they can also update authorization, user, and environment settings and configurations. Use this role in conjunction with the Administrator role to prevent accidental lockouts.

* **Auditor**: Those with this role have view-only privileges.

## March 2024

**Platform version 1.18.2.0**. Updated May 23, 2024.

Product versions:

* In this platform version, PingFederate deploys with version 11.3.6 instead of 11.3.5. You can find details regarding the release in the [PingFederate 11.3.6 release notes](https://docs.pingidentity.com/pingfederate/11.3/release_notes/pf_release_notes.html#pingfederate-11-3-6-april-2024).

* In this platform version, PingAccess deploys with version 7.0.7 instead of 7.0.5. You can find details regarding this release in the [PingAccess 7.0.7 release notes](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-70.pdf).

These applications are also included:

* [PingDirectory 9.2.0.4 suite of products](https://docs.pingidentity.com/archive/#pingdirectory)

* [PingCentral 1.10](https://docs.pingidentity.com/pingcentral/1.11/release_notes/pingcentral_relnotes_home.html#pingcentral-1-10-june-2022)

**Platform version: 1.18.1.0**. Updated March 27, 2024.

In this platform version, PingFederate deploys with version 11.3.5 instead of 11.3.3. You can find details regarding this release in the [PingFederate 11.3.5 release notes](https://docs.pingidentity.com/pingfederate/11.3/release_notes/pf_release_notes.html#pingfederate-11-3-5-february-2024).

These applications are also included:

* PingDirectory 9.2.0.4 suite of products

* PingAccess 7.0.5

* PingCentral 1.10

## December 2023

**Platform version: 1.18.0.0**

In this platform version:

* PingFederate deploys with version 11.3.3 instead of 11.1.8. You can find details regarding this release in the PingFederate 11.3.3 release notes.

* The PingDirectory suite of products deploys with version 9.2.0.4 instead of 9.2.0.2. You can find details regarding this release in the PingDirectory 9.2.0.4 release notes.

These applications are also included:

* PingAccess 7.0.5

* PingCentral 1.10

* Delegated Admin 4.10

### Delegated Admin

New

Administrators can now upload and download user reports.

### Prometheus

New

You can now access Prometheus metrics through a private link or VPN.

### PingDirectory

Improved

Several improvements were made to PingDirectory:

* Backend priming no longer occurs when PingDirectory is started, which decreases PingDirectory startup time.

* PingDirectory restarts have also been enhanced with increased health checking to reduce the chance of data inconsistencies within the cluster.

* Backup and restore now occurs within its own `PersistentVolume`. Learn more in [Backing up and restoring data](https://docs.pingidentity.com/pingdirectory/latest/pingdirectory_server_administration_guide/pd_ds_backup_restore_data.html) in the PingDirectory documentation.

### PingFederate

Improved

Kerberos authentication will no longer support RC4 encryption due to the use of the new 11.0.21 JDK version (which does not support this weak cipher). Any use of RC4 will need to be replaced with AES256 encryption.

### Parsing improvement

Improved

Multi-line logs generated from `server.log` (PingFederate) now appear in Kibana as a single document.

### ElasticSearch

Improved

A horizontal pod autoscaler was added and Logstash performance has improved. The number of warm nodes available has also been increased, which has improved performance and survives AZ failures.

### Fluent Bit

Improved

Now leverages IMDSv2 security instead of IMDSv1.

### Grafana

Improved

User authorization now displays in separate customer and internal teams views. Logging and alert metrics are also now available, but only to internal Ping Identity teams.

### Storage class provisioner and EBS volume type changes

Improved

The StorageClass provisioner was changed to CSI, and the EBS volume type was changed to GP3, which will improve performance and stability.

### Log file handling

Info

Our legacy logging mode (sending log files to Cloudwatch) has been removed, and log files are now sent to our internal ELK (Elasticsearch, Logstash, Kibana) stack or to a customer endpoint.

### Kibana (1.18 only)

Info

Kibana logs older than 90 days must be dropped for the migration to the new StorageClass provisioner. However, raw PROD logs from this time period are still available in S3 but can be restored to Kibana via a service request after the upgrade. When searching indexes, results contain the same fields and data, regardless of which index is chosen. For example, `pf-audit*` and`logstash*` return the same results.

### Argo CD

Info

Argo CD is now only deployed to the one per-region customer hub managing the development, staging, testing, and production environments.

## October 2023

**Platform version: 1.17.3.0.**

The PingDirectory suite of products deploys with version 9.2.0.2 instead of 9.2. You can find details regarding this release in the PingDirectory 9.2.0.2 release notes.

These applications are also included:

* PingAccess 7.0.5

* PingCentral 1.10

* Delegated Admin 4.10

* PingFederate 11.1.8

## September 2023

**Platform version: 1.17.2.0.**

PingFederate deploys with version 11.1.8 instead of 11.1.7. You can find details regarding this release in the PingFederate 11.1.8 release notes.

These applications are also included:

* PingAccess 7.0.5

* PingCentral 1.10

* PingDataSync 8.2.0.6

* Delegated Admin 4.10

* PingDirectory 9.2

## July 2023

**Platform version: 1.17.1.0.**

PingFederate deploys with version 11.1.7 instead of 11.1.5. You can find details regarding this release in the PingFederate 11.1.7 release notes.

These applications are also included:

* PingAccess 7.0.5

* PingCentral 1.10

* PingDataSync 8.2.0.6

* Delegated Admin 4.10

* PingDirectory 9.2

## March 2023

**Platform version: 1.17.0.0.**

PingDirectory deploys with version 9.2 instead of 9.0.0.2. You can find details regarding this release in the PingDirectory 9.2 release notes.

These applications are also included:

* PingAccess 7.0.5

* PingCentral 1.10

* PingDataSync 8.2.0.6

* Delegated Admin 4.10

* PingFederate 11.1.5

### Dashboard consolidation

Improved

The PingOne Advanced Services dashboard has been enhanced. Not only does it provide a consolidated view of key indicators, metrics, and data regarding the health of your infrastructure, but you can now access all of your environments from this location instead of using separate URLs.

### User interface updates

Improved

The PingOne Advanced Services user interface has also been updated to more closely match the look and feel of PingOne, which smooths the transition between the two.

## November 2022

**Platform version: 1.16.5.0**.

These applications are included:

* PingAccess 7.0.5

* PingCentral 1.10

* PingDataSync 8.2.0.6

* Delegated Admin 4.10

* PingDirectory 9.0.0.2

* PingFederate 11.1.5

### **Provision and deprovision users for SaaS applications**

New

Using PingOne Advanced Services, PingFederate administrators can now provision and deprovision users to the following software as a service (SaaS) applications:

* Slack

* Udemy

* Zscaler

* SCIM

* PingOne MFA

|   |                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In a multi-region deployment, SaaS provisioning is deployed to a single region, which is your primary region, and will not be deployed to your secondary region. |

### Performance metrics

Improved

You can now access up to 13 months of performance data that will help you better understand the activities occurring within your PingOne Advanced Services environments.

### **PingFederate patches now automatically updated**

Improved

PingFederate patch versions are now automatically updated in PingOne Advanced Services.

## September 2022

**Platform version: 1.16.2.0**.

PingOne Advanced Services deploys with PingFederate 11.1.5 instead of version 11.1.0. You can find details in the PingFederate 11.1.5 release notes.

These applications are also included:

* PingAccess 7.0.5

* PingCentral 1.10

* PingDataSync 8.2.0.6

* Delegated Admin 4.10

* PingDirectory 9.0.0.2

Kerberos gateway is also now supported.

### **Password policy added for topology administrators**

Fixed

Having a password policy specifically for topology administrators prevents them from being affected when password expiration policies are applied to non-administrator accounts.

### **PingFederate dashboard revisions**

Fixed

PingFederate **Failed SSO** and **Failed Authentication** dashboards have been revised to adjust to PingFederate 11.1 changes.

* The **Failed SSO** dashboard will not contain data if the **Fail Authentication on Account Lockout** option is disabled in PingFederate, which is the default.

* The **Failed Authentication** dashboard will not distinguish between SSO authentication requests and other types of authentication requests.

### **Additional time series data now available**

Improved

Up to 13 months of Prometheus time series data is now available for you to compare current performance metrics with historical data to better understand their environments. Contact your Ping Identity representative for additional information about this option.

### Active user numbers now available

Improved

The number of active users in each environment now displays on Grafana dashboards.

## July 2022

**Platform version: 1.16.1.1**.

These applications are included:

* PingAccess 7.0.5

* PingCentral 1.10

* PingDataSync 8.2.0.6

* Delegated Admin 4.10

* PingDirectory 9.0.0.2

* PingFederate 11.1

### **Use PingCentral to configure PingFederate and PingAccess environments**

New

PingCentral is now deployed with PingFederate and PingAccess environments. All of your development environments, (development, testing, staging, and production) will be configured for you and accessible from PingCentral.

### **Use PingFederate Admin API to create password credential validator and LDAP client manager**

Fixed

You can now use the PingFederate Admin API to create the PingDirectory password credential validator and the LDAP client manager instead of using static XML. If the credential validator or client manager already exists, they will not be overwritten.

### **Hot and warm Elasticsearch index tiers added**

Improved

Elasticsearch index lifecycle management (ILM) policies have been created, and a hot-warm-cold architecture has been implemented to improve performance and resiliency.

The indexer handles indexed data in a way that ages the data through several states. When the data is first indexed, it's added to a hot data tier and remains there for 90 days. Data nodes that are not actively written to are moved to a warm data tier, where they remain for 180 days. Data not accessed for more than 180 days is not indexed.

### **Health check services added**

Improved

Health check services, which provide operational status and performance data, were recently added to monitor internal APIs and clusters.

### **Configurable log-streaming pipeline added**

Improved

You can now use a variety of different security analytics services and customize the ways log data is streamed. You can filter streamed data by application, log, and keywords, and modify JSON files. Available security analytics services include:

* Customer S3 bucket

* Customer Cloudwatch ingestion

* Syslog

* IBM QRadar

## May 2022

**Platform version: 1.16.1.0**.

These applications are included:

* PingAccess 7.0.5

* PingCentral 1.10

* PingDataSync 8.2.0.6

* Delegated Admin 4.10

* PingDirectory 9.0.0.2

* PingFederate 11.1

### Synchronize all of your data sources into one source of truth

New

The PingDataSync Server is now available to synchronize the data from your on-premise and cloud-based data sources into PingDirectory, a high-performance, extensible LDAP directory that serves as the single source of identity truth.

### PingOne LDAP gateway connectivity

New

PingOne LDAP gateway connectivity is now supported in the PingOne Advanced Services Simple Network option, which is significantly less time-consuming to deploy than the Advanced Network option that used to be required for LDAP connectivity.

### RADIUS ports are now configured by default

Improved

Having these ports configured by default eliminates the need for our partners and professional services teams to manually configure them after deployment.

### PingFederate thread usage auto-tuning enhanced

Improved

The PingFederate server thread usage auto-tuning feature has been enhanced to improve the user experience and reduce the need for manual tuning.

### Custom password policies are now available through the admin portal

Improved

Now, not only can you request custom password policies through a service request form, but you can also request them through the admin portal.

### JVM metrics are now available for PingFederate and PingAccess

Improved

The PingFederate and PingAccess tenant dashboards now display Java Virtual Machine (JVM) metrics, which you can use to optimize system performance.

## March 2022

**Platform version: 1.16.0.1**.

These applications are included:

* PingAccess 7.0.5

* PingCentral 1.10

* PingDataSync 8.2.0.6

* Delegated Admin 4.9

* PingFederate 11.1.10

### Web application firewall offers additional protection

Security

A Signal Sciences Web Application Firewall (WAF) was added to the platform to protect environments against vulnerabilities and mitigate DoS and DDoS attacks.

### Log4j and Log4Shell security fixes

Security

This release contains several updates that address and remediate Log4j and Log4Shell vulnerabilities.

### Updated NGINX ingress controller

Improved

The Nginx ingress controller was updated to the latest version, which provides access to the latest network security and performance functionality.

### Updated dashboard and monitoring tools

Improved

NewRelic agent, Kibana, ElasticSearch, Logstash were updated to the latest versions available.

### Added OpenToken Adapter

New

The OpenToken Adapter Kit was added to the PingFederate default profile.

---

---
title: Platform version 2.0.0 (December 2024)
description: PingAccess 2.0.0
component: pingoneadvancedservices
page_id: pingoneadvancedservices:release_notes:p1as_rel_notes_dec2024
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/release_notes/p1as_rel_notes_dec2024.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 10, 2025
section_ids:
  enhancements: Enhancements
  self-service-api-beta-now-available: Self-service API Beta now available
---

# Platform version 2.0.0 (December 2024)

> **Collapse: This platform version deploys with these microservices and applications:**
>
> * PingAccess 2.0.0
>
>   * [PingAccess 8.0.4](https://docs.pingidentity.com/pingaccess/8.0/release_notes/pa_release_notes.html#pa_804_rn)
>
> * PingCentral 2.0.0
>
>   * [PingCentral 2.0.2](https://docs.pingidentity.com/pingcentral/2.0/release_notes/pingcentral_relnotes_home.html#pingcentral-2-0-2-april-2024)
>
> * PingDirectory 2.0.0
>
>   * [PingDirectory suite of products 10.0.0.2](https://docs.pingidentity.com/pingdirectory/10.1/release_notes/pd_release_notes.html#pingdirectory-suite-of-products-10-0-0-2-march-2024)
>
>     * PingDataSync 10.0.0.2
>
>     * Delegated Admin 5.0.0
>
> * PingFederate 2.0.0
>
>   * [PingFederate 12.1.0](https://docs.pingidentity.com/pingfederate/12.1/release_notes/pf_release_notes.html#pingfederate-12-1-june-2024)

## Enhancements

### Self-service API Beta now available

New

You and your administrators can now create and update virtual host certificates and TLS configurations yourselves through a self-service API. Configurations are automatically replicated to child regions in PingOne Advanced Services for the following applications:

* PingFederate

* PingFederate Admin API

* PingAccess

* PingAccess Admin API

* PingAccess Agents

* PingDirectory

* Delegated Admin

Learn more in [Creating and updating virtual hosts](../task_summary_table/p1as_platform_virtual_hosts.html).

If you don't want to create or update virtual hosts yourself, you can still submit a service request. Select **Advanced/Other** as your requested capability, provide a detailed description of your needs, and submit your request to the Support team.

You'll need to configure access to the administrative API before you can add or update virtual hosts. Learn more about configuring the API in [Configuring access to the administrative API](../task_summary_table/p1as_platform_admin_api.html#_platform_api_config).

You'll also need to add the **SelfService** attribute. Learn more about these attributes in [Creating custom user attributes](../task_summary_table/p1as_platform_mng_admins.html#p1as_custom_attributes). Then, update the application with the appropriate attribute mappings.

---

---
title: Platform version 2.0.1 (April 2025)
description: PingAccess 2.0.1
component: pingoneadvancedservices
page_id: pingoneadvancedservices:release_notes:p1as_rel_notes_april2025
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/release_notes/p1as_rel_notes_april2025.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 13, 2026
section_ids:
  pingfederate-2-0-2-november-2025: PingFederate 2.0.2 (November 2025)
  pingdirectory-2-0-3-march-2026: PingDirectory 2.0.3 (March 2026)
---

# Platform version 2.0.1 (April 2025)

> **Collapse: This platform version deploys with these microservices and applications:**
>
> * PingAccess 2.0.1
>
>   * [PingAccess 8.0.6](https://docs.pingidentity.com/pingaccess/8.0/release_notes/pa_release_notes.html#pingaccess-8-0-6-april-2025)
>
> * PingCentral 2.0.1
>
>   * [PingCentral 2.0.2](https://docs.pingidentity.com/pingcentral/2.0/release_notes/pingcentral_relnotes_home.html#pingcentral-2-0-2-april-2024)
>
> * PingDirectory 2.0.1
>
>   * [PingDirectory suite of products 10.0.0.4](https://docs.pingidentity.com:/pingdirectory/10.1/release_notes/pd_release_notes.html#pingdirectory-suite-of-products-10-0-0-4-october-2024)
>
>     * PingDataSync 10.0.0.2
>
>     * Delegated Admin 5.0.0
>
> * PingFederate 2.0.1
>
>   * [PingFederate 12.1.6](https://docs.pingidentity.com/pingfederate/12.2/release_notes/pf_release_notes.html#pingfederate-12-1-6-february-2025)

We've also updated these microservices and applications, which are available for platform version 2.0.1:

## PingFederate 2.0.2 (November 2025)

* [PingFederate 12.1.9](https://docs.pingidentity.com/pingfederate/12.1/release_notes/pf_release_notes.html#pingfederate-12-1-9-september-2025)

## PingDirectory 2.0.3 (March 2026)

* [PingDirectory 10.2.0.6](https://docs.pingidentity.com/pingdirectory/10.2/release_notes/pd_release_notes.html#pingdirectory-suite-of-products-10-2-0-6-march-2026)

---

---
title: Platform version 2.1.0 (May 2025)
description: PingAccess 2.1.0
component: pingoneadvancedservices
page_id: pingoneadvancedservices:release_notes:p1as_rel_notes_may2025
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/release_notes/p1as_rel_notes_may2025.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 12, 2026
section_ids:
  enhancements: Enhancements
  use-oauth-to-access-the-pingaccess-admin-api: Use OAuth to access the PingAccess Admin API
  ldaps-custom-domains-now-supported: LDAPS custom domains now supported
  automated-certificates-for-global-dns-domains-now-available: Automated certificates for global DNS domains now available
  logging-improvements: Logging improvements
---

# Platform version 2.1.0 (May 2025)

> **Collapse: This platform version deploys with these microservices and applications:**
>
> * PingAccess 2.1.0
>
>   * [PingAccess 8.2.0 release notes](https://docs.pingidentity.com/pingaccess/8.2/release_notes/pa_release_notes.html#pingaccess-8-2-december-2024).
>
>     |   |                                                                                                                                                               |
>     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>     |   | PingAccess was upgraded from Java 11 to Java 17 in this release, so compatibility testing and validation should be done before integrating with your systems. |
>
> * PingCentral 2.1.1
>
>   * PingCentral [PingCentral 2.2.0 release notes](https://docs.pingidentity.com/pingcentral/2.3/release_notes/pingcentral_relnotes_home.html#pingcentral-2-2-december-2024).
>
> * PingDirectory 2.1.0
>
>   * [PingDirectory suite of products 10.0.0.4](https://docs.pingidentity.com/pingdirectory/10.2/release_notes/pd_release_notes.html#pingdirectory-suite-of-products-10-0-0-4-october-2024)
>
>     * PingDataSync 10.0.0.2
>
>     * Delegated Admin 5.0.0
>
> * PingFederate 2.1.0
>
>   * [PingFederate 12.1.6](https://docs.pingidentity.com/pingfederate/12.2/release_notes/pf_release_notes.html#pingfederate-12-1-6-february-2025)

## Enhancements

### Use OAuth to access the PingAccess Admin API

New

* To connect to the PingAccess API, get an access token. This token can be retrieved using an [authorization code flow](../task_summary_table/p1as_platform_admin_api.html#_auth_code_flow) or a [client credentials flow](../task_summary_table/p1as_platform_admin_api.html#_client_cred_flow).

If you choose to use a client credentials flow, connections must be correctly configured for self-managing administrator accounts.

|   |                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For improved security, basic authentication for the PingAccess Admin API has been deprecated and will be removed in PingOne Advanced Services version 2.2. |

### LDAPS custom domains now supported

Improved

PingDirectory LDAPS URLs are now routed through NGINX, which has improved system flexibility and supports custom domains.

### Automated certificates for global DNS domains now available

Improved

Those using Let's Encrypt certificates to ensure that communications between PingOne Advanced Services products and services remain encrypted and secure (used by default), can now create automated certificates for global DNS domains.

### Logging improvements

Improved

Internal log pipeline stability improvements have been made, which will further help you observe and maintain your system.

---

---
title: Platform version 2.1.1 (September 2025)
description: PingAccess 2.1.0
component: pingoneadvancedservices
page_id: pingoneadvancedservices:release_notes:p1as_rel_notes_sept2025
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/release_notes/p1as_rel_notes_sept2025.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 13, 2026
section_ids:
  pingfederate-2-1-5-june-2026: PingFederate 2.1.5 (June 2026)
  pingaccess-2-1-5-june-2026: PingAccess 2.1.5 (June 2026)
  pingaccess-2-1-4-april-2026: PingAccess 2.1.4 (April 2026)
  pingaccess-2-1-3-march-2026: PingAccess 2.1.3 (March 2026)
  pingfederate-2-1-4-march-2026: PingFederate 2.1.4 (March 2026)
  pingfederate-2-1-3-january-2026: PingFederate 2.1.3 (January 2026)
  pingfederate-2-1-2-october-2025: PingFederate 2.1.2 (October 2025)
  enhancements: Enhancements
  use-oauth-to-access-the-pingfederate-admin-api: Use OAuth to access the PingFederate Admin API
---

# Platform version 2.1.1 (September 2025)

> **Collapse: This platform version deploys with these microservices and applications:**
>
> * PingAccess 2.1.0
>
>   * [PingAccess 8.2.0](https://docs.pingidentity.com/pingaccess/8.2/release_notes/pa_release_notes.html#pingaccess-8-2-december-2024)
>
> * PingCentral 2.1.0
>
>   * [PingCentral 2.2.0](https://docs.pingidentity.com/pingcentral/2.2/release_notes/pingcentral_relnotes_home.html#pingcentral-2-2-december-2024)
>
> * PingDirectory 2.1.1
>
>   * [PingDirectory suite of products 10.0.0.6](https://docs.pingidentity.com/pingdirectory/10.2/release_notes/pd_release_notes.html#pingdirectory-suite-of-products-10-0-0-6-june-2025)
>
>     * PingDataSync 10.0.0.2
>
>     * Delegated Admin 5.0.0
>
> * PingFederate 2.1.1
>
>   * [PingFederate 12.2.5](https://docs.pingidentity.com/pingfederate/13.0/release_notes/pf_release_notes.html#pingfederate-12-2-5-august-2025)

We've also updated these microservices and applications, which are available for platform version 2.1.1:

## PingFederate 2.1.5 (June 2026)

* [PingFederate 12.2.8](https://docs.pingidentity.com/pingfederate/12.3/release_notes/pf_release_notes.html#pingfederate-12-2-8-may-2026)

## PingAccess 2.1.5 (June 2026)

* [PingAccess 8.3.4](https://docs.pingidentity.com/pingaccess/8.3/release_notes/pa_release_notes.html#pa-834)

## PingAccess 2.1.4 (April 2026)

* [PingAccess 8.3.3](https://docs.pingidentity.com/pingaccess/8.3/release_notes/pa_release_notes.html#pa-833)

## PingAccess 2.1.3 (March 2026)

* [PingAccess 8.3.2](https://docs.pingidentity.com/pingaccess/8.3/release_notes/pa_release_notes.html#pa-832-rn)

## PingFederate 2.1.4 (March 2026)

* [PingFederate 12.2.7](https://docs.pingidentity.com/pingfederate/12.2/release_notes/pf_release_notes.html#pingfederate-12-2-7-february-2026)

## PingFederate 2.1.3 (January 2026)

* [PingFederate 12.2.6](https://docs.pingidentity.com/pingfederate/12.2/release_notes/pf_release_notes.html#pingfederate-12-2-6-november-2025)

## PingFederate 2.1.2 (October 2025)

* [PingFederate 12.2.5](https://docs.pingidentity.com/pingfederate/12.2/release_notes/pf_release_notes.html#pingfederate-12-2-5-august-2025)

## Enhancements

### Use OAuth to access the PingFederate Admin API

New

To connect to the PingFederate API, get an access token. This token can be retrieved using an [authorization code flow](../task_summary_table/p1as_platform_admin_api.html#_auth_code_flow) or a [client credentials flow](../task_summary_table/p1as_platform_admin_api.html#_client_cred_flow).

If you choose to use a client credentials flow, connections must be correctly configured for self-managing administrator accounts.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingOne Advanced Services platform version 2.1 is the last version that supports basic authentication for the PingFederate and PingAccess Admin APIs. After platform version 2.4.0 is released, 2.1.0 will move into extended support and six months later will reach its End of Life (EOL) status, as outlined in our [Support policy](https://docs.pingidentity.com/pingoneadvancedservices/p1as_support_policy.html). Exceptions to this policy will be granted on a case-by-case basis. |

---

---
title: Platform version 2.1.5 (June 2026)
description: PingAccess 2.1.5
component: pingoneadvancedservices
page_id: pingoneadvancedservices:release_notes:p1as_rel_notes_june2026
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/release_notes/p1as_rel_notes_june2026.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 15, 2026
section_ids:
  enhancements: Enhancements
  pingdirectory-restart-process-improved: PingDirectory restart process improved
---

# Platform version 2.1.5 (June 2026)

> **Collapse: This platform version deploys with these microservices and applications:**
>
> * PingAccess 2.1.5
>
>   * [PingAccess 8.3.4](https://docs.pingidentity.com/pingaccess/8.3/release_notes/pa_release_notes.html#pa-834)
>
> * PingCentral 2.1.0
>
>   * [PingCentral 2.2.0](https://docs.pingidentity.com/pingcentral/3.0/release_notes/pingcentral_relnotes_home.html#pingcentral-2-2-december-2024)
>
> * PingDirectory 2.1.5
>
>   * [PingDirectory suite of products 10.2.0.6](https://docs.pingidentity.com/pingdirectory/10.2/release_notes/pd_release_notes.html#pingdirectory-suite-of-products-10-2-0-6-march-2026)
>
>     * PingDataSync 10.2.0.7
>
>     * Delegated Admin 5.0.0
>
>       |   |                                                                                                                                                                  |
>       | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>       |   | PingDirectory was upgraded from Java 11 to Java 17 in this release, so compatibility testing and validation should be done before integrating with your systems. |
>
> * PingFederate 2.1.5
>
>   * [PingFederate 12.2.8](https://docs.pingidentity.com/pingfederate/13.0/release_notes/pf_release_notes.html#pingfederate-12-2-8-may-2026)

## Enhancements

### PingDirectory restart process improved

Improved

This update introduces a simplified deployment and configuration pattern for PingDirectory.

---

---
title: Platform version 2.2.0 (March 2026)
description: PingAccess 2.2.0
component: pingoneadvancedservices
page_id: pingoneadvancedservices:release_notes:p1as_rel_notes_march2026
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/release_notes/p1as_rel_notes_march2026.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 12, 2026
section_ids:
  pingfederate-2-2-2-june-2026: PingFederate 2.2.2 (June 2026)
  pingaccess-2-2-1-june-2026: PingAccess 2.2.1 (June 2026)
  pingfederate-2-2-1-april-2026: PingFederate 2.2.1 (April 2026)
  pingdirectory-2-2-1-april-2026: PingDirectory 2.2.1 (April 2026)
  enhancements: Enhancements
  support-policy-now-available: Support policy now available
  create-and-update-virtual-hosts-using-the-admin-console: Create and update virtual hosts using the admin console
  ip-allow-list-service-request-form-now-available: IP allow list service request form now available
  pingdirectory-restart-process-improved: PingDirectory restart process improved
---

# Platform version 2.2.0 (March 2026)

> **Collapse: This platform version deploys with these microservices and applications:**
>
> * PingAccess 2.2.0
>
>   * [PingAccess 9.0.0](https://docs.pingidentity.com/pingaccess/9.0/release_notes/pa_release_notes.html#pa-90)
>
> * PingCentral 2.2.0
>
>   * [PingCentral 2.2.0](https://docs.pingidentity.com/pingcentral/3.0/release_notes/pingcentral_relnotes_home.html#pingcentral-2-2-december-2024)
>
> * PingDirectory 2.2.0
>
>   * [PingDirectory suite of products 10.3.0.1](https://docs.pingidentity.com/pingdirectory/10.3/release_notes/pd_release_notes.html#rn10301)
>
>     * PingDataSync 10.3.0.0
>
>     * Delegated Admin 5.0.0
>
>       |   |                                                                                                                                                                  |
>       | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>       |   | PingDirectory was upgraded from Java 11 to Java 17 in this release, so compatibility testing and validation should be done before integrating with your systems. |
>
> * PingFederate 2.2.0
>
>   * [PingFederate 12.2.6](https://docs.pingidentity.com/pingfederate/12.2/release_notes/pf_release_notes.html#pingfederate-12-2-6-november-2025)

We've also updated these microservices and applications, which are available for platform version 2.2.0:

## PingFederate 2.2.2 (June 2026)

* [PingFederate 12.3.6](https://docs.pingidentity.com/pingfederate/12.3/release_notes/pf_release_notes.html#pingfederate-12-3-6-april-2026)

## PingAccess 2.2.1 (June 2026)

* [PingAccess 9.0.3](https://docs.pingidentity.com/pingaccess/9.0/release_notes/pa_release_notes.html#pa-903)

## PingFederate 2.2.1 (April 2026)

* [PingFederate 12.3.5](https://docs.pingidentity.com/pingfederate/13.0/release_notes/pf_release_notes.html#pingfederate-12-3-5-february-2026)

* New Update PingFederate templates using the admin console or the administrative API. Learn more in [Accessing the PingOne Advanced Services admin console and administrative API](../task_summary_table/p1as_platform_admin_api.html).

## PingDirectory 2.2.1 (April 2026)

* [PingDirectory 10.3.0.3](https://docs.pingidentity.com/pingdirectory/10.3/release_notes/pd_release_notes.html#pingdirectory-suite-of-products-10-3-0-3-march-2026)

## Enhancements

### Support policy now available

New

Our support policy is now available in our product documentation, which covers the platform versions we support, deprecation timelines, and information regarding upgrades. Learn more about our policy in [Support policy](../p1as_support_policy.html).

### Create and update virtual hosts using the admin console

New

You and your administrators can now create and update virtual host certificates and TLS configurations yourselves by using either the new PingOne Advanced Services admin console or the administrative API. Learn more about this process in [Creating and updating virtual hosts](../task_summary_table/p1as_platform_virtual_hosts.html).

### IP allow list service request form now available

New

IP allow lists are designed to restrict access to networks, applications, or services to only authorized, preapproved IP addresses. To request that an IP allow list be added or updated to specific PingOne Advanced Services public endpoints, submit a service request through the [Support Portal](https://support.pingidentity.com/s/). Learn more about submitting this type of request in [Platform service requests > IP allow list](../task_summary_table/p1as_platform_allowlist.html).

### PingDirectory restart process improved

Improved

This update introduces a simplified deployment and configuration pattern for PingDirectory.

---

---
title: September 2022
description: "Platform version: 1.16.2.0."
component: pingoneadvancedservices
page_id: pingoneadvancedservices:release_notes:p1as_rel_notes_sept2022
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/release_notes/p1as_rel_notes_sept2022.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 9, 2024
section_ids:
  password-policy-added-for-topology-administrators: Password policy added for topology administrators
  pingfederate-dashboard-revisions: PingFederate dashboard revisions
  additional-time-series-data-now-available: Additional time series data now available
  active-user-numbers-now-available: Active user numbers now available
---

# September 2022

**Platform version: 1.16.2.0**.

PingOne Advanced Services deploys with PingFederate 11.1.5 instead of version 11.1.0. You can find details in the PingFederate 11.1.5 release notes.

These applications are also included:

* PingAccess 7.0.5

* PingCentral 1.10

* PingDataSync 8.2.0.6

* Delegated Admin 4.10

* PingDirectory 9.0.0.2

Kerberos gateway is also now supported.

## **Password policy added for topology administrators**

Fixed

Having a password policy specifically for topology administrators prevents them from being affected when password expiration policies are applied to non-administrator accounts.

## **PingFederate dashboard revisions**

Fixed

PingFederate **Failed SSO** and **Failed Authentication** dashboards have been revised to adjust to PingFederate 11.1 changes.

* The **Failed SSO** dashboard will not contain data if the **Fail Authentication on Account Lockout** option is disabled in PingFederate, which is the default.

* The **Failed Authentication** dashboard will not distinguish between SSO authentication requests and other types of authentication requests.

## **Additional time series data now available**

Improved

Up to 13 months of Prometheus time series data is now available for you to compare current performance metrics with historical data to better understand their environments. Contact your Ping Identity representative for additional information about this option.

## Active user numbers now available

Improved

The number of active users in each environment now displays on Grafana dashboards.