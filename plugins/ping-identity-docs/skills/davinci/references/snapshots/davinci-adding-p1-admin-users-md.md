---
title: Adding DaVinci Admin Users in PingOne
description: You can add admin users to DaVinci through PingOne.
component: davinci
page_id: davinci::davinci_adding_p1_admin_users
canonical_url: https://docs.pingidentity.com/davinci/davinci_adding_p1_admin_users.html
llms_txt: https://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 28, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  result: Result
---

# Adding DaVinci Admin Users in PingOne

You can add admin users to DaVinci through PingOne.

## Before you begin

To grant an admin role to a user, you must have an equal or greater role. To grant the **DaVinci Admin** role, you must have the **DaVinci Admin** role. To grant the **DaVinci Admin Read Only** role, you must have the **DaVinci Admin** or **DaVinci Admin Read Only** role. For more information about managing administrator roles in PingOne, see [Managing administrator roles](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_manage_admin_roles.html).

## About this task

To add DaVinci admin users in PingOne:

## Steps

1. Sign on to PingOne.

2. Select the environment that includes your administrative users.

3. Go to **Directory > Users**.

4. Locate the user that you want to edit. You can browse or search for users.

5. Click the **Details** icon to expand the user that you want to edit, and then click the **Pencil** icon.

6. Click **Roles**.

7. Add a role for the user.

   1. Click **+Add Role**.

   2. Select the **DaVinci Admin** role to grant the user full admin access, or select the **DaVinci Admin Read Only** role to grant the user read-only access.

   3. Click **Next**.

   4. In the **Define Responsibilities** section, click the **Add** icon to add the environment that includes your DaVinci instance.

   5. Click **Add Role**.

## Result

The user can now access DaVinci through SSO.