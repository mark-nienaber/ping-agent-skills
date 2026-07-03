---
title: Connecting to a local process
description: Use the local process option to establish a connection when the PingAccess server is running on a local system.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_monitoring_guide:pa_connecting_to_a_local_process
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_monitoring_guide/pa_connecting_to_a_local_process.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 12, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Connecting to a local process

Use the local process option to establish a connection when the PingAccess server is running on a local system.

## About this task

Unless you are running the PingAccess server as a Windows service, the easiest method to launch JConsole on the same machine as the server is to select **Local Process**. For information about connecting to a remote process instead, see [Connecting to a remote process](pa_connecting_to_a_remote_process.html).

To connect to a local instance and start the monitoring process:

## Steps

* In the **Local Process** list, select `com.pingidentity.pa.cli.Starter`, then click **Connect.**

  |   |                                                                                                           |
  | - | --------------------------------------------------------------------------------------------------------- |
  |   | If you are running the process locally, the system might prompt you to accept the connection as insecure. |

  ![Screen capture of the JConsole: New Connection window with the local process option and the com.pingidentity.pa.cli.Starter connection highlighted.](_images/mzs1580499549454.png)
