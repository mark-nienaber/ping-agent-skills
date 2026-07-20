---
title: Administrative users
description: Replace the default PingIDM openidm-admin user with a custom internal user by creating a new admin account and updating authentication configuration
component: pingidm
version: 8.1
page_id: pingidm:auth-guide:admin-users
canonical_url: https://docs.pingidentity.com/pingidm/8.1/auth-guide/admin-users.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Administration"]
---

# Administrative users

The default IDM administrative user is `openidm-admin`. In a production environment, you might want to replace this user with a managed or internal user with the same roles, specifically the `openidm-admin` and `openidm-authorized` roles.

You can create either an internal or managed user with the same roles as the default `openidm-admin` user. To add these roles to an existing managed user, refer to [Grant Internal Authorization Roles Manually](authorization-and-roles.html#granting-internal-roles). The following procedure creates a new administrative internal user (`admin`):

1. Create an internal user:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --header "Content-Type: application/json" \
   --cacert ca-cert.pem \
   --request PUT \
   --data '{
     "password": "Passw0rd"
   }' \
   "https://localhost:8443/openidm/internal/user/admin"
   {
     "_id": "admin",
     "_rev": "00000000210f6746"
   }
   ```

2. Add a `STATIC_USER` authentication module to the authentication configuration:

   > **Collapse: Using the filesystem**
   >
   > Add the following to the `conf/authentication.json` file:
   >
   > ```json
   > {
   >   "name": "STATIC_USER",
   >   "properties": {
   >     "queryOnResource": "internal/user",
   >     "username": "admin",
   >     "password": {
   >       "$purpose": {
   >         "name": "idm.admin.password"
   >       }
   >     },
   >     "defaultUserRoles": [
   >       "internal/role/openidm-authorized",
   >       "internal/role/openidm-admin"
   >     ]
   >   },
   >   "enabled": true
   > }
   > ```

   > **Collapse: Using REST**
   >
   > ```
   > curl \
   > --header "X-OpenIDM-Username: openidm-admin" \
   > --header "X-OpenIDM-Password: openidm-admin" \
   > --header "Content-Type: application/json" \
   > --header "Accept-API-Version: resource=1.0" \
   > --cacert ca-cert.pem \
   > --request PATCH \
   > --data '[
   >   {
   >     "operation": "add",
   >     "field": "/serverAuthContext/authModules/-",
   >     "value": {
   >       "name": "STATIC_USER",
   >       "properties": {
   >         "queryOnResource": "internal/user",
   >         "username": "admin",
   >         "password": {
   >           "$purpose": {
   >             "name": "idm.admin.password"
   >           }
   >         },
   >         "defaultUserRoles": [
   >           "internal/role/openidm-authorized",
   >           "internal/role/openidm-admin"
   >         ]
   >       },
   >       "enabled": true
   >     }
   >   }
   > ]' \
   > "https://localhost:8443/openidm/config/authentication"
   > {
   >   "_id": "authentication",
   >   "serverAuthContext": {
   >     ...
   >     "authModules": [
   >       ...
   >       {
   >         "name": "STATIC_USER",
   >         "properties": {
   >           "queryOnResource": "internal/user",
   >           "username": "admin",
   >           "password": {
   >             "$purpose": {
   >               "name": "idm.admin.password"
   >             }
   >           },
   >           "defaultUserRoles": [
   >             "internal/role/openidm-authorized",
   >             "internal/role/openidm-admin"
   >           ]
   >         },
   >         "enabled": true
   >       },
   >       ...
   >     ]
   >   }
   > }
   > ```

3. In `conf/secrets.json`, add a new mapping for the `idm.admin.password` secret:

   ```json
   {
       "secretId": "idm.admin.password",
       "format": "PLAIN",
       "types": [
           "GENERIC"
       ]
   }
   ```

   |   |                                                                                                                                |
   | - | ------------------------------------------------------------------------------------------------------------------------------ |
   |   | Only use the optional `format` parameter if the secret is encoded using a different scheme than the rest of the secret volume. |

4. In the directory that you've configured to be your filesystem secret store, create a file named `idm.admin.password` and populate it with your secret data:

   ```json
   {
     "password":"Passw0rd"
   }
   ```

   Learn more about [Filesystem secret stores](../security-guide/secret-stores-filesystem.html).

5. To verify the changes, perform a REST call or sign on to the admin UI as the new admin user. For example, query the list of internal users:

   ```
   curl \
   --header "X-OpenIDM-Username: admin" \
   --header "X-OpenIDM-Password: Passw0rd" \
   --header "Accept-API-Version: resource=1.0" \
   --cacert ca-cert.pem \
   --request GET \
   "https://localhost:8443/openidm/internal/user?_queryFilter=true"
   {
     "result": [
       {
         "_id": "admin",
         "_rev": "00000000f8e1665a"
       }
     ],
     ...
   }
   ```

6. *After* you've verified the new admin user, you can delete or disable the `openidm-admin` user:

   > **Collapse: Delete 'openidm-admin' User**
   >
   > 1. Delete the `openidm-admin` object:
   >
   >    ```
   >    curl \
   >    --header "X-OpenIDM-Username: admin" \
   >    --header "X-OpenIDM-Password: Passw0rd" \
   >    --header "Accept-API-Version: resource=1.0" \
   >    --cacert ca-cert.pem \
   >    --request DELETE \
   >    "https://localhost:8443/openidm/internal/user/openidm-admin"
   >    {
   >      "_id": "openidm-admin",
   >      "_rev": "00000000210f6746"
   >    }
   >    ```
   >
   > 2. Delete the authentication module for `"username" : "openidm-admin"`:
   >
   >    > **Collapse: Using the Filesystem**
   >    >
   >    > Edit the `conf/authentication.json` file, and delete:
   >    >
   >    > ```json
   >    > {
   >    >   "name" : "STATIC_USER",
   >    >   "properties" : {
   >    >     "queryOnResource" : "internal/user",
   >    >     "username" : "openidm-admin",
   >    >     "password" : "&{openidm.admin.password}",
   >    >     "defaultUserRoles" : [
   >    >       "internal/role/openidm-authorized",
   >    >       "internal/role/openidm-admin"
   >    >     ]
   >    >   },
   >    >   "enabled" : true
   >    > }
   >    > ```
   >
   >    > **Collapse: Using REST**
   >    >
   >    > 1. Get the current authentication configuration:
   >    >
   >    >    ```
   >    >    curl \
   >    >    --header "X-OpenIDM-Username: openidm-admin" \
   >    >    --header "X-OpenIDM-Password: openidm-admin" \
   >    >    --header "Accept-API-Version: resource=1.0" \
   >    >    --cacert ca-cert.pem \
   >    >    --request GET \
   >    >    "https://localhost:8443/openidm/config/authentication"
   >    >    {
   >    >      "_id": "authentication",
   >    >      "serverAuthContext": {
   >    >        ...
   >    >        "authModules": [
   >    >          ...
   >    >          {
   >    >            "name": "STATIC_USER",
   >    >            "properties": {
   >    >              "queryOnResource": "internal/user",
   >    >              "username": "openidm-admin",
   >    >              "password": "&{openidm.admin.password}",
   >    >              "defaultUserRoles": [
   >    >                "internal/role/openidm-authorized",
   >    >                "internal/role/openidm-admin"
   >    >              ]
   >    >            },
   >    >            "enabled": true
   >    >          },
   >    >          ...
   >    >        ]
   >    >      }
   >    >    }
   >    >    ```
   >    >
   >    > 2. Remove the authentication module for `"username" : "openidm-admin"` and replace the authentication configuration:
   >    >
   >    >    ```
   >    >    curl \
   >    >    --header "X-OpenIDM-Username: openidm-admin" \
   >    >    --header "X-OpenIDM-Password: openidm-admin" \
   >    >    --header "Accept-API-Version: resource=1.0" \
   >    >    --header "Content-Type: application/json" \
   >    >    --cacert ca-cert.pem \
   >    >    --request PUT \
   >    >    --data '{
   >    >      "_id": "authentication",
   >    >      "serverAuthContext": {
   >    >        "sessionModule": {
   >    >          "name": "JWT_SESSION",
   >    >          "properties": {
   >    >            "maxTokenLifeMinutes": 120,
   >    >            "tokenIdleTimeMinutes": 30,
   >    >            "sessionOnly": true,
   >    >            "isHttpOnly": true,
   >    >            "enableDynamicRoles": false
   >    >          }
   >    >        },
   >    >        "authModules": [
   >    >          {
   >    >            "name": "STATIC_USER",
   >    >            "properties": {
   >    >              "queryOnResource": "internal/user",
   >    >              "username": "anonymous",
   >    >              "password": {
   >    >                "$crypto": {
   >    >                  "type": "x-simple-encryption",
   >    >                  "value": {
   >    >                    "cipher": "AES/CBC/PKCS5Padding",
   >    >                    "stableId": "openidm-sym-default",
   >    >                    "salt": "xBlTp67ze4Ca5LTocXOpoA==",
   >    >                    "data": "mdibV6UabU2M+M5MK7bjFQ==",
   >    >                    "keySize": 16,
   >    >                    "purpose": "idm.config.encryption",
   >    >                    "iv": "36D2+FumKbaUsndNQ+/+5w==",
   >    >                    "mac": "ZM8GMnh0n80QwtSH6QsNmA=="
   >    >                  }
   >    >                }
   >    >              },
   >    >              "defaultUserRoles": [
   >    >                "internal/role/openidm-reg"
   >    >              ]
   >    >            },
   >    >            "enabled": true
   >    >          },
   >    >          {
   >    >            "name": "STATIC_USER",
   >    >            "properties": {
   >    >              "queryOnResource": "internal/user",
   >    >              "username": "admin",
   >    >              "password": "{encrypted password}",
   >    >              "defaultUserRoles": [
   >    >                "internal/role/openidm-authorized",
   >    >                "internal/role/openidm-admin"
   >    >              ]
   >    >            },
   >    >            "enabled": true
   >    >          },
   >    >          {
   >    >            "name": "MANAGED_USER",
   >    >            "properties": {
   >    >              "augmentSecurityContext": {
   >    >                "type": "text/javascript",
   >    >                "source": "require('auth/customAuthz').setProtectedAttributes(security)"
   >    >              },
   >    >              "queryId": "credential-query",
   >    >              "queryOnResource": "managed/user",
   >    >              "propertyMapping": {
   >    >                "authenticationId": "username",
   >    >                "userCredential": "password",
   >    >                "userRoles": "authzRoles"
   >    >              },
   >    >              "defaultUserRoles": [
   >    >                "internal/role/openidm-authorized"
   >    >              ]
   >    >            },
   >    >            "enabled": true
   >    >          }
   >    >        ]
   >    >      }
   >    >    }' \
   >    >    "https://localhost:8443/openidm/config/authentication"
   >    >    ```
   >
   > 3. Prevent the `openidm-admin` user from being recreated on startup.
   >
   >    Delete the following lines from the `internal/user` array in `conf/repo.init.json`:
   >
   >    ```json
   >    {
   >        "id" : "openidm-admin",
   >        "password" : "&{openidm.admin.password}"
   >    }
   >    ```

   > **Collapse: Disable 'openidm-admin' User**
   >
   > Change the `enabled` state of the authentication module for `"username" : "openidm-admin"`:
   >
   > > **Collapse: Using the Filesystem**
   > >
   > > Edit the `conf/authentication.json` file:
   > >
   > > ```json
   > > {
   > >   "name" : "STATIC_USER",
   > >   "properties" : {
   > >     "queryOnResource" : "internal/user",
   > >     "username" : "openidm-admin",
   > >     "password" : "&{openidm.admin.password}",
   > >     "defaultUserRoles" : [
   > >       "internal/role/openidm-authorized",
   > >       "internal/role/openidm-admin"
   > >     ]
   > >   },
   > >   "enabled" : false
   > > }
   > > ```
   >
   > > **Collapse: Using REST**
   > >
   > > 1. Get the current authentication configuration:
   > >
   > >    ```
   > >    curl \
   > >    --header "X-OpenIDM-Username: openidm-admin" \
   > >    --header "X-OpenIDM-Password: openidm-admin" \
   > >    --header "Accept-API-Version: resource=1.0" \
   > >    --cacert ca-cert.pem \
   > >    --request GET \
   > >    "https://localhost:8443/openidm/config/authentication"
   > >    {
   > >      "_id": "authentication",
   > >      "serverAuthContext": {
   > >        ...
   > >        "authModules": [
   > >          ...
   > >          {
   > >            "name": "STATIC_USER",
   > >            "properties": {
   > >              "queryOnResource": "internal/user",
   > >              "username": "openidm-admin",
   > >              "password": "&{openidm.admin.password}",
   > >              "defaultUserRoles": [
   > >                "internal/role/openidm-authorized",
   > >                "internal/role/openidm-admin"
   > >              ]
   > >            },
   > >            "enabled": true
   > >          },
   > >          ...
   > >        ]
   > >      }
   > >    }
   > >    ```
   > >
   > > 2. Change the enabled state of the authentication module for `"username" : "openidm-admin"` and replace the authentication configuration:
   > >
   > >    ```
   > >    curl \
   > >    --header "X-OpenIDM-Username: openidm-admin" \
   > >    --header "X-OpenIDM-Password: openidm-admin" \
   > >    --header "Accept-API-Version: resource=1.0" \
   > >    --header "Content-Type: application/json" \
   > >    --cacert ca-cert.pem \
   > >    --request PUT \
   > >    --data '{
   > >      "_id": "authentication",
   > >      "serverAuthContext": {
   > >        "sessionModule": {
   > >          "name": "JWT_SESSION",
   > >          "properties": {
   > >            "maxTokenLifeMinutes": 120,
   > >            "tokenIdleTimeMinutes": 30,
   > >            "sessionOnly": true,
   > >            "isHttpOnly": true,
   > >            "enableDynamicRoles": false
   > >          }
   > >        },
   > >        "authModules": [
   > >          {
   > >            "name": "STATIC_USER",
   > >            "properties": {
   > >              "queryOnResource": "internal/user",
   > >              "username": "anonymous",
   > >              "password": {
   > >                "$crypto": {
   > >                  "type": "x-simple-encryption",
   > >                  "value": {
   > >                    "cipher": "AES/CBC/PKCS5Padding",
   > >                    "stableId": "openidm-sym-default",
   > >                    "salt": "xBlTp67ze4Ca5LTocXOpoA==",
   > >                    "data": "mdibV6UabU2M+M5MK7bjFQ==",
   > >                    "keySize": 16,
   > >                    "purpose": "idm.config.encryption",
   > >                    "iv": "36D2+FumKbaUsndNQ+/+5w==",
   > >                    "mac": "ZM8GMnh0n80QwtSH6QsNmA=="
   > >                  }
   > >                }
   > >              },
   > >              "defaultUserRoles": [
   > >                "internal/role/openidm-reg"
   > >              ]
   > >            },
   > >            "enabled": true
   > >          },
   > >          {
   > >            "name": "STATIC_USER",
   > >            "properties": {
   > >              "queryOnResource": "internal/user",
   > >              "username": "openidm-admin",
   > >              "password": "&{openidm.admin.password}",
   > >              "defaultUserRoles": [
   > >                "internal/role/openidm-authorized",
   > >                "internal/role/openidm-admin"
   > >              ]
   > >            },
   > >            "enabled": false
   > >          },
   > >          {
   > >            "name": "MANAGED_USER",
   > >            "properties": {
   > >              "augmentSecurityContext": {
   > >                "type": "text/javascript",
   > >                "source": "require('auth/customAuthz').setProtectedAttributes(security)"
   > >              },
   > >              "queryId": "credential-query",
   > >              "queryOnResource": "managed/user",
   > >              "propertyMapping": {
   > >                "authenticationId": "username",
   > >                "userCredential": "password",
   > >                "userRoles": "authzRoles"
   > >              },
   > >              "defaultUserRoles": [
   > >                "internal/role/openidm-authorized"
   > >              ]
   > >            },
   > >            "enabled": true
   > >          }
   > >        ]
   > >      }
   > >    }' \
   > >    "https://localhost:8443/openidm/config/authentication"
   > >    ```

---

---
title: Authenticate as a different user
description: Configure PingIDM to allow admin users to authenticate as other users using the `X-OpenIDM-RunAs` header and `runAsProperties`
component: pingidm
version: 8.1
page_id: pingidm:auth-guide:auth-run-as
canonical_url: https://docs.pingidentity.com/pingidm/8.1/auth-guide/auth-run-as.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Impersonation"]
---

# Authenticate as a different user

The `X-OpenIDM-RunAs` header lets an administrative user *masquerade* as a regular user, without needing that user's password. To support this header, you must add the `runAsProperties` object to the `properties` of your authentication module. For example:

```json
"runAsProperties" : {
    "adminRoles" : [
        "internal/role/openidm-admin"
    ],
    "disallowedRunAsRoles" : [
        "internal/role/openidm-admin"
    ],
    "defaultUserRoles" : [
        "internal/role/openidm-authorized"
    ],
    "queryId" : "credential-query",
    "queryOnResource" : "managed/user",
    "propertyMapping" : {
        "authenticationId" : "username",
        "userRoles" : "authzRoles"
    },
    "augmentSecurityContext" : {
        "type" : "text/javascript",
        "source" : "require('auth/customAuthz').setProtectedAttributes(security)"
    }
}
```

This configuration lets a user who authenticates with the `openidm-admin` role masquerade as any user *except* one with the `openidm-admin` role.

If you are adding this configuration to the `STATIC_USER` module, and you are using [Delegated administration](delegated-admin.html), you must add an additional `propertyMapping` to the `properties` of the authentication module. This mapping forces the privileges to be re-read into the security context when the session JWT is used on subsequent requests. For example:

```json
"propertyMapping" : {
    "authenticationId" : "username"
}
```

The sample `authentication.json` file in `openidm/samples/example-configurations/conf/runas/` adds the `runAsProperties` object to the `STATIC_USER` module. Users or clients who authenticate with this module can then masquerade as other users.

In the following example, the `openidm-admin` user authenticates with the `STATIC_USER` module, and can run REST calls as user `bjensen` without that user's password:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "X-OpenIDM-RunAs: bjensen" \
--request GET \
"http://localhost:8080/openidm/info/login"
{
  "_id": "login",
  "authenticationId": "bjensen",
  "authorization": {
    "userRolesProperty": "authzRoles",
    "component": "managed/user",
    "authLogin": false,
    "adminUser": "openidm-admin",
    "roles": [
      "internal/role/openidm-authorized"
    ],
    "ipAddress": "[0:0:0:0:0:0:0:1]",
    "authenticationId": "openidm-admin",
    "protectedAttributeList": [
      "password"
    ],
    "id": "bjensen",
    "moduleId": "STATIC_USER",
    "queryId": "credential-query"
  }
}
```

The authentication output shows that the request was made as user `bjensen` but with an `adminUser` of `openidm-admin`. This information is also logged in the authentication audit log.

If you were to actually authenticate as user `bjensen`, without the `runAs` header, the user is authenticated with the `MANAGED_USER` authentication module. The output still shows an `authenticationId` of `bjensen` but there is no reference to an `adminUser`:

```
curl \
--header "X-OpenIDM-Username: bjensen" \
--header "X-OpenIDM-Password: Passw0rd" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"http://localhost:8080/openidm/info/login"
{
  "_id": "login",
  "authenticationId": "bjensen",
  "authorization": {
    "userRolesProperty": "authzRoles",
    "component": "managed/user",
    "authLogin": false,
    "authenticationIdProperty": "username",
    "roles": [
      "internal/role/openidm-authorized"
    ],
    "ipAddress": "[0:0:0:0:0:0:0:1]",
    "authenticationId": "bjensen",
    "protectedAttributeList": [
      "password"
    ],
    "id": "bjensen",
    "moduleId": "MANAGED_USER",
    "queryId": "credential-query"
  }
}
```

---

---
title: Authenticate through AM
description: Configure PingIDM to authenticate through PingAM using OAuth 2.0 bearer tokens and the rsFilter, including subject mappings, static user mappings, and testing
component: pingidm
version: 8.1
page_id: pingidm:auth-guide:rsfilter-auth
canonical_url: https://docs.pingidentity.com/pingidm/8.1/auth-guide/rsfilter-auth.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "OAuth 2.0"]
section_ids:
  test-rsfilter-auth: Test authentication through AM
---

# Authenticate through AM

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | From IDM 7.0 onwards, using AM bearer tokens for authentication is the only supported method of integrating IDM with AM. |

PingAM (AM) is a product that provides an infrastructure for managing users, roles, and access to resources. When you use IDM and AM together in a *platform deployment*, you must configure IDM to use AM bearer tokens for authentication. This delegates all authentication to AM. In this configuration:

* IDM uses an `rsFilter` that replaces all other authentication methods.

* All IDM endpoints that require authentication are accessed using an authorization header that contains the bearer token, instead of `X-OpenIDM-Username` and `X-OpenIDM-Password`. Endpoints that allow anonymous access can be accessed without a token.

To use AM bearer tokens for authentication, your AM configuration must include at least the following configuration:

* Two OAuth 2.0 clients: an `idm-resource-server` client to introspect the bearer token and an `idm-provisioning` client used by AM to provision users in IDM. For information on configuring these clients, refer to [Configure OAuth Clients (separate identity stores)](https://backstage.forgerock.com/docs/platform/7.5/platform-setup-guide/am-setup-1.html#oauth-clients) or [Configure OAuth Clients (shared identity store)](https://backstage.forgerock.com/docs/platform/7.5/platform-setup-guide/am-setup-2.html#oauth-clients-2) in the sample platform deployments.

* An [OAuth 2 provider service (separate identity stores)](https://backstage.forgerock.com/docs/platform/7.5/platform-setup-guide/am-setup-1.html#oauth-service) or [OAuth 2 provider service (shared identity store)](https://backstage.forgerock.com/docs/platform/7.5/platform-setup-guide/am-setup-2.html#oauth-service-2).

* An [IDM provisioning service (separate identity stores)](https://backstage.forgerock.com/docs/platform/7.5/platform-setup-guide/am-setup-1.html#idm-prov-service) or [IDM provisioning service (shared identity store)](https://backstage.forgerock.com/docs/platform/7.5/platform-setup-guide/am-setup-2.html#idm-prov-service-2).

Your IDM authentication configuration *(tooltip: You can manage the authentication configuration over REST at the config/authentication endpoint, or directly in the conf/authentication.json file.)* must include the `rsFilter` configuration and *no other* authentication methods.

Sample `rsFilter` configuration

The following sample `rsFilter` configuration is also available in `/path/to/openidm/samples/example-configurations/conf/rsfilter/authentication.json`:

> **Collapse: Sample rsFilter authentication**
>
> ```json
> {
>     "rsFilter" : {
>         "clientId" : "test",
>         "clientSecret" : "changeme",
>         "tokenIntrospectUrl" : "http://am.example:8080/openam/oauth2/introspect",
>         "scopes" : [ ],
>         "cache" : {
>             "maxTimeout" : "300 seconds"
>         },
>         "augmentSecurityContext" : {
>             "type" : "text/javascript",
>             "source" : "require('auth/orgPrivileges').assignPrivilegesToUser(resource, security, properties, subjectMapping, privileges, 'privileges', 'privilegeAssignments');"
>         },
>         "subjectMapping" : [
>             {
>                 "resourceTypeMapping" : {
>                     "usr" : "managed/user"
>                 },
>                 "propertyMapping" : {
>                     "sub" : "_id"
>                 },
>                 "userRoles" : "authzRoles/*",
>                 "additionalUserFields" : [
>                     "adminOfOrg",
>                     "ownerOfOrg"
>                 ],
>                 "defaultRoles" : [
>                     "internal/role/openidm-authorized"
>                 ]
>             }
>         ],
>         "staticUserMapping" : [
>             {
>                 "subject" : "(usr!amadmin)",
>                 "localUser" : "internal/user/openidm-admin",
>                 "roles" : [
>                     "internal/role/openidm-authorized",
>                     "internal/role/openidm-admin"
>                 ]
>             },
>             {
>                 "subject" : "(age!idm-provisioning)",
>                 "localUser" : "internal/user/idm-provisioning",
>                 "roles" : [
>                     "internal/role/platform-provisioning"
>                 ]
>             }
>         ],
>         "anonymousUserMapping" : {
>             "localUser" : "internal/user/anonymous",
>             "roles" : [
>                 "internal/role/openidm-reg"
>             ],
>             "executeAugmentationScript" : false
>         }
>     }
> }
> ```

The `rsFilter` configuration includes the following properties:

* `clientId`

  The client ID of the AM OAuth 2.0 client used to introspect the bearer token (the `idm-resource-server`) client, in this example).

* `clientSecret`

  The client secret of the AM OAuth 2.0 client used to introspect the bearer token. IDM encrypts this field if it isn't already.

* `tokenIntrospectUrl`

  The URI to reach the `oauth2/introspect` endpoint in AM; for example, `http://am.example:8080/openam/oauth2/introspect`.

* `scopes`

  Any scopes required to be present in the access token. This varies depending on your configuration. For more information about scopes, refer to [OAuth 2.0 Scopes](https://docs.pingidentity.com/pingam/8.1/oauth2-guide/oauth2-scopes.html#delegating-realm-administration-privileges) in the AM *OAuth 2.0 Guide*.

* `cache`

  Sets the `maxTimeout`, in seconds, after which the token is removed from the cache.

* `augmentSecurityContext`

  Specifies a script that is executed only after a successful authentication request. The script helps to populate the expected security context. For more information, refer to [The `augmentSecurityContext` trigger](../scripting-guide/script-variables-augment-security.html).

  |   |                                                                                                                                                                                                                                                                   |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | You can disable execution of the script for anonymous and static user mappings using [the `executeAugmentationScript` property](#executeAugmentationScript). Doing so can improve IDM's performance for user mappings where it's not necessary to run the script. |

* `subjectMapping`

  An array of mappings that let you map AM realms to IDM managed object types. For example:

  ```json
  "subjectMapping" : [
      {
          "resourceTypeMapping" : {
              "usr" : "managed/user"
          },
          "propertyMapping" : {
              "sub" : "_id"
          },
          "userRoles" : "authzRoles/*",
          "additionalUserFields" : [
              "adminOfOrg",
              "ownerOfOrg"
          ],
          "defaultRoles" : [
              "internal/role/openidm-authorized"
          ]
      }
  ],
  ```

  Each `subjectMapping` includes the following properties:

  * Either a `resourceTypeMapping` or a `queryOnResource` property:

    * `resourceTypeMapping`: Maps the identity type of a subject claim in AM to a resource collection in IDM. In the access token, the subject claim is a compound identity that consists of the claim `type` and subject name, separated by a `!`.

      To use a `resourceTypeMapping`, unique Oauth2 subject claims must be enabled in AM. (From AM 7.1, these are enabled by default.) For more information about subject claims, refer to *About the Subject and the Subname Claims* in the section on [/oauth2/userinfo](https://docs.pingidentity.com/pingam/8.1/oidc1-guide/rest-api-oidc-userinfo-endpoint.html).

    * `queryOnResource`: The IDM resource to check for the authenticating user; for example, `managed/user`.

      |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | If your AM and IDM deployments use consistent realm and managed object naming, you can configure the `resourceTypeMapping` and the `queryOnResource` properties to let a single subject mapping match multiple realms. This uses a dynamic handlebars template, as in the following example:Example configuration```json
      "resourceTypeMapping" : {
          "usr" : "managed/{{substring realm 1}}"
      }
      ```This configuration lets an access token with the realm `employee` map to an IDM `managed/employee`, and an access token with the realm `contractor` map to an IDM `managed/contractor`. |

  * `realm`: The AM realm to which this subject mapping applies. A value of `/` specifies the top-level realm. If this property is absent, the mapping can apply to any realm, which is useful if the `resourceTypeMapping` or `queryOnResource` uses a dynamic handlebars template.

    You cannot have more than one mapping for the same realm, and you cannot have more than one mapping that has no `realm` in the configuration.

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

  Although you can configure an array of subject mappings, only one mapping is selected and used during the authentication process. If there is a `realm` attribute in the access token, that realm is used to select an appropriate mapping. If no mapping is defined for the access token's realm, or if the realm is not provided in the access token, the authentication uses a mapping that does not define a `realm`.

Subject mapping with a Remote Connector Server (RCS)

If you have an RCS that is authenticating against AM, you must add a subject mapping for it.

Example configuration

```json
{
    "subject" : "RCS-OAuth-clientId",
    "localUser" : "internal/user/idm-provisioning"
}
```

The `subject` property must be the OAuth2 client in AM set up for the remote connector server. The `localUser` property can be any existing user.

|   |                                                                                                 |
| - | ----------------------------------------------------------------------------------------------- |
|   | Do not assign the `localUser` any roles. Doing so can allow the RCS bearer token to be misused. |

* `staticUserMapping`

  Maps AM users to a matching IDM user. This mapping can contain multiple user mappings, each with the following properties:

  * `subject`: The subject of the access token is the AM user. If you've specified a `resourceTypeMapping`, the static user mapping includes the full new subject string to match service accounts or static subject mappings, for example:

    ```json
    "subject" : "(usr!amadmin)"
    ```

    |   |                                                                                                                                                                                                                                                                                                                                                    |
    | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | The `idm-provisioning` subject is a service account used by AM to provision users in IDM. You *must* include this subject in your `staticUserMapping`, for example:```json
    {
        "subject": "(age!idm-provisioning)",
        "localUser": "internal/user/idm-provisioning",
        "roles" : [
            "internal/role/platform-provisioning"
        ]
    }
    ``` |

  * `localUser`: The IDM user you want to associate with the AM user identified in `subject`. For example, if `subject` is set to `(usr!amadmin)`, you can set the corresponding `localUser` to `internal/user/openidm-admin`.

  * `roles`: The default IDM roles that this mapped user has after they authenticate.

    |   |                                                                                                                                                                                                                      |
    | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | Roles defined in `staticUserMapping` use the access policies defined in `conf/access.json`. Learn more about configuring access control in `access.json` in [Authorization and roles](authorization-and-roles.html). |

  * []()`executeAugmentationScript`: A boolean value. When `false`, the scripts specified in `augmentSecurityContext` will not run for the user mapping.

* `anonymousUserMapping`

  The default user used when no access token is included in the request. Contains the following:

  * `localUser`: The IDM user resource referenced when no specific user is identified. For example, `internal/user/anonymous`.

  * `roles`: The default roles the anonymous user has, usually `internal/role/openidm-reg`.

  * `executeAugmentationScript`: A boolean value. When `false`, the scripts specified in `augmentSecurityContext` will not run for the user mapping.

## Test authentication through AM

1. Obtain a bearer token from AM. For example:

   ```
   curl \
   --header "X-OpenAM-Username: amAdmin" \
   --header "X-OpenAM-Password: password" \
   --header "Accept-API-Version: resource=2.0, protocol=1.0" \
   --request POST \
   --data "grant_type=client_credentials" \
   --data "client_id=idm-provisioning" \
   --data "client_secret=openidm" \
   --data "scope=fr:idm:*" \
   "http://am.example.com:8080/am/oauth2/realms/root/access_token"
   {
     "access_token": "z4uKDWiv4wnxKY7OjeG04PujG8E",
     "scope": "fr:idm:*",
     "token_type": "Bearer",
     "expires_in": 3599
   }
   ```

2. Authenticate to IDM using that bearer token:

   ```
   curl \
   --request GET \
   --header "Content-Type: application/json" \
   --header "Authorization: Bearer z4uKDWiv4wnxKY7OjeG04PujG8E" \
   'http://localhost:8080/openidm/info/login'
   {
     "_id": "login",
     "authenticationId": "idm-provisioning",
     "authorization": {
       "id": "idm-provisioning",
       "roles": [
         "internal/role/platform-provisioning"
       ],
       "component": "internal/user"
     }
   }
   ```

   Refer to the [sample platform setup](https://backstage.forgerock.com/docs/platform/7.5/platform-setup-guide/preface.html) documentation for instructions on setting up IDM to use AM bearer tokens for authentication.

---

---
title: Authenticate users
description: Authenticate PingIDM internal and managed users, customize authentication attributes and query filters, and change the default admin password
component: pingidm
version: 8.1
page_id: pingidm:auth-guide:authenticating-users
canonical_url: https://docs.pingidentity.com/pingidm/8.1/auth-guide/authenticating-users.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Internal Users", "Users"]
section_ids:
  authentication-attributes: Attributes used for authentication
  managing-internal-users: Internal users
  change-default-admin-pwd: Change the administrator user password
---

# Authenticate users

IDM stores two types of users in its repository—internal users and managed users.

* Internal users

  *Internal users* are special user accounts that are stored separately from regular users to protect them from any reconciliation or synchronization processes. When IDM first starts up, it creates three internal users in the repository by default—`openidm-admin`, `anonymous`, and `idm-provisioning`:

  * openidm-admin

    This user serves as the top-level administrator and has full access to all IDM resources. This account provides a fallback mechanism in the event that other users are locked out of their accounts. Do not use `openidm-admin` for regular tasks. Under normal circumstances, the `openidm-admin` account does not represent a regular user, so audit log records for this account do not represent the actions of any real person.

    The default password for the `openidm-admin` user is `openidm-admin`. In production environments, you should change this password, as described in [Change the Administrator User Password](#change-default-admin-pwd). The new password is symmetrically encrypted as it is changed.

  * anonymous

    This user enables anonymous access to IDM. It is used to interact with IDM in limited ways without further authentication, such as when a user has not yet logged in and makes a login request. The anonymous user account also allows self-registration.

    The default password for the `anonymous` user is `anonymous`.

  * idm-provisioning

    The internal user `idm-provisioning` is a service account used by AM to provision accounts in IDM. It has no password, and isn't meant to be logged in directly. If you are not planning to use AM and IDM together as a platform, you can safely remove this user.

* Managed users

  Regular user accounts that are stored in IDM's repository are called *managed users* because IDM effectively manages these accounts.

  Both internal and managed users *must* authenticate to gain access to the server. The way in which these user types are authenticated is defined in your project's `conf/authentication.json` file.

  Any request to IDM will authenticate the user and return a token. To improve tracing through logs, authenticate internal and managed users over REST by sending a POST request to the `openidm/authentication` endpoint, with `_action=login`. The following example authenticates the `openidm-admin` user:

  ```
  curl \
  --header "X-OpenIDM-Username: openidm-admin" \
  --header "X-OpenIDM-Password: openidm-admin" \
  --header "Accept-API-Version: resource=1.0" \
  --cacert ca-cert.pem \
  --request POST  \
  "https://localhost:8443/openidm/authentication?_action=login"
  ```

## Attributes used for authentication

By default, the attribute names that are used to authenticate managed and internal users are `username` and `password`. You can change the attributes that store authentication information with the `propertyMapping` object in the `conf/authentication.json` file. The following excerpt of the `authentication.json` file shows the default authentication attributes:

```json
...
    "propertyMapping" : {
        "authenticationId" : "username",
        "userCredential" : "password",
        "userRoles" : "authzRoles"
    },
...
```

If you change the attributes that are used for authentication, you must also change any authentication queries that use those attributes. The following authentication queries are referenced in `authentication.json`:

* `credential-internaluser-query` authenticates internal users.

* `credential-query` authenticates managed users.

* `for-username`

To change the authentication queries for a customized authentication attribute, create a `queryFilters.json` file in your project's `conf` directory. Include the authentication query IDs and the amended query filter, taking into account your changed attributes. The default authentication queries are as follows:

```json
{
  "credential-query": {
    "_queryFilter": "/userName eq \"${username}\" AND /accountStatus eq \"active\""
  },
  "credential-internaluser-query": {
    "_queryFilter": "/_id eq \"${username}\""
  },
  "for-userName": {
    "_queryFilter": "/userName eq \"${uid}\""
  }
}
```

The following example `conf/queryFilters.json` file shows the authentication queries adjusted to use the `email` attribute instead of the `username` attribute:

```json
{
  "credential-query": {
    "_queryFilter": "/email eq \"${email}\" AND /accountStatus eq \"active\""
  },
  "credential-internaluser-query": {
    "_queryFilter": "/_id eq \"${email}\""
  },
  "for-userName": {
    "_queryFilter": "/email eq \"${uid}\""
  }
}
```

## Internal users

Although internal users are considered to be special user accounts, you can manage them over the REST interface as you would any regular user in the repository.

To list the internal users over REST, query the `internal/user` endpoint as follows:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET  \
"http://localhost:8080/openidm/internal/user?_queryFilter=true&fields=_id"
{
  "result": [
    {
      "_id": "openidm-admin",
      "_rev": "00000000ec996921"
    },
    {
      "_id": "anonymous",
      "_rev": "00000000d95a68b1"
    },
    {
      "_id": "idm-provisioning",
      "_rev": "00000000817e3805"
    },
    {
      "_id": "connector-server-client",
      "_rev": "000000003f2a3a85"
    }
  ],
  ...
}
```

To query the details of an internal user, include the user ID in the request, for example:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET  \
"http://localhost:8080/openidm/internal/user/openidm-admin"
{
  "_id": "openidm-admin",
  "_rev": "00000000ec996921"
}
```

Internal users have specific authorization roles by default. These roles determine what the users can access in IDM. The `anonymous` user has only the `openidm-reg` role by default. This role grants only the resource access required to log in, register, and so forth. To identify the authorization roles for the `openidm-admin` internal user, and for information about creating and managing other administrative users, see [Administrative Users](admin-users.html).

## Change the administrator user password

The password of the `openidm-admin` user is `openidm-admin` by default. This password is set in the following excerpt of the `authentication.json` file:

```json
{
    "name" : "STATIC_USER",
    "properties" : {
        "queryOnResource" : "internal/user",
        "username" : "openidm-admin",
        "password" : "&{openidm.admin.password}",
        "defaultUserRoles" : [
            "internal/role/openidm-authorized",
            "internal/role/openidm-admin"
        ]
    },
    "enabled" : true
}
```

The `password` property references the `openidm.admin.password` property, set in `resolver/boot.properties`:

```properties
openidm.admin.password=openidm-admin
```

|   |                                                                                                                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Storing secrets and passwords directly in configuration and property files is [deprecated](../release-notes/deprecated-functionality.html#deprecation-secrets-in-config). Use [Secret stores](../security-guide/secret-stores.html) for secret resolution. |

You can change the default administrator password in a number of ways:

* Edit the `resolver/boot.properties` file before you start IDM (or restart IDM after you change this file).

* Set the value directly in the `conf/authentication.json` file.

* Update the authentication configuration over REST.

  > **Collapse: Show me how**
  >
  > 1. Get the current authentication configuration:
  >
  >    ```
  >    curl \
  >    --header "X-OpenIDM-Username: openidm-admin" \
  >    --header "X-OpenIDM-Password: openidm-admin" \
  >    --header "Accept-API-Version: resource=1.0" \
  >    --cacert ca-cert.pem \
  >    --request GET \
  >    "https://localhost:8443/openidm/config/authentication"
  >    {
  >      "_id": "authentication",
  >      "serverAuthContext": {
  >        ...
  >        "authModules": [
  >          ...
  >          {
  >            "name": "STATIC_USER",
  >            "properties": {
  >              "queryOnResource": "internal/user",
  >              "username": "openidm-admin",
  >              "password": "&{openidm.admin.password}",
  >              "defaultUserRoles": [
  >                "internal/role/openidm-authorized",
  >                "internal/role/openidm-admin"
  >              ]
  >            },
  >            "enabled": true
  >          },
  >          ...
  >        ]
  >      }
  >    }
  >    ```
  >
  > 2. Change the `password` field of this `STATIC_USER` module and replace the authentication configuration:
  >
  >    ```
  >    curl \
  >    --header "X-OpenIDM-Username: openidm-admin" \
  >    --header "X-OpenIDM-Password: openidm-admin" \
  >    --header "Accept-API-Version: resource=1.0" \
  >    --header "Content-Type: application/json" \
  >    --cacert ca-cert.pem \
  >    --request PUT \
  >    --data '{
  >      "_id": "authentication",
  >      "serverAuthContext": {
  >        "sessionModule": {
  >          "name": "JWT_SESSION",
  >          "properties": {
  >            "maxTokenLifeMinutes": 120,
  >            "tokenIdleTimeMinutes": 30,
  >            "sessionOnly": true,
  >            "isHttpOnly": true,
  >            "enableDynamicRoles": false
  >          }
  >        },
  >        "authModules": [
  >          {
  >            "name": "STATIC_USER",
  >            "properties": {
  >              "queryOnResource": "internal/user",
  >              "username": "anonymous",
  >              "password": {
  >                "$crypto": {
  >                  "type": "x-simple-encryption",
  >                  "value": {
  >                    "cipher": "AES/CBC/PKCS5Padding",
  >                    "stableId": "openidm-sym-default",
  >                    "salt": "xBlTp67ze4Ca5LTocXOpoA==",
  >                    "data": "mdibV6UabU2M+M5MK7bjFQ==",
  >                    "keySize": 16,
  >                    "purpose": "idm.config.encryption",
  >                    "iv": "36D2+FumKbaUsndNQ+/5w==",
  >                    "mac": "ZM8GMnh0n80QwtSH6QsNmA=="
  >                  }
  >                }
  >              },
  >              "defaultUserRoles": [
  >                "internal/role/openidm-reg"
  >              ]
  >            },
  >            "enabled": true
  >          },
  >          {
  >            "name": "STATIC_USER",
  >            "properties": {
  >              "queryOnResource": "internal/user",
  >              "username": "openidm-admin",
  >              "password": "newAdminPassword",
  >              "defaultUserRoles": [
  >                "internal/role/openidm-authorized",
  >                "internal/role/openidm-admin"
  >              ]
  >            },
  >            "enabled": true
  >          },
  >          {
  >            "name": "MANAGED_USER",
  >            "properties": {
  >              "augmentSecurityContext": {
  >                "type": "text/javascript",
  >                "source": "var augmentYield = require('auth/customAuthz').setProtectedAttributes(security);require('auth/orgPrivileges').assignPrivilegesToUser(resource, security, properties, subjectMapping, privileges, 'privileges', 'privilegeAssignments', augmentYield);"
  >              },
  >              "queryId": "credential-query",
  >              "queryOnResource": "{managed_user}",
  >              "propertyMapping": {
  >                "authenticationId": "username",
  >                "userCredential": "password",
  >                "userRoles": "authzRoles"
  >              },
  >              "defaultUserRoles": [
  >                "internal/role/openidm-authorized"
  >              ]
  >            },
  >            "enabled": true
  >          }
  >        ]
  >      }
  >    }' \
  >    "{secureHostname}/openidm/config/authentication"
  >    {
  >      "_id": "authentication",
  >      "serverAuthContext": {
  >        "sessionModule": {
  >          "name": "JWT_SESSION",
  >          "properties": {
  >            "maxTokenLifeMinutes": 120,
  >            "tokenIdleTimeMinutes": 30,
  >            "sessionOnly": true,
  >            "isHttpOnly": true,
  >            "enableDynamicRoles": false
  >          }
  >        },
  >        "authModules": [
  >          {
  >            "name": "STATIC_USER",
  >            "properties": {
  >              "queryOnResource": "internal/user",
  >              "username": "anonymous",
  >              "password": {
  >                "$crypto": {
  >                  "type": "x-simple-encryption",
  >                  "value": {
  >                    "cipher": "AES/CBC/PKCS5Padding",
  >                    "stableId": "openidm-sym-default",
  >                    "salt": "xBlTp67ze4Ca5LTocXOpoA==",
  >                    "data": "mdibV6UabU2M+M5MK7bjFQ==",
  >                    "keySize": 16,
  >                    "purpose": "idm.config.encryption",
  >                    "iv": "36D2+FumKbaUsndNQ/+5w==",
  >                    "mac": "ZM8GMnh0n80QwtSH6QsNmA=="
  >                  }
  >                }
  >              },
  >              "defaultUserRoles": [
  >                "internal/role/openidm-reg"
  >              ]
  >            },
  >            "enabled": true
  >          },
  >          {
  >            "name": "STATIC_USER",
  >            "properties": {
  >              "queryOnResource": "internal/user",
  >              "username": "openidm-admin",
  >              "password": {
  >                "$crypto": {
  >                  "type": "x-simple-encryption",
  >                  "value": {
  >                    "cipher": "AES/CBC/PKCS5Padding",
  >                    "stableId": "openidm-sym-default",
  >                    "salt": "l0trJWBzg5JKcWLzNq8QDA==",
  >                    "data": "MKAkL9FVEq/FnWq+8a90+QcjfkEbrK7W4tIc3ORD1ck=",
  >                    "keySize": 16,
  >                    "purpose": "idm.config.encryption",
  >                    "iv": "UMjU6crk332MZtEjo+wEmw==",
  >                    "mac": "7EvTqjpmuS9PmY1aCT2s+g=="
  >                  }
  >                }
  >              },
  >              "defaultUserRoles": [
  >                "internal/role/openidm-authorized",
  >                "internal/role/openidm-admin"
  >              ]
  >            },
  >            "enabled": true
  >          },
  >          {
  >            "name": "MANAGED_USER",
  >            "properties": {
  >              "augmentSecurityContext": {
  >                "type": "text/javascript",
  >                "source": "var augmentYield = require('auth/customAuthz').setProtectedAttributes(security);require('auth/orgPrivileges').assignPrivilegesToUser(resource, security, properties, subjectMapping, privileges, 'privileges', 'privilegeAssignments', augmentYield);"
  >              },
  >              "queryId": "credential-query",
  >              "queryOnResource": "managed/user",
  >              "propertyMapping": {
  >                "authenticationId": "username",
  >                "userCredential": "password",
  >                "userRoles": "authzRoles"
  >              },
  >              "defaultUserRoles": [
  >                "internal/role/openidm-authorized"
  >              ]
  >            },
  >            "enabled": true
  >          }
  >        ]
  >      }
  >    }
  >    ```

---

---
title: Authentication
description: "Overview of PingIDM authentication modes: classic authentication modules and OAuth2 Resource Server configuration using PingAM"
component: pingidm
version: 8.1
page_id: pingidm:auth-guide:authentication
canonical_url: https://docs.pingidentity.com/pingidm/8.1/auth-guide/authentication.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication"]
---

# Authentication

*Authentication* is the process of verifying who is requesting access to a resource. The user or application making the request presents credentials, making it possible to prove that the requester is who they claim to be. The goal is to authorize access to specific IDM resources, depending on the confirmed identity of the user or application making the request.

IDM supports two authentication modes:

* Using one or more of the *classic* IDM [authentication modules](auth-session-modules.html).

* Configuring IDM as an OAuth2 Resource Server in a *platform deployment* using [AM as the Identity Provider](rsfilter-auth.html).

---

---
title: Authentication and authorization
description: Overview of PingIDM authentication, authorization, and delegated administration configuration
component: pingidm
version: 8.1
page_id: pingidm:auth-guide:preface
canonical_url: https://docs.pingidentity.com/pingidm/8.1/auth-guide/preface.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["index.adoc"]
---

# Authentication and authorization

This guide covers authentication, authorization, and delegated administration.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Starting with IDM 8.1, the [legacy admin UI is deprecated](../release-notes/deprecated-functionality.html#legacy-admin-ui-deprecated) and is no longer bundled with IDM. New deployments should use the [Platform admin UI](../setup-guide/platform-admin-ui.html), which is the replacement for the legacy admin UI.Both UIs are available as separate downloads from the [Backstage download site](https://backstage.forgerock.com/downloads):- To install the Platform admin UI, follow the steps in [Install the Platform admin UI for standalone IDM](../setup-guide/platform-admin-ui.html).

- To continue using the legacy admin UI, follow the steps in [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html). |

[icon: id-card, set=fad, size=3x]

#### [Authentication](authentication.html)

Authenticate users securely.

[icon: user-ninja, set=fad, size=3x]

#### [Authorization & roles](authorization-and-roles.html)

The authorization configuration grants rights to users based on their roles.

[icon: users, set=fad, size=3x]

#### [Delegated administration](delegated-admin.html)

Use privileges to give fine-grained administrative access to specific users.

---

---
title: Authentication and roles
description: Understand how PingIDM assigns and calculates internal roles on authentication, including default roles, dynamic role calculation, and the security context
component: pingidm
version: 8.1
page_id: pingidm:auth-guide:authentication-and-roles
canonical_url: https://docs.pingidentity.com/pingidm/8.1/auth-guide/authentication-and-roles.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Roles", "Security Context"]
section_ids:
  dynamic-role-calculation: Dynamic role calculation
  auth-security-context: Roles, authentication, and the security context
---

# Authentication and roles

When a user authenticates, they are given a set of default *internal roles*. These roles determine how much access the user has to IDM. The default roles can be static roles assigned by definition in `authentication.json` or dynamic roles assigned by a relationship to the user.

You can configure internal roles using the admin UI or the REST API at the `openidm/internal/roles` endpoint.

The following internal roles are defined by default:

* openidm-admin

  IDM administrator role, excluded from the reauthorization required policy definition by default.

* openidm-authorized

  Default role for any user who authenticates with a username and password.

* openidm-cert

  Default role for any user who authenticates with mutual SSL authentication.

  This role applies only to mutual authentication. The shared secret (certificate) must be adequately protected. The `openidm-cert` role is excluded from the reauthorization required policy definition by default.

* openidm-reg

  Assigned to users who access IDM with the default anonymous account.

  The `openidm-reg` role is excluded from the reauthorization required policy definition by default.

* openidm-tasks-manager

  Role for users who can be assigned to workflow tasks.

* platform-provisioning

  Role for platform provisioning access. If you are not planning to run AM and IDM together as a platform, you can safely remove this role.

When a user authenticates, IDM calculates that user's roles as follows:

* Each authentication module includes a `defaultUserRoles` property. Depending on how the user authenticates, IDM assigns the roles listed in that module's `defaultUserRoles` property to the user on authentication. The `defaultUserRoles` property is specified as an array. For most authentication modules, the user obtains the `openidm-authorized` role on authentication. For example:

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

* If the authentication module includes a `groupRoleMapping`, `groupMembership`, or `groupComparison` property, IDM can assign additional roles to the user, depending on the user's group membership on an *external* system. For more information, refer to [Use Groups to Control Access to IDM](../objects-guide/groups-and-access-to-idm.html).

  |   |                                                                                                                                                                                  |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The roles calculated in sequence are cumulative. Roles with temporal restrictions are not included in that list if the current time is outside of the time assigned to the role. |

## Dynamic role calculation

By default, IDM calculates a user's roles only on authentication. You can configure IDM to recalculate a user's roles dynamically, with each request, instead of only when the user reauthenticates. To enable this feature, set `enableDynamicRoles` to `true` in the `JWT_SESSION` session module in `authentication.json`:

To enable dynamic role calculation through the admin UI, click Configure > Authentication > Session > Enable Dynamic Roles.

Dynamic role calculation can be used independently of the *privileges* mechanism, but is required for privileges to work. For more information about privileges, refer to [How Privileges Restrict Administrative Access](delegated-admin.html#using-privileges).

## Roles, authentication, and the security context

The Security Context (`context.security`), consists of a principal (defined by the `authenticationId` property) and an access control element (defined by the `authorization` property).

If authentication is successful, the authentication framework sets the principal. IDM stores that principal as the `authenticationId`.

The `authorization` property includes an `id`, an array of `roles`, and a `component`, that specifies the resource against which authorization is validated.

---

---
title: Authentication and session module configuration
description: Configuration properties for PingIDM authentication and session modules, including managed user, internal user, client cert, passthrough, and static user
component: pingidm
version: 8.1
page_id: pingidm:auth-guide:appendix-auth-modules
canonical_url: https://docs.pingidentity.com/pingidm/8.1/auth-guide/appendix-auth-modules.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Sessions", "Internal Users", "Certificates", "Passthrough Authentication"]
---

# Authentication and session module configuration

This appendix includes configuration details for the authentication modules described in [Authentication and Session Modules](auth-session-modules.html).

Authentication modules, as configured in the `authentication.json` file, include a number of properties.

**Session Module**

| Authentication Property | Property as Listed in the Admin UI | Description                                                                                             |
| ----------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `keyAlias`              | (not shown)                        | Used by the Jetty Web server to service SSL requests.                                                   |
| `maxTokenLifeMinutes`   | Max Token Life (in seconds)        | Maximum time before a session is cancelled. Note the different units for the property and the UI.       |
| `tokenIdleTimeMinutes`  | Token Idle Time (in seconds)       | Maximum time before an idle session is cancelled. Note the different units for the property and the UI. |
| `sessionOnly`           | Session Only                       | Whether the session continues after browser restarts.                                                   |

**Static User Module**

| Authentication Property | Property as Listed in the Admin UI | Description                                         |
| ----------------------- | ---------------------------------- | --------------------------------------------------- |
| `enabled`               | Module Enabled                     | Does IDM use the module?                            |
| `queryOnResource`       | Query on Resource                  | Endpoint hard coded to user `anonymous`             |
| `username`              | Static User Name                   | Default for the static user, `anonymous`            |
| `password`              | Static User Password               | Default for the static user, `anonymous`            |
| `defaultUserRoles`      | Static User Role                   | Normally set to `openidm-reg` for self-registration |

The following table applies to several authentication modules:

* Managed User

* Internal User

* Client Cert

* Passthrough

**Common Module Properties**

| Authentication Property  | Property as Listed in the Admin UI | Description                                                                                                                                                                              |
| ------------------------ | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enabled`                | Module Enabled                     | Does IDM use the module?                                                                                                                                                                 |
| `queryOnResource`        | Query on Resource                  | Endpoint to query                                                                                                                                                                        |
| `queryId`                | Use Query ID                       | A defined `queryId` searches against the `queryOnResource` endpoint. An undefined `queryId` searches against `queryOnResource` with `action=reauthenticate`                              |
| `defaultUserRoles`       | Default User Roles                 | Normally blank for managed users                                                                                                                                                         |
| `authenticationId`       | Authentication ID                  | Defines how account credentials are derived from a `queryOnResource` endpoint                                                                                                            |
| `userCredential`         | User Credential                    | Defines how account credentials are derived from a `queryOnResource` endpoint; if required, typically `password` or `userPassword`                                                       |
| `userRoles`              | User Roles                         | Defines how account roles are derived from a `queryOnResource` endpoint                                                                                                                  |
| `groupMembership`        | Group Membership                   | Provides more information for calculated roles                                                                                                                                           |
| `groupRoleMapping`       | Group Role Mapping                 | Provides more information for calculated roles                                                                                                                                           |
| `groupComparisonMethod`  | Group Comparison Method            | Provides more information for calculated roles                                                                                                                                           |
| `augmentSecurityContext` | Augment Security Context           | Includes a script that is executed only after a successful authentication request. For more information on this property, refer to [Authenticate as a different user](auth-run-as.html). |

---

---
title: Authentication and session modules
description: Configure PingIDM authentication and session modules including JWT_SESSION, MANAGED_USER, INTERNAL_USER, CLIENT_CERT, PASSTHROUGH, and STATIC_USER in `authentication.json`
component: pingidm
version: 8.1
page_id: pingidm:auth-guide:auth-session-modules
canonical_url: https://docs.pingidentity.com/pingidm/8.1/auth-guide/auth-session-modules.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Sessions", "Internal Users", "Certificates", "Passthrough Authentication"]
section_ids:
  jwt-session-module: JWT_SESSION
  authenticate_without_a_session: Authenticate without a session
  deterministic_ecdsa_signatures: Deterministic ECDSA signatures
  static-user-module: STATIC_USER
  managed-user-module: MANAGED_USER
  internal-user-module: INTERNAL_USER
  client-cert-module: CLIENT_CERT
  client-cert-demo: Test client certificate authentication
  passthrough-module: PASSTHROUGH
---

# Authentication and session modules

An authentication module specifies how a user or client is authenticated. You configure authentication and session modules in your project's `conf/authentication.json` file.

IDM evaluates authentication modules in the order in which they appear in that file, and uses the first "successful" authentication module it finds. Subsequent modules are not evaluated. In a production environment, you should remove any unused authentication modules from your `authentication.json` file.

To authenticate a user or client, IDM validates the provided credentials against some resource. That resource can be either an IDM resource such as `managed/user` or `internal/user`, or it can be an external resource such as an LDAP server. You should prioritize the authentication modules that query IDM resources over those that query external resources. Prioritizing modules that query external resources can lead to authentication problems for internal users such as `openidm-admin`.

You can also configure authentication modules in the admin UI. Select Configure > Authentication, and select the Session or Module tab. To change the order of authentication modules in the admin UI, simply drag the modules up or down so that they appear in the order in which they should be evaluated.

|   |                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Modifying an authentication module in the admin UI might affect your current session. In this case, IDM prompts you with the following message:```
Your current session may be invalid. Click here to logout and re-authenticate.
```When you select the Click here link, IDM logs you out of any current session and returns you to the login screen. |

IDM supports the following authentication and session modules:

## JWT\_SESSION

IDM supports one session module, the JSON Web Token (JWT) Session Module. When a client authenticates successfully, the JWT Session Module creates a JWT and sets it as a cookie on the response. On subsequent requests, the module checks for the presence of the JWT as a cookie on the request, validates the signature and decrypts it, and checks the expiration time of the JWT.

JWT sessions are entirely stateless, that is, they are not persisted in the backend. All information pertaining to the session is encrypted in the JWT.

When a request to IDM produces a JWT, that value replaces the previous one used to send that request. In this way the JWT is always updated to the latest copy. The idle timeout in the JWT is therefore continuously updated and active sessions are not abruptly killed mid-session.

By default, the JWT cookie is deleted on logout. Deleting the cookie manually ends the session. You can modify what happens to the session after a browser restart by changing the value of the `sessionOnly` property.

The default JWT Session Module configuration, in `conf/authentication.json` , is as follows:

```json
"sessionModule" : {
    "name" : "JWT_SESSION",
    "properties" : {
        "maxTokenLifeMinutes" : 120,
        "tokenIdleTimeMinutes" : 30,
        "sessionOnly" : true,
        "isHttpOnly" : true,
        "enableDynamicRoles" : false
    }
}
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * In a production environment, ensure that only secure cookies are used. To do so, add the following property to the session module configuration:

  ```json
  "isSecure" : true
  ```

* If your `authentication.json` file uses a non-default cookie name for `name.openidm.csrfFilter.authCookieName`, add the following property to the session module configuration:

  ```json
  "sessionCookieName": "customCookieName"
  ``` |

For more information about this module, refer to the [Class JwtSessionModule JavaDoc](https://docs.pingidentity.com/pingam/8.1/_attachments/apidocs/org/forgerock/jaspi/modules/session/jwt/JwtSessionModule.html).

Attempting to access IDM without the appropriate headers or session cookie results in an HTTP 401 Unauthorized, or HTTP 403 Forbidden, depending on the situation. If you authenticate using a session cookie, you must include an additional header that indicates the origin of the request.

The following example shows a successful authentication attempt and the return of a session cookie:

```
curl \
--dump-header /dev/stdout \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--cacert ca-cert.pem \
"https://localhost:8443/openidm/managed/user?_queryFilter=true&_fields=_id"
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
Cache-Control: no-cache
Set-Cookie: session-jwt=2l0zobpuk6st1b2m7gvhg5zas ...;Path=/
Expires: Thu, 01 Jan 1970 00:00:00 GMT
Vary: Accept-Encoding, User-Agent
Content-Length: 82
Server: Jetty(8.y.z-SNAPSHOT)
```

The following example uses the cookie returned in the previous response, and includes the `X-Requested-With` header to indicate the origin of the request. The value of the header can be any string, but should be informative for logging purposes. If you do not include the `X-Requested-With` header, IDM returns HTTP 403 Forbidden:

```
curl \
--dump-header /dev/stdout \
--header "Cookie: session-jwt=2l0zobpuk6st1b2m7gvhg5zas ..." \
--header "X-Requested-With: OpenIDM Plugin" \
--header "Accept-API-Version: resource=1.0" \
--cacert ca-cert.pem \
"https://localhost:8443/openidm/managed/user?_queryFilter=true&_fields=_id"
Expires: Thu, 01 Jan 1970 00:00:00 GMT
Content-Type: application/json; charset=UTF-8
Cache-Control: no-cache
Vary: Accept-Encoding, User-Agent
Content-Length: 82
Server: Jetty(8.y.z-SNAPSHOT)
```

The expiration date of the JWT cookie, January 1, 1970, corresponds to the start of UNIX time. Since that time is in the past, browsers will not store that cookie after the browser session is closed.

Authentication requests are logged in the `authentication.audit.json` file. A successful authentication request is logged as follows:

```json
{
  "_id": "389d15d3-bdd5-4521-ae3c-bf096d334405-915",
  "timestamp": "2019-08-02T11:53:31.110Z",
  "eventName": "SESSION",
  "transactionId": "389d15d3-bdd5-4521-ae3c-bf096d334405-912",
  "trackingIds": [
    "5f9f4941-bcbd-4cbc-97f7-e763808e4310",
    "88973bcf-0d60-41b8-9922-73718ce76e11"
  ],
  "userId": "openidm-admin",
  "principal": [
    "openidm-admin"
  ],
  "entries": [
    {
      "moduleId": "JwtSession",
      "result": "SUCCESSFUL",
      "info": {
        "org.forgerock.authentication.principal": "openidm-admin"
      }
    }
  ],
  "result": "SUCCESSFUL",
  "provider": null,
  "method": "JwtSession"
}
```

For information about querying this log, refer to [Query the Authentication Audit Log](../audit-guide/querying-audit-over-rest.html#querying-auth-log).

### Authenticate without a session

Once a client has authenticated, the `JWT_SESSION` takes precedence over any other authentication modules, for subsequent requests. In some cases, you might want to force clients to re-authenticate for each request. This is the case, for example, if you authenticate using a [client certificate](#client-cert-module).

To request one-time authentication without a session, use the `X-OpenIDM-NoSession` header in the authentication request. For example:

```http
curl \
--dump-header /dev/stdout \
--header "X-OpenIDM-NoSession: true" \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--cacert ca-cert.pem \
--header "Accept-API-Version: resource=1.0" \
"https://localhost:8443/openidm/managed/user?_queryFilter=true&_fields=_id"
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
Cache-Control: no-cache
Vary: Accept-Encoding, User-Agent
Content-Length: 82
Server: Jetty(8.y.z-SNAPSHOT)
```

### Deterministic ECDSA signatures

By default, JWTs are signed with [deterministic Elliptic Curve Digital Signature Algorithm (ECDSA)](https://www.rfc-editor.org/rfc/rfc6979.html). In order to use this more secure signing method, [Bouncy Castle](https://www.bouncycastle.org), which is included in the default IDM installation, must be installed. If Bouncy Castle is unavailable, or the key is incompatible, IDM falls back to normal ECDSA.

|   |                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you need to turn off the use of deterministic ECDSA, set the following property in your `conf/system.properties` file:```properties
org.forgerock.secrets.preferDeterministicEcdsa=false
``` |

## STATIC\_USER

The `STATIC_USER` module provides an authentication mechanism that avoids database lookups by hard coding a static user. IDM includes a default `anonymous` static user, but you can create any static user for this module.

The following sample REST call uses `STATIC_USER` authentication with the `anonymous` user in the self-registration process:

```
curl \
--header "X-OpenIDM-Password: anonymous" \
--header "X-OpenIDM-Username: anonymous" \
--header "Accept-API-Version: resource=1.0" \
--cacert ca-cert.pem \
--header "Content-Type: application/json" \
--request POST \
--data '{
  "userName": "steve",
  "givenName": "Steve",
  "sn": "Carter",
  "telephoneNumber": "0828290289",
  "mail": "scarter@example.com",
  "password": "Passw0rd"
}' \
"https://localhost:8443/openidm/managed/user/?_action=create"
```

|   |                                                                              |
| - | ---------------------------------------------------------------------------- |
|   | This is not the same as an anonymous request that is issued without headers. |

Authenticating with the `STATIC_USER` module avoids the performance cost of reading the database for self-registration, certain UI requests, and other actions that can be performed anonymously. Authenticating the anonymous user with the `STATIC_USER` module is identical to authenticating the anonymous user with the `INTERNAL_USER` module, except that the database is not accessed. So, `STATIC_USER` authentication provides an authentication mechanism for the anonymous user that avoids the database lookups incurred when using `INTERNAL_USER`.

A sample `STATIC_USER` authentication configuration follows:

```json
{
    "name" : "STATIC_USER",
    "enabled" : true,
    "properties" : {
        "queryOnResource" : "internal/user",
        "username" : "anonymous",
        "password" : "anonymous",
        "defaultUserRoles" : [
            "internal/role/openidm-reg"
        ]
    }
}
```

IDM also uses the `STATIC_USER` module to set the password and default roles of the `openidm-admin` internal user on startup. The following configuration in the `authentication.json` file sets up the `openidm-admin` user:

```json
{
    "name" : "STATIC_USER",
    "properties" : {
        "queryOnResource" : "internal/user",
        "username" : "openidm-admin",
        "password" : "&{openidm.admin.password}",
        "defaultUserRoles" : [
            "internal/role/openidm-authorized",
            "internal/role/openidm-admin"
        ]
    },
    "enabled" : true
}
```

Related topics:

* [Change the administrator user password (`openidm-admin`)](authenticating-users.html#change-default-admin-pwd)

* [Secure access to RCS](authorization-and-roles.html#secure-openicf-access)

## MANAGED\_USER

`MANAGED_USER` authentication queries the repository and allows authentication if the credentials match. Despite the module name, the query is not restricted to managed/user objects. The resource that is queried is configurable. The default configuration uses the `username` and `password` of a managed user to authenticate, as shown in the following sample configuration:

```json
{
    "name" : "MANAGED_USER",
    "properties" : {
        "augmentSecurityContext": {
            "type" : "text/javascript",
            "source" : "require('auth/customAuthz').setProtectedAttributes(security)"
        },
        "queryId" : "credential-query",
        "queryOnResource" : "managed/user",
        "propertyMapping" : {
            "authenticationId" : "username",
            "userCredential" : "password",
            "userRoles" : "authzRoles"
        },
        "defaultUserRoles" : [
            "internal/role/openidm-authorized"
        ]
    },
    "enabled" : true
}
```

Use the `augmentSecurityContext` property to add custom properties to the security context of users who authenticate with this module. By default, this property adds a list of *protected properties* to the user's security context. These protected properties are defined in the managed object schema. The `isProtected` property is described in [Create and modify object types](../objects-guide/creating-modifying-managed-objects.html).

## INTERNAL\_USER

`INTERNAL_USER` authentication queries the `internal/user` objects in the repository and allows authentication if the credentials match. An example configuration that uses the `username` and `password` of the internal user to authenticate follows:

```json
{
    "name" : "INTERNAL_USER",
    "enabled" : true,
    "properties" : {
        "queryId" : "credential-internaluser-query",
        "queryOnResource" : "internal/user",
        "propertyMapping" : {
            "authenticationId" : "username",
            "userCredential" : "password",
            "userRoles" : "authzRoles"
        },
        "defaultUserRoles" : [ ]
    }
}
```

## CLIENT\_CERT

Client certificate authentication (also called *mutual SSL authentication*) occurs as part of the SSL or TLS handshake, which takes place before any data is transmitted in an SSL or TLS session. This authentication module is typically used when users have secure certificates that they install in their browsers for authentication and authorization.

The client certificate module, `CLIENT_CERT`, authenticates by validating a client certificate, transmitted through an HTTP request. IDM compares the subject DN of the request certificate with the subject DN of the truststore.

A sample `CLIENT_CERT` authentication configuration follows:

```json
{
  "name" : "CLIENT_CERT",
  "properties" : {
    "augmentSecurityContext" : {
      "type" : "text/javascript",
      "globals" : { },
      "file" : "auth/mapUserFromClientCert.js"
    },
    "queryOnResource" : "managed/user",
    "defaultUserRoles" : [
      "internal/role/openidm-authorized"
    ],
    "allowedAuthenticationIdPatterns" : [
      ".*CN=localhost, O=ForgeRock.*"
    ]
  },
  "enabled" : true
}
```

When a user authenticates with a client certificate, they receive the roles listed in the `defaultUserRoles` property of the `CLIENT_CERT` module. Privileges are calculated dynamically per request when enabled in the session module.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Client certificate authentication is also used when the client is a password plugin, such as those described in [Password Plugins](../pwd-plugin-guide/preface.html). This process is similar to an administrative request to modify the passwords of regular users.For password plugin clients, you must include `internal/role/openidm-cert` in the `defaultUserRoles` array (in the authentication configuration *(tooltip: You can manage the authentication configuration over REST at the config/authentication endpoint, or directly in the conf/authentication.json file.)*). |

### Test client certificate authentication

This procedure demonstrates client certificate authentication by generating a self-signed certificate, adding that certificate to the truststore, then authenticating with the certificate. At the end of this procedure, you will verify the certificate over port `8444` as defined in your project's `resolver/boot.properties` file:

```
openidm.auth.clientauthonlyports=8444
```

The example assumes an existing managed user, bjensen, with email address `bjensen@example.com`.

1. Create a self-signed certificate for user bjensen as follows:

   ```
   openssl req \
   -x509 \
   -newkey rsa:2048 \
   -keyout /path/to/key.pem \
   -out /path/to/cert.pem \
   -days 3650 \
   -nodes
   Generating a 2048 bit RSA private key
   .................
   ..................
   writing new private key to 'key.pem'
   -----
   You are about to be asked to enter information that will be incorporated
   into your certificate request.
   What you are about to enter is what is called a Distinguished Name or a DN.
   There are quite a few fields but you can leave some blank
   For some fields there will be a default value,
   If you enter '.', the field will be left blank.
   -----
   Country Name (2 letter code) []: US
   State or Province Name (full name) []: Washington
   Locality Name (eg, city) []: Vancouver
   Organization Name (eg, company) []: Example.com
   Organizational Unit Name (eg, section) []:
   Common Name (eg, fully qualified host name) []: localhost
   Email Address []: bjensen@example.com
   ```

   |   |                                                                                                                 |
   | - | --------------------------------------------------------------------------------------------------------------- |
   |   | The `Email Address` is used by the `mapUserFromClientCert.js` to map the user against an existing managed user. |

2. Import the client certificate into the IDM truststore:

   ```
   keytool \
   -importcert \
   -keystore /path/to/openidm/security/truststore \
   -storetype JKS \
   -storepass changeit \
   -file /path/to/cert.pem \
   -trustcacerts \
   -noprompt \
   -alias client-cert-example
   Certificate was added to keystore
   ```

   By default, users can authenticate only if their certificates have been issued by a Certificate Authority (CA) that is listed in the truststore. The default truststore includes several trusted root CA certificates, and any user certificate issued by those CAs will be trusted. Change the value of this property to restrict certificates to those issued to users in your domain, or use some other regular expression to limit who will be trusted. If you leave this property empty, no certificates will be trusted.

3. Edit your project's `conf/authentication.json` file. Add the `CLIENT_CERT` module, and add at least the email address from the certificate subject DN to the `allowedAuthenticationIdPatterns`:

   ```json
   {
     "name": "CLIENT_CERT",
     "properties": {
       "augmentSecurityContext": {
         "type": "text/javascript",
         "globals": {},
         "file": "auth/mapUserFromClientCert.js"
       },
       "queryOnResource": "managed/user",
       "defaultUserRoles": [
         "internal/role/openidm-cert",
         "internal/role/openidm-authorized"
       ],
       "allowedAuthenticationIdPatterns": [
         ".*EMAILADDRESS=bjensen@example.com.*"
       ]
     },
     "enabled": true
   }
   ```

   |   |                                                                                                                                                                                                                                       |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The `allowedAuthenticationIdPatterns` property is unique to this authentication module. This property contains a regular expression that defines which user distinguished names (DNs) are allowed to authenticate with a certificate. |

4. Send an HTTP request with your certificate file `cert.pem` to the secure port:

   ```
   curl \
   --insecure \
   --cert-type PEM \
   --key /path/to/key.pem \
   --key-type PEM \
   --cert /path/to/cert.pem \
   --header "X-Requested-With: curl" \
   --header "X-OpenIDM-NoSession: true" \
   --request GET "https://localhost:8444/openidm/info/login"
   {
     "_id": "login",
     "authenticationId": "EMAILADDRESS=bjensen@example.com, CN=localhost, O=Example.com, L=Vancouver, ST=Washington, C=US",
     "authorization": {
       "userRolesProperty": "authzRoles",
       "component": "managed/user",
       "authLogin": false,
       "roles": [
         "internal/role/openidm-cert",
         "internal/role/openidm-authorized"
       ],
       "ipAddress": "0:0:0:0:0:0:0:1",
       "id": "aba3e666-c0db-4669-8760-0eb21f310649",
       "moduleId": "CLIENT_CERT"
     }
   }
   ```

|   |                                                                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * Because we have used a self-signed certificate in this example, you must include the `--insecure` option. You should not include this option if you are using a CA cert.

* You must use the `X-Requested-With` and `X-OpenIDM-NoSession` headers for HTTP-based requests that use the `CLIENT_CERT` authentication module. |

## PASSTHROUGH

`PASSTHROUGH` authentication queries an external system, such as an LDAP server, and allows authentication if the credentials included in the REST request match those in the external system.

The following excerpt of an `authentication.json` shows a pass-through authentication configuration for an LDAP system:

```json
"authModules" : [
    {
       "name" : "PASSTHROUGH",
       "enabled" : true,
       "properties" : {
          "augmentSecurityContext": {
             "type" : "text/javascript",
             "file" : "auth/populateAsManagedUser.js"
          },
          "queryOnResource" : "system/ldap/account",
          "propertyMapping" : {
             "authenticationId" : "uid",
             "groupMembership" : "ldapGroups"
          },
          "groupRoleMapping" : {
             "internal/role/openidm-admin" : ["cn=admins,ou=Groups,dc=example,dc=com"]
          },
          "defaultUserRoles" : [
             "internal/role/openidm-authorized"
          ]
       },
    },
    ...
]
```

For more information on authentication module properties, refer to [Authentication and session module configuration](appendix-auth-modules.html).

Many of the documented [samples](../samples-guide/samples-provided.html) are configured for pass-through authentication. For example, the `sync-with-ldap*` samples use an external LDAP system for authentication.

---

---
title: Authorization and roles
description: Configure PingIDM role-based authorization using `access.json` and `router-authz.js` to control REST endpoint access by role, method, and action
component: pingidm
version: 8.1
page_id: pingidm:auth-guide:authorization-and-roles
canonical_url: https://docs.pingidentity.com/pingidm/8.1/auth-guide/authorization-and-roles.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Roles", "Scripts"]
section_ids:
  router-authz-js: Modify and extend the router authorization script
  access-json: Configure access control in access.json
  access-control-rest: Change the access configuration over REST
  get_the_current_access_configuration: Get the Current Access Configuration
  replace_the_access_configuration: Replace the Access Configuration
  granting-internal-roles: Grant internal authorization roles manually
  managing-workflow-access: Secure access to workflows
  secure-openicf-access: Secure RCS access
---

# Authorization and roles

IDM provides role-based authorization that restricts direct HTTP access to REST interface URLs. This access control applies to direct HTTP calls only. Access for internal calls (for example, calls from scripts) is not affected by this mechanism.

When a user authenticates, they are given a set of default *roles*, as described in [Authentication and Roles](authentication-and-roles.html). The authorization configuration grants access rights to users, based on these roles acquired during authentication.

You can use internal and managed roles to restrict access, with the following caveats:

* Internal roles are not meant to be provisioned or synchronized with external systems.

* Internal roles cannot be given assignments.

* Event scripts (such as `onCreate`) cannot be attached to internal roles.

* The internal role schema is not configurable.

Authorization roles are referenced in a user's `authzRoles` property by default, and are assigned when the user authenticates.

By default, managed users are assigned the `openidm-authorized` role when they authenticate. The following request shows the authorization roles for user psmith when that user logs in to the server:

```
curl \
--header "X-OpenIDM-Username: psmith" \
--header "X-OpenIDM-Password: Passw0rd" \
--header "Accept-API-Version: resource=1.0" \
--cacert ca-cert.pem \
--request GET \
"https://localhost:8443/openidm/info/login"
{
  "_id": "login",
  "authenticationId": "psmith",
  "authorization": {
    "userRolesProperty": "authzRoles",
    "component": "managed/user",
    "authLogin": false,
    "authenticationIdProperty": "username",
    "roles": [
      "internal/role/openidm-authorized"
    ],
    "ipAddress": "0:0:0:0:0:0:0:1",
    "authenticationId": "psmith",
    "protectedAttributeList": [
      "password"
    ],
    "id": "psmith",
    "moduleId": "MANAGED_USER",
    "queryId": "credential-query"
  }
}
```

The authorization implementation is configured in two files:

* `openidm/bin/defaults/script/router-authz.js`

* `project-dir/conf/access.json`

IDM calls the `router-authz.js` script for each request, through an `onRequest` hook defined in the `router.json` file. `router-authz.js` references your project's access configuration (`access.json` ) to determine the allowed HTTP requests. If access is denied, according to the configuration defined in `access.json` , the `router-authz.js` script throws an exception, and IDM denies the request.

`router.json` also defines an `onResponse` script, `relationshipFilter`. This provides additional filtering to ensure that the user has the appropriate access to see the data of the related object. You can change this behavior by extending or updating `/bin/defaults/script/relationshipFilter.js` , or by removing the `onResponse` script if you don't want additional filtering on relationships. For more information about relationships, refer to [Configuring relationships](../objects-guide/relationships.html).

|   |                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------- |
|   | You can configure [delegated administration](delegated-admin.html) to grant access that bypasses this access control. |

## Modify and extend the router authorization script

The router authorization script (`router-authz.js` contains a number of functions that enforce access rules. For example, the following function controls whether users with a certain role can start a specified process:

```javascript
function isAllowedToStartProcess() {
    var processDefinitionId = request.content._processDefinitionId;
    var key = request.content._key;
    return isProcessOnUsersList(function (process) {
        return (process._id === processDefinitionId) || (process.key === key);
    });
}
```

You can extend the default authorization mechanism by defining additional functions in `router-authz.js` and by creating new access control rules in `access.json`.

|   |                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Some authorization-related functions in `router-authz.js` should *not* be altered, because they affect the security of the server. Such functions are indicated in the comments in that file. |

## Configure access control in `access.json`

The `access.json` configuration includes a set of rules that govern access to specific endpoints. These rules are tested in the order in which they appear in the file. You can define more than one rule for the same endpoint. If one rule passes, the request is allowed. If all the rules fail, the request is denied.

The following rule (from a default `access.json` file) shows the access configuration structure:

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

  The REST endpoint for which access is being controlled. `"*"` specifies access to all endpoints in that path. For example, `"managed/user/*"` specifies access to all managed user objects.

* `roles`

  A comma-separated list of the roles to which this access configuration applies.

  The `roles` referenced here align with the object's security context (`security.authorization.roles`). The `authzRoles` relationship property of a managed user produces this security context value during authentication.

* `methods`

  A comma-separated list of the methods that can be performed with this access. Methods can include `create, read, update, delete, patch, action, query`. A value of `"*"` indicates that all methods are allowed. A value of `""` indicates that no methods are allowed.

* `actions`

  A comma-separated list of the allowed actions. The possible actions depend on the resource (URL) that is being exposed. Note that the `actions` in the default `access.json` file do not list all the [supported actions](../scripting-guide/scripting-func-ref.html#supported-actions) on each resource.

  A value of `"*"` indicates that all actions exposed for that resource are allowed. A value of `""` indicates that no actions are allowed.

* `customAuthz`

  An optional parameter that lets you define a custom function for additional authorization checks. Custom functions are defined in `router-authz.js` .

* `excludePatterns`

  An optional parameter that lets you specify endpoints to which access should not be granted.

## Change the access configuration over REST

You can manage the access configuration at the endpoint `openidm/config/access`. To change an access rule, first get the current access configuration, amend it to change the access rule, then submit the updated configuration in a PUT request. This example restricts access to the `info` endpoint to users who have authenticated:

### Get the Current Access Configuration

Request

```none
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0"  \
--request GET \
"http://localhost:8080/openidm/config/access"
```

> **Collapse: Show response**
>
> Response
>
> ```json
> {
>   "_id": "access",
>   "configs": [
>     {
>       "pattern": "health",
>       "roles": "*",
>       "methods": "read",
>       "actions": ""
>     },
>     {
>       "pattern": "info/*",
>       "roles": "*",
>       "methods": "read",
>       "actions": "*"
>     },
>     ...
>   ]
> }
> ```

### Replace the Access Configuration

Shortened request

```none
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Content-type: application/json" \
--header "Accept-API-Version: resource=1.0"  \
--request PUT \
--data '{
  "_id": "access",
  "configs": [ access-config-object ]
}' \
"http://localhost:8080/openidm/config/access"
```

> **Collapse: Show response**
>
> Response
>
> ```json
> {
>   "_id": "access",
>   "configs": [
>     {
>       "pattern": "health",
>       "roles": "*",
>       "methods": "read",
>       "actions": ""
>     },
>     {
>       "pattern": "info/*",
>       "roles": "internal/role/openidm-authorized",
>       "methods": "read",
>       "actions": "*"
>     },
>     ...
>   ]
> }
> ```

## Grant internal authorization roles manually

Apart from the default roles that users get when they authenticate, you can grant internal authorization roles manually, over REST or using the admin UI. This mechanism works in the same way as the granting of managed roles. For information about granting managed roles, refer to [Grant Roles to a User](../objects-guide/roles-over-rest.html#granting-role-user). To grant an internal role manually through the admin UI:

1. From the navigation bar, click Manage > User, and click a user.

2. From the Authorization Roles tab, click Add Authorization Roles.

3. Select Internal Role as the Type, click in the Authorization Roles field to select from the list of defined Internal Roles, and click Add.

To manually grant an internal role over REST, add a reference to the internal role to the user's `authzRoles` property. The following command adds the `openidm-admin` role to user bjensen (with ID `9dce06d4-2fc1-4830-a92b-bd35c2f6bcbb`):

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--cacert ca-cert.pem \
--request PATCH \
--data '[
  {
    "operation": "add",
    "field": "/authzRoles/-",
    "value": {"_ref" : "internal/role/openidm-admin"}
  }
]' \
"https://localhost:8443/openidm/managed/user/9dce06d4-2fc1-4830-a92b-bd35c2f6bcbb"
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

You can also grant internal roles dynamically using [conditional role grants](../objects-guide/roles-over-rest.html#conditional-role-grants).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Because internal roles are not managed objects, you cannot manipulate them in the same way as managed roles. Therefore, you cannot add a user to an internal role, as you would to a managed role.To add users directly to an internal role, add the users as values of the role's `authzMembers` property. For example:```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Content-Type: application/json" \
--cacert ca-cert.pem \
--request POST \
--data '{"_ref":"managed/user/bjensen"}' \
"https://localhost:8443/openidm/internal/role/3042798d-37fd-49aa-bae3-52598d2c8dc4/authzMembers?_action=create"
``` |

## Secure access to workflows

The end-user UI is integrated with the embedded Flowable workflow engine, enabling users to interact with workflows. Available workflows are displayed under the Processes item on the dashboard. For a workflow to be displayed here, the workflow definition file must be present in the `openidm/workflow` directory.

|   |                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------- |
|   | The end-user UI is not bundled with PingIDM. Learn more in [Install the end-user UI](../setup-guide/idm-enduser-ui.html). |

General access to workflow-related endpoints is based on the access rules defined in the `conf/access.json` file. The configuration defined in `conf/process-access.json` specifies who can invoke workflows. By default, all users with the role `openidm-authorized` or `openidm-admin` can invoke any available workflow. The default `process-access.json` file is as follows:

```json
{
    "workflowAccess" : [
        {
            "propertiesCheck" : {
                "property" : "_id",
                "matches" : ".*",
                "requiresRole" : "internal/role/openidm-authorized"
            }
        },
        {
            "propertiesCheck" : {
                "property" : "_id",
                "matches" : ".*",
                "requiresRole" : "internal/role/openidm-admin"
            }
        }
    ]
}
```

* `property`

  Specifies the property used to identify the process definition. By default, process definitions are identified by their `_id`.

* `matches`

  A regular expression match is performed on the process definitions, according to the specified property. The default (`"matches" : ".*"`) implies that all process definition IDs match.

* `requiresRole`

  Specifies the authorization role that is required for users to have access to the matched process definition IDs. In the default file, users with the role `openidm-authorized` or `openidm-admin` have access.

To extend the process action definition file, identify the processes to which users should have access, and specify the qualifying authorization roles. For example, if you want to allow access to users with a role of `ldap`, add the following code block to the `process-access.json` file:

```json
{
    "propertiesCheck" : {
        "property" : "_id",
        "matches" : ".*",
        "requiresRole" : "ldap"
    }
}
```

To configure multiple roles with access to the same workflow process, simply add additional `propertiesCheck` objects. The following example grants access to users with a role of doctor and nurse to the same workflows:

```json
{
     "propertiesCheck" : {
          "property" : "_id",
          "matches" : ".*",
          "requiresRole" : "doctor"
     }
},
{
     "propertiesCheck" : {
          "property" : "_id",
          "matches" : ".*",
          "requiresRole" : "nurse"
     }
}
```

## Secure RCS access

You can secure the `openicf` WebSocket endpoint used for communication between IDM and RCS client mode. This allows you to control which users or roles can connect to this endpoint on behalf of a specific RCS instance. The `openicf` servlet in your access configuration (`access.json`) lets you manage authorization for the `openicf` endpoint.

1. In your authentication configuration *(tooltip: You can manage the authentication configuration over REST at the config/authentication endpoint, or directly in the conf/authentication.json file.)* (`conf/authentication.json`), add a specific role to the `roles` array of the RCS static user mapping. This role authorizes access to the `openicf` endpoint for the specified RCS.

   Example

   ```json
   {
       "subject": "rcsclient",
       "localUser": "internal/user/idm-provisioning",
       "roles": [
           "internal/role/myrcsserver-authorized" (1)
       ],
       "executeAugmentationScript": false
   }
   ```

   |       |                                                                                                                         |
   | ----- | ----------------------------------------------------------------------------------------------------------------------- |
   | **1** | In this example, the role `internal/role/myrcsserver-authorized` is added to the authenticated user's security context. |

2. Add a new rule in your access configuration (`conf/access.json`) to define authorization for the `openicf` endpoint.

   Example

   ```json
   {
       "servlet": "openicf", (2)
       "pattern": "myrcsserver", (3)
       "roles": "internal/role/myrcsserver-authorized", (1)
       "methods": "read"
   }
   ```

   This rule ensures that:

   |       |                                                                                      |
   | ----- | ------------------------------------------------------------------------------------ |
   | **1** | only users possessing the `internal/role/myrcsserver-authorized` role can access the |
   | **2** | `openicf` WebSocket endpoint                                                         |
   | **3** | for the RCS named `myrcsserver`.                                                     |

---

---
title: Character encoding in authentication headers
description: How to use RFC 5987-encoded non-ASCII characters in PingIDM authentication headers, with UTF-8 and ISO 8859-1 support
component: pingidm
version: 8.1
page_id: pingidm:auth-guide:authentication-headers-encoding
canonical_url: https://docs.pingidentity.com/pingidm/8.1/auth-guide/authentication-headers-encoding.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Character Encoding"]
---

# Character encoding in authentication headers

You can use [encoded characters](https://www.rfc-editor.org/rfc/rfc5987.html) in all three IDM authentication headers (`X-OpenIDM-Username`, `X-OpenIDM-Password`, and `X-OpenIDM-Reauth-Password`). This lets you use non-ASCII characters in these header values. The RFC 5987-encoding is automatically detected and decoded when present. The following character sets are supported:

* UTF-8

* ISO 8859-1

The following command shows a request for a user (openidm-admin) whose password is `Passw£rd123`. The Unicode `£` sign (U+00A3) is encoded into the octet sequence C2 A3 using UTF-8 character encoding, then percent-encoded:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: UTF-8''Passw%C2%A3rd123" \
--header "Accept-API-Version: resource=1.0" \
--cacert ca-cert.pem \
--request GET \
"https://localhost:8443/openidm/managed/user?_queryFilter=true&_fields=_id"
```

---

---
title: Delegated administration
description: Configure PingIDM delegated administration using privileges to grant fine-grained access to non-administrative users through roles and REST
component: pingidm
version: 8.1
page_id: pingidm:auth-guide:delegated-admin
canonical_url: https://docs.pingidentity.com/pingidm/8.1/auth-guide/delegated-admin.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Delegated Administration", "Privileges"]
section_ids:
  using-privileges: How privileges restrict administrative access
  determining-access-privileges: Determine access privileges
  creating-privileges: Create privileges
  adding_privileges_using_the_admin_ui: Adding privileges using the admin UI
  adding_privileges_using_rest: Adding privileges using REST
  privilege-policies: Policies related to privileges
  getting-privilege-resources: Get privileges on a resource
  using-delegated-admin: Create a delegated administrator
  configure_search_ui_for_delegated_administrators: Configure search UI for delegated administrators
  da-min-filter-length: Minimum filter search length
  da-disable-sort-filter-collections: Disable sort and filter for resource collections
---

# Delegated administration

Delegated administration lets you give fine-grained administrative access to specific users, based on a *privilege* mechanism.

## How privileges restrict administrative access

*Privileges* enable you to grant administrative access to specific endpoints and objects, without needing to grant full administrative access to the server. For example, you might want to allow users with a help desk or support role to update the information of another user, without allowing them to delete user accounts or change the IDM system configuration.

You can use privileges to delegate specific administrative capabilities to non-administrative users, without exposing the admin UI to those users. For example, if a user has been granted a privilege that allows them to access a list of users and user information, they can access this list directly through the end-user UI.

|   |                                                                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | A delegated administrator does not have access to the same methods over REST as a regular administrator. IDM does not allow delegated administrator requests such as POST or DELETE. To add or remove relationships, use PATCH. For examples, refer to [Managed roles](../objects-guide/managed-roles.html). |

The privilege mechanism requires dynamic role calculation, which is disabled by default. To enable it, set the `enableDynamicRoles` property to `true` in your `conf/authentication.json` file, or select Configure > Authentication > Session > Enable Dynamic Roles in the admin UI. For more information about dynamic role calculation, refer to [Dynamic Role Calculation](authentication-and-roles.html#dynamic-role-calculation).

For more information on managing privileges over REST, refer to [Privileges](../rest-api-reference/endpoints/rest-privileges.html).

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

  * Attributes marked as `"readOnly": false` can be viewed and edited.

  * Attributes that aren't listed in the `accessFlags` array cannot be viewed or edited.

    |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
    | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | * Privileges aren't automatically aware of changes to the managed object schema. If new properties are added, removed, or made mandatory, you must update any existing privileges to account for these changes. When a new property is added, it has a default permission level of `NONE` in existing privileges, including when the privilege is set to access all attributes.

    * PingIDM applies policy validation when creating or updating a privilege to ensure that all required properties are writable when the `CREATE` permission is assigned. This validation doesn't run when schema changes are made, so you must verify that any existing privileges adhere to defined policies. |

* actions

  A list of the specific actions allowed if the `ACTION` permission has been specified.

  |   |                                            |
  | - | ------------------------------------------ |
  |   | Allowed actions must be explicitly listed. |

* description (optional)

  A description of the privilege.

* filter (optional)

  This property lets you apply a static or dynamic query filter to the privilege, which can be used to limit the scope of what the privilege allows the user to access.

  Static filter example

  To allow a delegated administrator to access information only about users for the `stateProvince` of Washington, include a static filter, such as:

  ```json
  filter : "stateProvince eq \"Washington\""
  ```

  Dynamic filter example

  []()Dynamic filters insert values from the authenticated resource. To allow a delegated administrator to access information only about users in their own `stateProvince`, include a dynamic filter by wrapping the parameter in curly braces:

  ```json
  filter : "stateProvince eq \"{{stateProvince}}\""
  ```

  Users with query filter privileges can't edit the properties specified in the filter in ways that would cause the privilege to lose access to the object. For example, if a user with either of the preceding example privileges attempted to edit another user's `stateProvince` field to a value not matching the query filter, the request would return a `403 Forbidden` error.

  |   |                                                                                                                                                                                                                                                                                                                            |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Fields must be *searchable* by PingIDM to be used in a privilege filter. Ensure that the field you are filtering has `"searchable" : true` set in the `repo.jdbc.json` file.Privilege filters are an additional layer of filter to any other query filters you create. Any output must satisfy all filters to be included. |

* name

  The name of the privilege.

* path

  The path to the service that you want to allow members of this privilege to access. For example, `managed/user`.

* permissions

  A list of permissions this privilege allows for the given path. The following permissions are available:

  |          |                                                                                         |
  | -------- | --------------------------------------------------------------------------------------- |
  | `VIEW`   | Allows reading and querying the path, such as viewing and querying managed users.       |
  | `CREATE` | Allows creation at the path, such as creating new managed users.                        |
  | `UPDATE` | Allows updating or patching existing information, such as editing managed user details. |
  | `DELETE` | Allows deletion, such as deleting users from `managed/user`.                            |
  | `ACTION` | Allows users to perform actions at the given path, such as custom scripted actions.     |

  |   |                                                                   |
  | - | ----------------------------------------------------------------- |
  |   | If you use an `ACTION`, there can be no filters on the privilege. |

### Adding privileges using the admin UI

1. From the navigation bar, click Manage > Role.

2. On the Roles page, click the Internal tab, and then click an existing role or create a new role.

3. On the Role Name page, click the Privileges tab.

   PingIDM displays the current privileges for the role.

4. To add privileges, click Add Privileges.

   * In the Add a privilege window, enter information, as necessary, and click Add.

### Adding privileges using REST

The following example creates a new `support` role with privileges that let members view, create, and update information about users, but not delete users:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
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
    "path": "managed/user",
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
"https://localhost:8443/openidm/internal/role/support"
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
      "path": "managed/user",
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

  Verifies that the `path` specified in the privilege is a valid object with a schema for IDM to reference. Only objects with a schema (such as `managed/user`) can have privileges applied to them.

* `valid-query-filter`

  Verifies that the query filter used to filter privileges is a valid query.

For more information about policies and creating custom policies, refer to [Use policies to validate data](../objects-guide/policies.html).

## Get privileges on a resource

To determine which privileges a user has on a service, you can query the privilege endpoint for a given resource path or object, based on the user you are currently logged in as. For example, if a user is a member of the support role mentioned in the previous example, checking the user's privileges for the `managed/user` resource would look like this:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--cacert ca-cert.pem \
--request GET \
"https://localhost:8443/openidm/privilege/managed/user"
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

In addition to checking privileges for a resource, it is also possible to check privileges for specific objects within a resource, such as `managed/user/scarter`.

## Create a delegated administrator

You can use the IDM REST API to create an `internal/role` with privileges that have object, array, and relationship type attribute access. You can then use that role as a delegated administrator to perform operations on those attributes.

|   |                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you want to experiment with delegated administrators in [Postman](https://www.postman.com/), download and import this [Postman collection](../_attachments/Delegated-Administration.postman_collection.json). |

Use the following example to create a delegated administrator:

> **Collapse: Step 1. Create a Managed Role**
>
> To ensure a role object exists when roles are requested, you must create a managed role.
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Content-Type: application/json" \
> --header "If-None-Match: *" \
> --request PUT \
> --data '{
>   "name": "testManagedRole",
>   "description": "a managed role for test"
> }' \
> "http://localhost:8080/openidm/managed/role/testManagedRole"
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
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
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
> "http://localhost:8080/openidm/managed/user/?_action=create"
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
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
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
>   "manager": {"_ref": "managed/user/9cae97b7-3bf3-4107-96d5-39ad153629db"},
>   "roles": [{"_ref": "managed/role/testManagedRole"}]
> }' \
> "http://localhost:8080/openidm/managed/user/?_action=create"
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
>       "_refResourceCollection": "managed/role",
>       "_refResourceId": "testManagedRole",
>       "_ref": "managed/role/testManagedRole"
>     }
>   ],
>   "memberOfOrgIDs": [],
>   "effectiveAssignments": []
> }
> ```
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
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
>   "manager": {"_ref": "managed/user/9cae97b7-3bf3-4107-96d5-39ad153629db"},
>   "roles": [{"_ref": "managed/role/testManagedRole"}]
> }' \
> "http://localhost:8080/openidm/managed/user/?_action=create"
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
>       "_refResourceCollection": "managed/role",
>       "_refResourceId": "testManagedRole",
>       "_ref": "managed/role/testManagedRole"
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
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
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
> "http://localhost:8080/openidm/managed/user/?_action=create"
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
> * A `managed/user` privilege with accessFlags attributes that are of types: "String" , "boolean" , and "number" ; but also for:
>
>   * An object type that is not a relationship (`preferences`).
>
>   * An object type that is a relationship (`manager`).
>
>   * Array types that are relationships (`roles`, `authzRoles`, `reports`).
>
> * A `managed/role` privilege for viewing details of the "roles" property of a managed user.
>
> * An `internal/role` privilege for viewing the details of the "authzRoles" property of a managed user.
>
> |   |                                                                                                                                                                                                                                                                                                                                                                                                              |
> | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
> |   | You can populate the privilege `filter` field to apply a finer level of permissions for what a delegated administrator can access or do with certain objects. The `filter` field is omitted in this example to allow all.For properties that are *not* relationships, such as `preferences`, you can't specify finer-grained permissions. For example, you can't set permissions on `preferences/marketing`. |
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Content-Type: application/json" \
> --header "If-None-Match: *" \
> --request PUT \
> --data '{
>   "name": "internal_role_with_object_array_and_relationship_privileges",
>   "description": "an internal role that has privileges for object & array types and relationships",
>   "privileges": [
>     {
>       "name": "managed_user_privilege",
>       "path": "managed/user",
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
>       "path": "managed/role",
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
> "http://localhost:8080/openidm/internal/role/testInternalRole"
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
>       "path": "managed/user",
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
>       "path": "managed/role",
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
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Content-Type: application/json" \
> --request POST \
> --data '{
>   "_ref": "managed/user/2d726b2a-3324-44b3-ba40-91b154d4f51e",
>   "_refProperties": {}
> }' \
> "http://localhost:8080/openidm/internal/role/testInternalRole/authzMembers?_action=create"
> {
>   "_id": "2e21f423-f934-4ed7-b6fd-9883b69d52d8",
>   "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1304",
>   "_ref": "managed/user/2d726b2a-3324-44b3-ba40-91b154d4f51e",
>   "_refResourceCollection": "managed/user",
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
> > "http://localhost:8080/openidm/managed/user?_queryFilter=true&_pageSize=100&_fields=*,*_ref/*"
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
> >           "_ref": "managed/user/aca0042c-9f4c-4ad5-8cf7-aca0adeb3470",
> >           "_refResourceCollection": "managed/user",
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
> >           "_ref": "managed/user/917bc052-ef39-4add-ae05-0a278e2de9c0",
> >           "_refResourceCollection": "managed/user",
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
> >         "_ref": "managed/user/9cae97b7-3bf3-4107-96d5-39ad153629db",
> >         "_refResourceCollection": "managed/user",
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
> >           "_ref": "managed/role/testManagedRole",
> >           "_refResourceCollection": "managed/role",
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
> >         "_ref": "managed/user/9cae97b7-3bf3-4107-96d5-39ad153629db",
> >         "_refResourceCollection": "managed/user",
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
> >           "_ref": "managed/role/testManagedRole",
> >           "_refResourceCollection": "managed/role",
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
> > "http://localhost:8080/openidm/managed/user/aca0042c-9f4c-4ad5-8cf7-aca0adeb3470?_fields=preferences"
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
> > "http://localhost:8080/openidm/managed/user/917bc052-ef39-4add-ae05-0a278e2de9c0/roles?_queryFilter=true&_fields=*"
> > {
> >   "result": [
> >     {
> >       "_id": "a33e2de0-83ff-481c-b8a7-8ffbc02d135c",
> >       "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1235",
> >       "name": "testManagedRole",
> >       "description": "a managed role for test",
> >       "_refResourceCollection": "managed/role",
> >       "_refResourceId": "testManagedRole",
> >       "_refResourceRev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-181",
> >       "_ref": "managed/role/testManagedRole",
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
> > "http://localhost:8080/openidm/managed/user/917bc052-ef39-4add-ae05-0a278e2de9c0/manager?_fields=*"
> > {
> >   "_id": "5bc2c633-8ae1-4ea2-adf6-8aa7ce5f8e70",
> >   "_rev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1233",
> >   "userName": "psmith",
> >   "sn": "Smith",
> >   "givenName": "Patricia",
> >   "mail": "psmith@example.com",
> >   "telephoneNumber": "082082082",
> >   "accountStatus": "active",
> >   "_refResourceCollection": "managed/user",
> >   "_refResourceId": "9cae97b7-3bf3-4107-96d5-39ad153629db",
> >   "_refResourceRev": "200bc5d6-7cc1-4648-a854-3137f3d9c103-1223",
> >   "_ref": "managed/user/9cae97b7-3bf3-4107-96d5-39ad153629db",
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
> >    "value" : [{"_ref" : "managed/user/917bc052-ef39-4add-ae05-0a278e2de9c0"}]
> > } ]' \
> > "http://localhost:8080/openidm/managed/user/9cae97b7-3bf3-4107-96d5-39ad153629db"
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
> >     "value": {"_ref" : "managed/user/9cae97b7-3bf3-4107-96d5-39ad153629db"}
> >   }
> > ]' \
> > "http://localhost:8080/openidm/managed/user/aca0042c-9f4c-4ad5-8cf7-aca0adeb3470"
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
> > "http://localhost:8080/openidm/managed/user/aca0042c-9f4c-4ad5-8cf7-aca0adeb3470"
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
> >     "value": {"_ref" : "managed/user/aca0042c-9f4c-4ad5-8cf7-aca0adeb3470"}
> >   }
> > ]' \
> > "http://localhost:8080/openidm/managed/user/917bc052-ef39-4add-ae05-0a278e2de9c0"
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
> > "http://localhost:8080/openidm/managed/user/9cae97b7-3bf3-4107-96d5-39ad153629db"
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
> >   "http://localhost:8080/openidm/managed/user"
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
> >   "http://localhost:8080/openidm/managed/user/psmith"
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
> > |   |                                                                                                                                                                                                                          |
> > | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
> > |   | Delegated administration may not work as expected when using DS as your repository if `_id` is something *other* than a UUID. JDBC repositories may use other forms for `_id`, though using a UUID is still recommended. |
>
> |   |                                                                                                         |
> | - | ------------------------------------------------------------------------------------------------------- |
> |   | For more examples, including working with filters, refer to the [Postman collection](#da-postman-coll). |

|   |                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | All patches are done with a PATCH request. Delegated administrator operations do not currently support using POST actions for patch requests (POST `_action=patch` will not work). |

|   |                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------- |
|   | This process only applies to managed users. It will not work for internal users, as they cannot have roles. |

## Configure search UI for delegated administrators

|   |                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------- |
|   | The end-user UI is not bundled with PingIDM. Learn more in [Install the end-user UI](../setup-guide/idm-enduser-ui.html). |

The IDM end-user UI support for delegated administration includes a search feature to filter a list of results. To keep search performant when working with large lists, you can configure the following constraints:

* [Set a minimum filter length](#da-min-filter-length).

* [Disable the ability to filter and sort](#da-disable-sort-filter-collections).

|   |                                                      |
| - | ---------------------------------------------------- |
|   | These settings only affect delegated administrators. |

### Minimum filter search length

You can set `minimumUIFilterLength` in `conf/ui-configuration.json` to define when results start filtering:

```json
"platformSettings" : {
    "managedObjectsSettings" : {
        "user" : {
            "minimumUIFilterLength" : 3
        }
    }
}
```

This setting prevents the UI from filtering until the user has typed at least three characters. `minimumUIFilterLength` can be used with any managed object, for example:

```json
"platformSettings" : {
    "managedObjectsSettings" : {
        "user" : {
            "minimumUIFilterLength" : 3
        },
        "role" : {
            "minimumUIFilterLength" : 2
        }
    }
}
```

### Disable sort and filter for resource collections

A *resource collection* is a set of objects that have a relationship with one or more other objects. For example:

* All users with a particular role assignment.

* All users who are members of an organization.

You can disable the ability to sort and filter resource collections using `"disableRelationshipSortAndSearch" : true` in `conf/ui-configuration.json`. This can be beneficial when working with *very* large lists. For example:

```json
"platformSettings" : {
    "managedObjectsSettings" : {
        "user" : {
            "disableRelationshipSortAndSearch" : true,
            "minimumUIFilterLength" : 3
        }
    }
}
```

---

---
title: IDM and HTTP basic authentication
description: Explains how PingIDM handles HTTP basic authentication, reading credentials from the Authorization header and returning a token for subsequent access
component: pingidm
version: 8.1
page_id: pingidm:auth-guide:http-basic-auth
canonical_url: https://docs.pingidentity.com/pingidm/8.1/auth-guide/http-basic-auth.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "HTTP Basic"]
---

# IDM and HTTP basic authentication

HTTP basic authentication is a simple challenge and response mechanism whereby the client submits a user ID and password to the server. IDM understands the authorization header of the HTTP basic authentication contract. However, it deliberately does not use the full HTTP basic authentication contract and does not cause the browser built-in mechanism to prompt for username and password. It also understands utilities, such as `curl` and Postman, that can send the username and password in the Authorization header.

In general, the HTTP basic authentication mechanism does not work well with client side web applications, and applications that need to render their own login screens. Because the browser stores and sends the username and password with each request, HTTP basic authentication has significant security vulnerabilities. You can therefore send the username and password via the authorization header, and IDM returns a token for subsequent access.

Access to the IDM REST interface *requires* that the client authenticate. User self-registration requires anonymous access. For this purpose, IDM includes an `anonymous` user, with the password `anonymous`. For more information, refer to [Internal Users](authenticating-users.html#internal-users).

The examples in this documentation use the IDM authentication headers in all REST examples, for example:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
...
```

---

---
title: Password changes
description: Understand how PingIDM enforces reauthentication when changing passwords over REST using the `X-OpenIDM-Reauth-Password` header
component: pingidm
version: 8.1
page_id: pingidm:auth-guide:authentication-password-change
canonical_url: https://docs.pingidentity.com/pingidm/8.1/auth-guide/authentication-password-change.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Password Change"]
---

# Password changes

Changing passwords can expose a server to potential security risks. An insecure password reset process can allow attackers to reset the passwords of other users in order to bypass authentication and gain access to user accounts.

Reauthentication forces users or clients to confirm their identity even this identity was verified previously. When passwords are changed over REST, using a PUT or PATCH request, IDM requires the `X-OpenIDM-Reauth-Password` header. If this header is absent, the server returns a `403` error.

For example, the following password change request fails:

```
curl \
--header "Content-Type: application/json" \
--header "X-OpenIDM-Username: bjensen" \
--header "X-OpenIDM-Password: Passw0rd" \
--header "Accept-API-Version: resource=1.0" \
--cacert ca-cert.pem \
--header "If-Match: *" \
--request PUT \
--data '{
  "userName": "bjensen",
  "givenName": "Babs",
  "sn": "Jensen",
  "mail": "babs.jensen@example.com",
  "telephoneNumber": "555-123-1234",
  "password": "NewPassw0rd"
}' \
"https://localhost:8443/openidm/managed/user/0638da14-e02e-4904-9076-b8ce8f700eb4"
{
  "code": 403,
  "reason": "Forbidden",
  "message": "Access denied"
}
```

The same request, including the `X-OpenIDM-Reauth-Password` header, succeeds:

```
curl \
--header "Content-Type: application/json" \
--header "X-OpenIDM-Username: bjensen" \
--header "X-OpenIDM-Password: Passw0rd" \
--header "Accept-API-Version: resource=1.0" \
--cacert ca-cert.pem \
--header "X-OpenIDM-Reauth-Password: Passw0rd" \
--header "If-Match: *" \
--request PUT \
--data '{
  "userName": "bjensen",
  "givenName": "Babs",
  "sn": "Jensen",
  "mail": "babs.jensen@example.com",
  "telephoneNumber": "555-123-1234",
  "password": "NewPassw0rd"
}' \
"https://localhost:8443/openidm/managed/user/0638da14-e02e-4904-9076-b8ce8f700eb4"
{
  "_id": "0638da14-e02e-4904-9076-b8ce8f700eb4",
  "_rev": "00000000fa190282",
  "userName": "bjensen",
  "givenName": "Babs",
  "sn": "Jensen",
  "mail": "babs.jensen@example.com",
  "telephoneNumber": "555-123-1234",
  ...
}
```