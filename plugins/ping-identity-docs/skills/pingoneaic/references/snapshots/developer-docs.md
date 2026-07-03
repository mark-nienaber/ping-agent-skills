---
title: Action
description: Use the Action verb to perform predefined operations on Advanced Identity Cloud REST API resources via HTTP POST
component: pingoneaic
page_id: pingoneaic:developer-docs:crest/action
canonical_url: https://docs.pingidentity.com/pingoneaic/developer-docs/crest/action.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  parameters: Parameters
---

# Action

Actions are a means of extending Advanced Identity Cloud REST APIs and are defined by the resource provider. The actions you can use depend on the implementation.

The standard action indicated by `_action=create` is described in [Create](create.html).

## Parameters

You can use the following query string parameters. Other parameters depend on the specific action implementation:

| Parameter                  | Description                                                                                                                                                                                                                                                                              |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_fields=field[,field...]` | Return only the specified fields in the body of the response.The `field` values are JSON pointers. For example, if the resource is `{"parent":{"child":"value"}}`, `parent/child` refers to the `"child":"value"`.If the `field` is left blank, the endpoint returns all default values. |
| `_prettyPrint=true`        | Format the body of the response.                                                                                                                                                                                                                                                         |
