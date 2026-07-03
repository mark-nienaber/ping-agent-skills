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

---

---
title: Deleting a variable
description: Delete an existing variable to remove it from the UI and from all flows.
component: davinci
page_id: davinci:variables:davinci_deleting_a_variable
canonical_url: http://docs.pingidentity.com/davinci/variables/davinci_deleting_a_variable.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 6, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Deleting a variable

Delete an existing variable to remove it from the UI and from all flows.

## About this task

|   |                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------- |
|   | If you plan to delete a variable used in one or more flows, you should update the flows to remove the variable before deleting it. |

## Steps

1. Click the **Variables** tab.

2. Find the variable you want to delete and click the **Delete** icon.

   A confirmation message displays.

3. Click **Delete**.

---

---
title: Editing a variable
description: Edit an existing variable to change its properties.
component: davinci
page_id: davinci:variables:davinci_editing_a_variable
canonical_url: http://docs.pingidentity.com/davinci/variables/davinci_editing_a_variable.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 31, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Editing a variable

Edit an existing variable to change its properties.

## About this task

|   |                                                        |
| - | ------------------------------------------------------ |
|   | You cannot change the name and context for a variable. |

## Steps

1. Click the **Variables** tab.

2. Find the variable you want to edit and click the **Pencil** icon.

3. (Optional) In the **Description** field, update the description for the variable.

4. (Optional) In the **Data Type** list, select a data type:

   ### Choose from:

   * **String**

   * **Boolean**

   * **Number**

   * **Object**

   * **Secret**

     |   |                                                                                                   |
     | - | ------------------------------------------------------------------------------------------------- |
     |   | If you change a variable's data type from **Secret** to another type, the existing value is lost. |

5. (Optional) In the **Value** field, enter a value for the variable.

   For flows with the **Company Context**, this field updates the current value. For all other contexts, this field sets the initial value.

   If the variable's data type is **Secret**, the existing value can only be replaced. It cannot be edited or viewed.

6. (Optional) Click the **Mutable** toggle to allow nodes within a flow to change the value of the variable.

7. (Optional) In the **Min** field, enter a minimum value for the variable.

8. (Optional) In the **Max** field, enter a maximum value for the variable.

9. Click **Update**.

---

---
title: Using variables in flows
description: You can use variables in multiple ways within a flow.
component: davinci
page_id: davinci:variables:davinci_using_variables_in_flows
canonical_url: http://docs.pingidentity.com/davinci/variables/davinci_using_variables_in_flows.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 19, 2024
section_ids:
  variables-connector: Variables connector
  including-variables-in-code: Including variables in code
  sharing-variable-values-between-flows: Sharing variable values between flows
---

# Using variables in flows

You can use variables in multiple ways within a flow.

## Variables connector

You can add the Variables connector to your flows. This connector has multiple capabilities that let you add variables to a flow and increment or otherwise change the variable's value.

The variables connector can be used to update User variables and Flow Instance variables. It can also be used to create flow instance variables, but user variables must be created in the variables tab.

## Including variables in code

You can include variable values in the code fields of nodes such as HTTP nodes, or as inputs in the fields of other nodes. Within the code field, click **{}**, then select a variable type.

You can also directly include a variable using the following syntax:

* Company Variable

  `{{global.company.variables.variableName}}`

* User Variable

  `{{global.userInfo.variables.variableName}}`

* Flow Variable

  `{{global.flow.variables.variableName}}`

* Flow Instance Variable

  `{{global.variables.variableName}}`

When you use a variable in this way, the variable's exact value is included in the code, and you should take the variable type into account when writing the code. For example, a string variable should be surrounded by quotation marks, while a boolean variable or number variable should not.

If a variable's value is an object and you want to reference a value within the object, use the syntax described above and append the value's location to the end outside of the brackets.

For example, if a company variable's value was the following object:

```
{
  "level1": {
    "level2":"value2"
  }
}
```

You could include value2 using the following syntax:

```
{{global.company.variables.variablename}}.level1.level2
```

## Sharing variable values between flows

You can pass variable data between flows and subflows using input and output schemas, which pass information into and out of the subflow.

To use an input schema in a subflow, open the flow and click **Input Schema**. Use the variable name the **Parameter Name**, select the **Data Type** that corresponds to the variable data type, and enable **Required** if the variable is necessary for the flow to function. After you add a parameter to a subflow's input schema, the Invoke Subflow or Invoke UI Subflow node that launches that subflow will include input fields that correspond to the input schema parameters. Add the variable values to these fields using the syntax described above.

To use an output schema in a subflow, click **[icon: ellipsis-v, set=fa]> Output Schema**, then declare the variable's name and type as part of the output schema JSON.

Next, open each of the nodes that sends a JSON success, error, or custom response at the end of the subflow. In the **Additional Fields in the Response** section, click **[icon: plus, set=fa]Field**. In the **Value** field, click **{}** and select Flow Instance Variables, then click the variable you want to share. You can also use the syntax described above to include variable values. Apply your changes to the node.

---

---
title: Variables
description: Variables let you track and adjust values from within your flows.
component: davinci
page_id: davinci:variables:davinci_variables
canonical_url: http://docs.pingidentity.com/davinci/variables/davinci_variables.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 31, 2024
---

# Variables

Variables let you track and adjust values from within your flows.

Variables are values that can be read and modified during a flow. They can be strings, Boolean values, numbers, or objects.

You can use variables in a flow to track information, and you can use a variable's value to determine which nodes are run within the flow.

Every variable has a context, which determines how widely its value is shared:

* **Company Context**

  The variable has a single value for the company. This value is used in all flows and for all users.

  Company context variables can be created as **Secret** variables, which are designed to store sensitive values such as API keys, client secrets, and access tokens. The current value for secret variables cannot be seen in the UI, logs, analytics, exported flows, or API queries.

  |   |                                                                                                                                     |
  | - | ----------------------------------------------------------------------------------------------------------------------------------- |
  |   | Secret variables can only be used in the HTTP connector's Make REST API Call capability in the **Headers** and **Body** parameters. |

* **Flow Context**

  The variable is tied to a specific flow and has a single, persistent value until that value is changed. The current value can be viewed in the **Variables** tab.

  To change variable values, you can run the containing flow or update the variable on the **Variables** tab. The variable's new value is set to the value of the latest update using either method.

* **Flow Instance Context**

  The variable can be used in multiple flows.

  * If the variable's value is set within a flow, the variable instance in that flow gets the value set by the flow's execution.

  * If the variable's value is not set within a flow, the variable instance in that flow inherits the value set on the **Variables** tab.

* **User Context**

  The variable has a separate value for each user. If you use a variable with this context in a flow, the user must be identified.