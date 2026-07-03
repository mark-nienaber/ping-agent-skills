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
