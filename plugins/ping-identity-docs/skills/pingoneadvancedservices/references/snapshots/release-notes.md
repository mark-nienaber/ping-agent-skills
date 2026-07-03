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
