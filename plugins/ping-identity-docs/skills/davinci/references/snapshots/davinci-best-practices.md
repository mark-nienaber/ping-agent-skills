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
