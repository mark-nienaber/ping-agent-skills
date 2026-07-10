---
title: December 2023
description: "Platform version: 1.18.0.0"
component: pingoneadvancedservices
page_id: pingoneadvancedservices:release_notes:p1as_rel_notes_dec2023
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/release_notes/p1as_rel_notes_dec2023.html
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
title: March 2024
description: Platform version 1.18.2.0. Updated May 23, 2024.
component: pingoneadvancedservices
page_id: pingoneadvancedservices:release_notes:p1as_rel_notes_march2024
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/release_notes/p1as_rel_notes_march2024.html
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
title: Platform version 2.0.1 (April 2025)
description: PingAccess 2.0.1
component: pingoneadvancedservices
page_id: pingoneadvancedservices:release_notes:p1as_rel_notes_april2025
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/release_notes/p1as_rel_notes_april2025.html
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