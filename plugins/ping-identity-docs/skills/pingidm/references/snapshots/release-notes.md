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

| Plugin                                           | Supported Version                                         |
| ------------------------------------------------ | --------------------------------------------------------- |
| DS Password Synchronization Plugin               | 8.1.x, supported with DS 8.1.x and IDM 8.1.x              |
| Active Directory Password Synchronization Plugin | 1.8.0 and 1.5.0 supported on Windows Server 2019 and 2022 |
