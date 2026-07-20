---
description: Install, configure, and test the MS Graph API connector for Azure AD, including authentication methods, custom extension attributes, and account sync
component: openicf
page_id: openicf:connector-reference:msgraph-conf
canonical_url: https://docs.pingidentity.com/openicf/connector-reference/msgraph-conf.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  msgraph-config: Install and configure the MS Graph API connector
  msgraphi-before-you-start: Microsoft Azure requirements
  install_the_ms_graph_api_connector: Install the MS Graph API connector
  msgraph-api-configure: Configure the MS Graph API connector
  ms_graph_api_authentication_configuration: MS Graph API authentication configuration
  msgraph-api-extension-attributes: Custom user extension attributes
  msgraph-api-connector-remote: MS Graph API remote connector
  config-connection-pooling-ms-graph: Configure connection pooling
  msgraph-api-test-config: Test the connector
  msgraph-api-sync: Synchronize accounts between IDM and Azure
  implemented-interfaces-org-forgerock-openicf-connectors-msgraphapi-MSGraphAPIConnector-1.5.20.35: OpenICF Interfaces Implemented by the MSGraphAPI Connector
  config-properties-org-forgerock-openicf-connectors-msgraphapi-MSGraphAPIConnector-1.5.20.35: MSGraphAPI Connector Configuration
  basic-configuration-properties-org-forgerock-openicf-connectors-msgraphapi-MSGraphAPIConnector-1.5.20.35: Basic Configuration Properties
---

## Install and configure the MS Graph API connector

## Microsoft Azure requirements

Before you can use the connector, you must register an application with Azure. You need a Microsoft Azure subscription to complete this procedure:

1. Log in to the [MS Azure portal](https://portal.azure.com/) as an administrative user.

2. Under Azure services , select App registrations.

3. On the Register an application page, enter a name for the application; for example, FR-Connector.

4. Select the supported account types, and enter a Redirect URI.

   The redirect URI is the IDM URI that Azure should redirect to after successful authentication; for example, `https://idm.example.com:8443/`.

5. On the new registration page for your application, make a note of the Application (client) ID and the Directory (tenant) ID. You will need these to configure the connector:

   > **Collapse: Show Me**
   >
   > ![MS Graph API essential info](../_images/ms-graph-api-app.png)

6. Generate a client secret:

   1. Select Certificates & secrets > New client secret .

   2. Enter a description, select an expiration date, and click Add.

   3. Copy the client secret Value:

      > **Collapse: Show Me**
      >
      > ![MS Graph API copy client secret](../_images/ms-graph-api-secret.png)

      |   |                                                                                             |
      | - | ------------------------------------------------------------------------------------------- |
      |   | You will not be able to retrieve the client secret in cleartext after you exit this screen. |

7. Set the API permissions:

   1. Select API permissions, click Microsoft Graph, and then click Application permissions.

      > **Collapse: Show Me**
      >
      > ![MS Graph API permissions](../_images/ms-graph-api-app-permissions.png)

   2. From the User item, select the following permissions:

      * `User.Export.All`

      * `User.ManageIdentities.All`

      * `User.Read.All`

      * `User.ReadWrite.All`

   3. From the UserAuthenticationMethod item, select the following permissions:

      * `UserAuthenticationMethod.Read.All`

      * `UserAuthenticationMethod.ReadWrite.All`

   4. From the Group item, select the following permissions:

      * `Group.Create`

      * `Group.Read.All`

      * `Group.ReadWrite.All`

   5. From the Directory item, select the following permissions:

      * `Directory.Read.All`

      * `Directory.ReadWrite.All`

   6. Click Add permissions .

8. Grant admin consent for the API permissions:

   On the Configured permissions page, Grant admin consent for org-name, then click Yes.

   > **Collapse: Show Me**
   >
   > ![MS Graph API configured permissions](../_images/ms-graph-api-consent.png)

## Install the MS Graph API connector

|   |                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To check for an Advanced Identity Cloud application for this connector, refer to:- [Application management](https://docs.pingidentity.com/pingoneaic/latest/app-management/applications.html)

- [App catalog](https://docs.pingidentity.com/pingoneaic/latest/app-management/app-catalog.html) |

You can download most connectors from [Backstage](https://backstage.forgerock.com/downloads/browse/idm/featured/connectors), but some are included in the default deployment for Advanced Identity Cloud, IDM, or RCS. When using an included connector, you can skip installing it and move directly to configuration.

**Connector included in default deployment**

| Connector                                | IDM                      | RCS                     |
| ---------------------------------------- | ------------------------ | ----------------------- |
| [Microsoft Graph API](ms-graph-api.html) | [icon: check, set=fa]Yes | [icon: times, set=fa]No |

Download the connector .jar file from [Backstage](https://backstage.forgerock.com/downloads/browse/idm/featured/connectors).

* If you're running the connector locally, place it in the `/path/to/openidm/connectors` directory, for example:

  ```
  mv ~/Downloads/msgraphapi-connector-1.5.20.35.jar /path/to/openidm/connectors/
  ```

* If you're using a remote connector server (RCS), place it in the `/path/to/openicf/connectors` directory on the RCS.

## Configure the MS Graph API connector

Create a connector configuration using the IDM admin UI:

1. From the navigation bar, click Configure > Connectors.

2. On the Connectors page, click New Connector.

3. On the New Connector page, type a Connector Name.

4. From the Connector Type list, select MS Graph API Connector - 1.5.20.35.

5. Complete the Base Connector Details and any applicable Additional Options.

   |   |                                                                                                                              |
   | - | ---------------------------------------------------------------------------------------------------------------------------- |
   |   | For a list of all configuration properties, refer to [MS Graph API Connector Configuration](#msgraphapi-config-prop-ezLink). |

6. Click Save.

When your connector is configured correctly, the connector displays as Active in the admin UI.

Refer to [this procedure](configure-connector.html#connector-wiz-REST) to create a connector configuration over REST.

Alternatively, copy the sample connector configuration file from `/path/to/openidm/samples/example-configurations/provisioners/provisioner.openicf-azuread.json` to your project's `conf/` directory.

### MS Graph API authentication configuration

You can configure authentication using one of the following methods:

* Direct authentication configuration

  Set the Azure `tenant`, `clientId` and `clientSecret` in the connector provisioner `configurationProperties`. For example:

  ```json
  "configurationProperties" : {
      "tenant" : "your tenant ID",
      "clientId" : "your client ID",
      "clientSecret" : "your client secret"
  }
  ```

* Environment-based authentication configuration \[[1](#_footnotedef_1 "View footnote.")]

  If you don't specify the `tenant`, `clientId`, and `clientSecret` properties in the connector configuration, the connector uses the [Azure Identity SDK's `DefaultAzureCredential` provider](https://learn.microsoft.com/en-us/dotnet/api/azure.identity.defaultazurecredential?view=azure-dotnet) to search for credentials in the connector's system environment.

  The provider searches for the following environment variables:

  * `AZURE_TENANT_ID`

  * `AZURE_CLIENT_ID`

  * `AZURE_CLIENT_SECRET`

  This feature supports other authentication mechanisms available through the Azure Identity SDK, such as [`EnvironmentCredential`](https://learn.microsoft.com/en-us/dotnet/api/azure.identity.environmentcredential), `WorkloadIdentityCredential`, and `ManagedIdentityCredential`. Create the configuration for these mechanisms in the system's environment, not in the connector configuration.

### Custom user extension attributes

If you set `extensionPropertySourceAppIds`, the connector discovers and exposes [custom extension properties](https://learn.microsoft.com/en-us/graph/api/resources/extensionproperty?view=graph-rest-1.0) registered in your Azure tenant for the listed application IDs. Only the `user` (\_\_ACCOUNT\_\_) object type supports custom extension attributes.

Provide application IDs as UUIDs, with or without dashes:

```json
"configurationProperties": {
  "extensionPropertySourceAppIds": [
    "00000000000000000000000000000001",
    "00000000-0000-0000-0000-000000000002"
  ]
}
```

The connector prefixes each discovered attribute name with `ext_` to prevent naming conflicts with built-in user attributes. For example, an extension property named `Department_level` is exposed as `ext_Department_level`.

Because custom extension attributes have the `NOT_RETURNED_BY_DEFAULT` flag, you must request them explicitly by name in the `_fields` parameter.

The connector supports the extension attribute types: `String`, `Integer`, `Boolean`, and `DateTime`. It doesn't support byte array types.

|   |                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Discovering extension attributes requires the `Directory.Read.All` or `Directory.ReadWrite.All` application permission. Both are included in the [Microsoft Azure requirements](#procedure-prepare-azuread). |

### MS Graph API remote connector

If you want to run this connector outside of PingOne Advanced Identity Cloud or IDM, you can configure the MS Graph API connector as a remote connector. Java Connectors installed remotely on a Java Connector Server function identically to those bundled locally within PingOne Advanced Identity Cloud or installed locally on IDM.

Refer to [Remote connectors](remote-connector.html) for configuring the MS Graph API remote connector.

### Configure connection pooling

The MS Graph API connector uses [ICF pooling](pooling.html#icf-pooling) to manage connections. Learn more about the different pooling mechanisms in [Connectors by pooling mechanism](pooling.html#pooling-table).

## Test the connector

One simple method for testing the connector configuration is using the `test` action on the `openidm/system/azuread` endpoint:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
"http://localhost:8080/openidm/system/azuread?_action=test"
{
  "name": "azuread",
  "enabled": true,
  "config": "config/provisioner.openicf/azuread",
  "connectorRef": {
    "bundleVersion": "[1.5.0.0,1.6.0.0)",
    "bundleName": "org.forgerock.openicf.connectors.msgraphapi-connector",
    "connectorName": "org.forgerock.openicf.connectors.msgraphapi.MSGraphAPIConnector"
  },
  "displayName": "MSGraphAPI Connector",
  "objectTypes": [
    "servicePrincipal",
    "__GROUP__",
    "roleEligibilitySchedule",
    "roleEligibilityScheduleInstance",
    "__ALL__",
    "roleEligibilityScheduleRequest",
    "directoryRole",
    "team",
    "roleAssignmentSchedule",
    "roleDefinition",
    "servicePlan",
    "directoryRoleTemplate",
    "application",
    "roleAssignmentScheduleRequest",
    "roleAssignmentScheduleInstance",
    "subscribedSku",
    "__ACCOUNT__",
    "roleAssignment"
  ],
  "ok": true (1)
}
```

|       |                                                                                |
| ----- | ------------------------------------------------------------------------------ |
| **1** | A status of `"ok": true` indicates that the connector is configured correctly. |

## Synchronize accounts between IDM and Azure

To use the MS Graph API connector to synchronize accounts between IDM and Azure, set up a [mapping](https://docs.pingidentity.com/pingidm/8/synchronization-guide/mappings.html) between the two data stores.

You can use the sample configuration file at `/path/to/openidm/samples/sync-with-azuread/conf/sync.json` as a starting point.

## OpenICF Interfaces Implemented by the MSGraphAPI Connector

The MSGraphAPI Connector implements the following OpenICF interfaces. For additional details, see [ICF interfaces](interfaces.html):

* Authenticate

  Provides simple authentication with two parameters, presumed to be a user name and password.

* Create

  Creates an object and its `uid`.

* Delete

  Deletes an object, referenced by its `uid`.

* Schema

  Describes the object types, operations, and options that the connector supports.

* Script on Connector

  Enables an application to run a script in the context of the connector.

  Any script that runs on the connector has the following characteristics:

  * The script runs in the same execution environment as the connector and has access to all the classes to which the connector has access.

  * The script has access to a `connector` variable that is equivalent to an initialized instance of the connector. At a minimum, the script can access the connector configuration.

  * The script has access to any script arguments passed in by the application.

* Search

  Searches the target resource for all objects that match the specified object class and filter.

* Sync

  Polls the target resource for synchronization events, that is, native changes to objects on the target resource.

* Test

  Tests the connector configuration.

  Testing a configuration checks all elements of the environment that are referred to by the configuration are available. For example, the connector might make a physical connection to a host that is specified in the configuration to verify that it exists and that the credentials that are specified in the configuration are valid.

  This operation might need to connect to a resource, and, as such, might take some time. Do not invoke this operation too often, such as before every provisioning operation. The test operation is not intended to check that the connector is alive (that is, that its physical connection to the resource has not timed out).

  You can invoke the test operation before a connector configuration has been validated.

* Update

  Updates (modifies or replaces) objects on a target resource.

[]()

## MSGraphAPI Connector Configuration

The MSGraphAPI Connector has the following configurable properties:

### Basic Configuration Properties

| Property                                                                                                                                                                                | Type            | Default | Encrypted(1)             | Required(2)               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | ------- | ------------------------ | ------------------------- |
| `tenant`                                                                                                                                                                                | `String`        | `null`  |                          | [icon: check, set=fas]Yes |
| The Azure AD tenant name or id.                                                                                                                                                         |                 |         |                          |                           |
| `clientId`                                                                                                                                                                              | `String`        | `null`  |                          | [icon: check, set=fas]Yes |
| The clientID used by the connector during the OAuth flow.                                                                                                                               |                 |         |                          |                           |
| `clientSecret`                                                                                                                                                                          | `GuardedString` | `null`  | [icon: lock, set=fas]Yes | [icon: times, set=fas]No  |
| The client secret used by the connector during the OAuth flow.                                                                                                                          |                 |         |                          |                           |
| `httpProxyHost`                                                                                                                                                                         | `String`        | `null`  |                          | [icon: times, set=fas]No  |
| The Http proxy host.                                                                                                                                                                    |                 |         |                          |                           |
| `httpProxyPort`                                                                                                                                                                         | `Integer`       | `null`  |                          | [icon: times, set=fas]No  |
| The Http proxy port.                                                                                                                                                                    |                 |         |                          |                           |
| `httpProxyUsername`                                                                                                                                                                     | `String`        | `null`  |                          | [icon: times, set=fas]No  |
| The Http proxy user name.                                                                                                                                                               |                 |         |                          |                           |
| `httpProxyPassword`                                                                                                                                                                     | `GuardedString` | `null`  | [icon: lock, set=fas]Yes | [icon: times, set=fas]No  |
| The Http proxy user password.                                                                                                                                                           |                 |         |                          |                           |
| `performHardDelete`                                                                                                                                                                     | `boolean`       | `false` |                          | [icon: times, set=fas]No  |
| If set to true, the Azure object will be deleted permanently on delete operation.                                                                                                       |                 |         |                          |                           |
| `readRateLimit`                                                                                                                                                                         | `String`        | `null`  |                          | [icon: times, set=fas]No  |
| Defines throttling for read operations either per seconds (`30/sec`) or per minute (`100/min`).                                                                                         |                 |         |                          |                           |
| `writeRateLimit`                                                                                                                                                                        | `String`        | `null`  |                          | [icon: times, set=fas]No  |
| Defines throttling for write operations (create/update/delete) either per second (`30/sec`) or per minute (`100/min`).                                                                  |                 |         |                          |                           |
| `licenseCacheExpiryTime`                                                                                                                                                                | `Long`          | `null`  |                          | [icon: times, set=fas]No  |
| Defines the expiry time for cached license information (in minutes).                                                                                                                    |                 |         |                          |                           |
| `extensionPropertySourceAppIds`                                                                                                                                                         | `String[]`      | `[]`    |                          | [icon: times, set=fas]No  |
| If defined, the schema will discover and the connector will expose the custom user extension attributes for the listed applications. Accepted values are UUIDs or UUIDs without dashes. |                 |         |                          |                           |

(1) Whether the property value is considered confidential, and is therefore encrypted in IDM.

(2) A list of operations in this column indicates that the property is required for those operations.

***

[1](#_footnoteref_1). MS Graph API connector version 1.5.20.30 and later supports environment-based authentication configuration.

---

---
title: <code>servicePrincipal</code> (MS Graph API)
description: "MS Graph API connector reference for the servicePrincipal resource type: query, read, create, update, delete, and add-password operations in PingIDM"
component: openicf
page_id: openicf:connector-reference:msgraph-servicePrincipal
canonical_url: https://docs.pingidentity.com/openicf/connector-reference/msgraph-servicePrincipal.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  msgraph-query-all-servicePrincipal: Query all servicePrincipal objects
  msgraph-read-servicePrincipal: Read a servicePrincipal
  msgraph-create-servicePrincipal: Create a servicePrincipal
  msgraph-add-pass-secret-servicePrincipal: Add a password (client secret) to a servicePrincipal
  msgraph-update-servicePrincipal: Update a servicePrincipal
  msgraph-delete-servicePrincipal: Delete a servicePrincipal
---

# `servicePrincipal` (MS Graph API)

The `servicePrincipal` resource type represents an instance of an application in a directory. For more information, refer to the [Microsoft Graph documentation](https://learn.microsoft.com/en-us/graph/api/resources/serviceprincipal?view=graph-rest-1.0).

## Query all `servicePrincipal` objects

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"http://localhost:8080/openidm/system/azuread/servicePrincipal?_queryFilter=true"
```

## Read a `servicePrincipal`

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"http://localhost:8080/openidm/system/azuread/servicePrincipal/1c696b95-7f68-4018-b627-6c9601faa80b"
```

Response

```json
{
  "_id": "1c696b95-7f68-4018-b627-6c9601faa80b",
  "addIns": [],
  "replyUrls": [],
  "keyCredentials": [],
  "oauth2PermissionScopes": [],
  "displayName": "Test-Application",
  "appRoleAssignments": [],
  "alternativeNames": [],
  "resourceSpecificApplicationPermissions": [],
  "appDisplayName": "Test-Application",
  "accountEnabled": true,
  "appOwnerOrganizationId": "9e91bf24-7a08-433e-b111-5542416b4f20",
  "passwordCredentials": [],
  "servicePrincipalNames": [
    "a293dbaf-ba5d-4692-8898-521a1da51bac"
  ],
  "appId": "a293dbaf-ba5d-4692-8898-521a1da51bac",
  "signInAudience": "AzureADandPersonalMicrosoftAccount",
  "notificationEmailAddresses": [],
  "servicePrincipalType": "Application",
  "tags": [],
  "appRoleAssignedTo": [],
  "info": {},
  "appRoles": [],
  "appRoleAssignmentRequired": false
}
```

## Create a `servicePrincipal`

|   |                                           |
| - | ----------------------------------------- |
|   | A `servicePrincipal` requires an `appId`. |

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request POST \
--data '{
  "appId": "0b9179f4-f617-4ab8-9c33-18a870c76722"
}' \
"http://localhost:8080/openidm/system/azuread/servicePrincipal"
```

Response

```json
{
  "_id": "7d164d58-6210-4c25-84db-d3dfce1171b4",
  "addIns": [],
  "replyUrls": [],
  "keyCredentials": [],
  "oauth2PermissionScopes": [],
  "displayName": "Test-Application",
  "appRoleAssignments": [],
  "alternativeNames": [],
  "resourceSpecificApplicationPermissions": [],
  "appDisplayName": "Test-Application",
  "accountEnabled": true,
  "appOwnerOrganizationId": "9e91bf24-7a08-433e-b111-5542416b4f20",
  "passwordCredentials": [],
  "servicePrincipalNames": [
    "0b9179f4-f617-4ab8-9c33-18a870c76722"
  ],
  "appId": "0b9179f4-f617-4ab8-9c33-18a870c76722",
  "signInAudience": "AzureADandPersonalMicrosoftAccount",
  "notificationEmailAddresses": [],
  "servicePrincipalType": "Application",
  "tags": [],
  "appRoleAssignedTo": [],
  "info": {},
  "appRoles": [],
  "appRoleAssignmentRequired": false
}
```

## Add a password (client secret) to a `servicePrincipal`

Adding `passwordCredential` when creating a `servicePrincipal` is not supported. You must use the `addPassword` method to add passwords or secrets to a `servicePrincipal`.

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request POST \
"http://localhost:8080/openidm/system/azuread/?_action=script&scriptId=addPassword&displayName=TestSecretGenesis&servicePrincipalId=32e18e7a-cb23-4453-b5f4-286bc1a629b8&builtinAction=addPassword"
```

Response

```json
{
  "actions": [
    {
      "result": {
        "secretText": "{GENERATED-CLIENT-SECRET}",
        "startDateTime": {
          "dateTime": {
            "date": {
              "month": 5,
              "year": 2023,
              "day": 5
            },
            "time": {
              "hour": 20,
              "nano": 91094000,
              "minute": 41,
              "second": 8
            }
          },
          "offset": {
            "totalSeconds": 0
          }
        },
        "displayName": "TestSecretGenesis",
        "hint": "rJn",
        "keyId": "862c0883-45ac-4e13-8adc-ce9bf3036570",
        "endDateTime": {
          "dateTime": {
            "date": {
              "month": 5,
              "year": 2025,
              "day": 5
            },
            "time": {
              "hour": 20,
              "nano": 91094000,
              "minute": 41,
              "second": 8
            }
          },
          "offset": {
            "totalSeconds": 0
          }
        }
      }
    }
  ]
}
```

## Update a `servicePrincipal`

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request PATCH \
--data '[
  {
    "operation": "replace",
    "field": "/appRoleAssignmentRequired",
    "value": true
  }
]' \
"http://localhost:8080/openidm/system/azuread/servicePrincipal/7d164d58-6210-4c25-84db-d3dfce1171b4"
```

Response

```json
{
  "_id": "7d164d58-6210-4c25-84db-d3dfce1171b4",
  "addIns": [],
  "replyUrls": [],
  "keyCredentials": [],
  "oauth2PermissionScopes": [],
  "displayName": "Test-Application",
  "appRoleAssignments": [],
  "alternativeNames": [],
  "resourceSpecificApplicationPermissions": [],
  "appDisplayName": "Test-Application",
  "accountEnabled": true,
  "appOwnerOrganizationId": "9e91bf24-7a08-433e-b111-5542416b4f20",
  "passwordCredentials": [],
  "servicePrincipalNames": [
    "0b9179f4-f617-4ab8-9c33-18a870c76722"
  ],
  "appId": "0b9179f4-f617-4ab8-9c33-18a870c76722",
  "signInAudience": "AzureADandPersonalMicrosoftAccount",
  "notificationEmailAddresses": [],
  "servicePrincipalType": "Application",
  "tags": [],
  "appRoleAssignedTo": [],
  "info": {},
  "appRoles": [],
  "appRoleAssignmentRequired": true
}
```

## Delete a `servicePrincipal`

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--header "If-Match: *" \
--request DELETE \
"http://localhost:8080/openidm/system/azuread/servicePrincipal/1df34a52-3491-4b3a-8ec7-51d77ab50860"
```

Response

```json
{
  "_id": "1df34a52-3491-4b3a-8ec7-51d77ab50860",
  "addIns": [],
  "replyUrls": [],
  "keyCredentials": [],
  "oauth2PermissionScopes": [],
  "displayName": "Test-Application",
  "appRoleAssignments": [],
  "alternativeNames": [],
  "resourceSpecificApplicationPermissions": [],
  "appDisplayName": "Test-Application",
  "accountEnabled": true,
  "appOwnerOrganizationId": "9e91bf24-7a08-433e-b111-5542416b4f20",
  "passwordCredentials": [],
  "servicePrincipalNames": [
    "a2179b48-33f0-4933-8c59-39639469bb13"
  ],
  "appId": "a2179b48-33f0-4933-8c59-39639469bb13",
  "signInAudience": "AzureADandPersonalMicrosoftAccount",
  "notificationEmailAddresses": [],
  "servicePrincipalType": "Application",
  "tags": [],
  "appRoleAssignedTo": [],
  "info": {},
  "appRoles": [],
  "appRoleAssignmentRequired": false
}
```

---

---
title: Adobe Admin Console connector
description: Configure the Adobe Admin Console connector to manage users, groups, and group memberships between Adobe Admin Console and PingIDM
component: openicf
page_id: openicf:connector-reference:adobe-admin-console
canonical_url: https://docs.pingidentity.com/openicf/connector-reference/adobe-admin-console.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  before_you_start: Before you start
  install_the_adobe_admin_console_connector: Install the Adobe Admin Console connector
  configure_the_adobe_admin_console_connector: Configure the Adobe Admin Console connector
  config-connection-pooling-adobe-admin: Configure connection pooling
  mapping: Mapping
  test_the_adobe_admin_console_connector: Test the Adobe Admin Console connector
  ADOBE_USERS: User
  create_user: Create user
  get_users: Get Users
  get_user: Get user
  get_users_type: Get users type
  update_user: Update user
  delete_user: Delete user
  ADOBE_GROUPS: GROUPS
  create_group: Create group
  get_groups: Get groups
  get_group: Get group
  update_a_group: Update a group
  delete_a_group: Delete a group
  implemented-interfaces-org-forgerock-openicf-connectors-adobe-AdobeConnector-1.5.20.35: OpenICF Interfaces Implemented by the Adobe Admin Console Connector
  config-properties-org-forgerock-openicf-connectors-adobe-AdobeConnector-1.5.20.35: Adobe Admin Console Connector Configuration
  basic-configuration-properties-org-forgerock-openicf-connectors-adobe-AdobeConnector-1.5.20.35: Basic Configuration Properties
---

# Adobe Admin Console connector

|   |                                                              |
| - | ------------------------------------------------------------ |
|   | This is a [SaaS common connector](preface.html#saas-common). |

The Adobe admin console connector allows you to manage users and groups, as well as manage user group memberships between the Adobe admin console and IDM. You need an administrator account.

## Before you start

1. Create an [Adobe Admin Console developer account](https://developer.adobe.com/console/home/).

2. Create a new project. Add User Management API, choose the type of authentication OAuth server-to-server

3. From the credentials tab, get the client\_id, client\_secret, orgId, and scope.

## Install the Adobe Admin Console connector

|   |                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To check for an Advanced Identity Cloud application for this connector, refer to:- [Application management](https://docs.pingidentity.com/pingoneaic/latest/app-management/applications.html)

- [App catalog](https://docs.pingidentity.com/pingoneaic/latest/app-management/app-catalog.html) |

You can download most connectors from [Backstage](https://backstage.forgerock.com/downloads/browse/idm/featured/connectors), but some are included in the default deployment for Advanced Identity Cloud, IDM, or RCS. When using an included connector, you can skip installing it and move directly to configuration.

**Connector included in default deployment**

| Connector                                       | IDM                     | RCS                     |
| ----------------------------------------------- | ----------------------- | ----------------------- |
| [Adobe Admin Console](adobe-admin-console.html) | [icon: times, set=fa]No | [icon: times, set=fa]No |

Download the connector .jar file from [Backstage](https://backstage.forgerock.com/downloads/browse/idm/featured/connectors).

* If you're running the connector locally, place it in the `/path/to/openidm/connectors` directory, for example:

  ```
  mv ~/Downloads/adobe-connector-1.5.20.35.jar /path/to/openidm/connectors/
  ```

* If you're using a remote connector server (RCS), place it in the `/path/to/openicf/connectors` directory on the RCS.

## Configure the Adobe Admin Console connector

Create a connector configuration using the IDM admin UI:

1. From the navigation bar, click Configure > Connectors.

2. On the Connectors page, click New Connector.

3. On the New Connector page, type a Connector Name.

4. From the Connector Type list, select Adobe Admin Console Connector - 1.5.20.35.

5. Complete the Base Connector Details and any applicable Additional Options.

   |   |                                                                                                                                |
   | - | ------------------------------------------------------------------------------------------------------------------------------ |
   |   | For a list of all configuration properties, refer to [Adobe Admin Console Connector Configuration](#adobe-config-prop-ezLink). |

6. Click Save.

When your connector is configured correctly, the connector displays as Active in the admin UI.

Refer to [this procedure](configure-connector.html#connector-wiz-REST) to create a connector configuration over REST.

> **Collapse: Base Connector Details**
>
> * `Adobe User Management API Endpoint` : https\://usermanagement.adobe.io/v2
>
> * `Use Basic Auth For OAuth Token Neg` : `true` | `false`
>
> * `Max connections`: Max size of the http connection pool used. Defaults to `10`.
>
> * `Connection Timeout (seconds)`: Defines a timeout for the underlying http connection in seconds. Defaults to `30`.

> **Collapse: Authentication**
>
> * `Token Endpoint`: https\://ims-na1.adobelogin.com/ims/token/v3
>
> * `Client ID`: Your Client ID.
>
> * `Client Secret`: Your Client Secret.
>
> * `Grant type`: client\_credentials
>
> * `Scope`: openid, AdobeID, user\_management\_sdk
>
> * `orgId`: Your Organization Id
>
> |   |                                                              |
> | - | ------------------------------------------------------------ |
> |   | In the Scope field, the scopes must be separated by a comma. |

> **Collapse: Object Types**
>
> If necessary, add or edit your object types to have these three objects with their properties:
>
> > **Collapse:&#x20;**
> >
> > | PROPERTY NAME     | TYPE    | NATIVE TYPE | REQUIRED |
> > | ----------------- | ------- | ----------- | -------- |
> > | `_id`             | String  | String      | NO       |
> > | `email`           | String  | String      | YES      |
> > | `firstname`       | String  | String      | NO       |
> > | `lastname`        | String  | String      | NO       |
> > | `status`          | String  | String      | NO       |
> > | `username`        | String  | String      | NO       |
> > | `type`            | String  | String      | YES      |
> > | `orgSpecific`     | boolean | boolean     | NO       |
> > | `businessAccount` | boolean | boolean     | NO       |
> > | `country`         | String  | String      | NO       |
> > | `__GROUPS__`      | Array   | String      | NO       |
>
> > **Collapse:&#x20;**
> >
> > | PROPERTY NAME      | TYPE    | NATIVE TYPE | REQUIRED |
> > | ------------------ | ------- | ----------- | -------- |
> > | `_id`              | String  | String      | NO       |
> > | `groupName`        | String  | String      | YES      |
> > | `type`             | String  | String      | NO       |
> > | `adminGroupName`   | String  | String      | NO       |
> > | `userGroupName`    | String  | String      | NO       |
> > | `memberCount`      | Integer | Integer     | NO       |
> > | `productName`      | String  | String      | NO       |
> > | `profileGroupName` | String  | String      | NO       |

If configuring the connector over REST or through the filesystem, specify the connection details to the Adobe resource provider in the `configurationProperties` for the connector. If you are using OAuth for your connection, the minimum required properties are `scope`, `orgId`, `grantType`, `serviceUri`, `tokenEndpoint`, `clientId`, and `clientSecret`.

On startup, IDM encrypts the value of the `clientSecret`.

> **Collapse: Sample Configuration**
>
> ```json
> {
>     "configurationProperties" : {
>         "tokenExpiration" : null,
>         "accessToken" : null,
>         "serviceUri" : "https://usermanagement.adobe.io/v2",
>         "login" : null,
>         "password" : null,
>         "authenticationMethod" : "OAUTH",
>         "tokenEndpoint" : "https://ims-na1.adobelogin.com/ims/token/v3",
>         "clientId" : "xxxxxxxxxxxxxxxxxx",
>         "clientSecret" : "xxxxxxxxxxxxxxxxxx",
>         "refreshToken" : null,
>         "authToken" : null,
>         "acceptSelfSignedCertificates" : false,
>         "disableHostNameVerifier" : false,
>         "disableHttpCompression" : false,
>         "clientCertAlias" : null,
>         "clientCertPassword" : null,
>         "maximumConnections" : "10",
>         "httpProxyHost" : null,
>         "httpProxyPort" : null,
>         "httpProxyUsername" : null,
>         "httpProxyPassword" : null,
>         "connectionTimeout" : "30",
>         "grantType" : "client_credentials",
>         "scope" : "openid, AdobeID, user_management_sdk",
>         "authorizationTokenPrefix" : "Bearer",
>         "useBasicAuthForOauthTokenNeg" : true,
>         "groupReadRateLimit" : "0.09/sec",
>         "userReadRateLimit" : "0.41/sec",
>         "writeRateLimit" : "0.16/sec"
>       }
> }
> ```
>
> |   |                                                                                                                                                                                                                       |
> | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | If throttling problems continue, this guide may be helpful: [Improve reconciliation query performance](https://docs.pingidentity.com/pingidm/8/synchronization-guide/chap-performance.html#recon-query-optimization). |

### Configure connection pooling

The Adobe Admin Console connector supports [HTTP pooling](pooling.html#http-pooling), which can substantially improve the performance of the connector. Learn more about the basic connection pooling configuration and different pooling mechanisms described in [Connection pooling configuration](pooling.html).

## Mapping

> **Collapse: From Adobe users to IDM Users**
>
> Attributes Grid: Where the columns represent the attribute name mapped from source to target and the necessary data transformation to synchronize successfully.
>
> | SOURCE            | TARGET            | TRANSFORMATION SCRIPT |
> | ----------------- | ----------------- | --------------------- |
> | `id`              | `userId`          | N/A                   |
> | `email`           | `_id`             | N/A                   |
> | `firstname`       | `givenName`       | N/A                   |
> | `lastname`        | `sn`              | N/A                   |
> | `type`            | `type`            | N/A                   |
> | `status`          | `status`          | N/A                   |
> | `username`        | `username`        | N/A                   |
> | `country`         | `country`         | N/A                   |
> | `orgSpecific`     | `orgSpecific`     | N/A                   |
> | `businessAccount` | `businessAccount` | N/A                   |
> | `__GROUPS__`      | `__GROUPS__`      | N/A                   |

> **Collapse: From IDM Users to Adobe Users**
>
> Attributes Grid: Where the columns represent the attribute name mapped from source to target and the necessary data transformation to synchronize successfully.
>
> | SOURCE       | TARGET       | TRANSFORMATION SCRIPT |
> | ------------ | ------------ | --------------------- |
> | `mail`       | `email`      | N/A                   |
> | `givenName`  | `firstname`  | N/A                   |
> | `sn`         | `lastname`   | N/A                   |
> | `type`       | `type`       | N/A                   |
> | `username`   | `username`   | N/A                   |
> | `country`    | `country`    | N/A                   |
> | `__GROUPS__` | `__GROUPS__` | N/A                   |

> **Collapse: From Adobe groups to IDM Groups**
>
> Attributes Grid: Where the columns represent the attribute name mapped from source to target and the necessary data transformation to synchronize successfully.
>
> | SOURCE             | TARGET             | TRANSFORMATION SCRIPT |
> | ------------------ | ------------------ | --------------------- |
> | `groupId`          | `_id`              | N/A                   |
> | `groupname`        | `groupName`        | N/A                   |
> | `type`             | `type`             | N/A                   |
> | `memberCount`      | `memberCount`      | N/A                   |
> | `adminGroupName`   | `adminGroupName`   | N/A                   |
> | `productName`      | `productName`      | N/A                   |
> | `licenseQuota`     | `licenseQuota`     | N/A                   |
> | `profileGroupName` | `profileGroupName` | N/A                   |

> **Collapse: From IDM Groups to Adobe groups**
>
> Attributes Grid: Where the columns represent the attribute name mapped from source to target and the necessary data transformation to synchronize successfully.
>
> | SOURCE        | TARGET        | TRANSFORMATION SCRIPT |
> | ------------- | ------------- | --------------------- |
> | `groupName`   | `groupName`   | N/A                   |
> | `description` | `description` | N/A                   |

## Test the Adobe Admin Console connector

Test that the connector was configured correctly:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Accept-API-Version: resource=1.0' \
--request POST \
'http://localhost:8080/system/adobe?_action=test'
{
    "name": "adobe",
    "enabled": true,
    "config": "config/provisioner.openicf/adobe",
    "connectorRef": {
        "bundleVersion": "1.5.20.35",
        "bundleName": "org.forgerock.openicf.connectors.adobe-connector",
        "connectorName": "org.forgerock.openicf.connectors.adobe.AdobeConnector"
    },
    "displayName": "Adobe Admin Console Connector",
    "objectTypes": [
        "__GROUP__",
        "__ACCOUNT__",
        "__ALL__",
    ],
    "ok": true
}
```

### User

#### Create user

To create a user, it is necessary to provide *at least* the `email` and `type` fields. The possible values for the `type` field are adobeID, federatedID, and enterpriseID (case insensitive). To add groups or product profiles to a user, you must use the `__GROUPS__` field. To do this, you need to provide the corresponding IDs. The country field of a set cannot be updated. If not sent, it defaults to the country of the domain name. When creating a user, the username field is initially set to be the same as the email address; however, this username field can be modified later through user profile updates:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request POST \
--data '{
    "email" : "john.doe@domain1.com",
    "type" : "adobeID",
    "firstName" : "John",
    "lastName" : "Doe",
    "lastName" : "US",
    "__GROUPS__" : [
            "groupId",
            "groupId",
    ]
}' \
'http://localhost:8080/system/adobe/__ACCOUNT__?_action=create'
{
    "_id" : "john.doe@domain1.com",
    "id" : "userID",
    "email" : "john.doe@domain1.com",
    "username" : "john.doe@domain1.com",
    "orgSpecific": true,
    "businessAccount": true,
    "firstName" : "John",
    "lastname" : "Doe",
    "type" : "adobeID",
    "__NAME__" : "john.doe@domain1.com",
    "status" : "active",
    "country" : "US",
    "__GROUPS__" : [
            "groupId"
            "groupId"
    ]
}
```

#### Get Users

Retrieve a list of users from Adobe Admin Console. To paginate the results, the parameter pageSize must have a value greater than 1. The size of each page is 2,000 except, for the first page, which can contain fewer results due to technical users not being retrieved. By default, all users are retrieved.

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request GET \
'http://localhost:8080/openidm/system/adobe/__ACCOUNT__?_queryFilter=true'
{
    "result": [
        {
            "_id": "email@domain1.com",
            "__GROUPS__": [
                "groupId"
            ],
            "id": "userID",
            "country": "US",
            "email": "email@domain1.com",
            "orgSpecific": true,
            "username": "email@domain1.com",
            "businessAccount": true,
            "firstname": "John",
            "__NAME__": "john.doe@domain1.com",
            "type": "adobeID",
            "status": "active",
            "lastname": "Doe"
        },
       /…​
    ],
    "resultCount": 999,
    "pagedResultsCookie": null,
    "totalPagedResultsPolicy": "NONE",
    "totalPagedResults": -1,
    "remainingPagedResults": -1
}
```

#### Get user

Retrieve a user from Adobe Admin Console. The user email must be provided in the URI path.

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request GET \
'http://localhost:8080/openidm/system/adobe/__ACCOUNT__/USER_EMAIL'
{
    "_id" : "email@domain1.com",
    "email" : "email@domain1.com",
    "firstname" : "John",
    "lastname" : "Doe",
    "username" : "email@domain1.com",
    "type" : "adobeID",
    "status" : "active",
    "orgSpecific" : true,
    "businessAccount" : true,
    "__GROUPS__" : [
            "groupId1",
            "groupId2",
    ]
}
```

#### Get users type

Retrieves Adobe users only by displaying `type` and `_id` field. By default, retrieves all users:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request GET \
'http://localhost:8080/openidm/system/adobe/__ACCOUNT__?_queryFilter=true&_fields=type'
{
    "result": [
        {
            "_id" : "email1@domain.com",
            "type": "adobeID"
        {
            "_id" : "email2@domain.net",
            "type": "federatedID"
        },
        {
            "_id" : "email3@domain.org",
            "type": "enterpriseID"
        }
    ],
    "resultCount": 999,
    "pagedResultsCookie": null,
    "totalPagedResultsPolicy": "NONE",
    "totalPagedResults": -1,
    "remainingPagedResults": -1
}
```

#### Update user

Only enterprise or federated users can be updated. The fields that can be updated are `firstname`, `lastname`, `username`, and `__GROUPS__`. The user email must be provided in the URI path:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request PUT \
--data '{
    "firstname" : "Jonny",
    "lastname" : "Doo",
    "username" : "jonnydoo",
    "__GROUPS__" : [
            "groupId1",
            "groupId2",
    ]
}' \
'http://localhost:8080/system/adobe/__ACCOUNT__/USER_EMAIL'
{
    "_id": "john.doe@domain1.com",
    "id": "userID",
    "firstname": "Jonny",
    "username": "jonnydoo",
    "lastname": "Doo",
    "email": "john.doe@domain1.com",
    "orgSpecific": true,
    "status": "active",
    "businessAccount": true,
    "country": "US",
    "type": "federatedID",
    "__NAME__": "userjd",
    "__GROUPS__": [
        "groupId1",
        "groupId2"
    ]
}
```

#### Delete user

Delete a user from the Adobe organization. The user email must be provided in the URI path:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request DELETE \
'http://localhost:8080/openidm/system/adobe/__ACCOUNT__/USER_EMAIL'
{
    "_id": "john.doe@domain1.com",
    "id": "946F1E3A65DDEA2A0A495CEB@196c1e336579f87e495faa.e",
    "firstname": "John",
    "username": "userjd",
    "lastname": "Doe",
    "email": "john.doe@domain1.com",
    "orgSpecific": true,
    "status": "active",
    "businessAccount": true,
    "country": "US",
    "type": "federatedID",
    "__NAME__": "userjd",
    "__GROUPS__": [
        "groupId"
    ]
}
```

### GROUPS

#### Create group

To create a group, it's necessary to *at least* provide `groupName` field. The `description` field is optional and isn't returned. It's only visible from the Adobe web interface console:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request POST \
--data '{
    "groupName" : "group name",
    "description" : "group description"
}' \
'http://localhost:8080/openidm/system/adobe/__GROUP__?_action=create'
{
    "_id" : "groupId",
    "__NAME__" : "groupId",
}
```

#### Get groups

Retrieve a list of groups. To paginate the results the pageSize parameter value must be greater than 1, the size of each page is 400. By default, retrieves all users:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request GET \
'http://localhost:8080/openidm/system/adobe/__GROUP__?_queryFilter=true'
{
    "result": [
        {
            "_id" : "groupId1"
        },
        {
            "_id" : "groupId2"
        },
        {
            "_id" : "groupId3",
        },
        ...
    ],
    "resultCount": 999,
    "pagedResultsCookie": null,
    "totalPagedResultsPolicy": "NONE",
    "totalPagedResults": -1,
    "remainingPagedResults": -1
}
```

#### Get group

Retrieve a group, only the `_id` field can be displayed. The group id must be provided in the URI path:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request GET \
'http://localhost:8080/openidm/system/adobe/__GROUP__/GROUP_ID'
{
    "_id" : "groupId",
    "__NAME__" : "groupId"
}
```

#### Update a group

The field that can be updated for a group is `description`. The group description is only visible from the web interface console. The group id must be provided in the URI path:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request PUT \
--header 'If-Match: *' \
--data '{
    "description" : "New Description"
}' \
'http://localhost:8080/openidm/system/adobe/__GROUP__/GROUP_ID'
{
    "_id" : "groupId",
    "__NAME__" : "groupId",
}
```

#### Delete a group

The group id must be provided in the URI path:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request DELETE \
'http://localhost:8080/openidm/system/adobe/__GROUP__/GROUP_ID'
{
    "_id" : "groupId",
    "__NAME__" : "groupId"
}
```

## OpenICF Interfaces Implemented by the Adobe Admin Console Connector

The Adobe Admin Console Connector implements the following OpenICF interfaces. For additional details, see [ICF interfaces](interfaces.html):

* Create

  Creates an object and its `uid`.

* Delete

  Deletes an object, referenced by its `uid`.

* Schema

  Describes the object types, operations, and options that the connector supports.

* Script on Connector

  Enables an application to run a script in the context of the connector.

  Any script that runs on the connector has the following characteristics:

  * The script runs in the same execution environment as the connector and has access to all the classes to which the connector has access.

  * The script has access to a `connector` variable that is equivalent to an initialized instance of the connector. At a minimum, the script can access the connector configuration.

  * The script has access to any script arguments passed in by the application.

* Search

  Searches the target resource for all objects that match the specified object class and filter.

* Test

  Tests the connector configuration.

  Testing a configuration checks all elements of the environment that are referred to by the configuration are available. For example, the connector might make a physical connection to a host that is specified in the configuration to verify that it exists and that the credentials that are specified in the configuration are valid.

  This operation might need to connect to a resource, and, as such, might take some time. Do not invoke this operation too often, such as before every provisioning operation. The test operation is not intended to check that the connector is alive (that is, that its physical connection to the resource has not timed out).

  You can invoke the test operation before a connector configuration has been validated.

* Update

  Updates (modifies or replaces) objects on a target resource.

[]()

## Adobe Admin Console Connector Configuration

The Adobe Admin Console Connector has the following configurable properties:

### Basic Configuration Properties

| Property                                                                                                                                                                                          | Type            | Default                 | Encrypted(1)             | Required(2)               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | ----------------------- | ------------------------ | ------------------------- |
| `serviceUri`                                                                                                                                                                                      | `String`        | `null`                  |                          | [icon: check, set=fas]Yes |
| The service endpoint URI.                                                                                                                                                                         |                 |                         |                          |                           |
| `orgId`                                                                                                                                                                                           | `String`        | `null`                  |                          | [icon: check, set=fas]Yes |
| Your organization's unique ID, for example 12345\@AdobeOrg.                                                                                                                                       |                 |                         |                          |                           |
| `login`                                                                                                                                                                                           | `String`        | `null`                  |                          | [icon: check, set=fas]Yes |
| The service login name.                                                                                                                                                                           |                 |                         |                          |                           |
| `groupReadRateLimit`                                                                                                                                                                              | `String`        | `null`                  |                          | [icon: check, set=fas]Yes |
| Defines throttling for read operations either per seconds (`30/sec`) or per minute (`100/min`).                                                                                                   |                 |                         |                          |                           |
| `password`                                                                                                                                                                                        | `GuardedString` | `null`                  | [icon: lock, set=fas]Yes | [icon: times, set=fas]No  |
| The service user password.                                                                                                                                                                        |                 |                         |                          |                           |
| `userReadRateLimit`                                                                                                                                                                               | `String`        | `null`                  |                          | [icon: check, set=fas]Yes |
| Defines throttling for read operations either per seconds (`30/sec`) or per minute (`100/min`).                                                                                                   |                 |                         |                          |                           |
| `authenticationMethod`                                                                                                                                                                            | `String`        | `OAUTH`                 |                          | [icon: check, set=fas]Yes |
| Defines which method is to be used to authenticate on the remote server. Options are `BASIC` (username/password), `OAUTH` (Client id/secret), `JWT_TOKEN` (jwt token), or `TOKEN` (static token). |                 |                         |                          |                           |
| `tokenEndpoint`                                                                                                                                                                                   | `String`        | `null`                  |                          | [icon: times, set=fas]No  |
| When using OAUTH as authentication method, this property defines the endpoint where a new access token should be queried for (<https://myserver.com/oauth2/token>).                               |                 |                         |                          |                           |
| `writeRateLimit`                                                                                                                                                                                  | `String`        | `null`                  |                          | [icon: check, set=fas]Yes |
| Defines throttling for write operations (create/update/delete) either per second (`30/sec`) or per minute (`100/min`).                                                                            |                 |                         |                          |                           |
| `clientId`                                                                                                                                                                                        | `String`        | `null`                  |                          | [icon: check, set=fas]Yes |
| The client identifier for OAuth2.                                                                                                                                                                 |                 |                         |                          |                           |
| `clientSecret`                                                                                                                                                                                    | `GuardedString` | `null`                  | [icon: lock, set=fas]Yes | [icon: times, set=fas]No  |
| Secure client secret for OAuth2.                                                                                                                                                                  |                 |                         |                          |                           |
| `authToken`                                                                                                                                                                                       | `GuardedString` | `null`                  | [icon: lock, set=fas]Yes | [icon: times, set=fas]No  |
| Static authentication token.                                                                                                                                                                      |                 |                         |                          |                           |
| `acceptSelfSignedCertificates`                                                                                                                                                                    | `boolean`       | `false`                 |                          | [icon: check, set=fas]Yes |
| To be used for debug/test purposes. To be avoided in production.                                                                                                                                  |                 |                         |                          |                           |
| `disableHostNameVerifier`                                                                                                                                                                         | `boolean`       | `false`                 |                          | [icon: check, set=fas]Yes |
| To be used for debug/test purposes. To be avoided in production.                                                                                                                                  |                 |                         |                          |                           |
| `disableHttpCompression`                                                                                                                                                                          | `boolean`       | `false`                 |                          | [icon: check, set=fas]Yes |
| Set this property to `true` to disable content compression.                                                                                                                                       |                 |                         |                          |                           |
| `clientCertAlias`                                                                                                                                                                                 | `String`        | `null`                  |                          | [icon: check, set=fas]Yes |
| If TLS Mutual Auth is needed, set this to the certificate alias from the keystore.                                                                                                                |                 |                         |                          |                           |
| `clientCertPassword`                                                                                                                                                                              | `GuardedString` | `null`                  | [icon: lock, set=fas]Yes | [icon: check, set=fas]Yes |
| If TLS Mutual Auth is needed and the client certificate (private key) password is different from the keystore password, set this to the client private key password.                              |                 |                         |                          |                           |
| `maximumConnections`                                                                                                                                                                              | `Integer`       | `10`                    |                          | [icon: check, set=fas]Yes |
| Defines the max size of the HTTP connection pool used.                                                                                                                                            |                 |                         |                          |                           |
| `httpProxyHost`                                                                                                                                                                                   | `String`        | `null`                  |                          | [icon: check, set=fas]Yes |
| Defines the Hostname if an HTTP proxy is used between the connector and the service.                                                                                                              |                 |                         |                          |                           |
| `httpProxyPort`                                                                                                                                                                                   | `Integer`       | `null`                  |                          | [icon: check, set=fas]Yes |
| Defines the Port if an HTTP proxy is used between the connector and the service.                                                                                                                  |                 |                         |                          |                           |
| `httpProxyUsername`                                                                                                                                                                               | `String`        | `null`                  |                          | [icon: check, set=fas]Yes |
| Defines Proxy Username if an HTTP proxy is used between the connector and the service.                                                                                                            |                 |                         |                          |                           |
| `httpProxyPassword`                                                                                                                                                                               | `GuardedString` | `null`                  | [icon: lock, set=fas]Yes | [icon: check, set=fas]Yes |
| Defines Proxy Password if an HTTP proxy is used between the connector and the service.                                                                                                            |                 |                         |                          |                           |
| `connectionTimeout`                                                                                                                                                                               | `int`           | `30`                    |                          | [icon: times, set=fas]No  |
| Defines a timeout for the underlying HTTP connection in seconds.                                                                                                                                  |                 |                         |                          |                           |
| `refreshToken`                                                                                                                                                                                    | `GuardedString` | `null`                  |                          | [icon: times, set=fas]No  |
| Used by the refresh\_token grant type.                                                                                                                                                            |                 |                         |                          |                           |
| `grantType`                                                                                                                                                                                       | `String`        | `null`                  |                          | [icon: times, set=fas]No  |
| The OAuth2 grant type to use (`client_credentials`, `refresh_token`, or `jwt_bearer`).                                                                                                            |                 |                         |                          |                           |
| `scope`                                                                                                                                                                                           | `String`        | `null`                  |                          | [icon: times, set=fas]No  |
| The OAuth2 scope to use.                                                                                                                                                                          |                 |                         |                          |                           |
| `authorizationTokenPrefix`                                                                                                                                                                        | `String`        | `Bearer`                |                          | [icon: times, set=fas]No  |
| The prefix to be used in the Authorization HTTP header for Token authentication.                                                                                                                  |                 |                         |                          |                           |
| `useBasicAuthForOauthTokenNeg`                                                                                                                                                                    | `boolean`       | `true`                  |                          | [icon: check, set=fas]Yes |
| The Authentication method for refresh token (Basic Authentication or Sending the ClientId and Client Secret in the Header).                                                                       |                 |                         |                          |                           |
| `jwtKey`                                                                                                                                                                                          | `GuardedString` | `null`                  | [icon: lock, set=fas]Yes | [icon: times, set=fas]No  |
| The JWT data structure that represents a cryptographic key.                                                                                                                                       |                 |                         |                          |                           |
| `jwtExpiration`                                                                                                                                                                                   | `Integer`       | `null`                  |                          | [icon: times, set=fas]No  |
| Defines the JWT expiration time in seconds.                                                                                                                                                       |                 |                         |                          |                           |
| `jwtAlgorithm`                                                                                                                                                                                    | `String`        | `null`                  |                          | [icon: times, set=fas]No  |
| The Algorithm type to sign payload.                                                                                                                                                               |                 |                         |                          |                           |
| `jwtClaims`                                                                                                                                                                                       | `Map`           | `null`                  |                          | [icon: times, set=fas]No  |
| JWT Claims to be included in the payload                                                                                                                                                          |                 |                         |                          |                           |
| `jwtPem`                                                                                                                                                                                          | `GuardedString` | `null`                  | [icon: lock, set=fas]Yes | [icon: times, set=fas]No  |
| The contents of the private key of the PEM file                                                                                                                                                   |                 |                         |                          |                           |
| `jwtCert`                                                                                                                                                                                         | `GuardedString` | `null`                  | [icon: lock, set=fas]Yes | [icon: times, set=fas]No  |
| The contents of the certificate of the PEM file                                                                                                                                                   |                 |                         |                          |                           |
| `keyAlgorithm`                                                                                                                                                                                    | `String`        | `null`                  |                          | [icon: times, set=fas]No  |
| Indicates the type of key (such as RSA, DSA or EC) used to sign from the PEM.                                                                                                                     |                 |                         |                          |                           |
| `userAgent`                                                                                                                                                                                       | `String`        | `PingIdentityConnector` |                          | [icon: times, set=fas]No  |
| The User Agent HTTP Header used by the connector. Defaults to `PingIdentityConnector`.                                                                                                            |                 |                         |                          |                           |

(1) Whether the property value is considered confidential, and is therefore encrypted in IDM.

(2) A list of operations in this column indicates that the property is required for those operations.

---

---
title: Adobe Marketing Cloud connector
description: Reference and configuration guide for the Adobe Marketing Cloud connector, which manages profiles in an Adobe Campaign data store using PingIDM
component: openicf
page_id: openicf:connector-reference:adobe
canonical_url: https://docs.pingidentity.com/openicf/connector-reference/adobe.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  adobe-before-you-start: Before you start
  install_the_adobe_marketing_cloud_connector: Install the Adobe Marketing Cloud connector
  adobe-connector-config: Configure the Adobe Marketing Cloud connector
  test_the_adobe_marketing_cloud_connector: Test the Adobe Marketing Cloud connector
  adobe-connector-remote: Adobe Marketing Cloud remote connector
  config-connection-pooling-adobe: Configure connection pooling
  implemented-interfaces-org-forgerock-openicf-acm-ACMConnector-1.5.20.35: OpenICF Interfaces Implemented by the Adobe Marketing Cloud Connector
  config-properties-org-forgerock-openicf-acm-ACMConnector-1.5.20.35: Adobe Marketing Cloud Connector Configuration
  basic-configuration-properties-org-forgerock-openicf-acm-ACMConnector-1.5.20.35: Basic Configuration Properties
  adobe-integration-properties-org-forgerock-openicf-acm-ACMConnector-1.5.20.35: Adobe Integration Properties
---

# Adobe Marketing Cloud connector

The Adobe Marketing Cloud connector lets you manage profiles in an Adobe Campaign data store. The connector supports a subset of the OpenICF operations, as listed in [OpenICF Interfaces Implemented by the Adobe Marketing Cloud Connector](#implemented-interfaces-org-forgerock-openicf-acm-ACMConnector-1.5.20.35).

|   |                                                |
| - | ---------------------------------------------- |
|   | To use this connector, you need an *Adobe ID*. |

## Before you start

Configure a new integration on AdobeIO, as shown in the following steps. Note that these steps assume a specific version of the AdobeIO user interface. For information on the current version, refer to the corresponding [Adobe documentation](https://experienceleague.adobe.com/docs/campaign-standard/using/campaign-standard-home.html).

|   |                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------ |
|   | The integration requires a public certificate and private key that will be used to sign the JWT token. |

1. You can use IDM's generated self-signed certificate and private key to test the connector. In a production environment, use a CA-signed certificate and key.

   Export IDM's self-signed certificate as follows:

   1. Export the certificate and key from JCEKS to standardized format PKCS #12:

      ```
      keytool \
      -importkeystore \
      -srckeystore /path/to/openidm/security/keystore.jceks \
      -srcstoretype jceks \
      -destkeystore /path/to/keystore.p12 \
      -deststoretype PKCS12 \
      -srcalias openidm-localhost \
      -deststorepass changeit \
      -destkeypass changeit
      ```

   2. Export the certificate:

      ```
      openssl pkcs12 \
      -in /path/to/keystore.p12 \
      -nokeys \
      -out /path/to/cert.pem
      ```

   3. Export the unencrypted private key:

      ```
      openssl pkcs12 \
      -in /path/to/keystore.p12 \
      -nodes \
      -nocerts \
      -out /path/to/key.pem
      ```

2. Log in to <https://console.adobe.io/>.

3. Click Integrations > New Integration.

4. Click Access an API > Continue.

5. Under the Experience Cloud item, click Adobe Campaign > Continue, then click New integration > Continue.

6. Enter a name and short description for the new integration. For example, `IDM-managed`.

7. Drag and drop your public certificate file into the Public keys certificates area. Alternatively, click Select a File, and browse to the file location.

8. Select a license, then click Create Integration.

9. Select Continue to integration details to obtain the Client Credentials required by the connector.

   You will need these details for the connector configuration.

## Install the Adobe Marketing Cloud connector

|   |                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To check for an Advanced Identity Cloud application for this connector, refer to:- [Application management](https://docs.pingidentity.com/pingoneaic/latest/app-management/applications.html)

- [App catalog](https://docs.pingidentity.com/pingoneaic/latest/app-management/app-catalog.html) |

You can download most connectors from [Backstage](https://backstage.forgerock.com/downloads/browse/idm/featured/connectors), but some are included in the default deployment for Advanced Identity Cloud, IDM, or RCS. When using an included connector, you can skip installing it and move directly to configuration.

**Connector included in default deployment**

| Connector                           | IDM                      | RCS                     |
| ----------------------------------- | ------------------------ | ----------------------- |
| [Adobe Marketing Cloud](adobe.html) | [icon: check, set=fa]Yes | [icon: times, set=fa]No |

Download the connector .jar file from [Backstage](https://backstage.forgerock.com/downloads/browse/idm/featured/connectors).

* If you're running the connector locally, place it in the `/path/to/openidm/connectors` directory, for example:

  ```
  mv ~/Downloads/adobecm-connector-1.5.20.35.jar /path/to/openidm/connectors/
  ```

* If you're using a remote connector server (RCS), place it in the `/path/to/openicf/connectors` directory on the RCS.

## Configure the Adobe Marketing Cloud connector

Create a connector configuration using the IDM admin UI:

1. From the navigation bar, click Configure > Connectors.

2. On the Connectors page, click New Connector.

3. On the New Connector page, type a Connector Name.

4. From the Connector Type list, select Adobe Marketing Cloud Connector - 1.5.20.35.

5. Complete the Base Connector Details and any applicable Additional Options.

   |   |                                                                                                                                    |
   | - | ---------------------------------------------------------------------------------------------------------------------------------- |
   |   | For a list of all configuration properties, refer to [Adobe Marketing Cloud Connector Configuration](#adobecm-config-prop-ezLink). |

6. Click Save.

When your connector is configured correctly, the connector displays as Active in the admin UI.

Refer to [this procedure](configure-connector.html#connector-wiz-REST) to create a connector configuration over REST.

Alternatively, you can create a connector configuration file and place it in your project's `conf/` directory. IDM bundles a sample configuration file (`/path/to/openidm/samples/example-configurations/provisioners/provisioner.openicf-adobe.json`) that you can use as a starting point.

The following example shows an excerpt of the provisioner configuration. Enable the connector (set `"enabled" : true`) then edit at least the `configurationProperties` to match your Adobe IO setup:

```json
"configurationProperties" : {
    "endpoint" : "mc.adobe.io",
    "imsHost" : "ims-na1.adobelogin.com",
    "tenant" : "https://example.adobesandbox.com/",
    "apiKey" : "",
    "techAccId" : "example@techacct.adobe.com",
    "orgId" : "example@AdobeOrg",
    "clientSecret" : "CLIENT_SECRET",
    "privateKey" : "PRIVATE_KEY"
},
...
```

* `endpoint`

  The Adobe IO endpoint for Marketing Cloud. `mc.adobe.io` by default - you should not have to change this value.

* `imsHost`

  The Adobe Identity Management System (IMS) host. `ims-na1.adobelogin.com` by default - you should not have to change this value.

* `tenant`

  Your tenant (organization) name or sandbox host.

* `apiKey`

  The API key (client ID) assigned to your API client account.

* `techAccId`

  Your Technical account ID, required to generate the JWT.

* `orgId`

  Your organization's unique ID, for example `12345@AdobeOrg`.

* `clientSecret`

  The client secret assigned to your API client account.

* `privateKey`

  The private key used to sign the JWT token, corresponds to the public key certificate that you attached to the integration.

|   |                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------- |
|   | For a list of all configuration properties, refer to [Adobe Marketing Cloud Connector Configuration](#adobecm-config-prop-ezLink). |

### Test the Adobe Marketing Cloud connector

When your connector is configured correctly, you can test its status by running the following command:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
"http://localhost:8080/openidm/system/adobecm?_action=test"
[
  {
    "name": "adobecm",
    "enabled": true,
    "config": "config/provisioner.openicf/adobecm",
    "connectorRef": {
      "bundleName": "org.forgerock.openicf.connectors.adobecm-connector",
      "connectorName": "org.forgerock.openicf.acm.ACMConnector",
      "bundleVersion": "[1.5.0.0,1.6.0.0)"
    },
    "displayName": "Adobe Marketing Cloud Connector",
    "objectTypes": [
      "__ALL__",
      "account"
    ],
    "ok": true
  }
]
```

A status of `"ok": true` indicates that the connector can reach the configured Adobe integration.

### Adobe Marketing Cloud remote connector

If you want to run this connector outside of PingOne Advanced Identity Cloud or IDM, you can configure the Adobe Marketing Cloud connector as a remote connector. Java Connectors installed remotely on a Java Connector Server function identically to those bundled locally within PingOne Advanced Identity Cloud or installed locally on IDM.

Refer to [Remote connectors](remote-connector.html) for configuring the Adobe Marketing Cloud remote connector.

### Configure connection pooling

The Adobe Marketing Cloud connector uses [ICF pooling](pooling.html#icf-pooling) to manage connections. Learn more about the different pooling mechanisms in [Connectors by pooling mechanism](pooling.html#pooling-table).

## OpenICF Interfaces Implemented by the Adobe Marketing Cloud Connector

The Adobe Marketing Cloud Connector implements the following OpenICF interfaces. For additional details, see [ICF interfaces](interfaces.html):

* Create

  Creates an object and its `uid`.

* Delete

  Deletes an object, referenced by its `uid`.

* Schema

  Describes the object types, operations, and options that the connector supports.

* Script on Connector

  Enables an application to run a script in the context of the connector.

  Any script that runs on the connector has the following characteristics:

  * The script runs in the same execution environment as the connector and has access to all the classes to which the connector has access.

  * The script has access to a `connector` variable that is equivalent to an initialized instance of the connector. At a minimum, the script can access the connector configuration.

  * The script has access to any script arguments passed in by the application.

* Search

  Searches the target resource for all objects that match the specified object class and filter.

* Test

  Tests the connector configuration.

  Testing a configuration checks all elements of the environment that are referred to by the configuration are available. For example, the connector might make a physical connection to a host that is specified in the configuration to verify that it exists and that the credentials that are specified in the configuration are valid.

  This operation might need to connect to a resource, and, as such, might take some time. Do not invoke this operation too often, such as before every provisioning operation. The test operation is not intended to check that the connector is alive (that is, that its physical connection to the resource has not timed out).

  You can invoke the test operation before a connector configuration has been validated.

* Update

  Updates (modifies or replaces) objects on a target resource.

[]()

## Adobe Marketing Cloud Connector Configuration

The Adobe Marketing Cloud Connector has the following configurable properties:

### Basic Configuration Properties

| Property                                                                         | Type     | Default                  | Encrypted(1) | Required(2)               |
| -------------------------------------------------------------------------------- | -------- | ------------------------ | ------------ | ------------------------- |
| `endpoint`                                                                       | `String` | `mc.adobe.io`            |              | [icon: check, set=fas]Yes |
| The Adobe IO endpoint for Marketing Cloud. You should not have to change this.   |          |                          |              |                           |
| `imsHost`                                                                        | `String` | `ims-na1.adobelogin.com` |              | [icon: check, set=fas]Yes |
| Adobe Identity Management System (IMS) host. You should not have to change this. |          |                          |              |                           |
| `tenant`                                                                         | `String` | `null`                   |              | [icon: check, set=fas]Yes |
| Your tenant (organization) name or sandbox host.                                 |          |                          |              |                           |

(1) Whether the property value is considered confidential, and is therefore encrypted in IDM.

(2) A list of operations in this column indicates that the property is required for those operations.

### Adobe Integration Properties

| Property                                                                                                           | Type            | Default | Encrypted(1)             | Required(2)               |
| ------------------------------------------------------------------------------------------------------------------ | --------------- | ------- | ------------------------ | ------------------------- |
| `apiKey`                                                                                                           | `GuardedString` | `null`  | [icon: lock, set=fas]Yes | [icon: check, set=fas]Yes |
| The API key (client ID) assigned to your API client account.                                                       |                 |         |                          |                           |
| `technicalAccountID`                                                                                               | `String`        | `null`  |                          | [icon: check, set=fas]Yes |
| Your Technical account ID, required to generate the JWT.                                                           |                 |         |                          |                           |
| `organizationID`                                                                                                   | `String`        | `null`  |                          | [icon: check, set=fas]Yes |
| Your organization's unique ID, for example 12345\@AdobeOrg.                                                        |                 |         |                          |                           |
| `clientSecret`                                                                                                     | `GuardedString` | `null`  | [icon: lock, set=fas]Yes | [icon: check, set=fas]Yes |
| The client secret assigned to your API client account.                                                             |                 |         |                          |                           |
| `privateKey`                                                                                                       | `GuardedString` | `null`  | [icon: lock, set=fas]Yes | [icon: check, set=fas]Yes |
| The private key used to sign the JWT token, corresponds to the public key certificate attached to the integration. |                 |         |                          |                           |

(1) Whether the property value is considered confidential, and is therefore encrypted in IDM.

(2) A list of operations in this column indicates that the property is required for those operations.

---

---
title: Amazon Web Services (AWS) connector
description: "AWS IAM connector reference for PingIDM: configure and use the connector to manage users, groups, roles, policies, and organizational units in AWS IAM"
component: openicf
page_id: openicf:connector-reference:aws-iam
canonical_url: https://docs.pingidentity.com/openicf/connector-reference/aws-iam.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  before_you_start: Before you start
  install_the_aws_connector: Install the AWS connector
  configure_the_aws_connector: Configure the AWS connector
  test_the_aws_connector: Test the AWS connector
  aws_remote_connector: AWS remote connector
  config-connection-pooling-aws-iam: Configure connection pooling
  supported_resource_types: Supported resource types
  supported_search_filters: Supported search filters
  supported_attributes: Supported attributes
  aws_account_user_attributes: AWS account (user) attributes
  aws_group_attributes: AWS group attributes
  aws_role_attributes: AWS role attributes
  aws_managed_policy_attributes: AWS managed policy attributes
  aws_inline_policy_attributes: AWS inline policy attributes
  aws_service_control_policy_scp_attributes: AWS Service Control Policy (SCP) attributes
  aws_organizational_unit_ou_attributes: AWS Organizational Unit (OU) attributes
  use_the_aws_connector: Use the AWS connector
  user_account_operations: User account operations
  create_an_aws_user: Create an AWS user
  update_an_aws_user: Update an AWS user
  assign_other_objects_to_a_user: Assign other objects to a user
  unassign_other_objects_from_a_user: Unassign other objects from a user
  query_aws_users: Query AWS users
  reset_an_aws_user_account_password: Reset an AWS user account password
  delete_an_aws_user_account: Delete an AWS user account
  other_object_type_operations: Other object type operations
  query_aws_groups: Query AWS Groups
  query_aws_roles: Query AWS Roles
  query_aws_managed_policies: Query AWS Managed Policies
  query_aws_inline_policies: Query AWS Inline Policies
  query_aws_service_control_policies_scps: Query AWS Service Control Policies (SCPs)
  query_aws_organizational_units: Query AWS organizational units
  implemented-interfaces-org-forgerock-openicf-connectors-aws-AwsConnector-1.5.20.34: OpenICF Interfaces Implemented by the AWS Connector
  config-properties-org-forgerock-openicf-connectors-aws-AwsConnector-1.5.20.34: AWS Connector Configuration
  basic-configuration-properties-org-forgerock-openicf-connectors-aws-AwsConnector-1.5.20.34: Basic Configuration Properties
---

# Amazon Web Services (AWS) connector

Amazon Web Services (AWS) Identity and Access Management (IAM) is a web service for securely controlling access to AWS services. The AWS connector lets you manage and synchronize accounts between AWS and IDM managed user objects. You can also search, assign, and unassign certain other objects from AWS.

|   |                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | To use this connector, you must have an AWS administrator account with proper access to AWS as described in the [AWS documentation](https://docs.aws.amazon.com/IAM/latest/APIReference/welcome.html). |

## Before you start

Before you configure the connector, log in to your AWS administrator account and note the following:

* Access Key ID

  The AWS access key ID for the IAM user whose credentials are used to call AWS APIs.

* Secret Key ID

  The AWS secret access key associated with the access key ID.

* Role ARN

  The Amazon Resource Name (ARN) for the role.

* Credentials Expiration

  Time (in seconds) to configure the duration in which the temporary credentials expire. Optional. Default: `3600`.

* Region

  The host region of the AWS instance.

* Parent ID

  The unique identifier assigned to the parent entity in the AWS Organization hierarchy. Required for Organizational Unit operations.

* UserName

  The unique name of a user. Required specifically for retrieving inline policies associated with that user.

## Install the AWS connector

|   |                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To check for an Advanced Identity Cloud application for this connector, refer to:- [Application management](https://docs.pingidentity.com/pingoneaic/latest/app-management/applications.html)

- [App catalog](https://docs.pingidentity.com/pingoneaic/latest/app-management/app-catalog.html) |

You can download most connectors from [Backstage](https://backstage.forgerock.com/downloads/browse/idm/featured/connectors), but some are included in the default deployment for Advanced Identity Cloud, IDM, or RCS. When using an included connector, you can skip installing it and move directly to configuration.

**Connector included in default deployment**

| Connector                                 | IDM                     | RCS                     |
| ----------------------------------------- | ----------------------- | ----------------------- |
| [Amazon Web Services (AWS)](aws-iam.html) | [icon: times, set=fa]No | [icon: times, set=fa]No |

Download the connector .jar file from [Backstage](https://backstage.forgerock.com/downloads/browse/idm/featured/connectors).

* If you're running the connector locally, place it in the `/path/to/openidm/connectors` directory, for example:

  ```
  mv ~/Downloads/aws-connector-1.5.20.34.jar /path/to/openidm/connectors/
  ```

* If you're using a remote connector server (RCS), place it in the `/path/to/openicf/connectors` directory on the RCS.

## Configure the AWS connector

Create a connector configuration using the IDM admin UI:

1. From the navigation bar, click Configure > Connectors.

2. On the Connectors page, click New Connector.

3. On the New Connector page, type a Connector Name.

4. From the Connector Type list, select AWS Connector - 1.5.20.34.

5. Complete the Base Connector Details and any applicable Additional Options.

   |   |                                                                                                              |
   | - | ------------------------------------------------------------------------------------------------------------ |
   |   | For a list of all configuration properties, refer to [AWS Connector Configuration](#aws-config-prop-ezLink). |

6. Click Save.

When your connector is configured correctly, the connector displays as Active in the admin UI.

Refer to [this procedure](configure-connector.html#connector-wiz-REST) to create a connector configuration over REST.

### Test the AWS connector

Test that the configuration is correct by running the following command:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
"http://localhost:8080/openidm/system/aws?_action=test"
{
  "name": "aws",
  "enabled": true,
  "config": "config/provisioner.openicf/aws",
  "connectorRef": {
    "bundleVersion": "[1.5.0.0,1.6.0.0)",
    "bundleName": "org.forgerock.openicf.connectors.aws-connector",
    "connectorName": "org.forgerock.openicf.connectors.aws.AwsConnector"
  },
  "displayName": "AWS Connector",
  "objectTypes": [
    "__ACCOUNT__",
    "__GROUP__",
    "__ROLE__",
    "__MANAGEDPOLICY__",
    "__INLINEPOLICY__",
    "__SERVICECONTROLPOLICY__",
    "__ORGUNIT__"
  ],
  "ok": true
}
```

If the command returns `"ok": true`, your connector has been configured correctly and can authenticate to the AWS system.

### AWS remote connector

If you want to run this connector outside of PingOne Advanced Identity Cloud or IDM, you can configure the AWS connector as a remote connector. Java Connectors installed remotely on a Java Connector Server function identically to those bundled locally within PingOne Advanced Identity Cloud or installed locally on IDM.

Refer to [Remote connectors](remote-connector.html) for configuring the AWS remote connector.

### Configure connection pooling

The AWS connector uses [connector-specific pooling](pooling.html#connector-specific-pooling) to manage connections. Learn more about the different pooling mechanisms in [Connectors by pooling mechanism](pooling.html#pooling-table).

## Supported resource types

The connector maps the following ICF native types to AWS resource types:

| ICF Native Type            | AWS Resource Type      | Naming Attribute                                                                |
| -------------------------- | ---------------------- | ------------------------------------------------------------------------------- |
| `__ACCOUNT__`              | User                   | `__NAME__`                                                                      |
| `__GROUP__`                | Group                  | `__NAME__`                                                                      |
| `__ROLE__`                 | Role                   | `__NAME__`                                                                      |
| `__MANAGEDPOLICY__`        | Managed Policy         | `__NAME__`Maps to PolicyArn                                                     |
| `__INLINEPOLICY__`         | Inline Policy          | `__NAME__`Maps to PolicyName                                                    |
| `__SERVICECONTROLPOLICY__` | Service Control Policy | `__NAME__`Maps to PolicyId                                                      |
| `__ORGUNIT__`              | Organizational Unit    | `__NAME__`Maps to ParentId or Organizational Unit Name/Arn depending on context |

## Supported search filters

The AWS connector supports search operations with the following filter operators and attributes:

| Object Type                | Operator      | Attributes                       |
| -------------------------- | ------------- | -------------------------------- |
| `__ACCOUNT__`              | Equals filter | `Path`, `UserName` (`__NAME__`)  |
| `__GROUP__`                | Equals filter | `Path`, `GroupName` (`__NAME__`) |
| `__ROLE__`                 | Equals filter | `Path`, `RoleName` (`__NAME__`)  |
| `__MANAGEDPOLICY__`        | Equals filter | `Path`, `PolicyArn` (`__NAME__`) |
| `__INLINEPOLICY__`         | Equals filter | `PolicyName` (`__NAME__`)        |
| `__SERVICECONTROLPOLICY__` | Equals filter | `PolicyId` (`__NAME__`)          |
| `__ORGUNIT__`              | Equals filter | `ParentId` (`__NAME__`)          |

## Supported attributes

The AWS connector supports the following attributes.

### AWS account (user) attributes

The AWS connector supports the following AWS account attributes:

| Attribute            | Description                                                                                                                                                                                                                                                                             |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `UserName`           | The name of the user. Required. Can contain up to 64 letters, digits, and the characters `+`, `=`, `,`, `.`, `@`, `_`, `-`. Must be unique within the account.                                                                                                                          |
| `UserId`             | Auto-generated unique user ID. Read-only.                                                                                                                                                                                                                                               |
| `Path`               | The path for the user. Used to create a folder-like hierarchy. Default value is `/`.                                                                                                                                                                                                    |
| `Password`           | Password for the user's console login profile. Write-only.                                                                                                                                                                                                                              |
| `Arn`                | Amazon Resource Names (ARNs) uniquely identify the AWS resource. Read-only.                                                                                                                                                                                                             |
| `CreatedDate`        | Date the user was created, in [ISO 8601 date-time format](http://www.iso.org/iso/iso8601). Read-only.                                                                                                                                                                                   |
| `PasswordLastUsed`   | Date the user's password was last used for login. Read-only.                                                                                                                                                                                                                            |
| `PermissionBoundary` | The ARN of the policy used to set the permissions boundary for the user.                                                                                                                                                                                                                |
| `Tags`               | A list of customizable key-value pairs attached to the user. For example:```json
"Tags": [{
    "Key": "Department",
    "Value": "Accounting"
}]
```Learn more about [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the AWS documentation. |
| `Group`              | List of group names the user belongs to.                                                                                                                                                                                                                                                |
| `ManagedPolicy`      | List of managed policy ARNs attached to the user.                                                                                                                                                                                                                                       |
| `InlinePolicy`       | List of inline policies embedded in the user. Each item contains `PolicyName` and `PolicyDocument`.                                                                                                                                                                                     |
| `Role`               | List of roles assigned to the user. Each item contains `RoleName` and potentially `PolicyArn`.                                                                                                                                                                                          |

### AWS group attributes

| Attribute   | Description                                                                                      |
| ----------- | ------------------------------------------------------------------------------------------------ |
| `GroupName` | Name of the group. Required.                                                                     |
| `GroupId`   | Auto-generated unique group ID. Read-only.                                                       |
| `Arn`       | Amazon Resource Name (ARN) uniquely identifies the group resource. Read-only.                    |
| `Path`      | The path for the group. Used to create a folder-like hierarchy. Default value is `/`. Read-only. |

### AWS role attributes

| Attribute                  | Description                                                                                     |
| -------------------------- | ----------------------------------------------------------------------------------------------- |
| `RoleName`                 | Name of the Role. Required.                                                                     |
| `RoleId`                   | Auto-generated unique role ID. Read-only.                                                       |
| `Path`                     | The path for the role. Used to create a folder-like hierarchy. Default value is `/`. Read-only. |
| `Arn`                      | Amazon Resource Name (ARN) uniquely identifies the role resource. Read-only.                    |
| `CreateDate`               | Date the role was created. Read-only.                                                           |
| `AssumeRolePolicyDocument` | The trust policy document associated with the role. Read-only.                                  |

### AWS managed policy attributes

| Attribute                       | Description                                                                                                    |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `PolicyArn`                     | The Amazon Resource Name (ARN) uniquely identifies the Managed Policy. Required for identification. Read-only. |
| `PolicyId`                      | Auto-generated unique policy ID. Read-only.                                                                    |
| `PolicyName`                    | Name of the policy. Read-only.                                                                                 |
| `Path`                          | The path for the policy. Used to create a folder-like hierarchy. Default value is `/`. Read-only.              |
| `CreateDate`                    | Date the policy was created. Read-only.                                                                        |
| `AttachmentCount`               | Number of entities (users, groups, roles) attached to the policy. Read-only.                                   |
| `IsAttachable`                  | Whether the policy can be attached to users, groups, or roles. Read-only.                                      |
| `DefaultVersionId`              | The identifier for the default version of the policy. Read-only.                                               |
| `PermissionsBoundaryUsageCount` | Number of entities using this policy as a permissions boundary. Read-only.                                     |
| `UpdateDate`                    | Date the policy was last updated. Read-only.                                                                   |

### AWS inline policy attributes

| Attribute        | Description                                                                     |
| ---------------- | ------------------------------------------------------------------------------- |
| `PolicyName`     | Name of the inline policy. Required.                                            |
| `UserName`       | Name of the user the inline policy is attached to. Required for identification. |
| `PolicyDocument` | The policy document.                                                            |

### AWS Service Control Policy (SCP) attributes

| Attribute       | Description                                                                              |
| --------------- | ---------------------------------------------------------------------------------------- |
| `Id`            | The unique identifier (ID) of the SCP. Required for identification. Read-only.           |
| `PolicyName`    | Name of the SCP. Read-only.                                                              |
| `PolicySummary` | Object containing details like Arn, Type, Description, and AwsManaged status. Read-only. |

### AWS Organizational Unit (OU) attributes

| Attribute             | Description                                                                                           |
| --------------------- | ----------------------------------------------------------------------------------------------------- |
| `ParentId`            | The unique identifier (ID) of the parent entity (root or OU). Required for identification. Read-only. |
| `OrganizationalUnits` | List of OU objects, each containing `Name` and `Arn`. Read-only.                                      |

## Use the AWS connector

You can use the AWS connector to perform create, read, update, and delete (CRUD) operations on AWS IAM objects.

### User account operations

#### Create an AWS user

The following example creates a user with the minimum required attributes:

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Content-Type: application/json" \
--request POST \
--data '{
  "__NAME__": "bjensen"
}' \
"http://localhost:8080/openidm/system/aws/__ACCOUNT__?_action=create"
```

Response

```json
{
  "_id": "bjensen",
  "Path": "/",
  "UserId": "AIDAW3FY74V57KNBRIDU6",
  "__NAME__": "bjensen",
  "Arn": "arn:aws:iam::470686885243:user/bjensen",
  "CreatedDate": "Thu Jun 02 16:46:39 PDT 2022"
}
```

The following example creates a user with all assignable attributes:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Content-Type: application/json" \
--request POST \
--data '{
  "__NAME__": "jdoe",
  "Path": "/engineering/",
  "__PASSWORD__": "P@ssw0rd123!",
  "PermissionsBoundary": "arn:aws:iam::aws:policy/PowerUserAccess",
  "Tags": [{ "Key": "Project", "Value": "Phoenix" }],
  "__GROUP__": ["developers"],
  "__MANAGEDPOLICY__": ["arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess"],
  "__ROLE__": [{"RoleName": "EC2InstanceRole"}],
  "__INLINEPOLICY__": [{
    "PolicyName": "S3BucketAccess",
    "PolicyDocument": {
      "Version": "2012-10-17",
      "Statement": [{
        "Effect": "Allow",
        "Action": "s3:ListBucket",
        "Resource": "arn:aws:s3:::example_bucket"
      }]
    }
  }]
}' \
"http://localhost:8080/openidm/system/aws/__ACCOUNT__?_action=create"
```

Response:

```json
{
  "_id": "jdoe",
  "CreatedDate": "Fri May 02 13:00:00 PDT 2025",
  "Arn": "arn:aws:iam::123456789012:user/engineering/jdoe",
  "__INLINEPOLICY__": [ { "PolicyName": "S3BucketAccess" } ],
  "__NAME__": "jdoe",
  "__GROUP__": [ "developers" ],
  "Path": "/engineering/",
  "__ROLE__": [ { "RoleName": "EC2InstanceRole" } ],
  "PermissionsBoundary": "arn:aws:iam::aws:policy/PowerUserAccess",
  "__MANAGEDPOLICY__": [ "arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess" ],
  "Tags": [ { "Project": "Phoenix" } ],
  "UserId": "AIDACKCEVSQ6C2EXAMPLE"
}
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | * You must specify at least `__NAME__` when creating a user.

* Usernames can be up to 64 characters long and include letters, digits, and `+ = , . @ _ -`.

* []()Assigning roles (`__ROLE__`) during user creation is informational in IAM; roles are assumed, not directly assigned like groups or policies. The connector reflects attached policies for consistency but doesn't perform role assignment in the AWS sense. |

#### Update an AWS user

Modify an existing user with a PUT request. Include all attributes you want the user to have; attributes not included in the PUT request might be removed or reset depending on the target system behavior (often equivalent to PATCH for specific fields like Tags, Group, Policy, Role additions/removals).

Modifiable attributes:

* `__NAME__` (Requires specifying the old ID in the URL)

* `__PASSWORD__` (Use PATCH for password changes)

* `Path`

* `PermissionsBoundary`

* `Tags`

* `__GROUP__`

* `__MANAGEDPOLICY__`

* `__INLINEPOLICY__`

* `__ROLE__` (Reference the [note in Create an AWS user](#role-note-create))

For example, to add a new tag to a user:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Content-Type: application/json" \
--header "If-Match:*" \
--request PUT \
--data '{
  "__NAME__": "bjensen",
  "Tags": [{
    "Key": "Project",
    "Value": "Meteor"
  }]
}' \
"http://localhost:8080/openidm/system/aws/__ACCOUNT__/bjensen"
{
  "_id": "bjensen",
  "Path": "/",
  "UserId": "AIDAW3FY74V57KNBRIDU6",
  "__NAME__": "bjensen",
  "Arn": "arn:aws:iam::470686885243:user/bjensen",
  "CreatedDate": "Thu Jun 02 16:46:39 PDT 2022",
  "Tags": [
    {
      "Project": "Meteor"
    }
  ]
}
```

#### Assign other objects to a user

Use PATCH or PUT to add groups, managed policies, inline policies, or roles to a user.

Example using PATCH to add a group and a managed policy:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Content-Type: application/json" \
--header "If-Match:*" \
--request PATCH \
--data '[
  {"operation": "add", "field": "__GROUP__", "value": ["qa-team"]},
  {"operation": "add", "field": "__MANAGEDPOLICY__", "value": ["arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"]}
]' \
"http://localhost:8080/openidm/system/aws/__ACCOUNT__/jdoe"
```

#### Unassign other objects from a user

Use PATCH or PUT to remove groups, managed policies, inline policies, or roles from a user.

Example using PATCH to remove a group and an inline policy:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Content-Type: application/json" \
--header "If-Match:*" \
--request PATCH \
--data '[
  {"operation": "remove", "field": "__GROUP__", "value": ["frontend-devs"]},
  {"operation": "remove", "field": "__INLINEPOLICY__", "value": [{"PolicyName": "S3BucketAccess"}]}
]' \
"http://localhost:8080/openidm/system/aws/__ACCOUNT__/jdoe"
```

#### Query AWS users

The following example queries all AWS users:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Content-Type: application/json" \
--request GET \
"http://localhost:8080/openidm/system/aws/__ACCOUNT__?_queryId=query-all-ids"
{
  "result": [
    {
      "_id": "bjensen"
    },
    {
      "_id": "frank@example.com"
    },
    {
      "_id": "testFR4User"
    },
    {
      "_id": "testFR5User"
    },
    {
      "_id": "testFR6User"
    }
  ],
  …​
}
```

The following command queries a specific user by their ID:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Content-Type: application/json" \
--request GET \
"http://localhost:8080/openidm/system/aws/__ACCOUNT__/bjensen"
{
  "_id": "bjensen",
  "Path": "/",
  "UserId": "AIDAW3FY74V57KNBRIDU6",
  "__NAME__": "bjensen",
  "Arn": "arn:aws:iam::470686885243:user/bjensen",
  "CreatedDate": "Thu Jun 02 16:46:39 PDT 2022",
  "Tags": [
    {
      "Project": "Meteor"
    }
  ]
}
```

#### Reset an AWS user account password

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Content-Type: application/json" \
--header "if-Match:*" \
--request PATCH \
--data '[{
  "operation": "add",
  "field": "__PASSWORD__",
  "value": "Passw0rd@123!"
}]' \
"http://localhost:8080/openidm/system/aws/__ACCOUNT__/bjensen"
{
  "_id": "bjensen",
  "Path": "/",
  "UserId": "AIDAW3FY74V57KNBRIDU6",
  "__NAME__": "bjensen",
  "Arn": "arn:aws:iam::470686885243:user/bjensen",
  "CreatedDate": "Thu Jun 02 16:46:39 PDT 2022",
  "Tags": [
    {
      "Project": "Meteor"
    }
  ]
}
```

|   |                                                                                                 |
| - | ----------------------------------------------------------------------------------------------- |
|   | While the `__PASSWORD__` field is not returned in the response, the user's password is updated. |

#### Delete an AWS user account

Use a DELETE request to remove a user from AWS IAM.

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Content-Type: application/json" \
--request DELETE \
"http://localhost:8080/openidm/system/aws/__ACCOUNT__/bjensen"
{
  "_id": "bjensen",
  "Path": "/",
  "UserId": "AIDAW3FY74V57KNBRIDU6",
  "__NAME__": "bjensen",
  "Arn": "arn:aws:iam::470686885243:user/bjensen",
  "CreatedDate": "Thu Jun 02 16:46:39 PDT 2022",
  "Tags": [
    {
      "Project": "Meteor"
    }
  ]
}
```

### Other object type operations

A similar query pattern applies to groups, roles, managed policies, inline policies, service control policies, and organizational units using their respective object types (`GROUP`, `ROLE`, and so on.) in the request URL. For example, `_queryFilter=True` to return all applicable objects, and using the specific object ID to return a particular object.

#### Query AWS Groups

Query all groups:

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--request GET \
"http://localhost:8080/openidm/system/aws/__GROUP__?_queryFilter=True"
```

Response

```json
{
  "result": [
    {
      "_id": "forge",
      "Path": "/",
      "__NAME__": "forge",
      "GroupId": "AGPAW3FY74V5TAMVGJTDO",
      "GroupName": "forge",
      "Arn": "arn:aws:iam::470686885243:group/forge"
    },
    {
      "_id": "IAMAdministrator",
      "Path": "/",
      "__NAME__": "IAMAdministrator",
      "GroupId": "AGPAW3FY74V5XKCZVOQI5",
      "GroupName": "IAMAdministrator",
      "Arn": "arn:aws:iam::470686885243:group/IAMAdministrator"
    },
    {
      "_id": "SuperUser",
      "Path": "/",
      "__NAME__": "SuperUser",
      "GroupId": "AGPAW3FY74V5XANUBMNXT",
      "GroupName": "SuperUser",
      "Arn": "arn:aws:iam::470686885243:group/SuperUser"
    },
    {
      "_id": "TempGroup",
      "Path": "/",
      "__NAME__": "TempGroup",
      "GroupId": "AGPAW3FY74V5RBM7LKG5S",
      "GroupName": "TempGroup",
      "Arn": "arn:aws:iam::470686885243:group/TempGroup"
    },
    {
      "_id": "Windows_Access",
      "Path": "/",
      "__NAME__": "Windows_Access",
      "GroupId": "AGPAW3FY74V57Z7SG3GRY",
      "GroupName": "Windows_Access",
      "Arn": "arn:aws:iam::470686885243:group/Windows_Access"
    }
  ],
  ...
}
```

Query a specific group:

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--request GET \
"http://localhost:8080/openidm/system/aws/__GROUP__/developers"
```

Response

```json
{
  "_id": "developers",
  "Path": "/",
  "__NAME__": "developers",
  "GroupId": "AGPACKCEVSQ6C2EXAMPLE",
  "GroupName": "developers",
  "Arn": "arn:aws:iam::123456789012:group/developers"
}
```

#### Query AWS Roles

Query all roles:

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--request GET \
"http://localhost:8080/openidm/system/aws/__ROLE__?_queryFilter=True"
```

Response

```json
{
  "result": [
    {
      "_id": "Adminrole",
      "CreatedDate": "Fri Mar 08 13:24:10 IST 2024",
      "AssumeRolePolicyDocument": "%7B%22Version%22%3A%222012-10-17%22%2C%22Statement%22%3A%5B%7B%22Effect%22%3A%22Allow%22%2C%22Principal%22%3A%7B%22AWS%22%3A%22arn%3Aaws%3Aiam%3A%3A470686885243%3Aroot%22%7D%2C%22Action%22%3A%22sts%3AAssumeRole%22%2C%22Condition%22%3A%7B%7D%7D%5D%7D",
      "__NAME__": "Adminrole",
      "Path": "/",
      "RoleArn": "arn:aws:iam::470686885243:role/Adminrole",
      "RoleName": "Adminrole",
      "RoleId": "AROAW3FY74V5XMWBZPK5U"
    },
    {
      "_id": "aws-quicksight-secretsmanager-role-v0",
      "CreatedDate": "Fri Jan 26 23:37:52 IST 2024",
      "AssumeRolePolicyDocument": "%7B%22Version%22%3A%222012-10-17%22%2C%22Statement%22%3A%5B%7B%22Effect%22%3A%22Allow%22%2C%22Principal%22%3A%7B%22Service%22%3A%22quicksight.amazonaws.com%22%7D%2C%22Action%22%3A%22sts%3AAssumeRole%22%7D%5D%7D",
      "__NAME__": "aws-quicksight-secretsmanager-role-v0",
      "Path": "/service-role/",
      "RoleArn": "arn:aws:iam::470686885243:role/service-role/aws-quicksight-secretsmanager-role-v0",
      "RoleName": "aws-quicksight-secretsmanager-role-v0",
      "RoleId": "AROAW3FY74V54P5FRC3ZC"
    },
    ...
  ]
}
```

Query a specific role:

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--request GET \
"http://localhost:8080/openidm/system/aws/__ROLE__/AWSTokenRole"
```

Response

```json
{
  "_id": "AWSTokenRole",
  "CreatedDate": "Mon Mar 28 19:23:45 IST 2022",
  "AssumeRolePolicyDocument": "%7B%22Version%22%3A%222012-10-       17%22%2C%22Statement%22%3A%5B%7B%22Effect%22%3A%22Allow%22%2C%22Principal%22%3A%7B%22AWS%22%3A%22arn%3Aaws%3Aiam%3A%3A470686885243%3Aroot%22%7D%2C%22Action%22%3A%22sts%3AAssumeRole%22%2C%22Condition%22%3A%7B%7D%7D%5D%7D",
  "__NAME__": "AWSTokenRole",
  "Path": "/",
  "RoleArn": "arn:aws:iam::470686885243:role/AWSTokenRole",
  "RoleName": "AWSTokenRole",
  "RoleId": "AROAW3FY74V54K33FGL7Z"
}
```

#### Query AWS Managed Policies

Query all managed policies:

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--request GET \
"http://localhost:8080/openidm/system/aws/__MANAGEDPOLICY__?_queryFilter=True"
```

Response

```json
{
  "result": [
    { "_id": "arn:aws:iam::aws:policy/AdministratorAccess", ... },
    { "_id": "arn:aws:iam::aws:policy/PowerUserAccess", ... },
    { "_id": "arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess", ... },
    ...
  ],
  ...
}
```

Query a specific managed policy using ARN as the ID:

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--request GET \
"http://localhost:8080/openidm/system/aws/__MANAGEDPOLICY__/arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess"
```

Response

```json
{
  "_id": "arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess",
  "UpdateDate": "...",
  "PolicyArn": "arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess",
  "AttachmentCount": "5",
  "CreatedDate": "...",
  "PermissionsBoundaryUsageCount": "0",
  "__NAME__": "AmazonEC2ReadOnlyAccess",
  "PolicyName": "AmazonEC2ReadOnlyAccess",
  "IsAttachable": "true",
  "Path": "/",
  "DefaultVersionId": "v15",
  "PolicyId": "ANPACKCEVSQ6C2EXAMPLE"
}
```

#### Query AWS Inline Policies

Query all inline policies:

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--request GET \
"http://localhost:8080/openidm/system/aws/__INLINEPOLICY__?_queryFilter=True"
```

Response

```json
{
  "result": [
    {
      "_id": "Demo_Inline",
      "Username": "Enduser",
      "PolicyDocument": "%7B%20%09%22Version%22%3A%20%222012-10-17%22%2C%20%09%22Statement%22%3A%20%5B%20%09%09%7B%20%09%09%09%22Sid%22%3A%20%22VisualEditor0%22%2C%20%09%09%09%22Effect%22%3A%20%22Allow%22%2C%20%09%09%09%22Action%22%3A%20%5B%20%09%09%09%09%22iam%3AGenerateCredentialReport%22%2C%20%09%09%09%09%22iam%3AGetAccountPasswordPolicy%22%2C%20%09%09%09%09%22iam%3AUpdateCloudFrontPublicKey%22%2C%20%09%09%09%09%22iam%3AGetServiceLastAccessedDetailsWithEntities%22%2C%20%09%09%09%09%22iam%3AListServerCertificates%22%2C%20%09%09%09%09%22iam%3ASetSTSRegionalEndpointStatus%22%2C%20%09%09%09%09%22iam%3AGetServiceLastAccessedDetails%22%2C%20%09%09%09%09%22iam%3AListVirtualMFADevices%22%2C%20%09%09%09%09%22iam%3AGetOrganizationsAccessReport%22%2C%20%09%09%09%09%22iam%3ASetSecurityTokenServicePreferences%22%2C%20%09%09%09%09%22iam%3AUpdateAccountName%22%2C%20%09%09%09%09%22iam%3ASimulateCustomPolicy%22%2C%20%09%09%09%09%22iam%3AGetAccountEmailAddress%22%2C%20%09%09%09%09%22iam%3AGetCloudFrontPublicKey%22%2C%20%09%09%09%09%22iam%3ACreateAccountAlias%22%2C%20%09%09%09%09%22iam%3AUpdateAccountEmailAddress%22%2C%20%09%09%09%09%22iam%3AGetAccountAuthorizationDetails%22%2C%20%09%09%09%09%22iam%3ADeleteCloudFrontPublicKey%22%2C%20%09%09%09%09%22iam%3ADeleteAccountAlias%22%2C%20%09%09%09%09%22iam%3AGetCredentialReport%22%2C%20%09%09%09%09%22iam%3AListPolicies%22%2C%20%09%09%09%09%22iam%3ADeleteAccountPasswordPolicy%22%2C%20%09%09%09%09%22iam%3AListSAMLProviders%22%2C%20%09%09%09%09%22iam%3AListCloudFrontPublicKeys%22%2C%20%09%09%09%09%22iam%3AListRoles%22%2C%20%09%09%09%09%22iam%3AListInstanceProfiles%22%2C%20%09%09%09%09%22iam%3AUploadCloudFrontPublicKey%22%2C%20%09%09%09%09%22iam%3AGetContextKeysForCustomPolicy%22%2C%20%09%09%09%09%22iam%3AUpdateAccountPasswordPolicy%22%2C%20%09%09%09%09%22iam%3AListOpenIDConnectProviders%22%2C%20%09%09%09%09%22iam%3AGetAccountName%22%2C%20%09%09%09%09%22iam%3AListAccountAliases%22%2C%20%09%09%09%09%22iam%3AListUsers%22%2C%20%09%09%09%09%22iam%3AListGroups%22%2C%20%09%09%09%09%22iam%3AListSTSRegionalEndpointsStatus%22%2C%20%09%09%09%09%22iam%3AGetAccountSummary%22%20%09%09%09%5D%2C%20%09%09%09%22Resource%22%3A%20%22%2A%22%20%09%09%7D%2C%20%09%09%7B%20%09%09%09%22Sid%22%3A%20%22VisualEditor1%22%2C%20%09%09%09%22Effect%22%3A%20%22Allow%22%2C%20%09%09%09%22Action%22%3A%20%22iam%3A%2A%22%2C%20%09%09%09%22Resource%22%3A%20%5B%20%09%09%09%09%22arn%3Aaws%3Aiam%3A%3A470686885243%3Auser%2F%2A%22%2C%20%09%09%09%09%22arn%3Aaws%3Aiam%3A%3A470686885243%3Aaccess-report%2F%2A%22%2C%20%09%09%09%09%22arn%3Aaws%3Aiam%3A%3A470686885243%3Aoidc-provider%2F%2A%22%2C%20%09%09%09%09%22arn%3Aaws%3Aiam%3A%3A470686885243%3Apolicy%2F%2A%22%2C%20%09%09%09%09%22arn%3Aaws%3Aiam%3A%3A470686885243%3Amfa%2F%2A%22%2C%20%09%09%09%09%22arn%3Aaws%3Aiam%3A%3A470686885243%3Ainstance-profile%2F%2A%22%2C%20%09%09%09%09%22arn%3Aaws%3Aiam%3A%3A470686885243%3Asms-mfa%2F%2A%22%2C%20%09%09%09%09%22arn%3Aaws%3Aiam%3A%3A470686885243%3Agroup%2F%2A%22%2C%20%09%09%09%09%22arn%3Aaws%3Aiam%3A%3A470686885243%3Asaml-provider%2F%2A%22%2C%20%09%09%09%09%22arn%3Aaws%3Aiam%3A%3A470686885243%3Arole%2F%2A%22%2C%20%09%09%09%09%22arn%3Aaws%3Aiam%3A%3A470686885243%3Aserver-certificate%2F%2A%22%20%09%09%09%5D%20%09%09%7D%20%09%5D%20%7D",
      "PolicyName": "Demo_Inline",
      "__NAME__": "Demo_Inline"
    },
    {
      "_id": "inline_example",
      "Username": "Enduser",
      "PolicyDocument": "%7B%0A%09%22Version%22%3A%20%222012-10-17%22%2C%0A%09%22Statement%22%3A%20%5B%0A%09%09%7B%0A%09%09%09%22Sid%22%3A%20%22VisualEditor0%22%2C%0A%09%09%09%22Effect%22%3A%20%22Allow%22%2C%0A%09%09%09%22Action%22%3A%20%22iam%3A%2A%22%2C%0A%09%09%09%22Resource%22%3A%20%22%2A%22%0A%09%09%7D%0A%09%5D%0A%7D",
      "PolicyName": "inline_example",
      "__NAME__": "inline_example"
    },
    {
      "_id": "Test_Inline_Policy",
      "Username": "Enduser",
      "PolicyDocument": "%7B%0A%09%22Version%22%3A%20%222012-10-17%22%2C%0A%09%22Statement%22%3A%20%5B%0A%09%09%7B%0A%09%09%09%22Sid%22%3A%20%22VisualEditor0%22%2C%0A%09%09%09%22Effect%22%3A%20%22Allow%22%2C%0A%09%09%09%22Action%22%3A%20%22iam%3A%2A%22%2C%0A%09%09%09%22Resource%22%3A%20%22%2A%22%0A%09%09%7D%0A%09%5D%0A%7D",
      "PolicyName": "Test_Inline_Policy",
      "__NAME__": "Test_Inline_Policy"
    }
  ],
  ...
}
```

Query a specific inline policy:

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--request GET \
"http://localhost:8080/openidm/system/aws/__INLINEPOLICY__/Demo_Inline"
```

Response

```json
{
  "_id": "Demo_Inline",
  "Username": "Enduser",
  "PolicyDocument": "%7B%20%09%22Version%22%3A%20%222012-10-17%22%2C%20%09%22Statement%22%3A%20%5B%20%09%09%7B%20%09%09%09%22Sid%22%3A%20%22VisualEditor0%22%2C%20%09%09%09%22Effect%22%3A%20%22Allow%22%2C%20%09%09%09%22Action%22%3A%20%5B%20%09%09%09%09%22iam%3AGenerateCredentialReport%22%2C%20%09%09%09%09%22iam%3AGetAccountPasswordPolicy%22%2C%20%09%09%09%09%22iam%3AUpdateCloudFrontPublicKey%22%2C%20%09%09%09%09%22iam%3AGetServiceLastAccessedDetailsWithEntities%22%2C%20%09%09%09%09%22iam%3AListServerCertificates%22%2C%20%09%09%09%09%22iam%3ASetSTSRegionalEndpointStatus%22%2C%20%09%09%09%09%22iam%3AGetServiceLastAccessedDetails%22%2C%20%09%09%09%09%22iam%3AListVirtualMFADevices%22%2C%20%09%09%09%09%22iam%3AGetOrganizationsAccessReport%22%2C%20%09%09%09%09%22iam%3ASetSecurityTokenServicePreferences%22%2C%20%09%09%09%09%22iam%3AUpdateAccountName%22%2C%20%09%09%09%09%22iam%3ASimulateCustomPolicy%22%2C%20%09%09%09%09%22iam%3AGetAccountEmailAddress%22%2C%20%09%09%09%09%22iam%3AGetCloudFrontPublicKey%22%2C%20%09%09%09%09%22iam%3ACreateAccountAlias%22%2C%20%09%09%09%09%22iam%3AUpdateAccountEmailAddress%22%2C%20%09%09%09%09%22iam%3AGetAccountAuthorizationDetails%22%2C%20%09%09%09%09%22iam%3ADeleteCloudFrontPublicKey%22%2C%20%09%09%09%09%22iam%3ADeleteAccountAlias%22%2C%20%09%09%09%09%22iam%3AGetCredentialReport%22%2C%20%09%09%09%09%22iam%3AListPolicies%22%2C%20%09%09%09%09%22iam%3ADeleteAccountPasswordPolicy%22%2C%20%09%09%09%09%22iam%3AListSAMLProviders%22%2C%20%09%09%09%09%22iam%3AListCloudFrontPublicKeys%22%2C%20%09%09%09%09%22iam%3AListRoles%22%2C%20%09%09%09%09%22iam%3AListInstanceProfiles%22%2C%20%09%09%09%09%22iam%3AUploadCloudFrontPublicKey%22%2C%20%09%09%09%09%22iam%3AGetContextKeysForCustomPolicy%22%2C%20%09%09%09%09%22iam%3AUpdateAccountPasswordPolicy%22%2C%20%09%09%09%09%22iam%3AListOpenIDConnectProviders%22%2C%20%09%09%09%09%22iam%3AGetAccountName%22%2C%20%09%09%09%09%22iam%3AListAccountAliases%22%2C%20%09%09%09%09%22iam%3AListUsers%22%2C%20%09%09%09%09%22iam%3AListGroups%22%2C%20%09%09%09%09%22iam%3AListSTSRegionalEndpointsStatus%22%2C%20%09%09%09%09%22iam%3AGetAccountSummary%22%20%09%09%09%5D%2C%20%09%09%09%22Resource%22%3A%20%22%2A%22%20%09%09%7D%2C%20%09%09%7B%20%09%09%09%22Sid%22%3A%20%22VisualEditor1%22%2C%20%09%09%09%22Effect%22%3A%20%22Allow%22%2C%20%09%09%09%22Action%22%3A%20%22iam%3A%2A%22%2C%20%09%09%09%22Resource%22%3A%20%5B%20%09%09%09%09%22arn%3Aaws%3Aiam%3A%3A470686885243%3Auser%2F%2A%22%2C%20%09%09%09%09%22arn%3Aaws%3Aiam%3A%3A470686885243%3Aaccess-report%2F%2A%22%2C%20%09%09%09%09%22arn%3Aaws%3Aiam%3A%3A470686885243%3Aoidc-provider%2F%2A%22%2C%20%09%09%09%09%22arn%3Aaws%3Aiam%3A%3A470686885243%3Apolicy%2F%2A%22%2C%20%09%09%09%09%22arn%3Aaws%3Aiam%3A%3A470686885243%3Amfa%2F%2A%22%2C%20%09%09%09%09%22arn%3Aaws%3Aiam%3A%3A470686885243%3Ainstance-profile%2F%2A%22%2C%20%09%09%09%09%22arn%3Aaws%3Aiam%3A%3A470686885243%3Asms-mfa%2F%2A%22%2C%20%09%09%09%09%22arn%3Aaws%3Aiam%3A%3A470686885243%3Agroup%2F%2A%22%2C%20%09%09%09%09%22arn%3Aaws%3Aiam%3A%3A470686885243%3Asaml-provider%2F%2A%22%2C%20%09%09%09%09%22arn%3Aaws%3Aiam%3A%3A470686885243%3Arole%2F%2A%22%2C%20%09%09%09%09%22arn%3Aaws%3Aiam%3A%3A470686885243%3Aserver-certificate%2F%2A%22%20%09%09%09%5D%20%09%09%7D%20%09%5D%20%7D",
  "PolicyName": "Demo_Inline",
  "__NAME__": "Demo_Inline"
}
```

#### Query AWS Service Control Policies (SCPs)

Query all SCPs:

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--request GET \
"http://localhost:8080/openidm/system/aws/__SERVICECONTROLPOLICY__?_queryFilter=True"
```

Response

```json
{
  "result": [
    {
      "_id": "p-FullAWSAccess",
      "PolicyName": "FullAWSAccess",
      "__NAME__": "FullAWSAccess",
      "Id": "p-FullAWSAccess",
      "PolicySummary": [
        {
          "Type": "SERVICE_CONTROL_POLICY",
          "Description": "",
          "Arn": "arn:aws:organizations::470686885243:policy/o-r7bvsqr1wd/service_control_policy/p-pcmxrekp",
          "AwsManaged": "false"
        }
      ]
    },
    {
      "_id": "p-pcmxrekp",
      "PolicyName": "Sandbox SCP",
      "__NAME__": "Sandbox SCP",
      "Id": "p-pcmxrekp",
      "PolicySummary": [
        {
          "Type": "SERVICE_CONTROL_POLICY",
          "Description": "",
          "Arn": "arn:aws:organizations::470686885243:policy/o-r7bvsqr1wd/service_control_policy/p-pcmxrekp",
          "AwsManaged": "false"
        }
      ]
    }
  ],
  ...
}
```

Query a specific SCP:

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--request GET \
"http://localhost:8080/openidm/system/aws/__SERVICECONTROLPOLICY__/p-DenyHighRiskActions"
```

Response

```json
{
  "_id": "p-pcmxrekp",
  "PolicyName": "Sandbox SCP",
  "__NAME__": "Sandbox SCP",
  "Id": "p-pcmxrekp",
  "PolicySummary": [
    {
      "Type": "SERVICE_CONTROL_POLICY",
      "Description": "",
      "Arn": "arn:aws:organizations::470686885243:policy/o-r7bvsqr1wd/service_control_policy/p-pcmxrekp",
      "AwsManaged": "false"
    }
  ]
}
```

#### Query AWS organizational units

Query all organizational units:

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--request GET \
"http://localhost:8080/openidm/system/aws/__ORGUNIT__?_queryFilter=True"
```

Response

```json
{
  "result": [
    {
      "_id": "ou-2g8u-y0g6eo9k",
      "__NAME__": "ORGTEST",
      "ParentId": "ou-2g8u-y0g6eo9k"
    },
    {
      "_id": "ou-2g8u-jvpza68y",
      "OrganizationalUnits": [
        {
          "Arn": "arn:aws:organizations::470686885243:ou/o-r7bvsqr1wd/ou-2g8u-kgsw9s1e",
          "Name": "1-Sandboxchild"
        }
      ],
      "__NAME__": "Sandbox",
      "ParentId": "ou-2g8u-jvpza68y"
    },
    {
      "_id": "ou-2g8u-mfus8u4b",
      "__NAME__": "Tempexample",
      "ParentId": "ou-2g8u-mfus8u4b"
    },
    {
      "_id": "ou-2g8u-b3z1vwel",
      "__NAME__": "TestOrganization",
      "ParentId": "ou-2g8u-b3z1vwel"
    }
  ],
  ...
}
```

Query a specific organizational unit:

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--request GET \
"http://localhost:8080/openidm/system/aws/__ORGUNIT__/ou-2g8u-jvpza68y"
```

Response

```json
{
  "_id": "ou-2g8u-jvpza68y",
  "OrganizationalUnits": [
    {
      "Arn": "arn:aws:organizations::470686885243:ou/o-r7bvsqr1wd/ou-2g8u-kgsw9s1e",
      "Name": "1-Sandboxchild"
    }
  ],
  "__NAME__": "Sandbox",
  "ParentId": "ou-2g8u-jvpza68y"
}
```

## OpenICF Interfaces Implemented by the AWS Connector

The AWS Connector implements the following OpenICF interfaces. For additional details, see [ICF interfaces](interfaces.html):

* Create

  Creates an object and its `uid`.

* Delete

  Deletes an object, referenced by its `uid`.

* Schema

  Describes the object types, operations, and options that the connector supports.

* Script on Connector

  Enables an application to run a script in the context of the connector.

  Any script that runs on the connector has the following characteristics:

  * The script runs in the same execution environment as the connector and has access to all the classes to which the connector has access.

  * The script has access to a `connector` variable that is equivalent to an initialized instance of the connector. At a minimum, the script can access the connector configuration.

  * The script has access to any script arguments passed in by the application.

* Search

  Searches the target resource for all objects that match the specified object class and filter.

* Test

  Tests the connector configuration.

  Testing a configuration checks all elements of the environment that are referred to by the configuration are available. For example, the connector might make a physical connection to a host that is specified in the configuration to verify that it exists and that the credentials that are specified in the configuration are valid.

  This operation might need to connect to a resource, and, as such, might take some time. Do not invoke this operation too often, such as before every provisioning operation. The test operation is not intended to check that the connector is alive (that is, that its physical connection to the resource has not timed out).

  You can invoke the test operation before a connector configuration has been validated.

* Update

  Updates (modifies or replaces) objects on a target resource.

[]()

## AWS Connector Configuration

The AWS Connector has the following configurable properties:

### Basic Configuration Properties

| Property                                                       | Type            | Default | Encrypted(1)             | Required(2)               |
| -------------------------------------------------------------- | --------------- | ------- | ------------------------ | ------------------------- |
| `accessKeyId`                                                  | `String`        | `null`  |                          | [icon: check, set=fas]Yes |
| Provides the Access Key ID to access the AWS IAM Service API.  |                 |         |                          |                           |
| `secretKey`                                                    | `GuardedString` | `null`  | [icon: lock, set=fas]Yes | [icon: check, set=fas]Yes |
| Provides the Secret Key ID to access the AWS IAM Service API.  |                 |         |                          |                           |
| `roleArn`                                                      | `String`        | `null`  |                          | [icon: check, set=fas]Yes |
| Provides the Amazon Resource Name specifying the Role.         |                 |         |                          |                           |
| `region`                                                       | `String`        | `null`  |                          | [icon: times, set=fas]No  |
| Provides the Regions.                                          |                 |         |                          |                           |
| `pageSize`                                                     | `int`           | `100`   |                          | [icon: times, set=fas]No  |
| Provides the Page Size.                                        |                 |         |                          |                           |
| `credentialsExpiration`                                        | `int`           | `3600`  |                          | [icon: times, set=fas]No  |
| Provides the temporary credentials expiration time in seconds. |                 |         |                          |                           |
| `parentId`                                                     | `String`        | `null`  |                          | [icon: times, set=fas]No  |
| Provides the Parent ID to access the Organization Service.     |                 |         |                          |                           |
| `userName`                                                     | `String`        | `null`  |                          | [icon: times, set=fas]No  |
| Provides the UserName to access the Inline policy of a User.   |                 |         |                          |                           |
| `proxyHost`                                                    | `String`        | `null`  |                          | [icon: times, set=fas]No  |
| Provides the ProxyHost.                                        |                 |         |                          |                           |
| `proxyPort`                                                    | `Integer`       | `null`  |                          | [icon: times, set=fas]No  |
| Provides the ProxyPort.                                        |                 |         |                          |                           |
| `proxyUsername`                                                | `String`        | `null`  |                          | [icon: times, set=fas]No  |
| Provides the Proxy Username.                                   |                 |         |                          |                           |
| `proxyPassword`                                                | `GuardedString` | `null`  |                          | [icon: times, set=fas]No  |
| Provides the Proxy Password.                                   |                 |         |                          |                           |
| `connectionTimeout`                                            | `Integer`       | `10000` |                          | [icon: times, set=fas]No  |
| Provides the Maximum Connection Timeout in milliseconds.       |                 |         |                          |                           |
| `maxConnections`                                               | `Integer`       | `10`    |                          | [icon: times, set=fas]No  |
| Provides the number of Maximum Connections.                    |                 |         |                          |                           |

(1) Whether the property value is considered confidential, and is therefore encrypted in IDM.

(2) A list of operations in this column indicates that the property is required for those operations.

---

---
title: Application permissions (MS Graph API)
description: How to add and remove application permissions (app role assignments) for the MS Graph API connector using PingIDM REST calls
component: openicf
page_id: openicf:connector-reference:msgraph-app-perms
canonical_url: https://docs.pingidentity.com/openicf/connector-reference/msgraph-app-perms.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  msgraph-add-appRoleAssignment-servicePrincipal: Add an app role assignment to a servicePrincipal
  msgraph-remove-appRoleAssignment-servicePrincipal: Remove an app role assignment from a servicePrincipal
  msgraph-add-appRoleAssignment-principal: Add an app role to a principal (user/group/servicePrincipal) via a servicePrincipal
  msgraph-remove-appRoleAssignment-principal: Remove an app role from a principal (user/group/servicePrincipal) via a servicePrincipal
---

# Application permissions (MS Graph API)

Application permissions are also known as *app roles* or *app role assignments*. You can grant application permissions directly by adding an app role assignment to an object, such as user, group, or `servicePrincipal`. For more information about app role assignments, refer to the [Microsoft Graph documentation](https://learn.microsoft.com/en-us/graph/api/resources/approleassignment?view=graph-rest-1.0).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The following table displays what the different id's involved in app role assignment represent:principalId&#xA;&#xA;&#x9;&#xA;&#xA;The id of a user, group, or client servicePrincipal. Depends on the type of object receiving the app role assignment.&#xA;&#xA;&#xA;&#xA;&#xA;resourceId&#xA;&#xA;&#x9;&#xA;&#xA;The object id of the servicePrincipal containing the appRole.&#xA;&#xA;&#xA;&#xA;&#xA;appRoleId&#xA;&#xA;&#x9;&#xA;&#xA;The id of the appRole. |

Special schema definitions for app role assignments

The following schema definitions are special attributes in the connector, not real, readable properties of a `servicePrincipal` or other directory objects. They allow the connector to add and remove the respective app role assignments that appear in their related relationship fields.

For example, `__addAppRoleAssignments__` stores a list of object data to populate the *actual* attribute `appRoleAssignments`.

\_\_addAppRoleAssignments\_\_

```json
{
  "type": "array",
  "items": {
    "type": "object",
    "nativeType": "object"
  },
  "nativeName": "__addAppRoleAssignments__",
  "nativeType": "object"
}
```

\_\_removeAppRoleAssignments\_\_

```json
{
  "type": "array",
  "items": {
    "type": "string",
    "nativeType": "string"
  },
  "nativeName": "__removeAppRoleAssignments__",
  "nativeType": "string"
}
```

\_\_addAppRoleAssignedTo\_\_

```json
{
  "type": "array",
  "items": {
    "type": "object",
    "nativeType": "object"
  },
  "nativeName": "__addAppRoleAssignedTo__",
  "nativeType": "object"
}
```

\_\_removeAppRoleAssignedTo\_\_

```json
{
  "type": "array",
  "items": {
    "type": "string",
    "nativeType": "string"
  },
  "nativeName": "__removeAppRoleAssignedTo__",
  "nativeType": "string"
}
```

## Add an app role assignment to a `servicePrincipal`

|   |                                                 |
| - | ----------------------------------------------- |
|   | This process is identical for users and groups. |

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--header "If-Match: *" \
--request PUT \
--data '{
  "__addAppRoleAssignments__": {
    "principalId": "05b49121-0bf5-479e-8a4e-140212648879",
    "resourceId": "b3e4e58e-16fa-4b3d-a7b5-f134b7387e62",
    "appRoleId": "df021288-bdef-4463-88db-98f22de89214"
  }
}' \
"http://localhost:8080/openidm/system/azuread/servicePrincipal/05b49121-0bf5-479e-8a4e-140212648879"
```

Response

```json
{
  "_id": "05b49121-0bf5-479e-8a4e-140212648879",
  "addIns": [],
  "replyUrls": [],
  "keyCredentials": [],
  "oauth2PermissionScopes": [],
  "displayName": "Test-Application",
  "appRoleAssignments": [
    {
      "resourceDisplayName": "Microsoft Graph",
      "resourceId": "b3e4e58e-16fa-4b3d-a7b5-f134b7387e62",
      "principalDisplayName": "Test-Application",
      "appRoleId": "df021288-bdef-4463-88db-98f22de89214",
      "createdDateTime": "2023-05-05T20:41:15.373168300Z",
      "principalId": "05b49121-0bf5-479e-8a4e-140212648879",
      "id": "IZG0BfULnkeKThQCEmSIeS7n5ay2n99BiFNwyj97w8Y",
      "principalType": "ServicePrincipal"
    }
  ],
  "alternativeNames": [],
  "resourceSpecificApplicationPermissions": [],
  "appDisplayName": "Test-Application",
  "accountEnabled": true,
  "appOwnerOrganizationId": "9e91bf24-7a08-433e-b111-5542416b4f20",
  "passwordCredentials": [],
  "servicePrincipalNames": [
    "93dd36a4-61ca-4a1d-89cf-eac96587de35"
  ],
  "appId": "93dd36a4-61ca-4a1d-89cf-eac96587de35",
  "signInAudience": "AzureADandPersonalMicrosoftAccount",
  "notificationEmailAddresses": [],
  "servicePrincipalType": "Application",
  "tags": [],
  "appRoleAssignedTo": [],
  "info": {},
  "appRoles": [],
  "appRoleAssignmentRequired": false
}
```

## Remove an app role assignment from a `servicePrincipal`

|   |                                                 |
| - | ----------------------------------------------- |
|   | This process is identical for users and groups. |

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--header "If-Match: *" \
--request PUT \
--data '{
  "__removeAppRoleAssignments__": "IZG0BfULnkeKThQCEmSIeS7n5ay2n99BiFNwyj97w8Y"
}' \
"http://localhost:8080/openidm/system/azuread/servicePrincipal/05b49121-0bf5-479e-8a4e-140212648879"
```

Response

```json
{
  "_id": "05b49121-0bf5-479e-8a4e-140212648879",
  "addIns": [],
  "replyUrls": [],
  "keyCredentials": [],
  "oauth2PermissionScopes": [],
  "displayName": "Test-Application",
  "appRoleAssignments": [],
  "alternativeNames": [],
  "resourceSpecificApplicationPermissions": [],
  "appDisplayName": "Test-Application",
  "accountEnabled": true,
  "appOwnerOrganizationId": "9e91bf24-7a08-433e-b111-5542416b4f20",
  "passwordCredentials": [],
  "servicePrincipalNames": [
    "93dd36a4-61ca-4a1d-89cf-eac96587de35"
  ],
  "appId": "93dd36a4-61ca-4a1d-89cf-eac96587de35",
  "signInAudience": "AzureADandPersonalMicrosoftAccount",
  "notificationEmailAddresses": [],
  "servicePrincipalType": "Application",
  "tags": [],
  "appRoleAssignedTo": [],
  "info": {},
  "appRoles": [],
  "appRoleAssignmentRequired": false
}
```

## Add an app role to a principal (user/group/servicePrincipal) via a `servicePrincipal`

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--header "If-Match: *" \
--request PUT \
--data '{
  "__addAppRoleAssignedTo__": {
    "principalId": "87f5b3f8-6a8c-4e50-8fd6-0467d5e97e0c",
    "resourceId": "bf960539-a1d8-4eab-a46e-e9ce0b3f15c8",
    "appRoleId": "00000000-0000-0000-0000-000000000000"
  }
}' \
"http://localhost:8080/openidm/system/azuread/servicePrincipal/bf960539-a1d8-4eab-a46e-e9ce0b3f15c8"
```

Response

```json
{
  "_id": "bf960539-a1d8-4eab-a46e-e9ce0b3f15c8",
  "addIns": [],
  "replyUrls": [],
  "keyCredentials": [],
  "oauth2PermissionScopes": [],
  "displayName": "Test-Application",
  "appRoleAssignments": [],
  "alternativeNames": [],
  "resourceSpecificApplicationPermissions": [],
  "appDisplayName": "Test-Application",
  "accountEnabled": true,
  "appOwnerOrganizationId": "9e91bf24-7a08-433e-b111-5542416b4f20",
  "passwordCredentials": [],
  "servicePrincipalNames": [
    "62212657-8f49-40b3-874b-9d1c25cb4388"
  ],
  "appId": "62212657-8f49-40b3-874b-9d1c25cb4388",
  "signInAudience": "AzureADandPersonalMicrosoftAccount",
  "notificationEmailAddresses": [],
  "servicePrincipalType": "Application",
  "tags": [],
  "appRoleAssignedTo": [
    {
      "resourceDisplayName": "Test-Application",
      "resourceId": "bf960539-a1d8-4eab-a46e-e9ce0b3f15c8",
      "principalDisplayName": "qcmozfwwygkebie",
      "appRoleId": "00000000-0000-0000-0000-000000000000",
      "createdDateTime": "2023-05-05T20:41:25.405071800Z",
      "principalId": "87f5b3f8-6a8c-4e50-8fd6-0467d5e97e0c",
      "id": "-LP1h4xqUE6P1gRn1el-DCzqXtqJH6NBt0Fr0lT0g2g",
      "principalType": "User"
    }
  ],
  "info": {},
  "appRoles": [],
  "appRoleAssignmentRequired": false
}
```

## Remove an app role from a principal (user/group/servicePrincipal) via a `servicePrincipal`

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--header "If-Match: *" \
--request PUT \
--data '{
  "__removeAppRoleAssignedTo__": "-LP1h4xqUE6P1gRn1el-DCzqXtqJH6NBt0Fr0lT0g2g"
}' \
"http://localhost:8080/openidm/system/azuread/servicePrincipal/bf960539-a1d8-4eab-a46e-e9ce0b3f15c8"
```

Response

```json
{
  "_id": "bf960539-a1d8-4eab-a46e-e9ce0b3f15c8",
  "addIns": [],
  "replyUrls": [],
  "keyCredentials": [],
  "oauth2PermissionScopes": [],
  "displayName": "Test-Application",
  "appRoleAssignments": [],
  "alternativeNames": [],
  "resourceSpecificApplicationPermissions": [],
  "appDisplayName": "Test-Application",
  "accountEnabled": true,
  "appOwnerOrganizationId": "9e91bf24-7a08-433e-b111-5542416b4f20",
  "passwordCredentials": [],
  "servicePrincipalNames": [
    "62212657-8f49-40b3-874b-9d1c25cb4388"
  ],
  "appId": "62212657-8f49-40b3-874b-9d1c25cb4388",
  "signInAudience": "AzureADandPersonalMicrosoftAccount",
  "notificationEmailAddresses": [],
  "servicePrincipalType": "Application",
  "tags": [],
  "appRoleAssignedTo": [],
  "info": {},
  "appRoles": [],
  "appRoleAssignmentRequired": false
}
```

---

---
title: Applications (MS Graph API)
description: How to query, read, create, update, delete, and add client secrets to Azure AD applications using the MS Graph API connector
component: openicf
page_id: openicf:connector-reference:msgraph-applications
canonical_url: https://docs.pingidentity.com/openicf/connector-reference/msgraph-applications.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  msgraph-query-all-apps: Query all applications
  msgraph-read-app: Read an application
  msgraph-create-app: Create an application
  msgraph-add-pass-secret-app: Add a password (client secret) to an application
  msgraph-update-app: Update an application
  msgraph-delete-app: Delete an application
---

# Applications (MS Graph API)

The MS Graph API connector lets you read and manage applications.

## Query all applications

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"http://localhost:8080/openidm/system/azuread/application?_queryFilter=true"
```

## Read an application

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"http://localhost:8080/openidm/system/azuread/application/e2dcfa77-5222-4715-a043-98baac00683d"
```

Response

```json
{
  "_id": "e2dcfa77-5222-4715-a043-98baac00683d",
  "tags": [],
  "spa": {
    "redirectUris": []
  },
  "parentalControlSettings": {
    "legalAgeGroupRule": "Allow",
    "countriesBlockedForMinors": []
  },
  "api": {
    "requestedAccessTokenVersion": 2,
    "knownClientApplications": [],
    "oauth2PermissionScopes": [],
    "preAuthorizedApplications": []
  },
  "passwordCredentials": [],
  "info": {},
  "addIns": [],
  "keyCredentials": [],
  "publicClient": {
    "redirectUris": []
  },
  "verifiedPublisher": {},
  "identifierUris": [],
  "web": {
    "implicitGrantSettings": {
      "enableAccessTokenIssuance": false,
      "enableIdTokenIssuance": false
    },
    "redirectUris": []
  },
  "publisherDomain": "example.com",
  "createdDateTime": "2023-05-05T20:40:02Z",
  "displayName": "Test-Application",
  "appRoles": [],
  "isDeviceOnlyAuthSupported": false,
  "appId": "bc146d82-be72-4e16-814d-76e977ad198e",
  "signInAudience": "AzureADandPersonalMicrosoftAccount",
  "requiredResourceAccess": [
    {
      "resourceAppId": "00000002-0000-0000-c000-000000000000",
      "resourceAccess": [
        {
          "id": "311a71cc-e848-46a1-bdf8-97ff7156d8e6",
          "type": "Scope"
        }
      ]
    }
  ]
}
```

## Create an application

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request POST \
--data '{
  "displayName": "Test-Application",
  "requiredResourceAccess": [
    {
      "resourceAppId": "00000002-0000-0000-c000-000000000000",
      "resourceAccess": [
        {
          "id": "311a71cc-e848-46a1-bdf8-97ff7156d8e6",
          "type": "Scope"
        }
      ]
    }
  ]
}' \
"http://localhost:8080/openidm/system/azuread/application"
```

Response

```json
{
  "_id": "e2dcfa77-5222-4715-a043-98baac00683d",
  "tags": [],
  "spa": {
    "redirectUris": []
  },
  "parentalControlSettings": {
    "legalAgeGroupRule": "Allow",
    "countriesBlockedForMinors": []
  },
  "api": {
    "requestedAccessTokenVersion": 2,
    "knownClientApplications": [],
    "oauth2PermissionScopes": [],
    "preAuthorizedApplications": []
  },
  "passwordCredentials": [],
  "info": {},
  "addIns": [],
  "keyCredentials": [],
  "publicClient": {
    "redirectUris": []
  },
  "verifiedPublisher": {},
  "identifierUris": [],
  "web": {
    "implicitGrantSettings": {
      "enableAccessTokenIssuance": false,
      "enableIdTokenIssuance": false
    },
    "redirectUris": []
  },
  "publisherDomain": "example.com",
  "createdDateTime": "2023-05-05T20:40:02Z",
  "displayName": "Test-Application",
  "appRoles": [],
  "isDeviceOnlyAuthSupported": false,
  "appId": "bc146d82-be72-4e16-814d-76e977ad198e",
  "signInAudience": "AzureADandPersonalMicrosoftAccount",
  "requiredResourceAccess": [
    {
      "resourceAppId": "00000002-0000-0000-c000-000000000000",
      "resourceAccess": [
        {
          "id": "311a71cc-e848-46a1-bdf8-97ff7156d8e6",
          "type": "Scope"
        }
      ]
    }
  ]
}
```

## Add a password (client secret) to an application

Adding `passwordCredential` when creating applications is not supported. You must use the `addPassword` method to add passwords or secrets to an application.

Some actions require more than a UUID on return and have no object to follow up with a subsequent read. In this instance, you can use the `scriptOnConnector` action, which requires at least the `builtinAction` parameter. Adding client secrets using this method requires the parameter `builtinAction=addPassword`. You can learn more about the other required parameter `applicationId` and optional parameters in the [Microsoft Graph documentation](https://learn.microsoft.com/en-us/graph/api/application-addpassword?view=graph-rest-1.0\&tabs=java).

The above also requires a *dummy* system action. For example:

```json
{
  "scriptId": "addPassword",
  "actions": [
    {
      "systemType": ".*MSGraphAPIConnector",
      "actionSource": "return;",
      "actionType": "Groovy"
    }
  ]
}
```

The `actionSource` is ignored for these `builtIn` requests, but still required to invoke the `scriptOnConnector` action.

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request POST \
"http://localhost:8080/openidm/system/azuread/?_action=script&scriptId=addPassword&displayName=TestSecretGenesis&applicationId=f619a0ac-0548-4e90-9314-84d967088d2b&builtinAction=addPassword"
```

Response

```json
{
  "actions": [
    {
      "result": {
        "secretText": "{GENERATED-CLIENT-SECRET}",
        "startDateTime": {
          "dateTime": {
            "date": {
              "month": 5,
              "year": 2023,
              "day": 5
            },
            "time": {
              "hour": 20,
              "nano": 771787000,
              "minute": 40,
              "second": 27
            }
          },
          "offset": {
            "totalSeconds": 0
          }
        },
        "displayName": "TestSecretGenesis",
        "hint": "LS8",
        "keyId": "8f48fb5e-a295-4969-b988-a723a02f2f28",
        "endDateTime": {
          "dateTime": {
            "date": {
              "month": 5,
              "year": 2025,
              "day": 5
            },
            "time": {
              "hour": 20,
              "nano": 771787000,
              "minute": 40,
              "second": 27
            }
          },
          "offset": {
            "totalSeconds": 0
          }
        }
      }
    }
  ]
}
```

## Update an application

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request PATCH \
--data '[
  {
    "operation": "replace",
    "field": "/displayName",
    "value": "Test-Application-Updated"
  }
]' \
"http://localhost:8080/openidm/system/azuread/application/4eff1242-bd95-463b-9c8c-f221ec489ba1"
```

Response

```json
{
  "_id": "4eff1242-bd95-463b-9c8c-f221ec489ba1",
  "tags": [],
  "spa": {
    "redirectUris": []
  },
  "parentalControlSettings": {
    "legalAgeGroupRule": "Allow",
    "countriesBlockedForMinors": []
  },
  "api": {
    "requestedAccessTokenVersion": 2,
    "knownClientApplications": [],
    "oauth2PermissionScopes": [],
    "preAuthorizedApplications": []
  },
  "passwordCredentials": [],
  "info": {},
  "addIns": [],
  "keyCredentials": [],
  "publicClient": {
    "redirectUris": []
  },
  "verifiedPublisher": {},
  "identifierUris": [],
  "web": {
    "implicitGrantSettings": {
      "enableAccessTokenIssuance": false,
      "enableIdTokenIssuance": false
    },
    "redirectUris": []
  },
  "publisherDomain": "example.com",
  "createdDateTime": "2023-05-05T20:40:11Z",
  "displayName": "Test-Application-Updated",
  "appRoles": [],
  "appId": "68e06ad2-569f-407d-b117-6cc1d9f5d787",
  "signInAudience": "AzureADandPersonalMicrosoftAccount",
  "requiredResourceAccess": []
}
```

## Delete an application

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--header "If-Match: *" \
--request DELETE \
"http://localhost:8080/openidm/system/azuread/application/579d5781-6e39-4b94-b741-1748d1e14199"
```

Response

```json
{
  "_id": "579d5781-6e39-4b94-b741-1748d1e14199",
  "tags": [],
  "spa": {
    "redirectUris": []
  },
  "parentalControlSettings": {
    "legalAgeGroupRule": "Allow",
    "countriesBlockedForMinors": []
  },
  "api": {
    "requestedAccessTokenVersion": 2,
    "knownClientApplications": [],
    "oauth2PermissionScopes": [],
    "preAuthorizedApplications": []
  },
  "passwordCredentials": [],
  "info": {},
  "addIns": [],
  "keyCredentials": [],
  "publicClient": {
    "redirectUris": []
  },
  "verifiedPublisher": {},
  "identifierUris": [],
  "web": {
    "implicitGrantSettings": {
      "enableAccessTokenIssuance": false,
      "enableIdTokenIssuance": false
    },
    "redirectUris": []
  },
  "publisherDomain": "example.com",
  "createdDateTime": "2023-05-05T20:40:18Z",
  "displayName": "Test-Application",
  "appRoles": [],
  "appId": "6e26b7a3-53ef-45ea-8492-fed30f1dd2ad",
  "signInAudience": "AzureADandPersonalMicrosoftAccount",
  "requiredResourceAccess": []
}
```

---

---
title: AS400 connector
description: "Reference for the AS400 connector: install, configure, and use it to manage and synchronize users and groups between AS400 and PingIDM"
component: openicf
page_id: openicf:connector-reference:as400
canonical_url: https://docs.pingidentity.com/openicf/connector-reference/as400.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  before_you_start: Before you start
  install_the_as400_connector: Install the AS400 connector
  configure_the_as400_connector: Configure the AS400 connector
  test_the_as400_connector: Test the AS400 connector
  as400_remote_connector: AS400 remote connector
  config-connection-pooling-as400: Configure connection pooling
  supported_resource_types: Supported resource types
  supported_search_filters: Supported search filters
  attributes: Attributes
  use_the_as400_connector: Use the AS400 connector
  as400-users: Users
  as400-groups: Groups
  implemented-interfaces-org-forgerock-openicf-connectors-as400-As400Connector-1.5.20.33: OpenICF Interfaces Implemented by the AS400 Connector
  config-properties-org-forgerock-openicf-connectors-as400-As400Connector-1.5.20.33: AS400 Connector Configuration
  configuration-properties-org-forgerock-openicf-connectors-as400-As400Connector-1.5.20.33: Configuration properties
  basic-configuration-properties-org-forgerock-openicf-connectors-as400-As400Connector-1.5.20.33: Basic Configuration Properties
---

# AS400 connector

You can use the AS400 connector to manage and synchronize users between AS400 and IDM or Advanced Identity Cloud.

## Before you start

These instructions assume you have an AS400 administrator account and you have access to AS400. You need the following information to configure the connector:

* Host Name

  The name or IP address of the host where AS400 is running.

* Username

  The AS400 Organizational Admin username.

* Password

  The AS400 Organizational Admin password.

* Is Secure

  Whether to enable a secure connection to AS400.

## Install the AS400 connector

|   |                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To check for an Advanced Identity Cloud application for this connector, refer to:- [Application management](https://docs.pingidentity.com/pingoneaic/latest/app-management/applications.html)

- [App catalog](https://docs.pingidentity.com/pingoneaic/latest/app-management/app-catalog.html) |

You can download most connectors from [Backstage](https://backstage.forgerock.com/downloads/browse/idm/featured/connectors), but some are included in the default deployment for Advanced Identity Cloud, IDM, or RCS. When using an included connector, you can skip installing it and move directly to configuration.

**Connector included in default deployment**

| Connector           | IDM                     | RCS                      |
| ------------------- | ----------------------- | ------------------------ |
| [AS400](as400.html) | [icon: times, set=fa]No | [icon: check, set=fa]Yes |

Download the connector .jar file from [Backstage](https://backstage.forgerock.com/downloads/browse/idm/featured/connectors).

* If you're running the connector locally, place it in the `/path/to/openidm/connectors` directory, for example:

  ```
  mv ~/Downloads/as400-connector-1.5.20.33.jar /path/to/openidm/connectors/
  ```

* If you're using a remote connector server (RCS), place it in the `/path/to/openicf/connectors` directory on the RCS.

## Configure the AS400 connector

Create a connector configuration using the IDM admin UI:

1. From the navigation bar, click Configure > Connectors.

2. On the Connectors page, click New Connector.

3. On the New Connector page, type a Connector Name.

4. From the Connector Type list, select AS400 Connector - 1.5.20.33.

5. Complete the Base Connector Details and any applicable Additional Options.

   |   |                                                                                                                  |
   | - | ---------------------------------------------------------------------------------------------------------------- |
   |   | For a list of all configuration properties, refer to [AS400 Connector Configuration](#as400-config-prop-ezLink). |

6. Click Save.

When your connector is configured correctly, the connector displays as Active in the admin UI.

Refer to [this procedure](configure-connector.html#connector-wiz-REST) to create a connector configuration over REST.

### Test the AS400 connector

Test that the configuration is correct by running the following command:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
"http://localhost:8080/openidm/system/as400?_action=test"
{
  "name": "as400",
  "enabled": true,
  "config" : "config/provisioner.openicf/as400",
  "connectorRef": {
    "bundleVersion": "[1.5.0.0,1.6.0.0)",
    "bundleName": "org.forgerock.openicf.connectors.as400-connector",
    "connectorName": "org.forgerock.openicf.connectors.as400.As400Connector"
  },
  "displayName": "AS400 Connector",
  "objectTypes": [
    "__ACCOUNT__",
    "__ALL__",
    "__GROUP__"
  ],
  "ok": true
}
```

If the command returns `"ok": true`, your connector has been configured correctly and can authenticate to the AS400 system.

### AS400 remote connector

If you want to run this connector outside of PingOne Advanced Identity Cloud or IDM, you can configure the AS400 connector as a remote connector. Java Connectors installed remotely on a Java Connector Server function identically to those bundled locally within PingOne Advanced Identity Cloud or installed locally on IDM.

Refer to [Remote connectors](remote-connector.html) for configuring the AS400 remote connector.

### Configure connection pooling

The AS400 connector uses a [non-poolable mechanism](pooling.html#non-poolable-connectors) to manage connections. Learn more about the different pooling mechanisms in [Connectors by pooling mechanism](pooling.html#pooling-table).

## Supported resource types

The AS400 connector supports the following resources:

| ICF Native Type | AS400 Resource Type |
| --------------- | ------------------- |
| `__ACCOUNT__`   | Users               |
| `__GROUP__`     | Groups              |

## Supported search filters

The AS400 connector supports search operations with the following filter operators and attributes:

| Object Type | Operators | Attributes |
| ----------- | --------- | ---------- |
| `__GROUP__` | id filter | `Id`       |

## Attributes

The AS400 connector supports the following account attributes:

| Attribute                   | Description                                                                                                                                                              |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `USPRF`                     | User Profile Name                                                                                                                                                        |
| `PASSWORD`                  | The password used to log in.                                                                                                                                             |
| `PreviousSignOn`            | The previous sign-on date.                                                                                                                                               |
| `PasswordChangedDate`       | The last date the password was changed.                                                                                                                                  |
| `IsPasswordNone`            | Whether or not the password is \*NONE.                                                                                                                                   |
| `UserExpirationAction`      | The user expiration action.                                                                                                                                              |
| `StorageUsed`               | The storage used.                                                                                                                                                        |
| `ObjectAuditValue`          | A value used for auditing the object.                                                                                                                                    |
| `ActionAuditLevel`          | The Action Audit Level.                                                                                                                                                  |
| `PWDEXP`                    | When the user's password is set to expire.                                                                                                                               |
| `STATUS`                    | The user's status. Permitted values are `enable` and `disable`.                                                                                                          |
| `USRCLS`                    | The special access control for the user.                                                                                                                                 |
| `ASTLVL`                    | Specifies which user interface to use.                                                                                                                                   |
| `CURLIB`                    | Specifies the name of the current library associated with the job.                                                                                                       |
| `INLPGM`                    | The initial program.                                                                                                                                                     |
| `INLMNU`                    | The initial menu.                                                                                                                                                        |
| `IsUserEntitlementRequired` | Whether or not user entitlement is required.                                                                                                                             |
| `IsAuthCollectionActive`    | Whether or not authority collection is active.                                                                                                                           |
| `MTCPB`                     | Limit capabilities.                                                                                                                                                      |
| `TEXT`                      | A free-form text field.                                                                                                                                                  |
| `SPCAUT`                    | The special access permissions for the user.                                                                                                                             |
| `SPCENV`                    | The special environment.                                                                                                                                                 |
| `DSPSGNINF`                 | The display sign-on information.                                                                                                                                         |
| `PWDEXPITV`                 | The password expiration interval.                                                                                                                                        |
| `PWDCHGBLK`                 | Whether or not to block password change.                                                                                                                                 |
| `LCLPWDMGT`                 | Local password management.                                                                                                                                               |
| `LMTDEVSSN`                 | Limit device session.                                                                                                                                                    |
| `KBDBUF`                    | Keyboard buffering.                                                                                                                                                      |
| `MAXSTG`                    | Maximum allowed storage.                                                                                                                                                 |
| `PTYLMT`                    | Highest schedule priority.                                                                                                                                               |
| `JOBD`                      | Job description.                                                                                                                                                         |
| `OWNER`                     | The owner of the user profile.                                                                                                                                           |
| `ACGCDE`                    | The accounting code.                                                                                                                                                     |
| `DOCPWD`                    | The document password.                                                                                                                                                   |
| `MSGQ`                      | The message queue.                                                                                                                                                       |
| `DLVRY`                     | Delivery.                                                                                                                                                                |
| `SEV`                       | The severity code.                                                                                                                                                       |
| `PRTDEV`                    | The print device.                                                                                                                                                        |
| `OUTQ`                      | The output queue.                                                                                                                                                        |
| `ATNPGM`                    | The attention program.                                                                                                                                                   |
| `SRTSEQ`                    | The sort sequence.                                                                                                                                                       |
| `LANGID`                    | The language ID.                                                                                                                                                         |
| `CNTRYID`                   | The country or region ID.                                                                                                                                                |
| `CCSID`                     | The Coded Character Set ID.                                                                                                                                              |
| `CHRIDCTL`                  | The character identifier control.                                                                                                                                        |
| `SETJOBATR`                 | The local job attributes.                                                                                                                                                |
| `LOCALE`                    | The locale.                                                                                                                                                              |
| `USROPT`                    | The user options.                                                                                                                                                        |
| `UID`                       | The user ID number.                                                                                                                                                      |
| `HOMEDIR`                   | The home directory.                                                                                                                                                      |
| `USREXPDATE`                | The user's expiration date.                                                                                                                                              |
| `USREXPITV`                 | The user's expiration interval.                                                                                                                                          |
| `AUT`                       | Authority.                                                                                                                                                               |
| `EIMASSOC`                  | The EIM association.                                                                                                                                                     |
| `PasswordExpireDate`        | The date the password expires.                                                                                                                                           |
| `GRPPRF`                    | Specifies the user's group profile name whose authority is used when there is no job-specific authority given to the user.                                               |
| `SUPGRPPRF`                 | Specifies the user's supplemental group profiles. Used with `GRPPRF` to determine what authority the user has when there is no job-specific authority given to the user. |

## Use the AS400 connector

The AS400 connector can perform the following actions:

### Users

> **Collapse: Create an AS400 user**
>
> The following example creates a user with all available attributes:
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Content-Type: application/json"\
> --request POST \
> --data "{
>   "__NAME__":"BJENSEN",
>   "__PASSWORD__":"ASDE1234",
>   "PWDEXP":false,
>   "__ENABLE__":true,
>   "USRCLS":"*USER",
>   "ASTLVL":"*BASIC",
>   "CURLIB":"*CRTDFT",
>   "INLPGM":"*NONE",
>   "INLMNU":"MAIN",
>   "TEXT":"TEXTFILEDVALUE",
>   "SPCAUT":["*AUDIT"],
>   "SPCENV":"*S36",
>   "DSPSGNINF":"*YES",
>   "PWDEXPITV":"323",
>   "PWDCHGBLK":"93",
>   "LCLPWDMGT":true,
>   "LMTDEVSSN":"*NO",
>   "MAXSTG":"10000",
>   "PTYLMT":8,
>   "JOBD":"QDFTJOBD",
>   "OWNER":"*USRPRF",
>   "ACGCDE":"*BLANK",
>   "DOCPWD":"W12345",
>   "MSGQ":"*USRPRF",
>   "DLVRY":"*HOLD",
>   "SEV":"50",
>   "PRTDEV":"*SYSVAL",
>   "OUTQ":"*DEV",
>   "ATNPGM":"*ASSIST",
>   "SRTSEQ":"*HEX",
>   "LANGID":"ENG",
>   "CCSID":"*HEX",
>   "CHRIDCTL":"*DEVD",
>   "SETJOBATR":["*CCSID"],
>   "LOCALE":"*C",
>   "USROPT":["*HLPFULL"],
>   "UID":"*GEN",
>   "HOMEDIR":"*USRPRF",
>   "EIMASSOC":["*NOCHG"],
>   "USREXPITV":99,
>   "USREXPDATE":"*USREXPITV",
>   "LMTCPB":"*YES",
>   "CNTRYID":"*SYSVAL",
>   "GRPPRF":"AZURE",
>   "SUPGRPPRF":["AWS"]
> }" \
> "https://localhost:8443/openidm/system/as400/__ACCOUNT__?_action=create&_prettyprint=true"
> {
>   "_id" : "BJENSEN",
>   "USROPT" : [ "*HLPFULL" ],
>   "SEV" : "50",
>   "USREXPITV" : 99,
>   "IsAuthCollectionActive" : false,
>   "HOMEDIR" : "/home/BJENSEN",
>   "MAXSTG" : "10000",
>   "UID" : "1277",
>   "PTYLMT" : 8,
>   "__NAME__" : "BJENSEN",
>   "PRTDEV" : "*SYSVAL",
>   "__ENABLE__" : true,
>   "LMTDEVSSN" : "*NO",
>   "__UID__" : "BJENSEN",
>   "SRTSEQ" : "*HEX",
>   "DSPSGNINF" : "*YES",
>   "PWDCHGBLK" : "93",
>   "GRPPRF" : "AZURE",
>   "USREXPDATE" : "12/06/22",
>   "CURLIB" : "*CRTDFT",
>   "LMTCPB" : "*YES",
>   "ASTLVL" : "*BASIC",
>   "SUPGRPPRF" : [ "AWS" ],
>   "MSGQ" : "/QSYS.LIB/QUSRSYS.LIB/BJENSEN.MSGQ",
>   "LANGID" : "ENG",
>   "CCSID" : "65535",
>   "PWDEXPITV" : "323",
>   "IsUserEntitlementRequired" : true,
>   "TEXT" : "TEXTFILEDVALUE",
>   "JOBD" : "/QSYS.LIB/QGPL.LIB/QDFTJOBD.JOBD",
>   "ActionAuditLevel" : "*BASIC",
>   "ObjectAuditValue" : "*NONE",
>   "PasswordChangedDate" : "Mon Aug 29 05:15:20 IST 2022",
>   "ATNPGM" : "/QSYS.LIB/QEZMAIN.PGM",
>   "LCLPWDMGT" : true,
>   "INLPGM" : "*NONE",
>   "USRCLS" : "*USER",
>   "SPCAUT" : [ "*AUDIT" ],
>   "SETJOBATR" : [ "*CCSID" ],
>   "SPCENV" : "*S36",
>   "ACGCDE" : "",
>   "IsPasswordNone" : false,
>   "DLVRY" : "*HOLD",
>   "IsAuthCollectionRepositoryExist" : false,
>   "UserExpirationAction" : "*DISABLE",
>   "INLMNU" : "/QSYS.LIB/%LIBL%.LIB/MAIN.MNU",
>   "LOCALE" : "*C",
>   "KBDBUF" : "*SYSVAL",
>   "OWNER" : "*USRPRF",
>   "PasswordExpireDate" : "Tue Jul 18 00:00:00 IST 2023",
>   "PWDEXP" : false,
>   "OUTQ" : "*DEV",
>   "CNTRYID" : "*SYSVAL",
>   "CHRIDCTL" : "*DEVD",
>   "StorageUsed" : "12"
> }
> ```
>
> |   |                                                                                                                                                                                                                                                                                                   |
> | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | When you create a new user, you must specify at least the `__NAME__` property. This property can be a maximum of 10 characters. These characters may be:- Any letter
>
> - Any digits
>
> - The #, $, \_, and @ special characters.If the `__NAME__` begins with a digit, it must be prefixed with a Q. |

> **Collapse: Query all users**
>
> The following example queries all users in the system:
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Content-Type: application/json" \
> --request GET \
> "http://localhost:8080/openidm/system/as400/__ACCOUNT__?_queryId=query-all-ids"
> {
>   "result": [
>     {"_id": "ADAM"},
>     {"_id": "BJENSEN"},
>     {"_id": "CHERYL"},
>     {"_id": "DAVID"},
>     {"_id": "EDDIE"}
>   ],
>   "resultCount":5,
>   "pagedResultsCookie":null,
>   "totalPagedResultsPolicy":"NONE",
>   "totalPagedResults":-1,
>   "remainingPagedResults":-1
> }
> ```

> **Collapse: Query a single user**
>
> The following example queries all users in the system:
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Content-Type: application/json" \
> --request GET \
> "http://localhost:8080/openidm/system/as400/__ACCOUNT__/BJENSEN?prettyprint=true"
> {
>   "_id" : "BJENSEN",
>   "USROPT" : [ "*HLPFULL" ],
>   "SEV" : "50",
>   "USREXPITV" : 99,
>   "IsAuthCollectionActive" : false,
>   "HOMEDIR" : "/home/BJENSEN",
>   "MAXSTG" : "10000",
>   "UID" : "1277",
>   "PTYLMT" : 8,
>   "__NAME__" : "BJENSEN",
>   "PRTDEV" : "*SYSVAL",
>   "__ENABLE__" : true,
>   "LMTDEVSSN" : "*NO",
>   "__UID__" : "BJENSEN",
>   "SRTSEQ" : "*HEX",
>   "DSPSGNINF" : "*YES",
>   "PWDCHGBLK" : "93",
>   "GRPPRF" : "AZURE",
>   "USREXPDATE" : "12/06/22",
>   "CURLIB" : "*CRTDFT",
>   "LMTCPB" : "*YES",
>   "ASTLVL" : "*BASIC",
>   "SUPGRPPRF" : [ "AWS" ],
>   "MSGQ" : "/QSYS.LIB/QUSRSYS.LIB/BJENSEN.MSGQ",
>   "LANGID" : "ENG",
>   "CCSID" : "65535",
>   "PWDEXPITV" : "323",
>   "IsUserEntitlementRequired" : true,
>   "TEXT" : "TEXTFILEDVALUE",
>   "JOBD" : "/QSYS.LIB/QGPL.LIB/QDFTJOBD.JOBD",
>   "ActionAuditLevel" : "*BASIC",
>   "ObjectAuditValue" : "*NONE",
>   "PasswordChangedDate" : "Mon Aug 29 05:15:20 IST 2022",
>   "ATNPGM" : "/QSYS.LIB/QEZMAIN.PGM",
>   "LCLPWDMGT" : true,
>   "INLPGM" : "*NONE",
>   "USRCLS" : "*USER",
>   "SPCAUT" : [ "*AUDIT" ],
>   "SETJOBATR" : [ "*CCSID" ],
>   "SPCENV" : "*S36",
>   "ACGCDE" : "",
>   "IsPasswordNone" : false,
>   "DLVRY" : "*HOLD",
>   "IsAuthCollectionRepositoryExist" : false,
>   "UserExpirationAction" : "*DISABLE",
>   "INLMNU" : "/QSYS.LIB/%LIBL%.LIB/MAIN.MNU",
>   "LOCALE" : "*C",
>   "KBDBUF" : "*SYSVAL",
>   "OWNER" : "*USRPRF",
>   "PasswordExpireDate" : "Tue Jul 18 00:00:00 IST 2023",
>   "PWDEXP" : false,
>   "OUTQ" : "*DEV",
>   "CNTRYID" : "*SYSVAL",
>   "CHRIDCTL" : "*DEVD",
>   "StorageUsed" : "12"
> }
> ```

> **Collapse: Modify a user**
>
> You can modify an existing user with a PUT request, including all attributes of the account in the request. You can use the AS400 connector to modify the following attributes:
>
> * `PASSWORD`
>
> * `PWDEXP`
>
> * `STATUS`
>
> * `USRCLS`
>
> * `ASTLVL`
>
> * `CURLIB`
>
> * `INLPGM`
>
> * `INLMNU`
>
> * `LMTCPB`
>
> * `TEXT`
>
> * `SPCAUT`
>
> * `SPCENV`
>
> * `DSPSGNINF`
>
> * `PWDEXPITV`
>
> * `PWDCHGBLK`
>
> * `LCLPWDMGT`
>
> * `LMTDEVSSN`
>
> * `KBDBUF`
>
> * `MAXSTG`
>
> * `PTYLMT`
>
> * `JOBD`
>
> * `OWNER`
>
> * `ACGCDE`
>
> * `DOCPWD`
>
> * `MSGQ`
>
> * `DLVRY`
>
> * `SEV`
>
> * `PRTDEV`
>
> * `OUTQ`
>
> * `ATNPGM`
>
> * `SRTSEQ`
>
> * `LANGID`
>
> * `CNTRYID`
>
> * `CCSID`
>
> * `CHRIDCTL`
>
> * `SETJOBATR`
>
> * `LOCALE`
>
> * `USROPT`
>
> * `UID`
>
> * `HOMEDIR`
>
> * `USREXPDATE`
>
> * `USREXPITV`
>
> * `EIMASSOC`
>
> * `GRPPRF`
>
> * `SUPGRPPRF`
>
> The following request updates a user:
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Content-Type: application/json" \
> --header "Accept-API-Version: resource=1.0" \
> --header "If-Match: *" \
> --request PUT \
> --data "{
>   "__PASSWORD__":"ASDE1234",
>   "PWDEXP":false,
>   "__ENABLE__":true,
>   "USRCLS":"*USER",
>   "ASTLVL":"*BASIC",
>   "CURLIB":"*CRTDFT",
>   "INLPGM":"*NONE",
>   "INLMNU":"MAIN",
>   "TEXT":"TEXTFILEDVALUE",
>   "SPCAUT":["*AUDIT"],
>   "SPCENV":"*S36",
>   "DSPSGNINF":"*YES",
>   "PWDEXPITV":"323",
>   "PWDCHGBLK":"93",
>   "LCLPWDMGT":true,
>   "LMTDEVSSN":"*NO",
>   "MAXSTG":"10000",
>   "PTYLMT":8,
>   "JOBD":"QDFTJOBD",
>   "OWNER":"*USRPRF",
>   "ACGCDE":"*BLANK",
>   "DOCPWD":"W12345",
>   "MSGQ":"*USRPRF",
>   "DLVRY":"*HOLD",
>   "SEV":"50",
>   "PRTDEV":"*SYSVAL",
>   "OUTQ":"*DEV",
>   "ATNPGM":"*ASSIST",
>   "SRTSEQ":"*HEX",
>   "LANGID":"ENG",
>   "CCSID":"*HEX",
>   "CHRIDCTL":"*DEVD",
>   "SETJOBATR":["*CCSID"],
>   "LOCALE":"*C",
>   "USROPT":["*HLPFULL"],
>   "UID":"*GEN",
>   "HOMEDIR":"*USRPRF",
>   "EIMASSOC":["*NOCHG"],
>   "USREXPITV":99,
>   "USREXPDATE":"*USREXPITV",
>   "LMTCPB":"*YES",
>   "CNTRYID":"*SYSVAL",
>   "GRPPRF":"AZURE","SUPGRPPRF":["AWS"]
> }" \
> "https://localhost:8443/openidm/system/as400/__ACCOUNT__/BJENSEN_prettyprint=true"
> {
>   "_id" : "BJENSEN",
>   "USROPT" : [ "*HLPFULL" ],
>   "SEV" : "50",
>   "USREXPITV" : 99,
>   "IsAuthCollectionActive" : false,
>   "HOMEDIR" : "/home/BJENSEN",
>   "MAXSTG" : "10000",
>   "UID" : "1277",
>   "PTYLMT" : 8,
>   "__NAME__" : "BJENSEN",
>   "PRTDEV" : "*SYSVAL",
>   "__ENABLE__" : true,
>   "LMTDEVSSN" : "*NO",
>   "__UID__" : "BJENSEN",
>   "SRTSEQ" : "*HEX",
>   "DSPSGNINF" : "*YES",
>   "PWDCHGBLK" : "93",
>   "GRPPRF" : "AZURE",
>   "USREXPDATE" : "12/06/22",
>   "CURLIB" : "*CRTDFT",
>   "LMTCPB" : "*YES",
>   "ASTLVL" : "*BASIC",
>   "SUPGRPPRF" : [ "AWS" ],
>   "MSGQ" : "/QSYS.LIB/QUSRSYS.LIB/BJENSEN.MSGQ",
>   "LANGID" : "ENG",
>   "CCSID" : "65535",
>   "PWDEXPITV" : "323",
>   "IsUserEntitlementRequired" : true,
>   "TEXT" : "TEXTFILEDVALUE",
>   "JOBD" : "/QSYS.LIB/QGPL.LIB/QDFTJOBD.JOBD",
>   "ActionAuditLevel" : "*BASIC",
>   "ObjectAuditValue" : "*NONE",
>   "PasswordChangedDate" : "Mon Aug 29 05:15:20 IST 2022",
>   "ATNPGM" : "/QSYS.LIB/QEZMAIN.PGM",
>   "LCLPWDMGT" : true,
>   "INLPGM" : "*NONE",
>   "USRCLS" : "*USER",
>   "SPCAUT" : [ "*AUDIT" ],
>   "SETJOBATR" : [ "*CCSID" ],
>   "SPCENV" : "*S36",
>   "ACGCDE" : "",
>   "IsPasswordNone" : false,
>   "DLVRY" : "*HOLD",
>   "IsAuthCollectionRepositoryExist" : false,
>   "UserExpirationAction" : "*DISABLE",
>   "INLMNU" : "/QSYS.LIB/%LIBL%.LIB/MAIN.MNU",
>   "LOCALE" : "*C",
>   "KBDBUF" : "*SYSVAL",
>   "OWNER" : "*USRPRF",
>   "PasswordExpireDate" : "Tue Jul 18 00:00:00 IST 2023",
>   "PWDEXP" : false,
>   "OUTQ" : "*DEV",
>   "CNTRYID" : "*SYSVAL",
>   "CHRIDCTL" : "*DEVD",
>   "StorageUsed" : "12"
> }
> ```

> **Collapse: Reset a user's password**
>
> To reset the password for an AS400 user account, you can use the connector to change the user's password:
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Content-Type: application/json" \
> --header "Accept-API-Version: resource=1.0" \
> --header "If-Match: *" \
> --request PUT \
> --data "{
>   "__PASSWORD__":"newpassword123"
> }" \
> "https://localhost:8443/openidm/system/as400/__ACCOUNT__/BJENSEN_prettyprint=true"
> {
>   "_id" : "BJENSEN",
>   "USROPT" : [ "*HLPFULL" ],
>   "SEV" : "50",
>   ...
> }
> ```

> **Collapse: Activate a user**
>
> The following example activates a user:
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Content-Type: application/json" \
> --header "Accept-API-Version: resource=1.0" \
> --header "If-Match: *" \
> --request PUT \
> --data "{
>   "__ENABLE__": true
> }
> "https://localhost:8443/openidm/system/as400/__ACCOUNT__/BJENSEN_prettyprint=true"
> {
>   "_id" : "BJENSEN",
>   ...
>   "__ENABLE__": true
>   ...
> }
> ```

> **Collapse: Deactivate a user**
>
> The following example deactivates a user:
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Content-Type: application/json" \
> --header "Accept-API-Version: resource=1.0" \
> --header "If-Match: *" \
> --request PUT \
> --data "{"
>   ""__ENABLE__": false
> }" \
> "https://localhost:8443/openidm/system/as400/__ACCOUNT__/BJENSEN_prettyprint=true"
> {
>   "_id" : "BJENSEN",
>   ...
>   "__ENABLE__": false
>   ...
> }
> ```

> **Collapse: Delete a user**
>
> The following example deletes a user:
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Content-Type: application/json" \
> --header "Accept-API-Version: resource=1.0" \
> --request DELETE \
> "https://localhost:8443/openidm/system/as400/__ACCOUNT__/BJENSEN_prettyprint=true"
> {
>   "_id" : "BJENSEN",
>   ...
> }
> ```

### Groups

> **Collapse: Query all groups**
>
> The following example queries all AS400 Groups by their IDs:
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Content-Type: application/json" \
> --header "Accept-API-Version: resource=1.0" \
> --request GET \
> "http://localhost:8080/openidm/system/as400/__GROUP__?_queryId=query-all-ids&_prettyprint=true"
> {
>   {
>   "result": [
>     {"_id": "AWS"},
>     {"_id": "AZURE"},
>     {"_id": "CLOUD"}
>   ],
>   "resultCount" : 3,
>   "pagedResultsCookie" : null,
>   "totalPagedResultsPolicy" : "NONE",
>   "totalPagedResults" : -1,
>   "remainingPagedResults" : -1
> }
> ```

> **Collapse: Query a single group**
>
> The following example queries a single AS400 group by its ID:
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Content-Type: application/json" \
> --header "Accept-API-Version: resource=1.0" \
> --request GET \
> "http://localhost:8080/openidm/system/as400/__GROUP__/AWS?_prettyprint=true"
> {
>   "_id" : "AWS",
>   "GID" : "116",
>   "__NAME__" : "AWS",
>   "GRPAUT" : "*NONE",
>   "GRPAUTTYP" : "*PRIVATE",
>   "__UID__" : "AWS"
> }
> ```

## OpenICF Interfaces Implemented by the AS400 Connector

The AS400 Connector implements the following OpenICF interfaces. For additional details, see [ICF interfaces](interfaces.html):

* Create

  Creates an object and its `uid`.

* Delete

  Deletes an object, referenced by its `uid`.

* Schema

  Describes the object types, operations, and options that the connector supports.

* Script on Connector

  Enables an application to run a script in the context of the connector.

  Any script that runs on the connector has the following characteristics:

  * The script runs in the same execution environment as the connector and has access to all the classes to which the connector has access.

  * The script has access to a `connector` variable that is equivalent to an initialized instance of the connector. At a minimum, the script can access the connector configuration.

  * The script has access to any script arguments passed in by the application.

* Search

  Searches the target resource for all objects that match the specified object class and filter.

* Test

  Tests the connector configuration.

  Testing a configuration checks all elements of the environment that are referred to by the configuration are available. For example, the connector might make a physical connection to a host that is specified in the configuration to verify that it exists and that the credentials that are specified in the configuration are valid.

  This operation might need to connect to a resource, and, as such, might take some time. Do not invoke this operation too often, such as before every provisioning operation. The test operation is not intended to check that the connector is alive (that is, that its physical connection to the resource has not timed out).

  You can invoke the test operation before a connector configuration has been validated.

* Update

  Updates (modifies or replaces) objects on a target resource.

[]()

## AS400 Connector Configuration

The AS400 Connector has the following configurable properties:

### Configuration properties

| Property                                   | Type            | Default | Encrypted(1)             | Required(2)               |
| ------------------------------------------ | --------------- | ------- | ------------------------ | ------------------------- |
| `hostName`                                 | `String`        | `null`  |                          | [icon: check, set=fas]Yes |
| Host name or IP address of As400.          |                 |         |                          |                           |
| `userName`                                 | `String`        | `null`  |                          | [icon: check, set=fas]Yes |
| The username to login As400.               |                 |         |                          |                           |
| `password`                                 | `GuardedString` | `null`  | [icon: lock, set=fas]Yes | [icon: check, set=fas]Yes |
| The password to login As400.               |                 |         |                          |                           |
| `isSecure`                                 | `boolean`       | `true`  |                          | [icon: check, set=fas]Yes |
| Enables or not secure connection to As400. |                 |         |                          |                           |

(1) Whether the property value is considered confidential, and is therefore encrypted in IDM.

(2) A list of operations in this column indicates that the property is required for those operations.

### Basic Configuration Properties

| Property                                                                                                                                                       | Type      | Default | Encrypted(1) | Required(2)              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ------- | ------------ | ------------------------ |
| `maximumConnections`                                                                                                                                           | `Integer` | `10`    |              | [icon: times, set=fas]No |
| Provides the maximum connections.                                                                                                                              |           |         |              |                          |
| `maxLifetime`                                                                                                                                                  | `Integer` | `null`  |              | [icon: times, set=fas]No |
| Provides the maximum life for an available connection.                                                                                                         |           |         |              |                          |
| `maxInactivity`                                                                                                                                                | `Integer` | `null`  |              | [icon: times, set=fas]No |
| Provides the maximum amount of inactive time before an available connection is closed.                                                                         |           |         |              |                          |
| `maxUseTime`                                                                                                                                                   | `Long`    | `null`  |              | [icon: times, set=fas]No |
| Provides the maximum amount of time a connection can be in use before it is closed and returned to the pool. A value of `-1` indicates that there is no limit. |           |         |              |                          |
| `maxUseCount`                                                                                                                                                  | `Integer` | `null`  |              | [icon: times, set=fas]No |
| Provides the maximum number of times a connection can be used before it is replaced in the pool. A value of `-1` indicates that there is no limit.             |           |         |              |                          |
| `isRunMaintenance`                                                                                                                                             | `boolean` | `true`  |              | [icon: times, set=fas]No |
| Indicates whether the maintenance thread is used to clean up expired connections.                                                                              |           |         |              |                          |
| `isThreadUsed`                                                                                                                                                 | `boolean` | `true`  |              | [icon: times, set=fas]No |
| Indicates whether threads are used in communication with the host servers and for running maintenance.                                                         |           |         |              |                          |
| `cleanupInterval`                                                                                                                                              | `Long`    | `null`  |              | [icon: times, set=fas]No |
| Time interval for how often the maintenance daemon is run.                                                                                                     |           |         |              |                          |

(1) Whether the property value is considered confidential, and is therefore encrypted in IDM.

(2) A list of operations in this column indicates that the property is required for those operations.

---

---
title: Authentication methods (MS Graph API)
description: How to read and manage multi-factor authentication (MFA) methods for Azure AD users using the PingIDM MS Graph API connector
component: openicf
page_id: openicf:connector-reference:msgraph-authentication-methods
canonical_url: https://docs.pingidentity.com/openicf/connector-reference/msgraph-authentication-methods.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  list_mfa_methods: List MFA methods
  create_or_update_email_mfa_method: Create or update email MFA method
  remove_email_mfa_method: Remove email MFA method
  manage_phone_mfa_method: Manage phone MFA method
  limitations: Limitations
  remove_microsoft_authenticator_fido2_and_software_oath_mfa_methods: Remove Microsoft Authenticator, FIDO2, and software OATH MFA methods
---

# Authentication methods (MS Graph API)

The MS Graph API connector lets you read and manage the following multi-factor authentication (MFA) methods from the user resource:

| MFA method              | Supported operations   |
| ----------------------- | ---------------------- |
| Email                   | Create, Update, Delete |
| Phone                   | Create, Update, Delete |
| FIDO2                   | Delete                 |
| Microsoft Authenticator | Delete                 |
| Software OATH           | Delete                 |

## List MFA methods

List the authentication methods with the `authenticationMethods` user relationship:

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"http://localhost:8080/openidm/system/azuread/user/88080bec-30bd-4026-b5af-5d4607dc7ccc/?_fields=authenticationMethods"
```

Response

```json
{
  "_id": "88080bec-30bd-4026-b5af-5d4607dc7ccc",
  ...
  "authenticationMethods": [
    {
      "@odata.type": "#microsoft.graph.passwordAuthenticationMethod",
      "createdDateTime": "2024-12-11T01:07:44Z",
      "id": "28c10230-6103-485e-b985-444c60001490"
    }
  ]
}
```

## Create or update email MFA method

|   |                                               |
| - | --------------------------------------------- |
|   | The create and update requests are identical. |

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--header "If-None-Match: *" \
--request PUT \
--data '{
  "__emailAuthenticationMethod__": "add_email@example.com"
}' \
"http://localhost:8080/openidm/system/azuread/user/a9299a21-c384-4882-b363-8d7427b36fc5"
```

Response

```json
{
  "_id": "a9299a21-c384-4882-b363-8d7427b36fc5",
  ...
  "authenticationMethods": [
    {
      "@odata.type": "#microsoft.graph.passwordAuthenticationMethod",
      "createdDateTime": "2024-12-11T01:07:47Z",
      "id": "28c10230-6103-485e-b985-444c60001490"
    },
    {
      "emailAddress": "add_email@example.com",
      "@odata.type": "#microsoft.graph.emailAuthenticationMethod",
      "id": "3ddfcfc8-9383-446f-83cc-3ab9be4be18f"
    }
  ]
}
```

## Remove email MFA method

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--header "If-None-Match: *" \
--request PUT \
--data '{
  "__emailAuthenticationMethod__": null
}' \
"http://localhost:8080/openidm/system/azuread/user/bfe4b140-3b76-4633-855c-26e21a7517c9"
```

Response

```json
{
  "_id": "bfe4b140-3b76-4633-855c-26e21a7517c9",
  ...
  "authenticationMethods": [
    {
      "@odata.type": "#microsoft.graph.passwordAuthenticationMethod",
      "createdDateTime": "2024-12-11T01:07:56Z",
      "id": "28c10230-6103-485e-b985-444c60001490"
    }
  ]
}
```

## Manage phone MFA method

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Managing authentication methods requires the following [Microsoft Graph application permissions](msgraph-conf.html#procedure-prepare-azuread) on your Azure app registration:- `UserAuthenticationMethod.Read.All`: Required to list authentication methods.

- `UserAuthenticationMethod.ReadWrite.All`: Required to create, update, or delete authentication methods.Learn more in the Microsoft documentation:- [phoneAuthenticationMethod resource type](https://learn.microsoft.com/en-us/graph/api/resources/phoneauthenticationmethod?view=graph-rest-1.0)

- [Microsoft Entra authentication methods API overview](https://learn.microsoft.com/en-us/graph/api/resources/authenticationmethods-overview?view=graph-rest-1.0) |

To manage phone MFA methods, provide an authoritative list of numbers using a PUT request on the user object. Phone numbers use the format `{phoneNumber}:{phoneType}` under the special user attribute `__phoneAuthenticationMethods__`. The connector performs a diff between the request and the user's current list of numbers, and does the following:

* Adds new numbers.

* Removes existing numbers not in the request.

* Replaces non-matching existing numbers for phone types.

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--header "If-None-Match: *" \
--request PUT \
--data '{
  "__phoneAuthenticationMethods__": [
    "+1 7322714703:mobile",
    "+1 7322714705:alternate_mobile",
    "+1 7322714709:office"
  ]
}' \
"http://localhost:8080/openidm/system/azuread/user/00490cf6-4fdd-4b7b-86dd-907e3d613fd0"
```

Response

```json
{
  "_id": "00490cf6-4fdd-4b7b-86dd-907e3d613fd0",
  ...
  "__phoneAuthenticationMethods__": [
    "+1 7322714709:OFFICE",
    "+1 7322714705:ALTERNATE_MOBILE",
    "+1 7322714703:MOBILE"
  ]
}
```

### Limitations

The Microsoft Graph API enforces the following constraints on phone authentication methods:

* A user must have a `mobile` phone number before you can add an `alternate_mobile` number.

* You can't change a phone number's type directly. To change the type, add a new number with the desired type, then delete the number with the original type.

* To remove a `mobile` number from a user that also has an `alternate_mobile` number, first update the `mobile` number to the new number, then delete the `alternate_mobile` number.

* If a user is enabled to use SMS sign-in, changing the `mobile` number triggers re-registration of the number for SMS sign-in.

Learn more in [phoneAuthenticationMethod resource type](https://learn.microsoft.com/en-us/graph/api/resources/phoneauthenticationmethod?view=graph-rest-1.0).

## Remove Microsoft Authenticator, FIDO2, and software OATH MFA methods

Microsoft's API only supports the removal of Microsoft Authenticator, FIDO2, and software OATH MFA methods. The connector implements the removal of these MFA methods using the following virtual attributes:

* `__removeMicrosoftAuthenticatorMethods__`

* `__removeFido2Methods__`

* `__removeSoftwareOathMethods__`

The following example removes a Microsoft Authenticator MFA method:

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--header "If-None-Match: *" \
--request PUT \
--data '{
  "__removeMicrosoftAuthenticatorMethods__": [
    "00490cf6-4fdd-4b7b-86dd-907e3d613fd0"
  ]
}' \
"http://localhost:8080/openidm/system/azuread/user/bfe4b140-3b76-4633-855c-26e21a7517c9"
```

Response

```json
{
  "_id": "bfe4b140-3b76-4633-855c-26e21a7517c9",
  ...
  "authenticationMethods": [
    {
      "@odata.type": "#microsoft.graph.passwordAuthenticationMethod",
      "createdDateTime": "2024-12-11T01:07:56Z",
      "id": "28c10230-6103-485e-b985-444c60001490"
    }
  ]
}
```

---

---
title: AWS Bedrock AgentCore connector
description: "Reference for the AWS Bedrock AgentCore connector: discover AgentCore runtimes, execution identity, workload identity, and inbound access policy."
component: openicf
page_id: openicf:connector-reference:aws-bedrock-agentcore
canonical_url: https://docs.pingidentity.com/openicf/connector-reference/aws-bedrock-agentcore.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  aws_bedrock_agentcore_requirements: AWS Bedrock AgentCore requirements
  required_permissions: Required permissions
  create_an_iam_user_for_explicit_credentials: Create an IAM user for explicit credentials
  install_the_aws_bedrock_agentcore_connector: Install the AWS Bedrock AgentCore connector
  configure_the_aws_bedrock_agentcore_connector: Configure the AWS Bedrock AgentCore connector
  connection_details: Connection details
  example_aws_bedrock_agentcore_configuration: Example AWS Bedrock AgentCore configuration
  test_the_aws_bedrock_agentcore_connector: Test the AWS Bedrock AgentCore connector
  aws_bedrock_agentcore_remote_connector: AWS Bedrock AgentCore remote connector
  implementation_specifics: Implementation specifics
  collection_architecture: Collection architecture
  live_data: Live data
  known_limitations: Known limitations
  use_the_aws_bedrock_agentcore_connector: Use the AWS Bedrock AgentCore connector
  account_attributes: __ACCOUNT__ attributes
  troubleshooting: Troubleshooting
  connector_initializes_but_reconciliation_fails_immediately: Connector initializes but reconciliation fails immediately
  no_runtime_objects_are_returned: No runtime objects are returned
  endpoint_attributes_are_empty: Endpoint attributes are empty
  resourcepolicy_is_empty: resourcePolicy is empty
  implemented-interfaces-org-forgerock-openicf-connectors-bedrockagentcore-BedrockAgentCoreConnector-1.5.20.33: OpenICF interfaces implemented by the AWS Bedrock AgentCore connector
  config-properties-org-forgerock-openicf-connectors-bedrockagentcore-BedrockAgentCoreConnector-1.5.20.33: AWS Bedrock AgentCore connector configuration
  basic-configuration-properties-org-forgerock-openicf-connectors-bedrockagentcore-BedrockAgentCoreConnector-1.5.20.33: Basic configuration properties
---

# AWS Bedrock AgentCore connector

AWS Bedrock AgentCore is Amazon Web Services' runtime environment for deploying AI agent workloads. The AWS Bedrock AgentCore connector is a read-only connector that discovers AgentCore runtimes and governance-relevant identity surfaces including execution identity, workload identity, runtime endpoint state, and resource-based inbound access policy.

Contact your Ping Identity Customer Success Outcome Manager (CSOM) or Account Executive to obtain this connector.

## AWS Bedrock AgentCore requirements

The AWS Bedrock AgentCore connector is read-only. It needs Bedrock AgentCore control-plane read permissions in the configured AWS region.

### Required permissions

Use the narrowest policy your environment allows. The following is a starting point:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "BedrockAgentCoreConnectorReadOnly",
      "Effect": "Allow",
      "Action": [
        "bedrock-agentcore:ListAgentRuntimes",
        "bedrock-agentcore:GetAgentRuntime",
        "bedrock-agentcore:GetAgentRuntimeEndpoint",
        "bedrock-agentcore:GetResourcePolicy"
      ],
      "Resource": "*"
    }
  ]
}
```

`ListAgentRuntimes` requires `Resource: "*"`. The other read actions can be scoped to AgentCore runtime ARNs if your AWS environment supports the narrower resource policy.

The connector doesn't need account-wide Identity and Access Management (IAM) list/read permissions. It doesn't scan IAM roles or policies. Inbound access is collected from the AgentCore runtime resource policy by calling `GetResourcePolicy` on the runtime Amazon Resource Name (ARN).

### Create an IAM user for explicit credentials

If `useDefaultCredentialsProvider` is `false`, create a dedicated IAM user and attach the policy above to it.

1. In the AWS console, go to IAM > Policies > Create policy.

2. On the JSON tab, paste the policy from [Required permissions](#required_permissions), then select Next.

3. Name the policy `iga-bedrock-agentcore-connector-policy`, then select Create policy.

4. Go to IAM > Users > Create user.

5. Enter a username, for example `iga-bedrock-agentcore-connector`.

   |   |                                                                                                                                      |
   | - | ------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Don't select Provide user access to the AWS Management Console. The connector authenticates with an access key, not console sign-on. |

6. Select Next.

7. Under Set permissions, choose Attach policies directly.

8. Search for `iga-bedrock-agentcore-connector-policy`, select it, then select Next > Create user.

To create the access key:

1. Open the user, then select the Security credentials tab.

2. Select Create access key.

3. For Use case, select Application running outside AWS, then select Next.

4. Copy the access key ID and secret access key. You'll need these for the `accessKeyId` and `secretAccessKey` configuration properties.

Before you configure the connector, confirm you have the following:

| Requirement                        | Value                                                                                           |
| ---------------------------------- | ----------------------------------------------------------------------------------------------- |
| AWS Bedrock AgentCore runtimes     | Configured in the target AWS account and region                                                 |
| AWS credentials                    | Available through the default AWS credentials provider chain or explicit access key credentials |
| Bedrock AgentCore read permissions | Required for AgentCore control-plane read APIs                                                  |

## Install the AWS Bedrock AgentCore connector

|   |                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To check for an Advanced Identity Cloud application for this connector, refer to:- [Application management](https://docs.pingidentity.com/pingoneaic/latest/app-management/applications.html)

- [App catalog](https://docs.pingidentity.com/pingoneaic/latest/app-management/app-catalog.html) |

To obtain the connector `.jar` file, contact your Ping Identity Customer Success Outcome Manager (CSOM) or Account Executive.

* If you're running the connector locally, place the `.jar` file in the `/path/to/openidm/connectors` directory.

* If you're using a remote connector server (RCS), place the `.jar` file in the `/path/to/openicf/connectors` directory on the RCS.

## Configure the AWS Bedrock AgentCore connector

Create a connector configuration using the IDM admin UI:

1. From the navigation bar, click Configure > Connectors.

2. On the Connectors page, click New Connector.

3. On the New Connector page, type a Connector Name.

4. From the Connector Type list, select AWS Bedrock AgentCore Connector - 1.5.20.33.

5. Complete the Base Connector Details and any applicable Additional Options.

   |   |                                                                                                                                             |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For a list of all configuration properties, refer to [AWS Bedrock AgentCore Connector Configuration](#bedrockagentcore-config-prop-ezLink). |

6. Click Save.

When your connector is configured correctly, the connector displays as Active in the admin UI.

Refer to [this procedure](configure-connector.html#connector-wiz-REST) to create a connector configuration over REST.

### Connection details

The AWS Bedrock AgentCore connector uses the following configuration properties:

| Property                        | Type          | Required    | Default     | Description                                                                                                                  |
| ------------------------------- | ------------- | ----------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `region`                        | String        | Yes         | `us-east-1` | AWS region. Deploy one connector configuration per region.                                                                   |
| `useDefaultCredentialsProvider` | Boolean       | Yes         | `true`      | When `true`, uses the AWS SDK `DefaultCredentialsProvider` chain. When `false`, provide `accessKeyId` and `secretAccessKey`. |
| `accessKeyId`                   | String        | Conditional | None        | AWS access key ID. Required when `useDefaultCredentialsProvider=false`.                                                      |
| `secretAccessKey`               | GuardedString | Conditional | None        | AWS secret access key. Required when `useDefaultCredentialsProvider=false`.                                                  |

The default credentials provider chain is the recommended production mode when the connector runs on AWS infrastructure with instance role, task role, or service account based credentials.

### Example AWS Bedrock AgentCore configuration

```json
{
  "connectorRef": {
    "bundleName": "org.forgerock.openicf.connectors.bedrockagentcore-connector",
    "bundleVersion": "[1.5.0.0,1.6.0.0)",
    "connectorName": "org.forgerock.openicf.connectors.bedrockagentcore.BedrockAgentCoreConnector"
  },
  "configurationProperties": {
    "region": "us-east-1",
    "useDefaultCredentialsProvider": true
  }
}
```

If you use explicit credentials instead of the default provider chain:

```json
{
  "connectorRef": {
    "bundleName": "org.forgerock.openicf.connectors.bedrockagentcore-connector",
    "bundleVersion": "[1.5.0.0,1.6.0.0)",
    "connectorName": "org.forgerock.openicf.connectors.bedrockagentcore.BedrockAgentCoreConnector"
  },
  "configurationProperties": {
    "region": "us-east-1",
    "useDefaultCredentialsProvider": false,
    "accessKeyId": "AKIA...",
    "secretAccessKey": {
      "$crypto": {
        "type": "x-simple-encryption",
        "value": {
          "cipher": "...",
          "data": "...",
          "iv": "...",
          "key": "openidm-sym-default"
        }
      }
    }
  }
}
```

### Test the AWS Bedrock AgentCore connector

Test that the configuration is correct by running the following command:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
"http://localhost:8080/openidm/system/bedrockagentcore?_action=test"
{
  "name": "bedrockagentcore",
  "enabled": true,
  "config": "config/provisioner.openicf/bedrockagentcore",
  "connectorRef": {
    "bundleVersion": "[1.5.0.0,1.6.0.0)",
    "bundleName": "org.forgerock.openicf.connectors.bedrockagentcore-connector",
    "connectorName": "org.forgerock.openicf.connectors.bedrockagentcore.BedrockAgentCoreConnector"
  },
  "displayName": "AWS Bedrock AgentCore Connector",
  "objectTypes": [
    "__ACCOUNT__",
    "__ALL__"
  ],
  "ok": true
}
```

If the command returns `"ok": true`, your connector has been configured correctly.

|   |                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | `TestOp` currently logs that the test operation was called but doesn't call AWS, and always succeeds regardless of credential validity. Validate credentials and IAM permissions by running a reconciliation against a known AgentCore runtime. |

### AWS Bedrock AgentCore remote connector

If you want to run this connector outside of PingOne Advanced Identity Cloud or IDM, you can configure the AWS Bedrock AgentCore connector as a remote connector. Java Connectors installed remotely on a Java Connector Server function identically to those bundled locally within PingOne Advanced Identity Cloud or installed locally on IDM.

Refer to [Remote connectors](remote-connector.html) for configuring the AWS Bedrock AgentCore remote connector.

## Implementation specifics

### Collection architecture

The AWS Bedrock AgentCore connector performs live collection during each reconciliation. There is no offline inventory mechanism for the current AgentCore connector.

For each runtime in the configured region, the connector calls AgentCore control-plane APIs and builds one ICF `__ACCOUNT__` object.

#### Live data

| Data                     | AWS API                                               |
| ------------------------ | ----------------------------------------------------- |
| Runtime list             | `ListAgentRuntimes`                                   |
| Runtime details          | `GetAgentRuntime`                                     |
| Default runtime endpoint | `GetAgentRuntimeEndpoint` with `endpointName=DEFAULT` |
| Runtime resource policy  | `GetResourcePolicy` using the runtime ARN             |

For GET-by-UID, the connector skips `ListAgentRuntimes` and calls `GetAgentRuntime` directly for the supplied `agentRuntimeId`, then fetches endpoint and resource policy details.

### Known limitations

| Limitation                                | Impact                                                                                                        |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Read-only connector                       | Can't create, update, or delete AgentCore runtimes.                                                           |
| No `SyncOp`                               | Every reconciliation is a full discovery pass.                                                                |
| Single region per instance                | Multi-region coverage requires multiple connector configurations.                                             |
| Only `__ACCOUNT__` object class           | Runtime, endpoint, workload identity, and resource policy data are flattened onto one object.                 |
| `TestOp` is a no-op                       | IDM test can pass even when AWS credentials or permissions are invalid.                                       |
| No retry logic                            | Transient AWS throttling or 5xx failures can fail reconciliation.                                             |
| `resourcePolicy` is raw JSON              | Downstream IDM policy logic must parse and evaluate policy statements.                                        |
| Workload identity grants are not expanded | The connector collects `workloadIdentityArn`, but doesn't discover what external systems trust that identity. |

## Use the AWS Bedrock AgentCore connector

The AWS Bedrock AgentCore connector discovers the following resource types:

| ICF Native Type | AWS Bedrock AgentCore Resource Type | Naming Attribute | Notes                                                                                                                                                                                                       |
| --------------- | ----------------------------------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `__ACCOUNT__`   | Bedrock AgentCore runtime           | `__NAME__`       | Represents one AgentCore runtime. UID is `agentRuntimeId`; name is `agentRuntimeName`. Runtime, endpoint, workload identity, code artifact, and resource policy details are flattened onto the same object. |

### `__ACCOUNT__` attributes

| Attribute                     | Type   | Multivalued | Description                                                                                                          |
| ----------------------------- | ------ | ----------- | -------------------------------------------------------------------------------------------------------------------- |
| `agentRuntimeArn`             | String | No          | Full AgentCore runtime ARN.                                                                                          |
| `agentRuntimeVersion`         | String | No          | Runtime version.                                                                                                     |
| `status`                      | String | No          | Runtime lifecycle status, such as `READY`.                                                                           |
| `roleArn`                     | String | No          | IAM execution role ARN for the runtime.                                                                              |
| `networkMode`                 | String | No          | Runtime network mode, such as `PUBLIC`.                                                                              |
| `createdAt`                   | String | No          | Runtime creation timestamp.                                                                                          |
| `lastUpdatedAt`               | String | No          | Runtime last updated timestamp.                                                                                      |
| `description`                 | String | No          | Runtime description. Empty string if absent.                                                                         |
| `workloadIdentityArn`         | String | No          | AgentCore workload identity ARN. Empty string if absent.                                                             |
| `lifecycleIdleTimeoutSeconds` | Long   | No          | Idle runtime session timeout. `0` if not set.                                                                        |
| `lifecycleMaxLifetimeSeconds` | Long   | No          | Maximum runtime lifetime. `0` if not set.                                                                            |
| `codeS3Bucket`                | String | No          | S3 bucket for the runtime code artifact. Empty string if absent.                                                     |
| `codeS3Prefix`                | String | No          | S3 prefix for the runtime code artifact. Empty string if absent.                                                     |
| `codeRuntime`                 | String | No          | Runtime language/runtime value, such as `PYTHON_3_14`. Empty string if absent.                                       |
| `codeEntryPoint`              | String | Yes         | Runtime entry point command list, when present.                                                                      |
| `endpointArn`                 | String | No          | Default runtime endpoint ARN. Empty string if the endpoint call fails.                                               |
| `endpointName`                | String | No          | Endpoint name. The connector requests `DEFAULT`.                                                                     |
| `endpointId`                  | String | No          | Endpoint ID. The connector expects `DEFAULT` in v1.                                                                  |
| `endpointLiveVersion`         | String | No          | Runtime version currently serving requests through the endpoint.                                                     |
| `endpointStatus`              | String | No          | Endpoint lifecycle status. Distinct from runtime `status`.                                                           |
| `endpointCreatedAt`           | String | No          | Endpoint creation timestamp.                                                                                         |
| `endpointLastUpdatedAt`       | String | No          | Endpoint last updated timestamp.                                                                                     |
| `resourcePolicy`              | String | No          | Raw JSON string returned by `GetResourcePolicy`. Empty string when no policy is attached or the policy lookup fails. |

## Troubleshooting

### Connector initializes but reconciliation fails immediately

Check:

1. `region` is valid for Bedrock AgentCore.

2. The connector principal has `bedrock-agentcore:ListAgentRuntimes`.

3. The AWS credentials provider mode is configured correctly.

4. If `useDefaultCredentialsProvider=false`, `accessKeyId` and `secretAccessKey` are populated.

5. The AWS SDK version bundled with the connector supports the `bedrockagentcorecontrol` module.

### No runtime objects are returned

Check:

1. The target region contains AgentCore runtimes.

2. The connector is configured for the same region where the runtimes exist.

3. `ListAgentRuntimes` succeeds for the connector principal.

4. `GetAgentRuntime` succeeds for each runtime ID.

5. Runtime objects are not being filtered out by an IDM-side query filter.

### Endpoint attributes are empty

Check:

1. The runtime has a `DEFAULT` endpoint.

2. The connector principal can call `bedrock-agentcore:GetAgentRuntimeEndpoint`.

3. The endpoint is available in the configured region.

4. Review connector logs; endpoint lookup failures are soft failures and don't suppress the runtime object.

### `resourcePolicy` is empty

Check:

1. A resource policy is attached to the AgentCore runtime ARN.

2. The connector principal can call `bedrock-agentcore:GetResourcePolicy`.

3. The runtime ARN in AWS matches the resource ARN used for policy retrieval.

4. If there is no attached policy, empty `resourcePolicy` is expected.

## OpenICF interfaces implemented by the AWS Bedrock AgentCore connector

The AWS Bedrock AgentCore connector implements the following OpenICF interfaces. You can find additional details in [ICF interfaces](interfaces.html):

* Schema

  Describes the object types, operations, and options that the connector supports.

* Search

  Searches the target resource for all objects that match the specified object class and filter.

* Test

  Tests the connector configuration.

  For this connector, `TestOp` logs that the test was called but does not make any AWS API calls, and always returns success regardless of credential validity. To validate credentials and IAM permissions, run a reconciliation against a known AgentCore runtime.

[]()

## AWS Bedrock AgentCore connector configuration

The AWS Bedrock AgentCore connector has the following configurable properties:

### Basic configuration properties

| Property                                                                                                                                                                      | Type            | Default     | Encrypted(1)             | Required(2)               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | ----------- | ------------------------ | ------------------------- |
| `region`                                                                                                                                                                      | `String`        | `us-east-1` |                          | [icon: check, set=fas]Yes |
| AWS region where AgentCore runtimes are deployed, for example `us-east-1`.                                                                                                    |                 |             |                          |                           |
| `useDefaultCredentialsProvider`                                                                                                                                               | `Boolean`       | `true`      |                          | [icon: check, set=fas]Yes |
| When enabled, uses the AWS SDK DefaultCredentialsProvider chain (environment variables, shared config, EC2/ECS role). When disabled, provide accessKeyId and secretAccessKey. |                 |             |                          |                           |
| `accessKeyId`                                                                                                                                                                 | `String`        | `null`      |                          | [icon: times, set=fas]No  |
| AWS access key ID. Required when the default credentials provider is disabled.                                                                                                |                 |             |                          |                           |
| `secretAccessKey`                                                                                                                                                             | `GuardedString` | `null`      | [icon: lock, set=fas]Yes | [icon: times, set=fas]No  |
| AWS secret access key. Required when the default credentials provider is disabled.                                                                                            |                 |             |                          |                           |

(1) Whether the property value is considered confidential, and is therefore encrypted in IDM.

(2) A list of operations in this column indicates that the property is required for those operations.

---

---
title: AWS Bedrock connector
description: "Reference for the AWS Bedrock connector: discover Bedrock agents, aliases, action groups, knowledge bases, guardrails, and identity bindings."
component: openicf
page_id: openicf:connector-reference:aws-bedrock
canonical_url: https://docs.pingidentity.com/openicf/connector-reference/aws-bedrock.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  aws_bedrock_requirements: AWS Bedrock requirements
  required_permissions: Required permissions
  create_an_iam_user_for_explicit_credentials: Create an IAM user for explicit credentials
  install_the_aws_bedrock_connector: Install the AWS Bedrock connector
  configure_the_aws_bedrock_connector: Configure the AWS Bedrock connector
  connection_details: Connection details
  example_aws_bedrock_configuration: Example AWS Bedrock configuration
  test_the_aws_bedrock_connector: Test the AWS Bedrock connector
  aws_bedrock_remote_connector: AWS Bedrock remote connector
  implementation_specifics: Implementation specifics
  collection_architecture: Collection architecture
  live_data: Live data
  s3_inventory_data: S3 inventory data
  s3_inventory_behavior: S3 inventory behavior
  use_the_aws_bedrock_connector: Use the AWS Bedrock connector
  account_attributes: __ACCOUNT__ attributes
  agenttool_attributes: agentTool attributes
  agentknowledgebase_attributes: agentKnowledgeBase attributes
  agentguardrail_attributes: agentGuardrail attributes
  agentidentitybinding_attributes: agentIdentityBinding attributes
  agenttoolcredentials_attributes: agentToolCredentials attributes
  troubleshooting: Troubleshooting
  connector_initializes_but_test_fails: Connector initializes but test fails
  agents_reconcile_but_agentprincipals_is_empty: Agents reconcile but agentPrincipals is empty
  agents_reconcile_but_toolcredentialids_is_empty: Agents reconcile but toolCredentialIds is empty
  implemented-interfaces-org-forgerock-openicf-connectors-awsbedrock-AwsBedrockConnector-1.5.20.33: OpenICF interfaces implemented by the AWS Bedrock connector
  config-properties-org-forgerock-openicf-connectors-awsbedrock-AwsBedrockConnector-1.5.20.33: AWS Bedrock connector configuration
  basic-configuration-properties-org-forgerock-openicf-connectors-awsbedrock-AwsBedrockConnector-1.5.20.33: Basic configuration properties
---

# AWS Bedrock connector

AWS Bedrock is Amazon Web Services' managed service for building and deploying AI agents. The AWS Bedrock connector is a read-only connector that discovers Bedrock agents and governance-relevant objects including aliases, action groups, knowledge bases, guardrails, identity bindings, and tool credential classifications.

Contact your Ping Identity Customer Success Outcome Manager (CSOM) or Account Executive to obtain this connector.

|   |                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Retrieval of `agentIdentityBinding` and `agentToolCredentials` is enabled through an offline inventory mechanism that requires an Agent Governance license. Contact your CSOM for details. |

## AWS Bedrock requirements

The AWS Bedrock connector is read-only. It needs Bedrock read permissions and S3 read permission for the inventory bucket.

### Required permissions

Use the narrowest policy your environment allows. The following is a starting point:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ReadBedrockAgents",
      "Effect": "Allow",
      "Action": [
        "bedrock:ListAgents",
        "bedrock:GetAgent",
        "bedrock:ListAgentAliases",
        "bedrock:GetAgentAlias",
        "bedrock:ListAgentActionGroups",
        "bedrock:GetAgentActionGroup",
        "bedrock:ListAgentKnowledgeBases",
        "bedrock:ListAgentCollaborators",
        "bedrock:GetGuardrail"
      ],
      "Resource": "*"
    },
    {
      "Sid": "ReadBedrockInventoryArtifacts",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject"
      ],
      "Resource": "arn:aws:s3:::<inventory-bucket>/latest/*"
    }
  ]
}
```

Replace `<inventory-bucket>` with the name of your S3 inventory bucket (the value of the `inventoryBucket` configuration property, which defaults to `bedrock-core-inventory`).

The connector doesn't need account-wide IAM list/read permissions when the companion inventory job is deployed. IAM scanning belongs to the inventory job, not to the connector.

### Create an IAM user for explicit credentials

If `useDefaultCredentialsProvider` is `false`, create a dedicated IAM user and attach the policy above to it.

1. In the AWS console, go to IAM > Policies > Create policy.

2. On the JSON tab, paste the policy from [Required permissions](#required_permissions), then select Next.

3. Name the policy `iga-bedrock-connector-policy`, then select Create policy.

4. Go to IAM > Users > Create user.

5. Enter a username, for example `iga-bedrock-connector`.

   |   |                                                                                                                                      |
   | - | ------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Don't select Provide user access to the AWS Management Console. The connector authenticates with an access key, not console sign-on. |

6. Select Next.

7. Under Set permissions, choose Attach policies directly.

8. Search for `iga-bedrock-connector-policy`, select it, then select Next > Create user.

To create the access key:

1. Open the user, then select the Security credentials tab.

2. Select Create access key.

3. For Use case, select Application running outside AWS, then select Next.

4. Copy the access key ID and secret access key. You'll need these for the `accessKeyId` and `secretAccessKey` configuration properties.

Before you configure the connector, confirm you have the following:

| Requirement             | Value                                                                                               |
| ----------------------- | --------------------------------------------------------------------------------------------------- |
| AWS Bedrock Agents      | Configured in the target AWS account and region                                                     |
| S3 inventory bucket     | Required for identity binding and tool credential enrichment                                        |
| Companion inventory job | Required if you want `agentIdentityBinding`, `agentPrincipals`, or `agentToolCredentials` populated |

## Install the AWS Bedrock connector

|   |                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To check for an Advanced Identity Cloud application for this connector, refer to:- [Application management](https://docs.pingidentity.com/pingoneaic/latest/app-management/applications.html)

- [App catalog](https://docs.pingidentity.com/pingoneaic/latest/app-management/app-catalog.html) |

To obtain the connector `.jar` file, contact your Ping Identity Customer Success Outcome Manager (CSOM) or Account Executive.

* If you're running the connector locally, place the `.jar` file in the `/path/to/openidm/connectors` directory.

* If you're using a remote connector server (RCS), place the `.jar` file in the `/path/to/openicf/connectors` directory on the RCS.

## Configure the AWS Bedrock connector

Create a connector configuration using the IDM admin UI:

1. From the navigation bar, click Configure > Connectors.

2. On the Connectors page, click New Connector.

3. On the New Connector page, type a Connector Name.

4. From the Connector Type list, select AWS Bedrock Connector - 1.5.20.33.

5. Complete the Base Connector Details and any applicable Additional Options.

   |   |                                                                                                                             |
   | - | --------------------------------------------------------------------------------------------------------------------------- |
   |   | For a list of all configuration properties, refer to [AWS Bedrock Connector Configuration](#awsbedrock-config-prop-ezLink). |

6. Click Save.

When your connector is configured correctly, the connector displays as Active in the admin UI.

Refer to [this procedure](configure-connector.html#connector-wiz-REST) to create a connector configuration over REST.

### Connection details

The AWS Bedrock connector uses the following configuration properties:

| Property                        | Type          | Required    | Default                  | Description                                                                                                                                                  |
| ------------------------------- | ------------- | ----------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `region`                        | String        | Yes         | `us-east-1`              | AWS region for Bedrock and S3 calls. Deploy one connector configuration per region.                                                                          |
| `accountId`                     | String        | Yes         | None                     | AWS account ID. Used to construct Bedrock Agent ARNs and relationship identifiers.                                                                           |
| `useDefaultCredentialsProvider` | Boolean       | Yes         | `true`                   | When `true`, uses the AWS SDK default credential provider chain. When `false`, provide `accessKeyId` and `secretAccessKey`.                                  |
| `accessKeyId`                   | String        | Conditional | None                     | AWS access key ID. Required when `useDefaultCredentialsProvider=false`.                                                                                      |
| `secretAccessKey`               | GuardedString | Conditional | None                     | AWS secret access key. Required when `useDefaultCredentialsProvider=false`.                                                                                  |
| `inventoryBucket`               | String        | Yes         | `bedrock-core-inventory` | S3 bucket containing `latest/agent-bindings.json` and `latest/agent-tool-credentials.json`. Use the bucket name only, don't include `s3://` or a key prefix. |
| `bindingsCacheTtlSeconds`       | Long          | No          | `300`                    | Cache TTL for S3 inventory artifacts.                                                                                                                        |

### Example AWS Bedrock configuration

```json
{
  "connectorRef": {
    "bundleName": "org.forgerock.openicf.connectors.awsbedrock-connector",
    "bundleVersion": "[1.5.0.0,1.6.0.0)",
    "connectorName": "org.forgerock.openicf.connectors.awsbedrock.AwsBedrockConnector"
  },
  "configurationProperties": {
    "region": "us-east-1",
    "accountId": "123456789012",
    "useDefaultCredentialsProvider": false,
    "accessKeyId": "AKIA...",
    "secretAccessKey": {
      "$crypto": {
        "type": "x-simple-encryption",
        "value": {
          "cipher": "...",
          "data": "...",
          "iv": "...",
          "key": "openidm-sym-default"
        }
      }
    },
    "inventoryBucket": "bedrock-core-inventory",
    "bindingsCacheTtlSeconds": 300
  }
}
```

### Test the AWS Bedrock connector

Test that the configuration is correct by running the following command:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
"http://localhost:8080/openidm/system/awsbedrock?_action=test"
{
  "name": "awsbedrock",
  "enabled": true,
  "config": "config/provisioner.openicf/awsbedrock",
  "connectorRef": {
    "bundleVersion": "[1.5.0.0,1.6.0.0)",
    "bundleName": "org.forgerock.openicf.connectors.awsbedrock-connector",
    "connectorName": "org.forgerock.openicf.connectors.awsbedrock.AwsBedrockConnector"
  },
  "displayName": "AWS Bedrock Connector",
  "objectTypes": [
    "__ACCOUNT__",
    "__ALL__"
  ],
  "ok": true
}
```

If the command returns `"ok": true`, your connector has been configured correctly and can authenticate to the Bedrock API.

|   |                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | `TestOp` validates connectivity by calling `listAgents()`. It doesn't prove that the S3 inventory artifacts exist. Verify S3 inventory separately when validating identity bindings or tool credential records. |

### AWS Bedrock remote connector

If you want to run this connector outside of PingOne Advanced Identity Cloud or IDM, you can configure the AWS Bedrock connector as a remote connector. Java Connectors installed remotely on a Java Connector Server function identically to those bundled locally within PingOne Advanced Identity Cloud or installed locally on IDM.

Refer to [Remote connectors](remote-connector.html) for configuring the AWS Bedrock remote connector.

## Implementation specifics

### Collection architecture

The AWS Bedrock connector uses a split collection model.

Live collection runs inside the Java connector during reconciliation, calling AWS Bedrock APIs to list agents, aliases, action groups, knowledge bases, collaborators, and guardrails.

Offline collection is handled by the companion `bedrock-core-tools-inventory` process. That process scans IAM and related AWS resources, writes normalized JSON artifacts to S3, and the connector reads those artifacts during reconciliation. This split keeps reconciliation fast and avoids giving the connector broad IAM enumeration permissions.

#### Live data

| Data                             | AWS API family |
| -------------------------------- | -------------- |
| Agents                           | Bedrock Agent  |
| Agent aliases                    | Bedrock Agent  |
| Action groups                    | Bedrock Agent  |
| Knowledge bases                  | Bedrock Agent  |
| Collaborators / connected agents | Bedrock Agent  |
| Guardrail details                | Bedrock        |

#### S3 inventory data

| Artifact         | S3 key                               | Used for                                                        |
| ---------------- | ------------------------------------ | --------------------------------------------------------------- |
| Agent bindings   | `latest/agent-bindings.json`         | `agentIdentityBinding`, `agentPrincipals`, `identityBindingIds` |
| Tool credentials | `latest/agent-tool-credentials.json` | `agentToolCredentials`, `toolCredentialIds`                     |

Both artifacts are cached in memory. The cache TTL is controlled by `bindingsCacheTtlSeconds`.

### S3 inventory behavior

| Behavior               | Description                                                                                      |
| ---------------------- | ------------------------------------------------------------------------------------------------ |
| Cache TTL              | Controlled by `bindingsCacheTtlSeconds`.                                                         |
| Cache scope            | Connector instance memory.                                                                       |
| Identity binding cache | Used for `agentIdentityBinding`, `agentPrincipals`, and `identityBindingIds`.                    |
| Tool credential cache  | Used for `agentToolCredentials` and `toolCredentialIds`.                                         |
| Missing S3 key         | Connector logs a warning and returns no S3-backed records. Live Bedrock objects still reconcile. |
| Read failure           | Connector logs an error or warning and continues with empty S3-backed data.                      |

## Use the AWS Bedrock connector

The AWS Bedrock connector discovers the following resource types:

| ICF Native Type        | AWS Bedrock Resource Type                                           | Naming Attribute | Notes                                                                                                                                        |
| ---------------------- | ------------------------------------------------------------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `__ACCOUNT__`          | Bedrock Agent Alias, or Bedrock Agent when the agent has no aliases | `__NAME__`       | UID is `agentId:aliasId` for aliases, and `agentId` for bare agents.                                                                         |
| `agentTool`            | Bedrock Agent Action Group                                          | `__NAME__`       | Maps to action groups attached to an agent.                                                                                                  |
| `agentKnowledgeBase`   | Bedrock Agent Knowledge Base association                            | `__NAME__`       | Represents a knowledge base attached to an agent, not the standalone Bedrock Knowledge Base object.                                          |
| `agentGuardrail`       | Bedrock Guardrail attached to an agent                              | `__NAME__`       | Derived from the agent's `guardrailConfiguration`, enriched with guardrail details.                                                          |
| `agentIdentityBinding` | Derived IAM-to-Bedrock invocation binding                           | `__NAME__`       | Not a native Bedrock entity. Represents who can invoke an agent or alias, derived from IAM policies and read from the S3 inventory artifact. |
| `agentToolCredentials` | Derived action-group credential surface                             | `__NAME__`       | Not a native Bedrock entity. Represents credential-related metadata for an action group. Read from the S3 inventory artifact.                |

### `__ACCOUNT__` attributes

| Attribute                  | Type    | Multivalued | Description                                                   |
| -------------------------- | ------- | ----------- | ------------------------------------------------------------- |
| `platform`                 | String  | No          | Connector platform identifier. Current value is `awsbedrock`. |
| `agentId`                  | String  | No          | Bedrock Agent ID.                                             |
| `agentName`                | String  | No          | Bedrock Agent name.                                           |
| `version`                  | String  | No          | Agent version returned by Bedrock.                            |
| `status`                   | String  | No          | Agent status.                                                 |
| `description`              | String  | No          | Agent description.                                            |
| `foundationModel`          | String  | No          | Foundation model configured for the agent.                    |
| `roleArn`                  | String  | No          | Agent resource role ARN.                                      |
| `idleSessionTtlSeconds`    | Integer | No          | Idle session TTL in seconds.                                  |
| `createdAt`                | String  | No          | Agent creation timestamp.                                     |
| `updatedAt`                | String  | No          | Agent update timestamp.                                       |
| `preparedAt`               | String  | No          | Agent prepared timestamp.                                     |
| `agentArn`                 | String  | No          | Agent ARN constructed from region, account ID, and agent ID.  |
| `region`                   | String  | No          | AWS region configured on this connector instance.             |
| `customerEncryptionKeyArn` | String  | No          | Customer KMS key ARN, if present.                             |
| `failureReasons`           | String  | Yes         | Failure reason list from Bedrock.                             |
| `recommendedActions`       | String  | Yes         | Recommended remediation actions from Bedrock.                 |
| `guardrailId`              | String  | No          | Guardrail identifier from the agent guardrail configuration.  |
| `guardrailVersion`         | String  | No          | Guardrail version from the agent guardrail configuration.     |
| `tools`                    | String  | Yes         | Action group IDs associated with the agent.                   |
| `knowledgeBases`           | String  | Yes         | Knowledge base IDs associated with the agent.                 |
| `agentCollaboration`       | String  | No          | Bedrock multi-agent collaboration mode.                       |
| `connectedAgents`          | String  | Yes         | Collaborator alias ARNs returned by Bedrock.                  |
| `aliasId`                  | String  | No          | Alias ID. Present only on alias objects.                      |
| `aliasName`                | String  | No          | Alias name. Present only on alias objects.                    |
| `agentAliasStatus`         | String  | No          | Alias status. Present only on alias objects.                  |
| `agentPrincipals`          | String  | Yes         | Computed principal references from S3 identity bindings.      |
| `identityBindingIds`       | String  | Yes         | Forward pointers to `agentIdentityBinding` records.           |
| `toolCredentialIds`        | String  | Yes         | Forward pointers to `agentToolCredentials` records.           |

### `agentTool` attributes

| Attribute                    | Type   | Multivalued | Description                                          |
| ---------------------------- | ------ | ----------- | ---------------------------------------------------- |
| `platform`                   | String | No          | Connector platform identifier.                       |
| `agentId`                    | String | No          | Parent agent ID.                                     |
| `agentVersion`               | String | No          | Agent version used to list action groups.            |
| `actionGroupId`              | String | No          | Action group ID.                                     |
| `actionGroupName`            | String | No          | Action group name.                                   |
| `description`                | String | No          | Action group description.                            |
| `status`                     | String | No          | Action group state/status.                           |
| `executorArn`                | String | No          | Lambda executor ARN, when present.                   |
| `parentActionGroupSignature` | String | No          | Bedrock system action group signature, when present. |
| `schemaUri`                  | String | No          | S3 schema URI, when present.                         |

### `agentKnowledgeBase` attributes

| Attribute         | Type   | Multivalued | Description                                 |
| ----------------- | ------ | ----------- | ------------------------------------------- |
| `platform`        | String | No          | Connector platform identifier.              |
| `agentId`         | String | No          | Parent agent ID.                            |
| `agentVersion`    | String | No          | Agent version used to list knowledge bases. |
| `knowledgeBaseId` | String | No          | Knowledge base ID.                          |
| `description`     | String | No          | Knowledge base description.                 |
| `status`          | String | No          | Knowledge base association state/status.    |
| `updatedAt`       | String | No          | Last update timestamp.                      |

### `agentGuardrail` attributes

| Attribute              | Type   | Multivalued | Description                                                |
| ---------------------- | ------ | ----------- | ---------------------------------------------------------- |
| `platform`             | String | No          | Connector platform identifier.                             |
| `agentId`              | String | No          | Parent agent ID.                                           |
| `agentVersion`         | String | No          | Agent version.                                             |
| `guardrailId`          | String | No          | Guardrail identifier.                                      |
| `guardrailVersion`     | String | No          | Guardrail version.                                         |
| `guardrailName`        | String | No          | Guardrail display name.                                    |
| `guardrailDescription` | String | No          | Guardrail description.                                     |
| `state`                | String | No          | Guardrail state.                                           |
| `deploymentStatus`     | String | No          | Guardrail deployment status.                               |
| `inputAction`          | String | No          | Input action / filter information serialized as a string.  |
| `outputAction`         | String | No          | Output action / filter information serialized as a string. |

### `agentIdentityBinding` attributes

| Attribute     | Type   | Multivalued | Description                                         |
| ------------- | ------ | ----------- | --------------------------------------------------- |
| `platform`    | String | No          | Connector platform identifier.                      |
| `agentId`     | String | No          | Agent ID, or wildcard marker for wildcard bindings. |
| `kind`        | String | No          | Binding kind.                                       |
| `principal`   | String | No          | Principal reference.                                |
| `permissions` | String | Yes         | Permissions associated with the binding.            |

### `agentToolCredentials` attributes

| Attribute                | Type   | Multivalued | Description                                                                                           |
| ------------------------ | ------ | ----------- | ----------------------------------------------------------------------------------------------------- |
| `id`                     | String | No          | Tool credential record ID.                                                                            |
| `agentId`                | String | No          | Parent agent ID.                                                                                      |
| `agentArn`               | String | No          | Agent ARN.                                                                                            |
| `agentServiceRoleArn`    | String | No          | Agent service role ARN.                                                                               |
| `actionGroupId`          | String | No          | Action group ID.                                                                                      |
| `actionGroupName`        | String | No          | Action group name.                                                                                    |
| `actionGroupState`       | String | No          | Action group state.                                                                                   |
| `credentialType`         | String | No          | Credential classification.                                                                            |
| `credentialRef`          | String | No          | Reference to the credential surface, such as a Lambda ARN or S3 URI. Doesn't contain secret material. |
| `apiSchemaSource`        | String | No          | API schema source.                                                                                    |
| `functionSchema`         | String | No          | Whether the action group uses a function schema.                                                      |
| `accountId`              | String | No          | AWS account ID.                                                                                       |
| `region`                 | String | No          | AWS region.                                                                                           |
| `lambdaExecutionRoleArn` | String | No          | Lambda execution role ARN, when available.                                                            |

## Troubleshooting

### Connector initializes but test fails

Check:

1. `region` is valid for Bedrock Agents.

2. `accountId` is populated.

3. Explicit credentials are configured, or `useDefaultCredentialsProvider=true` and the connector runs on AWS infrastructure with an instance role, task role, or service account.

4. The principal has Bedrock read permissions.

5. The target account has Bedrock Agents in the configured region.

### Agents reconcile but `agentPrincipals` is empty

Check:

1. The companion inventory job has run successfully.

2. `latest/agent-bindings.json` exists in the configured S3 bucket.

3. The connector principal can call `s3:GetObject` on the inventory key.

4. `bindingsCacheTtlSeconds` has expired, or the connector has been restarted after a fresh inventory run.

5. IAM policies actually grant `bedrock:InvokeAgent` to the expected principals.

### Agents reconcile but `toolCredentialIds` is empty

Check:

1. `latest/agent-tool-credentials.json` exists in the configured S3 bucket.

2. The inventory job has permissions to inspect action groups and related credential surfaces.

3. The connector principal can read the S3 artifact.

4. The action groups are present for the same region and account as the connector configuration.

## OpenICF interfaces implemented by the AWS Bedrock connector

The AWS Bedrock connector implements the following OpenICF interfaces. You can find additional details in [ICF interfaces](interfaces.html):

* Schema

  Describes the object types, operations, and options that the connector supports.

* Search

  Searches the target resource for all objects that match the specified object class and filter.

* Test

  Tests the connector configuration.

  Testing a configuration checks all elements of the environment that are referred to by the configuration are available. For example, the connector might make a physical connection to a host that is specified in the configuration to verify that it exists and that the credentials that are specified in the configuration are valid.

  This operation might need to connect to a resource, and, as such, might take some time. Do not invoke this operation too often, such as before every provisioning operation. The test operation is not intended to check that the connector is alive (that is, that its physical connection to the resource has not timed out).

  You can invoke the test operation before a connector configuration has been validated.

[]()

## AWS Bedrock connector configuration

The AWS Bedrock connector has the following configurable properties:

### Basic configuration properties

| Property                                                                                                                                                     | Type            | Default                  | Encrypted(1)             | Required(2)               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- | ------------------------ | ------------------------ | ------------------------- |
| `region`                                                                                                                                                     | `String`        | `us-east-1`              |                          | [icon: check, set=fas]Yes |
| AWS region where Bedrock Agents are deployed, for example `us-east-1` or `us-west-2`.                                                                        |                 |                          |                          |                           |
| `accountId`                                                                                                                                                  | `String`        | `null`                   |                          | [icon: check, set=fas]Yes |
| AWS account ID. Used to construct Bedrock Agent ARNs and relationship identifiers.                                                                           |                 |                          |                          |                           |
| `useDefaultCredentialsProvider`                                                                                                                              | `Boolean`       | `true`                   |                          | [icon: check, set=fas]Yes |
| If enabled, the connector uses the AWS SDK DefaultCredentialsProvider chain (environment variables, shared config, EC2/ECS role).                            |                 |                          |                          |                           |
| `accessKeyId`                                                                                                                                                | `String`        | `null`                   |                          | [icon: times, set=fas]No  |
| AWS access key ID used to authenticate when the default credentials provider is disabled.                                                                    |                 |                          |                          |                           |
| `secretAccessKey`                                                                                                                                            | `GuardedString` | `null`                   | [icon: lock, set=fas]Yes | [icon: times, set=fas]No  |
| AWS secret access key used to authenticate when the default credentials provider is disabled.                                                                |                 |                          |                          |                           |
| `inventoryBucket`                                                                                                                                            | `String`        | `bedrock-core-inventory` |                          | [icon: check, set=fas]Yes |
| S3 bucket containing `latest/agent-bindings.json` and `latest/agent-tool-credentials.json`. Use the bucket name only, don't include `s3://` or a key prefix. |                 |                          |                          |                           |
| `bindingsCacheTtlSeconds`                                                                                                                                    | `Long`          | `300`                    |                          | [icon: times, set=fas]No  |
| Cache TTL in seconds for S3 inventory artifacts.                                                                                                             |                 |                          |                          |                           |

(1) Whether the property value is considered confidential, and is therefore encrypted in IDM.

(2) A list of operations in this column indicates that the property is required for those operations.

---

---
title: AWS IAM Identity Center connector
description: Configure the AWS IAM Identity Center connector to manage users and groups between AWS IAM Identity Center and PingIDM
component: openicf
page_id: openicf:connector-reference:aws-iam-identity-center
canonical_url: https://docs.pingidentity.com/openicf/connector-reference/aws-iam-identity-center.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  before_you_start: Before you start
  install_the_aws_iam_identity_center_connector: Install the AWS IAM Identity Center connector
  configure_the_aws_iam_identity_center_connector: Configure the AWS IAM Identity Center connector
  config-connection-pooling-aws-iam-identity-center: Configure connection pooling
  mapping: Mapping
  test_the_aws_iam_identity_center_connector: Test the AWS IAM Identity Center connector
  use_the_aws_iam_identity_center_connector: Use the AWS IAM Identity Center connector
  AWS_IAM_IDENTITY_CENTER_USERS: User
  create_user: Create user
  get_users: Get Users
  get_user: Get user
  get_user_by_filter: Get user by filter
  get_users_ids: Get users IDs
  update_user: Update user
  delete_user: Delete user
  AWS_IAM_IDENTITY_CENTER_GROUPS: GROUPS
  create_group: Create group
  get_groups: Get groups
  get_groups_ids: Get groups IDs
  get_group: Get group
  get_group_by_filter: Get group by filter
  update_a_group: Update a group
  delete_a_group: Delete a group
  implemented-interfaces-org-forgerock-openicf-connectors-awsiam-AwsIamConnector-1.5.20.35: OpenICF Interfaces Implemented by the AWS IAM Identity Center Connector
  config-properties-org-forgerock-openicf-connectors-awsiam-AwsIamConnector-1.5.20.35: AWS IAM Identity Center Connector Configuration
  basic-configuration-properties-org-forgerock-openicf-connectors-awsiam-AwsIamConnector-1.5.20.35: Basic Configuration Properties
---

# AWS IAM Identity Center connector

The AWS IAM Identity Center connector allows you to manage users and groups, as well as manage user group memberships between the AWS IAM identity center and IDM. You need an administrator account.

## Before you start

Before you configure the connector, log in to your AWS administrator account in the web console and obtain the following data to be able to connect: `accessKey`, `secretKey`, `identityStoreId`, `region`, and `roleArn`.

## Install the AWS IAM Identity Center connector

|   |                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To check for an Advanced Identity Cloud application for this connector, refer to:- [Application management](https://docs.pingidentity.com/pingoneaic/latest/app-management/applications.html)

- [App catalog](https://docs.pingidentity.com/pingoneaic/latest/app-management/app-catalog.html) |

You can download most connectors from [Backstage](https://backstage.forgerock.com/downloads/browse/idm/featured/connectors), but some are included in the default deployment for Advanced Identity Cloud, IDM, or RCS. When using an included connector, you can skip installing it and move directly to configuration.

**Connector included in default deployment**

| Connector                                               | IDM                     | RCS                     |
| ------------------------------------------------------- | ----------------------- | ----------------------- |
| [AWS IAM Identity Center](aws-iam-identity-center.html) | [icon: times, set=fa]No | [icon: times, set=fa]No |

Download the connector .jar file from [Backstage](https://backstage.forgerock.com/downloads/browse/idm/featured/connectors).

* If you're running the connector locally, place it in the `/path/to/openidm/connectors` directory, for example:

  ```
  mv ~/Downloads/awsiam-connector-1.5.20.35.jar /path/to/openidm/connectors/
  ```

* If you're using a remote connector server (RCS), place it in the `/path/to/openicf/connectors` directory on the RCS.

## Configure the AWS IAM Identity Center connector

Create a connector configuration using the IDM admin UI:

1. From the navigation bar, click Configure > Connectors.

2. On the Connectors page, click New Connector.

3. On the New Connector page, type a Connector Name.

4. From the Connector Type list, select AWS IAM Identity Center Connector - 1.5.20.35.

5. Complete the Base Connector Details and any applicable Additional Options.

   |   |                                                                                                                                     |
   | - | ----------------------------------------------------------------------------------------------------------------------------------- |
   |   | For a list of all configuration properties, refer to [AWS IAM Identity Center Connector Configuration](#awsiam-config-prop-ezLink). |

6. Click Save.

When your connector is configured correctly, the connector displays as Active in the admin UI.

Refer to [this procedure](configure-connector.html#connector-wiz-REST) to create a connector configuration over REST.

> **Collapse: Connection details**
>
> * `Access Key ID`: The access key ID is a globally unique IAM user identifier to access the AWS service API.
>
> * `Secret Key ID`: The secret key is a password to access the AWS service API.
>
> * `Role ARN`: Amazon Resource Name (ARN) for the role which has IAM Full Access permissions.
>
> * `Session Name`: A name used to uniquely identify a user session within the identity service.
>
> * `Credentials Expiration Time`: Time (in seconds) to configure the duration in which the temporary credentials would expire. The time must be between 900 and 3600 seconds.
>
> * `Region`: The region where the AWS instance is hosted.
>
> * `Identity Store ID`: Unique identifier associated with an identity store used by AWS IAM Identity Center.
>
> * `Max connections`: Max size of the http connection pool used. Optional.
>
> * `Connection Timeout (seconds)`: Defines a timeout for the http connection in seconds. Optional.
>
> * `ProxyHost`: Proxy server host. Optional.
>
> * `ProxyPort`: Proxy server port number. Optional.
>
> * `ReadRateLimit`: Limits the request rate for read operations. The recommended rate is 20/sec.
>
> * `WriteRateLimit`: Limits the request rate for write operations. The recommended rate is 10/sec.

> **Collapse: Object Types**
>
> If necessary, add or edit your object types to have these three objects with their properties:
>
> > **Collapse:&#x20;**
> >
> > | PROPERTY NAME       | TYPE   | NATIVE TYPE | REQUIRED |
> > | ------------------- | ------ | ----------- | -------- |
> > | `_id`               | String | String      | NO       |
> > | `__NAME__`          | String | String      | YES      |
> > | `name`              | Object | Object      | YES      |
> > | `displayName`       | String | String      | YES      |
> > | `userType`          | String | String      | NO       |
> > | `profileUrl`        | String | String      | NO       |
> > | `title`             | String | String      | NO       |
> > | `preferredLanguage` | String | String      | NO       |
> > | `locale`            | String | String      | NO       |
> > | `nickName`          | String | String      | NO       |
> > | `timezone`          | String | String      | NO       |
> > | `emails`            | Array  | Object      | NO       |
> > | `phoneNumbers`      | Array  | Object      | NO       |
> > | `addresses`         | Array  | Object      | NO       |
> > | `externalIds`       | Array  | Object      | NO       |
> > | `__GROUPS__`        | Array  | String      | NO       |
>
> > **Collapse:&#x20;**
> >
> > | PROPERTY NAME | TYPE   | NATIVE TYPE | REQUIRED |
> > | ------------- | ------ | ----------- | -------- |
> > | `_id`         | String | String      | NO       |
> > | `__NAME__`    | String | String      | YES      |
> > | `description` | String | String      | NO       |
> > | `externalIds` | Array  | Object      | NO       |
>
> |   |                                                                                        |
> | - | -------------------------------------------------------------------------------------- |
> |   | The \_\_NAME\_\_ field represents the username for users and the groupName for groups. |

If configuring the connector over REST or through the filesystem, specify the connection details to the AWS IAM Identity Center resource provider in the `configurationProperties` for the connector. The minimum required properties are `accessKey`, `secretKey`, `roleArn`, `roleSessionName`, `region`, and `identityStoreId`.

> **Collapse: Sample Configuration**
>
> ```json
> {
>   "configurationProperties": {
>     "accessKey": "ACCEES_KEY",
>     "secretKey": "xxxxxxxxxxxx",
>     "roleArn": "arn:aws:iam::000000000:role/USERNAME_ROLE",
>     "roleSessionName": "SESSION_NAME",
>     "region": "us-east-2",
>     "identityStoreId": "d-0a010101e0",
>     "sessionExpirationTime": 3600,
>     "proxyHost": null,
>     "proxyPort": null,
>     "proxyUsername": null,
>     "proxyPassword": null,
>     "connectionTimeout": null,
>     "maxConnections": null,
>     "readRateLimit": "20/sec",
>     "writeRateLimit": "10/sec"
>   }
> }
> ```
>
> |   |                                                        |
> | - | ------------------------------------------------------ |
> |   | On startup, IDM encrypts the value of the `secretKey`. |

### Configure connection pooling

The AWS IAM Identity Center connector uses a [non-poolable mechanism](pooling.html#non-poolable-connectors) to manage connections. Learn more about the different pooling mechanisms in [Connectors by pooling mechanism](pooling.html#pooling-table).

## Mapping

> **Collapse: From AWS users to IDM or Advanced Identity Cloud users**
>
> Attributes mapping table where the columns represent the attribute name mapped from source to target and the necessary data transformation to synchronize successfully.
>
> | SOURCE              | TARGET              | TRANSFORMATION SCRIPT |
> | ------------------- | ------------------- | --------------------- |
> | `_id`               | `_id`               | N/A                   |
> | `__NAME__`          | `userName`          | N/A                   |
> | `displayName`       | `displayName`       | N/A                   |
> | `timezone`          | `timezone`          | N/A                   |
> | `nickname`          | `nickname`          | N/A                   |
> | `title`             | `title`             | N/A                   |
> | `locale`            | `locale`            | N/A                   |
> | `preferredLanguage` | `preferredLanguage` | N/A                   |
> | `profileUrl`        | `profileUrl`        | N/A                   |
> | `userType`          | `userType`          | N/A                   |
> | `name`              | `name`              | N/A                   |
> | `phoneNumbers`      | `phoneNumbers`      | N/A                   |
> | `addresses`         | `addresses`         | N/A                   |
> | `emails`            | `emails`            | N/A                   |
> | `externalIds`       | `externalIds`       | N/A                   |
> | `__GROUPS__`        | `groups`            | N/A                   |

> **Collapse: From IDM or Advanced Identity Cloud users to AWS users**
>
> Attributes mapping table where the columns represent the attribute name mapped from source to target and the necessary data transformation to synchronize successfully.
>
> | SOURCE              | TARGET              | TRANSFORMATION SCRIPT |
> | ------------------- | ------------------- | --------------------- |
> | `userName`          | `__NAME__`          | N/A                   |
> | `displayName`       | `displayName`       | N/A                   |
> | `timezone`          | `timezone`          | N/A                   |
> | `nickname`          | `nickname`          | N/A                   |
> | `title`             | `title`             | N/A                   |
> | `locale`            | `locale`            | N/A                   |
> | `preferredLanguage` | `preferredLanguage` | N/A                   |
> | `profileUrl`        | `profileUrl`        | N/A                   |
> | `userType`          | `userType`          | N/A                   |
> | `name`              | `name`              | N/A                   |
> | `phoneNumbers`      | `phoneNumbers`      | N/A                   |
> | `addresses`         | `addresses`         | N/A                   |
> | `emails`            | `emails`            | N/A                   |
> | `__GROUPS__`        | `groups`            | N/A                   |

> **Collapse: From AWS groups to IDM or Advanced Identity Cloud groups**
>
> Attributes mapping table where the columns represent the attribute name mapped from source to target and the necessary data transformation to synchronize successfully.
>
> | SOURCE        | TARGET        | TRANSFORMATION SCRIPT |
> | ------------- | ------------- | --------------------- |
> | `_id`         | `_id`         | N/A                   |
> | `__NAME__`    | `groupName`   | N/A                   |
> | `description` | `description` | N/A                   |
> | `externalIds` | `externalIds` | N/A                   |

> **Collapse: From IDM or Advanced Identity Cloud groups to AWS Groups**
>
> Attributes mapping table where the columns represent the attribute name mapped from source to target and the necessary data transformation to synchronize successfully.
>
> | SOURCE        | TARGET        | TRANSFORMATION SCRIPT |
> | ------------- | ------------- | --------------------- |
> | `__NAME__`    | `groupName`   | N/A                   |
> | `description` | `description` | N/A                   |

## Test the AWS IAM Identity Center connector

Test that the connector was configured correctly:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Accept-API-Version: resource=1.0' \
--request POST \
'http://localhost:8080/system/awsiam?_action=test'
{
    "name": "awsiam",
    "enabled": true,
    "config": "config/provisioner.openicf/awsiam",
    "connectorRef": {
    "bundleVersion": "1.5.20.35",
    "bundleName": "org.forgerock.openicf.connectors.awsiam-connector",
    "connectorName": "org.forgerock.openicf.connectors.awsiam.AwsIamConnector"
    },
    "displayName": "AWS IAM IC Connector",
    "objectTypes": [
    "__ACCOUNT__",
    "__ALL__",
    "__GROUP__"
    ],
    "ok": true
}
```

## Use the AWS IAM Identity Center connector

### User

#### Create user

To create a user in AWS IAM Identity Center, you must provide *at least* the `__NAME__`, `name` (givenName and familyName) and `displayName` fields.

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request POST \
--data '{
    "__NAME__": "JohnDoe",
    "displayName": "John Doe",
    "locale": "US",
    "nickName": "JonnyDoe",
    "timezone": "UTC",
    "title": "Engineer",
    "profileUrl": "https://www.profile.com/jdoe",
    "userType": "USER",
    "preferredLanguage": "us-US",
    "name": {
        "givenName": "John",
        "middleName": "Michael",
        "familyName": "Doe",
        "honorificPrefix": "Sr.",
        "honorificSufix": "PhD",
        "formatted": "Sr. John Michael Doe, PhD"
    },
    "addresses": {
        "type": "home",
        "streetAddress": "123 Main St",
        "locality": "Springfield",
        "region": "IL",
        "postalCode": "62701",
        "country": "USA",
        "primary": true,
        "formatted": "123 Main St, Springfield, IL 62701, USA"
    },
    "emails": {
        "type": "home",
        "value": "johndoe@example.com",
        "primary": true
    },
    "phoneNumbers": {
        "type": "mobile",
        "value": "+0101010101",
        "primary": true
    },
    "__GROUPS__": [
        "groupId1",
        "groupId2",
    ]
}' \
'http://localhost:8080/system/awsiam/__ACCOUNT__?_action=create'
{
    "_id" : " "userId",
    "__NAME__": "JohnDoe",
    "displayName": "John Doe",
    "locale": "US",
    "nickName": "JonnyDoe",
    "timezone": "UTC",
    "title": "Engineer",
    "profileUrl": "https://www.profile.com/jdoe",
    "userType": "USER",
    "preferredLanguage": "us-US",
    "name": {
        "givenName": "John",
        "middleName": "Michael",
        "familyName": "Doe",
        "honorificPrefix": "Sr.",
        "honorificSufix": "PhD",
        "formatted": "Sr. John Michael Doe, PhD"
    },
    "addresses": {
        "type": "home",
        "streetAddress": "123 Main St",
        "locality": "Springfield",
        "region": "IL",
        "postalCode": "62701",
        "country": "USA",
        "primary": true,
        "formatted": "123 Main St, Springfield, IL 62701, USA"
    },
    "emails": {
        "type": "home",
        "value": "johndoe@example.com",
        "primary": true
    },
    "phoneNumbers": {
        "type": "mobile",
        "value": "+0101010101",
        "primary": true
    },
    "__GROUPS__": [
        "groupId1",
        "groupId2",
    ]
}
```

#### Get Users

Return all users from AWS IAM Identity Center.

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request GET \
'http://localhost:8080/openidm/system/awsiam/__ACCOUNT__?_queryFilter=true'
{
    "result": [
        {
            "_id": "",
            "__NAME__": "jdoe",
            "displayName": "John Doe",
            "name": {
                "givenName": "John",
                "middleName": "Michael",
                "familyName": "Doe",
            },
            "addresses": [].
            "emails": [],
            "phoneNumbers": [],
            "__GROUPS__": [
                "groupId1",
                "groupId2"
            ]
        },
    ...
        {
            "_id": "",
            "__NAME__": "jdoe",
            "displayName": "John Doe",
            "name": {
                "givenName": "John",
                "middleName": "Michael",
                "familyName": "Doe",
            },
            "addresses": [].
            "emails": [],
            "phoneNumbers": [],
            "__GROUPS__": [
                "groupId1",
                "groupId2"
            ]
        },
    ],
    "resultCount": 999,
    "pagedResultsCookie": null,
    "totalPagedResultsPolicy": "NONE",
    "totalPagedResults": -1,
    "remainingPagedResults": -1
}
```

|   |                                                                   |
| - | ----------------------------------------------------------------- |
|   | To paginate the results, the maximum value of `_pageSize` is 100. |

#### Get user

Return a user from AWS IAM Identity Center. The user ID must be provided in the URI path:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request GET \
'http://localhost:8080/openidm/system/awsiam/__ACCOUNT__/USER_ID'
{
    "_id" : " "userId",
    "__NAME__": "jdoe",
    "displayName": "John Doe",
    "locale": "en-US",
    "nickname": "Johnny",
    "timezone": "America/New_York",
    "title": "Software Engineer",
    "profileUrl": "https://www.profile.com/jdoe",
    "userType": "employee",
    "preferredLanguage": "en",
    "name": {
        "givenName": "John",
        "middleName": "Michael",
        "familyName": "Doe",
        "honorificPrefix": "Sr.",
        "honorificSufix": "PhD",
        "formatted": "Sr. John Michael Doe, PhD"
    },
    "addresses": {
        "type": "home",
        "streetAddress": "123 Main St",
        "locality": "Springfield",
        "region": "IL",
        "postalCode": "62701",
        "country": "USA",
        "primary": true,
        "formatted": "123 Main St, Springfield, IL 62701, USA"
    },
    "emails": {
        "type": "work",
        "value": "john.doe@example.com",
        "primary": true
    },
    "phoneNumbers": {
        "type": "mobile",
        "value": "+0101010101",
        "primary": true
    },
    "__GROUPS__": [
        "groupId1",
        "groupId2"
    ]
}
```

#### Get user by filter

Return a user from AWS IAM Identity Center:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request GET \
'http://localhost:8080/openidm/system/awsiam/__ACCOUNT___queryFilter=__NAME__%20eq%20"name"'
{
    "_id" : " "userId",
    "__NAME__": "jdoe",
    "displayName": "John Doe",
    "locale": "en-US",
    "nickname": "Johnny",
    "timezone": "America/New_York",
    "title": "Software Engineer",
    "profileUrl": "https://www.profile.com/jdoe",
    "userType": "employee",
    "preferredLanguage": "en",
    "name": {
        "givenName": "John",
        "middleName": "Michael",
        "familyName": "Doe",
        "honorificPrefix": "Sr.",
        "honorificSufix": "PhD",
        "formatted": "Sr. John Michael Doe, PhD"
    },
    "addresses": {
        "type": "home",
        "streetAddress": "123 Main St",
        "locality": "Springfield",
        "region": "IL",
        "postalCode": "62701",
        "country": "USA",
        "primary": true,
        "formatted": "123 Main St, Springfield, IL 62701, USA"
    },
    "emails": {
        "type": "work",
        "value": "john.doe@example.com",
        "primary": true
    },
    "phoneNumbers": {
        "type": "mobile",
        "value": "+0101010101",
        "primary": true
    },
    "__GROUPS__": [
        "groupId1",
        "groupId2"
    ]
}
```

|   |                                                        |
| - | ------------------------------------------------------ |
|   | The \_\_NAME\_\_ field only supports the equal filter. |

#### Get users IDs

Return all users from AWS IAM Identity Center displaying only the `_id` field:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request GET \
'http://localhost:8080/openidm/system/awsiam/__ACCOUNT__?_queryId=query-all-ids'
{
    "result": [
        {
            "_id": "userID1"
        },
        ...
        {
            "_id": userID2"
        }
    ],
    "resultCount": 999,
    "pagedResultsCookie": null,
    "totalPagedResultsPolicy": "NONE",
    "totalPagedResults": -1,
    "remainingPagedResults": -1
}
```

#### Update user

Update a user in AWS IAM Identity Center. The user ID must be provided in the URI path:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request PUT \
--data '{
    "__NAME__": "JonnyDoe",
    "displayName": "Jonny Doe",
    "locale": "US",
    "nickName": "JonnyDoe",
    "timezone": "UTC",
    "title": "",
    "profileUrl": "https://www.profile.com/jonnydoe",
    "userType": "USER",
    "preferredLanguage": "us-US",
    "name": {
        "givenName": "Jonny",
        "middleName": "Michael",
        "familyName": "Doe",
        "honorificPrefix": "Jr.",
        "honorificSufix": "PhD",
        "formatted": "Jr. John Michael Doe, PhD"
    },
    "addresses": {
        "type": "home",
        "streetAddress": "123 Main St",
        "locality": "Springfield",
        "region": "IL",
        "postalCode": "60999",
        "country": "US",
        "primary": true,
        "formatted": "123 Main St, Springfield, IL 62701, USA"
    },
    "emails": {
        "type": "home",
        "value": "johndoe@example.com",
        "primary": true
    },
    "phoneNumbers": {
        "type": "home",
        "value": "505050",
        "primary": true
    },
    "__GROUPS__": [
        "groupID1",
        "groupID2",
    ]
}' \
'http://localhost:8080/system/awsiam/__ACCOUNT__/USER_ID'
{
    "_id" : "userId",
    "__NAME__" : "JonnyDoe",
    "displayName" : "Jonny Doe",
    "locale" : "US",
    "nickName" : "JonnyDoe",
    "timezone" : "UTC",
    "title" : "",
    "profileUrl" : "https://www.profile.com/jonnydoe",
    "userType" : "USER",
    "preferredLanguage" : "us-US",
    "name" : {
        "givenName" : "Jonny",
        "middleName" : "middleName",
        "familyName" : "Doe",
        "honorificPrefix" : "Jr",
        "honorificSufix" : "PhD",
        "formatted" : "Jr. John Doe, PhD"
    },
    "addresses": {
        "type": "home",
        "streetAddress": "123 Main St",
        "locality": "Springfield",
        "region": "IL",
        "postalCode": "60999",
        "country": "US",
        "primary": true,
        "formatted": "123 Main St, Springfield, IL 62701, USA"
    },
    "emails" : {
        "type" : "home",
        "value" : "johndoe@example.com",
        "primary" : true
    },
    "phoneNumbers" : {
        "type" : "home",
        "value" : "505050",
        "primary" : true
    },
    "__GROUPS__" : [
        "groupID1",
        "groupID2",
    ]
}
```

#### Delete user

Delete a user in the AWS IAM Identity Center. The user ID must be provided in the URI path:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request DELETE \
'http://localhost:8080/openidm/system/awsiam/__ACCOUNT__/USER_ID'
{
    "_id" : "userId",
    "__NAME__" : "JohnDoe",
    "displayName" : "John Doe",
    "locale" : "US",
    "nickName" : "JonnyDoe",
    "timezone" : "UTC",
    "title" : "",
    "profileUrl" : "www.example.doe",
    "userType" : "USER",
    "preferredLanguage" : "us-US",
    "name" : {
        "givenName" : "John",
        "middleName" : "middleName",
        "familyName" : "Doe",
        "honorificPrefix" : "Sr",
        "honorificSufix" : "PhD",
        "formatted" : "Sr. John Doe, PhD"
    },
    "addresses" : {
        "type" : "home",
        "streetAddress" : "false street",
        "locality" : "springfield",
        "region" : "north",
        "postalCode" : "0000",
        "country" : "US",
        "primary" : false,
        "formatted" : "no"
    },
    "emails" : {
        "type" : "home",
        "value" : "testeruser@example.com",
        "primary" : true
    },
    "phoneNumbers" : {
        "type" : "home",
        "value" : "505050",
        "primary" : true
    },
    "__GROUPS__" : [
        "groupID1",
        "groupID2",
    ]
}
```

### GROUPS

#### Create group

To create a group in AWS IAM Identity Center, it is necessary to *at least* provide the `__NAME__` field. The `description` field is optional:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request POST \
--data '{
    "__NAME__" : "New Group",
    "description" : "Some description"
}' \
'http://localhost:8080/openidm/system/awsiam/__GROUP__?_action=create'
{
    "_id": "groupId",
    "description": "description",
    "__NAME__": "New Group",
    "externalIds": []
}
```

#### Get groups

Return all groups from AWS IAM Identity Center.

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request GET \
'http://localhost:8080/openidm/system/awsiam/__GROUP__?_queryFilter=true'
{
    "result": [
        {
            "_id": "groupId1",
            "__NAME__": "Display name group 1",
            "description": "description",
            "externalIds": []
        },
        ...
        {
            "_id": "groupId99",
            "__NAME__": "Display name group 99",
            "description": "description",
            "externalIds": []
        }
    ],
    "resultCount": 99,
    "pagedResultsCookie": null,
    "totalPagedResultsPolicy": "NONE",
    "totalPagedResults": -1,
    "remainingPagedResults": -1
}
```

|   |                                                                   |
| - | ----------------------------------------------------------------- |
|   | To paginate the results, the maximum value of `_pageSize` is 100. |

#### Get groups IDs

Return all groups from AWS IAM Identity Center displaying only the `_id` field:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request GET \
'http://localhost:8080/openidm/system/awsiam/__GROUP__?_queryId=query-all-ids'
{
    "result": [
        {
            "_id": "groupID1",
        },
        ...
        {
            "_id": "groupID99",
        }
    ],
    "resultCount": 99,
    "pagedResultsCookie": null,
    "totalPagedResultsPolicy": "NONE",
    "totalPagedResults": -1,
    "remainingPagedResults": -1
}
```

#### Get group

Return a group from AWS IAM Identity Center. The group ID must be provided in the URI path:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request GET \
'http://localhost:8080/openidm/system/awsiam/__GROUP__/GROUP_ID'
{
    "_id": "groupId",
    "description": "Some description",
    "__NAME__": "Group Name",
    "externalIds": []
}
```

#### Get group by filter

Return a group from AWS IAM Identity Center:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request GET \
'http://localhost:8080/openidm/system/awsiam/__GROUP___queryFilter=__NAME__%20eq%20"username"'
{
    "_id": "groupId",
    "description": "Some description",
    "__NAME__": "Group Name",
    "externalIds": []
}
```

|   |                                                        |
| - | ------------------------------------------------------ |
|   | The \_\_NAME\_\_ field only supports the equal filter. |

#### Update a group

Update a group in AWS IAM Identity Center. The group ID must be provided in the URI path:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request PUT \
--header 'If-Match: *' \
--data '{
    "__NAME__" : "New DisplayName",
    "description" : "New Description"
}' \
'http://localhost:8080/openidm/system/awsiam/__GROUP__/GROUP_ID'
{
    "_id": "groupId",
    "description": "New description",
    "__NAME__": "New DisplayName",
    "externalIds": []
}
```

#### Delete a group

Delete a group in AWS IAM Identity Center. The group ID must be provided in the URI path:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request DELETE \
'http://localhost:8080/openidm/system/awsiam/__GROUP__/GROUP_ID'
{
    "_id": "groupId",
    "description": "description",
    "__NAME__": "deleted group",
    "externalIds": []
}
```

## OpenICF Interfaces Implemented by the AWS IAM Identity Center Connector

The AWS IAM Identity Center Connector implements the following OpenICF interfaces. For additional details, see [ICF interfaces](interfaces.html):

* Create

  Creates an object and its `uid`.

* Delete

  Deletes an object, referenced by its `uid`.

* Schema

  Describes the object types, operations, and options that the connector supports.

* Script on Connector

  Enables an application to run a script in the context of the connector.

  Any script that runs on the connector has the following characteristics:

  * The script runs in the same execution environment as the connector and has access to all the classes to which the connector has access.

  * The script has access to a `connector` variable that is equivalent to an initialized instance of the connector. At a minimum, the script can access the connector configuration.

  * The script has access to any script arguments passed in by the application.

* Search

  Searches the target resource for all objects that match the specified object class and filter.

* Test

  Tests the connector configuration.

  Testing a configuration checks all elements of the environment that are referred to by the configuration are available. For example, the connector might make a physical connection to a host that is specified in the configuration to verify that it exists and that the credentials that are specified in the configuration are valid.

  This operation might need to connect to a resource, and, as such, might take some time. Do not invoke this operation too often, such as before every provisioning operation. The test operation is not intended to check that the connector is alive (that is, that its physical connection to the resource has not timed out).

  You can invoke the test operation before a connector configuration has been validated.

* Update

  Updates (modifies or replaces) objects on a target resource.

[]()

## AWS IAM Identity Center Connector Configuration

The AWS IAM Identity Center Connector has the following configurable properties:

### Basic Configuration Properties

| Property                                                                                                               | Type            | Default | Encrypted(1)             | Required(2)               |
| ---------------------------------------------------------------------------------------------------------------------- | --------------- | ------- | ------------------------ | ------------------------- |
| `accessKey`                                                                                                            | `String`        | `null`  |                          | [icon: check, set=fas]Yes |
| Provides the Access Key ID to access the AWS IAM IC Service API.                                                       |                 |         |                          |                           |
| `secretKey`                                                                                                            | `GuardedString` | `null`  | [icon: lock, set=fas]Yes | [icon: check, set=fas]Yes |
| Provides the Secret Key ID to access the AWS IAM IC Service API.                                                       |                 |         |                          |                           |
| `roleArn`                                                                                                              | `String`        | `null`  |                          | [icon: check, set=fas]Yes |
| Provides the Amazon Resource Name specifying the Role.                                                                 |                 |         |                          |                           |
| `roleSessionName`                                                                                                      | `String`        | `null`  |                          | [icon: check, set=fas]Yes |
| Temporary name for the role session.                                                                                   |                 |         |                          |                           |
| `region`                                                                                                               | `String`        | `null`  |                          | [icon: check, set=fas]Yes |
| Provides the Regions.                                                                                                  |                 |         |                          |                           |
| `identityStoreId`                                                                                                      | `String`        | `null`  |                          | [icon: check, set=fas]Yes |
| Provides the identity store ID for the user and group store.                                                           |                 |         |                          |                           |
| `sessionExpirationTime`                                                                                                | `Integer`       | `3600`  |                          | [icon: check, set=fas]Yes |
| Provides the temporary Session expiration time in seconds.                                                             |                 |         |                          |                           |
| `proxyHost`                                                                                                            | `String`        | `null`  |                          | [icon: times, set=fas]No  |
| Provides the Proxy Host.                                                                                               |                 |         |                          |                           |
| `proxyPort`                                                                                                            | `String`        | `null`  |                          | [icon: times, set=fas]No  |
| Provides the Proxy Port.                                                                                               |                 |         |                          |                           |
| `proxyUsername`                                                                                                        | `String`        | `null`  |                          | [icon: times, set=fas]No  |
| Provides the Proxy Username.                                                                                           |                 |         |                          |                           |
| `proxyPassword`                                                                                                        | `GuardedString` | `null`  | [icon: lock, set=fas]Yes | [icon: times, set=fas]No  |
| Provides the Proxy Password.                                                                                           |                 |         |                          |                           |
| `connectionTimeout`                                                                                                    | `Integer`       | `null`  |                          | [icon: times, set=fas]No  |
| Provides the Maximum Connection Timeout in seconds.                                                                    |                 |         |                          |                           |
| `maxConnections`                                                                                                       | `Integer`       | `null`  |                          | [icon: times, set=fas]No  |
| Provides the number of Maximum Connections.                                                                            |                 |         |                          |                           |
| `readRateLimit`                                                                                                        | `String`        | `null`  |                          | [icon: check, set=fas]Yes |
| Defines throttling for read operations either per seconds (`30/sec`) or per minute (`100/min`).                        |                 |         |                          |                           |
| `writeRateLimit`                                                                                                       | `String`        | `null`  |                          | [icon: check, set=fas]Yes |
| Defines throttling for write operations (create/update/delete) either per second (`30/sec`) or per minute (`100/min`). |                 |         |                          |                           |

(1) Whether the property value is considered confidential, and is therefore encrypted in IDM.

(2) A list of operations in this column indicates that the property is required for those operations.

---

---
title: Azure AI Foundry connector
description: "Reference for the Azure AI Foundry connector: discover AI agents, tools, knowledge bases, guardrails, service accounts, and identity bindings."
component: openicf
page_id: openicf:connector-reference:azure-ai-foundry
canonical_url: https://docs.pingidentity.com/openicf/connector-reference/azure-ai-foundry.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  azure_ai_foundry_requirements: Azure AI Foundry requirements
  register_an_app_in_microsoft_entra: Register an app in Microsoft Entra
  install_the_azure_ai_foundry_connector: Install the Azure AI Foundry connector
  configure_the_azure_ai_foundry_connector: Configure the Azure AI Foundry connector
  connection_details: Connection details
  example_azure_ai_foundry_configuration: Example Azure AI Foundry configuration
  test_the_azure_ai_foundry_connector: Test the Azure AI Foundry connector
  azure_ai_foundry_remote_connector: Azure AI Foundry remote connector
  use_the_azure_ai_foundry_connector: Use the Azure AI Foundry connector
  account_attributes: __ACCOUNT__ attributes
  agenttool_attributes: agentTool attributes
  agentknowledgebase_attributes: agentKnowledgeBase attributes
  agentguardrail_attributes: agentGuardrail attributes
  agentidentitybinding_attributes: agentIdentityBinding attributes
  serviceaccount_attributes: serviceAccount attributes
  agenttoolcredential_attributes: agentToolCredential attributes
  agentconnection_attributes: agentConnection attributes
  implemented-interfaces-org-forgerock-openicf-connectors-azureaifoundry-AzureAIFoundryConnector-1.5.20.33: OpenICF interfaces implemented by the Azure AI Foundry connector
  config-properties-org-forgerock-openicf-connectors-azureaifoundry-AzureAIFoundryConnector-1.5.20.33: Azure AI Foundry connector configuration
  basic-configuration-properties-org-forgerock-openicf-connectors-azureaifoundry-AzureAIFoundryConnector-1.5.20.33: Basic configuration properties
---

# Azure AI Foundry connector

Azure AI Foundry is Microsoft's unified platform for building and deploying AI agents and applications. The Azure AI Foundry connector discovers AI agents created in Azure AI Foundry and governance-relevant objects including tools, knowledge bases, guardrails, connections, service accounts, and identity bindings. It supports `Delete` for agents; all other object classes are read-only.

Contact your Ping Identity Customer Success Outcome Manager (CSOM) or Account Executive to obtain this connector.

|   |                                                                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Retrieval of `agentIdentityBinding`, `serviceAccount`, `agentConnection`, and `agentToolCredential` is enabled through an offline inventory mechanism that requires an Agent Governance license. Contact your CSOM for details. |

## Azure AI Foundry requirements

Before you configure the connector, you must register an application with Microsoft Entra and configure the Azure AI Foundry project. You need a Microsoft Azure subscription to complete this procedure.

### Register an app in Microsoft Entra

1. Sign on to the [Azure portal](https://portal.azure.com/) as an administrative user.

2. Select App registrations under Azure services.

3. On the Register an application page, enter a name for the application and select the supported account types.

4. On the new registration page, make a note of the Application (client) ID and the Directory (tenant) ID.

5. Generate a client secret. Select Certificates & secrets > New client secret, enter a description, and click Add. Copy the client secret value.

6. Note the Azure subscription ID and the resource group where your Azure AI Foundry project resides.

Before you configure the connector, confirm you have the following:

| Requirement            | Value                                                                                                                |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Tenant ID              | Microsoft Entra tenant GUID                                                                                          |
| Subscription ID        | Azure subscription ID                                                                                                |
| Resource Group         | Azure Resource Group for the Foundry project                                                                         |
| Project Location       | Location of the Foundry project                                                                                      |
| Client ID              | Service principal (app registration) client ID                                                                       |
| Client Secret          | Service principal client secret                                                                                      |
| Agent Service Endpoint | Azure AI Foundry project endpoint URL, for example `https://<resource>.services.ai.azure.com/api/projects/<project>` |

## Install the Azure AI Foundry connector

|   |                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To check for an Advanced Identity Cloud application for this connector, refer to:- [Application management](https://docs.pingidentity.com/pingoneaic/latest/app-management/applications.html)

- [App catalog](https://docs.pingidentity.com/pingoneaic/latest/app-management/app-catalog.html) |

To obtain the connector `.jar` file, contact your Ping Identity Customer Success Outcome Manager (CSOM) or Account Executive.

* If you're running the connector locally, place the `.jar` file in the `/path/to/openidm/connectors` directory.

* If you're using a remote connector server (RCS), place the `.jar` file in the `/path/to/openicf/connectors` directory on the RCS.

## Configure the Azure AI Foundry connector

Create a connector configuration using the IDM admin UI:

1. From the navigation bar, click Configure > Connectors.

2. On the Connectors page, click New Connector.

3. On the New Connector page, type a Connector Name.

4. From the Connector Type list, select Azure AI Foundry Connector - 1.5.20.33.

5. Complete the Base Connector Details and any applicable Additional Options.

   |   |                                                                                                                                      |
   | - | ------------------------------------------------------------------------------------------------------------------------------------ |
   |   | For a list of all configuration properties, refer to [Azure AI Foundry Connector Configuration](#azureaifoundry-config-prop-ezLink). |

6. Click Save.

When your connector is configured correctly, the connector displays as Active in the admin UI.

Refer to [this procedure](configure-connector.html#connector-wiz-REST) to create a connector configuration over REST.

### Connection details

The Azure AI Foundry connector uses the following configuration properties:

| Property                     | Type          | Required    | Default   | Description                                                                                                                                                                                                                                                   |
| ---------------------------- | ------------- | ----------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tenantId`                   | String        | Yes         | None      | Microsoft Entra tenant GUID.                                                                                                                                                                                                                                  |
| `subscriptionId`             | String        | Yes         | None      | Azure subscription ID.                                                                                                                                                                                                                                        |
| `resourceGroupName`          | String        | No          | None      | Azure Resource Group for the Foundry project.                                                                                                                                                                                                                 |
| `workspaceName`              | String        | No          | None      | Azure AI Foundry workspace name used for agent discovery and operations.                                                                                                                                                                                      |
| `defaultLocation`            | String        | Yes         | `eastus`  | Azure region where AI Foundry resources are deployed.                                                                                                                                                                                                         |
| `useManagedIdentity`         | Boolean       | Yes         | `false`   | When `true`, uses managed identity for authentication instead of `clientId` and `clientSecret`.                                                                                                                                                               |
| `clientId`                   | String        | Conditional | None      | Service principal (app registration) client ID. Required when `useManagedIdentity=false`.                                                                                                                                                                     |
| `clientSecret`               | GuardedString | Conditional | None      | Service principal client secret. Required when `useManagedIdentity=false`.                                                                                                                                                                                    |
| `agentServiceEndpoint`       | String        | Yes         | None      | Azure AI Foundry project endpoint URL, for example `https://<resource>.services.ai.azure.com/api/projects/<project>`.                                                                                                                                         |
| `agentApiFlavor`             | String        | No          | `classic` | Agent discovery flavor. Use `classic` for the `/agents` API, `new` for the `/assistants` API, or `both`.                                                                                                                                                      |
| `apiVersion`                 | String        | No          | `v1`      | API version string used when calling the Azure AI Foundry Agents API, for example `2025-01-01`.                                                                                                                                                               |
| `identityBindingScanEnabled` | Boolean       | No          | `false`   | Enables offline inventory scan for identity bindings, service accounts, connections, and tool credentials. When `false`, those object classes return no data.                                                                                                 |
| `toolsInventoryUrl`          | String        | No          | None      | HTTPS URL to the tools inventory JSON (Azure Blob SAS URL or Azure Function HTTP trigger URL). Required when `identityBindingScanEnabled=true`.                                                                                                               |
| `toolsInventoryFilePath`     | String        | No          | None      | Local filesystem path to the tools inventory JSON. Alternative to `toolsInventoryUrl`. Intended for development or test use.                                                                                                                                  |
| `agentNameFilterRegex`       | String        | No          | None      | Optional regular expression to restrict which agents are returned during discovery based on display name.                                                                                                                                                     |
| `entraAgentIdLookupEnabled`  | Boolean       | No          | `false`   | When `true`, queries the Microsoft Graph beta API to resolve Entra agent identity service principals and enrich agents with their Entra object IDs. Requires `Application.Read.All` Graph API permission. Correlation is by agent display name (best-effort). |

### Example Azure AI Foundry configuration

```json
{
  "connectorRef": {
    "bundleName": "org.forgerock.openicf.connectors.azureaifoundry-connector",
    "bundleVersion": "[1.5.0.0,1.6.0.0)",
    "connectorName": "org.forgerock.openicf.connectors.azureaifoundry.AzureAIFoundryConnector"
  },
  "configurationProperties": {
    "tenantId": "00000000-0000-0000-0000-000000000000",
    "subscriptionId": "11111111-1111-1111-1111-111111111111",
    "resourceGroupName": "my-foundry-rg",
    "defaultLocation": "eastus",
    "clientId": "22222222-2222-2222-2222-222222222222",
    "clientSecret": {
      "$crypto": {
        "type": "x-simple-encryption",
        "value": {
          "cipher": "...",
          "data": "...",
          "iv": "...",
          "key": "openidm-sym-default"
        }
      }
    },
    "useManagedIdentity": false,
    "agentServiceEndpoint": "https://myresource.services.ai.azure.com/api/projects/myproject",
    "agentApiFlavor": "classic",
    "identityBindingScanEnabled": false
  }
}
```

### Test the Azure AI Foundry connector

Test that the configuration is correct by running the following command:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
"http://localhost:8080/openidm/system/azureaifoundry?_action=test"
{
  "name": "azureaifoundry",
  "enabled": true,
  "config": "config/provisioner.openicf/azureaifoundry",
  "connectorRef": {
    "bundleVersion": "[1.5.0.0,1.6.0.0)",
    "bundleName": "org.forgerock.openicf.connectors.azureaifoundry-connector",
    "connectorName": "org.forgerock.openicf.connectors.azureaifoundry.AzureAIFoundryConnector"
  },
  "displayName": "Azure AI Foundry Connector",
  "objectTypes": [
    "__ACCOUNT__",
    "__ALL__"
  ],
  "ok": true
}
```

If the command returns `"ok": true`, your connector has been configured correctly and can authenticate to the Azure AI Foundry API.

### Azure AI Foundry remote connector

If you want to run this connector outside of PingOne Advanced Identity Cloud or IDM, you can configure the Azure AI Foundry connector as a remote connector. Java Connectors installed remotely on a Java Connector Server function identically to those bundled locally within PingOne Advanced Identity Cloud or installed locally on IDM.

Refer to [Remote connectors](remote-connector.html) for configuring the Azure AI Foundry remote connector.

## Use the Azure AI Foundry connector

The Azure AI Foundry connector discovers the following resource types:

| ICF Native Type        | Azure AI Foundry Resource Type                                       | Naming Attribute | Notes                                                                                                                                                                                     |
| ---------------------- | -------------------------------------------------------------------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `__ACCOUNT__`          | Azure AI Foundry agent                                               | `__NAME__`       | Represents one AI Foundry agent. UID is the agent ID. Supports `Delete`; the connector calls the Azure AI Foundry agents API to delete the agent. All other object classes are read-only. |
| `agentTool`            | Agent tool                                                           | `__NAME__`       | Represents tools attached to an AI Foundry agent.                                                                                                                                         |
| `agentKnowledgeBase`   | Agent knowledge base                                                 | `__NAME__`       | Represents knowledge bases attached to an AI Foundry agent.                                                                                                                               |
| `agentIdentityBinding` | Derived IAM-to-agent identity binding                                | `__NAME__`       | Not a native Azure AI Foundry entity. Read from the offline inventory artifact.                                                                                                           |
| `agentGuardrail`       | Agent guardrail (RAI policy)                                         | `__NAME__`       | Represents the Responsible AI policy associated with an agent.                                                                                                                            |
| `serviceAccount`       | Azure managed identity or service principal associated with an agent | `__NAME__`       | Read from the offline inventory artifact.                                                                                                                                                 |
| `agentToolCredential`  | Derived tool credential surface                                      | `__NAME__`       | Read from the offline inventory artifact.                                                                                                                                                 |
| `agentConnection`      | Azure AI Foundry project connection                                  | `__NAME__`       | Represents connections (such as to Azure OpenAI or storage) configured in the Foundry project.                                                                                            |

### `__ACCOUNT__` attributes

| Attribute            | Type   | Multivalued | Description                                                    |
| -------------------- | ------ | ----------- | -------------------------------------------------------------- |
| `platform`           | String | No          | Connector platform identifier.                                 |
| `agentId`            | String | No          | Azure AI Foundry agent ID.                                     |
| `agentVersion`       | String | No          | Agent version.                                                 |
| `description`        | String | No          | Agent description.                                             |
| `foundationModel`    | String | No          | Foundation model configured for the agent.                     |
| `instructions`       | String | No          | System prompt / instructions for the agent.                    |
| `createdAt`          | String | No          | Agent creation timestamp.                                      |
| `raiPolicyName`      | String | No          | Responsible AI policy name applied to the agent.               |
| `temperature`        | Number | No          | Model temperature parameter.                                   |
| `topP`               | Number | No          | Model top-P parameter.                                         |
| `responseFormat`     | String | No          | Response format configuration.                                 |
| `toolsRaw`           | String | No          | Raw tools configuration from the agent definition.             |
| `toolResourcesRaw`   | String | No          | Raw tool resources configuration.                              |
| `guardrailId`        | String | No          | Forward pointer to the `agentGuardrail` object.                |
| `entraAgentObjectId` | String | No          | Microsoft Entra object ID associated with the agent.           |
| `serviceAccount`     | String | No          | Service account or managed identity associated with the agent. |
| `region`             | String | No          | Azure region where the agent is deployed.                      |
| `toolIds`            | String | Yes         | Forward pointers to `agentTool` objects.                       |
| `knowledgeBaseIds`   | String | Yes         | Forward pointers to `agentKnowledgeBase` objects.              |
| `identityBindingIds` | String | Yes         | Forward pointers to `agentIdentityBinding` records.            |
| `serviceAccountIds`  | String | Yes         | Forward pointers to `serviceAccount` records.                  |
| `toolCredentialIds`  | String | Yes         | Forward pointers to `agentToolCredential` records.             |
| `connectionIds`      | String | Yes         | Forward pointers to `agentConnection` records.                 |
| `connectedAgents`    | String | Yes         | IDs of connected agents.                                       |

### `agentTool` attributes

| Attribute     | Type   | Multivalued | Description                       |
| ------------- | ------ | ----------- | --------------------------------- |
| `platform`    | String | No          | Connector platform identifier.    |
| `description` | String | No          | Tool description.                 |
| `toolType`    | String | No          | Tool type classification.         |
| `executorArn` | String | No          | Executor reference, when present. |
| `schemaUri`   | String | No          | Schema URI, when present.         |

### `agentKnowledgeBase` attributes

| Attribute            | Type   | Multivalued | Description                                         |
| -------------------- | ------ | ----------- | --------------------------------------------------- |
| `platform`           | String | No          | Connector platform identifier.                      |
| `knowledgeBaseId`    | String | No          | Knowledge base ID.                                  |
| `knowledgeBaseState` | String | No          | Knowledge base state.                               |
| `sourceType`         | String | No          | Knowledge base source type.                         |
| `connectionRef`      | String | No          | Connection reference for the knowledge base source. |

### `agentGuardrail` attributes

| Attribute                | Type   | Multivalued | Description                              |
| ------------------------ | ------ | ----------- | ---------------------------------------- |
| `platform`               | String | No          | Connector platform identifier.           |
| `guardrailId`            | String | No          | Guardrail ID.                            |
| `raiPolicyName`          | String | No          | Responsible AI policy name.              |
| `raiPolicyShortName`     | String | No          | Short name for the RAI policy.           |
| `agentIdsUsingGuardrail` | String | Yes         | Agent IDs that reference this guardrail. |

### `agentIdentityBinding` attributes

| Attribute          | Type    | Multivalued | Description                                                     |
| ------------------ | ------- | ----------- | --------------------------------------------------------------- |
| `platform`         | String  | No          | Connector platform identifier.                                  |
| `agentId`          | String  | No          | Agent ID.                                                       |
| `agentVersion`     | String  | No          | Agent version.                                                  |
| `kind`             | String  | No          | Binding kind.                                                   |
| `principal`        | String  | No          | Principal reference.                                            |
| `principalId`      | String  | No          | Principal object ID.                                            |
| `principalType`    | String  | No          | Principal type, such as `User`, `Group`, or `ServicePrincipal`. |
| `roleName`         | String  | No          | Azure role name.                                                |
| `roleDefinitionId` | String  | No          | Azure role definition ID.                                       |
| `iamMember`        | String  | No          | IAM member string.                                              |
| `permissions`      | String  | Yes         | Permissions associated with the binding.                        |
| `scope`            | String  | No          | Azure RBAC scope.                                               |
| `scopeResourceId`  | String  | No          | Resource ID of the scope.                                       |
| `scopeType`        | String  | No          | Scope type.                                                     |
| `tenantId`         | String  | No          | Azure tenant ID.                                                |
| `conditionJson`    | String  | No          | Azure RBAC condition, serialized as JSON.                       |
| `sourceTag`        | String  | No          | Source tag from the inventory artifact.                         |
| `confidence`       | String  | No          | Confidence value from the inventory artifact.                   |
| `expanded`         | Boolean | No          | Whether the principal was expanded by the inventory process.    |

### `serviceAccount` attributes

| Attribute        | Type   | Multivalued | Description                                                     |
| ---------------- | ------ | ----------- | --------------------------------------------------------------- |
| `platform`       | String | No          | Connector platform identifier.                                  |
| `identityType`   | String | No          | Identity type, such as `ManagedIdentity` or `ServicePrincipal`. |
| `identityScope`  | String | No          | Identity scope.                                                 |
| `principalId`    | String | No          | Service principal or managed identity object ID.                |
| `tenantId`       | String | No          | Azure tenant ID.                                                |
| `clientId`       | String | No          | Client ID of the managed identity or service principal.         |
| `serviceAccount` | String | No          | Service account reference.                                      |
| `linkedAgentIds` | String | Yes         | Agent IDs linked to this service account.                       |

### `agentToolCredential` attributes

| Attribute           | Type   | Multivalued | Description                                            |
| ------------------- | ------ | ----------- | ------------------------------------------------------ |
| `toolId`            | String | No          | Tool ID.                                               |
| `toolType`          | String | No          | Tool type classification.                              |
| `authType`          | String | No          | Authentication type.                                   |
| `credentialRef`     | String | No          | Credential reference. Doesn't contain secret material. |
| `connectionId`      | String | No          | Connection ID used by the tool.                        |
| `connectionName`    | String | No          | Connection name used by the tool.                      |
| `target`            | String | No          | Target endpoint or resource.                           |
| `backingResourceId` | String | No          | Azure resource ID backing the tool credential.         |
| `agentIds`          | String | Yes         | Agent IDs that use this tool credential.               |

### `agentConnection` attributes

| Attribute           | Type    | Multivalued | Description                                             |
| ------------------- | ------- | ----------- | ------------------------------------------------------- |
| `platform`          | String  | No          | Connector platform identifier.                          |
| `connectionType`    | String  | No          | Connection type, such as `AzureOpenAI` or `AzureBlob`.  |
| `credentialsType`   | String  | No          | Credentials type used by the connection.                |
| `target`            | String  | No          | Connection target endpoint or resource URI.             |
| `backingResourceId` | String  | No          | Azure resource ID backing the connection.               |
| `isDefault`         | Boolean | No          | Whether this is the default connection for the project. |

## OpenICF interfaces implemented by the Azure AI Foundry connector

The Azure AI Foundry connector implements the following OpenICF interfaces. You can find additional details in [ICF interfaces](interfaces.html):

* Delete

  Deletes an object, referenced by its `uid`.

* Schema

  Describes the object types, operations, and options that the connector supports.

* Search

  Searches the target resource for all objects that match the specified object class and filter.

* Test

  Tests the connector configuration.

  Testing a configuration checks all elements of the environment that are referred to by the configuration are available. For example, the connector might make a physical connection to a host that is specified in the configuration to verify that it exists and that the credentials that are specified in the configuration are valid.

  This operation might need to connect to a resource, and, as such, might take some time. Do not invoke this operation too often, such as before every provisioning operation. The test operation is not intended to check that the connector is alive (that is, that its physical connection to the resource has not timed out).

  You can invoke the test operation before a connector configuration has been validated.

[]()

## Azure AI Foundry connector configuration

The Azure AI Foundry connector has the following configurable properties:

### Basic configuration properties

| Property                                                                                                                                                                                                                                                    | Type            | Default   | Encrypted(1)             | Required(2)               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | --------- | ------------------------ | ------------------------- |
| `tenantId`                                                                                                                                                                                                                                                  | `String`        | `null`    |                          | [icon: check, set=fas]Yes |
| Microsoft Entra tenant ID (GUID) where Azure AI Foundry resources reside.                                                                                                                                                                                   |                 |           |                          |                           |
| `subscriptionId`                                                                                                                                                                                                                                            | `String`        | `null`    |                          | [icon: check, set=fas]Yes |
| Azure subscription ID that contains the Azure AI Foundry workspace.                                                                                                                                                                                         |                 |           |                          |                           |
| `resourceGroupName`                                                                                                                                                                                                                                         | `String`        | `null`    |                          | [icon: times, set=fas]No  |
| Name of the Azure Resource Group containing the workspace.                                                                                                                                                                                                  |                 |           |                          |                           |
| `workspaceName`                                                                                                                                                                                                                                             | `String`        | `null`    |                          | [icon: times, set=fas]No  |
| Azure AI Foundry workspace name used for agent discovery and operations.                                                                                                                                                                                    |                 |           |                          |                           |
| `defaultLocation`                                                                                                                                                                                                                                           | `String`        | `eastus`  |                          | [icon: check, set=fas]Yes |
| Azure region where AI Foundry resources (agents, tools, KBs, guardrails) are deployed.                                                                                                                                                                      |                 |           |                          |                           |
| `useManagedIdentity`                                                                                                                                                                                                                                        | `Boolean`       | `false`   |                          | [icon: check, set=fas]Yes |
| If true, the connector authenticates using a managed identity attached to the runtime environment. If false, a service principal (clientId + clientSecret) is used.                                                                                         |                 |           |                          |                           |
| `clientId`                                                                                                                                                                                                                                                  | `String`        | `null`    |                          | [icon: times, set=fas]No  |
| Client ID (Application ID) of a service principal when managed identity is not used.                                                                                                                                                                        |                 |           |                          |                           |
| `clientSecret`                                                                                                                                                                                                                                              | `GuardedString` | `null`    | [icon: lock, set=fas]Yes | [icon: times, set=fas]No  |
| Client secret for the service principal. Required only when useManagedIdentity=false.                                                                                                                                                                       |                 |           |                          |                           |
| `identityBindingScanEnabled`                                                                                                                                                                                                                                | `Boolean`       | `false`   |                          | [icon: times, set=fas]No  |
| Enables scanning Azure RBAC roles to produce identity bindings. Currently optional and may require additional privileges.                                                                                                                                   |                 |           |                          |                           |
| `agentNameFilterRegex`                                                                                                                                                                                                                                      | `String`        | `null`    |                          | [icon: times, set=fas]No  |
| Optional regular expression used to restrict which agents are returned during discovery.                                                                                                                                                                    |                 |           |                          |                           |
| `agentServiceEndpoint`                                                                                                                                                                                                                                      | `String`        | `null`    |                          | [icon: check, set=fas]Yes |
| Base endpoint for Azure AI Foundry Agents API, for example `https://<resource>.services.ai.azure.com/api/projects/<project>`.                                                                                                                               |                 |           |                          |                           |
| `toolsInventoryUrl`                                                                                                                                                                                                                                         | `String`        | `null`    |                          | [icon: times, set=fas]No  |
| HTTP(S) URL pointing to the tools-inventory JSON document that includes tools, knowledge bases, guardrails, and agent relationships.                                                                                                                        |                 |           |                          |                           |
| `toolsInventoryFilePath`                                                                                                                                                                                                                                    | `String`        | `null`    |                          | [icon: times, set=fas]No  |
| Local filesystem path to the tools-inventory JSON document. Used only if `toolsInventoryUrl` is not provided.                                                                                                                                               |                 |           |                          |                           |
| `agentApiFlavor`                                                                                                                                                                                                                                            | `String`        | `classic` |                          | [icon: times, set=fas]No  |
| Agent discovery flavor. Use `classic` for the `/agents` API, `new` for the `/assistants` API, or `both`.                                                                                                                                                    |                 |           |                          |                           |
| `apiVersion`                                                                                                                                                                                                                                                | `String`        | `v1`      |                          | [icon: times, set=fas]No  |
| API version string used when calling the Azure AI Foundry Agents API, for example `2025-01-01`.                                                                                                                                                             |                 |           |                          |                           |
| `entraAgentIdLookupEnabled`                                                                                                                                                                                                                                 | `Boolean`       | `false`   |                          | [icon: times, set=fas]No  |
| When enabled, queries Microsoft Graph beta API to resolve Entra agent identity service principals and enrich agents with their Entra object IDs. Requires `Application.Read.All` Graph API permission. Correlation is by agent `displayName` (best-effort). |                 |           |                          |                           |

(1) Whether the property value is considered confidential, and is therefore encrypted in IDM.

(2) A list of operations in this column indicates that the property is required for those operations.

---

---
title: Box connector
description: "Box connector reference for PingIDM: install, configure, and use the connector to manage Box users and groups using the Box API"
component: openicf
page_id: openicf:connector-reference:box
canonical_url: https://docs.pingidentity.com/openicf/connector-reference/box.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  box-before-you-install: Before you start
  Box-install: Install the Box connector
  configure_the_box_connector: Configure the Box connector
  test_the_box_connector: Test the Box connector
  box_remote_connector: Box remote connector
  config-connection-pooling-box: Configure connection pooling
  using-box-connector: Use the Box connector
  users: Users
  box-user-create: Create a Box user
  Box-user-create-full: Create a Box full user
  list-all-box-users: List all Box users
  box-user-ids: List all Box user IDs
  box-user-get: Get Box user
  box-user-update: Update a Box user
  box-user-delete: Delete a Box user
  groups: GROUPS
  box-create-group: Create a Box group
  box-query-group: Query all Box groups
  box-get-group: Get a Box group
  box-update-group: Update a Box group
  box-delete-group: Delete a Box group
  mapping: Mapping
  implemented-interfaces-org-forgerock-openicf-connectors-box-BoxConnector-1.5.20.35: OpenICF Interfaces Implemented by the Box.com Connector
  config-properties-org-forgerock-openicf-connectors-box-BoxConnector-1.5.20.35: Box.com Connector Configuration
  basic-configuration-properties-org-forgerock-openicf-connectors-box-BoxConnector-1.5.20.35: Basic Configuration Properties
---

# Box connector

|   |                                                              |
| - | ------------------------------------------------------------ |
|   | This is a [SaaS common connector](preface.html#saas-common). |

The Box connector lets you manage Box service accounts and synchronize accounts and groups between Box and the IDM managed user repository.

This topic describes how to install and configure the Box connector and how to perform basic tests to ensure that it's running correctly.

## Before you start

The instructions in this guide assume you have a Box Administrator Account and you have created and authorized a Custom Application, as described in the [Box Documentation](https://developer.box.com/guides/getting-started/first-application/). Before you configure the connector, log in to your administrator account and note the following information:

* Client ID

* Client Secret

* Authentication Method

* Grant Type

* Subject Type

* Subject ID

* Service Uri

* Token Endpoint

## Install the Box connector

|   |                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To check for an Advanced Identity Cloud application for this connector, refer to:- [Application management](https://docs.pingidentity.com/pingoneaic/latest/app-management/applications.html)

- [App catalog](https://docs.pingidentity.com/pingoneaic/latest/app-management/app-catalog.html) |

You can download most connectors from [Backstage](https://backstage.forgerock.com/downloads/browse/idm/featured/connectors), but some are included in the default deployment for Advanced Identity Cloud, IDM, or RCS. When using an included connector, you can skip installing it and move directly to configuration.

**Connector included in default deployment**

| Connector       | IDM                     | RCS                     |
| --------------- | ----------------------- | ----------------------- |
| [Box](box.html) | [icon: times, set=fa]No | [icon: times, set=fa]No |

Download the connector .jar file from [Backstage](https://backstage.forgerock.com/downloads/browse/idm/featured/connectors).

* If you're running the connector locally, place it in the `/path/to/openidm/connectors` directory, for example:

  ```
  mv ~/Downloads/box-connector-1.5.20.35.jar /path/to/openidm/connectors/
  ```

* If you're using a remote connector server (RCS), place it in the `/path/to/openicf/connectors` directory on the RCS.

## Configure the Box connector

Create a connector configuration using the IDM admin UI:

1. From the navigation bar, click Configure > Connectors.

2. On the Connectors page, click New Connector.

3. On the New Connector page, type a Connector Name.

4. From the Connector Type list, select Box Connector - 1.5.20.35.

5. Complete the Base Connector Details and any applicable Additional Options.

   |   |                                                                                                              |
   | - | ------------------------------------------------------------------------------------------------------------ |
   |   | For a list of all configuration properties, refer to [Box Connector Configuration](#box-config-prop-ezLink). |

6. Click Save.

When your connector is configured correctly, the connector displays as Active in the admin UI.

Refer to [this procedure](configure-connector.html#connector-wiz-REST) to create a connector configuration over REST.

The following excerpt shows sample configuration properties:

```json
"configurationProperties": {
  "serviceUri" : "_CHANGEME_",
  "tokenEndpoint" : "_CHANGEME_",
  "clientId" : "_CHANGEME_",
  "clientSecret" : "_CHANGEME_",
  "acceptSelfSignedCertificates" : true,
  "disableHostNameVerifier" : true,
  "authenticationMethod" : "_CHANGEME_",
  "grantType" : "_CHANGEME_",
  "useBasicAuthForOauthTokenNeg" : false,
  "boxSubjectType" : "_CHANGEME_",
  "boxSubjectId" : "_CHANGEME_"
  "rateLimit": "_CHANGEME_"
}
```

* `serviceUri`

  The Box API hostname. In most cases it should be `https://api.box.com/2.0`.

* `tokenEndpoint`

  URL to obtain `access tokens` and `refresh tokens`. In most cases it should be `https://api.box.com/oauth2/token`.

* `clientId`

  The Box Application `Client ID`. To locate this value, log in to your Box account and go to Dev Console > Box Developer > My Apps > Select the app > Configuration > OAuth 2.0 Credentials > Client ID.

* `clientSecret`

  The Box Application `Secret Key`. To locate this value, log in to your Box account and go to Dev Console > Box Developer > My Apps > Select the app > Configuration > OAuth 2.0 Credentials > Client Secret.

* `acceptSelfSignedCertificates`

  The `acceptSelfSignedCertificates` option enables Box Sync to connect to Box servers that present self-signed digital certificates.

* `disableHostNameVerifier`

  The `disableHostNameVerifier` is a configuration option used to disable host name verification on `HTTPS` connections.

* `grantType`

  Parameter used within the `OAuth 2.0 authorization` flow to specify the type of grant being used to obtain an access token. The only value supported is `client_credentials`.

* `boxSubjectType`

  The Box Application `SubjectType`. `User` or `Enterprise`, according to availability. To locate this value, log in to your Box account and go to Dev Console > Box Developer > My Apps > Select the app > General Settings > UserID / EnterpriseID.

* `boxSubjectId`

  The Box Application `User ID` or `Enterprise ID`. It must match with the selected `boxSubjectType`. To locate this value, log in to your Box account and go to Dev Console > Box Developer > My Apps > Select the app > General Settings > UserID / EnterpriseID.

* `rateLimit`

  Limits how many requests the connector makes over a certain period of time. The default value is 1000 requests per minute (`1000/min`) as described in the [Box Documentation](https://developer.box.com/guides/api-calls/permissions-and-errors/rate-limits/). Additional examples: `997/min` or `600/sec`.

  |   |                                                                                                                                                                                                                  |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If throttling problems occur, this guide can be helpful:[Improve reconciliation query performance](https://docs.pingidentity.com/pingidm/8/synchronization-guide/chap-performance.html#recon-query-optimization) |

### Test the Box connector

Test that the configuration is correct by running the following command:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request POST \
'http://localhost:8080/openidm/system/box?_action=test'
{
  "name": "box",
  "enabled": true,
  "config": "config/provisioner.openicf/box",
  "connectorRef": {
    "bundleVersion": "[1.5.0.0,1.6.0.0)",
    "bundleName": "org.forgerock.openicf.connectors.box-connector",
    "connectorName": "org.forgerock.openicf.connectors.box.BoxConnector"
  },
  "displayName": "org.forgerock.openicf.connectors.box.BoxConnector",
  "objectTypes": [
    "__ACCOUNT__",
    "__ALL__",
    "__GROUP__"
  ],
  "ok": true
}
```

If the command returns `"ok": true`, your connector was configured correctly and can authenticate to the Box server.

### Box remote connector

If you want to run this connector outside of PingOne Advanced Identity Cloud or IDM, you can configure the Box connector as a remote connector. Java Connectors installed remotely on a Java Connector Server function identically to those bundled locally within PingOne Advanced Identity Cloud or installed locally on IDM.

Refer to [Remote connectors](remote-connector.html) for configuring the Box remote connector.

### Configure connection pooling

The Box connector supports [HTTP pooling](pooling.html#http-pooling), which can substantially improve the performance of the connector. Learn more about the basic connection pooling configuration and different pooling mechanisms described in [Connection pooling configuration](pooling.html).

## Use the Box connector

You can use the Box connector to perform the following actions on a Box account.

### Users

#### Create a Box user

This example creates a Box user with the minimum required attributes.

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \ \
--header 'Content-Type: application/json' \
--request POST \
--data '{
  "__NAME__": "Jane Doe",
  "login": "janeDoe@example.com"
}' \
'http://localhost:8080/openidm/system/box/__ACCOUNT__'
{
  "_id": "34383152830",
  "hostname": "https://app.box.com/",
  "__NAME__": "Jane Doe",
  "is_exempt_from_device_limits": "false",
  "type": "user",
  "job_title": "",
  "space_amount": "1.000000456753152E15",
  "phone": "",
  "status": "active",
  "enterprise": [
    {
      "type": "enterprise",
      "id": "1162568706",
      "name": "testing"
    }
  ],
  "can_see_managed_users": "true",
  "is_external_collab_restricted": "false",
  "external_app_user_id": null,
  "is_exempt_from_login_verification": "false",
  "is_sync_enabled": "true",
  "groups": [],
  "max_upload_size": "5.36870912E10",
  "language": "en",
  "login": "janedoe@nexter.net",
  "avatar_url": "https://app.box.com/api/avatar/large/34721687671",
  "role": "user",
  "address": "",
  "is_platform_access_only": "false"
}
```

|   |                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When you create a new user, you must specify at least the `login` and `__NAME__` attributes. The `login` attribute is typically the user's email address. |

#### Create a Box full user

This example creates a Box full user.

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request POST \
--data '{
  "__NAME__": "Miguel Benitez",
  "is_exempt_from_device_limits": "false",
  "type": "user",
  "job_title": "Designer",
  "space_amount": "1.000000456753152E15",
  "phone": "578945621",
  "status": "active",
  "enterprise": [
    {
      "type": "enterprise",
      "name": "testing"
    }
  ],
  "can_see_managed_users": "true",
  "is_external_collab_restricted": "false",
  "external_app_user_id": null,
  "is_exempt_from_login_verification": "false",
  "is_sync_enabled": "true",
  "groups": ["20013904637", "20013904699"],
  "max_upload_size": "5.36870912E10",
  "language": "en",
  "login": "someone@example.com",
  "avatar_url": "https://app.box.com/api/avatar/large/34721853021",
  "role": "user",
  "address": "San Carlos Buenos Aires",
  "is_platform_access_only": "false"
}' \
'http://localhost:8080/openidm/system/box/__ACCOUNT__'
{
  "_id": "34721853021",
  "hostname": "https://app.box.com/",
  "__NAME__": "Miguel Benitez",
  "is_exempt_from_device_limits": "false",
  "type": "user",
  "job_title": "Designer",
  "space_amount": "1.000000456753152E15",
  "phone": "578945621",
  "status": "active",
  "enterprise": [
    {
      "type": "enterprise",
      "id": "1162568706",
      "name": "testing"
    }
  ],
  "can_see_managed_users": "true",
  "is_external_collab_restricted": "false",
  "external_app_user_id": null,
  "is_exempt_from_login_verification": "false",
  "is_sync_enabled": "true",
  "groups": [
    "20013904637",
    "20013904699"
  ],
  "max_upload_size": "5.36870912E10",
  "language": "en",
  "login": "someone@example.com",
  "avatar_url": "https://app.box.com/api/avatar/large/34721853021",
  "role": "user",
  "address": "San Carlos, Buenos Aires",
  "is_platform_access_only": "false"
}
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Attribute limitations:- `job_title`: Max length 100.

- `phone`: Max length 100.

- `address`: Max length 255.

- `language`: The language of the user, formatted in a modified version of the [ISO 639-1](https://developer.box.com/guides/api-calls/language-codes/) format.

- `role`: The user's enterprise role. Value is `coadmin` or `user`.

- `status`: Value is one of `active`, `inactive`, `cannot_delete_edit`, `cannot_delete_edit_upload`.

- `space_amount`: (int64) The user's total available space in bytes. Set this to -1 to indicate unlimited storage.

- `timezone`: The user's timezone. Example: "Africa/Bujumbura". |

#### List all Box users

This example queries all Box users:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request GET \
'http://localhost:8080/openidm/system/box/__ACCOUNT__?_queryFilter=True'
{
  "result": [
    {
      "_id": "34383152830",
      "hostname": "https://app.box.com/",
      "__NAME__": "Jane Doe",
      "is_exempt_from_device_limits": "false",
      "type": "user",
      "job_title": "",
      "space_amount": "1.000000456753152E15",
      "phone": "",
      "status": "active",
      "enterprise": [
        {
          "type": "enterprise",
          "id": "1162568706",
          "name": "testing"
        }
      ],
      "can_see_managed_users": "true",
      "is_external_collab_restricted": "false",
      "external_app_user_id": null,
      "is_exempt_from_login_verification": "false",
      "is_sync_enabled": "true",
      "groups": [],
      "max_upload_size": "5.36870912E10",
      "language": "en",
      "login": "janedoe@nexter.net",
      "avatar_url": "https://app.box.com/api/avatar/large/34383152830",
      "role": "user",
      "address": "",
      "is_platform_access_only": "false"
    },
    ...
    {
      "_id": "34721853021",
      "hostname": "https://app.box.com/",
      "__NAME__": "Miguel Benitez",
      "is_exempt_from_device_limits": "false",
      "type": "user",
      "job_title": "Designer",
      "space_amount": "1.000000456753152E15",
      "phone": "578945621",
      "status": "active",
      "enterprise": [
        {
          "type": "enterprise",
          "id": "1162568706",
          "name": "testing"
        }
      ],
      "can_see_managed_users": "true",
      "is_external_collab_restricted": "false",
      "external_app_user_id": null,
      "is_exempt_from_login_verification": "false",
      "is_sync_enabled": "true",
      "groups": ["20013904637", "20013904699"],
      "max_upload_size": "5.36870912E10",
      "language": "en",
      "login": "someone@example.com",
      "avatar_url": "https://app.box.com/api/avatar/large/34721853021",
      "role": "user",
      "address": "San Carlos, Buenos Aires",
      "is_platform_access_only": "false"
    }
  ],
  "resultCount": 10,
  "pagedResultsCookie": "eyJ0eXBlIjoiaWQiLCJkaXIiOiJuZXh0IiwidGFpbCI6IjM0NzIxODUzMDIxIn0",
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": -1
}
```

|   |                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------- |
|   | * For `pagedResultsCookie`, the last page returned is empty.

* `startsWith` for `__NAME__` is the only filter available. |

#### List all Box user IDs

This example queries all Box users by their IDs:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request GET \
'http://localhost:8080/openidm/system/box/__ACCOUNT__?_queryId=query-all-ids'
{
  "result": [
    {
      "_id": "32996521506"
    },
    ...
    {
      "_id": "34721853021"
    }
  ],
  "resultCount": 10,
  "pagedResultsCookie": "eyJ0eXBlIjoiaWQiLCJkaXIiOiJuZXh0IiwidGFpbCI6IjM0NzIxODUzMDIxIn0",
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": -1
}
```

#### Get Box user

The following command queries a specific Box user by its ID:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request GET \
'http://localhost:8080/openidm/system/box/__ACCOUNT__/34721853021'
{
  "_id": "34721853021",
  "hostname": "https://app.box.com/",
  "__NAME__": "Miguel Benitez",
  "is_exempt_from_device_limits": "false",
  "type": "user",
  "job_title": "",
  "space_amount": "1.000000456753152E15",
  "phone": "578945621",
  "status": "active",
  "enterprise": [
    {
      "type": "enterprise",
      "id": "1162568706",
      "name": "testing"
    }
  ],
  "can_see_managed_users": "true",
  "is_external_collab_restricted": "false",
  "external_app_user_id": null,
  "is_exempt_from_login_verification": "false",
  "is_sync_enabled": "true",
  "groups": [
    "20013904637",
    "20013904699"
  ],
  "max_upload_size": "5.36870912E10",
  "language": "en",
  "login": "someone@example.com",
  "avatar_url": "https://app.box.com/api/avatar/large/34721853021",
  "role": "user",
  "address": "San Carlos, Buenos Aires",
  "is_platform_access_only": "false"
}
```

#### Update a Box user

The following command updates a specific Box user by its ID:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--header "If-Match: *" \
--request PUT \
--data '{
  "__NAME__": "Miguel Benitez",
  "is_exempt_from_device_limits": "false",
  "type": "user",
  "job_title": "Web Developer",
  "space_amount": "1.000000456753152E15",
  "phone": "1157199024",
  "status": "active",
  "enterprise": [
    {
      "type": "enterprise",
      "id": "1162568706",
      "name": "testing"
    }
  ],
  "can_see_managed_users": "true",
  "is_external_collab_restricted": "false",
  "external_app_user_id": null,
  "is_exempt_from_login_verification": "false",
  "is_sync_enabled": "true",
  "groups": [agregarle el grupo que esta arriba],
  "max_upload_size": "5.36870912E10",
  "language": "en",
  "avatar_url": "https://app.box.com/api/avatar/large/34721853021",
  "role": "user",
  "address": "Puerto La Cruz P.R",
  "is_platform_access_only": "false"
}' \
'http://localhost:8080/openidm/system/box/__ACCOUNT__/34721853021'
{
  "_id": "34721853021",
  "hostname": "https://app.box.com/",
  "__NAME__": "Miguel Benitez",
  "is_exempt_from_device_limits": "false",
  "type": "user",
  "job_title": "Web Developer",
  "space_amount": "9.99999999999999E14",
  "phone": "1157199024",
  "status": "active",
  "enterprise": [
    {
      "type": "enterprise",
      "id": "1162568706",
      "name": "testing"
    }
  ],
  "can_see_managed_users": "true",
  "is_external_collab_restricted": "false",
  "external_app_user_id": null,
  "is_exempt_from_login_verification": "false",
  "is_sync_enabled": "true",
  "groups": [
    "20013904637",
    "20013904699"
  ],
  "max_upload_size": "5.36870912E10",
  "language": "en",
  "login": "someone@example.com",
  "avatar_url": "https://app.box.com/api/avatar/large/34721853021",
  "role": "user",
  "address": "Puerto La Cruz, P.R",
  "is_platform_access_only": "false"
}
```

|   |                                                                                                |
| - | ---------------------------------------------------------------------------------------------- |
|   | If the target user's email is not confirmed, you can't change the primary login email address. |

#### Delete a Box user

The following example deletes a Box user:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--header "If-Match: *" \
--request DELETE \
'http://localhost:8080/openidm/system/box/__ACCOUNT__/34721853021'
{
  "_id": "34721853021",
  "is_platform_access_only": "false",
  "is_sync_enabled": "true",
  "avatar_url": "https://app.box.com/api/avatar/large/34740572881",
  "hostname": "https://app.box.com/",
  "external_app_user_id": null,
  "is_exempt_from_login_verification": "false",
  "groups": [
    "20013904637",
    "20013904699"
  ],
  "type": "user",
  "enterprise": [
    {
      "type": "enterprise",
      "id": "1162568706",
      "name": "testing"
    }
  ],
  "max_upload_size": "5.36870912E10",
  "__NAME__": "Miguel Benitez",
  "space_amount": "9.99999999999999E14",
  "language": "en",
  "is_external_collab_restricted": "false",
  "address": "Puerto La Cruz, P.R",
  "can_see_managed_users": "true",
  "job_title": "Web Developer",
  "is_exempt_from_device_limits": "false",
  "status": "active",
  "role": "user",
  "phone": "1157199024",
  "login": "someone@example.com"
}
```

|   |                                                       |
| - | ----------------------------------------------------- |
|   | The response returns the user object before deletion. |

### GROUPS

#### Create a Box group

This example creates a Box group:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request POST \
--data '{
  "type": "group",
  "description": "Support Group - as imported from Active Directory",
  "external_sync_identifier": "AD:123456",
  "group_type": "managed_group",
  "invitability_level": "admins_only",
  "member_viewability_level": "admins_only",
  "__NAME__": "Support",
  "permissions": {
    "can_invite_as_collaborator": true
  },
  "provenance": "Active Directory"
}' \
'http://localhost:8080/openidm/system/box/__GROUP__'
{
  "_id": "20147818911",
  "provenance": "Active Directory",
  "description": "Support Group - as imported from Active Directory",
  "group_type": "managed_group",
  "invitability_level": "admins_only",
  "member_viewability_level": "admins_only",
  "__NAME__": "Support",
  "type": "group",
  "external_sync_identifier": "AD:123456"
}
```

#### Query all Box groups

This example queries all Box groups:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request GET \
'http://localhost:8080/openidm/system/box/__GROUP__?_queryFilter=True'
{
  "result": [
    {
      "_id": "20005069402",
      "provenance": null,
      "description": "generic_description",
      "group_type": "managed_group",
      "invitability_level": "all_managed_users",
      "member_viewability_level": "all_managed_users",
      "__NAME__": "A_20240611161336713",
      "type": "group",
      "external_sync_identifier": null
    },
    ...
    {
      "_id": "20147818911",
      "provenance": "Active Directory",
      "description": "Support Group - as imported from Active Directory",
      "group_type": "managed_group",
      "invitability_level": "admins_only",
      "member_viewability_level": "admins_only",
      "__NAME__": "Support",
      "type": "group",
      "external_sync_identifier": "AD:123456"
    }
  ],
  "resultCount": 22,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": -1
}
```

#### Get a Box group

This example gets a Box group by its ID:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--request GET \
'http://localhost:8080/openidm/system/box/__GROUP__/20147818911'
{
  "_id": "20147818911",
  "provenance": "Active Directory",
  "description": "Support Group - as imported from Active Directory",
  "group_type": "managed_group",
  "invitability_level": "admins_only",
  "member_viewability_level": "admins_only",
  "__NAME__": "Support",
  "type": "group",
  "external_sync_identifier": "AD:123456"
}
```

#### Update a Box group

This example updates a Box group by its ID:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--header "If-Match: *" \
--request PUT \
--data '{
  "type": "group",
  "description": "Support Group - as imported from Active Directory",
  "external_sync_identifier": "AD:123456",
  "group_type": "managed_group",
  "invitability_level": "admins_only",
  "member_viewability_level": "admins_only",
  "name": "Support",
  "permissions": {
    "can_invite_as_collaborator": true
  },
  "provenance": "Active Directory"
}' \
'http://localhost:8080/openidm/system/box/__GROUP__/20147818911'
{
  "_id": "20147818911",
  "provenance": "Active Directory",
  "description": "Support Group - as imported from Active Directory",
  "group_type": "managed_group",
  "invitability_level": "admins_only",
  "member_viewability_level": "admins_only",
  "__NAME__": "Support",
  "type": "group",
  "external_sync_identifier": "AD:123456"
}
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Other fields you can update are:- `invitability_level`: Specifies who can invite the group to collaborate on folders. Available values:

  * `admins_only`

  * `admins_and_members`

  * `all_managed_users`

- `member_viewability_level`: Specifies who can see the members of the group. Available values:

  * `admins_only`

  * `admins_and_members`

  * `all_managed_users`

- `provenance`: Max length 255 |

#### Delete a Box group

This example deletes a Box group by its ID:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header 'Content-Type: application/json' \
--header "If-Match: *" \
--request DELETE \
'http://localhost:8080/openidm/system/box/__GROUP__/20147818911'
{
  "_id": "20147818911",
  "provenance": "Active Directory",
  "description": "Support Group - as imported from Active Directory",
  "group_type": "managed_group",
  "invitability_level": "admins_only",
  "member_viewability_level": "admins_only",
  "__NAME__": "Support",
  "type": "group",
  "external_sync_identifier": "AD:123456"
}
```

|   |                                                        |
| - | ------------------------------------------------------ |
|   | The response returns the group object before deletion. |

## Mapping

> **Collapse: From Box users to IDM users**
>
> Attributes Grid: Where the columns represent the attribute name mapped from source to target and the necessary data transformation to synchronize successfully.
>
> | SOURCE                              | TARGET                              | TRANSFORMATION SCRIPT |
> | ----------------------------------- | ----------------------------------- | --------------------- |
> | `id`                                | `userId`                            | N/A                   |
> | `__NAME__`                          | `UserName`                          | N/A                   |
> | `enterprise`                        | `enterprise`                        | N/A                   |
> | `external_app_user_id`              | `external_app_user_id`              | N/A                   |
> | `login`                             | `mail`                              | N/A                   |
> | `type`                              | `type`                              | N/A                   |
> | `address`                           | `address`                           | N/A                   |
> | `avatar_url`                        | `avatar_url`                        | N/A                   |
> | `can_see_managed_users`             | `can_see_managed_users`             | N/A                   |
> | `hostname`                          | `hostname`                          | N/A                   |
> | `is_exempt_from_device_limits`      | `is_exempt_from_device_limits`      | N/A                   |
> | `is_exempt_from_login_verification` | `is_exempt_from_login_verification` | N/A                   |
> | `job_title`                         | `job_title`                         | N/A                   |
> | `phone`                             | `phone`                             | N/A                   |
> | `space_amount`                      | `space_amounts`                     | N/A                   |
> | `max_upload_size`                   | `max_upload_size`                   | N/A                   |
> | `language`                          | `language`                          | N/A                   |
> | `status`                            | `status`                            | N/A                   |
> | `memberof`                          | `memberof`                          | N/A                   |
> | `is_sync_enabled`                   | `is_sync_enabled`                   | N/A                   |
> | `is_external_collab_restricted`     | `is_external_collab_restricted`     | N/A                   |
> | `is_platform_access_only`           | `is_platform_access_only`           | N/A                   |
> | `role`                              | `role`                              | N/A                   |

> **Collapse: From IDM users to Box users**
>
> Attributes Grid: Where the columns represent the attribute name mapped from source to target and the necessary data transformation to synchronize successfully.
>
> |                                     |                                     |                       |
> | ----------------------------------- | ----------------------------------- | --------------------- |
> | SOURCE                              | TARGET                              | TRANSFORMATION SCRIPT |
> | `userId`                            | `id`                                | N/A                   |
> | `UserName`                          | `__NAME__`                          | N/A                   |
> | `enterprise`                        | `enterprise`                        | N/A                   |
> | `external_app_user_id`              | `external_app_user_id`              | N/A                   |
> | `mail`                              | `login`                             | N/A                   |
> | `type`                              | `type`                              | N/A                   |
> | `address`                           | `address`                           | N/A                   |
> | `avatar_url`                        | `avatar_url`                        | N/A                   |
> | `can_see_managed_users`             | `can_see_managed_users`             | N/A                   |
> | `hostname`                          | `hostname`                          | N/A                   |
> | `is_exempt_from_device_limits`      | `is_exempt_from_device_limits`      | N/A                   |
> | `is_exempt_from_login_verification` | `is_exempt_from_login_verification` | N/A                   |
> | `job_title`                         | `job_title`                         | N/A                   |
> | `phone`                             | `phone`                             | N/A                   |
> | `space_amount`                      | `space_amounts`                     | N/A                   |
> | `max_upload_size`                   | `max_upload_size`                   | N/A                   |
> | `language`                          | `language`                          | N/A                   |
> | `status`                            | `status`                            | N/A                   |
> | `memberof`                          | `memberof`                          | N/A                   |
> | `is_sync_enabled`                   | `is_sync_enabled`                   | N/A                   |
> | `is_external_collab_restricted`     | `is_external_collab_restricted`     | N/A                   |
> | `is_platform_access_only`           | `is_platform_access_only`           | N/A                   |
> | `role`                              | `role`                              | N/A                   |

> **Collapse: From Box groups to IDM groups**
>
> Attributes Grid: Where the columns represent the attribute name mapped from source to target and the necessary data transformation to synchronize successfully.
>
> | SOURCE                     | TARGET                       | TRANSFORMATION SCRIPT               |
> | -------------------------- | ---------------------------- | ----------------------------------- |
> | `_id`                      | `_id`                        | N/A                                 |
> | `__NAME__`                 | `groupName`                  | N/A                                 |
> | `group_type`               | `group_type`                 | N/A                                 |
> | `invitability_level`       | `invitability_level`         | N/A                                 |
> | `permissions`              | `can_invite_as_collaborator` | `source.can_invite_as_collaborator` |
> | `external_sync_identifier` | `external_sync_identifier`   | N/A                                 |
> | `provenance`               | `provenance`                 | N/A                                 |
> | `description`              | `description`                | N/A                                 |
> | `member_viewability_level` | `member_viewability_level`   | N/A                                 |
> | `type`                     | `type`                       | N/A                                 |

> **Collapse: From IDM groups to Box groups**
>
> Attributes Grid: Where the columns represent the attribute name mapped from source to target and the necessary data transformation to synchronize successfully.
>
> | SOURCE                       | TARGET                     | TRANSFORMATION SCRIPT               |
> | ---------------------------- | -------------------------- | ----------------------------------- |
> | `groupName`                  | `__NAME__`                 | N/A                                 |
> | `group_type`                 | `group_type`               | N/A                                 |
> | `_id`                        | `_id`                      | N/A                                 |
> | `invitability_level`         | `invitability_level`       | N/A                                 |
> | `can_invite_as_collaborator` | `permissions`              | `source.can_invite_as_collaborator` |
> | `external_sync_identifier`   | `external_sync_identifier` | N/A                                 |
> | `provenance`                 | `provenance`               | N/A                                 |
> | `description`                | `description`              | N/A                                 |
> | `member_viewability_level`   | `member_viewability_level` | N/A                                 |
> | `type`                       | `type`                     | N/A                                 |

## OpenICF Interfaces Implemented by the Box.com Connector

The Box.com Connector implements the following OpenICF interfaces. For additional details, see [ICF interfaces](interfaces.html):

* Create

  Creates an object and its `uid`.

* Delete

  Deletes an object, referenced by its `uid`.

* Schema

  Describes the object types, operations, and options that the connector supports.

* Script on Connector

  Enables an application to run a script in the context of the connector.

  Any script that runs on the connector has the following characteristics:

  * The script runs in the same execution environment as the connector and has access to all the classes to which the connector has access.

  * The script has access to a `connector` variable that is equivalent to an initialized instance of the connector. At a minimum, the script can access the connector configuration.

  * The script has access to any script arguments passed in by the application.

* Search

  Searches the target resource for all objects that match the specified object class and filter.

* Test

  Tests the connector configuration.

  Testing a configuration checks all elements of the environment that are referred to by the configuration are available. For example, the connector might make a physical connection to a host that is specified in the configuration to verify that it exists and that the credentials that are specified in the configuration are valid.

  This operation might need to connect to a resource, and, as such, might take some time. Do not invoke this operation too often, such as before every provisioning operation. The test operation is not intended to check that the connector is alive (that is, that its physical connection to the resource has not timed out).

  You can invoke the test operation before a connector configuration has been validated.

* Update

  Updates (modifies or replaces) objects on a target resource.

[]()

## Box.com Connector Configuration

The Box.com Connector has the following configurable properties:

### Basic Configuration Properties

| Property                                                                                                                                                                                                                                        | Type            | Default                 | Encrypted(1)             | Required(2)               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | ----------------------- | ------------------------ | ------------------------- |
| `serviceUri`                                                                                                                                                                                                                                    | `String`        | `null`                  |                          | [icon: check, set=fas]Yes |
| The service endpoint URI.                                                                                                                                                                                                                       |                 |                         |                          |                           |
| `boxSubjectType`                                                                                                                                                                                                                                | `String`        | `null`                  |                          | [icon: check, set=fas]Yes |
| The type of Box subject to use for authentication. This can be either a user or a service account. A user is a Box user, while a service account is a Box application that has been granted access to a Box enterprise account.                 |                 |                         |                          |                           |
| `login`                                                                                                                                                                                                                                         | `String`        | `null`                  |                          | [icon: check, set=fas]Yes |
| The service login name.                                                                                                                                                                                                                         |                 |                         |                          |                           |
| `boxSubjectId`                                                                                                                                                                                                                                  | `String`        | `null`                  |                          | [icon: check, set=fas]Yes |
| The unique identifier of the Box subject to use for authentication. This can be either the user ID of a Box user or the client ID of a Box service account. If the Box subject type is set to user, this should be the user ID of the Box user. |                 |                         |                          |                           |
| `password`                                                                                                                                                                                                                                      | `GuardedString` | `null`                  | [icon: lock, set=fas]Yes | [icon: times, set=fas]No  |
| The service user password.                                                                                                                                                                                                                      |                 |                         |                          |                           |
| `rateLimit`                                                                                                                                                                                                                                     | `String`        | `null`                  |                          | [icon: check, set=fas]Yes |
| The rate limit for the Box API. This is the maximum number of requests that can be made to the Box API in a given time period. If not set, it will default to the limits set by Box API.                                                        |                 |                         |                          |                           |
| `authenticationMethod`                                                                                                                                                                                                                          | `String`        | `OAUTH`                 |                          | [icon: check, set=fas]Yes |
| Defines which method is to be used to authenticate on the remote server. Options are `BASIC` (username/password), `OAUTH` (Client id/secret), `JWT_TOKEN` (jwt token), or `TOKEN` (static token).                                               |                 |                         |                          |                           |
| `tokenEndpoint`                                                                                                                                                                                                                                 | `String`        | `null`                  |                          | [icon: times, set=fas]No  |
| When using OAUTH as authentication method, this property defines the endpoint where a new access token should be queried for (<https://myserver.com/oauth2/token>).                                                                             |                 |                         |                          |                           |
| `clientId`                                                                                                                                                                                                                                      | `String`        | `null`                  |                          | [icon: check, set=fas]Yes |
| Client Id of the application registered at Box.com.                                                                                                                                                                                             |                 |                         |                          |                           |
| `clientSecret`                                                                                                                                                                                                                                  | `GuardedString` | `null`                  | [icon: lock, set=fas]Yes | [icon: times, set=fas]No  |
| Client Secret of the application registered at Box.com.                                                                                                                                                                                         |                 |                         |                          |                           |
| `authToken`                                                                                                                                                                                                                                     | `GuardedString` | `null`                  | [icon: lock, set=fas]Yes | [icon: times, set=fas]No  |
| Static authentication token.                                                                                                                                                                                                                    |                 |                         |                          |                           |
| `acceptSelfSignedCertificates`                                                                                                                                                                                                                  | `boolean`       | `false`                 |                          | [icon: check, set=fas]Yes |
| To be used for debug/test purposes. To be avoided in production.                                                                                                                                                                                |                 |                         |                          |                           |
| `disableHostNameVerifier`                                                                                                                                                                                                                       | `boolean`       | `false`                 |                          | [icon: check, set=fas]Yes |
| To be used for debug/test purposes. To be avoided in production.                                                                                                                                                                                |                 |                         |                          |                           |
| `disableHttpCompression`                                                                                                                                                                                                                        | `boolean`       | `false`                 |                          | [icon: check, set=fas]Yes |
| Set this property to `true` to disable content compression.                                                                                                                                                                                     |                 |                         |                          |                           |
| `clientCertAlias`                                                                                                                                                                                                                               | `String`        | `null`                  |                          | [icon: check, set=fas]Yes |
| If TLS Mutual Auth is needed, set this to the certificate alias from the keystore.                                                                                                                                                              |                 |                         |                          |                           |
| `clientCertPassword`                                                                                                                                                                                                                            | `GuardedString` | `null`                  | [icon: lock, set=fas]Yes | [icon: check, set=fas]Yes |
| If TLS Mutual Auth is needed and the client certificate (private key) password is different from the keystore password, set this to the client private key password.                                                                            |                 |                         |                          |                           |
| `maximumConnections`                                                                                                                                                                                                                            | `Integer`       | `10`                    |                          | [icon: check, set=fas]Yes |
| Defines the max size of the HTTP connection pool used.                                                                                                                                                                                          |                 |                         |                          |                           |
| `httpProxyHost`                                                                                                                                                                                                                                 | `String`        | `null`                  |                          | [icon: check, set=fas]Yes |
| Defines the Hostname if an HTTP proxy is used between the connector and the service.                                                                                                                                                            |                 |                         |                          |                           |
| `httpProxyPort`                                                                                                                                                                                                                                 | `Integer`       | `null`                  |                          | [icon: check, set=fas]Yes |
| Defines the Port if an HTTP proxy is used between the connector and the service.                                                                                                                                                                |                 |                         |                          |                           |
| `httpProxyUsername`                                                                                                                                                                                                                             | `String`        | `null`                  |                          | [icon: check, set=fas]Yes |
| Defines Proxy Username if an HTTP proxy is used between the connector and the service.                                                                                                                                                          |                 |                         |                          |                           |
| `httpProxyPassword`                                                                                                                                                                                                                             | `GuardedString` | `null`                  | [icon: lock, set=fas]Yes | [icon: check, set=fas]Yes |
| Defines Proxy Password if an HTTP proxy is used between the connector and the service.                                                                                                                                                          |                 |                         |                          |                           |
| `connectionTimeout`                                                                                                                                                                                                                             | `int`           | `30`                    |                          | [icon: times, set=fas]No  |
| Defines a timeout for the underlying HTTP connection in seconds.                                                                                                                                                                                |                 |                         |                          |                           |
| `refreshToken`                                                                                                                                                                                                                                  | `GuardedString` | `null`                  |                          | [icon: times, set=fas]No  |
| A refresh token retrieved in the final leg of OAuth 2. In most cases these are valid for 60 days, or until used.                                                                                                                                |                 |                         |                          |                           |
| `grantType`                                                                                                                                                                                                                                     | `String`        | `null`                  |                          | [icon: times, set=fas]No  |
| The OAuth2 grant type to use (`client_credentials`, `refresh_token`, or `jwt_bearer`).                                                                                                                                                          |                 |                         |                          |                           |
| `scope`                                                                                                                                                                                                                                         | `String`        | `null`                  |                          | [icon: times, set=fas]No  |
| The OAuth2 scope to use.                                                                                                                                                                                                                        |                 |                         |                          |                           |
| `authorizationTokenPrefix`                                                                                                                                                                                                                      | `String`        | `Bearer`                |                          | [icon: times, set=fas]No  |
| The prefix to be used in the Authorization HTTP header for Token authentication.                                                                                                                                                                |                 |                         |                          |                           |
| `useBasicAuthForOauthTokenNeg`                                                                                                                                                                                                                  | `boolean`       | `true`                  |                          | [icon: check, set=fas]Yes |
| The Authentication method for refresh token (Basic Authentication or Sending the ClientId and Client Secret in the Header).                                                                                                                     |                 |                         |                          |                           |
| `jwtKey`                                                                                                                                                                                                                                        | `GuardedString` | `null`                  | [icon: lock, set=fas]Yes | [icon: times, set=fas]No  |
| The JWT data structure that represents a cryptographic key.                                                                                                                                                                                     |                 |                         |                          |                           |
| `jwtExpiration`                                                                                                                                                                                                                                 | `Integer`       | `null`                  |                          | [icon: times, set=fas]No  |
| Defines the JWT expiration time in seconds.                                                                                                                                                                                                     |                 |                         |                          |                           |
| `jwtAlgorithm`                                                                                                                                                                                                                                  | `String`        | `null`                  |                          | [icon: times, set=fas]No  |
| The Algorithm type to sign payload.                                                                                                                                                                                                             |                 |                         |                          |                           |
| `jwtClaims`                                                                                                                                                                                                                                     | `Map`           | `null`                  |                          | [icon: times, set=fas]No  |
| JWT Claims to be included in the payload                                                                                                                                                                                                        |                 |                         |                          |                           |
| `jwtPem`                                                                                                                                                                                                                                        | `GuardedString` | `null`                  | [icon: lock, set=fas]Yes | [icon: times, set=fas]No  |
| The contents of the private key of the PEM file                                                                                                                                                                                                 |                 |                         |                          |                           |
| `jwtCert`                                                                                                                                                                                                                                       | `GuardedString` | `null`                  | [icon: lock, set=fas]Yes | [icon: times, set=fas]No  |
| The contents of the certificate of the PEM file                                                                                                                                                                                                 |                 |                         |                          |                           |
| `keyAlgorithm`                                                                                                                                                                                                                                  | `String`        | `null`                  |                          | [icon: times, set=fas]No  |
| Indicates the type of key (such as RSA, DSA or EC) used to sign from the PEM.                                                                                                                                                                   |                 |                         |                          |                           |
| `userAgent`                                                                                                                                                                                                                                     | `String`        | `PingIdentityConnector` |                          | [icon: times, set=fas]No  |
| The User Agent HTTP Header used by the connector. Defaults to `PingIdentityConnector`.                                                                                                                                                          |                 |                         |                          |                           |

(1) Whether the property value is considered confidential, and is therefore encrypted in IDM.

(2) A list of operations in this column indicates that the property is required for those operations.

---

---
title: Cerner connector
description: Configure the Cerner connector to manage and synchronize healthcare accounts, organizations, and personnel groups between Cerner and PingIDM
component: openicf
page_id: openicf:connector-reference:cerner
canonical_url: https://docs.pingidentity.com/openicf/connector-reference/cerner.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  before_you_start: Before you start
  install_the_cerner_connector: Install the Cerner connector
  configure_the_cerner_connector: Configure the Cerner connector
  test_the_cerner_connector: Test the Cerner connector
  cerner_remote_connector: Cerner remote connector
  config-connection-pooling-cerner: Configure connection pooling
  use_the_cerner_connector: Use the Cerner connector
  implemented-interfaces-org-forgerock-openicf-connectors-cerner-CernerConnector-1.5.20.34: OpenICF Interfaces Implemented by the Cerner Connector
  config-properties-org-forgerock-openicf-connectors-cerner-CernerConnector-1.5.20.34: Cerner Connector Configuration
  configuration-properties-org-forgerock-openicf-connectors-cerner-CernerConnector-1.5.20.34: Configuration properties
---

# Cerner connector

Cerner is a healthcare-related service which provides an integrated healthcare IT solution for large healthcare providers. The Cerner connector lets you manage and synchronize accounts between Cerner and IDM managed user objects. A Cerner system account is required for this connector to work.

## Before you start

Before you configure the connector, log in to your Cerner system account and note the following:

* Bearer token

  The bearer token associated with your system account.

* Tenant

  Your Cerner tenant ID.

* Region

  The Cerner Cloud region where the tenant resides.

## Install the Cerner connector

|   |                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To check for an Advanced Identity Cloud application for this connector, refer to:- [Application management](https://docs.pingidentity.com/pingoneaic/latest/app-management/applications.html)

- [App catalog](https://docs.pingidentity.com/pingoneaic/latest/app-management/app-catalog.html) |

You can download most connectors from [Backstage](https://backstage.forgerock.com/downloads/browse/idm/featured/connectors), but some are included in the default deployment for Advanced Identity Cloud, IDM, or RCS. When using an included connector, you can skip installing it and move directly to configuration.

**Connector included in default deployment**

| Connector             | IDM                     | RCS                      |
| --------------------- | ----------------------- | ------------------------ |
| [Cerner](cerner.html) | [icon: times, set=fa]No | [icon: check, set=fa]Yes |

Download the connector .jar file from [Backstage](https://backstage.forgerock.com/downloads/browse/idm/featured/connectors).

* If you're running the connector locally, place it in the `/path/to/openidm/connectors` directory, for example:

  ```
  mv ~/Downloads/cerner-connector-1.5.20.34.jar /path/to/openidm/connectors/
  ```

* If you're using a remote connector server (RCS), place it in the `/path/to/openicf/connectors` directory on the RCS.

## Configure the Cerner connector

Create a connector configuration using the IDM admin UI:

1. From the navigation bar, click Configure > Connectors.

2. On the Connectors page, click New Connector.

3. On the New Connector page, type a Connector Name.

4. From the Connector Type list, select Cerner Connector - 1.5.20.34.

5. Complete the Base Connector Details and any applicable Additional Options.

   |   |                                                                                                                    |
   | - | ------------------------------------------------------------------------------------------------------------------ |
   |   | For a list of all configuration properties, refer to [Cerner Connector Configuration](#cerner-config-prop-ezLink). |

6. Click Save.

When your connector is configured correctly, the connector displays as Active in the admin UI.

Refer to [this procedure](configure-connector.html#connector-wiz-REST) to create a connector configuration over REST.

### Test the Cerner connector

Test that the configuration is correct by running the following command:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
"http://localhost:8080/openidm/system/cerner?_action=test"
{
  "name": "cerner",
  "enabled": true,
  "config": "config/provisioner.openicf/cerner",
  "connectorRef": {
    "bundleVersion": "[1.5.0.0,1.6.0.0)",
    "bundleName": "org.forgerock.openicf.connectors.cerner-connector",
    "connectorName": "org.forgerock.openicf.connectors.cerner.CernerConnector"
  },
  "displayName": "Cerner Connector",
  "objectTypes": [
    "__ORGANIZATION__",
    "__ACCOUNT__",
    "__ORGANIZATIONGROUP__",
    "__ALL__",
    "__PERSONNELGROUP__"
  ],
  "ok": true
}
```

If the command returns `"ok": true`, your connector was configured correctly, and can authenticate to the Cerner system.

### Cerner remote connector

If you want to run this connector outside of PingOne Advanced Identity Cloud or IDM, you can configure the Cerner connector as a remote connector. Java Connectors installed remotely on a Java Connector Server function identically to those bundled locally within PingOne Advanced Identity Cloud or installed locally on IDM.

Refer to [Remote connectors](remote-connector.html) for configuring the Cerner remote connector.

### Configure connection pooling

The Cerner connector supports [HTTP pooling](pooling.html#http-pooling), which can substantially improve the performance of the connector. Learn more about the basic connection pooling configuration and different pooling mechanisms described in [Connection pooling configuration](pooling.html).

## Use the Cerner connector

**Supported object types**

| Connector resource      | Cerner resource type |
| ----------------------- | -------------------- |
| `__ACCOUNT__`           | Personnel            |
| `__ORGANIZATION__`      | Organization         |
| `__PERSONNELGROUP__`    | Personnel Group      |
| `__ORGANIZATIONGROUP__` | Organization Group   |

> **Collapse: attributes**
>
> | Attribute           | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
> | ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | []()`__NAME__`      | The user's name, in a `FAMILY, GIVEN` format. Required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
> | `birthDate`         | Must be in `YYYY-MM-DD` format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
> | `gender`            | Accepted values are `MALE`, `FEMALE`, `OTHER`, `UNKNOWN`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
> | `given`             | The user's first name. Required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
> | `family`            | The user's last name. Required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
> | `name`              | given&#xA;&#xA;&#x9;&#xA;&#xA;&#xA;middle&#xA;&#xA;&#x9;&#xA;&#xA;&#xA;family&#xA;&#xA;&#x9;&#xA;&#xA;&#xA;suffix&#xA;&#xA;&#x9;&#xA;&#xA;&#xA;prefix&#xA;&#xA;	                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
> | `addresses`         | postalCode&#xA;&#xA;&#x9;&#xA;&#xA;&#xA;country&#xA;&#xA;&#x9;&#xA;&#xA;&#xA;use&#xA;&#xA;&#x9;&#xA;&#xA;Accepted values are HOME or WORK.&#xA;&#xA;&#xA;&#xA;&#xA;city&#xA;&#xA;&#x9;&#xA;&#xA;&#xA;state&#xA;&#xA;&#x9;&#xA;&#xA;&#xA;lines&#xA;&#xA;&#x9;&#xA;&#xA;The street portion of the address.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
> | `aliasType`         | Accepted values are: `SPI`, `TAX`, `SL`, `EXTERNAL`, `UPIN`, `USER`, or `UNKNOWN`. Required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
> | `aliasValue`        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
> | `aliasSystem`       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
> | `sourceIdentifiers` | id&#xA;&#xA;&#x9;&#xA;&#xA;&#xA;dataPartitionId&#xA;&#xA;	                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
> | `qualifications`    | issuer&#xA;&#xA;&#x9;&#xA;&#xA;&#xA;code&#xA;&#xA;&#x9;&#xA;&#xA;Qualification code such as MD or PhD.&#xA;&#xA;Accepted values are: AA, AAS, ABA, AE, AS, BA, BBA, BE, BFA, BN, BS, BSL, BSN, BT, CANP, CER, CMA, CNM, CNP, CNS, CPNP, CRN, CTR, DBA, DED, DIP, DO, EMT, EMTP, FPNP, HS, JD, MA, MBA, MCE, MD, MDA, MDI, ME, MED, MEE, MFA, MME, MS, MSL, MSN, MT, MTH, NG, NP, PA, PHD, PHE, PNS, PN, PharmD, RMA, RN, RPH, SEC, or TS.&#xA;&#xA;&#xA;&#xA;&#xA;start&#xA;&#xA;&#x9;&#xA;&#xA;The first date and time that the qualification is valid, in a YYYY-MM-DDThh:mm:ssZ date format.&#xA;&#xA;&#xA;&#xA;&#xA;end&#xA;&#xA;&#x9;&#xA;&#xA;The date and time that the qualification expires, in a YYYY-MM-DDThh:mm:ssZ date format. |
> | `telecoms`          | system&#xA;&#xA;&#x9;&#xA;&#xA;Accepted values are PHONE, EMAIL, or OTHER.&#xA;&#xA;&#xA;&#xA;&#xA;value&#xA;&#xA;	                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
> | `languages`         | For a list of valid language tags, refer to the *Internet Assigned Numbers Authority* (IANA) [language subtag registry](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

> **Collapse: attributes**
>
> | Attribute                 | Notes                                                                                                                                                                                                                                                                                                          |
> | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | `__NAME__`                | The name of the organization. This corresponds to `aliasValue`, `aliasSystem`, comma separated. Required.                                                                                                                                                                                                      |
> | `name`                    | The name of the organization. Required.                                                                                                                                                                                                                                                                        |
> | `aliasType`               | Alias types related to the organization. `DEA`, `TAX`, `SOI`, and `NPI` are supported for queries. Organizations with `NPI` and `DEA` cannot be created or updated.                                                                                                                                            |
> | `telecoms`                | system&#xA;&#xA;&#x9;&#xA;&#xA;Accepted values are PHONE, EMAIL, or OTHER.&#xA;&#xA;&#xA;&#xA;&#xA;value&#xA;&#xA;	                                                                                                                                                                                            |
> | `addresses`               | postalCode&#xA;&#xA;&#x9;&#xA;&#xA;&#xA;country&#xA;&#xA;&#x9;&#xA;&#xA;&#xA;text&#xA;&#xA;&#x9;&#xA;&#xA;Formatted display text of the address.&#xA;&#xA;&#xA;&#xA;&#xA;city&#xA;&#xA;&#x9;&#xA;&#xA;&#xA;state&#xA;&#xA;&#x9;&#xA;&#xA;&#xA;lines&#xA;&#xA;&#x9;&#xA;&#xA;The street portion of the address. |
> | `aliases`                 | type&#xA;&#xA;&#x9;&#xA;&#xA;Types of alias for the organization.&#xA;&#xA;&#xA;&#xA;&#xA;system&#xA;&#xA;&#x9;&#xA;&#xA;&#xA;value&#xA;&#xA;	                                                                                                                                                                 |
> | `languages`               | For a list of valid language tags, refer to the *Internet Assigned Numbers Authority* (IANA) [language subtag registry](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry).                                                                                                   |
> | `coverageAreaPostalCodes` | The postal codes indicating the area of coverage provided by the organization.                                                                                                                                                                                                                                 |
> | `sourceIdentifiers`       | id&#xA;&#xA;&#x9;&#xA;&#xA;&#xA;dataPartitionId&#xA;&#xA;	                                                                                                                                                                                                                                                     |

> **Collapse: attributes**
>
> | Attribute      | Notes                                                                                  |
> | -------------- | -------------------------------------------------------------------------------------- |
> | `__NAME__`     | A comma-separated name for the personnel group.                                        |
> | `mnemonic`     | The mnemonic determines the function of the personnel group.                           |
> | `mnemonicType` | The type of the personnel group mnemonic. Usually either `SINGLETON` or `MULTIVALUED`. |
> | `name`         | The name of the personnel group.                                                       |
> | `aliases`      | type&#xA;&#xA;&#x9;&#xA;&#xA;&#xA;system&#xA;&#xA;&#x9;&#xA;&#xA;&#xA;value&#xA;&#xA;	 |
> | `aliasType`    | The type of alias. Requires `aliasValue` and `aliasSystem`.                            |
> | `aliasSystem`  | The source of the alias value. Requires `aliasType` and `aliasValue`.                  |
> | `aliasValue`   | The unique identifier of alias. Requires `aliasType` and `aliasSystem`.                |

> **Collapse: attributes**
>
> | Attribute        | Notes                                                                                  |
> | ---------------- | -------------------------------------------------------------------------------------- |
> | `__NAME__`       | A comma-separated name for the organization group.                                     |
> | `organizationId` | A list of organization IDs that are members of the organization group.                 |
> | `name`           | The name of the organization group.                                                    |
> | `aliases`        | type&#xA;&#xA;&#x9;&#xA;&#xA;&#xA;system&#xA;&#xA;&#x9;&#xA;&#xA;&#xA;value&#xA;&#xA;	 |
> | `aliasType`      | The type of alias. Requires `aliasValue` and `aliasSystem`.                            |
> | `aliasSystem`    | The source of the alias value. Requires `aliasType` and `aliasValue`.                  |
> | `aliasValue`     | The unique identifier of alias. Requires `aliasType` and `aliasSystem`.                |

You can use the Cerner connector to perform the following actions on a Cerner account:

> **Collapse: Create a Cerner user**
>
> The following example creates a user with the minimum required attributes:
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Content-Type: application/json" \
> --request POST \
> --data '{
>   "given": "Barbara",
>   "family": "Jensen",
>   "aliasType": "USER",
>   "__NAME__": "Jensen, Barbara"
> }' \
> "http://localhost:8080/openidm/system/cerner/__ACCOUNT__?_action=create"
> {
>   "_id": "5170a9cd-e501-4cbf-a1bf-9e6d293362c6",
>   "updatedAt": "2022-04-29T22:54:08Z",
>   "given": "Barbara",
>   "name": {
>     "given": "Barbara",
>     "family": "Jensen",
>     "formatted": "Barbara Jensen"
>   },
>   "id": "5170a9cd-e501-4cbf-a1bf-9e6d293362c6",
>   "languages": [],
>   "formattedName": "Barbara Jensen",
>   "aliases": {
>     "type": "USER",
>     "value": "Jensen",
>     "system": "Barbara"
>   },
>   "aliasValue": "Jensen",
>   "__NAME__": "Jensen,Barbara",
>   "createdAt": "2022-04-29T22:54:08Z",
>   "aliasType": "USER",
>   "family": "Jensen",
>   "isManual": true,
>   "aliasSystem": "Barbara"
> }
> ```
>
> |   |                                                                                                                                                                                              |
> | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | When you create a new user, you must specify *at least* `__NAME__`, `aliasType`, `given`, and `family`. Refer to the list of [account attributes](#account-attributes) for more information. |

> **Collapse: Update a Cerner user**
>
> You can modify an existing user with a PUT request, including all attributes of the account in the request:
>
> For example, to add the user's middle name:
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Content-Type: application/json" \
> --header "If-Match:*" \
> --request PUT \
> --data '{
>   "given": "Barbara",
>   "family": "Jensen",
>   "aliasType": "USER",
>   "__NAME__": "Jensen, Barbara",
>   "name": {
>     "middle": "Simone"
>   }
> }' \
> "http://localhost:8080/openidm/system/cerner/__ACCOUNT__/5170a9cd-e501-4cbf-a1bf-9e6d293362c6"
> {
>   "_id": "5170a9cd-e501-4cbf-a1bf-9e6d293362c6",
>   "updatedAt": "2022-04-29T23:03:57Z",
>   "given": "Barbara",
>   "name": {
>     "given": "Barbara",
>     "middle": "Simone",
>     "family": "Jensen",
>     "formatted": "Barbara Simone Jensen"
>   },
>   "id": "5170a9cd-e501-4cbf-a1bf-9e6d293362c6",
>   "languages": [],
>   "formattedName": "Barbara Simone Jensen",
>   "aliases": {
>     "type": "USER",
>     "value": "Jensen",
>     "system": "Barbara"
>   },
>   "aliasValue": "Jensen",
>   "__NAME__": "Jensen,Barbara",
>   "createdAt": "2022-04-29T22:54:08Z",
>   "aliasType": "USER",
>   "family": "Jensen",
>   "isManual": true,
>   "aliasSystem": "Barbara"
> }
> ```

> **Collapse: Query Cerner users**
>
> The following example queries all Cerner users:
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Content-Type: application/json" \
> --request GET \
> "http://localhost:8080/openidm/system/cerner/__ACCOUNT__?_queryId=query-all-ids"
> {
>   "result": [
>     {
>       "_id": "7d9538c8-1c2a-4894-a403-129b35308f39"
>     },
>     {
>       "_id": "8f1c2671-9ebb-4105-9537-a3a0fc24afce"
>     },
>     {
>       "_id": "ac944860-705f-4487-99bf-6959c5e6157c"
>     },
>     {
>       "_id": "d308e459-51fa-469a-a07e-72f96906a4b4"
>     },
>     {
>       "_id": "ff9d6902-20be-4c6e-821a-5a0f3ccaebc8"
>     },
>     {
>       "_id": "bf2b9346-715e-4f59-9dc5-2bc89b8216cd"
>     },
>     {
>       "_id": "055def33-a845-4100-bcd1-2b59a3526ec5"
>     },
>     {
>       "_id": "167609b8-dfd0-4302-9022-4a3e8809b166"
>     },
>     [ ... ]
>     {
>       "_id": "9f4ea23d-bacc-46ee-b8c9-75916a5f5128"
>     },
>     {
>       "_id": "a4d6be21-a5ce-4a56-91af-94c627701d4f"
>     }
>   ],
>   "resultCount": 1020,
>   "pagedResultsCookie": null,
>   "totalPagedResultsPolicy": "NONE",
>   "totalPagedResults": -1,
>   "remainingPagedResults": -1
> }
> ```
>
> |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
> | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | Querying all ids can take a significant amount of time to return when the data set is large. Consider using paginated results instead, for example:```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Content-Type: application/json" \
> --request GET \
> "http://localhost:8080/openidm/system/cerner/__ACCOUNT__?_queryFilter=true&_fields=_id&_pageSize=2&_pagedResultsOffset=50"
> {
>   "result": [
>     {
>       "_id": "878c87d4-8322-4908-a858-555a1cb45e36"
>     },
>     {
>       "_id": "9ecaa98b-58df-4dd1-bc99-34341411b151"
>     }
>   ],
>   "resultCount": 2,
>   "pagedResultsCookie": null,
>   "totalPagedResultsPolicy": "NONE",
>   "totalPagedResults": -1,
>   "remainingPagedResults": -1
> }
> ``` |
>
> The following command queries a specific user by their ID:
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Content-Type: application/json" \
> --request GET \
> "http://localhost:8080/openidm/system/cerner/__ACCOUNT__/5170a9cd-e501-4cbf-a1bf-9e6d293362c6"
> {
>   "_id": "5170a9cd-e501-4cbf-a1bf-9e6d293362c6",
>   "updatedAt": "2022-04-29T23:03:57Z",
>   "given": "Barbara",
>   "name": {
>     "given": "Barbara",
>     "middle": "Simone",
>     "family": "Jensen",
>     "formatted": "Barbara Simone Jensen"
>   },
>   "id": "5170a9cd-e501-4cbf-a1bf-9e6d293362c6",
>   "languages": [],
>   "formattedName": "Barbara Simone Jensen",
>   "aliases": {
>     "type": "USER",
>     "value": "Jensen",
>     "system": "Barbara"
>   },
>   "aliasValue": "Jensen",
>   "__NAME__": "Jensen,Barbara",
>   "createdAt": "2022-04-29T22:54:08Z",
>   "aliasType": "USER",
>   "family": "Jensen",
>   "isManual": true,
>   "aliasSystem": "Barbara"
> }
> ```

> **Collapse: Delete a Cerner user account**
>
> You can use the Cerner connector to delete an account from the Cerner repository.
>
> The following example deletes a Cerner account:
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Content-Type: application/json" \
> --request DELETE \
> "http://localhost:8080/openidm/system/cerner/__ACCOUNT__/5170a9cd-e501-4cbf-a1bf-9e6d293362c6"
> {
>   "_id": "5170a9cd-e501-4cbf-a1bf-9e6d293362c6",
>   "updatedAt": "2022-04-29T23:03:57Z",
>   "given": "Barbara",
>   "name": {
>     "given": "Barbara",
>     "middle": "Simone",
>     "family": "Jensen",
>     "formatted": "Barbara Simone Jensen"
>   },
>   "id": "5170a9cd-e501-4cbf-a1bf-9e6d293362c6",
>   "languages": [],
>   "formattedName": "Barbara Simone Jensen",
>   "aliases": {
>     "type": "USER",
>     "value": "Jensen",
>     "system": "Barbara"
>   },
>   "aliasValue": "Jensen",
>   "__NAME__": "Jensen,Barbara",
>   "createdAt": "2022-04-29T22:54:08Z",
>   "aliasType": "USER",
>   "family": "Jensen",
>   "isManual": true,
>   "aliasSystem": "Barbara"
> }
> ```

All supported resources can be queried. You can update user accounts, organizations, organization groups, and personnel groups, but only user accounts can be created or deleted. Available additional operations include:

> **Collapse: Assign personnel groups to a user**
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Content-Type: application/json" \
> --header "If-Match:*" \
> --request PUT \
> --data '{
>   "given": "Barbara",
>   "family": "Jensen",
>   "aliasType": "USER",
>   "__NAME__": "Jensen, Barbara",
>   "name": {
>     "middle": "Simone"
>   },
>   "personnelGroupId": [
>   	"8636d4c3-de7c-4f8a-828b-b709d6bfd636"
>   ]
> }' \
> "http://localhost:8080/openidm/system/cerner/__ACCOUNT__/5170a9cd-e501-4cbf-a1bf-9e6d293362c6"
> {
>   "_id": "5170a9cd-e501-4cbf-a1bf-9e6d293362c6",
>   "formattedName": "Barbara Simone Jensen",
>   "__NAME__": "Jensen,Barbara",
>   "aliasValue": "Jensen",
>   "family": "Jensen",
>   "updatedAt": "2022-10-25T23:50:31Z",
>   "aliasType": "USER",
>   "given": "Barbara",
>   "organizationId": [],
>   "aliasSystem": "Barbara",
>   "name": {
>     "given": "Barbara",
>     "middle": "Simone",
>     "family": "Jensen",
>     "formatted": "Barbara Simone Jensen"
>   },
>   "languages": [],
>   "id": "5170a9cd-e501-4cbf-a1bf-9e6d293362c6",
>   "isManual": true,
>   "personnelGroupId": [
>     "8636d4c3-de7c-4f8a-828b-b709d6bfd636"
>   ],
>   "aliases": {
>     "type": "USER",
>     "value": "Jensen",
>     "system": "Barbara"
>   },
>   "createdAt": "2022-04-29T22:54:08Z"
> }
> ```

> **Collapse: Remove a user from a personnel group**
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Content-Type: application/json" \
> --header "If-Match:*" \
> --request PUT \
> --data '{
>   "given": "Barbara",
>   "family": "Jensen",
>   "aliasType": "USER",
>   "__NAME__": "Jensen, Barbara",
>   "name": {
>     "middle": "Simone"
>   },
>   "personnelGroupId": []
> }' \
> "http://localhost:8080/openidm/system/cerner/__ACCOUNT__/5170a9cd-e501-4cbf-a1bf-9e6d293362c6"
> {
>   "_id": "5170a9cd-e501-4cbf-a1bf-9e6d293362c6",
>   "formattedName": "Barbara Simone Jensen",
>   "__NAME__": "Jensen,Barbara",
>   "aliasValue": "Jensen",
>   "family": "Jensen",
>   "updatedAt": "2022-10-26T00:03:40Z",
>   "aliasType": "USER",
>   "given": "Barbara",
>   "organizationId": [],
>   "aliasSystem": "Barbara",
>   "name": {
>     "given": "Barbara",
>     "middle": "Simone",
>     "family": "Jensen",
>     "formatted": "Barbara Simone Jensen"
>   },
>   "languages": [],
>   "id": "5170a9cd-e501-4cbf-a1bf-9e6d293362c6",
>   "isManual": true,
>   "personnelGroupId": [],
>   "aliases": {
>     "type": "USER",
>     "value": "Jensen",
>     "system": "Barbara"
>   },
>   "createdAt": "2022-04-29T22:54:08Z"
> }
> ```

> **Collapse: Assign an organization member**
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Content-Type: application/json" \
> --header "If-Match:*" \
> --request PUT \
> --data '{
>   "given": "Barbara",
>   "family": "Jensen",
>   "aliasType": "USER",
>   "__NAME__": "Jensen, Barbara",
>   "name": {
>     "middle": "Simone"
>   },
>   "organizationId": [
>     "c66f037b-50f5-4703-b51f-838f42a49e84"
>   ]
> }' \
> "http://localhost:8080/openidm/system/cerner/__ACCOUNT__/5170a9cd-e501-4cbf-a1bf-9e6d293362c6"
> {
>   "_id": "5170a9cd-e501-4cbf-a1bf-9e6d293362c6",
>   "formattedName": "Barbara Simone Jensen",
>   "__NAME__": "Jensen,Barbara",
>   "aliasValue": "Jensen",
>   "family": "Jensen",
>   "updatedAt": "2022-10-26T00:03:40Z",
>   "aliasType": "USER",
>   "given": "Barbara",
>   "organizationId": [
>     "c66f037b-50f5-4703-b51f-838f42a49e84"
>   ],
>   "aliasSystem": "Barbara",
>   "name": {
>     "given": "Barbara",
>     "middle": "Simone",
>     "family": "Jensen",
>     "formatted": "Barbara Simone Jensen"
>   },
>   "languages": [],
>   "id": "5170a9cd-e501-4cbf-a1bf-9e6d293362c6",
>   "isManual": true,
>   "personnelGroupId": [],
>   "aliases": {
>     "type": "USER",
>     "value": "Jensen",
>     "system": "Barbara"
>   },
>   "createdAt": "2022-04-29T22:54:08Z"
> }
> ```

> **Collapse: Remove an organization member**
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Content-Type: application/json" \
> --header "If-Match:*" \
> --request PUT \
> --data '{
>   "given": "Barbara",
>   "family": "Jensen",
>   "aliasType": "USER",
>   "__NAME__": "Jensen, Barbara",
>   "name": {
>     "middle": "Simone"
>   },
>   "organizationId": []
> }' \
> "http://localhost:8080/openidm/system/cerner/__ACCOUNT__/5170a9cd-e501-4cbf-a1bf-9e6d293362c6"
> {
>   "_id": "5170a9cd-e501-4cbf-a1bf-9e6d293362c6",
>   "formattedName": "Barbara Simone Jensen",
>   "__NAME__": "Jensen,Barbara",
>   "aliasValue": "Jensen",
>   "family": "Jensen",
>   "updatedAt": "2022-10-26T00:03:40Z",
>   "aliasType": "USER",
>   "given": "Barbara",
>   "organizationId": [],
>   "aliasSystem": "Barbara",
>   "name": {
>     "given": "Barbara",
>     "middle": "Simone",
>     "family": "Jensen",
>     "formatted": "Barbara Simone Jensen"
>   },
>   "languages": [],
>   "id": "5170a9cd-e501-4cbf-a1bf-9e6d293362c6",
>   "isManual": true,
>   "personnelGroupId": [],
>   "aliases": {
>     "type": "USER",
>     "value": "Jensen",
>     "system": "Barbara"
>   },
>   "createdAt": "2022-04-29T22:54:08Z"
> }
> ```

> **Collapse: Assign an organization to an organization group**
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Content-Type: application/json" \
> --header "If-Match:*" \
> --request PUT \
> --data '{
>   "organizationId": [
>     "f90a6224-1880-4935-a838-e19d3079a23c",
>     "19b5157e-6fbe-4716-860b-28d6df90f331",
>     "c66f037b-50f5-4703-b51f-838f42a49e84"
>   ]
> }' \
> "http://localhost:8080/openidm/system/cerner/__ORGANIZATIONGROUP__/67203020-aae7-4f44-865f-c8591d618ffc"
> {
>   "_id": "67203020-aae7-4f44-865f-c8591d618ffc",
>   "organizationId": [
>     "c66f037b-50f5-4703-b51f-838f42a49e84",
>     "f90a6224-1880-4935-a838-e19d3079a23c",
>     "19b5157e-6fbe-4716-860b-28d6df90f331"
>   ],
>   "updatedAt": "2022-05-06T12:56:02Z",
>   "aliases": {
>     "type": "SOGI",
>     "value": "0001ORGVALUE",
>     "system": "0001System"
>   },
>   "id": "67203020-aae7-4f44-865f-c8591d618ffc",
>   "aliasType": "SOGI",
>   "aliasValue": "0001ORGVALUE",
>   "aliasSystem": "0001System",
>   "name": "ABC SK ORG GROUP",
>   "createdAt": "2022-05-06T12:56:02Z",
>   "__NAME__": "0001ORGVALUE,0001System"
> }
> ```

> **Collapse: Remove an organization from an organization group**
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Content-Type: application/json" \
> --header "If-Match:*" \
> --request PUT \
> --data '{
>   "organizationId": [
>     "f90a6224-1880-4935-a838-e19d3079a23c",
>     "19b5157e-6fbe-4716-860b-28d6df90f331"
>   ]
> }' \
> "http://localhost:8080/openidm/system/cerner/__ORGANIZATIONGROUP__/67203020-aae7-4f44-865f-c8591d618ffc"
> {
>   "_id": "67203020-aae7-4f44-865f-c8591d618ffc",
>   "organizationId": [
>     "f90a6224-1880-4935-a838-e19d3079a23c",
>     "19b5157e-6fbe-4716-860b-28d6df90f331"
>   ],
>   "updatedAt": "2022-05-06T12:56:02Z",
>   "aliases": {
>     "type": "SOGI",
>     "value": "0001ORGVALUE",
>     "system": "0001System"
>   },
>   "id": "67203020-aae7-4f44-865f-c8591d618ffc",
>   "aliasType": "SOGI",
>   "aliasValue": "0001ORGVALUE",
>   "aliasSystem": "0001System",
>   "name": "ABC SK ORG GROUP",
>   "createdAt": "2022-05-06T12:56:02Z",
>   "__NAME__": "0001ORGVALUE,0001System"
> }
> ```

## OpenICF Interfaces Implemented by the Cerner Connector

The Cerner Connector implements the following OpenICF interfaces. For additional details, see [ICF interfaces](interfaces.html):

* Create

  Creates an object and its `uid`.

* Delete

  Deletes an object, referenced by its `uid`.

* Schema

  Describes the object types, operations, and options that the connector supports.

* Script on Connector

  Enables an application to run a script in the context of the connector.

  Any script that runs on the connector has the following characteristics:

  * The script runs in the same execution environment as the connector and has access to all the classes to which the connector has access.

  * The script has access to a `connector` variable that is equivalent to an initialized instance of the connector. At a minimum, the script can access the connector configuration.

  * The script has access to any script arguments passed in by the application.

* Search

  Searches the target resource for all objects that match the specified object class and filter.

* Test

  Tests the connector configuration.

  Testing a configuration checks all elements of the environment that are referred to by the configuration are available. For example, the connector might make a physical connection to a host that is specified in the configuration to verify that it exists and that the credentials that are specified in the configuration are valid.

  This operation might need to connect to a resource, and, as such, might take some time. Do not invoke this operation too often, such as before every provisioning operation. The test operation is not intended to check that the connector is alive (that is, that its physical connection to the resource has not timed out).

  You can invoke the test operation before a connector configuration has been validated.

* Update

  Updates (modifies or replaces) objects on a target resource.

[]()

## Cerner Connector Configuration

The Cerner Connector has the following configurable properties:

### Configuration properties

| Property                                            | Type            | Default      | Encrypted(1)             | Required(2)               |
| --------------------------------------------------- | --------------- | ------------ | ------------------------ | ------------------------- |
| `bearerToken`                                       | `GuardedString` | `null`       | [icon: lock, set=fas]Yes | [icon: check, set=fas]Yes |
| Provides the bearer token to authorize Cerner.      |                 |              |                          |                           |
| `tenant`                                            | `String`        | `playground` |                          | [icon: times, set=fas]No  |
| Provides the tenant to authorize Cerner.            |                 |              |                          |                           |
| `region`                                            | `String`        | `us-1`       |                          | [icon: times, set=fas]No  |
| Provides the region to authorize Cerner.            |                 |              |                          |                           |
| `maximumConnections`                                | `Integer`       | `10`         |                          | [icon: times, set=fas]No  |
| Provides the maximum connections.                   |                 |              |                          |                           |
| `connectionTimeout`                                 | `Integer`       | `300`        |                          | [icon: times, set=fas]No  |
| Provides the maximum connection timeout in seconds. |                 |              |                          |                           |
| `httpProxyHost`                                     | `String`        | `null`       |                          | [icon: check, set=fas]Yes |
| Provides the Proxy Host.                            |                 |              |                          |                           |
| `httpProxyPort`                                     | `Integer`       | `null`       |                          | [icon: check, set=fas]Yes |
| Provides the Proxy Port.                            |                 |              |                          |                           |
| `httpProxyUsername`                                 | `String`        | `null`       |                          | [icon: check, set=fas]Yes |
| Provides the Proxy Username.                        |                 |              |                          |                           |
| `httpProxyPassword`                                 | `GuardedString` | `null`       | [icon: lock, set=fas]Yes | [icon: check, set=fas]Yes |
| Provides the Proxy Password.                        |                 |              |                          |                           |

(1) Whether the property value is considered confidential, and is therefore encrypted in IDM.

(2) A list of operations in this column indicates that the property is required for those operations.

---

---
title: Configure a remote connector server (RCS)
description: How to configure a Remote Connector Server (RCS) with PingIDM in client or server mode, including SSL, failover groups, and ConnectorServer.properties settings
component: openicf
page_id: openicf:connector-reference:configure-server
canonical_url: https://docs.pingidentity.com/openicf/connector-reference/configure-server.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  rcs-properties: RCS configuration properties
  mask-clear-text-passwords-rcs: Mask clear text passwords in RCS
  use-openicfopts-env-var: Use OPENICF_OPTS environment variables
  icfservlet_configuration_options: ICFServlet configuration options
  configure-rcs-client-mode: Configure RCS in client mode
  configure-rcs-server-mode: Configure RCS in server mode
  rcs-failover: Configure failover between RCS servers
  configure-rcs-ssl: Secure the connection to the RCS with SSL
  configure_the_rcs_for_ssl: Configure the RCS for SSL
  configure_idm_for_ssl: Configure IDM for SSL
  generate_keys_for_an_rcs_in_server_mode: Generate keys for an RCS in server mode
  generate_keys_for_an_rcs_in_client_mode: Generate keys for an RCS in client mode
---

# Configure a remote connector server (RCS)

RCS runs in one of two modes:

* Client mode

  In client mode, RCS initiates the connection with IDM. Run the RCS in client mode if you need to communicate with a system that's behind a firewall and IDM is outside that firewall (such as Advanced Identity Cloud).

  The following diagram shows an RCS in client mode:

  ![connector-server-client](_images/connector-server-client.png)

* Server mode

  In server mode, RCS acts as the server, with IDM acting as a client. IDM initiates the connection with the RCS. Run the RCS in server mode if IDM can initiate the connection.

  The following diagram shows an RCS in server mode:

  ![connector-server-server](_images/connector-server-server.png)

This example shows how to retrieve the RCS types over REST:

> **Collapse: List the RCS types**
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Accept-API-Version: resource=1.0" \
> --request POST \
> "http://localhost:8080/openidm/system?_action=availableConnectorServers"
> {
>   "connectorServers": [
>     {
>       "displayName": "Remote Connector Server",
>       "systemType": "provisioner.openicf",
>       "type": "remoteConnectorServer"
>     },
>     {
>       "displayName": "Remote Connector Servers Group",
>       "systemType": "provisioner.openicf",
>       "type": "remoteConnectorServersGroup"
>     },
>     {
>       "displayName": "Remote Connector Server in Client mode",
>       "systemType": "provisioner.openicf",
>       "type": "remoteConnectorClient"
>     },
>     {
>       "displayName": "Remote Connector Servers Group in Client mode",
>       "systemType": "provisioner.openicf",
>       "type": "remoteConnectorClientsGroup"
>     }
>   ]
> }
> ```

## RCS configuration properties

The following table displays the complete list of RCS configuration properties with truncated property names for readability. The full name for each property is prefixed with `connectorserver.` in the `conf/ConnectorServer.properties` configuration file included with RCS.

Time interval properties

The default values for the `nameInterval` and `webSocketConnections` properties are suitable for most RCS deployments. Don't adjust these property values without specific guidance from Ping.

**RCS properties**

| Property                                                                                                                                                                                                                                                                   | RCS Mode   (Server or Client) | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Example                                                                                                                                                                             |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connectorServerName`                                                                                                                                                                                                                                                      | Client                        | Name of the remote connector client. This name is used to identify the remote connector server in the list of connector reference objects. The name must be lower case alphanumeric characters (`^[a-z0-9]*$`), and must match the `name` property in the `provisioner.openicf.connectorinfoprovider.json` file on your IDM server.                                                                                                                                                                                        | rcs1                                                                                                                                                                                |
| `url`                                                                                                                                                                                                                                                                      | Client                        | The IDM or Advanced Identity Cloud server URL. To use multiple values, use the applicable delimiter:- For Java RCS *not* deployed in a Docker container, separate each value with a space.

- For Java RCS deployed in a Docker container, separate each value with a comma (only supported for version 1.5.20.26 and later).                                                                                                                                                                                              | `wss://openidm.example.com:8443/openicf` \[[1](#_footnotedef_1 "View footnote.")]***[1](#_footnoteref_1). Note the `wss` (WebSocket transport protocol) and the `openicf` endpoint. |
| `hostId`                                                                                                                                                                                                                                                                   | Client                        | Unique identifier for the RCS.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `MY_UNIQUE_RCS_HOST_ID`                                                                                                                                                             |
| `proxyHost`                                                                                                                                                                                                                                                                | Client                        | Proxy server host.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                     |
| `proxyPort`                                                                                                                                                                                                                                                                | Client                        | Proxy server port number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                     |
| `proxyPrincipal`                                                                                                                                                                                                                                                           | Client                        | Proxy server principal.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                     |
| `proxyPassword`                                                                                                                                                                                                                                                            | Client                        | Proxy server password.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                     |
| `housekeepingInterval`                                                                                                                                                                                                                                                     | Client                        | Interval at which RCS checks WebSockets to determine if they should be closed and recycled according to the specified interval, in seconds.                                                                                                                                                                                                                                                                                                                                                                                | 20                                                                                                                                                                                  |
| `groupCheckInterval`                                                                                                                                                                                                                                                       | Client                        | Interval at which RCS checks WebSocket connection groups (group of WebSocket connections associated with the same IDM <-> RCS link) to see if they should be closed, in seconds. WebSocket connection groups are closed when they no longer contain any active WebSocket connections.                                                                                                                                                                                                                                      | 60                                                                                                                                                                                  |
| `webSocketConnections`                                                                                                                                                                                                                                                     | Client                        | Number of WebSocket connections to open.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 2                                                                                                                                                                                   |
| `connectionTtl`                                                                                                                                                                                                                                                            | Client                        | Time to live of a WebSocket connection, in seconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 300                                                                                                                                                                                 |
| `newConnectionsInterval`                                                                                                                                                                                                                                                   | Client                        | Interval at which RCS establishes new WebSocket connections, in seconds. Ensures that connection establishment is staggered.                                                                                                                                                                                                                                                                                                                                                                                               | 10                                                                                                                                                                                  |
| `tokenEndpoint`                                                                                                                                                                                                                                                            | Client                        | Token endpoint from which to retrieve the access token if you are using OAuth2 to authenticate against AM.                                                                                                                                                                                                                                                                                                                                                                                                                 | `https://am.example.com/am/oauth2/realms/root/access_token`                                                                                                                         |
| `scope`                                                                                                                                                                                                                                                                    | Client                        | OAuth2 token scope, if you're using OAuth2 to authenticate against AM.                                                                                                                                                                                                                                                                                                                                                                                                                                                     | fr:idm:\*                                                                                                                                                                           |
| `clientId`                                                                                                                                                                                                                                                                 | Client                        | OAuth2 Client ID used to request an access token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | RCSClient                                                                                                                                                                           |
| 	If the RCS is authenticating against AM, you must update your IDM authentication configuration (in conf/authentication.json). Add a user mapping for this client ID in the rsFilter authentication module configuration. Learn more about how to Authenticate through AM. |                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                     |
| `clientSecret`                                                                                                                                                                                                                                                             | Client                        | OAuth2 Client Secret.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | openidm                                                                                                                                                                             |
| `pingPongInterval`                                                                                                                                                                                                                                                         | Both                          | Interval at which RCS sends ping/pong messages between IDM <-> RCS, in seconds. Used to determine health/connectivity of the underlying WebSocket connection. The purpose of the *ping* is to keep connections alive (for firewalls or load balancers that honor connections in use). If your firewall or load balancer doesn't honor connections in use (that is, connections are timed out, regardless of their usage), the ping has no effect, and you should disable it. Set this property to `0` to disable the ping. | 60                                                                                                                                                                                  |
| `trustStoreFile`                                                                                                                                                                                                                                                           | Both                          | The IDM truststore file. You don't need to set this property if the IDM certificate is a CA-signed certificate.                                                                                                                                                                                                                                                                                                                                                                                                            | `security/truststore.pkcs12`                                                                                                                                                        |
| `trustStoreType`                                                                                                                                                                                                                                                           | Both                          | The IDM truststore type. You don't need to set this property if the IDM certificate is a CA-signed certificate.                                                                                                                                                                                                                                                                                                                                                                                                            | `PKCS12`                                                                                                                                                                            |
| `trustStorePass`                                                                                                                                                                                                                                                           | Both                          | The IDM truststore password. You don't need to set this property if the IDM certificate is a CA-signed certificate.                                                                                                                                                                                                                                                                                                                                                                                                        | changeit                                                                                                                                                                            |
| `keyStoreFile`                                                                                                                                                                                                                                                             | Both                          | The IDM keystore file. You don't need to set this property if the IDM certificate is a CA-signed certificate.                                                                                                                                                                                                                                                                                                                                                                                                              | `security/keyStore.pkcs12`                                                                                                                                                          |
| `keyStoreType`                                                                                                                                                                                                                                                             | Both                          | The IDM keystore type. You don't need to set this property if the IDM certificate is a CA-signed certificate.                                                                                                                                                                                                                                                                                                                                                                                                              | `PKCS12`                                                                                                                                                                            |
| `keyStorePass`                                                                                                                                                                                                                                                             | Both                          | The IDM keystore password. You don't need to set this property if the IDM certificate is a CA-signed certificate.                                                                                                                                                                                                                                                                                                                                                                                                          | changeit                                                                                                                                                                            |
| `keyPass`                                                                                                                                                                                                                                                                  | Both                          | The IDM certificate password. You don't need to set this property if the IDM certificate is a CA-signed certificate.                                                                                                                                                                                                                                                                                                                                                                                                       | changeit                                                                                                                                                                            |
| `libDir`                                                                                                                                                                                                                                                                   | Both                          | Directory on the RCS host in which connector library file dependencies are located (relative to `/path/to/openicf/`).                                                                                                                                                                                                                                                                                                                                                                                                      | `lib`                                                                                                                                                                               |
| `bundleDir`                                                                                                                                                                                                                                                                | Both                          | Directory on the RCS host in which connector .jar files are located (relative to `/path/to/openicf/`).                                                                                                                                                                                                                                                                                                                                                                                                                     | `connectors`                                                                                                                                                                        |
| `loggerClass`                                                                                                                                                                                                                                                              | Both                          | The RCS logger class.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `org.forgerock.openicf.common.logging.slf4j.SLF4JLog`                                                                                                                               |
| `principal`                                                                                                                                                                                                                                                                | Both                          | Principal to authenticate to the RCS. This property is not used if the RCS obtains its access token through PingAM (AM) (which is the case when using Advanced Identity Cloud).                                                                                                                                                                                                                                                                                                                                            | anonymous                                                                                                                                                                           |
| `password`                                                                                                                                                                                                                                                                 | Both                          | Password to authenticate to the RCS. This property isn't used if the RCS obtains its access token through AM (which is the case when using Advanced Identity Cloud.                                                                                                                                                                                                                                                                                                                                                        | changeit                                                                                                                                                                            |
| `usessl`                                                                                                                                                                                                                                                                   | Server                        | Whether the connection between IDM and the RCS should be over SSL.                                                                                                                                                                                                                                                                                                                                                                                                                                                         | false/true                                                                                                                                                                          |
| `port`                                                                                                                                                                                                                                                                     | Server                        | Port on which the RCS listens for the connection from IDM.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 8759                                                                                                                                                                                |

Certain configuration properties are dependent on the RCS mode. For more information, refer to [Configure a Remote Connector Server (RCS)](configure-server.html).

> **Collapse: Sample  file for client mode**
>
> ```properties
> connectorserver.url=wss://my-tenant.forgeblocks.com:8443/openicf
> connectorserver.connectorServerName=myconnectorserver
> connectorserver.hostId=MY_UNIQUE_RCS_HOST_ID
> connectorserver.pingPongInterval=60
> connectorserver.housekeepingInterval=20
> connectorserver.groupCheckInterval=60
> connectorserver.webSocketConnections=2
> connectorserver.connectionTtl=300
> connectorserver.newConnectionsInterval=10
> connectorserver.tokenEndpoint=https://my-tenant.forgeblocks.com/am/oauth2/realms/root/realms/alpha/access_token
> connectorserver.clientId=RCSClient
> connectorserver.clientSecret=my-client-secret
> connectorserver.trustStoreFile=security/truststore.pkcs12
> connectorserver.trustStoreType=PKCS12
> connectorserver.trustStorePass=changeit
> connectorserver.keyStoreFile=security/keyStore.pkcs12
> connectorserver.keyStoreType=PKCS12
> connectorserver.keyStorePass=changeit
> connectorserver.keyPass=changeit
> connectorserver.scope=fr:idm:*
> connectorserver.bundleDir=connectors
> connectorserver.libDir=lib
> connectorserver.loggerClass=org.forgerock.openicf.common.logging.slf4j.SLF4JLog
> ```

> **Collapse: Sample  file for server mode**
>
> ```properties
> connectorserver.port=8759
> connectorserver.pingPongInterval=60
> connectorserver.principal=anonymous
> connectorserver.password=changeit
> connectorserver.usessl=true
> connectorserver.trustStoreFile=security/truststore.pkcs12
> connectorserver.trustStoreType=PKCS12
> connectorserver.trustStorePass=changeit
> connectorserver.keyStoreFile=security/keyStore.pkcs12
> connectorserver.keyStoreType=PKCS12
> connectorserver.keyStorePass=changeit
> connectorserver.keyPass=changeit
> connectorserver.bundleDir=connectors
> connectorserver.libDir=lib
> connectorserver.key=lmA6bMfENJGlIDbfrVtklXFK32s\=
> connectorserver.loggerClass=org.forgerock.openicf.common.logging.slf4j.SLF4JLog
> ```

## Mask clear text passwords in RCS

When you configure the RCS, you specify the settings for your server in the `ConnectorServer.properties` file. By default, you enter clear text passwords for multiple settings, such as `connectorserver.clientSecret` and `connectorserver.password`. Depending on your requirements, you could want to mask specific details for security reasons. You can do this using `OPENICF_OPTS` environment variables.

### Use `OPENICF_OPTS` environment variables

If you don't want to save clear text information in the `ConnectorServer.properties` file, you can specify potentially sensitive settings at runtime through the `OPENICF_OPTS` environment variables.

For example, to set `connectorserver.clientSecret` and `connectorserver.password`, you can run the following command before starting the RCS:

```shell
cd /path/to/openicf/bin
export OPENICF_OPTS="-Dconnectorserver.clientSecret=Passw0rd! -Dconnectorserver.password=Passw0rd!"
./ConnectorServer.sh /start
```

You can use `OPENICF_OPTS` environment variables for as many settings as you require.

## ICFServlet configuration options

You can configure the following optional ICFServlet settings in your `conf/provisioner.openicf.connectorinfoprovider.json` file:

* `maxMessageSize`

  Integer.

  You can set a maximum message size in kilobytes. The default is 20MB.

* `idleTimeout`

  Integer.

  The maximum time, in minutes, that a WebSocket connection can be idle before it's removed. The default is 15 minutes.

Example `provisioner.openicf.connectorinfoprovider.json`:

```json
{
  "_id": "provisioner.openicf.connectorinfoprovider",
  "connectorsLocation": "connectors",
  "ICFServlet": {
    "maxMessageSize": 40960,
    "idleTimeout": 23
  },
  ...
}
```

## Configure RCS in client mode

The RCS configuration will differ between server mode and client mode. Refer to [RCS Properties](#rcs-properties) for a list of properties and the mode to which they apply.

To generate the core configuration, use the `createConnectorServerCoreConfig` action on the `system` endpoint. Include at least the RCS `type` (`remoteConnectorClient`) and the `systemType` in the JSON payload. The `systemType` is always `provisioner.openicf`, regardless of the RCS type:

> **Collapse: Create a core RCS configuration (client mode)**
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Accept-API-Version: resource=1.0" \
> --header "Content-Type: application/json" \
> --request POST \
> --data '{
>   "type": "remoteConnectorClient",
>   "systemType": "provisioner.openicf"
> }' \
> "http://localhost:8080/openidm/system?_action=createConnectorServerCoreConfig"
> {
>   "displayName": "",
>   "name": "",
>   "enabled": true,
>   "usessl": false
> }
> ```

IDM returns the basic configuration properties for an RCS in client mode. The configuration that's returned isn't functional. It doesn't contain the required configuration property values, such as the name of the RCS.

Use the output returned by the previous example to create your complete RCS configuration. Specify at least the `name` of the RCS, and use a PUT request on the `config` endpoint. Note that this step creates an RCS configuration on IDM. The values of these properties must match the RCS configuration, specified in the `ConnectorServer.properties` file on the RCS:

> **Collapse: Create a new RCS configuration (client mode)**
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Accept-API-Version: resource=1.0" \
> --header "Content-Type: application/json" \
> --request PUT \
> --data '{
>   "_id": "provisioner.openicf.connectorinfoprovider",
>   "connectorsLocation": "connectors",
>   "enabled": true,
>   "remoteConnectorClients": [
>     {
>       "displayName": "On premise 1",
>       "name": "onprem",
>       "enabled": true
>     }
>   ]
> }' \
> "http://localhost:8080/openidm/config/provisioner.openicf.connectorinfoprovider"
> {
>   "_id": "provisioner.openicf.connectorinfoprovider",
>   "connectorsLocation": "connectors",
>   "enabled": true,
>   "remoteConnectorClients": [
>     {
>       "displayName": "On premise 1",
>       "name": "onprem",
>       "enabled": true
>     }
>   ]
> }
> ```

## Configure RCS in server mode

|   |                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Server mode isn't compatible with PingOne Advanced Identity Cloud. If you're using Advanced Identity Cloud, [configure RCS in client mode](#configure-rcs-client-mode) instead. |

The RCS configuration will differ between server mode and client mode. Refer to [RCS Properties](#rcs-properties) for a list of properties and the mode to which they apply.

To generate the core configuration, use the `createConnectorServerCoreConfig` action on the `system` endpoint. Include at least the RCS `type` (`remoteConnectorServer`) and the `systemType` in the JSON payload. The `systemType` is always `provisioner.openicf`, regardless of the RCS type:

> **Collapse: Create a Core RCS Configuration (Server Mode)**
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Accept-API-Version: resource=1.0" \
> --header "Content-Type: application/json" \
> --request POST \
> --data '{
>   "type": "remoteConnectorServer",
>   "systemType": "provisioner.openicf"
> }' \
> "http://localhost:8080/openidm/system?_action=createConnectorServerCoreConfig"
> {
>   "displayName": "",
>   "proxyPassword": null,
>   "proxyHost": null,
>   "enabled": true,
>   "usessl": false,
>   "proxyPort": 8080,
>   "port": "",
>   "name": "",
>   "host": "",
>   "proxyUser": null,
>   "housekeepingInterval": 20,
>   "connectionGroupCheckInterval": 60,
>   "pingPongInterval": 60,
>   "key": "password",
>   "webSocketConnections": 2
> }
> ```

IDM returns the required configuration properties for an RCS in server mode. The configuration that's returned isn't functional. It doesn't contain the specific property values, such as the host name and port of the RCS.

Use the output returned by the previous example to create your complete RCS configuration. Specify at least the `host` and `port` of the RCS, and use a PUT request on the `config` endpoint. Note that this step creates an RCS configuration on IDM. The values of these properties must match the RCS configuration, specified in the `ConnectorServer.properties` file on the RCS:

> **Collapse: Create a New RCS Configuration (Server Mode)**
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Accept-API-Version: resource=1.0" \
> --header "Content-Type: application/json" \
> --request PUT \
> --data '{
>   "_id": "provisioner.openicf.connectorinfoprovider",
>   "connectorsLocation": "connectors",
>   "enabled": true,
>   "remoteConnectorServers": [
>     {
>       "type": "remoteConnectorServer",
>       "displayName": "Remote Connector Server 1",
>       "proxyPassword": null,
>       "proxyHost": null,
>       "enabled": true,
>       "usessl": false,
>       "proxyPort": 8080,
>       "port": 8759,
>       "name": "rcs1",
>       "host": "rcs.example.com",
>       "proxyUser": null,
>       "housekeepingInterval": 20,
>       "connectionGroupCheckInterval": 60,
>       "pingPongInterval": 60,
>       "key": "Passw0rd",
>       "webSocketConnections": 2
>     }
>   ]
> }' \
> "http://localhost:8080/openidm/config/provisioner.openicf.connectorinfoprovider"
> {
>   "_id": "provisioner.openicf.connectorinfoprovider",
>   "connectorsLocation": "connectors",
>   "enabled": true,
>   "remoteConnectorServers": [
>     {
>       "type": "remoteConnectorServer",
>       "displayName": "Remote Connector Server 1",
>       "proxyPassword": null,
>       "proxyHost": null,
>       "enabled": true,
>       "usessl": false,
>       "proxyPort": 8080,
>       "port": 8759,
>       "name": "rcs1",
>       "host": "rcs.example.com",
>       "proxyUser": null,
>       "housekeepingInterval": 20,
>       "connectionGroupCheckInterval": 60,
>       "pingPongInterval": 60,
>       "key": {
>         "$crypto": {
>           "type": "x-simple-encryption",
>           "value": {
>             "cipher": "AES/CBC/PKCS5Padding",
>             "stableId": "openidm-sym-default",
>             "salt": "3Mq1UJuZXqANx2AzUtbFbg==",
>             "data": "4WHBEI3nSVWJ2DfIs2dPZg==",
>             "keySize": 16,
>             "purpose": "idm.config.encryption",
>             "iv": "BvFAQ4sjwJCNY2e7WZPkGw==",
>             "mac": "ximBz/BlqC8SEsBTuYQX5Q=="
>           }
>         }
>       },
>       "webSocketConnections": 2
>     }
>   ]
> }
> ```

## Configure failover between RCS servers

For failover purposes, you can configure a *group* of RCSs, in either server or client mode. Failover is particularly important when you configure an RCS in client mode because IDM has no way of knowing whether the RCS is available.

To prevent the RCS from being a single point of failure, you can specify a list of RCS servers that the connector can target. To set up a failover configuration, you create either a `remoteConnectorServersGroup` or a `remoteConnectorClientsGroup` and list the RCS servers. The connector attempts to contact the first RCS in the list. If that RCS is down, it proceeds to the next RCS.

> **Collapse: Configure failover for RCS servers in client mode**
>
> This example configures a `remoteConnectorClientsGroup` that lists two remote RCS servers, on hosts `remote-host-1` and `remote-host-2`. The RCS servers are listed by their `name` property. You can configure multiple groups and multiple servers per group.
>
> First, generate the core configuration to obtain the required properties:
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Accept-API-Version: resource=1.0" \
> --header "Content-Type: application/json" \
> --request POST \
> --data '{
>   "type" : "remoteConnectorClientsGroup",
>   "systemType" : "provisioner.openicf"
> }' \
> "http://localhost:8080/openidm/system?_action=createConnectorServerCoreConfig"
> {
>    "displayName": "",
>    "name": "",
>    "serversList": [],
>    "algorithm": "failover"
>  }
> ```
>
> Use the output returned by the previous example to create your RCS group configuration. Use a PUT request on the `config` endpoint:
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Accept-API-Version: resource=1.0" \
> --header "Content-Type: application/json" \
> --request PUT \
> --data '{
>   "_id": "provisioner.openicf.connectorinfoprovider",
>   "connectorsLocation": "connectors",
>   "enabled": true,
>   "remoteConnectorClients": [
>     {
>       "type": "remoteConnectorClientsGroup",
>       "displayName": ".NET Failover Group",
>       "name" : "dotnet-ha",
>       "algorithm" : "failover",
>       "serversList" : [
>         {"name": "remote-host-1"},
>         {"name": "remote-host-2"}
>       ]
>     }
>   ]
> }' \
> "http://localhost:8080/openidm/config/provisioner.openicf.connectorinfoprovider"
> {
>   "_id": "provisioner.openicf.connectorinfoprovider",
>   "connectorsLocation": "connectors",
>   "enabled": true,
>   "remoteConnectorClients": [
>     {
>       "type": "remoteConnectorClientsGroup",
>       "displayName": ".NET Failover Group",
>       "name": "dotnet-ha",
>       "algorithm": "failover",
>       "serversList": [
>         {
>           "name": "remote-host-1"
>         },
>         {
>           "name": "remote-host-2"
>         }
>       ]
>     }
>   ]
> }
> ```
>
> The `algorithm` can be either `failover` or `roundrobin`. If the algorithm is `failover`, requests are always sent to the first RCS in the list, unless it's unavailable; in which case, requests are sent to the next RCS in the list. If the algorithm is `roundrobin`, requests are distributed equally between the RCS servers in the list, in the order in which they're received.
>
> Your connector configuration (`provisioner.openicf-connectorName.json`) references the RCS group, rather than a single RCS. For example, the following excerpt of a PowerShell connector configuration file references the `dotnet-ha` RCS group created in the previous example:
>
> ```json
> {
>    "connectorRef" : {
>      "bundleName" : "MsPowerShell.Connector",
>      "connectorName" : "Org.ForgeRock.OpenICF.Connectors.MsPowerShell.MsPowerShellConnector",
>      "connectorHostRef" : "dotnet-ha",
>      "bundleVersion" : "[1.4.3.0,1.5.0.0)"
>    },
>    ...
>  }
> ```

> **Collapse: Configure failover for RCS servers in server mode**
>
> This example configures a `remoteConnectorServersGroup` that lists two remote RCS servers, on hosts `remote-host-1` and `remote-host-2`. The RCS servers are listed by their `name` property. You can configure multiple groups and multiple servers per group.
>
> First, generate the core configuration to obtain the required properties:
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Accept-API-Version: resource=1.0" \
> --header "Content-Type: application/json" \
> --request POST \
> --data '{
>   "type" : "remoteConnectorServersGroup",
>   "systemType" : "provisioner.openicf"
> }' \
> "http://localhost:8080/openidm/system?_action=createConnectorServerCoreConfig"
> {
>    "displayName": "",
>    "name": "",
>    "serversList": [],
>    "algorithm": "failover"
>  }
> ```
>
> Use the output returned by the previous example to create your RCS group configuration. Use a PUT request on the `config` endpoint:
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Accept-API-Version: resource=1.0" \
> --header "Content-Type: application/json" \
> --request PUT \
> --data '{
>   "_id": "provisioner.openicf.connectorinfoprovider",
>   "connectorsLocation": "connectors",
>   "enabled": true,
>   "remoteConnectorServers": [
>     {
>       "type": "remoteConnectorServersGroup",
>       "displayName": ".NET Failover Group",
>       "name" : "dotnet-ha",
>       "algorithm" : "failover",
>       "serversList" : [
>         {"name": "remote-host-1"},
>         {"name": "remote-host-2"}
>       ]
>     }
>   ]
> }' \
> "http://localhost:8080/openidm/config/provisioner.openicf.connectorinfoprovider"
> {
>   "_id": "provisioner.openicf.connectorinfoprovider",
>   "connectorsLocation": "connectors",
>   "enabled": true,
>   "remoteConnectorServers": [
>     {
>       "type": "remoteConnectorServersGroup",
>       "displayName": ".NET Failover Group",
>       "name": "dotnet-ha",
>       "algorithm": "failover",
>       "serversList": [
>         {
>           "name": "remote-host-1"
>         },
>         {
>           "name": "remote-host-2"
>         }
>       ]
>     }
>   ]
> }
> ```
>
> The `algorithm` can be either `failover` or `roundrobin`. If the algorithm is `failover`, requests are always sent to the first RCS in the list, unless it's unavailable; in which case, requests are sent to the next RCS in the list. If the algorithm is `roundrobin`, requests are distributed equally between the RCS servers in the list, in the order in which they're received.
>
> Your connector configuration (`provisioner.openicf-connectorName.json`) references the RCS group, rather than a single RCS. For example, the following excerpt of a PowerShell connector configuration file references the `dotnet-ha` RCS group created in the previous example:
>
> ```json
> {
>    "connectorRef" : {
>      "bundleName" : "MsPowerShell.Connector",
>      "connectorName" : "Org.ForgeRock.OpenICF.Connectors.MsPowerShell.MsPowerShellConnector",
>      "connectorHostRef" : "dotnet-ha",
>      "bundleVersion" : "[1.4.3.0,1.5.0.0)"
>    },
>    ...
>  }
> ```

## Secure the connection to the RCS with SSL

|   |                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------- |
|   | The following section doesn't apply to Advanced Identity Cloud, as it requires filesystem access to your installation. |

The SSL configuration for an RCS depends on whether you're running the RCS in server mode or in client mode:

* In **server mode**, IDM initiates the connection to the RCS.

  The RCS needs a public/private key pair and a certificate (either self-signed or CA-signed). The RCS sends its certificate to the client (IDM) during the SSL handshake.

  If you're using a CA-signed certificate, IDM will trace the certificate back to the root certificate. If you're using a self-signed certificate (or a certificate that depends on an unreachable issuer in the chain from the root certificate), you must import the certificate into the IDM truststore.

* In **client mode**, the RCS initiates the connection to IDM. IDM sends its certificate during the SSL handshake. If you're using the IDM self-signed certificate, you must import the certificate into the RCS truststore.

  If you're using TLS Mutual Authentication, the RCS needs a public/private key pair and a certificate. IDM requests the certificate from the RCS during the SSL handshake.

### Configure the RCS for SSL

On the RCS, edit the `conf/ConnectorServer.properties` file to specify a secure connection between IDM and the RCS:

* RCS in server mode

  * Set `connectorserver.usessl=true`.

  * Specify the RCS keystore and truststore. For example:

    ```javascript
    connectorserver.trustStoreFile=security/truststore.pkcs12
    connectorserver.trustStoreType=PKCS12
    connectorserver.trustStorePass=changeit
    connectorserver.keyStoreFile=security/keyStore.pkcs12
    connectorserver.keyStoreType=PKCS12
    connectorserver.keyStorePass=changeit
    connectorserver.keyPass=changeit
    ```

* RCS in client mode

  * Connection security is determined by the value of the `connectorserver.url` property. Use the `wss` protocol to establish a WebSocket over an encrypted TLS connection, for example, `wss://my-tenant.forgeblocks.com/openicf`.

    The `connectorserver.usessl` property isn't used in client mode.

  * Specify the RCS keystore and truststore. For example:

    ```javascript
    connectorserver.trustStoreFile=security/truststore.pkcs12
    connectorserver.trustStoreType=PKCS12
    connectorserver.trustStorePass=changeit
    connectorserver.keyStoreFile=security/keyStore.pkcs12
    connectorserver.keyStoreType=PKCS12
    connectorserver.keyStorePass=changeit
    connectorserver.keyPass=changeit
    ```

### Configure IDM for SSL

In your `conf/provisioner.openicf.connectorinfoprovider.json` file, set `"usessl" : true`.

### Generate keys for an RCS in server mode

1. Generate the RCS private/public key pair and create a new PKCS12 keystore:

   ```
   keytool \
   -genkeypair \
   -keyalg EC \
   -alias icf-rcs \
   -dname "CN=icf.example.com,O=Example Corp,C=FR" \
   -keystore rcsKeystore \
   -storetype PKCS12 \
   -storepass changeit \
   ```

2. Verify the contents of the new keystore:

   ```
   keytool \
   -list \
   -v \
   -keystore rcsKeystore
   Enter keystore password:  changeit
   Keystore type: PKCS12
   Keystore provider: SUN

   Your keystore contains 1 entry

   Alias name: icf-rcs
   Creation date: Jul 13, 2020
   Entry type: PrivateKeyEntry
   Certificate chain length: 1
   Certificate[1]:
   Owner: CN=icf.example.com, O=Example Corp, C=FR
   Issuer: CN=icf.example.com, O=Example Corp, C=FR
   Serial number: 611e093d
   Valid from: Mon Jul 13 23:58:49 SAST 2020 until: Sun Oct 11 23:58:49 SAST 2020
   Certificate fingerprints:
   SHA1: Fingerprint
   SHA256: Fingerprint
   Signature algorithm name: SHA256withECDSA
   Subject Public Key Algorithm: 256-bit EC key
   ...
   ```

3. Export the RCS certificate:

   ```
   keytool \
   -export \
   -alias icf-rcs \
   -file rcs.cert \
   -keystore rcsKeystore.pkcs12
   Enter keystore password: changeit
   Certificate stored in file <rcs.cert>
   ```

4. If you aren't using a self-signed certificate, have the certificate signed by a Certificate Authority (CA):

   1. Create a Certificate Signing Request (CSR):

      ```
      keytool \
      -keystore rcsKeystore.pkcs12 \
      -certreq \
      -alias icf-rcs \
      -file rcs.csr
      ```

      ```
      more rcs.csr
      -----BEGIN NEW CERTIFICATE REQUEST-----

      MIIEKTCCA9QCAQAwVzELMAkGA1UEBhMCRlIxCzAJBgNVBAgTAkZSMQswCQYDVQQH
      xZ47rzcY6OrElh8+/TYG50NRqcQYMzm4CefCrhxTm6dHW4XQEa24tHmHdUmEaVys
      A1UdDgQWBBSivxV9AzgbrIo3gG6vCBlNaXf3wjANBglghkgBZQMEAwIFAANAADA9
      ...
      AhxL791/ikf1hqxOD3uttV7qumg+TNednsgtk6uOAh0AlINk+1LBeyUkQA7iUHy/
      3KLYWog/Npu5USdCeA==

      -----END NEW CERTIFICATE REQUEST-----
      ```

   2. Submit the CSR to your CA for signature.

5. Import the signed certificate into the RCS keystore:

   ```
   keytool \
   -importcert \
   -trustcacerts \
   -file rcs.cert \
   -keystore rcsKeystore.pkcs12 \
   -storetype pkcs12 \
   -alias icf-rcs
   Enter keystore password: changeit
   Certificate reply was installed in keystore
   ```

   |   |                                                                                                          |
   | - | -------------------------------------------------------------------------------------------------------- |
   |   | If your CA certificate isn't trusted, you might need to import the CA certificate into the keystore too. |

6. Import the RCS certificate into the IDM truststore:

   ```
   keytool \
   -import \
   -alias icf-rcs \
   -keystore /path/to/openidm/truststore \
   -file rcs.cert
   Enter keystore password: changeit
   Owner: CN=icf.example.com, O=Example Corp, C=FR
   Issuer: CN=icf.example.com, O=Example Corp, C=FR
   Serial number: 611e093d
   Valid from: Fri Apr 05 16:04:04 CEST 2019 until: Mon Aug 17 16:04:04 CEST 2020
   Certificate fingerprints:
   MD5:  Fingerprint
   SHA1: Fingerprint
   SHA256: Fingerprint
   Signature algorithm name: SHA256withRSA
   Subject Public Key Algorithm: 2048-bit DSA key
   Version: 1
   Trust this certificate? [no]:  yes
   Certificate was added to keystore
   ```

### Generate keys for an RCS in client mode

1. Generate the RCS private/public key pair and create a new PKCS12 keystore:

   ```
   keytool \
   -genkeypair \
   -keyalg EC \
   -alias icf-rcs \
   -dname "CN=icf.example.com,O=Example Corp,C=FR" \
   -keystore rcsKeystore \
   -storetype PKCS12 \
   -storepass changeit \
   ```

2. Verify the contents of the new keystore:

   ```
   keytool \
   -list \
   -v \
   -keystore rcsKeystore
   Enter keystore password:  changeit
   Keystore type: PKCS12
   Keystore provider: SUN

   Your keystore contains 1 entry

   Alias name: icf-rcs
   Creation date: Jul 13, 2020
   Entry type: PrivateKeyEntry
   Certificate chain length: 1
   Certificate[1]:
   Owner: CN=icf.example.com, O=Example Corp, C=FR
   Issuer: CN=icf.example.com, O=Example Corp, C=FR
   Serial number: 611e093d
   Valid from: Mon Jul 13 23:58:49 SAST 2020 until: Sun Oct 11 23:58:49 SAST 2020
   Certificate fingerprints:
   SHA1: Fingerprint
   SHA256: Fingerprint
   Signature algorithm name: SHA256withECDSA
   Subject Public Key Algorithm: 256-bit EC key
   ...
   ```

3. Export the RCS certificate:

   ```
   keytool \
   -export \
   -alias icf-rcs \
   -file rcs.cert \
   -keystore rcsKeystore.pkcs12
   Enter keystore password: changeit
   Certificate stored in file <rcs.cert>
   ```

4. If you are not using a self-signed certificate, have the certificate signed by a Certificate Authority (CA):

   1. Create a Certificate Signing Request (CSR):

      ```
      keytool \
      -keystore rcsKeystore.pkcs12 \
      -certreq \
      -alias icf-rcs \
      -file rcs.csr
      ```

      ```
      more rcs.csr
      -----BEGIN NEW CERTIFICATE REQUEST-----

      MIIEKTCCA9QCAQAwVzELMAkGA1UEBhMCRlIxCzAJBgNVBAgTAkZSMQswCQYDVQQH
      xZ47rzcY6OrElh8+/TYG50NRqcQYMzm4CefCrhxTm6dHW4XQEa24tHmHdUmEaVys
      A1UdDgQWBBSivxV9AzgbrIo3gG6vCBlNaXf3wjANBglghkgBZQMEAwIFAANAADA9
      ...
      AhxL791/ikf1hqxOD3uttV7qumg+TNednsgtk6uOAh0AlINk+1LBeyUkQA7iUHy/
      3KLYWog/Npu5USdCeA==

      -----END NEW CERTIFICATE REQUEST-----
      ```

   2. Submit the CSR to your CA for signature.

5. Import the signed certificate into the RCS keystore:

   ```
   keytool \
   -importcert \
   -trustcacerts \
   -file rcs.cert \
   -keystore rcsKeystore.pkcs12 \
   -storetype pkcs12 \
   -alias icf-rcs
   Enter keystore password: changeit
   Certificate reply was installed in keystore
   ```

   |   |                                                                                                          |
   | - | -------------------------------------------------------------------------------------------------------- |
   |   | If your CA certificate isn't trusted, you might need to import the CA certificate into the keystore too. |

6. Import the RCS certificate into the IDM truststore:

   ```
   keytool \
   -import \
   -alias icf-rcs \
   -keystore /path/to/openidm/truststore \
   -file rcs.cert
   Enter keystore password: changeit
   Owner: CN=icf.example.com, O=Example Corp, C=FR
   Issuer: CN=icf.example.com, O=Example Corp, C=FR
   Serial number: 611e093d
   Valid from: Fri Apr 05 16:04:04 CEST 2019 until: Mon Aug 17 16:04:04 CEST 2020
   Certificate fingerprints:
   MD5:  Fingerprint
   SHA1: Fingerprint
   SHA256: Fingerprint
   Signature algorithm name: SHA256withRSA
   Subject Public Key Algorithm: 2048-bit DSA key
   Version: 1
   Trust this certificate? [no]:  yes
   Certificate was added to keystore
   ```

7. Export the IDM self-signed certificate:

   ```
   keytool \
   -export \
   -alias openidm-localhost \
   -keystore keystore.jceks \
   -storetype jceks \
   -file idm.cert \
   Enter keystore password: changeit
   Certificate stored in file <idm.cert>
   ```

8. Import the IDM self-signed certificate into the RCS truststore:

   ```
   keytool \
   -import \
   -alias openidm-localhost \
   -keystore /path/to/rcs/security/truststore.pkcs12 \
   -storetype pkcs12 \
   -file idm.cert
   Enter keystore password: changeit

   Owner: CN=openidm-localhost, O=OpenIDM Self-Signed Certificate, OU=None, L=None, ST=None, C=None
   Issuer: CN=openidm-localhost, O=OpenIDM Self-Signed Certificate, OU=None, L=None, ST=None, C=None
   Serial number: 16981c79d8d
   Valid from: Wed Feb 13 15:35:36 CET 2019 until: Thu Mar 15 15:35:36 CET 2029
   Certificate fingerprints:
   MD5:  fingerprint
   SHA1: fingerprint
   SHA256: fingerprint
   Signature algorithm name: SHA512withRSA
   Subject Public Key Algorithm: 2048-bit RSA key
   Version: 3
   Trust this certificate? [no]:  yes

   Certificate was added to keystore
   ```

---

---
title: Configure connectors
description: How to configure ICF connectors in PingIDM using the admin UI, REST, or sample files, with reference for all provisioner configuration properties
component: openicf
page_id: openicf:connector-reference:configure-connector
canonical_url: https://docs.pingidentity.com/openicf/connector-reference/configure-connector.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  sample-provisioner-files: Sample provisioner files
  connector-wiz-adminui: Configure connectors with the admin UI
  connector-wiz-REST: Configure connectors over REST
  connector-reference-props: Connector reference properties
  pool-configuration-option: Pool configuration
  operation-timeout: Operation timeouts
  operation-rate-limits: Operation rate limits
  configuration-properties: Connection configuration
  sync-failure-handler: Synchronization failure configuration
  results-handler-config: Configure how results are handled
  exclude-unmodified: Specify which attributes are updated
  object-types: Set the supported object types
  object-extensions-ui: Add objects and properties through the UI
  object-level-extensions: Specify object types on the external resource
  empty-attributes: Behavior for empty attributes
  property-level-extensions: Specify attribute types on the external resource
  operation-options: Configure operation options
---

# Configure connectors

You configure connectors through the ICF provisioner service, and access them over REST at the `openidm/conf` endpoint.

Connector configurations are stored in files in your project's `conf/` directory, and are named `project-dir/conf/provisioner.openicf-name` where *name* corresponds to the name of the connector. If you are creating your own connector configuration files, *do not* include additional dash characters (`-`) in the connector name, as this can cause problems with the OSGi parser. For example, `provisioner.openicf-hrdb.json` is acceptable, and `provisioner.openicf-hr-db.json` is not.

You can create a connector configuration in the following ways:

* Start with the sample provisioner files in the `/path/to/openidm/samples/example-configurations/provisioners` directory. Learn more in the [Sample Provisioner Files](#sample-provisioner-files).

* Configure connectors in the admin UI. Sign on to the admin UI at `https://localhost:8443/admin`, then continue with the process described in [Configure Connectors With the admin UI](#connector-wiz-adminui).

* Use the service that IDM exposes through the REST interface to create basic connector configuration files. Learn more in [Configure Connectors Over REST](#connector-wiz-REST).

* Use the `cli.sh` or `cli.bat` scripts to generate a basic connector configuration. Learn more in the [`configureconnector`](https://docs.pingidentity.com/pingidm/8/setup-guide/chap-cli.html#cli-configureconnector) documentation.

## Sample provisioner files

A number of sample connector configurations are available in the `openidm/samples/example-configurations/provisioners` directory. To use these connector configurations, edit the configuration files as required, and copy them to your project's `conf` directory.

The following example shows a high-level connector configuration. The individual configuration objects are described in detail later in this section:

```json
{
  "connectorRef"              : connector-ref-object,
  "producerBufferSize"        : integer,
  "poolConfigOption"          : pool-config-option-object,
  "operationTimeout"          : operation-timeout-object,
  "operationRateLimits"       : operation-rate-limits-object,
  "configurationProperties"   : configuration-properties-object,
  "syncFailureHandler"        : sync-failure-handler-object,
  "resultsHandlerConfig"      : results-handler-config-object,
  "excludeUnmodified"         : boolean, true/false,
  "objectTypes"               : object-types-object,
  "operationOptions"          : operation-options-object
}
```

## Configure connectors with the admin UI

To configure connectors in the admin UI, select Configure > Connector.

If your project has an existing connector configuration (for example, if you have started IDM with one of the sample configurations), click on that connector to edit it. If you're starting with a new project, click New Connector to configure a new connector.

The connectors displayed on the Connectors page reflect the provisioner files in your project's `conf/` directory. To add a new connector configuration, you can also copy a provisioner file from the `/path/to/openidm/samples/example-configurations/provisioners` directory, then edit it to fit your deployment.

When you add a new connector, the Connector Type dropdown list reflects the connector .jar files that are in the `/path/to/openidm/connectors` directory. You can have more than one connector configuration for a specific connector type. For example, you might use the LDAP connector to set up two connector configurations—one to an Active Directory server and one to a PingDS (DS) instance.

The Connector Types listed here do not include all supported connectors. The *scripted* connectors (such as scripted Groovy, scripted REST, scripted SQL, and PowerShell) are not available in the list of connector types. In general, the scripted connectors require extensive custom configuration changes, and a single HTML template to cover all possible permutations is not feasible. To add a scripted connector configuration, [configure the connector over REST](#connector-wiz-REST).

Alternatively, copy one of the example provisioner files in `/path/to/openidm/samples/example-configurations/provisioners` into your project's `conf` directory and edit the configuration directly in the provisioner file.

Additional connectors are available from the [Backstage download site](https://backstage.forgerock.com/downloads) site. For connectors that are not bundled with IDM, the UI displays a generic template, based on the schema provided by the connector.

The tabs on the connector configuration screens correspond to the objects and properties described in the remaining sections of this chapter.

When a connector configuration is complete, and IDM is able to establish the connection to the remote resource, the Data tab displays the objects in that remote resource. For example, the following image shows the contents of a connected LDAP resource:

![connector-config-data](_images/connector-config-data.png)Figure 1. Data Tab For a Connected LDAP Resource

You can search through these objects with either the Basic Filter shown in each column, or the Advanced Filter option, which lets you build many of the queries shown in [Define and call data queries](https://docs.pingidentity.com/pingidm/8/objects-guide/queries.html).

## Configure connectors over REST

To create a new connector configuration over REST, follow these steps:

1. List the available connectors.

2. Generate the core configuration.

3. Add the target system properties, then connect to the target system to generate the final configuration.

4. Submit the final configuration to IDM.

This procedure walks you through creating a connector configuration over REST, for a CSV file connector.

1. List the available connectors.

   In a default IDM installation, the available connectors are installed in the `openidm/connectors` directory. If you are using a remote connector server, additional connectors might be available in the `openicf/connectors` directory on the remote server.

   Run the following command to list the available connectors:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request POST \
   "http://localhost:8080/openidm/system?_action=availableConnectors"
   ```

   On a default IDM installation, this command returns the following output:

   > **Collapse: Sample output**
   >
   > ```json
   > {
   >   "connectorRef": [
   >     {
   >       "displayName": "SSH Connector",
   >       "bundleVersion": "1.5.20.35",
   >       "systemType": "provisioner.openicf",
   >       "bundleName": "org.forgerock.openicf.connectors.ssh-connector",
   >       "connectorName": "org.forgerock.openicf.connectors.ssh.SSHConnector"
   >     },
   >     {
   >       "displayName": "ServiceNow Connector",
   >       "bundleVersion": "1.5.20.35",
   >       "systemType": "provisioner.openicf",
   >       "bundleName": "org.forgerock.openicf.connectors.servicenow-connector",
   >       "connectorName": "org.forgerock.openicf.connectors.servicenow.ServiceNowConnector"
   >     },
   >     {
   >       "displayName": "Scripted SQL Connector",
   >       "bundleVersion": "1.5.20.35",
   >       "systemType": "provisioner.openicf",
   >       "bundleName": "org.forgerock.openicf.connectors.scriptedsql-connector",
   >       "connectorName": "org.forgerock.openicf.connectors.scriptedsql.ScriptedSQLConnector"
   >     },
   >     {
   >       "displayName": "Scripted REST Connector",
   >       "bundleVersion": "1.5.20.35",
   >       "systemType": "provisioner.openicf",
   >       "bundleName": "org.forgerock.openicf.connectors.scriptedrest-connector",
   >       "connectorName": "org.forgerock.openicf.connectors.scriptedrest.ScriptedRESTConnector"
   >     },
   >     {
   >       "displayName": "SCIM Connector",
   >       "bundleVersion": "1.5.20.35",
   >       "systemType": "provisioner.openicf",
   >       "bundleName": "org.forgerock.openicf.connectors.scim-connector",
   >       "connectorName": "org.forgerock.openicf.connectors.scim.ScimConnector"
   >     },
   >     {
   >       "displayName":"Salesforce Connector",
   >       "bundleVersion":"1.5.20.35",
   >       "systemType":"provisioner.openicf",
   >       "bundleName":"org.forgerock.openicf.connectors.salesforce-connector",
   >       "connectorName":"org.forgerock.openicf.connectors.salesforce.SalesforceConnector"
   >     },
   >     {
   >       "displayName":"MSGraphAPI Connector",
   >       "bundleVersion":"1.5.20.35",
   >       "systemType":"provisioner.openicf",
   >       "bundleName":"org.forgerock.openicf.connectors.msgraphapi-connector",
   >       "connectorName":"org.forgerock.openicf.connectors.msgraphapi.MSGraphAPIConnector"
   >     },
   >     {
   >       "displayName": "MongoDB Connector",
   >       "bundleVersion": "1.5.20.35",
   >       "systemType": "provisioner.openicf",
   >       "bundleName": "org.forgerock.openicf.connectors.mongodb-connector",
   >       "connectorName": "org.forgerock.openicf.connectors.mongodb.MongoDBConnector"
   >     },
   >     {
   >       "displayName": "Marketo Connector",
   >       "bundleVersion": "1.5.20.35",
   >       "systemType": "provisioner.openicf",
   >       "bundleName": "org.forgerock.openicf.connectors.marketo-connector",
   >       "connectorName": "org.forgerock.openicf.connectors.marketo.MarketoConnector"
   >     },
   >     {
   >       "displayName": "LDAP Connector",
   >       "bundleVersion": "1.5.20.35",
   >       "systemType": "provisioner.openicf",
   >       "bundleName": "org.forgerock.openicf.connectors.ldap-connector",
   >       "connectorName": "org.identityconnectors.ldap.LdapConnector"
   >     },
   >     {
   >       "displayName": "Kerberos Connector",
   >       "bundleVersion": "1.5.20.35",
   >       "systemType": "provisioner.openicf",
   >       "bundleName": "org.forgerock.openicf.connectors.kerberos-connector",
   >       "connectorName": "org.forgerock.openicf.connectors.kerberos.KerberosConnector"
   >     },
   >     {
   >       "displayName": "Scripted Poolable Groovy Connector",
   >       "bundleVersion": "1.5.20.35",
   >       "systemType": "provisioner.openicf",
   >       "bundleName": "org.forgerock.openicf.connectors.groovy-connector",
   >       "connectorName": "org.forgerock.openicf.connectors.groovy.ScriptedPoolableConnector"
   >     },
   >     {
   >       "displayName": "Scripted Groovy Connector",
   >       "bundleVersion": "1.5.20.35",
   >       "systemType": "provisioner.openicf",
   >       "bundleName": "org.forgerock.openicf.connectors.groovy-connector",
   >       "connectorName": "org.forgerock.openicf.connectors.groovy.ScriptedConnector"
   >     },
   >     {
   >       "displayName": "GoogleApps Connector",
   >       "bundleVersion": "1.5.20.35",
   >       "systemType": "provisioner.openicf",
   >       "bundleName": "org.forgerock.openicf.connectors.googleapps-connector",
   >       "connectorName": "org.forgerock.openicf.connectors.googleapps.GoogleAppsConnector"
   >     },
   >     {
   >       "displayName": "Database Table Connector",
   >       "bundleVersion": "1.5.20.35",
   >       "systemType": "provisioner.openicf",
   >       "bundleName": "org.forgerock.openicf.connectors.databasetable-connector",
   >       "connectorName": "org.identityconnectors.databasetable.DatabaseTableConnector"
   >     },
   >     {
   >       "displayName": "CSV File Connector",
   >       "bundleVersion": "1.5.20.35",
   >       "systemType": "provisioner.openicf",
   >       "bundleName": "org.forgerock.openicf.connectors.csvfile-connector",
   >       "connectorName": "org.forgerock.openicf.csvfile.CSVFileConnector"
   >     },
   >     {
   >       "displayName": "Adobe Marketing Cloud Connector",
   >       "bundleVersion": "1.5.20.35",
   >       "systemType": "provisioner.openicf",
   >       "bundleName": "org.forgerock.openicf.connectors.adobecm-connector",
   >       "connectorName": "org.forgerock.openicf.acm.ACMConnector"
   >     }
   >   ]
   > }
   > ```

2. Generate a core configuration.

   Locate the connector to configure from the previous step's output, and copy the JSON object to insert as the value of the `"connectorRef"` property in the `data` payload of the following command.

   This example generates a core configuration for the CSV file connector:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --header "Content-Type: application/json" \
   --request POST \
   --data '{
     "connectorRef": {
       "systemType": "provisioner.openicf",
       "bundleName": "org.forgerock.openicf.connectors.csvfile-connector",
       "connectorName": "org.forgerock.openicf.csvfile.CSVFileConnector",
       "displayName": "CSV File Connector",
       "bundleVersion": "1.5.20.35"
     }
   }' \
   "http://localhost:8080/openidm/system?_action=createCoreConfig"
   ```

   The command returns a connector configuration, similar to the following:

   ```json
   {
     "connectorRef": {
       "systemType": "provisioner.openicf",
       "bundleName": "org.forgerock.openicf.connectors.csvfile-connector",
       "connectorName": "org.forgerock.openicf.csvfile.CSVFileConnector",
       "displayName": "CSV File Connector",
       "bundleVersion": "1.5.20.35"
     },
     "resultsHandlerConfig": {
       "enableNormalizingResultsHandler": false,
       "enableFilteredResultsHandler": false,
       "enableCaseInsensitiveFilter": false,
       "enableAttributesToGetSearchResultsHandler": true
     },
     "operationTimeout": {
       "CREATE": 15000,
       "UPDATE": 15000,
       "DELETE": 15000,
       "TEST": 5000,
       "SCRIPT_ON_CONNECTOR": 15000,
       "SCRIPT_ON_RESOURCE": 15000,
       "GET": 15000,
       "RESOLVEUSERNAME": 10000,
       "AUTHENTICATE": 10000,
       "SEARCH": 15000,
       "VALIDATE": 5000,
       "SYNC": 15000,
       "SCHEMA": 10000
     },
     "configurationProperties": {
       "headerPassword": "password",
       "spaceReplacementString": "_",
       "csvFile": null,
       "newlineString": "\n",
       "headerUid": "uid",
       "quoteCharacter": "\"",
       "escapeCharacter": "\\",
       "fieldDelimiter": ",",
       "syncFileRetentionCount": 3
     }
   }
   ```

3. Connect to the target system to generate the final configuration.

   The configuration returned in the previous step is not functional. It does not include the required `configurationProperties` that are specific to the target system (such as the host name and port number of the target system, or the `csvFile` for a CSV file connector). It also doesn't include the complete list of `objectTypes` and `operationOptions`.

   To connect to the target system, add values for the required `configurationProperties`, and submit the updated configuration in the data payload of the following command.

   This example connects to the specified CSV file:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --header "Content-Type: application/json" \
   --request POST \
   --data '{
     "configurationProperties": {
       "headerPassword": "password",
       "spaceReplacementString": "_",
       "csvFile": "&{idm.instance.dir}/data/csvConnectorData.csv",
       "newlineString": "\n",
       "headerUid": "uid",
       "quoteCharacter": "\"",
       "fieldDelimiter": ",",
       "syncFileRetentionCount": 3
     },
     "connectorRef": {
       "systemType": "provisioner.openicf",
       "bundleName": "org.forgerock.openicf.connectors.csvfile-connector",
       "connectorName": "org.forgerock.openicf.csvfile.CSVFileConnector",
       "displayName": "CSV File Connector",
       "bundleVersion": "1.5.20.35"
     },
     "resultsHandlerConfig": {
       "enableNormalizingResultsHandler": true,
       "enableFilteredResultsHandler": true,
       "enableCaseInsensitiveFilter": false,
       "enableAttributesToGetSearchResultsHandler": true
     },
     "operationTimeout": {
       "CREATE": 15000,
       "UPDATE": 15000,
       "DELETE": 15000,
       "TEST": 5000,
       "SCRIPT_ON_CONNECTOR": 15000,
       "SCRIPT_ON_RESOURCE": 15000,
       "GET": 15000,
       "RESOLVEUSERNAME": 10000,
       "AUTHENTICATE": 10000,
       "SEARCH": 15000,
       "VALIDATE": 5000,
       "SYNC": 15000,
       "SCHEMA": 10000
     }
   }' \
   "http://localhost:8080/openidm/system?_action=createFullConfig"
   ```

   |   |                                                                                                                                                                                                                 |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The single quotes around the JSON object in the `--data` parameter prevent the command from being executed when a new line is encountered in the content. You can therefore include line feeds for readability. |

   With this command, IDM connects to the target resource, and attempts to read the schema, if it is available. It then iterates through the schema objects and attributes, and creates JSON representations of the supported objects and operations. The command output includes the JSON payload that you submitted, along with the `operationOptions` and `objectTypes`.

   |   |                                                                                                                                                                                                                                                                                                                                                                                              |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Because IDM produces a full property set for all attributes and all object types in the schema, the resulting configuration can be very large. For an LDAP server, for example, IDM can generate a configuration containing several tens of thousands of lines. It might be useful to reduce the schema on the external resource to a minimum before you run the `createFullConfig` command. |

4. When you have the final configuration, use a PUT request to add it to the IDM configuration, in the JSON payload of the following command:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --header "Content-Type: application/json" \
   --request PUT \
   --data '{complete-configuration}' \
   "http://localhost:8080/openidm/config/provisioner.openicf/connectorName"
   ```

   Alternatively, you can save the complete configuration in a file named `provisioner.openicf-connectorName.json`, and place the file in the `conf` directory of your project.

## Connector reference properties

The following example shows a connector reference object:

```json
"connectorRef" : {
    "bundleName"    : "org.forgerock.openicf.connectors.csvfile-connector",
    "bundleVersion" : "[1.5.0.0,1.6.0.0)",
    "connectorName" : "org.forgerock.openicf.csvfile.CSVFileConnector",
    "connectorHostRef" : "csv"
}
```

* `bundleName`

  string, required

  The `ConnectorBundle-Name` of the ICF connector.

* `bundleVersion`

  string, required

  The `ConnectorBundle-Version` of the ICF connector. The value can be a single version (such as `1.4.0.0`) or a range of versions, which lets you support multiple connector versions in a single project.

  You can specify a range of versions as follows:

  * `[1.1.0.0,1.4.0.0]` indicates that all connector versions from 1.1 to 1.4, inclusive, are supported.

  * `[1.1.0.0,1.4.0.0)` indicates that all connector versions from 1.1 to 1.4, including 1.1 but excluding 1.4, are supported.

  * `(1.1.0.0,1.4.0.0]` indicates that all connector versions from 1.1 to 1.4, excluding 1.1 but including 1.4, are supported.

  * `(1.1.0.0,1.4.0.0)` indicates that all connector versions from 1.1 to 1.4, exclusive, are supported.

  When a range of versions is specified, IDM uses the latest connector that is available within that range. If your project requires a specific connector version, you must explicitly state the version in your connector configuration file, or constrain the range to address only the version that you need.

* `connectorName`

  string, required

  The connector implementation class name.

* `connectorHostRef`

  string, optional

  If the connector runs remotely, the value of this field must match the `name` field of the `RemoteConnectorServers` object in the connector server configuration file (`provisioner.openicf.connectorinfoprovider.json`). For example:

  ```json
  ...
      "remoteConnectorServers" :
          [
              {
                  "name" : "dotnet",
                  ...
              }
          ]
  ...
  ```

  If the connector runs locally, the value of this field can be one of the following:

  * If the connector .jar is installed in `openidm/connectors/` , the value must be `"#LOCAL"`. This is currently the default, and recommended location.

  * If the connector .jar is installed in `openidm/bundle/` (not recommended), the value must be `"osgi:service/org.forgerock.openicf.framework.api.osgi.ConnectorManager"`.

## Pool configuration

Learn more about [Connection pooling configuration](pooling.html) and the connectors that use each pooling mechanism in [Connector by pooling mechanism](pooling.html#pooling-table).

## Operation timeouts

Use the `operationTimeout` property to configure timeout values for each operation type. Use the value `-1` to configure an operation to have no timeout.

Default operation timeouts

```json
{
  "CREATE"              : 15000,
  "UPDATE"              : 15000,
  "DELETE"              : 15000,
  "TEST"                : 5000,
  "SCRIPT_ON_CONNECTOR" : 15000,
  "SCRIPT_ON_RESOURCE"  : 15000,
  "GET"                 : 15000,
  "RESOLVEUSERNAME"     : 10000,
  "AUTHENTICATE"        : 10000,
  "SEARCH"              : 15000,
  "VALIDATE"            : 5000,
  "SYNC"                : 15000,
  "SCHEMA"              : 10000
}
```

* operation-name

  Timeout in milliseconds

  A value of `-1` disables the timeout.

## Operation rate limits

The `operationRateLimits` property enables you to configure rate limit values per operation type. By default, no rate limit is configured for any operation type. A sample configuration follows:

```json
"operationRateLimits": {
  "CREATE": {
    "requestLimit": 50,
    "requestPeriod": 500,
    "requestTimeout": 5000
  }
}
```

* `operation-name`

  * `requestLimit`

    The number of requests allowed over a period of time (`requestPeriod`). The default value is `50` requests.

  * `requestPeriod`

    The request limit resets after this period of time (in milliseconds). The default value is `500` milliseconds.

    For example, using the previous example configuration allows 50 requests in a 500 millisecond period of time.

  * `requestTimeout`

    The amount of time (in milliseconds) before throwing an `OperationTimeoutException` for an operation. The default is `5000` milliseconds (5 seconds).

## Connection configuration

The `configurationProperties` object specifies the configuration for the connection between the connector and the resource, and is therefore resource-specific.

The following example shows a configuration properties object for the default CSV sample resource connector:

```json
"configurationProperties" : {
    "csvFile" : "&{idm.instance.dir}/data/csvConnectorData.csv"
}
```

* property

  Individual properties depend on the type of connector.

## Synchronization failure configuration

The `syncFailureHandler` object specifies what should happen if a liveSync operation reports a failure for an operation. The following example shows a synchronization failure configuration:

```json
{
    "maxRetries" : 5,
    "postRetryAction" : "logged-ignore"
}
```

* `maxRetries`

  positive integer or `-1`, required

  The number of attempts that IDM should make to process a failed modification. A value of zero indicates that failed modifications should not be reattempted. In this case, the post retry action is executed immediately when a liveSync operation fails. A value of -1 (or omitting the `maxRetries` property, or the entire `syncFailureHandler` object) indicates that failed modifications should be retried an infinite number of times. In this case, no post retry action is executed.

* `postRetryAction`

  string, required

  The action that should be taken if the synchronization operation fails after the specified number of attempts. The post retry action can be one of the following:

  * `logged-ignore` - IDM ignores the failed modification, and logs its occurrence.

  * `dead-letter-queue` - IDM saves the details of the failed modification in a table in the repository (accessible over REST at `repo/synchronisation/deadLetterQueue/provisioner-name`).

  * `script` specifies a custom script that should be executed when the maximum number of retries has been reached.

  Learn more in [Configure the LiveSync Retry Policy](https://docs.pingidentity.com/pingidm/8/synchronization-guide/chap-implicit-live-sync.html#livesync-retry-strategy).

## Configure how results are handled

The `resultsHandlerConfig` object specifies how OpenICF returns results. These configuration properties do not apply to all connectors and depend on the interfaces that are implemented by each connector. For information about the interfaces that connectors support, refer to the [Connector reference](preface.html).

The following example shows a results handler configuration object:

```json
"resultsHandlerConfig" : {
    "enableNormalizingResultsHandler" : true,
    "enableFilteredResultsHandler" : false,
    "enableCaseInsensitiveFilter" : false,
    "enableAttributesToGetSearchResultsHandler" : false
}
```

* `enableNormalizingResultsHandler`

  boolean, false by default

  When this property is enabled, ICF normalizes returned attributes to ensure that they are filtered consistently. If the connector implements the attribute normalizer interface, enable the interface by setting this property to `true`. If the connector does not implement the attribute normalizer interface, the value of this property has no effect.

* `enableFilteredResultsHandler`

  boolean, false by default

  Most connectors use the filtering and search capabilities of the remote connected system. In these cases, you can leave this property set to `false`. If the connector does not use the remote system's filtering and search capabilities, you *must* set this property to `true`.

  All the non-scripted connectors, except for the CSV connector, use the filtering mechanism of the remote system. In the case of the CSV connector, the remote resource has no filtering mechanism, so you must set `enableFilteredResultsHandler` to `true`. For the scripted connectors, the setting will depend on how you have implemented the connector.

* `enableCaseInsensitiveFilter`

  boolean, false by default

  This property applies only if `enableFilteredResultsHandler` is set to `true`. The filtered results handler is case-sensitive by default. For example, a search for `lastName = "Jensen"` will not match a stored user with `lastName : jensen`. When the filtered results handler is enabled, you can use this property to enable case-insensitive filtering. If you leave this property set to `false`, searches on that resource will be case-sensitive.

* `enableAttributesToGetSearchResultsHandler`

  boolean, false by default

  By default, IDM determines which attributes should be retrieved in a search. If you set this property to `true`, the ICF framework removes *all* attributes from the READ/QUERY response, except for those that are specifically requested. For performance reasons, you should set this property to `false` for local connectors and to `true` for remote connectors.

## Specify which attributes are updated

The `excludeUnmodified` property determines which properties are updated during synchronization. When this property is set to `true`, synchronization operations update *only* the modified properties on a target resource, rather than the whole target object. The default behavior is to include all attributes. In the sample LDAP provisioner files provided with IDM, `excludeUnmodified` is set to `true`, so unmodified attributes are excluded during update operations.

## Set the supported object types

The `objectTypes` configuration specifies the object types (user, group, account, and so on) that are supported by the connector. The object names that you define here determine how the object is accessed in the URI. For example:

```none
system/systemName/objectType
```

This configuration is based on the [JSON Schema](https://json-schema.org) with the extensions described in the following section.

Attribute names that start or end with `__` are regarded as *special attributes* by OpenICF. The purpose of the special attributes in ICF is to enable someone who is developing a *new* connector to create a contract regarding how a property can be referenced, regardless of the application that is using the connector. In this way, the connector can map specific object information between an arbitrary application and the resource, without knowing how that information is referenced in the application.

These attributes have no specific meaning in the context of IDM, although some of the connectors that are bundled with IDM use these attributes. The generic LDAP connector, for example, can be used with PingDS (DS), Active Directory, OpenLDAP, and other LDAP directories. Each of these directories might use a different attribute name to represent the same type of information. For example, Active Directory uses `unicodePassword` and DS uses `userPassword` to represent the same thing, a user's password. The LDAP connector uses the special OpenICF `__PASSWORD__` attribute to abstract that difference. In the same way, the LDAP connector maps the `__NAME__` attribute to an LDAP `dn`.

The ICF `__UID__` is a special case. The `__UID__` *must not* be included in the IDM configuration or in any update or create operation. This attribute denotes the unique identity attribute of an object and IDM always maps it to the `_id` of the object.

The following excerpt shows the configuration of an `account` object type:

```json
{
    "account" : {
        "$schema" : "http://json-schema.org/draft-03/schema",
        "id" : "__ACCOUNT__",
        "type" : "object",
        "nativeType" : "__ACCOUNT__",
        "absentIfEmpty" : false,
        "absentIfNull" : true,
        "properties" : {
            "name" : {
                "type" : "string",
                "nativeName" : "__NAME__",
                "nativeType" : "JAVA_TYPE_PRIMITIVE_LONG",
                "flags" : [
                    "NOT_CREATABLE",
                    "NOT_UPDATEABLE",
                    "NOT_READABLE",
                    "NOT_RETURNED_BY_DEFAULT"
                ]
            },
            "groups" : {
                "type" : "array",
                "items" : {
                    "type" : "string",
                    "nativeType" : "string"
                },
                "nativeName" : "__GROUPS__",
                "nativeType" : "string",
                "flags" : [
                    "NOT_RETURNED_BY_DEFAULT"
                ]
            },
            "givenName" : {
                "type" : "string",
                "nativeName" : "givenName",
                "nativeType" : "string"
            },
        }
    }
}
```

ICF supports an `__ALL__` object type that ensures that objects of every type are included in a synchronization operation. The primary purpose of this object type is to prevent synchronization errors when multiple changes affect more than one object type.

For example, imagine a deployment synchronizing two external systems. On system A, the administrator creates a user, `jdoe`, then adds the user to a group, `engineers`. When these changes are synchronized to system B, if the `__GROUPS__` object type is synchronized first, the synchronization will fail, because the group contains a user that does not yet exist on system B. Synchronizing the `__ALL__` object type ensures that user `jdoe` is created on the external system before he is added to the group `engineers`.

The `__ALL__` object type is assumed by default - you do not need to declare it in your provisioner configuration file. If it is not declared, the object type is named `__ALL__`. If you want to map a different name for this object type, declare it in your provisioner configuration. The following excerpt from a sample provisioner configuration uses the name `allobjects`:

```json
"objectTypes": {
    "allobjects": {
        "$schema": "http://json-schema.org/draft-03/schema",
        "id": "__ALL__",
        "type": "object",
        "nativeType": "__ALL__"
    },
    ...
}
```

A liveSync operation invoked with no object type assumes an object type of `__ALL__`. For example, the following call invokes a liveSync operation on all defined object types in an LDAP system:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
"http://localhost:8080/openidm/system/ldap?_action=liveSync"
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Using the `__ALL__` object type requires a mechanism to ensure the order in which synchronization changes are processed. Servers that use the `cn=changelog` mechanism to order sync changes, such as PingDS (DS), Oracle DSEE, and the legacy Sun Directory Server, cannot use the `__ALL__` object type by default. Such servers must be forced to use timestamps to order their sync changes. For these LDAP server types, set `useTimestampsForSync` to `true` in the provisioner configuration.Additionally, you can use the `timestampSyncOffset` LDAP configuration property to account for replication delays between LDAP instances. Refer to [LDAP connector](ldap.html).LDAP servers that use timestamps rather than change logs (such as Active Directory GCs and OpenLDAP) can use the `__ALL__` object type without any additional configuration. Active Directory and Active Directory LDS, which use Update Sequence Numbers, can also use the `__ALL__` object type without additional configuration. |

### Add objects and properties through the UI

To add object types and properties to a connector configuration by using the admin UI, select Configure > Connectors. Select the connector that you want to change, then select the Object Types tab.

In the case of the LDAP connector, the connector reads the schema from the remote resource to determine the object types and properties that can be added to its configuration. When you select one of these object types, you can think of it as a template. Edit the basic object type, as required, to suit your deployment.

To add a property to an object type, select the Edit icon next to the object type, then select Add Property.

### Specify object types on the external resource

At the object level, the `nativeType` property refers to an object type supported by a connector or external resource. For example, an LDAP connector might have object types such as `__ACCOUNT__` and `__GROUP__`.

* `nativeType`

  string, optional

  The native ICF object type.

  The value of this property must be an object type supported by the resource or the connector.

### Behavior for empty attributes

The `absentIfEmpty` and `absentIfNull` object class properties enable you to specify how attributes are handled during synchronization if their values are null (for single-valued attributes) or empty (for multivalued attributes). You can set these properties per object type.

By default, these properties are set as follows:

* `"absentIfEmpty" : false`

  Multivalued attributes whose values are empty are included in the resource response during synchronization.

* `"absentIfNull" : true`

  Single-valued attributes whose values are null are removed from the resource response during synchronization.

### Specify attribute types on the external resource

At the property level, `nativeType` refers to the data type of an attribute on the external resource.

* `nativeType`

  string, optional

  The native ICF attribute type.

  The following native types are supported:

  ```
  JAVA_TYPE_BIGDECIMAL
  JAVA_TYPE_BIGINTEGER
  JAVA_TYPE_BYTE
  JAVA_TYPE_BYTE_ARRAY
  JAVA_TYPE_CHAR
  JAVA_TYPE_CHARACTER
  JAVA_TYPE_DATE
  JAVA_TYPE_DOUBLE
  JAVA_TYPE_FILE
  JAVA_TYPE_FLOAT
  JAVA_TYPE_GUARDEDBYTEARRAY
  JAVA_TYPE_GUARDEDSTRING
  JAVA_TYPE_INT
  JAVA_TYPE_INTEGER
  JAVA_TYPE_LONG
  JAVA_TYPE_OBJECT
  JAVA_TYPE_PRIMITIVE_BOOLEAN
  JAVA_TYPE_PRIMITIVE_BYTE
  JAVA_TYPE_PRIMITIVE_DOUBLE
  JAVA_TYPE_PRIMITIVE_FLOAT
  JAVA_TYPE_PRIMITIVE_LONG
  JAVA_TYPE_STRING
  ```

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | * IDM only handles JSON primitive types (`boolean`, `map`, `list`, `number`, and `string`). You must encode any non-JSON primitive types so that they can be stored as JSON.

    As a general rule, your connector configurations should always map the property type on the external resource (`nativeType`) to a supported JSON primitive type in IDM. If you are synchronizing pre-hashed passwords, set the `nativeType` to a `JAVA_TYPE_BYTE_ARRAY`, and the IDM `type` to a `string`, for example:

    ```json
    ...
        "userPassword" : {
            "type" : "string",
            "nativeName" : "userPassword",
            "nativeType" : "JAVA_TYPE_BYTE_ARRAY"
        },
    ...
    ```

    With this configuration, when a `userPassword` is read from the remote system, it is returned as a `Byte[]` by the connector. It is then converted to a `String` (Base64-encoded `Byte[]`) by IDM.

    Alternatively, you can make sure that any non-JSON primitive types returned by your connector are appropriately [transformed](https://docs.pingidentity.com/pingidm/8/synchronization-guide/mapping-transforming-attributes.html) into an encoded `string` value in your mapping. For example:

    ```json
    {
        "source": "password",
        "target": "password",
        "transform": {
            "type": "text/javascript",
            "source": "source.toString();"
        }
    },
    ```

  * The `JAVA_TYPE_DATE` property is deprecated. Functionality may be removed in a future release. This type is an alias for `string`. Any dates with this type should be formatted according to ISO 8601. |

* `nativeName`

  string, optional

  The native ICF attribute name.

- `flags`

  string, optional

  The native ICF attribute flags. ICF supports the following attribute flags:

  * `MULTIVALUED`

    The property can be multivalued.

    For multivalued properties, if the property value type is anything other than a `string`, you *must* include an `items` property that declares the data type.

    The following example shows the `entries` property of the `authentication` object in a provisioner file. The `entries` property is multivalued, and its elements are of type `object`:

    ```json
    "authentication" : {
        ...
        "properties" : {
            ...
            "entries" : {
                "type" : "object",
                "required" : false,
                "nativeName" : "entries",
                "nativeType" : "object",
                    "items" : {
                        "type" : "object"
                    },
                "flags" : [
                    "MULTIVALUED"
                ]
            },
            ...
        },
        ...
    }
    ```

    |   |                                                                                                                                                                                                                                                                     |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | When comparing multivalued properties across systems, the *order* of the values is important. Two properties with the same values, but in different orders, will be seen as a *change* during reconciliation, regardless of whether the value has actually changed. |

  * `NOT_CREATABLE`, `NOT_READABLE`, `NOT_UPDATEABLE`

    In some cases, the connector might not support manipulating an attribute because the attribute can only be changed directly on the remote system. For example, if the `name` attribute of an account can only be created by Active Directory, and *never* changed by IDM, you would add `NOT_CREATABLE` and `NOT_UPDATEABLE` to the provisioner configuration for that attribute.

  * `NOT_RETURNED_BY_DEFAULT`

    Some attributes, such as LDAP groups or other calculated attributes, can be expensive to read. To avoid returning these attributes in a default read of the object, unless they are explicitly requested, add the `NOT_RETURNED_BY_DEFAULT` flag to the provisioner configuration for that attribute.

    You can also use this flag to prevent properties from being read by default during a synchronization operation. To synchronize changes to a target object, IDM performs an UPDATE rather than a PATCH. This causes *all* attributes that are mapped from the source to the target to be modified when the synchronization is processed (rather than only those attributes that have changed). Although the *value* of a property might not change, the property still registers an update. This behavior can be problematic for properties such as the `password`, which might have restrictions on updating with a similar value. To prevent such properties from being updated during synchronization, set the `NOT_RETURNED_BY_DEFAULT` flag, which effectively prevents the property from being read from the source during the synchronization. For example:

    ```json
    "__PASSWORD__" : {
        "type" : "string",
        "nativeName" : "__PASSWORD__",
        "nativeType" : "JAVA_TYPE_GUARDEDSTRING",
        "flags" : [
            "NOT_RETURNED_BY_DEFAULT"
        ],
        "runAsUser" : true
    }
    ```

You can configure connectors to enable provisioning of any arbitrary property. For example, the following property definitions would enable you to provision image files, used as avatars, to `account` objects in a system resource. The first definition would work for a single photo encoded as a base64 string. The second definition would work for multiple photos encoded in the same way:

```json
"attributeByteArray" : {
    "type" : "string",
    "nativeName" : "attributeByteArray",
    "nativeType" : "JAVA_TYPE_BYTE_ARRAY"
},
```

```json
"attributeByteArrayMultivalue": {
    "type": "array",
    "items": {
        "type": "string",
        "nativeType": "JAVA_TYPE_BYTE_ARRAY"
    },
    "nativeName": "attributeByteArrayMultivalue"
},
```

|   |                                                                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Do not use the dash character ( `-` ) in property names, like `last-name`. Dashes in names make JavaScript syntax more complex. If you cannot avoid the dash, write `source['last-name']` instead of `source.last-name` in your JavaScript scripts. |

## Configure operation options

The `operationOptions` object enables you to deny specific operations on a resource. For example, you can use this configuration object to deny `CREATE` and `DELETE` operations on a read-only resource to avoid IDM accidentally updating the resource during a synchronization operation.

The following example defines the options for the `"SYNC"` operation:

```json
"operationOptions" : {
    "SYNC" : {
        "denied" : true,
        "onDeny" : "DO_NOTHING",
        "objectFeatures" : {
            "__ACCOUNT__" : {
                "denied" : true,
                "onDeny" : "THROW_EXCEPTION",
                "operationOptionInfo" : {
                    "$schema" : "http://json-schema.org/draft-03/schema",
                    "type" : "object",
                    "properties" : {
                        "_OperationOption-float" : {
                            "type" : "number",
                            "nativeType" : "JAVA_TYPE_PRIMITIVE_FLOAT"
                        }
                    }
                }
            },
            "__GROUP__" : {
                "denied" : false,
                "onDeny" : "DO_NOTHING"
            }
        }
    },
    ...
}
```

The ICF Framework supports the following operations:

* `AUTHENTICATE`

* `CREATE`

* `DELETE`

* `GET`

* `RESOLVEUSERNAME`

* `SCHEMA`

* `SCRIPT_ON_CONNECTOR`

* `SCRIPT_ON_RESOURCE`

* `SEARCH`

* `SYNC`

* `TEST`

* `UPDATE`

* `VALIDATE`

For detailed information on these operations, refer to the [ICF API documentation](../_attachments/apidocs/index.html).

The `operationOptions` object has the following configurable properties:

* `denied`

  boolean, optional

  This property prevents operation execution if the value is `true`.

* `onDeny`

  string, optional

  If `denied` is `true`, then the service uses this value. Default value: `DO_NOTHING`.

  * `DO_NOTHING`: On operation the service does nothing.

  * `THROW_EXCEPTION`: On operation the service throws a `ForbiddenException` exception.

---

---
title: Configuring <code>ldapGroups</code> in the LDAP connector
description: How to configure and use the ldapGroups virtual attribute in the LDAP connector to manage LDAP group memberships from PingIDM
component: openicf
page_id: openicf:connector-reference:ldapgroups
canonical_url: https://docs.pingidentity.com/openicf/connector-reference/ldapgroups.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  ldapgroups-membership: LDAP group membership
  example_memberof_in_ad: "Example: memberOf in AD"
  example_ismemberof_in_pingds_ds: "Example: isMemberOf in PingDS (DS)"
  ldapgroups-overview: "ldapGroups: A connector-level solution"
  ldapgroups-configuring: Configuration
  1_add_ldapgroups_to_the_connector_schema: 1. Add ldapGroups to the connector schema
  2_update_user_mapping: 2. Update user mapping
  example_assigning_ad_groups_using_roles: "Example: Assigning AD groups using roles"
  ldapgroups-performance: Performance and functional considerations
  performance_cost: Performance cost
  functional_limitations_default_behavior: Functional limitations (default behavior)
  ldapgroups-comparison: ldapGroups compared to memberOf and isMemberOf
  ldapgroups-parameter: The ldapGroupsUseStaticGroups parameter
  base_context_filtering: Base context filtering
  ad_considerations: AD considerations
  ldapgroups-best-practices: Recommendations and best practices
---

# Configuring `ldapGroups` in the LDAP connector

The LDAP Connector includes a special virtual attribute, `ldapGroups`, which simplifies managing LDAP group memberships. This topic explains the [functionality of `ldapGroups`](#ldapgroups-membership), [provides configuration instructions](#ldapgroups-configuring), details [important considerations](#ldapgroups-performance), and [best practices](#ldapgroups-best-practices).

## LDAP group membership

In standard LDAP directories, such as PingDS or Active Directory (AD), directory servers typically store group membership information on the **group** entry, not the **user** entry. A group object contains a list of its members, often as distinguished names (DNs) pointing to user entries (for example, using the `member` or `uniqueMember` attribute).

By default, a user entry doesn't list the groups to which it belongs, so a client application could need to search numerous group entries to determine a user's group memberships. To simplify this process, most directory servers provide a **computed** attribute on the user entry that dynamically lists the groups where the user is a member.

* In **PingDS**, this attribute is `isMemberOf`.

* In **AD**, this attribute is `memberOf`.

These attributes are valuable for reading membership information but are **read-only**. You cannot directly modify a user's `memberOf` or `isMemberOf` attribute to change group memberships; you must modify the actual group entry's member list.

### Example: `memberOf` in AD

A query for an AD user might return:

```
dn: CN=user five,OU=test1,DC=example,DC=com
...
memberOf: CN=testgroup,OU=test1,DC=example,DC=com
...
```

### Example: `isMemberOf` in PingDS (DS)

A query for a DS user, requesting the `isMemberOf` attribute, might return:

```
dn: uid=user.3,ou=People,dc=example,dc=com
...
isMemberOf: cn=Test Group,ou=groups,dc=example,dc=com
...
```

|   |                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Directory servers often do not return these calculated attributes by default because their computation incurs a performance cost. You typically need to request these attributes in LDAP searches. |

## `ldapGroups`: A connector-level solution

The `ldapGroups` attribute is a feature **specific to the LDAP Connector**. It functions as a writable proxy for managing group memberships directly using the user object within IDM.

When you map and use `ldapGroups`:

* **Reads (GET operations):** The connector determines the user's group memberships. By default, it does this by searching group entries on the target directory for the user's DN (for example, searching for `(member=<userDN>)` or `(uniqueMember=<userDN>)`).

* **Writes (Update operations):** When you add or remove group DNs from the `ldapGroups` attribute in IDM and save the user object, the connector translates these changes into the necessary LDAP modify operations against the **group** entries on the target directory (adding or removing the user's DN from the group's member list).

This mechanism lets you manage group assignments within IDM (for example, through role assignments) without directly interacting with group objects.

## Configuration

To use `ldapGroups`, configure it in the LDAP connector's provisioner file (`provisioner.openicf-ldap.json` or similar) and include it in the user object mapping.

### 1. Add `ldapGroups` to the connector schema

Add the following definition to the `account` object type within the connector configuration's `objectTypes` section:

```json
"ldapGroups" : {
  "type" : "array",
  "nativeType" : "string",
  "nativeName" : "ldapGroups",
  "required" : false,
  "items" : {
    "type" : "string",
    "nativeType" : "string"
  }
}
```

### 2. Update user mapping

The goal of this step is to produce a list of group DN values for `ldapGroups` during the synchronization process. There are a variety of methods which you can use, including:

* Property mappings

* An `onUpdate` script

* Role assignment processing

Ensure the synchronization mapping (`sync.json`) for the user object includes a mapping for `ldapGroups`. For example:

```json
{
    "source": "ldapGroups",
    "target": "ldapGroups"
}
```

If you manage assignments using roles, configure the role assignment to target the `ldapGroups` attribute. You can also grant roles to users directly. Learn more in [Roles](https://docs.pingidentity.com/pingidm/8/objects-guide/roles.html) in the PingIDM documentation.

### Example: Assigning AD groups using roles

1. Configure the connector and mapping as described previously.

2. Create an internal role (for example, "AD Finance Group Users").

3. In the admin UI, navigate to the role's Managed Assignments (or equivalent section).

4. Create a new assignment targeting the appropriate AD connector or mapping.

5. Select the `ldapGroups` attribute.

6. Select the desired AD group (for example, `CN=Finance Users,OU=Groups,DC=example,DC=com`) from the provided list.

7. Save the assignment and the role.

Assigning this IDM role to a user automatically adds that user to the specified AD group. Learn more in [Working with role assignments](https://docs.pingidentity.com/pingidm/8/objects-guide/working-with-role-assignments.html) in the PingIDM documentation.

## Performance and functional considerations

Although `ldapGroups` offers convenience, it's crucial to understand its implications.

### Performance cost

* **Default read behavior:** By default, `ldapGroups` requires the connector to search group entries on the target directory. This makes read operations (such as GET User or reconciliation) consume more resources. The connector performs an additional search for each user to identify the **static** groups they belong to. This slows performance when querying for many users with `ldapGroups` included or, to a lesser extent, users who are members of many groups.

* **Update behavior:** Updates involving `ldapGroups` also add overhead. The connector must determine the user's current group memberships (often involving another search), calculate the difference between the current state and the desired state, and then execute LDAP modify operations on the relevant group entries. This can slow performance when updating groups with many members.

### Functional limitations (default behavior)

* **Static groups only:** By default, `ldapGroups` discovers and manages only memberships in **static** groups (those that have explicit `member` or `uniqueMember` attributes). It does **not** recognize or manage memberships from:

* **Dynamic groups:** Groups where rules or LDAP URLs determine membership (common in DS).

* **Nested groups:** Groups that contain other groups as members.

* **Incomplete view:** Relying **only** on `ldapGroups` (using default settings) to ascertain a user's effective group memberships might give an incomplete picture if your environment uses dynamic or nested groups.

### `ldapGroups` compared to `memberOf` and `isMemberOf`

|                |                                       |                                            |
| -------------- | ------------------------------------- | ------------------------------------------ |
| Feature        | `ldapGroups`                          | `memberOf` and `isMemberOf`                |
| **Purpose**    | Read/write proxy for group membership | Read-only view of group membership         |
| **Scope**      | Static groups only                    | All group types (static, dynamic, nested)  |
| **Writable?**  | Yes (using connector logic)           | No (read-only virtual attribute)           |
| **Read cost**  | Higher (connector searches groups)    | Lower (directory calculates; often faster) |
| **Managed by** | LDAP Connector                        | Target directory server                    |

### The `ldapGroupsUseStaticGroups` parameter

To address performance and functional limitations, the LDAP connector includes the `ldapGroupsUseStaticGroups` configuration parameter (located in the main connector configuration file, `provisioner.openicf-ldap.json`).

* **`false` (default):** `ldapGroups` operates as described previously, searching static group entries. This approach is safer for updates involving mixed group types but has performance drawbacks and limits visibility to static groups.

* **`true`:** `ldapGroups` uses the directory's `memberOf` (AD) or `isMemberOf` (DS) virtual attribute for **reading** group memberships.

* **Pros:** Improves read and query performance; includes dynamic and nested groups in the results that `ldapGroups` returns.

* **Cons:** **Presents high risk for updates.** If IDM tries to modify memberships derived from dynamic or nested groups (which `isMemberOf` or `memberOf` might return), the connector could attempt inappropriate LDAP operations (such as modifying a dynamic group as if it were static). This can lead to errors (for example, DS schema violation code 65) and failed updates. Use this setting only if the environment exclusively uses static groups and you have thoroughly tested it.

### Base context filtering

* When `ldapGroupsUseStaticGroups` is `false` (default), the connector's search for static groups follows the `baseContexts` defined in the connector configuration. The connector considers only groups within these specified base contexts.

* When `ldapGroupsUseStaticGroups` is `true`, the `memberOf` or `isMemberOf` attribute returns **all** groups the user belongs to, regardless of the connector's `baseContexts` setting. This happens because the directory server typically does not filter the virtual attribute itself by base context.

### AD considerations

* AD primarily uses static groups, which makes the default `ldapGroups` behavior suitable.

* AD's `memberOf` attribute does **not** natively display nested memberships unless the query includes a specific LDAP control (LDAP\_SERVER\_CHAINING\_OID: `1.2.840.113556.1.4.1941`). The connector's use of `memberOf` (when `ldapGroupsUseStaticGroups` is true) might or might not retrieve nested memberships, depending on internal implementation specifics.

## Recommendations and best practices

1. **Understand the trade-offs:** Recognize that `ldapGroups` offers convenience but affects performance and potentially adds complexity, particularly when different group types exist in the environment.

2. **Prefer `memberOf` or `isMemberOf` for reading:** To view a user's complete group memberships, you should map the directory's native `memberOf` or `isMemberOf` attribute as read-only (`"flags": ["NOT_CREATABLE", "NOT_UPDATEABLE"]`). This method is generally more efficient and comprehensive than reading `ldapGroups`.

3. **Use `ldapGroups` cautiously for writing:** If IDM must manage group memberships:

   * Keep the `ldapGroupsUseStaticGroups` setting as `false` (the default) unless you confirm the environment uses **only** static groups and you've performed comprehensive testing.

     |   |                                                                                                                                                                                                                                                                                                                                        |
     | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If you can't guarantee that only static groups are used and want to update the static groups, use a transform script. Create logic which filters all of the non-static groups from the `isMemberOf` group DN list. This allows you make reasonable updates to static groups without the high performance cost of reading `ldapGroups`. |

   * Consider adding the `"flags": ["NOT_RETURNED_BY_DEFAULT"]` to the `ldapGroups` definition within the provisioner file. This flag prevents the performance degradation that calculating `ldapGroups` causes during default read operations, such as reconciliation synchronization checks, while still allowing you to use it explicitly in updates or specific requests.

   * Add the `NOT_RETURNED_BY_DEFAULT` flag to optimize read performance:

     ```json
     {
       "ldapGroups": {
         "type": "array",
         "nativeType": "string",
         "nativeName": "ldapGroups",
         "required": false,
         "items": {
           "type": "string",
           "nativeType": "string"
         },
         "flags": [
           "NOT_RETURNED_BY_DEFAULT"
         ]
       }
     }
     ```

4. **Index directory attributes:** Ensure the directory server indexes the `member` (AD) or `uniqueMember` (DS) attributes on group objects. Indexing is critical to lessen the performance impact when `ldapGroups` searches static groups (`ldapGroupsUseStaticGroups: false`). Consult the directory server documentation for indexing best practices.

5. **Alternative: Manage group objects:** The most technically direct LDAP approach involves managing memberships by modifying the group objects directly within IDM (assuming you synchronize group objects). However, this method often requires more complex configuration and scripting compared to using `ldapGroups` through role assignments.

By understanding how `ldapGroups` operates and its associated trade-offs, you can configure it effectively to meet group management requirements while minimizing performance impacts and avoiding potential issues.

---

---
title: Connection pooling configuration
description: Explains ICF connector connection pooling mechanisms (ICF, HTTP, JDBC, connector-specific, non-poolable) and lists connectors by pooling type
component: openicf
page_id: openicf:connector-reference:pooling
canonical_url: https://docs.pingidentity.com/openicf/connector-reference/pooling.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  pooling-mechanisms: Pooling mechanisms
  icf-pooling: ICF pooling
  http-pooling: HTTP pooling
  jdbc-connectors: JDBC connectors
  connector-specific-pooling: Connector-specific pooling
  non-poolable-connectors: Non-poolable connectors
  pooling-table: Connectors by pooling mechanism
---

# Connection pooling configuration

Certain connectors can be pooled, while other connectors are non-poolable. Learn more about the five [Pooling mechanisms](#pooling-mechanisms) used in OpenICF and understand [Connectors by pooling mechanism](#pooling-table).

## Pooling mechanisms

If a connector depends on a third-party library that has its own pooling mechanism, then ICF leverages that pooling mechanism. For example, an HTTP connector uses an Apache HTTP client and a DB connector uses a Tomcat JDBC.

OpenICF uses an ICF pooling mechanism only if:

* A connector has no third-party library pooling mechanism, or

* If OpenICF can't control the amount of connections the third-party library uses. For example, the [Microsoft Graph API connector](ms-graph-api.html).

OpenICF uses the following pooling mechanisms to manage connections.

### ICF pooling

ICF pooling maintains connector objects and is managed by the framework. This pooling mechanism improves throughput and is used by, and is only relevant to, the connectors that implement the `PoolableConnector` interface.

For an ICF-pooled connector, ICF maintains a pool of connector instances and reuses these instances for connector operations. When an operation must be run, an existing connector instance is taken from the connector pool. If no connector instance exists, a new instance is initialized. When the operation has been run, the connector instance is released back into the connector pool, ready to be used for a subsequent operation.

The following example shows a pool configuration option object for an ICF poolable connector:

```json
{
  "maxObjects"                 : 10,
  "maxIdle"                    : 10,
  "maxWait"                    : 150000,
  "minEvictableIdleTimeMillis" : 120000,
  "minIdle"                    : 1
}
```

To configure ICF connection pooling, set the following values in the connector configuration file `poolConfigOptions` property:

* `maxObjects`

  The maximum number of connector instances in the pool, both idle and active. The default value is `10` instances.

* `maxIdle`

  The maximum number of idle connector instances in the pool. The default value is `10` idle instances.

* `maxWait`

  The maximum period to wait for a free connector instance to become available before failing. The default period is `150000` milliseconds, or 150 seconds.

* `minEvictableIdleTimeMillis`

  The minimum period to wait before evicting an idle connector instance from the pool. The default period is `120000` milliseconds, or 120 seconds.

* `minIdle`

  The minimum number of idle connector instances in the pool. If `minIdle=0`, then a connector pool cleaner thread will run and close expired connections.

### HTTP pooling

Connectors that use HTTP pooling require an HTTP client and leverage `PoolingHttpClientConnectionManager` to manage a pool of HTTP connections. Each connector defines and supports different properties that configure the pooling connection manager.

### JDBC connectors

This pooling mechanism applies to connectors interacting with a database. A Tomcat JDBC driver handles the pooling.

### Connector-specific pooling

For connector-specific pooling, the connector implements the pooling and can include properties to configure the pool.

### Non-poolable connectors

For non-poolable connectors, ICF creates a new instance of the connector class and uses a new or existing instance of the connector configuration to initialize the instance before the operation runs. After the operation is run, OpenICF disposes of the connector instance.

## Connectors by pooling mechanism

To ensure you configure the correct pooling option for a connector, consult the following table for a list of connectors by pooling type.

**Connectors by pooling mechanism**

| ICF                                             | HTTP                                            | JDBC connectors                     | Connector-specific                        | Non-poolable                                            |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------- | ----------------------------------------- | ------------------------------------------------------- |
| [Adobe Marketing Cloud](adobe.html)             | [Adobe Admin Console](adobe-admin-console.html) | [Database table](dbtable.html)      | [Amazon Web Services (AWS)](aws-iam.html) | [AS400](as400.html)                                     |
| [Groovy connector toolkit](groovy.html)         | [Box](box.html)                                 | [Oracle EBS](ebs.html)              |                                           | [AWS IAM Identity Center](aws-iam-identity-center.html) |
| [Kerberos](kerberos.html)                       | [Cerner](cerner.html)                           | [SAP HANA Database](saphanadb.html) |                                           | [CSV file](csv.html)                                    |
| [LDAP](ldap.html)                               | [DocuSign](docusign.html)                       | [Scripted SQL](scripted-sql.html)   |                                           | [Duo](duo.html)                                         |
| [Microsoft Graph API](ms-graph-api.html)        | [Dropbox](dropbox.html)                         |                                     |                                           | [Google Apps](google.html)                              |
| [PeopleSoft](peoplesoft.html)                   | [Epic](epic.html)                               |                                     |                                           | [Groovy connector toolkit](groovy.html)                 |
| [PowerShell connector toolkit](powershell.html) | [Google Cloud Platform (GCP)](gcp.html)         |                                     |                                           | [Multiple CSV](multicsv.html)                           |
| [ServiceNow](servicenow.html)                   | [HubSpot](hubspot.html)                         |                                     |                                           | [Multiple CSV Cloud](multicsvcloud.html)                |
| [SSH](ssh.html)                                 | [IBM RACF](racf.html)                           |                                     |                                           | [SAP S/4HANA](sap-hana.html)                            |
| [Workday](workday.html)                         | [Marketo](marketo.html)                         |                                     |                                           |                                                         |
|                                                 | [MongoDB](mongodb.html)                         |                                     |                                           |                                                         |
|                                                 | [PingOne](pingone.html)                         |                                     |                                           |                                                         |
|                                                 | [SaaS REST](rest.html)                          |                                     |                                           |                                                         |
|                                                 | [Salesforce](salesforce.html)                   |                                     |                                           |                                                         |
|                                                 | [SAP](sap.html)                                 |                                     |                                           |                                                         |
|                                                 | [SAP SuccessFactors](successfactors.html)       |                                     |                                           |                                                         |
|                                                 | [SCIM](scim.html)                               |                                     |                                           |                                                         |
|                                                 | [Scripted REST](scripted-rest.html)             |                                     |                                           |                                                         |
|                                                 | [Snowflake](snowflake.html)                     |                                     |                                           |                                                         |
|                                                 | [Webex](webex.html)                             |                                     |                                           |                                                         |

---

---
title: Connector logs
description: Configure ICF connector logging for PingIDM and the Remote Connector Server, including log levels, debug logging, and rolling log policies
component: openicf
page_id: openicf:connector-reference:icf-logs
canonical_url: https://docs.pingidentity.com/openicf/connector-reference/icf-logs.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Logs", "Troubleshooting"]
section_ids:
  logging_levels: Logging levels
  enable_idm_connector_logging: Enable IDM connector logging
  java_rcs_logging: Java RCS logging
  icf-logging-config-file: Logging configuration file
  enable_java_rcs_debug_logging: Enable Java RCS debug logging
  icf-rolling-log-policy: Rolling log policy
  troubleshooting_java_rcs_windows_logging: Troubleshooting Java RCS Windows logging
  net_rcs_logging: .NET RCS logging
---

# Connector logs

|   |                                             |
| - | ------------------------------------------- |
|   | By default, logging is not enabled for RCS. |

It can be difficult to determine if the root cause of a problem is at the ICF or connector level, or at the application level.

The ICF API sets the `LoggingProxy` at a very high level. You can consider the Logging Proxy as the *border* between the application (IDM) and the ICF framework.

## Logging levels

Finer logging levels generate more noise but can be helpful when troubleshooting:

* `SEVERE` (highest value, least noise)

* `WARNING`

* `INFO`

* `CONFIG`

* `FINE`

* `FINER`

* `FINEST` (lowest value, most noise)

## Enable IDM connector logging

If you are using ICF connectors bundled with IDM, you can adjust the log levels for specific parts of the system in the `path/to/openidm/conf/logging.properties` file. To start logging, enable the Logging Proxy and set the level for all or some operations:

Enable the LoggingProxy

```properties
org.identityconnectors.framework.impl.api.LoggingProxy.level=FINE
```

Log all operations

```properties
org.identityconnectors.framework.api.operations.level=FINE
```

Log specific operations

```properties
org.identityconnectors.framework.api.operations.CreateApiOp.level=FINE
org.identityconnectors.framework.api.operations.UpdateApiOp.level=FINE
org.identityconnectors.framework.api.operations.DeleteApiOp.level=FINE
```

You can log any of the following operations:

* `AuthenticationApiOp`

* `CreateApiOp`

* `DeleteApiOp`

* `GetApiOp`

* `ResolveUsernameApiOp`

* `SchemaApiOp`

* `ScriptOnConnectorApiOp`

* `ScriptOnResourceApiOp`

* `SearchApiOp`

* `SyncApiOp`

* `TestApiOp`

* `UpdateApiOp`

* `ValidateApiOp`

## Java RCS logging

### Logging configuration file

The default location for the logging configuration file is `/path/to/openicf/conf/logback.xml`.

You can set the configuration file location using the `LOGGING_CONFIG` system property. For example, you can add the system property to the `OPENICF_OPTS` environment variable before starting RCS:

```shell
export LOGGING_CONFIG="-Dlogback.configurationFile=/path/to/your/logback.xml"
```

### Enable Java RCS debug logging

|   |                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For additional Java RCS debug logging information, refer to this [Knowledge Base article](https://backstage.forgerock.com/knowledge/kb/article/a38411747). |

To enable debug logging in the remote Java Connector Server, uncomment the following line in the [logging configuration file](#icf-logging-config-file):

```xml
<logger name="org.identityconnectors.framework.impl.api.LoggingProxy" level="DEBUG" additivity="false">
    <appender-ref ref="TRACE-FILE"/>
</logger>
<logger name="org.identityconnectors.framework.api.operations" level="DEBUG" additivity="false">
    <appender-ref ref="TRACE-FILE"/>
</logger>
```

### Rolling log policy

To change the total size for all log files or maximum time length before a log rolls over to a new file, edit `conf/logback.xml` and update the applicable `maxHistory` and `totalSizeCap` properties. The default rolling log policy has the following configuration:

```xml
<maxHistory>30</maxHistory>
<totalSizeCap>1GB</totalSizeCap>
```

To roll log files based on both time and file size, configure the `SizeAndTimeBasedRollingPolicy`. This policy requires a `maxFileSize` property to define the maximum size of a single log file before a rollover occurs. Using this policy ensures individual log files remain a manageable size while still respecting your overall `maxHistory` and `totalSizeCap` retention limits.

Learn more in the Logback documentation:

* [maxHistory](https://logback.qos.ch/manual/appenders.html#tbrpMaxHistory)

* [totalSizeCap](https://logback.qos.ch/manual/appenders.html#tbrpTotalSizeCap)

* [SizeAndTimeBasedRollingPolicy](https://logback.qos.ch/manual/appenders.html#SizeAndTimeBasedRollingPolicy)

### Troubleshooting Java RCS Windows logging

If you previously started the RCS using `/run`, the user account that entered the command owns the log files in `openicf\logs\`. When you install and start the RCS as a Windows service, the Windows service account doesn't have write access to those log files. The service starts without error but produces no log output.

To avoid this issue, use one of the following workarounds before running `/install`:

* Delete the `openicf\logs\` directory. The RCS recreates it with the correct permissions when the service starts.

* In the Windows Services management console, open the RCS service properties, click the Log On tab, and select Local System Account.

  |   |                                                                                                                                                                     |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The Local System Account has broad local system privileges. For production deployments, grant the existing service account write access to `openicf\logs\` instead. |

Learn more about [installing the Java RCS on Windows](java-server.html#java-connector-server-windows).

## .NET RCS logging

To enable logging in the .NET RCS, edit the `ConnectorServer.exe.config` configuration file, and set the `logging.proxy` key to `true`:

```xml
<add key="logging.proxy" value="true"/>
```