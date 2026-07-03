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
