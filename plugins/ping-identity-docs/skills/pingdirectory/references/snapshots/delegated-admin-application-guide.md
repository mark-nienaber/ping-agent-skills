---
title: Adding a user to a group
description: You can add users to groups from the Manage Users page and from the Manage Groups page in the Delegated Admin GUI.
component: pingdirectory
version: 11.1
page_id: pingdirectory:delegated_admin_application_guide:pd_da_add_user_to_group
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/delegated_admin_application_guide/pd_da_add_user_to_group.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
page_aliases: ["pd_da_add_user_to_configured_group.adoc", "pd_da_add_user_from_manage_users_window.adoc", "pd_da_add_user_from_manage_groups_window.adoc"]
section_ids:
  adding-a-new-user-to-a-configured-group: Adding a new user to a configured group
  about-this-task: About this task
  steps: Steps
  adding-a-user-from-the-manage-users-window: Adding a user from the Manage Users window
  steps-2: Steps
  result: Result:
  adding-a-user-from-the-manage-groups-window: Adding a user from the Manage Groups window
  steps-3: Steps
  result-2: Result:
---

# Adding a user to a group

You can add users to groups from the **Manage Users** page and from the **Manage Groups** page in the Delegated Admin GUI.

## Adding a new user to a configured group

### About this task

When the delegated admin rights for a user REST resource type have the `resources-in-specific-groups` admin scope, a user is added to one of the configured groups when you create the user:

* For admins with rights to only one group, the new user is automatically added to that group. No field for `Select Group` displays.

* For admins with rights to more than one group, the admin selects a group to add the user to in the `Select Group` list.

* Admins can select from both static and dynamic groups.

* For dynamic groups, in addition to selecting the group, the new entry must also match criteria for membership of that group.

  For example, in a dynamic group of members with `uid=user.111*`, the `uid` starts with `user.111`.

To create a new user in that group, an administrator must:

### Steps

1. In the `Select Group` list, select the group name.

2. Enter the value for `uid` that starts with `user.111`.

## Adding a user from the Manage Users window

You can add users to groups using the **Manage Users** window in the Delegated Admin GUI.

### Steps

1. In the Delegated Admin GUI, go to the **Manage Users** window.

2. Use to search field to search for the user to add to a group.

3. Click the **Expand** icon on the appropriate user profile.

4. To edit the user profile, click the **Pencil** icon.

5. Click the **Group Membership** tab.

6. Use the search field to search for the appropriate group.

7. To add the user to the respective group, in the **Nonmember Groups** list, click **[icon: plus, set=fa]**.

   #### Result:

   The group moves to the **Member Groups** list.

## Adding a user from the Manage Groups window

You can add users to groups using the **Manage Groups** window in the Delegated Admin GUI.

### Steps

1. In the Delegated Admin GUI, go to the **Manage Groups** window.

2. To filter by group resource type, make a selection from the drop-down list for the group resource type you want to search within.

3. (Optional) To narrow your results, use the search field to search for the appropriate group.

4. Click the **Expand** icon on your chosen group.

5. To edit the group profile, click the **Pencil** icon.

6. Under the group name, click **Group Membership**.

7. (Optional) To filter entries by resource type, make a selection from the **Select a Type** drop-down list.

   |   |                                                                                                                                                                     |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If there is a parent resource type, a second drop-down list appears. Make an additional selection, or leave it to **All** to see all entries in that resource type. |

8. Use the search field to search for the appropriate entry.

9. To add an entry to the group, from the **Nonmembers** list, click **[icon: plus, set=fa]**.

   #### Result:

   The user moves to the **Members** list.
