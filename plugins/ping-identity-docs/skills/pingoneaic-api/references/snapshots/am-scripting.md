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

---

---
title: Delete a script
description: To delete a script, perform an HTTP DELETE using the /json{/realm}/scripts endpoint, specifying the UUID in the URL.
component: pingoneaic-api
page_id: pingoneaic-api:am-scripting:rest-api-scripts-delete
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-scripting/rest-api-scripts-delete.html
keywords: ["Scripts", "REST"]
---

# Delete a script

To delete a script, perform an HTTP DELETE using the `/json{/realm}/scripts` endpoint, specifying the UUID in the URL.

```bash
$ curl \
--request DELETE \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.1" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/scripts/aeb22d32-100c-46c0-ac51-af571889e5b9'
{}
```

|   |                                                                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You can't read, update, or delete the default scripts prefixed `ForgeRock Internal` (UUIDs: `234ba0b-58a1-4cfd-9567-09edde980745` and `1f389a3d-21cf-417c-a6d3-42ea620071f0`). These scripts appear in the query but aren't accessible in Advanced Identity Cloud. |

---

---
title: Manage scripts over REST
description: Advanced Identity Cloud provides the /scripts endpoint to manage scripts using REST calls.
component: pingoneaic-api
page_id: pingoneaic-api:am-scripting:manage-scripts-rest
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-scripting/manage-scripts-rest.html
keywords: ["Extensibility", "Scripts"]
page_aliases: ["index.adoc"]
---

# Manage scripts over REST

Advanced Identity Cloud provides the `/scripts` endpoint to manage scripts using REST calls.

Scripts are represented in JSON using standard JSON objects and values.

Each script is identified by a system-generated *universally unique identifier* (UUID), which must be specified when reading or updating existing scripts. Renaming a script doesn't affect the UUID.

```json
{
  "_id": "aeb22d32-100c-46c0-ac51-af571889e5b9",
  "name": "MyJavaScript",
  "description": "An example script",
  "script": "dmFyIGEgPSAxMjM7CnZhciBiID0gNDU2Ow==",
  "default": false,
  "language": "JAVASCRIPT",
  "context": "POLICY_CONDITION",
  "createdBy": "null",
  "creationDate": 0,
  "lastModifiedBy": "null",
  "lastModifiedDate": 0,
  "evaluatorVersion": "1.0"
}
```

The values for the fields shown in the example are explained below:

* `_id`

  The UUID that Advanced Identity Cloud generates for the script.

* `name`

  The name provided for the script.

* `description`

  An optional text string to help identify the script.

* `script`

  The source code of the script. The source code is in UTF-8 format and encoded into Base64.

  For example, the following script:

  ```javascript
  var a = 123;
  var b = 456;
  ```

  becomes `dmFyIGEgPSAxMjM7IA0KdmFyIGIgPSA0NTY7` when encoded into Base64.

* `default`

  Whether the script is a default script (`true`) that applies to all realms, or custom (`false`).

* `language`

  The language the script is written in: `JAVASCRIPT`.

* `context`

  The context type of the script.

  **Supported context values**

  | Value                                       | Description                                                                                                                                                                                                                               |
  | ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | `AUTHENTICATION_CLIENT_SIDE`                | Client-side authentication script                                                                                                                                                                                                         |
  | `AUTHENTICATION_SERVER_SIDE`                | Server-side authentication script                                                                                                                                                                                                         |
  | `AUTHENTICATION_TREE_DECISION_NODE`         | Legacy authentication scripts used by [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html)s and [Device Match node](https://docs.pingidentity.com/auth-node-ref/latest/device-match.html)s |
  | `CONFIG_PROVIDER_NODE`                      | Configuration Provider node script                                                                                                                                                                                                        |
  | `DEVICE_MATCH_NODE`                         | Next-generation authentication scripts used by [Device Match node](https://docs.pingidentity.com/auth-node-ref/latest/device-match.html)s                                                                                                 |
  | `OAUTH2_ACCESS_TOKEN_MODIFICATION`          | Legacy access token modification script.                                                                                                                                                                                                  |
  | `OAUTH2_ACCESS_TOKEN_MODIFICATION_NEXT_GEN` | Next-generation access token modification script.                                                                                                                                                                                         |
  | `OAUTH2_AUTHORIZE_ENDPOINT_DATA_PROVIDER`   | Script to enhance the data returned from the OAuth 2.0 provider in the authorization request                                                                                                                                              |
  | `OAUTH2_EVALUATE_SCOPE`                     | Script to customize the scopes in an OAuth 2.0 access token                                                                                                                                                                               |
  | `OAUTH2_MAY_ACT`                            | Script to add `may_act` claims to tokens for token exchange                                                                                                                                                                               |
  | `OAUTH2_SCRIPTED_JWT_ISSUE`                 | Script to configure a trusted JWT issuer                                                                                                                                                                                                  |
  | `OAUTH2_VALIDATE_SCOPE`                     | Script to validate the requested scopes                                                                                                                                                                                                   |
  | `OIDC_CLAIMS`                               | Modify OIDC claims when issuing an ID token or calling the `/userinfo` endpoint                                                                                                                                                           |
  | `LIBRARY`                                   | Reuse code with a library script                                                                                                                                                                                                          |
  | `POLICY_CONDITION`                          | Legacy scripted conditions for authorization policies                                                                                                                                                                                     |
  | `POLICY_CONDITION_NEXT_GEN`                 | Next-generation scripted conditions for authorization policies                                                                                                                                                                            |
  | `SAML2_IDP_ADAPTER`                         | Script for customizing the authentication request in a SAML 2.0 journey                                                                                                                                                                   |
  | `SAML2_IDP_ATTRIBUTE_MAPPER`                | Script for customizing SAML 2.0 attribute mapping                                                                                                                                                                                         |
  | `SAML2_NAMEID_MAPPER`                       | Next-generation script to customize the NameID attribute returned in the SAML assertion                                                                                                                                                   |
  | `SAML2_SP_ADAPTER`                          | Script for customizing the authentication request on the SP side in a SAML 2.0 journey                                                                                                                                                    |
  | `SCRIPTED_DECISION_NODE`                    | Next-generation authentication scripts used by [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html)s                                                                                       |
  | `SOCIAL_IDP_PROFILE_TRANSFORMATION`         | Map fields from the social IDP to fields expected by Advanced Identity Cloud                                                                                                                                                              |

* `createdBy`

  A string containing the universal identifier DN of the subject that created the script, or `null` when not used in Advanced Identity Cloud.

* `creationDate`

  An integer containing the creation date and time, in ISO 8601 format, or `0` when not used in Advanced Identity Cloud.

* `lastModifiedBy`

  A string containing the universal identifier DN of the subject that most recently updated the resource type, or `null` when not used in Advanced Identity Cloud.

  If the script hasn't been modified since it was created, this property will have the same value as `createdBy`.

* `lastModifiedDate`

  A string containing the last modified date and time, in ISO 8601 format, or `0` when not used in Advanced Identity Cloud.

  If the script has not been modified since it was created, this property will have the same value as `creationDate`.

* `evaluatorVersion`

  A number representing the script engine version: `1.0` for legacy or `2.0` for next-generation. Learn more in [Next-generation scripts](https://docs.pingidentity.com/pingoneaic/latest/am-scripting/next-generation-scripts.html).

  When invalid or unspecified, the value defaults to `1.0` for all script types except [library scripts](https://docs.pingidentity.com/pingoneaic/latest/am-scripting/library-scripts.html), which are always `2.0` (next-generation).

---

---
title: Query scripts
description: To list all the scripts in a realm, as well as any default scripts, perform an HTTP GET to the /json{/realm}/scripts endpoint with a _queryFilter parameter set to true.
component: pingoneaic-api
page_id: pingoneaic-api:am-scripting:rest-api-scripts-query
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-scripting/rest-api-scripts-query.html
keywords: ["Scripts", "REST"]
---

# Query scripts

To list all the scripts in a realm, as well as any default scripts, perform an HTTP GET to the `/json{/realm}/scripts` endpoint with a `_queryFilter` parameter set to `true`.

```bash
$ curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.1" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/scripts?_queryFilter=true'
{
  "result": [
 {
      "_id": "01e1a3c0-038b-4c16-956a-6c9d89328cff",
      "name": "Authentication Tree Decision Node Script",
      "description": "Default global script for a scripted decision node",
      "script": "LyoKICAtIERhdGE…​",
      "default": true,
      "language": "JAVASCRIPT",
      "context": "AUTHENTICATION_TREE_DECISION_NODE",
      "createdBy": "null",
      "creationDate": 0,
      "lastModifiedBy": "null",
      "lastModifiedDate": 0,
      "evaluatorVersion": "1.0"
    },
    {
      "_id": "aeb22d32-100c-46c0-ac51-af571889e5b9",
      "name": "MyJavaScript",
      "description": "An example script",
      "script": "dmFyIGEgPSAxMjM7CnZhciBiID0gNDU2Ow==",
      "default": false,
      "language": "JAVASCRIPT",
      "context": "POLICY_CONDITION",
      "createdBy": "null",
      "creationDate": 0,
      "lastModifiedBy": "null",
      "lastModifiedDate": 0,
      "evaluatorVersion": "1.0"
    },
  ],
  "resultCount": 2,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": -1
}
```

|   |                                                                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You can't read, update, or delete the default scripts prefixed `ForgeRock Internal` (UUIDs: `234ba0b-58a1-4cfd-9567-09edde980745` and `1f389a3d-21cf-417c-a6d3-42ea620071f0`). These scripts appear in the query but aren't accessible in Advanced Identity Cloud. |

**Supported \_queryFilter fields and operators**

| Field         | Supported operators                                |
| ------------- | -------------------------------------------------- |
| `_id`         | Equals (`eq`), Contains (`co`), Starts with (`sw`) |
| `name`        | Equals (`eq`), Contains (`co`), Starts with (`sw`) |
| `description` | Equals (`eq`), Contains (`co`), Starts with (`sw`) |
| `script`      | Equals (`eq`), Contains (`co`), Starts with (`sw`) |
| `language`    | Equals (`eq`), Contains (`co`), Starts with (`sw`) |
| `context`     | Equals (`eq`), Contains (`co`), Starts with (`sw`) |

---

---
title: Read a script
description: To read an individual script in a realm, perform an HTTP GET using the /json{/realm}/scripts endpoint, specifying the UUID in the URL.
component: pingoneaic-api
page_id: pingoneaic-api:am-scripting:rest-api-scripts-read
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-scripting/rest-api-scripts-read.html
keywords: ["Scripts", "REST"]
---

# Read a script

To read an individual script in a realm, perform an HTTP GET using the `/json{/realm}/scripts` endpoint, specifying the UUID in the URL.

```bash
$ curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.1" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/scripts/aeb22d32-100c-46c0-ac51-af571889e5b9'
{
  "_id": "aeb22d32-100c-46c0-ac51-af571889e5b9",
  "name": "MyJavaScript",
  "description": "An example script",
  "script": "dmFyIGEgPSAxMjM7CnZhciBiID0gNDU2Ow==",
  "default": false,
  "language": "JAVASCRIPT",
  "context": "POLICY_CONDITION",
  "createdBy": "null",
  "creationDate": 0,
  "lastModifiedBy": "null",
  "lastModifiedDate": 0,
  "evaluatorVersion": "1.0"
}
```

|   |                                                                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You can't read, update, or delete the default scripts prefixed `ForgeRock Internal` (UUIDs: `234ba0b-58a1-4cfd-9567-09edde980745` and `1f389a3d-21cf-417c-a6d3-42ea620071f0`). These scripts appear in the query but aren't accessible in Advanced Identity Cloud. |

---

---
title: Update a script
description: To update a script, perform an HTTP PUT using the /json{/realm}/scripts endpoint, specifying the UUID in both the URL and the PUT body. Include a JSON representation of the updated script in the PUT data alongside the UUID.
component: pingoneaic-api
page_id: pingoneaic-api:am-scripting:rest-api-scripts-update
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-scripting/rest-api-scripts-update.html
keywords: ["Scripts", "REST"]
---

# Update a script

To update a script, perform an HTTP PUT using the `/json{/realm}/scripts` endpoint, specifying the UUID in both the URL and the PUT body. Include a JSON representation of the updated script in the `PUT` data alongside the UUID.

```bash
$ curl \
--header "Authorization: Bearer <access-token>" \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=1.1" \
--request PUT \
--data '{
    "name": "MyUpdatedJavaScript",
    "script": "dmFyIGEgPSAxMjM7CnZhciBiID0gNDU2Ow==",
    "language": "JAVASCRIPT",
    "context": "POLICY_CONDITION",
    "description": "An updated example script configuration"
}' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/scripts/aeb22d32-100c-46c0-ac51-af571889e5b9'
{
  "_id": "aeb22d32-100c-46c0-ac51-af571889e5b9",
  "name": "UpdatedJavaScript",
  "description": "An updated example script",
  "script": "dmFyIGEgPSAxMjM7CnZhciBiID0gNDU2Ow==",
  "default": false,
  "language": "JAVASCRIPT",
  "context": "POLICY_CONDITION",
  "createdBy": "null",
  "creationDate": 0,
  "lastModifiedBy": "id=ed6816a3-c158-48e0-8402-b2f971b5b492,ou=user,ou=am-config",
  "lastModifiedDate": 1687792307783,
  "evaluatorVersion": "1.0"
}
```

|   |                                                                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You can't read, update, or delete the default scripts prefixed `ForgeRock Internal` (UUIDs: `234ba0b-58a1-4cfd-9567-09edde980745` and `1f389a3d-21cf-417c-a6d3-42ea620071f0`). These scripts appear in the query but aren't accessible in Advanced Identity Cloud. |

---

---
title: Validate a script
description: To validate a script, perform an HTTP POST using the /json{/realm}/scripts endpoint, with an _action parameter set to validate. Include a JSON representation of the script and the script language, JAVASCRIPT, in the POST data.
component: pingoneaic-api
page_id: pingoneaic-api:am-scripting:rest-api-scripts-validate
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-scripting/rest-api-scripts-validate.html
keywords: ["Scripts", "REST"]
---

# Validate a script

To validate a script, perform an HTTP POST using the `/json{/realm}/scripts` endpoint, with an `_action` parameter set to `validate`. Include a JSON representation of the script and the script language, `JAVASCRIPT`, in the POST data.

The value for `script` must be in UTF-8 format and then encoded into Base64.

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.1" \
--data '{
    "script": "dmFyIGEgPSAxMjM7dmFyIGIgPSA0NTY7Cg==",
    "language": "JAVASCRIPT"
}' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/scripts/?_action=validate'
{
    "success": true
}
```

If the script is valid the JSON response contains a `success` key with a value of `true`.

If the script is invalid the JSON response contains a `success` key with a value of `false`, and an indication of the problem and where it occurs, as shown below:

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.1" \
--data '{
    "script": "dmFyIGEgPSAxMjM7dmFyIGIgPSA0NTY7ID1WQUxJREFUSU9OIFNIT1VMRCBGQUlMPQo=",
    "language": "JAVASCRIPT"
}' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/scripts/?_action=validate'
{
    "success": false,
    "errors": [
        {
            "line": 1,
            "column": 27,
            "message": "syntax error"
        }
    ]
}
```