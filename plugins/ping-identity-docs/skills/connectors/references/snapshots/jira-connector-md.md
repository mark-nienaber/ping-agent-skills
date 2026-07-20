---
title: Jira Connector
description: Configure the Jira connector to manage issues and trigger Jira workflows in your PingOne DaVinci flow
component: connectors
page_id: connectors::jira_connector
canonical_url: https://docs.pingidentity.com/connectors/jira_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  setting_up_jira: Setting up Jira
  setting-up-the-jira-connector-configuration: Setting up the Jira connector configuration
  connector-configuration: Connector configuration
  base-url: Base URL
  email-address: Email Address
  jira-api-token: Jira API token
  using-the-connector-in-a-flow: Using the connector in a flow
  managing-jira-issues: Managing Jira issues
  searching-for-jira-issues: Searching for Jira issues
  creating-a-custom-api-call: Creating a custom API call
  capabilities: Capabilities
  create-an-issue: Create an Issue
  get-issue-details: Get Issue Details
  update-an-issue: Update an Issue
  delete-an-issue: Delete an Issue
  assign-an-issue: Assign an Issue
  search-for-issues-using-jql: Search for Issues Using JQL
  make-custom-api-call: Make Custom API Call
---

# Jira Connector

The Jira connector lets you manage issues and trigger Jira workflows in your PingOne DaVinci flow.

You can use the Jira connector to:

* Search for issues in the Jira workflow

* Receive information about new and updated issues by listening for a webhook

* Set up a custom application programming interface (API) *(tooltip: \<div class="paragraph">
  \<p>A specification of interactions available for building software to access an application or service.\</p>
  \</div>)* call to suit your needs

## Setup

### Resources

Learn more in the following documentation:

* Jira documentation:

  * [Create an API token](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/)

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need a Jira license.

### Setting up Jira

Follow the instructions in [Create an API token](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/).

### Setting up the Jira connector configuration

In PingOne DaVinci, add a **Jira** connection. Learn more in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html).

#### Connector configuration

##### Base URL

The base URL for your Jira Cloud API. For example, `https://id.atlassian.com`.

##### Email Address

Your Jira administrator email address.

##### Jira API token

The Jira API token that you created in [Setting up Jira](#setting_up_jira), such as "bACbrdOf3q6vLCLGMSbxDDDD".

## Using the connector in a flow

### Managing Jira issues

The connector has several capabilities that allow you to manage issues in Jira:

* **Create an Issue**

* **Get Issue Details**

* **Delete an Issue**

* **Assign an Issue**

* **Update an Existing Issue**

No special flow configuration is needed. Add the capability you want and populate its properties according to the help text.

For capabilities that have a **Query Parameters** section, you can add any query parameters that are supported by the Jira API. Learn more in the [Jira Cloud platform REST API documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-groups/#api-group-groups).

### Searching for Jira issues

You can use the connector to search for Jira issues using the Jira Query Language (JQL).

The **JQL Query** field in the **Search for Issues Using JQL** capability accepts an advanced search string. Learn more in [Use advanced search with Jira Query Language (JQL)](https://support.atlassian.com/jira-work-management/docs/use-advanced-search-with-jira-query-language-jql/) in the Jira documentation.

Other properties let you control the type of information you get about the issues.

If you expect to get more results than the **Maximum Number of Results** you define, you can run the query several times with a different **Starting Result Number** to paginate the results.

### Creating a custom API call

If you want to do something not supported by one of the provided capabilities, you can use the **Make a Custom API Call** capability to define your own action.

This capability uses the credentials from your connector to make an API call with the HTTP method, headers, query parameters, and body you specify.

## Capabilities

### Create an Issue

Create an issue in JIRA.

> **Collapse: Show details**
>
> * * Properties
>   * Project `dropDown` `required`
>
>   The Jira project to create the issue in. For a dynamic value, select Use Project Key and enter a value in the Project Key field.
>
>   * Use Project Key (Default)
>
> * Project Key `textField` `required`
>
>   The Jira project to create the issue in, such as "PROJ".
>
> * Summary `textField` `required`
>
>   The issue summary, such as "Fix development workflow".
>
> * Issue Type `dropDown` `required`
>
>   The type of issue to create.
>
>   * Story
>
>   * Task
>
>   * Sub-task
>
>   * Bug
>
>   * Epic
>
> * Parent Issue ID `textField`
>
>   The ID of an existing issue, such as "PROJ-10". When this value is provided, the new issue will be created as a sub-task of the parent issue.
>
> * Components `textFieldArrayView`
>
>   The ID of the component to associate with the issue, such as "10000".
>
> * Description `textField`
>
>   The issue description, such as "Please fix the following development workflow issue…"
>
> * Reporter `dropDown`
>
>   The person reporting the issue. For a dynamic value, select Use Reporter ID and enter a value in the Reporter ID field.
>
>   * Leave Blank (Default)
>
>   * Use Reporter ID
>
> * Reporter ID `textField` `required`
>
>   The ID of the reporter, such as "5b10a2844c20165700ede21g".
>
> * Fix Versions `textFieldArrayView`
>
>   The ID of the fix version to associate with the issue, such as "10001". Type an ID and press Enter to add it.
>
> * Versions `textFieldArrayView`
>
>   The ID of the version to associate with the issue, such as "10001". Type an ID and press Enter to add it.
>
> * Due Date `textField`
>
>   The due date for the issue, formatted as "2022-01-30".
>
> * Assignee `dropDown`
>
>   The person to assign the issue to. For a dynamic value, select Use Assignee ID and enter a value in the Assignee ID field.
>
>   * Leave Blank (Default)
>
>   * Use Assignee ID
>
> * Assignee ID `textField` `required`
>
>   The ID of the assignee, such as "5b10a2844c20165700ede21g".
>
> * Priority `textField`
>
>   The priority for the issue, such as "3".
>
> * Labels `textFieldArrayView`
>
>   The labels to associate with the issue. Type a label and press enter to add it.
>
> * Query Parameters `keyValueList`
>
>   Define additional query parameters to send to Jira. Learn more in the Jira Cloud platform REST API documentation.
>
> * Other Attributes `variableInputList`
>
>   Add other attributes and their values. Will overwrite attributes in General tab if key is the same.
>
> - - Input Schema
>   - default `object`
>   - apiUrl `string` `required`
>   - email `string` `required`
>   - apiKey `string` `required`
>   - project `string` `required`
>   - projectKey `string`
>   - summary `string` `required`
>   - issueType `string` `required`
>   - parent `string`
>   - components `array`
>   - description `string`
>   - reporter `string`
>   - reporterId `string`
>   - fixVersions `array`
>   - versions `array`
>   - dueDate `string`
>   - assignee `string`
>   - assigneeId `string`
>   - priority `string`
>   - labels `array`
>   - items `array`
>   - 0 `string`
>   - queryParams `array`
>   - otherAttributes `array`
>   - Output Schema
>   - output `object`
>   - headers `object`
>   - statusCode `integer`
>   - rawResponse `object`

### Get Issue Details

Get details for an issue by providing the issue ID.

> **Collapse: Show details**
>
> * * Properties
>   * Issue ID `textField` `required`
>
>   The ID of the issue, such as "PROJ-1".
>
> * Query Parameters `keyValueList`
>
>   Define additional query parameters to send to Jira. Learn more in the Jira Cloud platform REST API documentation.
>
> - - Input Schema
>   - default `object`
>   - apiUrl `string` `required`
>   - email `string` `required`
>   - apiKey `string` `required`
>   - issueId `string` `required`
>   - queryParams `array`
>   - Output Schema
>   - output `object`
>   - headers `object`
>   - statusCode `integer`
>   - rawResponse `object`

### Update an Issue

Update an issue in JIRA.

> **Collapse: Show details**
>
> * * Properties
>   * Issue ID `textField` `required`
>
>   The ID of the issue, such as "PROJ-1".
>
> * Summary `textField`
>
>   The issue summary, such as "Fix development workflow".
>
> * Issue Type `dropDown`
>
>   The updated issue type.
>
>   * Story
>
>   * Task
>
>   * Sub-task
>
>   * Bug
>
>   * Epic
>
> * Parent Issue ID `textField`
>
>   The ID of an existing issue, such as "PROJ-10". When this value is provided, the new issue will be created as a sub-task of the parent issue.
>
> * Components `textFieldArrayView`
>
>   The ID of the component to associate with the issue, such as "10000".
>
> * Description `textField`
>
>   The issue description, such as "Please fix the following development workflow issue…"
>
> * Reporter `dropDown`
>
>   The person reporting the issue. For a dynamic value, select Use Reporter ID and enter a value in the Reporter ID field.
>
>   * Leave Blank (Default)
>
>   * Use Reporter ID
>
> * Reporter ID `textField` `required`
>
>   The ID of the reporter, such as "5b10a2844c20165700ede21g".
>
> * Fix Versions `textFieldArrayView`
>
>   The ID of the fix version to associate with the issue, such as "10001". Type an ID and press Enter to add it.
>
> * Versions `textFieldArrayView`
>
>   The ID of the version to associate with the issue, such as "10001". Type an ID and press Enter to add it.
>
> * Due Date `textField`
>
>   The due date for the issue, formatted as "2022-01-30".
>
> * Assignee `dropDown`
>
>   The person to assign the issue to. For a dynamic value, select Use Assignee ID and enter a value in the Assignee ID field.
>
>   * Leave Blank (Default)
>
>   * Use Assignee ID
>
> * Assignee ID `textField` `required`
>
>   The ID of the assignee, such as "5b10a2844c20165700ede21g".
>
> * Priority `textField`
>
>   The priority for the issue, such as "3".
>
> * Labels `textFieldArrayView`
>
>   The labels to associate with the issue. Type a label and press enter to add it.
>
> * Query Parameters `keyValueList`
>
>   Define additional query parameters to send to Jira. Learn more in the Jira Cloud platform REST API documentation.
>
> * Other Attributes `variableInputList`
>
>   Add other attributes and their values. Will overwrite attributes in General tab if key is the same.
>
> - - Input Schema
>   - default `object`
>   - apiUrl `string` `required`
>   - email `string` `required`
>   - apiKey `string` `required`
>   - issueId `string` `required`
>   - updateSummary `string`
>   - parent `string`
>   - components `array`
>   - updateIssueType `string`
>   - description `string`
>   - reporter `string`
>   - reporterId `string`
>   - fixVersions `array`
>   - versions `array`
>   - dueDate `string`
>   - assignee `string`
>   - assigneeId `string`
>   - priority `string`
>   - labels `array`
>   - items `array`
>   - 0 `string`
>   - queryParams `array`
>   - otherAttributes `array`
>   - Output Schema
>   - output `object`
>   - headers `object`
>   - statusCode `integer`

### Delete an Issue

Delete an issue in the project.

> **Collapse: Show details**
>
> * * Properties
>   * Issue ID `textField` `required`
>
>   The ID of the issue, such as "PROJ-1".
>
> * Query Parameters `keyValueList`
>
>   Define additional query parameters to send to Jira. Learn more in the Jira Cloud platform REST API documentation.
>
> - - Input Schema
>   - default `object`
>   - apiUrl `string` `required`
>   - email `string` `required`
>   - apiKey `string` `required`
>   - issueId `string` `required`
>   - queryParams `array`
>   - Output Schema
>   - output `object`
>   - headers `object`
>   - statusCode `integer`

### Assign an Issue

Assign an issue to an account.

> **Collapse: Show details**
>
> * * Properties
>   * Assignee `dropDown`
>
>   The person to assign the issue to. For a dynamic value, select Use Assignee ID and enter a value in the Assignee ID field.
>
>   * Leave Blank (Default)
>
>   * Use Assignee ID
>
> * Assignee ID `textField` `required`
>
>   The ID of the assignee, such as "5b10a2844c20165700ede21g".
>
> * Issue ID `textField` `required`
>
>   The ID of the issue, such as "PROJ-1".
>
> - - Input Schema
>   - default `object`
>   - apiUrl `string` `required`
>   - email `string` `required`
>   - apiKey `string` `required`
>   - assignee `string`
>   - assigneeId `string`
>   - issueId `string` `required`
>   - Output Schema
>   - output `object`
>   - headers `object`
>   - statusCode `integer`

### Search for Issues Using JQL

Search for issues using Jira Query Language.

> **Collapse: Show details**
>
> * * Properties
>   * JQL Query `textField`
>
>   The JQL query used to search for issues, such as "project=SysAdmin AND assignee=jsmith". Learn more in documentation for the Jira Query Language.
>
> * Starting Result Number `textField`
>
>   The index number of the first item to return in the results. For example, "101" will return the maximum number of results starting with result number 101. Use this to get pages of results for queries that return more than the maximum number of results.
>
> * Maximum Number of Results `textField`
>
>   The maximum number of results to return from the query. Use with Starting Result Number to get pages of results for queries that return more than the maximum number of results.
>
> * Fields `textFieldArrayView`
>
>   The fields to get for each issue returned in the results, such as "assignee" or "comment". Type a field name and press enter to add it.
>
> * Identify Fields with Keys `toggleSwitch`
>
>   Enable this when the "Fields" list uses keys, rather than IDs, to identify fields.
>
> * Query Validation `dropDown`
>
>   The method to use to validate the JQL query.
>
>   * Strict (Default)
>
>   * Warn
>
>   * None
>
> * Expanded Information `textFieldArrayView`
>
>   Additional information to get for the issues returned in the results, such as "names", "schema", or "changelog". Learn more in "Search for issues with JQL (POST)" in the Jira Cloud platform REST API documentation.
>
> * Properties `textFieldArrayView`
>
>   The app or entity properties to get for each issue returned in the results. Type a property name and press enter to add it, to a maximum of five properties.
>
> - - Input Schema
>   - default `object`
>   - apiUrl `string` `required`
>   - email `string` `required`
>   - apiKey `string` `required`
>   - jql `string` `required`
>   - startAt `string`
>   - maxResults `string`
>   - fields `array`
>   - validateQuery `string`
>   - expand `array`
>   - searchProperties `array` `maxItems: 5`
>   - fieldsByKeys `boolean`
>   - Output Schema
>   - output `object`
>   - headers `object`
>   - statusCode `integer`
>   - rawResponse `object`

### Make Custom API Call

Define and invoke custom call to the Atlassian Jira REST API.

> **Collapse: Show details**
>
> * * Properties
>   * Endpoint `textField` `required`
>
>   The Jira API endpoint, such as /rest/api/3/search.
>
> * HTTP Method `dropDown` `required`
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
> * Query Parameters `keyValueList`
>
>   Define additional query parameters to send to Jira. Learn more in the Jira Cloud platform REST API documentation.
>
> * Additional Headers `keyValueList`
>
>   Additional headers for the request, connector automatically adds 'Authorization' and 'Content-Type' headers.
>
> * Body `codeEditor`
>
>   The body of the API call.
>
> - - Input Schema
>   - default `object`
>   - apiUrl `string` `required`
>   - email `string` `required`
>   - apiKey `string` `required`
>   - endpoint `string` `required`
>   - method `string` `required`
>   - customQueryParams `array`
>   - headers `array`
>   - bodyData `object`
>   - Output Schema
>   - output `object`
>   - headers `object`
>   - statusCode `integer`
>   - rawResponse `object`