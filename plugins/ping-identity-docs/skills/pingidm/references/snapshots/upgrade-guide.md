---
title: About upgrades
description: Overview of the manual PingIDM upgrade process, including supported upgrade paths, installation, configuration migration, and repository updates
component: pingidm
version: 8.1
page_id: pingidm:upgrade-guide:about-upgrades
canonical_url: https://docs.pingidentity.com/pingidm/8.1/upgrade-guide/about-upgrades.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Upgrade", "Migration"]
section_ids:
  supported-upgrade-paths: Supported upgrade paths
---

# About upgrades

The automated update process available with previous IDM versions is no longer supported. This chapter describes the manual process required to upgrade an existing IDM deployment. At a high level, the manual update process involves the following steps:

1. Install IDM 8.1.

2. Migrate your existing IDM configuration to the new installation.

3. Update your repository.

4. Test your scripts and customizations work as expected.

5. Migrate existing data to the new installation.

## Supported upgrade paths

The following table contains information about the supported upgrade paths to IDM 8.1:

**Upgrade Paths**

| Version   | Upgrade Supported to IDM 8.1 |
| --------- | ---------------------------- |
| IDM 8.0.x | YES                          |
| IDM 7.5.x | YES                          |
| IDM 7.4.x | YES                          |
| IDM 7.3.x | YES                          |
| IDM 7.2.x | YES                          |
| IDM 7.1.x | YES                          |
| IDM 7.0.x | YES                          |
| IDM 6.5.x | YES                          |
| IDM 6.0.x | YES                          |
| IDM 5.5.x | YES                          |
| IDM 5.0.x | YES                          |

|   |                                                                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Depending on how you have customized your deployment, there might be incompatible configuration changes when you upgrade from versions prior to IDM 6.5.x. Read the upgrade documentation for each interim release and apply all required script and configuration changes. |
