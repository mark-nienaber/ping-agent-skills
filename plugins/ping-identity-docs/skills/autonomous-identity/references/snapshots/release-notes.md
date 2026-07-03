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

---

---
title: Changelog
description: "Subscribe to get automatic updates: Ping Autonomous Identity changelog RSS feed"
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:release-notes:changelog
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/release-notes/changelog.html
section_ids:
  latest_updates: Latest updates
  march_07_2025: March 07, 2025
  june_17_2024: June 17, 2024
  april_05_2024: April 05, 2024
  february_15_2024: February 15, 2024
  december_12_2023: December 12, 2023
  october_23_2023: October 23, 2023
  september_11_2023: September 11, 2023
  september_05_2023: September 05, 2023
  august_15_2023: August 15, 2023
  july_20_2023: July 20, 2023
  june_05_2023: June 05, 2023
  april_13_2023: April 13, 2023
  april_12_2023: April 12, 2023
  april_11_2023: April 11, 2023
  february_24_2023: February 24, 2023
  january_09_2023: January 09, 2023
  december_08_2022: December 08, 2022
  november_28_2022: November 28, 2022
  november_15_2022: November 15, 2022
---

# Changelog

Subscribe to get automatic updates: [icon: rss-square, set=fa][Ping Autonomous Identity changelog RSS feed](../release-notes/changelog.xml)

Ping Identity continuously provides updates to Ping Autonomous Identity to introduce new features, fix known bugs and address security issues.

## Latest updates

### March 07, 2025

* 2022.11.12

  Initial release of Ping Autonomous Identity 2022.11.12. This release contains a collection of security fixes.

### June 17, 2024

* 2022.11.11

  Initial release of Ping Autonomous Identity 2022.11.11. This release contains a collection of security fixes. The documentation has been rebranded to Ping.

### April 05, 2024

* 2022.11.10

  Initial release of Ping Identity Autonomous Identity 2022.11.10. This release contains a collection of security fixes.

### February 15, 2024

* 2022.11.9

  Initial release of Ping Identity Autonomous Identity 2022.11.09. This release contains a collection of security fixes. This version updated Opensearch and Opensearch Dashboards 1.3.14.

### December 12, 2023

* 2022.11.8

  Initial release of Ping Identity Autonomous Identity 2022.11.08. This release contains a collection of security fixes.

### October 23, 2023

* 2022.11.7

  Initial release of Ping Identity Autonomous Identity 2022.11.07. This release contains a collection of security and bug fixes. Additionally, Ping Autonomous Identity requires Opensearch 1.3.13 in this release.

### September 11, 2023

* 2022.11.6

  Initial release of Ping Identity Autonomous Identity 2022.11.06. This release contains the latest container images.

### September 05, 2023

* 2022.11.6

  Initial release of Ping Identity Autonomous Identity 2022.11.05. This release contains a collection of security and bug fixes.

### August 15, 2023

* 2022.11.5

  This release contains a collection of security and bug fixes.

### July 20, 2023

* 2022.11.5

  Initial release of Ping Identity Autonomous Identity 2022.11.05. The following bugs were fixed in this release as well as other security fixes:

  * [AUTOID-3174](https://bugster.forgerock.org/jira/browse/AUTOID-3174): Need an assignments API

  * [AUTOID-3362](https://bugster.forgerock.org/jira/browse/AUTOID-3362): Allow customer to change timeout for API container when run Opensearch query

### June 05, 2023

* 2022.11.4

  Initial release of Ping Identity Autonomous Identity 2022.11.04. The following bugs were fixed in this release:

  * [AUTOID-3329](https://bugster.forgerock.org/jira/browse/AUTOID-3329): Misspelled http header for kibana conf

  * [AUTOID-3331](https://bugster.forgerock.org/jira/browse/AUTOID-3331): Elasticsearch keystore and truststore password

### April 13, 2023

* 2022.11.3

  Initial release of Ping Identity Autonomous Identity 2022.11.03. This release contains a collection of important security fixes.

### April 12, 2023

* 2022.11.3

  The following bugs were fixed in this release as well as other security fixes:

  * [AUTOID-2766](https://bugster.forgerock.org/jira/browse/AUTOID-2766): Analytics results show inconsistent results

  * [AUTOID-2864](https://bugster.forgerock.org/jira/browse/AUTOID-2864): Not able to delete data sources in AutoID

  * [AUTOID-2894](https://bugster.forgerock.org/jira/browse/AUTOID-2894): Support for updating all certificates in AutoID

  * [AUTOID-3130](https://bugster.forgerock.org/jira/browse/AUTOID-3130): Upgrade Spark to 3.3

  * [AUTOID-3135](https://bugster.forgerock.org/jira/browse/AUTOID-3135): Upgrade Open Distro to Opensearch

  * [AUTOID-3145](https://bugster.forgerock.org/jira/browse/AUTOID-3145): Upgrade Python to 3.8

  * [AUTOID-3160](https://bugster.forgerock.org/jira/browse/AUTOID-3160): Upgrade OpenJDK to 11

### April 11, 2023

* 2022.11.3

  Initial release of Ping Identity Autonomous Identity 2022.11.03. Initial release of Ping Identity Autonomous Identity 2022.11.3. Added an assignments endpoint to the API.

### February 24, 2023

* 2022.11.2

  Initial release of Ping Identity Autonomous Identity 2022.11.2.

### January 09, 2023

* 2022.11.1

  Initial release of Ping Identity Autonomous Identity 2022.11.1.

### December 08, 2022

* 2022.11.0

  Removed the `refresh-company-view` command as it is no longer required in the Analytics pipeline process.

### November 28, 2022

* 2022.11.0

  Change to the MongoDB password post-deployment process.

### November 15, 2022

* 2022.11.0

  Initial release of Ping Identity Autonomous Identity 2022.11.0.

---

---
title: Deprecated
description: No functionality has been deprecated in these releases.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:release-notes:chap-deprecated
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/release-notes/chap-deprecated.html
---

# Deprecated

* 2022.11.0–2022.11.12

  No functionality has been deprecated in these releases.

---

---
title: Documentation updates
description: The following table tracks changes to the documentation following the release of Ping Autonomous Identity 2022.11.12:
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:release-notes:chap-doc-updates
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/release-notes/chap-doc-updates.html
---

# Documentation updates

The following table tracks changes to the documentation following the release of Ping Autonomous Identity 2022.11.12:

**Documentation Change Log**

| Date       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2025-09-23 | Added an RSS feed to the changelog.                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 2025-03-07 | Initial release of Ping Autonomous Identity 2022.11.12.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 2024-06-17 | Initial release of Ping Autonomous Identity 2022.11.11. Rebranded the docs to Ping.                                                                                                                                                                                                                                                                                                                                                                                         |
| 2024-04-05 | Initial release of Ping Identity Autonomous Identity 2022.11.10.                                                                                                                                                                                                                                                                                                                                                                                                            |
| 2024-02-15 | Initial release of Ping Identity Autonomous Identity 2022.11.9.- Updated the Opensearch and Opensearch Dashboard versions to 1.3.14.                                                                                                                                                                                                                                                                                                                                        |
| 2023-12-12 | Initial release of Ping Identity Autonomous Identity 2022.11.8.                                                                                                                                                                                                                                                                                                                                                                                                             |
| 2023-10-23 | Initial release of Ping Identity Autonomous Identity 2022.11.7.- Updated the Opensearch version to 1.3.13. Refer to [Third-party software](chap-before-you-install.html#sec-third-party-sw-requirements).                                                                                                                                                                                                                                                                   |
| 2023-09-11 | Added a step to install the Python wheel file after upgrade with deployer pro. Refer to [Upgrade from 2022.11.x to 2022.11.6 (Non Air-Gap) using deployer pro](../install-guide/chap-upgrade.html#sec-upgrade-2022.11.x-to-2022.11.6-deployer-pro) or [Upgrade from 2022.11.x to 2022.11.6 Air-Gapped using deployer pro](../install-guide/chap-upgrade.html#sec-upgrade-2022.11.x-to-2022.11.6-airgap-deployer-pro).                                                       |
| 2023-09-05 | Initial release of Ping Identity Autonomous Identity 2022.11.6.- Conflated the fixes, known issues, deprecated, and removed sections into one changelog file. Refer to [Changelog](changelog.html).                                                                                                                                                                                                                                                                         |
| 2023-08-15 | Added a line that you need to update your third-party software packages to the supported versions prior to upgrading Ping Autonomous Identity. Refer to [Upgrade from Autonomous Identity 2022.11.x to 2022.11.5 using deployer pro](../install-guide/chap-upgrade.html#sec-upgrade-2022.11.x-to-2022.11.5-deployer-pro).                                                                                                                                                   |
| 2023-07-20 | Initial release of Ping Identity Autonomous Identity 2022.11.5.- Updated the Python version. Refer to [Third-party software](chap-before-you-install.html#sec-third-party-sw-requirements).

- Moved the [Ports](../install-guide/appendix-deployment-ports.html) section from the release notes to the installation section.                                                                                                                                               |
| 2023-06-05 | Initial release of Ping Identity Autonomous Identity 2022.11.4.                                                                                                                                                                                                                                                                                                                                                                                                             |
| 2023-04-13 | Added a known issue. Refer to [Known issues in 2022.11.3](changelog.html#known-issues.adoc).                                                                                                                                                                                                                                                                                                                                                                                |
| 2023-04-12 | Added a section on updating the domain and namespace in existing deployments. Refer to [Customize the Domain and Namespace (New deployments)](../admin-guide/chap-deployment-tasks.html#customize-domain-existing).                                                                                                                                                                                                                                                         |
| 2023-04-11 | * Initial release of Ping Identity Autonomous Identity 2022.11.3.

* Added a section to change the default timeout (30 ms) for the API's Elasticsearch client request timeout. Refer to [Change the API's Elasticsearch client request timeout](../admin-guide/chap-admin-user-tasks.html#change-elasticsearch-client-request-timeout).

* Added the Assignments endpoint to the API. Refer to [Assignments](../api-guide/chap-assignments-api.html).                       |
| 2023-02-24 | Initial release of Ping Identity Autonomous Identity 2022.11.2.                                                                                                                                                                                                                                                                                                                                                                                                             |
| 2023-01-09 | Initial release of Ping Identity Autonomous Identity 2022.11.1.                                                                                                                                                                                                                                                                                                                                                                                                             |
| 2022-12-08 | - Removed the refresh-company-view command as it is no longer required in the Analytics pipeline process.

- Updated the steps to install the Python egg file. Refer to [Install Ping Autonomous Identity](../install-guide/chap-install-singlenode-target.html#install-autoid).

- Removed sections pertaining to third-party component backup-restore and import-export data in the [Server Maintenance](../admin-guide/chap-server-maintenance.html#server-maintenance). |
| 2022-11-28 | Added a section to change the MongoDB password post-deployment. Refer to [Change the MongoDB password post-deployment](../admin-guide/chap-server-maintenance.html#sec-mongodb-pwd-change).                                                                                                                                                                                                                                                                                 |
| 2022-11-15 | Initial release of Ping Identity Autonomous Identity 2022.11.0.                                                                                                                                                                                                                                                                                                                                                                                                             |

---

---
title: Getting support
description: Ping Identity provides support services, professional services, training through Ping Identity University, and partner services to assist you in setting up and maintaining your deployments. For a general overview of these services, refer to https://www.pingidentity.com.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:release-notes:appendix-getting-support
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/release-notes/appendix-getting-support.html
---

# Getting support

Ping Identity provides support services, professional services, training through Ping Identity University, and partner services to assist you in setting up and maintaining your deployments. For a general overview of these services, refer to <https://www.pingidentity.com>.

Ping Identity has staff members around the globe who support our international customers and partners. For details on Ping Identity's support offering, including support plans and service level agreements (SLAs), visit <https://support.pingidentity.com/>.

Ping Identity publishes comprehensive documentation online:

* The Ping Identity [Knowledge Base](https://backstage.forgerock.com/knowledge/kb) offers a large and increasing number of up-to-date, practical articles that help you deploy and manage Ping Identity software.

  While many articles are visible to community members, Ping Identity customers have access to much more, including advanced information for customers using Ping Identity software in a mission-critical capacity.

* Ping Identity product documentation, such as this document, aims to be technically accurate and complete with respect to the software documented. It is visible to everyone and covers all product features and examples of how to use them.

---

---
title: Known issues
description: There are no known issues in this release.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:release-notes:chap-known-issues
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/release-notes/chap-known-issues.html
---

# Known issues

* 2022.11.4–2022.11.12

  There are no known issues in this release.

- 2022.11.3

  * **Discovered regression**

    Ping Autonomous Identity 2022.11.3 was originally released on 04-11-2023.

    We discovered a regression where Apache Livy has log4j1 binaries included with the deployer. If you installed 2022.11.3 *before* 04/13/2023, run the steps below to upgrade log4j1 to log4j2.

    If you installed 2022.11.3 *after* 04/13/2023, the binaries are updated, and you do not need to upgrade log4j1 binaries.

    Update log4j1 to log4j2

    1. Stop the Apache Livy server:

       ```
       ~/livy/bin/livy-server stop
       ```

    2. Back up your old log4j and related jar files:

       ```
       cd ~/livy/jars
       mv log4j-1.2.16.jar ~/log4j-1.2.16.jar.bkp
       mv slf4j-log4j12-1.6.1.jar ~/slf4j-log4j12-1.6.1.jar.bkp
       mv slf4j-reload4j-1.7.36.jar ~/slf4j-reload4j-1.7.36.jar.bkp
       mv slf4j-api-1.7.25.jar ~/slf4j-api-1.7.25.jar.bkp
       ```

    3. Replace with log4j2 jar and its bridge jars:

       ```
       cd ~/livy/jars
       wget https://repo1.maven.org/maven2/org/apache/logging/log4j/log4j-1.2-api/2.18.0/log4j-1.2-api-2.18.0.jar
       wget https://repo1.maven.org/maven2/org/apache/logging/log4j/log4j-core/2.18.0/log4j-core-2.18.0.jar
       wget https://repo1.maven.org/maven2/org/apache/logging/log4j/log4j-slf4j-impl/2.18.0/log4j-slf4j-impl-2.18.0.jar
       wget https://repo1.maven.org/maven2/org/apache/logging/log4j/log4j-api/2.18.0/log4j-api-2.18.0.jar
       wget https://repo1.maven.org/maven2/org/slf4j/slf4j-api/1.7.36/slf4j-api-1.7.36.jar
       ```

    4. Under the `conf` folder, create a `log4j2.properties` file:

       ```
       cd ~/livy/conf
       vi log4j2.properties
       ```

    5. In your `log4j2.properties` file, adjust the log level and related configuration suited for your requirements:

       ```
       status = info
       name= RollingFileLogConfigDemo
       # Log files location
       property.basePath = ./logs
       # RollingFileAppender name, pattern, path and rollover policy
       appender.rolling.type = RollingFile
       appender.rolling.name = fileLogger
       appender.rolling.fileName= ${basePath}/autoid.log
       appender.rolling.filePattern= ${basePath}/autoid_%d{yyyyMMdd}.log.gz
       appender.rolling.layout.type = PatternLayout
       appender.rolling.layout.pattern = %d{yyyy-MM-dd HH:mm:ss.SSS} %level [%t] [%l] - %msg%n
       appender.rolling.policies.type = Policies
       # RollingFileAppender rotation policy
       appender.rolling.policies.size.type = SizeBasedTriggeringPolicy
       appender.rolling.policies.size.size = 10MB
       appender.rolling.policies.time.type = TimeBasedTriggeringPolicy
       appender.rolling.policies.time.interval = 1
       appender.rolling.policies.time.modulate = true
       appender.rolling.strategy.type = DefaultRolloverStrategy
       appender.rolling.strategy.delete.type = Delete
       appender.rolling.strategy.delete.basePath = ${basePath}
       appender.rolling.strategy.delete.maxDepth = 10
       appender.rolling.strategy.delete.ifLastModified.type = IfLastModified
       # Delete all files older than 30 days
       appender.rolling.strategy.delete.ifLastModified.age = 30d
       # Configure root logger
       rootLogger.level = info
       rootLogger.appenderRef.rolling.ref = fileLogger
       log4j1.compatibility = true
       ```

    6. Restart Apache Livy:

       ```
       cd ~/livy/
       ./bin/livy-server start
       ```

    7. Check that Apache Livy is up and running. You can access a log on an analytics jobs. Specific Ping Autonomous Identity logs are at `~/livy/logs/autoid.log.`

- 2022.11.2

  There are no known issues in this release.

- 2022.11.1

  There are no known issues in this release.

* 2022.11.0

  There is a known issue with RHEL8/CentOS Stream 8 when Docker swarm overlay network configuration breaks when the outside network maximum transmission unit (mtu) is smaller than the default value. The `mtu` is the maximum size of the packet that can be transmitted from a network interface.

  Refer to <https://github.com/moby/libnetwork/issues/2661> and <https://github.com/moby/moby/pull/43197>.

  When deploying a multinode configuration on RHEL 8/CentOS Stream 8, run the following steps:

  1. Check mtu for docker0 and eth0 using `ifconfig | grep mtu`.

  2. Set the docker0 mtu value to be equal to `eth0` using `sudo ifconfig eth0 mtu 1500`. Make sure to set the command on all nodes and also after each virtual machine reboot.

---

---
title: Release levels and interface stability
description: Ping Identity defines Major, Minor, and Patch product release levels. The release level is reflected in the version number. The release level tells you what sort of compatibility changes to expect.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:release-notes:appendix-interface-stability
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/release-notes/appendix-interface-stability.html
section_ids:
  upgrade-patching: Upgrade and Patching
  interface-stability: Ping Identity Product Stability Labels
---

# Release levels and interface stability

Ping Identity defines Major, Minor, and Patch product release levels. The release level is reflected in the version number. The release level tells you what sort of compatibility changes to expect.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Ping Autonomous Identity uses a different version numbering system from other Ping Identity products. The version number use the following format: `Major.Minor.Patch`, where *Major* is the year of the release, *Minor* is the month of the release, *Patch* is the number beginning with 0, and increases for each patch release.Thus, for this release of Ping Autonomous Identity, the version number is **2022.11.12**. |

**Release Level Definitions**

| Release Label | Version Numbers   | Characteristics                                                                                                                                                                                                                                             |
| ------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Major         | Version: x\[.0.0] | * Bring major new features, minor features, and bug fixes

* Can include changes even to Stable interfaces

* Major indicates the year of the release, for example, `2021`                                                                                  |
| Minor         | Version: x.y\[.0] | - Bring minor features, and bug fixes

- Can include backwards-compatibile changes to Stable interfaces in the same Major release, and incompatible changes to Evolving interfaces

- Minor indicates the month of the release, for example, `8` for August |
| Patch         | Version: x.y.z    | * Bring bug fixes

* Are intended to be fully compatible with previous versions from the same Minor release

* Patch starts with `0` and increases for each bug fix release                                                                                 |

## Upgrade and Patching

Ping Identity plans to introduce quarterly upgrades and patches for Ping Autonomous Identity as a service to our customers. Ping Autonomous Identity's architecture supports seamless rolling upgrades to simplify the process.

The following are some general points about upgrades and patches:

* Upgrades and patches are implemented using a simple swap of the underlying container. The operation is zero down-time as long as the cluster has a redundant instance of the microservice.

* Patching doesn't require schema changes.

  Ping Autonomous Identity schema changes are additive and backward-compatible. This means that during a zero-downtime upgrade, older versions of the container can still write to the new version of the schema. Also, newer versions of the container may alter the tables in a way that preserves the semantics of the previous columns.

* If an upgrade requires a downgrade due to some issue, the downgrade will not restore the previous schema.

More information about upgrading, refer to [Upgrade Ping Autonomous Identity](../install-guide/chap-upgrade.html).

## Ping Identity Product Stability Labels

Ping Identity products support many features, protocols, APIs, GUIs, and command-line interfaces. Some of these are standard and very stable. Others offer new functionality that is continuing to evolve.

Ping Identity acknowledges that you invest in these features and interfaces, and therefore must know when and how Ping Identity expects them to change. For that reason, Ping Identity defines stability labels and uses these definitions in Ping Identity products.

**Ping Identity Stability Label Definitions**

| Stability Label       | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Stable                | This documented feature or interface is expected to undergo backwards-compatible changes only for major releases. Changes may be announced at least one minor release before they take effect.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Evolving              | This documented feature or interface is continuing to evolve and so is expected to change, potentially in backwards-incompatible ways even in a minor release. Changes are documented at the time of product release.While new protocols and APIs are still in the process of standardization, they are Evolving. This applies for example to recent Internet-Draft implementations, and also to newly developed functionality.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Legacy                | This feature or interface has been replaced with an improved version, and is no longer receiving development effort from Ping Identity.You should migrate to the newer version, however the existing functionality will remain.Legacy features or interfaces will be marked as *Deprecated* if they are scheduled to be removed from the product.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Deprecated            | This feature or interface is deprecated and likely to be removed in a future release. For previously stable features or interfaces, the change was likely announced in a previous release. Deprecated features or interfaces will be removed from Ping Identity products.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Removed               | This feature or interface was deprecated in a previous release and has now been removed from the product.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Technology Preview    | Technology previews provide access to new features that are considered as new technology that is not yet supported. Technology preview features may be functionally incomplete and the function as implemented is subject to change without notice. DO NOT DEPLOY A TECHNOLOGY PREVIEW INTO A PRODUCTION ENVIRONMENT.Customers are encouraged to test drive the technology preview features in a non-production environment and are welcome to make comments and suggestions about the features in the associated forums.Ping Identity doesn't guarantee that a technology preview feature will be present in future releases, the final complete version of the feature is liable to change between preview and the final version. After a technology preview moves into the completed version, the feature will become part of the Ping Identity platform. Technology previews are provided on an "AS-IS" basis for evaluation purposes only and Ping Identity accepts no liability or obligations for the use thereof. |
| Internal/Undocumented | Internal and undocumented features or interfaces can change without notice. If you depend on one of these features or interfaces, contact Ping Identity support to discuss your needs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

---

---
title: Release notes
description: Ping® Autonomous Identity is an entitlements and roles analytics system that lets you fully manage your company's access to your data.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:release-notes:preface
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/release-notes/preface.html
page_aliases: ["_@autonomous-identity::index.adoc"]
---

# Release notes

Ping® Autonomous Identity is an entitlements and roles analytics system that lets you fully manage your company's access to your data.

These release notes are written for anyone using the Ping Autonomous Identity 2022.11.12 release. Read these notes before you install Ping Autonomous Identity software, especially for production deployments.

[icon: newspaper, set=fas, size=3x]

#### [What's New](chap-whats-new.html)

Discover new features.

[icon: cogs, set=fas, size=3x]

#### [Before You Install](chap-before-you-install.html)

Check prerequisites.

[icon: asterisk, set=fas, size=3x]

#### [Changelog](changelog.html)

Check key fixes, known issues, deprecated, and removed items.

[icon: book, set=fas, size=3x]

#### [Documentation](chap-doc-updates.html)

Track doc changes.

[icon: wrench, set=fas, size=3x]

#### [Interface Stability](appendix-interface-stability.html)

Learn about the Release Levels, upgrades, and stability levels.

[icon: life-ring, set=fas, size=3x]

#### [Getting Support](appendix-getting-support.html)

Get support and training.

---

---
title: Removed functionality
description: No functionality has been removed in these releases.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:release-notes:chap-removed
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/release-notes/chap-removed.html
---

# Removed functionality

* 2022.11.0–2022.11.12

  No functionality has been removed in these releases.

---

---
title: Security advisories
description: Ping Identity issues security advisories in collaboration with our customers and the open source community to address any security vulnerabilities transparently and rapidly. Ping Identity's security advisory policy governs the process on how security issues are submitted, received, and evaluated as well as the timeline for the issuance of security advisories and patches.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:release-notes:chap-security-advisories
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/release-notes/chap-security-advisories.html
---

# Security advisories

Ping Identity issues security advisories in collaboration with our customers and the open source community to address any security vulnerabilities transparently and rapidly. Ping Identity's security advisory policy governs the process on how security issues are submitted, received, and evaluated as well as the timeline for the issuance of security advisories and patches.

---

---
title: What&#8217;s new
description: Ping Autonomous Identity 2022.11.12 is the latest patch release containing a collection of security fixes released as part of our commitment to our customers.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:release-notes:chap-whats-new
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/release-notes/chap-whats-new.html
section_ids:
  ping_autonomous_identity_2022_11_12: Ping Autonomous Identity 2022.11.12
  ping_autonomous_identity_2022_11_11: Ping Autonomous Identity 2022.11.11
  ping_autonomous_identity_2022_11_10: Ping Autonomous Identity 2022.11.10
  ping_autonomous_identity_2022_11_9: Ping Autonomous Identity 2022.11.9
  ping_autonomous_identity_2022_11_8: Ping Autonomous Identity 2022.11.8
  ping_autonomous_identity_2022_11_7: Ping Autonomous Identity 2022.11.7
  ping_autonomous_identity_2022_11_6: Ping Autonomous Identity 2022.11.6
  ping_autonomous_identity_2022_11_5: Ping Autonomous Identity 2022.11.5
  ping_autonomous_identity_2022_11_4: Ping Autonomous Identity 2022.11.4
  ping_autonomous_identity_2022_11_3: Ping Autonomous Identity 2022.11.3
  ping_autonomous_identity_2022_11_2: Ping Autonomous Identity 2022.11.2
  ping_autonomous_identity_2022_11_1: Ping Autonomous Identity 2022.11.1
  ping_autonomous_identity_2022_11_0: Ping Autonomous Identity 2022.11.0
---

# What's new

Ping Autonomous Identity 2022.11.12 is the latest patch release containing a collection of security fixes released as part of our commitment to our customers.

You can find more general information about Ping Identity's sustaining process for maintenance releases and customer patches in [ForgeRock Sustaining Processes for Maintenance Releases and Customer Patches](https://backstage.forgerock.com/knowledge/cs/article/a67990254).

You can deploy Ping Autonomous Identity 2022.11.12 as an initial deployment or upgrade it from an existing 2022.11.x deployment.

## Ping Autonomous Identity 2022.11.12

* **Security fixes**. Ping Autonomous Identity introduces security fixes. For specific information on the fixes, contact ForgeRock.

## Ping Autonomous Identity 2022.11.11

* **Security fixes**. Ping Autonomous Identity introduces security fixes. For specific information on the fixes, contact ForgeRock.

## Ping Autonomous Identity 2022.11.10

* **Security fixes**. Ping Autonomous Identity introduces security fixes. For specific information on the fixes, contact ForgeRock.

## Ping Autonomous Identity 2022.11.9

* **Security fixes**. Ping Autonomous Identity introduces security fixes. For specific information on the fixes, contact ForgeRock.

* **Opensearch 1.3.14**. Ping Autonomous Identity 2022.11.12 requires Opensearch 1.3.14.

## Ping Autonomous Identity 2022.11.8

* **Security fixes**. Ping Autonomous Identity introduces security fixes. For specific information on the fixes, contact ForgeRock.

## Ping Autonomous Identity 2022.11.7

* **Security and bug fixes**. Ping Autonomous Identity introduces security and bug fixes. For specific information on the fixes, contact ForgeRock.

* **Opensearch 1.3.13**. Ping Autonomous Identity now requires Opensearch 1.3.13.

  * For all new deployments from 2022.11.x to the latest version 2022.11.7 using `deployer-pro`, update Opensearch from version 1.3.9 to 1.3.13 prior to running your upgrade. For more information, refer to [Opensearch 1.3.13](https://opensearch.org/versions/opensearch-1-3-13.html).

  * For deployments upgraded from 2022.8.x using the `deployer` installer, Ping Autonomous Identity upgrades to version Opensearch 1.3.13 automatically.

## Ping Autonomous Identity 2022.11.6

Ping Autonomous Identity introduces updated container images.

## Ping Autonomous Identity 2022.11.5

* **Security and bug fixes**. Ping Autonomous Identity introduces security and bug fixes. For specific information on the fixes, contact ForgeRock.

* **Upgraded components**. Ping Autonomous Identity requires the following third-party software dependency:

  * Python 3.10.9

## Ping Autonomous Identity 2022.11.4

* **Security and bug fixes**. Ping Autonomous Identity introduces security and bug fixes. For specific information on the fixes, contact ForgeRock.

## Ping Autonomous Identity 2022.11.3

* **New property to use MongoDB with LDAP**. Ping Autonomous Identity has a new `vars.yml` property, `mongo_ldap=false,` which when set to `true`, lets Ping Autonomous Identity authenticate with MongoDB, configured with LDAP.

* **New assignments endpoint**. Ping Autonomous Identity now provides an endpoint to support the extraction of assignments. Refer to [Assignments](../api-guide/chap-assignments-api.html).

* ForgeRock discovered a regression in 2022.11.3. Refer to [Known issues in 2022.11.3](changelog.html#known-issues.adoc).

## Ping Autonomous Identity 2022.11.2

* **Security and bug fixes**. Ping Autonomous Identity introduces security and bug fixes. For specific information on the fixes, contact ForgeRock.

## Ping Autonomous Identity 2022.11.1

* **Security and bug fixes**. Ping Autonomous Identity introduces security and bug fixes. For specific information on the fixes, contact ForgeRock.

## Ping Autonomous Identity 2022.11.0

* **Upgraded deployer script**. Ping Autonomous Identity introduces a new deployer script, *Deployer Pro*. The Deployer Pro script downloads and installs Ping Autonomous Identity within your environment. However, customers must now install the third-party software dependencies required for Ping Autonomous Identity prior to running Deployer Pro *on new deployments only.* The deployer pro lets customers install and configure those dependencies best suited for their network environment as well as their scale, performance, high availability (HA), and disaster recovery (DR) requirements.

  |   |                                                                                                                                                                                                                  |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Customers with existing 2021.8.7 deployments can upgrade their Ping Autonomous Identity systems to 2022.11, while maintaining their existing third-party software components used in their 2021.8.7 deployments. |

* **Upgraded components**. Ping Autonomous Identity requires the following third-party software dependencies:

  * Opensearch and Opensearch Dashboards 1.3.6

  * Apache Cassandra 4

  * Apache MongoDB 4.4

  * Apache Spark 3.3

  * Apache Livy with log4j2 support

  * Python 3.8

  * OpenJDK 11

* **Internal Security Fixes**. ForgeRock has made a number of important security fixes and updates.