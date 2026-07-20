---
title: HTTP Connector
description: Configure the PingOne DaVinci HTTP connector to show custom HTML pages, make REST API calls, and build custom user interfaces in your flow
component: connectors
page_id: connectors::http_connector
canonical_url: https://docs.pingidentity.com/connectors/http_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  setup: Setup
  configuring-the-http-connector: Configuring the HTTP connector
  connector-configuration: Connector configuration
  recaptcha-v2-site-key: reCAPTCHA v2 Site Key
  recaptcha-v2-secret-key: reCAPTCHA v2 Secret Key
  select-an-openid-token-management-connection-for-signed-http-responses: Select an OpenID token management connection for signed HTTP responses
  using-the-connector-in-a-flow: Using the connector in a flow
  showing-simple-messages: Showing simple messages
  building-a-custom-page: Building a custom page
  starting-with-a-template-from-the-ui-studio: Starting with a template from the UI Studio
  adding-your-html-css-and-scripts: Adding your HTML, CSS, and scripts
  adding-custom-html: Adding custom HTML
  adding-custom-css: Adding custom CSS
  example-triggering-a-script-with-a-button: "Example: Triggering a script with a button"
  managing-the-widgets-states-and-functions: Managing the widget's states and functions
  adding-form-validation-rules: Adding form validation rules
  adding-output-fields: Adding output fields
  making-a-rest-api-call: Making a REST API call
  getting-an-api-response: Getting an API response
  capabilities: Capabilities
  createSuccessResponse: Send Success JSON Response
  createErrorResponse: Send Error JSON Response
  createUnwrappedResponse: Send Custom JSON Response
  customHtmlMessage: Custom HTML Message
  recaptchaVerification: reCAPTCHA v2 Verification
  makeRestApiCall: Make REST API Call
  customHTMLTemplate: Custom HTML Template
  createQr: Create QR Code for URL
  continuePolling: Continue Polling
  simulateLatency: Simulate Latency
---

# HTTP Connector

This powerful and versatile connector lets you show custom HTML pages, make REST application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* calls, and more in your PingOne DaVinci orchestration flow.

Use it to create a custom HTML message, show flow progress, or send custom responses in an API-triggered flow. You can use the messages as quick placeholders to help you sketch out a new flow. If you want to craft a memorable user experience, use the **Custom HTML Template** capability to create complete HTML pages with your own structure, style, and scripts.

Because this connector allows you to quickly add API calls and user interfaces, it can be a valuable sketching tool in your flow design process or to prove the design for a connector your organization might build.

## Setup

### Configuring the HTTP connector

In PingOne DaVinci, add an **HTTP** connection. Learn more in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html).

#### Connector configuration

##### reCAPTCHA v2 Site Key

The site key provided in your reCAPTCHA dashboard. Learn more in [Creating reCAPTCHA keys](https://cloud.google.com/recaptcha-enterprise/docs/create-key) in the Google documentation.

This field is only needed for the connector's reCAPTCHA capability.

##### reCAPTCHA v2 Secret Key

The secret key provided in your reCAPTCHA dashboard. Learn more in [Creating reCAPTCHA keys](https://cloud.google.com/recaptcha-enterprise/docs/create-key) in the Google documentation.

This field is only needed for the connector's reCAPTCHA capability.

##### Select an OpenID token management connection for signed HTTP responses

To add a selection to this list, go to **Connections** and add a **Token Management** connector.

This selection is only needed if you want to sign HTTP responses.

## Using the connector in a flow

### Showing simple messages

If you want to show information to the user, the **Custom HTML Message** capability gives you a premade page with a title, message, and button. You can't change the structure, but you can add an icon or style the message with your CSS. This is useful for error messages and confirmations, such as confirming a user's registration details.

1. In your flow, add the **HTTP** connector and select the **Custom HTML Message** capability.

2. Add a **Message Title**, such as "Welcome."

3. Add a **Message**. You can include values from elsewhere in your flow by clicking **{}**, then selecting the attribute that holds the value you want.

   For this example, insert the username that the user entered into the registration form created by the PingOne Forms connector:

   ![A screen capture that shows the user inserting a variable in the Message field.](_images/connector-images/dvc-http-message-field-variable.gif)

4. If you don't want the flow to end here, turn on **Show Continue Button** and customize the button **Display Name**.

### Building a custom page

The **Custom HTML Template** capability lets you include an HTML page in your flow. The structure, style, and behavior is entirely up to you.

|   |                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | For creating forms, the PingOne Forms connector provides a drag-and-drop experience builder. Learn more in [Form Connector](form_connector.html) and [PingOne Forms](https://docs.pingidentity.com/pingone/user_experience/p1_forms.html). |

#### Starting with a template from the UI Studio

To start your custom HTML page, you can autofill its settings from any template you created in the [UI Studio](https://docs.pingidentity.com/davinci/ui_studio/davinci_ui_studio.html). This makes it easy to create several pages from the same template. Keep the following in mind:

* If you modify your HTML page in your flow, it won't affect your original template in the UI Studio.

* When you select a UI template from within an HTTP node, it overwrites any work you've done in that node. The UI templates are best used for newly-created HTTP nodes.

![A screen capture showing the user selecting a UI template.](_images/connector-images/dvc-http-ui-template-selection.gif)

#### Adding your HTML, CSS, and scripts

Your custom page defines the look and behavior of a widget that's powered by React.

##### Adding custom HTML

The **HTML Template** field lets you read and modify the HTML for your page.

|   |                                                                                                                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * Click **Switch View** to display the HTML formatted with syntax highlighting.

* Click the **Maximize**([icon: expand, set=fas]) icon to give yourself more room to work.

* To access a variety of useful tools, right-click the field when you're in syntax highlighting mode (dark background). |

|   |                                                                                                                                                                                                                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For security reasons, the **HTML** field only allows certain HTML elements. You can find the elements on the allow list in the [DOMPurify allow list](https://github.com/cure53/DOMPurify/blob/2.3.6/src/tags.js).Note that custom HTML elements from the `svgDisallowed` and `mathMlDisallowed` lists are not allowed.These restrictions apply to all custom HTML fields in PingOne DaVinci. |

If you want your HTML to include values from elsewhere in your flow, switch back to the initial view (white background), click **{}**, and then select the variable that holds the value you want.

![A screen capture that shows the user switching the HTML Template field to normal view, then inserting an input variable.](_images/connector-images/dvc-http-html-template-field-normal-view.gif)

|   |                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The **HTML Template** field doesn't support inline events or script tags. Refer to the following script [Adding a custom script](#docs-internal-guid-83834755-7fff-3512-245e-776c252d77ed). |

##### Adding custom CSS

The **CSS** field lets you add styles to the HTML page. The contents of the CSS field is appended to the body of the widget. You can use any standard CSS, including @import.

![A screen capture of the CSS field with some sample CSS.](_images/connector-images/dvc-http-css-field-sample.jpg)

* []()Adding a custom script

  The **Script** field allows you to customize the behavior of your page. You can use any standard JavaScript in the **Script** field.

  |   |                                                                                                                                                                                                                                                  |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | The **HTML Template** field doesn't support inline events or script tags. Instead of triggering events with the HTML, such as with `<button onclick="myFunction()">Click me</button>`, use the **Script** field to listen for the event instead. |

##### Example: Triggering a script with a button

In the **HTML Template** field, add a button.

```
<h2>JavaScript addEventListener()</h2>

<p>This example uses the addEventListener() method to attach a click event to a button.</p>

<button id="myButton">Try it</button>

<p id="demo"></p>
```

In the **Script** field, add an event listener and associate it with the button ID.

```
//Listen for a click event on 'myButton', then run myFunction
document.getElementById("myButton").addEventListener("click", myFunction);

function myFunction () {
  //Enter your code here, for example:
  document.getElementById("demo").innerHTML = Date();
}
```

##### Managing the widget's states and functions

By default, scripts can't access the state and functions of the widget that contains the HTML page. To access them, you can use event-based communication between the script and the widget by dispatching JavaScript custom events.

In the **Script** field, trigger a custom event using the following structure.

```
const event = new window.CustomEvent('skevent', {
    detail: {
        type: EVENT_TYPE,
        payload: PAYLOAD
    }
})

window.dispatchEvent(event);
```

The widget has an event listener for `skevent`, so the widget will catch and process this event. The detail object is designed to match syntax of a standard [Redux](https://redux.js.org/tutorials/fundamentals/part-3-state-actions-reducers) action object. You can use the following event types:

* `SET_STATE` lets you set a value in the state of the widget:

  ```
  const event = new window.CustomEvent('skevent', {
      detail: {
          type: 'SET_STATE',
          payload: {
              name: 'email',
              value: 'testuser@example.com'
          }
      }
  });

  window.dispatchEvent(event);
  ```

* `GET_STATE` lets you get a value from the current state of the widget:

  ```
  const event = new window.CustomEvent('skevent', {
      detail: {
          type: 'GET_STATE',
          payload: 'email'
      }
  });

  window.dispatchEvent(event);
  ```

  The `GET_STATE` event dispatches an event called `skeventresponse` with the `STATE` event type. To complete the process, add an event listener to listen for the `skeventresponse` event:

  ```
  window.addEventListener('skeventresponse', e => {
      switch(e.detail.type) {
          case 'STATE':
              console.log(e.detail.payload);
              break;
      }
  });
  ```

  The event listener produces the result from the `GET_STATE` event:

  ```json
  {
    "name": "email",
    "value": "testuser@example.com"
  }
  ```

##### Adding form validation rules

You can add one or more form validation rules. Enter the name of the field in the **Property Name** field, then select a validation rule in the **Rule Name** list. The options for validation rules are:

* **Required**

* **Email**

* **Length**

* **Format**

* **Equality**

For each rule, validation is checked, and a validation message is displayed based on the results.

##### Adding output fields

You can add one or more output fields under **Output Fields List**. These fields outline the different outputs of the HTML form for use in Direct or SDK Flow Executions.

To configure an output field:

1. Enter a unique name for the property in the **Property Name** field. This name is assigned to the output in subsequent nodes when selecting the field as a variable.

2. Select a **Control Type** from the list and configure it based on the following table:

   | **Control Type**                 | Description                                                                              | Configuration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | -------------------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Text Field**                   | A field for users to input relevant information.                                         | This control type is supported by both Direct and SDK Flow Executions with the following configuration:- The **Display Name** provides text to help users understand the purpose of the text field.

   - The **Value** represents a default text value that will be populated in the text field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | **Secure Text Field / Password** | A field to allow users to authenticate with a password.                                  | This control type is supported by both Direct and SDK Flow Executions with the following configuration:- The **Control Type** must be **Text Field**.

   - The **Display Name** provides text to help users understand the purpose of the password field.

   - **Secure** must be toggled on to make the text field a password field.

   - The **Value** represents a default, pre-populated password. We recommend leaving this field empty.                                                                                                                                                                                                                                                                                                                                                               |
   | **Dropdown**                     | A dropdown list for uses such as providing country codes for phone numbers.              | This component is supported only by SDK Flow Executions with the following configuration:- The **Display Name** provides text to help users understand the purpose of the dropdown.

   - You can enter label-value pairs to populate the dropdown options in two ways:

     * Toggle on **Enter label-value pairs as CSV** and enter pairs separated by commas:

       ![The Enter label-value pairs as CSV field populated with examples of label-value pairs, separated by commas.](_images/connector-images/dvc-http-connector-csv.png)

     * In **Enter label-value pairs**, click the **[icon: plus, set=fa]**icon and enter the **Label** and **Value**.

       ![The Enter label-value pairs field with the label and value fields populated.](_images/connector-images/dvc-http-label-value-pairs.png) |
   | **Radio Button List**            | A radio button component to provide a user with a small set of options.                  | This component is supported only by SDK Flow Executions with the following configuration:- The **Display Name** provides text to help users understand the purpose of the radio button list.

   - You can enter label-value pairs to populate the dropdown options in two ways:

     * Toggle on **Enter label-value pairs as CSV** and enter pairs separated by commas.

     * In **Enter label-value pairs**, click the **[icon: plus, set=fa]**icon and enter the **Label** and **Value**.                                                                                                                                                                                                                                                                                                               |
   | **Label**                        | A label for the form that can be used as a form heading, such as "Welcome" or "Sign On." | This component is supported only by SDK Flow Executions with the following configuration:- The **Value** is required to provide the content of the label in the user-facing form. For example:

     ![The value field with the label content reading Forgot Password Form.](_images/connector-images/dvc-http-label-field.png)                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

### Making a REST API call

![A screen capture of the complete REST API flow.](_images/connector-images/dvc-http-rest-api-flow.jpg)

You can use the HTTP connector to make a call to any REST API. You can choose the call method (such as GET or POST) and configure query parameters, headers, body, and the responses. This is a flexible way to integrate your flow with external systems.

|   |                                                                                                                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Best practice is to use secret variables stored in **DaVinci > Variables**. Learn more in [Variables](https://docs.pingidentity.com/davinci/variables/davinci_variables.html) and [Creating Variables](https://docs.pingidentity.com/davinci/davinci_best_practices/davinci_best_practices_variables.html). |

The following example uses the <http://deckofcardsapi.com/>Deck of Cards API] call to draw five cards, then make the cards available in the flow.

The Deck of Cards API documentation specifies the following URL to draw five cards:

`http://deckofcardsapi.com/api/deck/new/draw/?count=5`

### Getting an API response

1. Making an API call

   1. In your flow, add the **HTTP** connector and select the **Make REST API Call** capability.

   2. In the **URL**, enter the API URL. In this example, this is `http://deckofcardsapi.com/api/deck/new/draw/`.

   3. From the **HTTP Method** list, select the action to take, such as **GET**.

   4. In the **Query Parameters** section, add each query parameter and its value. You can include values from elsewhere in your flow by clicking **{}**, then selecting the variable that holds the value you want. For this example, get five cards every time:

      ![A screen capture that shows the Query Parameters field with a key-value pair added.](_images/connector-images/dvc-http-query-parameters.jpg)

   5. In the **MTLS Support** list, select a key configured in PingOne to select the client certificate used in outbound mTLS connections.

      |   |                                                                                                                           |
      | - | ------------------------------------------------------------------------------------------------------------------------- |
      |   | Keys are configured in PingOne. To create a key in the PingOne admin console, click the **Certificates & Keypairs** link. |

   6. (Optional) In the **Timeout (ms)** field, enter a timeout for the API call.

      |   |                                                                                                                                                              |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | To not have a timeout, leave the field blank. You can select any timeout value, but if the API call needs a response, there is a hard timeout at 30 seconds. |

   7. Click **Apply** to save your changes.

      |   |                                                                                                                                                                                                                                                   |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | In your own flow, you can use the **Headers** and **Body Parameters** sections the same way to add any other parameters you need in your API call, and use the **Body** list, select the content type of the body data you're sending to the API. |

2. Working with the API response

   1. Following your **Make REST API Call** node, add an **HTTP** connector and select the **Custom HTML Message** capability.

   2. In the **Message** field, click **{}** and select the **rawResponse** variable from your **Make REST API Call** node by clicking **(+)**.

      ![A screen capture that shows the user inserting the rawResponse variable into the Message field.](_images/connector-images/dvc-http-rawresponse-variable.gif)

   3. Test the flow by clicking **Save**, **Deploy**, and **Try Flow**.

      The resulting message shows the card information, including the card value, suit, and an image. Copy this block of text, starting with `{"headers"…​`. You'll use it in the next step.

      ![A screen capture that shows the HTML message with the raw JSON response in text form.](_images/connector-images/dvc-http-json-response.jpg)

3. Separate the raw response into usable values by defining a response schema:

   1. In a browser, open the [Online JSON Schema Validator and Generator](https://extendsclass.com/json-schema-validator.html) tool. You'll use it to generate the JavaScript Object Notation (JSON) *(tooltip: \<div class="paragraph">
      \<p>An open, lightweight data-interchange format that uses human-readable text to store and transmit data.\</p>
      \</div>)* schema.

   2. Paste the JSON response you copied into the **JSON** field. Click **Generate Schema From JSON**. Copy the output from the **JSON SCHEMA** field.

      ![A screen capture that shows the JSON Schema Validator and Generator tool after generating the JSON schema.](_images/connector-images/dvc-flow-conductor-json-schema-validator.jpg)

   3. In your **Make REST API Call** node, paste the JSON schema into the **Success Response Schema** field.

      ![A screen capture that shows the Success Response Schema with the JSON schema added.](_images/connector-images/dvc-http-success-response-schema-json.jpg)

   4. Apply your changes, then go back to your **Custom HTML Message** node.

   5. In your **Custom HTML Message** node, remove the **rawOutput** variable that you included in the **Message** field. Because you added a response schema, you can select specific parts of the JSON response to include in our message. Click **{}** and select the `cards` variable:

      ![A screen capture that shows the user inserting the cards variable in the Message field.](_images/connector-images/dvc-http-cards-variable.jpg)

## Capabilities

### Send Success JSON Response

Send a successful response.

> **Collapse: Show details**
>
> * Properties
>
> - - returnRequestParameters toggleSwitch
>   - Additional Fields in the Response selectNameValueListColumn
>
>   Use this section to add additional fields to the response
>
> - * additionalFieldsName textField
>   * Validate the additional properties toggleSwitch
>
>   The flow will fail if the validation is failed.
>
> - Signed Response toggleSwitch
>
>   Sign the response as JWT using your company's private keys. Signatures can be validated using JWKS public keys in the Company section.
>
> - Validity textField
>
>   Expiry time in milliseconds. Default is 86400000 (1 day).

### Send Error JSON Response

Send an error response.

> **Collapse: Show details**
>
> * Properties
>
> - - returnRequestParameters toggleSwitch
>   - Additional Fields in the Response selectNameValueListColumn
>
>   Use this section to add additional fields to the response
>
> - * additionalFieldsName textField
>   * Signed Response toggleSwitch
>
>   Sign the response as JWT using your company's private keys. Signatures can be validated using JWKS public keys in the Company section.
>
> - Validity textField
>
>   Expiry time in milliseconds. Default is 86400000 (1 day).

### Send Custom JSON Response

Send a custom response.

> **Collapse: Show details**
>
> * Properties
>
> - HTTP Body (JSON) textArea
>
>   This property needs to be a properly formatted JSON value. It can contain DaVinci parameters, which will be replaced at runtime. If you are using DaVinci parameters that are of type 'string', you will need to put string quotes around it.
>
> - * httpStatusCode textField
>   * httpHeaders textArea

### Custom HTML Message

Creates a customizable HTML message.

> **Collapse: Show details**
>
> * Properties
>
> - messageTitle textField
>
>   Default: `Information`
>
> - * message textArea
>   * Message Icon URL textField
>   * Message Icon Height (in pixels) textField
>   * showFooter toggleSwitch
>   * Display Name button
>   * challenge textField
>   * Enable Polling? toggleSwitch
>   * pollInterval textField
>
>   Default: `2000`
>
> - pollRetries textField
>
>   Default: `60`
>
> - * pollChallengeStatus toggleSwitch
>   * showContinueButton toggleSwitch

### reCAPTCHA v2 Verification

Verify that you are not a robot and proceed.

> **Collapse: Show details**
>
> * Properties
>
> - title textField
>
>   Form title.
>
> - bodyHeaderText textField
>
>   Form body title.
>
> - nextButtonText textField

### Make REST API Call

Extend the functionality of the DaVinci platform by invoking any third party service.

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - - URL textField required
>   - HTTP Method dropDown required
>   - Query Params keyValueList
>   - Headers keyValueList
>   - Body dropDown
>   - Body Params keyValueList
>   - raw codeEditor
>
>   Input your raw request body
>
> - Success Response Content Type dropdownWithCreate
>
>   Content Type of the response data. To apply output schema content type must be application/json
>
> - outputSchema codeEditor
>
>   Follow example for JSON schema.
>
> - * Keep API output if the validation failed toggleSwitch
>   * Error Response Content Type dropdownWithCreate
>
>   Content Type of the response data. To apply output schema content type must be application/json
>
> - outputSchemaError codeEditor
>
>   Follow example for JSON schema.
>
> - MTLS Support dropDown
>
>   Select the client certificate used to make outbound mTLS connections.
>
>   * None (Default)
>
> - Ignore TLS Errors toggleSwitch
>
>   When enabled, the connector ignores TLS errors. Use this for testing in non-production environments.
>
> - Block Redirects toggleSwitch
>
>   When enabled, DaVinci enhances the security of the flow by preventing the browser from automatically following redirects and an error occurs instead.
>
> - Timeout (ms) textField
>
>   Timeout for API call. Leave blank to not have timeout.
>
> * output object
>
>   * rawResponse object
>
>     * statusCode integer
>
>     * body array/object/number/string/boolean
>
>     * headers array
>
>       * item object

### Custom HTML Template

Create an HTML page using this customizable template.

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - Content Source dropDown
>
>   Select the source of the HTML, CSS, & Script content
>
> - * Template
>   * HTML Template textArea
>   * HTML CDN URL textField required
>
>   Enter the CDN URL that hosts the HTML you would like to use. The CDN hostname must be listed in the Trusted Sites under the connector settings.
>
> - * CSS codeEditor
>   * CSS CDN URL textField
>
>   Enter the CDN URL that hosts the CSS you would like to use. The CDN hostname must be listed in the Trusted Sites under the connector settings.
>
> - Script codeEditor
>
>   Write custom JavaScript. Caution: Custom code is for advanced users only. Before using custom code, review the security risks in the DaVinci documentation by searching for "Using custom code safely".
>
> - Script CDN URL textField
>
>   Enter the CDN URL that hosts the Javascript you would like to use. The CDN hostname must be listed in the Trusted Sites under the connector settings.
>
> - Use Recaptcha Verification toggleSwitch
>
>   Add sk-component skrecaptcha to use this feature.
>
> - Form validation rules validationRules
>
>   Rules to check to validate form inputs
>
> - inputSchema codeEditor
>
>   Follow example for JSON schema.
>
> - outputSchema codeEditor
>
>   Follow example for JSON schema.
>
> - * formFieldsList formFieldsList
>   * challenge textField
>
> * output object
>
>   * formFieldsList object

### Create QR Code for URL

Create a QR code that contains a URL.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - URL textField required
>
> * default object
>
>   * properties object
>
>     * customUrl string required minLength: 0 maxLength: 400
>
>       Custom URL to create the QR Code
>
> Input Example
>
> ```json
> {
>   "properties": {
>     "customUrl": "testurl.com"
>   }
> }
> ```
>
> * output object
>
>   * generatedQr string

### Continue Polling

Use this capability in conjunction with Polling in Custom HTTP capabilities.

> **Collapse: Show details**
>
> * Properties
>
> - Node ID of the UI node (Optional) textField
>
>   In advanced scenarios, it might be required to specify the Node ID of the UI node where polling in enabled. When a Node ID is not entered (default behavior), polling will continue on the current UI node.

### Simulate Latency

Send a response with latency.

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - Delay Time (ms) textField
>
>   Time to wait for response to be sent in milliseconds. Default: 50
>
>   Default: `50`
>
> - Return Success Response toggleSwitch
>
>   Return success or failure response
>
> - HTTP Body (JSON) textArea
>
>   This property needs to be a properly formatted JSON value. It can contain DaVinci parameters, which will be replaced at runtime. If you are using DaVinci parameters that are of type 'string', you will need to put string quotes around it.
>
> * output object