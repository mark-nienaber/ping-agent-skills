---
title: Action
description: Use the Common REST action verb to call custom, implementation-defined operations on a resource using HTTP POST
component: pingidm
version: 8.1
page_id: pingidm::crest/crest-action
canonical_url: https://docs.pingidentity.com/pingidm/8.1/crest/crest-action.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Rest", "REST API", "JSON"]
---

# Action

Actions are a means of extending Common REST APIs and are defined by the resource provider, so the actions you can use depend on the implementation.

The standard action indicated by `_action=create` is described in [Create](crest-create.html).

Parameters

You can use the following parameters. Other parameters might depend on the specific action implementation:

* `_prettyPrint=true`

  Format the body of the response.

- `_fields=field[,field...]`

  Return only the specified fields in the body of the response.

  The `field` values are JSON pointers. For example if the resource is `{"parent":{"child":"value"}}`, `parent/child` refers to the `"child":"value"`.

  If the `field` is left blank, the server returns all default values.
