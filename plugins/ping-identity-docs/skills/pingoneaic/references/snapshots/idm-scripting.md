---
title: Create custom endpoints to launch scripts
description: Create custom REST endpoints that run arbitrary scripts with HTTP method handling
component: pingoneaic
page_id: pingoneaic:idm-scripting:script-custom-endpoints
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-scripting/script-custom-endpoints.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  custom-endpoint-scripts: Custom endpoint scripts
  sample-custom-endpoint-script: Sample custom endpoint script
  adding-custom-endpoints-structure: Custom endpoint configuration
  sample_custom_endpoint_configuration: Sample custom endpoint configuration
  custom-script-errors: Script exceptions
---

# Create custom endpoints to launch scripts

*Custom endpoints* let you run arbitrary scripts through the REST API.

A custom endpoint configuration *(tooltip: You can create and change custom endpoint configurations over REST at the config/endpoint-\<name> endpoint.)* includes an inline script that provides the endpoint functionality.

## Custom endpoint scripts

The following [custom endpoint script](#sample-custom-endpoint-script) demonstrates all the HTTP operations that can be called by a script. Each HTTP operation is associated with a `method` (`create`, `read`, `update`, `delete`, `patch`, `action`, or `query`). Requests sent to the custom endpoint return a list of the variables available to each method.

All scripts are invoked with a global `request` variable in their scope. This request structure carries all the information about the request.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Read requests on custom endpoints must not modify the state of the resource, either on the client or the server, as this can make them susceptible to Cross Site Request Forgery (CSRF) exploits.The standard READ endpoints are safe from CSRF exploits because they are read-only. This is consistent with the *Guidelines for Implementation of REST*, from the US National Security Agency, as "... CSRF protections need only be applied to endpoints that will modify information in some way." |

Custom endpoint scripts *must* return a JSON object. The structure of the return object depends on the `method` in the request.

Depending on the method, the variables available to the script can include the following:

* `resourceName`

  The name of the resource, without the `endpoint/` prefix, such as `echo`.

* `newResourceId`

  The identifier of the new object, available as the results of a `create` request.

* `revision`

  The revision of the object.

* `parameters`

  Any additional parameters provided in the request. The sample code returns request parameters from an HTTP GET with `?param=x`, as `"parameters":{"param":"x"}`.

* `content`

  Content based on the latest revision of the object, using `getObject`.

* `context`

  The context of the request, including headers and security. For more information, refer to [Request context chain](request-context.html).

* Paging parameters

  The `pagedResultsCookie`, `pagedResultsOffset`, and `pageSize` parameters are specific to `query` methods. For more information refer to [Page Query Results](../idm-objects/queries.html#paging-query-results).

* Query parameters

  The `queryId` and `queryFilter` parameters are specific to `query` methods. For more information refer to [Construct Queries](../idm-objects/queries.html#constructing-queries).

### Sample custom endpoint script

```javascript
(function(){
    if (request.method === "create") {
        return {
            method: "create",
            resourceName: request.resourcePath,
            newResourceId: request.newResourceId,
            parameters: request.additionalParameters,
            content: request.content,
            context: context.current
        };
    } else if (request.method === "read") {
        return {
            method: "read",
            resourceName: request.resourcePath,
            parameters: request.additionalParameters,
            context: context.current
        };
    } else if (request.method === "update") {
        return {
            method: "update",
            resourceName: request.resourcePath,
            revision: request.revision,
            parameters: request.additionalParameters,
            content: request.content,
            context: context.current
        };
    } else if (request.method === "patch") {
        return {
            method: "patch",
            resourceName: request.resourcePath,
            revision: request.revision,
            parameters: request.additionalParameters,
            patch: request.patchOperations,
            context: context.current
        };
    } else if (request.method === "query") {
        // query results must be returned as a list of maps
        return [ {
            method: "query",
            resourceName: request.resourcePath,
            pagedResultsCookie: request.pagedResultsCookie,
            pagedResultsOffset: request.pagedResultsOffset,
            pageSize: request.pageSize,
            queryId: request.queryId,
            queryFilter: request.queryFilter.toString(),
            parameters: request.additionalParameters,
            content: request.content,
            context: context.current
        } ];
    } else if (request.method === "delete") {
        return {
            method: "delete",
            resourceName: request.resourcePath,
            revision: request.revision,
            parameters: request.additionalParameters,
            context: context.current
        };
    } else if (request.method === "action") {
        return {
            method: "action",
            action: request.action,
            content: request.content,
            parameters: request.additionalParameters,
            context: context.current
        };
    } else {
        throw { code : 500, message : "Unknown request type " + request.method };
    }
})();
```

## Custom endpoint configuration

A custom endpoint configuration *(tooltip: You can create and change custom endpoint configurations over REST at the config/endpoint-\<name> endpoint.)* has the following structure:

```json
{
    "context" : "context path",
    "type" : "script language",
    "source" : "script source"
}
```

* `context`

  string, optional

  The root URL path for the endpoint, in other words, the *route* to the endpoint. An endpoint with the context `endpoint/test` is addressable over REST at the URL `https://<tenant-env-fqdn>/openidm/endpoint/test` or using a script such as `openidm.read("endpoint/test")`.

  Endpoint contexts support wild cards, as shown in the preceding example. The `endpoint/linkedview/*` route matches the following patterns:

  ```
  endpoint/linkedView/managed/realm-name_user/bjensen
  endpoint/linkedView/system/ldap/account/bjensen
  endpoint/linkedView/
  endpoint/linkedView
  ```

* `type`

  string, required

  The script type.

  IDM supports `"text/javascript"`.

* `source`

  The inline script source.

  For example:

  ```none
  "source" : "require('linkedView').fetch(request.resourcePath);"
  ```

### Sample custom endpoint configuration

```json
{
    "type" : "text/javascript",
    "source" : "<script>"
}
```

## Script exceptions

Some custom endpoint scripts require exception-handling logic. To return meaningful messages in REST responses and in logs, you must comply with the language-specific method of throwing errors.

JavaScript scripts should comply with the following exception format:

```json
throw {
    "code": 400, // any valid HTTP error code
    "message": "custom error message",
    "detail" : {
        "var": parameter1,
        "complexDetailObject" : [
            "detail1",
            "detail2"
        ]
    }
}
```

Any exceptions will include the specified HTTP error code, the corresponding HTTP error message, such as `Bad Request`, a custom error message that can help you diagnose the error, and any additional detail that you think might be helpful.

---

---
title: Register custom scripted actions
description: Register custom scripts to define actions on managed object endpoints
component: pingoneaic
page_id: pingoneaic:idm-scripting:custom-scripted-actions
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-scripting/custom-scripted-actions.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  example_scenario: Example scenario
---

# Register custom scripted actions

You can register custom scripts that initiate an action on a managed object endpoint. You can declare any number of actions in your managed object schema and associate those actions with a script.

The return value of a custom scripted action is ignored. The managed object is returned as the response of the scripted action, whether that object has been updated by the script or not.

Custom scripted actions have access to the following variables:

* `context`

* `request`

* `resourcePath`

* `object`

## Example scenario

In this scenario, you want your managed users to have the option to receive update notifications. You can define an *action* that toggles the value of a specific property on the user object.

1. Add an `updates` property to the managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint.)*:

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                          |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | The property `updates` is used for readability in the following example. In Advanced Identity Cloud you do not extend the default Advanced Identity Cloud managed object schema. Instead, you use one of the generic extension attributes. For more information, refer to [General purpose extension attributes](../identities/user-identity-properties-attributes-reference.html#general-purpose-extension-attributes). |

   ```json
   "properties": {
       ...
       "updates": {
           "title": "Automatic Updates",
           "viewable": true,
           "type": "boolean",
           "searchable": true,
           "userEditable": true
       },
       ...
   }
   ```

2. Add a `toggleUpdates` action to the managed user object definition:

   ```json
   {
       "objects" : [
           {
               "name" : "user",
               "onCreate" : {
                   ...
               },
               ...
               "actions" : {
                   "toggleUpdates" : {
                       "type" : "text/javascript",
                       "source" : "openidm.patch(resourcePath, null, [{ 'operation' : 'replace', 'field' : '/updates', 'value' : !object.updates }])"
                   }
               },
               ...
           }
       ]
   }
   ```

   |   |                                                                                                    |
   | - | -------------------------------------------------------------------------------------------------- |
   |   | The `toggleUpdates` action calls a script that changes the value of the user's `updates` property. |

3. To call the script, specify the ID of the action in a POST request on the user object:

   ```
   curl \
   --header "Authorization: Bearer <access-token>" \
   --header "Accept-API-Version: resource=1.0" \
   --request POST \
   "https://<tenant-env-fqdn>/openidm/managed/realm-name_user/ID?_action=toggleUpdates"
   ```

   You can now test the functionality.

4. Create a managed user, `bjensen`, with an `updates` property set to `true`:

   ```
   curl \
   --header "Authorization: Bearer <access-token>" \
   --header "Accept-API-Version: resource=1.0" \
   --header "Content-Type: application/json" \
   --request POST \
   --data '{
     "userName":"bjensen",
     "sn":"Jensen",
     "givenName":"Barbara",
     "mail":"bjensen@example.com",
     "telephoneNumber":"5556787",
     "description":"Created by OpenIDM REST.",
     "updates": true,
     "password":"Passw0rd"
   }' \
   "https://<tenant-env-fqdn>/openidm/managed/realm-name_user?_action=create"
   {
     "_id": "9dce06d4-2fc1-4830-a92b-bd35c2f6bcbb",
     "_rev": "0000000050c62938",
     "userName": "bjensen",
     "sn": "Jensen",
     "givenName": "Barbara",
     "mail": "bjensen@example.com",
     "telephoneNumber": "5556787",
     "description": "Created by OpenIDM REST.",
     "updates": true,
     "accountStatus": "active",
     "effectiveRoles": [],
     "effectiveAssignments": []
   }
   ```

5. Run the `toggleUpdates` action on `bjensen`:

   ```
   curl \
   --header "Authorization: Bearer <access-token>" \
   --header "Accept-API-Version: resource=1.0" \
   --request POST \
   "https://<tenant-env-fqdn>/openidm/managed/realm-name_user/9dce06d4-2fc1-4830-a92b-bd35c2f6bcbb?_action=toggleUpdates"
   {
     "_id": "9dce06d4-2fc1-4830-a92b-bd35c2f6bcbb",
     "_rev": "00000000a92657c7",
     "userName": "bjensen",
     "sn": "Jensen",
     "givenName": "Barbara",
     "mail": "bjensen@example.com",
     "telephoneNumber": "5556787",
     "description": "Created by OpenIDM REST.",
     "updates": false,
     "accountStatus": "active",
     "effectiveRoles": [],
     "effectiveAssignments": []
   }
   ```

   |   |                                                           |
   | - | --------------------------------------------------------- |
   |   | This action sets bjensen's `updates` property to `false`. |