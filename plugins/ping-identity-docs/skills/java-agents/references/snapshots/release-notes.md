---
title: Archive
description: This archive contains the release notes for Java Agent versions that have reached End of Maintenance (EOM).
component: java-agents
version: release-notes
page_id: java-agents::archive
canonical_url: https://docs.pingidentity.com/java-agents/release-notes/archive.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Archive

This archive contains the release notes for Java Agent versions that have reached End of Maintenance (EOM).

You can find information about release and lifecycle dates in the [Ping Identity End of Life (EOL) Software Tracker](https://support.pingidentity.com/s/article/Ping-Identity-EOL-Tracker#pamagents).

---

---
title: Changes
description: The changes that impact existing functionality in versions of Java Agent that have reached End of Maintenance (EOM).
component: java-agents
version: release-notes
page_id: java-agents::archive-changes
canonical_url: https://docs.pingidentity.com/java-agents/release-notes/archive-changes.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Changes

The changes that impact existing functionality in versions of Java Agent that have reached End of Maintenance (EOM).

* [Changes in Java Agent 2023.x](changes-2023.html)

* [Changes in Java Agent 5.10.x](changes-510.html)

---

---
title: Changes in Java Agent 2023.x
description: There are no incompatible changes in the Java Agent 2023.11 release or the Java Agent 2023.11.1 maintenance release.
component: java-agents
version: release-notes
page_id: java-agents::changes-2023
canonical_url: https://docs.pingidentity.com/java-agents/release-notes/changes-2023.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  java_agent_2023_11_x: Java Agent 2023.11.x
  java_agent_2023_11_2: Java Agent 2023.11.2
  url-handling-changes-2023112: URL handling
  monitoring: Monitoring
  java_agent_2023_9: Java Agent 2023.9
  tomcat_java_agent_software_update: Tomcat Java Agent software update
  jboss_and_wildfly_java_agent_software_update: JBoss and WildFly Java Agent software update
  jetty_java_agent_software_update: Jetty Java Agent software update
  weblogic_java_agent_software_update: WebLogic Java Agent software update
  changed-in-2023.6: Java Agent 2023.6
  changed-in-2023.3: Java Agent 2023.3
  jdk_8: JDK 8
  jdk_11_with_weblogic_12c_java_agent_and_websphere_java_agent: JDK 11 with WebLogic 12c Java Agent and WebSphere Java Agent
---

# Changes in Java Agent 2023.x

## Java Agent 2023.11.x

There are no incompatible changes in the Java Agent 2023.11 release or the Java Agent 2023.11.1 maintenance release.

### Java Agent 2023.11.2

#### URL handling

To improve security, we've made changes to how the agent handles incoming URLs. These changes may affect the agent's behavior because not-enforced rules and AM policies are evaluated against normalized paths with the path parameters removed.

Learn more about these changes in [URL handling](whats-new.html#url-handling-2023112).

#### Monitoring

The common REST monitoring endpoint has been removed. Use the [Prometheus endpoint](https://docs.pingidentity.com/java-agents/2023.11/maintenance-guide/monitoring.html#monitor-prometheus) for monitoring your deployment.

## Java Agent 2023.9

### Tomcat Java Agent software update

The `agent.jar` isn't required for drop-in software update to Java Agent 2023.9. If the file is present in the container, delete it as described in *Tomcat Java Agent software update*.

### JBoss and WildFly Java Agent software update

You must now provide the full path to `jee-agents-sdk-version.jar` in the `module.xml` file for drop-in software update to Java Agent 2023.9. The following libraries are no longer required:

* `agent.jar`

* `jee-agents-jboss-common-version.jar`

* `tyrus-standalone-client-version.jar`

For more information, refer to *JBoss and WildFly Java Agent software update*.

### Jetty Java Agent software update

The `agent.jar` file isn't required for drop-in software update to Java Agent 2023.9. If the file is present in `amlogin.mod`, delete it as described in *Jetty Java Agent software update*.

### WebLogic Java Agent software update

The following libraries aren't required for drop-in software update to Java Agent 2023.9:

* `agent.jar`

* `jee-agents-installtools-version.jar`

For more information, refer to *WebLogic Java Agent software update*.

## Java Agent 2023.6

There are no incompatible changes in this release.

## Java Agent 2023.3

### JDK 8

Support for JDK 8 has been removed.

### JDK 11 with WebLogic 12c Java Agent and WebSphere Java Agent

WebLogic 12c Java Agent and WebSphere Java Agent do not support JDK 11, which is the minimum JDK version supported in this release. Consequently, these platforms are not supported in this release. Use Java Agent 5.10 or an earlier version for these platforms.

---

---
title: Changes in Java Agent 2024.x
description: There are no incompatible changes in the Java Agent 2024.11.1 maintenance release.
component: java-agents
version: release-notes
page_id: java-agents::changes-2024
canonical_url: https://docs.pingidentity.com/java-agents/release-notes/changes-2024.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  java_agent_2024_11_x: Java Agent 2024.11.x
  java_agent_2024_11: Java Agent 2024.11
  url-handling-changes: URL handling
  java_agent_2024_9: Java Agent 2024.9
  monitoring: Monitoring
  java_agent_2024_6: Java Agent 2024.6
  commons_audit_framework: Commons Audit Framework
  java_agent_2024_3: Java Agent 2024.3
---

# Changes in Java Agent 2024.x

## Java Agent 2024.11.x

There are no incompatible changes in the Java Agent 2024.11.1 maintenance release.

### Java Agent 2024.11

#### URL handling

To improve security, we've made changes to how the agent handles incoming URLs. These changes may affect the agent's behavior because not-enforced rules and AM policies are evaluated against normalized paths with the path parameters removed.

Learn more about these changes in [URL handling](whats-new.html#url-handling).

## Java Agent 2024.9

### Monitoring

The common REST monitoring endpoint has been removed. Use the *Prometheus endpoint* for monitoring your deployment.

## Java Agent 2024.6

### Commons Audit Framework

To improve security, the audit handling code is deprecated and replaced by the Commons Audit Framework.

To prevent logging of sensitive data for an audit event, the Commons Audit Framework uses a safelist to specify which audit event fields appear in the logs.

By default, only safelisted audit event fields are included in the logs. To include and exclude elements from JSON audit events, use `Audit Log Include Paths` and `Audit Log Exclude Paths`.

## Java Agent 2024.3

There are no incompatible changes in this release.

---

---
title: Changes in Java Agent 2025.x
description: There are no incompatible changes in this release.
component: java-agents
version: release-notes
page_id: java-agents::changes-2025
canonical_url: https://docs.pingidentity.com/java-agents/release-notes/changes-2025.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  changes_in_java_agent_2025_11: Changes in Java Agent 2025.11
  changes_in_java_agent_2025_3: Changes in Java Agent 2025.3
  am_6_5: AM 6.5
---

# Changes in Java Agent 2025.x

## Changes in Java Agent 2025.11

There are no incompatible changes in this release.

## Changes in Java Agent 2025.3

### AM 6.5

AM 6.5 has reached End of Life (EOL) and is no longer supported.

---

---
title: Changes in Java Agent 2026.x
description: Support for JDK 11 has been removed.
component: java-agents
version: release-notes
page_id: java-agents::changes-2026
canonical_url: https://docs.pingidentity.com/java-agents/release-notes/changes-2026.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  changes_in_java_agent_2026_6: Changes in Java Agent 2026.6
  jdk_11: JDK 11
  jdk_17_with_weblogic_14c_14_1_1_java_agent: JDK 17 with WebLogic 14c (14.1.1) Java Agent
---

# Changes in Java Agent 2026.x

## Changes in Java Agent 2026.6

### JDK 11

Support for JDK 11 has been removed.

### JDK 17 with WebLogic 14c (14.1.1) Java Agent

WebLogic 14c (14.1.1) doesn't support JDK 17, which is the minimum JDK version supported in this release. Consequently, this platform isn't supported in this release.

---

---
title: Changes in Java Agent 5.10.x
description: To improve security, we've made changes to how the agent handles incoming URLs. These changes may affect the agent's behavior because not-enforced rules and AM policies are evaluated against normalized paths with the path parameters removed.
component: java-agents
version: release-notes
page_id: java-agents::changes-510
canonical_url: https://docs.pingidentity.com/java-agents/release-notes/changes-510.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  java_agent_5_10_4: Java Agent 5.10.4
  url-handling-changes-5104: URL handling
  java_agent_5_10: Java Agent 5.10
  logback: Logback
---

# Changes in Java Agent 5.10.x

## Java Agent 5.10.4

### URL handling

To improve security, we've made changes to how the agent handles incoming URLs. These changes may affect the agent's behavior because not-enforced rules and AM policies are evaluated against normalized paths with the path parameters removed.

Learn more about these changes in [URL handling](whats-new.html#url-handling-5104).

## Java Agent 5.10

### Logback

Log messages in Java Agent and third-party dependencies are now recorded using the Logback implementation of the Simple Logging Facade for Java (SLF4J) API.

From this release, `TRACE` is the highest log level. In previous releases, `ON` was the highest log level.

From this release, when the log level is `ON`, `TRACE` level logs are written to file. In previous releases, `TRACE` level logs were written to the standard output.

---

---
title: Deprecated
description: Deprecated is defined in Release levels and interface stability:
component: java-agents
version: release-notes
page_id: java-agents::archive-deprecated
canonical_url: https://docs.pingidentity.com/java-agents/release-notes/archive-deprecated.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Deprecated

Deprecated is defined in [Release levels and interface stability](stability.html):

| Deprecated in | Description | Replaced by | Removed in |
| ------------- | ----------- | ----------- | ---------- |
| 2023.11       | -           | -           | -          |
| 2023.9        | -           | -           | -          |
| 2023.6        | -           | -           | -          |
| 2023.3        | -           | -           | -          |
| 5.10          | -           | -           | -          |

---

---
title: Deprecated
description: Deprecated is defined in Release levels and interface stability.
component: java-agents
version: release-notes
page_id: java-agents::deprecated
canonical_url: https://docs.pingidentity.com/java-agents/release-notes/deprecated.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Deprecated

Deprecated is defined in [Release levels and interface stability](stability.html).

| Deprecated in | Description                                            | Replaced by                                                                                                                                                                                                                                                     | Removed in      |
| ------------- | ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| 2026.6        | Java EE support                                        | -                                                                                                                                                                                                                                                               | Not yet removed |
| 2025.11       | -                                                      | -                                                                                                                                                                                                                                                               | -               |
| 2025.3        | -                                                      | -                                                                                                                                                                                                                                                               | -               |
| 2024.11       | -                                                      | -                                                                                                                                                                                                                                                               | -               |
| 2024.9        | -                                                      | -                                                                                                                                                                                                                                                               | -               |
| 2024.6        | Local audit handling with `Local Audit Log Filename`   | Commons Audit Framework, using:- `Audit Log Directory`

- `Audit Log Include Paths`

- `Audit Log Exclude Paths`Sensitive information, such as cookies and some headers, is no longer audited by default. Learn more from [Incompatible changes](changes.html). | Not yet removed |
| 2024.3        | AM 6.5 support                                         | Later versions of AM                                                                                                                                                                                                                                            | 2025.3          |
|               | Java 11 support                                        | Java 17 support                                                                                                                                                                                                                                                 | 2026.6          |
|               | `Login Attempt Limit Cookie Name``Login Attempt Limit` | -                                                                                                                                                                                                                                                               | Not yet removed |

---

---
title: Fixes
description: The fixed issues in versions of Java Agent that have reached End of Maintenance (EOM).
component: java-agents
version: release-notes
page_id: java-agents::archive-fixes
canonical_url: https://docs.pingidentity.com/java-agents/release-notes/archive-fixes.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Fixes

The fixed issues in versions of Java Agent that have reached End of Maintenance (EOM).

* [Fixes in Java Agent 2023.x](fixes-2023.html)

* [Fixes in Java Agent 5.10.x](fixes-510.html)

---

---
title: Fixes
description: The following pages list important fixes in maintained Java Agent versions.
component: java-agents
version: release-notes
page_id: java-agents::fixes
canonical_url: https://docs.pingidentity.com/java-agents/release-notes/fixes.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Fixes

The following pages list important fixes in maintained Java Agent versions.

|   |                                                                                                                                                                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Fixes are cumulative by release date. An issue fixed in a maintenance release, such as Java Agent 2024.11.1, isn't included in a major release, such as Java Agent 2025.3, if the major release was issued before the minor release.You can find the fixes for previous versions that have reached End of Maintenance in the [Archive](archive.html). |

* [Fixes in Java Agent 2026.x](fixes-2026.html)

* [Fixes in Java Agent 2025.x](fixes-2025.html)

* [Fixes in Java Agent 2024.x](fixes-2024.html)

---

---
title: Fixes in Java Agent 2023.x
description: This page lists the cumulative fixes in Java Agent 2023.x releases:
component: java-agents
version: release-notes
page_id: java-agents::fixes-2023
canonical_url: https://docs.pingidentity.com/java-agents/release-notes/fixes-2023.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  java_agent_2023_11_x: Java Agent 2023.11.x
  java_agent_2023_11_2: Java Agent 2023.11.2
  java_agent_2023_11_1: Java Agent 2023.11.1
  java_agent_2023_11: Java Agent 2023.11
  java_agent_2023_9: Java Agent 2023.9
  fix-in-2023.6: Java Agent 2023.6
  fix-in-2023.3: Java Agent 2023.3
---

# Fixes in Java Agent 2023.x

This page lists the cumulative fixes in Java Agent 2023.x releases:

## Java Agent 2023.11.x

### Java Agent 2023.11.2

No issues were fixed in this release.

### Java Agent 2023.11.1

|               |                                                      |
| ------------- | ---------------------------------------------------- |
| AMAGENTS-6258 | Enforce agent's Logback configuration isolation      |
| AMAGENTS-6131 | Tomcat Agent uninstall fails when done a second time |

### Java Agent 2023.11

No issues were fixed in this release.

## Java Agent 2023.9

|               |                                                                                          |
| ------------- | ---------------------------------------------------------------------------------------- |
| AMAGENTS-5999 | Cannot initialize logback when invoking classes in the agent SDK                         |
| AMAGENTS-5928 | Remove META-INF/services/javax.servlet.ServletContainerInitializer from the distribution |
| AMAGENTS-5798 | Oracle WebLogic admin console fails after patch upgrade                                  |
| AMAGENTS-3798 | The AM Conditional Login URL should check that the entry has a \| in it                  |

## Java Agent 2023.6

|               |                                                                                           |
| ------------- | ----------------------------------------------------------------------------------------- |
| AMAGENTS-5797 | java.lang.NullPointerException in org.forgerock.agents.util.UrlParamNormaliser            |
| AMAGENTS-5685 | JPA: Address bug in cache thawing                                                         |
| AMAGENTS-5654 | JPA conditional login does not work in case when specific header should match any value   |
| AMAGENTS-5600 | JPA: Enabling pathinfo and using URL encoding raises exception                            |
| AMAGENTS-5236 | JPA does not respect port/protocol overrides for Not Enforced Rules and Policy Evaluation |

## Java Agent 2023.3

|               |                                                                                                    |
| ------------- | -------------------------------------------------------------------------------------------------- |
| AMAGENTS-5550 | Changing the log level at runtime stops logging altogether                                         |
| AMAGENTS-5497 | Avoid use of the "Agent Tree" for JPA login                                                        |
| AMAGENTS-5089 | agentadmin --encrypt Agent\_Id \<password-file> throws error                                       |
| AMAGENTS-4816 | Do not invoke rest logout for some special cases                                                   |
| AMAGENTS-3912 | Avoid displaying a huge stacktrace to the user when the bootstrap properties file cannot be opened |

---

---
title: Fixes in Java Agent 2024.x
description: This page lists the cumulative fixes in Java Agent 2024.x releases:
component: java-agents
version: release-notes
page_id: java-agents::fixes-2024
canonical_url: https://docs.pingidentity.com/java-agents/release-notes/fixes-2024.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  java_agent_2024_11_x: Java Agent 2024.11.x
  java_agent_2024_11_1: Java Agent 2024.11.1
  java_agent_2024_11: Java Agent 2024.11
  java_agent_2024_9: Java Agent 2024.9
  java_agent_2024_6: Java Agent 2024.6
  java_agent_2024_3: Java Agent 2024.3
---

# Fixes in Java Agent 2024.x

This page lists the cumulative fixes in Java Agent 2024.x releases:

## Java Agent 2024.11.x

### Java Agent 2024.11.1

|               |                                          |
| ------------- | ---------------------------------------- |
| AMAGENTS-7034 | Uninstalling Weblogic agent doesn't work |

### Java Agent 2024.11

|               |                                                                                                               |
| ------------- | ------------------------------------------------------------------------------------------------------------- |
| AMAGENTS-6860 | The count for the number of allowed by policy requests also counts the redirection to authentication callback |

## Java Agent 2024.9

|               |                                                                                                      |
| ------------- | ---------------------------------------------------------------------------------------------------- |
| AMAGENTS-6612 | Java Agent in accept SSO token mode with custom login false writes JWT tokens to iPlanetDirectoryPro |

## Java Agent 2024.6

|               |                                                       |
| ------------- | ----------------------------------------------------- |
| AMAGENTS-6588 | agentadmin writes a log file every time it is started |
| AMAGENTS-6258 | Enforce agent's Logback configuration isolation       |

## Java Agent 2024.3

|               |                                                                 |
| ------------- | --------------------------------------------------------------- |
| AMAGENTS-6131 | Tomcat Agent uninstall fails when done a second time            |
| AMAGENTS-6119 | Menu for uninstall options has number 11 at start rather than 1 |
| AMAGENTS-6118 | Install help has error in the output                            |

---

---
title: Fixes in Java Agent 2025.x
description: This page lists the cumulative fixes in Java Agent 2025.x releases:
component: java-agents
version: release-notes
page_id: java-agents::fixes-2025
canonical_url: https://docs.pingidentity.com/java-agents/release-notes/fixes-2025.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  java_agent_2025_11: Java Agent 2025.11
  java_agent_2025_3: Java Agent 2025.3
---

# Fixes in Java Agent 2025.x

This page lists the cumulative fixes in Java Agent 2025.x releases:

## Java Agent 2025.11

|               |                                                               |
| ------------- | ------------------------------------------------------------- |
| AMAGENTS-7495 | Failure running agentadmin --key 80 on Windows for Java Agent |
| AMAGENTS-6615 | agentadmin option "--getEncryptKey" doesn't work on Windows   |

## Java Agent 2025.3

|               |                                                     |
| ------------- | --------------------------------------------------- |
| AMAGENTS-7034 | Uninstalling Weblogic agent doesn't work            |
| AMAGENTS-6809 | Monitoring endpoint doesn't work for Jakarta builds |

---

---
title: Fixes in Java Agent 2026.x
description: This page lists the cumulative fixes in Java Agent 2026.x releases:
component: java-agents
version: release-notes
page_id: java-agents::fixes-2026
canonical_url: https://docs.pingidentity.com/java-agents/release-notes/fixes-2026.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  java_agent_2026_6: Java Agent 2026.6
---

# Fixes in Java Agent 2026.x

This page lists the cumulative fixes in Java Agent 2026.x releases:

## Java Agent 2026.6

No issues were fixed in this release.

---

---
title: Fixes in Java Agent 5.10.x
description: This page lists the cumulative fixes in Java Agent 5.10.x releases:
component: java-agents
version: release-notes
page_id: java-agents::fixes-510
canonical_url: https://docs.pingidentity.com/java-agents/release-notes/fixes-510.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  java_agent_5_10_4: Java Agent 5.10.4
  fix-in-5103: Java Agent 5.10.3
  java_agent_5_10_2: Java Agent 5.10.2
  java_agent_5_10_1: Java Agent 5.10.1
  java_agent_5_10: Java Agent 5.10
---

# Fixes in Java Agent 5.10.x

This page lists the cumulative fixes in Java Agent 5.10.x releases:

## Java Agent 5.10.4

No issues were fixed in this release.

## Java Agent 5.10.3

|               |                                        |
| ------------- | -------------------------------------- |
| AMAGENTS-5590 | JPA version is not set in config files |

## Java Agent 5.10.2

|               |                                                            |
| ------------- | ---------------------------------------------------------- |
| AMAGENTS-5550 | Changing the log level at runtime stops logging altogether |
| AMAGENTS-5497 | Avoid use of the "Agent Tree" for JPA login                |

## Java Agent 5.10.1

|               |                                                                           |
| ------------- | ------------------------------------------------------------------------- |
| AMAGENTS-5182 | Log level should be WARN if agent-profile authN fails using service=Agent |
| AMAGENTS-5089 | agentadmin --encrypt Agent\_Id \<password-file> throws error              |
| AMAGENTS-4816 | Agent does not invoke rest logout for special cases                       |

## Java Agent 5.10

|               |                                               |
| ------------- | --------------------------------------------- |
| AMAGENTS-4677 | Reimplement pre-authentication cookie signing |
| AMAGENTS-4667 | Bug in i18n not-enforced pattern matching     |
| AMAGENTS-4655 | Align fragment handling cookie with Web Agent |

---

---
title: Getting support
description: Ping Identity provides support services, professional services, training, and partner services to assist you in setting up and maintaining your deployments. Find a general overview of these services at https://www.pingidentity.com.
component: java-agents
version: release-notes
page_id: java-agents::support
canonical_url: https://docs.pingidentity.com/java-agents/release-notes/support.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Getting support

Ping Identity provides support services, professional services, training, and partner services to assist you in setting up and maintaining your deployments. Find a general overview of these services at <https://www.pingidentity.com>.

Ping Identity has staff members around the globe who support our international customers and partners. For details on Ping Identity's support offering, visit <https://www.pingidentity.com/support>.

Ping Identity publishes comprehensive documentation online:

* The Ping Identity [Knowledge Base](https://support.pingidentity.com/s/knowledge-base) offers a large and increasing number of up-to-date, practical articles that help you deploy and manage Ping Advanced Identity Software software.

  While many articles are visible to everyone, Ping Identity customers have access to much more, including advanced information for customers using Ping Advanced Identity Software software in a mission-critical capacity.

* Ping Identity product documentation, such as this document, aims to be technically accurate and complete with respect to the software documented. It is visible to everyone and covers all product features and examples of how to use them.

---

---
title: Incompatible changes
description: Incompatible changes impact existing functionality and may affect your migration from a previous release. Before you upgrade, review these lists and make the appropriate changes to your scripts and plugins.
component: java-agents
version: release-notes
page_id: java-agents::changes
canonical_url: https://docs.pingidentity.com/java-agents/release-notes/changes.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Incompatible changes

Incompatible changes impact existing functionality and may affect your migration from a previous release. Before you upgrade, review these lists and make the appropriate changes to your scripts and plugins.

|   |                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------- |
|   | You can find information about previous versions that have reached End of Maintenance in the [Archive](archive.html). |

* [Changes in Java Agent 2026.x](changes-2026.html)

* [Changes in Java Agent 2025.x](changes-2025.html)

* [Changes in Java Agent 2024.x](changes-2024.html)

---

---
title: Known issues
description: "AMAGENTS-6258: Enforce Agent's Logback configuration isolation"
component: java-agents
version: release-notes
page_id: java-agents::archive-known-issues
canonical_url: https://docs.pingidentity.com/java-agents/release-notes/archive-known-issues.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  java_agent_2023_11: Java Agent 2023.11
  java_agent_2023_9: Java Agent 2023.9
  java_agent_2023_6: Java Agent 2023.6
  java_agent_2023_3: Java Agent 2023.3
  java_agent_5_10: Java Agent 5.10
---

# Known issues

## Java Agent 2023.11

| Issue                                                                          | Comment                    |
| ------------------------------------------------------------------------------ | -------------------------- |
| AMAGENTS-6258: Enforce Agent's Logback configuration isolation                 | Fixed in 2024.6, 2023.11.1 |
| AMAGENTS-6131: Tomcat Agent uninstall fails when done a second time            | Fixed in 2024.3, 2023.11.1 |
| AMAGENTS-6119: Menu for uninstall options has number 11 at start rather than 1 | Fixed in 2024.3            |
| AMAGENTS-6118: Install help has error in the output                            | Fixed in 2024.3            |
| AMAGENTS-6078: JPA does not remove the pre-authn cookie in all circumstances   | Won't fix                  |

## Java Agent 2023.9

| Issue                                                                          | Comment                    |
| ------------------------------------------------------------------------------ | -------------------------- |
| AMAGENTS-6131: Tomcat Agent uninstall fails when done a second time            | Fixed in 2024.3, 2023.11.1 |
| AMAGENTS-6119: Menu for uninstall options has number 11 at start rather than 1 | Fixed in 2024.3            |
| AMAGENTS-6118: Install help has error in the output                            | Fixed in 2024.3            |
| AMAGENTS-6078: JPA does not remove the pre-authn cookie in all circumstances   | Won't fix                  |

## Java Agent 2023.6

| Issue                                                                                                                 | Comment                  |
| --------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| AMAGENTS-5999: Cannot initialize logback when invoking classes in the agent SDK                                       | Fixed in 2023.9          |
| AMAGENTS-5928: Remove META-INF/services/javax.servlet.ServletContainerInitializer from the distribution               | Fixed in 2023.9          |
| AMAGENTS-5798: Oracle WebLogic admin console fails after patch upgrade                                                | Fixed in 2023.9          |
| AMAGENTS-4984:Setting samesite cookie to lax will cause the agent auth flow to fail if we are using different sites - | Duplicates AMAGENTS-5996 |
| AMAGENTS-3798: The AM Conditional Login URL should check that the entry has a \| in it                                | Fixed in 2023.9          |

## Java Agent 2023.3

| Issue                                                                                                                | Comment                  |
| -------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| AMAGENTS-5999: Cannot initialize logback when invoking classes in the agent SDK                                      | Fixed in 2023.9          |
| AMAGENTS-5928: Remove META-INF/services/javax.servlet.ServletContainerInitializer from the distribution              | Fixed in 2023.9          |
| AMAGENTS-5798: Oracle WebLogic admin console fails after patch upgrade                                               | Fixed in 2023.9          |
| AMAGENTS-5797: java.lang.NullPointerException in org.forgerock.agents.util.UrlParamNormaliser                        | Fixed in 2023.6          |
| AMAGENTS-5685: JPA: Address bug in cache thawing                                                                     | Fixed in 2023.6          |
| AMAGENTS-5654: Conditional login does not work in case when specific header should match any value                   | Fixed in 2023.6          |
| AMAGENTS-5631: Encrypt-in-place does not overwrite existing password                                                 | Fixed in 2023.6          |
| AMAGENTS-5602: Pathinfo stripping is only done for not-enforced rules                                                | Won't fix                |
| AMAGENTS-5601: NotEnforcedRuleHelper instantiates a metrics object, but never uses it.                               | Not a defect             |
| AMAGENTS-5600: Enabling pathinfo and using URL encoding raises exception                                             | Fixed in 2023.6          |
| AMAGENTS-4984: Setting samesite cookie to lax will cause the agent auth flow to fail if we are using different sites | Duplicates AMAGENTS-5996 |
| AMAGENTS-3798: The AM Conditional Login URL should check that the entry has a \| in it                               | Fixed in 2023.9          |

## Java Agent 5.10

| Issue                                                                                                                | Comment                  |
| -------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| AMAGENTS-5999: Can't initialize logback when invoking classes in the agent SDK                                       | Fixed in 2023.9          |
| AMAGENTS-5928: Remove META-INF/services/javax.servlet.ServletContainerInitializer from the distribution              | Fixed in 2023.9          |
| AMAGENTS-5590: JPA version is not set in config files                                                                | Fixed in 5.10.3          |
| AMAGENTS-5798: Oracle WebLogic admin console fails after patch upgrade                                               | Fixed in 2023.9          |
| AMAGENTS-4984: Setting samesite cookie to lax will cause the agent auth flow to fail if we are using different sites | Duplicates AMAGENTS-5996 |
| AMAGENTS-4816: The agent does not invalidate session before redirecting to logout                                    | Fixed in 2023.3, 5.10.1  |
| AMAGENTS-3798: The AM Conditional Login URL should check that the entry has a \| in it                               | Fixed in 2023.9          |
| AMAGENTS-3912: Avoid displaying a huge stacktrace to the user when the bootstrap properties file cannot be opened    | Fixed in 2023.3          |

---

---
title: Known issues
description: "AMAGENTS-6838: JPA will create a JWT cookie in SSO Token Acceptance mode"
component: java-agents
version: release-notes
page_id: java-agents::known-issues
canonical_url: https://docs.pingidentity.com/java-agents/release-notes/known-issues.html
llms_txt: https://docs.pingidentity.com/java-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  java_agent_2026_6: Java Agent 2026.6
  java_agent_2025_11: Java Agent 2025.11
  java_agent_2025_3: Java Agent 2025.3
  java_agent_2024_11: Java Agent 2024.11
  java_agent_2024_9: Java Agent 2024.9
  java_agent_2024_6: Java Agent 2024.6
  java_agent_2024_3: Java Agent 2024.3
---

# Known issues

## Java Agent 2026.6

| Issue                                                                                        | Comment    |
| -------------------------------------------------------------------------------------------- | ---------- |
| AMAGENTS-6838: JPA will create a JWT cookie in SSO Token Acceptance mode                     | Unresolved |
| AMAGENTS-6603: JPA: Change all file access to use UTF-8, in JPA itself, and in the installer | Unresolved |

## Java Agent 2025.11

| Issue                                                                                        | Comment    |
| -------------------------------------------------------------------------------------------- | ---------- |
| AMAGENTS-6838: JPA will create a JWT cookie in SSO Token Acceptance mode                     | Unresolved |
| AMAGENTS-6603: JPA: Change all file access to use UTF-8, in JPA itself, and in the installer | Unresolved |

## Java Agent 2025.3

| Issue                                                                                        | Comment          |
| -------------------------------------------------------------------------------------------- | ---------------- |
| AMAGENTS-6838: JPA will create a JWT cookie in SSO Token Acceptance mode                     | Unresolved       |
| AMAGENTS-6615: agentadmin option "--getEncryptKey" doesn't work on Windows                   | Fixed in 2025.11 |
| AMAGENTS-6603: JPA: Change all file access to use UTF-8, in JPA itself, and in the installer | Unresolved       |

## Java Agent 2024.11

| Issue                                                                                        | Comment          |
| -------------------------------------------------------------------------------------------- | ---------------- |
| AMAGENTS-6838: JPA will create a JWT cookie in SSO Token Acceptance mode                     | Unresolved       |
| AMAGENTS-6809: Monitoring endpoint doesn't work for Jakarta builds                           | Fixed in 2025.3  |
| AMAGENTS-6615: agentadmin option "--getEncryptKey" doesn't work on Windows                   | Fixed in 2025.11 |
| AMAGENTS-6603: JPA: Change all file access to use UTF-8, in JPA itself, and in the installer | Unresolved       |

## Java Agent 2024.9

| Issue                                                                                        | Comment          |
| -------------------------------------------------------------------------------------------- | ---------------- |
| AMAGENTS-6838: JPA will create a JWT cookie in SSO Token Acceptance mode                     | Unresolved       |
| AMAGENTS-6809: Monitoring endpoint doesn't work for Jakarta builds                           | Fixed in 2025.3  |
| AMAGENTS-6615: agentadmin option "--getEncryptKey" doesn't work on Windows                   | Fixed in 2025.11 |
| AMAGENTS-6603: JPA: Change all file access to use UTF-8, in JPA itself, and in the installer | Unresolved       |

## Java Agent 2024.6

| Issue                                                                                                               | Comment          |
| ------------------------------------------------------------------------------------------------------------------- | ---------------- |
| AMAGENTS-6615: agentadmin option "--getEncryptKey" doesn't work on Windows                                          | Fixed in 2025.11 |
| AMAGENTS-6612: Java Agent in accept SSO token mode with custom login false writes JWT tokens to iPlanetDirectoryPro | Fixed in 2024.9  |
| AMAGENTS-6603: JPA: Change all file access to use UTF-8, in JPA itself, and in the installer                        | Unresolved       |

## Java Agent 2024.3

| Issue                                                                        | Comment                    |
| ---------------------------------------------------------------------------- | -------------------------- |
| AMAGENTS-6258: Enforce Agent's Logback configuration isolation               | Fixed in 2024.6, 2023.11.1 |
| AMAGENTS-6078: JPA does not remove the pre-authn cookie in all circumstances | Won't fix                  |