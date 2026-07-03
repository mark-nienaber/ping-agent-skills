---
title: Code Snippet Connector
description: The Code Snippet connector lets you create custom JavaScript code that you can reuse across multiple PingOne DaVinci flows. You can use it to provide dynamic messages, get a specific attribute from a JavaScript Object Notation (JSON) payload, or insert any other custom behavior into your flow.
component: connectors
page_id: connectors::code_snippet_connector
canonical_url: https://docs.pingidentity.com/connectors/code_snippet_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 16, 2024
section_ids:
  setup: Setup
  configuring-the-code-snippet-connector: Configuring the Code Snippet connector
  connector-configuration: Connector configuration
  code-snippet: Code Snippet
  input-schema: Input Schema
  output-schema: Output Schema
  using-the-connector-in-a-flow: Using the connector in a flow
  showing-a-dynamic-message-with-a-switch: Showing a dynamic message with a switch
  getting-a-value-from-a-json-response: Getting a value from a JSON response
  using-variables-in-code-snippets: Using variables in code snippets
  capabilities: Capabilities
  snippet: Snippet
---

# Code Snippet Connector

The Code Snippet connector lets you create custom JavaScript code that you can reuse across multiple PingOne DaVinci flows. You can use it to provide dynamic messages, get a specific attribute from a JavaScript Object Notation (JSON) *(tooltip: \<div class="paragraph">
\<p>An open, lightweight data-interchange format that uses human-readable text to store and transmit data.\</p>
\</div>)* payload, or insert any other custom behavior into your flow.

This piece of code is saved at the environment level, so you can use it multiple times in a flow, or reuse it in all of your flows. When you update the code, it affects every flow that you added it to. This is different from the [Functions Connector](functions_connector.html)'s **Custom Function** capability, which only exists once in a single flow.

Because this code is reusable, it can help in the centralization or automation of your organization's common processes.

|   |                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Learn more about best practices to use custom code in your flows in [Using custom code safely](https://docs.pingidentity.com/davinci/davinci_best_practices/davinci_best_practices_custom_code.html). |

|   |                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The following libraries are available in custom functions:- [File System](https://nodejs.org/api/fs.html) (non-functional mockup only)

- [Buffer](https://nodejs.org/api/buffer.html)

- All JavaScript built-in objects |

## Setup

### Configuring the Code Snippet connector

Add the connector in DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

##### Code Snippet

Enter your own JavaScript code within the default `module.exports`. This gives you access to the variables from your flow.

|   |                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * To give yourself more room to work, click the Expand (![A screen capture of the Maximize icon.](_images/connector-images/dvc-entrust-maximize-icon.jpg)) button.

* To access a variety of useful coding tools, right-click the field.

  ![A screenshot of the Code Snippet field.](_images/connector-images/dvc-code-snippet-field.jpg) |

##### Input Schema

This defines the structure of the data that your code receives from the flow. When you pass variables into your code from the flow, use this space to define whether it is a string, boolean, or other type. Learn more in [JSON-Schema.org](https://json-schema.org/).

##### Output Schema

This defines the structure of the data that your code returns to the flow. Use this space to define the type for any variable your code returns.

Get your output schema:

1. Copy your raw JSON output:

   1. Following your **Code Snippet** node, add an [HTTP](http_connector.html) connector and select the **Custom HTML Message** capability. Click the new node in your flow.

   2. In the **Message** field, click **{}** and insert the **output (object)** variable from your **Code Snippet** node.

   3. Click **Apply**.

   4. Click **Save**, **Deploy**, and **Try Flow**.

   5. Copy the JSON payload that appears in your HTML message.

2. In a browser, open the [Online JSON Schema Validator and Generator](https://extendsclass.com/json-schema-validator.html) tool.

3. Paste the JSON response you copied into the **JSON** field. Click **Generate Schema From JSON**. Copy the output from the **JSON SCHEMA** field.

   ![A screen capture that shows the JSON Schema Validator and Generator tool after generating the JSON schema.](_images/connector-images/dvc-flow-conductor-json-schema-validator.jpg)

4. In your **Code Snippet** node, paste the JSON schema into the **Output Schema** field.

   To edit your Code Snippet after adding it to a flow, come back to these details by clicking the **Edit** button.

   ![A screen capture of the Code Snippet settings, showing the Edit button.](_images/connector-images/dvc-code-snippet-settings.jpg)

   |   |                                                                          |
   | - | ------------------------------------------------------------------------ |
   |   | Any changes you make will affect every flow that uses this Code Snippet. |

## Using the connector in a flow

### Showing a dynamic message with a switch

In this example, a user has selected a multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)* method. Depending on which method they chose, we'll display a different message on the screen.

1. Add a **Code Snippet** connection to your environment. For help, refer to [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html).

2. Click the **Gear** icon to open the **Code Snippet Details** window.

   ![Mouse clicking the connector's Gear icon to open the configuration window](_images/connector-images/dvc-code-snippet-details-gif.gif)

3. In the **Code Snippet** field, enter the following switch code:

   ```
   // Write your code here
   // Supported language: Javascript
   module.exports = a = async ({params}) => {
       switch (params.mfaMethod){
           case "SMS":
               return {'HTMLResult': "Enter your phone number"};
           break;

           case "EMAIL":
               return {'HTMLResult': "Please enter your email address"};
           break;

           default:
               return {'HTMLResult': "No MFA method selected."}
       }
   }
   ```

4. This code takes the `mfaMethod` variable from earlier in our flow and checks the value. If it matches `SMS` or `EMAIL`, it returns the matching message. If the `mfaMethod` variable doesn't match one of the two options, the code returns the error "No MFA method selected".

5. We know that the `mfaMethod` variable in our flow contains text, so we define it as a string in the **Input Schema** field:

   ```json
   {
       "input": {
           "type": "object",
           "properties": {
               "mfaMethod": {
                   "type": "string"
               }
           }
       }
   }
   ```

6. Our example code always returns a message in the *HTMLResult* variable, so we define it as a string in the **Output Schema** field:

   ```json
   {
       "output": {
           "type": "object",
           "properties": {
               "HTMLResult": {
                   "type": "string"
               }
           }
       }
   }
   ```

7. In your flow, add the **Code Snippet** connection that you created and select the **Snippet** capability. No other setup is needed.

### Getting a value from a JSON response

In this example, we retrieved information about a user from a directory, including the user's name, address, phone number, and more. To continue our flow, we need the user ID, which is buried somewhere in the response.

1. Add a **Code Snippet** connection to your environment. Learn more in [Online JSON Schema Validator and Generator](https://extendsclass.com/json-schema-validator.html).

2. Click the **Gear** icon to open the **Code Snippet Details** window.

   ![Mouse clicking the connector's gear icon to open the configuration window](_images/connector-images/dvc-code-snippet-details-gif.gif)

3. In the **Code Snippet** field, enter the following:

   ```
   // Write your code here
   // Supported language: Javascript
   module.exports = a = async ({params}) => {
       console.log('params: ', params)
       const body = JSON.parse(params.body)
       return {
           'userId': body._embedded.users[0].id
           }
   }
   ```

4. This code uses `JSON.parse` to put the usable data into the `body` object. This is a good starting point when you want to parse a JSON payload.

5. Next, the code returns a variable called `userId`. In our case, the user ID is located at `__embedded.users[0].id` inside the `body` object we created. When creating your own code, look at the structure of the payload to determine the path you need.

6. We know that the `id` contains text, so we define it as a string in the **Input Schema** field:

   ```json
   {
       "input": {
           "type": "object",
           "properties": {
               "id": {
                   "type": "string"
               }
           }
       }
   }
   ```

7. Our user ID contains text, so we define it as a string in the **Output Schema** field:

   ```json
   {
       "output": {
           "type": "object",
           "properties": {
               "userId": {
                   "type": "string"
               }
           }
       }
   }
   ```

8. In your flow, add the **Code Snippet** connection that you created and select the **Snippet** capability. No other setup is needed.

### Using variables in code snippets

You can create dynamic code by including variables in your code snippets. Variables are populated when the flows runs.

* Global variables

  For global variables, use the following syntax:

  ```json
  {{global.variables.variablename}}
  ```

  For example, to include the following `username` variable, include the following:

  ```json
  {{global.variables.userInfo.username}}
  ```

* Flow instance variables

  For flow instance variables, use the following syntax:

  ```json
  {{local.nodeid.output.variablename}}
  ```

To find the value for any variable:

1. Open your flow.

2. Select a node that has access to the variable you want to use.

3. In any field, click **{}** and select the variable.

4. Use your mouse to hover over the inserted variable.

![A screen recording that shows the flow builder inserting a variable in the UI and checking the hover text.](_images/connector-images/dvc-code-snippet-inserting-variable.gif)

## Capabilities

### Snippet

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - functionArgumentList functionArgumentList
>
> * output object::
