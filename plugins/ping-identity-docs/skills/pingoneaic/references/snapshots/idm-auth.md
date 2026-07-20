---
title: Authentication
description: Overview of authentication in Advanced Identity Cloud including credential verification and access to identity management resources
component: pingoneaic
page_id: pingoneaic:idm-auth:authentication
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-auth/authentication.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication"]
---

# Authentication

*Authentication* is the process of verifying who is requesting access to a resource. The user or application making the request presents credentials, making it possible to prove that the requester is who they claim to be. The goal is to authorize access to specific IDM resources, depending on the confirmed identity of the user or application making the request.

---

---
title: Authentication and authorization
description: Guide to configuring authentication and authorization.
component: pingoneaic
page_id: pingoneaic:idm-auth:preface
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-auth/preface.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["index.adoc"]
---

# Authentication and authorization

This guide covers authentication, authorization, and delegated administration.

[icon: id-card, set=far, size=3x]

#### [Authentication](authentication.html)

Authenticate users securely.

[icon: user-ninja, set=fas, size=3x]

#### [Authorization & roles](authorization-and-roles.html)

The authorization configuration grants rights to users based on their roles.

[icon: users, set=fas, size=3x]

#### [Delegated administration](delegated-admin.html)

Use privileges to give fine-grained administrative access to specific users.

---

---
title: Authentication and roles
description: Understand how internal roles are assigned during user authentication
component: pingoneaic
page_id: pingoneaic:idm-auth:authentication-and-roles
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-auth/authentication-and-roles.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Roles", "Security Context"]
section_ids:
  dynamic-role-calculation: Dynamic role calculation
  auth-security-context: Roles, authentication, and the security context
  authentication-control-rest: Change the authentication configuration over REST
---

# Authentication and roles

When a user authenticates, the user is given a set of default *internal roles*. These roles determine what Advanced Identity Cloud resources the user can access. Advanced Identity Cloud includes a number of default internal roles on the `openidm/internal/roles` endpoint. You can configure additional internal roles to customize how you restrict access to the server.

The following internal roles are defined by default:

* openidm-admin

  IDM administrator role, excluded from the reauthorization required policy definition by default.

* openidm-authorized

  Default role for any user who authenticates with a username and password.

* openidm-cert

  Default role for any user who authenticates with mutual SSL authentication.

  This role applies only to mutual authentication. The shared secret (certificate) must be adequately protected. The `openidm-cert` role is excluded from the reauthorization required policy definition by default.

* openidm-reg

  Assigned to users who access Advanced Identity Cloud with the default anonymous account.

  The `openidm-reg` role is excluded from the reauthorization required policy definition by default.

* openidm-tasks-manager

  Role for users who can be assigned to workflow tasks.

* platform-provisioning

  Role for platform provisioning access.

When a user authenticates, Advanced Identity Cloud calculates that user's roles as follows:

* Each authentication module includes a `defaultUserRoles` property. Depending on how the user authenticates, Advanced Identity Cloud assigns the roles listed in that module's `defaultUserRoles` property to the user on authentication. The `defaultUserRoles` property is specified as an array. For most authentication modules, the user obtains the `openidm-authorized` role on authentication. For example:

  ```json
  {
      "name" : "MANAGED_USER",
      "properties" : {
          ...
          "defaultUserRoles" : [
              "internal/role/openidm-authorized"
          ]
      },
      ...
  }
  ```

* The `userRoles` property in an authentication module maps to an attribute (or list of attributes) in a user entry that contains that user's authorization roles. This attribute is usually `authzRoles`, unless you have changed how user roles are stored.

  Any internal roles that are conditionally applied are also calculated and included in the user's `authzRoles` property at this point.

* If the authentication module includes a `groupRoleMapping`, `groupMembership`, or `groupComparison` property, Advanced Identity Cloud can assign additional roles to the user, depending on the user's group membership on an *external* system. Learn more in [Map external groups to internal authz roles](../idm-objects/groups-and-access-to-idm.html).

  |   |                                                                                                                                                                                 |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The roles calculated in sequence are cumulative. Roles with temporal restrictions aren't included in that list if the current time is outside of the time assigned to the role. |

## Dynamic role calculation

By default, Advanced Identity Cloud calculates a user's roles only on authentication. You can configure Advanced Identity Cloud to recalculate a user's roles dynamically, with each request, instead of only when the user reauthenticates. To enable this feature, set `enableDynamicRoles` to `true` in the `JWT_SESSION` session module in the authentication configuration *(tooltip: You can manage the authentication configuration over REST at the config/authentication endpoint.)*.

## Roles, authentication, and the security context

The security context (`context.security`), consists of a principal (defined by the `authenticationId` property) and an access control element (defined by the `authorization` property).

If authentication is successful, the authentication framework sets the principal. Advanced Identity Cloud stores that principal as the `authenticationId`.

The `authorization` property includes an `id`, an array of `roles`, and a `component`, that specifies the resource against which authorization is validated.

## Change the authentication configuration over REST

You can change the authentication configuration using the endpoint `openidm/config/authentication`. First, get the entire current authentication configuration with a GET request, then modify it as necessary, and finally, resubmit the complete, updated configuration using a PUT request.

1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token).

2. Get the current authentication configuration:

   ```none
   curl \
   --header "Authorization: Bearer <access-token>" \
   --header "Accept-API-Version: resource=1.0"  \
   --request GET \
   "https://<tenant-env-fqdn>/openidm/config/authentication"
   ```

   > **Collapse: Show response**
   >
   > ```json
   > {
   >   "_id": "authentication",
   >   "rsFilter": {
   >     "augmentSecurityContext": {
   >       "source": "require('auth/orgPrivileges').assignPrivilegesToUser(resource, security, properties, subjectMapping, privileges, security.authorization.component.includes('/alpha_') ? 'alphaOrgPrivileges' : 'bravoOrgPrivileges', 'privilegeAssignments');",
   >       "type": "text/javascript"
   >     },
   >     "cache": {
   >       "maxTimeout": "300 seconds"
   >     },
   >     "scopes": [
   >       "fr:idm:*"
   >     ],
   >     "subjectMapping": [
   >       {
   >         "additionalUserFields": [
   >           "adminOfOrg",
   >           "ownerOfOrg"
   >         ],
   >         "defaultRoles": [
   >           "internal/role/openidm-authorized"
   >         ],
   >         "propertyMapping": {
   >           "sub": "_id"
   >         },
   >         "queryOnResource": "managed/{{substring realm 1}}_user",
   >         "userRoles": "authzRoles/*"
   >       }
   >     ]
   >   }
   > }
   > ```

3. Create a local copy of the authentication configuration from the response in step 2, then modify it.

   This example adds a `staticUserMapping` attribute. It contains configuration that assigns the access management OAuth 2.0 client `myrcs1-client` the `myrcs1-client-authorized` role after successful authentication.

   ```json
   {
     "_id": "authentication",
     "rsFilter": {
       "augmentSecurityContext": {
         "source": "require('auth/orgPrivileges').assignPrivilegesToUser(resource, security, properties, subjectMapping, privileges, security.authorization.component.includes('/alpha_') ? 'alphaOrgPrivileges' : 'bravoOrgPrivileges', 'privilegeAssignments');",
         "type": "text/javascript"
       },
       "cache": {
         "maxTimeout": "300 seconds"
       },
       "scopes": [
         "fr:idm:*"
       ],
       "staticUserMapping": [ (1)
         {
           "subject": "myrcs1-client",
           "roles": [
             "myrcs1-client-authorized"
           ]
         }
       ],  (2)
       "subjectMapping": [
         {
           "additionalUserFields": [
             "adminOfOrg",
             "ownerOfOrg"
           ],
           "defaultRoles": [
             "internal/role/openidm-authorized"
           ],
           "propertyMapping": {
             "sub": "_id"
           },
           "queryOnResource": "managed/{{substring realm 1}}_user",
           "userRoles": "authzRoles/*"
         }
       ]
     }
   }
   ```

   |       |                                         |
   | ----- | --------------------------------------- |
   | **1** | Start of `staticUserMapping` attribute. |
   | **2** | End of `staticUserMapping` attribute.   |

4. Replace the authentication configuration:

   ```none
   curl \
   --header "Authorization: Bearer <access-token>" \
   --header "Content-type: application/json" \
   --header "Accept-API-Version: resource=1.0"  \
   --request PUT \
   --data '{
     "_id": "access",
     "rsFilter": <authentication-configuration-object> (1)
   }' \
   "https://<tenant-env-fqdn>/openidm/config/authentication"
   ```

   |       |                                                                                                   |
   | ----- | ------------------------------------------------------------------------------------------------- |
   | **1** | Replace \<authentication-configuration-object> with the `rsFilter` object you modified in step 3. |

   > **Collapse: Show response**
   >
   > ```json
   > {
   >   "_id": "authentication",
   >   "rsFilter": {
   >     "augmentSecurityContext": {
   >       "source": "require('auth/orgPrivileges').assignPrivilegesToUser(resource, security, properties, subjectMapping, privileges, security.authorization.component.includes('/alpha_') ? 'alphaOrgPrivileges' : 'bravoOrgPrivileges', 'privilegeAssignments');",
   >       "type": "text/javascript"
   >     },
   >     "cache": {
   >       "maxTimeout": "300 seconds"
   >     },
   >     "scopes": [
   >       "fr:idm:*"
   >     ],
   >     "staticUserMapping": [ (1)
   >       {
   >         "subject": "myrcs1-client",
   >         "roles": [
   >           "myrcs1-client-authorized"
   >         ]
   >       }
   >     ],
   >     "subjectMapping": [
   >       {
   >         "additionalUserFields": [
   >           "adminOfOrg",
   >           "ownerOfOrg"
   >         ],
   >         "defaultRoles": [
   >           "internal/role/openidm-authorized"
   >         ],
   >         "propertyMapping": {
   >           "sub": "_id"
   >         },
   >         "queryOnResource": "managed/{{substring realm 1}}_user",
   >         "userRoles": "authzRoles/*"
   >       }
   >     ]
   >   }
   > }
   > ```
   >
   > |       |                                                                                  |
   > | ----- | -------------------------------------------------------------------------------- |
   > | **1** | The authentication configuration contains the new `staticUserMapping` attribute. |

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can also modify configuration using a PATCH request to the same endpoint.- The following example adds the same `staticUserMapping` attribute example in step 3 directly to the `rsFilter` attribute:

     ```none
     curl \
     --header "Authorization: Bearer <access-token>" \
     --header "Content-type: application/json" \
     --header "Accept-API-Version: resource=1.0"  \
     --request PATCH \
     --data '
     [
       {
         "operation" : "add",
         "field" : "/rsFilter/staticUserMapping/", (1)
         "value" : [ {
             "subject" : "myrcs1_client",
             "roles" : [
               "myrcsclient1-authorized"
             ]
           }
         ]
       }
     ]' \
     "https://<tenant-env-fqdn>/openidm/config/authentication"
     ```

     1	If you specify the field name on its own (/rsFilter/staticUserMapping/), the value is added on the first request and overwrites on subsequent requests.

   - The following example appends an object to the `staticUserMapping` attribute:

     ```none
     curl \
     --header "Authorization: Bearer <access-token>" \
     --header "Content-type: application/json" \
     --header "Accept-API-Version: resource=1.0"  \
     --request PATCH \
     --data '
     [
       {
         "operation" : "add",
         "field" : "/rsFilter/staticUserMapping/-", (1)
         "value" : {
           "subject" : "myrcs2_client",
           "roles" : [
             "myrcsclient2-authorized"
           ]
         }
       }
     ]' \
     "https://<tenant-env-fqdn>/openidm/config/authentication"
     ```

     1	If you specify the field name followed by a hyphen (/rsFilter/staticUserMapping/-), the value is appended. |

---

---
title: Authentication through OAuth 2.0 and subject mappings
description: Delegate authentication from identity management to access management using OAuth 2.0 bearer tokens
component: pingoneaic
page_id: pingoneaic:idm-auth:rsfilter-module
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-auth/rsfilter-module.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "OAuth 2.0"]
section_ids:
  test-rsfilter-auth: Test authentication
---

# Authentication through OAuth 2.0 and subject mappings

Ping Identity IDM uses AM bearer tokens for authentication. Accordingly, all authentication is delegated to AM. With AM bearer tokens, all Advanced Identity Cloud endpoints that require authentication are accessed using an authorization header that contains the bearer token. Endpoints that allow anonymous access can be accessed without a token.

This page details the backend process of how AM does this, which includes subject mappings.

An `rsFilter` is an authentication method used to delegate authentication from IDM to AM. In Advanced Identity Cloud, the `rsFilter` is predefined in the authentication configuration *(tooltip: You can manage the authentication configuration over REST at the config/authentication endpoint.)*.

The `rsFilter` configuration includes the following properties:

* `scopes`

  Any scopes that are required to be present in the access token. This will vary depending on your configuration. For more information about scopes, refer to [OAuth 2.0 scopes](../am-oauth2/oauth2-scopes.html) in the AM *OAuth 2.0 Guide*.

* `cache`

  Sets the timeout (`maxTimeout`), in seconds, after which the token is removed from the cache.

* `augmentSecurityContext`

  Specifies a script that is executed only after a successful authentication request. The script helps to populate the expected security context. For more information, refer to [The `augmentSecurityContext` trigger](../idm-scripting/script-variables-augment-security.html).

* `subjectMapping`

  An array of mappings that maps the AM realms (in Advanced Identity Cloud `/alpha` and `/bravo`) to IDM managed object types. For example:

  ```json
  {
    "subjectMapping": [
      {
        "queryOnResource": "managed/realm-name_user",
        "propertyMapping": {
          "sub": "_id"
        },
        "userRoles": [
          "authzRoles/*"
        ],
        "additionalUserFields": [
          "adminOfOrg",
          "ownerOfOrg"
        ],
        "defaultRoles": [
          "internal/role/openidm-authorized"
        ]
      }
    ]
  }
  ```

  * `queryOnResource`: The IDM resource to check for the authenticating user; for example, `managed/realm-name_user`.

    The `queryOnResource` property supports dynamic handlebars template that lets a single subject mapping match multiple realms, if the managed objects are named prescriptively, and based on the realm name.

    For example:

    ```json
    "queryOnResource" : "managed/realm-name_user"
    ```

    This example configuration lets an access token with the realm `alpha` map to an IDM `managed/alpha_user`, and an access token with the realm `bravo` map to an IDM `managed/bravo_user`. The configuration is useful if your AM and IDM deployments use a consistent realm and managed object naming.

    * `realm`: The AM realm to which this subject mapping applies. A value of `/` specifies the top-level realm. If this property is absent, the mapping can apply to any realm, which is useful if the `queryOnResource` uses a dynamic handlebars template.

      |   |                                                                                                                                               |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | You cannot have more than one mapping for the same realm, and you cannot have more than one mapping that has no `realm` in the configuration. |

    * `propertyMapping`: Maps fields in the AM access token to properties in IDM. This mapping is used to construct the query filter that locates the authenticating user. The default configuration maps the subject (`sub`) in the access token to the `_id` in IDM.

    * `userRoles`: Specifies one or more relationship fields containing authorization roles. IDM uses the `_refId` from the array elements in these fields to populate the user roles in the security context.

      `userRoles` accepts an array of strings, allowing roles to be sourced from multiple relationship fields.

      Example: Single relationship field (current array format)

      ```json
      "userRoles" : [ "authzRoles/*" ]
      ```

      Example: Multiple relationship fields

      ```json
      "userRoles" : [ "authzRoles/*", "groups/*" ]
      ```

      Example: Single relationship field (legacy format)

      ```json
      "userRoles" : "authzRoles/*"
      ```

    * `additionalUserFields`: Determines the field to consult for locating the authorization roles; usually `authzRoles`, unless you have changed how user roles are stored. This field must be a relationship field. IDM uses the `_refId` from the array elements to populate the user roles in the security context.

    * `defaultRoles`: The default roles that should be applied to a user who authenticates using the `rsFilter`.

      ```json
      {
          "subject" : "RCS-OAuth-clientId",
          "localUser" : "internal/user/idm-provisioning"
      }
      ```

      The `subject` must reflect the OAuth2 client in AM that has been set up for the remote connector server. The `localUser` can be any existing user. Do not assign that user any roles to ensure that the connector server bearer token cannot be used for any other purpose.

* `staticUserMapping`

  Maps AM users to a matching IDM user. Can contain multiple user mappings, each with three properties: `subject`, `localUser`, and `roles`.

  * `subject` of the access token (the AM user). If you have specified a `resourceTypeMapping`, the static user mapping includes the full new subject string to match service accounts or static subject mappings, for example:

    ```json
    "subject" : "amadmin"
    ```

  * `localUser` is the IDM user you want to associate with the AM user identified in `subject`. For example, if `subject` is set to `amadmin`, you might set the corresponding `localUser` to `internal/user/openidm-admin`.

  * `roles` the default IDM roles that this mapped user will have after they authenticate.

    |   |                                                                                                                                                                     |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | The `idm-provisioning` subject is a service account used by AM to provision users in IDM. You *must* include this subject in your `staticUserMapping`. For example: |

    ```json
    {
        "subject": "(age!idm-provisioning)",
        "localUser": "internal/user/idm-provisioning",
        "roles" : [
            "internal/role/platform-provisioning"
        ]
    }
    ```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Only one mapping is selected and used during the authentication process. If there is a `realm` attribute in the access token, that realm is used to select an appropriate mapping. If no mapping is defined for the access token's realm, or if the realm is not provided in the access token, the authentication uses a mapping that does not define a `realm`.In most situations if you have a remote connector server that is authenticating against AM, you must add a subject mapping specifically for the connector server.In this case you must add a `staticUserMapping`. |

## Test authentication

To test authentication, create your own OAuth 2.0 client with the proper grant types. For more information, refer to [Create custom OAuth 2.0 applications with application management.](../app-management/applications.html#oidc-openid-connect-applications)

1. Obtain a bearer token from AM.

   For example, the bearer token would look like:

   ```
   Authorization: Bearer z4uKDWiv4wnxKY7OjeG04PujG8E
   ```

   For more information on how get a bearer token, refer to [Authenticate to REST API with an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#overview).

2. Authenticate to IDM using that bearer token:

   ```
   curl \
   --request GET \
   --header "Content-Type: application/json" \
   --header "Authorization: Bearer z4uKDWiv4wnxKY7OjeG04PujG8E" \
   'https://<tenant-env-fqdn>/openidm/info/login'
   {
     "_id": "login",
     "authenticationId": "testClientID",
     "authorization": {
       "id": "testClientID",
       "roles": [
         "internal/role/platform-provisioning"
       ],
       "component": "internal/user"
     }
   }
   ```

---

---
title: Authorization and roles
description: Configure role-based authorization to restrict HTTP access to REST endpoints
component: pingoneaic
page_id: pingoneaic:idm-auth:authorization-and-roles
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-auth/authorization-and-roles.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Roles", "Scripts"]
section_ids:
  access-control-rest: Change the access configuration over REST
  access-config: Access configuration format
  granting-internal-roles: Grant internal authorization roles manually
  secure-openicf-access: Secure RCS access to Advanced Identity Cloud connector servers
---

# Authorization and roles

Advanced Identity Cloud provides role-based authorization that restricts direct HTTP access to REST interface URLs. This access control applies to direct HTTP calls only. Access for internal calls (for example, calls from scripts) is not affected by this mechanism.

When a user authenticates, the user is given a set of default *roles*, as described in [Authentication and Roles](authentication-and-roles.html). The authorization configuration grants access rights to users, based on these roles acquired during authentication.

You can use internal and managed roles to restrict access, with the following caveats:

* Internal roles aren't meant to be provisioned or synchronized with external systems.

* Internal roles can't be given assignments.

* Event scripts, such as `onCreate`, can't be attached to internal roles.

* The internal role schema isn't configurable.

By default, managed users are assigned the `openidm-authorized` role when they authenticate.

The following request shows the authorization roles for a user after they have authenticated and obtained a bearer token. Learn more in [Authentication through OAuth 2.0 and subject mappings](rsfilter-module.html).

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"https://<tenant-env-fqdn>/openidm/info/login"
{
  "_id": "login",
  "authenticationId": "f7d...e9b",
  "authorization": {
    "component": "managed/realm-name_user",
    "roles": [
      "internal/role/openidm-authorized"
    ],
    "id": "f7d...e9b"
  }
}
```

The authorization implementation is configured in a router authorization script and the access configuration.

Advanced Identity Cloud calls the router authorization for each request and checks against your access configuration to determine whether to allow HTTP requests.

The `onResponse` and `relationshipFilter` filters provide additional filtering to ensure the user has the appropriate access to observe the data of the related object. Learn more in [Relationships between objects](../idm-objects/relationships.html).

|   |                                                                                                   |
| - | ------------------------------------------------------------------------------------------------- |
|   | You can configure [delegated administration](delegated-admin.html) to bypass this access control. |

## Change the access configuration over REST

You can change the access configuration using the endpoint `openidm/config/access`. First, get the entire current access configuration with a GET request, then modify it as necessary, and finally, resubmit the complete, updated configuration using a PUT request.

1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token).

2. Get the current access configuration:

   ```none
   curl \
   --header "Authorization: Bearer <access-token>" \
   --header "Accept-API-Version: resource=1.0"  \
   --request GET \
   "https://<tenant-env-fqdn>/openidm/config/access"
   ```

   > **Collapse: Show response**
   >
   > ```json
   > {
   >   "_id": "access",
   >   "configs": [
   >     {
   >       "actions": "*",
   >       "methods": "read",
   >       "pattern": "info/*",
   >       "roles": "*"
   >     },
   >     {
   >       "actions": "login,logout",
   >       "methods": "read,action",
   >       "pattern": "authentication",
   >       "roles": "*"
   >     },
   >     ... (1)
   >   ]
   > }
   > ```
   >
   > |       |                                                                                                                            |
   > | ----- | -------------------------------------------------------------------------------------------------------------------------- |
   > | **1** | The response has been truncated to make the example clearer. Your response should contain the entire access configuration. |

3. Create a local copy of the access configuration from the response in step 2, then modify it. This example adds a rule that restricts access to the `info` endpoint to users who have authenticated:

   ```json
   {
     "_id": "access",
     "configs": [
       {
         "actions": "*",
         "methods": "read",
         "pattern": "info/*",
         "roles": "*"
       },
       {
         "actions": "login,logout",
         "methods": "read,action",
         "pattern": "authentication",
         "roles": "*"
       },
       ... (1)
       {  (2)
         "pattern": "info/*",
         "roles": "*",
         "methods": "read",
         "actions": "*"
       }  (3)
     ]
   }
   ```

   |       |                                                                                                |
   | ----- | ---------------------------------------------------------------------------------------------- |
   | **1** | The example has been truncated. Your local copy should contain the whole response from step 2. |
   | **2** | Start of new rule.                                                                             |
   | **3** | End of new rule.                                                                               |

4. Replace the access configuration:

   ```none
   curl \
   --header "Authorization: Bearer <access-token>" \
   --header "Content-type: application/json" \
   --header "Accept-API-Version: resource=1.0"  \
   --request PUT \
   --data '{
     "_id": "access",
     "configs": <access-configuration-array> (1)
   }' \
   "https://<tenant-env-fqdn>/openidm/config/access"
   ```

   |       |                                                                                                |
   | ----- | ---------------------------------------------------------------------------------------------- |
   | **1** | Replace \<access-configuration-array> with the array of access rules from `configs` in step 3. |

   > **Collapse: Show response**
   >
   > ```json
   > {
   >   "_id": "access",
   >   "configs": [
   >     {
   >       "actions": "*",
   >       "methods": "read",
   >       "pattern": "info/*",
   >       "roles": "*"
   >     },
   >     {
   >       "actions": "login,logout",
   >       "methods": "read,action",
   >       "pattern": "authentication",
   >       "roles": "*"
   >     },
   >     ...
   >     {  (1)
   >       "pattern": "info/*",
   >       "roles": "*",
   >       "methods": "read",
   >       "actions": "*"
   >     }
   >   ]
   > }
   > ```
   >
   > |       |                                                 |
   > | ----- | ----------------------------------------------- |
   > | **1** | The access configuration contains the new rule. |

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can also modify configuration using a PATCH request to the same endpoint.The following example appends the same configuration example in step 3 directly to the `configs` array:```none
   curl \
   --header "Authorization: Bearer <access-token>" \
   --header "Content-type: application/json" \
   --header "Accept-API-Version: resource=1.0"  \
   --request PATCH \
   --data '
   [
     {
       "operation" : "add",
       "field" : "/configs/-",
       "value" : {
         "pattern": "info/",
         "roles": "",
         "methods": "read",
         "actions": "*"
       }
     }
   ]' \
   "https://<tenant-env-fqdn>/openidm/config/access"
   ``` |

## Access configuration format

The access configuration includes a set of rules that govern access to specific endpoints. These rules are tested in the order they appear in the file. You can define more than one rule for the same endpoint. If one rule passes, the request is allowed. If all the rules fail, the request is denied.

The following rule shows the access configuration structure:

```json
{
    "pattern"   : "system/*",
    "roles"     : "internal/role/openidm-admin",
    "methods"   : "action",
    "actions"   : "test,testConfig,createconfiguration,liveSync,authenticate"
}
```

This rule specifies that users with the `openidm-admin` role can perform the listed actions on all `system` endpoints.

The parameters in each access rule are as follows:

* `pattern`

The REST endpoint for which access is being controlled. `"*"` specifies access to all endpoints in that path. For example, `"managed/realm-name_user/*"` specifies access to all managed user objects.

* `roles`

  A comma-separated list of the roles to which this access configuration applies.

  The `roles` referenced here align with the object's security context (`security.authorization.roles`). The `authzRoles` relationship property of a managed user produces this security context value during authentication.

* `methods`

  A comma-separated list of the methods that can be performed with this access. Methods can include `create, read, update, delete, patch, action, query`. A value of `"*"` indicates that all methods are allowed. A value of `""` indicates that no methods are allowed.

* `actions`

  A comma-separated list of the allowed actions. The possible actions depend on the resource (URL) that is being exposed. Note that the `actions` in the example access file do not list all the [supported actions](../idm-scripting/scripting-func-engine.html#supported-actions) on each resource.

  A value of `"*"` indicates that all actions exposed for that resource are allowed. A value of `""` indicates that no actions are allowed.

* `customAuthz`

  An optional parameter that lets you define a custom function for additional authorization checks.

* `excludePatterns`

  An optional parameter that lets you specify endpoints to which access shouldn't be granted.

## Grant internal authorization roles manually

Apart from the default roles that users get when they authenticate, you can grant internal authorization roles manually, over REST or using the IDM admin console. This mechanism works in the same way as the granting of managed roles. Learn more about granting managed roles in [Grant Roles to a User](../idm-objects/roles-over-rest.html#granting-role-user). To grant an internal role manually through the IDM admin console:

1. In the Advanced Identity Cloud admin console, click Native Consoles > Identity Management.

2. Click Manage Users and click a user.

3. On the Authorization Roles tab, click Add Authorization Roles.

4. Select Internal Role as the Type, click in the Authorization Roles field to select from the list of defined Internal Roles and click Add.

To grant an internal role over REST manually, add a reference to the internal role to the user's `authzRoles` property. The following command adds the `openidm-admin` role to user bjensen with ID `9dce06d4-2fc1-4830-a92b-bd35c2f6bcbb`:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request PATCH \
--data '[
  {
    "operation": "add",
    "field": "/authzRoles/-",
    "value": {"_ref" : "internal/role/openidm-admin"}
  }
]' \
"https://<tenant-env-fqdn>/openidm/managed/realm-name_user/9dce06d4-2fc1-4830-a92b-bd35c2f6bcbb"
{
  "_id": "9dce06d4-2fc1-4830-a92b-bd35c2f6bcbb",
  "_rev": "0000000050c62938",
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

You can also grant internal roles dynamically using [conditional role grants](../idm-objects/roles-over-rest.html#conditional-role-grants).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Because internal roles aren't managed objects, you can't manipulate them in the same way as managed roles. You can't add a user to an internal role as you would to a managed role.To add users directly to an internal role, add the users as values of the role's `authzMembers` property. For example:```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Content-Type: application/json" \
--request POST \
--data '{"_ref":"managed/realm-name_user/bjensen"}' \
"https://<tenant-env-fqdn>/openidm/internal/role/3042798d-37fd-49aa-bae3-52598d2c8dc4/authzMembers?_action=create"
``` |

## Secure RCS access to Advanced Identity Cloud connector servers

You can secure the `openicf` WebSocket endpoint used for communication between RCS client mode and Advanced Identity Cloud connector servers. Specifying the authorization roles allowed to connect to the `openicf` servlet for each RCS instance ensures that Advanced Identity Cloud connector servers can only be accessed by trusted RCS clients.

|   |                                                                                                                                                                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This feature is [migration dependant](../product-information/migration-dependent-features.html), so isn't configured for connectors servers in tenants created before its introduction. Learn more about the introduction of the feature in [RCS configuration migration FAQ](../product-information/migration-dependent-features/rcs-configuration-migration-faq.html). |

1. Using the following example as a template, in your authentication configuration add a specific role to the `roles` array of the RCS static user mapping. This role authorizes access to the `openicf` endpoint for the specified RCS.

   Example

   ```json
   {
       "subject": "myrcsclient", (2)
       "roles": [
           "myrcsserver-authorized" (1)
       ],
       "executeAugmentationScript": false
   }
   ```

   |       |                                                                                                                  |
   | ----- | ---------------------------------------------------------------------------------------------------------------- |
   | **1** | In this example, the role `myrcsserver-authorized` is added to the authenticated user's security context for the |
   | **2** | `myrcsclient` OAuth 2.0 client.                                                                                  |

   Use the instructions in [Change the authentication configuration over REST](authentication-and-roles.html#authentication-control-rest) to make the update. For further examples, refer to the [RCS configuration migration FAQ](../product-information/migration-dependent-features/rcs-configuration-migration-faq.html).

2. Using the following example as a template, add a new rule in your access configuration to define authorization for the `openicf` endpoint. Learn more about [changing the access configuration over REST](#access-control-rest).

   Example

   ```json
   {
       "servlet": "openicf", (2)
       "pattern": "myrcsserver", (3)
       "roles": "~myrcsserver-authorized", (1)
       "methods": "read"
   }
   ```

   This rule ensures that:

   |       |                                                                        |
   | ----- | ---------------------------------------------------------------------- |
   | **1** | only users possessing the `myrcsserver-authorized` role can access the |
   | **2** | `openicf` WebSocket endpoint                                           |
   | **3** | for the RCS named `myrcsserver`.                                       |

   Use the instructions in [Change the access configuration over REST](#access-control-rest) to make the update. For further examples, refer to the [RCS configuration migration FAQ](../product-information/migration-dependent-features/rcs-configuration-migration-faq.html).

---

---
title: Delegated administration
description: Grant fine-grained administrative access to specific users using privileges
component: pingoneaic
page_id: pingoneaic:idm-auth:delegated-admin
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-auth/delegated-admin.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Delegated Administration", "Privileges"]
section_ids:
  using-privileges: How privileges restrict administrative access
  determining-access-privileges: Determine access privileges
  creating-privileges: Create privileges
  add_privileges_using_the_advanced_identity_cloud_admin_console: Add privileges using the Advanced Identity Cloud admin console
  add_privileges_using_rest: Add privileges using REST
  privilege-policies: Policies related to privileges
  getting-privilege-resources: Get privileges on a resource
  using-delegated-admin: Create a delegated administrator
---

# Delegated administration

Delegated administration lets you give fine-grained administrative access to specific users, based on a *privilege* mechanism.

|   |                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Delegated administration is only available to Alpha realm users. For detailed information, refer to [Alpha and Bravo realms → Delegated administration](../realms/alpha-bravo-realms.html#delegated_administration). |

## How privileges restrict administrative access

*Privileges* enable you to grant fine-grained administrative access to specific endpoints and objects. For example, you could allow help desk or support users to update the information of other user accounts, but not delete user accounts or change system configuration.

You can use privileges to delegate specific administrative capabilities to non-administrative users, without exposing the IDM admin console to those users. If a user has been granted a privilege that lets them see a list of users and user information, for example, they can access this list directly through the End User UI.

|   |                                                                                                                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | A delegated administrator does not have access to the same REST API methods as a regular administrator. IDM does not allow REST API methods such as POST or DELETE to delegated administrators. To add or remove relationships, use the PATCH method. For examples, refer to [Managed roles](../idm-objects/managed-roles.html). |

For more information on managing privileges using REST, refer to [Privileges](../idm-rest-api/endpoints/rest-privileges.html).

## Determine access privileges

IDM determines what access a user has as follows:

1. IDM checks the `onRequest` script specified in `router.json` . By default, this script calls `router-authz.js` .

2. If access requirements are not satisfied, IDM then checks for any privileges associated with the user's roles.

`onResponse` and `onFailure` scripts are supported when using privileges. `onFailure` scripts are called only if both the `onRequest` script *and* the privilege filter fail. `onRequest`, `onResponse`, and `onFailure` scripts are not required for the privilege mechanism.

## Create privileges

Privileges are assigned to internal roles. A privilege specifies the following information:

* The service path where users with that internal role have access.

* The methods and actions allowed on that service path.

* The specific attributes of the objects at that service path where access is allowed.

You can use a query filter within a privilege so that the privilege applies to a subset of managed objects only.

The `privileges` property is an array and can contain multiple privileges. Each privilege can contain:

* accessFlags

  A list of attributes within a managed object that you want to give access to. Each attribute has two fields:

  | Field                | Description                                          |
  | -------------------- | ---------------------------------------------------- |
  | `attribute`          | The name of the property you are granting access to. |
  | `readOnly` (boolean) | Determines what level of access is allowed.          |

  * Attributes marked as `"readOnly": true` can be viewed, but not edited.

  * Attributes marked as `"readOnly": false` can be both viewed and edited.

  * Attributes that aren't listed in the `accessFlags` array cannot be viewed or edited.

    |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
    | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | * Privileges aren't automatically aware of changes to the managed object schema. If new properties are added, removed, or made mandatory, you must update any existing privileges to account for these changes. When a new property is added, it has a default permission level of `NONE` in existing privileges, including when the privilege is set to access all attributes.

    * PingIDM applies policy validation when creating or updating a privilege, to ensure that all required properties are writable when the `CREATE` permission is assigned. This validation doesn't run when schema changes are made, so you must verify that any existing privileges adhere to defined policies. |

* actions

  A list of the specific actions allowed if the `ACTION` permission has been specified.

  |   |                                            |
  | - | ------------------------------------------ |
  |   | Allowed actions must be explicitly listed. |

* description (optional)

  A description of the privilege.

* filter (optional)

  This property lets you apply a static or dynamic query filter to the privilege, which can be used to limit the scope of what the privilege allows the user to access.

  Static Filter Example

  To allow a delegated administrator to access information only about users for the `stateProvince` of Washington, include a static filter, such as:

  ```json
  filter : "stateProvince eq \"Washington\""
  ```

  Dynamic Filter Example

  Dynamic filters insert values from the authenticated resource. To allow a delegated administrator to access information only about users in their own `stateProvince`, include a dynamic filter by wrapping the parameter in curly braces:

  ```json
  filter : "stateProvince eq \"{{stateProvince}}\""
  ```

  Users with query filter privileges can't edit the properties specified in the filter in ways that would cause the privilege to lose access to the object. For example, if a user with either of the preceding example privileges attempted to edit another user's `stateProvince` field to a value not matching the query filter, the request would return a `403 Forbidden` error.

  |   |                                                                                                                                                |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Privilege filters are an additional layer of filter to any other query filters you create. Any output must satisfy all filters to be included. |

* name

  The name of the privilege.

* path

  The path to the service that you want to allow members of this privilege to access. For example, `managed/realm-name_user`.

* permissions

  A list of permissions this privilege allows for the given path. The following permissions are available:

  |          |                                                                                         |
  | -------- | --------------------------------------------------------------------------------------- |
  | `VIEW`   | Allows reading and querying the path, such as viewing and querying managed users.       |
  | `CREATE` | Allows creation at the path, such as creating new managed users.                        |
  | `UPDATE` | Allows updating or patching existing information, such as editing managed user details. |
  | `DELETE` | Allows deletion, such as deleting users from `managed/realm-name_user`.                 |
  | `ACTION` | Allows users to perform actions at the given path, such as custom scripted actions.     |

  |   |                                                                              |
  | - | ---------------------------------------------------------------------------- |
  |   | If you use an `ACTION` permission, there can be no filters on the privilege. |

### Add privileges using the Advanced Identity Cloud admin console

Refer to [Alpha and Bravo realms → Delegated administration](../realms/alpha-bravo-realms.html#delegated_administration).

### Add privileges using REST

The following example creates a new `support` role with privileges that let members view, create, and update information about users, but not delete users:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--cacert ca-cert.pem \
--request PUT \
--data '{
  "name": "support",
  "description": "Support Role",
  "privileges": [ {
    "name": "support",
    "description": "Support access to user information.",
    "path": "managed/realm-name_user",
    "permissions": [
      "VIEW", "UPDATE", "CREATE"
    ],
    "actions": [],
    "filter": null,
    "accessFlags": [
      {
        "attribute" : "userName",
        "readOnly" : false
      },
      {
        "attribute" : "mail",
        "readOnly" : false
      },
      {
        "attribute" : "givenName",
        "readOnly" : false
      },
      {
        "attribute" : "sn",
        "readOnly" : false
      },
      {
        "attribute" : "accountStatus",
        "readOnly" : true
      }
    ]
  } ]
}' \
"https://<tenant-env-fqdn>/openidm/internal/role/support"
{
  "_id": "support",
  "_rev": "00000000bfbac2ed",
  "name": "support",
  "description": "Support Role",
  "temporalConstraints": [],
  "condition": null,
  "privileges": [
    {
      "name": "support",
      "description": "Support access to user information.",
      "path": "managed/realm-name_user",
      "permissions": [
        "VIEW",
        "UPDATE",
        "CREATE"
      ],
      "actions": [],
      "filter": null,
      "accessFlags": [
        {
          "attribute": "userName",
          "readOnly": false
        },
        {
          "attribute": "mail",
          "readOnly": false
        },
        {
          "attribute": "givenName",
          "readOnly": false
        },
        {
          "attribute": "sn",
          "readOnly": false
        },
        {
          "attribute": "accountStatus",
          "readOnly": true
        }
      ]
    }
  ]
}
```

### Policies related to privileges

When creating privileges, IDM runs policies found in `policy.json` and `policy.js`, including the five policies used for validating privileges:

* `valid-accessFlags-object`

  Verifies that `accessFlag` objects are correctly formatted. Only two fields are permitted in an `accessFlag` object: `readOnly`, which must be a boolean; and `attribute`, which must be a string.

* `valid-array-items`

  Verifies that each item in an array contains the properties specified in `policy.json`, and that each of those properties satisfies any specific policies applied to it. By default, this is used to verify that each privilege contains `name`, `path`, `accessFlags`, `actions`, and `permissions` properties, and that the `filter` property is valid if included.

* `valid-permissions`

  Verifies that the permissions set on the privilege are all valid and can be achieved with the `accessFlags` that have been set. It checks:

  * `CREATE` permissions must have write access to all properties required to create a new object.

  * `CREATE` and `UPDATE` permissions must have write access to at least one property.

  * `ACTION` permissions must include a list of allowed actions, with at least one action included.

  * If any attributes have write access, then the privilege must also have either `CREATE` or `UPDATE` permission.

  * All permissions listed must be valid types of permission: `VIEW`, `CREATE`, `UPDATE`, `ACTION`, or `DELETE`. Also, no permissions are repeated.

* `valid-privilege-path`

  Verifies that the `path` specified in the privilege is a valid object with a schema for IDM to reference. Only objects with a schema (such as `managed/realm-name_user`) can have privileges applied to them.

* `valid-query-filter`

  Verifies the query filter used to filter privileges is valid.

## Get privileges on a resource

To determine which privileges a user has on a service, you can query the privilege endpoint for a given resource path or object based on the user you are currently logged in as. For example, if a user is a member of the support role mentioned in the previous example, checking the user's privileges for the `managed/realm-name_user` resource would look like this:

```
curl \
--header "Authorization: Bearer <access-token>" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--cacert ca-cert.pem \
--request GET \
"https://<tenant-env-fqdn>/openidm/privilege/managed/realm-name_user"
{
  "VIEW": {
    "allowed": true,
    "properties": [
      "userName",
      "givenName",
      "sn",
      "mail",
      "accountStatus"
    ]
  },
  "CREATE": {
    "allowed": true,
    "properties": [
      "userName",
      "givenName",
      "sn",
      "mail"
    ]
  },
  "UPDATE": {
    "allowed": true,
    "properties": [
      "userName",
      "givenName",
      "sn",
      "mail"
    ]
  },
  "DELETE": {
    "allowed": false
  },
  "ACTION": {
    "allowed": false,
    "actions": []
  }
}
```

In the above example, `accountStatus` is listed as a property for `VIEW`, but not for `CREATE` or `UPDATE`, because the privilege sets this property to be read only. Since both `CREATE` and `UPDATE` need the ability to write to a property, setting `readOnly` to false applies to both permissions. If you need more granular control, split these permissions into two privileges.

In addition to checking privileges for a resource, it is also possible to check privileges for specific objects within a resource, such as `managed/realm-name_user/scarter`.

## Create a delegated administrator

You can use the IDM REST API to create an `internal/role` with privileges that have object, array, and relationship type attribute access. You can then use that role as a delegated administrator to perform operations on those attributes.

|   |                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you want to experiment with delegated administrators in [Postman](https://www.postman.com/), download and import this [Postman collection](_attachments/Delegated-Administration.postman_collection.json). |

Use the following example to create a delegated administrator:

> **Collapse: Step 1. Create a Managed Role**
>
> To ensure a role object exists when roles are requested, you must create a managed role.
>
> ```
> curl \
> --header "Authorization: Bearer <access-token>" \
> --header "Content-Type: application/json" \
> --header "If-None-Match: *" \
> --request PUT \
> --data '{
>   "name": "testManagedRole",
>   "description": "a managed role for test"
> }' \
> "https://<tenant-env-fqdn>/openidm/managed/realm-name_role/testManagedRole"
> {
>   "_id": "testManagedRole",
>   "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-181",
>   "name": "testManagedRole",
>   "description": "a managed role for test"
> }
> ```

> **Collapse: Step 2. Create a  User**
>
> ```
> curl \
> --header "Authorization: Bearer <access-token>" \
> --header "Content-Type: application/json" \
> --request POST \
> --data '{
>   "userName": "psmith",
>   "sn": "Smith",
>   "givenName": "Patricia",
>   "mail": "psmith@example.com",
>   "telephoneNumber": "082082082",
>   "password": "Passw0rd"
> }' \
> "https://<tenant-env-fqdn>/openidm/managed/realm-name_user/?_action=create"
> {
>   "_id": "9cae97b7-3bf3-4107-96d5-39ad153629db",
>   "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1223",
>   "userName": "psmith",
>   "sn": "Smith",
>   "givenName": "Patricia",
>   "mail": "psmith@example.com",
>   "telephoneNumber": "082082082",
>   "accountStatus": "active",
>   "effectiveRoles": [],
>   "memberOfOrgIDs": [],
>   "effectiveAssignments": []
> }
> ```

> **Collapse: Step 3. Create Additional Users**
>
> In this step, you'll create two users with the following attributes:
>
> * `preferences`
>
> * `manager`
>
> * `roles`
>
> ```
> curl \
> --header "Authorization: Bearer <access-token>" \
> --header "Content-Type: application/json" \
> --request POST \
> --data '{
>   "userName": "scarter",
>   "sn": "Carter",
>   "givenName": "Steven",
>   "mail": "scarter@example.com",
>   "telephoneNumber": "082082082",
>   "password": "Passw0rd",
>   "preferences": {
>     "updates": true,
>     "marketing": false
>   },
>   "manager": {"_ref": "managed/realm-name_user/9cae97b7-3bf3-4107-96d5-39ad153629db"},
>   "roles": [{"_ref": "managed/realm-name_role/testManagedRole"}]
> }' \
> "https://<tenant-env-fqdn>/openidm/managed/realm-name_user/?_action=create"
> {
>   "_id": "917bc052-ef39-4add-ae05-0a278e2de9c0",
>   "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1238",
>   "userName": "scarter",
>   "sn": "Carter",
>   "givenName": "Steven",
>   "mail": "scarter@example.com",
>   "telephoneNumber": "082082082",
>   "preferences": {
>     "updates": true,
>     "marketing": false
>   },
>   "accountStatus": "active",
>   "effectiveRoles": [
>     {
>       "_refResourceCollection": "managed/realm-name_role",
>       "_refResourceId": "testManagedRole",
>       "_ref": "managed/realm-name_role/testManagedRole"
>     }
>   ],
>   "memberOfOrgIDs": [],
>   "effectiveAssignments": []
> }
> ```
>
> ```
> curl \
> --header "Authorization: Bearer <access-token>" \
> --header "Content-Type: application/json" \
> --request POST \
> --data '{
>   "userName": "jdoe",
>   "sn": "Doe",
>   "givenName": "John",
>   "mail": "jdoe@example.com",
>   "telephoneNumber": "082082082",
>   "password": "Passw0rd",
>   "preferences": {
>     "updates": true,
>     "marketing": false
>   },
>   "manager": {"_ref": "managed/realm-name_user/9cae97b7-3bf3-4107-96d5-39ad153629db"},
>   "roles": [{"_ref": "managed/realm-name_role/testManagedRole"}]
> }' \
> "https://<tenant-env-fqdn>/openidm/managed/realm-name_user/?_action=create"
> {
>   "_id": "aca0042c-9f4c-4ad5-8cf7-aca0adeb3470",
>   "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1267",
>   "userName": "jdoe",
>   "sn": "Doe",
>   "givenName": "John",
>   "mail": "jdoe@example.com",
>   "telephoneNumber": "082082082",
>   "preferences": {
>     "updates": true,
>     "marketing": false
>   },
>   "accountStatus": "active",
>   "effectiveRoles": [
>     {
>       "_refResourceCollection": "managed/realm-name_role",
>       "_refResourceId": "testManagedRole",
>       "_ref": "managed/realm-name_role/testManagedRole"
>     }
>   ],
>   "memberOfOrgIDs": [],
>   "effectiveAssignments": []
> }
> ```

> **Collapse: Step 4. Create Another User**
>
> You will delegate an internal/role with privileges to this user in the next step:
>
> ```
> curl \
> --header "Authorization: Bearer <access-token>" \
> --header "Content-Type: application/json" \
> --request POST \
> --data '{
>   "userName": "bjensen",
>   "sn": "Jensen",
>   "givenName": "Barbara",
>   "mail": "bjensen@example.com",
>   "telephoneNumber": "082082082",
>   "password": "Passw0rd"
> }' \
> "https://<tenant-env-fqdn>/openidm/managed/realm-name_user/?_action=create"
> {
>   "_id": "2d726b2a-3324-44b3-ba40-91b154d4f51e",
>   "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1291",
>   "userName": "bjensen",
>   "sn": "Jensen",
>   "givenName": "Barbara",
>   "mail": "bjensen@example.com",
>   "telephoneNumber": "082082082",
>   "accountStatus": "active",
>   "effectiveRoles": [],
>   "memberOfOrgIDs": [],
>   "effectiveAssignments": []
> }
> ```

> **Collapse: Step 5. Create an**
>
> This role will have the following privileges:
>
> * A `managed/realm-name_user` privilege with accessFlags attributes that are of types: "String" , "boolean" , and "number" ; but also for:
>
>   * An object type that is not a relationship (`preferences`).
>
>   * An object type that is a relationship (`manager`).
>
>   * Array types that are relationships (`roles`, `authzRoles`, `reports`).
>
> * A `managed/realm-name_role` privilege for viewing details of the "roles" property of a managed user.
>
> * An `internal/role` privilege for viewing the details of the "authzRoles" property of a managed user.
>
> |   |                                                                                                                                                                                                                                                                                                                                                                                                           |
> | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | You can populate the privilege `filter` field to apply a finer level of permissions for what a delegated administrator can see or do with certain objects. The `filter` field is omitted in this example to allow all.For properties that are *not* relationships, such as `preferences`, you can't specify finer-grained permissions. For example, you can't set permissions on `preferences/marketing`. |
>
> ```
> curl \
> --header "Authorization: Bearer <access-token>" \
> --header "Content-Type: application/json" \
> --header "If-None-Match: *" \
> --request PUT \
> --data '{
>   "name": "internal_role_with_object_array_and_relationship_privileges",
>   "description": "an internal role that has privileges for object & array types and relationships",
>   "privileges": [
>     {
>       "name": "managed_user_privilege",
>       "path": "managed/realm-name_user",
>       "permissions": [
>         "VIEW",
>         "CREATE",
>         "UPDATE",
>         "DELETE"
>       ],
>       "actions": [],
>       "accessFlags": [
>         {
>           "attribute": "userName",
>           "readOnly": false
>         },
>         {
>           "attribute": "password",
>           "readOnly": false
>         },
>         {
>           "attribute": "givenName",
>           "readOnly": false
>         },
>         {
>           "attribute": "sn",
>           "readOnly": false
>         },
>         {
>           "attribute": "mail",
>           "readOnly": false
>         },
>         {
>           "attribute": "description",
>           "readOnly": false
>         },
>         {
>           "attribute": "accountStatus",
>           "readOnly": false
>         },
>         {
>           "attribute": "telephoneNumber",
>           "readOnly": false
>         },
>         {
>           "attribute": "postalAddress",
>           "readOnly": false
>         },
>         {
>           "attribute": "city",
>           "readOnly": false
>         },
>         {
>           "attribute": "postalCode",
>           "readOnly": false
>         },
>         {
>           "attribute": "country",
>           "readOnly": false
>         },
>         {
>           "attribute": "stateProvince",
>           "readOnly": false
>         },
>         {
>           "attribute": "preferences",
>           "readOnly": false
>         },
>         {
>           "attribute": "roles",
>           "readOnly": false
>         },
>         {
>           "attribute": "manager",
>           "readOnly": false
>         },
>         {
>           "attribute": "authzRoles",
>           "readOnly": false
>         },
>         {
>           "attribute": "reports",
>           "readOnly": false
>         }
>       ]
>     },
>     {
>       "name": "managed_role_privilege",
>       "path": "managed/realm-name_role",
>       "permissions": [
>         "VIEW"
>       ],
>       "actions": [],
>       "accessFlags": [
>         {
>           "attribute": "name",
>           "readOnly": true
>         },
>         {
>           "attribute": "description",
>           "readOnly": true
>         }
>       ]
>     },
>     {
>       "name": "internal_role_privilege",
>       "path": "internal/role",
>       "permissions": [
>         "VIEW"
>       ],
>       "actions": [],
>       "accessFlags": [
>         {
>           "attribute": "name",
>           "readOnly": true
>         },
>         {
>           "attribute": "description",
>           "readOnly": true
>         },
>         {
>           "attribute": "authzMembers",
>           "readOnly": true
>         }
>       ]
>     }
>   ]
> }' \
> "https://<tenant-env-fqdn>/openidm/internal/role/testInternalRole"
> {
>   "_id": "testInternalRole",
>   "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-300",
>   "name": "internal_role_with_object_array_and_relationship_privileges",
>   "description": "an internal role that has privileges for object & array types and relationships",
>   "temporalConstraints": [],
>   "condition": null,
>   "privileges": [
>     {
>       "name": "managed_user_privilege",
>       "path": "managed/realm-name_user",
>       "permissions": [
>         "VIEW",
>         "CREATE",
>         "UPDATE",
>         "DELETE"
>       ],
>       "actions": [],
>       "accessFlags": [
>         {
>           "attribute": "userName",
>           "readOnly": false
>         },
>         {
>           "attribute": "password",
>           "readOnly": false
>         },
>         {
>           "attribute": "givenName",
>           "readOnly": false
>         },
>         {
>           "attribute": "sn",
>           "readOnly": false
>         },
>         {
>           "attribute": "mail",
>           "readOnly": false
>         },
>         {
>           "attribute": "description",
>           "readOnly": false
>         },
>         {
>           "attribute": "accountStatus",
>           "readOnly": false
>         },
>         {
>           "attribute": "telephoneNumber",
>           "readOnly": false
>         },
>         {
>           "attribute": "postalAddress",
>           "readOnly": false
>         },
>         {
>           "attribute": "city",
>           "readOnly": false
>         },
>         {
>           "attribute": "postalCode",
>           "readOnly": false
>         },
>         {
>           "attribute": "country",
>           "readOnly": false
>         },
>         {
>           "attribute": "stateProvince",
>           "readOnly": false
>         },
>         {
>           "attribute": "preferences",
>           "readOnly": false
>         },
>         {
>           "attribute": "roles",
>           "readOnly": false
>         },
>         {
>           "attribute": "manager",
>           "readOnly": false
>         },
>         {
>           "attribute": "authzRoles",
>           "readOnly": false
>         },
>         {
>           "attribute": "reports",
>           "readOnly": false
>         }
>       ]
>     },
>     {
>       "name": "managed_role_privilege",
>       "path": "managed/realm-name_role",
>       "permissions": [
>         "VIEW"
>       ],
>       "actions": [],
>       "accessFlags": [
>         {
>           "attribute": "name",
>           "readOnly": true
>         },
>         {
>           "attribute": "description",
>           "readOnly": true
>         }
>       ]
>     },
>     {
>       "name": "internal_role_privilege",
>       "path": "internal/role",
>       "permissions": [
>         "VIEW"
>       ],
>       "actions": [],
>       "accessFlags": [
>         {
>           "attribute": "name",
>           "readOnly": true
>         },
>         {
>           "attribute": "description",
>           "readOnly": true
>         },
>         {
>           "attribute": "authzMembers",
>           "readOnly": true
>         }
>       ]
>     }
>   ]
> }
> ```

> **Collapse: Step 6. Create the Relationship Between User and**
>
> In this step, assign the internal/role from step 5 to the user created in step 4 by creating a relationship:
>
> ```
> curl \
> --header "Authorization: Bearer <access-token>" \
> --header "Content-Type: application/json" \
> --request POST \
> --data '{
>   "_ref": "managed/realm-name_user/2d726b2a-3324-44b3-ba40-91b154d4f51e",
>   "_refProperties": {}
> }' \
> "https://<tenant-env-fqdn>/openidm/internal/role/testInternalRole/authzMembers?_action=create"
> {
>   "_id": "2e21f423-f934-4ed7-b6fd-9883b69d52d8",
>   "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1304",
>   "_ref": "managed/realm-name_user/2d726b2a-3324-44b3-ba40-91b154d4f51e",
>   "_refResourceCollection": "managed/realm-name_user",
>   "_refResourceId": "2d726b2a-3324-44b3-ba40-91b154d4f51e",
>   "_refProperties": {
>     "_id": "2e21f423-f934-4ed7-b6fd-9883b69d52d8",
>     "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1304"
>   }
> }
> ```

> **Collapse: Step 7. Perform Operations as a Delegated Administrator**
>
> You can now perform operations as a delegated administrator, such as:
>
> > **Collapse: Query All Users**
> >
> > The query results display all users' properties that are allowed by the privileges:
> >
> > ```
> > curl \
> > --header "X-OpenIDM-Username: bjensen" \
> > --header "X-OpenIDM-Password: Passw0rd" \
> > --request GET \
> > "https://<tenant-env-fqdn>/openidm/managed/realm-name_user?_queryFilter=true&_pageSize=100&_fields=*,*_ref/*"
> > {
> >   "result": [
> >     {
> >       "_id": "9cae97b7-3bf3-4107-96d5-39ad153629db",
> >       "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1223",
> >       "userName": "psmith",
> >       "sn": "Smith",
> >       "givenName": "Patricia",
> >       "mail": "psmith@example.com",
> >       "telephoneNumber": "082082082",
> >       "accountStatus": "active",
> >       "reports": [
> >         {
> >           "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1267",
> >           "_id": "aca0042c-9f4c-4ad5-8cf7-aca0adeb3470",
> >           "userName": "jdoe",
> >           "sn": "Doe",
> >           "givenName": "John",
> >           "mail": "jdoe@example.com",
> >           "telephoneNumber": "082082082",
> >           "preferences": {
> >             "updates": true,
> >             "marketing": false
> >           },
> >           "accountStatus": "active",
> >           "_ref": "managed/realm-name_user/aca0042c-9f4c-4ad5-8cf7-aca0adeb3470",
> >           "_refResourceCollection": "managed/realm-name_user",
> >           "_refResourceId": "aca0042c-9f4c-4ad5-8cf7-aca0adeb3470",
> >           "_refProperties": {
> >             "_id": "e01a922b-a60d-46c2-b6bc-2b821c1580b4",
> >             "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1262"
> >           }
> >         },
> >         {
> >           "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1238",
> >           "_id": "917bc052-ef39-4add-ae05-0a278e2de9c0",
> >           "userName": "scarter",
> >           "sn": "Carter",
> >           "givenName": "Steven",
> >           "mail": "scarter@example.com",
> >           "telephoneNumber": "082082082",
> >           "preferences": {
> >             "updates": true,
> >             "marketing": false
> >           },
> >           "accountStatus": "active",
> >           "_ref": "managed/realm-name_user/917bc052-ef39-4add-ae05-0a278e2de9c0",
> >           "_refResourceCollection": "managed/realm-name_user",
> >           "_refResourceId": "917bc052-ef39-4add-ae05-0a278e2de9c0",
> >           "_refProperties": {
> >             "_id": "5bc2c633-8ae1-4ea2-adf6-8aa7ce5f8e70",
> >             "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1233"
> >           }
> >         }
> >       ],
> >       "manager": null,
> >       "roles": [],
> >       "authzRoles": []
> >     },
> >     {
> >       "_id": "917bc052-ef39-4add-ae05-0a278e2de9c0",
> >       "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1238",
> >       "userName": "scarter",
> >       "sn": "Carter",
> >       "givenName": "Steven",
> >       "mail": "scarter@example.com",
> >       "telephoneNumber": "082082082",
> >       "preferences": {
> >         "updates": true,
> >         "marketing": false
> >       },
> >       "accountStatus": "active",
> >       "reports": [],
> >       "manager": {
> >         "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1223",
> >         "_id": "9cae97b7-3bf3-4107-96d5-39ad153629db",
> >         "userName": "psmith",
> >         "sn": "Smith",
> >         "givenName": "Patricia",
> >         "mail": "psmith@example.com",
> >         "telephoneNumber": "082082082",
> >         "accountStatus": "active",
> >         "_ref": "managed/realm-name_user/9cae97b7-3bf3-4107-96d5-39ad153629db",
> >         "_refResourceCollection": "managed/realm-name_user",
> >         "_refResourceId": "9cae97b7-3bf3-4107-96d5-39ad153629db",
> >         "_refProperties": {
> >           "_id": "5bc2c633-8ae1-4ea2-adf6-8aa7ce5f8e70",
> >           "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1233"
> >         }
> >       },
> >       "roles": [
> >         {
> >           "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-181",
> >           "_id": "testManagedRole",
> >           "name": "testManagedRole",
> >           "description": "a managed role for test",
> >           "_ref": "managed/realm-name_role/testManagedRole",
> >           "_refResourceCollection": "managed/realm-name_role",
> >           "_refResourceId": "testManagedRole",
> >           "_refProperties": {
> >             "_id": "a33e2de0-83ff-481c-b8a7-8ffbc02d135c",
> >             "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1235"
> >           }
> >         }
> >       ],
> >       "authzRoles": []
> >     },
> >     {
> >       "_id": "aca0042c-9f4c-4ad5-8cf7-aca0adeb3470",
> >       "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1267",
> >       "userName": "jdoe",
> >       "sn": "Doe",
> >       "givenName": "John",
> >       "mail": "jdoe@example.com",
> >       "telephoneNumber": "082082082",
> >       "preferences": {
> >         "updates": true,
> >         "marketing": false
> >       },
> >       "accountStatus": "active",
> >       "reports": [],
> >       "manager": {
> >         "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1223",
> >         "_id": "9cae97b7-3bf3-4107-96d5-39ad153629db",
> >         "userName": "psmith",
> >         "sn": "Smith",
> >         "givenName": "Patricia",
> >         "mail": "psmith@example.com",
> >         "telephoneNumber": "082082082",
> >         "accountStatus": "active",
> >         "_ref": "managed/realm-name_user/9cae97b7-3bf3-4107-96d5-39ad153629db",
> >         "_refResourceCollection": "managed/realm-name_user",
> >         "_refResourceId": "9cae97b7-3bf3-4107-96d5-39ad153629db",
> >         "_refProperties": {
> >           "_id": "e01a922b-a60d-46c2-b6bc-2b821c1580b4",
> >           "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1262"
> >         }
> >       },
> >       "roles": [
> >         {
> >           "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-181",
> >           "_id": "testManagedRole",
> >           "name": "testManagedRole",
> >           "description": "a managed role for test",
> >           "_ref": "managed/realm-name_role/testManagedRole",
> >           "_refResourceCollection": "managed/realm-name_role",
> >           "_refResourceId": "testManagedRole",
> >           "_refProperties": {
> >             "_id": "1528ab24-3ec3-4113-ac3f-26cc71a2d678",
> >             "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1264"
> >           }
> >         }
> >       ],
> >       "authzRoles": []
> >     },
> >     {
> >       "_id": "2d726b2a-3324-44b3-ba40-91b154d4f51e",
> >       "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1305",
> >       "userName": "bjensen",
> >       "sn": "Jensen",
> >       "givenName": "Barbara",
> >       "mail": "bjensen@example.com",
> >       "telephoneNumber": "082082082",
> >       "accountStatus": "active",
> >       "reports": [],
> >       "manager": null,
> >       "roles": [],
> >       "authzRoles": [
> >         {
> >           "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-300",
> >           "_id": "testInternalRole",
> >           "name": "internal_role_with_object_array_and_relationship_privileges",
> >           "description": "an internal role that has privileges for object & array types and relationships",
> >           "_ref": "internal/role/testInternalRole",
> >           "_refResourceCollection": "internal/role",
> >           "_refResourceId": "testInternalRole",
> >           "_refProperties": {
> >             "_id": "2e21f423-f934-4ed7-b6fd-9883b69d52d8",
> >             "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1304"
> >           }
> >         }
> >       ]
> >     }
> >   ],
> >   "resultCount": 4,
> >   "pagedResultsCookie": null,
> >   "totalPagedResultsPolicy": "NONE",
> >   "totalPagedResults": -1,
> >   "remainingPagedResults": -1
> > }
> > ```
>
> > **Collapse: Read a Specified User's Preferences Object**
> >
> > ```
> > curl \
> > --header "X-OpenIDM-Username: bjensen" \
> > --header "X-OpenIDM-Password: Passw0rd" \
> > --request GET \
> > "https://<tenant-env-fqdn>/openidm/managed/realm-name_user/aca0042c-9f4c-4ad5-8cf7-aca0adeb3470?_fields=preferences"
> > {
> >   "_id": "aca0042c-9f4c-4ad5-8cf7-aca0adeb3470",
> >   "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1267",
> >   "preferences": {
> >     "updates": true,
> >     "marketing": false
> >   }
> > }
> > ```
>
> > **Collapse: Query a Specified User's Roles**
> >
> > ```
> > curl \
> > --header "X-OpenIDM-Username: bjensen" \
> > --header "X-OpenIDM-Password: Passw0rd" \
> > --request GET \
> > "https://<tenant-env-fqdn>/openidm/managed/realm-name_user/917bc052-ef39-4add-ae05-0a278e2de9c0/roles?_queryFilter=true&_fields=*"
> > {
> >   "result": [
> >     {
> >       "_id": "a33e2de0-83ff-481c-b8a7-8ffbc02d135c",
> >       "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1235",
> >       "name": "testManagedRole",
> >       "description": "a managed role for test",
> >       "_refResourceCollection": "managed/realm-name_role",
> >       "_refResourceId": "testManagedRole",
> >       "_refResourceRev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-181",
> >       "_ref": "managed/realm-name_role/testManagedRole",
> >       "_refProperties": {
> >         "_id": "a33e2de0-83ff-481c-b8a7-8ffbc02d135c",
> >         "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1235"
> >       }
> >     }
> >   ],
> >   "resultCount": 1,
> >   "pagedResultsCookie": null,
> >   "totalPagedResultsPolicy": "NONE",
> >   "totalPagedResults": -1,
> >   "remainingPagedResults": -1
> > }
> > ```
>
> > **Collapse: Read a Specified User's Manager**
> >
> > ```
> > curl \
> > --header "X-OpenIDM-Username: bjensen" \
> > --header "X-OpenIDM-Password: Passw0rd" \
> > --request GET \
> > "https://<tenant-env-fqdn>/openidm/managed/realm-name_user/917bc052-ef39-4add-ae05-0a278e2de9c0/manager?_fields=*"
> > {
> >   "_id": "5bc2c633-8ae1-4ea2-adf6-8aa7ce5f8e70",
> >   "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1233",
> >   "userName": "psmith",
> >   "sn": "Smith",
> >   "givenName": "Patricia",
> >   "mail": "psmith@example.com",
> >   "telephoneNumber": "082082082",
> >   "accountStatus": "active",
> >   "_refResourceCollection": "managed/realm-name_user",
> >   "_refResourceId": "9cae97b7-3bf3-4107-96d5-39ad153629db",
> >   "_refResourceRev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1223",
> >   "_ref": "managed/realm-name_user/9cae97b7-3bf3-4107-96d5-39ad153629db",
> >   "_refProperties": {
> >     "_id": "5bc2c633-8ae1-4ea2-adf6-8aa7ce5f8e70",
> >     "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1233"
> >   }
> > }
> > ```
>
> > **Collapse: Update a Specified User's Reports**
> >
> > ```
> > curl \
> > --header "X-OpenIDM-Username: bjensen" \
> > --header "X-OpenIDM-Password: Passw0rd" \
> > --header "Content-Type: application/json" \
> > --request PATCH \
> > --data '[ {
> >    "operation" : "replace",
> >    "field" : "reports",
> >    "value" : [{"_ref" : "managed/realm-name_user/917bc052-ef39-4add-ae05-0a278e2de9c0"}]
> > } ]' \
> > "https://<tenant-env-fqdn>/openidm/managed/realm-name_user/9cae97b7-3bf3-4107-96d5-39ad153629db"
> > {
> >   "_id": "9cae97b7-3bf3-4107-96d5-39ad153629db",
> >   "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1223",
> >   "userName": "psmith",
> >   "sn": "Smith",
> >   "givenName": "Patricia",
> >   "mail": "psmith@example.com",
> >   "telephoneNumber": "082082082",
> >   "accountStatus": "active"
> > }
> > ```
>
> > **Collapse: Assign a Specified User's Manager**
> >
> > ```
> > curl \
> > --header "X-OpenIDM-Username: bjensen" \
> > --header "X-OpenIDM-Password: Passw0rd" \
> > --header "Content-Type: application/json" \
> > --request PATCH \
> > --data '[
> >   {
> >     "operation": "add",
> >     "field": "manager",
> >     "value": {"_ref" : "managed/realm-name_user/9cae97b7-3bf3-4107-96d5-39ad153629db"}
> >   }
> > ]' \
> > "https://<tenant-env-fqdn>/openidm/managed/realm-name_user/aca0042c-9f4c-4ad5-8cf7-aca0adeb3470"
> > {
> >   "_id": "aca0042c-9f4c-4ad5-8cf7-aca0adeb3470",
> >   "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1517",
> >   "userName": "jdoe",
> >   "sn": "Doe",
> >   "givenName": "John",
> >   "mail": "jdoe@example.com",
> >   "telephoneNumber": "082082082",
> >   "preferences": {
> >     "updates": true,
> >     "marketing": false
> >   },
> >   "accountStatus": "active"
> > }
> > ```
>
> > **Collapse: Remove a Specified User's Manager**
> >
> > ```
> > curl \
> > --header "X-OpenIDM-Username: bjensen" \
> > --header "X-OpenIDM-Password: Passw0rd" \
> > --header "Content-Type: application/json" \
> > --request PATCH \
> > --data '[
> >   {
> >      "operation": "remove",
> >      "field": "manager"
> >   }
> > ]' \
> > "https://<tenant-env-fqdn>/openidm/managed/realm-name_user/aca0042c-9f4c-4ad5-8cf7-aca0adeb3470"
> > {
> >   "_id": "aca0042c-9f4c-4ad5-8cf7-aca0adeb3470",
> >   "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1545",
> >   "userName": "jdoe",
> >   "sn": "Doe",
> >   "givenName": "John",
> >   "mail": "jdoe@example.com",
> >   "telephoneNumber": "082082082",
> >   "preferences": {
> >     "updates": true,
> >     "marketing": false
> >   },
> >   "accountStatus": "active"
> > }
> > ```
>
> > **Collapse: Update a Specified User's Manager**
> >
> > ```
> > curl \
> > --header "X-OpenIDM-Username: bjensen" \
> > --header "X-OpenIDM-Password: Passw0rd" \
> > --header "Content-Type: application/json" \
> > --request PATCH \
> > --data '[
> >   {
> >     "operation": "replace",
> >     "field": "manager",
> >     "value": {"_ref" : "managed/realm-name_user/aca0042c-9f4c-4ad5-8cf7-aca0adeb3470"}
> >   }
> > ]' \
> > "https://<tenant-env-fqdn>/openidm/managed/realm-name_user/917bc052-ef39-4add-ae05-0a278e2de9c0"
> > {
> >   "_id": "917bc052-ef39-4add-ae05-0a278e2de9c0",
> >   "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1565",
> >   "userName": "scarter",
> >   "sn": "Carter",
> >   "givenName": "Steven",
> >   "mail": "scarter@example.com",
> >   "telephoneNumber": "082082082",
> >   "preferences": {
> >     "updates": true,
> >     "marketing": false
> >   },
> >   "accountStatus": "active"
> > }
> > ```
>
> > **Collapse: Delete a Specified User**
> >
> > ```
> > curl \
> > --header "X-OpenIDM-Username: bjensen" \
> > --header "X-OpenIDM-Password: Passw0rd" \
> > --header "Content-Type: application/json" \
> > --request DELETE \
> > "https://<tenant-env-fqdn>/openidm/managed/realm-name_user/9cae97b7-3bf3-4107-96d5-39ad153629db"
> > {
> >   "_id": "9cae97b7-3bf3-4107-96d5-39ad153629db",
> >   "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1223",
> >   "userName": "psmith",
> >   "sn": "Smith",
> >   "givenName": "Patricia",
> >   "mail": "psmith@example.com",
> >   "telephoneNumber": "082082082",
> >   "accountStatus": "active"
> > }
> > ```
>
> > **Collapse: Create a User**
> >
> > * Using POST:
> >
> >   ```
> >   curl \
> >   --header "Content-Type: application/json" \
> >   --header "X-OpenIDM-Username: bjensen" \
> >   --header "X-OpenIDM-Password: Passw0rd" \
> >   --request POST \
> >   --data '{
> >     "userName": "psmith",
> >     "sn": "Smith",
> >     "givenName": "Patricia",
> >     "mail": "psmith@example.com",
> >     "telephoneNumber": "082082082",
> >     "password": "Passw0rd"
> >   }' \
> >   "https://<tenant-env-fqdn>/openidm/managed/realm-name_user"
> >   {
> >     "_id": "1a20930b-cf61-4b43-a730-9f73af9147cb",
> >     "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-571",
> >     "userName": "psmith",
> >     "sn": "Smith",
> >     "givenName": "Patricia",
> >     "mail": "psmith@example.com",
> >     "telephoneNumber": "082082082",
> >     "accountStatus": "active"
> >   }
> >   ```
> >
> > * Using PUT:
> >
> >   ```
> >   curl \
> >   --header "Content-Type: application/json" \
> >   --header "X-OpenIDM-Username: bjensen" \
> >   --header "X-OpenIDM-Password: Passw0rd" \
> >   --header "If-None-Match: *" \
> >   --request PUT \
> >   --data '{
> >     "userName": "psmith",
> >     "sn": "Smith",
> >     "givenName": "Patricia",
> >     "mail": "psmith@example.com",
> >     "telephoneNumber": "082082082",
> >     "password": "Passw0rd"
> >   }' \
> >   "https://<tenant-env-fqdn>/openidm/managed/realm-name_user/psmith"
> >   {
> >     "_id": "psmith",
> >     "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-590",
> >     "userName": "psmith",
> >     "sn": "Smith",
> >     "givenName": "Patricia",
> >     "mail": "psmith@example.com",
> >     "telephoneNumber": "082082082",
> >     "accountStatus": "active"
> >   }
> >   ```
> >
> > |   |                                                                                              |
> > | - | -------------------------------------------------------------------------------------------- |
> > |   | Delegated administration may not work as expected if `_id` is something *other* than a UUID. |
>
> |   |                                                                                                         |
> | - | ------------------------------------------------------------------------------------------------------- |
> |   | For more examples, including working with filters, refer to the [Postman collection](#da-postman-coll). |

|   |                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | All patches are done with a PATCH request. Delegated administrator operations do not currently support using POST actions for patch requests (POST `_action=patch` will not work). |