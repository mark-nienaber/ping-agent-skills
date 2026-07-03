---
title: BPMN 2.0 and workflow tools
description: Use BPMN 2.0 to define PingIDM workflows and business processes with Groovy or JavaScript scripts for provisioning and identity management tasks
component: pingidm
version: 8.1
page_id: pingidm:workflow-guide:about-workflow-tools
canonical_url: https://docs.pingidentity.com/pingidm/8.1/workflow-guide/about-workflow-tools.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Workflows", "BPMN", "BPM", "Groovy", "JavaScript", "Scripting"]
section_ids:
  workflow_limitations: Workflow limitations
---

# BPMN 2.0 and workflow tools

The [Business Process Model and Notation (BPMN)](https://www.omg.org/spec/BPMN/) is a standard maintained by the [Object Management Group (OMG)](https://omg.org/).

Use BPMN 2.0 to add workflow and business process artifacts to IDM for provisioning and other identity management tasks. You can create workflow definitions with a text editor or a compatible tool. Workflow scripts can use Groovy or JavaScript.

Scripts in BPMN 2.0 XML files can access the following variables:

* `openidm`

* `identityServer`

* `console`

For example, to log a message with Groovy:

```groovy
console.log('my message')
```

|   |                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | For more information about graphical notations and XML representations for BPMN 2.0, refer to the [Flowable BPMN 2.0 Constructs](https://flowable.com/open-source/docs/bpmn/ch07b-BPMN-Constructs/) documentation. |

## Workflow limitations

IDM doesn't support the following constructs:

* [Mule task](https://flowable.com/open-source/docs/bpmn/ch07b-BPMN-Constructs/#mule-task)

* [Camel task](https://flowable.com/open-source/docs/bpmn/ch07b-BPMN-Constructs/#camel-task)

The following reserved terms can't be used as variable names:

* `out`

* `out:print`

* `lang:import`

* `context`

* `elcontext`
