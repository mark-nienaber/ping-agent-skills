---
title: Access data objects
description: Access managed objects through scripts, REST, remote proxies, and queries
component: pingoneaic
page_id: pingoneaic:idm-objects:access-data-objects-preface
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-objects/access-data-objects-preface.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model"]
---

# Access data objects

Advanced Identity Cloud gives you the ability to access three types of data objects so you can seamlessly manage your users, control platform behavior, and interact with the underlying database storage:

* **Managed objects (for identity orchestration):** Access these objects to create, update, or query user accounts, device profiles, and group relationships. This is the primary layer used by your sync mappings and workflows to automate the lifecycle of identities.

* **Configuration objects (for DevOps and automation):** Access these objects to programmatically read or modify platform settings, authentication journeys, and connector definitions. This allows you to manage your identity configuration as code, enabling automated backups and migration between test and production environments.

* **Repository objects (for low-level auditing and data parity):** Access these objects to directly interact with the persistent database layer behind the platform. This is critical when you need to perform deep data troubleshooting, structural auditing, or mass data operations that bypass standard workflow logic.

Advanced Identity Cloud standardizes the objects through a uniform programming model. This model uses the Resource API to query and manipulate all objects. The URL or URI that is used to identify the target object for an operation depends on the [object type](appendix-objects.html).

You can access data objects in the following ways:

* Access data objects using [scripts](data-scripts.html)

* Access data objects using [REST](data-rest.html)

  * [Query](queries.html) data objects

* Access data objects (between two Advanced Identity Cloud tenants or between an Advanced Identity Cloud tenant and a PingIDM instance) using a [remote proxy](remote-proxy.html).

---

---
title: Access data objects using scripts
description: Access data objects through the Resource API in inline and standalone scripts
component: pingoneaic
page_id: pingoneaic:idm-objects:data-scripts
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-objects/data-scripts.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Scripts"]
---

# Access data objects using scripts

PingIDM gives you the ability to access various data objects (such as managed objects, configuration objects, repository objects and so on) and perform actions (functions) through inline scripts. Advanced Identity Cloud standardizes the objects through a uniform programming model.

For more information about scripts and the objects available to scripts, refer to [Scripting](../idm-scripting/preface.html).

You can use the Resource API to obtain managed, system, configuration, and repository objects, as follows:

```javascript
val = openidm.read("managed/realm-name_organization/mysampleorg")
val = openidm.read("system/mysystem/account")
val = openidm.read("config/custom/mylookuptable")
val = openidm.read("repo/custom/mylookuptable")
```

For information about constructing an object ID, refer to [URI Scheme](../idm-rest-api/rest-structure.html#rest-uri-scheme).

For information on all the actions you can take on a resource, refer to [scripting functions](../idm-scripting/scripting-func-engine.html).

---

---
title: Access data objects using the REST API
description: Access managed objects through the REST API using HTTP requests
component: pingoneaic
page_id: pingoneaic:idm-objects:data-rest
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-objects/data-rest.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "REST API"]
---

# Access data objects using the REST API

PingIDM provides access to data objects through the Advanced Identity Cloud REST API. To access objects over REST, you can use a browser-based REST client, such as the *Simple REST Client* for Chrome or *RESTClient* for Firefox. Alternatively, you can use the [curl](https://curl.se/) command-line utility.

Refer to the [REST API](../idm-rest-api/preface.html) for a comprehensive overview.

To obtain a managed object through the REST API, perform an HTTP GET on the corresponding URL; for example:

```
https://<tenant-env-fqdn>/openidm/managed/realm-name_organization/mysampleorg
```

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | Performing an HTTP GET on the corresponding URL is dependent on your security settings and authentication configuration. |

By default, the HTTP GET returns a JSON representation of the object.

In general, you can map any HTTP request to the corresponding `openidm.method` call. For more information, refer to [script functions](../idm-scripting/scripting-func-engine.html).

The following example shows how the parameters provided in an `openidm.query` request correspond with the key-value pairs you would include in a similar HTTP GET request. It shows the same call using the Resource API and the REST API:

* Resource API

* REST API

Reading an object using the Resource API:

```javascript
openidm.query("managed/realm-name_user", { "_queryFilter": "true" }, ["userName","sn"])
```

Reading an object using the REST API:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/managed/realm-name_user?_queryFilter=true&_fields=userName,sn"
```

---

---
title: Apply policies to managed objects
description: Apply validation policies to managed object properties to enforce constraints
component: pingoneaic
page_id: pingoneaic:idm-objects:configuring-default-policy
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-objects/configuring-default-policy.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Policy"]
section_ids:
  policy-config-aic-ui: Configure policy validation in the Advanced Identity Cloud admin console
  policy-config-idm-ui: Configure policy validation in the IDM native admin console
  policy-config-object: Policy configuration objects
  policy-reference: Policy reference
  policy-config-element: Policy configuration element
  policy-config-input: Validate object data types
  conditional-policy-definitions: Add conditional policy definitions
---

# Apply policies to managed objects

In Advanced Identity Cloud, you can apply policies to managed objects to ensure that their values meet specific requirements. For example, you can require a password to have a minimum length or ensure a username is unique.

You can add a policy using:

* [The Advanced Identity Cloud admin console](#policy-config-aic-ui) (recommended)

* [The IDM native admin console](#policy-config-idm-ui)

* The policy configuration *(tooltip: You can edit the policy configuration over REST at the config/policy endpoint.)*

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Be cautious when using validation policies. If a policy relates to an array of [relationships](relationships.html), Return by Default should always be set to `false`. You can verify this in your managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint.)*. Any managed object that has `items` of `"type" : "relationship"`, must also have `"returnByDefault" : false`. |

The policy configuration *(tooltip: You can edit the policy configuration over REST at the config/policy endpoint.)* determines which policies apply to resources *other than managed objects*. The default policy configuration includes policies that are applied to internal user objects, but you can extend the configuration to apply policies to system objects.

## Configure policy validation in the Advanced Identity Cloud admin console

1. In the Advanced Identity Cloud admin console, go to Identities > Configure.

2. Select the managed object type, for example, Alpha realm - User or Bravo realm - User.

3. Click the Properties tab.

4. Do one of the following:

   * To edit an existing property, click the property.

   * To create a property, click Add a Property, select the property type and enter the required information, and click Save. Then, select the property you just created.

5. On the property's Validation tab, define the validation policy for the property.

6. Click Save.

## Configure policy validation in the IDM native admin console

1. In the Advanced Identity Cloud admin console, click Native Consoles > Identity Management.

2. Select the managed object type, for example, Alpha Realm - User or Bravo Realm - User.

3. On the Managed Object NAME page, do one of the following:

   * To edit an existing property, click the property.

   * To create a property, click Add a Property, enter the required information, and click Save. Then, select the property you just created.

4. On the Validation tab, click Add Policy.

5. In the Add/Edit Policy window, enter information in the following fields and click Add or Save:

   * Policy Id

     Refers to the unique `PolicyId`.

     You can find a list of the default policies in the [Policy reference](#policy-reference).

   * Parameter Name

     Refers to the parameters for the `PolicyId`. You can find a list of the default policy parameters in the [Policy reference](#policy-reference).

   * Value

     The parameter's value to validate.

## Policy configuration objects

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
| `policyExec`            | The name of the function that contains the policy implementation.                                                                                                                                                        |
| `clientValidation`      | Indicates whether the policy decision can be made on the client. When `"clientValidation": true`, the source code for the policy decision function is returned when the client requests the requirements for a property. |
| `validateOnlyIfPresent` | Notes that the policy is to be validated only if the field within the object being validated exists.                                                                                                                     |
| `policyRequirements`    | An array containing the policy requirement ID of each requirement that is associated with the policy. Typically, a policy will validate only one requirement, but it can validate more than one.                         |

## Policy reference

You can apply policies defined by Advanced Identity Cloud to the properties of any managed object or internal object.

Advanced Identity Cloud includes the following default policies and parameters:

| Policy Id                    | Parameters         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `required`                   |                    | The property is required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `not-empty`                  |                    | The property can't be empty.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `not-null`                   |                    | The property can't be null.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `unique`                     |                    | The property must be unique.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `valid-username`             |                    | The property must be unique and not have internal user conflicts.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `no-internal-user-conflict`  |                    | The property must not have internal user conflicts.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `regexpMatches`              | `regexp``flags`    | The property must match a regular expression pattern.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `valid-type`                 | `types`            | The property must have valid, specified types.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `valid-query-filter`         |                    | This rule enforces that each `privilege` entry adheres to the privilege defined in [Policies related to privileges](https://docs.pingidentity.com/pingidm/8/auth-guide/delegated-admin.html#privilege-policies). The policy validates that the query filter used to filter privileges is a valid query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `valid-array-items`          |                    | This rule enforces that each `privilege` entry adheres to the privilege defined in [Policies related to privileges](https://docs.pingidentity.com/pingidm/8/auth-guide/delegated-admin.html#privilege-policies). This policy validates that each item in an array contains the properties specified in the policy JSON, and that each of those properties satisfies any specific policies applied to it. By default, this policy verifies that each privilege contains `name`, `path`, `accessFlags`, `actions`, and `permissions` properties and that the `filter` property is valid if included.For example, the following parameters have a set of properties found within the array with individual policies for them:```json
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
| `valid-date`                 |                    | The property must have a valid date. Learn more in [RFC 3339-5.6](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `valid-formatted-date`       |                    | The property must have a valid date format. Learn more in [RFC 3339-5.6](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `valid-time`                 |                    | The property must have a valid time. Learn more in [RFC 3339-5.6](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `valid-datetime`             |                    | The property must have a valid date and time. Learn more in [RFC 3339-5.6](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `valid-duration`             |                    | The property must have a valid duration format. Learn more in [RFC 3339-appendix-A](https://datatracker.ietf.org/doc/html/rfc3339#appendix-A).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `valid-email-address-format` |                    | The property must have a valid email address. Learn more in [RFC 5321-4.1.2](https://datatracker.ietf.org/doc/html/rfc5321#section-4.1.2).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `valid-name-format`          |                    | The property must have a valid name format. Learn more in [RFC 5321-3.5.1](https://datatracker.ietf.org/doc/html/rfc5321#section-3.5.1).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `valid-phone-format`         |                    | The property must have a valid phone number format. Learn more in [E.123](https://en.wikipedia.org/wiki/E.123).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `at-least-X-capitals`        | `numCaps`          | The property must contain the minimum specified number of capital letters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `at-least-X-numbers`         | `numNums`          | The property value must contain the minimum specified number of numbers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `validNumber`                |                    | The property value must be an integer or floating-point number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `minimumNumber`              | `minimum`          | The property value must be greater than the `minimum` value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `maximumNumber`              | `maximum`          | The property value must be less than the `maximum` value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `minimum-length`             | `minLength`        | The property's minimum string length.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `maximum-length`             | `maxLength`        | The property's maximum string length.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `cannot-contain-others`      | `disallowedFields` | The property can't contain values of the specified fields. A comma-separated list of the fields to check against. For example, the default user password policy specifies `userName,givenName,sn` as disallowed fields.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `cannot-contain-characters`  | `forbiddenChars`   | The property can't contain the specified characters. A comma-separated list of disallowed characters. For example, the default user `userName` policy specifies `/` as a disallowed character.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `cannot-contain-duplicates`  |                    | The property cannot contain duplicate characters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `mapping-exists`             |                    | A sync mapping must exist for the property.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `valid-permissions`          |                    | This rule enforces that each `privilege` entry adheres to the privilege defined in [Policies related to privileges](https://docs.pingidentity.com/pingidm/8/auth-guide/delegated-admin.html#privilege-policies). The policy enforces well-formed permissions that include essential permissions, such as viewing, modification, or creation and adhere to a consistent and expected structure. This policy checks:- `CREATE` permissions must have write access to all properties required to create a new object.

- `CREATE` and `UPDATE` permissions must have write access to at least one property.

- `ACTION` permissions must include a list of allowed actions with at least one action included.

- If any attributes have write access, then the privilege must also have either the `CREATE` or `UPDATE` permission.

- All permissions listed must be valid types of permission: `VIEW`, `CREATE`, `UPDATE`, `ACTION`, or `DELETE`. No permissions are repeated.For example, a policy failure of `PRIVILEGE_MISSING_REQUIRED_CREATE_ATTRIBUTES` means that the privilege to create a managed object lacks access to that object's required attributes.                                                                                                                                                                            |
| `valid-accessFlags-object`   |                    | This rule enforces that each `privilege` entry adheres to the privilege defined in [Policies related to privileges](https://docs.pingidentity.com/pingidm/8/auth-guide/delegated-admin.html#privilege-policies). This policy validates if the `accessFlags` for a privilege matches the defined schema. The `accessFlag` entry must:- Contain an `attribute` property with a `String` value that matches a property name defined within the managed object's schema. The string value, such as "firstName", must be a property of the managed object for IDM to reference.

- Contain a `readOnly` property with a boolean value.

- Not contain any other attributes.For example, property names must be strings, such as "firstName", "lastName", "email". The property value must contain a property named `readOnly` whose value is a boolean, or `true` or `false`. The property value is invalid if it contains properties other than `readOnly`.                                                                                                                                                                                                                                                                                                                                                                                        |
| `valid-privilege-path`       |                    | This rule enforces that each `privilege` entry adheres to the privilege defined in [Policies related to privileges](https://docs.pingidentity.com/pingidm/8/auth-guide/delegated-admin.html#privilege-policies). This policy validates that the `path` specified in the privilege is a valid object with a schema for IDM to reference. Only objects with a schema, such as `managed/user` can have privileges applied to them.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `valid-temporal-constraints` |                    | The property must have valid temporal constraints. A non-empty array or a `ScriptableList` that must conform to a specific, predefined structure or pattern.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

## Policy configuration element

Properties defined in the managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint.)* can include a `policies` element that specifies how policy validation should be applied to that property. The following excerpt of the default managed object configuration shows how policy validation is applied to the `id` property of a managed/realm-name\_user object.

|   |                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Policies have the following restrictions:- They may be declared **only** on top-level managed object attributes.

- They may **not** be declared on an attribute that is an array or on any nested attributes (those within an array or object). |

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
                "isPersonal" : false
            }
        }
    }
}
```

The policy for the `_id` property references the function `cannot-contain-characters`. This is a [default policy](#policy-reference) that you can apply.

## Validate object data types

The `type` property of a managed object specifies the data type of that property. For example, `array`, `boolean`, `number`, `null`, `object`, or `string`. Learn more about data types in the [JSON Schema Primitive Types](https://json-schema.org/draft-04/draft-zyp-json-schema-04#rfc.section.3.5) section of the JSON Schema standard.

The `type` property is subject to policy validation when a managed object is created or updated. Validation fails if data doesn't match the specified `type`, such as when the data is an `array` instead of a `string`. The default `valid-type` policy enforces the match between property values and the `type` defined in the managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint.)*.

Advanced Identity Cloud supports multiple valid property types. For example, you might have a scenario where a managed user can have more than one telephone number, or a *null* telephone number when the user entry is first created and the telephone number is not yet known. In such a case, you can specify the accepted property type as follows in your managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint.)*:

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

In this case, the type is defined in the policy configuration *(tooltip: You can edit the policy configuration over REST at the config/policy endpoint.)*. The policy checks the telephone number for an accepted `type` and `pattern`, either for a real telephone number or a `null` entry.

## Add conditional policy definitions

You can extend the policy service to support policies that are applied only under specific conditions. To apply a conditional policy to objects types, add the policy to your project's managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint.)*. To apply a conditional policy to other objects, add it to your project's policy configuration *(tooltip: You can edit the policy configuration over REST at the config/policy endpoint.)*.

The following managed object configuration shows a sample conditional policy for the `password` property of user objects. The policy indicates that `sys-admin` users have a more lenient password policy than regular employees:

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
                                        "policyId" : "at-least-X-numbers",
                                        "params" : {
                                            "numNums" : ["1"]
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
                                        "policyId" : "at-least-X-numbers",
                                        "params" : {
                                            "numNums" : ["2"]
                                        }
                                    }
                                ]
                            }
                        ],
                        "fallbackPolicies" : [
                            {
                                "policyId" : "at-least-X-numbers",
                                "params" : {
                                    "numNums" : ["1"]
                                }
                            }
                        ]
                    }
                    ...
}
```

There are two distinct scripted conditions that are defined in the `condition` elements. The first condition asserts that the user object, contained in the `fullObject` argument, is a member of the `sys-admin` org. If that assertion is true, the `at-least-X-numbers` policy is applied to the `password` attribute of the user object, and minimum numbers is set to `1`.

The second condition asserts that the user object is a member of the `employees` org. If that assertion is true, the `at-least-X-numbers` policy is applied to the `password` attribute of the user object, and the minimum numbers is `2`.

In the event that neither condition is met: the user object is not a member of the `sys-admin` org or the `employees` org, an optional fallback policy can be applied. In this example, the fallback policy also references the `at-least-X-numbers` policy and specifies that for such users, the minimum numbers is `1`.

The `dependencies` field prevents the condition scripts from being run at all, if the user object doesn't include an `org` attribute.

|   |                                                            |
| - | ---------------------------------------------------------- |
|   | Scripted conditions do not apply to progressive profiling. |

---

---
title: Configure relationship change notification
description: Configure notifications when relationships change to recalculate derived properties
component: pingoneaic
page_id: pingoneaic:idm-objects:relationships-notification
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-objects/relationships-notification.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Relationships", "Roles", "Change Notification", "REST API"]
section_ids:
  origin_and_referenced_objects: Origin and referenced objects
  notification_properties: Notification properties
  relationship_change_notifications: Relationship change notifications
---

# Configure relationship change notification

A relationship exists between two managed objects. By default, when a relationship changes for any create, update, or delete operation, the managed objects on either side of the relationship are *not* notified of that change. This means that the *state* of each object with respect to that relationship field is not recalculated until the object is read. This default behavior improves performance, especially cases where many objects are affected by a single relationship change.

For `roles`, change notification *is* set to `TRUE` by default. This default configuration lets managed users receive notifications when any relationships that link users, roles, and assignments are manipulated. For more information about relationship change notification, refer to [Roles and relationship change notification](roles-change-notification.html).

## Origin and referenced objects

A relationship exists between an *origin* object and a *referenced* object. These terms reflect which managed object is specified in the URL (for example `managed/realm-name_user/psmith`), and which object is referenced by the relationship (`_ref*`) properties. For more information about the relationship properties, refer to [Create a relationship between two objects](relationships-between-objects.html).

In an example in the [Create a relationship between two objects](relationships-between-objects.html) section, a POST on `managed/realm-name_user/psmith` (UUID is `51257f1e-6562-4b67-a80b-47b84f693f1b`) with `"manager":{_ref:"managed/realm-name_user/bjensen"}` (UUID is `1dff18dc-ac57-4388-8127-dff309f80002`) causes `managed/realm-name_user/psmith` to be the origin object, and `managed/realm-name_user/bjensen` to be the referenced object for that relationship.

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request POST \
--data '{
  "sn":"Smith",
  "userName":"psmith",
  "givenName":"Patricia",
  "displayName":"Patti Smith",
  "description" : "psmith - new user",
  "mail" : "psmith@example.com",
  "telephoneNumber" : "0831245986",
  "password" : "Passw0rd",
  "manager" : {"_ref" : "managed/realm-name_user/1dff18dc-ac57-4388-8127-dff309f80002"}
}' \
"https://<tenant-env-fqdn>/openidm/managed/realm-name_user?_action=create"
{
  "_id": "51257f1e-6562-4b67-a80b-47b84f693f1b",
  "_rev": "6aad0f3b-eb20-4ae4-8c72-7e904b1062e5-34787",
  "country": null,
  "frUnindexedString1": null,
  "mail": "psmith@example.com",
  "memberOfOrgIDs": [],
  ...
}
```

This relationship is illustrated as follows:

![Illustration shows the origin and referenced objects in a relationship](_images/relationship-objects.png)Figure 1. Relationship Objects

Note that for the reverse relationship (a POST on `managed/realm-name_user/bjensen` with `"reports":[{_ref = "managed/realm-name_user/psmith"}]`) `managed/realm-name_user/bjensen` would be the origin object, and `managed/realm-name_user/psmith` would be the referenced object.

By default, when a relationship changes, neither the origin object nor the referenced object is *notified* of the change. So, with the POST on `managed/realm-name_user/psmith` with `"manager":{_ref:"managed/realm-name_user/bjensen"}`, neither `psmith`'s object nor `bjensen`'s object is notified. This means that the objects are not updated to reflect the latest change.

## Notification properties

To configure relationship change notifications, set the `notify` and `notifySelf` properties in your managed object schema.

|   |                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Auditing is not tied to relationship change notification and is always triggered when a *relationship* changes; therefore, relationship changes are audited, regardless of the `notifySelf`, `notify`, and `notifyRelationships` properties. |

The following properties specify whether objects that reference relationships are notified of a relationship change:

* `notifySelf`

  Notifies the origin object of the relationship change.

  In our example, if the `manager` definition includes `"notifySelf":true` and if the relationship is changed through a URL that references `psmith`, then `psmith`'s object would be notified of the change. Thus, for any CREATE, UPDATE or DELETE request on the `psmith/manager`, `psmith` would be notified, but the managed object referenced by this relationship (`bjensen`) would not be notified.

  If the relationship were manipulated through a request to `bjensen/reports`, then `bjensen` would only be notified if the `reports` relationship specified `"notifySelf":true`.

* `notify`

  Notifies the referenced object of the relationship change. Set this property on the `resourceCollection` of the relationship property.

  In our example, assume that the `manager` definition has a `resourceCollection` with a `path` of `managed/realm-name_user` and that this object specifies `"notify":true`. If the relationship changes through any CREATE, UPDATE, or DELETE operation on the URL `psmith/manager`, then the reference object (`managed/realm-name_user/bjensen`) would be notified of the change to the relationship.

* `notifyRelationships`

  This property controls the propagation of notifications out of a managed object when one of its properties changes through an update or patch or when that object receives a notification through one of these fields.

  The `notifyRelationships` property takes an array of relationships as a value; for example, `"notifyRelationships":["relationship1", "relationship2"]`. The relationships specified here are fields defined on the managed object type, which might itself be a relationship.

  Notifications are propagated according to the *recipient's*`notifyRelationships` configuration. If a managed object type is notified of a change through one if its relationship fields, the notification is done according to the configuration of the recipient object.

  To illustrate, review the `attributes` property in the default `managed/realm-name_assignment` object:

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

This configuration means that if an assignment is updated or patched and the assignment's `attributes` change in some way, all the `roles` connected to that assignment are notified.

Note that the `role` managed object has `"notifyRelationships":["members"]` defined on its `assignments` field as follows:

```json
{
  "name" : "role",
    "schema" : {
      ...
      "properties" : {
        ...
        "assignments" : {
          ...
          "notifyRelationships" : ["members"]
        }
    ...
}
```

When a role is notified of the creation of a new relationship to an assignment, the notification is propagated through the `assignments` property. Because `"notifyRelationships":["members"]` is set on the `assignments` property, the notification is propagated across the role to all of its members.

## Relationship change notifications

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

In this case, `notifySelf` indicates the origin or `user` object. If any changes are made to a relationship referencing a role through a URL that includes a user, the user is notified of the change. For example, if there is a CREATE on `managed/realm-name_user/psmith/roles` specifying a set of references to existing roles, user `psmith` is notified of the change.

Similarly, the `role` object also includes a `members` property. That property includes the following schema definition:

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
                "path" : "managed/realm-name_user",
                "label" : "User",
                ...
              }
           ]
          }
          ...
```

Notice the `"notify":true` setting on the `resourceCollection`. This setting indicates that if the relationship is created, updated, or deleted through a URL that references that role, all objects in that resource collection (in this case, `managed/realm-name_user` objects), which are identified as `members` of that role, are notified of the change.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * To notify an object that the relationship has changed (using the `notify` property), the relationship *must* be [bidirectional](reverse-relationships.html) (`"reverseRelationship":true`).

  When an object is notified of a relationship state change (create, delete, or update), part of that notification process involves calculating the changed object state with respect to the changed relationship field. For example, if a managed user is notified that a role was created, the user object calculates its base state and the state of its `roles` field, before and after the new role is created. This *before* and *after* state is then reconciled.

  An object referenced by a forward (unidirectional) relationship does not have a field referencing that relationship; the object is "pointed-to" but does not "point-back". Because this object cannot calculate its *before* and *after* state with respect to the relationship field, it cannot be notified.

  Similarly, relationships that are notified of changes to the objects that reference them *must* be bidirectional relationships.

  If you configure relationship change notification on a unidirectional relationship, IDM throws an exception.

* You cannot configure relationship change notification in the IDM admin console; you must update the managed object schema directly. |

---

---
title: Create a relationship between two objects
description: Create relationships between managed objects using reference properties
component: pingoneaic
page_id: pingoneaic:idm-objects:relationships-between-objects
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-objects/relationships-between-objects.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Relationships", "REST API"]
---

# Create a relationship between two objects

In the default IDM schema, several user properties are defined as relationships, for example, the `manager` relationship.

Relationships let you *reference* one managed object from another using the `_ref*` relationship properties. Three properties make up a relationship reference:

* `_refResourceCollection` specifies the container of the referenced object, for example, `managed/realm-name_user`.

* `_refResourceId` specifies the ID of the referenced object. This is generally a system-generated UUID, such as `9dce06d4-2fc1-4830-a92b-bd35c2f6bcbb`.

* `_ref` is a derived path that is a combination of `_refResourceCollection` and a URL-encoded `_refResourceId`.

For example, imagine that you are creating a new user, `psmith`, and that `psmith`'s manager is `bjensen`. You would add `psmith`'s user entry, and *reference* `bjensen`'s entry with the `_ref` property.

First, retrieve `bjensen`'s UUID, displayed in the `_id` property value.

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request GET \
"https://<tenant-env-fqdn>/openidm/managed/realm-name_user?_queryFilter=userName+eq+%22bjensen%22"
{
  "result": [
    {
      "_id": "1dff18dc-ac57-4388-8127-dff309f80002",
      "_rev": "f4816053-aa01-4a7b-8380-8f3646787fd0-23348",
      "country": null,
      ...
    }
  ]
  ...
}
```

Next, add the new user `psmith` and specify `bjensen` as the manager using the `_ref` property. Make sure to use `bjensen`'s UUID, for example, `1dff18dc-ac57-4388-8127-dff309f80002`.

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request POST \
--data '{
  "sn":"Smith",
  "userName":"psmith",
  "givenName":"Patricia",
  "displayName":"Patti Smith",
  "description" : "psmith - new user",
  "mail" : "psmith@example.com",
  "telephoneNumber" : "0831245986",
  "password" : "Passw0rd",
  "manager" : {"_ref" : "managed/realm-name_user/1dff18dc-ac57-4388-8127-dff309f80002"}
}' \
"https://<tenant-env-fqdn>/openidm/managed/realm-name_user?_action=create"
{
  "_id": "51257f1e-6562-4b67-a80b-47b84f693f1b",
  "_rev": "6aad0f3b-eb20-4ae4-8c72-7e904b1062e5-34787",
  "country": null,
  "frUnindexedString1": null,
  "mail": "psmith@example.com",
  "memberOfOrgIDs": [],
  ...
}
```

Note that relationship information is not returned by default. To show the relationship in `psmith`'s entry, you must explicitly request their manager entry, as follows:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/managed/realm-name_user?_queryFilter=userName+eq+%22psmith%22&_fields=manager"
{
  "result": [
    {
      "_id": "51257f1e-6562-4b67-a80b-47b84f693f1b",
      "_rev": "6aad0f3b-eb20-4ae4-8c72-7e904b1062e5-34787",
      "manager": {
        "_ref": "managed/alpha_user/1dff18dc-ac57-4388-8127-dff309f80002",
        "_refResourceCollection": "managed/alpha_user",
        "_refResourceId": "1dff18dc-ac57-4388-8127-dff309f80002",
        "_refProperties": {
          "_id": "3dd2c42d-598e-4b78-bf59-0aab43113be7",
          "_rev": "6aad0f3b-eb20-4ae4-8c72-7e904b1062e5-34784"
        }
      }
    }
  ],
  ...
}
```

If a relationship changes, you can query the updated relationship state when any referenced managed objects are queried. So, after creating user `psmith` with manager `bjensen`, run a query on `bjensen`'s user entry. The query shows a reference to `psmith`'s entry in their `reports` property, which is configured as the `reversePropertyName` of the `manager` property.

The following query shows `bjensen`'s direct reports including the new user entry, `psmith`:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/managed/realm-name_user?_queryFilter=userName+eq+%22bjensen%22&_fields=reports"
{
  "result": [
    {
      "_id": "1dff18dc-ac57-4388-8127-dff309f80002",
      "_rev": "f4816053-aa01-4a7b-8380-8f3646787fd0-23348",
      "reports": [
        ...
        {
          "_ref": "managed/alpha_user/51257f1e-6562-4b67-a80b-47b84f693f1b",
          "_refResourceCollection": "managed/alpha_user",
          "_refResourceId": "51257f1e-6562-4b67-a80b-47b84f693f1b",
          "_refProperties": {
            "_id": "3dd2c42d-598e-4b78-bf59-0aab43113be7",
            "_rev": "6aad0f3b-eb20-4ae4-8c72-7e904b1062e5-34784"
          }
        }
      ]
    }
  ],
  ...
}
```

|   |                                                                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | IDM maintains referential integrity by deleting the relationship reference if the object referred to by that relationship is deleted. In our example, if `bjensen`'s user entry is deleted, the corresponding reference in `psmith`'s `manager` property is removed. |

---

---
title: Create and modify managed object types
description: Create new managed object types and modify existing ones using UI or REST
component: pingoneaic
page_id: pingoneaic:idm-objects:creating-modifying-managed-objects
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-objects/creating-modifying-managed-objects.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Schema"]
section_ids:
  manage-object-ui: Create a managed object type using the IDM native admin console
  manage-object-types-rest: Create a managed object type using the REST API
  managed-objects-property-def-fields: Typical managed object property definition fields
  default-values-managed-obj: Default values
---

# Create and modify managed object types

If the managed object types provided in the default configuration don't meet your needs, you can create or modify them.

Every object type has a `name` and a `schema` that describes the properties associated with that object. The `name` can only include the characters `a-z`, `A-Z`, `0-9`, and `_` (underscore). You can add any arbitrary properties to the schema.

You can create or modify managed object type using the UI or the REST API.

The Advanced Identity Cloud admin console is the recommended console for managing object types. Learn more in [Configure managed objects](../identities/configure-object-types.html). The IDM native admin console has limited functionality and doesn't support features such as relationship fields and enums.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Ping Identity recommends that you don't delete the default managed object types in your tenant. In many cases it can break your tenant.The IDM native admin console depends on the presence of the default managed object types and the default properties nested within them. If you remove any of these schema elements, and you use the IDM native admin console to configure IDM, you must modify the IDM native admin console code accordingly. For example, if you remove the `assignment` object type from the managed object configuration, the UI will throw exceptions wherever it queries this schema element. |

## Create a managed object type using the IDM native admin console

To create a new managed object type in the IDM native admin console:

1. From the Advanced Identity Cloud admin console, select Native Consoles > Identity Management.

2. Click New Managed Object.

3. On the New Managed Object page, enter a name and readable title for the object, make optional changes, as necessary, and click Save. The readable title specifies what the object will be called in the UI.

4. On the Properties tab, specify the schema for the managed object (the properties that make up the object).

5. On the Scripts tab, specify any scripts that will be applied on events associated with that managed object. For example, scripts that will be run when an object of that type is created, updated, or deleted.

   > **Collapse: Example:  managed object definition**
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

To create a custom property:

1. In the Advanced Identity Cloud admin console, click Native Consoles > Identity Management.

2. Click the object type, for example Alpha\_user or Bravo\_user.

3. Click + Add a Property. This scrolls the page to the bottom and automatically focuses on the Name input field.

4. In the Name input field, enter a new property name prefixed with `custom_`; for example, enter `custom_department`.

5. In the Label input field, optionally enter a display name for the new property.

6. Click Save.

To delete a custom property:

1. Delete all data stored in the custom property for all users, then run a full reconciliation.

   |   |                                                                                                                                                            |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you don't delete all data stored in the custom property **before** deleting the property, you might see errors when running subsequent reconciliations. |

2. In the Advanced Identity Cloud admin console, click Native Consoles > Identity Management.

3. Click the object type, for example Alpha\_user or Bravo\_user.

4. In the list of properties, find the row for the custom property that you want to delete:

   1. Click the row's cross icon ([icon: times, set=fa]).

   2. In the Delete Property confirmation modal, click Confirm.

To customize an extension property:

1. In the Advanced Identity Cloud admin console, click Native Consoles > Identity Management.

2. Click the object type, for example, Alpha Realm - User or Bravo Realm - User.

3. Find an extension property that has one of the following default labels:

   * Generic Indexed String 1–20 or Generic Unindexed String 1–5

   * Generic Indexed Multivalue 1–5 or Generic Multivalue String 1–5

   * Generic Indexed Date 1–5 or Generic Date String 1–5

   * Generic Indexed Integer 1–5 or Generic Integer String 1–5

     |   |                                                                                               |
     | - | --------------------------------------------------------------------------------------------- |
     |   | If you need to make the property searchable, make sure you use an indexed extension property. |

4. Click the pen icon ([icon: pen, set=fa]) to edit the property.

5. In the Readable Title input field, enter a custom label. For example, `Department`.

6. Click Save.

## Create a managed object type using the REST API

1. Get the current managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint.)*:

   ```none
   curl \
   --header "Authorization: Bearer <access-token>" \
   --header "Accept-API-Version: resource=1.0"  \
   --request GET \
   "https://<tenant-env-fqdn>/openidm/config/managed"
   {
     "_id": "managed",
     "objects": [ {managed-config-object} ]
   }
   ```

2. Make changes and replace the managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint.)*:

   ```none
   curl \
   --header "Authorization: Bearer <access-token>" \
   --header "Content-type: application/json" \
   --header "Accept-API-Version: resource=1.0"  \
   --request PUT \
   --data '{
     "_id": "managed",
     "objects": [ {managed-config-object} ]
   }' \
   "https://<tenant-env-fqdn>/openidm/config/managed"
   {
     "_id": "managed",
     "objects": [ {managed-config-object} ]
   }
   ```

## Typical managed object property definition fields

The schema of a managed object describes the properties associated with that object.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | * Avoid using the dash character in property names (like `last-name`) because dashes in names make JavaScript syntax more complex. Instead, use "camel case" (`lastName`). If you can't avoid dash characters, write `source['last-name']` instead of `source.last-name` in your JavaScript.

* Managed object properties that contain an underscore (`_`) are reserved for internal use. **Do not create** new properties that contain underscores, and do not include these properties in update requests. |

* `title`

  The name of the property, in human-readable language, used to display the property in the UI.

* `description`

  A brief description of the property.

* `viewable`

  Specifies whether this property is viewable in the object's profile in the UI. Boolean, `true` or `false` (`true` by default).

* `searchable`

  Specifies whether this property can be searched in the UI. A searchable property is visible in the end-user UI.

  Boolean, `true` or `false` (`false` by default).

  |   |                                                                                                                                   |
  | - | --------------------------------------------------------------------------------------------------------------------------------- |
  |   | Do not modify the searchable setting on properties in the default managed object schema, unless otherwise noted in documentation. |

* `userEditable`

  Specifies whether users can edit the property value in the UI. This property applies in the context of the End User UI, where users are able to edit certain properties of their own accounts. Boolean, `true` or `false` (`false` by default).

* `pattern`

  Any specific pattern to which the value of the property must adhere. For example, a property whose value is a date might require a specific date format.

* `policies`

  Any policy validation that must be applied to the property.

* `required`

  Specifies whether the property must be supplied when an object of this type is created. Boolean, `true` or `false`.

  > **Collapse: To set a property as  in the Advanced Identity Cloud admin console:**
  >
  > 1. In the Advanced Identity Cloud admin console, go to Identities > Configure.
  >
  > 2. Select the object type, for example, Alpha Realm - User or Bravo Realm - User.
  >
  > 3. Click the Properties tab.
  >
  > 4. Click the property you want to update.
  >
  > 5. On the Details tab, select the Required checkbox.
  >
  > 6. Click Save.

  > **Collapse: To set a property as  in the IDM native admin console:**
  >
  > 1. In the left menu, go to Native Consoles > Identity Management.
  >
  > 2. Select the managed object, for example, Alpha Realm - User or Bravo Realm - User. A list of the properties in the managed object displays. The Required column displays which properties Advanced Identity Cloud currently requires.
  >
  > 3. Click the property you want to update.
  >
  > 4. In the Details tab, enable the Required field.
  >
  > 5. Click Save.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                  |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The `required` policy is assessed only during object creation, not when a managed object is updated. You can effectively bypass the policy by updating the managed object and supplying an empty value for that property. To prevent this inconsistency, set both `required` and `notEmpty` to `true` for required properties. This configuration indicates that the property must exist, and must have a value. |

* `type`

  The data type for the property value; can be `string`, `array`, `boolean`, `integer`, `number`, `object`, `Resource Collection`, or `null`.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If any user might not have a value for a specific property (such as a `telephoneNumber`), you must include `null` as one of the property *types*. You can set a null property type in the UI:- In the Advanced Identity Cloud admin console: Identities > Configure > *identity\_object*, select the property, and under the Property Value tab, Show Advanced, select Nullable.

  - In the IDM native admin console: Configure > Managed Objects > User, select the property, and under the Property Value tab, Show Advanced, select `Nullable` to `true`.You can also set a null property type in your managed object configuration by setting `"type" : '[ "string","null" ]'` for that property (where `string` can be any other valid property type. This information is validated by the policy service.If you're configuring a data `type` of `array` through the Advanced Identity Cloud admin console or IDM native admin console, you're limited to two values. |

* `isVirtual`

  Specifies whether the property takes a static value, or whether its value is calculated "on the fly" as the result of a script. Boolean, `true` or `false`.

* `returnByDefault`

  For non-core attributes (virtual attributes and relationship fields), specifies whether the property is returned in the results of a query on an object of this type *if it is not explicitly requested*. Virtual attributes and relationship fields are not returned by default. Boolean, `true` or `false`. When the property is in an array within a relationship, always set to `false`.

- `default`

  Specifies a default value if the object is created without passing a value. Default values are available for the following data types, and arrays of those types:

  * boolean

  * number

  * object

  * string

  |   |                                                                              |
  | - | ---------------------------------------------------------------------------- |
  |   | Advanced Identity Cloud assumes all default values are valid for the schema. |

- `enum`

  []()Restricts a field's possible values to a defined set of options. `enum` is supported for `string` and `number` types, and for `array` types containing strings or numbers.

  To define `enum` values, add the `enum` property to the field's schema definition. You can do this using an API PUT request to the `/openidm/config/managed` endpoint or in the Advanced Identity Cloud admin console. Learn more in [Property settings reference](../identities/customize-object-types.html#property-settings-reference).

  You can't use the IDM native admin console to add, remove, or edit enums.

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

  |   |                                                                                                                                                                                                                                                                                                |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Labels and translations for `enum` values are not set within the managed object schema. They must be configured using the [translation override feature](../tenants/tenant-localize.html#translating-enum-values) using API POST requests to the `/openidm/config/uilocale/<locale>` endpoint. |

## Default values

You can specify default values in the managed object schema. If you omit a value when creating an object, the default value is automatically applied to the object type. You can have default values for the following data types, and arrays of those types:

* boolean

* number

* object

* string

For example, the default managed object schema includes a default value that makes `accountStatus:active`, which effectively replaces the `onCreate` script that was previously used to achieve the same result. The following excerpt from the managed object schema displays the default value for `accountStatus`:

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

|   |                                                                              |
| - | ---------------------------------------------------------------------------- |
|   | Advanced Identity Cloud assumes all default values are valid for the schema. |

---

---
title: Data models and objects reference
description: Reference documentation for managed, system, configuration, and repository objects
component: pingoneaic
page_id: pingoneaic:idm-objects:appendix-objects
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-objects/appendix-objects.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Schema"]
page_aliases: ["appendix-links.adoc", "appendix-system-objects.adoc"]
---

# Data models and objects reference

You can customize a variety of objects that can be addressed via a URL or URI. IDM can perform a common set of functions on these objects, such as CRUDPAQ (create, read, update, delete, patch, action, and query).

Depending on how you intend to use them, different object types are appropriate.

**Object Types**

| Object Type           | Intended Use                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Special Functionality                                                                                            |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Managed objects       | Serve as targets and sources for synchronization, and to build virtual identities.For more information, refer to [Managed objects](managed-objects.html).                                                                                                                                                                                                                                                                                                                                                                                                                                    | Provide appropriate auditing, script hooks, declarative mappings and so forth in addition to the REST interface. |
| Configuration objects | Ideal for look-up tables or other custom configuration, which you can configure externally like any other system configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Adds file view, REST interface, and so forth                                                                     |
| Repository objects    | The equivalent of arbitrary database table access. Appropriate for managing data through the underlying data store or repository API.For information on how to access identity related data using REST, refer to [REST and IDM](../idm-rest-api/rest-and-idm.html).                                                                                                                                                                                                                                                                                                                          | Persistence and API access                                                                                       |
| System objects        | Pluggable representations of objects on external systems. They follow the same RESTful resource based design principles as managed objects. There is a default implementation for the ICF framework, which allows any connector object to be represented as a system object.For more information on system objects and connectors, refer to [Ping Identity ICF](https://docs.pingidentity.com/openicf/connector-reference/openidm-openicf.html).For information on REST endpoints relating to system objects, refer to [System objects](../idm-rest-api/endpoints/rest-system-objects.html). |                                                                                                                  |
| Audit objects         | Houses audit data in the repository.For more information on how to access audit data in Advanced Identity Cloud, refer to [Access logs with API key and secret](../developer-docs/authenticate-to-rest-api-with-api-key-and-secret.html).                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                  |
| Links                 | Link objects define relations between source objects and target objects, usually relations between managed objects and system objects.The link relationship is established by provisioning activity that either results in a new account on a target system, or a reconciliation or synchronization scenario that takes a `LINK` action.For more information, refer to [Reuse links between mappings](../idm-synchronization/reusing-links.html).                                                                                                                                            |                                                                                                                  |

---

---
title: Define and call data queries
description: Define and call data queries using common filter expressions and REST APIs
component: pingoneaic
page_id: pingoneaic:idm-objects:queries
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-objects/queries.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "REST API", "Virtual Properties"]
section_ids:
  query-filters: Common filter expressions (_queryFilter)
  special-char-queries: Special characters in queries
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
  execute-on-retrieve: Recalculate properties based on other properties (virtual) in queries
---

# Define and call data queries

You can define and call queries using the REST or Resource API. Queries are supported on both managed and system objects, and you can define them through:

* Common filter expressions using the `_queryFilter` keyword.

* Parameterized, or predefined queries, such as the keyword `_pageSize`.

## Common filter expressions (`_queryFilter`)

The Advanced Identity Cloud REST API defines common filter expressions that enable you to form arbitrary queries using a number of supported filter operations. This query capability is the standard way to query data if no predefined query exists and is supported for all managed and system objects.

Common filter expressions are useful because they do not require knowledge of how the object is stored, and they do not require additions to the repository configuration.

Common filter expressions are called with the `_queryFilter` keyword. The following example uses a common filter expression to retrieve managed user objects whose user name is Smith:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
'https://<tenant-env-fqdn>/openidm/managed/realm-name_user?_queryFilter=userName+eq+"smith"'
```

The filter is URL encoded in this example. The corresponding filter using the resource API would be:

```javascript
openidm.query("managed/realm-name_user", { "_queryFilter" : '/userName eq "smith"' });
```

### Special characters in queries

JavaScript query invocations are not subject to the same URL-encoding requirements as GET requests. Since JavaScript supports the use of single quotes, it is not necessary to escape the double quotes from most examples in this guide. Make sure to protect against pulling in data that could contain special characters, such as double-quotes (`"`). The following example shows one method of handling special characters:

```json
"correlationQuery" : {
  "type" : "text/javascript",
  "source" : "var qry = {'_queryFilter': org.forgerock.util.query.QueryFilter.equalTo('uid', source.userName).toString()}; qry"
}
```

### Construct queries

The `openidm.query` function lets you query managed and system objects. The query syntax is `openidm.query(id, params)`, where `id` specifies the object upon the query should be performed, and `params` provides the parameters passed to the query (the `_queryFilter`). For example:

```javascript
var equalTo = org.forgerock.util.query.QueryFilter.equalTo;
queryParams = {
    "_queryFilter": equalTo("uid", value).toString()
};
openidm.query("managed/realm-name_user", queryParams)
```

Over the REST interface, the query filter is specified as `_queryFilter=filter`, for example:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
'https://<tenant-env-fqdn>/openidm/managed/realm-name_user?_queryFilter=userName+eq+"Smith"'
```

|   |                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------- |
|   | In `_queryFilter` expressions, string values *must* use double-quotes. Numeric and boolean expressions should not use quotes. |

When called over REST, you must URL encode the filter expression. The following examples show the filter expressions using the Resource API and the REST API but do not show the URL encoding to make them easier to read.

The filter expression is constructed from the building blocks shown in this section. In these expressions, the simplest json-pointer is a field of the JSON resource, such as `userName` or `id`. A JSON pointer can, however, point to nested elements.

|   |                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can also use the negation operator (**`!`**) in query construction. For example, a `_queryFilter=!(userName+eq+"jdoe")` query would return every `userName` except for `jdoe`. |

#### Comparison expressions

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
> --header "Authorization: Bearer <access-token>" \
> --header "Accept-API-Version: resource=1.0" \
> --request GET \
> 'https://<tenant-env-fqdn>/openidm/managed/realm-name_user?_queryFilter=givenName+eq+"Dan"&_fields=userName,givenName'
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
> --header "Authorization: Bearer <access-token>" \
> --header "Accept-API-Version: resource=1.0" \
> --request GET \
> 'https://<tenant-env-fqdn>/openidm/managed/realm-name_role?_queryFilter=stringArrayField+eq+"foo"'
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
> The following REST call returns the username and given name of all managed users whose first name (`givenName`) contains "Da":
>
> ```
> curl \
> --header "Authorization: Bearer <access-token>" \
> --header "Accept-API-Version: resource=1.0" \
> --request GET \
> 'https://<tenant-env-fqdn>/openidm/managed/realm-name_user?_queryFilter=givenName+co+"Da"&_fields=userName,givenName'
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
> --header "Authorization: Bearer <access-token>" \
> --header "Accept-API-Version: resource=1.0" \
> --request GET \
> 'https://<tenant-env-fqdn>/openidm/managed/realm-name_user?_queryFilter=sn+sw+"Jen"&_fields=userName'
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
> --header "Authorization: Bearer <access-token>" \
> --header "Accept-API-Version: resource=1.0" \
> --request GET \
> 'https://<tenant-env-fqdn>/openidm/managed/realm-name_user?_queryFilter=employeeNumber+lt+5000&_fields=userName,employeeNumber'
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
> --header "Authorization: Bearer <access-token>" \
> --header "Accept-API-Version: resource=1.0" \
> --request GET \
> 'https://<tenant-env-fqdn>/openidm/managed/realm-name_user?_queryFilter=employeeNumber+le+5000&_fields=userName,employeeNumber'
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
> --header "Authorization: Bearer <access-token>" \
> --header "Accept-API-Version: resource=1.0" \
> --request GET \
> 'https://<tenant-env-fqdn>/openidm/managed/realm-name_user?_queryFilter=employeeNumber+gt+5000&_fields=userName,employeeNumber'
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
> --header "Authorization: Bearer <access-token>" \
> --header "Accept-API-Version: resource=1.0" \
> --request GET \
> 'https://<tenant-env-fqdn>/openidm/managed/realm-name_user?_queryFilter=employeeNumber+ge+5000&_fields=userName,employeeNumber'
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

#### Presence expressions

The following examples show how you can build filters using a presence expression, shown as `pr`. The presence expression is a filter that returns all records with a given attribute.

A presence expression filter evaluates to `true` when a `json-pointer pr` matches any object in which the json-pointer is present and contains a non-null value. Consider the following expression:

```json
"_queryFilter" : '/mail pr'
```

The following REST call uses that expression to return the mail addresses for all managed users with a `mail` property:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
'https://<tenant-env-fqdn>/openidm/managed/realm-name_user?_queryFilter=mail+pr&_fields=mail'
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
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
'https://<tenant-env-fqdn>/openidm/system/csvfile/account?_queryFilter=email+pr&_fields=email'
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

|   |                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Not all connectors support the presence filter. In most cases, you can replicate the behavior of the presence filter with an "equals" (`eq`) query, such as `_queryFilter=email+eq+"*"` |

#### Literal expressions

A literal expression is a boolean:

* `true` matches any object in the resource.

* `false` matches no object in the resource.

For example, you can list the `_id` of all managed objects as follows:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
'https://<tenant-env-fqdn>/openidm/managed/realm-name_user?_queryFilter=true&_fields=_id'
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

#### `In` expression clause

PingIDM provides limited support for the [in expression clause](#query-in). You can use this clause for queries on singleton string properties or arrays. The `in` query expression is not supported through the IDM admin console or for use by [delegated administrators](../idm-auth/delegated-admin.html#using-delegated-admin).

The `in` operator is shorthand for multiple `OR` conditions.

|   |                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The following example command includes escaped characters. For readability, the non-escaped URL syntax is:```none
https://<tenant-env-fqdn>/openidm/managed/realm-name_user?_pageSize=1000&_fields=userName&_queryFilter=/userName in '["user4a","user3a"]'
``` |

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/managed/realm-name_user?_pageSize=1000&_fields=userName&_queryFilter=userName%20in%20'%5B%22user4a%22%2C%22user3a%22%5D'"
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

#### Filter expanded relationships

You can use `_queryFilter` to filter expanded relationships from a collection, such as `authzRoles`. The following example queries the `manager-int` authorization role of a user:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/managed/realm-name_user/b70293db-8743-45a7-9215-1ca8fd8a0073/authzRoles?_queryFilter=name+eq+'manager-int'&_fields=*"
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

#### Complex expressions

You can combine expressions using the boolean operators `and`, `or`, and `!` (not). The following example queries managed user objects located in London with the last name Jensen:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
'https://<tenant-env-fqdn>/openidm/managed/realm-name_user/?_queryFilter=city+eq+"London"and+sn+eq"Jensen"&_fields=userName,givenName,sn'
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

#### Filter objects in arrays

Use query grouping to perform your query on properties within an array. For example, to query `effectiveRoles` for users who have the `testManagedRole`, check the `_refResourceId` inside the `effectiveRoles` array:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
'https://<tenant-env-fqdn>/openidm/managed/realm-name_user/?_queryFilter=/effectiveRoles\[/_refResourceId+eq+"testManagedRole"]&_fields=userName,givenName,sn,effectiveRoles'
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
          "_refResourceCollection": "managed/realm-name_role",
          "_refResourceId": "testManagedRole",
          "_ref": "managed/realm-name_role/testManagedRole"
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
          "_refResourceCollection": "managed/realm-name_role",
          "_refResourceId": "testManagedRole",
          "_ref": "managed/realm-name_role/testManagedRole"
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

|   |                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Since `curl` uses brackets (`[]`, `{}`) for processing, you need to escape your brackets with a `\`. This may be unnecessary when you use a different method to call PingIDM. |

### Page query results

The common filter query mechanism supports paged query results for managed objects, and for some system objects, depending on the system resource. There are two ways to page objects in a query:

* Using a cookie based on the value of a specified sort key.

* Using an offset that specifies how many records should be skipped before the first result is returned.

These methods are implemented with the following query parameters:

* `_pagedResultsCookie`

  Opaque cookie used by the server to keep track of the position in the search results. The format of the cookie is a base-64 encoded version of the value of the unique sort key property. The value of the returned cookie is URL-encoded to prevent values such as `+` from being incorrectly translated.

  You cannot page results without sorting them (using the `_sortKeys` parameter). If you do not specify a sort key, the `_id` of the record is used as the default sort key. At least one of the specified sort key properties must be a unique value property, such as `_id`.

  |   |                                                                                                                                                                                                                                                                                                                  |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | For paged searches on generic mappings, you should sort on the `_id` property, because this is the only property that is stored outside of the JSON blob. If you sort on something other than `_id`, the search will incur a performance hit because PingIDM has to pull the entire result set and then sort it. |

  The server provides the cookie value on the first request. You should then supply the cookie value in subsequent requests until the server returns a null cookie, meaning that the final page of results has been returned.

  The `_pagedResultsCookie` parameter is supported only for filtered queries, that is, when used with the `_queryFilter` parameter. You cannot use the `_pagedResultsCookie` with a `_queryId`.

  The `_pagedResultsCookie` and `_pagedResultsOffset` parameters are mutually exclusive and cannot be used together.

  Paged results are enabled only if the `_pageSize` is a non-zero integer.

* `_pagedResultsOffset`

  Specifies the index within the result set of the number of records to be skipped before the first result is returned. The format of the `_pagedResultsOffset` is an integer value. When the value of `_pagedResultsOffset` is greater than or equal to 1, the server returns pages, starting after the specified index.

  This request assumes that the `_pageSize` is set, and not equal to zero.

  For example, if the result set includes 10 records, the `_pageSize` is 2, and the `_pagedResultsOffset` is 6, the server skips the first 6 records, then returns 2 records, 7 and 8. The `_remainingPagedResults` value would be 2, the last two records (9 and 10) that have not yet been returned.

  If the offset points to a page beyond the last of the search results, the result set returned is empty.

* `_pageSize`

  An optional parameter indicating that query results should be returned in pages of the specified size. For all paged result requests other than the initial request, a cookie should be provided with the query request.

  The default behavior is not to return paged query results. If set, this parameter should be an integer value, greater than zero.

  When a `_pageSize` is specified, and non-zero, the server calculates the `totalPagedResults` in accordance with the `totalPagedResultsPolicy` and provides the value as part of the response. If a count policy is specified (`_totalPagedResultsPolicy=EXACT`), the `totalPagedResults` returns the total result count. If no count policy is specified in the query, or if `_totalPagedResultsPolicy=NONE`, result counting is disabled, and the server returns a value of -1 for `totalPagedResults`. The following example shows a query that requests two results with a `totalPagedResultsPolicy` of `EXACT`:

  ```
  curl \
  --header "Authorization: Bearer <access-token>" \
  --header "Accept-API-Version: resource=1.0" \
  --request GET \
  "https://<tenant-env-fqdn>/openidm/managed/realm-name_user?_queryFilter=true&_pageSize=2&_totalPagedResultsPolicy=EXACT"
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

  The `totalPagedResults` and `_remainingPagedResults` parameters are not supported for all queries. Where they are not supported, their returned value is always `-1`. In addition, counting query results using these parameters is not currently supported for a DS repository.

  Requesting the total result count (with `_totalPagedResultsPolicy=EXACT`) incurs a performance cost on the query.

  Queries that return large data sets will have a significant impact on heap requirements, particularly if they are run in parallel with other large data requests. To avoid out of memory errors, analyze your data requirements, set the heap configuration appropriately, and modify access controls to restrict requests on large data sets.

### Sort query results

For common filter query expressions, you can sort the results of a query using the `_sortKeys` parameter. This parameter takes a comma-separated list as a value and orders the way the JSON result is returned based on this list.

The `_sortKeys` parameter is not supported for predefined queries.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * Pagination using `_pageSize` is recommended if you intend to use `_sortKeys`. If you do not paginate your query, the data you are querying must be indexed.

* When viewing data that is persisted in Advanced Identity Cloud's data store and sorted by un-indexed `_sortKeys`, the `_pageSize` parameter must be less than or equal to the `index-entry-limit` as configured in DS (default value is 4000). |

The following query returns all users with the `givenName` Dan and sorts the results alphabetically, according to surname (`sn`):

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
'https://<tenant-env-fqdn>/openidm/system/ldap/account?_queryFilter=givenName+eq+"Dan"&_fields=givenName,sn&_sortKeys=sn'
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

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | When you query a relationship field, fields that belong to the related object are not available as `_sortKeys`. For example, if you query a list of a manager's reports, you cannot sort by the reports' last names. This is because the available `_sortKeys` are based on the object being queried, which in the case of [relationships](relationships.html) is a list of references to other objects, not the objects themselves. |

### Recalculate properties based on other properties (virtual) in queries

For managed objects, PingIDM includes an [*onRetrieve*](../idm-scripting/script-triggers-managedConfig.html#managed_object_configuration_object) script hook that enables you to recalculate property values, known as [virtual properties](managed-object-virtual-properties.html), when an object is retrieved as the result of a query. To use the `onRetrieve` trigger, the query must include the `executeOnRetrieve` parameter, for example:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
'https://<tenant-env-fqdn>/openidm/managed/realm-name_user?_queryFilter=sn+eq+"Jensen"&executeOnRetrieve=true'
```

If a query includes `executeOnRetrieve`, the query recalculates virtual property values, based on the current state of the system. The result of the query will be the same as a `read` on a specific object, because reads always recalculate virtual property values.

If a query does not include `executeOnRetrieve`, the query returns the virtual properties of an object based on the value that is persisted in the repository. Virtual property values are not recalculated.

For performance reasons, `executeOnRetrieve` is `false` by default.

|   |                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Virtual properties that use [*queryConfig*](managed-object-virtual-properties.html#relationship-derived-virtual-properties) for calculation instead of an `onRetrieve` script are not recalculated by `executeOnRetrieve`. These properties are recalculated only when there is a change (such as adding or removing a role affecting `effectiveRoles`, or a temporal constraint being triggered or changed). |

---

---
title: Effective roles and effective assignments
description: Understand virtual properties calculated from role and assignment relationships
component: pingoneaic
page_id: pingoneaic:idm-objects:effective-roles-and-assignments
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-objects/effective-roles-and-assignments.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Roles", "Assignments", "Virtual Properties"]
---

# Effective roles and effective assignments

*Effective roles* and *effective assignments* are virtual properties of a user object. IDM uses the relationships between objects to know when to recalculate the values of these properties.

The relationships between objects are configured using the `notify`, `notifySelf`, and `notifyRelationships` settings for `managed/realm-name_user`, `managed/realm-name_role`, and `managed/realm-name_assignment`. The `queryConfig` property is used to configure which related objects to traverse for this calculation.

Calculation or recalculation is performed when IDM notifies the related objects that the roles or assignments for a managed user have been added, removed, or changed.

The following excerpt of the IDM managed object schema shows how these two virtual properties are constructed for each managed user object:

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

When a user references a role which references an assignment, that user automatically references the assignment in its list of effective assignments.

`effectiveRoles` uses the `roles` relationship to calculate the grants currently in effect, including any qualified by temporal constraints.

`effectiveAssignments` uses the `roles` relationship and the `assignments` relationship for each role to calculate the current assignments in effect for that user. The synchronization engine reads the calculated value of the `effectiveAssignments` attribute when it processes the user. The target system is updated according to the configured `assignmentOperation` for each assignment.

When a user's roles or assignments are updated, IDM calculates their `effectiveRoles` and `effectiveAssignments` based on the current value of their `roles` property and the `assignments` property of any roles referenced by that property. The previous set of examples showed the creation of a role `employee` that referenced an assignment `employee` and was granted to user bjensen. Querying that user entry would show the following effective roles and effective assignments:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/managed/realm-name_user/<bjensenUUID>?_fields=userName,roles,effectiveRoles,effectiveAssignments"
{
  "_id": "ca8855fd-a404-42c7-88b7-02f8a8a825b2",
  "_rev": "0000000081eebe1a",
  "userName": "bjensen",
  "effectiveRoles": [
    {
      "_refResourceCollection": "managed/realm-name_role",
      "_refResourceId": "2243f5f8-ed75-4c3b-b4b3-058d5c58fbb4"
      "_ref": "managed/realm-name_role/2243f5f8-ed75-4c3b-b4b3-058d5c58fbb4"
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
      "_refResourceCollection": "managed/realm-name_assignment",
      "_refResourceId": "46befacf-a7ad-4633-864d-d93abfa561e9",
      "_ref": "managed/realm-name_assignment/46befacf-a7ad-4633-864d-d93abfa561e9"
    }
  ],
  "roles": [
    {
      "_ref": "managed/realm-name_role/2243f5f8-ed75-4c3b-b4b3-058d5c58fbb4",
      "_refResourceCollection": "managed/realm-name_role",
      "_refResourceId": "2243f5f8-ed75-4c3b-b4b3-058d5c58fbb4",
      "_refProperties": {
        "_id": "93552530-10fa-49a4-865f-c942dffd2801",
        "_rev": "0000000081ed9f2b"
      }
    }
  ]
}
```

In this example, synchronizing the `managed/realm-name_user` repository with the external LDAP system defined in the mapping populates user bjensen's `employeeType` attribute in LDAP with the value `employee`.

---

---
title: Enable self-service by tracking user metadata
description: Track user metadata for self-service features like progressive profile and consent
component: pingoneaic
page_id: pingoneaic:idm-objects:object-meta-data
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-objects/object-meta-data.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Metadata"]
---

# Enable self-service by tracking user metadata

Some self-service features, such as [progressive profile completion](../self-service/progressive-profile.html), [privacy and consent](../self-service/self-registration.html#privacy-consent), and [acceptance of terms and conditions](../self-service/self-registration.html#terms-conditions), rely on user *metadata* that tracks information related to a managed object state.

For example, this data might include when the object was created or the date of the most recent change. This metadata is not stored within the object itself but in a **separate** resource location.

In Advanced Identity Cloud, metadata is only tracked for `managed/alpha_user` and `managed/bravo_user` managed objects.

|   |                                                                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you are not using the self-service features that require metadata, you can remove the `meta` stanza from the two managed objects in the schema. Preventing the creation and tracking of metadata where it is not required improves performance. |

The metadata configuration includes the following properties:

* `property`

  The property dynamically added to the managed object schema for this object.

* `resourceCollection`

  The resource location where the metadata is stored.

  Metadata is stored under `ou=usermeta,ou=internal,dc=openidm,dc=forgerock,dc=com` by default.

  You must include the `ou` specified in the preceding `dnTemplate` attribute.

* `trackedProperties`

  The properties tracked as metadata for this object. In the [following example](#track-user-metadata-example), the `createDate` (when the object was created) and the `lastChanged` date (when the object was last modified) are tracked.

You cannot search on metadata, and it is not returned by the results of a query, unless it is specifically requested. To return all metadata for an object, include `_fields=,_meta/*` in your request. The following example returns a user entry **without** requesting the metadata:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/managed/realm-name_user/bjensen"
{
  "_id": "bjensen",
  "_rev": "000000000444dd1a",
  "mail": "bjensen@example.com",
  "givenName": "Barbara",
  "sn": "Jensen",
  "description": "Created By CSV",
  "userName": "bjensen",
  "telephoneNumber": "1234567",
  "accountStatus": "active",
  "effectiveRoles": [],
  "effectiveAssignments": []
}
```

The following example returns the same user entry, **with metadata**:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/managed/realm-name_user/bjensen?_fields=,_meta/*"
{
  "_id": "bjensen",
  "_rev": "000000000444dd1a",
  "mail": "bjensen@example.com",
  "givenName": "Barbara",
  "sn": "Jensen",
  "description": "Created By CSV",
  "userName": "bjensen",
  "telephoneNumber": "1234567",
  "accountStatus": "active",
  "effectiveRoles": [],
  "effectiveAssignments": []
  "_meta": {
    "_ref": "internal/usermeta/284273ff-5e50-4fa4-9d30-4a3cf4a5f642",
    "_refResourceCollection": "internal/usermeta",
    "_refResourceId": "284273ff-5e50-4fa4-9d30-4a3cf4a5f642",
    "_refProperties": {
      "_id": "30076e2e-8db5-4b4d-ab91-5351d2da4620",
      "_rev": "000000001ad09f00"
    },
    "createDate": "2018-04-12T19:53:19.004Z",
    "lastChanged": {
      "date": "2018-04-12T19:53:19.004Z"
    },
    "loginCount": 0,
    "_rev": "0000000094605ed9",
    "_id": "284273ff-5e50-4fa4-9d30-4a3cf4a5f642"
  }
}
```

|   |                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Apart from the `createDate` and `lastChanged` shown previously, the request also returns the `loginCount`. This property is stored by default and increments with each login request based on password or social authentication. |

The request also returns a `_meta` property that includes [relationship](relationships.html) information. IDM uses the relationship model to store the metadata. When the `meta` stanza is added to the user object definition, the attribute specified by the `property` (`"property" : "_meta",` in this case) is added to the schema as a uni-directional relationship to the resource collection specified by `resourceCollection`.

In this example, the user object's `_meta` field is stored as an `internal/usermeta` object. The `_meta/_ref` property shows the full resource path to the internal object where the metadata for this user is stored.

---

---
title: Extend functionality through scripts
description: Extend managed object functionality using script hooks at various lifecycle stages
component: pingoneaic
page_id: pingoneaic:idm-objects:managed-objects-scripts
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-objects/managed-objects-scripts.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Scripts"]
---

# Extend functionality through scripts

|   |                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Before implementing a script, it's highly recommended that you validate the script over [REST](../idm-scripting/script-endpoint.html). Use scripts in a test environment before deploying them to a production environment. |

A number of *script hooks* let you manipulate managed objects using scripts. Scripts can be triggered during various stages of the lifecycle of the managed object, and are defined in the managed object schema.

You can trigger scripts when a managed object is:

* Created (onCreate)

* Deleted (onDelete)

* Read (onRead)

* Retrieved (onRetrieve)

* Stored in the repository (onStore)

* Synchronized (onSync)

* Updated (onUpdate)

* Validated (onValidate)

Post-action scripts let you manipulate objects after they are:

* Created (postCreate)

* Updated (postUpdate)

* Deleted (postDelete)

Learn more about the scripts triggered by these script hooks in [managed object configuration properties](appendix-managed-objects.html#managed-object-configuration-properties).

---

---
title: Grant relationships conditionally
description: Grant relationships dynamically based on conditions or query filters
component: pingoneaic
page_id: pingoneaic:idm-objects:conditional-relationships
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-objects/conditional-relationships.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Relationships"]
---

# Grant relationships conditionally

Relationships can be granted dynamically, based on a specified condition. In order to conditionally grant a relationship, the schemas for the resources you are creating a relationship between need to be configured to support conditional association. To do this, three fields in the schema are used:

* `conditionalAssociation`

  Boolean. This property is applied to the `resourceCollection` for the grantor of the relationship. For example, the `members` relationship on `managed/realm-name_role` specifies that there is a conditional association with the `managed/realm-name_user` resource:

  ```json
  "resourceCollection" : [
    {
      "notify" : true,
      "conditionalAssociation" : true,
      "path" : "managed/realm-name_user",
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

  String. This property specifies the field used to determine whether a conditional relationship is granted. The field is applied to the `resourceCollection` of the grantee of the relationship. For example, the `roles` relationship on `managed/realm-name_user` specifies that the conditional association with `managed/realm-name_role` is defined by the `condition` field in `managed/realm-name_role`.

  ```json
  "resourceCollection" : [
    {
      "path" : "{managed_role}",
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

  |   |                                                                                                                                                                   |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If you are using the default schema, the field name is usually the `condition` but can be any field that evaluates a condition and is flagged as `isConditional`. |

* `isConditional`

  Boolean. This property is applied to the field to check whether membership in a relationship is granted. You can only mark one field on a resource as `isConditional`. For example, in the relationship between `managed/realm-name_user` and `managed/realm-name_role`, conditional membership in the relationship is determined by the query filter specified in the `managed/realm-name_role` `condition` field:

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
title: Groups
description: Manage groups to simplify permissions and authorizations for user collections
component: pingoneaic
page_id: pingoneaic:idm-objects:groups
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-objects/groups.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Groups", "Relationships"]
---

# Groups

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Groups may not be enabled in your tenant. To check if groups are enabled, from the Advanced Identity Cloud admin console, go to Identities > Manage. If Alpha realm - Groups is present, then groups are enabled.If this is not present, enable groups using the [Feature enablement](../idm-rest-api/endpoints/rest-feature.html) endpoint.If you previously used AM static groups, create a Ping Identity [support case](https://support.pingidentity.com/s/) for guidance on how to migrate group membership to managed groups. |

Groups are an important tool for identity management because they simplify managing collections of users by applying permissions and authorizations to all members of a group rather than to individual users. Groups may follow an organization structure or be based on the needs and privileges of an arbitrary set of users.

The managed *group* object is a default managed object type and is defined like any other managed object type. Managed groups simplify management by using common groups across the entire platform.

Users are made members of groups through the [relationships](relationships.html) mechanism. You should understand how relationships work before you read about IDM groups.

A group can be assigned to a user manually, as a static value of the user's `groups` attribute, or dynamically, as a result of a condition or script. For example, a user might be assigned to a group such as `sales` dynamically, if that user is in the `sales` organization.

A user's `groups` attribute takes an array of *references* as a value, where the references point to the managed groups. For example, if user bjensen has been assigned to two groups (`employees` and `supervisors`), the value of bjensen's `groups` attribute would look something like the following:

```json
"groups": [
  {
    "_ref": "managed/realm-name_group/employees",
    "_refResourceCollection": "managed/realm-name_group",
    "_refResourceId": "employees",
    "_refProperties": {
      "_id": "38a23ddc-1345-48d6-b753-ad97f472a90e",
      "_rev": "ae6e63c4-94f5-463b-8bef-7a359b8e3004-1692"
    }
  },
  {
    "_ref": "managed/realm-name_group/supervisors",
    "_refResourceCollection": "managed/realm-name_group",
    "_refResourceId": "supervisors",
    "_refProperties": {
      "_id": "0fabd212-f0c2-4d91-91f2-2b211bb58e89",
      "_rev": "ae6e63c4-94f5-463b-8bef-7a359b8e3004-1974"
    }
  }
]
```

|   |                                                                                                                                                                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | We recommend you use managed objects for all data management in Advanced Identity Cloud. While managed groups display in the AM admin UI and can serve the same function as a static group created in AM, they are not the same. A managed group supports dynamic, conditional membership you can leverage in other parts of Advanced Identity Cloud. |

The `_refResourceCollection` is the container that holds the group. The `_refResourceId` is the ID of the group. The `_ref` property is a resource path derived from the `_refResourceCollection` and the URL-encoded `_refResourceId`. `_refProperties` provides more information about the relationship.

|   |                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | In most cases, Advanced Identity Cloud uses UUIDs as the `_id` for managed objects. Managed groups are an exception: the `_id` and `name` properties should match. |

---

---
title: Grow organizations downward if possible
description: Optimize organization hierarchy growth patterns in high-latency network environments
component: pingoneaic
page_id: pingoneaic:idm-objects:orgs-in-high-latency-environments
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-objects/orgs-in-high-latency-environments.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Organizations", "Virtual Properties"]
---

# Grow organizations downward if possible

The relationship-derived virtual properties that support the organization model are calculated in response to relationship signals that travel *down* the organization tree hierarchy. For example, suppose you:

* Add a new root organization to an existing organization hierarchy

* Add a new admin or owner to the root organization in an existing organization hierarchy

The relationship signals that trigger relationship-derived virtual property calculation are propagated down to all organizations in the organization hierarchy, and to all the members of the organizations in the hierarchy. This updates their relationship-derived virtual property state.

If there are many thousands of members of the organizations in the hierarchy, such an operation can take a long time to complete. Because of this, it is a best practice to grow organization hierarchies *downward*, adding new organizations as leaves of an existing hierarchy, and adding new admins and members to the leaves in the hierarchy tree. This is preferable to growing the hierarchy *upwards*, starting with the leaves, and then growing the hierarchy up towards the root organization.

If you *must* add a new root to an existing organization hierarchy with many organizations and many members, or add a new admin or owner to an organization near the top of the hierarchy, perform the operations over the command line, using the examples in [Manage organizations over REST](manage-orgs-rest.html).

---

---
title: Manage custom relationship properties
description: Create custom relationship properties between managed objects
component: pingoneaic
page_id: pingoneaic:idm-objects:relationships-custom
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-objects/relationships-custom.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Relationships"]
page_aliases: ["release-notes:rapid-channel/custom-relationships-schema.adoc"]
section_ids:
  custom-relationships-legacy: Manage custom relationships in the IDM native admin console
  create_a_custom_relationship: Create a custom relationship
  update_a_custom_relationship: Update a custom relationship
  delete_a_custom_relationship_property: Delete a custom relationship property
---

# Manage custom relationship properties

Custom relationship properties allow you to define custom relationships between managed objects. For example, you could model a parent-child relationship by creating the `custom_Parents` and `custom_Children` properties and configuring them as one-way one-to-many relationships.

You can manage relationships in the following ways:

* The Advanced Identity Cloud admin console (recommended). Learn more in [Configure relationships](../identities/configure-relationships.html).

* The [IDM native admin console](#custom-relationships-legacy)

* The Schema API. Learn more in [Schema](../idm-rest-api/endpoints/rest-schema.html).

|   |                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Only use the Advanced Identity Cloud admin console, IDM native admin console, or the Schema API to manage relationships. Using other methods might cause your data to de-sync. |

## Manage custom relationships in the IDM native admin console

### Create a custom relationship

To create a custom relationship property using the Advanced Identity Cloud admin console:

1. In the Advanced Identity Cloud admin console, click Native Consoles > Identity Management.

2. From the top navigation menu, click Configure > Managed Objects.

3. Select a managed object type.

4. Click Add a Property. An entry field displays.

5. In the Name field, enter a name for the custom relationship property. The name must begin with the string `custom_`, such as `custom_Example`.

6. From the Type drop-down, select Relationship.

7. Click Next. The Add Resources modal displays.

8. From the Resource drop-down, select the resource to map the custom relationship property to.

9. From the Display Properties drop-down, select the properties on the resource to map to the custom relationship property.

10. Click Save. The Relationships Property screen for the new relationship property displays.

|   |                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Objects are limited to 10 custom relationships. If you need an object to have more, create custom relationships from the related object and map them to the original object. |

### Update a custom relationship

You can adjust a custom relationship's **cardinality** by configuring each side of the relationship to have one, many, or none of the other side. For instance, `custom_Managers` might have many `custom_Employees`, while `custom_Employees` have only one `custom_Managers`.

To change the cardinality of a custom relationship using the Advanced Identity Cloud admin console:

1. In the Advanced Identity Cloud admin console, click Native Consoles > Identity Management.

2. From the top navigation menu, click Configure > Managed Objects.

3. Click the managed object type which has the relationship property to modify.

4. Click the relationship property to modify.

5. In the Relationship Configuration section, click the cardinality relationship name associated with the arrow indicating the direction of the relationship. A popover displays.

6. From the Relationship drop-down on the popover, select the cardinality of the relationship. The Changes Pending notification displays in the lower left of the UI.

7. Click Save.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When you change the configuration of a custom relationship, existing objects which contain that custom relationship aren't automatically updated to match the new configuration. Ensure your data is updated to reflect the new relationship configuration.For example, suppose `custom_Doctors` have many `custom_Patients` and `custom_Patients` have many `custom_Doctors`. The rules change and now `custom_Patients` have one `custom_Doctor`. In addition to updating the custom relationship's cardinality in the configuration, you must also update all existing `custom_Patients` with more than one `custom_Doctor` to have at most one. |

### Delete a custom relationship property

Existing objects are not automatically updated when you delete a custom relationship property. When you delete a custom relationship property, you must also update the existing objects to no longer reference them. Failing to do this may result in the "orphaned" data unpredictably reappearing if Advanced Identity Cloud reuses the deleted reference attribute for other data.

Before you delete a custom relationship property, find all the managed objects in the custom relationship and either modify or delete the data. The following REST API query returns all managed users with the property `custom_Example`:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=2.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/managed/user?_queryFilter=/custom_Example+pr&_pageSize=30"
```

For more information on using the REST API to manage custom relationship properties, refer to [Schema](../idm-rest-api/endpoints/rest-schema.html).

---

---
title: Manage groups
description: Create and manage groups to organize users and apply permissions
component: pingoneaic
page_id: pingoneaic:idm-objects:manage-groups
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-objects/manage-groups.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Groups", "REST API"]
section_ids:
  create-a-group: Create a group
  using_rest: Using REST
  using_the_advanced_identity_cloud_admin_console: Using the Advanced Identity Cloud admin console
  list-groups: List groups
  using_rest_2: Using REST
  using_the_advanced_identity_cloud_admin_console_2: Using the Advanced Identity Cloud admin console
  add-users-to-group: Add users to a group
  add-members-statically: Add group members statically
  using_rest_3: Using REST
  using_the_advanced_identity_cloud_admin_console_3: Using the Advanced Identity Cloud admin console
  add-members-dynamically: Add group members dynamically
  using_rest_4: Using REST
  using_the_advanced_identity_cloud_admin_console_4: Using the Advanced Identity Cloud admin console
  querying-user-groups: Query a user's group memberships
  using_rest_5: Using REST
  using_the_advanced_identity_cloud_admin_console_5: Using the Advanced Identity Cloud admin console
  remove-group-member: Remove a member from a group
  using_rest_6: Using REST
  using_the_advanced_identity_cloud_admin_console_6: Using the Advanced Identity Cloud admin console
  delete-group: Delete a group
  using_rest_7: Using REST
  using_the_advanced_identity_cloud_admin_console_7: Using the Advanced Identity Cloud admin console
---

# Manage groups

You can manage groups over REST or by using the Advanced Identity Cloud admin console.

You can perform the following actions with groups:

* [Create a group](#create-a-group)

* [List groups](#list-groups)

* [Add users to a group](#add-users-to-group)

* [Query a user's group memberships](#querying-user-groups)

* [Remove a member from a group](#remove-group-member)

* [Delete a group](#delete-group)

## Create a group

You can create groups using REST or by using the Advanced Identity Cloud admin console.

### Using REST

To create a group, send a PUT or POST request to the `/openidm/managed/realm-name_group` context path. The following example creates a group named `employees`, with ID `employees`:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request POST \
--data '{
  "name": "employees",
  "description": "Group that includes temporary and permanent employees"
}' \
"https://<tenant-env-fqdn>/openidm/managed/realm-name_group?_action=create"
{
  "_id": "employees",
  "_rev": "ae6e63c4-94f5-463b-8bef-7a359b8e3004-1028",
  "name": "employees",
  "condition": null,
  "description": "Group that includes temporary and permanent employees"
}
```

You can also omit `?_action=create` and achieve the same result:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request POST \
--data '{
  "name": "employees2",
  "description": "Second group that includes temporary and permanent employees"
}' \
"https://<tenant-env-fqdn>/openidm/managed/realm-name_group"
{
  "_id": "employees2",
  "_rev": "ae6e63c4-94f5-463b-8bef-7a359b8e3004-1053",
  "name": "employees2",
  "condition": null,
  "description": "Second group that includes temporary and permanent employees"
}
```

### Using the Advanced Identity Cloud admin console

1. From the navigation bar, click Identities > Manage > Alpha realm - Groups.

2. On the Groups page, click New Alpha realm - Group.

3. On the New Alpha realm - Group page, enter a name and description, and click Next.

4. Optionally, create a conditional filter to assign the group dynamically. Conditional filters are custom rules you create that, when met, assign the user to your group automatically.

5. Click Save.

## List groups

### Using REST

To list groups over REST, query the `openidm/managed/realm-name_group` endpoint. The following example shows the `employees` group that you created in the previous example:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/managed/realm-name_group?_queryFilter=true"
{
  "result": [
    {
      "_id": "employees",
      "_rev": "ae6e63c4-94f5-463b-8bef-7a359b8e3004-1028",
      "name": "employees",
      "condition": null,
      "description": "Group that includes temporary and permanent employees"
    },
    {
      "_id": "employees2",
      "_rev": "ae6e63c4-94f5-463b-8bef-7a359b8e3004-1053",
      "name": "employees2",
      "condition": null,
      "description": "Second group that includes temporary and permanent employees"
    }
  ],
  "resultCount": 2,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": -1
}
```

### Using the Advanced Identity Cloud admin console

To list the managed groups in the Advanced Identity Cloud admin console, select Identities > Manage > Alpha realm - Groups.

## Add users to a group

You add users to a group through the relationship mechanism. [Relationships](relationships.html) are references from one managed object to another; in this case, from a user object to a group object. For more information, refer to [Relationships between objects](relationships.html).

You can add group members *statically* (manually) or *dynamically* (automated assigning through rules).

To add members statically, do one of the following:

* Update the value of the user's `groups` property to reference the group.

* Update the value of the group's `members` property to reference the user.

Dynamic groups use the result of a condition or script to update a user's list of groups.

### Add group members statically

Add a user to a group statically using the REST interface or the Advanced Identity Cloud admin console.

#### Using REST

Use one of the following methods to add group members over REST:

* Add the user as a group member. The following example adds user scarter as a member of the `employees` group:

  ```
  curl \
  --header "Authorization: Bearer <access-token>" \
  --header "Accept-API-Version: resource=1.0" \
  --header "Content-Type: application/json" \
  --request POST \
  --data '{
    "_ref":"managed/realm-name_user/d5b52064-6571-488a-8d85-440a99ed00d4"
  }' \
  "https://<tenant-env-fqdn>/openidm/managed/realm-name_group/employees/members?_action=create"
  {
    "_id": "7ab79f9b-70cc-4205-acec-e675a55c9bcf",
    "_rev": "ae6e63c4-94f5-463b-8bef-7a359b8e3004-1479",
    "_ref": "managed/realm-name_user/d5b52064-6571-488a-8d85-440a99ed00d4",
    "_refResourceCollection": "managed/realm-name_user",
    "_refResourceId": "d5b52064-6571-488a-8d85-440a99ed00d4",
    "_refProperties": {
      "_id": "7ab79f9b-70cc-4205-acec-e675a55c9bcf",
      "_rev": "ae6e63c4-94f5-463b-8bef-7a359b8e3004-1479"
    }
  }
  ```

  |   |                                                                                                                 |
  | - | --------------------------------------------------------------------------------------------------------------- |
  |   | This is the preferred method as it does not incur an unnecessary performance cost for groups with many members. |

* Update the user's `groups` property.

  The following example adds the `employees` group to user scarter:

  ```
  curl \
  --header "Authorization: Bearer <access-token>" \
  --header "Accept-API-Version: resource=1.0" \
  --header "Content-Type: application/json" \
  --request PATCH \
  --data '[
    {
      "operation": "add",
      "field": "/groups/-",
      "value": {"_ref" : "managed/realm-name_group/employees2"}
    }
  ]' \
  "https://<tenant-env-fqdn>/openidm/managed/realm-name_user/d5b52064-6571-488a-8d85-440a99ed00d4"
  {
    "_id": "d5b52064-6571-488a-8d85-440a99ed00d4",
    "_rev": "ae6e63c4-94f5-463b-8bef-7a359b8e3004-1569",
    "country": null,
    "telephoneNumber": null,
    "mail": "scarter@example.com",
    "memberOfOrgIDs": [],
    "city": null,
    "displayName": null,
    "assignedDashboard": [],
    "effectiveAssignments": [],
    "postalCode": null,
    "description": null,
    "profileImage": null,
    "expireAccount": null,
    "accountStatus": "active",
    "aliasList": [],
    "kbaInfo": [],
    "inactiveDate": null,
    "activeDate": null,
    "consentedMappings": [],
    "sn": "Carter",
    "effectiveGroups": [
      {
        "_refResourceCollection": "managed/realm-name_group",
        "_refResourceId": "employees",
        "_ref": "managed/realm-name_group/employees"
      },
      {
        "_refResourceCollection": "managed/realm-name_group",
        "_refResourceId": "employees2",
        "_ref": "managed/realm-name_group/employees2"
      }
    ],
    "preferences": null,
    "organizationName": null,
    "givenName": "Sam",
    "stateProvince": null,
    "userName": "scarter",
    "postalAddress": null,
    "effectiveRoles": [],
    "activateAccount": null
  }
  ```

  When you update a user's existing groups array, use the `-` special index to add the new value to the set. For more information, refer to *Set semantic arrays* in [Patch](../developer-docs/crest/patch.html).

* Update the group's `members` property to refer to the user.

  The following sample command makes scarter a member of the `employees` group:

  ```
  curl \
  --header "Authorization: Bearer <access-token>" \
  --header "Accept-API-Version: resource=1.0" \
  --header "Content-Type: application/json" \
  --request PATCH \
  --data '[
    {
      "operation": "add",
      "field": "/members/-",
      "value": {"_ref" : "managed/realm-name_user/d5b52064-6571-488a-8d85-440a99ed00d4"}
    }
  ]' \
  "https://<tenant-env-fqdn>/openidm/managed/realm-name_group/employees"
  {
    "_id": "employees",
    "_rev": "ae6e63c4-94f5-463b-8bef-7a359b8e3004-1028",
    "name": "employees",
    "condition": null,
    "description": "Group that includes temporary and permanent employees"
  }
  ```

  The `members` property of a group is not returned by default in the output. To show all members of a group, you must specifically request the `members` property. The following example lists the members of the `employees` group:

  ```
  curl \
  --header "Authorization: Bearer <access-token>" \
  --header "Accept-API-Version: resource=1.0" \
  --request GET \
  "https://<tenant-env-fqdn>/openidm/managed/realm-name_group/employees?_fields=name,members"
  {
    "_id": "employees",
    "_rev": "ae6e63c4-94f5-463b-8bef-7a359b8e3004-1028",
    "name": "employees",
    "members": [
      {
        "_ref": "managed/realm-name_user/d5b52064-6571-488a-8d85-440a99ed00d4",
        "_refResourceCollection": "managed/realm-name_user",
        "_refResourceId": "d5b52064-6571-488a-8d85-440a99ed00d4",
        "_refProperties": {
          "_id": "38a23ddc-1345-48d6-b753-ad97f472a90e",
          "_rev": "ae6e63c4-94f5-463b-8bef-7a359b8e3004-1692"
        }
      }
    ]
  }
  ```

#### Using the Advanced Identity Cloud admin console

Use one of the following UI methods to add members to a group:

* Update the user entry:

  1. Select Identities > Manage > Alpha realm - Users and select the user to add.

  2. Select the Group tab and click Add Groups.

     1. Select the group from the Groups list and click Save.

* Update the group entry:

  1. Select Identities > Manage > Alpha realm - Groups and select the group to which you want to add members.

  2. Select the Members tab and click Add Members.

  3. Select the user from the Members list and click Save.

### Add group members dynamically

To add a member to a group *dynamically*, use a *condition*, expressed as a query filter, in the group definition. If the condition is `true` for a member, they are added to the group. A conditional group is a group whose members are based on a defined condition, which you can specify when you [create](#create-a-group) or [modify](#manage-groups) a group. You can create a condition after you create the group as well.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You must configure the properties you use to create a conditional filter for a group as `searchable`. To configure a property as `searchable`, update its definition in your managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint.)*. You can find more information in [General purpose extension attributes](../identities/customize-object-types.html#use-general-purpose-extension-attributes). |

When you create or update a conditional group, Advanced Identity Cloud performs the following actions:

* Assesses all managed users

* Recalculates the value of the user's `group` property. This only takes place if the user is a member of the group.

* If you remove a condition from a group and members in the group are now not a part of the condition, all members are removed from the group and their `group` property is updated.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When you define a conditional group in a data set, every user entry (including the mapped entries on remote systems) updates with the relationships implied by that conditional group. The time that it takes to create a new conditional group is impacted by the number of managed users affected by the condition.In a data set with a large number of users, creating a new conditional group can incur a significant performance cost when you create it. If possible, set up your conditional groups at the beginning of your deployment to avoid performance issues later. |

#### Using REST

To create a conditional group over REST, include the query filter as a value of the `condition` property in the group definition. The following example creates a group, `fr-employees`, whose members will be only users who live in France (whose `country` property is set to `FR`):

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request POST \
--data '{
  "name": "fr-employees",
  "description": "Group for employees resident in France",
  "condition": "/country eq \"FR\""
}' \
"https://<tenant-env-fqdn>/openidm/managed/realm-name_group?_action=create"
{
  "_id": "fr-employees",
  "_rev": "ae6e63c4-94f5-463b-8bef-7a359b8e3004-1898",
  "name": "fr-employees",
  "condition": "/country eq \"FR\"",
  "description": "Group for employees resident in France"
}
```

#### Using the Advanced Identity Cloud admin console

1. Select Identities > Manage > Alpha realm - Groups and select the group to add a condition to.

2. Select the Settings tab and click Set up.

3. Toggle the box and define the query filter to assess the condition.

4. Click Save.

## Query a user's group memberships

To list a user's groups, query their `groups` property.

### Using REST

The following example shows that scarter is a member of two groups — the `employees` group and the `supervisors` group:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/managed/realm-name_user/d5b52064-6571-488a-8d85-440a99ed00d4/groups?_queryFilter=true&_fields=_ref/*,name"
{
  "result": [
    {
      "_id": "38a23ddc-1345-48d6-b753-ad97f472a90e",
      "_rev": "ae6e63c4-94f5-463b-8bef-7a359b8e3004-1692",
      "_refResourceCollection": "managed/realm-name_group",
      "_refResourceId": "employees",
      "_refResourceRev": "ae6e63c4-94f5-463b-8bef-7a359b8e3004-1028",
      "name": "employees",
      "_ref": "managed/realm-name_group/employees",
      "_refProperties": {
        "_id": "38a23ddc-1345-48d6-b753-ad97f472a90e",
        "_rev": "ae6e63c4-94f5-463b-8bef-7a359b8e3004-1692"
      }
    },
    {
      "_id": "0fabd212-f0c2-4d91-91f2-2b211bb58e89",
      "_rev": "ae6e63c4-94f5-463b-8bef-7a359b8e3004-1974",
      "_refResourceCollection": "managed/realm-name_group",
      "_refResourceId": "supervisors",
      "_refResourceRev": "ae6e63c4-94f5-463b-8fbef-7a359b8e3004-1965",
      "name": "supervisors",
      "_ref": "managed/realm-name_group/supervisors",
      "_refProperties": {
        "_id": "0fabd212-f0c2-4d91-91f2-2b211bb58e89",
        "_rev": "ae6e63c4-94f5-463b-8bef-7a359b8e3004-1974"
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

### Using the Advanced Identity Cloud admin console

1. Select Identities > Manage > Alpha realm - Users, then select the user whose groups you want to check.

2. Select the Group tab.

## Remove a member from a group

To remove a static group membership from a user entry, do one of the following:

* Update the value of the user's `groups` property to remove the reference to the role.

* Update the value of the group's `members` property to remove the reference to that user.

You can use both of these methods over REST or by using the Advanced Identity Cloud admin console.

|   |                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | A delegated administrator must use PATCH to add or remove relationships.Conditional group membership can only be removed when the condition is changed or removed, or when the group itself is deleted. |

### Using REST

Use one of the following methods to remove a member from a group:

* DELETE the group from the user's `groups` property, including the reference ID (the ID of the relationship between the user and the group) in the delete request.

  The following example removes the `employees` group from user scarter. The ID required in the DELETE request is not the ID of the group but the reference `_id` of the relationship:

  ```
  curl \
  --header "Authorization: Bearer <access-token>" \
  --header "Accept-API-Version: resource=1.0" \
  --request DELETE \
  "https://<tenant-env-fqdn>/openidm/managed/realm-name_user/d5b52064-6571-488a-8d85-440a99ed00d4/groups/e450a32c-e289-49e3-8de5-b0f84e07c740"
  {
    "_id": "e450a32c-e289-49e3-8de5-b0f84e07c740",
    "_rev": "ae6e63c4-94f5-463b-8bef-7a359b8e3004-2122",
    "_ref": "managed/realm-name_group/employees",
    "_refResourceCollection": "managed/realm-name_group",
    "_refResourceId": "employees",
    "_refProperties": {
      "_id": "e450a32c-e289-49e3-8de5-b0f84e07c740",
      "_rev": "ae6e63c4-94f5-463b-8bef-7a359b8e3004-2122"
    }
  }
  ```

* PATCH the user entry to remove the group from the array of groups, specifying the *value* of the group object in the JSON payload.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | When you remove a group in this way, you must include the *entire object* in the value, as shown in the following example:```
  curl \
  --header "Content-type: application/json" \
  --header "Authorization: Bearer <access-token>" \
  --header "Accept-API-Version: resource=1.0" \
  --request PATCH \
  --data '[
    {
      "operation" : "remove",
      "field" : "/groups",
      "value" : {
        "_ref": "managed/realm-name_group/employees",
        "_refResourceCollection": "managed/realm-name_group",
        "_refResourceId": "employees",
        "_refProperties": {
          "_id": "731120c0-a4e9-4e27-b201-7442169e8b7c",
          "_rev": "ae6e63c4-94f5-463b-8bef-7a359b8e3004-2218"
        }
      }
    }
  ]' \
  "https://<tenant-env-fqdn>/openidm/managed/realm-name_user/d5b52064-6571-488a-8d85-440a99ed00d4"
  {
    "_id": "d5b52064-6571-488a-8d85-440a99ed00d4",
    "_rev": "ae6e63c4-94f5-463b-8bef-7a359b8e3004-2387",
    "country": null,
    "telephoneNumber": null,
    "mail": "scarter@example.com",
    "memberOfOrgIDs": [],
    "city": null,
    "displayName": null,
    "assignedDashboard": [],
    "effectiveAssignments": [],
    "postalCode": null,
    "description": null,
    "profileImage": null,
    "expireAccount": null,
    "accountStatus": "active",
    "aliasList": [],
    "kbaInfo": [],
    "inactiveDate": null,
    "activeDate": null,
    "consentedMappings": [],
    "sn": "Carter",
    "effectiveGroups": [
      {
        "_refResourceCollection": "managed/realm-name_group",
        "_refResourceId": "supervisors",
        "_ref": "managed/realm-name_group/supervisors"
      }
    ],
    "preferences": null,
    "organizationName": null,
    "givenName": "Sam",
    "stateProvince": null,
    "userName": "scarter",
    "postalAddress": null,
    "effectiveRoles": [],
    "activateAccount": null
  }
  ``` |

* DELETE the user from the group's `members` property, including the reference ID (the ID of the relationship between the user and the role) in the delete request.

  The following example first queries the members of the `employees` group, to obtain the ID of the relationship, then removes scarter's membership from that group:

  ```
  curl \
  --header "Authorization: Bearer <access-token>" \
  --header "Accept-API-Version: resource=1.0" \
  --request GET \
  "https://<tenant-env-fqdn>/openidm/managed/realm-name_group/employees/members?_queryFilter=true&_fields=_ref/*,name"
  {
    "result": [
      {
        "_id": "ef3261cd-a66f-4d3e-aad8-c0850e0b4a0e",
        "_rev": "ae6e63c4-94f5-463b-8bef-7a359b8e3004-2430",
        "_refResourceCollection": "managed/realm-name_user",
        "_refResourceId": "d5b52064-6571-488a-8d85-440a99ed00d4",
        "_refResourceRev": "ae6e63c4-94f5-463b-8bef-7a359b8e3004-2432",
        "_ref": "managed/realm-name_user/d5b52064-6571-488a-8d85-440a99ed00d4",
        "_refProperties": {
          "_id": "ef3261cd-a66f-4d3e-aad8-c0850e0b4a0e",
          "_rev": "ae6e63c4-94f5-463b-8bef-7a359b8e3004-2430"
        }
      }
    ],
    "resultCount": 1,
    "pagedResultsCookie": null,
    "totalPagedResultsPolicy": "NONE",
    "totalPagedResults": -1,
    "remainingPagedResults": -1
  }

  curl \
  --header "Authorization: Bearer <access-token>" \
  --header "Accept-API-Version: resource=1.0" \
  --request DELETE \
  "https://<tenant-env-fqdn>/openidm/managed/realm-name_group/employees/members/ef3261cd-a66f-4d3e-aad8-c0850e0b4a0e"
  {
    "_id": "ef3261cd-a66f-4d3e-aad8-c0850e0b4a0e",
    "_rev": "ae6e63c4-94f5-463b-8bef-7a359b8e3004-2430",
    "_ref": "managed/realm-name_user/d5b52064-6571-488a-8d85-440a99ed00d4",
    "_refResourceCollection": "managed/realm-name_user",
    "_refResourceId": "d5b52064-6571-488a-8d85-440a99ed00d4",
    "_refProperties": {
      "_id": "ef3261cd-a66f-4d3e-aad8-c0850e0b4a0e",
      "_rev": "ae6e63c4-94f5-463b-8bef-7a359b8e3004-2430"
    }
  }
  ```

### Using the Advanced Identity Cloud admin console

Use one of the following methods to remove a group member:

* Select Identities > Manage > Users and select the user whose group or groups you want to remove.

  Select the Group tab, select the group you want to remove, then select Remove.

* Select Identities > Manage > Groups, and select the group whose members you want to remove.

  Select the Members tab, select the member or members you want to remove, then select Remove.

## Delete a group

|   |                                                                                |
| - | ------------------------------------------------------------------------------ |
|   | Deleting a group removes all users in the group. This action cannot be undone. |

### Using REST

To delete a group over the REST interface, simply delete that managed object. The following command deletes the `employees` group created in the previous section:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request DELETE \
"https://<tenant-env-fqdn>/openidm/managed/realm-name_group/employees"
{
  "_id": "employees",
  "_rev": "ae6e63c4-94f5-463b-8bef-7a359b8e3004-1028",
  "name": "employees",
  "condition": null,
  "description": "Group that includes temporary and permanent employees"
}
```

### Using the Advanced Identity Cloud admin console

1. Select Identities > Manage > Alpha realm - Groups.

2. Select the group to delete.

3. Click then Delete Alpha realm - Group.

4. A confirmation dialog displays. Click Delete.

---

---
title: Manage identities
description: Retrieve, add, modify, and delete managed user identities over REST
component: pingoneaic
page_id: pingoneaic:idm-objects:users
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-objects/users.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Users", "Identities", "REST API"]
section_ids:
  managed_users_examples: Managed users examples
  retrieve_ids_of_all_managed_users_in_a_realm: Retrieve IDs of all managed users in a realm
  query_managed_users_for_a_specific_user: Query managed users for a specific user
  retrieve_a_managed_user_by_their_id: Retrieve a managed user by their ID
  add_a_user_with_a_specific_user_id: Add a user with a specific user ID
  add_a_user_with_a_system_generated_id: Add a user with a system-generated ID
  update_a_user: Update a user
  delete_a_user: Delete a user
---

# Manage identities

In Advanced Identity Cloud user identities are sometimes referred to as *managed users* or user managed objects. There are alpha users and bravo users.

To retrieve, add, change, and delete managed users, use one of the following methods:

* In the Advanced Identity Cloud admin console, any of the options in Identities > Manage > realm-name\_user.

* The REST interface at the context path `/openidm/managed/realm-name_user`.

## Managed users examples

The following examples show how to retrieve, add, change, and delete users over the REST interface. For more information on all the managed user endpoints and actions, refer to the [Managed users](../idm-rest-api/endpoints/rest-managed-users.html) endpoint.

### Retrieve IDs of all managed users in a realm

|   |                                                                                     |
| - | ----------------------------------------------------------------------------------- |
|   | The size of the returned set can be large when there are many users in your tenant. |

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/managed/realm-name_user?_queryFilter=true&_fields=_id"
{
  "result": [
    {
      "_id": "1dff18dc-ac57-4388-8127-dff309f80002",
      "_rev": "ceea2483-7f92-411e-9194-dcca0d61198e-48377"
    },
    {
      "_id": "7750881d-1622-451e-9ee5-71f7aaafcadf",
      "_rev": "ecf2cd07-f187-482e-9fa0-1127c267bce2-65781"
    },
    ...
  ],
  ...
}
```

### Query managed users for a specific user

You can return a subset of users based on a query. If the conditions are met, then the users are returned.

The `_queryFilter` requires double quotes, or the URL-encoded equivalent (`%22`), around the search term. This example uses the URL-encoded equivalent:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/managed/realm-name_user?_queryFilter=userName+eq+%22scarter%22"
{
  "result": [
    {
      "_id": "7750881d-1622-451e-9ee5-71f7aaafcadf",
      "_rev": "ecf2cd07-f187-482e-9fa0-1127c267bce2-65781",
      "userName": "scarter",
      "givenName": "Sam",
      "sn": "Carter",
      "telephoneNumber": "12345678",
      "active": "true",
      "mail": "scarter@example.com",
      "accountStatus": "active",
      "effectiveAssignments": [],
      "effectiveRoles": []
    }
  ],
  ...
}
```

This example uses single quotes around the URL to avoid conflicts with the double quotes around the search term:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
'https://<tenant-env-fqdn>/openidm/managed/realm-name_user?_queryFilter=userName+eq+"scarter"'
{
  "result": [
    {
      "_id": "7750881d-1622-451e-9ee5-71f7aaafcadf",
      "_rev": "ecf2cd07-f187-482e-9fa0-1127c267bce2-65781",
      "userName": "scarter",
      "givenName": "Sam",
      "sn": "Carter",
      "telephoneNumber": "12345678",
      "active": "true",
      "mail": "scarter@example.com",
      "accountStatus": "active",
      "effectiveAssignments": [],
      "effectiveRoles": []
    }
  ],
  ...
}
```

### Retrieve a managed user by their ID

In the following example, `7750881d-1622-451e-9ee5-71f7aaafcadf` is the UUID of the user.

|   |                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you do not know the UUID of the user, you can retrieve the user by performing a search query, as described in [Query managed users for a specific user](#query_managed_users_for_a_specific_user). |

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/managed/realm-name_user/7750881d-1622-451e-9ee5-71f7aaafcadf"
{
  "_id": "7750881d-1622-451e-9ee5-71f7aaafcadf",
  "_rev": "ecf2cd07-f187-482e-9fa0-1127c267bce2-65781",
  "userName": "scarter",
  "givenName": "Sam",
  "sn": "Carter",
  "telephoneNumber": "12345678",
  "active": "true",
  "mail": "scarter@example.com",
  "accountStatus": "active",
  "effectiveAssignments": [],
  "effectiveRoles": []
}
```

### Add a user with a specific user ID

To add a user, you must provide the minimum required attributes.

To locate the minimum required attributes:

1. From the Advanced Identity Cloud admin console, click Native Consoles > Identity Management.

2. Click Configure > Managed Objects > managed/realm-name\_user.

3. In the Required column, note the properties that have *required* marked.

   1. To create a user, these are the minimum attributes you must present.

|   |                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------- |
|   | If you create an object using PUT, the ID you assign must be a UUID, for example, `4cf65bb9-baa4-4488-aa73-216adf0787a1`. |

```
curl \
--header "Content-Type: application/json" \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--header "If-None-Match: *" \
--request PUT \
--data '{
  "userName": "bjackson",
  "sn": "Jackson",
  "givenName": "Barbara",
  "mail": "bjackson@example.com",
  "telephoneNumber": "082082082",
  "password": "Passw0rd"
}' \
"https://<tenant-env-fqdn>/openidm/managed/realm-name_user/4cf65bb9-baa4-4488-aa73-216adf0787a1"
{
  "_id": "4cf65bb9-baa4-4488-aa73-216adf0787a1",
  "_rev": "ceea2483-7f92-411e-9194-dcca0d61198e-51099",
  "userName": "bjackson",
  "sn": "Jackson",
  "givenName": "Barbara",
  "mail": "bjackson@example.com",
  "telephoneNumber": "082082082",
  "accountStatus": "active",
  "effectiveAssignments": [],
  "effectiveRoles": []
}
```

### Add a user with a system-generated ID

To add a user, you must provide the minimum required attributes.

To locate the minimum required attributes:

1. From the Advanced Identity Cloud admin console, click Native Consoles > Identity Management.

2. Click Configure > Managed Objects > managed/realm-name\_user.

3. In the Required column, note the properties that have *required* marked.

   1. To create a user, these are the minimum attributes you must present.

In this instance, Advanced Identity Cloud will create a UUID for you.

```
curl \
--header "Content-Type: application/json" \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
--data '{
  "userName": "pjensen",
  "sn": "Jensen",
  "givenName": "Pam",
  "mail": "pjensen@example.com",
  "telephoneNumber": "082082082",
  "password": "Passw0rd"
}' \
"https://<tenant-env-fqdn>/openidm/managed/realm-name_user?_action=create"
{
  "_id": "4121ae44-7bf4-4dcb-b853-cfc8b5b8582c",
  "_rev": "ceea2483-7f92-411e-9194-dcca0d61198e-51129",
  "userName": "pjensen",
  "sn": "Jensen",
  "givenName": "Pam",
  "mail": "pjensen@example.com",
  "telephoneNumber": "082082082",
  "accountStatus": "active",
  "effectiveAssignments": [],
  "effectiveRoles": []
}
```

### Update a user

This example checks whether user `bjackson` exists, then replaces the telephone number attribute with the new data provided in the request body:

```
curl \
--header "Content-Type: application/json" \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
--data '[
  {
    "operation": "replace",
    "field": "/telephoneNumber",
    "value": "0763483726"
  }
]' \
"https://<tenant-env-fqdn>/openidm/managed/realm-name_user?_action=patch&_queryFilter=userName+eq+'bjackson'"
{
  "userName": "bjackson",
  "sn": "Jackson",
  "givenName": "Barbara",
  "mail": "bjackson@example.com",
  "telephoneNumber": "0763483726",
  "accountStatus": "active",
  "effectiveAssignments": [],
  "effectiveRoles": [],
  "_rev": "ceea2483-7f92-411e-9194-dcca0d61198e-51153",
  "_id": "4cf65bb9-baa4-4488-aa73-216adf0787a1"
}
```

### Delete a user

To delete a user, all you need is the UUID.

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request DELETE \
"https://<tenant-env-fqdn>/openidm/managed/realm-name_user/4cf65bb9-baa4-4488-aa73-216adf0787a1"
{
  "_id": "4cf65bb9-baa4-4488-aa73-216adf0787a1",
  "_rev": "ceea2483-7f92-411e-9194-dcca0d61198e-51153",
  "userName": "bjackson",
  "sn": "Jackson",
  "givenName": "Barbara",
  "mail": "bjackson@example.com",
  "telephoneNumber": "0763483726",
  "accountStatus": "active",
  "effectiveAssignments": [],
  "effectiveRoles": []
}
```

---

---
title: Manage organizations over REST
description: Create, modify, and delete organizations and their relationships over REST
component: pingoneaic
page_id: pingoneaic:idm-objects:manage-orgs-rest
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-objects/manage-orgs-rest.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Organizations", "REST API"]
section_ids:
  add_and_modify_organizations: Add and modify organizations
  query_organizations: Query organizations
---

# Manage organizations over REST

IDM provides RESTful access to managed organizations, at the context path `/openidm/managed/realm-name_organization`. You can add, change, and delete organizations by using the IDM admin console or over the REST interface. To use the IDM admin console, select Manage > Organization.

The examples on this page show how to add, query, modify, and delete organizations over the REST interface. For a reference of all managed organization endpoints and actions, refer to [Managed organizations](../idm-rest-api/endpoints/rest-managed-organizations.html).

## Add and modify organizations

The examples in this section create the `example-org` organization and add admins and members to the organization. In this organization, users bjensen and scarter can create and delete child organizations, also known as suborganizations, of `example-org`, and can create and delete members within the child organizations:

![example-org](_images/example-org.png)

> **Collapse: Add a top level organization to IDM.**
>
> Only IDM tenant administrators can create top level organizations.
>
> ```
> curl \
> --header "Authorization: Bearer <access-token>" \
> --header "Content-Type: application/json" \
> --header "Accept-API-Version: resource=1.0" \
> --header "If-None-Match: *" \
> --request PUT \
> --data '{
>   "name": "example-org"
> }' \
> "https://<tenant-env-fqdn>/openidm/managed/realm-name_organization/example-org"
> {
>   "_id": "example-org",
>   "name": "example-org"
>   ...
> }
> ```

> **Collapse: Make a user the organization's owner.**
>
> Advanced Identity Cloud tenant administrators can designate organizations' owners. In this example, the tenant administrator makes bjensen the owner of the `example-org` organization created previously.
>
> The example assumes the user bjensen already exists:
>
> ```
> curl \
> --header "Authorization: Bearer <access-token>" \
> --header "Content-Type: application/json" \
> --header "Accept-API-Version: resource=1.0" \
> --request POST \
> --data '{
>   "_ref":"managed/realm-name_user/<bjensenUUID>"
> }' \
> "https://<tenant-env-fqdn>/openidm/managed/realm-name_organization/example-org/owners?_action=create"
> ```

> **Collapse: Add a member to the organization.**
>
> Organization owners can create members in the organizations that they own. In this example, bjensen creates user scarter. bjensen also makes scarter a member of the `example-org` organization:
>
> ```
> curl \
> --header "Authorization: Bearer <access-token>" \
> --header "Content-Type: application/json" \
> --header "Accept-API-Version: resource=1.0" \
> --request POST \
> --data '{
>   "userName": "scarter",
>   "sn": "Carter",
>   "givenName": "Steven",
>   "mail": "scarter@example.com",
>   "password": "Th3Password!",
>   "memberOfOrg": [{"_ref": "managed/realm-name_organization/example-org"}]
> }' \
> "https://<tenant-env-fqdn>/openidm/managed/realm-name_user?_action=create"
> {
>  ...
>  "mail":"scarter@example.com",
>  "memberOfOrgIDs":["example-org"],
>  ...
> }
> ```

> **Collapse: Make one of the organization's members an admin.**
>
> Organization owners can designate admins for the organizations they own. An organization admin must be a member of the organization. In this example, bjensen makes scarter an admin of the `example-org` organization:
>
> ```
> curl \
> --header "Authorization: Bearer <access-token>" \
> --header 'Content-Type: application/json' \
> --header "Accept-API-Version: resource=1.0" \
> --request PATCH \
> --data '[
>     {
>         "operation": "add",
>         "field": "/admins/-",
>         "value": {
>           "_ref": "managed/realm-name_user/<scarterUUID>"
>         }
>     }
> ]' \
> "https://<tenant-env-fqdn>/openidm/managed/realm-name_organization/example-org"
> {
>   "_id": "example-org",
>   ...
>   "name": "example-org"
> }
> ```

> **Collapse: Add a member to the organization.**
>
> Organization admins can add members to the organizations they administer. In this example, the organization admin, scarter, creates a new member, jsanchez. scarter also makes jsanchez a member of the `example-org` organization:
>
> ```
> curl \
> --header "Authorization: Bearer <access-token>" \
> --header "Content-Type: application/json" \
> --header "Accept-API-Version: resource=1.0" \
> --request POST \
> --data '{
>   "userName": "jsanchez",
>   "sn": "Sanchez",
>   "givenName": "Juanita",
>   "mail": "jsanchez@example.com",
>   "password": "Th3Password!",
>   "memberOfOrg": [{"_ref": "managed/realm-name_organization/example-org"}]
> }' \
> "https://<tenant-env-fqdn>/openidm/managed/realm-name_user?_action=create"
> {
>  ...
>  "mail":"jsanchez@example.com",
>  "memberOfOrgIDs":["example-org"],
>  ...
> }
> ```

> **Collapse: Create a child organization.**
>
> Organization owners and admins can create and manage child organizations of the organizations they own or administer. In this example, the organization owner, bjensen, creates a new organization named `example-child-org`, and makes it a child organization of the `example-org` organization:
>
> ```
> curl \
> --header "Authorization: Bearer <access-token>" \
> --header "Content-Type: application/json" \
> --header "Accept-API-Version: resource=1.0" \
> --header "If-None-Match: *" \
> --request POST \
> --data '{
>   "name": "example-child-org",
>   "parent": {"_ref": "managed/realm-name_organization/example-org"}
> }' \
> "https://<tenant-env-fqdn>/openidm/managed/realm-name_organization?_action=create"
> {
>   ...
>   "parentIDs":["example-org"],
>   ...
>   "name":"example-child-org"
> }
> ```
>
> |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
> | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | When creating a child organization, you need to add custom attributes to the access flags for the `owner-view-update-delete-orgs` and `owner-create-orgs` privileges. After you add these attributes, you can create a child organization and the custom attributes are visible.For more information on adding and updating privileges that apply to managed organizations, refer to [Server configuration](../idm-rest-api/endpoints/rest-server-config.html). |

## Query organizations

The examples in this section demonstrate several ways you can query organizations and organization membership:

> **Collapse: List all the organizations a user owns.**
>
> This example lists the organizations bjensen owns:
>
> ```
> curl \
> --header "Authorization: Bearer <access-token>" \
> --header "Accept-API-Version: resource=1.0" \
> --request GET \
> "https://<tenant-env-fqdn>/openidm/managed/realm-name_user/<bjensenUUID>/ownerOfOrg?_queryFilter=true"
> {
>   "result": [
>     {
>       ...
>       "_ref": "managed/realm-name_organization/example-org",
>       "_refResourceCollection": "managed/realm-name_organization",
>       "_refResourceId": "example-org",
>       ...
>     }
>   ],
>   ...
> }
> ```

> **Collapse: List an organization's members.**
>
> Organization owners can list the members of the organizations they own. In this example, bjensen lists the members of the `example-org` organization:
>
> ```
> curl \
> --header "Authorization: Bearer <access-token>" \
> --header "Accept-API-Version: resource=1.0" \
> --request GET \
> "https://<tenant-env-fqdn>/openidm/managed/realm-name_organization/example-org/members?_queryFilter=true"
> {
>   "result": [
>     ...
>   ],
>   "resultCount":1,
>   ...
> }
> ```

> **Collapse: List organizations that you own or administer, and list their child organizations.**
>
> An organization owner or admin can list the organizations that they own or administer. When a user runs the curl command in this example, it lists:
>
> * The organizations that the user owns or administers
>
> * Those organizations' child organizations
>
> ```
> curl \
> --header "Authorization: Bearer <access-token>" \
> --header "Accept-API-Version: resource=1.0" \
> --request GET \
> "https://<tenant-env-fqdn>/openidm/managed/realm-name_organization?_queryFilter=true"
> {
>   "result": [
>     {
>       "_id":"example-org",
>       "parentIDs":[],
>       "name":"example-org"
>     },
>     {
>       "_id":"<example-child-orgUUID>",
>       "parentIDs":["example-org"],
>       "name":"example-child-org"
>     }
>     "resultCount":2,
>   ...
> }
> ```

> **Collapse: List organizations of which another user is a member.**
>
> Organization owners and admins can list all the organizations they own or administer that contain a given user. In this example, scarter lists the organizations of which jsanchez is a member:
>
> ```
> curl \
> --header "Authorization: Bearer <access-token>" \
> --header "Accept-API-Version: resource=1.0" \
> --request GET \
> "https://<tenant-env-fqdn>/openidm/managed/realm-name_user/<jsanchezUUID>?_fields=memberOfOrg"
> {
>   "_id": ...
>   "memberOfOrg":[
>     {
>       "_ref":"managed/realm-name_organization/example-org",
>       "_refResourceCollection":"managed/realm-name_organization",
>       "_refResourceId":"example-org",
>       ...
> }
> ```

---

---
title: Manage policies over REST
description: Manage and validate policies for managed and internal objects over REST
component: pingoneaic
page_id: pingoneaic:idm-objects:policies-over-REST
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-objects/policies-over-REST.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
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

Manage policies over REST through the policy configuration *(tooltip: You can edit the policy configuration over REST at the config/policy endpoint.)*.

## List the defined policies

The following REST call displays a list of all the policies defined (policies for objects other than managed objects). The policy objects are returned in JSON format, with one object for each defined policy ID:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/policy"
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
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/policy/managed/realm-name_user/*"
{
  "_id": "*",
  "resource": "managed/realm-name_user/*",
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
--header "Authorization: Bearer <access-token>" \
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
"https://<tenant-env-fqdn>/openidm/policy/managed/realm-name_user/test?_action=validateObject"
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
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request POST \
--data '{
  "password": "12345"
}' \
"https://<tenant-env-fqdn>/openidm/policy/managed/realm-name_user/9dce06d4-2fc1-4830-a92b-bd35c2f6bcbb?_action=validateProperty"
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
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request POST \
--data '{
  "password": "1NewPassword"
}' \
"https://<tenant-env-fqdn>/openidm/policy/managed/realm-name_user/9dce06d4-2fc1-4830-a92b-bd35c2f6bcbb?_action=validateProperty"
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
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request POST \
--data '{
  "_remove": [ "description", "givenName" ]
}' \
"https://<tenant-env-fqdn>/openidm/policy/managed/realm-name_user/ca5a3196-2ed3-4a76-8881-30403dee70e9?_action=validateProperty"
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

To perform a `validateProperty` action to a path that is unknown (`*`), such as `managed/realm-name_user/*` or `managed/realm-name_user/userDoesntExistYet`, the payload must include:

* An `object` field that contains the object details.

* A `properties` field that contains the properties to be evaluated.

#### Pre-registration validation example

A common use case for validating properties for unknown resources is prior to object creation, such as during pre-registration.

1. Always pass the object and properties content in the POST body because Advanced Identity Cloud has no object to look up.

2. Use any placeholder id in the request URL, as `*` has no special meaning in the API.

   This example uses a conditional policy for any object with the description `test1`:

   ```json
   "givenName" : {
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

3. Using the above conditional policy, you could perform a `validateProperty` action to `managed/realm-name_user/*` with the request:

   ```
   curl \
   --header "Authorization: Bearer <access-token>" \
   --header "Accept-API-Version: resource=1.0" \
   --header "Content-Type: application/json" \
   --request POST \
   --data '{
     "object": {
       "description": "test1"
     },
     "properties": {
       "givenName": "passw0rd"
     }
   }' \
   "https://<tenant-env-fqdn>/openidm/policy/managed/realm-name_user/*?_action=validateProperty"
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
         "property": "givenName"
       }
     ]
   }
   ```