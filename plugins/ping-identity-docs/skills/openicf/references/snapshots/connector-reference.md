---
description: Install, configure, and test the MS Graph API connector for Azure AD, including authentication methods, custom extension attributes, and account sync
component: openicf
page_id: openicf:connector-reference:msgraph-conf
canonical_url: https://docs.pingidentity.com/openicf/connector-reference/msgraph-conf.html
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

You can download any connector from [Backstage](https://backstage.forgerock.com/downloads/browse/idm/featured/connectors), but some are included in the default deployment for Advanced Identity Cloud, IDM, or RCS. When using an included connector, you can skip installing it and move directly to configuration.

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

You can download the MS Graph API connector [from here](https://backstage.forgerock.com/downloads/browse/idm/all/productId:idm-connectors).

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
