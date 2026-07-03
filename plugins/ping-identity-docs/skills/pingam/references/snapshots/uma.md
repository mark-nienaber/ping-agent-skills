---
title: /json/users/{user}/oauth2/resources/labels
description: PingAM endpoint for creating, deleting, and querying User-Managed Access (UMA) user and star labels
component: pingam
version: 8.1
page_id: pingam:uma:endpoint-labels
canonical_url: https://docs.pingidentity.com/pingam/8.1/uma/endpoint-labels.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["User-Managed Access (UMA)", "Endpoints", "Resource Labels"]
page_aliases: ["uma-guide:endpoint-labels.adoc"]
---

# /json/users/{user}/oauth2/resources/labels

AM-specific endpoint used to create, delete, and query UMA user and star labels.

> **Collapse: Supported HTTP methods**
>
> | Action | HTTP method |
> | ------ | ----------- |
> | Create | POST        |
> | Query  | GET         |
> | Delete | DELETE      |

|   |                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Use the AM API Explorer for detailed information about this endpoint, and to test it against your deployed AM instance.In the AM admin UI, click the Help icon, and go to API Explorer > users > *user* > oauth2 > resources > labels. |

You must compose the path to the token endpoint addressing the specific realm where the token will be issued. For example, `https://am.example.com:8443/am/json/realms/root/realms/subrealm1/users/user/oauth2/resources/labels`.

The labels endpoint does not support any parameters. To authenticate to the endpoint, send the SSO token of the resource owner as the value of the `iPlanetDirectoryPro` header.

To create a label, send an HTTP POST request to the endpoint, adding the description of the label as a JSON object in the body. For example:

```json
{
  "name" : "My Favorites",
  "type" : "STAR",
  "resourceSetIDs": [
      "UMA_resource_ID_1234567890",
      "UMA_resource_ID_0987654321"
  ]
}
```

The value of the `type` object can be `USER`, for user labels, and `STAR`, for star labels. For more information about the label types, see [UMA labels](uma-manage-resource-set-labels.html).

The `resourceSetIDs` object is an array of UMA resource IDs that the label applies to. It is not mandatory; if you do not add it, the label will be created without any resource associated. You will need to update the *resource* to add it to the label, because the labels endpoint does not support updating labels.

For examples, see [Manage UMA user and favorite labels](uma-labels-with-REST-users.html).
