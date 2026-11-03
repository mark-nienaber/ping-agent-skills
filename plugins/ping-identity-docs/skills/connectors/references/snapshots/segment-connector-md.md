---
title: Segment Connector
description: "Configure the Segment connector in PingOne DaVinci to collect, clean, and control customer data with Segment's HTTP Tracking API"
component: connectors
page_id: connectors::segment_connector
canonical_url: https://docs.pingidentity.com/connectors/segment_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 24, 2026
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  configuring-the-segment-connector: Configuring the Segment connector
  connector-configuration: Connector configuration
  using-the-connector-in-a-flow: Using the connector in a flow
  collecting-user-data-in-a-flow: Collecting user data in a flow
  capabilities: Capabilities
  identifyUser: Identify User
  groupUserIsIn: Identify User's Group
  trackUser: Track User
  pageUserIsOn: Page User Is On
  screenUserIsOn: Screen User Is On
  userAlias: User Alias
  makeCustomApiCall: Make Custom API Call
---

# Segment Connector

The Segment connector lets you use [Segment](https://www.twilio.com/en-us/segment) software and APIs to collect, clean, and control your customer data in your PingOne DaVinci flow.

The connector sends identify, group, track, page, screen, and alias calls to Segment's HTTP Tracking API so that you can record what users do as they journey through your flow.

## Setup

### Resources

You can find more information and setup help in the following:

* Segment documentation:

  * [Segment HTTP Tracking API documentation](https://www.twilio.com/docs/segment/connections/sources/catalog/libraries/server/http-api)

  * [Find your Segment write key](https://www.twilio.com/docs/segment/getting-started/02-simple-install)

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* A Segment account and workspace.

* Your Segment write key, base 64 encoded.

* A source in Segment to collect the data sent by your flow.

### Configuring the Segment connector

Add the connector in PingOne DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

| Setting                   | Description                                                                                                        |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Write Key                 | Your base 64 encoded Segment write key. Insert only the encoded write key into the field.                          |
| HTTP Tracking API Version | The version of Segment's HTTP Tracking API. The default is v1. Only change this if the API version is out of date. |

## Using the connector in a flow

### Collecting user data in a flow

You can use the connector to create or update users, track the actions they take, and record the pages and screens they view as they journey through a flow.

At a high level:

1. The **Identify User** capability ties a user to their actions and records traits about them, such as their email or name, using the user ID you define.

2. The **Track User** capability records the actions the user performs, such as a button click or an item added to a cart, using the event name you specify.

3. The **Page User Is On** and **Screen User Is On** capabilities record the webpages and mobile screens a user views.

4. The **Identify User's Group** capability associates the user with a group, such as a company or team, using the group ID you specify.

5. The **User Alias** capability merges two user identities so that two sets of user data are connected as one.

|   |                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The connector doesn't generate any output on its own. To see the HTTP response object sent by Segment, use the output variables of a capability, such as the status code, in a subsequent node. |

Test the flow by clicking **Save**, **Deploy**, and **Try Flow**.

## Capabilities

### Identify User

Identify lets you tie a user to their actions and record traits about them. It includes a unique User ID and any optional traits you know about them.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField required
>
>   Unique identifier for the user
>
> - Traits keyValueList required
>
>   Any desired descriptive attribute(s)
>
> * default object
>
>   * properties object
>
>     * userId string/number
>
>       Unique identifier for the user
>
>     * genericTraits array
>
>       Any desired general attribute
>
> Input Example
>
> ```json
> {
>   "properties": {
>     "userId": "12345",
>     "genericTraits": {
>       "email": "user_name123@example.com",
>       "phone": "720-101-1010",
>       "name": "John Smith",
>       "gender": "male",
>       "age": "25",
>       "title": "VP of Engineering",
>       "birthday": "1/10/95",
>       "address": "111 Yellow Brick Rd.",
>       "industry": "Technology",
>       "music": "rock"
>     }
>   }
> }
> ```
>
> * output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * headers object

### Identify User's Group

Group lets you associate an identified user with a group. A group could be a company, organization, account, project, or team. It also lets you record custom traits about the group, like industry or number of employees.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField required
>
>   Unique identifier for the user
>
> - Group ID textField required
>
>   Unique identifier which you recognize a group by
>
> - Traits keyValueList required
>
>   Any desired descriptive attribute(s)
>
> * default object
>
>   * properties object
>
>     * userId string/number
>
>       Unique identifier for the user
>
>     * groupId string/number
>
>       Unique group identifier for a user
>
>     * genericTraits array
>
>       Any desired general attribute
>
> Input Example
>
> ```json
> {
>   "properties": {
>     "userId": "12345",
>     "groupId": "0001",
>     "genericTraits": {
>       "email": "user_name@pingidentity.com",
>       "team": "DaVinci",
>       "company": "Ping Identity",
>       "industry": "Technology"
>     }
>   }
> }
> ```
>
> * output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * headers object

### Track User

Identify lets you record the actions your users perform. Every action triggers an "event", which can also have associated properties.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField required
>
>   Unique identifier for the user
>
> - Event textField required
>
>   Name of the action that the user has performed
>
> - Properties keyValueList required
>
>   Any desired descriptive attribute(s)
>
> * default object
>
>   * properties object
>
>     * userId string/number
>
>       Unique identifier for the user
>
>     * userEvent string
>
>       Name of the action that the user has performed
>
>     * genericProperties array
>
>       Any desired general attribute
>
> Input Example
>
> ```json
> {
>   "properties": {
>     "userId": "12345",
>     "genericProperties": {
>       "item": "Chocolate",
>       "revenue": 1.99,
>       "location": "Denver, CO"
>     }
>   }
> }
> ```
>
> * output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * headers object

### Page User Is On

Lets you record page views on your website, along with optional extra information about the page being viewed.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField required
>
>   Unique identifier for the user
>
> - Page Name textField required
>
>   Name of the page - Reserved for future use
>
> - Properties keyValueList required
>
>   Any desired descriptive attribute(s)
>
> * default object
>
>   * properties object
>
>     * userId string/number
>
>       Unique identifier for the user
>
>     * pageName string
>
>       Name of the page - Reserved for future use
>
>     * genericProperties array
>
>       Any desired general attribute
>
> Input Example
>
> ```json
> {
>   "properties": {
>     "userId": "12345",
>     "name": "Home Page",
>     "properties": {
>       "title": "Welcome | What We Do",
>       "url": "https://www.pingidentity.com/en.html",
>       "company": "Ping Identity"
>     }
>   }
> }
> ```
>
> * output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * headers object

### Screen User Is On

Lets you record whenever a user sees a screen of your mobile app. You'll want to send the screen message whenever a user requests a page of your app.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField required
>
>   Unique identifier for the user
>
> - Screen Name textField required
>
>   Name of the screen from a mobile device - Reserved for future use
>
> - Properties keyValueList required
>
>   Any desired descriptive attribute(s)
>
> * default object
>
>   * properties object
>
>     * userId string/number
>
>       Unique identifier for the user
>
>     * screenName string
>
>       Name of the screen from a mobile device - Reserved for future use
>
>     * genericProperties array
>
>       Any desired general attribute
>
> Input Example
>
> ```json
> {
>   "properties": {
>     "userId": "12345",
>     "name": "Home Screen",
>     "properties": {
>       "title": "Welcome | What We Do",
>       "company": "Ping Identity"
>     }
>   }
> }
> ```
>
> * output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * headers object

### User Alias

The alias method is used to merge two user identities, effectively connecting two sets of user data as one. This is an advanced method, but it is required to manage user identities successfully in some of our destinations.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Previous User ID textField required
>
>   The existing ID you've referred to this user by
>
> - User ID textField required
>
>   Unique identifier for the user
>
> * default object
>
>   * properties object
>
>     * userId string/number
>
>       Unique identifier for the user
>
>     * previousId string/number
>
>       The existing ID you've referred to this user by
>
> Input Example
>
> ```json
> {
>   "properties": {
>     "previousId": "00001",
>     "userId": "00002"
>   }
> }
> ```
>
> * output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * headers object

### Make Custom API Call

Define a custom API call to Segment's HTTP Tracking API.

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
>   Use an HTTP Tracking API endpoint, such as "identify, track, page, screen, group, or alias".
>
> - User ID textField required
>
>   Unique identifier for the user
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
> - Traits / Properties keyValueList
>
>   Key-value pairs that are used to define any desired characteristics about a certain endpoint call.
>
> - Headers keyValueList
>
>   Add HTTP headers and provide their values.
>
> - Body codeEditor
>
>   The raw custom JSON body
>
> * default object
>
>   * properties object
>
>     * endpoint string required
>
>       Endpoint
>
>     * userId string/number
>
>       Unique identifier for the user
>
>     * method string required
>
>       Method
>
>     * queryParameters array
>
>       Parameters
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