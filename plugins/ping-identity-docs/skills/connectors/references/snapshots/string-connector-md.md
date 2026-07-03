---
title: String Connector
description: The String connector lets you transform the text value of a variable in your PingOne DaVinci flow.
component: connectors
page_id: connectors::string_connector
canonical_url: https://docs.pingidentity.com/connectors/string_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 19, 2024
section_ids:
  setup: Setup
  resources: Resources
  configuring-the-string-connector: Configuring the String connector
  using-the-connector-in-a-flow: Using the connector in a flow
  changing-the-capitalization-of-a-string: Changing the capitalization of a string
  changing-values-to-another-data-type: Changing values to another data type
  concatenating-two-strings: Concatenating two strings
  decoding-or-encoding-a-string: Decoding or encoding a string
  searching-and-replacing-content: Searching and replacing content
  generating-random-strings: Generating random strings
  removing-white-space-from-string: Removing white space from string
  capabilities: Capabilities
  toLowerCase: Convert to Lowercase
  toUpperCase: Convert to Uppercase
  toTitleCase: Convert to Title Case
  changeDataType: Change Data Type
  concatenateStrings: Concatenate
  decodeString: Decode String
  encodeString: Encode String
  findString: Find Substring
  replace: Find and Replace
  generateRandomString: Generate String
  trimWhiteSpace: Remove White Space
---

# String Connector

The String connector lets you transform the text value of a variable in your PingOne DaVinci flow.

You can use the String connector to:

* Convert strings to lowercase, uppercase, or title case

* Convert any type of variable to a different data type

* Concatenate two or more strings

* Encode and decode a string

* Search and replace text in a string

* Generate a random string

* Remove white space from a string

## Setup

### Resources

Learn more in the following:

* DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Configuring the String connector

Add the connector in DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

## Using the connector in a flow

### Changing the capitalization of a string

You can use the **Convert to Lowercase**, **Covert to Uppercase**, or **Convert to Title Case** capabilities to change a string's capitalization.

For example, if your **Input String** is `myVariableValue`, you'll get one of the following results depending on the capability you choose:

* `MYVARIABLEVALUE`

* `myvariablevalue`

* `Myvariablevalue`

Changing the case of a string can help you to standardize values before you compare them, such as when using the Function connector.

You can use the **Convert to Lowercase** capability with the **Concatenate** capability to generate usernames. For example, you can take the inputs `John` and `Smith` and convert them to lowercase before using the **Concatenate** capability to convert both variables to `johnsmith@example.com`.

To remove an unnecessary blank space at the beginning or end of your output string, enable **Remove White Space**.

### Changing values to another data type

You can use the **Change Data Type** capability to change the data of any value to a **Boolean**, **Number**, or **String**. For example, if your **Input Value** is the string `true`, you can convert to the boolean `true`. Or take the number `3` and convert to the string `"3"`.

Changing the data type is useful for testing that the incoming data is in the correct format. For example, if you want to convert driver license numbers, such as `456123789`, from a string to number, the capability will return `True`. However, if the capability instead receives a passport ID, such as `P123456AA`, it will return `False` (error code `400`; invalid input).

No special configuration is needed. Add the capability and populate its properties according to the help text.

### Concatenating two strings

The **Concatenate** capability lets you merge multiple strings.

The following example takes the input strings `john` and `smith` and converts them to `johnsmith@example.com`:

1. In the **Input Value** section, add `john` to the **Value 1** field or click **{}** and select a variable from your flow that contains the string that you want to concatenate.

2. In the **Value 2**, add `smith` or click **{}** and select a variable from your flow that contains the string that you want to concatenate.

3. Click **Add** to include an additional field to concatenate.

   ![A GIF showing a user clicking the add button in the String connector's concatenate string capability to add a field before including example text.](_images/connector-images/dvc-string-add-input-value.gif)

4. In the new **Value 3** field, add an email domain such as `@example.com`.

No special configuration is needed. Add the capability and populate its properties according to the help text.

### Decoding or encoding a string

The **Decode** and **Encode** capabilities let you decode and encode a string from one of several formats: **Base64**, **URL**, or **Base64 URL**.

For example, you can take the plain text input `johnsmith@example.com` and encode with Base64 to `am9obnNtaXRoQGV4YW1wbGUuY29t`.

No special configuration is needed. Add the capability and populate its properties according to the help text.

### Searching and replacing content

The **Find Substring** capability lets you find a substring and its index. The outputs will include a `found` variable which is a boolean returning true if the substring is found and an `index` variable which is the substring's position in the string.

For example, if you take the string `johnsmith@example.com` and search for the substring `exa`, you get the following output:

```json
{
   "originalValue": "johnsmith@example.com"
   "match": ["exa"]
   "index": 10
   "found": true
}
```

The **Find and Replace** capability lets you search for text using literal matching or a regular expression. For example, you could replace every instance of `test` with `production`:

1. In the **Input String** field, click **{}** and select a variable from your flow that contains the string that you want to search for.

2. If your original variable value has blank space at the end that you don't want, enable **Trim White Space** to remove it.

3. In the **Input String** field, enter the text that you want to find in the string, such as `test`. Alternatively, you can enter a regular expression, such as `/te[xs]t/g`, which will match both `test` and `text` and the `/g` flag will apply the change to all matches in the input string.

4. If you entered a regular expression in the **Input String** field, enable **Search Using Regex**.

   |   |                                                                                                                                              |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | **Replace Mode** is for simple matching. When **Search Using Regex** is enabled, the regex itself determines which matched text is replaced. |

5. In the **New Value** field, enter the string that you want to replace the match with, such as `production`.

When **Search Using Regex?** is enabled, the **Search** field accepts regular expressions in the format `/<expression>/`.

|   |                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This uses the ECMA / JavaScript regex engine. Learn more in [Regular expressions - JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions) on the MDN site. |

For example, you can mask part of a user's email address in the user interface by entering the following regular expression: `/(?<=.{2}).(?=[^@]*?@)/g`.

![A screen capture showing the Find and Replace capability with the example expression in the Search field.](_images/connector-images/dvc-string-find-and-replace.png)

In this example, `jsmith@example.com` becomes `js**@example.com`:

![A screen capture showing the output of the example.](_images/connector-images/dvc-string-result-screen.png)

### Generating random strings

The **Generate String** capability lets you create pseudorandom numeric or alphanumeric strings of a certain length. You can use this to create temporary passwords or add unique suffixes to user identifiers.

No special configuration is needed. Add the capability and populate its properties according to the help text.

### Removing white space from string

The **Remove White Space** capability lets you remove leading or trailing white space from a variable.

No special configuration is needed. Add the capability and populate its properties according to the help text.

## Capabilities

### Convert to Lowercase

Change a string value to lowercase and optionally remove white space, such as " MYVALUE" to "myvalue".

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
>   The string to process. Enter a string or select a string value from your flow.
>
> - Trim White Space toggleSwitch
>
>   When enabled, removes any white space at the beginning or end of the input string.
>
> * default object
>
>   * properties object
>
>     * originalValue string/number required
>
> - output object
>
>   * originalValue string
>
>   * newValue string
>
> Output Example
>
> ```json
> {
>   "originalValue": "Frank",
>   "newValue": "frank"
> }
> ```

### Convert to Uppercase

Change a string value to uppercase and optionally remove white space, such as " myvalue" to "MYVALUE".

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
>   The string to process. Enter a string or select a string value from your flow.
>
> - Trim White Space toggleSwitch
>
>   When enabled, removes any white space at the beginning or end of the input string.
>
> * default object
>
>   * properties object
>
>     * originalValue string/number required
>
> - output object
>
>   * originalValue string
>
>   * newValue string
>
> Output Example
>
> ```json
> {
>   "originalValue": "Frank",
>   "newValue": "FRANK"
> }
> ```

### Convert to Title Case

Change a string value to title case and optionally remove white space, such as " my value" to "My Value".

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
>   The string to process. Enter a string or select a string value from your flow.
>
> - Trim White Space toggleSwitch
>
>   When enabled, removes any white space at the beginning or end of the input string.
>
> * default object
>
>   * properties object
>
>     * originalValue string/number required
>
> - output object
>
>   * originalValue string
>
>   * newValue string
>
> Output Example
>
> ```json
> {
>   "originalValue": "my value",
>   "newValue": "My Value"
> }
> ```

### Change Data Type

Change the data type of any value to boolean, number, or string.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Input String textField
>
>   The value to process. Enter a string or select a string value from your flow.
>
> - Change to dropDown required
>
>   Select the data type to change the input value to.
>
>   * String (Default)
>
>   * Boolean
>
>   * Number
>
> - Trim White Space toggleSwitch
>
>   When enabled, removes any white space at the beginning or end of the input string.
>
> * default object
>
>   * properties object
>
>     * inputValue string/number required
>
> - output object
>
>   * originalValue string
>
>   * newValue string
>
> Output Example
>
> ```json
> {
>   "newValue": "frank"
> }
> ```

### Concatenate

Merge multiple strings together.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Input String multipleTextFields
>
>   The string to process. Enter a string or select a string value from your flow.
>
> - Delimiter textField
>
>   The optional string to include between each concatenated value, such as ", " or "-".
>
> - Include Final Delimiter toggleSwitch
>
>   When enabled, the delimiter is also included at the end of the concatenated string.
>
> - Trim White Space toggleSwitch
>
>   When enabled, removes any white space at the beginning or end of the input string.
>
> * default object
>
>   * properties object
>
>     * concatenateInput array required
>
>     * concatenateDelimiter string
>
>     * finalDelimiter boolean
>
>     * shouldTrim boolean
>
> - output object
>
>   * originalValue string
>
>   * newValue string

### Decode String

Decode a string using one of several formats, such as Base64 or URL.

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
>   The string to process. Enter a string or select a string value from your flow.
>
> - String Decode Method dropDown required
>
>   The decoding format applied to the input string.
>
>   * Base64 (Default)
>
>   * URL
>
>   * Base64 URL
>
> * default object
>
>   * properties object
>
>     * originalValue string required
>
>     * method string
>
> - output object
>
>   * originalValue string
>
>   * newValue string

### Encode String

Encode a string using one of several formats, such as Base64 or URL.

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
>   The string to process. Enter a string or select a string value from your flow.
>
> - String Encode Method dropDown required
>
>   The encoding format applied to the input string.
>
>   * Base64 (Default)
>
>   * URL
>
>   * Base64 URL
>
> * default object
>
>   * properties object
>
>     * originalValue string required
>
>     * method string
>
> - output object
>
>   * originalValue string
>
>   * newValue string

### Find Substring

Find a substring and its index.

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
>   The string to process. Enter a string or select a string value from your flow.
>
> - Find Substring textField required
>
>   The substring to process. Enter a string or select a string value from your flow.
>
> * default object
>
>   * properties object
>
>     * originalValue string required
>
>     * finder string required
>
> - output object
>
>   * originalValue string
>
>   * match string
>
>   * index number
>
>   * found boolean

### Find and Replace

Replace part of a string using simple matching or Regex.

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
>   The string to process. Enter a string or select a string value from your flow.
>
> - Search textField
>
>   The text to search for in the original string value. For simple matching, enter literal text, such as "test". For more complex matching, enter a valid regular expression and enable Search Using Regex. For example, entering "/te\[xs]t/g" matches both "test" and "text".
>
> - New String Value textField
>
>   When a match is found, the text identified by the Search field is replaced with this string.
>
> - Search Using Regex? toggleSwitch
>
>   By default, the value in the Search field is used for simple matching. When enabled, the value in the Search field must be formatted as a regular expression such as "/\<expression>/g"
>
> - Replace Mode dropDown
>
>   Determines whether the first match or all matches are replaced with the new value.
>
>   * All Matches
>
>   * First Match (Default)
>
> - Trim White Space toggleSwitch
>
>   When enabled, removes any white space at the beginning or end of the input string.
>
> * default object
>
>   * properties object
>
>     * originalValue string/number required
>
>     * oldToken string/number required
>
>     * newToken string/number required
>
> - output object
>
>   * originalValue string
>
>   * newValue string
>
> Output Example
>
> ```json
> {
>   "newValue": "frank"
> }
> ```

### Generate String

Generate an alphabetic or alphanumeric string of a defined length.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - String Length textField
>
>   Enter the number of characters you want in the string, such as "15".
>
> - Include Numbers toggleSwitch
>
>   By default, generated strings are a mix of uppercase and lowercase letters. When enabled, the string also includes numbers.
>
> * default object
>
>   * properties object
>
>     * length number required
>
>     * isAlphaNumeric boolean
>
> - output object
>
>   * generatedString string
>
> Output Example
>
> ```json
> {
>   "generatedString": "aivsdvjqwoit"
> }
> ```

### Remove White Space

Remove leading or trailing white space.

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
>   The string to process. Enter a string or select a string value from your flow.
>
> * default object
>
>   * properties object
>
>     * originalValue string required
>
> - output object
>
>   * originalValue string
>
>   * newValue string
>
> Output Example
>
> ```json
> {
>   "newValue": "my value"
> }
> ```
