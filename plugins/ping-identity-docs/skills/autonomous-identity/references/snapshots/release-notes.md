---
title: Before you start
description: "Ping Autonomous Identity server software requires the following hardware, storage, and operating system requirements to run in your production environment. Ping Autonomous Identity's flexible architecture runs in a variety of network environments: on-prem, cloud, multi-cloud, and hybrid."
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:release-notes:chap-before-you-install
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/release-notes/chap-before-you-install.html
section_ids:
  sec-downloadables: Ping Google Cloud Registry key
  sec-hardware-memory-requirements: Hardware and memory requirements
  sec-storage-requirements: Storage requirements
  sec-operating-systems: Operating systems requirements
  cloud_services_requirements: Cloud services requirements
  sec-java-requirements: Java requirements
  sec-third-party-sw-requirements: Third-party software
  sec-supported-browsers: Supported browsers
---

# Before you start

Ping Autonomous Identity server software requires the following hardware, storage, and operating system requirements to run in your production environment. Ping Autonomous Identity's flexible architecture runs in a variety of network environments: on-prem, cloud, multi-cloud, and hybrid.

|   |                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | All production systems differ in many ways. Please discuss with your Ping Identity Professional Services, installers, or partner representatives about your environment specifics. |

## Ping Google Cloud Registry key

You deploy Ping Autonomous Identity using a Docker image that pulls other dependent images from the Ping Google Cloud Registry repository and installs the components on a target node.

For specific instructions on obtaining the registry key, refer to [How To Configure Service Credentials (Push Auth, Docker) in Backstage](https://backstage.forgerock.com/knowledge/backstagehelp/article/a92326771).

## Hardware and memory requirements

Ping Autonomous Identity has a number of components that include application, data, and analytics servers, which are all included in the Docker images. The minimum hardware and memory requirements for a single-node target and a separate deployer machine are as follows:

**Hardware and memory requirements**

| Vendor                  | Versions          |
| ----------------------- | ----------------- |
| Deployer Node           | 32 GB RAM, 8 CPU  |
| Analytics (Target) Node | 64 GB RAM, 16 CPU |

## Storage requirements

Ping Autonomous Identity has a number of components that include application, data, and analytics servers, which are included in the Docker images. The minimum storage requirements for a single-node deployment are as follows:

Ping Autonomous Identity requires the following minimum storage requirements:

**Storage requirements**

| Type         | Size                                |
| ------------ | ----------------------------------- |
| Data Storage | 500 GB (minimum), 1 TB (production) |

## Operating systems requirements

Ping Autonomous Identity is supported on the following operating system:

**Operating System Requirements**

| Vendor                  | Versions\[[1](#_footnotedef_1 "View footnote.")] |
| ----------------------- | ------------------------------------------------ |
| CentOS Stream           | 8.0                                              |
| Redhat Enterprise Linux | 8.0                                              |

## Cloud services requirements

Ping Autonomous Identity has been successfully deployed on the following cloud services:

**Cloud Services Requirements**

| Vendor                                                                    | Versions |
| ------------------------------------------------------------------------- | -------- |
| Google Cloud Platform (GCP)                                               | Latest   |
| Amazon Web Services (AWS) standard Elastic File System (EFS) shared drive | Latest   |

## Java requirements

Ping Autonomous Identity software supports the following Java version:

**Java requirements**

| Vendor  | Versions |
| ------- | -------- |
| OpenJDK | 11.0.16  |

## Third-party software

Ping Autonomous Identity uses the following third-party software in the deployment.

IMPORTANT:

If your existing deployment uses the deployer-pro installer (2022.11.0 and later), you can upgrade these third-party dependencies to these versions.

If your existing deployment uses the deployer installer (pre-2022.11.0 or earlier), you do not need to pre-install or upgrade these components in your environment. The Ping Autonomous Identity deployer installs or upgrades these dependencies.

**Third-party software**

| Component                        | Version                          | Usage                                                                                                                                           |
| -------------------------------- | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Python                           | 3.10.9                           | Deployer and Deployer Pro scripts                                                                                                               |
| Docker CE                        | 20.10.17                         | Container cluster management                                                                                                                    |
| Apache Cassandra                 | 4.0.8                            | Database for all Ping Autonomous Identity services                                                                                              |
| MongoDB                          | 4.4.19                           | Database for all Ping Autonomous Identity services. If using MongoDB with LDAP, set the `mongo_ldap` property to `true` in the `vars.yml` file. |
| Apache Spark                     | 3.3.2 with Hadoop 3              | Cluster to run Ping Autonomous Identity analytics                                                                                               |
| Apache Livy                      | Updated to work with Spark 3.3.2 | REST interface to Spark master to run Ping Autonomous Identity analytics                                                                        |
| Opensearch/Opensearch Dashboards | 1.3.14                           | Distributed, open source search engine and visualization tool for all data types.                                                               |

## Supported browsers

Ping Autonomous Identity supports the following browsers:

**Supported browsers**

| Vendor          | Versions                         |
| --------------- | -------------------------------- |
| Google Chrome   | version 85.0.4183.121 and higher |
| Mozilla Firefox | version 86.0.1 and higher        |

***

[1](#_footnoteref_1). For Ping Autonomous Identity 2022.8.x systems that use CentOS/Redhat Enterprise Linux 7.0 and upgrade to Ping Autonomous Identity 2022.11.x, Ping Autonomous Identity continues to run on CentOS/Redhat Enterprise Linux 7.0. For new Ping Autonomous Identity 2022.11.x installations, use CentOS/Redhat Enterprise Linux 8.0.
