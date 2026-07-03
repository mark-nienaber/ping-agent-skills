---
title: Action
description: Actions are a means of extending Advanced Identity Cloud REST APIs and are defined by the resource provider. The actions you can use depend on the implementation.
component: pingoneaic-api
page_id: pingoneaic-api::crest/action
canonical_url: https://developer.pingidentity.com/pingoneaic-api/crest/action.html
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
