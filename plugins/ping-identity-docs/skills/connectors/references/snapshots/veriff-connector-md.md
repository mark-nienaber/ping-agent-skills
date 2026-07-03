---
title: Veriff Connector
description: The Veriff connector lets you verify users with Veriff's artificial intelligence (AI)-powered identity solution for identity fraud prevention in your PingOne DaVinci flow.
component: connectors
page_id: connectors::veriff_connector
canonical_url: https://docs.pingidentity.com/connectors/veriff_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 19, 2024
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  setting-up-veriff: Setting up Veriff
  configuring-the-veriff-connector: Configuring the Veriff connector
  connector-configuration: Connector configuration
  base-url: Base URL
  api-key: API Key
  shared-secret-key: Shared Secret Key
  using-the-connector-in-a-flow: Using the connector in a flow
  verify-a-users-age-by-redirecting-to-veriff: Verify a user's age by redirecting to Veriff
  creating-a-custom-api-call: Creating a custom API call
  capabilities: Capabilities
  createSession: Create Session
  submitPhotos: Upload Images
  submitSession: Submit Session for Review
  webhook: Wait for Session Review Result
  redirectToVeriff: Redirect to Veriff for Verification
  makeCustomApiCall: Make Custom API Call
---

# Veriff Connector

The Veriff connector lets you verify users with Veriff's artificial intelligence (AI)-powered identity solution for identity fraud prevention in your PingOne DaVinci flow.

You can use the Veriff connector to:

* Verify a user's age with user-submitted identity documents

* Redirect to Veriff for age verification

* Make a custom API call

## Setup

### Resources

Learn more in the following:

* Veriff documentation:

  * [Veriff documentation](https://developers.veriff.com/#introduction)

  * [Getting started with Veriff](https://devdocs.veriff.com/docs/getting-started)

* DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* A Veriff license

* Your Veriff credentials

### Setting up Veriff

Follow the instructions in [Getting started with Veriff](https://devdocs.veriff.com/docs/getting-started).

### Configuring the Veriff connector

Add the connector in DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

##### Base URL

The API URL to target, for example, `https://stationapi.veriff.com/`

##### API Key

Your Veriff API key, for example, `123-456-789`

##### Shared Secret Key

Your Veriff shared secret key, for example, `123-456-789`

## Using the connector in a flow

### Verify a user's age by redirecting to Veriff

The **Redirect to Veriff for Verification** capability provides an alternative to age verification with a custom DaVinci user experience flow, instead redirecting the user to a complete age verification experience hosted by Veriff.

No special configuration is needed. Add the capability and populate its properties according to the help text.

### Creating a custom API call

If you want to do something that isn't supported by one of the provided capabilities, you can use the **Make a Custom API Call** capability to define your own action.

This capability uses the credentials from your connector to make an API call with the HTTP method, headers, query parameters, and body you specify.

## Capabilities

### Create Session

Create a verification session with the user's name and personal details.

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - First Name textField required
>
>   The user's first name.
>
> - Last Name textField required
>
>   The user's last name.
>
> - Gender textField required
>
>   The user's gender, such as 'male' or 'female'.
>
> - Date of Birth textField required
>
>   The user's date of Birth, formatted as YYYY-MM-DD, such as '1979-01-30'.
>
> - National Identification Number textField required
>
>   The user's national identification number, such as 'AB123456C'.
>
> - Vendor Data textField required
>
>   Your organization's unique identifier for the user. This value is returned by Veriff in the Receive Webhook Response capability, which allows you to identify users that submit multiple different photos or documents using the same user identifier.
>
> * output object
>
>   * status string
>
>   * verification object
>
>     * id string
>
>     * url string
>
>     * vendorData string
>
>     * host string
>
>     * status string
>
>     * sessionToken string
>
>   * sessionId string

### Upload Images

Submit identity documents and selfie photos.

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - Session ID textField required
>
>   The user's Veriff session ID. Use the Create Session capability to get a session ID.
>
> - Document Front textArea required
>
>   The Base64-encoded image of the front of the identity document.
>
> - Document Back textArea required
>
>   The Base64-encoded image of the back of the identity document.
>
> - Selfie Image textArea required
>
>   The Base64-encoded image of the user's selfie photo.
>
> * output object
>
>   * documentFront object
>
>     * status string
>
>     * image object
>
>       * context string
>
>       * id string
>
>       * name string
>
>       * timestamp string
>
>       * size integer
>
>       * mimetype string
>
>       * url string
>
>   * documentBack object
>
>     * status string
>
>     * image object
>
>       * context string
>
>       * id string
>
>       * name string
>
>       * timestamp string
>
>       * size integer
>
>       * mimetype string
>
>       * url string
>
>   * face object
>
>     * status string
>
>     * image object
>
>       * context string
>
>       * id string
>
>       * name string
>
>       * timestamp string
>
>       * size integer
>
>       * mimetype string
>
>       * url string

### Submit Session for Review

Submit the session for review after uploading images.

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - Session ID textField required
>
>   The user's Veriff session ID. Use the Create Session capability to get a session ID.
>
> * output object
>
>   * response object
>
>     * status string
>
>     * verification object
>
>       * id string
>
>       * url string
>
>       * vendorData string
>
>       * host string
>
>       * status string
>
>       * sessionToken string
>
>   * challengeId string

### Wait for Session Review Result

Wait for Veriff to send the result of the session review to the DaVinci webhook URL.

> **Collapse: Show details**
>
> * Output Schema
>
> - output object
>
>   * response object
>
>     * status string
>
>     * verification object
>
>       * id string
>
>       * code number
>
>       * vendorData string
>
>       * person object
>
>       * status string
>
>   * vendorData string
>
>   * rawResponse object

### Redirect to Veriff for Verification

Redirect the browser to a complete user verification experience provided by Veriff.

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - First Name textField required
>
>   The user's first name.
>
> - Last Name textField required
>
>   The user's last name.
>
> - Vendor Data textField required
>
>   Your organization's unique identifier for the user. This value is returned by Veriff in the Receive Webhook Response capability, which allows you to identify users that submit multiple different photos or documents using the same user identifier.
>
> * output object
>
>   * response object
>
>     * status string
>
>     * verification object
>
>   * sessionId object
>
>   * redirectUrl string
>
>   * challenge string

### Make Custom API Call

Define and use your own call to the Veriff API.

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - Endpoint textField required
>
>   The Veriff API endpoint, such as "sessions/:sessionID/media".
>
> - Method dropDown required
>
>   The method to use for the call.
>
>   * GET (Default)
>
>   * POST
>
>   * DELETE
>
>   * PATCH
>
> - Query parameters and values to include in the call keyValueList
>
>   Add query parameters and provide their values.
>
> - Headers keyValueList
>
>   HTTP headers and values to use in the call.
>
> - Body textArea
>
>   The raw JSON body
>
> * output object
>
>   * rawResponse object
>
>   * status number
>
>   * headers object