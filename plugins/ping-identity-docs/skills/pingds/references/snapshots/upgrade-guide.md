---
title: About upgrades
description: Overview of PingDS upgrade scope, supported upgrade paths from DS 6 and later, and steps to activate new features after upgrading.
component: pingds
version: 8.1
page_id: pingds:upgrade-guide:about-upgrades
canonical_url: https://docs.pingidentity.com/pingds/8.1/upgrade-guide/about-upgrades.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Compatibility", "LDAP", "Replication", "Upgrade"]
section_ids:
  upgrade-features: Activate new features after upgrade
  upgrade-paths: Supported upgrades
---

# About upgrades

This documentation explains how to upgrade PingDS software. It doesn't cover upgrading DS client applications or changing the directory service schema or configuration. Keep those operations separate from the DS software upgrade.

|   |                                                                                                                                                                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This documentation assumes you:- Are upgrading from DS 7 or later.

- Performed all the recommended upgrade procedures when moving to the currently deployed version, including the "After you upgrade" procedures.If not, begin with the [upgrade documentation for DS 7.5](https://docs.pingidentity.com/pingds/7.5/upgrade-guide/preface.html). |

## Activate new features after upgrade

When you upgrade DS in place, the upgrade process preserves the existing configuration as much as possible. This maintains compatibility, but you do not have access to all new features immediately after upgrade.

You must take additional steps to complete the process, including activating new features.

## Supported upgrades

| From…​                                         | To…​                                                                        | Important Notes                                                                                                                                                                        |
| ---------------------------------------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Official DS release, version 6.0 or later      | Official DS release, same edition of directory server or replication server | Supported.                                                                                                                                                                             |
| Official ForgeRock release, 2.6.x to 5.5.x     | Official DS release, directory server or replication server                 | Not supported.1                                                                                                                                                                        |
| Official ForgeRock release, version 2.4 or 2.5 | Official DS release, directory server or replication server                 | Not supported.2                                                                                                                                                                        |
| Evaluation release                             | Official DS release                                                         | Not supported.The evaluation version includes an additional server plugin and configuration. Official releases do not have an upgrade task to remove the plugin and its configuration. |
| Unofficial build                               | Official DS release                                                         | Not supported.                                                                                                                                                                         |

1 Workaround: First upgrade to DS 6.5, then to DS 7.5.

2 Workaround: First upgrade to OpenDJ 2.6, then to DS 6.5, then to DS 7.5.
