---
title: Admin console best practices
description: The admin console is a convenient way to configure and manage your PingFederate environment. However, you should keep the following best practices in mind while using the admin console so that you don't inadvertently create errors or corrupt your PingFederate configuration.
component: pingfederate
version: 13.1
page_id: pingfederate:getting_started_with_pingfederate:pf_admin_console_best_practices
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/getting_started_with_pingfederate/pf_admin_console_best_practices.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Admin console best practices

The admin console is a convenient way to configure and manage your PingFederate environment. However, you should keep the following best practices in mind while using the admin console so that you don't inadvertently create errors or corrupt your PingFederate configuration.

* Don't use your browser's **Back** button

  Using your browser's navigation buttons such as **Back** or **Reload**, can cause PingFederate to behave inconsistently.

  If you need to go back to a previous menu, use the navigation buttons at the top or right side of the PingFederate menu.

  To go back a step in a configuration workflow with multiple tabs, click the tab you want to visit, or click **Previous** at the bottom of the screen.

  ![a screencapture of the Protocol Settings menu with arrows pointing to the previous tab and Previous button.](../administrators_reference_guide/_images/pf_img_backnav.png)

* Don't use multiple browser tabs

  Using PingFederate in multiple browser tabs could cause errors or inconsistencies.

* Wait for a page to finish loading before going to another page

  Going to another page before the current page finishes loading can cause inconsistent behavior. Even if you go to a page by mistake, allow it to load fully before going elsewhere.

* One administrator at a time

  You should allow only one administrative user to sign on to PingFederate at any one time. Because admins can create or change configurations, having multiple admins working in PingFederate at the same time risks causing conflicts.

  |   |                                                                                                                                                 |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | To configure PingFederate to allow only one administrator at a time, set the `pf.console.login.mode` parameter in `run.properties` to `single`. |

  You can have one or more auditors in PingFederate at the same time as an admin. Auditors can see settings in the admin console, but they can't change them.

* Don't replicate while an admin is working

  If you're running PingFederate in a clustered environment, you should only replicate configurations to other nodes while no admins are working in the admin console. If an admin is creating or changing a configuration while replication is in progress, the replication might only carry over a portion of the configuration.

* Clear your cache and cookies

  If pages in PingFederate aren't loading at all, or it returns the **Something's not right** error page, trying clearing the cache and cookies in your browser. This can be particularly effective after an upgrade.
