---
title: Create a script
description: To create a script in a realm, perform an HTTP POST using the /json{/realm}/scripts endpoint, with an _action parameter set to create. Include a JSON representation of the script in the POST data.
component: pingoneaic-api
page_id: pingoneaic-api:am-scripting:rest-api-scripts-create
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-scripting/rest-api-scripts-create.html
keywords: ["Scripts", "REST"]
---

# Create a script

To create a script in a realm, perform an HTTP POST using the `/json{/realm}/scripts` endpoint, with an `_action` parameter set to `create`. Include a JSON representation of the script in the POST data.

The value for `script` must be in UTF-8 format and encoded into Base64.

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.1" \
--data '{
    "name": "MyJavaScript",
    "script": "dmFyIGEgPSAxMjM7CnZhciBiID0gNDU2Ow==",
    "language": "JAVASCRIPT",
    "context": "POLICY_CONDITION",
    "description": "An example script"
}' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/scripts/?_action=create'
{
    "_id": "0168d494-015a-420f-ae5a-6a2a5c1126af",
    "_rev": "-482518750",
    "name": "MyJavaScript",
    "description": "An example script",
    "script": "dmFyIGEgPSAxMjM7CnZhciBiID0gNDU2Ow==",
    "default": false,
    "language": "JAVASCRIPT",
    "context": "POLICY_CONDITION",
    "createdBy": "id=ed6816a3-c158-48e0-8402-b2f971b5b492,ou=user,ou=am-config",
    "creationDate": 1687779600329,
    "lastModifiedBy": "id=ed6816a3-c158-48e0-8402-b2f971b5b492,ou=user,ou=am-config",
    "lastModifiedDate": 1687779600329,
    "evaluatorVersion": "1.0"
}
```
