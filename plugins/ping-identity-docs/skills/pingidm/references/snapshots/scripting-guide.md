---
title: Call a script from the IDM configuration
description: Call a script from the PingIDM configuration using inline source or a file reference, with examples of passing variables and globals
component: pingidm
version: 8.1
page_id: pingidm:scripting-guide:script-call
canonical_url: https://docs.pingidentity.com/pingidm/8.1/scripting-guide/script-call.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scripting", "Configuration", "Call"]
section_ids:
  examples: Examples
---

# Call a script from the IDM configuration

To call a script from the IDM configuration, edit the configuration object. For example:

Provide a script source

```json
{
    "type" : "text/javascript",
    "source": "scriptSource",
    "resourceBindings" : [{
        "resource" : "resourceName",
        "version" : "1.0",
        "binding" : "customName"
    }]
}
```

or

Provide a file reference

```json
{
    "type" : "text/javascript",
    "file" : "file location"
}
```

Script variables are not necessarily simple `key:value` pairs, and can be any arbitrarily complex JSON object.

* type

  string, required

  The script type.

  IDM supports `"text/javascript"` and `"groovy"`.

* source

  string, required if `file` is not specified

  Specifies the source code of the script to be executed.

* resourceBindings

  JSON object, optional

  Allows specifying a resource, a vanity binding for that resource, and the API version the script should use. For example:

  ```json
  {
      "source" : "var response = consent.action(\"getConsentMappings\", {}); response[0];",
      "resourceBindings" : [{
          "resource" : "consent",
          "version" : "1.0",
          "binding" : "consent"
      }],
      "type" : "text/javascript"
  }
  ```

  This can improve the legibility of your scripts, by no longer needing to pass additional information within your script function.

* file

  string, required if `source` is not specified

  Specifies the file containing the source code of the script to execute. The file path must be relative to project-dir. Absolute paths are not supported.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In general, you should namespace variables passed into scripts with the `globals` map. Passing variables in this way prevents collisions with the top-level reserved words for script maps, such as `source`, `file`, and `type`. This example uses the `globals` map to namespace the variables passed in the previous example.```json
"script": {
    "type" : "text/javascript",
    "file" : "script/triggerEmailNotification.js",
    "globals" : {
        "fromSender" : "admin@example.com",
        "toEmail" : "user@example.com"
    }
}
``` |

## Examples

The following example script (in the mapping configuration *(tooltip: You can manage the mapping configuration over REST at the config/sync endpoint, directly in the conf/sync.json file, or in individual conf/mapping-\<mappingName>.json files.)*) determines whether to include or ignore a target object in the reconciliation process based on an `employeeType` of `true`:

```json
"validTarget" : {
    "type" : "text/javascript",
    "source" : "target.employeeType == 'external'"
}
```

The following example script (in the mapping configuration *(tooltip: You can manage the mapping configuration over REST at the config/sync endpoint, directly in the conf/sync.json file, or in individual conf/mapping-\<mappingName>.json files.)*) sets the `__PASSWORD__` attribute to `defaultpwd` when IDM creates a target object:

```json
"onCreate" : {
    "type" : "text/javascript",
    "source" : "target.__PASSWORD__ = 'defaultpwd'"
}
```

Often, script files are reused in different contexts. You can pass variables to your scripts to provide these contextual details at runtime. You pass variables to the scripts that are referenced in configuration files by declaring the variable name in the script reference.

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
            "file" : "script/triggerEmailNotification.js",
            "fromSender" : "admin@example.com",
            "toEmail" : "user@example.com"
        }
    }
}
```

---

---
title: Create custom endpoints to launch scripts
description: Create custom endpoints in PingIDM to run arbitrary JavaScript or Groovy scripts through the REST API, with configuration and scripting examples
component: pingidm
version: 8.1
page_id: pingidm:scripting-guide:script-custom-endpoints
canonical_url: https://docs.pingidentity.com/pingidm/8.1/scripting-guide/script-custom-endpoints.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scripting", "REST", "Endpoints", "Custom"]
section_ids:
  adding-custom-endpoints-structure: Custom endpoint configuration
  custom-endpoint-scripts: Custom endpoint scripts
  custom-script-errors: Script exceptions
  custom-endpoint-api-descriptor: Write an API descriptor for a custom endpoint
---

# Create custom endpoints to launch scripts

*Custom endpoints* let you run arbitrary scripts through the REST API.

A custom endpoint configuration *(tooltip: You can create and change custom endpoint configurations over REST at the config/endpoint/\<name> endpoint, or in files named conf/endpoint-\<name>.json, where \<name> generally describes the purpose of the endpoint.)* includes an inline script or script file reference in JavaScript or Groovy. The script provides the endpoint functionality.

> **Collapse: Sample Custom Endpoint Configuration**
>
> ```json
> {
>     "type" : "text/javascript",
>     "source" : "<script>",
>     "apiDescription" : {
>         "title" : "Echo",
>         "description" : "Service that echo's your HTTP requests.",
>         "mvccSupported" : false,
>         "create" : {
>             "description" : "Echo a CREATE request.",
>             "mode" : "ID_FROM_SERVER",
>             "singleton" : false
>         },
>         "read" : { "description" : "Echo a READ request." },
>         "update" : { "description" : "Echo an UPDATE request." },
>         "delete" : { "description" : "Echo a DELETE request." },
>         "patch" : {
>             "description" : "Echo a PATCH request.",
>             "operations" : [ "ADD", "REMOVE", "REPLACE", "INCREMENT", "COPY", "MOVE", "TRANSFORM" ]
>         },
>         "actions" : [
>             {
>                 "description" : "Echo an ACTION request.",
>                 "name" : "echo",
>                 "request" : { "type" : "object" },
>                 "response" : {
>                     "title" : "Echo action response",
>                     "type" : "object",
>                     "properties" : {
>                         "method" : {
>                             "type" : "string",
>                             "enum" : [ "action" ]
>                         },
>                         "action" : { "type" : "string" },
>                         "content" : { "type" : "object" },
>                         "parameters" : { "type" : "object" },
>                         "context" : { "type" : "object" }
>                     }
>                 }
>             }
>         ],
>         "queries" : [
>             {
>                 "description" : "Echo a query-filter request.",
>                 "type" : "FILTER",
>                 "queryableFields" : [ "*" ]
>             },
>             {
>                 "description" : "Echo a query-all request.",
>                 "type" : "ID",
>                 "queryId" : "query-all"
>             },
>             {
>                 "description" : "Echo a query-all-ids request.",
>                 "type" : "ID",
>                 "queryId" : "query-all-ids"
>             }
>         ],
>         "resourceSchema" : {
>             "title" : "Echo resource",
>             "type" : "object",
>             "properties" : {
>                 "method" : {
>                     "title" : "CREST method",
>                     "type" : "string"
>                 },
>                 "resourceName" : { "type" : "string" },
>                 "parameters" : { "type" : "object" },
>                 "context" : { "type" : "object" }
>             }
>         }
>     }
> }
> ```

> **Collapse: Sample Custom Endpoint Script**
>
> ```javascript
> (function(){
>     if (request.method === "create") {
>         return {
>             method: "create",
>             resourceName: request.resourcePath,
>             newResourceId: request.newResourceId,
>             parameters: request.additionalParameters,
>             content: request.content,
>             context: context.current
>         };
>     } else if (request.method === "read") {
>         return {
>             method: "read",
>             resourceName: request.resourcePath,
>             parameters: request.additionalParameters,
>             context: context.current
>         };
>     } else if (request.method === "update") {
>         return {
>             method: "update",
>             resourceName: request.resourcePath,
>             revision: request.revision,
>             parameters: request.additionalParameters,
>             content: request.content,
>             context: context.current
>         };
>     } else if (request.method === "patch") {
>         return {
>             method: "patch",
>             resourceName: request.resourcePath,
>             revision: request.revision,
>             parameters: request.additionalParameters,
>             patch: request.patchOperations,
>             context: context.current
>         };
>     } else if (request.method === "query") {
>         // query results must be returned as a list of maps
>         return [ {
>             method: "query",
>             resourceName: request.resourcePath,
>             pagedResultsCookie: request.pagedResultsCookie,
>             pagedResultsOffset: request.pagedResultsOffset,
>             pageSize: request.pageSize,
>             queryId: request.queryId,
>             queryFilter: request.queryFilter.toString(),
>             parameters: request.additionalParameters,
>             content: request.content,
>             context: context.current
>         } ];
>     } else if (request.method === "delete") {
>         return {
>             method: "delete",
>             resourceName: request.resourcePath,
>             revision: request.revision,
>             parameters: request.additionalParameters,
>             context: context.current
>         };
>     } else if (request.method === "action") {
>         return {
>             method: "action",
>             action: request.action,
>             content: request.content,
>             parameters: request.additionalParameters,
>             context: context.current
>         };
>     } else {
>         throw { code : 500, message : "Unknown request type " + request.method };
>     }
> })();
> ```

A sample custom endpoint configuration is provided in the `openidm/samples/example-configurations/custom-endpoint` directory. The sample includes three files:

* conf/endpoint-echo.json

  Provides the configuration for the endpoint.

* script/echo.js

  Provides the endpoint functionality in JavaScript.

* script/echo.groovy

  Provides the endpoint functionality in Groovy.

|   |                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------- |
|   | This sample endpoint is described in detail in the sample: [Create a custom endpoint](../samples-guide/custom-endpoint.html). |

## Custom endpoint configuration

A custom endpoint configuration *(tooltip: You can create and change custom endpoint configurations over REST at the config/endpoint/\<name> endpoint, or in files named conf/endpoint-\<name>.json, where \<name> generally describes the purpose of the endpoint.)* has the following structure:

```json
{
    "context" : "context path",
    "type" : "script language",
    "source" : "script source" | "file" : "script file",
    "apiDescription" : "API descriptor object"
}
```

* `context`

  string, optional

  The root URL path for the endpoint, in other words, the *route* to the endpoint. An endpoint with the context `endpoint/test` is addressable over REST at the URL `http://localhost:8080/openidm/endpoint/test` or by using a script such as `openidm.read("endpoint/test")`.

  Endpoint contexts support wild cards, as shown in the preceding example. The `endpoint/linkedview/*` route matches the following patterns:

  ```
  endpoint/linkedView/managed/user/bjensen
  endpoint/linkedView/system/ldap/account/bjensen
  endpoint/linkedView/
  endpoint/linkedView
  ```

  The `context` parameter is not mandatory in the endpoint configuration file. If you do not include a `context`, the route to the endpoint is identified by the name of the file. For example, in the sample endpoint configuration provided in `openidm/samples/example-configurations/custom-endpoint/conf/endpoint-echo.json`, the route to the endpoint is `endpoint/echo`.

* `type`

  string, required

  The script type.

  IDM supports `"text/javascript"` and `"groovy"`.

* `file` or `source`

  The path to the script file, or the script itself, inline.

  For example:

  ```none
  "file" : "workflow/gettasksview.js"
  ```

  or

  ```none
  "source" : "require('linkedView').fetch(request.resourcePath);"
  ```

* `apiDescription`

  JSON object, optional

  Describes the custom endpoint and includes its documentation in the [REST API Explorer](../rest-api-reference/api-explorer.html).

|   |                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Custom endpoints do not support versioning.You must set authorization for any custom endpoints that you add, for example, by restricting the methods to the appropriate roles. For more information, refer to [Authorization and Roles](../auth-guide/authorization-and-roles.html#idm-authorization). |

## Custom endpoint scripts

The custom endpoint script files in the `samples/example-configurations/custom-endpoint/script` directory demonstrate all the HTTP operations that can be called by a script.

Each HTTP operation is associated with a `method`. Allowed methods are:

* `create`

* `read`

* `update`

* `delete`

* `patch`

* `action`

* `query`

Requests sent to the custom endpoint return a list of the variables available to each method.

All scripts are invoked with a global `request` variable in their scope. This request structure carries all the information about the request.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | `Read` requests on custom endpoints must not modify the state of the resource, either on the client or the server, as this can make them susceptible to Cross-Site Request Forgery (CSRF) exploits.Endpoints which only read data without modifying state are inherently safe from CSRF attacks. This is consistent with the US National Security Agency's *Guidelines for Implementation of REST*, which states, "... CSRF protections need only be applied to endpoints that will modify information in some way." |

Custom endpoint scripts *must* return a JSON object. The structure of the return object depends on the `method` in the request.

The following example shows the `create` method in the `echo.js` file:

```javascript
if (request.method === "create") {
    return {
        method: "create",
        resourceName: request.resourcePath,
        newResourceId: request.newResourceId,
        parameters: request.additionalParameters,
        content: request.content,
        context: context.current
    }
}
```

The following example shows the `query` method in the `echo.groovy` file:

```groovy
else if (request instanceof QueryRequest) {
    // query results must be returned as a list of maps
    return [
        [
            method: "query",
            resourceName: request.resourcePath,
            pagedResultsCookie: request.pagedResultsCookie,
            pagedResultsOffset: request.pagedResultsOffset,
            pageSize: request.pageSize,
            queryId: request.queryId,
            queryFilter: request.queryFilter.toString(),
            parameters: request.additionalParameters,
            context: context.toJsonValue().getObject()
        ]
    ]
}
```

Depending on the method, the variables available to the script can include the following:

* `resourceName`

  The name of the resource without the `endpoint/` prefix, such as `echo`.

* `newResourceId`

  The identifier of the new object available as the results of a `create` request.

* `revision`

  The revision of the object.

* `parameters`

  Any additional parameters provided in the request. The sample code returns request parameters from an HTTP GET with `?param=x`, as `"parameters":{"param":"x"}`.

* `content`

  Content based on the latest revision of the object, using `getObject`.

* `context`

  The context of the request, including headers and security. For more information, refer to [Request context chain](request-context.html).

* Paging parameters

  The `pagedResultsCookie`, `pagedResultsOffset`, and `pageSize` parameters are specific to `query` methods. For more information refer to [Page Query Results](../objects-guide/queries.html#paging-query-results).

* Query parameters

  The `queryId` and `queryFilter` parameters are specific to `query` methods. For more information, refer to [Construct Queries](../objects-guide/queries.html#constructing-queries).

## Script exceptions

Some custom endpoint scripts require exception-handling logic. To return meaningful messages in REST responses and in logs, you must comply with the language-specific method of throwing errors.

A script written in JavaScript should comply with the following exception format:

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

Exception objects include the specified HTTP error code, the corresponding HTTP error message (such as `Bad Request`), a custom error message, and additional details that may be helpful to determine what actions need to be taken to fix the error.

A script written in Groovy should comply with the following exception format:

```groovy
import org.forgerock.json.resource.ResourceException
import org.forgerock.json.JsonValue

throw new ResourceException(404, "Your error message").setDetail(new JsonValue([
    "var": "parameter1",
    "complexDetailObject" : [
        "detail1",
        "detail2"
    ]
]))
```

## Write an API descriptor for a custom endpoint

Most IDM endpoints are described in the [REST API Explorer](../rest-api-reference/api-explorer.html). Documentation is not generated automatically for custom endpoints.

To generate the documentation for your custom endpoint in the API Explorer, add an `apiDescription` object to your custom endpoint configuration file. The `apiDescription` object includes the following properties:

* `title`

  The endpoint name that expresses its purpose, for example, `Audit`, or `Authentication`.

* `description`

  A description of the endpoint.

* `mvccSupported`

  A Boolean value that indicates whether object versioning is supported. To enable `If-None-Match` or `If-Match` headers in read, delete, and patch requests, this property must be `true`.

* Operations

  An object that describes each operation supported on that endpoint (`create`, `read`, `update`, `delete`, `patch`, `actions`, and `queries`).

* `resourceSchema`

  The schema for the objects at this endpoint.

To refer to examples of the API descriptors included in IDM, log in to the [admin UI](http://localhost:8080/admin), then point your browser to <http://localhost:8080/openidm?_crestapi>.

Compare the descriptors at that URL with what you refer to in the [API Explorer](http://localhost:8080/admin/#apiExplorer).

In addition, the sample configuration file (`openidm/samples/example-configurations/custom-endpoint/conf/endpoint-echo.json`) shows how API descriptors must be constructed:

> **Collapse: Sample API Descriptor Object**
>
> ```json
> {
>     "apiDescription" : {
>         "title" : "Echo",
>         "description" : "Service that echo's your HTTP requests.",
>         "mvccSupported" : false,
>         "create" : {
>             "description" : "Echo a CREATE request.",
>             "mode" : "ID_FROM_SERVER",
>             "singleton" : false
>         },
>         "read" : { "description" : "Echo a READ request." },
>         "update" : { "description" : "Echo an UPDATE request." },
>         "delete" : { "description" : "Echo a DELETE request." },
>         "patch" : {
>             "description" : "Echo a PATCH request.",
>             "operations" : [ "ADD", "REMOVE", "REPLACE", "INCREMENT", "COPY", "MOVE", "TRANSFORM" ]
>         },
>         "actions" : [
>             {
>                 "description" : "Echo an ACTION request.",
>                 "name" : "echo",
>                 "request" : { "type" : "object" },
>                 "response" : {
>                     "title" : "Echo action response",
>                     "type" : "object",
>                     "properties" : {
>                         "method" : {
>                             "type" : "string",
>                             "enum" : [ "action" ]
>                         },
>                         "action" : { "type" : "string" },
>                         "content" : { "type" : "object" },
>                         "parameters" : { "type" : "object" },
>                         "context" : { "type" : "object" }
>                     }
>                 }
>             }
>         ],
>         "queries" : [
>             {
>                 "description" : "Echo a query-filter request.",
>                 "type" : "FILTER",
>                 "queryableFields" : [ "*" ]
>             },
>             {
>                 "description" : "Echo a query-all request.",
>                 "type" : "ID",
>                 "queryId" : "query-all"
>             },
>             {
>                 "description" : "Echo a query-all-ids request.",
>                 "type" : "ID",
>                 "queryId" : "query-all-ids"
>             }
>         ],
>         "resourceSchema" : {
>             "title" : "Echo resource",
>             "type" : "object",
>             "properties" : {
>                 "method" : {
>                     "title" : "CREST method",
>                     "type" : "string"
>                 },
>                 "resourceName" : { "type" : "string" },
>                 "parameters" : { "type" : "object" },
>                 "context" : { "type" : "object" }
>             }
>         }
>     }
> }
> ```
>
> This object generates API documentation in the API explorer that looks like this:
>
> ![echo-api-descriptor](_images/echo-api-descriptor.png)

---

---
title: Filter objects
description: Configure filter objects in the PingIDM router to trigger scripts on request, response, or failure based on pattern and method
component: pingidm
version: 8.1
page_id: pingidm:scripting-guide:filter-objects
canonical_url: https://docs.pingidentity.com/pingidm/8.1/scripting-guide/filter-objects.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scripting", "Router", "Filters", "Objects"]
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
title: "Pattern matching in the <span class=\"fr-alt\" title=\"You can edit the router configuration over REST at the config/router endpoint, or directly in the conf/router.json file.\">router configuration</span>"
description: Use pattern matching in the PingIDM router configuration to limit script execution to specific methods and endpoints
component: pingidm
version: 8.1
page_id: pingidm:scripting-guide:script-pattern-match
canonical_url: https://docs.pingidentity.com/pingidm/8.1/scripting-guide/script-pattern-match.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scripting", "Router", "Configuration", "Pattern Matching"]
---

# Pattern matching in the router configuration *(tooltip: You can edit the router configuration over REST at the config/router endpoint, or directly in the conf/router.json file.)*

Pattern matching can minimize overhead in the router service. The default router configuration *(tooltip: You can edit the router configuration over REST at the config/router endpoint, or directly in the conf/router.json file.)* includes instances of the `pattern` filter object, that limit script requests to specified methods and endpoints.

Based on the following code snippet, the router service would trigger the `policyFilter.js` script for `CREATE` and `UPDATE` calls to managed and internal objects:

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
description: Register custom scripted actions on PingIDM managed object endpoints and learn which variables are available to those scripts
component: pingidm
version: 8.1
page_id: pingidm:scripting-guide:custom-scripted-actions
canonical_url: https://docs.pingidentity.com/pingidm/8.1/scripting-guide/custom-scripted-actions.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scripting", "Registration", "Custom", "Managed Object"]
section_ids:
  example_scenario: Example scenario
---

# Register custom scripted actions

You can register custom scripts that initiate some arbitrary action on a managed object endpoint. You can declare any number of actions in your managed object schema and associate those actions with a script.

The return value of a custom scripted action is ignored. The managed object is returned as the response of the scripted action, whether that object has been updated by the script or not.

Custom scripted actions have access to the following variables:

* `context`

* `request`

* `resourcePath`

* `object`

## Example scenario

In this scenario, you want your managed users to have the option to receive update notifications. You can define an *action* that toggles the value of a specific property on the user object.

1. Add an `updates` property to the managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint, or directly in the conf/managed.json file.)*:

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
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request POST \
   "http://localhost:8080/openidm/managed/user/ID?_action=toggleUpdates"
   ```

   You can now test the functionality.

4. Create a managed user, `bjensen`, with an `updates` property set to `true`:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
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
   "http://localhost:8080/openidm/managed/user?_action=create"
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
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request POST \
   "http://localhost:8080/openidm/managed/user/9dce06d4-2fc1-4830-a92b-bd35c2f6bcbb?_action=toggleUpdates"
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

   |   |                                                                                              |
   | - | -------------------------------------------------------------------------------------------- |
   |   | Note in the command output that this action has set bjensen's `updates` property to `false`. |

---

---
title: Request context chain
description: The PingIDM request context chain, including root, security, HTTP, and router contexts established for each request
component: pingidm
version: 8.1
page_id: pingidm:scripting-guide:request-context
canonical_url: https://docs.pingidentity.com/pingidm/8.1/scripting-guide/request-context.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scripting", "Context Chain"]
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
description: Configure the PingIDM router service, which provides a uniform interface to managed, system, and configuration objects using filters
component: pingidm
version: 8.1
page_id: pingidm:scripting-guide:router-config
canonical_url: https://docs.pingidentity.com/pingidm/8.1/scripting-guide/router-config.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scripting", "Router", "Configuration"]
---

# Router configuration

The router service provides the uniform interface to all IDM objects: managed objects, system objects, configuration objects, and so on.

The router configuration *(tooltip: You can edit the router configuration over REST at the config/router endpoint, or directly in the conf/router.json file.)* contains an array of [Filter objects](filter-objects.html):

```json
{
  "filters": [ filter object, ... ]
}
```

---

---
title: Script configuration
description: Configure PingIDM script engine parameters for JavaScript and Groovy, including optimization levels, recompile intervals, and source directories
component: pingidm
version: 8.1
page_id: pingidm:scripting-guide:script-config
canonical_url: https://docs.pingidentity.com/pingidm/8.1/scripting-guide/script-config.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scripting", "Configuration", "JavaScript", "Groovy"]
---

# Script configuration

To modify the parameters used for compiling, debugging, and running scripts, edit the script configuration *(tooltip: You can manage the script configuration over REST at the config/script endpoint, or directly in the conf/script.json file.)*.

Script Configuration Parameters

* properties

  Any custom properties.

* ECMAScript

  JavaScript debug and compile options. JavaScript is an ECMAScript language.

  * `javascript.optimization.level` - The current optimization level. Expected integer range is from -1 to 9. For more information about optimization level, refer to [Rhino Optimization](https://rhino.github.io/docs/configuration/#optimization-levels).

    The default value is `9`.

  * `javascript.recompile.minimumInterval` - The minimum time between script recompile.

    The default value is `60000`, or 60 seconds. This means that any changes made to scripts will not get picked up for up to 60 seconds. If you are developing scripts, reduce this parameter to around `100` (100 milliseconds).

    If you set the `javascript.recompile.minimumInterval` to `-1`, or remove this property from the script configuration *(tooltip: You can manage the script configuration over REST at the config/script endpoint, or directly in the conf/script.json file.)*, IDM does not poll JavaScript files to check for changes.

* Groovy

  Compilation and debugging options related to Groovy scripts. Many of these options are commented out in the default script configuration file. Remove the comments to set these properties:

  * `groovy.warnings` - The Groovy script log level. Possible values are `none`, `likely`, `possible`, and `paranoia`.

  * `groovy.source.encoding` - The Groovy script encoding format. Possible values are `UTF-8` and `US-ASCII`.

  * `groovy.target.directory` - The compiled Groovy class output directory. The default directory is `install-dir/classes` .

  * `groovy.target.bytecode` - The Groovy script bytecode version. The default version is `1.5`.

  * `groovy.classpath` - The directory where the compiler should look for compiled classes. The default classpath is `install-dir/lib` .

    To call an external library from a Groovy script, you must specify the complete path to the .jar file or files, as a value of this property. For example:

    ```groovy
    "groovy.classpath" : "/&{idm.install.dir}/lib/http-builder-0.7.1.jar:
            /&{idm.install.dir}/lib/json-lib-2.3-jdk15.jar:
            /&{idm.install.dir}/lib/xml-resolver-1.2.jar:
            /&{idm.install.dir}/lib/commons-collections-3.2.1.jar",
    ```

    |   |                                                                                                                                       |
    | - | ------------------------------------------------------------------------------------------------------------------------------------- |
    |   | If you're deploying on Microsoft Windows, use a semicolon (`;`) instead of a colon to separate directories in the `groovy.classpath`. |

  * `groovy.output.verbose` - Verbosity of stack traces. Boolean, `true` or `false`.

  * `groovy.output.debug` - Whether to output debug messages. Boolean, \`true \` or `false`.

  * `groovy.errors.tolerance` - The number of non-fatal errors that can occur before a compilation is aborted. The default is `10` errors.

  * `groovy.script.extension` - Groovy script file extension. The default is `.groovy`.

  * `groovy.script.base` - Groovy script base class. By default, any class extends `groovy.lang.Script`.

  * `groovy.recompile` - Whether scripts can be recompiled. Boolean, `true` or `false`, with default `true`.

  * `groovy.recompile.minimumInterval` - Groovy script minimum recompile interval.

    The default value is `60000`, or 60 seconds. Using the default value, any changes made to scripts may not be in effect for up to 60 seconds. If you are developing scripts, reduce this parameter to `100` (100 milliseconds).

  * `groovy.target.indy` - Whether to use a [Groovy indy test](http://docs.groovy-lang.org/latest/html/documentation/invokedynamic-support.html). Boolean, `true` or`false`, with default `true`.

  * `groovy.disabled.global.ast.transformations` - A list of disabled Abstract Syntax Transformations (ASTs).

* sources

  The directories where IDM looks for referenced scripts.

  Excerpt of a script configuration *(tooltip: You can manage the script configuration over REST at the config/script endpoint, or directly in the conf/script.json file.)* displaying default directories:

  ```json
  "sources" : {
     "default" : {
         "directory" : "&{idm.install.dir}/bin/defaults/script"
     },
     "install" : {
         "directory" : "&{idm.install.dir}"
     },
     "project" : {
         "directory" : "&{idm.instance.dir}"
     },
     "project-script" : {
         "directory" : "&{idm.instance.dir}/script"
  }
  ```

  |   |                                                                    |
  | - | ------------------------------------------------------------------ |
  |   | IDM loads scripts from `sources` in reverse order (bottom to top). |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | By default, debug information (for example, file name and line number) is excluded from JavaScript and Groovy exceptions. To troubleshoot script exceptions, you can include debug information by changing the following settings to `true` in `resolver/boot.properties`:```properties
javascript.exception.debug.info=false
groovy.exception.debug.info=false
```Including debug information in a production environment is not recommended. |

---

---
title: Script execution sequence
description: The PingIDM script execution sequence for onRequest and onResponse filters, with onRequest processed top-down and onResponse bottom-up
component: pingidm
version: 8.1
page_id: pingidm:scripting-guide:script-sequence
canonical_url: https://docs.pingidentity.com/pingidm/8.1/scripting-guide/script-sequence.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scripting", "Router", "Configuration"]
---

# Script execution sequence

All `onRequest` and `onResponse` scripts are executed in sequence. First, the `onRequest` scripts are executed from the top down, then the `onResponse` scripts are executed from the bottom up.

```
client -> filter 1 onRequest -> filter 2 onRequest -> resource
client <- filter 1 onResponse <- filter 2 onResponse <- resource
```

The following sample router configuration *(tooltip: You can edit the router configuration over REST at the config/router endpoint, or directly in the conf/router.json file.)* shows the order in which the scripts would be executed:

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
            "pattern" : "^managed/user",
            "methods" : [
                "read"
            ],
            "onRequest" : {
                "type" : "text/javascript",
                "source" : "console.log('requestFilter 1');"
            }
        },
        {
            "pattern" : "^managed/user",
            "methods" : [
                "read"
            ],
            "onResponse" : {
                "type" : "text/javascript",
                "source" : "console.log('responseFilter 1');"
            }
        },
        {
            "pattern" : "^managed/user",
            "methods" : [
                "read"
            ],
            "onRequest" : {
                "type" : "text/javascript",
                "source" : "console.log('requestFilter 2');"
            }
        },
        {
            "pattern" : "^managed/user",
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
>             "pattern": "^managed/user",
>             "methods": [
>                 "create",
>                 "update"
>             ],
>             "onResponse": {
>                 "type": "text/javascript",
>                 "file": "scripts/afterUpdateUser.js"
>             }
>         }
>     ]
> }
> ```

---

---
title: Script scope
description: Script scope provided to PingIDM router filter scripts, including openidm, request, response, and exception objects
component: pingidm
version: 8.1
page_id: pingidm:scripting-guide:filter-script-scope
canonical_url: https://docs.pingidentity.com/pingidm/8.1/scripting-guide/filter-script-scope.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scripting", "Router", "Configuration", "Scope"]
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

  [openidm-functions object](scripting-func-ref.html)

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
description: Overview of where PingIDM scripts can be triggered, including mappings, managed object configuration, and the router configuration
component: pingidm
version: 8.1
page_id: pingidm:scripting-guide:script-triggers
canonical_url: https://docs.pingidentity.com/pingidm/8.1/scripting-guide/script-triggers.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scripting", "Triggers"]
---

# Script triggers

|   |                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------- |
|   | For more information about the variables available to scripts, refer to [Script variables](script-vars.html). |

Scripts can be triggered in different places, and by different events. The following list indicates the configuration files in which scripts can be referenced, the events upon which the scripts can be triggered, and the actual scripts that can be triggered on each of these files.

* Scripts called in [mappings](../synchronization-guide/mappings.html)

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

    `sync.json` supports only one script per hook. If multiple scripts are defined for the same hook, only the last one is kept.

  * Scripts inside policies

    condition

    Within a synchronization policy, you can use a `condition` script to apply different policies based on the link type, for example:

    ```json
    "condition" : {
      "type" : "text/javascript",
      "source" : "linkQualifier == \"user\""
    }
    ```

* Scripts called in the managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint, or directly in the conf/managed.json file.)*

  onCreate, onRead, onUpdate, onDelete, onValidate, onRetrieve, onStore, onSync, postCreate, postUpdate, and postDelete

  The managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint, or directly in the conf/managed.json file.)* supports only one script per hook. If multiple scripts are defined for the same hook, only the last one is kept.

* Scripts called in the router configuration *(tooltip: You can edit the router configuration over REST at the config/router endpoint, or directly in the conf/router.json file.)*

  onRequest, onResponse, onFailure

  The router configuration *(tooltip: You can edit the router configuration over REST at the config/router endpoint, or directly in the conf/router.json file.)* supports multiple scripts per hook.

---

---
title: Script triggers defined in mappings
description: Script triggers and available variables for PingIDM mapping configuration, covering object-mapping, property, and policy objects
component: pingidm
version: 8.1
page_id: pingidm:scripting-guide:script-triggers-mappings
canonical_url: https://docs.pingidentity.com/pingidm/8.1/scripting-guide/script-triggers-mappings.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scripting", "Triggers", "Managed Objects", "Mappings"]
section_ids:
  object_mapping_object: Object-mapping object
  property_object: Property object
  policy_object: Policy object
---

# Script triggers defined in mappings

For information about how managed objects in mappings are handled, and the script triggers available, refer to [Object-Mapping Objects](../synchronization-guide/synchronization-ref.html#sync-object-mapping).

## Object-mapping object

| Trigger                                                      | Variable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `correlationQuery`, `correlationScript`*Returns JSON object* | * **source**: Represents the source object.

* **linkQualifier**: The link qualifier associated with the current sync.

* **context**: Information related to the current request, such as source and target.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `linkQualifiers`*Returns JSON object*                        | - **mapping**: The name of the current mapping.

- **object**: The value of the source object. During a DELETE event, that source object may not exist, and may be null.

- **oldValue**: The former value of the deleted source object, if any. If the source object is new, oldValue will be null. When there are deleted objects, oldValue is populated only if the source is a managed object.

- **returnAll** (boolean): Link qualifier scripts must return every valid link qualifier when returnAll is true, independent of the source object. If returnAll is true, the script must not attempt to use the object variable, because it will be null. It's best practice to configure scripts to start with a check for the value of returnAll.

- **context**: Information related to the current request, such as source and target.                                                                           |
| `onCreate`*Returns JSON object*                              | * **source**: Represents the source object.

* **target**: Represents the target object.

* **situation**: The situation associated with the current sync operation.

* **linkQualifier**: The link qualifier associated with the current sync operation.

* **context**: Information related to the current sync operation.

* **sourceId**: The object ID for the source object.

* **targetId**: The object ID for the target object.

* **mappingConfig**: A configuration object representing the mapping being processed.                                                                                                                                                                                                                                                                                                                                                                                          |
| `onDelete`, `onUpdate`*Returns JSON object*                  | - **source**: Represents the source object.

- **target**: Represents the target object.

- **oldTarget**: Represents the target object prior to the DELETE or UPDATE action.

- **oldSource**: Available during UPDATE and DELETE operations performed through implicit sync. When implicit synchronization triggers on a specific change to the source object, it can populate `oldSource` with the prior value. During reconciliation and liveSync operations, `oldSource` is undefined.

- **situation**: The situation associated with the current sync operation.

- **linkQualifier**: The link qualifier associated with the current sync.

- **context**: Information related to the current sync operation.

- **sourceId**: The object ID for the source object.

- **targetId**: The object ID for the target object.

- **mappingConfig**: A configuration object representing the mapping being processed. |
| `onLink`, `onUnlink`*Returns JSON object*                    | * **source**: Represents the source object.

* **target**: Represents the target object.

* **oldSource**: Available during UPDATE and DELETE operations performed through implicit sync. When implicit synchronization triggers on a specific change to the source object, it can populate `oldSource` with the prior value. During reconciliation and liveSync operations, `oldSource` is undefined.

* **linkQualifier**: The link qualifier associated with the current sync operation.

* **context**: Information related to the current sync operation.

* **sourceId**: The object ID for the source object.

* **targetId**: The object ID for the target object.

* **mappingConfig**: A configuration object representing the mapping being processed.                                                                                                                                                        |
| `onError`*Returns JSON object*                               | - **source**: Represents the source object.

- **target**: Represents the target object.

- **linkQualifier**: The link qualifier associated with the current sync operation.

- **context**: Information related to the current sync operation.

- **situation**: The situation associated with the current sync operation.

- **sourceId**: The object ID for the source object.

- **targetId**: The object ID for the target object.

- **oldSource**: Available during UPDATE and DELETE operations performed through implicit sync. When implicit synchronization triggers on a specific change to the source object, it can populate `oldSource` with the prior value. During reconciliation and liveSync operations, `oldSource` is undefined.

- **error**: The result of the resource exception, as a JSON object.

- **mappingConfig**: A configuration object representing the mapping being processed.      |
| `postMapping`*Returns JSON object*                           | * **source**: Represents the source object.

* **target**: Represents the target object.

* **oldSource**: Available during UPDATE and DELETE operations performed through implicit sync. When implicit synchronization triggers on a specific change to the source object, it can populate `oldSource` with the prior value. During reconciliation and liveSync operations, `oldSource` is undefined.

* **oldTarget**: Represents the target object prior to any changes.

* **linkQualifier**: The link qualifier associated with the current sync operation.

* **context**: Information related to the current sync operation.

* **sourceId**: The object ID for the source object.

* **targetId**: The object ID for the target object.

* **mappingConfig**: A configuration object representing the mapping being processed.                                                                                   |
| `result`*Returns JSON object of reconciliation results*      | - **source**: Provides statistics about the source phase of the reconciliation.

- **target**: Provides statistics about the target phase of the reconciliation.

- **context**: Information related to the current operation, such as source and target.

- **global**: Provides statistics about the entire reconciliation operation.

- **mappingConfig**: A configuration object representing the mapping being processed.

- **reconState**: Provides the state of reconciliation operation; such as, *success*, *failure*, or *active*.                                                                                                                                                                                                                                                                                                                                                                            |
| `validSource`*Returns boolean*                               | * **source**: Represents the source object.

* **linkQualifier**: The link qualifier associated with the current sync operation.

* **context**: Information related to the current sync operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `validTarget`*Returns boolean*                               | - **target**: Represents the target object.

- **linkQualifier**: The link qualifier associated with the current sync operation.

- **context**: Information related to the current sync operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

## Property object

| Trigger                          | Variable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `condition`*Returns boolean*     | * **object**: The current object being mapped.

* **context**: Information related to the current operation, such as source and target.

* **linkQualifier**: The link qualifier associated with the current sync operation.

* **target**: Represents the target object.

* **oldTarget**: Represents the target object prior to any changes.

* **oldSource**: Available during UPDATE and DELETE operations performed through implicit sync. When implicit synchronization triggers on a specific change to the source object, it can populate `oldSource` with the prior value. During reconciliation and liveSync operations, `oldSource` is undefined. |
| `transform`*Returns JSON object* | - **source**: Represents the source object.

- **linkQualifier**: The link qualifier associated with the current sync operation.

- **context**: Information related to the current sync operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## Policy object

| Trigger                                 | Variable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `action`*Returns string OR JSON object* | * **source**: Represents the source object.

* **target**: Represents the target object.

* **sourceAction** (boolean): Indicates whether the action is being processed during the source or target synchronization phase (true if performed during a source synchronization, false if performed during a target synchronization).

* **linkQualifier**: The link qualifier used for this operation (`default` if no other link qualifier is specified).

* **context**: Information related to the current sync operation.

* **recon**: Represents the reconciliation operation.

* The `recon.actionParam` object contains information about the current reconciliation operation and includes the following variables:

  * `reconId`: The ID of the reconciliation operation.

  * `mapping`: The mapping for which the reconciliation was performed, for example, `systemLdapAccounts_managedUser`.

  * `situation`: The situation encountered, for example, `AMBIGUOUS`.

  * `action`: The default action that would be used for this situation, if not for this script. The script being executed replaces the default action (and is used instead of any other named action).

  * `sourceId`: The `_id` value of the source record.

  * `linkQualifier`: The link qualifier used for that mapping, (`default` if no other link qualifier is specified).

  * `targetId`: The `_id` value of the target record involved in a reconciliation. In a `CONFIRMED` situation, the `targetId` points to the already linked target. If there is no target, the `targetId` is undefined.

  * `ambiguousTargetIds`: An array of the target record IDs that were found in an `AMBIGUOUS` situation during correlation.

  * `_action`: The synchronization action (only `performAction` is supported). |
| `postAction`*Returns JSON object*       | - **source**: Represents the source object.

- **target**: Represents the target object.

- **action**: The sync action that was performed.

- **sourceAction** (boolean): Indicates whether the action is being processed during the source or target synchronization phase (true if performed during a source synchronization, false if performed during a target synchronization).

- **linkQualifier**: The link qualifier used for this operation (`default` if no other link qualifier is specified).

- **reconId**: Represents the ID of the reconciliation.

- **situation**: Represents the situation for this policy.

- **context**: Information related to the current operation, such as source and target.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

---

---
title: "Script triggers defined in the <span class=\"fr-alt\" title=\"You can edit the managed object configuration over REST at the config/managed endpoint, or directly in the conf/managed.json file.\">managed object configuration</span>"
description: Script triggers and available variables for PingIDM managed object configuration, including onCreate, onUpdate, onDelete, and onStore
component: pingidm
version: 8.1
page_id: pingidm:scripting-guide:script-triggers-managedConfig
canonical_url: https://docs.pingidentity.com/pingidm/8.1/scripting-guide/script-triggers-managedConfig.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scripting", "Triggers", "Managed Object", "Configuration"]
section_ids:
  managed_object_configuration_object: Managed object configuration object
  property_object: Property object
---

# Script triggers defined in the managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint, or directly in the conf/managed.json file.)*

For information about how managed objects are handled and the available script triggers, refer to [Managed objects reference](../objects-guide/appendix-managed-objects.html).

## Managed object configuration object

| Trigger                                                  | Variable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `onCreate`, `postCreate`                                 | * **object**: The content of the object being created.

* **newObject**: The object after the create operation is complete.

* **context**: Information related to the current request, such as client, end user, and routing.

* **resourceName**: The resource path of the object of the query. For example, if you create a managed user with ID `42f8a60e-2019-4110-a10d-7231c3578e2b`, resourceName returns `managed/user/42f8a60e-2019-4110-a10d-7231c3578e2b`.

* **request**: Information related to the request, such as headers, credentials, and the desired action. Also includes the endpoint, and payload to be processed.                                                                                                                                                                                                                  |
| `onUpdate`, `postUpdate`*Returns JSON object*            | - **object**: The content of the object being updated.

- **oldObject**: The state of the object, before the update.

- **newObject**: Changes to be applied to the object. May continue with the `onUpdate` trigger.

- **context**: Information related to the current request, such as client, end user, and routing.

- **resourceName**: The resource path of the object the query.

- **request**: Information related to the request, such as headers, credentials, and the desired action. Also includes the endpoint, and payload to be processed.                                                                                                                                                                                                                                                                                               |
| `onDelete`, `onRetrieve`, `onRead`*Returns JSON object.* | * **object**: The content of the object.

* **context**: Information related to the current request, such as client, end user, and routing.

* **resourceName**: The resource path of the object the query.

* **request**: Information related to the request, such as headers, credentials, and the desired action. Also includes the endpoint, and payload to be processed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `postDelete`*Returns JSON object.*                       | - **oldObject**: Represents the deleted object.

- **context**: Information related to the current request, such as client, end user, and routing.

- **resourceName**: The resource path of the object the query is performed upon.

- **request**: Information related to the request, such as headers, credentials, and the desired action. Also includes the endpoint, and payload to be processed.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `onSync`*Returns JSON object*                            | * **oldObject**: Represents the object prior to sync. If sync has not been run before, the value will be `null`.

* **newObject**: Represents the object after sync is completed.

* **context**: Information related to the current request, such as client, end user, and routing.

* **request**: Information related to the request, such as headers, credentials, and the desired action. Also includes the endpoint, and payload to be processed.

* **resourceName**: An object representing the resource path the query is performed upon.

* **syncResults**: A map containing the results and details of the sync, including:

  * **success** (boolean): Success or failure of the sync operation.

  * **action**: Returns the name of the action performed as a string.

  * **syncDetails**: The mappings attempted during synchronization. |
| `onStore`, `onValidate`*Returns JSON object*             | - **object**: Represents the object being stored or validated.

- **value**: The content to be stored or validated for the object.

- **context**: Information related to the current request, such as client, end user, and routing.

- **resourceName**: The resource path of the object the query is performed upon.

- **request**: Information related to the request, such as headers, credentials, and the desired action. Also includes the endpoint, and payload to be processed.                                                                                                                                                                                                                                                                                                                                                                |

## Property object

| Trigger                                      | Variable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `onRetrieve`, `onStore`*Returns JSON object* | * **object**: Represents the object being operated upon.

* **property**: The value of the property being retrieved or stored.

* **propertyName**: The name of the property being retrieved or stored.

* **context**: Information related to the current request, such as client, end user, and routing.

* **resourceName**: The resource path of the object the query is performed upon.

* **request**: Information related to the request, such as headers, credentials, and the desired action. Also includes the endpoint, and payload to be processed. |
| `onValidate`*Returns JSON object*            | - **property**: The value of the property being validated.

- **context**: Information related to the current request, such as client, end user, and routing.

- **resourceName**: The resource path of the object the query is performed upon.

- **request**: Information related to the request, such as headers, credentials, and the desired action. Also includes the endpoint, and payload to be processed.                                                                                                                                              |

---

---
title: "Script triggers defined in the <span class=\"fr-alt\" title=\"You can edit the router configuration over REST at the config/router endpoint, or directly in the conf/router.json file.\">router configuration</span>"
description: Script triggers and available variables for PingIDM router configuration filters, including onRequest, onResponse, and onFailure
component: pingidm
version: 8.1
page_id: pingidm:scripting-guide:script-triggers-routerConfig
canonical_url: https://docs.pingidentity.com/pingidm/8.1/scripting-guide/script-triggers-routerConfig.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scripting", "Triggers", "Router", "Configuration"]
---

# Script triggers defined in the router configuration *(tooltip: You can edit the router configuration over REST at the config/router endpoint, or directly in the conf/router.json file.)*

| Trigger      | Variable  |
| ------------ | --------- |
| `onFailure`  | exception |
| `onRequest`  | request   |
| `onResponse` | response  |

---

---
title: Script variables
description: Overview of variables available to PingIDM scripts, determined by the trigger, configuration file, and object type
component: pingidm
version: 8.1
page_id: pingidm:scripting-guide:script-vars
canonical_url: https://docs.pingidentity.com/pingidm/8.1/scripting-guide/script-vars.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scripting", "Variables", "Managed Object", "Mappings"]
---

# Script variables

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | For more information about the variables available in script triggers, refer to [Script triggers](script-triggers.html). |

The variables available to a script depend on several factors:

* The trigger that launches the script.

* The configuration file in which that trigger is defined.

* The object type:

  * For objects defined in the managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint, or directly in the conf/managed.json file.)*, the object type is either a managed object, or a managed object property.

  * For objects defined in the mapping configuration *(tooltip: You can manage the mapping configuration over REST at the config/sync endpoint, directly in the conf/sync.json file, or in individual conf/mapping-\<mappingName>.json files.)*, the object can be an object-mapping object, a property object, or a policy object. For more information, refer to [Policy Objects](../synchronization-guide/synchronization-ref.html#sync-policy-objects)).

The following subtopics list the variables available to scripts, based on the configuration file in which the trigger is defined.

---

---
title: Scripting
description: Guide to scripting for PingIDM
component: pingidm
version: 8.1
page_id: pingidm:scripting-guide:preface
canonical_url: https://docs.pingidentity.com/pingidm/8.1/scripting-guide/preface.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scripting"]
page_aliases: ["index.adoc"]
---

# Scripting

> Guide to scripting for PingIDM.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Starting with IDM 8.1, the [legacy admin UI is deprecated](../release-notes/deprecated-functionality.html#legacy-admin-ui-deprecated) and is no longer bundled with IDM. New deployments should use the [Platform admin UI](../setup-guide/platform-admin-ui.html), which is the replacement for the legacy admin UI.Both UIs are available as separate downloads from the [Backstage download site](https://backstage.forgerock.com/downloads):- To install the Platform admin UI, follow the steps in [Install the Platform admin UI for standalone IDM](../setup-guide/platform-admin-ui.html).

- To continue using the legacy admin UI, follow the steps in [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html). |

Scripting lets you extend IDM functionality. For example, you can provide custom logic between source and target mappings, define correlation rules, filters, triggers, and so on. This guide shows you how to use scripts in IDM and provides reference information on the script engine.

[icon: cogs, set=fad, size=3x]

#### [Script Configuration](script-config.html)

Modify the parameters to compile, debug, and run scripts.

[icon: wrench, set=fad, size=3x]

#### [Custom Endpoints](script-custom-endpoints.html)

Run arbitrary scripts through the REST URI.

[icon: play-circle, set=fad, size=3x]

#### [Script Triggers](script-triggers.html)

Learn where and how you can trigger scripts.

[icon: file-code, set=fad, size=3x]

#### [Script Variables](script-vars.html)

Learn about the variables available to scripts.

IDM supports scripts written in JavaScript and Groovy, and uses the following libraries:

* Rhino version 1.7.14 to run JavaScript.

  |   |                                                                                                                                                                                  |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Rhino has limited support for ES6 / ES2015 (JavaScript version 1.7). For more information, refer to [Rhino ES2015 Support](https://mozilla.github.io/rhino/compat/engines.html). |

* Groovy version 3.0.22 for Groovy script support.

* Lodash 3.10.1 and Handlebars 4.7.7 for Rhino scripting.

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

* BouncyCastle 1.70 for signing JWTs.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The BouncyCastle .JAR file that is bundled with IDM includes the `org.bouncycastle.asn1.util.Dump` command-line utility. Although this utility is not used directly by IDM, it is possible to reference the utility in your scripts. Due to a security vulnerability in this utility, you should *not* reference it in your scripts. For more information, refer to the corresponding [BouncyCastle issue](https://github.com/bcgit/bc-java/issues/634). |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Script options and locations are defined in the script configuration *(tooltip: You can manage the script configuration over REST at the config/script endpoint, or directly in the conf/script.json file.)*.Default scripts are located in (`/path/to/openidm/bin/defaults/script/`). Do not modify the scripts in this directory. Rather copy the default scripts to a different location, make the changes, and update the referenced scripts in the applicable `conf/` file. You can put custom scripts in any of the locations referenced in the `sources` property in `conf/script.json`. |

---

---
title: Scripting function reference
description: Reference for PingIDM scripting functions, including openidm object methods, global utility functions, and logger functions
component: pingidm
version: 8.1
page_id: pingidm:scripting-guide:scripting-func-ref
canonical_url: https://docs.pingidentity.com/pingidm/8.1/scripting-guide/scripting-func-ref.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scripting", "Router", "Configuration", "Functions"]
section_ids:
  openidm_functions: openidm functions
  global-utility-functions: Global utility functions
  logger-functions: Log functions
---

# Scripting function reference

|   |                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------- |
|   | If you need to request specific resource versions, refer to [REST API versioning](../rest-api-reference/rest-api-versioning.html). |

Functions (access to managed objects, system objects, and configuration objects) within IDM are accessible to scripts using the `openidm` object that's included in the top-level scope provided to each script. IDM also provides a `logger` object and utility functions available globally in the script execution context.

|   |                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Most of the following function examples are in JavaScript. To use the functions in Groovy scripts, make adjustments as necessary. For example, you need to pass parameters using square brackets (not curly braces):```groovy
openidm.query("managed/user", ["_queryFilter" : "/userName sw \"user.1\""], ["userName", "_id"])
``` |

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
>     The container in which the object will be created, for example, `managed/user`.
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
>   An exception is thrown if the object couldn't be created.
>
> * Example
>
>   ```javascript
>   openidm.create("managed/user", ID, JSON object);
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
>           "_ref": "managed/user/adonnelly",
>           "_refResourceCollection": "managed/user",
>           "_refResourceId": "adonnelly",
>           "_refProperties": {
>             "_id": "ed6620e4-98ba-410c-abc0-e06dc1be7aa7",
>             "_rev": "000000008815942b"
>           }
>         }
>     }
>     ```
>
>     If an invalid value is specified (that's a value that doesn't exist for that property in the current object) the patch request is silently ignored.
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
>   openidm.patch("managed/role/" + role._id, null, [{"operation":"add", "field":"/members/-", "value": {"_ref":"managed/user/" + user._id}}]);
>   ```
>
>   Patching an object to remove an existing property:
>
>   ```javascript
>   openidm.patch("managed/user/" + user._id, null, [{"operation":"remove", "field":"marital_status", "value":"single"}]);
>   ```
>
>   Patching an object to remove a specific value from a multivalued relationship array:
>
>   ```javascript
>   openidm.patch("managed/user/" + user._id, null, [{
>     "operation": "remove",
>     "field": "/roles",
>     "value": {
>       "_ref": "managed/role/" + role._id,
>       "_refResourceCollection": "managed/role",
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
>   openidm.patch("managed/user/" + user._id, null, [{"operation":"replace", "field":"/password", "value":"Passw0rd"}]);
>   ```
>
>   Patching an object to increment an integer value:
>
>   ```javascript
>   openidm.patch("managed/user/" + user._id, null, [{"operation":"increment","field":"/age","value":1}]);
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
>   openidm.read("managed/user/"+userId, null, ["*", "manager"]);
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
>   var user_read = openidm.read('managed/user/' + source._id);
>   user_read['description'] = 'The entry has been updated';
>   openidm.update('managed/user/' + source._id, null, user_read);
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
>   openidm.delete('managed/user/'+ user._id, user._rev);
>   ```

> **Collapse: openidm.query(resourceName, params, fields)**
>
> This function performs a query on the specified resource object. Learn more in [Construct queries](../objects-guide/queries.html#constructing-queries).
>
> * Parameters
>
>   * resourceName
>
>     string
>
>     The resource object on which the query should be performed, for example, `"managed/user"`, or `"system/ldap/account"`.
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
>     You can find more information about `_queryFilter` syntax in [Common filter expressions](../objects-guide/queries.html#query-filters). Learn more in [Page query results](../objects-guide/queries.html#paging-query-results).
>
>   * fields
>
>     list
>
>     A list of the fields that should be returned in the result. The list of fields can include wild cards, such as `*` or `*_ref`. The following example returns only the `userName` and `_id` fields:
>
>     ```javascript
>     openidm.query("managed/user", { "_queryFilter": "/userName sw \"user.1\""}, ["userName", "_id"]);
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
>   openidm.query("managed/user", {'_queryFilter': userIdPropertyName + ' eq "' + security.authenticationId  + '"'});
>   ```
>
>   The following sample query references the `for-userName` query, defined in the repository configuration, to query the managed user repository:
>
>   ```javascript
>   openidm.query("managed/user", {"_queryId": "for-userName", "uid": request.additionalParameters.uid });
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
>     The resource that the function acts upon, for example, `managed/user`.
>
>   * actionName
>
>     string
>
>     The action to execute. Actions are used to represent functionality that isn't covered by the standard methods for a resource (create, read, update, delete, patch, or query). In general, you shouldn't use the `openidm.action` function for create, read, update, patch, delete or query operations. Instead, use the corresponding function specific to the operation (for example, `openidm.create`).
>
>     Using the operation-specific functions lets you benefit from the well-defined [REST API](../rest-api-reference/preface.html), which follows the same pattern as all other standard resources in the system. Using the REST API enhances usability for your own API, and enforces the established patterns.
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
>       Custom endpoints enable you to run arbitrary scripts through the REST URI, and are routed at `endpoint/name`, where name describes the purpose of the endpoint. Learn more about custom endpoints in [Create custom endpoints to launch scripts](script-custom-endpoints.html). You can implement whatever actions you require on a custom endpoint. IDM uses custom endpoints in its workflow implementation. Those endpoints, and their actions are as follows:
>
>       `endpoint/getprocessforuser` - `create, complete`\
>       `endpoint/gettasksview` - `create, complete`
>
>     * Actions supported on the `external` endpoint
>
>       * `external/email` - `send`, for example:
>
>         ```javascript
>         {
>             emailParams = {
>                 "from" : 'admin@example.com',
>                 "to" : user.mail,
>                 "subject" : 'Password expiry notification',
>                 "type" : 'text/plain',
>                 "body" : 'Your password will expire soon. Please change it!'
>             }
>             openidm.action("external/email", "send",  emailParams);
>         }
>         ```
>
>       * `external/email` - `sendTemplate`, for example:
>
>         ```javascript
>         {
>             emailParams = {
>                 "templateName" : "welcome",
>                 "to" : user.mail,
>                 "cc" : "ccUser1@example.com,ccUser2@example.com",
>                 "bcc" : "bigBoss@example.com"
>             }
>             openidm.action("external/email", "sendTemplate",  emailParams);
>         }
>         ```
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
>     Additional parameters passed to the script. The `params` object must be a set of simple key-value pairs and can't include complex values. The parameters must map directly to URL variables, which take the form `name1=val1&name2=val2&...`.
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
>   If the action can't be run, an object containing an `error` property is returned.

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
>     The cipher with which to encrypt the value, using the form "algorithm/mode/padding" or just "algorithm". Example: `AES/CBC/PKCS5Padding`.
>
>   * alias
>
>     string
>
>     A purpose defined in the `secrets.json` file, such as `idm.password.encryption`.
>
>     |   |                                                                                                          |
>     | - | -------------------------------------------------------------------------------------------------------- |
>     |   | Using key aliases from the keystore, such as `openidm-sym-default`, is deprecated. Use purposes instead. |
>
> * Returns
>
>   The value, encrypted with the specified cipher and key.
>
> * Throws
>
>   An exception is thrown if the object couldn't be encrypted.

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
>     The object whose value should be checked to determine if it's encrypted.
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
> **Supported Hashing Algorithms and Configuration Properties**
>
> | Algorithm                                        | Config Property and Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
> | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | `BCRYPT`\[[1](#_footnotedef_1 "View footnote.")] | * `cost`
>
>   Value between 4 and 31. Default is `13`.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
> | `PBKDF2`                                         | - `hashLength`
>
>   Byte-length of the generated hash. Default is `16`.
>
> - `saltLength`
>
>   Byte-length of the salt value. Default is `16`.
>
> - `iterations`
>
>   Number of cryptographic iterations. Default is `20000`.
>
> - `hmac`
>
>   HMAC algorithm. Default is `SHA3-256`.
>
>   Supported values:
>
>   * `SHA-224`
>
>   * `SHA-256`
>
>   * `SHA-384`
>
>   * `SHA-512`
>
>   * `SHA3-224`
>
>   * `SHA3-256`
>
>   * `SHA3-384`
>
>   * `SHA3-512`                                                                                          |
> | `SCRYPT`\[[1](#_footnotedef_1 "View footnote.")] | * `hashLength`
>
>   Byte-length of the generated hash, must be greater than or equal to 8. Default is `16`.
>
> * `saltLength`
>
>   Byte-length of the salt value. Default is `16`.
>
> * `n`
>
>   CPU/Memory cost. Must be greater than 1, a power of 2, and less than *2^(128 \* r / 8)*. Default is `32768`.
>
> * `p`
>
>   Parallelization. Must be a positive integer less than or equal to *Integer.MAX\_VALUE / (128 \* r \* 8)*. Default is `1`.
>
> * `r`
>
>   Block size. Must be greater than or equal to 1. Default is `8`. |
> | `SHA-256`                                        | - `saltLength`
>
>   Byte-length of the salt value. Default is `16`.	This is the default hashing.                                                                                                                                                                                                                                                                                                                                                                                                                    |
> | `SHA-384`                                        | * `saltLength`
>
>   Byte-length of the salt value. Default is `16`.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
> | `SHA-512`                                        | - `saltLength`
>
>   Byte-length of the salt value. Default is `16`.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
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
>     For Groovy, Map or JSON value (optional)
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
>   * Groovy (Map)
>
>     ```groovy
>     openidm.hash(\"dummy\", \"BCRYPT\", [\"cost\": 10]);
>     ```
>
>   * Groovy (JSON value)
>
>     ```groovy
>     JsonValue v = new JsonValue( [\"cost\": 10]); return openidm.hash(\"dummy\", \"BCRYPT\", v);
>     ```
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
> * Returns
>
>   Boolean, `true` if the hash of the string matches the hashed value, and `false` otherwise.
>
> * Throws
>
>   An exception is thrown if the string couldn't be hashed.
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
> |       |                                                                                                                                                                                                                    |
> | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
> | **1** | Learn more about available fields for the request object in [Create custom endpoints to launch scripts](script-custom-endpoints.html).                                                                             |
> | **2** | The `openidm.matches` function references the full `$crypto` object value instead of a hashed string, and its boolean result is stored in `SHA256HashedPassword` and returned in the `body` field of the response. |
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

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | These functions can also have a vanity binding to make them more descriptive, such as `consent.action()` instead of `openidm.action("consent" ...)`, by setting `resourceBindings` when you declare the script. In this case, the syntax for these functions would omit the resource name from the function parameters.Learn more in [Call a script from the IDM configuration](script-call.html) for more information about `resourceBindings`. |

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
>   An ASCII string representing the Base64-encoded version of `stringToEncode`.
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
> Decodes a Base64-encoded string. This is a global script binding that implements the canonical JavaScript `atob` function.
>
> * Parameters
>
>   * encodedString
>
>     string
>
>     The Base64-encoded string to be decoded.
>
> * Returns
>
>   An ASCII string representing the decoded version of `encodedString`.
>
> * Throws
>
>   An exception is typically thrown if the input `encodedString` is not a valid Base64 string.
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

## Log functions

IDM also provides a `logger` object to access the Simple Logging Facade for Java (SLF4J) facilities. The following code shows an example of the `logger` object.

```javascript
logger.info("Parameters passed in: {} {} {}", param1, param2, param3);
```

To set the log level for JavaScript scripts, add an appender with the `<filter class="ThresholdFilter">` tag to your project's `conf/logback.xml` file:

```xml
<filter class="ThresholdFilter">
    <level>DEBUG</level>
</filter>
```

Learn more about log levels in [log levels](../monitoring-guide/server-logs.html#log-levels).

In addition, JavaScript has a useful logging function named `console.log()`. This function provides an easy way to dump data to the IDM standard output (usually the same output as the OSGi console). The function works well with the JavaScript built-in function `JSON.stringify` and provides fine-grained details about any given object. For example, the following line will print a formatted JSON structure that represents the HTTP request details to STDOUT.

```javascript
console.log(JSON.stringify(context.http, null, 4));
```

|   |                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | These logging functions apply only to JavaScript scripts. To use the logging functions in Groovy scripts, the following lines must be added to the Groovy scripts:```groovy
import org.slf4j.*;
logger = LoggerFactory.getLogger('logger');
``` |

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
>   An exception is thrown if the message couldn't be logged.

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
>   An exception is thrown if the message couldn't be logged.

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
>   An exception is thrown if the message couldn't be logged.

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
>   An exception is thrown if the message couldn't be logged.

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
>   An exception is thrown if the message couldn't be logged.

***

[1](#_footnoteref_1). This hashing algorithm is not supported by [Bouncy Castle FIPS](../security-guide/security-bouncy-castle-fips.html)

---

---
title: The <code>augmentSecurityContext</code> trigger
description: Variables and bindings available to PingIDM augmentSecurityContext scripts, used to populate security context after authentication
component: pingidm
version: 8.1
page_id: pingidm:scripting-guide:script-variables-augment-security
canonical_url: https://docs.pingidentity.com/pingidm/8.1/scripting-guide/script-variables-augment-security.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scripting", "Triggers", "Authorization", "Mappings"]
---

# The `augmentSecurityContext` trigger

The `augmentSecurityContext` trigger, defined in the authentication configuration *(tooltip: You can manage the authentication configuration over REST at the config/authentication endpoint, or directly in the conf/authentication.json file.)*, can reference a script that is executed after successful authentication. Such scripts can populate the security context of the authenticated user. If the authenticated user is not found in the resource specified by `queryOnResource`, the `augmentSecurityContext` can provide the required authorization map.

Such scripts have access to the following bindings:

* `security` - includes the `authenticationId` and the `authorization` key, which includes the `moduleId`.

  The main purpose of an `augmentSecurityContext` script is to modify the `authorization` map that is part of this `security` binding. The authentication module determines the value of the `authenticationId`, and IDM attempts to populate the `authorization` map with the details that it finds, related to that `authenticationId` value. These details include the following:

  * `security.authorization.component` - the resource that contains the account (this will always will be the same as the value of `queryOnResource` by default).

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

---

---
title: The <code>identityServer</code> variable
description: The PingIDM identityServer script variable and its functions for retrieving properties, install location, project location, and working location
component: pingidm
version: 8.1
page_id: pingidm:scripting-guide:script-variables-identity-server
canonical_url: https://docs.pingidentity.com/pingidm/8.1/scripting-guide/script-variables-identity-server.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scripting", "Variables", "REST", "Endpoints", "Identities", "Configuration", "Files"]
---

# The `identityServer` variable

IDM provides an additional variable, named `identityServer`, to scripts. You can use this variable in several ways. The `ScriptRegistryService`, described in [Validate scripts over REST](script-endpoint.html), binds this variable to:

* `getProperty`

  Retrieves property information from system configuration files. Takes up to three parameters:

  * The name of the property you are requesting.

  * *(Optional)* The default result to return if the property wasn't set.

  * *(Optional)* Boolean to determine whether or not to use property substitution when getting the property.

    For more information about property substitution, refer to [Property value substitution](../setup-guide/using-property-substitution.html).

    Returns the first property found following the same order of precedence IDM uses to check for properties: environment variables, `system.properties`, `boot.properties`, and then other configuration files.

    For more information, refer to [Server configuration](../setup-guide/chap-configuration.html).

    For example, you can retrieve the value of the `openidm.config.crypto.alias` property with the following code: `alias = identityServer.getProperty("openidm.config.crypto.alias", "true", true);`

* `getInstallLocation`

  Retrieves the IDM installation path, such as `/path/to/openidm`. May be superseded by an absolute path.

* `getProjectLocation`

  Retrieves the directory used when you started IDM. That directory includes configuration and script files for your project.

  For more information on the project location, refer to [Startup configuration](../install-guide/startup-configuration.html).

* `getWorkingLocation`

  Retrieves the directory associated with database cache and audit logs. You can find `db/` and `audit/` subdirectories there.

  For more information on the working location, refer to [Startup configuration](../install-guide/startup-configuration.html).

---

---
title: Validate scripts over REST
description: "Validate and compile PingIDM scripts over REST using the script endpoint's eval and compile actions"
component: pingidm
version: 8.1
page_id: pingidm:scripting-guide:script-endpoint
canonical_url: https://docs.pingidentity.com/pingidm/8.1/scripting-guide/script-endpoint.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Scripting", "Validation", "REST"]
---

# Validate scripts over REST

IDM exposes a `script` endpoint over which scripts can be validated, by specifying the script parameters as part of the JSON payload. This functionality lets you test how a script will operate in your deployment, with complete control over the inputs and outputs. Testing scripts in this way can be useful in debugging.

In addition, the script registry service supports calls to other scripts. For example, you might have logic written in JavaScript, but also some code available in Groovy. Ordinarily, it would be challenging to interoperate between these two environments, but this script service lets you call one from the other on the IDM router.

The `script` endpoint supports two actions - `eval` and `compile`.

The `eval` action evaluates a script, by taking any actions referenced in the script, such as router calls to affect the state of an object. For JavaScript scripts, the last statement that is executed is the value produced by the script, and the expected result of the REST call.

The following REST call attempts to evaluate the `autoPurgeAuditRecon.js` script (provided in `openidm/bin/defaults/script/audit`), but provides an incorrect purge type (`"purgeByNumOfRecordsToKeep"` instead of `"purgeByNumOfReconsToKeep"`). The error is picked up in the evaluation. The example assumes that the script exists in the directory reserved for custom scripts (`openidm/script`):

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request POST \
--data '{
  "type": "text/javascript",
  "file": "script/autoPurgeAuditRecon.js",
  "globals": {
    "input": {
      "mappings": ["%"],
      "purgeType": "purgeByNumOfRecordsToKeep",
      "numOfRecons": 1
    }
  }
}' \
"http://localhost:8080/openidm/script?_action=eval"
"Must choose to either purge by expired or number of recons to keep"
```

|   |                                                                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The variables passed into this script are namespaced with the `globals` map. It is preferable to namespace variables passed into scripts in this way, to avoid collisions with the top-level reserved words for script maps, such as `file`, `source`, and `type`. |

The `compile` action compiles a script, but does not execute it. A successful compilation returns `true`. An unsuccessful compilation returns the reason for the failure.

The following REST call tests whether a transformation script will compile:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request POST \
--data '{
  "type":"text/javascript",
  "source":"source.mail ? source.mail.toLowerCase() : null"
}' \
"http://localhost:8080/openidm/script?_action=compile"
True
```

If the script is not valid, the action returns an indication of the error, for example:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request POST \
--data '{
  "type":"text/javascript",
  "source":"source.mail ? source.mail.toLowerCase()"
}' \
"http://localhost:8080/openidm/script?_action=compile"
{
  "code": 400,
  "reason": "Bad Request",
  "message": "missing : in conditional expression (386...BF2#1)in 386...BF2 at line number 1 at column number 39"
}
```