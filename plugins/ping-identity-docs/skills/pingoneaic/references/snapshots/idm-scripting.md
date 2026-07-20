---
title: Call a script from the IDM configuration
description: Call scripts from identity management with inline source or file references
component: pingoneaic
page_id: pingoneaic:idm-scripting:script-call
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-scripting/script-call.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  examples: Examples
---

# Call a script from the IDM configuration

To call a script from the IDM configuration, edit the configuration object. For example:

Provide a script source

```json
{
    "type" : "text/javascript",
    "source": "scriptSource"
}
```

Script variables are not necessarily simple `key:value` pairs, and can be any arbitrarily complex JSON object.

* type

  string, required

  The script type.

  IDM supports `"text/javascript"`.

* source

  string, required

  Specifies the source code of the script to be executed.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Use namespace variables passed into scripts with the `globals` map. Passing variables in this way prevents collisions with the top-level reserved words for script maps, such as `source` and `type`. This example uses the `globals` map to namespace the variables passed in the previous example.```json
"script": {
    "type" : "text/javascript",
    "source" : "scriptSource",
    "globals" : {
        "fromSender" : "admin@example.com",
        "toEmail" : "user@example.com"
    }
}
``` |

## Examples

The following example script (in the mapping configuration *(tooltip: You can manage the mapping configuration over REST at the config/sync endpoint.)*) determines whether to include or ignore a target object in the reconciliation process based on an `employeeType` of `true`:

```json
"validTarget" : {
    "type" : "text/javascript",
    "source" : "target.employeeType == 'external'"
}
```

The following example script (in the mapping configuration *(tooltip: You can manage the mapping configuration over REST at the config/sync endpoint.)*) sets the `__PASSWORD__` attribute to `defaultpwd` when IDM creates a target object:

```json
"onCreate" : {
    "type" : "text/javascript",
    "source" : "target.__PASSWORD__ = 'defaultpwd'"
}
```

You can pass variables to your scripts to provide contextual details at runtime by declaring the variable name in the script reference.

The following scheduled task configuration calls a script that triggers an email notification, but sets the sender and recipient of the email in the schedule configuration, rather than in the script itself:

```json
{
    "enabled" : true,
    "type" : "cron",
    "schedule" : "0 0/1 * * * ?",
    "persisted" : true,
    "invokeService" : "script",
    "invokeContext" : {
        "script" : {
            "type" : "text/javascript",
            "source" : "scriptSource",
            "fromSender" : "admin@example.com",
            "toEmail" : "user@example.com"
        }
    }
}
```

---

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
title: Filter objects
description: Define filters with scripts to process requests on router objects conditionally
component: pingoneaic
page_id: pingoneaic:idm-scripting:filter-objects
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-scripting/filter-objects.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Filter objects

The required filters array defines a list of filters to be processed on each router request. Filters are processed in the order in which they are specified in this array, and have the following configuration:

```json
{
  "pattern": string,
  "methods": [ string, ... ],
  "condition": script object,
  "onRequest": script object,
  "onResponse": script object,
  "onFailure": script object
}
```

* pattern

  string, optional

  Specifies a regular expression pattern matching the JSON pointer of the object to trigger scripts. If not specified, all identifiers (including `null`) match. Pattern matching is done on the resource name, rather than on individual objects.

* methods

  array of strings, optional

  One or more methods for which the script(s) should be triggered. Supported methods are: `"create"`, `"read"`, `"update"`, `"delete"`, `"patch"`, `"query"`, `"action"`. If not specified, all methods are matched.

* condition

  script object, optional

  Specifies a script that is called first to determine if the script should be triggered. If the condition yields `"true"`, the other script(s) are executed. If no condition is specified, the script(s) are called unconditionally.

* onRequest

  script object, optional

  Specifies a script to execute before the request is dispatched to the resource. If the script throws an exception, the method is not performed, and a client error response is provided.

* onResponse

  script object, optional

  Specifies a script to execute after the request is successfully dispatched to the resource and a response is returned. Throwing an exception from this script does not undo the method already performed.

* onFailure

  script object, optional

  Specifies a script to execute if the request resulted in an exception being thrown. Throwing an exception from this script does not undo the method already performed.

---

---
title: Functions available in identity-related scripts
description: Functions for identity operations including CRUD, encryption, hashing, and queries
component: pingoneaic
page_id: pingoneaic:idm-scripting:scripting-func-engine
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-scripting/scripting-func-engine.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scripts", "Triggers"]
page_aliases: ["scripting-func-ref.adoc"]
section_ids:
  openidm_functions: openidm functions
  global-utility-functions: Global utility functions
---

# Functions available in identity-related scripts

|   |                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------- |
|   | If you need to request specific resource versions, refer to [REST API versioning](../idm-rest-api/rest-api-versioning.html). |

Identity-related functions (access to managed objects, system objects, and configuration objects) within Advanced Identity Cloud are accessible to scripts using the `openidm` object that's included in the top-level scope provided to each script.

Identity-related scripts can be created using [custom endpoints](script-custom-endpoints.html) or [script triggers](script-triggers.html).

## `openidm` functions

The script engine supports the following functions:

> **Collapse: openidm.create(resourceName, newResourceId, content, params, fields)**
>
> This function creates a new resource object.
>
> * Parameters
>
>   * resourceName
>
>     string
>
>     The container in which the object will be created, for example, `managed/realm-name_user`.
>
>   * newResourceId
>
>     string
>
>     The identifier of the object to be created, if the client is supplying the ID. If the server should generate the ID, pass null here.
>
>   * content
>
>     JSON object
>
>     The content of the object to be created.
>
>   * params
>
>     JSON object (optional)
>
>     Additional parameters that are passed to the create request.
>
>   * fields
>
>     JSON array (optional)
>
>     An array of the fields that should be returned in the result. The list of fields can include wild cards, such as `*` or `*_ref`. If no fields are specified, the entire new object is returned.
>
> * Returns
>
>   The created resource object.
>
> * Throws
>
>   An exception is thrown if the object could not be created.
>
> * Example
>
>   ```javascript
>   openidm.create("managed/realm-name_user", ID, JSON object);
>   ```

> **Collapse: openidm.patch(resourceName, rev, value, params, fields)**
>
> This function performs a partial modification of a managed or system object. Unlike the `update` function, only the modified attributes are provided, not the entire object.
>
> * Parameters
>
>   * resourceName
>
>     string
>
>     The full path to the object being updated, including the ID.
>
>   * rev
>
>     string
>
>     The revision of the object to be updated. Use `null` if the object is not subject to revision control, or if you want to skip the revision check and update the object, regardless of the revision.
>
>   * value
>
>     An array of one or more JSON objects
>
>     The value of the modifications to be applied to the object. The patch set includes the operation type, the field to be changed, and the new values. A PATCH request can `add`, `remove`, `replace`, or `increment` an attribute value.
>
>     A `remove` operation removes a property if the value of that property equals the specified value, or if no value is specified in the request. The following example `value` removes the `marital_status` property from the object, *if* the value of that property is `single`:
>
>     ```json
>     [
>         {
>             "operation": "remove",
>             "field": "marital_status",
>             "value": "single"
>         }
>     ]
>     ```
>
>     For fields whose value is an array, it's not necessary to know the position of the value in the array, as long as you specify the full object. If the full object is found in the array, that value is removed. The following example removes user adonnelly from bjensen's `reports`:
>
>     ```json
>     {
>         "operation": "remove",
>         "field": "/manager",
>         "value": {
>           "_ref": "managed/realm-name_user/adonnelly",
>           "_refResourceCollection": "managed/realm-name_user",
>           "_refResourceId": "adonnelly",
>           "_refProperties": {
>             "_id": "ed6620e4-98ba-410c-abc0-e06dc1be7aa7",
>             "_rev": "000000008815942b"
>           }
>         }
>     }
>     ```
>
>     If an invalid value is specified (that is a value that does not exist for that property in the current object) the patch request is silently ignored.
>
>     A `replace` operation replaces the entire field value. For array or multivalued relationship fields (such as `/roles`), this means the entire array is replaced, not just a single element. To swap a single element in an array, use a `remove` operation followed by an `add` operation.
>
> * params
>
>   JSON object (optional)
>
>   Additional parameters that are passed to the patch request.
>
> * fields
>
>   JSON array (optional)
>
>   An array of the fields that should be returned in the result. The list of fields can include wild cards, such as `*` or `*_ref`. If no fields are specified, the entire new object is returned.
>
> * Returns
>
>   The modified resource object.
>
> * Throws
>
>   An exception is thrown if the object couldn't be updated.
>
> * Examples
>
>   Patching an object to add a value to an array:
>
>   ```javascript
>   openidm.patch("managed/realm-name_role/" + role._id, null, [{"operation":"add", "field":"/members/-", "value": {"_ref":"managed/realm-name_user/" + user._id}}]);
>   ```
>
>   Patching an object to remove an existing property:
>
>   ```javascript
>   openidm.patch("managed/realm-name_user/" + user._id, null, [{"operation":"remove", "field":"marital_status", "value":"single"}]);
>   ```
>
>   Patching an object to remove a specific value from a multivalued relationship array:
>
>   ```javascript
>   openidm.patch("managed/realm-name_user/" + user._id, null, [{
>     "operation": "remove",
>     "field": "/roles",
>     "value": {
>       "_ref": "managed/realm-name_role/" + role._id,
>       "_refResourceCollection": "managed/realm-name_role",
>       "_refResourceId": role._id,
>       "_refProperties": {
>         "_id": "ef85ae74-6675-4f76-8bc3-19ac226cc703",
>         "_rev": "778e7955-cd0a-43c2-a714-7076d83fb710-132"
>       }
>     }
>   }]);
>   ```
>
>   Patching an object to replace a field value:
>
>   ```javascript
>   openidm.patch("managed/realm-name_user/" + user._id, null, [{"operation":"replace", "field":"/password", "value":"Passw0rd"}]);
>   ```
>
>   Patching an object to increment an integer value:
>
>   ```javascript
>   openidm.patch("managed/realm-name_user/" + user._id, null, [{"operation":"increment","field":"/age","value":1}]);
>   ```

> **Collapse: openidm.read(resourceName, params, fields)**
>
> This function reads and returns a resource object.
>
> * Parameters
>
>   * resourceName
>
>     string
>
>     The full path to the object to be read, including the ID.
>
>   * params
>
>     JSON object (optional)
>
>     The parameters that are passed to the read request. Generally, no additional parameters are passed to a read request, but this might differ, depending on the request. If you need to specify a list of `fields` as a third parameter, and you have no additional `params` to pass, you must pass `null` here. Otherwise, you simply omit both parameters.
>
>   * fields
>
>     JSON array (optional)
>
>     An array of the fields that should be returned in the result. The list of fields can include wild cards, such as `*` or `*_ref`. If no fields are specified, the entire object is returned.
>
> * Returns
>
>   The resource object, or `null` if not found.
>
> * Example
>
>   ```javascript
>   openidm.read("managed/realm-name_user/"+userId, null, ["*", "manager"]);
>   ```

> **Collapse: openidm.update(resourceName, rev, value, params, fields)**
>
> This function updates an entire resource object.
>
> * Parameters
>
>   * id
>
>     string
>
>     The complete path to the object to be updated, including its ID.
>
>   * rev
>
>     string
>
>     The revision of the object to be updated. Use `null` if the object isn't subject to revision control, or if you want to skip the revision check and update the object, regardless of the revision.
>
>   * value
>
>     object
>
>     The complete replacement object.
>
>   * params
>
>     JSON object (optional)
>
>     The parameters that are passed to the update request.
>
>   * fields
>
>     JSON array (optional)
>
>     An array of the fields that should be returned in the result. The list of fields can include wild cards, such as `*` or `*_ref`. If no fields are specified, the entire object is returned.
>
> * Returns
>
>   The modified resource object.
>
> * Throws
>
>   An exception is thrown if the object couldn't be updated.
>
> * Example
>
>   In this example, the managed user entry is read (with an `openidm.read`, the user entry that has been read is updated with a new description, and the entire updated object is replaced with the new value.
>
>   ```javascript
>   var user_read = openidm.read('managed/realm-name_user/' + source._id);
>   user_read['description'] = 'The entry has been updated';
>   openidm.update('managed/realm-name_user/' + source._id, null, user_read);
>   ```

> **Collapse: openidm.delete(resourceName, rev, params, fields)**
>
> This function deletes a resource object.
>
> * Parameters
>
>   * resourceName
>
>     string
>
>     The complete path to the to be deleted, including its ID.
>
>   * rev
>
>     string
>
>     The revision of the object to be deleted. Use `null` if the object isn't subject to revision control, or if you want to skip the revision check and delete the object, regardless of the revision.
>
>   * params
>
>     JSON object (optional)
>
>     The parameters that are passed to the delete request.
>
>   * fields
>
>     JSON array (optional)
>
>     An array of the fields that should be returned in the result. The list of fields can include wild cards, such as `*` or `*_ref`. If no fields are specified, the entire object is returned.
>
> * Returns
>
>   Returns the deleted object if successful.
>
> * Throws
>
>   An exception is thrown if the object couldn't be deleted.
>
> * Example
>
>   ```javascript
>   openidm.delete('managed/realm-name_user/'+ user._id, user._rev);
>   ```

> **Collapse: openidm.query(resourceName, params, fields)**
>
> This function performs a query on the specified resource object. Learn more in [Construct queries](../idm-objects/queries.html#constructing-queries).
>
> * Parameters
>
>   * resourceName
>
>     string
>
>     The resource object on which the query should be performed, for example, `"managed/realm-name_user"`, or `"system/ldap/account"`.
>
>   * params
>
>     JSON object
>
>     The parameters that are passed to the query (`_queryFilter`, or `_queryId`). Additional parameters passed to the query will differ, depending on the query.
>
>     Certain common parameters can be passed to the query to restrict the query results. The following sample query passes paging parameters and sort keys to the query.
>
>     ```javascript
>     reconAudit = openidm.query("audit/recon", {
>         "_queryFilter": queryFilter,
>         "_pageSize": limit,
>         "_pagedResultsOffset": offset,
>         "_pagedResultsCookie": string,
>         "_sortKeys": "-timestamp"
>     });
>     ```
>
>     Learn more about `_queryFilter` syntax in [Common filter expressions](../idm-objects/queries.html#query-filters) and paging in [Page query results](../idm-objects/queries.html#paging-query-results).
>
>   * fields
>
>     list
>
>     A list of the fields that should be returned in the result. The list of fields can include wild cards, such as `*` or `*_ref`. The following example returns only the `userName` and `_id` fields:
>
>     ```javascript
>     openidm.query("managed/realm-name_user", { "_queryFilter": "/userName sw \"user.1\""}, ["userName", "_id"]);
>     ```
>
>     This parameter is particularly useful in enabling you to return the response from a query without including intermediary code to massage it into the right format.
>
>     Fields are specified as JSON pointers.
>
> * Returns
>
>   The result of the query. A query result includes the following parameters:
>
>   * query-time-ms
>
>     (For JDBC repositories only) the time, in milliseconds, that IDM took to process the query.
>
>   * result
>
>     The list of entries retrieved by the query. The result includes the properties that were requested in the query.
>
>     The following example shows the result of a custom query that requests the ID, user name, and email address of all managed users in the repository.
>
>     ```json
>     {
>       "result": [
>         {
>           "_id": "9dce06d4-2fc1-4830-a92b-bd35c2f6bcbb",
>           "_rev": "00000000a059dc9f",
>           "userName": "bjensen",
>           "mail": "bjensen@example.com"
>         },
>         {
>           "_id": "42f8a60e-2019-4110-a10d-7231c3578e2b",
>           "_rev": "00000000d84ade1c",
>           "userName": "scarter",
>           "mail": "scarter@example.com"
>         }
>       ],
>       "resultCount": 2,
>       "pagedResultsCookie": null,
>       "totalPagedResultsPolicy": "NONE",
>       "totalPagedResults": -1,
>       "remainingPagedResults": -1
>     }
>     ```
>
> * Throws
>
>   An exception is thrown if the given query couldn't be processed.
>
> * Examples
>
>   The following sample query uses a `_queryFilter` to query the managed user repository:
>
>   ```javascript
>   openidm.query("managed/realm-name_user", {'_queryFilter': userIdPropertyName + ' eq "' + security.authenticationId  + '"'});
>   ```
>
>   The following sample query references the `for-userName` query, defined in the repository configuration, to query the managed user repository:
>
>   ```javascript
>   openidm.query("managed/realm-name_user", {"_queryId": "for-userName", "uid": request.additionalParameters.uid });
>   ```

> **Collapse: openidm.action(resource, actionName, content, params, fields)**
>
> This function performs an action on the specified resource object. The `resource` and `actionName` are required. All other parameters are optional.
>
> * Parameters
>
>   * resource
>
>     string
>
>     The resource that the function acts upon, for example, `managed/realm-name_user`.
>
>   * actionName
>
>     string
>
>     The action to execute. Actions are used to represent functionality that isn't covered by the standard methods for a resource (create, read, update, delete, patch, or query). In general, you shouldn't use the `openidm.action` function for create, read, update, patch, delete or query operations. Instead, use the corresponding function specific to the operation (for example, `openidm.create`).
>
>     Using the operation-specific functions lets you benefit from the well-defined [REST API](../idm-rest-api/preface.html), which follows the same pattern as all other standard resources in the system. Using the REST API enhances usability for your own API, and enforces the established patterns.
>
>     IDM-defined resources support a fixed set of actions. For user-defined resources (scriptable endpoints) you can implement whatever actions you require.
>
>   - Supported Actions Per Resource
>
>     The following list outlines the supported actions for each resource or endpoint. The actions listed here are also supported over the REST interface.
>
>     * Actions supported on the `authentication` endpoint (`authentication/*`)
>
>       reauthenticate
>
>     * Actions supported on the configuration resource (`config/`)
>
>       No action parameter applies.
>
>     * Actions supported on custom endpoints
>
>       Custom endpoints enable you to run arbitrary scripts through the REST URI, and are routed at `endpoint/name`, where name describes the purpose of the endpoint. Learn more about custom endpoints in [Create custom endpoints to launch scripts](script-custom-endpoints.html). You can implement whatever actions you require on a custom endpoint. IDM uses custom endpoints in its workflow implementation. Those endpoints and their actions are as follows:
>
>       `endpoint/getprocessforuser` - `create, complete`\
>       `endpoint/gettasksview` - `create, complete`
>
>     * Actions supported on the `external` endpoint
>
>       * `external/email` - `send`, for example:
>
>         ```javascript
>         var emailParams = {
>             "from" : "admin@example.com",
>             "to" : user.mail,
>             "subject" : "Your profile has been updated",
>             "type" : "text/plain",
>             "body" : "Details on your user profile have been successfully updated."
>         };
>         openidm.action("external/email", "send",  emailParams);
>         ```
>
>       * `external/email` - `sendTemplate`, for example:
>
>         ```javascript
>         var emailParams = {
>             "templateName" : "welcome",
>             "to" : user.mail,
>             "cc" : "ccUser1@example.com,ccUser2@example.com",
>             "bcc" : "bigBoss@example.com",
>             "object" : {
>                 "this": "value",
>                 "that": "another value"
>             }
>         };
>         openidm.action("external/email", "sendTemplate",  emailParams);
>         ```
>
>         |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
>         | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>         |   | When sending an email template, there are two key parameters to understand:- **`templateName`**: This parameter identifies the template to send. Its value is the template's unique ID, which is generated from the template's original name and converted to camelCase. This ID is immutable, meaning it won't change even if you rename the template later.
>
>           You can find the template ID in the Advanced Identity Cloud admin console URL when editing the template. For example, the template ID for the Forgotten Username template is `forgottenUsername`:
>
>           ```none
>           https://<tenant-env-fqdn>/?realm=alpha#/email/templates/edit/forgottenUsername
>           ```
>
>         - **`object`**: This parameter passes dynamic data to the template. Email templates use [Handlebars expressions](https://handlebarsjs.com/guide/) to render data from the `object` parameter you provide.
>
>           To render the data from the example script, your template would use the following expressions:
>
>           * `{{object.this}}` resolves to `value`.
>
>           * `{{object.that}}` resolves to `another value`.Learn more in [Send email templates](../tenants/email-send.html#email-templates-send). |
>
>       * `external/rest` - `call`, for example:
>
>         ```javascript
>         openidm.action("external/rest", "call", params);
>         ```
>
>     * Actions supported on the `info` endpoint (`info/*`)
>
>       No action parameter applies.
>
>     * Actions supported on managed resources (`managed/*`)
>
>       patch, triggerSyncCheck
>
>     * Actions supported on the policy resource (`policy`)
>
>       validateObject, validateProperty
>
>       For example:
>
>       ```javascript
>       openidm.action("policy/" + fullResourcePath, "validateObject", request.content, { "external" : "true" });
>       ```
>
>     * Actions supported on the reconciliation resource (`recon`)
>
>       recon, reconById, cancel
>
>       For example:
>
>       ```javascript
>       openidm.action("recon/_id", "cancel", content, params);
>       ```
>
>       |   |                                                                            |
>       | - | -------------------------------------------------------------------------- |
>       |   | A *cancel* action requires the entire reconciliation resource path (\_id). |
>
>     * Actions supported on the repository (`repo`)
>
>       command
>
>       For example:
>
>       ```javascript
>       var r, command = {
>           "commandId": "purge-by-recon-number-of",
>           "numberOf": numOfRecons,
>           "includeMapping": includeMapping,
>           "excludeMapping": excludeMapping
>       };
>       r = openidm.action("repo/audit/recon", "command", {}, command);
>       ```
>
>     * Actions supported on the script resource (`script`)
>
>       eval
>
>       For example:
>
>       ```javascript
>       openidm.action("script", "eval", getConfig(scriptConfig), {});
>       ```
>
>     * Actions supported on the synchronization resource (`sync`)
>
>       getLinkedResources, notifyCreate, notifyDelete, notifyUpdate, performAction
>
>       For example:
>
>       ```javascript
>       openidm.action('sync', 'performAction', content, params);
>       ```
>
>     * Actions supported on system resources (`system/*`)
>
>       availableConnectors, createCoreConfig, createFullConfig, test, testConfig, liveSync, authenticate, script
>
>       For example:
>
>       ```javascript
>       openidm.action("system/ldap/account", "authenticate", {"username" : "bjensen", "password" : "Passw0rd"});
>       ```
>
>     * Actions supported on the task scanner resource (`taskscanner`)
>
>       execute, cancel
>
>     * Actions supported on the workflow resource (`workflow/*`)
>
>       On `workflow/processdefinition` create, complete
>
>       On `workflow/processinstance` create, complete
>
>       For example:
>
>       ```javascript
>       var params = {
>           "_key":"contractorOnboarding"
>       };
>       openidm.action('workflow/processinstance', 'create', params);
>       ```
>
>       On `workflow/taskinstance` claim, create, complete
>
>       For example:
>
>       ```javascript
>       var params = {
>           "userId":"manager1"
>       };
>       openidm.action('workflow/taskinstance/15', 'claim', params);
>       ```
>
>   - content
>
>     object
>
>     Content given to the action for processing.
>
>   - params
>
>     object (optional)
>
>     Additional parameters passed to the script. The `params` object must be a set of simple key-value pairs, and can't include complex values. The parameters must map directly to URL variables, which take the form `name1=val1&name2=val2&...`.
>
>   - fields
>
>     JSON array (optional)
>
>     An array of the fields that should be returned in the result. The list of fields can include wild cards, such as `*` or `*_ref`. If no fields are specified, the entire object is returned.
>
> * Returns
>
>   The result of the action may be `null`.
>
> * Throws
>
>   If the action can't be executed, an exception is thrown.

> **Collapse: openidm.encrypt(value, cipher, alias)**
>
> This function encrypts a value.
>
> * Parameters
>
>   * value
>
>     any
>
>     The value to be encrypted.
>
>   * cipher
>
>     string
>
>     The cipher with which to encrypt the value. Advanced Identity Cloud only supports AES with a key size of 128.
>
>   * alias
>
>     string
>
>     An encryption purpose defined in the secrets configuration *(tooltip: You can edit the secrets configuration over REST at the config/secrets endpoint.)*. The default is `idm.password.encryption`.
>
>     |   |                                                                                                                                                                                                                                                               |
>     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>     |   | The secrets configuration *(tooltip: You can edit the secrets configuration over REST at the config/secrets endpoint.)* contains mappings between keys and various functions. The keys reside in a keystore. To request a custom key, raise a support ticket. |
>
> * Returns
>
>   The value, encrypted with the specified cipher and key.
>
> * Throws
>
>   An exception is thrown if the object could not be encrypted.

> **Collapse: openidm.decrypt(value)**
>
> This function decrypts a value.
>
> * Parameters
>
>   * value
>
>     object
>
>     The value to be decrypted.
>
> * Returns
>
>   A deep copy of the value, with any encrypted value decrypted.
>
> * Throws
>
>   An exception is thrown if the object couldn't be decrypted for any reason. An error is thrown if the value is passed in as a string - it must be passed in an object.

> **Collapse: openidm.isEncrypted(object)**
>
> This function determines if a value is encrypted.
>
> * Parameters
>
>   * object to check
>
>     any
>
>     The object whose value should be checked to determine if it is encrypted.
>
> * Returns
>
>   Boolean, `true` if the value is encrypted, and `false` if it isn't encrypted.
>
> * Throws
>
>   An exception is thrown if the server is unable to detect whether the value is encrypted, for any reason.

> **Collapse: openidm.hash(value, algorithm, options)**
>
> This function calculates a value using a salted hash algorithm.
>
> Supported hashing algorithms and configuration properties
>
> The following list describes the algorithms and their configuration properties:
>
> * `BCRYPT`
>
>   * `cost`
>
>     Value between 4 and 31. The default is `13`.
>
> * `PBKDF2`
>
>   * `hashLength`
>
>     Byte-length of the generated hash. The default is `16`.
>
>   * `saltLength`
>
>     Byte-length of the salt value. The default is `16`.
>
>   * `iterations`
>
>     Number of cryptographic iterations. The default is `20000`.
>
>   * `hmac`
>
>     HMAC algorithm. The default is `SHA3-256`.
>
>     Supported values:
>
>     * `SHA-224`
>
>     * `SHA-256`
>
>     * `SHA-384`
>
>     * `SHA-512`
>
>     * `SHA3-224`
>
>     * `SHA3-256`
>
>     * `SHA3-384`
>
>     * `SHA3-512`
>
> * `SCRYPT`
>
>   * `hashLength`
>
>     Byte-length of the generated hash, must be greater than or equal to 8. The default is `16`.
>
>   * `saltLength`
>
>     Byte-length of the salt value. The default is `16`.
>
>   * `n`
>
>     CPU/Memory cost. Must be greater than 1, a power of 2, and less than *2^(128 \* r / 8)*. The default is `32768`.
>
>   * `p`
>
>     Parallelization. Must be a positive integer less than or equal to *Integer.MAX\_VALUE / (128 \* r \* 8)*. The default is `1`.
>
>   * `r`
>
>     Block size. Must be greater than or equal to 1. The default is `8`.
>
> * `SHA-256`
>
>   * `saltLength`
>
>     Byte-length of the salt value. The default is `16`.
>
>     |   |                              |
>     | - | ---------------------------- |
>     |   | This is the default hashing. |
>
> * `SHA-384`
>
>   * `saltLength`
>
>     Byte-length of the salt value. The default is `16`.
>
> * `SHA-512`
>
>   * `saltLength`
>
>     Byte-length of the salt value. The default is `16`.
>
> * Parameters
>
>   * value
>
>     any
>
>     The value to be hashed.
>
>   * algorithm
>
>     string (optional)
>
>     The hashing algorithm. Example: `SHA-512`.
>
>     If no algorithm is provided, a `null` value must be passed, and the algorithm defaults to SHA-256.
>
>   * options
>
>     For JavaScript, JSON object (optional)
>
>     Configuration properties for the selected algorithm.
>
> * Returns
>
>   The value, calculated with the specified hash algorithm.
>
> * Throws
>
>   An exception is thrown if the object couldn't be hashed for any reason.
>
> * Examples
>
>   * JavaScript
>
>     ```javascript
>     openidm.hash(\"dummy\", \"BCRYPT\", {\"cost\": 10})
>     ```

> **Collapse: openidm.isHashed(value)**
>
> This function detects whether a value has been calculated with a salted hash algorithm.
>
> * Parameters
>
>   * value
>
>     any
>
>     The value to be reviewed.
>
> * Returns
>
>   Boolean, `true` if the value is hashed, and `false` otherwise.
>
> * Throws
>
>   An exception is thrown if the server is unable to detect whether the value is hashed, for any reason.

> **Collapse: openidm.matches(string, value)**
>
> This function detects whether a string, when hashed, matches an existing hashed value.
>
> * Parameters
>
>   * string
>
>     any
>
>     A string to be hashed.
>
>   * value
>
>     any
>
>     The hashed value (as a `$crypto` object) to compare against the hash of the string.
>
>     |   |                                                                                                                                                                                                             |
>     | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>     |   | To store an IDM hash value, don't enable hashing on a string attribute. The hash value is an object and not a string. Instead, use a custom attribute, such as a `custom_myHash` field, to store the value. |
>
> * Returns
>
>   Boolean, `true` if the hash of the string matches the hashed value, and `false` otherwise.
>
> * Throws
>
>   An exception is thrown if the string can't be hashed.
>
> * Example
>
>   JavaScript
>
>   ```javascript
>   (function () {
>       var body = request.content; (1)
>
>       if (request.method === 'create') {
>           // POST
>           // SHA256HashedPassword = openidm.hash(body.password, "SHA-256");
>           var hashedValue = {
>               "$crypto": {
>                   "value": {
>                       "algorithm": "SHA-256",
>                       "data": "QVjOMKdAifIxKC5y/bl4SXdlUx79EHLegucBF3SXEUP7LVKlXuluJH0J5y33a648"
>                   },
>                   "type": "salted-hash"
>               }
>           };
>           var SHA256HashedPassword = openidm.matches(body.password, hashedValue); (2)
>           return {
>               body: SHA256HashedPassword (2)
>           };
>       }
>   }());
>   ```
>
> |       |                                                                                                                                        |
> | ----- | -------------------------------------------------------------------------------------------------------------------------------------- |
> | **1** | Learn more about available fields for the request object in [Create custom endpoints to launch scripts](script-custom-endpoints.html). |
> | **2** | The `openidm.matches` function references the full `$crypto` object value instead of a hashed string.                                  |
>
> > **Collapse: Show example output**
> >
> > ```json
> > {
> >   "_id": "",
> >   "body": true  (1)
> > }
> > ```
> >
> > |       |                                                                         |
> > | ----- | ----------------------------------------------------------------------- |
> > | **1** | You must call the full `$crypto` object value to get a `true` response. |

## Global utility functions

These functions are available globally in the script execution context.

> **Collapse: btoa(stringToEncode)**
>
> Encodes a string in Base64. This is a global script binding that implements the canonical JavaScript `btoa` function.
>
> * Parameters
>
>   * stringToEncode
>
>     string
>
>     The string to Base64 encode. This string should consist of characters that can be represented by a single byte (Latin1 characters). For strings containing multi-byte characters, an error might occur or the output might be unexpected, as standard `btoa` is designed for binary strings.
>
> * Returns
>
>   An ASCII string representing the Base64 encoded version of `stringToEncode`.
>
> * Example
>
>   ```javascript
>   var originalString = "Hello World!";
>   var encodedString = btoa(originalString);
>   encodedString; (1)
>   ```
>
>   |       |                                                                        |
>   | ----- | ---------------------------------------------------------------------- |
>   | **1** | In this example, the returned `encodedString` is `"SGVsbG8gV29ybGQh"`. |

> **Collapse: atob(encodedString)**
>
> Decodes a Base64 encoded string. This is a global script binding that implements the canonical JavaScript `atob` function.
>
> * Parameters
>
>   * encodedString
>
>     string
>
>     The Base64 encoded string to be decoded.
>
> * Returns
>
>   An ASCII string representing the decoded version of `encodedString`.
>
> * Throws
>
>   An exception is typically thrown if the input `encodedString` isn't a valid Base64 string.
>
> * Example
>
>   ```javascript
>   var base64String = "SGVsbG8gV29ybGQh";
>   var decodedString = atob(base64String);
>   decodedString; (1)
>   ```
>
>   |       |                                                                    |
>   | ----- | ------------------------------------------------------------------ |
>   | **1** | In this example, the returned `decodedString` is `"Hello World!"`. |

---

---
title: Logging in identity-related scripts
description: Logging functions for scripts using SLF4J facilities at various log levels
component: pingoneaic
page_id: pingoneaic:idm-scripting:scripting-func-logs
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-scripting/scripting-func-logs.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scripts", "Logs"]
---

# Logging in identity-related scripts

Identity-related logs can be used in scripts created for [custom endpoints](script-custom-endpoints.html) or [script triggers](script-triggers.html).

Advanced Identity Cloud provides a `logger` object to access the Simple Logging Facade for Java (SLF4J) facilities. The following code shows an example of the `logger` object.

```javascript
logger.info("Parameters passed in: {} {} {}", param1, param2, param3);
```

In addition, JavaScript has a useful logging function named `console.log()`. This function provides an easy way to dump data to the Advanced Identity Cloud standard output (usually the same output as the OSGi console). The function works well with the JavaScript built-in function `JSON.stringify` and provides fine-grained details about any given object. For example, the following line will print a formatted JSON structure that represents the HTTP request details to STDOUT.

```javascript
console.log(JSON.stringify(context.http, null, 4));
```

The script engine supports the following log functions:

> **Collapse: logger.debug(string message, object... params)**
>
> Logs a message at DEBUG level.
>
> * Parameters
>
>   * message
>
>     string
>
>     The message format to log. Params replace `{}` in your message.
>
>   * params
>
>     object
>
>     Arguments to include in the message.
>
> * Returns
>
>   A `null` value if successful.
>
> * Throws
>
>   An exception is thrown if the message could not be logged.

> **Collapse: logger.error(string message, object... params)**
>
> Logs a message at ERROR level.
>
> * Parameters
>
>   * message
>
>     string
>
>     The message format to log. Params replace `{}` in your message.
>
>   * params
>
>     object
>
>     Arguments to include in the message.
>
> * Returns
>
>   A `null` value if successful.
>
> * Throws
>
>   An exception is thrown if the message could not be logged.

> **Collapse: logger.info(string message, object... params)**
>
> Logs a message at INFO level.
>
> * Parameters
>
>   * message
>
>     string
>
>     The message format to log. Params replace `{}` in your message.
>
>   * params
>
>     object
>
>     Arguments to include in the message.
>
> * Returns
>
>   A `null` value if successful.
>
> * Throws
>
>   An exception is thrown if the message could not be logged.

> **Collapse: logger.trace(string message, object... params)**
>
> Logs a message at TRACE level.
>
> * Parameters
>
>   * message
>
>     string
>
>     The message format to log. Params replace `{}` in your message.
>
>   * params
>
>     object
>
>     Arguments to include in the message.
>
> * Returns
>
>   A `null` value if successful.
>
> * Throws
>
>   An exception is thrown if the message could not be logged.

> **Collapse: logger.warn(string message, object... params)**
>
> Logs a message at WARN level.
>
> * Parameters
>
>   * message
>
>     string
>
>     The message format to log. Params replace `{}` in your message.
>
>   * params
>
>     object
>
>     Arguments to include in the message.
>
> * Returns
>
>   A `null` value if successful.
>
> * Throws
>
>   An exception is thrown if the message could not be logged.

---

---
title: "Pattern matching in the <span class=\"fr-alt\" title=\"You can edit the router configuration over REST at the config/router endpoint.\">router configuration</span>"
description: Use pattern matching in router configuration to improve script performance
component: pingoneaic
page_id: pingoneaic:idm-scripting:script-pattern-match
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-scripting/script-pattern-match.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Pattern matching in the router configuration *(tooltip: You can edit the router configuration over REST at the config/router endpoint.)*

Pattern matching can minimize overhead in the router service. The default router configuration *(tooltip: You can edit the router configuration over REST at the config/router endpoint.)* includes instances of the `pattern` filter object, that limit script requests to specified methods and endpoints.

Based on the following code snippet, the router service would trigger a script for `CREATE` and `UPDATE` calls to managed and internal objects:

```json
{
    "pattern" : "^(managed|internal)($|(/.+))",
    "onRequest" : {
        "type" : "text/javascript",
        "source" : "require('policyFilter').runFilter()"
    },
    "methods" : [
        "create",
        "update"
    ]
}
```

Without this `pattern`, IDM would apply the policy filter to additional objects, such as the audit service, which could affect performance.

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

   |   |                                                                                                                                                                                                                                                                                                                                                                                  |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The property `updates` is used for readability in the following example. In IDM you do not extend the default IDM managed object schema. Instead, you use one of the generic extension attributes. For more information, refer to [General purpose extension attributes](../identities/user-identity-properties-attributes-reference.html#general-purpose-extension-attributes). |

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

---

---
title: Request context chain
description: Understand request context chain from root through security and HTTP layers
component: pingoneaic
page_id: pingoneaic:idm-scripting:request-context
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-scripting/request-context.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Request context chain

The context chain of any request is established as follows:

1. The request starts with a *root context*, associated with a specific context ID.

2. The root context is wrapped in the *security context* that includes the authentication and authorization detail for the request.

3. The security context is further wrapped by the *HTTP context*, with the target URI. The HTTP context is associated with the normal parameters of the request, including a user agent, authorization token, and method.

4. The HTTP context is wrapped by one or more server/router context(s), with an endpoint URI. The request can have several layers of server and router contexts.

---

---
title: Router configuration
description: Manage uniform interface to objects through router service with filter objects
component: pingoneaic
page_id: pingoneaic:idm-scripting:router-config
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-scripting/router-config.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Router configuration

The router service provides the uniform interface to all IDM objects: managed objects, system objects, configuration objects, and so on.

The router configuration *(tooltip: You can edit the router configuration over REST at the config/router endpoint.)* contains an array of [Filter objects](filter-objects.html):

```json
{
  "filters": [ filter object, ... ]
}
```

---

---
title: Script execution sequence
description: Understand execution order of onRequest and onResponse scripts in filter chain
component: pingoneaic
page_id: pingoneaic:idm-scripting:script-sequence
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-scripting/script-sequence.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Script execution sequence

All `onRequest` and `onResponse` scripts are executed in sequence. First, the `onRequest` scripts are executed from the top down, then the `onResponse` scripts are executed from the bottom up.

```
client -> filter 1 onRequest -> filter 2 onRequest -> resource
client <- filter 1 onResponse <- filter 2 onResponse <- resource
```

The following sample router configuration *(tooltip: You can edit the router configuration over REST at the config/router endpoint.)* shows the order in which the scripts would be executed:

```json
{
    "filters" : [
        {
            "onRequest" : {
                "type" : "text/javascript",
                "source" : "require('router-authz').testAccess()"
            }
        },
        {
            "pattern" : "^managed/realm-name_user",
            "methods" : [
                "read"
            ],
            "onRequest" : {
                "type" : "text/javascript",
                "source" : "console.log('requestFilter 1');"
            }
        },
        {
            "pattern" : "^managed/realm-name_user",
            "methods" : [
                "read"
            ],
            "onResponse" : {
                "type" : "text/javascript",
                "source" : "console.log('responseFilter 1');"
            }
        },
        {
            "pattern" : "^managed/realm-name_user",
            "methods" : [
                "read"
            ],
            "onRequest" : {
                "type" : "text/javascript",
                "source" : "console.log('requestFilter 2');"
            }
        },
        {
            "pattern" : "^managed/realm-name_user",
            "methods" : [
                "read"
            ],
            "onResponse" : {
                "type" : "text/javascript",
                "source" : "console.log('responseFilter 2');"
            }
        }
    ]
}
```

This configuration would produce a log as follows:

```none
requestFilter 1
requestFilter 2
responseFilter 2
responseFilter 1
```

> **Collapse: Example Filter Configuration**
>
> This example executes a script after a managed user object is created or updated:
>
> ```json
> {
>     "filters": [
>         {
>             "pattern": "^managed/realm-name_user",
>             "methods": [
>                 "create",
>                 "update"
>             ],
>             "onResponse": {
>                 "type": "text/javascript",
>                 "source": "inlineScript"
>             }
>         }
>     ]
> }
> ```

---

---
title: Script scope
description: Access request and response objects in filter scripts through standard scope
component: pingoneaic
page_id: pingoneaic:idm-scripting:filter-script-scope
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-scripting/filter-script-scope.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Script scope

Scripts are provided with the following scope:

```json
{
  "openidm": openidm-functions object,
  "request": resource-request object,
  "response": resource-response object,
  "exception": exception object
}
```

* openidm

  [openidm-functions object](scripting-func-engine.html)

  Provides access to IDM resources.

* request

  resource-request object

  The resource-request context, which has one or more parent contexts. Provided in the scope of all scripts. For more information about the request context, refer to [Request context chain](request-context.html).

* response

  resource-response object

  The response to the resource-request. Only provided in the scope of the `"onResponse"` script.

* exception

  exception object

  The exception value that was thrown as a result of processing the request. Only provided in the scope of the `"onFailure"` script. An exception object is defined as:

  ```json
  {
    "code": integer,
    "reason": string,
    "message": string,
    "detail": string
  }
  ```

* code

  integer

  The numeric HTTP code of the exception.

* reason

  string

  The short reason phrase of the exception.

* message

  string

  A brief message describing the exception.

* detail

  (optional), string

  A detailed description of the exception, in structured JSON format, suitable for programmatic evaluation.

---

---
title: Script triggers
description: Overview of script triggers available in mappings, managed objects, and router config
component: pingoneaic
page_id: pingoneaic:idm-scripting:script-triggers
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-scripting/script-triggers.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Script triggers

Scripts can be triggered in different places and by different events. The following list indicates the configuration files in which scripts can be referenced, the events upon which the scripts can be triggered, and the actual scripts that can be triggered on each of these files.

|   |                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------- |
|   | For more information about the variables available to scripts, refer to [Script variables](script-vars.html). |

* Scripts called in [mappings](../idm-synchronization/mappings.html)

  * Triggered by situation

    onCreate, onUpdate, onDelete, onLink, onUnlink

  * Object filter

    validSource, validTarget

  * Triggered when correlating objects

    correlationQuery, correlationScript

  * Triggered on any reconciliation

    result

  * Scripts inside properties

    condition, transform

    Mappings support one script per hook. If multiple scripts are defined for the same hook, only the last one is kept.

  * Scripts inside policies

    condition

    Within a synchronization policy, you can use a `condition` script to apply different policies based on the link type, for example:

    ```json
    "condition" : {
      "type" : "text/javascript",
      "source" : "linkQualifier == \"user\""
    }
    ```

* Scripts called in the managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint.)*

  onCreate, onRead, onUpdate, onDelete, onValidate, onRetrieve, onStore, onSync, postCreate, postUpdate, and postDelete

  The managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint.)* supports only one script per hook. If multiple scripts are defined for the same hook, only the last one is kept.

* Scripts called in the router configuration *(tooltip: You can edit the router configuration over REST at the config/router endpoint.)*

  onRequest, onResponse, onFailure

  The router configuration *(tooltip: You can edit the router configuration over REST at the config/router endpoint.)* supports multiple scripts per hook.

---

---
title: Script triggers defined in mappings
description: Script triggers available in synchronization mappings for correlation and actions
component: pingoneaic
page_id: pingoneaic:idm-scripting:script-triggers-mappings
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-scripting/script-triggers-mappings.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  object_mapping_object: Object-mapping object
  property_object: Property object
  policy_object: Policy object
---

# Script triggers defined in mappings

For information about how managed objects in mappings are handled, and the script triggers available, refer to [Object-mapping objects](../idm-synchronization/synchronization-ref.html#sync-object-mapping).

## Object-mapping object

The following list describes the variables for each trigger:

* `correlationQuery`, `correlationScript`

  Return a JSON object. Variables:

  * **source**: Represents the source object.

  * **linkQualifier**: The link qualifier associated with the current sync.

  * **context**: Information related to the current request, such as source and target.

* `linkQualifiers`

  Returns a JSON object. Variables:

  * **mapping**: The name of the current mapping.

  * **object**: The value of the source object. During a DELETE event, that source object may not exist, and may be null.

  * **oldValue**: The former value of the deleted source object, if any. If the source object is new, oldValue will be null. When there are deleted objects, oldValue is populated only if the source is a managed object.

  * **returnAll** (boolean): Link qualifier scripts must return every valid link qualifier when returnAll is true, independent of the source object. If returnAll is true, the script must not attempt to use the object variable, because it will be null. It's best practice to configure scripts to start with a check for the value of returnAll.

  * **context**: Information related to the current request, such as source and target.

* `onCreate`

  Returns a JSON object. Variables:

  * **source**: Represents the source object.

  * **target**: Represents the target object.

  * **situation**: The situation associated with the current sync operation.

  * **linkQualifier**: The link qualifier associated with the current sync operation.

  * **context**: Information related to the current sync operation.

  * **sourceId**: The object ID for the source object.

  * **targetId**: The object ID for the target object.

  * **mappingConfig**: A configuration object representing the mapping being processed.

* `onDelete`, `onUpdate`

  Return a JSON object. Variables:

  * **source**: Represents the source object.

  * **target**: Represents the target object.

  * **oldTarget**: Represents the target object prior to the DELETE or UPDATE action.

  * **situation**: The situation associated with the current sync operation.

  * **linkQualifier**: The link qualifier associated with the current sync.

  * **context**: Information related to the current sync operation.

  * **sourceId**: The object ID for the source object.

  * **targetId**: The object ID for the target object.

  * **mappingConfig**: A configuration object representing the mapping being processed.

* `onLink`, `onUnlink`

  Return a JSON object. Variables:

  * **source**: Represents the source object.

  * **target**: Represents the target object.

  * **linkQualifier**: The link qualifier associated with the current sync operation.

  * **context**: Information related to the current sync operation.

  * **sourceId**: The object ID for the source object.

  * **targetId**: The object ID for the target object.

  * **mappingConfig**: A configuration object representing the mapping being processed.

* `onError`

  Returns a JSON object. Variables:

  * **source**: Represents the source object.

  * **target**: Represents the target object.

  * **linkQualifier**: The link qualifier associated with the current sync operation.

  * **context**: Information related to the current sync operation.

  * **situation**: The situation associated with the current sync operation.

  * **sourceId**: The object ID for the source object.

  * **targetId**: The object ID for the target object.

  * **oldSource**: Available during UPDATE and DELETE operations performed through implicit sync. With implicit synchronization, the synchronization operation is triggered by a specific change to the source object. As such, implicit sync can populate the old value within the `oldSource` variable and pass it on to the sync engine.

  * **error**: The result of the resource exception, as a JSON object.

  * **mappingConfig**: A configuration object representing the mapping being processed.

* `result`

  Returns JSON object of reconciliation results. Variables:

  * **source**: Provides statistics about the source phase of the reconciliation.

  * **target**: Provides statistics about the target phase of the reconciliation.

  * **context**: Information related to the current operation, such as source and target.

  * **global**: Provides statistics about the entire reconciliation operation.

  * **mappingConfig**: A configuration object representing the mapping being processed.

  * **reconState**: Provides the state of reconciliation operation; such as, *success*, *failure*, or *active*.

* `validSource`

  Returns a boolean. Variables:

  * **source**: Represents the source object.

  * **linkQualifier**: The link qualifier associated with the current sync operation.

  * **context**: Information related to the current sync operation.

* `validTarget`

  Returns a boolean. Variables:

  * **target**: Represents the target object.

  * **linkQualifier**: The link qualifier associated with the current sync operation.

  * **context**: Information related to the current sync operation.

## Property object

The following list describes the variables for each trigger:

* `condition`

  Returns a boolean. Variables:

  * **object**: The current object being mapped.

  * **context**: Information related to the current operation, such as source and target.

  * **linkQualifier**: The link qualifier associated with the current sync operation.

  * **target**: Represents the target object.

  * **oldTarget**: Represents the target object prior to any changes.

  * **oldSource**: Available during UPDATE and DELETE operations performed through implicit sync. With implicit synchronization, the synchronization operation is triggered by a specific change to the source object. As such, implicit sync can populate the old value within the `oldSource` variable and pass it on to the sync engine.

    During reconciliation operations `oldSource` will be undefined. A reconciliation operation cannot populate the value of the `oldSource` variable as it has no awareness of the specific change to the source object. Reconciliation simply synchronizes the static source object to the target.

* `transform`

  Returns a JSON object. Variables:

  * **source**: Represents the source object.

  * **linkQualifier**: The link qualifier associated with the current sync operation.

  * **context**: Information related to the current sync operation.

## Policy object

The following list describes the variables for each trigger:

* `action`

  Returns a string or a JSON object. Variables:

  * **source**: Represents the source object.

  * **target**: Represents the target object.

  * **sourceAction** (boolean): Indicates whether the action is being processed during the source or target synchronization phase (true if performed during a source synchronization, false if performed during a target synchronization).

  * **linkQualifier**: The link qualifier used for this operation (`default` if no other link qualifier is specified).

  * **context**: Information related to the current sync operation.

  * **recon**: Represents the reconciliation operation.

  * The `recon.actionParam` object contains information about the current reconciliation operation and includes the following variables:

    * `reconId`: The ID of the reconciliation operation.

    * `mapping`: The mapping for which the reconciliation was performed, for example, `systemLdapAccounts_managedUser`.

    * `situation`: The situation encountered, for example, AMBIGUOUS.

    * `action`: The default action that would be used for this situation, if not for this script. The script being executed replaces the default action (and is used instead of any other named action).

    * `sourceId`: The `_id` value of the source record.

    * `linkQualifier`: The link qualifier used for that mapping, (`default` if no other link qualifier is specified).

    * `ambiguousTargetIds`: An array of the target object IDs that were found in an AMBIGUOUS situation during correlation.

    * `_action`: The synchronization action (only `performAction` is supported).

* `postAction`

  Returns a JSON object. Variables:

  * **source**: Represents the source object.

  * **target**: Represents the target object.

  * **action**: The sync action that was performed.

  * **sourceAction** (boolean): Indicates whether the action is being processed during the source or target synchronization phase (true if performed during a source synchronization, false if performed during a target synchronization).

  * **linkQualifier**: The link qualifier used for this operation (`default` if no other link qualifier is specified).

  * **reconId**: Represents the ID of the reconciliation.

  * **situation**: Represents the situation for this policy.

  * **context**: Information related to the current operation, such as source and target.

---

---
title: "Script triggers defined in the <span class=\"fr-alt\" title=\"You can edit the managed object configuration over REST at the config/managed endpoint.\">managed object configuration</span>"
description: Script triggers available in managed object configuration for CRUD operations and lifecycle events
component: pingoneaic
page_id: pingoneaic:idm-scripting:script-triggers-managedConfig
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-scripting/script-triggers-managedConfig.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  managed_object_configuration_object: Managed object configuration object
  property_object: Property object
---

# Script triggers defined in the managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint.)*

For information about how managed objects are handled, and the available script triggers, refer to [Managed objects](../idm-objects/managed-objects.html).

## Managed object configuration object

The following list describes the variables for each trigger:

* `onCreate`, `postCreate`

  * **object**: The content of the object being created.

  * **newObject**: The object after the create operation is complete.

  * **context**: Information related to the current request, such as client, end user, and routing.

  * **resourceName**: The resource path of the object of the query. For example, if you create a managed user with ID `42f8a60e-2019-4110-a10d-7231c3578e2b`, resourceName returns `managed/realm-name_user/42f8a60e-2019-4110-a10d-7231c3578e2b`.

  * **request**: Information related to the request, such as headers, credentials, and the desired action. Also includes the endpoint, and payload to be processed.

* `onUpdate`, `postUpdate`

  Return a JSON object. Variables:

  * **object**: The content of the object being updated.

  * **oldObject**: The state of the object, before the update.

  * **newObject**: Changes to be applied to the object. May continue with the `onUpdate` trigger.

  * **context**: Information related to the current request, such as client, end user, and routing.

  * **resourceName**: The resource path of the object the query.

  * **request**: Information related to the request, such as headers, credentials, and the desired action. Also includes the endpoint, and payload to be processed.

* `onDelete`, `onRetrieve`, `onRead`

  Return a JSON object. Variables:

  * **object**: The content of the object.

  * **context**: Information related to the current request, such as client, end user, and routing.

  * **resourceName**: The resource path of the object the query.

  * **request**: Information related to the request, such as headers, credentials, and the desired action. Also includes the endpoint, and payload to be processed.

* `postDelete`

  Returns a JSON object. Variables:

  * **oldObject**: Represents the deleted object.

  * **context**: Information related to the current request, such as client, end user, and routing.

  * **resourceName**: The resource path of the object the query is performed upon.

  * **request**: Information related to the request, such as headers, credentials, and the desired action. Also includes the endpoint, and payload to be processed.

* `onSync`

  Returns a JSON object. Variables:

  * **oldObject**: Represents the object prior to sync. If sync has not been run before, the value will be `null`.

  * **newObject**: Represents the object after sync is completed.

  * **context**: Information related to the current request, such as client, end user, and routing.

  * **request**: Information related to the request, such as headers, credentials, and the desired action. Also includes the endpoint, and payload to be processed.

  * **resourceName**: An object representing the resource path the query is performed upon.

  * **syncResults**: A map containing the results and details of the sync, including:

    * **success** (boolean): Success or failure of the sync operation.

    * **action**: Returns the name of the action performed as a string.

    * **syncDetails**: The mappings attempted during synchronization.

* `onStore`, `onValidate`

  Return a JSON object. Variables:

  * **object**: Represents the object being stored or validated.

  * **value**: The content to be stored or validated for the object.

  * **context**: Information related to the current request, such as client, end user, and routing.

  * **resourceName**: The resource path of the object the query is performed upon.

  * **request**: Information related to the request, such as headers, credentials, and the desired action. Also includes the endpoint, and payload to be processed.

## Property object

The following list describes the variables for each trigger:

* `onRetrieve`, `onStore`

  Return a JSON object. Variables:

  * **object**: Represents the object being operated upon.

  * **property**: The value of the property being retrieved or stored.

  * **propertyName**: The name of the property being retrieved or stored.

  * **context**: Information related to the current request, such as client, end user, and routing.

  * **resourceName**: The resource path of the object the query is performed upon.

  * **request**: Information related to the request, such as headers, credentials, and the desired action. Also includes the endpoint, and payload to be processed.

* `onValidate`

  Returns a JSON object. Variables:

  * **property**: The value of the property being validated.

  * **context**: Information related to the current request, such as client, end user, and routing.

  * **resourceName**: The resource path of the object the query is performed upon.

  * **request**: Information related to the request, such as headers, credentials, and the desired action. Also includes the endpoint, and payload to be processed.

---

---
title: "Script triggers defined in the <span class=\"fr-alt\" title=\"You can edit the router configuration over REST at the config/router endpoint.\">router configuration</span>"
description: Script triggers in router configuration for request, response, and failure handling
component: pingoneaic
page_id: pingoneaic:idm-scripting:script-triggers-routerConfig
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-scripting/script-triggers-routerConfig.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Script triggers defined in the router configuration *(tooltip: You can edit the router configuration over REST at the config/router endpoint.)*

The router service provides the uniform interface to all IDM objects: managed objects, system objects, configuration objects, and so on.

| Trigger      | Variable  |
| ------------ | --------- |
| `onFailure`  | exception |
| `onRequest`  | request   |
| `onResponse` | response  |

For more information, refer to [Router configuration](router-config.html).

---

---
title: Script variables
description: Variables available in scripts based on trigger location and configuration
component: pingoneaic
page_id: pingoneaic:idm-scripting:script-vars
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-scripting/script-vars.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Script variables

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | For more information about the variables available in script triggers, refer to [Script triggers](script-triggers.html). |

The variables available to a script depend on several factors:

* The trigger that launches the script.

* The configuration file in which that trigger is defined.

* The object type:

  * For objects defined in the managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint.)*, the object type is a managed object or a managed object property.

  * For objects defined in the mapping configuration *(tooltip: You can manage the mapping configuration over REST at the config/sync endpoint.)*, the object can be an object-mapping object, a property object, or a policy object. For more information, refer to [Policy Objects](../idm-synchronization/synchronization-ref.html#sync-policy-objects)).

The following subtopics list the variables available to scripts, based on the configuration file in which the trigger is defined.

---

---
title: Scripting
description: Overview of JavaScript scripting in Advanced Identity Cloud for custom endpoints, filters, triggers, and identity operations
component: pingoneaic
page_id: pingoneaic:idm-scripting:preface
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-scripting/preface.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["index.adoc"]
---

# Scripting

Scripting lets you extend Advanced Identity Cloud functionality. For example, you can provide custom logic between source and target mappings, define correlation rules, filters, triggers, and so on. This guide shows you how to use scripts in Advanced Identity Cloud and provides reference information on the script engine.

[icon: wrench, set=fas, size=3x]

#### [Custom Endpoints](script-custom-endpoints.html)

Run arbitrary scripts through the REST URI.

[icon: play-circle, set=far, size=3x]

#### [Script Triggers](script-triggers.html)

Learn where and how you can trigger scripts.

[icon: file-code, set=far, size=3x]

#### [Script Variables](script-vars.html)

Learn about the variables available to scripts.

Advanced Identity Cloud supports scripts written in JavaScript, and uses the following libraries:

* Rhino version 1.7.14 to run JavaScript.

  |   |                                                                                                                                                                                  |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Rhino has limited support for ES6 / ES2015 (JavaScript version 1.7). For more information, refer to [Rhino ES2015 Support](https://mozilla.github.io/rhino/compat/engines.html). |

* Lodash 3.10.1 and Handlebars 4.7.6 for Rhino scripting.

  |   |                                                                                                                                                                                                                                                                                                                                                                                  |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Using Handlebars JS in server-side JS scripts requires *synchronization*; for example:```javascript
  var Handlebars = require("lib/handlebars");
  var result = new Packages.org.mozilla.javascript.Synchronizer(function() {
    var template = Handlebars.compile("Handlebars {{doesWhat}}");
    return template({ doesWhat: "rocks!" });
  }, Handlebars)();
  console.log(result);
  ``` |

* BouncyCastle 1.67 for signing JWTs.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The BouncyCastle .JAR file that is bundled with IDM includes the `org.bouncycastle.asn1.util.Dump` command-line utility. Although this utility is not used directly by IDM, it is possible to reference the utility in your scripts. Due to a security vulnerability in this utility, you should *not* reference it in your scripts. For more information, refer to the corresponding [BouncyCastle issue](https://github.com/bcgit/bc-java/issues/634). |

---

---
title: The <code>augmentSecurityContext</code> trigger
description: Use augmentSecurityContext trigger to populate user security context after authentication
component: pingoneaic
page_id: pingoneaic:idm-scripting:script-variables-augment-security
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-scripting/script-variables-augment-security.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# The `augmentSecurityContext` trigger

The `augmentSecurityContext` trigger, defined in the authentication configuration *(tooltip: You can manage the authentication configuration over REST at the config/authentication endpoint.)*, can reference a script that is executed after successful authentication. These scripts can populate the security context of the authenticated user. If the authenticated user is not found in the resource specified by `queryOnResource`, the `augmentSecurityContext` can provide the required authorization map.

These scripts have access to the following bindings:

* `security` - includes the `authenticationId` and the `authorization` key, which includes the `moduleId`.

  The main purpose of an `augmentSecurityContext` script is to modify the `authorization` map that is part of this `security` binding. The authentication module determines the value of the `authenticationId`, and IDM attempts to populate the `authorization` map with the details that it finds, related to that `authenticationId` value. These details include the following:

  * `security.authorization.component` - the resource that contains the account (by default, this will always be the same as the value of `queryOnResource`).

  * `security.authorization.id` - the internal `_id` value that is associated with the account.

  * `security.authorization.roles` - any roles that were determined, either from reading the `userRoles` property of the account or from calculation.

  * `security.authorization.moduleId` - the authentication module responsible for performing the original authentication.

  You can use the `augmentSecurityContext` script to change any of these `authorization` values. The script can also add new values to the `authorization` map, which will be available for the lifetime of the session.

* `properties` - corresponds to the `properties` map of the related authentication module.

* `httpRequest` - a reference to the `Request` object that was responsible for handling the incoming HTTP request.

  This binding is useful to the augment script because it has access to all of the raw details from the HTTP request, such as the headers. The following code snippet shows how you can access a header using the `httpRequest` binding. This example accesses the `authToken` request header:

  ```none
  httpRequest.getHeaders().getFirst('authToken').toString()
  ```

For more information, refer to [Roles, authentication, and the Security Context](../idm-auth/authentication-and-roles.html#auth-security-context).

---

---
title: The <code>identityServer</code> variable
description: Retrieve property information using identityServer variable in scripts
component: pingoneaic
page_id: pingoneaic:idm-scripting:script-variables-identity-server
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-scripting/script-variables-identity-server.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# The `identityServer` variable

IDM provides an additional variable, named `identityServer`, to scripts. You can use this variable in several ways. The `ScriptRegistryService`, described in [Validate scripts over REST](script-endpoint.html), binds this variable to:

* `getProperty`

  Retrieves property information from system configuration files. Takes up to three parameters:

  * The name of the property you are requesting.

  * *(Optional)* The default result to return if the property wasn't set.

  * *(Optional)* Boolean to determine whether to use property substitution when getting the property.

  For example, you can retrieve the value of the `openidm.config.crypto.alias` property with the following code:

  ```
  alias = identityServer.getProperty("openidm.config.crypto.alias", "true", true);
  ```

---

---
title: Validate scripts over REST
description: Validate and evaluate scripts over REST using eval and compile actions
component: pingoneaic
page_id: pingoneaic:idm-scripting:script-endpoint
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-scripting/script-endpoint.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Validate scripts over REST

IDM exposes a `script` endpoint over which scripts can be validated, by specifying the script parameters as part of the JSON payload. This functionality lets you test how a script will operate in your deployment, with complete control over the inputs and outputs. Testing scripts in this way can be useful in debugging.

The `script` endpoint supports two actions - `eval` and `compile`.

The `eval` action evaluates a script, by taking any actions referenced in the script, such as router calls to affect the state of an object. For JavaScript scripts, the last statement that is executed is the value produced by the script, and the expected result of the REST call.

|   |                                                                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The variables passed into this script are namespaced with the `globals` map. It is preferable to namespace variables passed into scripts in this way, to avoid collisions with the top-level reserved words for script maps, such as `file`, `source`, and `type`. |

The `compile` action compiles a script, but does not execute it. A successful compilation returns `true`. An unsuccessful compilation returns the reason for the failure.

The following REST call tests whether a transformation script will compile:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request POST \
--data '{
  "type":"text/javascript",
  "source":"source.mail ? source.mail.toLowerCase() : null"
}' \
"https://<tenant-env-fqdn>/openidm/script?_action=compile"
True
```

If the script is not valid, the action returns an indication of the error, for example:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request POST \
--data '{
  "type":"text/javascript",
  "source":"source.mail ? source.mail.toLowerCase()"
}' \
"https://<tenant-env-fqdn>/openidm/script?_action=compile"
{
  "code": 400,
  "reason": "Bad Request",
  "message": "missing : in conditional expression (386...BF2#1)in 386...BF2 at line number 1 at column number 39"
}
```