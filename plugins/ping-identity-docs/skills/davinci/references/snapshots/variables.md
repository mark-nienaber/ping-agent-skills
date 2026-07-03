---
title: Adding a variable
description: Add a new variable that can be used in flows.
component: davinci
page_id: davinci:variables:davinci_adding_a_variable
canonical_url: http://docs.pingidentity.com/davinci/variables/davinci_adding_a_variable.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 31, 2024
section_ids:
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
---

# Adding a variable

Add a new variable that can be used in flows.

## Steps

1. Click the **Variables** tab.

2. Click **Add New Variable**.

3. In the **Name** field, enter a name for the variable.

   |   |                                                      |
   | - | ---------------------------------------------------- |
   |   | The name `challenge` is reserved and cannot be used. |

4. In the **Variable Context** list, select a context in which the variable is shared:

   ### Choose from:

   * **Flow Instance Context**: The variable has one value for each instance of each flow.

   * **User Context**: The variable has one value for each user. The user must be identified.

   * **Company Context**: The variable has one value for the company, across all flows and users. All secret variables use this context.

     |   |                                                                                                                                                                                               |
     | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | A variable with a flow context can only be created within a flow by using the Variables connector. After you create a flow context variable, you can edit its value in the **Variables** tab. |

5. (Optional) In the **Description** field, enter a description for the variable.

6. In the **Data Type** list, select a data type:

   ### Choose from:

   * **String**

   * **Boolean**

   * **Number**

   * **Object**

   * **Secret**: This data type indicates that the variable value is sensitive and should not be visible in the UI, analytics, logs, or API queries. It is only available for company context variables. Secret variables are for custom API calls, so they can only be used in the **Headers** and **Body** parameters of the Make REST API Call capability (HTTP connector). They are not available anywhere else in DaVinci.

7. In the **Value** field, enter an initial value for the variable.

8. (Optional) Click the **Mutable** toggle to allow nodes within a flow to change the value of the variable.

   You can trace the expected value of a variable through the nodes of your flow to help you decide whether the variable should be mutable or not.

9. (Optional) In the **Min** field, enter a minimum value for the variable.

10. (Optional) In the **Max** field, enter a maximum value for the variable.

11. Click **Create**.
