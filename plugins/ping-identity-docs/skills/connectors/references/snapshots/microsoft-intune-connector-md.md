---
title: Microsoft Intune Connector
description: Configure the Microsoft Intune connector in PingOne DaVinci to query and manage user devices through Microsoft Graph
component: connectors
page_id: connectors::microsoft_intune_connector
canonical_url: https://docs.pingidentity.com/connectors/microsoft_intune_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 24, 2026
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  configuring-the-microsoft-intune-connector: Configuring the Microsoft Intune connector
  connector-configuration: Connector configuration
  using-the-connector-in-a-flow: Using the connector in a flow
  managing-user-devices-in-a-flow: Managing user devices in a flow
  limitations: Limitations
  capabilities: Capabilities
  getDeviceBySerialNumber: Get Device by Serial Number
  userDeviceManagement: User Device Management
  makeCustomApiCall: Make Custom API Call
---

# Microsoft Intune Connector

The Microsoft Intune connector lets you access the resources and APIs available through [Microsoft Graph](https://learn.microsoft.com/en-us/graph/overview) in your PingOne DaVinci flow.

The connector queries devices by user and device serial number so that you can use device information in access decisions in your flow.

## Setup

### Resources

You can find more information and setup help in the following:

* Microsoft Intune documentation:

  * [Get access without a user](https://learn.microsoft.com/en-us/graph/auth-v2-service?view=graph-rest-1.0)

  * [List user devices](https://learn.microsoft.com/en-us/graph/api/user-list-owneddevices?view=graph-rest-1.0\&tabs=http)

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* An account with API access on the Microsoft identity platform.

### Configuring the Microsoft Intune connector

Add the connector in PingOne DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

| Setting       | Description                                                                                                    |
| ------------- | -------------------------------------------------------------------------------------------------------------- |
| Tenant        | Your Microsoft Entra tenant.                                                                                   |
| Client ID     | The client ID of your registered Microsoft application.                                                        |
| Client Secret | The client secret of your registered Microsoft application.                                                    |
| Grant Type    | The grant type used to request access tokens from the Microsoft identity platform, such as client_credentials. |
| Scope         | The scope of the access request, such as <https://graph.microsoft.com/.default>.                               |

## Using the connector in a flow

### Managing user devices in a flow

You can use the connector to get the list of devices owned by a user, retrieve device information by serial number, and make custom API calls to Microsoft Graph.

At a high level:

1. The **User Device Management** capability returns the list of devices owned by the user you specify, using the user ID or user principal name from an earlier node, such as an HTML form.

2. The **Get Device by Serial Number** capability retrieves device information using the device serial number you specify.

3. The **Make Custom API Call** capability calls a Microsoft Graph API that isn't available as a connector capability, using the endpoint, method, query parameters, headers, and request body you provide.

Test the flow by clicking **Save**, **Deploy**, and **Try Flow**.

## Limitations

Use of the connector is limited by the availability of the Microsoft Intune API and your account access.

## Capabilities

### Get Device by Serial Number

Retrieve device information using the device serial number.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Serial Number textField
>
>   Device Serial Number
>
> * default object
>
>   * properties object
>
>     * serialNumber string
>
>       Device Serial Number
>
> - output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * headers object

### User Device Management

User Device Management

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   user ID
>
> - User Principal Name textField
>
>   User Principal Name
>
> * default object
>
>   * properties object
>
>     * userId string
>
>       user ID
>
>     * userPrincipalName string
>
>       User Principal Name
>
> - output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * headers object

### Make Custom API Call

Define a custom API call to Microsoft Intune

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Endpoint textField required
>
>   Endpoint
>
> - Method dropDown required
>
>   The HTTP Method.
>
>   * GET
>
>   * POST
>
>   * PUT
>
>   * DELETE
>
>   * PATCH
>
> - Query Parameters keyValueList
>
>   Add query parameters and provide their values.
>
> - Headers keyValueList
>
>   Add HTTP headers and provide their values.
>
> - Body codeEditor
>
>   The raw JSON body, such as "{ "Username": "<jsmith@example.com>", "ProfileId": "00e8a0000024zkjAAA" }".
>
> * default object
>
>   * properties object
>
>     * endpoint string required
>
>       Server endpoint URL to where we send request
>
>     * method string required
>
>       Method
>
>     * queryParameters array
>
>       Query Parameters
>
>     * headers array
>
>       Headers
>
>     * body object
>
>       Body
>
> - output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * headers object