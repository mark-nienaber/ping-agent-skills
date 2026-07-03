---
title: Best practices for creating subflows
description: Use these best practices when creating a subflow.
component: davinci
page_id: davinci:davinci_best_practices:davinci_best_practices_subflows_creating
canonical_url: http://docs.pingidentity.com/davinci/davinci_best_practices/davinci_best_practices_subflows_creating.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 17, 2023
section_ids:
  begin-the-subflow-name-with-subflow: Begin the subflow name with Subflow
  dont-use-css-even-for-ui-subflows: Don't use CSS, even for UI subflows
  dont-configure-subflows-as-pingone-flows: Don't configure subflows as PingOne flows
  add-color-coded-http-connectors-for-success-and-failure: Add color-coded HTTP connectors for success and failure
---

# Best practices for creating subflows

Use these best practices when creating a subflow.

## Begin the subflow name with **Subflow**

When naming a new subflow, begin the name with **Subflow**.

## Don't use CSS, even for UI subflows

Don't include CSS in subflows, even UI subflows. The subflow inherits the CSS styling from the parent flow, and controlling the CSS from that top-level flow is preferable.

## Don't configure subflows as PingOne flows

For subflows that connect to PingOne main flows, only configure the main flow as a PingOne flow, not the subflow. Learn more in [Editing flow settings](../flows/davinci_editing_flow_settings.html).

## Add color-coded HTTP connectors for success and failure

Use HTTP Connector nodes to send a JSON success or error response at the conclusion of the subflow. Give clear titles to these nodes and color them according to their purposes.

![A screen capture showing a subflow with success and failure JSON response nodes.](_images/cnd1665095357674.png)

Add a boolean value to each JSON Response node, specifying whether the subflow was successful. You can reference this value in the parent flow to branch based on how the subflow completed.

![A screen capture showing the boolean success value.](_images/hpi1665097186572.png)

---

---
title: Best practices for data sharing
description: Follow these best practices when passing data between a flow and a subflow.
component: davinci
page_id: davinci:davinci_best_practices:davinci_best_practices_subflows_data_sharing
canonical_url: http://docs.pingidentity.com/davinci/davinci_best_practices/davinci_best_practices_subflows_data_sharing.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 25, 2025
section_ids:
  passing-data-to-a-subflow: Passing data to a subflow
  returning-data-from-a-subflow: Returning data from a subflow
---

# Best practices for data sharing

Follow these best practices when passing data between a flow and a subflow.

## Passing data to a subflow

Add an input schema to the subflow to pass information from the parent flow to the subflow.

To see the input schema for the subflow, open the subflow, then click **Input Schema** in the upper-right corner of the flow canvas. You can add any number of required or optional properties to the subflow's input schema.

We recommend using a consistent format, such as camel case, for naming input schema variables. For example, `userName`, `emailAddress`, and so on.

If the input variable is required for the execution of the flow, mark it as **Required**. Alternatively, you can select **Require all defined parameters** to require all parameters.

In the subflow, you can reference the input schema parameters as `{{global.parameters.paramName}}`, where `paramName` is the name used in the input schema.

In the parent flow, the **Flow Conductor** node that launches the subflow includes fields for each parameter in the input schema. Map values from the parent flow to each of the subflow's input schema parameters.

## Returning data from a subflow

Add an output schema to the subflow to pass information back to the parent flow.

When you configure the **Send Success JSON Response** and **Send Error JSON Response** nodes at the end of the subflow, you can include one or more fields in the response. By adding these fields to the subflow's exit schema, you make them available in the parent flow after the subflow completes.

Click **⋮ > Output Schema** to open the output schema, then add one or more parameters to the properties section of the output code block. For example, this output schema outputs the errorMessage and selectedDeviceOtpEnabled properties:

```json
{
  "output": {
    "type": "object",
    "additionalProperties":true,
    "properties": {
      "errorMessage": {
        "type": "string",
        "displayName": "Error Message",
        "preferredControlType": "textField",
        "enableParameters": true,
        "propertyName": "errorMessage"
      },
      "selectedDeviceOtpEnabled": {
        "type":"bool"
      }
    }
  }
}
```

In the parent flow, you can reference parameters included in the output schema using the structure `{{local.nodeId.payload.output.property}}`, where `nodeId` is the node ID of the **Flow Conductor** node that launched the subflow and `property` is the property name. You can also find these parameters in the `{}` menu.

---

---
title: Best practices for using subflows
description: Follow these best practices when using subflows.
component: davinci
page_id: davinci:davinci_best_practices:davinci_best_practices_subflows_using
canonical_url: http://docs.pingidentity.com/davinci/davinci_best_practices/davinci_best_practices_subflows_using.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 22, 2024
section_ids:
  send-a-json-response-for-the-subflows-end-state: Send a JSON Response for the subflow's end state
  use-styling-rules-from-the-parent-flow: Use styling rules from the parent flow
  use-the-appropriate-capability-for-the-subflow: Use the appropriate capability for the subflow
  minimize-the-number-of-layers-subflows-calling-other-subflows: Minimize the number of layers (subflows calling other subflows)
  avoid-multiple-branches-leading-to-a-single-subflow: Avoid multiple branches leading to a single subflow
  dont-loop-subflows: Don't loop subflows
---

# Best practices for using subflows

Follow these best practices when using subflows.

## Send a JSON Response for the subflow's end state

If the subflow completes successfully, end the subflow with an HTTP node set to the **Send Success JSON Response** capability. In the parent flow, the flow conductor node that launched the subflow then evaluates to true.

If the subflow completes unsuccessfully, end the subflow with an HTTP node set to the **Send Error JSON Response** capability. In the parent flow, the flow conductor node that launched the subflow then evaluates to false.

The **Send Custom JSON Response** capability isn't recommended for use in subflows. If a subflow ends with a node that uses this capability, the flow conductor node that launched the subflow always evaluates to true.

If you plan to use a custom JSON response to conclude a subflow and you need to return a success or error condition, use a variable to store the condition, then use an evaluation node in the parent flow if you need to make branching decisions based on the variable's value.

For example, to use a custom variable in that HTTP node to indicate that the use case is an error response, use `IS_MFA_Required_Response=false`.

Redirect-based nodes, such as the **Return Success Response (Redirect)** capability of the **PingOne Authentication** connector, aren't recommended as terminal nodes in subflows. Redirect-based nodes redirect the browser, so the parent flow doesn't receive a response from the subflow if the subflow ends with a redirect-based node. You should put redirect-based nodes in the parent flow instead.

## Use styling rules from the parent flow

Avoid defining CSS in a subflow. Instead, set the styles in the flow settings of the parent flow. You can override the flow-level CSS by defining CSS for individual nodes if you need those nodes to have a different appearance.

## Use the appropriate capability for the subflow

When you invoke a subflow, use the appropriate capacity for the type of subflow:

* Use the **Invoke UI Subflow** capability if the subflow contains user interface nodes. Verify that every possible user path includes at least one user interface node.

* Use the **Invoke Subflow** capability if the subflow doesn't contain user interface nodes.

## Minimize the number of layers (subflows calling other subflows)

Because each subflow has a performance cost, avoid solutions that require subflows to reference other subflows. Don't exceed five levels of depth. Instead, design a single parent flow that references multiple subflows in sequence.

## Avoid multiple branches leading to a single subflow

If more than one branch leads to a single subflow node, the subflow might not consistently launch the correct number of times. If each branch must conclude with a subflow invocation, include a separate node for each invocation.

## Don't loop subflows

If your flow invokes a subflow, make sure that the subflow doesn't invoke the parent flow.

---

---
title: Branching
description: Use these best practices when creating branches within a flow.
component: davinci
page_id: davinci:davinci_best_practices:davinci_best_practices_branching
canonical_url: http://docs.pingidentity.com/davinci/davinci_best_practices/davinci_best_practices_branching.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 31, 2024
section_ids:
  build-the-main-path-along-the-top: Build the main path along the top
  branch-flows-using-one-logical-operator-per-node-or-exit-path: Branch flows using one logical operator per node or exit path
  branch-using-all-true-and-any-false: Branch using All true and Any false
  merge-branches-with-common-data-using-flow-instance-variables: Merge branches with common data using flow instance variables
  dont-build-flows-with-simultaneous-ui-paths: Don't build flows with simultaneous UI paths
  merge-parallel-branches-using-all-triggers-complete: Merge parallel branches using All triggers complete
  branch-before-teleport-nodes: Branch before Teleport nodes
  use-teleport-nodes-for-looping-flows: Use Teleport nodes for looping flows
  keep-teleport-destination-nodes-simple: Keep Teleport destination nodes simple
  handle-all-potential-false-branches: Handle all potential false branches
  use-only-any-true-operators-for-teleport-nodes-and-function-nodes-with-multiple-outcomes: Use only Any True operators for teleport nodes and function nodes with multiple outcomes
---

# Branching

Use these best practices when creating branches within a flow.

## Build the main path along the top

The most common success path should continue in a straight line to the right from the starting node. Alternate paths and error messages should branch downward from the main flow.

For example, consider the following flows. They are identical aside from layout and annotations:

Success path along the top (recommended):

![A screen capture of a sample flow with the success path along the top.](_images/dzg1664991079172.jpg)

Success path moving up and down (not recommended):

![A screen capture of a flow with the success path moving up and down, making it harder to follow.](_images/ial1664991244644.jpg)

## Branch flows using one logical operator per node or exit path

A logical operator is the circular branching point that is automatically created when you join one node to another. When you create a branch in a flow, make sure that there is exactly one logical operator per node or exit path.

If you branch after a simple node, the branches should all emerge from a single logical operator:

Branch originating from logical operator (recommended):

![A screen capture of a flow in which the initial node has one decision point and multiple branches.](_images/rkb1664991873081.png)

Branches originating from connector (not recommended):

![A screen capture of a flow in which the initial node has multiple decision points and multiple branches.](_images/xta1664992259221.png)

If you're branching from a node that has multiple exit paths, such as a Functions connector node, use one logical operator for each exit path:

Branches using one logical operator per exit path (recommended):

![A screen capture of a flow in which the node with multiple exit paths uses a separate logical operator for each exit path.](_images/fkn1672961055812.png)

Branches using one logical operator for multiple exit paths (not recommended):

![A screen capture of a flow in which the node with multiple exit paths uses a single logical operator for more than one exit path.](_images/nou1672961293426.png)

## Branch using **All true** and **Any false**

If creating a true/false branch, you should select the **All Triggers True** option for the true branch and **Any Trigger False** for the false branch.

![A screen capture showing a flow in which the first node's top branch is set to All Triggers True.](_images/vsd1664993229450.png)![A screen capture showing a flow in which the first node's bottom branch is set to Any Trigger False.](_images/nnc1664993604266.png)

|   |                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When you duplicate multiple nodes, the connecting option might default to **All Triggers True** in the duplicated nodes. Verify that the option is correct after you duplicate nodes. |

## Merge branches with common data using flow instance variables

When branches that perform similar tasks converge, you can make sure you reference the data from the correct branch by setting a flow instance variable to contain the data. Nodes that come after the flow converges can reference the flow instance variable.

This solution applies where the flow branches on a choice and can follow one path or the other, then converges back together. If your flow has similar data in parallel branches that run simultaneously, you don't need a flow instance variable.

![A screen capture in which two branches update a flow instance variable before merging.](_images/sxp1664996170278.png)

## Don't build flows with simultaneous UI paths

When branching a flow, make sure that the user can only encounter one user-facing node at a time. If the flow moves down multiple paths with UI nodes, some of these nodes will not display correctly.

## Merge parallel branches using **All triggers complete**

When merging branches that are executing in parallel and you want to be sure that both have completed their work, merge both branches into a connector with the **All Triggers Complete** option.

![A screen capture showing two branches in a flow, with an All Triggers Complete option connecting them both to the final node.](_images/ttu1664998990113.png)

## Branch before Teleport nodes

When using the Teleport connector's **Go to Start Node** or **Return to Calling Node** capabilities, branch before the node, not after. Branching after a Teleport connector that is configured to send the flow progression to a start node or calling node can skew your **Flow Analytics** data.

Branching before teleporting (supported):

![A screen capture of a flow that branches before a Teleport node](_images/wbw1691425893864.png)

Branching after teleporting (not supported):

![A screen capture of a flow that branches after a Teleport node](_images/qkh1691426214408.png)

## Use Teleport nodes for looping flows

When flows loop, the canvas can become cluttered with looping lines that make the flow hard to understand. To avoid this, use the Teleport connector. Define a start node at the point where the loop returns, and then use the Teleport connector to go to that start node to execute the loop.

Teleport nodes (recommended):

![A screen capture of a flow in which the looping is done using Teleport nodes.](_images/enk1664999620504.png)

Looping (not recommended):

![A screen capture of a flow in which the looping is done using long direct paths.](_images/iif1665000233168.png)

|   |                                                                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If your flow loops, you might want a field in one node to include a value from a node further to the right. When you are configuring the value for a field, you can enable the **Show all nodes** option to show values from all nodes, not just nodes to the left of the current node. |

## Keep Teleport destination nodes simple

Configure the logical operator that immediately follows a destination Teleport node to **All Triggers True**.

Make sure there is a one-to-one relationship between the teleport destination node and the node that follows it. You don't want to branch the flow immediately after the teleport destination node, and you should reuse teleport destination nodes rather that creating multiple destinations that lead to the same following node.

## Handle all potential false branches

If a node returns a false result but does not have a false branch as an output, the flow will fail, presenting a confusing experience for the end user and a challenge for troubleshooting.

To prevent this issue, you should make sure any node that can return a false result has a false output that presents an error message.

## Use only **Any True** operators for teleport nodes and function nodes with multiple outcomes

Some nodes should only use **Any True** operators:

* For a **Functions** connector with more than one outcome, such as **A == B (Multiple Conditions)**, use an **Any True** operator for each of the possible outcomes.

* For a teleport destination node, use an **Any True** operator.

---

---
title: Building flows
description: Use these best practices when creating a flow.
component: davinci
page_id: davinci:davinci_best_practices:davinci_best_practices_building_flows
canonical_url: http://docs.pingidentity.com/davinci/davinci_best_practices/davinci_best_practices_building_flows.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 3, 2024
section_ids:
  annotate-flows: Annotate flows
  add-meaningful-node-titles: Add meaningful node titles
  align-nodes-in-straight-lines-with-equal-spacing: Align nodes in straight lines with equal spacing
  use-a-single-start-node: Use a single start node
  host-images-outside-of-flows: Host images outside of flows
  use-teleport-nodes-for-large-flows: Use Teleport nodes for large flows
  include-an-id-for-input-elements: Include an ID for input elements
  use-an-appropriate-timeout-value: Use an appropriate timeout value
  validate-your-flows: Validate your flows
  use-automatic-user-id-mapping: Use automatic user ID mapping
  consider-flow-limits: Consider flow limits
  consider-flow-complexity-when-designing-and-testing: Consider flow complexity when designing and testing
  simulate-latency-using-the-http-connector: Simulate latency using the HTTP connector
  delete-unused-nodes: Delete unused nodes
  delete-unused-flows: Delete unused flows
---

# Building flows

Use these best practices when creating a flow.

## Annotate flows

Annotate your flows to make them easy to understand at a glance. These annotations might benefit another flow builder in your organization, or they might benefit you if you haven't worked on the flow in a while.

To add an annotation to the flow canvas:

![A screen capture of the DaVinci canvas with the CMD+Click context menu showing the Add Annotation option.](_images/ujr1671736758429.png)

1. CMD+Click (macOS) or CTRL+Click (Windows) a blank part of the canvas.

2. Click **Add Annotation**.

3. Click the annotation to enter the text and configure the appearance.

Use annotations to describe what happens in the main steps of the flow. Although there are rare occasions where a single node should have its own annotation, in most cases, you should use one annotation for each logical grouping of nodes.

![A screen capture showing a flow with an annotation near each major portion of the flow.](_images/tem1664574860660.jpg)

## Add meaningful node titles

On the **Settings** tab for each node, set the **Node Title** to a meaningful name that describes or identifies each node. This name appears in the flow canvas and, combined with the annotations, makes it easier to read the flow.

For example, consider the following flows. They are identical aside from node titles and annotations.

Recommended:

![A screen capture showing an annotated flow with informative node titles.](_images/nfk1664577041669.png)

Not recommended:

![A screen capture showing an un-annotated flow with uninformative note titles.](_images/smr1664576189807.jpg)

## Align nodes in straight lines with equal spacing

To make it easier to see the connections and overall structure, align your nodes in neat rows and columns. Avoid overlapping nodes and clustering them close together.

![A screen capture showing two versions of a simple flow, with the first version neatly aligned and the second version sloppily aligned.](_images/hmk1667923303470.png)

## Use a single start node

Begin your flow with a single node that serves as a clear starting point. If you include loops in your flow, don't loop back to this start node. Instead, loop back to a later node.

|   |                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------- |
|   | Do not begin the flow with a **Teleport Start** node. Routing to an initial **Teleport Start** node can cause flow timeout issues. |

## Host images outside of flows

Large images and assets should be hosted on a CDN and referenced by the flow settings using CSS, not packaged within the flow.

## Use Teleport nodes for large flows

If you are creating a very large flow, you can use Teleport nodes to connect different sections of the flow. This makes the flow more readable by breaking it down into discrete sections. It can also let you reuse some sections of the flow rather than duplicating content.

|   |                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Configure the logical operator that immediately follows a destination Teleport node to **All Triggers True**. Use a different node following each destination Teleport node; don't create flow patterns where multiple destination Teleport nodes connect directly to the same node. |

## Include an ID for input elements

If you're including an input element in an HTML or other user-facing node, include an ID:

```html
<div>
     <label>Bar: <input id="bar" type="text" /></label>
</div>
```

You can reference the value entered by the user later in the flow using this ID. The ID must be unique across the entire flow.

## Use an appropriate timeout value

The **Flow Timeout** setting specifies the maximum runtime for a flow. You should set a value that will not rush your users, but will prevent excessive flow runtimes. Values between 300 (5 minutes) and 900 (15 minutes) are appropriate for most flows. Do not use a value greater than 7200 (2 hours).

## Validate your flows

DaVinci includes a **Validate Flow** option that identifies errors that will break your flow as well as smaller issues that could make it harder to maintain. Use this feature regularly when developing and testing your flows, and fix the errors it identifies before you deploy the flows. Learn more in [Validating a flow](../flows/davinci_validating_a_flow.html).

## Use automatic user ID mapping

By default, when a user authenticates during a flow, DaVinci automatically tracks the user ID and authentication methods and passes them to the PingOne Authentication connector to create a session. Use this default user ID mapping unless you are creating a session for someone other than the authenticated user, such as in impersonation and delegation use cases.

## Consider flow limits

There are some limitations in flow creation, such as a maximum number of node exections and a maximum number of saved versions of each flow. Review these limitations before creating flows, as they could affect the way you create and update your flows. Learn more in [Flow limits](../flows/davinci_flow_limits.html).

## Consider flow complexity when designing and testing

The more complex the goal of a flow is, the more planning and testing is required to ensure that the flow works correctly. When planning a flow, bear in mind that some tasks and elements will increase the complexity and testing requirements:

* Parallel branches that run simultaneously

* Large amounts of data processing

* Looping flows

* Large flows

* API normalization

## Simulate latency using the HTTP connector

If you want to simulate latency in a flow, use the **Simulate Latency** capability of the HTTP connector instead of using custom code. Use this node only immediately after a UI node.

## Delete unused nodes

If you don't want an existing node to be part of the flow, delete it entirely instead of disconnecting or disabling it.

## Delete unused flows

If you don't want to use a flow, delete it to make it easier to find relevant flows.

---

---
title: Change management
description: Follow these best practices to manage and track changes to your flows.
component: davinci
page_id: davinci:davinci_best_practices:davinci_best_practices_change_management
canonical_url: http://docs.pingidentity.com/davinci/davinci_best_practices/davinci_best_practices_change_management.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 23, 2024
section_ids:
  use-flow-aliases-for-version-control: Use flow aliases for version control
  export-flows-and-subflows-for-source-control: Export flows and subflows for source control
---

# Change management

Follow these best practices to manage and track changes to your flows.

## Use flow aliases for version control

When your flow reaches a milestone, add an alias to the flow version with a name, deployment status, and version number, such as `Dashboard-PROD_v.117`.

1. Open the flow.

2. Go to **More options ( [icon: ellipsis-v, set=fa]) > Flow Versions**.

3. Find the correct version and go to **... > Set Version Alias**.

4. Enter the alias and click **Save**.

![A screen capture showing flows with the environment and version included in their names.](_images/ozv1665163232644.png)

Configure your application's flow policy to use the specific version of the flow instead of the latest version. This allows you to continue developing your flow without affecting production.

![A screen capture of an application's flow policy, showing that the selected version of the flow is not the latest version.](_images/bvi1665160060800.png)

When you change the flow, update the version number in the name, as shown in the following examples.

![A screen capture showing a flow renamed to include the version number.](_images/ley1665160860038.png)

## Export flows and subflows for source control

With each version change of the flow, go to the menu and export the flow as a JSON file:

1. In the upper-right corner of the flow editor, click the **More Options ( [icon: ellipsis-v, set=fa])** icon and click **Download Flow JSON**.

2. Save the file.

3. Follow your organization's source control best practices for maintaining the file.

   |   |                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------- |
   |   | Do not post flows or subflows to externally-accessible locations to protect secure information. |

---

---
title: Collaborating
description: Use these best practices when collaborating with other flow builders to create or update a flow.
component: davinci
page_id: davinci:davinci_best_practices:davinci_best_practices_collaborating
canonical_url: http://docs.pingidentity.com/davinci/davinci_best_practices/davinci_best_practices_collaborating.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 22, 2024
section_ids:
  use-subflows: Use subflows
  rename-flows-to-show-working-status: Rename flows to show working status
---

# Collaborating

Use these best practices when collaborating with other flow builders to create or update a flow.

## Use subflows

If you can break a large flow into separate, smaller flows (subflows), each flow builder can work independently. See the [Subflows](davinci_best_practices_subflows.html) section for best practices.

## Rename flows to show working status

Rename the flow with your initials while you are working in the flow, and change the name back to the original name when you are finished. This will let other flow builders know to wait until you are finished with your changes.

---

---
title: Creating variables
description: To preserve variable capacity and reduce administrative overhead, follow these best practices when creating DaVinci variables.
component: davinci
page_id: davinci:davinci_best_practices:davinci_best_practices_variables
canonical_url: http://docs.pingidentity.com/davinci/davinci_best_practices/davinci_best_practices_variables.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 9, 2023
section_ids:
  reuse-variables-when-possible: Reuse variables when possible
  standardize-your-variable-names: Standardize your variable names
  choose-an-appropriate-variable-context: Choose an appropriate variable context
  use-secret-variables-for-sensitive-information: Use secret variables for sensitive information
---

# Creating variables

To preserve variable capacity and reduce administrative overhead, follow these best practices when creating DaVinci variables.

## Reuse variables when possible

Your environment can contain up to [200 variables](../flows/davinci_flow_limits.html). To limit the number of redundant variables in your company, before creating a new variable, review the **Variables** tab to see if a variable has been defined for the value that you need. If a variable exists and satisfies the flow requirements, you can reuse that variable in your flow.

When reviewing existing variables for reuse:

* Read the **Name** and **Description** fields to guide you to potential matches.

* Confirm that the **Context**, **Data Type**, and **Value** parameters work for your flow design.

* Click **Edit** on a variable to review its **Mutable**, **Min**, and **Max** configurations.

|   |                                                   |
| - | ------------------------------------------------- |
|   | Flow instance variables are always safe to reuse. |

## Standardize your variable names

To help flow builders quickly identify which variables pertain to their desired values, standardize your variable names and description requirements, and then communicate these standards to all DaVinci stakeholders. You can define standards for individual variables or variable categories.

You can find examples of standardized variable names in [Common flow variables](../flows/davinci_common_flow_variables.html).

## Choose an appropriate variable context

To allow a variable to be used in as many flows as possible, select the most general context that applies to the purpose of the variable. Variable contexts apply as follows:

* **Company Context**

  With this context, the variable has one definition for all flows and users. Consider selecting **Company Context** for variables that represent your company name or a company-wide ID.

* **User Context**

  With this context, the variable has a separate value for each user. Consider selecting **User Context** for variables that represent user-specific data, such as a user ID or status.

* **Flow Instance Context**

  With this context, the variable's value can be set upon execution of a flow that contains the variable. That value is unique to that execution of the containing flow. The variable can also inherit a value from the **Variables** tab, if no value is set by the execution of the containing flow.

  Consider selecting **Flow Instance Context** for variables that represent information that might change from one flow execution to the next (even for the same user), such as a time value.

* **Flow Context**

  With this context, the variable is tied to a specific flow and has a persistent value. This value is set by the latest of either an execution of its containing flow or an update to the **Variables** tab. Consider selecting **Flow Context** for variables that represent values that are common to all users within a flow, such as a task ID or task-related information.

For more information on variable context, see [Variables](../variables/davinci_variables.html).

## Use secret variables for sensitive information

Some values, such as API keys, client secrets, and access tokens, are required for some flows to function but shouldn't be readily visible. You should store these values in secret variables.

Secret variables are a type of company context variable. Their values can be used in the HTTP connector's Make REST API call capability, in the `Headers` and `Body Parameters` sections. Their values are not visible in logs, analytics, API queries, flow JSON files, or to other DaVinci administrators. Administrators can replace the value for a secret variable, but they cannot view the current value after it's been saved. Saving sensitive values in secret variables makes them more secure and simplifies administration by putting all of the values in one place rather than in multiple connector configurations.

Learn more in [Variables](../variables/davinci_variables.html) and [Adding a variable](../variables/davinci_adding_a_variable.html).

---

---
title: DaVinci Best Practices
description: This document describes best practices for creating and maintaining flows in DaVinci.
component: davinci
page_id: davinci:davinci_best_practices:davinci_best_practices
canonical_url: http://docs.pingidentity.com/davinci/davinci_best_practices/davinci_best_practices.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 22, 2024
---

# DaVinci Best Practices

This document describes best practices for creating and maintaining flows in DaVinci.

DaVinci flows are a powerful tool for orchestrating your organization's identity services. However, because DaVinci flows are versatile, it can be difficult to create flows that work optimally for the user, for the people maintaining the flows, and from the perspective of security.

These best practices can help you avoid common problems, improve performance and reliability, and simplify future improvements.

* [Building flows](davinci_best_practices_building_flows.html)

* [Branching](davinci_best_practices_branching.html)

* [Creating variables](davinci_best_practices_variables.html)

* [Collaborating](davinci_best_practices_collaborating.html)

* [Performance Tuning](davinci-best-practices-performance-tuning.html)

* [Subflows](davinci_best_practices_subflows.html)

  * [Best practices for creating subflows](davinci_best_practices_subflows_creating.html)

  * [Best practices for using subflows](davinci_best_practices_subflows_using.html)

  * [Best practices for data sharing](davinci_best_practices_subflows_data_sharing.html)

* [Debugging and analytics](davinci_best_practices_debugging_and_analytics.html)

* [Change management](davinci_best_practices_change_management.html)

* [Using custom code safely](davinci_best_practices_custom_code.html)

* [Gathering support information](davinci_best_practices_gathering_support_info.html)

* [Handling sensitive data](davinci-best-practices-sensitive-data.html)

---

---
title: Debugging and analytics
description: Use these best practices when troubleshooting issues with flows and reviewing flow analytics data.
component: davinci
page_id: davinci:davinci_best_practices:davinci_best_practices_debugging_and_analytics
canonical_url: http://docs.pingidentity.com/davinci/davinci_best_practices/davinci_best_practices_debugging_and_analytics.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 23, 2024
section_ids:
  review-the-flow-execution-log: Review the flow execution log
  use-debug-mode-to-view-additional-details: Use debug mode to view additional details
  use-node-ids-to-track-nodes: Use Node IDs to track nodes
  review-api-responses: Review API responses
  use-the-error-message-connector: Use the Error Message connector
  send-flow-data-to-an-external-analytics-tool: Send flow data to an external analytics tool
  add-the-flow-analytics-connector-to-the-flow: Add the Flow Analytics connector to the flow
  correlate-information-using-available-ids: Correlate information using available IDs
---

# Debugging and analytics

Use these best practices when troubleshooting issues with flows and reviewing flow analytics data.

## Review the flow execution log

Open your flow in PingOne DaVinci.

In the lower left corner of the flow editor, click **Analytics**.

This opens the **Flow Analytics** window. You can change the date range for the executions of your flow. You can also click **Refresh** to load information for your latest flow executions.

![A screen capture showing the date range selector.](_images/nxy1665172948492.png)

Hover over the graph to see the flow count for the selected timeframe.

![A screen capture showing the flow count for a flow.](_images/wts1665173186505.png)

In the **Events Logs** section, flow executions are displayed in chronological order with the most recent on top. You can search for a specific flow execution using the **Flow Execution ID**, **User ID**, **User Name**, **Correlation ID**, or **Transaction ID**. After searching or scrolling to locate a flow execution, you can select it to see its details.

![A screen capture showing the event logs.](_images/davinci-analytics-event-log-2.png)

After you select a flow execution, you can see **Flow Duration** and connector details such as **Node Title**, **Connector**, and **Capability**. Expand the view or scroll to the right to see the **Date** and **Event Message** columns. If an error occurred during a node execution, an error icon displays next to the node title. You can mouse-over this icon to display error details, or click any event to highlight the corresponding node.

In the canvas view, the nodes show analytic information for the flow execution you selected. Hover over a node to see the related events in the **Flow Analytics** window.

![A screen capture showing the canvas view.](_images/xwa1665174433698.png)

Click an event in the log to expand the JSON request or response for the event. This allows you to see the information that passed through the flow, including error codes and messages. The types of events included in the analytics depend on the [log level](../flows/davinci_editing_flow_settings.html) of the flow.

![A screen capture showing the expanded event information.](_images/Analytics-json-details-2.png)

If there are any errors, you might see a **Send Error Response** that will show you the error encountered.

## Use debug mode to view additional details

Use the **Debug Mode** flow setting to capture additional details in the **Flow Analytics** log. Enabling debug mode provides additional insight into the properties, parameters, and connector inputs between nodes in the flow.

In the upper-right corner of the flow editor, click the **More Options ( [icon: ellipsis-v, set=fa])** icon and select **Flow Settings**. On the **Logging** tab, in the **Log Level** list, select a logging level. **Debug** captures the most detailed information.

![A screen capture showing the Flow Settings option for a flow.](_images/xsb1665427844061.png)![A screen capture showing a flow with the Log Level set at Debug.](_images/DV_best_practice_debug_logging_settings.png)

|   |                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------ |
|   | When **Debug Mode** is selected, the logs can include sensitive data, such as credentials or personal information. |

If the flow could contain sensitive information, use the **Scrub Sensitive Information** and **Sensitive Information Fields** options to exclude fields with sensitive information from the logs.

When you are done analyzing the flow, reset the log level to **Info** to improve performance.

## Use Node IDs to track nodes

Turn on node IDs to identify nodes in your flow:

1. Open your flow in PingOne DaVinci.

2. In the upper-right corner of the flow editor, click the **More Options ( [icon: ellipsis-v, set=fa])** icon and click **Show Node ID**.

When you use variables to populate capability properties in your flow, you can hover over the variable to see the ID of the node that the variable comes from. With **Show Node ID** enabled, you can check the source of the variable to make sure it's correct.

![A screen capture of a flow showing the connection between a displayed Node ID and the source of a variable.](_images/jwt1665429991778.png)

|   |                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------- |
|   | Always make sure your variables point to the expected node ID after you copy or clone nodes or flows. |

## Review API responses

Learning how to read API responses is also useful for troubleshooting in PingOne DaVinci.

If you scroll to the top of an event, you can review the properties of the API call and the schema for the connector.

## Use the Error Message connector

The Error Message connector allows you to display custom error messages in a DaVinci flow and is useful for handling errors consistently in a production flow.

For debugging a test flow, use the HTTP connector with the **Custom HTML Message** capability to capture and display errors.

![A screen capture showing the Custom HTML message option.](_images/uzx1665432439401.png)

When using the HTTP connector, use the **skerrormessage** SK-component to capture and show DaVinci-specific error information.

There are two ways to display the **skerrormessage**.

Use a basic message:

1. In your flow, add an HTTP connector and select the **Custom HTML Message** capability. Select the node on the canvas.

2. In the **Message** field, click **{}** and select the **skerrormessage** variable from the **SK-Component** source.

   ![A screen capture showing the skerrormessage component.](_images/adb1665432811037.png)

Use a custom HTML template:

1. In your flow, add an HTTP connector and select the **Custom HTML Template** capability. Select the node on the canvas.

2. In the **Message** field, click **{}** and select the **skerrormessage** variable from the **SK-Component** source.

For example, if you want to capture the **skerrormessage** on a password validation, HTML similar to the following may be used:

```html
<div id="password-validation-message"
  class="errormsg feedback--error sk-alert sk-alert-danger has-text-danger has-background-danger-light text-center"
  style="color:red" data-skcomponent="skerrormessage" data-skerrorid="password">
</div>
<div data-skcomponent="skerror"
  class="feedback feedback--error sk-alert sk-alert-danger has-text-danger has-background-danger-light text-center"
  style="color:red" data-id="feedback" data-skvisibility="">
</div>
```

## Send flow data to an external analytics tool

You can use the HTTP connector's **Make REST API Call** capability to send DaVinci log data to an external log aggregator or analytics tool.

1. In your flow, add an **HTTP connector** and select the **Make REST API Call** capability. Select the node on the canvas.

2. In the **Headers** section, click the **Add (+)** icon.

3. In the **Key** field, enter `x-log-key`.

4. In the **Value** field, enter the API key.

   ![A screen capture showing an HTTP connector configured to send data to an external analytics tool.](_images/acg1665505535808.png)

## Add the Flow Analytics connector to the flow

The Flow Analytics connector enhances the standard analytics view with cumulative results. Use the Flow Analytics connector in key places in your flow to collect the information that's most important to you.

![A screen capture showing the configuration for a flow analytics connector.](_images/nib1665506964200.png)![A screen capture showing the placement of two flow analytics connector nodes in a flow.](_images/ypz1665507353918.png)

## Correlate information using available IDs

Multiple ID values display in the analytics and in webhook events at all logging levels. You can use these IDs to correlate events between products and gain a clearer understanding of issues you encounter.

| **Identifier**          | **Description**                                                                                                                                                                                                                                                                                                                                                         | **Purpose**                                                                                                    |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `correlationId`         | A `correlationId` is generated for each API call. A node that communicates with PingOne uses one or more API calls, such as `/as/authorize`, `/policy/:policyId/start`, or `/capabilities/customHTMLTemplate`.                                                                                                                                                          | Lets you trace a specific HTTP request execution within PingOne that spans multiple PingOne microservices.     |
| `transactionId`         | A `transactionId` is assigned for each flow execution across all services.For example, if a PingOne flow is initiated from the OAuth authorization endpoint, the `transactionId` would be set at the first step and then passed to DaVinci. Even if the same flow execution returns to PingOne, the same `transactionId` is maintained.                                 | Used to trace a flow execution across all PingOne services.                                                    |
| `externalTransactionId` | A `externalTransactionId` is a unique identifier set outside of PingOne by an external application. It's then passed to PingOne and DaVinci and carried throughout the flow execution.For example, flows executed as part of PingFederate integration are assigned an `externalTransactionId` by PingFederate, and that value is tracked throughout the flow execution. | Used to trace the flow execution across all PingOne and external services when an external system is involved. |
| `sessionId`             | A `sessionId` identifies a unique user session. It's set when the session is created in PingOne.                                                                                                                                                                                                                                                                        | Used to trace user sessions across flow executions.                                                            |
| `externalSessionId`     | An `externalSessionId` identifies a unique user session. It's set by an external application such as PingFederate and passed to PingOne and DaVinci.                                                                                                                                                                                                                    | Used to trace user sessions across flow executions and external applications.                                  |

---

---
title: Gathering support information
description: Use these best practices to gather information for working with Ping support to resolve issues.
component: davinci
page_id: davinci:davinci_best_practices:davinci_best_practices_gathering_support_info
canonical_url: http://docs.pingidentity.com/davinci/davinci_best_practices/davinci_best_practices_gathering_support_info.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 27, 2025
section_ids:
  gather-environment-information: Gather environment information
  gather-flow-specific-information: Gather flow-specific information
---

# Gathering support information

Use these best practices to gather information for working with Ping support to resolve issues.

## Gather environment information

Find the environment and organization details in PingOne:

1. In the PingOne admin console, go to **Settings > Environment Properties**.

2. Copy the **Environment ID** for later reference.

3. Copy the **Organization ID** for later reference.

## Gather flow-specific information

If your issue involves a specific flow, gather information about the flow:

1. Export the flow as JSON:

   1. In DaVinci, go to **Flows**.

   2. Click the flow you want to export.

   3. Click **⋮ > Download Flow JSON**.

   4. Clear **Include Variable Values**.

   5. Click **Export**.

2. Capture an HTTP trace of the flow, following the [HTTP tracing best practices](https://support.pingidentity.com/s/article/HTTP-Tracing).

3. If the flow is a sample flow created by Ping, note any customization you applied to the flow.

4. If the flow is custom, describe the use case, the intended method of operation, and, if possible, the section or sections causing problems.

5. Update the logging settings to gather additional information:

   1. In DaVinci, go to **Flows**.

   2. Click the flow, then click **⋮ > Flow Settings**.

   3. Click the **Logging** tab.

   4. Set the **Log Level** to **Debug**.

   5. If the flow normally contains sensitive information, select **Scrub Sensitive Information**.

6. If you can identify specific flow executions or nodes where the problem occurs, gather information about the specific error:

   1. In DaVinci, go to **Flows**.

   2. Click the flow.

   3. Click **Analytics**.

   4. In the timeframe selector, select a timeframe that includes the relevant executions.

   5. In the **Events Logs** section, select a search parameter and locate a flow execution affected by the error.

   6. Note the **Flow Execution ID**.

   7. If possible, note the **User ID** or **User Name** of the user associated with the flow execution.

   8. If you can identify the node or nodes causing the error, take a screenshot of the node. Locate the response event for the node and note any additional details such as error codes or messages. If it's a PingOne connector, note the **Correlation ID** for the node execution.

---

---
title: Handling sensitive data
description: Use these best practices to protect sensitive data from internal or external exposure.
component: davinci
page_id: davinci:davinci_best_practices:davinci-best-practices-sensitive-data
canonical_url: http://docs.pingidentity.com/davinci/davinci_best_practices/davinci-best-practices-sensitive-data.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 31, 2024
section_ids:
  use-an-appropriate-logging-level: Use an appropriate logging level
  manage-davinci-access: Manage DaVinci access
  use-sensitive-fields-to-keep-sensitive-data-out-of-analytics: Use sensitive fields to keep sensitive data out of analytics
  use-secret-variables-for-sensitive-information: Use secret variables for sensitive information
  exclude-variables-from-exported-flows: Exclude variables from exported flows
---

# Handling sensitive data

Use these best practices to protect sensitive data from internal or external exposure.

## Use an appropriate logging level

Logging tracks various system events and requires a certain amount of system resources. More verbose logging provides additional information but consumes more system resources, which impacts the flow's overall performance.

DaVinci supports multiple logging levels:

* **Error** (default): Gathers basic information about the flow start and any errors encountered.

* **None**: Performs no logging.

* **Info**: Gathers information about every node that runs.

* **Debug**: Gathers detailed information about every node that runs.

You should leave flow logging set to **Error** unless you're actively attempting to diagnose an issue, and you should set flow logging back to **Error** as soon as you're done.

You can update the log level by opening the flow and clicking **More options ( [icon: ellipsis-v, set=fa]) > Flow Settings**, then clicking the **Logging** tab. Learn more in [Editing flow settings](../flows/davinci_editing_flow_settings.html).

## Manage DaVinci access

Administrative users in DaVinci are created through PingOne. When you add admin users, only give these users the necessary permissions for their roles, and only for the necessary environments. This prevents users from accidentally or intentionally making changes to flows or environments beyond the scope of their responsiblities.

Regularly review the list of admin users to ensure no admin user has unnecessary access.

## Use sensitive fields to keep sensitive data out of analytics

By default, DaVinci removes the values of known sensitive fields from analytics. Learn more about the fields that are automatically scrubbed in [Viewing flow analytics](../flows/davinci_viewing_flow_analytics.html).

If you want to add additional sensitive fields, update the flow settings to scrub their values using the **Scrub Sensitive Information** and **Sensitive Information Fields** fields. Learn more in [Editing flow settings](../flows/davinci_editing_flow_settings.html).

## Use secret variables for sensitive information

Some values, such as API keys, client secrets, and access tokens, are required for some flows to function but shouldn't be readily visible. You should store these values in secret variables.

Secret variables are a type of company context variable. Their values can be used in the HTTP connector's Make REST API call capability, in the `Headers` and `Body Parameters` sections. Their values are not visible in logs, analytics, API queries, flow JSON files, or to other DaVinci administrators. Administrators can replace the value for a secret variable, but they cannot view the current value after it's been saved. Saving sensitive values in secret variables makes them more secure and simplifies administration by putting all of the values in one place rather than in multiple connector configurations.

Learn more in [Variables](../variables/davinci_variables.html) and [Adding a variable](../variables/davinci_adding_a_variable.html).

## Exclude variables from exported flows

When you export a flow as JSON, deselect the **Include Variable Values** so that the JSON does not include the values of company or flow variables that are used in the flow. Learn more in [Exporting a flow](../flows/davinci_exporting_a_flow.html).

---

---
title: Performance Tuning
description: Use these best practices to enhance the latency, throughput, and resource efficiency of your flows while minimizing downtime and risk.
component: davinci
page_id: davinci:davinci_best_practices:davinci-best-practices-performance-tuning
canonical_url: http://docs.pingidentity.com/davinci/davinci_best_practices/davinci-best-practices-performance-tuning.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 31, 2024
section_ids:
  use-an-appropriate-logging-level: Use an appropriate logging level
  minimize-the-number-of-nodes: Minimize the number of nodes
  avoid-unhandled-execution-paths: Avoid unhandled execution paths
  minimize-the-payload-size: Minimize the payload size
  minimize-loop-iterations: Minimize loop iterations
  follow-good-coding-practices-in-custom-functions: Follow good coding practices in custom functions
---

# Performance Tuning

Use these best practices to enhance the latency, throughput, and resource efficiency of your flows while minimizing downtime and risk.

## Use an appropriate logging level

Logging tracks various system events and requires a certain amount of system resources. More verbose logging provides additional information but consumes more system resources, which impacts the flow's overall performance.

DaVinci supports multiple logging levels:

* **Error** (default): Gathers basic information about the flow start and any errors encountered.

* **None**: Performs no logging.

* **Info**: Gathers information about every node that runs.

* **Debug**: Gathers detailed information about every node that runs.

You should leave flow logging set to **Error** unless you're actively attempting to diagnose an issue, and you should set flow logging back to **Error** as soon as you're done.

You can update the log level by opening the flow and clicking **More options ( [icon: ellipsis-v, set=fa]) > Flow Settings**, then clicking the **Logging** tab. Learn more in [Editing flow settings](../flows/davinci_editing_flow_settings.html).

## Minimize the number of nodes

The number of nodes that run in an execution impacts the flow execution time. You should take steps to minimize the number of nodes that run:

* Divide larger flows into subflows when possible.

* Remove any unnecessary nodes from the flow.

* Skip nodes that aren't needed in a given execution.

## Avoid unhandled execution paths

If a flow takes a path that's not handled by existing nodes, it can result in flow timeouts. For example, if a flow contains a function connector to compare two values and branches based on which value is larger, but doesn't contain any nodes to handle the scenario where the values are equal, it can time out.

You should verify that error cases are handled as soon as they occur. Ensure that all execution paths for connectors are explicitly defined, and all success and failure paths are handled.

## Minimize the payload size

Any data that's used during the flow requires computational resources, which slows the flow. Remove any unnecessary references to large data, including variables, images, and the output from custom functions.

## Minimize loop iterations

If your flow contains loops, minimize the number of times the loops are repeated, and ensure that every loop has defined exit conditions.

## Follow good coding practices in custom functions

If your flow uses custom functions, minimize the use of long-running loops, and avoid creating custom functions with deeply nested JSON structures.

---

---
title: Subflows
description: Use these best practices when creating and using subflows (flows invoked by other flows).
component: davinci
page_id: davinci:davinci_best_practices:davinci_best_practices_subflows
canonical_url: http://docs.pingidentity.com/davinci/davinci_best_practices/davinci_best_practices_subflows.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 21, 2023
section_ids:
  ui-subflows: UI subflows
  non-ui-subflows: Non-UI subflows
---

# Subflows

Use these best practices when creating and using subflows (flows invoked by other flows).

A subflow is a normal flow that does not represent a complete identity orchestration solution or user experience. Instead, it's designed to be used as part of a larger parent flow. For example, a complex sign-on flow might reference subflows to handle password reset requests and user registration. Subflows make flow maintenance and reuse easier.

|   |                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------- |
|   | To invoke a subflow, you must use the [Flow Conductor](http://docs.pingidentity.com/connectors/flow_conductor_connector.html) connector. |

There are two types of subflows.

## UI subflows

Subflows that include UI components (for example, an HTTP connector), such as:

* Magic link flow

* Login/authentication

## Non-UI subflows

Subflows that don't include UI components. These subflows perform backend functions such as:

* Common API calls (for example, create a user or reset a password)

* Computational functions

---

---
title: Using custom code safely
description: Follow these best practices to use custom code in your flows.
component: davinci
page_id: davinci:davinci_best_practices:davinci_best_practices_custom_code
canonical_url: http://docs.pingidentity.com/davinci/davinci_best_practices/davinci_best_practices_custom_code.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 10, 2024
section_ids:
  risks: Risks
  code-execution-location: Code Execution Location
  recommendations: Recommendations
---

# Using custom code safely

Follow these best practices to use custom code in your flows.

Custom code is a feature that lets you create your own code to include in DaVinci flows. It's available in multiple connectors and capabilities, including:

* Custom HTML template **script** field

* Custom Functions

* Code Snippet fields

## Risks

Because custom code fields can run any code provided, they carry additional security risks.

Learn more about the risks of custom code in the [Open Worldwide Application Security Project resources](https://owasp.org/www-project-top-10-client-side-security-risks/).

## Code Execution Location

When you include custom code, it either runs on the server side or the client side, depending on the node type:

* The **Code Snippet** connector and the **Custom Function** capability of the **Functions** connector run code on the server side.

* Script fields in any other node with a customizable HTML template are run on the client side.

You need to consider where the code runs when designing and building flows. Because client-side code can be viewed, you shouldn't include sensitive values in code that is run on the client side.

In addition, variable and parameter values included in custom code have their values added in different ways, which can impact your flow design.

* Variable values included using the `{{global.variables.variableName}}` structure have the value substituted on the server side before the code runs, replacing the structure with the unescaped value or, if the variable value is a object, a stringified version. This means that, if you want to include non-static HTML in your custom code, you should use variables and not parameters.

* Parameters included using the `{{parameterName}}` structure are sent as an additional argument to the client, where Handlebars uses it to process the template. This does escape any special characters in the parameter value.

If you want to use an object or a portion of an object in custom code, you can use the following methods, ordered from most to least secure:

1. Add the input properties to the node's input schema and map the values from the source object.

2. If the number of inputs can't be known ahead of time, create an input property to pass the object, then use Handlebars #each, #with, and lookup helpers to access the individual values.

3. Use an alternate syntax for the object property you want to reference. Replace the periods in the object name with slashes. For example, `{{myUser/category/example}}`.

4. If you want to use JavaScript instead of Handlebars to add content, you can use input parameters using this format: `(const myObject = JSON.parse({{myInput}});)` or use DaVinci parameter substitution using this format: `(const myObject = JSON.parse({{local.aNodeId.aCapability.output.someObject}});)`.

## Recommendations

Follow these recommendations when using custom code fields:

* Make sure that only trusted users can access DaVinci to add custom code.

* Make sure that any custom code you plan to use is reviewed before it is added to user-facing flows, regardless of whether the custom code was produced by you or by a third party. You can use [Semgrep](https://semgrep.dev/docs/getting-started/quickstart) as a tool for reviewing your code for security vulnerabilities.

* Make sure that sensitive or private information isn't exposed by any variables or run-time data processed by custom code.