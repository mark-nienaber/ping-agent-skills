---
title: Marketo Connector
description: Configure the Marketo connector in PingOne DaVinci to add, search, and update leads and manage lists in Marketo
component: connectors
page_id: connectors::marketo_connector
canonical_url: https://docs.pingidentity.com/connectors/marketo_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  setting-up-marketo: Setting up Marketo
  configuring-the-marketo-connector: Configuring the Marketo connector
  connector-configuration: Connector configuration
  api-url: API URL
  client-id: Client ID
  client-secret: Client Secret
  using-the-connector-in-a-flow: Using the connector in a flow
  lead-management: Lead management
  list-management: List Management
  creating-a-custom-api-call: Creating a custom API call
  capabilities: Capabilities
  createLead: Create Lead
  createList: Create Static List
  searchList: Get List Information
  readLead: Read Lead
  updateLead: Update Lead
  searchLeads: Search Leads
  readListLeads: Read Static List Leads
  addLeadsToList: Add Leads to List
  makeCustomApiCall: Make Custom API Call
---

# Marketo Connector

The Marketo connector lets you add, search, and update leads into Marketo in your PingOne DaVinci flow.

You can use the Marketo connector to:

* Manage leads in Marketo

* Manage lists in Marketo

## Setup

### Resources

Learn more in the following:

* Marketo documentation:

  * [Marketo Setup Steps](https://experienceleague.adobe.com/docs/marketo/using/getting-started-with-marketo/setup/setup-steps.html?lang=en)

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* A Marketo license

* Your Marketo credentials

### Setting up Marketo

Follow the instructions in [Marketo Setup Checklist](https://experienceleague.adobe.com/docs/marketo/using/getting-started-with-marketo/setup/setup-checklist.html?lang=en).

### Configuring the Marketo connector

Add the connector in PingOne DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

##### API URL

The API endpoint for your Adobe Marketo instance, for example, `abc123.mktorest.com/rest`

##### Client ID

Your Adobe Marketo client ID

##### Client Secret

Your Adobe Marketo client secret

## Using the connector in a flow

### Lead management

The connector has several capabilities that allow you to manage users:

* **Create Lead**

* **Read Lead**

* **Update Lead**

* **Search Lead**

No special configuration is needed. Add the capability and populate its properties according to the help text.

### List Management

The connector has several capabilities that allow you to manage lists:

* **Create Static List**

* **Get List Information**

* **Read Static List Leads**

* **Add Leads to List**

No special configuration is needed. Add the capability and populate its properties according to the help text.

### Creating a custom API call

If you want to do something that isn't supported by one of the provided capabilities, you can use the **Make a Custom API Call** capability to define your own action.

This capability uses the credentials from your connector to make an API call with the HTTP method, headers, query parameters, and body you specify.

## Capabilities

### Create Lead

Create a new lead.

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - First Name textField
>
>   The user's first name.
>
> - Middle Name textField
>
>   The user's middle name.
>
> - Last Name textField
>
>   The user's last name.
>
> - Email textField required
>
>   The user's email address.
>
> - Phone Number textField
>
>   The user's phone number.
>
> - Custom Attributes keyValueList
>
>   Additional attributes.
>
> * output object
>
>   * rawResponse object
>
>     * result object
>
>       * requestId string
>
>       * result object
>
>         * id string
>
>         * status string
>
>       * success string
>
>   * statusCode number
>
>   * headers object

### Create Static List

Create a new static list.

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - List Name textField required
>
>   Enter a name for the new list.
>
> * output object
>
>   * rawResponse object
>
>     * result object
>
>       * id number
>
>       * name string
>
>       * createdAt date
>
>       * updatedAt date
>
>       * folder object
>
>         * id number
>
>         * type string
>
>         * name string
>
>       * computedUrl string
>
>   * statusCode number
>
>   * headers object

### Get List Information

Get information about one or more lists using the list ID, name, or folder.

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - Search Type dropDown required
>
>   Select "Use List ID" or "Use List Name" to get information about a single list, or select a folder to get information about all lists within it.
>
>   * Use Folder Name (Default)
>
>   * Use List ID
>
>   * Use List Name
>
> - Folder dropDown required
>
>   Select the folder that contains the lists you want information about.
>
> - List Name textField
>
>   The name of the list to get information about, such as "Founders".
>
> - List Type dropDown
>
>   Select the type of list you are reading. Smart lists support additional accuracy and functionality.
>
>   * Static List (Default)
>
>   * Smart List (Default)
>
> - List ID textField required
>
>   The unique ID for the list, such as "56789".
>
> * output object
>
>   * rawResponse object
>
>     * result array
>
>   * statusCode number
>
>   * headers object

### Read Lead

Read a lead using the lead ID.

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - Lead ID textField required
>
>   The unique identifier for the lead, such as "318581".
>
> * output object
>
>   * rawResponse object
>
>     * result object
>
>       * requestId string
>
>       * result object
>
>         * id string
>
>         * email string
>
>         * firstName string
>
>         * lastName string
>
>         * updatedAt string
>
>         * createdAt string
>
>       * success string
>
>   * statusCode number
>
>   * headers object

### Update Lead

Update an existing lead using the lead ID.

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - Lead ID textField required
>
>   The unique identifier for the lead, such as "318581".
>
> - First Name textField
>
>   The user's first name.
>
> - Middle Name textField
>
>   The user's middle name.
>
> - Last Name textField
>
>   The user's last name.
>
> - Email textField required
>
>   The user's email address.
>
> - Phone Number textField
>
>   The user's phone number.
>
> - Custom Attributes keyValueList
>
>   Additional attributes.
>
> * output object
>
>   * rawResponse object
>
>     * result object
>
>       * requestId string
>
>       * result array
>
>       * success string
>
>   * statusCode number
>
>   * headers object

### Search Leads

Search for one or more leads.

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - Search Attribute dropDown required
>
>   Select the Marketo lead attribute that you want to search.
>
>   * Cookies
>
>   * Department
>
>   * Email
>
>   * Email Suspended Cause
>
>   * External Company ID
>
>   * External Sales Person ID
>
>   * ID
>
>   * Lead Partition ID
>
>   * Marketo Name
>
> - Search Values textField required
>
>   Enter the values to look for in the search attribute. Separate multiple values with a comma, such as "138273,<jsmith@example.com>".
>
> * output object
>
>   * rawResponse object
>
>     * result object
>
>       * requestId string
>
>       * result array
>
>       * success string
>
>   * statusCode number
>
>   * headers object

### Read Static List Leads

Read leads in a static list using the list ID.

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - List ID textField required
>
>   The unique ID for the list, such as "56789".
>
> * output object
>
>   * rawResponse object
>
>     * result object
>
>       * requestId string
>
>       * result array
>
>       * success string
>
>   * statusCode number
>
>   * headers object

### Add Leads to List

Add leads to a list using lead IDs.

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - List ID textField required
>
>   The unique ID for the list, such as "56789".
>
> - Lead IDs textField required
>
>   Enter the unique ID of the leads to add to the list. Separate multiple values with a comma, such as "456123,987654".
>
> * output object
>
>   * rawResponse object
>
>     * result object
>
>       * requestId string
>
>       * result array
>
>       * success string
>
>   * statusCode number
>
>   * headers object

### Make Custom API Call

Define and use your own call to Adobe Marketo.

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - Custom Endpoint textField required
>
>   This endpoint is added to the base API URL selected in the connector configuration. Remeber to removed "rest/" from the endpoint
>
> - HTTP Method dropDown required
>
>   The HTTP method of the API call.
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
>   Query parameters for the request.
>
> - Additional Headers keyValueList
>
>   Define additional headers to send to Adobe Marketo. Learn more in the API documentation.
>
> - Body codeEditor
>
>   The body of the API call.
>
> * output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * headers object