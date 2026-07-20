---
title: Access data objects by remote proxy
description: Proxy REST requests to a remote PingIDM instance to use it as a sync source or target, with basic or bearer token authentication
component: pingidm
version: 8.1
page_id: pingidm:objects-guide:data-rest-proxy
canonical_url: https://docs.pingidentity.com/pingidm/8.1/objects-guide/data-rest-proxy.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Synchronization"]
section_ids:
  determine-instancename-value: How to determine the value for instanceName
  using_the_filesystem: Using the filesystem
  using_rest: Using REST
  prerequisites: Prerequisites
  mapping: Mapping
  authentication: Authentication
  examples: Examples
  basic_authentication: Basic authentication
  beareroauth2_authentication: Bearer/Oauth2 authentication
  rest_request: REST request
  script: Script
---

# Access data objects by remote proxy

You can proxy REST requests to a remote IDM or Advanced Identity Cloud instance using the `openidm/external/idm/instanceName` endpoint.

|   |                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For more information on determining the exact value for `instanceName`, refer to [How to determine the value for `instanceName`](#determine-instancename-value). |

This functionality lets you treat any other IDM or Advanced Identity Cloud instance as a resource within the one you are managing. You can then use it in a sync mapping, call actions on it, use it within scripts, or use it in any other way that you might use a resource in IDM. You can call any endpoint in the remote IDM system using this proxy.

A few situations where this feature may be useful include:

* Situations where some, but not all, data needs to be migrated from an older version to a newer release.

* Situations where a development or testing environment has data that needs to be synced into the production environment.

* Situations where data is deployed in geographically diverse data centers and changes need to be kept in sync with one another.

* Situations where a new instance needs to sync data between existing on-premises and cloud instances.

This feature does not support liveSync/implicit sync from the remote IDM resources. This means that you will be limited to using recon when it comes to pulling data from a remote system.

|   |                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------ |
|   | If requests sent to the source server include an `X-Requested-With` header, the value of the header will be set to `RemoteIDMProxy`. |

## How to determine the value for `instanceName`

The `instanceName` is a fragment of the external configuration's name. You can determine the value for `instanceName` using REST or the filesystem:

### Using the filesystem

1. Go to `/path/to/openidm/conf/`.

2. Locate the file named `external.idm-instanceName.json`.

   For example, a file named `external.idm-name1.json` would be available as a remote system at the `openidm/external/idm/name1` endpoint.

### Using REST

1. Get the configurations:

   Request

   ```none
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request GET \
   "https://localhost:8443/openidm/config/"
   ```

2. Locate the external configuration:

   Return

   ```json
   {
     "_id": "",
     "configurations": [
       ...
       {
         "_id": "emailTemplate/welcome",
         "pid": "emailTemplate.212e...f7a",
         "factoryPid": "emailTemplate"
       },
       ...
       {
         "_id": "external.idm/name1", (1)
         "pid": "external.idm.29cd...f4a",
         "factoryPid": "external.idm"
       },
       ...
     ]
   }
   ```

   |       |                                                                                                                                                               |
   | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **1** | In this example, the external configuration `"_id": "external.idm/name1"` would be available as a remote system at the `openidm/external/idm/name1` endpoint. |

## Prerequisites

To connect to a remote instance over SSL, you must import the remote instance's server certificate into your local instance's truststore. For example:

```
keytool \
-import \
-alias fr-platform \
-keystore security/truststore \
-file ~/fr-platform.pem
```

## Mapping

To use the remote IDM proxy in a [synchronization mapping](../synchronization-guide/mappings.html), add the following to your `sync.json` file or individual mapping file (updating the values as necessary):

```json
{
  "name" : "onprem_user_to_fidc_alpha_user",
  "source" : "external/idm/65/managed/user",
  "target" : "external/idm/fidc/managed/alpha_user"
}
```

## Authentication

[Authentication](../auth-guide/authentication.html) against the remote IDM instance is supported via `basic` authentication, or `bearer` token authentication when IDM is configured to use rsFilter. The authentication strategy determines some of the parameters required for the request.

| Property       | Required?          | Definition                                                                 |
| -------------- | ------------------ | -------------------------------------------------------------------------- |
| enabled        | No                 | The enable state of the service. Default is `true`.                        |
| scope          | No                 | The requested OAuth2 scope(s).                                             |
| scopeDelimiter | No                 | The scope delimiter to use. Defaults to space.                             |
| authtype       | Yes                | The authentication strategy to use. Either `basic` or `bearer`.            |
| instanceUrl    | Yes                | The URL of the remote instance to relay the request to.                    |
| userName       | With `basic` auth  | The basic authentication user name.                                        |
| password       | With `basic` auth  | The basic authentication password.                                         |
| clientId       | With `bearer` auth | The clientId used to request an access token from the token endpoint.      |
| clientSecret   | With `bearer` auth | The client secret used to request an access token from the token endpoint. |
| tokenEndpoint  | With `bearer` auth | The OAuth2 token endpoint.                                                 |

## Examples

### Basic authentication

```json
{
  "enabled" : true,
  "authType" : "basic",
  "instanceUrl" : "https://localhost:8443/openidm/",
  "userName" : "openidm-admin",
  "password" : "openidm-admin"
}
```

### Bearer/Oauth2 authentication

```json
{
  "enabled" : true,
  "authType" : "bearer",
  "instanceUrl" : "https://fr-platform.iam.example.com/openidm/",
  "clientId" : "idm-provisioning",
  "clientSecret" : "password",
  "scope" : [ ],
  "tokenEndpoint" : "https://fr-platform.iam.example.com/am/oauth2/realms/root/access_token",
  "scopeDelimiter" : " "
}
```

### REST request

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--insecure \
--header "Accept-API-Version: resource=1.0" \
--request GET \
'https://localhost:8443/openidm/external/idm/platform/managed/user?_queryFilter=true'
```

Return

```json
{
  "result": [
    {
      "_id": "95b2b43c-621e-4bca-8a97-efc768f17751",
      "_rev": "00000000f20217df",
      "userName": "testUser",
      "accountStatus": "active",
      "givenName": "Test",
      "sn": "User",
      "mail": "testUser@test.com"
    }
  ],
  "resultCount": 1,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": -1
}
```

### Script

```javascript
openidm.query("external/idm/fidc/managed/alpha_user", {"_queryFilter": "userName eq 'bjensen'"});
```

---

---
title: Access data objects using scripts
description: Access and manipulate PingIDM managed, system, configuration, and repository objects using the Resource API in scripts
component: pingidm
version: 8.1
page_id: pingidm:objects-guide:data-scripts
canonical_url: https://docs.pingidentity.com/pingidm/8.1/objects-guide/data-scripts.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Scripts"]
---

# Access data objects using scripts

IDM's uniform programming model means that all objects are queried and manipulated in the same way, using the Resource API. The URL or URI that is used to identify the target object for an operation depends on the [object type](appendix-objects.html). For more information about scripts and the objects available to scripts, refer to [Scripting](../scripting-guide/preface.html).

You can use the Resource API to obtain managed, system, configuration, and repository objects, as follows:

```javascript
val = openidm.read("managed/organization/mysampleorg")
val = openidm.read("system/mysystem/account")
val = openidm.read("config/custom/mylookuptable")
val = openidm.read("repo/custom/mylookuptable")
```

For information about constructing an object ID, refer to [URI Scheme](../rest-api-reference/rest-structure.html#rest-uri-scheme).

You can update entire objects with the `update()` function, as follows:

```javascript
openidm.update("managed/organization/mysampleorg", rev, object)
openidm.update("system/mysystem/account", rev, object)
```

You can apply a partial update to a managed or system object by using the `patch()` function:

```javascript
openidm.patch("managed/organization/mysampleorg", rev, value)
```

The `create()`, `delete()`, and `query()` functions work the same way.

---

---
title: Access data objects using the REST API
description: Access PingIDM managed, system, and configuration objects over REST using common HTTP methods and the Common REST API
component: pingidm
version: 8.1
page_id: pingidm:objects-guide:data-rest
canonical_url: https://docs.pingidentity.com/pingidm/8.1/objects-guide/data-rest.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "REST API"]
---

# Access data objects using the REST API

IDM provides RESTful access to data objects through the Common REST API. To access objects over REST, you can use a browser-based REST client, such as the *Simple REST Client* for Chrome, or *RESTClient* for Firefox. Alternatively, you can use the [curl](https://curl.se/) command-line utility.

For a comprehensive overview of the REST API, refer to the [REST API reference](../rest-api-reference/preface.html).

To obtain a managed object through the REST API, depending on your security settings and authentication configuration, perform an HTTP GET on the corresponding URL, for example `http://localhost:8080/openidm/managed/organization/mysampleorg`.

By default, the HTTP GET returns a JSON representation of the object.

In general, you can map any HTTP request to the corresponding `openidm.method` call. The following example shows how the parameters provided in an `openidm.query` request correspond with the key-value pairs that you would include in a similar HTTP GET request:

Reading an object using the Resource API:

```javascript
openidm.query("managed/user", { "_queryFilter": "true" }, ["userName","sn"])
```

Reading an object using the REST API:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"http://localhost:8080/openidm/managed/user?_queryFilter=true&_fields=userName,sn"
```

---

---
title: Audit objects
description: Reference for PingIDM audit objects, which contain audit data selected for local storage in the repository
component: pingidm
version: 8.1
page_id: pingidm:objects-guide:appendix-audit-objects
canonical_url: https://docs.pingidentity.com/pingidm/8.1/objects-guide/appendix-audit-objects.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model"]
---

# Audit objects

[Audit objects](../audit-guide/audit.html) contain audit data selected for local storage in repository.

---

---
title: Configuration objects
description: Configure and access PingIDM custom configuration objects, including naming conventions, file mappings, and REST and scripting access
component: pingidm
version: 8.1
page_id: pingidm:objects-guide:appendix-config-objects
canonical_url: https://docs.pingidentity.com/pingidm/8.1/objects-guide/appendix-config-objects.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Scripts", "Setup &amp; Configuration"]
section_ids:
  configuration-objects-when-to-use: When To use custom configuration objects
  configuration-objects-naming: Custom configuration object naming conventions
  configuration-objects-file-mapping: Mapping configuration objects To configuration files
  configuration-objects-formats: Configuration objects file and REST payload formats
  configuration-objects-access-rest: Accessing configuration objects through the REST API
  configuration-objects-access-programmatic: Accessing configuration objects programmatically
  configuration-objects-programmatic-create: Creating objects
  configuration-objects-programmatic-update: Updating objects
  configuration-objects-programmatic-delete: Deleting objects
  configuration-objects-programmatic-read: Reading objects
---

# Configuration objects

IDM provides an extensible configuration to allow you to leverage regular configuration mechanisms.

Unlike native the IDM configuration, which is interpreted automatically and can start new services, IDM stores custom configuration objects and makes them available to your code through the API.

For an introduction to the standard configuration objects, refer to [Server configuration](../setup-guide/chap-configuration.html).

## When To use custom configuration objects

Configuration objects are ideal for metadata and settings that need not be included in the data to reconcile. Use configuration objects for data that does not require audit logs, and does not serve directly as a target or source for mappings.

Although you can set and manipulate configuration objects programmatically and manually, configuration objects are expected to change slowly, through both manual file updates and programmatic updates. To store temporary values that can change frequently and that you do not expect to be updated by configuration file changes, custom repository objects might be more appropriate.

## Custom configuration object naming conventions

By convention custom configuration objects are added under the reserved context, `config/custom`.

You can choose any name under `config/context`. Be sure, however, to choose a value for context that does not clash with future IDM configuration names.

## Mapping configuration objects To configuration files

If you have not disabled the file-based view for configuration, you can view and edit all configuration including custom configuration in `openidm/conf/*.json` files. The configuration maps to a file named `context-config-name.json`, where context for custom configuration objects is `custom` by convention, and config-name is the configuration object name. A configuration object named `escalation` thus maps to a file named `conf/custom-escalation.json`.

IDM detects and automatically picks up changes to the file.

IDM also applies changes made through APIs to the file.

By default, IDM stores configuration objects in the repository. The file view is an added convenience aimed to help you in the development phase of your project.

## Configuration objects file and REST payload formats

By default, IDM maps configuration objects to JSON representations.

IDM represents objects internally in plain, native types like maps, lists, strings, numbers, booleans, null. The object model is restricted to simple types so that mapping objects to external representations is easy.

The following example shows a representation of a configuration object with a look-up map.

```json
{
    "CODE123" : "ALERT",
    "CODE889" : "IGNORE"
}
```

In the JSON representation, maps are represented with braces (`{ }`), and lists are represented with brackets (`[ ]`). Objects can be arbitrarily complex, as in the following example.

```json
{
    "CODE123" : {
        "email" : ["sample@sample.com", "john.doe@somedomain.com"],
        "sms" : ["555666777"]
    }
    "CODE889" : "IGNORE"
}
```

## Accessing configuration objects through the REST API

You can list all available configuration objects, including system and custom configurations, using an HTTP GET on `/openidm/config`.

The `_id` property in the configuration object provides the link to the configuration details with an HTTP GET on `/openidm/config/id-value`. By convention, the id-value for a custom configuration object called `escalation` is `custom/escalation`.

IDM supports REST mappings for create, read, update, delete, patch, and query of configuration objects.

## Accessing configuration objects programmatically

You can address configuration objects as resources using the URL or URI `config/` prefix both internally and also through the REST interface. The resource API provides script object functions for create, read, update, query, and delete operations.

IDM supports concurrency through a multi version concurrency control mechanism. Each time an object changes, IDM assigns it a new revision.

Objects can be arbitrarily complex as long as they use supported types, such as maps, lists, numbers, strings, and booleans.

## Creating objects

The following script example creates an object type.

```javascript
openidm.create("config/custom", "myconfig", mymap)
```

## Updating objects

The following script example updates a custom configuration object type.

```javascript
openidm.update("config/custom/myconfig", mymap)
```

## Deleting objects

The following script example deletes a custom configuration object type.

```javascript
openidm.delete("config/custom/myconfig")
```

## Reading objects

The following script example reads an object type.

```javascript
val = openidm.read("config/custom/myconfig")
```

---

---
title: Configure relationship change notification
description: Configure PingIDM relationship change notification using notify, notifySelf, and notifyRelationships to propagate changes between managed objects
component: pingidm
version: 8.1
page_id: pingidm:objects-guide:relationships-notification
canonical_url: https://docs.pingidentity.com/pingidm/8.1/objects-guide/relationships-notification.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Relationships", "Roles", "Change Notification"]
---

# Configure relationship change notification

A relationship exists between two managed objects. By default, when a relationship changes (when it is created, updated, or deleted), the managed objects on either side of the relationship are not *notified* of that change. This means that the *state* of each object with respect to that relationship field is not recalculated until the object is read. This default behavior improves performance, especially in the case where many objects are affected by a single relationship change.

For `roles`, a special kind of relationship, change notification *is* configured by default. The purpose of this default configuration is to notify managed users when any of the relationships that link users, roles, and assignments are manipulated. Learn more about relationship change notification in managed roles in [Roles and relationship change notification](roles-change-notification.html).

To change the default configuration, or to set up notification for other relationship changes, use the `notify*` properties in the relationship definition, as described in this section.

A relationship exists between an *origin* object and a *referenced* object. These terms reflect which managed object is specified in the URL (for example, `managed/user/psmith`) and which object is referenced by the relationship (`_ref*`) properties. Learn more about relationship properties in [relationship properties](relationships.html#relationship-properties).

In the previous example, a PUT on `managed/user/psmith` with `"manager" : {_ref : "managed/user/bjensen"}`, causes `managed/user/psmith` to be the origin object, and `managed/user/bjensen` to be the referenced object for that relationship, as shown in the following illustration:

![Illustration shows the origin and referenced objects in a relationship](_images/relationship-objects.svg)Figure 1. Relationship Objects

Note that for the reverse relationship (a PUT on `managed/user/bjensen` with `"reports" : [{_ref = "managed/user/psmith"}]`) `managed/user/bjensen` would be the origin object, and `managed/user/psmith` would be the referenced object.

By default, when a relationship changes, neither the origin object nor the referenced object is *notified* of the change. So, with the PUT on `managed/user/psmith` with `"manager" : {_ref : "managed/user/bjensen"}`, neither psmith's object nor bjensen's object is notified.

|   |                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Auditing is not tied to relationship change notification and is always triggered when a *relationship* changes. Therefore, relationship changes are audited, regardless of the `notify` and `notifySelf` properties. |

To configure relationship change notification, set the `notify` and `notifySelf` properties in your managed object schema. These properties specify whether objects that reference relationships are notified of a relationship change:

* `notifySelf`

  Notifies the origin object of the relationship change.

  In our example, if the `manager` definition includes `"notifySelf" : true`, and if the relationship is changed through a URL that references psmith, then psmith's object would be notified of the change. For example, for a CREATE, UPDATE or DELETE request on the `psmith/manager`, psmith would be notified, but the managed object referenced by this relationship (bjensen) would not be notified.

  If the relationship were manipulated through a request to `bjensen/reports`, then bjensen would only be notified if the `reports` relationship specified `"notifySelf" : true`.

* `notify`

  Notifies the referenced object of the relationship change. Set this property on the `resourceCollection` of the relationship property.

  In our example, assume that the `manager` definition has a `resourceCollection` with a `path` of `managed/user`, and that this object specifies `"notify" : true`. If the relationship changes through a CREATE, UPDATE, or DELETE on the URL `psmith/manager`, then the reference object (`managed/user/bjensen`) would be notified of the change to the relationship.

* `notifyRelationships`

  This property controls the propagation of notifications out of a managed object when one of its properties changes through an update or patch, or when that object receives a notification through one of these fields.

  The `notifyRelationships` property takes an array of relationships as a value; for example, `"notifyRelationships" : ["relationship1", "relationship2"]`. The relationships specified here are fields defined on the managed object type (which might itself be a relationship).

  Notifications are propagated according to the *recipient's*`notifyRelationships` configuration. If a managed object type is notified of a change through one if its relationship fields, the notification is done according to the configuration of the recipient object. To illustrate, look at the `attributes` property in the default `managed/assignment` object:

  ```json
  {
      "name" : "assignment",
      "schema" : {
          ...
          "properties" : {
              ...
              "attributes" : {
                  "description" : "The attributes operated on by this assignment.",
                  "title" : "Assignment Attributes",
                  ...
                  "notifyRelationships" : ["roles"]
              },
  ...
  ```

  This configuration means that if an assignment is updated or patched, and the assignment's `attributes` change in some way, all the `roles` connected to that assignment are notified. Because the `role` managed object has `"notifyRelationships" : ["members"]` defined on its `assignments` field, the notification that originated from the change to the assignment attribute is propagated to the connected `roles`, and then out to the `members` of those roles.

  So, the `role` is notified through its `assignments` field because an `attribute` in the assignment changed. This notification is propagated out of the `members` field because the role definition has `"notifyRelationships" : ["members"]` on its `assignments` field.

By default, `roles`, `assignments`, and `members` use relationship change notification to ensure that relationship changes are accurately provisioned.

For example, the default `user` object includes a `roles` property with `notifySelf` set to `true`:

```json
{
   "name" : "user",
   ...
   "schema" : {
       ...
       "properties" : {
           ...
           "roles" : {
               "description" : "Provisioning Roles",
               ...
               "items" : {
                   "type" : "relationship",
                   ...
                   "reverseRelationship" : true,
                   "reversePropertyName" : "members",
                   "notifySelf" : true,
                   ...
               }
...
```

In this case, `notifySelf` indicates the origin or `user` object. If any changes are made to a relationship referencing a role through a URL that includes a user, the user will be notified of the change. For example, if there is a CREATE on `managed/user/psmith/roles` which specifies a set of references to existing roles, user `psmith` will be notified of the change.

Similarly, the `role` object includes a `members` property. That property includes the following schema definition:

```json
{
    "name" : "role",
    ...
    "schema" : {
        ...
        "properties" : {
            ...
            "members" : {
                ...
                "items" : {
                    "type" : "relationship",
                    ...
                    "properties" : {
                        ...
                        "resourceCollection" : [
                            {
                                "notify" : true,
                                "path" : "managed/user",
                                "label" : "User",
                                ...
                            }
                        ]
                    }
...
```

Notice the `"notify" : true` setting on the `resourceCollection`. This setting indicates that if the relationship is created, updated, or deleted through a URL that references that role, all objects in that resource collection (in this case, `managed/user` objects) that are identified as `members` of that role must be notified of the change.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * To notify an object at the end of a relationship that the relationship has changed (using the `notify` property), the relationship *must* be [bidirectional](reverse-relationships.html) (`"reverseRelationship" : true`).

  When an object is notified of a relationship state change (create, delete, or update), part of that notification process involves calculating the changed object state with respect to the changed relationship field. For example, if a managed user is notified that a role has been created, the user object calculates its base state, and the state of its `roles` field, before and after the new role was created. This *before* and *after* state is then reconciled. An object that is referenced by a forward (unidirectional) relationship does not have a field that references that relationship; the object is "pointed-to", but does not "point-back". Because this object cannot calculate its *before* and *after* state with respect to the relationship field, it cannot be notified.

  Similarly, relationships that are notified of changes to the objects that reference them *must* be bidirectional relationships.

  If you configure relationship change notification on a unidirectional relationship, IDM throws an exception. |

---

---
title: Configuring relationships
description: Configure PingIDM relationships between managed objects, and retrieve, create, update, and delete relationships over the REST interface
component: pingidm
version: 8.1
page_id: pingidm:objects-guide:relationships
canonical_url: https://docs.pingidentity.com/pingidm/8.1/objects-guide/relationships.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Relationships", "Roles", "Organizations"]
page_aliases: ["relationships-between-objects.adoc", "view-relationships-over-rest.adoc"]
section_ids:
  example-relationship: "Example relationship: manager"
  retrieve-relationship-data: Retrieve relationship data
  relationship-endpoint-query: Query a relationship endpoint
  relationship-endpoint-read: Read relationship fields
  create-relationship: Create a relationship
  establishing-relationships-between-objects: Creating a relationship as part of a created object
  update-relationship: Update a relationship
  delete-relationship: Delete a relationship
  relationship-properties: Relationship properties
  ref-property: Relationship reference properties
---

# Configuring relationships

Relationships are references between managed objects. They are defined in your managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint, or directly in the conf/managed.json file.)* file. You can interact with relationships over REST using the relationship's endpoint, `openidm/managed/user/userName/relationshipName?_queryFilter=true`.

Learn more about relationships in:

* [Example relationship: manager](#example-relationship)

* [Relationship properties](#relationship-properties)

Learn more about interacting with relationships over `REST` in:

* [Retrieve relationship data](#retrieve-relationship-data)

* [Create a relationship](#create-relationship)

* [Update a relationship](#update-relationship)

* [Delete a relationship](#delete-relationship)

When modeling relationships, be aware of [bidirectional relationships](reverse-relationships.html) and model them properly in your schema.

[Roles](roles.html) and [Organizations](organizations.html) are implemented using relationships, but you can create relationships between any managed object type.

You can also:

* [Manage relationships using the admin UI](ui-relationships.html).

* Configure IDM to [validate relationships](relationships-validation.html) when they're created.

* Create [custom relationship properties](relationships-custom.html).

* Create [custom relationships](relationships-custom.html).

* Update [relationship-derived vritual properties](managed-object-virtual-properties.html#relationship-derived-virtual-properties) by configuring [relationship change notifications](relationships-notification.html).

* Require the system to [validate relationships](relationships-validation.html) when they're created.

IDM maintains referential integrity by deleting the relationship reference if the object referred to by that relationship is deleted.

## Example relationship: manager

The default configuration includes a relationship named `manager` that lets you configure a relationship between two managed users. This relationship is a good example for understanding how relationships work.

The default `manager` relationship is configured as follows:

```json
"manager" : {
    "type" : "relationship",
    "validate" : true,
    "reverseRelationship" : true,
    "reversePropertyName" : "reports",
    "description" : "Manager",
    "title" : "Manager",
    "viewable" : true,
    "searchable" : false,
    "usageDescription" : "",
    "isPersonal" : false,
    "properties" : {
        "_ref" : {
            "description" : "References a relationship from a managed object",
            "type" : "string"
        },
        "_refProperties" : {
            "description" : "Supports metadata within the relationship",
            "type" : "object",
            "title" : "Manager _refProperties",
            "properties" : {
                "_id" : {
                    "description" : "_refProperties object ID",
                    "type" : "string"
                }
            }
        }
    },
    "resourceCollection" : [
        {
            "path" : "managed/user",
            "label" : "User",
            "query" : {
                "queryFilter" : "true",
                "fields" : [
                    "userName",
                    "givenName",
                    "sn"
                ]
            }
        }
    ],
    "userEditable" : false
},
```

## Retrieve relationship data

There are two ways to retrieve data about a relationship over REST, [querying the relationship endpoint](#relationship-endpoint-query) or [reading relationship fields](#relationship-endpoint-read).

Querying the relationship endpoint supports filtering and paginating the results. It's the safest and most efficient way of retrieving data.

Reading relationship fields does not support filtering or paginating results. To prevent problems that could result from requesting a large amount of data, use this method only in situations where you are certain there are few results.

### Query a relationship endpoint

You can retrieve a managed object's relationship data by querying the relationship endpoint. The endpoint's name is the name of the relationship field.

A relationship endpoint query can use the `_queryFilter` and `_pageSize` parameters to filter and paginate large numbers of results. To avoid the risk of a large query overwhelming your system, use this method whenever possible.

The `_queryFilter` parameter can filter by any fields which are indexed attributes of the related object.

The following example demonstrates querying managed user `bjensen` for all `reports`:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"http://localhost:8080/openidm/managed/user/bjensen/reports?_queryFilter=true"
{
  "result": [
    {
      "_id": "78483e83-9577-40cd-a1d4-6ea0a896e916-4311",
      "_rev": "78483e83-9577-40cd-a1d4-6ea0a896e916-4312",
      "_ref": "managed/user/psmith",
      "_refResourceCollection": "managed/user",
      "_refResourceId": "psmith",
      "_refProperties": {
        "_id": "78483e83-9577-40cd-a1d4-6ea0a896e916-4311",
        "_rev": "78483e83-9577-40cd-a1d4-6ea0a896e916-4312"
      }
    },
    {
      "_id": "78483e83-9577-40cd-a1d4-6ea0a896e916-4934",
      "_rev": "78483e83-9577-40cd-a1d4-6ea0a896e916-4935",
      "_ref": "managed/user/scarter",
      "_refResourceCollection": "managed/user",
      "_refResourceId": "scarter",
      "_refProperties": {
        "_id": "78483e83-9577-40cd-a1d4-6ea0a896e916-4934",
        "_rev": "78483e83-9577-40cd-a1d4-6ea0a896e916-4935"
      }
    }
  ],
  "resultCount": 2,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": -1
}
```

The following example demonstrates querying managed user `bjensen` for all `reports` where the `sn` is Smith:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"http://localhost:8080/openidm/managed/user/bjensen/reports?_queryFilter=sn+eq+'Smith'&_pageSize=1"
{
  "result": [
    {
      "_id": "78483e83-9577-40cd-a1d4-6ea0a896e916-4311",
      "_rev": "78483e83-9577-40cd-a1d4-6ea0a896e916-4312",
      "_ref": "managed/user/psmith",
      "_refResourceCollection": "managed/user",
      "_refResourceId": "psmith",
      "_refProperties": {
        "_id": "78483e83-9577-40cd-a1d4-6ea0a896e916-4311",
        "_rev": "78483e83-9577-40cd-a1d4-6ea0a896e916-4312"
      }
    }
  ],
  "resultCount": 1,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": -1
}
```

You can also pass the `_fields` query parameter to include them in the response, demonstrated here with `userName` and `phoneNumber`:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \ \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"http://localhost:8080/openidm/managed/user/bjensen/reports?_queryFilter=sn+eq+'Smith'&_fields=userName,phoneNumber&_pageSize=1"
{
  "result" : [ {
    "_id" : "78483e83-9577-40cd-a1d4-6ea0a896e916-45700",
    "_rev" : "78483e83-9577-40cd-a1d4-6ea0a896e916-45701",
    "_ref" : "managed/user/psmith",
    "_refResourceCollection" : "managed/user",
    "_refResourceId" : "psmith",
    "_refResourceRev" : "d776f795-512f-4c09-a673-1f081a8ef3ef-4955",
    "_refProperties" : {
      "_id" : "78483e83-9577-40cd-a1d4-6ea0a896e916-45700",
      "_rev" : "78483e83-9577-40cd-a1d4-6ea0a896e916-45701"
    },
    "userName" : "psmith",
    "phoneNumber" : "0831245986"
  } ],
  "resultCount" : 1,
  "pagedResultsCookie" : null,
  "totalPagedResultsPolicy" : "NONE",
  "totalPagedResults" : -1,
  "remainingPagedResults" : -1
}
```

When you query an endpoint which is a collection, you must use the `_queryFilter` parameter, or you'll receive an error with an `HTTP 400` error code. If you don't want to filter the results, pass `_queryFilter=true`.

Learn more about `_queryFilter` in [Query](../crest/crest-query.html) and [Constructing queries](queries.html#constructing-queries).

### Read relationship fields

To read relationship fields, query a managed object and pass the `_fields` parameter to request associated data fields.

|   |                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Do not use `_fields` to request a field that is a relationship with more than a few members, as this data cannot be filtered or paginated. |

The following example reads a singleton relationship (manager) associated with a managed user (psmith):

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"http://localhost:8080/openidm/managed/user/psmith?_fields=manager"
{
  "_id": "0cb7c704-77ab-4211-9f13-04e45847f5e9-17222",
  "_rev": "0cb7c704-77ab-4211-9f13-04e45847f5e9-17223",
  "_ref": "managed/user/bjensen",
  "_refResourceCollection": "managed/user",
  "_refResourceId": "bjensen",
  "_refProperties": {
    "_id": "0cb7c704-77ab-4211-9f13-04e45847f5e9-17222",
    "_rev": "0cb7c704-77ab-4211-9f13-04e45847f5e9-17223"
  }
}
```

When you're reading relationship fields, you can use the managed object endpoint directly using the following syntax:

* `relatedObject/property` (for a simple string value)

* `relatedObject/*/property` (for an array of values)

This example demonstrates retrieving the `mail` and `phoneNumber` properties from psmith's manager using this method:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"http://localhost:8080/openidm/managed/user/psmith?_fields=manager/mail,manager/phoneNumber"
{
  "_id": "psmith",
  "_rev": "0000000014c0b68d",
  "manager": {
    "_rev": "000000005bac8c10",
    "_id": "bjensen",
    "phoneNumber": "12345678",
    "mail": "bjensen@example.com",
    "_ref": "managed/user/bjensen",
    "_refResourceCollection": "managed/user",
    "_refResourceId": "bjensen",
    "_refProperties": {
      "_id": "42418f09-ad6c-4b77-bf80-2a12d0c44678",
      "_rev": "00000000288b921e"
    }
  }
}
```

## Create a relationship

To create a relationship between two managed objects, send a POST request to the relationship's endpoint with a `_ref` parameter containing the path to the other side of the relationship.

For example, suppose the user `psmith` has the user `bjensen` as a manager. The following call creates the `manager` relationship between them:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request POST \
--data '{
  "_ref" : "managed/user/bjensen"
}' \
"http://localhost:8080/openidm/managed/user/psmith/manager"
{
  "_id": "0cb7c704-77ab-4211-9f13-04e45847f5e9-82148",
  "_rev": "0cb7c704-77ab-4211-9f13-04e45847f5e9-82149",
  "_ref": "managed/user/bjensen",
  "_refResourceCollection": "managed/user",
  "_refResourceId": "bjensen",
  "_refProperties": {
    "_id": "0cb7c704-77ab-4211-9f13-04e45847f5e9-82148",
    "_rev": "0cb7c704-77ab-4211-9f13-04e45847f5e9-82149"
  }
}
```

To learn more about the `_ref` parameter or the relationship reference properties in general, refer to [Relationship properties](#relationship-properties).

### Creating a relationship as part of a created object

In addition to creating a relationship between two existing managed objects, you can create a relationship at the same time as you create a managed object. For example, imagine that you are creating a new user, psmith, and that psmith's manager will be bjensen. You would create psmith's user entry, and *reference* bjensen's entry with the `_ref` property, as follows:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "If-None-Match: *" \
--header "Content-Type: application/json" \
--request PUT \
"http://localhost:8080/openidm/managed/user/psmith" \
--data '{
    "_id": "psmith",
    "_rev": "00000000ec41097c",
    "sn": "Smith",
    "userName": "psmith",
    "givenName": "Patricia",
    "displayName": "Patti Smith",
    "description": "psmith - new user",
    "mail": "psmith@example.com",
    "phoneNumber": "0831245986",
    "manager": {
      "_ref": "managed/user/bjensen"
    }
  }'
```

|   |                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Relationship information is not returned by default. To show the relationship in psmith's entry, you must explicitly request her manager entry, as follows: |

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"http://localhost:8080/openidm/managed/user/psmith?_fields=manager"
{
  "_id": "psmith",
  "_rev": "00000000ec41097c",
  "manager": {
    "_ref": "managed/user/bjensen",
    "_refResourceCollection": "managed/user",
    "_refResourceId": "bjensen",
    "_refProperties": {
      "_id": "ffc6f0f3-93db-4939-b9eb-1f8389a59a52",
      "_rev": "0000000081aa991a"
    }
  }
}
```

To learn more about the `_ref` parameter or the relationship reference properties in general, refer to [Relationship properties](#relationship-properties).

## Update a relationship

You can update a managed object's relationship data by making a PUT request to its endpoint. The endpoint's name is the name of the relationship field.

When you update a relationship, the related objects automatically update to reflect the new state. In the following example, scarter's `reports` entry is automatically updated when the change to psmith's `manager` entry is updated.

The following example updates psmith's manager to scarter:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \ \
--header "Accept-API-Version: resource=1.0" \
--header "If-Match: *" \
--header "Content-Type: application/json" \
--request PUT \
--data '{
  "_ref":"managed/user/scarter"
}' \
"http://localhost:8080/openidm/managed/user/psmith/manager"
{
  "_id": "0cb7c704-77ab-4211-9f13-04e45847f5e9-82148",
  "_rev": "0cb7c704-77ab-4211-9f13-04e45847f5e9-108753",
  "_ref": "managed/user/scarter",
  "_refResourceCollection": "managed/user",
  "_refResourceId": "scarter",
  "_refProperties": {
    "_id": "0cb7c704-77ab-4211-9f13-04e45847f5e9-82148",
    "_rev": "0cb7c704-77ab-4211-9f13-04e45847f5e9-108753"
  }
}
```

## Delete a relationship

You can delete a relationship by sending a DELETE request to its endpoint.

The following example deletes psmith's manager:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \\
--header "Accept-API-Version: resource=1.0" \
--request DELETE \
"http://localhost:8080/openidm/managed/user/psmith/manager"
```

## Relationship properties

Relationships have the following specific configurable properties:

|   |                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------- |
|   | Most of these properties apply to any [managed object type](creating-modifying-managed-objects.html). |

* `type` (string)

  The object type. Must be `relationship` for a relationship object.

* `returnByDefault` (boolean `true, false`)

  Specifies whether the relationship should be returned as part of the response. The `returnByDefault` property is not specific to relationships. This flag applies to all managed object types. However, relationship properties are not returned by default, unless explicitly requested.

* `reverseRelationship` (boolean `true, false`)

  Specifies whether this is a [bidirectional relationship](reverse-relationships.html).

* `reversePropertyName` (string)

  The corresponding property name, in the case of a [bidirectional relationship](reverse-relationships.html). For example, the `manager` property has a `reversePropertyName` of `reports`.

* `resourceCollection` (JSON object)

  The collection of resources (objects) on which this relationship is based (for example, `managed/user` objects).

### Relationship reference properties

When you have defined a relationship, you can use the relationship properties to *reference* one managed user from another. These properties make up a relationship reference:

* `_ref` (JSON object)

  Specifies how the relationship between two managed objects is referenced.

  The value of the `_ref` property is a derived path that is a combination of `_refResourceCollection` and a URL-encoded `_refResourceId`.

* `_refResourceCollection`

  Specifies the container of the referenced object (for example, `managed/user`).

* `_refResourceId`

  Specifies the ID of the referenced object. This is generally a system-generated UUID, such as `9dce06d4-2fc1-4830-a92b-bd35c2f6bcbb`. For clarity, this documentation uses client-assigned IDs such as `bjensen` and `psmith`.

* `_refProperties` (JSON object)

  Any required properties from the relationship that should be included in the managed object. The `_refProperties` field includes a unique ID (`_id`) and the revision (`_rev`) of the object. `_refProperties` can also contain arbitrary fields to support metadata within the relationship.

---

---
title: Create and modify object types
description: Create and modify PingIDM managed object types using the admin UI or configuration file, including property definitions, default values, and enum fields
component: pingidm
version: 8.1
page_id: pingidm:objects-guide:creating-modifying-managed-objects
canonical_url: https://docs.pingidentity.com/pingidm/8.1/objects-guide/creating-modifying-managed-objects.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Schema"]
section_ids:
  managed-objects-property-def-fields: Typical managed object property definition fields
  create_an_object_using_the_admin_ui: Create an object using the admin UI
  default-values-managed-obj: Default values
---

# Create and modify object types

If the managed object types provided in the default configuration don't meet your needs, you can create or modify them.

Every managed object type has a `name` and a `schema` that describes the properties associated with that object. The `name` can only include the characters `a-z`, `A-Z`, `0-9`, and `_` (underscore). You can add any arbitrary properties to the schema.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * Avoid using the dash character (`-`) in property names (for example, `last-name`) because dashes in names make JavaScript syntax more complex. Instead, use camel case (for example, `lastName`). If you can't avoid dash characters, write `source['last-name']` instead of `source.last-name` in your JavaScript.

* Managed object properties that contain an underscore (`_`) are reserved for internal use. Don't create new properties that contain underscores or include these properties in update requests. |

## Typical managed object property definition fields

* `title`

  The name of the property, in human-readable language, used to display the property in the UI.

* `description`

  A brief description of the property.

* `viewable`

  Specifies whether this property is viewable in the object's profile in the UI. Boolean, `true` or `false` (`true` by default).

* `searchable`

  Specifies whether this property can be searched in the UI. A searchable property is visible within the Managed Object data grid in the end-user UI.

  For a property to be searchable in the UI, it *must be indexed* in the repository configuration. For information on indexing properties in a repository, refer to [Object mappings](explicit-generic-mapping.html).

  Boolean, `true` or `false` (`false` by default).

  |   |                                                                                                                           |
  | - | ------------------------------------------------------------------------------------------------------------------------- |
  |   | The end-user UI is not bundled with PingIDM. Learn more in [Install the end-user UI](../setup-guide/idm-enduser-ui.html). |

* `userEditable`

  Specifies whether users can edit the property value in the UI. This property applies in the context of the End User UI, where users are able to edit certain properties of their own accounts. Boolean, `true` or `false` (`false` by default).

* `isProtected`

  Specifies whether reauthentication is required if the value of this property changes.

  For certain properties, such as passwords, changing the value of the property should force an end user to reauthenticate. These properties are referred to as *protected properties*. Depending on how the user authenticates (which authentication module is used), the list of protected properties is added to the user's security context. For example, if a user logs in with the login and password of their managed user entry (`MANAGED_USER` authentication module), their security context will include this list of protected properties. The list of protected properties is not included in the security context if the user logs in with a module that does not support reauthentication.

* `pattern`

  Any specific pattern to which the value of the property must adhere. For example, a property whose value is a date might require a specific date format.

* `policies`

  Any policy validation that must be applied to the property. For more information on managed object policies, refer to [Default policy for managed objects](configuring-default-policy.html).

* `required`

  Specifies whether the property must be supplied when an object of this type is created. Boolean, `true` or `false`.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                   |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | IDM assesses the `required` policy only during object creation, not when an object is updated. You can effectively bypass the policy by updating the object and supplying an empty value for that property. To prevent this inconsistency, set both `required` and `notEmpty` to `true` for required properties. This configuration indicates that the property must exist and must have a value. |

* `type`

  The data type for the property value; can be `string`, `array`, `boolean`, `integer`, `number`, `object`, `Resource Collection`, or `null`.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If any user might not have a value for a specific property (such as a `telephoneNumber`), you must include `null` as one of the property `types`. You can set a null property type in the admin UI (Configure > Managed Objects > User, select the property, and under the Details tab, Advanced Options, set `Nullable` to `true`).You can also set a null property type in your managed object configuration by setting `"type" : '[ "string","null" ]'` for that property (where `string` can be any other valid property type. This information is validated by the policy service, as described in [Validate Managed Object Data Types](configuring-default-policy.html#policy-config-input).If you're configuring a data `type` of `array` through the admin UI, you're limited to two values. |

* `isVirtual`

  Specifies whether the property takes a static value, or whether its value is calculated "on the fly" as the result of a script. Boolean, `true` or `false`.

* `returnByDefault`

  For non-core attributes (virtual attributes and relationship fields), specifies whether the property is returned in the results of a query on an object of this type *if it is not explicitly requested*. Virtual attributes and relationship fields are not returned by default. Boolean, `true` or `false`. When the property is in an array within a relationship, always set to `false`.

* `relationshipGrantTemporalConstraintsEnforced`

  For attributes with relationship fields. Specifies whether this relationship should have temporal constraints enforced. Boolean, `true` or `false`. For more information about temporal constraints, refer to [Use temporal constraints to restrict effective roles](roles-temporal-constraints.html).

* `default`

  Specifies a default value if the object is created without passing a value. Default values are available for the following data types, and arrays of those types:

  * boolean

  * number

  * object

  * string

  |   |                                                          |
  | - | -------------------------------------------------------- |
  |   | IDM assumes all default values are valid for the schema. |

* `enum`

  []()Restricts a field's possible values to a defined set of options. `enum` is supported for `string` and `number` types, and for `array` types containing strings or numbers.

  To define `enum` values, add the `enum` property to the field's schema definition in the managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint, or directly in the conf/managed.json file.)* using an API PUT request to the `/openidm/config/managed` endpoint or editing the file. Currently, you can't use the IDM admin UI to add, remove, or edit enums directly.

  In the following examples, the `string` type shows the JSON hierarchy of the property, while the others truncate everything except the property itself.

  * string

  * number

  * array of strings

  ```json
  {
    "_id": "managed",
    "objects": [
      {
        ...
        "schema": {
          ...
          "properties": [
            ...
            {
              "favoriteColor": {
                "enum": [
                  "red",
                  "green",
                  "blue"
                ],
                "title": "Favorite Color",
                "type": "string",
                "viewable": true,
                "searchable": false,
                "userEditable": true,
                "description": "Choose your favorite color",
                "format": null,
                "isVirtual": false
              },
              ...
  ```

  ```json
  {
    "custom_enum_single_number": {
      "title": "Rating",
      "description": "Select the best number",
      "type": "number",
      "viewable": true,
      "userEditable": true,
      "enum": [
        4,
        8,
        15,
        16,
        23,
        42
      ]
    }
  }
  ```

  ```json
  {
    "custom_enum_array_string": {
      "title": "Preferred Colors",
      "description": "Choose your preferred colors",
      "type": "array",
      "viewable": true,
      "userEditable": true,
      "items": {           (1)
        "type": "string",
        "enum": [
          "red",
          "green",
          "blue",
          "yellow"
        ]
      }
    }
  }
  ```

  |       |                                                                 |
  | ----- | --------------------------------------------------------------- |
  | **1** | The `enum` definition must be placed within the `items` object. |

## Create an object using the admin UI

1. Select Configure > Managed Objects > New Managed Object.

2. On the New Managed Object page, enter a name and readable title for the object, make optional changes, as necessary, and click Save. The readable title specifies the label that displays in the UI.

3. On the Properties tab, specify the schema for the object type (the properties that make up the object).

4. On the Scripts tab, specify any scripts that are triggered by events associated with the object type. For example, scripts that run when an object of this type is created, updated, or deleted.

You can also create a new managed object type by editing your managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint, or directly in the conf/managed.json file.)* using an API PUT request to the `/openidm/config/managed` endpoint or editing the file.

> **Collapse: Example:  object created using the admin UI**
>
> ```json
> {
>     "name": "Phone",
>     "schema": {
>         "$schema": "http://forgerock.org/json-schema#",
>         "type": "object",
>         "properties": {
>             "brand": {
>                 "description": "The supplier of the mobile phone",
>                 "title": "Brand",
>                 "viewable": true,
>                 "searchable": true,
>                 "userEditable": false,
>                 "policies": [],
>                 "returnByDefault": false,
>                 "pattern": "",
>                 "isVirtual": false,
>                 "type": [
>                     "string",
>                     "null"
>                 ]
>             },
>             "assetNumber": {
>                 "description": "The asset tag number of the mobile device",
>                 "title": "Asset Number",
>                 "viewable": true,
>                 "searchable": true,
>                 "userEditable": false,
>                 "policies": [],
>                 "returnByDefault": false,
>                 "pattern": "",
>                 "isVirtual": false,
>                 "type": "string"
>             },
>             "model": {
>                 "description": "The model number of the mobile device, such as 6 plus, Galaxy S4",
>                 "title": "Model",
>                 "viewable": true,
>                 "searchable": false,
>                 "userEditable": false,
>                 "policies": [],
>                 "returnByDefault": false,
>                 "pattern": "",
>                 "isVirtual": false,
>                 "type": "string"
>             }
>         },
>         "required": [],
>         "order": [
>             "brand",
>             "assetNumber",
>             "model"
>         ]
>     }
> }
> ```

## Default values

You can specify default values in the managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint, or directly in the conf/managed.json file.)*. If you omit a default value when creating an object, the default value is automatically applied to the object. You can have default values for the following data types, and arrays of those types:

* boolean

* number

* object

* string

For example, the default managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint, or directly in the conf/managed.json file.)* includes a default value that makes `accountStatus:active`, which effectively replaces the `onCreate` script that was previously used to achieve the same result. The following excerpt from the managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint, or directly in the conf/managed.json file.)* displays the default value for `accountStatus`:

```json
"accountStatus" : {
    "title" : "Status",
    "description" : "Status",
    "viewable" : true,
    "type" : "string",
    "searchable" : true,
    "userEditable" : false,
    "usageDescription" : "",
    "isPersonal" : false,
    "policies" : [
        {
            "policyId": "regexpMatches",
            "params": {
                "regexp": "^(active|inactive)$"
            }
        }
    ],
    "default" : "active"
}
```

|   |                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | IDM assumes all default values are valid for the schema. Although IDM skips policy validation for objects with default values, you can [force validation](policies-over-REST.html#force-validation-default-values) on property values. |

---

---
title: Create bidirectional relationships
description: Define PingIDM bidirectional relationships using reverseRelationship and reversePropertyName so objects can be queried from either side
component: pingidm
version: 8.1
page_id: pingidm:objects-guide:reverse-relationships
canonical_url: https://docs.pingidentity.com/pingidm/8.1/objects-guide/reverse-relationships.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Relationships"]
---

# Create bidirectional relationships

In most cases, you define a relationship between two objects *in both directions*. For example, a relationship between a user and his manager might indicate a *reverse relationship* between the manager and her direct report. Reverse relationships are particularly useful for queries. You might want to query jdoe's user entry to discover who his manager is, *or* query bjensen's user entry to discover all the users who report to bjensen.

You declare a reverse relationship as part of the relationship definition. Consider the following sample excerpt of the default managed object configuration:

```json
"reports" : {
    "description" : "Direct Reports",
    "title" : "Direct Reports",
    ...
    "type" : "array",
    "returnByDefault" : false,
    "items" : {
        "type" : "relationship",
        "reverseRelationship" : true,
        "reversePropertyName" : "manager",
        "validate" : true,
        ...
    }
...
```

The `reports` property is a `relationship` between users and managers. So, you can *refer* to a managed user's reports by referencing the `reports`. However, the reports property is also a reverse relationship (`"reverseRelationship" : true`) which means that you can list all users that reference that report.

You can list all users whose `manager` property is set to the currently queried user.

The reverse relationship includes an optional `resourceCollection` that lets you query a set of objects, based on specific fields:

```json
"resourceCollection" : [
    {
        "path" : "managed/user",
        "label" : "User",
        "query" : {
            "queryFilter" : "true",
            "fields" : [
                "userName",
                "givenName",
                "sn"
            ]
        }
    }
]
```

The `path` property of the `resourceCollection` points to the set of objects to be queried. If this path is not in the local repository, the link expansion can incur a significant performance cost. Although the `resourceCollection` is optional, the same performance cost is incurred if the property is absent.

The `query` property indicates how you will query this resource collection to configure the relationship. In this case, `"queryFilter" : "true",` indicates that you can search on any of the properties listed in the `fields` array when you are assigning a manager to a user or a new report to a manager.

To configure these relationships from the admin UI, refer to [Manage relationships using the admin UI](ui-relationships.html).

---

---
title: Data models and objects reference
description: "Reference overview of PingIDM data object types: managed, configuration, repository, system, audit, and link objects and their intended uses"
component: pingidm
version: 8.1
page_id: pingidm:objects-guide:appendix-objects
canonical_url: https://docs.pingidentity.com/pingidm/8.1/objects-guide/appendix-objects.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Schema"]
---

# Data models and objects reference

You can customize a variety of objects that can be addressed via a URL or URI. IDM can perform a common set of functions on these objects, such as CRUDPAQ (create, read, update, delete, patch, action, and query).

Depending on how you intend to use them, different object types are appropriate.

**Object Types**

| Object Type           | Intended Use                                                                                                                                 | Special Functionality                                                                                            |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Managed objects       | Serve as targets and sources for synchronization, and to build virtual identities.                                                           | Provide appropriate auditing, script hooks, declarative mappings and so forth in addition to the REST interface. |
| Configuration objects | Ideal for look-up tables or other custom configuration, which can be configured externally like any other system configuration.              | Adds file view, REST interface, and so forth                                                                     |
| Repository objects    | The equivalent of arbitrary database table access. Appropriate for managing data purely through the underlying data store or repository API. | Persistence and API access                                                                                       |
| System objects        | Representation of target resource objects, such as accounts, but also resource objects such as groups.                                       |                                                                                                                  |
| Audit objects         | Houses audit data in the repository.                                                                                                         |                                                                                                                  |
| Links                 | Defines a relation between two objects.                                                                                                      |                                                                                                                  |

---

---
title: Default policy for managed objects
description: Configure the default policy service for PingIDM managed objects, including policy scripts, configuration objects, and the admin UI validation setup
component: pingidm
version: 8.1
page_id: pingidm:objects-guide:configuring-default-policy
canonical_url: https://docs.pingidentity.com/pingidm/8.1/objects-guide/configuring-default-policy.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Policy"]
section_ids:
  policy-script-file: Policy script
  policy-config-object: Policy configuration objects
  policy-function: Policy implementation functions
  policy-reference: Default policy reference
  policy-config-element: Policy configuration element
  policy-config-input: Validate managed object data types
  policy-config-ui: Configure policy validation using the admin UI
---

# Default policy for managed objects

Policies applied to managed objects are configured in two places:

* A policy script that defines each policy and specifies how policy validation is performed.

  Learn more in the [Policy Script](#policy-script-file).

* A managed object policy element, defined in your managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint, or directly in the conf/managed.json file.)*, that specifies which policies are applicable to each managed resource. Learn more in the [Policy Configuration Element](#policy-config-element).

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                   |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The policy configuration *(tooltip: You can edit the policy configuration over REST at the config/policy endpoint, or directly in the conf/policy.json file.)* determines which policies apply to resources *other than managed objects*. The default policy configuration includes policies that are applied to internal user objects, but you can extend the configuration to apply policies to system objects. |

## Policy script

The policy script file (`openidm/bin/defaults/script/policy.js`) separates policy configuration into two parts:

* A policy configuration object, which defines each element of the policy. Learn more in [Policy Configuration Objects](#policy-config-object).

* A policy implementation function, which describes the requirements that are enforced by that policy.

Together, the configuration object and the implementation function determine whether an object is valid in terms of the applied policy. The following excerpt of a policy script file configures a policy that specifies that the value of a property must contain a certain number of capital letters:

```javascript
...
{   "policyId": "at-least-X-capitals",
    "policyExec": "atLeastXCapitalLetters",
    "clientValidation": true,
    "validateOnlyIfPresent": true,
    "policyRequirements": ["AT_LEAST_X_CAPITAL_LETTERS"]
},
...

policyFunctions.atLeastXCapitalLetters = function(fullObject, value, params, property) {
    var isRequired = _.find(this.failedPolicyRequirements, function (fpr) {
            return fpr.policyRequirement === "REQUIRED";
        }),
        isString = (typeof(value) === "string"),
        valuePassesRegexp = (function (v) {
            var test = isString ? v.match(/[A-Z]/g) : null;
            return test !== null && test.length >= params.numCaps;
        }(value));

    if ((isRequired || isString) && !valuePassesRegexp) {
        return [ { "policyRequirement" : "AT_LEAST_X_CAPITAL_LETTERS", "params" : {"numCaps": params.numCaps} } ];
    }

    return [];
}
...
```

To enforce user passwords that contain at least one capital letter, the `policyId` from the preceding example is applied to the appropriate resource (`managed/user/*`). The required number of capital letters is defined in the policy configuration element of the managed object configuration file. Learn more in the [Policy Configuration Element](#policy-config-element).

### Policy configuration objects

Each element of the policy is defined in a policy configuration object. The structure of a policy configuration object is as follows:

```json
{
    "policyId": "minimum-length",
    "policyExec": "minLength",
    "clientValidation": true,
    "validateOnlyIfPresent": true,
    "policyRequirements": ["MIN_LENGTH"]
}
```

|                         |                                                                                                                                                                                                                          |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `policyId`              | A unique ID that enables the policy to be referenced by component objects.                                                                                                                                               |
| `policyExec`            | The name of the function that contains the policy implementation. Learn more in [Policy Implementation Functions](#policy-function).                                                                                     |
| `clientValidation`      | Indicates whether the policy decision can be made on the client. When `"clientValidation": true`, the source code for the policy decision function is returned when the client requests the requirements for a property. |
| `validateOnlyIfPresent` | Notes that the policy is to be validated only if the field within the object being validated exists.                                                                                                                     |
| `policyRequirements`    | An array containing the policy requirement ID of each requirement that is associated with the policy. Typically, a policy will validate only one requirement, but it can validate more than one.                         |

### Policy implementation functions

Each policy ID has a corresponding policy implementation function that performs the validation. Implementation functions take the following form:

```javascript
function <name>(fullObject, value, params, propName) {
	<implementation_logic>
}
```

* `fullObject` is the full resource object that is supplied with the request.

* `value` is the value of the property that is being validated.

* `params` refers to the `params` array that is specified in the property's policy configuration.

* `propName` is the name of the property that is being validated.

The following example shows the implementation function for the `required` policy:

```javascript
function required(fullObject, value, params, propName) {
    if (value === undefined) {
        return [ { "policyRequirement" : "REQUIRED" } ];
    }
    return [];
}
```

## Default policy reference

IDM includes the following default policies and parameters:

| Policy Id                    | Parameters         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `required`                   |                    | The property is required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `not-empty`                  |                    | The property can't be empty.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `not-null`                   |                    | The property can't be null.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `unique`                     |                    | The property must be unique.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `valid-username`             |                    | The property must be unique and not have internal user conflicts.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `no-internal-user-conflict`  |                    | The property must not have internal user conflicts.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `regexpMatches`              | `regexp``flags`    | The property must match a regular expression pattern.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `valid-type`                 | `types`            | The property must have valid, specified types.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `valid-query-filter`         |                    | This rule enforces that each `privilege` entry adheres to the privilege defined in [Policies related to privileges](../auth-guide/delegated-admin.html#privilege-policies). The policy validates that the query filter used to filter privileges is a valid query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `valid-array-items`          |                    | This rule enforces that each `privilege` entry adheres to the privilege defined in [Policies related to privileges](../auth-guide/delegated-admin.html#privilege-policies). This policy validates that each item in an array contains the properties specified in `policy.json`, and that each of those properties satisfies any specific policies applied to it. By default, this policy verifies that each privilege contains `name`, `path`, `accessFlags`, `actions`, and `permissions` properties and that the `filter` property is valid if included.For example, the following parameters have a set of properties found within the array with individual policies for them:```json
{
  "params": {
    "properties": [
      {
        "name": "name",
        "policies": [
          {
            "policyId": "required"
          },
          {
            "policyId": "not-empty"
          },
          {
            "params": {
              "types": [
                "string"
              ]
            },
            "policyId": "valid-type"
          }
        ]
      },
      {
        "name": "path",
        "policies": [
          {
            "policyId": "required"
          },
          {
            "policyId": "not-empty"
          },
          ...
``` |
| `valid-date`                 |                    | The property must have a valid date. Learn more in [RFC 3339-5.6](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `valid-formatted-date`       |                    | The property must have a valid date format. Learn more in [RFC 3339-5.6](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `valid-time`                 |                    | The property must have a valid time. Learn more in [RFC 3339-5.6](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `valid-datetime`             |                    | The property must have a valid date and time. Learn more in [RFC 3339-5.6](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `valid-duration`             |                    | The property must have a valid duration format. Learn more in [RFC 3339-appendix-A](https://datatracker.ietf.org/doc/html/rfc3339#appendix-A).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `valid-email-address-format` |                    | The property must have a valid email address. Learn more in [RFC 5321-4.1.2](https://datatracker.ietf.org/doc/html/rfc5321#section-4.1.2).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `valid-name-format`          |                    | The property must have a valid name format. Learn more in [RFC 5321-3.5.1](https://datatracker.ietf.org/doc/html/rfc5321#section-3.5.1).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `valid-phone-format`         |                    | The property must have a valid phone number format. Learn more in [E.123](https://en.wikipedia.org/wiki/E.123).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `at-least-X-capitals`        | `numCaps`          | The property must contain the minimum specified number of capital letters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `at-least-X-numbers`         | `numNums`          | The property value must contain the minimum specified number of numbers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `validNumber`                |                    | The property value must be an integer or floating-point number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `minimumNumber`              | `minimum`          | The property value must be greater than the `minimum` value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `maximumNumber`              | `maximum`          | The property value must be less than the `maximum` value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `minimum-length`             | `minLength`        | The property's minimum string length.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `maximum-length`             | `maxLength`        | The property's maximum string length.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `cannot-contain-others`      | `disallowedFields` | The property cannot contain values of the specified fields. A comma-separated list of the fields to check against. For example, the default managed user password policy specifies `userName,givenName,sn` as disallowed fields.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `cannot-contain-characters`  | `forbiddenChars`   | The property cannot contain the specified characters. A comma-separated list of disallowed characters. For example, the default managed user `userName` policy specifies `/` as a disallowed character.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `cannot-contain-duplicates`  |                    | The property cannot contain duplicate characters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `mapping-exists`             |                    | A sync mapping must exist for the property.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `valid-permissions`          |                    | This rule enforces that each `privilege` entry adheres to the privilege defined in [Policies related to privileges](../auth-guide/delegated-admin.html#privilege-policies). The policy enforces well-formed permissions that include essential permissions, such as viewing, modification, or creation and adhere to a consistent and expected structure. This policy checks:- `CREATE` permissions must have write access to all properties required to create a new object.

- `CREATE` and `UPDATE` permissions must have write access to at least one property.

- `ACTION` permissions must include a list of allowed actions with at least one action included.

- If any attributes have write access, then the privilege must also have either the `CREATE` or `UPDATE` permission.

- All permissions listed must be valid types of permission: `VIEW`, `CREATE`, `UPDATE`, `ACTION`, or `DELETE`. No permissions are repeated.For example, a policy failure of `PRIVILEGE_MISSING_REQUIRED_CREATE_ATTRIBUTES` means that the privilege to create a managed object lacks access to that object's required attributes.                                                                                                                                                                          |
| `valid-accessFlags-object`   |                    | This rule enforces that each `privilege` entry adheres to the privilege defined in [Policies related to privileges](../auth-guide/delegated-admin.html#privilege-policies). This policy validates if the `accessFlags` for a privilege matches the defined schema. The `accessFlag` entry must:- Contain an `attribute` property with a `String` value that matches a property name defined within the managed object's schema. The string value, such as "firstName", must be a property of the managed object for IDM to reference.

- Contain a `readOnly` property with a boolean value.

- Not contain any other attributes.For example, property names must be strings, such as "firstName", "lastName", "email". The property value must contain a property named `readOnly` whose value is a boolean, or `true` or `false`. The property value is invalid if it contains properties other than `readOnly`.                                                                                                                                                                                                                                                                                                                                                                                      |
| `valid-privilege-path`       |                    | This rule enforces that each `privilege` entry adheres to the privilege defined in [Policies related to privileges](../auth-guide/delegated-admin.html#privilege-policies). This policy validates that the `path` specified in the privilege is a valid object with a schema for IDM to reference. Only objects with a schema, such as `managed/user` can have privileges applied to them.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `valid-temporal-constraints` |                    | The property must have valid temporal constraints. A non-empty array or a `ScriptableList` that must conform to a specific, predefined structure or pattern.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

## Policy configuration element

Properties defined in the managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint, or directly in the conf/managed.json file.)* can include a `policies` element that specifies how policy validation should be applied to that property. The following excerpt of the default managed object configuration shows how policy validation is applied to the `password` and `_id` properties of a managed/user object.

|   |                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can only declare policies on top-level managed object attributes. Nested attributes, or those within an array or object, cannot have policy declared on them. |

```json
{
    "name" : "user",
    "schema" : {
        "id" : "http://jsonschema.net",
        "properties" : {
            "_id" : {
                "description" : "User ID",
                "type" : "string",
                "viewable" : false,
                "searchable" : false,
                "userEditable" : false,
                "usageDescription" : "",
                "isPersonal" : false,
                "policies" : [
                    {
                        "policyId" : "cannot-contain-characters",
                        "params" : {
                            "forbiddenChars" : [
                                "/"
                            ]
                        }
                    }
                ]
            },
            "password" : {
                "title" : "Password",
                "description" : "Password",
                "type" : "string",
                "viewable" : false,
                "searchable" : false,
                "userEditable" : true,
                "encryption" : {
                    "purpose" : "idm.password.encryption"
                },
                "scope" : "private",
                "isProtected": true,
                "usageDescription" : "",
                "isPersonal" : false,
                "policies" : [
                    {
                        "policyId" : "minimum-length",
                        "params" : {
                            "minLength" : 8
                        }
                    },
                    {
                        "policyId" : "at-least-X-capitals",
                        "params" : {
                            "numCaps" : 1
                        }
                    },
                    {
                        "policyId" : "at-least-X-numbers",
                        "params" : {
                            "numNums" : 1
                        }
                    },
                    {
                        "policyId" : "cannot-contain-others",
                        "params" : {
                            "disallowedFields" : [
                                "userName",
                                "givenName",
                                "sn"
                            ]
                        }
                    }
                ]
            }
        }
    }
}
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The policy for the `_id` property references the function `cannot-contain-characters` that is defined in the `policy.js` file. The policy for the `password` property references the functions `minimum-length`, `at-least-X-capitals`, `at-least-X-numbers`, and `cannot-contain-others` that are defined in the `policy.js` file. The parameters that are passed to these functions, such as the number of capitals required, are specified in the same element. |

## Validate managed object data types

The `type` property of a managed object specifies the data type of that property, for example, `array`, `boolean`, `number`, `null`, `object`, or `string`. Learn more about data types in the [Type-specific Keywords](https://json-schema.org/understanding-json-schema/reference/type) section of the JSON Schema Reference.

The `type` property is subject to policy validation when a managed object is created or updated. Validation fails if data doesn't match the specified `type`, such as when the data is an `array` instead of a `string`. The default `valid-type` policy enforces the match between property values and the `type` defined in the managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint, or directly in the conf/managed.json file.)*.

IDM supports multiple valid property types. For example, you might have a scenario where a managed user can have more than one telephone number or a *null* telephone number when the user entry is first created, and the telephone number is not yet known. In such a case, you can specify the accepted property type as follows in your managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint, or directly in the conf/managed.json file.)*:

```json
"telephoneNumber" : {
    "type" : "string",
    "title" : "Telephone Number",
    "description" : "Telephone Number",
    "viewable" : true,
    "userEditable" : true,
    "pattern" : "^\\+?([0-9\\- \\(\\)])*$",
    "usageDescription" : "",
    "isPersonal" : true,
    "policies" : [
        {
            "policyId" : "minimum-length",
            "params" : {
                "minLength" : 1
            }
        },
        {
            "policyId": "maximum-length",
            "params": {
                "maxLength": 255
            }
        }
    ]
}
```

In this case, the `valid-type` policy from the `policy.js` file checks the telephone number for an accepted `type` and `pattern` either for a real telephone number or a `null` entry.

## Configure policy validation using the admin UI

To configure policy validation for a managed object type using the IDM admin UI, update the configuration of the object type:

1. Go to the managed object, and edit or create a property.

2. Click the Validation tab, and add the policy.

> **Collapse: Show Me**
>
> ![createPolicyUI](_images/createPolicyUI.gif)

1. In the navigation bar, click Configure > Managed Objects.

2. On the Managed Objects page, [edit or create a managed object](creating-modifying-managed-objects.html).

3. On the Managed Object NAME page, do one of the following:

   * To edit an existing property, click the property.

   * To create a property, click Add a Property, enter the required information, and click Save.

     * Now click the property.

4. On the Validation tab, click Add Policy.

5. In the Add/Edit Policy modal, enter information in the following fields, and click Add or Save:

   * Policy Id

     Refers to the unique `PolicyId` in the `policy.js` file.

     Learn more about default policies in the [Policy Reference](#policy-reference).

   * Parameter Name

     Refers to the parameters for the `PolicyId`. You can find a list of the default policy parameters in the [Policy Reference](#policy-reference).

   * Value

     The parameter's value to validate.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Be cautious when using validation policies. If a policy relates to an array of relationships, such as between a user and multiple devices, you should always set Return by Default to `false`. You can verify this setting in your managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint, or directly in the conf/managed.json file.)*. Any managed object that has `items` of `"type" : "relationship"`, must also have `"returnByDefault" : false`. |

---

---
title: Define and call data queries
description: Define and call PingIDM queries using common filter expressions, parameterized queries, and native query expressions on managed and system objects
component: pingidm
version: 8.1
page_id: pingidm:objects-guide:queries
canonical_url: https://docs.pingidentity.com/pingidm/8.1/objects-guide/queries.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "REST API", "JDBC", "Virtual Properties"]
section_ids:
  query-array-reqs: Queries on object array properties (JDBC)
  special-char-queries: Special characters in queries
  query-filters: Common filter expressions
  parameterized-queries: Parameterized queries
  parameterized-queries-queryid-entries: queryId entries
  parameterized-queries-query-filters: queryFilters
  native-queries: Native query expressions
  constructing-queries: Construct queries
  query-comp-expression: Comparison expressions
  query-presence: Presence expressions
  query-literal: Literal expressions
  query-in: In expression clause
  filter-expand-relation: Filter expanded relationships
  query-complex: Complex expressions
  filter_objects_in_arrays: Filter objects in arrays
  paging-query-results: Page query results
  sorting-query-results: Sort query results
  execute-on-retrieve: Recalculate virtual property values in queries
---

# Define and call data queries

An advanced query model enables you to define queries and to call them over the REST or Resource API. The following types of queries are supported, on both managed, and system objects:

* Common filter expressions

* Parameterized, or predefined queries

* Native query expressions

## Queries on object array properties (JDBC)

Support for queries on object array properties requires the following:

* A JDBC repository with [generic object mapping](explicit-generic-mapping-jdbc.html#generic-mappings-jdbc). Queries on arrays are not supported with explicit mappings. If you need to convert from explicitly mapped objects to generic, refer to [Convert an Explicit Mapped Object to a Hybrid Mapped Object (JDBC)](explicit-generic-mapping-jdbc.html#convert-explicit-to-hybrid-jdbc).

* For PostgreSQL only, you must [configure array fields](../install-guide/repository-postgresql.html#postgres-conf-search-array). [Additional information about PostgreSQL JSON functions](https://www.postgresql.org/docs/9.5/functions-json.html).

* For JDBC repositories other than PostgreSQL, the array property must be [configured as searchable](explicit-generic-mapping-jdbc.html#generic-mappings-jdbc). If you add additional properties as searchable after the initial install/migration of IDM, run the `/path/to/openidm/bin/defaults/script/update/rewriteObjects.js` script, specifying the new `objectPaths` of properties to make searchable:

  ```none
  curl \
  --header "Content-Type: application/json" \
  --header "X-OpenIDM-Username: openidm-admin" \
  --header "X-OpenIDM-Password: openidm-admin" \
  --header 'X-OpenIDM-NoSession: true' \
  --request POST \
  --data-raw '{
    "type": "text/javascript",
    "file": "/path/to/openidm/bin/defaults/script/update/rewriteObjects.js",
    "globals": {
      "rewriteConfig": {
        "queryFilter": "true",
        "pageSize": 1000,
        "objectPaths": [
          "repo/config",
          "repo/internal/usermeta",
          "repo/managed/role",
          "repo/managed/user",
          "repo/reconprogressstate",
          "repo/relationships",
          "repo/scheduler/triggers"
        ]
      }
    }
  }' \
  "http://localhost:8080/openidm/script/?_action=eval"
  ```

* Do not use array fields in a `sortKey`.

## Special characters in queries

JavaScript query invocations are not subject to the same URL-encoding requirements as GET requests. Because JavaScript supports the use of single quotes, it is not necessary to escape the double quotes from most examples in this guide. Make sure to protect against pulling in data that could contain special characters, such as double-quotes (`"`). The following example shows one method of handling special characters:

```json
"correlationQuery" : {
  "type" : "text/javascript",
  "source" : "var qry = {'_queryFilter': org.forgerock.util.query.QueryFilter.equalTo('uid', source.userName).toString()}; qry"
}
```

## Common filter expressions

The Ping REST API defines common filter expressions that enable you to form arbitrary queries using a number of supported filter operations. This query capability is the standard way to query data if no predefined query exists, and is supported for all managed and system objects.

Common filter expressions are useful in that they do not require knowledge of how the object is stored and do not require additions to the repository configuration.

Common filter expressions are called with the `_queryFilter` keyword. The following example uses a common filter expression to retrieve managed user objects whose user name is Smith:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
'http://localhost:8080/openidm/managed/user?_queryFilter=userName+eq+"smith"'
```

The filter is URL encoded in this example. The corresponding filter using the resource API would be:

```javascript
openidm.query("managed/user", { "_queryFilter" : '/userName eq "smith"' });
```

|   |                                                                                                                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This JavaScript invocation is internal and isn't subject to the same URL-encoding requirements that a GET request would be. Because JavaScript supports the use of single quotes, it's not necessary to escape the double quotes in the preceding example. |

## Parameterized queries

You can access managed objects in JDBC repositories using custom parameterized queries through [queryId entries](#parameterized-queries-queryid-entries). Define these queries in your JDBC repository configuration in `repo.*.json` and call them by their `_queryId`.

|   |                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For system objects or for PingDS repositories, parameterized queries are defined outside of the JDBC repository configuration using [query filters](#parameterized-queries-query-filters) in the `queryFilters.json` file in your project's `conf` directory. |

### queryId entries

A typical query definition is as follows:

```sql
"query-all-ids" : "SELECT objectid FROM ${_dbSchema}.${_table} LIMIT ${int:_pageSize} OFFSET ${int:_pagedResultsOffset}",
```

To call this query, you would reference its ID, as follows:

```javascript
?_queryId=query-all-ids
```

The following example calls `query-all-ids` over the REST interface:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
"http://localhost:8080/openidm/managed/user?_queryId=query-all-ids"
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | In `repo.jdbc.json`, the `queries` configuration object has a property, `validInRelationshipQuery`, which is an array specifying the IDs of queries that use relationships. If you define parameterized queries that you expect to use as part of a relationship query, you must add the query ID to this array. If no query IDs are specified or if the property is absent, relationship information isn't returned in query results, even if requested. Learn more in [Configuring relationships](relationships.html). |

### queryFilters

To define parameterized queries outside of JDBC repositories, use the `queryFilters.json` file in your project's `conf` directory. This configuration file also allows customers to define additional `queryId` to `queryFilter` mappings and to change the authentication queries for customized authentication attributes related to `queryIds`. Learn more in [Attributes used for authentication](../auth-guide/authenticating-users.html#authentication-attributes).

The following queries demonstrate using `queryFilters.json`:

```json
{
    "credential-query" : {
        "_queryFilter" : "/userName eq \"${username}\" AND /accountStatus eq \"active\"",
        "_fields" : [
            "sn"
        ]
    },
    "credential-internaluser-query" : {
        "_queryFilter" : "/_id eq \"${username}\"",
        "_fields" : [
            "sn"
        ]
    },
    "for-userName" : {
        "_queryFilter" : "/userName eq \"${uid}\"",
        "_fields" : [
            "sn"
        ]
    }
}
```

## Native query expressions

Native query expressions are supported for system objects only, and can be called directly.

You should only use native queries in situations where common query filters or parameterized queries are insufficient. For example, native queries are useful if the query needs to be generated dynamically.

The query expression is specific to the target resource and uses the native query language of that system resource.

Native queries are made using the `_queryExpression` keyword.

## Construct queries

The `openidm.query` function lets you query managed and system objects. The query syntax is `openidm.query(id, params)`, where `id` specifies the object on which the query should be performed, and `params` provides the parameters that are passed to the query (the `_queryFilter`). For example:

```javascript
var equalTo = org.forgerock.util.query.QueryFilter.equalTo;
queryParams = {
    "_queryFilter": equalTo("uid", value).toString()
};
openidm.query("managed/user", queryParams)
```

Over the REST interface, the query filter is specified as `_queryFilter=filter`, for example:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
'http://localhost:8080/openidm/managed/user?_queryFilter=userName+eq+"Smith"'
```

|   |                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------- |
|   | In `_queryFilter` expressions, string values *must* use double-quotes. Numeric and boolean expressions should not use quotes. |

When called over REST, you must URL encode the filter expression. The following examples show the filter expressions using the resource API and the REST API, but do not show the URL encoding, to make them easier to read.

For generic mappings, any fields that are included in the query filter (for example `userName` in the previous query), must be explicitly defined as *searchable*, if you have set the global `searchableDefault` to false. For more information, refer to [Improving Generic Mapping Search Performance (JDBC)](explicit-generic-mapping-jdbc.html#searches-with-generic-mappings).

The filter expression is constructed from the building blocks shown in this section. In these expressions the simplest json-pointer is a field of the JSON resource, such as `userName` or `id`. A JSON pointer can, however, point to nested elements.

|   |                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can also use the negation operator (**`!`**) in query construction. For example, a `_queryFilter=!(userName+eq+"jdoe")` query would return every `userName` except for `jdoe`. |

### Comparison expressions

You can use comparison query filters for objects and object array properties that:

> **Collapse: Equal a specified value**
>
> This is the associated JSON comparison expression: `json-pointer eq json-value`.
>
> Example 1
>
> ```json
> "_queryFilter" : '/givenName eq "Dan"'
> ```
>
> The following REST call returns the user name and given name of all managed users whose first name (`givenName`) is "Dan":
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Accept-API-Version: resource=1.0" \
> --request GET \
> 'http://localhost:8080/openidm/managed/user?_queryFilter=givenName+eq+"Dan"&_fields=userName,givenName'
> {
>   "result": [
>     {
>       "givenName": "Dan",
>       "userName": "dlangdon"
>     },
>     {
>       "givenName": "Dan",
>       "userName": "dcope"
>     },
>     {
>       "givenName": "Dan",
>       "userName": "dlanoway"
>     }
>   ],
>   ...
> }
> ```
>
> Example 2
>
> ```json
> "_queryFilter" : "/stringArrayField eq 'foo'"
> ```
>
> The following REST call returns role entries where a value within the `stringArrayField` array equals "foo":
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Accept-API-Version: resource=1.0" \
> --request GET \
> 'http://localhost:8080/openidm/managed/role?_queryFilter=stringArrayField+eq+"foo"'
> {
>   "result": [
>     {
>       "_id": "admin2",
>       "_rev": "0",
>       "name": "admin2",
>       "stringArrayField": [
>         "foo",
>         "bar"
>       ]
>     }
>   ],
>   ...
> }
> ```
>
> [Additional information about PostgreSQL JSON functions](https://www.postgresql.org/docs/9.5/functions-json.html).

> **Collapse: Contain a specified value**
>
> This is the associated JSON comparison expression: `json-pointer co json-value`.
>
> Example
>
> ```json
> "_queryFilter" : '/givenName co "Da"'
> ```
>
> The following REST call returns the user name and given name of all managed users whose first name (`givenName`) contains "Da":
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Accept-API-Version: resource=1.0" \
> --request GET \
> 'http://localhost:8080/openidm/managed/user?_queryFilter=givenName+co+"Da"&_fields=userName,givenName'
> {
>   "result": [
>     {
>       "givenName": "Dave",
>       "userName": "djensen"
>     },
>     {
>       "givenName": "David",
>       "userName": "dakers"
>     },
>     {
>       "givenName": "Dan",
>       "userName": "dlangdon"
>     },
>     {
>       "givenName": "Dan",
>       "userName": "dcope"
>     },
>     {
>       "givenName": "Dan",
>       "userName": "dlanoway"
>     },
>     {
>       "givenName": "Daniel",
>       "userName": "dsmith"
>     },
>     ...
>   ],
>   "resultCount": 10,
>   "pagedResultsCookie": null,
>   "remainingPagedResults": -1
> }
> ```

> **Collapse: Start with a specified value**
>
> This is the associated JSON comparison expression: `json-pointer sw json-value`.
>
> Example
>
> ```json
> "_queryFilter" : '/sn sw "Jen"'
> ```
>
> The following REST call returns the user names of all managed users whose last name (`sn`) starts with "Jen":
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Accept-API-Version: resource=1.0" \
> --request GET \
> 'http://localhost:8080/openidm/managed/user?_queryFilter=sn+sw+"Jen"&_fields=userName'
> {
>   "result": [
>     {
>       "userName": "bjensen"
>     },
>     {
>       "userName": "djensen"
>     },
>     {
>       "userName": "cjenkins"
>     },
>     {
>       "userName": "mjennings"
>     }
>   ],
>   "resultCount": 4,
>   "pagedResultsCookie": null,
>   "remainingPagedResults": -1
> }
> ```

> **Collapse: Are less than a specified value**
>
> This is the associated JSON comparison expression: `json-pointer lt json-value`.
>
> Example
>
> ```json
> "_queryFilter" : '/employeeNumber lt 5000'
> ```
>
> The following REST call returns the user names of all managed users whose `employeeNumber` is lower than 5000:
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Accept-API-Version: resource=1.0" \
> --request GET \
> 'http://localhost:8080/openidm/managed/user?_queryFilter=employeeNumber+lt+5000&_fields=userName,employeeNumber'
> {
>   "result": [
>     {
>       "employeeNumber": 4907,
>       "userName": "jnorris"
>     },
>     {
>       "employeeNumber": 4905,
>       "userName": "afrancis"
>     },
>     {
>       "employeeNumber": 3095,
>       "userName": "twhite"
>     },
>     {
>       "employeeNumber": 3921,
>       "userName": "abasson"
>     },
>     {
>       "employeeNumber": 2892,
>       "userName": "dcarter"
>     },
>     ...
>   ],
>   "resultCount": 4999,
>   "pagedResultsCookie": null,
>   "remainingPagedResults": -1
> }
> ```

> **Collapse: Are less than or equal to a specified value**
>
> This is the associated JSON comparison expression: `json-pointer le json-value`.
>
> Example
>
> ```json
> "_queryFilter" : '/employeeNumber le 5000'
> ```
>
> The following REST call returns the user names of all managed users whose `employeeNumber` is 5000 or less:
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Accept-API-Version: resource=1.0" \
> --request GET \
> 'http://localhost:8080/openidm/managed/user?_queryFilter=employeeNumber+le+5000&_fields=userName,employeeNumber'
> {
>   "result": [
>     {
>       "employeeNumber": 4907,
>       "userName": "jnorris"
>     },
>     {
>       "employeeNumber": 4905,
>       "userName": "afrancis"
>     },
>     {
>       "employeeNumber": 3095,
>       "userName": "twhite"
>     },
>     {
>       "employeeNumber": 3921,
>       "userName": "abasson"
>     },
>     {
>       "employeeNumber": 2892,
>       "userName": "dcarter"
>     },
>     ...
>   ],
>   "resultCount": 5000,
>   "pagedResultsCookie": null,
>   "remainingPagedResults": -1
> }
> ```

> **Collapse: Are greater than a specified value**
>
> This is the associated JSON comparison expression: `json-pointer gt json-value`
>
> Example
>
> ```json
> "_queryFilter" : '/employeeNumber gt 5000'
> ```
>
> The following REST call returns the user names of all managed users whose `employeeNumber` is higher than 5000:
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Accept-API-Version: resource=1.0" \
> --request GET \
> 'http://localhost:8080/openidm/managed/user?_queryFilter=employeeNumber+gt+5000&_fields=userName,employeeNumber'
> {
>   "result": [
>     {
>       "employeeNumber": 5003,
>       "userName": "agilder"
>     },
>     {
>       "employeeNumber": 5011,
>       "userName": "bsmith"
>     },
>     {
>       "employeeNumber": 5034,
>       "userName": "bjensen"
>     },
>     {
>       "employeeNumber": 5027,
>       "userName": "cclarke"
>     },
>     {
>       "employeeNumber": 5033,
>       "userName": "scarter"
>     },
>     ...
>   ],
>   "resultCount": 1458,
>   "pagedResultsCookie": null,
>   "remainingPagedResults": -1
> }
> ```

> **Collapse: Are greater than or equal to a specified value**
>
> This is the associated JSON comparison expression: `json-pointer ge json-value`.
>
> Example
>
> ```json
> "_queryFilter" : '/employeeNumber ge 5000'
> ```
>
> The following REST call returns the user names of all managed users whose `employeeNumber` is 5000 or greater:
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Accept-API-Version: resource=1.0" \
> --request GET \
> 'http://localhost:8080/openidm/managed/user?_queryFilter=employeeNumber+ge+5000&_fields=userName,employeeNumber'
> {
>   "result": [
>     {
>       "employeeNumber": 5000,
>       "userName": "agilder"
>     },
>     {
>       "employeeNumber": 5011,
>       "userName": "bsmith"
>     },
>     {
>       "employeeNumber": 5034,
>       "userName": "bjensen"
>     },
>     {
>       "employeeNumber": 5027,
>       "userName": "cclarke"
>     },
>     {
>       "employeeNumber": 5033,
>       "userName": "scarter"
>     },
>     ...
>   ],
>   "resultCount": 1457,
>   "pagedResultsCookie": null,
>   "remainingPagedResults": -1
> }
> ```

|   |                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Although specific system endpoints also support `EndsWith` and `ContainsAllValues` queries, such queries are *not supported* for managed objects and have not been tested with all supported ICF connectors. |

### Presence expressions

The following examples show how you can build filters using a presence expression, shown as `pr`. The presence expression is a filter that returns all records with a given attribute.

A presence expression filter evaluates to `true` when a `json-pointer pr` matches any object in which the json-pointer is present, and contains a non-null value. Consider the following expression:

```json
"_queryFilter" : '/mail pr'
```

The following REST call uses that expression to return the mail addresses for all managed users with a `mail` property:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
'http://localhost:8080/openidm/managed/user?_queryFilter=mail+pr&_fields=mail'
{
  "result": [
    {
      "mail": "jdoe@exampleAD.com"
    },
    {
      "mail": "bjensen@example.com"
    }
  ],
  "resultCount": 2,
  "pagedResultsCookie": null,
  "remainingPagedResults": -1
}
```

Depending on the connector, you can apply the presence filter on system objects. The following query returns the email address of all users in a CSV file who have the `email` attribute in their entries:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
'http://localhost:8080/openidm/system/csvfile/account?_queryFilter=email+pr&_fields=email'
{
  "result": [
    {
      "_id": "bjensen",
      "email": "bjensen@example.com"
    },
    {
      "_id": "scarter",
      "email": "scarter@example.com"
    }
  ],
  "resultCount": 2,
  "pagedResultsCookie": "MA%3D%3D",
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": -1
}
```

|   |                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Not all connectors support the presence filter. In most cases, you can replicate the behavior of the presence filter with an "equals" (`eq`) query such as `_queryFilter=email+eq"*"` |

### Literal expressions

A literal expression is a boolean:

* `true` matches any object in the resource.

* `false` matches no object in the resource.

For example, you can list the `_id` of all managed objects as follows:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
'http://localhost:8080/openidm/managed/user?_queryFilter=true&_fields=_id'
{
  "result": [
    {
      "_id": "d2e29d5f-0d74-4d04-bcfe-b1daf508ad7c"
    },
    {
      "_id": "709fed03-897b-4ff0-8a59-6faaa34e3af6"
    }
  ],
  "resultCount": 2,
  "pagedResultsCookie": null,
  "remainingPagedResults": -1
}
```

### `In` expression clause

IDM provides limited support for the [in expression clause](#query-in). You can use this clause for queries on singleton string properties or arrays. The `in` query expression is not supported through the admin UI or for use by [delegated administrators](../auth-guide/delegated-admin.html#using-delegated-admin).

The `in` operator is shorthand for multiple `OR` conditions.

|   |                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The following example command includes escaped characters. For readability, the non-escaped URL syntax is:```none
http://localhost:8080/openidm/managed/user?_pageSize=1000&_fields=userName&_queryFilter=/userName in '["user4a","user3a"]'
``` |

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"http://localhost:8080/openidm/managed/user?_pageSize=1000&_fields=userName&_queryFilter=userName%20in%20'%5B%22user4a%22%2C%22user3a%22%5D'"
{
  "result": [
    {
      "_id": "e32f9a3d-0039-4cb0-82d7-347cb808672e",
      "_rev": "000000000ae18357",
      "userName": "user3a"
    },
    {
      "_id": "120625c5-cfe7-48e7-b66a-6a0a0f9d2901",
      "_rev": "000000005ad98467",
      "userName": "user4a"
    }
  ],
  "resultCount": 2,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": -1
}
```

### Filter expanded relationships

You can use `_queryFilter` to directly filter expanded relationships from a collection, such as `authzRoles`. The following example queries the `manager-int` authorization role of a user:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"http://localhost:8080/openidm/managed/user/b70293db-8743-45a7-9215-1ca8fd8a0073/authzRoles?_queryFilter=name+eq+'manager-int'&_fields=*"
{
  "result": [
    {
      "_id": "b1d78144-7029-4135-8e73-85efe0a40b6b",
      "_rev": "00000000d4b8ab97",
      "_ref": "internal/role/c0a38233-c0f2-477d-8f18-f5485b7d002f",
      "_refResourceCollection": "internal/role",
      "_refResourceId": "c0a38233-c0f2-477d-8f18-f5485b7d002f",
      "_refProperties": {
        "_grantType": "",
        "_id": "b1d78144-7029-4135-8e73-85efe0a40b6b",
        "_rev": "00000000d4b8ab97"
      },
      "name": "manager-int",
      "description": "manager-int-desc",
      "temporalConstraints": null,
      "condition": null,
      "privileges": null
    }
  ],
  "resultCount": 1,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": -1
}
```

|   |                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can use `_queryFilter` on fields within `_refProperties` when using DS as your repository. This functionality is not available if you are using a JDBC repository. |

### Complex expressions

You can combine expressions using the boolean operators `and`, `or`, and `!` (not). The following example queries managed user objects located in London, with last name Jensen:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
'http://localhost:8080/openidm/managed/user/?_queryFilter=city+eq+"London"and+sn+eq"Jensen"&_fields=userName,givenName,sn'
{
  "result": [
    {
      "sn": "Jensen",
      "givenName": "Clive",
      "userName": "cjensen"
    },
    {
      "sn": "Jensen",
      "givenName": "Dave",
      "userName": "djensen"
    },
    {
      "sn": "Jensen",
      "givenName": "Margaret",
      "userName": "mjensen"
    }
  ],
  "resultCount": 3,
  "pagedResultsCookie": null,
  "remainingPagedResults": -1
}
```

### Filter objects in arrays

Use query grouping to perform your query on properties within an array. For example, to query `effectiveRoles` for users who have the `testManagedRole`, check the `_refResourceId` inside the `effectiveRoles` array:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
'http://localhost:8080/openidm/managed/user/?_queryFilter=/effectiveRoles\[/_refResourceId+eq+"testManagedRole"]&_fields=userName,givenName,sn,effectiveRoles'
{
  "result": [
    {
      "_id": "917bc052-ef39-4add-ae05-0a278e2de9c0",
      "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1565",
      "userName": "scarter",
      "sn": "Carter",
      "givenName": "Steven",
      "effectiveRoles": [
        {
          "_refResourceCollection": "managed/role",
          "_refResourceId": "testManagedRole",
          "_ref": "managed/role/testManagedRole"
        }
      ]
    },
    {
      "_id": "aca0042c-9f4c-4ad5-8cf7-aca0adeb3470",
      "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1545",
      "userName": "jdoe",
      "sn": "Doe",
      "givenName": "John",
      "effectiveRoles": [
        {
          "_refResourceCollection": "managed/role",
          "_refResourceId": "testManagedRole",
          "_ref": "managed/role/testManagedRole"
        }
      ]
    }
  ],
  "resultCount": 2,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": -1
}
```

|   |                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Because `curl` uses brackets (`[]`, `{}`) for processing, you need to escape your brackets with a `\`. This may be unnecessary in cases where you are using a different method to call IDM. |

|   |                                                                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This syntax is only available when using DS or PostgreSQL as your repository.When using a PostgreSQL repository and querying an array, properties that are a string, boolean, number, or object are supported. However, arrays are not supported (you can't filter on an array within an array). |

## Page query results

The common filter query mechanism supports paged query results for managed objects, and for some system objects, depending on the system resource. There are two ways to page objects in a query:

* Using a cookie based on the value of a specified sort key.

* Using an offset that specifies how many records should be skipped before the first result is returned.

These methods are implemented with the following query parameters:

* `_pagedResultsCookie`

  Opaque cookie used by the server to keep track of the position in the search results. The format of the cookie is a base-64 encoded version of the value of the unique sort key property. The value of the returned cookie is URL-encoded to prevent values such as `+` from being incorrectly translated.

  You cannot page results without sorting them (using the `_sortKeys` parameter). If you do not specify a sort key, the `_id` of the record is used as the default sort key. At least one of the specified sort key properties must be a unique value property, such as `_id`.

  |   |                                                                                                                                                                                                                                                                                                                           |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | For paged searches on generic mappings, you should sort on the `_id` property, because this is the only property that is stored outside of the JSON blob. If you sort on something other than `_id`, the search will incur a performance hit because IDM effectively has to pull the entire result set, and then sort it. |

  The server provides the cookie value on the first request. You should then supply the cookie value in subsequent requests until the server returns a null cookie, meaning that the final page of results has been returned.

  The `_pagedResultsCookie` parameter is supported only for filtered queries, that is, when used with the `_queryFilter` parameter. You cannot use the `_pagedResultsCookie` with a `_queryId`.

  The `_pagedResultsCookie` and `_pagedResultsOffset` parameters are mutually exclusive, and cannot be used together.

  Paged results are enabled only if the `_pageSize` is a non-zero integer.

* `_pagedResultsOffset`

  Specifies the index within the result set of the number of records to be skipped before the first result is returned. The format of the `_pagedResultsOffset` is an integer value. When the value of `_pagedResultsOffset` is greater than or equal to 1, the server returns pages, starting after the specified index.

  This request assumes that the `_pageSize` is set, and not equal to zero.

  For example, if the result set includes 10 records, the `_pageSize` is 2, and the `_pagedResultsOffset` is 6, the server skips the first 6 records, then returns 2 records, 7 and 8. The `_remainingPagedResults` value would be 2, the last two records (9 and 10) that have not yet been returned.

  If the offset points to a page beyond the last of the search results, the result set returned is empty.

* `_pageSize`

  An optional parameter indicating that query results should be returned in pages of the specified size. For all paged result requests other than the initial request, a cookie should be provided with the query request.

  The default behavior is not to return paged query results. If set, this parameter should be an integer value, greater than zero.

  When a `_pageSize` is specified, and non-zero, the server calculates the `totalPagedResults`, in accordance with the `totalPagedResultsPolicy`, and provides the value as part of the response. If a count policy is specified (`_totalPagedResultsPolicy=EXACT`, The `totalPagedResults` returns the total result count. If no count policy is specified in the query, or if `_totalPagedResultsPolicy=NONE`, result counting is disabled, and the server returns a value of -1 for `totalPagedResults`. The following example shows a query that requests two results with a `totalPagedResultsPolicy` of `EXACT`:

  ```
  curl \
  --header "X-OpenIDM-Username: openidm-admin" \
  --header "X-OpenIDM-Password: openidm-admin" \
  --header "Accept-API-Version: resource=1.0" \
  --request GET \
  "http://localhost:8080/openidm/managed/user?_queryFilter=true&_pageSize=2&_totalPagedResultsPolicy=EXACT"
  {
    "result": [
      {
        "_id": "adonnelly",
        "_rev": "0",
        "userName": "adonnelly",
        "givenName": "Abigail",
        "sn": "Donnelly",
        "telephoneNumber": "12345678",
        "active": "true",
        "mail": "adonnelly@example.com",
        "accountStatus": "active",
        "effectiveRoles": [],
        "effectiveAssignments": []
      },
      {
        "_id": "bjensen",
        "_rev": "0",
        "userName": "bjensen",
        "givenName": "Babs",
        "sn": "Jensen",
        "telephoneNumber": "12345678",
        "active": "true",
        "mail": "bjensen@example.com",
        "accountStatus": "active",
        "effectiveRoles": [],
        "effectiveAssignments": []
      }
    ],
    "resultCount": 2,
    "pagedResultsCookie": "eyIvX2lkIjoiYm11cnJheSJ9",
    "totalPagedResultsPolicy": "EXACT",
    "totalPagedResults": 22,
    "remainingPagedResults": -1
  }
  ```

  The `totalPagedResults` and `_remainingPagedResults` parameters are not supported for all queries. Where they are not supported, their returned value is always `-1`. In addition, counting query results using these parameters is not currently supported for a PingDS (DS) repository.

  Requesting the total result count (with `_totalPagedResultsPolicy=EXACT`) incurs a performance cost on the query.

  Queries that return large data sets will have a significant impact on heap requirements, particularly if they are run in parallel with other large data requests. To avoid out of memory errors, analyze your data requirements, set the heap configuration appropriately, and modify access controls to restrict requests on large data sets.

## Sort query results

For common filter query expressions, you can sort the results of a query using the `_sortKeys` parameter. This parameter takes a comma-separated list as a value and orders the way in which the JSON result is returned, based on this list.

The `_sortKeys` parameter is not supported for predefined queries.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When using DS as a repo:- Pagination using `_pageSize` is recommended if you intend to use `_sortKeys`. If you do not paginate your query, the data you are querying must be indexed in DS.

- When viewing data that is persisted in DS and sorted by un-indexed `_sortKeys`, the `_pageSize` parameter must be less than or equal to the `index-entry-limit` as configured in DS (default value is 4000).For more information about how to set up indexes in DS, refer to [Indexes](https://docs.pingidentity.com/pingds/8.1/config-guide/indexing.html) in the *DS Configuration Guide*. |

The following query returns all users with the `givenName` Dan, and sorts the results alphabetically, according to surname (`sn`):

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
'http://localhost:8080/openidm/system/ldap/account?_queryFilter=givenName+eq+"Dan"&_fields=givenName,sn&_sortKeys=sn'
{
  "result": [
    {
      "sn": "Cope",
      "givenName": "Dan"
    },
    {
      "sn": "Langdon",
      "givenName": "Dan"
    },
    {
      "sn": "Lanoway",
      "givenName": "Dan"
    }
  ],
  "resultCount": 3,
  "pagedResultsCookie": null,
  "remainingPagedResults": -1
}
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When you query a relationship field, fields that belong to the related object are not available as `_sortKeys`. For example, if you query a list of a manager's reports, you cannot sort by the reports' last names. This is because the available `_sortKeys` are based on the object being queried, which, in the case of [relationships](relationships.html), is actually a list of references to other objects, not the objects themselves. |

## Recalculate virtual property values in queries

For managed objects IDM includes an `onRetrieve` script hook that enables you to recalculate property values when an object is retrieved as the result of a query. To use the `onRetrieve` trigger, the query must include the `executeOnRetrieve` parameter, for example:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
'http://localhost:8080/openidm/managed/user?_queryFilter=sn+eq+"Jensen"&executeOnRetrieve=true'
```

If a query includes `executeOnRetrieve`, the query recalculates virtual property values, based on the current state of the system. The result of the query will be the same as a `read` on a specific object, because reads always recalculate virtual property values.

If a query does not include `executeOnRetrieve`, the query returns the virtual properties of an object, based on the value that is persisted in the repository. Virtual property values are not recalculated.

For performance reasons, `executeOnRetrieve` is `false` by default.

|   |                                                                                                                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Virtual properties that use `queryConfig` for calculation instead of an `onRetrieve` script are not recalculated by `executeOnRetrieve`. These properties are recalculated only when there is a change (such as adding or removing a role affecting `effectiveRoles`, or a temporal constraint being triggered or changed). |

---

---
title: Disable policy enforcement
description: "Temporarily disable PingIDM back-end policy enforcement to import data that doesn't meet validation requirements"
component: pingidm
version: 8.1
page_id: pingidm:objects-guide:disabling-policies
canonical_url: https://docs.pingidentity.com/pingidm/8.1/objects-guide/disabling-policies.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Policy"]
---

# Disable policy enforcement

*Policy enforcement* is the automatic validation of data when it is created, updated, or patched. In certain situations you might want to disable policy enforcement temporarily. You might, for example, want to import existing data that does not meet the validation requirements with the intention of cleaning up this data at a later stage.

You can disable policy enforcement by setting `openidm.policy.enforcement.enabled` to `false` in your `resolver/boot.properties` file. This setting disables policy enforcement in the back-end only, and has no impact on direct policy validation calls to the Policy Service (which the UI makes to validate input fields). So, with policy enforcement disabled, data added directly over REST is not subject to validation, but data added with the UI is still subject to validation.

You should not disable policy enforcement permanently, in a production environment.

---

---
title: Effective roles and effective assignments
description: Understand how PingIDM calculates effective roles and effective assignments as virtual properties using relationship notifications and queryConfig
component: pingidm
version: 8.1
page_id: pingidm:objects-guide:effective-roles-and-assignments
canonical_url: https://docs.pingidentity.com/pingidm/8.1/objects-guide/effective-roles-and-assignments.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Roles", "Assignments", "Virtual Properties"]
---

# Effective roles and effective assignments

*Effective roles* and *effective assignments* are virtual properties of a user object. Their values are calculated by IDM, using relationships between related objects to know when to recalculate when changes occur. The relationships between objects are configured using the `notify`, `notifySelf`, and `notifyRelationships` settings for `managed/user`, `managed/role`, and `managed/assignment`. Which related objects to traverse for calculation is configured using `queryConfig`. Calculation or recalculation is triggered when the roles or assignments for a managed user are added, removed, or changed, including by changes from temporal constraints, and notification of that change is sent to the related objects.

The following excerpt of the managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint, or directly in the conf/managed.json file.)* file shows how these two virtual properties are constructed for each managed user object:

```json
"effectiveRoles" : {
    "type" : "array",
    "title" : "Effective Roles",
    "description" : "Effective Roles",
    "viewable" : false,
    "returnByDefault" : true,
    "isVirtual" : true,
    "queryConfig" : {
        "referencedRelationshipFields" : ["roles"]
    },
    "usageDescription" : "",
    "isPersonal" : false,
    "items" : {
        "type" : "object",
        "title" : "Effective Roles Items"
    }
},
"effectiveAssignments" : {
    "type" : "array",
    "title" : "Effective Assignments",
    "description" : "Effective Assignments",
    "viewable" : false,
    "returnByDefault" : true,
    "isVirtual" : true,
    "queryConfig" : {
        "referencedRelationshipFields" : ["roles", "assignments"],
        "referencedObjectFields" : ["*"]
    },
    "usageDescription" : "",
    "isPersonal" : false,
    "items" : {
        "type" : "object",
        "title" : "Effective Assignments Items"
    }
}
```

When a role references an assignment, and a user references the role, that user automatically references the assignment in its list of effective assignments.

`effectiveRoles` uses the `roles` relationship to calculate the grants that are currently in effect, including any qualified by temporal constraints.

`effectiveAssignments` uses the `roles` relationship, and the `assignments` relationship for each role, to calculate the current assignments in effect for that user. The synchronization engine reads the calculated value of the `effectiveAssignments` attribute when it processes the user. The target system is updated according to the configured `assignmentOperation` for each assignment.

When a user's roles or assignments are updated, IDM calculates the `effectiveRoles` and `effectiveAssignments` for that user based on the current value of the user's `roles` property, and the `assignments` property of any roles referenced by the `roles` property. The previous set of examples showed the creation of a role `employee` that referenced an assignment `employee` and was granted to user bjensen. Querying that user entry would show the following effective roles and effective assignments:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"http://localhost:8080/openidm/managed/user/bjensen?_fields=userName,roles,effectiveRoles,effectiveAssignments"
{
  "_id": "ca8855fd-a404-42c7-88b7-02f8a8a825b2",
  "_rev": "0000000081eebe1a",
  "userName": "bjensen",
  "effectiveRoles": [
    {
      "_refResourceCollection": "managed/role",
      "_refResourceId": "2243f5f8-ed75-4c3b-b4b3-058d5c58fbb4"
      "_ref": "managed/role/2243f5f8-ed75-4c3b-b4b3-058d5c58fbb4"
    }
  ],
  "effectiveAssignments": [
    {
      "name": "employee",
      "description": "Assignment for employees.",
      "mapping": "managedUser_systemLdapAccounts",
      "attributes": [
        {
          "assignmentOperation": "mergeWithTarget",
          "name": "employeeType",
          "unassignmentOperation": "removeFromTarget",
          "value": [
            "employee"
          ]
        }
      ],
      "_rev": "0000000087d5a9a5",
      "_id": "46befacf-a7ad-4633-864d-d93abfa561e9"
      "_refResourceCollection": "managed/assignment",
      "_refResourceId": "46befacf-a7ad-4633-864d-d93abfa561e9",
      "_ref": "managed/assignment/46befacf-a7ad-4633-864d-d93abfa561e9"
    }
  ],
  "roles": [
    {
      "_ref": "managed/role/2243f5f8-ed75-4c3b-b4b3-058d5c58fbb4",
      "_refResourceCollection": "managed/role",
      "_refResourceId": "2243f5f8-ed75-4c3b-b4b3-058d5c58fbb4",
      "_refProperties": {
        "_id": "93552530-10fa-49a4-865f-c942dffd2801",
        "_rev": "0000000081ed9f2b"
      }
    }
  ]
}
```

In this example, synchronizing the managed/user repository with the external LDAP system defined in the mapping populates user bjensen's `employeeType` attribute in LDAP with the value `employee`.

---

---
title: Extend the policy service
description: Extend the PingIDM policy service with custom scripted policies and conditional policy definitions applied to managed or other objects
component: pingidm
version: 8.1
page_id: pingidm:objects-guide:extending-policies
canonical_url: https://docs.pingidentity.com/pingidm/8.1/objects-guide/extending-policies.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Policy", "Scripts"]
section_ids:
  custom-scripted-policies: Add custom scripted policies
  conditional-policy-definitions: Add conditional policy definitions
---

# Extend the policy service

You can extend the policy service by adding custom scripted policies, and by adding policies that are applied only under certain conditions.

## Add custom scripted policies

If your deployment requires additional validation functionality that is not supplied by the default policies, you can add your own policy scripts to your project's `script` directory, and reference them in your project's policy configuration *(tooltip: You can edit the policy configuration over REST at the config/policy endpoint, or directly in the conf/policy.json file.)*.

Do not modify the default policy script file (`openidm/bin/defaults/script/policy.js`) as doing so might result in interoperability issues in a future release.

To reference additional policy scripts, set the `additionalFiles` property in you policy configuration *(tooltip: You can edit the policy configuration over REST at the config/policy endpoint, or directly in the conf/policy.json file.)*.

The following example creates a custom policy that rejects properties with null values. The policy is defined in a script named `mypolicy.js`:

```javascript
var policy = {   "policyId" : "notNull",
       "policyExec" : "notNull",
       "policyRequirements" : ["NOT_NULL"]
}

addPolicy(policy);

function notNull(fullObject, value, params, property) {
   if (value == null) {
      var requireNotNull = [
        {"policyRequirement": "NOT_NULL"}
      ];
      return requireNotNull;
   }
   return [];
}
```

The `mypolicy.js` policy is referenced in the `policy.json` configuration file as follows:

```json
{
    "type" : "text/javascript",
    "file" : "policy.js",
    "additionalFiles" : ["script/mypolicy.js"],
    "resources" : [
        {
            ...
        }
    ]
}
```

|   |                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | In cases where you are using the admin UI, both `policy.js` and `mypolicy.js` will be run within the client, and then again by the the server. When creating new policies, be aware that these policies may be run in both contexts. |

## Add conditional policy definitions

You can extend the policy service to support policies that are applied only under specific conditions. To apply a conditional policy to managed objects, add the policy to your project's managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint, or directly in the conf/managed.json file.)*. To apply a conditional policy to other objects, add it to your project's policy configuration *(tooltip: You can edit the policy configuration over REST at the config/policy endpoint, or directly in the conf/policy.json file.)*.

The following managed object configuration shows a sample conditional policy for the `password` property of managed user objects. The policy indicates that sys-admin users have a more lenient password policy than regular employees:

```json
{
    "objects" : [
        {
            "name" : "user",
            ...
                "properties" : {
                ...
                    "password" : {
                        "title" : "Password",
                        "type" : "string",
                        ...
                        "conditionalPolicies" : [
                            {
                                "condition" : {
                                    "type" : "text/javascript",
                                    "source" : "(fullObject.org === 'sys-admin')"
                                },
                                "dependencies" : [ "org" ],
                                "policies" : [
                                    {
                                        "policyId" : "max-age",
                                        "params" : {
                                            "maxDays" : ["90"]
                                        }
                                    }
                                ]
                            },
                            {
                                "condition" : {
                                    "type" : "text/javascript",
                                    "source" : "(fullObject.org === 'employees')"
                                },
                                "dependencies" : [ "org" ],
                                "policies" : [
                                    {
                                        "policyId" : "max-age",
                                        "params" : {
                                            "maxDays" : ["30"]
                                        }
                                    }
                                ]
                            }
                        ],
                        "fallbackPolicies" : [
                            {
                                "policyId" : "max-age",
                                "params" : {
                                    "maxDays" : ["7"]
                                }
                            }
                        ]
                    }
                    ...
}
```

To understand how a conditional policy is defined, examine the components of this sample policy. For more information on the policy function, refer to [Policy Implementation Functions](configuring-default-policy.html#policy-function).

There are two distinct scripted conditions (defined in the `condition` elements). The first condition asserts that the user object, contained in the `fullObject` argument, is a member of the `sys-admin` org. If that assertion is true, the `max-age` policy is applied to the `password` attribute of the user object, and the maximum number of days that a password may remain unchanged is set to `90`.

The second condition asserts that the user object is a member of the `employees` org. If that assertion is true, the `max-age` policy is applied to the `password` attribute of the user object, and the maximum number of days that a password may remain unchanged is set to `30`.

In the event that neither condition is met (the user object is not a member of the `sys-admin` org or the `employees` org), an optional fallback policy can be applied. In this example, the fallback policy also references the `max-age` policy and specifies that for such users, their password must be changed after 7 days.

The `dependencies` field prevents the condition scripts from being run at all, if the user object does not include an `org` attribute.

|   |                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This example assumes that a custom `max-age` policy validation function has been defined, as described in [Add Custom Scripted Policies](#custom-scripted-policies). |

---

---
title: Grant relationships conditionally
description: Configure PingIDM conditional relationships to dynamically grant membership based on query filter conditions defined in the managed object schema
component: pingidm
version: 8.1
page_id: pingidm:objects-guide:conditional-relationships
canonical_url: https://docs.pingidentity.com/pingidm/8.1/objects-guide/conditional-relationships.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Relationships"]
---

# Grant relationships conditionally

Relationships can be granted dynamically, based on a specified condition. In order to conditionally grant a relationship, the schemas for the resources you are creating a relationship between need to be configured to support conditional association. To do this, three fields in the schema are used:

* `conditionalAssociation`

  Boolean. This property is applied to the `resourceCollection` for the grantor of the relationship. For example, the `members` relationship on `managed/role` specifies that there is a conditional association with the `managed/user` resource:

  ```json
  "resourceCollection" : [
      {
          "notify" : true,
          "conditionalAssociation" : true,
          "path" : "managed/user",
          "label" : "User",
          "query" : {
              "queryFilter" : "true",
              "fields" : [
                  "userName",
                  "givenName",
                  "sn"
              ]
          }
      }
  ]
  ```

* `conditionalAssociationField`

  This property is a string, specifying the field used to determine whether a conditional relationship is granted. The field is applied to the `resourceCollection` of the grantee of the relationship. For example, the `roles` relationship on `managed/user` specifies that the conditional association with `managed/role` is defined by the `condition` field in `managed/role`:

  ```json
  "resourceCollection" : [
      {
          "path" : "managed/role",
          "label" : "Role",
          "conditionalAssociationField" : "condition",
          "query" : {
              "queryFilter" : "true",
              "fields" : [
                  "name"
              ]
          }
      }
  ]
  ```

  The field name specified will usually be `condition` if you are using default schema, but can be any field that evaluates a condition and has been flagged as `isConditional`.

* `isConditional`

  Boolean. This is applied to the field you wish to check to determine whether membership in a relationship is granted. Only one field on a resource can be marked as `isConditional`. For example, in the relationship between `managed/user` and `managed/role`, conditional membership in the relationship is determined by the query filter specified in the `managed/role` `condition` field:

  ```json
  "condition" : {
      "description" : "A conditional filter for this role",
      "title" : "Condition",
      "viewable" : false,
      "searchable" : false,
      "isConditional" : true,
      "type" : "string"
  }
  ```

Conditions support both properties and [virtual properties derived from other relationships](managed-object-virtual-properties.html#relationship-derived-virtual-properties), if the query property has been configured. Conditions are a powerful tool for dynamically creating relationships between two objects. An example of conditional relationships in use is covered in [Grant a Role Based on a Condition](roles-over-rest.html#conditional-role-grants).

---

---
title: Links
description: Reference for PingIDM link objects, which define relations between source and target objects established during provisioning or reconciliation
component: pingidm
version: 8.1
page_id: pingidm:objects-guide:appendix-links
canonical_url: https://docs.pingidentity.com/pingidm/8.1/objects-guide/appendix-links.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model"]
---

# Links

Link objects define relations between source objects and target objects, usually relations between managed objects and system objects. The link relationship is established by provisioning activity that either results in a new account on a target system, or a reconciliation or synchronization scenario that takes a `LINK` action.

---

---
title: Manage custom relationship properties
description: Create and configure custom relationship properties between PingIDM managed objects using the admin UI, including cardinality and deletion considerations
component: pingidm
version: 8.1
page_id: pingidm:objects-guide:relationships-custom
canonical_url: https://docs.pingidentity.com/pingidm/8.1/objects-guide/relationships-custom.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Relationships"]
page_aliases: ["release-notes:rapid-channel/custom-relationships-schema.adoc"]
section_ids:
  create_a_custom_relationship_property: Create a custom relationship property
  update_a_custom_relationship: Update a custom relationship
  delete_a_custom_relationship_property: Delete a custom relationship property
---

# Manage custom relationship properties

Custom relationship properties allow you to define custom relationships between managed objects. For example, you could model a parent-child relationship by creating the `custom_Parents` and `custom_Children` properties and configuring them as one-way one-to-many relationships.

## Create a custom relationship property

To create a custom relationship property using the admin UI:

1. From the top navigation menu, click Configure > Managed Objects.

2. Select a managed object type.

3. Click Add a Property. An entry field displays.

4. In the Name field, enter a name for the custom relationship property.

5. From the Type drop-down, select Relationship.

6. Click Next. The Add Resources modal displays.

7. From the Resource drop-down, select the resource to map the custom relationship property to.

8. From the Display Properties drop-down, select the properties on the resource to map to the custom relationship property.

9. Click Save. The Relationships Property screen for the new relationship property displays.

|   |                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Objects are limited to 10 custom relationships. If you need an object to have more, create custom relationships from the related object and map them to the original object. |

## Update a custom relationship

You can adjust a custom relationship's **cardinality** by configuring each side of the relationship to be have one, many, or none of the other side. For instance, `custom_Managers` may have many `custom_Employees`, while `custom_Employees` have only one `custom_Managers`.

To change the cardinality of a custom relationship using the admin UI:

1. From the top navigation menu, click Configure > Managed Objects.

2. Click the managed object type which has the relationship property to modify.

3. Click the relationship property to modify.

4. In the Relationship Configuration section, click the cardinality relationship name associated with the arrow indicating the direction of the relationship. A popover displays.

5. From the Relationship drop-down on the popover, select the cardinality of the relationship. The Changes Pending notification displays in the lower left of the UI.

6. Click Save.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When you change the configuration of a custom relationship, existing objects which contain that custom relationship are not automatically updated to match the new configuration. Ensure your data is updated to reflect the new relationship configuration.For example, suppose `custom_Doctors` have many `custom_Patients` and `custom_Patients` have many `custom_Doctors`. The rules change and now `custom_Patients` have one `custom_Doctor`. In addition to updating the custom relationship's cardinality in the configuration, you must also update all existing `custom_Patients` with more than one `custom_Doctor` to have at most one. |

### Delete a custom relationship property

Existing objects are not automatically updated when you delete a custom relationship property. When you delete a custom relationship property, you must also update the existing objects to no longer reference them. Failing to do this may result in the "orphaned" data unpredictably reappearing if PingIDM reuses the deleted reference attribute for other data.

Before you delete a custom relationship property, find all of the managed objects which are in the custom relationship and either modify or delete the data. The following REST API query returns all managed users with the property `custom_Example`:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=2.0" \
--request GET \
"https://localhost:8443/openidm/managed/user?_queryFilter=/custom_Example+pr&_pageSize=30"
```

For more information on using the REST API to manage custom relationship properties, refer to [Schema](../rest-api-reference/endpoints/rest-schema.html).

---

---
title: Manage organizations over REST
description: Create, manage, and delete PingIDM organizations, owners, admins, members, and child organizations using the REST interface
component: pingidm
version: 8.1
page_id: pingidm:objects-guide:manage-orgs-rest
canonical_url: https://docs.pingidentity.com/pingidm/8.1/objects-guide/manage-orgs-rest.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Organizations"]
---

# Manage organizations over REST

IDM provides RESTful access to managed organizations, at the context path `/openidm/managed/organization`. You can add, change, and delete organizations by using the admin UI or over the REST interface. To use the admin UI, select Manage > Organization.

The following examples show how to add, change, and delete organizations over the REST interface. For a reference of all managed organization endpoints and actions, refer to [Managed organizations](../rest-api-reference/endpoints/rest-managed-organizations.html).

You can also use the [REST API Explorer](../rest-api-reference/api-explorer.html) as a reference to the managed object REST API.

> **Collapse: Add an organization**
>
> Only IDM administrators can create top level organizations.
>
> ```
> curl \
> --header "Content-Type: application/json" \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Accept-API-Version: resource=1.0" \
> --header "If-None-Match: *" \
> --request PUT \
> --data '{
>   "name": "example-org"
> }' \
> "http://localhost:8080/openidm/managed/organization/example-org"
> {
>   "_id": "example-org",
>   "_rev": "00000000bc9871c8",
>   "adminIDs": [],
>   "ownerIDs": [],
>   "parentAdminIDs": [],
>   "parentIDs": [],
>   "parentOwnerIDs": [],
>   "name": "example-org"
> }
> ```

> **Collapse: Add an organization owner**
>
> IDM administrators can create owners for an organization. This example makes bjensen the owner of the organization created previously. The example assumes that the managed user bjensen already exists:
>
> ```
> curl \
> --header "Content-Type: application/json" \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Accept-API-Version: resource=1.0" \
> --request POST \
> --data '{"_ref":"managed/user/bjensen"}' \
> "http://localhost:8080/openidm/managed/organization/example-org/owners?_action=create"
> {
>   "_id": "fcb0f4d0-dad2-4138-a80c-62407a8e831e",
>   "_rev": "00000000496d9920",
>   "_ref": "managed/user/bjensen",
>   "_refResourceCollection": "managed/user",
>   "_refResourceId": "bjensen",
>   "_refProperties": {
>     "_id": "fcb0f4d0-dad2-4138-a80c-62407a8e831e",
>     "_rev": "00000000496d9920"
>   }
> }
> ```

> **Collapse: List an owner's organizations**
>
> This example lists the organizations of which bjensen is an owner:
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Accept-API-Version: resource=1.0" \
> --request GET \
> "http://localhost:8080/openidm/managed/user/bjensen/ownerOfOrg?_queryFilter=true"
> {
>   "result": [
>     {
>       "_id": "fcb0f4d0-dad2-4138-a80c-62407a8e831e",
>       "_rev": "00000000496d9920",
>       "_ref": "managed/organization/example-org",
>       "_refResourceCollection": "managed/organization",
>       "_refResourceId": "example-org",
>       "_refProperties": {
>         "_id": "fcb0f4d0-dad2-4138-a80c-62407a8e831e",
>         "_rev": "00000000496d9920"
>       }
>     }
>   ],
>   ...
> }
> ```

> **Collapse: Add an organization member**
>
> Organization owners can create members in the organizations that they own. In this example bjensen creates user scarter and makes him a member of the organization created previously:
>
> ```
> curl \
> --header "Content-Type: application/json" \
> --header "X-OpenIDM-Username: bjensen" \
> --header "X-OpenIDM-Password: Th3Password" \
> --header "Accept-API-Version: resource=1.0" \
> --request PUT \
> --data '{
>   "userName": "scarter",
>   "sn": "Carter",
>   "givenName": "Steven",
>   "mail": "scarter@example.com",
>   "password": "Th3Password",
>   "memberOfOrg": [{"_ref": "managed/organization/example-org"}]
> }' \
> "http://localhost:8080/openidm/managed/user/scarter"
> {
>   "_id": "scarter",
>   "_rev": "00000000eac81c23"
> }
> ```

> **Collapse: List the members of an organization**
>
> Organization owners can view the members of the organizations that they own. In this example, bjensen lists the members of example-org:
>
> ```
> curl \
> --header "X-OpenIDM-Username: bjensen" \
> --header "X-OpenIDM-Password: Th3Password" \
> --header "Accept-API-Version: resource=1.0" \
> --request GET \
> "http://localhost:8080/openidm/managed/organization/example-org/members?_queryFilter=true"
> {
>   "result": [
>     {
>       "_id": "b71e8dd9-6224-466f-9630-4358a69c69fd",
>       "_rev": "0000000038ea999e",
>       "_ref": "managed/user/scarter",
>       "_refResourceCollection": "managed/user",
>       "_refResourceId": "scarter",
>       "_refProperties": {
>         "_id": "b71e8dd9-6224-466f-9630-4358a69c69fd",
>         "_rev": "0000000038ea999e"
>       }
>     }
>   ],
>   ...
> }
> ```

> **Collapse: Add an organization admin**
>
> Organization owners can create admins of the organizations that they own. An organization admin must be a member of the organization. In this example, bjensen makes scarter an admin of example-org:
>
> ```
> curl \
> --header 'Content-Type: application/json' \
> --header "Accept-API-Version: resource=1.0" \
> --header 'X-OpenIDM-Username: bjensen' \
> --header 'X-OpenIDM-Password: Th3Password' \
> --request PATCH \
> --data '[
>     {
>         "operation": "add",
>         "field": "/admins/-",
>         "value": {
>             "_ref": "managed/user/scarter"
>         }
>     }
> ]' \
> "http://localhost:8080/openidm/managed/organization/example-org"
> {
>   "_id": "example-org",
>   "_rev": "000000009c248a4a",
>   "adminIDs": [
>     "scarter"
>   ],
>   "ownerIDs": [
>     "bjensen"
>   ],
>   "parentAdminIDs": [],
>   "parentIDs": [],
>   "parentOwnerIDs": [],
>   "name": "example-org"
> }
> ```

> **Collapse: List an admin's organizations**
>
> An organization owner or admin can only access the organizations that they own or administer. In this example, the admin scarter lists the organizations, and accesses only those of which they are an admin:
>
> ```
> curl \
> --header "X-OpenIDM-Username: scarter" \
> --header "X-OpenIDM-Password: Th3Password" \
> --header "Accept-API-Version: resource=1.0" \
> --request GET \
> "http://localhost:8080/openidm/managed/organization?_queryFilter=true"
> {
>   "result": [
>     {
>       "_id": "example-org",
>       "_rev": "000000009c248a4a",
>       "adminIDs": [
>         "scarter"
>       ],
>       "ownerIDs": [
>         "bjensen"
>       ],
>       "parentAdminIDs": [],
>       "parentIDs": [],
>       "parentOwnerIDs": [],
>       "name": "example-org"
>     }
>   ],
>   ...
> }
> ```

> **Collapse: Add a member as an organization admin**
>
> Organization admins can also add members to the organizations they administer. In this example, the organization admin, scarter, creates a new member, jsanchez, and makes her a member of example-org:
>
> ```
> curl \
> --header "Content-Type: application/json" \
> --header "X-OpenIDM-Username: scarter" \
> --header "X-OpenIDM-Password: Th3Password" \
> --header "Accept-API-Version: resource=1.0" \
> --request PUT \
> --data '{
>   "userName": "jsanchez",
>   "sn": "Sanchez",
>   "givenName": "Juanita",
>   "mail": "jsanchez@example.com",
>   "password": "Th3Password",
>   "memberOfOrg": [{"_ref": "managed/organization/example-org"}]
> }' \
> "http://localhost:8080/openidm/managed/user/jsanchez"
> {
>   "_id": "jsanchez",
>   "_rev": "00000000f9341bd6"
> }
> ```

> **Collapse: List a member's organizations**
>
> Organization owners and admins can list the organizations of which a user is a member, as long as those organizations are owned or administrated by them. In this example, scarter lists the organizations of which jsanchez is a member:
>
> ```
> curl \
> --header "X-OpenIDM-Username: scarter" \
> --header "X-OpenIDM-Password: Th3Password" \
> --header "Accept-API-Version: resource=1.0" \
> --request GET \
> "http://localhost:8080/openidm/managed/user/jsanchez?_fields=memberOfOrg"
> {
>   "_id": "jsanchez",
>   "_rev": "00000000f9341bd6",
>   "memberOfOrg": [
>     {
>       "_ref": "managed/organization/example-org",
>       "_refResourceCollection": "managed/organization",
>       "_refResourceId": "example-org",
>       "_refProperties": {
>         "_id": "078d14b2-e5f1-4b21-9801-041138e691f4",
>         "_rev": "00000000ac2e9927"
>       }
>     }
>   ]
> }
> ```

The organization established by the previous set of examples can be represented as follows:

![example-org](_images/example-org.png)

In this organization, both bjensen and scarter can create and delete sub-organizations, also known as *child organizations*, of example-org, and can create and delete members within these child organizations.

The following example shows how to add and delete child organizations over the REST interface:

> **Collapse: Add a child organization**
>
> Organization owners and admins can create and manage child organizations of the organizations that they own or administer. In this example, the organization owner, bjensen, creates a new organization named `example-child-org`, and makes it a child organization of `example-org`:
>
> ```
> curl \
> --header "Content-Type: application/json" \
> --header "X-OpenIDM-Username: bjensen" \
> --header "X-OpenIDM-Password: Th3Password" \
> --header "Accept-API-Version: resource=1.0" \
> --header "If-None-Match: *" \
> --request PUT \
> --data '{
>   "name": "example-child-org",
>   "parent": {"_ref": "managed/organization/example-org"}
> }' \
> "http://localhost:8080/openidm/managed/organization/example-child-org"
> {
>   "_id": "example-child-org",
>   "_rev": "00000000db852a9d"
> }
> ```
>
> |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
> | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | The organization model is based on [delegated administration](../auth-guide/delegated-admin.html). As with delegated administration, you cannot explicitly change the relationship endpoints. So, for example, so you cannot create, update, delete, or patch relationship edges. The following type of request is therefore *not possible* with the organization model:```
> curl \
> --header "Content-Type: application/json" \
> --header "X-OpenIDM-Username: bjensen" \
> --header "X-OpenIDM-Password: Th3Password" \
> --header "Accept-API-Version: resource=1.0" \
> --header "If-None-Match: *" \
> --request PUT \
> --data '{
> "name": "example-child-org",
> "parent": {"_ref": "managed/organization/example-org"}
> }' \
> "http://localhost:8080/openidm/managed/organization/children?_action=create"
> ``` |

> **Collapse: List an owner's organizations and child organzations**
>
> Organization owners and admins have access to any organizations that are *child* organizations of their own orgs. In this example, admin scarter lists his visible organizations again:
>
> ```
> curl \
> --header "X-OpenIDM-Username: scarter" \
> --header "X-OpenIDM-Password: Th3Password" \
> --header "Accept-API-Version: resource=1.0" \
> --request GET \
> "http://localhost:8080/openidm/managed/organization?_queryFilter=true"
> {
>   "result": [
>     {
>       "_id": "example-org",
>       "_rev": "000000009c248a4a",
>       "adminIDs": [
>         "scarter"
>       ],
>       "ownerIDs": [
>         "bjensen"
>       ],
>       "parentAdminIDs": [],
>       "parentIDs": [],
>       "parentOwnerIDs": [],
>       "name": "example-org"
>     },
>     {
>       "_id": "example-child-org",
>       "_rev": "00000000db852a9d",
>       "adminIDs": [],
>       "ownerIDs": [],
>       "parentAdminIDs": [
>         "scarter"
>       ],
>       "parentIDs": [
>         "example-org"
>       ],
>       "parentOwnerIDs": [
>         "bjensen"
>       ],
>       "name": "example-child-org"
>     }
>   ],
>   ...
> }
> ```
>
> Notice that scarter can now access the example-child-org that bjensen created in the previous example.

---

---
title: Manage policies over REST
description: List, validate, and manage PingIDM policies over the REST interface at the openidm/policy endpoint for objects and individual properties
component: pingidm
version: 8.1
page_id: pingidm:objects-guide:policies-over-REST
canonical_url: https://docs.pingidentity.com/pingidm/8.1/objects-guide/policies-over-REST.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Policy", "REST API"]
section_ids:
  listing-policies: List the defined policies
  policy-validate: Validate objects and properties over REST
  validate_field_removal: Validate field removal
  force-validation-default-values: Force validation of default values
  validate-props-unknown-resources: Validate properties to unknown resource paths
  pre_registration_validation_example: Pre-registration validation example
---

# Manage policies over REST

Manage the policy service over the REST interface at the `openidm/policy` endpoint.

## List the defined policies

The following REST call displays a list of all the policies defined in `policy.json` (policies for objects other than managed objects). The policy objects are returned in JSON format, with one object for each defined policy ID:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"http://localhost:8080/openidm/policy"
{
  "_id": "",
  "resources": [
    ...
    {
      "resource": "internal/user/*",
      "properties": [
        {
          "name": "_id",
          "policies": [
            {
              "policyId": "cannot-contain-characters",
              "params": {
                "forbiddenChars": [ "/" ]
              },
              "policyFunction": "\nfunction (fullObject, value, params, property) {\n    ...",
              "policyRequirements": [
                "CANNOT_CONTAIN_CHARACTERS"
              ]
            }
          ],
          "policyRequirements": [
            "CANNOT_CONTAIN_CHARACTERS"
          ]
        }
        ...
      ]
      ...
    }
  ]
}
```

To display the policies that apply to a specific resource, include the resource name in the URL. For example, the following REST call displays the policies that apply to managed users:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"http://localhost:8080/openidm/policy/managed/user/*"
{
  "_id": "*",
  "resource": "managed/user/*",
  "properties": [
    {
      "policyRequirements": [
        "VALID_TYPE",
        "CANNOT_CONTAIN_CHARACTERS"
      ],
      "fallbackPolicies": null,
      "name": "_id",
      "policies": [
        {
          "policyRequirements": [
            "VALID_TYPE"
          ],
          "policyId": "valid-type",
          "params": {
            "types": [
              "string"
            ]
          }
        },
        {
          "policyId": "cannot-contain-characters",
          "params": {
            "forbiddenChars": [ "/" ]
          },
          "policyFunction": "...",
          "policyRequirements": [
            "CANNOT_CONTAIN_CHARACTERS"
          ]
        }
      ],
      "conditionalPolicies": null
    }
    ...
  ]
}
```

## Validate objects and properties over REST

To verify that an object adheres to the requirements of all applied policies, include the `validateObject` action in the request.

The following example verifies that a new managed user object is acceptable, in terms of the policy requirements. Note that the ID in the URL (`test` in this example) is ignored—the action simply validates the object in the JSON payload:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request POST \
--data '{
  "sn": "Jones",
  "givenName": "Bob",
  "telephoneNumber": "0827878921",
  "passPhrase": null,
  "mail": "bjones@example.com",
  "accountStatus": "active",
  "userName": "bjones@example.com",
  "password": "123"
}' \
"http://localhost:8080/openidm/policy/managed/user/test?_action=validateObject"
{
  "result": false,
  "failedPolicyRequirements": [
    {
      "policyRequirements": [
        {
          "policyRequirement": "MIN_LENGTH",
          "params": {
            "minLength": 8
          }
        }
      ],
      "property": "password"
    },
    {
      "policyRequirements": [
        {
          "policyRequirement": "AT_LEAST_X_CAPITAL_LETTERS",
          "params": {
            "numCaps": 1
          }
        }
      ],
      "property": "password"
    }
  ]
}
```

The result (`false`) indicates that the object is not valid. The unfulfilled policy requirements are provided as part of the response - in this case, the user password does not meet the validation requirements.

Use the `validateProperty` action to verify that a specific property adheres to the requirements of a policy.

The following example checks whether a user's new password (`12345`) is acceptable:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request POST \
--data '{
  "password": "12345"
}' \
"http://localhost:8080/openidm/policy/managed/user/9dce06d4-2fc1-4830-a92b-bd35c2f6bcbb?_action=validateProperty"
{
  "result": false,
  "failedPolicyRequirements": [
    {
      "policyRequirements": [
        {
          "policyRequirement": "MIN_LENGTH",
          "params": {
            "minLength": 8
          }
        }
      ],
      "property": "password"
    },
    {
      "policyRequirements": [
        {
          "policyRequirement": "AT_LEAST_X_CAPITAL_LETTERS",
          "params": {
            "numCaps": 1
          }
        }
      ],
      "property": "password"
    }
  ]
}
```

The result (`false`) indicates that the password is not valid. The unfulfilled policy requirements are provided as part of the response - in this case, the minimum length and the minimum number of capital letters.

Validating a property that fulfills the policy requirements returns a `true` result, for example:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request POST \
--data '{
  "password": "1NewPassword"
}' \
"http://localhost:8080/openidm/policy/managed/user/9dce06d4-2fc1-4830-a92b-bd35c2f6bcbb?_action=validateProperty"
{
  "result": true,
  "failedPolicyRequirements": []
}
```

### Validate field removal

To validate field removal, specify the fields to remove when calling the policy `validateProperty` action. You cannot remove fields that:

* Are required in the `required` schema array.

* Have a `required` policy.

* Have a default value.

The following example validates the removal of the fields `description` and `givenName`:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request POST \
--data '{
  "_remove": [ "description", "givenName" ]
}' \
"http://localhost:8080/openidm/policy/managed/user/ca5a3196-2ed3-4a76-8881-30403dee70e9?_action=validateProperty"
```

Because `givenName` is a required field, IDM returns a failed policy validation:

```json
{
  "result": false,
  "failedPolicyRequirements": [
    {
      "policyRequirements": [
        {
          "policyRequirement": "REQUIRED"
        }
      ],
      "property": "givenName"
    }
  ]
}
```

### Force validation of default values

IDM does not perform policy validation for default values specified in the managed objects schema. It may be necessary to force validation when validating properties for an object that does not yet exist. To force validation, include `forceValidate=true` in the request URL.

### Validate properties to unknown resource paths

To perform a `validateProperty` action to a path that is unknown (`*`), such as `managed/user/*` or `managed/user/userDoesntExistYet`, the payload must include:

* An `object` field that contains the object details.

* A `properties` field that contains the properties to be evaluated.

#### Pre-registration validation example

A common use case for validating properties for unknown resources is prior to object creation, such as during pre-registration.

1. Always pass the object and properties content in the POST body because IDM has no object to look up.

2. Use any placeholder id in the request URL, as `*` has no special meaning in the API.

   This example uses a conditional policy for any object with the description `test1`:

   ```json
   "password" : {
       ...
       "conditionalPolicies" : [
           {
               "condition" : {
                   "type" : "text/javascript",
                   "source" : "(fullObject.description === 'test1')"
               },
               "dependencies" : [ "description" ],
               "policies" : [
                   {
                       "policyId" : "at-least-X-capitals",
                       "params" : {
                           "numCaps" : 1
                       }
                   }
               ]
           }
       ],
   ```

3. Using the above conditional policy, you could perform a `validateProperty` action to `managed/user/*` with the request:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --header "Content-Type: application/json" \
   --request POST \
   --data '{
     "object": {
       "description": "test1"
     },
     "properties": {
       "password": "passw0rd"
     }
   }' \
   "http://localhost:8080/openidm/policy/managed/user/*?_action=validateProperty"
   {
     "result": false,
     "failedPolicyRequirements": [
       {
         "policyRequirements": [
           {
             "params": {
               "numCaps": 1
             },
             "policyRequirement": "AT_LEAST_X_CAPITAL_LETTERS"
           }
         ],
         "property": "password"
       }
     ]
   }
   ```