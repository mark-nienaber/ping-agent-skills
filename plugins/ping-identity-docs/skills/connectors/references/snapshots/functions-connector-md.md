---
title: Functions Connector
description: The Functions connector lets you branch your PingOne DaVinci flow using logical conditions or based on the result of custom JavaScript code.
component: connectors
page_id: connectors::functions_connector
canonical_url: https://docs.pingidentity.com/connectors/functions_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 19, 2024
section_ids:
  setup: Setup
  setting-up-the-functions-connector: Setting up the Functions connector
  using-the-connector-in-a-flow: Using the connector in a flow
  comparing-values: Comparing values
  adding-a-custom-function-to-your-flow: Adding a custom function to your flow
  checking-whether-a-variable-has-a-value: Checking whether a variable has a value
  hashing-a-value: Hashing a value
  capabilities: Capabilities
  AEqualsB: A == B
  ANotEqualsB: A != B
  ALessThanB: A < B
  ALessThanEqualToB: A ⇐ B
  AGreaterThanB: A > B
  AGreaterThanEqualToB: A >= B
  AGreaterThanBLessThanC: B < A < C
  AGreaterThanBLessThanEqualC: B < A ⇐ C
  AGreaterThanEqualBLessThanC: B ⇐ A < C
  AGreaterThanEqualBLessThanEqualC: B ⇐ A ⇐ C
  AIsEmpty: A is Empty
  arrayOfAIncludesB: If Array A includes B
  stringAContainsB: If String A includes B
  customFunction: Custom Function
  digestMessage: Create a Hash
  AEqualsMultipleB: A == B (Multiple Conditions)
---

# Functions Connector

The Functions connector lets you branch your PingOne DaVinci flow using logical conditions or based on the result of custom JavaScript code.

You can use the Functions connector to:

* Compare the value of variables in your flow, such as A > B

* Perform calculations

* Run custom JavaScript

|   |                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can find best practices to use custom code in your flows in [Using custom code safely](https://docs.pingidentity.com/davinci/davinci_best_practices/davinci_best_practices_custom_code.html). |

## Setup

### Setting up the Functions connector

In DaVinci, add a **Functions** connection. Learn more in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html).

This connector doesn't have a configuration at the environment level. You configure it in your flow instead.

## Using the connector in a flow

### Comparing values

You can compare values using a variety of comparison capabilities, such as **A == B**, **A != B**, and **A < B < C**.

|   |                                                                                                                                                                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | A node with the **A == B (Multiple Conditions)** capability cannot be branched from the top. You must branch from the conditional outcomes that are available after you configure the node.![A screen capture showing an incorrect example of branching from the top of an A == B node.](_images/connector-images/dvc-functions-incorrect-branching.png) |

For example, we can check whether a user is eligible for a senior's discount based on their age:

1. In your flow, add the **Functions** connector and select the **A >= B** capability. Select the node that appears in your flow.

2. In the **Value A** field, click **{}**, then select the attribute that holds the user's current age.

3. In the **Value B** field, enter 65.

   ![A screen capture of the user inserting variables into the value fields.](_images/connector-images/dvc-functions-variable-value-field.gif)

4. After applying your changes, you can add a True branch from your node for seniors, and a False branch for those who aren't.

### Adding a custom function to your flow

You can make your flows more powerful and flexible by adding your own custom code. This capability lets you take inputs from your flow, work with them in JavaScript, and make the results available in your flow.

The JavaScript in a custom function runs on the server, not the client. These functions stay with your flow if you export it to another DaVinci environment.

For example, we want to know how long until a user turns 65 and gets a senior's discount. We already know their age from earlier in the flow and that they're younger than 65. Our code subtracts their current age from 65 and make the result available in the flow.

|   |                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The following libraries are available in custom functions:- [File System](https://nodejs.org/api/fs.html) (non-functional mockup only)

- [Buffer](https://nodejs.org/api/buffer.html)

- All JavaScript built-in objects |

|   |                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | All code for custom functions must comply with JavaScript's strict mode. Learn more in [Strict Mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode). |

1. In your flow, add the **Functions** connector and select the **Custom Function** capability.

2. Select the node that appears in your flow.

3. Make the variable with their current age available in your function:

   1. In the **Variable Input List**, click **Add**.

   2. In the **Variable Name** field, enter `currentAge`. Our code will call the variable by this name.

   3. In the **Value** field, click the input button and select the variable from your flow that you want as the value of `currentAge` in your function.

   4. In the **Data Type** list, select the type that best suits the value your variable holds.

   5. (Optional) To bring in more variables, click **Add** again.

      |   |                                                                            |
      | - | -------------------------------------------------------------------------- |
      |   | To remove an extra variable, click **Edit**, then click the remove button. |

4. In the **Code** field, enter your JavaScript custom code.

   |   |                                                                                                                                                   |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To give yourself more room to work, click the **Expand** ([icon: expand, set=fas]) icon. This lets you use your browser zoom to enlarge the code. |

   Our code creates a variable called `ageDelta` that holds the difference between the user's current age and 65:

   ```
   // How long until eligible for a senior's discount?
   module.exports = a = async ({params}) => {
       Let ageDelta = 65 - params.currentAge
       return {'yearsUntilDiscount': ageDelta}
   }
   ```

   Our code returns a variable called `yearsUntilDiscount`.

5. In the **Output Schema** field, capture the return variables from your code and make them available elsewhere in your flow.

   ```json
   {
       "output": {
           "type": "object",
           "properties": {
               "yearsUntilDiscount": {
                   "type": "integer"
               }
           }
       }
   }
   ```

   Now, `yearsUntilDiscount` is available to use elsewhere in your flow.

### Checking whether a variable has a value

When building a flow, it can be useful to check whether a variable contains a value. For example, testing whether the expected user ID or token has actually been provided earlier in the flow.

![A screen capture of a short flow that branches based on whether a variable is empty.](_images/connector-images/dvc-functions-empty-variable-branching.png)

1. Check whether the variable is empty:

   1. In your flow, add a **Functions** connector with the **A is Empty** capability.

   2. In the **Value A** field, click **{}** and select the variable that you want to check.

   3. Enable **Check undefined/null**.

   4. In the **Type** list, select the type of data that the variable should contain.

      ![A screen capture of the A Is Empty capability configuration.](_images/connector-images/dvc-functions-a-is-empty.png)

   5. Click **Apply**.

2. Add a success path by following the **A is Empty** node using the **Any Trigger False** condition.

   |   |                                                                                                                                                                                                   |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The **A is Empty** capability returns "false" when the expected User ID, token, or other value is provided. As a result, the success path for your flow follows branches from the "false" result. |

3. Add an error message or failure path by following the **A is Empty** node using the **All Triggers True** condition.

### Hashing a value

You can use the **Create a Hash** capability to hash the value provided by another node in your flow. Hashing transforms an input value into a fixed-length string or number for secure verification.

To hash a value:

1. In your flow, add a **Functions** connector with the **Create a Hash** capability.

2. In the **Input Value** field, enter the value or select the variable containing the value to hash.

3. Select a **Hash Algorithm** to use.

4. Select a **Salt Mode** to determine whether to add a salt value to make the hash value more unique and difficult to guess.

   |   |                                                                                                                         |
   | - | ----------------------------------------------------------------------------------------------------------------------- |
   |   | To use a custom value, you can select **Use Custom Salt Value** and define your own in the **Custom Salt Value** field. |

5. Select the **Output Encoding Format** for the resulting hash value.

   |   |                                                                                                                                    |
   | - | ---------------------------------------------------------------------------------------------------------------------------------- |
   |   | Binary encoding produces raw binary, which does not render meaningfully when the hashed value outputs to the screen in plain text. |

## Capabilities

### A == B

If A equals B

> **Collapse: Show details**
>
> * Properties
>
> - - leftValueA textField
>   - rightValueB textField
>   - type dropDown
>   - Case Sensitive toggleSwitch
>
>   When enabled, the values are considered a match only if the case is the same.

### A != B

If A is not equal to B

> **Collapse: Show details**
>
> * Properties
>
> - - leftValueA textField
>   - rightValueB textField
>   - type dropDown
>   - Case Sensitive toggleSwitch
>
>   When enabled, the values are considered a match only if the case is the same.

### A < B

If A is less than B

> **Collapse: Show details**
>
> * Properties
>
> - - leftValueA textField
>   - rightValueB textField
>   - type dropDown

### A ⇐ B

If A is less than or equal to B

> **Collapse: Show details**
>
> * Properties
>
> - - leftValueA textField
>   - rightValueB textField
>   - type dropDown

### A > B

If A is greater than B

> **Collapse: Show details**
>
> * Properties
>
> - - leftValueA textField
>   - rightValueB textField
>   - type dropDown

### A >= B

If A is greater than or equal to B

> **Collapse: Show details**
>
> * Properties
>
> - - leftValueA textField
>   - rightValueB textField
>   - type dropDown

### B < A < C

If A is between B and C

> **Collapse: Show details**
>
> * Properties
>
> - - leftValueA textField
>   - rightValueB textField
>   - rightValueC textField
>   - type dropDown

### B < A ⇐ C

If A is between B and C or equal to C

> **Collapse: Show details**
>
> * Properties
>
> - - leftValueA textField
>   - rightValueB textField
>   - rightValueC textField
>   - type dropDown

### B ⇐ A < C

If A is between B and C or equal to B

> **Collapse: Show details**
>
> * Properties
>
> - - leftValueA textField
>   - rightValueB textField
>   - rightValueC textField
>   - type dropDown

### B ⇐ A ⇐ C

If A is between B and C or equal to B or C

> **Collapse: Show details**
>
> * Properties
>
> - - leftValueA textField
>   - rightValueB textField
>   - rightValueC textField
>   - type dropDown

### A is Empty

If A is Empty

> **Collapse: Show details**
>
> * Properties
>
> - - leftValueA textField
>   - Check undefined/null toggleSwitch
>
>   Check undefined/null
>
> - type dropDown

### If Array A includes B

> **Collapse: Show details**
>
> * Properties
>
> - - leftValueA textField
>   - rightValueB textField
>   - type dropDown
>   - inputContains dropDown
>   - Case Sensitive toggleSwitch
>
>   When enabled, the values are considered a match only if the case is the same.

### If String A includes B

> **Collapse: Show details**
>
> * Properties
>
> - - leftValueA textField
>   - rightValueB textField
>   - Case Sensitive toggleSwitch
>
>   When enabled, the values are considered a match only if the case is the same.

### Custom Function

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - - variableInputList variableInputList
>   - code codeEditor
>
>   Follow example for code. Caution: Custom code is for advanced users only. Before using custom code, review the security risks in the DaVinci documentation by searching for "Using custom code safely".
>
>   Default:
>
>   ```none
>   // Write your code here
>   // Supported language: Javascript
>   module.exports = async ({params}) => {
>   console.log('params: ', params)
>   return {'testVariable': params.testVariable}
>   }
>   ```
>
> - outputSchema codeEditor
>
>   Follow example for JSON schema.
>
>   Default:
>
>   ```none
>   {
>   "output": {
>   "type": "object",
>   "properties": {
>   "testVariable": {
>   "type": "string"
>   }
>   }
>   }
>   }
>   ```
>
> * output object::

### Create a Hash

Hash a value using the selected algorithm

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Input Value textField
>
>   The value to hash, such as "myPa55woRd123#".
>
> - Hash Algorithm dropDown
>
>   The hash algorithm to use.
>
>   * SHA-1
>
>   * SHA-256 (Default)
>
>   * SHA-384
>
>   * SHA-512
>
> - Salt Mode dropDown required
>
>   Determines whether to add a salt value to make the hashed value unique and more difficult to guess. For a custom value, select Use Custom Salt Value and enter the value in Custom Salt Value.
>
>   * Off (Default)
>
>   * Generate random salt
>
>   * Use Custom Salt Value
>
> - Custom Salt Value textField required
>
>   Enter the salt value to use when hashing, such as "mySaltu7v8w9x0".
>
> - Output Encoding Format dropDown required
>
>   The encoding method for the resulting hashed value.
>
>   * Base64
>
>   * Binary
>
>   * Hexadecimal (Default)
>
> * default object
>
>   * properties object
>
>     * message string required
>
>       The input value to hash, such as "myPa55woRd123#".
>
>     * digestAlgorithm string required
>
>       The hash algorithm to use.
>
>     * saltMode string
>
>       Determines whether to add a salt value to make the hashed value unique. For useCustomSaltValue, provide the customSaltValue.
>
>     * customSaltValue string
>
>       The salt value to use when hashing, such as "mySaltu7v8w9x0".
>
>     * outputEncodingFormat string
>
>       The encoding method for the resulting hashed value.
>
> Input Example
>
> ```json
> {
>   "properties": {
>     "message": "mysecretpassword",
>     "digestAlgorithm": "sha256",
>     "saltMode": "useCustomSaltValue",
>     "customSaltValue": "mySaltu7v8w9x0",
>     "outputEncodingFormat": "base64"
>   }
> }
> ```
>
> * output object
>
>   * hash string
>
>     The hashed value.
>
>   * salt string
>
>     The salt value used in the hash.
>
>   * length number
>
>     The length of the hashed value.
>
> Output Example
>
> ```json
> {
>   "hash": "NJM86MstFd2CZO4M5nMR4HvJdUafOwpeSL5aFgS+r9A=",
>   "salt": "mySaltu7v8w9x0",
>   "length": 44
> }
> ```

### A == B (Multiple Conditions)

If A equals B or A equals to C …​

> **Collapse: Show details**
>
> * Properties
>
> - - leftValueA textField
>   - rightValueMultiple multipleTextFields
>   - type dropDown
>   - Case Sensitive toggleSwitch
>
>   When enabled, the values are considered a match only if the case is the same.
