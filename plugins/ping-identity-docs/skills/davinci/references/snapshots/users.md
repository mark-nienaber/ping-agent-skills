---
title: Deleting a user
description: Delete a user to remove all information about the user from DaVinci.
component: davinci
page_id: davinci:users:davinci_deleting_a_user
canonical_url: http://docs.pingidentity.com/davinci/users/davinci_deleting_a_user.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 28, 2024
section_ids:
  steps: Steps
---

# Deleting a user

Delete a user to remove all information about the user from DaVinci.

## Steps

1. Click the **Users** tab.

2. Find the user and click **Delete**.

   |   |                                                                      |
   | - | -------------------------------------------------------------------- |
   |   | Use the search pane if your environment has a large number of users. |

   A confirmation message displays.

3. Click **Delete**.

---

---
title: Users
description: "Users are end users created during flows. You can view and edit users' properties and delete users."
component: davinci
page_id: davinci:users:davinci_users
canonical_url: http://docs.pingidentity.com/davinci/users/davinci_users.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 28, 2024
---

# Users

Users are end users created during flows. You can view and edit users' properties and delete users.

The **Users** table displays the following user properties.

| Property            | Description                                                   |
| ------------------- | ------------------------------------------------------------- |
| **User ID**         | The user ID.                                                  |
| **Connection Name** | The name of the connection which was used to create the user. |
| **Full Name**       | The user's full given name.                                   |
| **Email Address**   | The user's email address.                                     |
| **Created Date**    | The date on which the user was first created.                 |
| **User Name**       | The user's username.                                          |

You can view the following properties when editing a user.

| Property                   | Description                                                                                                            |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Username**               | The user's username.                                                                                                   |
| **User Alias**             | If a team member has created an alias for the user, it is displayed.                                                   |
| **User ID**                | The user ID.                                                                                                           |
| **Connection ID**          | The ID of the connection used to create the user.                                                                      |
| **Company ID**             | The ID of the company with which the user is associated.                                                               |
| **Name**                   | If the user's given name is known, it is displayed.                                                                    |
| **Email**                  | If the user's email address is known, it is displayed.                                                                 |
| **Created Date**           | The date on which the user was first created.                                                                          |
| **Variables**              | If your environment includes one or more variables with the user context, the values of those variables are displayed. |
| **Authentication Methods** | If the user has configured one or more authentication methods, they are displayed.                                     |

---

---
title: Viewing and editing a user
description: View and edit a user's properties, including variables and user events.
component: davinci
page_id: davinci:users:davinci_viewing_and_editing_a_user
canonical_url: http://docs.pingidentity.com/davinci/users/davinci_viewing_and_editing_a_user.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 2, 2023
section_ids:
  steps: Steps
---

# Viewing and editing a user

View and edit a user's properties, including variables and user events.

## Steps

1. Click the **Users** tab.

2. Find the user and click **Edit**.

   |   |                                                                      |
   | - | -------------------------------------------------------------------- |
   |   | Use the search pane if your environment has a large number of users. |

3. (Optional) To view user details, click **User Info**.

4. (Optional) Add a user alias:

   1. Click **User Info**.

   2. Click **Add User Alias**.

   3. In the **User Alias** field, enter an internal alias for the user.

   4. Click **Update**.

5. (Optional) To view a list of logged events involving the user, click **Events**.

6. Click **Close**.