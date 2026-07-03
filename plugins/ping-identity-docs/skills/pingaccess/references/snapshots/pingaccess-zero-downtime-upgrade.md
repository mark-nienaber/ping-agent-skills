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
