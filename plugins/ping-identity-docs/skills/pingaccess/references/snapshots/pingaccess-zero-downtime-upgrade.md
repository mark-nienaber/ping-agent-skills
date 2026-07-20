---
title: Adding the engine to the load balancer configuration
description: Add the engine back to the load balancer configuration. Since this step is dependent on your environment, no specific instruction will be provided.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_zero_downtime_upgrade:pa_adding_the_engine_to_the_load_balancer_configuration
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_zero_downtime_upgrade/pa_adding_the_engine_to_the_load_balancer_configuration.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  next-steps: Next steps
---

# Adding the engine to the load balancer configuration

Add the engine back to the load balancer configuration. Since this step is dependent on your environment, no specific instruction will be provided.

## Before you begin

You must be familiar with the steps required to add the engine back to the load balancer configuration.

After you confirm that the engine has been successfully added to the load balancer and is reporting properly to PingAccess, you can begin the upgrade process on additional engines.

![Flowchart showing a deployment as an upgraded node is returned to the load balancer configuration.](_images/hog1564006857251.png)

In the previous flowchart:

1. A user with a WebSession Cookie sends a request to the load balancer.

2. The load balancer directs the request to one of the three engine nodes. The first engine node is using the target version of PingAccess, and it has been added to the load balancer configuration.

3. The administrative node is using the target version of PingAccess.

## Steps

1. To add the engine to the load balancer configuration, reverse the steps you took in [Removing the engine from the load balancer configuration](pa_removing_the_engine_from_the_load_balancer_configuration.html) to remove the engine.

2. Restart the load balancer.

## Next steps

Repeat the [Upgrading engines](pa_upgrading_engines.html) process until each engine has been upgraded. When all engines have been upgraded, added to the load balancer configuration, and are reporting to PingAccess, you can move on to the final step, [Enable key rolling](pa_enabling_key_rolling.html), to complete the zero downtime upgrade process.

---

---
title: Disabling key rolling
description: Disable key rolling to prevent active sessions from being invalidated during the upgrade process. This is a temporary modification, and you will reenable key rolling at the end of the upgrade process.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_zero_downtime_upgrade:pa_disabling_key_rolling
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_zero_downtime_upgrade/pa_disabling_key_rolling.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  next-steps: Next steps
---

# Disabling key rolling

Disable key rolling to prevent active sessions from being invalidated during the upgrade process. This is a temporary modification, and you will reenable key rolling at the end of the upgrade process.

There are different procedures at this stage depending on the source version of PingAccess. The following flowchart gives an example.

![Flowchart showing a deployment as key rolling is disabled.](_images/pix1564006855117.png)

In this flowchart:

1. A user with a WebSession Cookie sends a request to the load balancer.

2. The load balancer directs the request to one of three engine nodes, which are all still using the source version of PingAccess.

3. At the Admin node, key rolling has been paused.

## Next steps

* [Disabling key rolling in PingAccess 6.0 or later](pa_disabling_key_rolling_in_pa_60_or_later.html)

* [Disabling key rolling in PingAccess 5.2 or 5.3](pa_disabling_key_rolling_in_pa_52_or_53.html)

* [Disabling key rolling in PingAccess 5.0 or 5.1](pa_disabling_key_rolling_in_pa_50_or_51.html)

* [Disabling key rolling in PingAccess 4.3 or earlier](pa_disabling_key_rolling_in_pa_43_or_earlier.html)

Next, you will [upgrade the Admin node](pa_upgrading_the_admin_node.html).

---

---
title: Disabling key rolling in PingAccess 4.3 or earlier
description: If the source is a version of PingAccess earlier than 5.0, you can set the key rolling interval to a value that allows enough time for the upgrade to be completed successfully.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_zero_downtime_upgrade:pa_disabling_key_rolling_in_pa_43_or_earlier
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_zero_downtime_upgrade/pa_disabling_key_rolling_in_pa_43_or_earlier.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 17, 2024
section_ids:
  steps: Steps
  next-steps: Next steps
---

# Disabling key rolling in PingAccess 4.3 or earlier

If the source is a version of PingAccess earlier than 5.0, you can set the key rolling interval to a value that allows enough time for the upgrade to be completed successfully.

## Steps

1. Go to **Settings → Access → Identity Mappings**.

2. In the **Auth Token Management** section, specify a **Key Roll Interval** of 240 (10 days).

3. Click **Save**.

4. Go to **Settings → Access → Web Sessions**.

5. In the **Web Session Management** section, specify a **Key Roll interval** of 240 (10 days).

6. Click **Save**.

## Next steps

Next, you will [upgrade the Admin node](pa_upgrading_the_admin_node.html).

---

---
title: Disabling key rolling in PingAccess 5.0 or 5.1
description: If the source is PingAccess 5.0 or 5.1, you can disable key rolling.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_zero_downtime_upgrade:pa_disabling_key_rolling_in_pa_50_or_51
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_zero_downtime_upgrade/pa_disabling_key_rolling_in_pa_50_or_51.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 17, 2024
section_ids:
  steps: Steps
  next-steps: Next steps
---

# Disabling key rolling in PingAccess 5.0 or 5.1

If the source is PingAccess 5.0 or 5.1, you can disable key rolling.

## Steps

1. Go to **Settings → Access → Identity Mappings**.

2. In the **Auth Token Management** section, deselect **Key Roll Enabled**.

3. Click **Save**.

4. Go to **Settings → Access → Web Sessions**.

5. In the **Web Session Management** section, deselect **Key Roll Enabled**.

6. Click **Save**.

## Next steps

Next, you will [upgrade the Admin node](pa_upgrading_the_admin_node.html).

---

---
title: Disabling key rolling in PingAccess 5.2 or 5.3
description: If the source is PingAccess 5.2 or 5.3, you can disable key rolling.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_zero_downtime_upgrade:pa_disabling_key_rolling_in_pa_52_or_53
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_zero_downtime_upgrade/pa_disabling_key_rolling_in_pa_52_or_53.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 17, 2024
section_ids:
  steps: Steps
  next-steps: Next steps
---

# Disabling key rolling in PingAccess 5.2 or 5.3

If the source is PingAccess 5.2 or 5.3, you can disable key rolling.

## Steps

1. Go to **Settings → Access → Identity Mappings**.

2. In the **Auth Token Management** section, deselect **Key Roll Enabled**.

3. Click **Save**.

4. Go to **Settings → Access → Web Sessions**.

5. In the **Web Session Management** section, deselect **Key Roll Enabled**.

6. Click **Save**.

7. Go to **Settings → System → Token Validation**.

8. In the **OAuth Key Management** section, deselect **Key Roll Enabled**.

9. Click **Save**.

## Next steps

Next, you will [upgrade the Admin node](pa_upgrading_the_admin_node.html).

---

---
title: Disabling key rolling in PingAccess 6.0 or later
description: If the source is PingAccess 6.0 or later, you can disable key rolling.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_zero_downtime_upgrade:pa_disabling_key_rolling_in_pa_60_or_later
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_zero_downtime_upgrade/pa_disabling_key_rolling_in_pa_60_or_later.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 17, 2024
section_ids:
  steps: Steps
  next-steps: Next steps
---

# Disabling key rolling in PingAccess 6.0 or later

If the source is PingAccess 6.0 or later, you can disable key rolling.

## Steps

1. Click **Access**, then go to **Identity Mappings > Auth Token Management**.

2. In the **Auth Token Management** section, deselect **Key Roll Enabled**.

3. Click **Save**.

4. Click **Access**, then go to **Web Sessions > Web Session Management**.

5. In the **Web Session Management** section, deselect **Key Roll Enabled**.

6. Click **Save**.

7. Click **Access**, then go to **Token Validation > OAuth Key Management**.

8. In the **OAuth Key Management** section, deselect **Key Roll Enabled**.

9. Click **Save**.

## Next steps

Next, you will [upgrade the Admin node](pa_upgrading_the_admin_node.html).

---

---
title: Enabling key rolling
description: Resume key rolling.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_zero_downtime_upgrade:pa_enabling_key_rolling
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_zero_downtime_upgrade/pa_enabling_key_rolling.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Enabling key rolling

Resume key rolling.

## About this task

![Flowchart showing a deployment as key rolling is resumed.](_images/jqq1564006857998.png)

In the previous flowchart:

1. A user with a WebSession Cookie sends a request to the load balancer.

2. The load balancer directs the request to one of the three upgraded engine nodes. The engine nodes are all using the target version of PingAccess.

3. The administrative node is using the target version of PingAccess.

## Steps

1. Click **Access**, then go to **Identity Mappings > Auth Token Management**.

2. In the **Auth Token Management** section, select the **Key Roll Enabled** check box.

3. Verify that the **Key Roll Interval (H)** is correct, then click **Save**.

4. Click **Access**, then go to **Web Sessions > Web Session Management**.

5. In the **Web Session Management** section, select the **Key Roll Enabled** check box.

6. Verify that the **Key Roll Interval (H)** is correct, then click **Save**.

7. Click **Access**, then go to **Token Validation > OAuth Key Management**.

8. In the **OAuth Key Management** section, select the **Key Roll Enabled** check box.

9. Verify that the **Key Roll Interval (H)** is correct, then click **Save**.

---

---
title: PingAccess zero downtime upgrade
description: A zero downtime upgrade allows you to upgrade your clustered PingAccess environment to the latest version with no impact to resource availability or existing user sessions.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_zero_downtime_upgrade:pa_zero_downtime_upgrade
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_zero_downtime_upgrade/pa_zero_downtime_upgrade.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
---

# PingAccess zero downtime upgrade

A zero downtime upgrade allows you to upgrade your clustered PingAccess environment to the latest version with no impact to resource availability or existing user sessions.

Though this procedure is applicable to any PingAccess cluster upgrade to version 5.0 or later, there are minor variations depending on your PingAccess source version. Those variations are clearly described where applicable.

|   |                                                                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Some steps, particularly those related to working with a load balancer, are dependent on your environment. It is expected that you are familiar with the tasks required by these steps. This document does not offer detailed instruction on performing these tasks. |

You can upgrade from any version using the upgrade utility, or you can upgrade from version 6.1 to the latest maintenance release using the incremental update bundle. This procedure includes the steps for both methods.

|   |                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | To achieve a successful upgrade, perform the tasks in this document in the order that they are presented. Deviation from these tasks might result in a failed upgrade, system downtime, or both. |

|   |                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------- |
|   | If you are using PingAccess 3.2 or earlier, you must upgrade to PingAccess 4.3 or 5.3 before upgrading to PingAccess 6.1. |

Before you begin, review the [Upgrade considerations](../upgrading_pingaccess/pa_upgrade_considerations.html).

To begin the upgrade process, disable key rolling to prevent active sessions from being invalidated. For more information, see [Disabling key rolling](pa_disabling_key_rolling.html).

---

---
title: Recovering from a failed upgrade
description: You can recover your PingAccess cluster by switching back to the source version if the upgrade fails.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_zero_downtime_upgrade:pa_recovering_from_a_failed_upgrade
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_zero_downtime_upgrade/pa_recovering_from_a_failed_upgrade.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Recovering from a failed upgrade

You can recover your PingAccess cluster by switching back to the source version if the upgrade fails.

## About this task

The zero downtime upgrade process creates a set of new folders for the upgraded installation. The pre-upgrade source installation is not affected.

To recover your PingAccess cluster in the event of a failure, you would resume the former installation using these steps.

## Steps

1. Stop any upgraded PingAccess instances.

2. Start the original PingAccess instance on the admin node.

3. Import the engine definitions back into the original PingAccess instance.

4. Start the original PingAccess instances on the engine nodes.

5. Ensure all engines are added to the load balancer configuration.

---

---
title: Removing the engine from the load balancer configuration
description: Remove the engine from the load balancer configuration. Because this step is dependent on your environment, no specific instruction will be provided.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_zero_downtime_upgrade:pa_removing_the_engine_from_the_load_balancer_configuration
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_zero_downtime_upgrade/pa_removing_the_engine_from_the_load_balancer_configuration.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 8, 2024
section_ids:
  before-you-begin: Before you begin
  steps: Steps
---

# Removing the engine from the load balancer configuration

Remove the engine from the load balancer configuration. Because this step is dependent on your environment, no specific instruction will be provided.

## Before you begin

You must be familiar with the steps required to temporarily remove the engine from your load balancer configuration.

|   |                                                                                                                                                                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To maintain resource availability, you should remove only the engine you are upgrading. After the upgrade is complete, add the engine back to the load balancer configuration. Only after you confirm that the engine has been successfully added to the load balancer and is reporting properly to PingAccess should you begin the upgrade process on additional engines. |

The following flowchart demonstrates engine removal.

![Flowchart showing a deployment as an engine is removed from the load balancer.](_images/qht1564006856570.png)

In the previous flowchart:

1. A user with a WebSession Cookie sends a request to the load balancer.

2. The load balancer directs the request to one of the other two engine nodes. All of the engine nodes are still using the source version of PingAccess.

3. The administrative node is using the target version of PingAccess.

## Steps

1. Identify and note the engine you want to upgrade. Ensure you have the engine definition for this engine available.

2. Remove the engine from the load balancer.

   |   |                                                                                                                                                                                                             |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Keep a record of the changes you make so that you can reverse this operation later in [Adding the engine to the load balancer configuration](pa_adding_the_engine_to_the_load_balancer_configuration.html). |

3. Restart the load balancer.

---

---
title: Resuming configuration replication
description: Resume the configuration replication that was disabled by the Upgrade Utility. Perform this step for all engine nodes in the cluster.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_zero_downtime_upgrade:pa_resuming_configuration_replication
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_zero_downtime_upgrade/pa_resuming_configuration_replication.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  example: Example:
  result: Result:
---

# Resuming configuration replication

Resume the configuration replication that was disabled by the Upgrade Utility. Perform this step for all engine nodes in the cluster.

## About this task

You will use the PingAccess Admin API to GET and PUT the relevant configuration data for each of these items.

![Flowchart showing a deployment as configuration replication is resumed.](_images/rxs1564006860388.png)

In the previous flowchart:

1. A user with a WebSession Cookie sends a request to the load balancer.

2. The load balancer directs the request to one of the un-upgraded engine nodes. The first engine node is using the target version of PingAccess, and its connection to the administrative node is resuming.

3. The administrative node is using the target version of PingAccess.

|   |                                                             |
| - | ----------------------------------------------------------- |
|   | Perform the following steps for each engine in the cluster. |

To resume configuration replication:

## Steps

1. In a browser, go to https\://*\<host>*:*\<admin-port>*/pa-admin-api/v3/api-docs/.

   ### Example:

   https\://localhost:9000/pa-admin-api/v3/api-docs/

2. For engines, expand the **/engines** endpoint.

3. Click the **GET /engines** operation.

4. Click **Try it out!** and note the engine id for each engine.

5. Click the **GET /engines/{id}** operation.

6. In the **ID** field, enter the id of the engine you want to update and click **Try it out!**

7. Copy the entire Response Body.

8. Click the **PUT /engines/{id}** operation and enter the id of the engine you want to update.

9. In the **Engine** field, paste the response body you copied and change `"configReplicationEnabled"` to `true`.

10. Click **Try it out!**

    ### Result:

    If the operation is successful, you will receive a response code of `200`.

11. Start the node.

12. Repeat the previous steps for each node.

13. Click **Settings**, then go to **Clustering > Engines**.

14. Ensure the engines are displayed and reporting. A healthy engine shows a green status indicator.

    |   |                                                                                                                                                                                                 |
    | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | There might be a delay in bringing the engine to a running status. If the engine does not immediately show as reporting, refresh the page until the engine status indicator is green (running). |

![This flowchart shows a deployment after configuration replication has resumed.](_images/svh1564006861224.png)

In the previous flowchart:

1. A user with a WebSession Cookie sends a request to the load balancer.

2. The load balancer directs the request to one of the un-upgraded engine nodes. The first engine node is using the target version of PingAccess, and its connection to the administrative node has resumed.

3. The administrative node is using the target version of PingAccess.

---

---
title: Upgrading engines
description: This phase of the zero downtime upgrade focuses on upgrading each engine in the cluster. To maintain resource availability, perform this set of steps on one engine at a time until all engines are successfully upgraded.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_zero_downtime_upgrade:pa_upgrading_engines
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_zero_downtime_upgrade/pa_upgrading_engines.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  removing-the-engine-from-the-load-balancer-configuration: Removing the engine from the load balancer configuration
  before-you-begin: Before you begin
  steps: Steps
  upgrading-the-engine: Upgrading the engine
  before-you-begin-2: Before you begin
  about-this-task: About this task
  steps-2: Steps
  example: Example:
  choose-from: Choose from:
  example-2: Example:
  next-steps: Next steps
  resuming-configuration-replication: Resuming configuration replication
  about-this-task-2: About this task
  steps-3: Steps
  example-3: Example:
  result: Result:
  adding-the-engine-to-the-load-balancer-configuration: Adding the engine to the load balancer configuration
  before-you-begin-3: Before you begin
  steps-4: Steps
  next-steps-2: Next steps
---

# Upgrading engines

This phase of the zero downtime upgrade focuses on upgrading each engine in the cluster. To maintain resource availability, perform this set of steps on one engine at a time until all engines are successfully upgraded.

|   |                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Engines are identified by the engine name. Ensure that the engine that you remove from the load balancer aligns with the engine definition you import. |

This phase requires that the following steps take place for each engine in the cluster, one at a time:

* [Remove the engine from the load balancer](pa_removing_the_engine_from_the_load_balancer_configuration.html)

* [Upgrade the engine](pa_upgrading_the_engine.html)

* [Resuming configuration replication](pa_resuming_configuration_replication.html)

* [Add the engine to the load balancer](pa_adding_the_engine_to_the_load_balancer_configuration.html)

|   |                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Do not begin the upgrade of an additional engine until the active engine upgrade is completed and the engine is reporting to the PingAccess administrative node. |

## Removing the engine from the load balancer configuration

Remove the engine from the load balancer configuration. Because this step is dependent on your environment, no specific instruction will be provided.

### Before you begin

You must be familiar with the steps required to temporarily remove the engine from your load balancer configuration.

|   |                                                                                                                                                                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To maintain resource availability, you should remove only the engine you are upgrading. After the upgrade is complete, add the engine back to the load balancer configuration. Only after you confirm that the engine has been successfully added to the load balancer and is reporting properly to PingAccess should you begin the upgrade process on additional engines. |

The following flowchart demonstrates engine removal.

![Flowchart showing a deployment as an engine is removed from the load balancer.](_images/qht1564006856570.png)

In the previous flowchart:

1. A user with a WebSession Cookie sends a request to the load balancer.

2. The load balancer directs the request to one of the other two engine nodes. All of the engine nodes are still using the source version of PingAccess.

3. The administrative node is using the target version of PingAccess.

### Steps

1. Identify and note the engine you want to upgrade. Ensure you have the engine definition for this engine available.

2. Remove the engine from the load balancer.

   |   |                                                                                                                                                                                                             |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Keep a record of the changes you make so that you can reverse this operation later in [Adding the engine to the load balancer configuration](pa_adding_the_engine_to_the_load_balancer_configuration.html). |

3. Restart the load balancer.

## Upgrading the engine

Use the PingAccess Upgrade Utility to upgrade the engine.

### Before you begin

For more information on upgrading PingAccess, see [Upgrade PingAccess](../upgrading_pingaccess/pa_upgrading_pa_landing_topic.html). The following flowchart displays an example engine upgrade.

![Flowchart showing a deployment as the engine is upgraded.](_images/pgc1564006859458.png)

In this flowchart:

1. A user with a WebSession Cookie sends a request to the load balancer.

2. The load balancer directs the request to one of the un-upgraded engine nodes. The first engine node is using the target version of PingAccess, while the other engine nodes are still using the source version of PingAccess.

3. The administrative node is using the target version of PingAccess.

Before beginning the upgrade process, make sure you have:

* Ensured the PingAccess engine is running

* Downloaded the PingAccess [distribution](https://www.pingidentity.com/en/resources/downloads/pingaccess.html) `.zip` file or the incremental update bundle and extracted it.

* The PingAccess license

### About this task

Any warnings or errors encountered are recorded in `log/upgrade.log`, as well as on the screen while the utility is running. The upgrade uses an exit code of `0` to indicate a successful upgrade and an exit code of `1` to indicate failure.

### Steps

1. If you are using the upgrade utility, change to the new version's `/upgrade/bin` directory on the command line.

   #### Example:

   ```
   cd /pingaccess-6.1.0/upgrade/bin
   ```

2. Upgrade the system:

   #### Choose from:

   * If you are using the upgrade utility on a Windows system, use this command: `upgrade.bat <admin_port>] <directory>] <jvm_memory_options_file>] <newPingAccessLicense>] [-s \| --silent] <sourcePingAccessRootDir>`.

     For example:

     ```
     upgrade.bat ../pingaccess-5.3.0
     ```

   * If you are using the upgrade utility on a Linux system, use this command: `./upgrade.sh <admin_port>] <directory>] <jvm_memory_options_file>] <newPingAccessLicense>] [-s \| --silent] <sourcePingAccessRootDir>`.

     For example:

     ```
     ./upgrade.sh ../pingaccess-5.3.0
     ```

   * If you are using the incremental update package, open the `ReadMeFirst.txt` file and make the file changes specified in the readme.

     The command-line parameters are the same regardless of the platform, and are defined as follows:

     **Parameter definitions**

     | Parameter                         | Value description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
     | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
     | -p <*admin\_port*>                | Optional port to be used by the temporary PingAccess instance run during the upgrade. The default is `9001`.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
     | -i <*directory*>                  | An optional directory containing additional library JAR files (for example, plugins, JDBC drivers) to be copied into the target installation.Beginning in version 6.0, JAR files are stored in the `<PA_HOME>/deploy` folder.During an upgrade from versions earlier than 6.0, third-party JAR files are migrated from the `lib` folder to the `deploy` folder if no directory is specified.During an upgrade from version 6.0 or later, the contents of the `deploy` folder are migrated to the new `<PA_HOME>/deploy` folder if no directory is specified. |
     | <*sourcePingAccessRootDir*>       | The PA\_HOME for the source PingAccess version.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
     | -l <*newPingAccessLicense*>       | An optional path to the PingAccess license file to use for the target version. If not specified, the existing license is reused.                                                                                                                                                                                                                                                                                                                                                                                                                             |
     | -j <*jvm\_memory\_options\_file*> | An optional path to a file with Java Virtual Machine (JVM) *(tooltip: \<div class="paragraph">&#xA;\<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>&#xA;\</div>)* memory options to use for the new PingAccess instance during the upgrade.                                                                                                                                                                                                                                           |
     | -s \| --silent                    | Run the upgrade with no user input required. To use this option, specify the source version's credentials using environment variables.                                                                                                                                                                                                                                                                                                                                                                                                                       |

     **Environment Variables**

     You can specify the username and password for the source version using these environment variables:

     | Environment variable     | Description                                                                                                                                                                                                                                                                                   |
     | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     | `PA_SOURCE_API_USERNAME` | The username for the source version's Admin application programming interface (API) *(tooltip: \<div class="paragraph">&#xA;\<p>A specification of interactions available for building software to access an application or service.\</p>&#xA;\</div>)*. This should be set to Administrator. |
     | `PA_SOURCE_API_PASSWORD` | The basic authorization password for the Administrator in the source version's Admin API.                                                                                                                                                                                                     |

     **JVM Memory options**

     These options can be included in the JVM memory options file. Memory amounts use `m` or `g` to specify the unit.

     | Memory option             | Description                                                   |
     | ------------------------- | ------------------------------------------------------------- |
     | `-Xms<amount>`            | Minimum heap size.                                            |
     | `-Xmx<amount>`            | Maximum heap size.                                            |
     | `-XX:NewSize=<amount>`    | Minimum size for the Young Gen space.                         |
     | `-XX:MaxNewSize=<amount>` | Maximum size for the Young Gen space.                         |
     | `-XX:+UseParallelGC`      | Specifies that the parallel garbage collector should be used. |

     #### Example:

     ```
     #Sample JVM Memory options file
     -Xms512m
     -Xmx1g
     -XX:NewSize=256m
     -XX:MaxNewSize=512m
     -XX:+UseParallelGC
     ```

     You can copy the existing `PA_HOME/conf/jvm-memory.options` file to create a JVM memory options file for the upgrade.

3. Stop the existing PingAccess instance. Do not start the new instance.

### Next steps

|   |                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If PingAccess is running as a service and you upgraded using the upgrade utility:- In Linux, update `PA_HOME` in `/etc/systemd/system/pingaccess.service` to point to the new installation.

- In Windows, remove the existing PingAccess service (`<OLD_PA_HOME>\sbin\Windows\uninstall-service.bat`) and add the new service (`<NEW_PA_HOME>\sbin\Windows\install-service.bat`). |

## Resuming configuration replication

Resume the configuration replication that was disabled by the Upgrade Utility. Perform this step for all engine nodes in the cluster.

### About this task

You will use the PingAccess Admin API to GET and PUT the relevant configuration data for each of these items.

![Flowchart showing a deployment as configuration replication is resumed.](_images/rxs1564006860388.png)

In the previous flowchart:

1. A user with a WebSession Cookie sends a request to the load balancer.

2. The load balancer directs the request to one of the un-upgraded engine nodes. The first engine node is using the target version of PingAccess, and its connection to the administrative node is resuming.

3. The administrative node is using the target version of PingAccess.

|   |                                                             |
| - | ----------------------------------------------------------- |
|   | Perform the following steps for each engine in the cluster. |

To resume configuration replication:

### Steps

1. In a browser, go to https\://*\<host>*:*\<admin-port>*/pa-admin-api/v3/api-docs/.

   #### Example:

   https\://localhost:9000/pa-admin-api/v3/api-docs/

2. For engines, expand the **/engines** endpoint.

3. Click the **GET /engines** operation.

4. Click **Try it out!** and note the engine id for each engine.

5. Click the **GET /engines/{id}** operation.

6. In the **ID** field, enter the id of the engine you want to update and click **Try it out!**

7. Copy the entire Response Body.

8. Click the **PUT /engines/{id}** operation and enter the id of the engine you want to update.

9. In the **Engine** field, paste the response body you copied and change `"configReplicationEnabled"` to `true`.

10. Click **Try it out!**

    #### Result:

    If the operation is successful, you will receive a response code of `200`.

11. Start the node.

12. Repeat the previous steps for each node.

13. Click **Settings**, then go to **Clustering > Engines**.

14. Ensure the engines are displayed and reporting. A healthy engine shows a green status indicator.

    |   |                                                                                                                                                                                                 |
    | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | There might be a delay in bringing the engine to a running status. If the engine does not immediately show as reporting, refresh the page until the engine status indicator is green (running). |

![This flowchart shows a deployment after configuration replication has resumed.](_images/svh1564006861224.png)

In the previous flowchart:

1. A user with a WebSession Cookie sends a request to the load balancer.

2. The load balancer directs the request to one of the un-upgraded engine nodes. The first engine node is using the target version of PingAccess, and its connection to the administrative node has resumed.

3. The administrative node is using the target version of PingAccess.

## Adding the engine to the load balancer configuration

Add the engine back to the load balancer configuration. Since this step is dependent on your environment, no specific instruction will be provided.

### Before you begin

You must be familiar with the steps required to add the engine back to the load balancer configuration.

After you confirm that the engine has been successfully added to the load balancer and is reporting properly to PingAccess, you can begin the upgrade process on additional engines.

![Flowchart showing a deployment as an upgraded node is returned to the load balancer configuration.](_images/hog1564006857251.png)

In the previous flowchart:

1. A user with a WebSession Cookie sends a request to the load balancer.

2. The load balancer directs the request to one of the three engine nodes. The first engine node is using the target version of PingAccess, and it has been added to the load balancer configuration.

3. The administrative node is using the target version of PingAccess.

### Steps

1. To add the engine to the load balancer configuration, reverse the steps you took in [Removing the engine from the load balancer configuration](pa_removing_the_engine_from_the_load_balancer_configuration.html) to remove the engine.

2. Restart the load balancer.

### Next steps

Repeat the [Upgrading engines](pa_upgrading_engines.html) process until each engine has been upgraded. When all engines have been upgraded, added to the load balancer configuration, and are reporting to PingAccess, you can move on to the final step, [Enable key rolling](pa_enabling_key_rolling.html), to complete the zero downtime upgrade process.

---

---
title: Upgrading the administrative node
description: Upgrade the PingAccess administrative node using the PingAccess Upgrade Utility. You will use the -r switch to disable configuration replication on the target version.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_zero_downtime_upgrade:pa_upgrading_the_admin_node
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_zero_downtime_upgrade/pa_upgrading_the_admin_node.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 27, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  example: Example:
  result: Result:
  example-2: Example:
  result-2: Result:
  choose-from: Choose from:
  next-steps: Next steps
---

# Upgrading the administrative node

Upgrade the PingAccess administrative node using the PingAccess Upgrade Utility. You will use the `-r` switch to disable configuration replication on the target version.

## Before you begin

For more information on upgrading PingAccess, see [Upgrading PingAccess](../upgrading_pingaccess/pa_upgrading_pa_landing_topic.html).

![This flowchart shows a deployment as the administrative node is upgraded.](_images/zil1564006855826.png)

In the previous flowchart:

1. A user with a WebSession Cookie sends a request to the load balancer.

2. The load balancer directs the request to one of three engine nodes, which are all using the source version of PingAccess

3. The administrative node is using the target version of PingAccess.

Before beginning the upgrade process, make sure you have:

* Ensured PingAccess is running

* Downloaded the PingAccess [distribution](https://www.pingidentity.com/en/resources/downloads/pingaccess.html) `.zip` file or the incremental update bundle and extracted it.

* The PingAccess license, if you are switching to a new license file

* Administrator credentials

* Basic Authentication enabled

## About this task

Any warnings or errors encountered are recorded in `log/upgrade.log`, as well as on the screen while the utility is running. The upgrade uses an exit code of `0` to indicate a successful upgrade and an exit code of `1` to indicate failure.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you are upgrading from version 4.3 or earlier, and your installation uses custom plugins, they will need to be rebuilt against the new (5.0) Software Development Kit (SDK) *(tooltip: \<div class="paragraph">&#xA;\<p>A set of tools that allows a developer to build a custom application that integrates with or connects to a platform or service.\</p>&#xA;\</div>)*. You will then run the upgrade utility manually with the new `-i` command-line option to specify a directory containing the custom plugin jars and only the custom plugin jars. To migrate your custom plugins, see the [PingAccess Addon SDK for Java Migration Guide](../agents_and_integrations/pa_add_on_sdk_for_java_migration_guide.html). |

During the upgrade, it is important to not make any changes to the running PingAccess environment.

## Steps

1. If you are using the upgrade utility, change to the new version's `/upgrade/bin` directory on the command line. For example:

   ```
   cd /pingaccess-6.1.0/upgrade/bin
   ```

2. If you are using the incremental update bundle, disable configuration replication for the replica administrative node.

   1. In a browser, go to https\://*\<host>*:*\<admin-port>*/pa-admin-api/v3/api-docs/.

      ### Example:

      https\://localhost:9000/pa-admin-api/v3/api-docs/

   2. Expand the **/adminConfig/replicaAdmins** endpoint.

   3. Click the **GET /adminConfig/replicaAdmins** operation.

   4. Click **Try it out!** and note the `id` for the replica admin.

   5. Click the **GET /adminConfig/replicaAdmins/{id}** operation.

   6. Enter the `id` of the replica admin you want to update and click **Try it out!**

   7. Copy the **Response Body**.

   8. Click the **PUT /adminConfig/replicaAdmins/{id}** operation and enter the `id` of the replica admin you want to update.

   9. Paste the **Response Body** you copied and change `"configReplicationEnabled"` to `false`.

   10. Click **Try it out!**

       ### Result:

       If the operation is successful, you will receive a **Response Code** of **200**.

3. If you are using the incremental update bundle, disable configuration replication for each engine node.

   1. In a browser, go to https\://*\<host>*:*\<admin-port>*/pa-admin-api/v3/api-docs/.

      ### Example:

      https\://localhost:9000/pa-admin-api/v3/api-docs/

   2. Expand the **/engines** endpoint.

   3. Click the **GET /engines** operation.

   4. Click **Try it out!** and note the engine `id` for each engine.

   5. Click the **GET /engines/{id}** operation.

   6. Enter the `id` of the engine you want to update and click **Try it out!**

   7. Copy the **Response Body**.

   8. Click the **PUT /engines/{id}** operation and enter the `id` of the engine you want to update.

   9. Paste the **Response Body** you copied and change `"configReplicationEnabled"` to `false`.

   10. Click **Try it out!**

       ### Result:

       If the operation is successful, you will receive a **Response Code** of **200**.

4. Upgrade the system:

   ### Choose from:

   * If you are using the upgrade utility on a Windows system, use this command: `upgrade.bat -r <admin_port>] <directory>] <jvm_memory_options_file>] <newPingAccessLicense>] [-s \| --silent] <sourcePingAccessRootDir>`.

     For example:

     ```
     upgrade.bat -r ../pingaccess-5.3.0
     ```

   * If you are using the upgrade utility on a Linux system, use this command: `./upgrade.sh -r <admin_port>] <directory>] <jvm_memory_options_file>] <newPingAccessLicense>] [-s \| --silent] <sourcePingAccessRootDir>`.

     For example:

     ```
     ./upgrade.sh -r ../pingaccess-5.3.0
     ```

   * If you are using the incremental update package, open the readme file and make the file changes specified in the readme.

     |   |                                                                                                                                                                               |
     | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | The `-r` switch will disable configuration replication on the administrative node. You will re-enable configuration replication for each node as part of the upgrade process. |

     **Parameter definitions**

     The command-line parameters are the same regardless of the platform, and are defined as follows:

     | Parameter                          | Value description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
     | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
     | -r \| --disable-config-replication | Disables configuration replication on the administrative node.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
     | -p <*admin\_port*>                 | Optional port to be used by the temporary PingAccess instance run during the upgrade. The default is 9001.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
     | -i <*directory*>                   | An optional directory containing additional library JAR files (for example, plugins, JDBC drivers) to be copied into the target installation.Beginning in version 6.0, JAR files are stored in the `<PA HOME>/deploy` folder.During an upgrade from versions earlier than 6.0, third-party JAR files are migrated from the `lib` folder to the `deploy` folder if no directory is specified.During an upgrade from version 6.0 or later, the contents of the `deploy` folder are migrated to the new `<PA HOME>/deploy` folder if no directory is specified. |
     | <*sourcePingAccessRootDir*>        | The PA\_HOME for the source PingAccess version.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
     | -l <*newPingAccessLicense*>        | An optional path to the PingAccess license file to use for the target version. If not specified, the existing license is reused.                                                                                                                                                                                                                                                                                                                                                                                                                             |
     | -j <*jvm\_memory\_options\_file*>  | An optional path to a file with Java Virtual Machine (JVM) *(tooltip: \<div class="paragraph">&#xA;\<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>&#xA;\</div>)* memory options to use for the new PingAccess instance during the upgrade.                                                                                                                                                                                                                                           |
     | -s \| --silent                     | Run the upgrade with no user input required. To use this option, specify the source version's credentials using environment variables.                                                                                                                                                                                                                                                                                                                                                                                                                       |

     **Environment Variables**

     You can specify the username and password for the source version using these environment variables:

     | Environment variable     | Description                                                                                                                                                                                                                                                                                   |
     | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     | `PA_SOURCE_API_USERNAME` | The username for the source version's Admin application programming interface (API) *(tooltip: \<div class="paragraph">&#xA;\<p>A specification of interactions available for building software to access an application or service.\</p>&#xA;\</div>)*. This should be set to Administrator. |
     | `PA_SOURCE_API_PASSWORD` | The basic authorization password for the Administrator in the source version's Admin API.                                                                                                                                                                                                     |

     **JVM Memory options**

     These options can be included in the JVM memory options file. Memory amounts use `m` or `g` to specify the unit.

     | Memory option             | Description                                                   |
     | ------------------------- | ------------------------------------------------------------- |
     | `-Xms<amount>`            | Minimum heap size.                                            |
     | `-Xmx<amount>`            | Maximum heap size.                                            |
     | `-XX:NewSize=<amount>`    | Minimum size for the Young Gen space.                         |
     | `-XX:MaxNewSize=<amount>` | Maximum size for the Young Gen space.                         |
     | `-XX:+UseParallelGC`      | Specifies that the parallel garbage collector should be used. |

     For example:

     ```
     #Sample JVM Memory options file
     -Xms512m
     -Xmx1g
     -XX:NewSize=256m
     -XX:MaxNewSize=512m
     -XX:+UseParallelGC
     ```

     You can copy the existing `PA_HOME/conf/jvm-memory.options` file to create a JVM memory options file for the upgrade.

5. Stop the existing PingAccess admin instance.

6. Start the new PingAccess admin instance.

## Next steps

|   |                                                                                                                                                                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If PingAccess is running as a service, and you upgraded using the upgrade utility:- In Linux, update **PA\_HOME** in `/etc/systemd/system/pingaccess.service` to point to the new installation.

- In Windows, remove the existing PingAccess service (`<OLD_PA_HOME>\sbin\Windows\uninstall-service.bat`) and add the new service (`<NEW_PA_HOME>\sbin\Windows\install-service.bat`). |

After you have upgraded the administrative node, you can [upgrade the replica admin node](pa_upgrading_the_replica_admin_node.html).

---

---
title: Upgrading the engine
description: Use the PingAccess Upgrade Utility to upgrade the engine.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_zero_downtime_upgrade:pa_upgrading_the_engine
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_zero_downtime_upgrade/pa_upgrading_the_engine.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  example: Example:
  choose-from: Choose from:
  example-2: Example:
  next-steps: Next steps
---

# Upgrading the engine

Use the PingAccess Upgrade Utility to upgrade the engine.

## Before you begin

For more information on upgrading PingAccess, see [Upgrade PingAccess](../upgrading_pingaccess/pa_upgrading_pa_landing_topic.html). The following flowchart displays an example engine upgrade.

![Flowchart showing a deployment as the engine is upgraded.](_images/pgc1564006859458.png)

In this flowchart:

1. A user with a WebSession Cookie sends a request to the load balancer.

2. The load balancer directs the request to one of the un-upgraded engine nodes. The first engine node is using the target version of PingAccess, while the other engine nodes are still using the source version of PingAccess.

3. The administrative node is using the target version of PingAccess.

Before beginning the upgrade process, make sure you have:

* Ensured the PingAccess engine is running

* Downloaded the PingAccess [distribution](https://www.pingidentity.com/en/resources/downloads/pingaccess.html) `.zip` file or the incremental update bundle and extracted it.

* The PingAccess license

## About this task

Any warnings or errors encountered are recorded in `log/upgrade.log`, as well as on the screen while the utility is running. The upgrade uses an exit code of `0` to indicate a successful upgrade and an exit code of `1` to indicate failure.

## Steps

1. If you are using the upgrade utility, change to the new version's `/upgrade/bin` directory on the command line.

   ### Example:

   ```
   cd /pingaccess-6.1.0/upgrade/bin
   ```

2. Upgrade the system:

   ### Choose from:

   * If you are using the upgrade utility on a Windows system, use this command: `upgrade.bat <admin_port>] <directory>] <jvm_memory_options_file>] <newPingAccessLicense>] [-s \| --silent] <sourcePingAccessRootDir>`.

     For example:

     ```
     upgrade.bat ../pingaccess-5.3.0
     ```

   * If you are using the upgrade utility on a Linux system, use this command: `./upgrade.sh <admin_port>] <directory>] <jvm_memory_options_file>] <newPingAccessLicense>] [-s \| --silent] <sourcePingAccessRootDir>`.

     For example:

     ```
     ./upgrade.sh ../pingaccess-5.3.0
     ```

   * If you are using the incremental update package, open the `ReadMeFirst.txt` file and make the file changes specified in the readme.

     The command-line parameters are the same regardless of the platform, and are defined as follows:

     **Parameter definitions**

     | Parameter                         | Value description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
     | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
     | -p <*admin\_port*>                | Optional port to be used by the temporary PingAccess instance run during the upgrade. The default is `9001`.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
     | -i <*directory*>                  | An optional directory containing additional library JAR files (for example, plugins, JDBC drivers) to be copied into the target installation.Beginning in version 6.0, JAR files are stored in the `<PA_HOME>/deploy` folder.During an upgrade from versions earlier than 6.0, third-party JAR files are migrated from the `lib` folder to the `deploy` folder if no directory is specified.During an upgrade from version 6.0 or later, the contents of the `deploy` folder are migrated to the new `<PA_HOME>/deploy` folder if no directory is specified. |
     | <*sourcePingAccessRootDir*>       | The PA\_HOME for the source PingAccess version.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
     | -l <*newPingAccessLicense*>       | An optional path to the PingAccess license file to use for the target version. If not specified, the existing license is reused.                                                                                                                                                                                                                                                                                                                                                                                                                             |
     | -j <*jvm\_memory\_options\_file*> | An optional path to a file with Java Virtual Machine (JVM) *(tooltip: \<div class="paragraph">&#xA;\<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>&#xA;\</div>)* memory options to use for the new PingAccess instance during the upgrade.                                                                                                                                                                                                                                           |
     | -s \| --silent                    | Run the upgrade with no user input required. To use this option, specify the source version's credentials using environment variables.                                                                                                                                                                                                                                                                                                                                                                                                                       |

     **Environment Variables**

     You can specify the username and password for the source version using these environment variables:

     | Environment variable     | Description                                                                                                                                                                                                                                                                                   |
     | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     | `PA_SOURCE_API_USERNAME` | The username for the source version's Admin application programming interface (API) *(tooltip: \<div class="paragraph">&#xA;\<p>A specification of interactions available for building software to access an application or service.\</p>&#xA;\</div>)*. This should be set to Administrator. |
     | `PA_SOURCE_API_PASSWORD` | The basic authorization password for the Administrator in the source version's Admin API.                                                                                                                                                                                                     |

     **JVM Memory options**

     These options can be included in the JVM memory options file. Memory amounts use `m` or `g` to specify the unit.

     | Memory option             | Description                                                   |
     | ------------------------- | ------------------------------------------------------------- |
     | `-Xms<amount>`            | Minimum heap size.                                            |
     | `-Xmx<amount>`            | Maximum heap size.                                            |
     | `-XX:NewSize=<amount>`    | Minimum size for the Young Gen space.                         |
     | `-XX:MaxNewSize=<amount>` | Maximum size for the Young Gen space.                         |
     | `-XX:+UseParallelGC`      | Specifies that the parallel garbage collector should be used. |

     ### Example:

     ```
     #Sample JVM Memory options file
     -Xms512m
     -Xmx1g
     -XX:NewSize=256m
     -XX:MaxNewSize=512m
     -XX:+UseParallelGC
     ```

     You can copy the existing `PA_HOME/conf/jvm-memory.options` file to create a JVM memory options file for the upgrade.

3. Stop the existing PingAccess instance. Do not start the new instance.

## Next steps

|   |                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If PingAccess is running as a service and you upgraded using the upgrade utility:- In Linux, update `PA_HOME` in `/etc/systemd/system/pingaccess.service` to point to the new installation.

- In Windows, remove the existing PingAccess service (`<OLD_PA_HOME>\sbin\Windows\uninstall-service.bat`) and add the new service (`<NEW_PA_HOME>\sbin\Windows\install-service.bat`). |

---

---
title: Upgrading the replica administrative node
description: Upgrade the PingAccess replica administrative node using the PingAccess Upgrade Utility, then resume configuration replication.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_zero_downtime_upgrade:pa_upgrading_the_replica_admin_node
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_zero_downtime_upgrade/pa_upgrading_the_replica_admin_node.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 7, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  example: Example:
  choose-from: Choose from:
  example-2: Example:
  result: Result:
  next-steps: Next steps
---

# Upgrading the replica administrative node

Upgrade the PingAccess replica administrative node using the PingAccess Upgrade Utility, then resume configuration replication.

## About this task

Any warnings or errors encountered are recorded in `log/upgrade.log`, as well as on the screen while the utility is running. The upgrade uses an exit code of `0` to indicate a successful upgrade and an exit code of `1` to indicate failure.

|   |                                                                                                    |
| - | -------------------------------------------------------------------------------------------------- |
|   | During the upgrade, it is important to not make any changes to the running PingAccess environment. |

## Steps

1. If you are using the upgrade utility, change to the new version's `/upgrade/bin` directory on the command line.

   ### Example:

   ```
   cd /pingaccess-6.1.0/upgrade/bin
   ```

2. Upgrade the system:

   ### Choose from:

   * If you are using the upgrade utility on a Windows system, use this command: `upgrade.bat <admin_port>] <directory>] <jvm_memory_options_file>] <newPingAccessLicense>] [-s \| --silent] <sourcePingAccessRootDir>`

     For example:

     ```
     upgrade.bat ../pingaccess-5.3.0
     ```

   * If you are using the upgrade utility on a Linux system, use this command: `./upgrade.sh <admin_port>] <directory>] <jvm_memory_options_file>] <newPingAccessLicense>] [-s \| --silent] <sourcePingAccessRootDir>`

     For example:

     ```
     ./upgrade.sh ../pingaccess-5.3.0
     ```

   * If you are using the incremental update package, open the `ReadMeFirst.txt` file and make the file changes specified in the readme.

     The command-line parameters are the same regardless of the platform, and are defined as follows.

     **Parameter definitions**

     | Parameter                         | Value description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
     | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
     | -p <*admin\_port*>                | Optional port to be used by the temporary PingAccess instance run during the upgrade. The default is 9001.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
     | -i <*directory*>                  | An optional directory containing additional library JAR files (for example, plugins, JDBC drivers) to be copied into the target installation.Beginning in version 6.0, JAR files are stored in the `<PA_HOME>/deploy` folder.During an upgrade from versions earlier than 6.0, third-party JAR files are migrated from the `lib` folder to the `deploy` folder if no directory is specified.During an upgrade from version 6.0 or later, the contents of the `deploy` folder are migrated to the new `<PA_HOME>/deploy` folder if no directory is specified. |
     | <*sourcePingAccessRootDir*>       | The *PA\_HOME* for the source PingAccess version.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
     | -l <*newPingAccessLicense*>       | An optional path to the PingAccess license file to use for the target version. If not specified, the existing license is reused.                                                                                                                                                                                                                                                                                                                                                                                                                             |
     | -j <*jvm\_memory\_options\_file*> | An optional path to a file with Java Virtual Machine (JVM) *(tooltip: \<div class="paragraph">&#xA;\<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>&#xA;\</div>)* memory options to use for the new PingAccess instance during the upgrade.                                                                                                                                                                                                                                           |
     | -s \| --silent                    | Run the upgrade with no user input required. To use this option, specify the source version's credentials using environment variables.                                                                                                                                                                                                                                                                                                                                                                                                                       |

     **Environment Variables**

     You can specify the username and password for the source version using these environment variables:

     | Environment variable     | Description                                                                                                                                                                                                                                                                                   |
     | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     | `PA_SOURCE_API_USERNAME` | The username for the source version's Admin application programming interface (API) *(tooltip: \<div class="paragraph">&#xA;\<p>A specification of interactions available for building software to access an application or service.\</p>&#xA;\</div>)*. This should be set to Administrator. |
     | `PA_SOURCE_API_PASSWORD` | The basic authorization password for the Administrator in the source version's Admin API.                                                                                                                                                                                                     |

     **JVM Memory options**

     These options can be included in the JVM memory options file. Memory amounts use `m` or `g` to specify the unit.

     | Memory option             | Description                                                   |
     | ------------------------- | ------------------------------------------------------------- |
     | `-Xms<amount>`            | Minimum heap size.                                            |
     | `-Xmx<amount>`            | Maximum heap size.                                            |
     | `-XX:NewSize=<amount>`    | Minimum size for the Young Gen space.                         |
     | `-XX:MaxNewSize=<amount>` | Maximum size for the Young Gen space.                         |
     | `-XX:+UseParallelGC`      | Specifies that the parallel garbage collector should be used. |

     For example:

     ```
     #Sample JVM Memory options file
     -Xms512m
     -Xmx1g
     -XX:NewSize=256m
     -XX:MaxNewSize=512m
     -XX:+UseParallelGC
     ```

     You can copy the existing `<PA_HOME>/conf/jvm-memory.options` file to create a JVM memory options file for the upgrade.

3. Stop the existing PingAccess replica admin instance.

4. Start the new PingAccess replica admin instance.

   You're now ready to resume configuration replication for the replica administrative node.

5. In a browser, go to https\://*\<host>*:*\<admin-port>*/pa-admin-api/v3/api-docs/.

   ### Example:

   https\://localhost:9000/pa-admin-api/v3/api-docs/

6. Expand the **/adminConfig/replicaAdmins** endpoint.

7. Click the **GET /adminConfig/replicaAdmins** operation.

8. Click **Try it out!** and note the `id` for the replica admin.

9. Click the **GET /adminConfig/replicaAdmins/{id}** operation.

10. Enter the id of the replica admin you want to update and click **Try it out!**

11. Copy the Response Body.

12. Click the **PUT /adminConfig/replicaAdmins/{id}** operation and enter the id of the replica admin you want to update.

13. Paste the Response Body you copied and change `"configReplicationEnabled"` to `true`.

14. Click **Try it out!**

    ### Result:

    If the operation is successful, you will receive a response code of `200`.

15. Click **Settings**, then go to **Clustering > Administrative Nodes**.

16. Ensure the Replica Administrative Node displayed and reporting on the **Administrative Nodes** tab. A healthy node shows a green status indicator.

## Next steps

After you have upgraded the administrative and replica administrative nodes, you can begin [upgrading the engines](pa_upgrading_engines.html).