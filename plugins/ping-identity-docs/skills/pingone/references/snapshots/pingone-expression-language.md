---
title: Arrays and lists
description: Use arrays and lists in the PingOne Expression Language.
component: pingone
page_id: pingone:pingone_expression_language:p1_expressionlang_arrays_lists
canonical_url: https://docs.pingidentity.com/pingone/pingone_expression_language/p1_expressionlang_arrays_lists.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 3, 2024
---

# Arrays and lists

You can build arrays for the following primitives:

* byte

* short

* int

* long

* float

* double

* char

* boolean

For example, `new <type>[<size>]` or `new <type>[] {<comma-separated values>}`.

You can use lists such as `{<comma-separated values>}`.

|   |                                                       |
| - | ----------------------------------------------------- |
|   | Lists can contain both non-primitives and primitives. |

Access arrays and lists using `[index]`.

| Array or list type                            | Example                               |
| --------------------------------------------- | ------------------------------------- |
| int array                                     | `new long[4]`                         |
| float array                                   | `new float[4]`                        |
| Array initializer                             | `new int[] {1,2,3,4}`                 |
| 2-dimensional array (cannot have initializer) | `new int[2][2]`                       |
| Initializing and accessing array              | `new int[] {1,2,3,4} [0]`             |
| Accessing array property                      | `contacts[0]`                         |
| Empty list                                    | `{}`                                  |
| Integer list                                  | `{1,2,3,4}`                           |
| String list                                   | `{'List', 'of', 'Strings'}`           |
| Accessing list element                        | `{'List', 'of', 'Strings'}[1]`        |
| List with property references                 | `{user.name.given, user.name.family}` |

---

---
title: Collection operations
description: You can use PingOne Expression Language collection operations to transform existing collections.
component: pingone
page_id: pingone:pingone_expression_language:p1_expressionlang_collection_operations
canonical_url: https://docs.pingidentity.com/pingone/pingone_expression_language/p1_expressionlang_collection_operations.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 25, 2025
page_aliases: ["p1_expressionlang_collection_selection.adoc", "p1_expressionlang_collection_projection.adoc"]
section_ids:
  p1-exp-lang-collect-select: Collection selection
  p1-exp-lang-collect-project: Collection projection
---

# Collection operations

You can use collection operations to transform existing collections.

## Collection selection

You can transform an existing collection by selecting a subset based on filtering criteria, which results in a new collection.

`<Collection>.?[<Filter Criteria Expression>]` becomes a new collection.

In addition to returning a filtered collection, you can extract the first or last entry in a collection matching the filter criteria.

`<Collection>.^[<Filter Criteria Expression>]` returns the first element matching the filter criteria.

`<Collection>.$[<Filter Criteria Expression>]` returns the last element matching the filter criteria.

| Selection                                                            | Input                                      | Output         |
| -------------------------------------------------------------------- | ------------------------------------------ | -------------- |
| From an array or collection of numbers, select only the even numbers | `{1,2,3,4,5,6,7,8,9,10}.?[#this % 2 == 0]` | `[2,4,6,8,10]` |
| From an array or collection of numbers, select the first even number | `{1,2,3,4,5,6,7,8,9,10}.^[#this % 2 == 0]` | `2`            |
| From an array or collection of numbers, select the last even number  | `{1,2,3,4,5,6,7,8,9,10}.$[#this % 2 == 0]` | `10`           |

For the following input data model, the table following the data model describes possible selections.

```json
{
    "user": {
        "contacts": [
            {
                "info": "user01@test.com",
                "primary": false,
                "type": "email"
            },
            {
                "info": 9876512345,
                "primary": true,
                "type": "phone"
            },
            {
                "info": 9876511111,
                "primary": false,
                "type": "phone"
            }
        ]
    }
}
```

| Selection                               | Input                              | Output                                                                                                                                      |
| --------------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Select all contact info of type `phone` | `user.contacts.?[type == 'phone']` | ```json
{
  "info": 9876512345,
  "primary": true,
  "type": "phone"
},
{
  "info": 9876511111,
  "primary": false,
  "type": "phone"
}
``` |
| Select the first primary contact info   | `user.contacts.?[primary]`         | ```json
{
  "info": 9876512345,
  "primary": true,
  "type": "phone"
}
```                                                                  |

## Collection projection

You can transform an existing collection by applying transformations on the input collection's data or by selecting specific data, which results in a new collection containing entirely different data sets.

`<Collection>.![<Projection Expression>]` becomes a new collection.

For the following input data model, the table following the data model describes possible projections:

```json
{
    "user": {
        "contacts": [
            {
                "info": "user01@test.com",
                "primary": false,
                "type": "email"
            },
            {
                "info": 9876512345,
                "primary": true,
                "type": "phone"
            },
            {
                "info": 9876511111,
                "primary": false,
                "type": "phone"
            }
        ]
    }
}
```

| Projection                                                      | Input                                                  | Output                             |
| --------------------------------------------------------------- | ------------------------------------------------------ | ---------------------------------- |
| Transform to a list of contact types only                       | `user.contacts.![type]`                                | `["email", "phone", "phone"]`      |
| Extract all primary info attributes                             | `user.contacts.?[primary].![info]`                     | `[9876512345]`                     |
| Extract the primary info attribute as a different object format | `user.contacts.?[primary].![{'primaryContact': info}]` | `[{"primaryContact": 9876512345}]` |

---

---
title: Custom library functions
description: Use the following PingOne Expression Language custom library functions to process data in strings, arrays, and collections.
component: pingone
page_id: pingone:pingone_expression_language:p1_expressionlang_custom_library_functions
canonical_url: https://docs.pingidentity.com/pingone/pingone_expression_language/p1_expressionlang_custom_library_functions.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 25, 2025
page_aliases: ["p1_expressionlang_string_library.adoc", "p1_expressionlang_date_time_library.adoc", "p1_expressionlang_data_library.adoc", "p1_expressionlang_regex_library.adoc", "p1_expressionlang_crypto_library.adoc", "p1_expressionlang_core_library.adoc"]
section_ids:
  exp-lang-string-lib: String library
  exp-lang-date-time-lib: Date and time library
  exp-lang-data-lib: Data library
  exp-lang-regex-lib: Regex library
  exp-lang-crypto-lib: Crypto library
  exp-lang-core-lib: Core library
  examples: Examples
---

# Custom library functions

Use the following custom library functions to process data in strings, arrays, and collections.

## String library

You can perform string-related operations within an expression using the following library.

| String                                                                                                                                                                                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Input                                                                                                                                                                                                        | Output                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| `boolean isNotEmpty(String <input>)`where `<input>` is the string to check.                                                                                                                                                                                                                                                                                                                         | Returns `true` if the input string is not empty (`""`) and not null.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 1. `#string.isNotEmpty('InputData')`

2. `#string.isNotEmpty('')`                                                                                                                                            | 1) `true`

2) `false`                                            |
| `boolean isNotBlank(String <input>)`where `<input>` is the string to check.                                                                                                                                                                                                                                                                                                                         | Returns `true` if the input string is not empty (`""`), not null and not white space only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 1. `#string.isNotBlank('InputData')`

2. `#string.isNotBlank(' ')`                                                                                                                                           | 1) `true`

2) `false`                                            |
| `String upperCase(String <input>)`where `<input>` is the string being converted to upper case.                                                                                                                                                                                                                                                                                                      | Converts all characters to uppercase. Returns all characters in upper case if input is not null. Returns `null` if input is null.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `#string.upperCase('john')`                                                                                                                                                                                  | `JOHN`                                                           |
| `String lowerCase(String <input>)`where `<input>` is the string being converted to lower case.                                                                                                                                                                                                                                                                                                      | Converts all characters to lowercase. Returns all characters in lower case if input is not null. Returns `null` if input is null.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `#string.lowerCase('LOWER')`                                                                                                                                                                                 | `lower`                                                          |
| `String trim(String <input>)`where `<input>` is the string being trimmed.                                                                                                                                                                                                                                                                                                                           | Removes white space from the start and end of `string` if input is not null. Returns `null` if input is null.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `#string.trim(' No Padding ')`                                                                                                                                                                               | `No Padding`                                                     |
| `String substring(String <input>, int <start>, int <end>)`where:- `<input>` is the string to get the substring from

- `<start>` is the position to start from

- `<end>` is the exclusive position to end at                                                                                                                                                                                       | Gets a substring from the input string starting from the start position and up until the end position, not including the end position. You can use a negative value to start or end *n* characters from the end of the string. All position counting is zero-based. If start is not to the left of end, `""` is returned. Returns `null` if input is null.                                                                                                                                                                                                                                                                                                                                                                                                        | 1. `#string.substring('example input for substring demo', 8, 13)`

2. `#string.substring('example input for substring demo', -24, 13)`

3. `#string.substring('example input for substring demo', -24, -19)` | 1) `input`

2) `input`

3) `input`                               |
| `boolean startsWith(String <input>, String <prefix>)`where:- `<input>` is the string to check

- `<prefix>` is the prefix to match at the start of the input string.                                                                                                                                                                                                                                | Checks if the input string starts with the specified prefix and the comparison is case sensitive. Returns `true` if the input string starts with the prefix with the same case or if both are null.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `#string.startsWith('InputData', 'In')`                                                                                                                                                                      | `true`                                                           |
| `boolean endsWith(String <input>, String <suffix>)`where:- `<input>` is the string to check

- `<suffix>` is the suffix to match at the end of the input string                                                                                                                                                                                                                                     | Checks if the input string ends with the specified suffix and the comparison is case sensitive. Returns `true` if input string ends with the suffix with the same case or if both are null.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `#string.endsWith('InputData', 'Data')`                                                                                                                                                                      | `true`                                                           |
| `String[] split(String <input>, String <separators>)`where:- `<input>` is the string to split

- `<separators>` are the characters to be used as delimiters to split the input string                                                                                                                                                                                                               | Splits the provided text into an array based on the specified separators. Returned array won't contain any separators. A null separator splits on white space. Returns `null` if input is null.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `#string.split('Administrator, User, Guest', ', ')`                                                                                                                                                          | `["Administrator", "User", "Guest"]`                             |
| `String join(Array <values>, String <separator>)`where:- `<values>` is the array containing the values to be joined.

- `<separator>` is the delimiter to use when joining the values in the input array. A null separator is treated as an empty string.                                                                                                                                           | Joins the elements of the provided array into a single string containing the provided elements separated by the provided separator. Returns the joined string or `null` if the array is null.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `#string.join(\{'Administrator', 'User', 'Guest'}, ', ')`                                                                                                                                                    | `Administrator, User, Guest`                                     |
| `int indexOf(String <input>, String <searchStr>, int <fromIndex>)`where:- `<input>` is the string to search against

- `<searchStr>` is the string to find

- `<fromIndex>` is the start position in the input string to start the search from                                                                                                                                                      | Finds the first index of the search string within the input string. A negative start position is treated as zero, and a start position greater than the input string length only matches an empty search. An empty search string (`""`) always matches. Returns `-1` if a match is not found.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `#string.indexOf('To find and return index or return -1', 'return', -1)`                                                                                                                                     | `12`                                                             |
| `int lastIndexOf(String <input>, String <searchStr>, int <fromIndex>)`where:- `<input>` is the string to search against

- `<searchStr>` is the string to find

- `<fromIndex>` is the start position in the input string to begin the search from                                                                                                                                                  | Finds the last index within the input string. Search starts from the start position and continues backwards. A negative start position is treated as zero, and a start position greater than the input string length searches the entire string backwards. Returns `-1` if a match is not found.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `#string.lastIndexOf('To find and return index or return -1', 'return', 50)`                                                                                                                                 | `28`                                                             |
| `int length(String <input>)`where `<input>` is the string to find the length of.                                                                                                                                                                                                                                                                                                                    | Returns the length of the input string or `0` if *input* is null.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `#string.length('Input')`                                                                                                                                                                                    | `5`                                                              |
| `String replace(String <input>, String <searchStr>, String <replacement>, int <max>)`where:- `<input>` is the string to be searched against to be replaced in.

- `<searchStr>` is the string to be matched and replaced.

- `<replacement>` is the string to be replaced with.

- `<max>` is the maximum number of times replacement should be done. If `-1`, all matched values will be replaced. | Replaces all occurrences of `searchStr` within `input` according to the `replacement` and `max` values. A null reference passed to this method is a no-op.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `#string.replace('input values replaced by input replacement', 'in', 'out', -1)`                                                                                                                             | `output values replaced by output replacement`                   |
| `int compare(String <str1>, String <str2>, boolean <ignoreCase>)`where:- `<str1>` is the string to compare against

- `<str2>` is the string to compare

- `<ignoreCase>` determines whether the comparison is case-sensitive.                                                                                                                                                                      | Compares two strings lexicographically. Returns `0` if `str1` is equal to `str2` or both are null. Returns a negative number if `str1` is less than `str2`. Returns a positive number if `str1` is greater than `str2`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `#string.compare('Input', 'INPUT', true)`                                                                                                                                                                    | `0`                                                              |
| `Number asInt(String <input>, Number <defaultIfNullOrInvalid>)`where:- `<input>` is the string representation of an integer number

- `<defaultIfNullOrInvalid>` is the default value to be used if the string input is null, not a valid number, or out of range for integers                                                                                                                      | Parses the string argument as a signed decimal integer (min `-2147483648` and max `2147483647`).The characters in the string must all be decimal digits, except that the first character can be an ASCII minus sign (`-`) to indicate a negative value or an ASCII plus sign (`+`) to indicate a positive value. If input is null or not a valid integer, `defaultIfNullOrInvalid` is returned.                                                                                                                                                                                                                                                                                                                                                                   | 1. `#string.asInt('12', 0)`

2. `#string.asInt('NaN', 0)`

3. `#string.asInt('9876543210123456789', 0)`                                                                                                      | 1) `12`

2) `0`

3) `0`                                          |
| `Number asLong(String <input>, Number <defaultIfNullOrInvalid>)`where:- *\<input>* is the string representation of a Long number

- *\<defaultIfNullOrInvalid>* is the default value to be used if string input is null, not a valid number, or out of range for Longs                                                                                                                              | Parses the string argument as a signed decimal long (min `-9223372036854775808` and max `9223372036854775807`).The characters in the string must all be decimal digits, except that the first character can be an ASCII minus sign (`-`) to indicate a negative value or an ASCII plus sign (`+`) to indicate a positive value. If input is null or not a valid Long, `defaultIfNullOrInvalid` is returned.                                                                                                                                                                                                                                                                                                                                                       | 1. `#string.asLong('12', 0)`

2. `#string.asLong('NaN', 0)`

3. `#string.asLong('9876543210123456789', 0)`                                                                                                   | 1) `12`

2) `0`

3) `0`                                          |
| `Number asBigInt(String <input>, Number <defaultIfNullOrInvalid>)`where:- *\<input>* is the string representation of a BigInteger number

- *\<defaultIfNullOrInvalid>* is the default value to be used if string input is null, not a valid number, or out of range for BigInteger                                                                                                                 | Translates the decimal string representation of a BigInteger into a BigInteger.The string representation consists of an optional minus sign followed by a sequence of one or more decimal digits. The character-to-digit mapping is provided by Character.digit. If input is null or not a valid Big Integer, `defaultIfNullOrInvalid` is returned.                                                                                                                                                                                                                                                                                                                                                                                                               | 1. `#string.asBigInt('1234567890987654321', 0)`

2. `#string.asBigInt('NaN', 0)`                                                                                                                             | 1) `1234567890987654321`

2) `0`                                 |
| `Number asFloat(String <input>, Number <defaultIfNullOrInvalid>)`where:- *\<input>* is the string representation of a Float number

- *\<defaultIfNullOrInvalid>* is the default value to be used if string input is null, not a valid number, or out of range for Floats                                                                                                                           | Parses the string argument as a signed decimal float. If input is null, not a valid Float, or Infinity, `defaultIfNullOrInvalid` is returned.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 1. `#string.asFloat('12.5', 0)`

2. `#string.asFloat('NaN', 0)`

3. `#string.asFloat('1234567899876543210123456789987654321019.12', 0)`                                                                      | 1) `12.5`

2) `0`

3) `0`                                        |
| `Number asDouble(String <input>, Number <defaultIfNullOrInvalid>)`where:- *\<input>* is the string representation of a Double number

- *\<defaultIfNullOrInvalid>* is the default value to be used if string input is null, not a valid number, or out of range for doubles                                                                                                                        | Parses the string argument as a signed decimal double. If input is null, not a valid number within the range of Double, or Infinity, `defaultIfNullOrInvalid` is returned.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 1. `#string.asDouble('1234567899876543210123456789987654321019.12', 0)`

2. `#string.asDouble('NaN', 0)`                                                                                                     | 1) `1234567899876543210123456789987654321019.12`

2) `0`         |
| `Number asBigDecimal(String <input>, Number <defaultIfNullOrInvalid>)`where:- *\<input>* is the string representation of a BigDecimal number

- *\<defaultIfNullOrInvalid>* is the default value to be used if string input is null, not a valid number, or out of range for BigDecimal                                                                                                             | Translates the string representation of a BigDecimal into a BigDecimal.The string representation consists of an optional sign, (`+` or `-`), followed by a sequence of zero or more decimal digits (the integer), optionally followed by a fraction, optionally followed by an exponent. The fraction consists of a decimal point followed by zero or more decimal digits. The string must contain at least one digit in either the integer or the fraction. The exponent consists of the character `e` or `E` followed by one or more decimal digits.The value of the exponent must lie between `-Integer.MAX_VALUE (Integer.MIN_VALUE+1)` and `Integer.MAX_VALUE`, inclusive. If input is null or not a valid BigDecimal, `defaultIfNullOrInvalid` is returned. | 1. `#string.asBigDecimal('1234567890987654321.14', 0)`

2. `#string.asBigDecimal('NaN', 0)`                                                                                                                  | 1) `1234567890987654321.14`

2) `0`                              |
| `String asBase64Encoded(String <input>)`where *\<input>* is the string to be encoded.                                                                                                                                                                                                                                                                                                               | Encodes the input string into a new string using the Base64 encoding scheme. Returns the encoded string if input is not empty, or else input is returned as-is.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `#string.asBase64Encoded('Test Value for encoding')`                                                                                                                                                         | `VGVzdCBWYWx1ZSBmb3IgZW5jb2Rpbmc=`                               |
| `String asBase64Decoded(String <input>)`where *\<input>* is the Base64 encoded string to be decoded.                                                                                                                                                                                                                                                                                                | Decodes a Base64 encoded string into a new string using the Base64 encoding scheme. Returns the encoded string if input is not empty, or else input is returned as-is. This will return null if the input string is not in the valid Base64 schema.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `#string.asBase64Decoded('VGVzdCBWYWx1ZSBmb3IgZW5jb2Rpbmc=')`                                                                                                                                                | `Test Value for encoding`                                        |
| `String asUrlEncoded(String <input>)`where *\<input>* is the string to be encoded.                                                                                                                                                                                                                                                                                                                  | Translates a string into application/x-www-form-urlencoded format using UTF-8 encoding scheme. Returns the encoded string if input is not empty, or else input is returned as-is.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `#string.asUrlEncoded('username=johndoe+admin')`                                                                                                                                                             | `username%3Djohndoe%2Badmin`                                     |
| `String asUrlDecoded(String <input>)`where *\<input>* is the URL encoded string to be decoded.                                                                                                                                                                                                                                                                                                      | Decodes an application/x-www-form-urlencoded string using UTF-8 encoding scheme. Returns the decoded string if input is not empty, or else input is returned as it is. Returns null if the input string cannot be decoded due to any illegal characters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `#string.asUrlDecoded('username%3Djohndoe%2Badmin')`                                                                                                                                                         | `username=johndoe+admin`                                         |
| `String format(String <format>, String…​ <args>)`where:- *\<format>* is the format supported by java.util.Formatter

- *\<args>* are the arguments referenced by the format specifiers in the format string. If there are more arguments than format specifiers, the extra arguments are ignored. The number of arguments is variable and can be zero                                               | Returns a formatted string using the specified format string and arguments. Returns null if a format string contains an illegal syntax, a format specifier that is incompatible with the given arguments, insufficient arguments given the format string, or other illegal conditions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 1. `#string.format('UserId: %s, Full Name: %s, %s', 'johndoe','John', 'Doe')`

2. `#string.format('Hex for 10 is %X', 10)`                                                                                   | 1) `UserId: johndoe, Full Name: John, Doe`

2) `Hex for 10 is A` |
| `String uuidAsBase64Guid(String <input>, String <defaultIfNullOrInvalid>)`where:- *\<input>* is a string representation of a UUID. Invalid if not compatible with regex `/[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}/`

- *\<defaultIfNullOrInvalid>* is the default value to be used if input is null or not a valid UUID                                         | Translates the string representation of a UUID to a GUID in Base64 format. If input is null or not a valid UUID, *\<defaultIfNullOrInvalid>* is returned.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 1. `#string.uuidAsBase64Guid('7754d487-1fc3-4206-9e95-ce012f1586e5', null)`

2. `#string.uuidAsBase64Guid('invalid', 'lZkqAJgEv0ueGKboT/JFVg==')`                                                            | 1) `h9RUd8MfBkKelc4BLxWG5Q==`

2) `lZkqAJgEv0ueGKboT/JFVg==`     |
| `String firstNonEmpty(String <value1>, String…​ <value2…​10>)`where:- *\<value1>* is the input value to test. Can be null or empty

- *\<value2…​10>* are additional and optional input values to test. Can be null or empty                                                                                                                                                                        | Returns the first value in the input values which is not empty ('') or null. If all input values are null or empty, then null is returned. There must be at least one input value and the rest are optional. You can enter a maximum of 10 input values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 1. `#string.firstNonEmpty(null, '', 'firstNonEmpty', 'secondNonEmpty')`

2. `#string.firstNonEmpty('', '')`                                                                                                  | 1) `firstNonEmpty`

2) `null`                                    |
| `String firstNonBlank(String <value1>, String…​ <value2…​10>)`where:- *\<value1>* is the input value to test. Can be null, empty or blank.

- *\<value2…​10>* are additional and optional input values to test. Can be null, empty or blank                                                                                                                                                         | Returns the first value in the input values which is not empty (''), null or whitespace only. If all input values are null, empty or blank then null is returned. There must be at least one input value and the rest are optional. You can enter a maximum of 10 input values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 1. `#string.firstNonBlank(null, '', ' ', 'firstNonEmpty', 'secondNonEmpty')`

2. `#string.firstNonBlank('', ' ', '')`                                                                                        | 1) `firstNonEmpty`

2) `null`                                    |

## Date and time library

You can parse, format, and process the date and time within an expression. Dates use the ISO 8601 format in UTC.

Examples of valid dates:

* 2023-01-01T23:59:59Z

* 2023-01-01T23:59:59.123Z

* 2023-01-01T23:59:59.123456Z

* 2023-01-01T23:59:59+800

Default output formats are in UTC:

* 2023-01-01T23:59:59.001Z

* 2023-01-01Z

* 23:59:59Z

|   |                                                                                                                                                                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you input the ISO 8601 format incorrectly, the system returns `null`.This library accepts DateTime with millisecond precision greater than 3, but the output always truncates to millisecond precision of 3.Additional input formats not documented above are not officially supported and subject to change without notice. |

| String                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Input                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Output                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `String addDays(String <inputDate>, int <days>)`where:- `<inputDate>` is the date in a supported ISO 8601 format.

- `<days>` is the number of days to add. Can be negative to decrement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Adds a number of days to the date represented by a supported ISO 8601 string representation and returns the new date in the default ISO 8601 output format. Returns `null` if `inputDate` is null, empty, blank, not a supported ISO 8601 format, or has an invalid date range or values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | 1. `#datetime.addDays('2021-01-31T01:01:01Z', 1)`

2. `#datetime.addDays('2021-03-01Z', -1)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 1) `2021-02-01T01:01:01.000Z`

2) `2021-02-28T00:00:00.000Z`                                                               |
| `String addMonths(String <inputDate>, int <months>)`where:- `<inputDate>` is the date in a supported ISO 8601 format.

- `<months>` is the number of months to add. Can be negative to decrement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Adds a number of months to the date represented by a supported ISO 8601 string representation and returns the new date in the default ISO 8601 output format. Returns `null` if `inputDate` is null, empty, blank, not a supported ISO 8601 format, or has an invalid date range or values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 1. `#datetime.addMonths('2020-12-31T01:01:01.001Z', 2)`

2. `#datetime.addMonths('2021-02-28T01:01:01Z', -1)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 1) `2021-02-28T01:01:01.001Z`

2) `2021-01-28T01:01:01.000Z`                                                               |
| `String addYears(String <inputDate>, int <years>)`where:- `<inputDate>` is the date in a supported ISO 8601 format.

- `<years>` is the number of years to add. Can be negative to decrement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Adds a number of years to the date represented by a supported ISO 8601 string representation and returns the new date in the default ISO 8601 output format. Returns `null` if `inputDate` is null, empty, blank, not a supported ISO 8601 format, or has invalid date range or values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `#datetime.addYears('2021-01-31T01:01:01Z', 1)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `2022-01-31T01:01:01.000Z`                                                                                                 |
| `String addHours(String <inputDate>, int <hours>)`where:- `<inputDate>` is the date in a supported ISO 8601 format.

- `<hours>` is the number of hours to add. Can be negative to decrement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Adds a number of hours to the date represented by a supported ISO 8601 string representation and returns the new date in the default ISO 8601 output format. Returns `null` if `inputDate` is null, empty, blank, not a supported ISO 8601 format, or has an invalid date range or values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `#datetime.addHours('2020-12-31T23:59:59.001Z', 3)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `2021-01-01T02:59:59.001Z`                                                                                                 |
| `String addMinutes(String <inputDate>, int <minutes>)`where:- `<inputDate>` is the date in a supported ISO 8601 format.

- `<minutes>` is the number of minutes to add. Can be negative to decrement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Adds a number of minutes to the date represented by a supported ISO 8601 string representation and returns the new date in the default ISO 8601 output format. Returns `null` if `inputDate` is null, empty, blank, not a supported ISO 8601 format, or has an invalid date range or values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `#datetime.addMinutes('2021-01-31T23:59:59Z', 10)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `2021-02-01T00:09:59.000Z`                                                                                                 |
| `String addSeconds(String <inputDate>, int <seconds>)`where:- `<inputDate>` is the date in a supported ISO 8601 format.

- `<seconds>` is the number of seconds to add. Can be negative to decrement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Adds a number of seconds to the date represented by a supported ISO 8601 string representation and returns the new date in the default ISO 8601 output format. Returns `null` if `inputDate` is null, empty, blank, not a supported ISO 8601 format or has invalid date range or values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `#datetime.addSeconds('2021-02-28Z', 1)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `2021-02-28T00:00:01.000Z`                                                                                                 |
| `int getDayOfMonth(String <inputDate>)`where `<inputDate>` is the date in a supported ISO 8601 format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Returns day-of-month, a value from `1` to `31` for valid input or `-1` if `inputDate` is null, empty, blank, not a supported ISO 8601 format, or has an invalid date range or values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `#datetime.getDayOfMonth('2021-01-31T23:59:59Z')`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `31`                                                                                                                       |
| `int getMonth(String <inputDate>)`where `<inputDate>` is the date in a supported ISO 8601 format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Returns the month from `1` to `12` for valid input or `-1` if `inputDate` is null, empty, blank, not a supported ISO 8601 format, or has an invalid date range or values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `#datetime.getMonth('2021-02-28Z')`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `2`                                                                                                                        |
| `int getYear(String <inputDate>)`where `<inputDate>` is the date in a supported ISO 8601 format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Returns value for the year for valid input or `-1` if `inputDate` is null, empty, blank, not a supported ISO 8601 format, or has an invalid date range or values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `#datetime.getYear('2021-01-31T23:59:59Z')`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `2021`                                                                                                                     |
| `int getHour(String <inputDate>)`where `<inputDate>` is the date in a supported ISO 8601 format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Returns the hour of the day as a value between `0` and `23` for valid input or `-1` if `inputDate` is null, empty, blank, not a supported ISO 8601 format, or has an invalid date range or values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `#datetime.getHour('2021-01-31T23:59:59Z')`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `23`                                                                                                                       |
| `int getMinute(String <inputDate>)`where `<inputDate>` is the date in a supported ISO 8601 format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Returns the minute of the hour as a value between `0` to `59` for valid input or `-1` if `inputDate` is null, empty, blank, not a supported ISO 8601 format, or has an invalid date range or values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `#datetime.getMinute('2021-01-31T23:59:59Z')`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `59`                                                                                                                       |
| `int getSecond(String <inputDate>)`where `<inputDate>` is the date is ISO 8601 format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Returns the second of the minute as a value between `0` to `59` for valid input or `-1` if `inputDate` is null, empty, blank, not a supported ISO 8601 format, or has an invalid date range or values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `#datetime.getSecond('2020-12-30T23:59:59.001Z')`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `59`                                                                                                                       |
| `String now()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Obtains the current date-time in default ISO 8601 output format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `#datetime.now()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *\<Current date and time in default ISO 8601 format>*                                                                      |
| `String toDateTime(int <year>, int <month>, int <dayOfMonth>, int <hour>, int <minute>, int <second>)`where:- `<year>` is the year to represent

- `<month>` is the month-of-year to represent, from `1` (January) to `12` (December)

- `<dayOfMonth>` is the day-of-month to represent, from `1` to `31`

- `<hour>` is the hour-of-day to represent, from `0` to `23`

- `<minute>` is the minute-of-hour to represent, from `0` to `59`

- `<second>` is the second-of-minute to represent, from `0` to `59`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Obtains the date and time from the provided year, month, day, hour, minute, and second and returns valid date and time in default ISO 8601 output format.Returns `null` if the value for any field is incorrect or out of range, such as day-of-month being invalid for the provided month or year.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `#datetime.toDateTime(2021, 1, 31, 10, 15, 0)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `2021-01-31T10:15:00.000Z`                                                                                                 |
| `String toDate(String <inputDate>)`where `<inputDate>` is the date in a supported ISO 8601 format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Transforms the date and time in a supported ISO 8601 format to a UTC date in the format `yyyy-MM-ddX`. Returns `null` if `inputDate` is null, empty, blank, not a supported ISO 8601 format, or has an invalid date range or values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `#datetime.toDate('2021-02-28Z')`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `2021-02-28Z`                                                                                                              |
| `String toTime(String <inputDate>)`where `<inputDate>` is the date in a supported ISO 8601 format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Transforms the date and time in a supported ISO 8601 format to a UTC time in the format `HH:mm:ss[.SSS]X`. Returns `null` if `inputDate` is null, empty, blank, not a supported ISO 8601 format, or has an invalid date range or values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `#datetime.toTime('2021-01-31T23:59:59Z')`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `23:59:59Z`                                                                                                                |
| `String format(String <inputDate>, String <pattern>)`where:- `<inputDate>` is the date in a supported ISO 8601 format.

- `<pattern>` is a valid pattern supported by Java 8 DateTimeFormatter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Transforms the date and time in a supported ISO 8601 format to the date and time in the specified format. Returns `null` if the input `dateTime` or format is not valid. For more information, see the available formats in the Reference section. Returns `null` if `inputDate` is null, empty, blank, not a supported ISO 8601 format, has invalid date range or values, or if pattern is null or invalid.                                                                                                                                                                                                                                                                                                                                                                                                                            | 1. `#datetime.format('2021-01-01T09:15:00Z', 'EEEE, dd MMMM; h:mm a')`

2. `#datetime.format('2021-02-28Z', "QQQQ 'of year' yyyy")`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 1) `Friday, 01 January; 9:15 AM`

2) `1st quarter of year 2021`                                                            |
| `int compare(String <inputDateTime1>, String <inputDateTime2>)`where:- `<inputDateTime1>` is the primary date-time in a supported ISO 8601 format to compare with

- `<inputDateTime2>` is the other date-time in a supported ISO 8601 format to compare to&#xA;&#xA;Both values are treated as null if null, empty, blank, or not a supported ISO 8601 format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Compares this date and time to another date and time, including the chronology. Returns `0` if they are the same, a negative number if the former date is earlier, and a positive number if the former date is later.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 1. `#datetime.compare('2021-01-01T00:00:00Z', '2021-01-01T00:00:00Z')`

2. `#datetime.compare('2021-01-01T00:00:01Z', '2021-01-01T00:00:00Z')`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 1) `0`

2) `1`                                                                                                             |
| `Number daysBetween(String <inputDateTime1>, String <inputDateTime2>, Number <defaultIfNotDate>)`where:- *\<inputDateTime1>* is the primary date-time in a supported ISO 8601 format to compare with

- *\<inputDateTime2>* is the other date-time in a supported ISO 8601 format to compare to

- *\<defaultIfNotDate>* is the default value to return if either of the input date-time are null, empty, blank or not a supported ISO 8601 format&#xA;&#xA;\<inputDateTime1> and \<inputDateTime2> are treated as null if null, empty, blank, or not a supported ISO 8601 format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Calculates the number of days between input dates. The result is negative if *\<inputDateTime2>* is before *\<inputDateTime1>*. If either of the input date-time are null, empty, blank or not a supported ISO 8601 format, the value provided for *\<defaultIfNotDate>* is returned.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 1. `#datetime.daysBetween('2021-01-01T00:00:00Z', '2021-01-01T08:45:00Z', -1)`

2. `#datetime.daysBetween('2021-01-01T00:00:01Z', '2021-01-03T10:30:00Z', -1)`

3. `#datetime.daysBetween('2021-01-03T00:00:01Z', '2021-01-01T10:30:00Z', -1)`                                                                                                                                                                                                                                                                                                                                                                                                                       | 1) `0`

2) `2`

3) `-2`                                                                                                    |
| `Number weeksBetween(String <inputDateTime1>, String <inputDateTime2>, Number <defaultIfNotDate>)`where:- *\<inputDateTime1>* is the primary date-time in a supported ISO 8601 format to compare with

- *\<inputDateTime2>* is the other date-time in a supported ISO 8601 format to compare to

- *\<defaultIfNotDate>* is the default value to return if either of the input date-time are null, empty, blank, or not a supported ISO 8601 format&#xA;&#xA;\<inputDateTime1> and \<inputDateTime2> are treated as null if null, empty, blank, or not a supported ISO 8601 format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Calculates the number of weeks between input dates. The result is negative if *\<inputDateTime2>* is before *\<inputDateTime1>*. If either of the input date-time are null, empty, blank or not a supported ISO 8601 format, the value provided for *\<defaultIfNotDate>* is returned.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 1. `#datetime.weeksBetween('2021-01-01T00:00:00Z', '2021-01-01T08:45:00Z', -1)`

2. `#datetime.weeksBetween('2021-01-01T00:00:01Z', '2021-01-15T10:30:00Z', -1)`

3. `#datetime.weeksBetween('2021-01-15T00:00:01Z', '2021-01-01T10:30:00Z', -1)`                                                                                                                                                                                                                                                                                                                                                                                                                    | 1) `0`

2) `2`

3) `-2`                                                                                                    |
| `Number monthsBetween(String <inputDateTime1>, String <inputDateTime2>, Number <defaultIfNotDate>)`where:- *\<inputDateTime1>* is the primary date-time in a supported ISO 8601 format to compare with

- *\<inputDateTime2>* is the other date-time in a supported ISO 8601 format to compare to

- *\<defaultIfNotDate>* is the default value to return if either of the input date-time are null, empty, blank, or not a supported ISO 8601 format&#xA;&#xA;\<inputDateTime1> and \<inputDateTime2> are treated as null if null, empty, blank, or not a supported ISO 8601 format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Calculates the number of months between input dates. The result is negative if *\<inputDateTime2>* is before *\<inputDateTime1>*. If either of the input date-time are null, empty, blank or not a supported ISO 8601 format, the value provided for *\<defaultIfNotDate>* is returned.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 1. `#datetime.monthsBetween('2021-01-01T00:00:00Z', '2021-01-01T08:45:00Z', -1)`

2. `#datetime.monthsBetween('2021-01-01T00:00:01Z', '2021-02-01T10:30:00Z', -1)`

3. `#datetime.monthsBetween('2021-02-01T00:00:01Z', '2021-03-01T10:30:00Z', -1)`                                                                                                                                                                                                                                                                                                                                                                                                                 | 1) `0`

2) `1`

3) `1`                                                                                                     |
| `Number yearsBetween(String <inputDateTime1>, String <inputDateTime2>, Number <defaultIfNotDate>)`where:- *\<inputDateTime1>* is the primary date-time in a supported ISO 8601 format to compare with

- *\<inputDateTime2>* is the other date-time in a supported ISO 8601 format to compare to

- *\<defaultIfNotDate>* is the default value to return if either of the input date-time are null, empty, blank, or not a supported ISO 8601 format&#xA;&#xA;\<inputDateTime1> and \<inputDateTime2> are treated as null if null, empty, blank, or not a supported ISO 8601 format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Calculates the number of years between input dates. The result is negative if *\<inputDateTime2>* is before *\<inputDateTime1>*. If either of the input date-time are null, empty, blank or not a supported ISO 8601 format, the value provided for *\<defaultIfNotDate>* is returned.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 1. `#datetime.yearsBetween('2021-01-01T00:00:00Z', '2021-01-01T08:45:00Z', -1)`

2. `#datetime.yearsBetween('2021-01-01T00:00:01Z', '2022-01-01T10:30:00Z', -1)`

3. `#datetime.yearsBetween('2022-01-01T00:00:01Z', '2021-01-01T10:30:00Z', -1)`                                                                                                                                                                                                                                                                                                                                                                                                                    | 1) `0`

2) `1`

3) `-1`                                                                                                    |
| `String periodBetween(String <inputDateTime1>, String <inputDateTime2>, String <defaultIfNotDate>)`where:- *\<inputDateTime1>* is the primary date-time in a supported ISO 8601 format to compare with. The value is inclusive.

- *\<inputDateTime2>* is the other date-time in a supported ISO 8601 format to compare to. The value is exclusive.

- *\<defaultIfNotDate>* is the default value to return if either of the input date-time are null, empty, blank, or not a supported ISO 8601 format.&#xA;&#xA;\<inputDateTime1> and \<inputDateTime2> are treated as null if null, empty, blank, or not a supported ISO 8601 format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Calculates the period between input dates represented as amount of time in years, months, and days using ISO 8601 period format `P[nY][nM][nD]`.The letter `P` starts the period, `n`] is an integer representing the number of years, months, and days, represented by `Y`, `M`, and `D`, respectively.A zero period is represented as zero days, or `P0D`. The result is negative if *\<inputDateTime2>* is before *\<inputDateTime1>*. If either of the input date-time is null, empty, blank or not a supported ISO 8601 format, the value provided for *\<defaultIfNotDate>* is returned.The period is calculated by removing complete months, then calculating the remaining number of days, adjusting to ensure that both have the same sign. The number of months is then split into years and months based on a 12 month year. | 1. `#datetime.periodBetween('2021-01-01T00:00:00Z', '2021-01-01T00:00:00Z', -1)`

2. `#datetime.periodBetween('2021-01-01Z', '2022-02-11Z', -1)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 1) `P0D`

2) `P1Y1M10D`                                                                                                    |
| `String toUnixTimestamp(String <inputDateTime>)`where *\<inputDateTime>* is the date-time in a supported ISO 8601 format.&#xA;&#xA;\<inputDateTime> is treated as null if null, empty, blank, or not a supported ISO 8601 format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Transforms the date-time in a supported ISO 8601 format to the number of seconds from the epoch of 1970-01-01T00:00:00Z. This returns null if *\<inputDateTime>* is null, empty, blank, or not a supported ISO 8601 format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 1. `#datetime.toUnixTimestamp('2020-12-31Z')`

2. `#datetime.toUnixTimestamp('2020-12-31T23:59:59Z')`

3. `#datetime.toUnixTimestamp('2020-12-31T23:59:59.001Z')`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 1) `1609372800`

2) `1609459199`

3) `1609459199`                                                                          |
| `String fromUnixTimestamp(Number <epochSeconds>)`where *\<epochSeconds>* is the number of seconds from the epoch of 1970-01-01T00:00:00Z.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Builds date-time using the number of seconds from the epoch of 1970-01-01T00:00:00Z to a UTC date-time in default ISO 8601 format. Returns null if *\<epochSeconds>* is null.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `#datetime.fromUnixTimestamp(1609459199)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `2020-12-31T23:59:59.000Z`                                                                                                 |
| `String parse(String <inputDateTime>, String <format>, Object <options>)`where:- *\<inputDateTime>* is the date with or without time to parse in a format other than ISO 8601

- *\<format>* is the custom format supported by Java DateTimeFormatter used for the specified *\<inputDateTime>*

- *\<options>* is an optional JSON object with default values for allowed date-time fields which cannot be obtained from the *\<inputDateTime>* format. Supported fields are `zoneid` - if *\<inputDateTime>* doesn't contain any zone information, users can configure the `zoneid` to be used in the input options JSON, or else UTC will be used.&#xA;&#xA;\<inputDateTime> is treated as null if null, empty, blank, or not a supported ISO 8601 format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Parses *\<inputDateTime>* in a format other than ISO 8601 as specified by *\<format>*, and uses any default values specified in *\<options>* if required to transform it to a date-time in ISO 8601 format.Will return null if *\<inputDateTime>*:- Is null

- Is not in a valid format

- Cannot be transformed to ISO 8601 if it lacks any required fields such as day, month, or year

- Any of those fields are out of range                                                                                                                                                                                                                                                                                                                                                                                                        | * Parsing date with format yyyy-MM-dd without zone information which uses UTC as default zone

  `#datetime.parse('2022-01-01', 'yyyy-MM-dd', null)`

* Parsing date with format yyyy-MM-dd without zone information but with zone defaults configured using options

  `#datetime.parse('2022-01-01', 'yyyy-MM-dd', \{'zoneid': 'America/Vancouver'})`

* Parsing date with format yyyy-MM-dd z with zone information

  `#datetime.parse('2022-01-01 PST', 'yyyy-MM-dd z', null)`

* Parsing date with format dd/MM/yyyy HH:mm:ss without zone information which uses UTC as default zone

  `#datetime.parse('03/12/2021 09:30:45', 'dd/MM/yyyy HH:mm:ss', null)` | 1. `2022-01-01T00:00:00.000Z`

2. `2022-01-01T08:00:00.000Z`

3. `2022-01-01T08:00:00.000Z`

4. `2021-12-03T09:30:45.000Z` |
| `String toDateTimeInTimezone(String <inputDateTime>, String <timezone>, String <pattern>)`where:- *\<inputDateTime>* is the date in a supported ISO 8601 format.

- *\<timezone>* is a valid zone ID supported by Java 8. Parsing matches the zone ID as follows:

  1. If the zone ID equals `Z`, the result is UTC.

  2. If the zone ID consists of a single letter, the zone ID is invalid.

  3. If the zone ID equals `GMT`, `UTC`, or `UT`, then the result is a timezone with the same ID and rules equivalent to UTC.Zone IDs must match regular expression characters. If the zone ID is not in the Java 8 configured set of IDs, it is invalid. The detailed format of the region ID depends on the group supplying the data. The default set of data is supplied by the IANA Time Zone Database (TZDB).IANA TZDB has region IDs of the form *\<area>*/*\<city>*, such as `Europe/Paris` or `America/New_York`. This is compatible with most IDs from Time Zone. \* *\<pattern>* is a pattern supported by Java 8 DateTimeFormatter. For available formats, see the [References](p1_expressionlang_references.html) section.&#xA;&#xA;\<inputDateTime> is treated as null if null, empty, blank, or not a supported ISO 8601 format. | Transforms the date-time in a supported ISO 8601 format to date-time in the specified timezone in the required format if specified, or the default format `yyyy-MM-dd'T'HH:mm:ss[.SSS]Z`.Will return null if:- *\<inputDateTime>* is null, empty, or blank

- *\<inputDateTime>* is not a supported ISO 8601 format, or has invalid dates or values

- *\<timezone>* or *\<pattern>* are null or invalid                                                                                                                                                                                                                                                                                                                                                                                                                                | * Change time zone to America/Vancouver with default pattern

  `#datetime.toDateTimeInTimezone('2023-01-01T04:30:30.000Z', 'America/Vancouver', null)`

* Change time zone to +100 with default pattern

  `#datetime.toDateTimeInTimezone('2023-01-01T04:30:30Z', '+0100', null)`

* Change time zone to America/Vancouver with custom pattern

  `#datetime.toDateTimeInTimezone('2023-01-01T04:30:30.123Z', 'America/Vancouver', 'dd-MM-YYYY hh:mm a')`                                                                                                                                                                                                          | 1. `2022-12-31T20:30:30-0800`

2. `2023-01-01T05:30:30.000+0100`

3. `31-12-2022 08:30 PM`                                 |

## Data library

You can process data in arrays and collections using the following library.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When using a collection format, some of the following methods which perform operations between two arrays or collections determine data type automatically based on Java defaults. For example, `3` is treated as integer, `3.5` as a double and `c` as a string. However, array comparison is based on the array data types.`#data.containsAll(new int[] {2,4,6,8,10}, new int[] {2,8})` returns as true because both are int arrays.`#data.containsAll(new int[] {2,4,6,8,10}, {2,8})` returns as true because the first argument is an int array and the second argument uses int by default.`#data.containsAll(new float[] {2.1,4.1,6.1,8.1,10.1}, {2.1,8.1})` returns as false because the first argument is a float array and the second argument is a double, which is the default for floating point numbers.`#data.containsAll(new double[] {2.1,4.1,6.1,8.1,10.1}, {2.1,8.1})` returns as true because the first argument is a double array and the second argument is treated as a double by default.`#data.containsAll({2.1,4.1,6.1,8.1,10.1}, {2.1,8.1})` returns as true because both arguments are collections and use the default data types. |

| String                                                                                                                                                                                                                    | Description                                                                                                                                                   | Input                                                                                                                                                                                                                                                                                                              | Output                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------- |
| `int indexOf(Array <srcArray>, <valueToFind>)`where:- `<srcArray>` is the array to search through

- `<valueToFind>` is the value to find.                                                                                | Finds and returns the index of the `valueToFind` in the input array. Returns `-1` if not found or if `srcArray` is null.                                      | 1. `#data.indexOf(new int[] {2,4,6,8,10}, 6)`

2. `#data.indexOf({'This', 'is', 'String', 'collection'}, 'is')`                                                                                                                                                                                                    | 1) `2`

2) `1`                                          |
| `boolean isNotEmpty(Array <srcArray>)`where `<srcArray>` is the array to check.                                                                                                                                           | Checks if the input array is not empty and not null.                                                                                                          | 1. `#data.isNotEmpty(new int[] {2,4,6,8,10})`

2. `#data.isNotEmpty({'This', 'is', 'String', 'collection'})`                                                                                                                                                                                                       | 1) `true`

2) `true`                                    |
| `boolean containsAll(Array <srcData>, Array <searchData>)`where `<searchData>` is the array of values to be searched for in the `<srcData>` array.                                                                        | Returns true if all elements of `searchData` are contained in `srcData`.                                                                                      | 1. `#data.containsAll(new int[] {2,4,6,8,10}, new int[] {2,8})`

2. `#data.containsAll(new int[] {2,4,6,8,10}, {2,8})`

3. `#data.containsAll({2,4,6,8,10}, {2,9})`

4. `#data.containsAll(new float[] {2.1,4.1,6.1,8.1,10.1}, {2.1,8.1})`

5. `#data.containsAll(new double[] {2.1,4.1,6.1,8.1,10.1}, {2.1,8.1})` | 1) `true`

2) `true`

3) `false`

4) `false`

5) `true` |
| `boolean containsAny(Array <srcData>, Array <searchData>)`where `<searchData>` is the array of values to be searched for in the `<srcData>` array.                                                                        | Returns `true` if there is at least one common element in both arrays.                                                                                        | 1. `#data.containsAny({2,4,6,8,10}, {2,9,11})`

2. `#data.containsAny(new int[] {2,4,6,8,10}, {2,9,11})`

3. `#data.containsAny({2,4,6,8,10}, new int[] {1,9})`                                                                                                                                                    | 1) `true`

2) `true`

3) `false`                        |
| `Array removeAll(Array <srcData>, Array <dataToRemove>)`where `<dataToRemove>` is the array of values to be removed from the `<srcData>` array.                                                                           | Removes the elements in `dataToRemove` from `srcData` and returns a new array.                                                                                | 1. `#data.removeAll(new int[] {2,4,6,8,10}, new int[] {2,6,11})`

2. `#data.removeAll({2,4,6,8,10}, {2,6,11})`                                                                                                                                                                                                     | 1) `[4,8,10]`

2) `[4,8,10]`                            |
| `Array retainAll(Array <srcData>, Array <dataToRetain>)`where:- *\<srcData>* is the array from which values are to be removed

- `<dataToRetain>` is the array of values to be retained if they also exist in `<srcData>` | Retains only the elements that exist in both `srcData` and `dataToRetain`.                                                                                    | 1. `#data.retainAll(new int[] {2,4,6,8,10}, new int[] {2,6,11})`

2. `#data.retainAll({2,4,6,8,10}, new int[] {2,6,11})`                                                                                                                                                                                           | 1) `[2,6]`

2) `[2,6]`                                  |
| `Array union(Array <array1>, Array <array2>)`where:- `<array1>` is the first array to which elements will be added to

- `<array2>` is the second array whose elements will be appended to first array.                   | Returns a new array containing the second array appended to the first array.                                                                                  | 1. `#data.union(new int[] {2,4,6,8,10}, new int[] {1,10,11})`

2. `#data.union(new int[] {2,4,6,8,10}, {1,10,11})`                                                                                                                                                                                                 | 1) `[2,4,6,8,10,1,10,11]`

2) `[2,4,6,8,10,1,10,11]`    |
| `int size(Array <inputArray>)`where `<inputArray>` is the array for which the size is determined.                                                                                                                         | Returns the size of the input array.                                                                                                                          | 1. `#data.size(new int[] {2,4,6,8,10})`

2. `#data.size({2,4,6,8,10})`                                                                                                                                                                                                                                             | 1) `5`

2) `5`                                          |
| `boolean equals(Array <array1>, Array <array2>)`where `<array1>` is the first array which is compared against `<array2>`.                                                                                                 | Tests two arrays for value-equality and returns `true` if both arrays have the same size and all corresponding pairs of elements in the two arrays are equal. | 1. `#data.equals(new int[] {2,4,6,8,10}, new int[] {2,4,6,8,10})`

2. `#data.equals({2,4,6,8,10}, new int[] {2,4,6,8,10})`                                                                                                                                                                                         | 1) `true`

2) `true`                                    |

## Regex library

You can use regular expressions in operations with the following library.

| String                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                 | Input                                                                                                                                                                                              | Output                                                                                  |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `String replaceFirst(String <input>, String <regex>, String <replacement>)`where:- `<input>` is the string to search and replace in

- `<regex>` is the regular expression to which this string is to be matched

- `<replacement>` is the string to be substituted for the first match                                                                                                                                                                                                                                                                                                                                                                                                                   | Replaces the first substring of the text string that matches the given regular expression with the given replacement. A null reference passed to this method is a no-op and returns `null`.                                                                 | 1. `#regex.replaceFirst('upper case', '()( +)([a-z])', '$1_$3')`

2. `#regex.replaceFirst('upper case AND lower case', '()( +)([a-z])', '$1_$3')`                                                  | 1) `upper_case`

2) `upper_case AND lower case`                                         |
| `String replaceAll(String <input>, String <regex1>, String <replacement1>, …​, String <regexN>, String <replacementN>)`where:- `<input>` is the string to search and replace in

- `<regex1>` is the regular expression to which this string is to be matched

- `<replacement1>` is the string to be substituted for each match

- `<regex[2…​N]>` is an optional additional regular expression to which this string is to be matched

- `<replacement[2…​N]>` is an optional additional string to be substituted for each match. If replacement is missing, the corresponding regex string won't be altered.&#xA;&#xA;The first pair of find-replace arguments are mandatory and the rest are optional. | Replaces each substring of the text string that matches the given regular expression with the given replacement. You can use this for 1 or more find and replace options. The first pair of find-replace arguments are mandatory and the rest are optional. | 1. `#regex.replaceAll('upper case AND lower case', '()( +)([a-z])', '$1_$3')`

2. `#regex.replaceAll('numeric data to be replaced with textual data [1, 2]', 'to be', '', '1', 'one', '2', 'two')` | 1) `upper_case AND lower_case`

2) `numeric data replaced with textual data [one, two]` |
| `boolean matches(String <input>, String <regex>)`where:- `<input>` is the string to be matched with

- `<regex>` is the regular expression to which the string is matched                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Checks if the entire input string matches the regex pattern. If a null is passed as input, it returns `false`.                                                                                                                                              | `#regex.matches('upper case', '()( +)([a-z])')`                                                                                                                                                    | `true`                                                                                  |
| `Array findAllMatches(String <input>, String <regex>)`where:- `<input>` is the string to search in

- `<regex>` is the regular expression to which the string is matched                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Find all matching substrings in the input string matching the regex pattern.                                                                                                                                                                                | `#regex.findAllMatches('upper case AND lower case', '()( +)([a-z])')`                                                                                                                              | `["upper case", "lower case"]`                                                          |

## Crypto library

You can perform crypto operations such as hashing using the following library.

| String                                                                                                                                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                     | Input                                                   | Output                             |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ---------------------------------- |
| `String hmacHexDigest(String <data>, String <key>, String <algorithm>)`where:- `<data>` is the string value to be hashed and must not be null

- `<key>` is the string secret key to use and must not be null

- `<algorithm>` is the hashing algorithm to use and must not be null&#xA;&#xA;Supported algorithms are HmacMD5, HmacSHA1, HmacSHA224, HmacSHA256, HmacSHA384, and HmacSHA512. | Creates a hash for the required data with Hashed Message Authentication Code (HMAC) using the specified secret key and cryptographic hashing function algorithm.Returns the hash or digest as a string containing only hexadecimal digits.Supported algorithms for hashing functions are HmacMD5, HmacSHA1, HmacSHA224, HmacSHA256, HmacSHA384, and HmacSHA512. | `#crypto.hmacHexDigest('data', 'secretKey', 'HmacMD5')` | `6659dfc3b860b836c087e3fd82c0d16b` |

## Core library

You can perform basic conditional expressions using if-else and switch alternatives.

| String                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Any ifelse(Boolean <condition>, Any <value>, Boolean <elseifCondition<1…​10>>, Any <elseifValue<1…​10>>, Any <elseValue>)`where:- `<condition>` is the primary If conditional expression which should evaluate to a boolean value. If it is not boolean, every attempt will be made to convert it to a boolean value.

- `<value>` is the value to use if the primary condition evaluates to true.

- `<elseifCondition<1…​10>>` is an elseIf conditional expression which should evaluate to a boolean value. If it is not boolean, every attempt will be made to convert it to a boolean value. The elseIfValue should always follow the elseIf condition.

- *\<elseifValue<1…​10>>* is the value to use if the related elseIf condition evaluates to true.

- *\<elseValue>>* is the value to use if none of the conditions evaluate to true. | Library function for an If-Else statement. Expressions provided for If and elseIf conditions should evaluate to a boolean value and if not, every attempt will be made to convert the evaluated value to boolean.If the condition evaluates to a Number, any value greater than 0 will be treated as True, or else false. If the condition evaluates to a String, the values `true`, `on`, `y`, `t`, `yes` are treated as true irrespective of the case, and otherwise false. If the condition evaluates to something other than Boolean, Number or String, it will be treated as false.The If statement and elseIf statement is a pair: a condition and a value to be used if condition evaluates to true. The elseIf statements are optional, and can enter 0 to 10 elseIf statements as needed.The elseValue to be used if no condition evaluates to true is also optional and is always the last parameter in the method. |
| `Any switchExpr(Any <valueToFind>, Any <choiceToMatch1>, Any <valueToReturn1>, Any <choiceToMatch<2…​10>>, Any <valueToReturn<2…​10>>, Any <defaultValue>)`where:- `<valueToFind>` is the value against which all the choices are compared with to identify the match.

- `<choiceToMatch1>` is the choice to match.

- `<valueToReturn1>` is the value to use or return if the valueToFind matches the corresponding valueToMatch.

- *\<choiceToMatch<2…​10>>* are additonal and optional choices to match.

- *\<valueToReturn<2…​10>>* is the value to use or return if the valueToFind matches the corresponding choiceToMatch\<n>.

- *\<defaultValue>* is the value to use if no matching choice is found for valueToFind. If this is not provided, null is returned.                                                                       | Library function for a switch statement. A *\<valueToFind>* is compared against 1 or more choices to match (*\<choiceToMatch<1…​10>>*).If a match is found, the value corresponding to the matched choice (*\<valueToReturn<1…​10>>*) is returned. If no match is found, *\<defaultValue>* is returned if provided, or else null.*\<choiceToMatch\<n>>* and *\<valueToReturn\<n>>* are a pair and there should be a minimum of 1 pair and not exceed 10 pairs. A default value can be provided as the last parameter to the method.                                                                                                                                                                                                                                                                                                                                                                                           |

### Examples

| String                                                                                                                                                      | Input                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Any ifelse(Boolean <condition>, Any <value>, Boolean <elseifCondition<1…​10>>, Any <elseifValue<1…​10>>, Any <elseValue>)`                                 | ```json
{
  user: {
    type: "User"
  }
}
#core.ifelse(user.type == 'Administrator', 'Full Access', user.type == 'User', 'Restricted Access', 'No Access')
```returns `Restricted Access````json
{
  user: {
    memberOfGroupIDs: ["User"],
    type: "Dev"
  }
}
#core.ifelse(#data.indexOf(user.memberOfGroupIDs, 'Administrator') >= 0, 'Full Access',
	#data.indexOf(user.memberOfGroupIDs, 'User') >= 0,
	#core.ifelse(user.type == 'SRE', 'Power Access', user.type == 'Dev', 'Debugging Access', 'Read Access'), 'No Access')
```returns `Debugging Access` |
| `Any switchExpr(Any <valueToFind>, Any <choiceToMatch1>, Any <valueToReturn1>, Any <choiceToMatch<2…​10>>, Any <valueToReturn<2…​10>>, Any <defaultValue>)` | ```json
{
  user: {
    type: "Administrator"
  }
}
#core.switchExpr(user.type, 'Administrator', 'Full Access')
```returns `Restricted Access````json
{
  user: {
    type: "User"
  }
}
#core.switchExpr(user.type, 'Administrator', 'Full Access', 'User', 'Restricted Access', 'No Access')
```returns `Restricted Access`                                                                                                                                                                                                                                        |

---

---
title: Disabled and restricted SpEL features
description: Learn which SpEL features are disabled or restricted in PingOne.
component: pingone
page_id: pingone:pingone_expression_language:p1_disabled_spel_features
canonical_url: https://docs.pingidentity.com/pingone/pingone_expression_language/p1_disabled_spel_features.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 3, 2024
---

# Disabled and restricted SpEL features

* [Array declaration and initialization](https://docs.spring.io/spring-framework/docs/5.1.x/spring-framework-reference/core.html#expressions-properties-arrays)

  You can only declare primitive arrays. Use List for both primitive and non-primitive arrays.

* [Type (T) operator](https://docs.spring.io/spring-framework/docs/5.1.x/spring-framework-reference/core.html#expressions-types)

  This feature is disabled along with the restriction on Java class usage.

* [instanceof operator](https://docs.spring.io/spring-framework/docs/5.1.x/spring-framework-reference/core.html#expressions-operators)

  This feature is disabled along with the restriction on Java class usage.

* [Assignment operator](https://docs.spring.io/spring-framework/docs/5.1.x/spring-framework-reference/core.html#expressions-assignment)

  All external data used in the expression through external property references are read only.

* [Static and Instance methods](https://docs.spring.io/spring-framework/docs/5.1.x/spring-framework-reference/core.html#expressions-methods)

  None of the static or instance methods in the Java API are accessible in expressions.

* [Operators](p1_expressionlang_operators.html)

  A leading and trailing space is required for the binary operators, as explained in the [Operators](p1_expressionlang_operators.html) section.

* [Safe Navigation (?.) Operator](https://docs.spring.io/spring-framework/docs/5.1.x/spring-framework-reference/core.html#expressions-operator-safe-navigation)

  The Safe Navigation operator is disabled because PingOne's expression language already attempts safe navigation internally when accessing object properties, except for object literals similar to the Safe Navigation operator (`?.`). This allows access to child properties against a parent object without errors, even if the parent object is null.

For example, `user.address.city` returns null if either `user` or `address` is null.

---

---
title: Expressions and concatenation
description: Use expressions and concatenation with the PingOne expression builder.
component: pingone
page_id: pingone:pingone_expression_language:p1_expressionlang_expressions_concatenation
canonical_url: https://docs.pingidentity.com/pingone/pingone_expression_language/p1_expressionlang_expressions_concatenation.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 3, 2024
section_ids:
  property-reference-expressions: Property reference expressions
  literal-expressions: Literal expressions
  string-concatenation: String concatenation
  p1-expressions-microsoft: Using expressions to retrieve Microsoft Entra attributes
  p1-entra-additional-attributes: Attributes that aren't predefined in PingOne
  steps: Steps
  example: Example:
  p1-entra-custom-attributes: Custom attributes
  p1-extension-attributes: Extension attributes
  before-you-begin: Before you begin
  steps-2: Steps
  result: Result:
  example-2: Example:
  result-2: Result
  p1-directory-extensions: Directory extensions
  before-you-begin-2: Before you begin
  steps-3: Steps
  example-3: Example:
  example-4: Example:
  example-5: Example:
  result-3: Result
  p1-schema-extensions: Schema extensions
  before-you-begin-3: Before you begin
  steps-4: Steps
  choose-from: Choose from:
  example-6: Example:
  result-4: Result
  example-7: Example:
  result-5: Result
---

# Expressions and concatenation

## Property reference expressions

Property reference expressions are the most common expression pattern to refer to a JSON object property using dotted syntax, `object.property1`, or map access syntax, `object[property]`.

Any property that begins with a letter and only contains letters, numbers or underscores can be accessed using dot notation or map access syntax, for example:

* `user.accountId`

* `user.name.given`

* `user['accountId']`

* `user['name']['given']`

If a property contains a character other than the ones mentioned previously, such as a hyphen or dollar sign, it can only be accessed using the map access syntax, for example `user.name['full-name']` or `providerAttributes['amountIn$']`.

## Literal expressions

PingOne supports literal expressions in the form of strings, numeric values, boolean, and null.

Strings are delimited by single quotation marks. To put a single quotation mark itself in a string, use two single quotation mark characters around it. For example, `'''string'''` returns `'string'`.

Numeric literals used directly in expressions must adhere to Java standards, such as adhering to min and max limits and using `l` or `L` for long literals. Numeric literals are also subject to the Java floating point rounding issues.

| Expression type         | Example                        |
| ----------------------- | ------------------------------ |
| String in double quotes | `"Hello"`                      |
| String in single quotes | `'Hello', '''Hello'''`         |
| Numbers                 | `1`, `8.57`, `34533535454345L` |
| Boolean                 | `true` or `false`              |

## String concatenation

You can use the `+` operator to concatenate values. You must include a leading and trailing space around the operator.

For example, `user.name.family + ', ' + user.name.given` or `'Hi'
user.name.given`.

|   |                                                                                     |
| - | ----------------------------------------------------------------------------------- |
|   | Because it's missing a leading space, `'Hi'+ user.name.given` will return an error. |

## Using expressions to retrieve Microsoft Entra attributes

When setting up Microsoft as an external identity provider (IdP) in PingOne, you can use expressions to retrieve user attributes from Microsoft Entra ID, including:

* [Attributes that aren't predefined](#p1-entra-additional-attributes) in the attribute mappings in PingOne

* [Custom attributes you can add](#p1-entra-custom-attributes) in the Microsoft Entra admin center

### Attributes that aren't predefined in PingOne

You can define user attributes to map from the Entra admin center to PingOne by selecting from attributes that are predefined. However, the Entra admin center includes additional user attributes for each user record that aren't predefined in PingOne as attributes you can select, such as **Employee ID** and **Employee type**.

#### Steps

To retrieve additional attributes that aren't predefined in the attribute mappings list in PingOne:

1. In the Microsoft Entra admin center, locate the name of the attribute you want to map to PingOne.

2. Map the attribute to a PingOne user attribute:

   1. In the PingOne admin console, go to **Integrations > External IdPs** and browse or search for the Microsoft IdP.

   2. Click the Microsoft IdP to open the details panel.

   3. On the **Attributes** tab, click the **Pencil** ([icon: pencil, set=fa]) icon.

      |   |                                                                    |
      | - | ------------------------------------------------------------------ |
      |   | To add a new attribute mapping, click **[icon: plus, set=fa]Add**. |

   4. Click the **Gear** ([icon: gear, set=fa]) icon next to an attribute mapping to open the **Build and Test Expression** modal. Learn more in [Using the expression builder](p1_use_expression_builder.html) and [Mapping attributes](../directory/p1_editsamlattributemapping.html).

   5. Enter an **Expression** in the following format:

      `providerAttributes.<attributeName>`

      where `<attributeName>` is the attribute name from the Entra admin center.

      #### Example:

      To map **Employee type** from the Entra admin center, enter `providerAttributes.employeeType`.

   6. Click **Save**.

   7. On the **Attributes** tab, click **Save**.

### Custom attributes

You can use expressions in PingOne to retrieve custom user attributes from Microsoft Entra ID. Learn more in [Add custom data to resources using extensions](https://learn.microsoft.com/en-us/graph/extensibility-overview) in the Microsoft Entra documentation.

PingOne supports three types of Microsoft Entra attributes:

* [Extension attributes](#p1-extension-attributes)

* [Directory extensions](#p1-directory-extensions)

* [Schema extensions](#p1-schema-extensions)

#### Extension attributes

Extension attributes in Microsoft Entra are custom attributes you can use to add information about a user or device, such as an employee ID or organizational unit (OU), when syncing on-premise Active Directory (AD) to Microsoft Entra. Microsoft Entra supports 15 extension attribute properties and assigns 1 - 15 to the end of the attribute property name in the order you create them, such as `extensionAttribute1` for the first custom attribute and so on.

#### Before you begin

* [Add extension attributes](https://learn.microsoft.com/en-us/graph/extensibility-overview?tabs=http#add-or-update-data-in-extension-attributes) in the Microsoft Entra admin center.

* [Add Microsoft as an identity provider (IdP) in PingOne](../integrations/p1_add_idp_microsoft.html).

#### Steps

1. Review the extension attribute number assigned in Microsoft Entra for any attributes you want to map to PingOne:

   1. In the Microsoft Entra admin center, go to **Users** and select a user with an extension attribute.

   2. In the **On-premises** section, click **View** next to **Extension attributes**.

      ##### Result:

      Any extension attributes configured for this user display as numbered attributes, such as **Extension attribute 11** with an example value of Account Executive.

   3. Confirm the assigned number for any extension attributes you want to map to a PingOne user attribute, such as **Extension attribute 11** in this example.

      You'll need the number when adding an expression in PingOne.

2. Map an extension attribute to a PingOne user attribute:

   1. In the PingOne admin console, go to **Integrations > External IdPs** and browse or search for the Microsoft IdP.

   2. Click the Microsoft IdP to open the details panel.

   3. On the **Attributes** tab, click the **Pencil** ([icon: pencil, set=fa]) icon.

      |   |                                                                    |
      | - | ------------------------------------------------------------------ |
      |   | To add a new attribute mapping, click **[icon: plus, set=fa]Add**. |

   4. Click the **Gear** ([icon: gear, set=fa]) icon next to an attribute mapping to open the **Build and Test Expression** modal. Learn more in [Using the expression builder](p1_use_expression_builder.html) and [Mapping attributes](../directory/p1_editsamlattributemapping.html).

   5. In the modal, enter an expression in the **Expression** field in the following format:

      `providerAttributes.onPremisesExtensionAttributes.extensionAttribute<number>`

      where `<number>` can be 1 - 15 based on the extension attribute number you want to map from Microsoft Entra.

      #### Example:

      For Extension attribute 11, use the following format:

      `providerAttributes.onPremisesExtensionAttributes.extensionAttribute11`

   6. Click **Save**.

   7. On the **Attributes** tab, click **Save**.

   #### Result

   PingOne populates the extension attribute value from Microsoft Entra as the value for this user attribute. For example, Account Executive for Extension attribute 11.

|   |                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The user attribute in PingOne must have **Type** set to **STRING**, and **Multi-valued** can be set to **Yes** or **No**. Learn more in [Viewing user attributes](../directory/p1_viewuserattributes.html). |

#### Directory extensions

Directory extensions can be used to add a custom property to directory objects without requiring an external data store and don't come from on-premise AD. For example, you can add a custom property for user job groups, such as `jobGroupTracker`.

You must first register a directory extension on an application through the `Create extensionProperty` operation in Microsoft Entra and then target the directory extension to specific directory objects. Learn more in [Directory extensions](https://learn.microsoft.com/en-us/graph/extensibility-overview?tabs=http#directory-microsoft-entra-id-extensions) in the Microsoft Entra documentation.

#### Before you begin

[Add Microsoft as an identity provider (IdP) in PingOne](../integrations/p1_add_idp_microsoft.html).

#### Steps

1. In the Microsoft Entra admin center, define a directory extension on an application.

   Learn more in the [Microsoft Entra documentation](https://learn.microsoft.com/en-us/graph/extensibility-overview?tabs=http#define-the-directory-extension).

   |   |                                                                                                                                                                                                                                  |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Use the same application ID in Microsoft Entra used when creating the Microsoft IdP connection in PingOne. Learn more in [Adding Microsoft as an identity provider (IdP) in PingOne](../integrations/p1_add_idp_microsoft.html). |

   #### Example:

   You can define a directory extension named `jobGroupTracker` to identify user job groups. In the response, the directory extension property name is returned as follows:

   ```
   "name": "extension_b7d8e648520f41d3b9c0fdeb91768a0a_jobGroupTracker"
   ```

   You can find a [sample response](https://learn.microsoft.com/en-us/graph/extensibility-overview?tabs=http#response-1) in the Microsoft Entra documentation.

2. Define the value of the directory extension to a target object, such as a specific user, in the Microsoft Entra admin center.

   #### Example:

   You can add a value, such as `JobGroupN`, for the directory extension property `jobGroupTracker` that can be assigned to specific users as follows:

   ```
   "extension_b7d8e648520f41d3b9c0fdeb91768a0a_jobGroupTracker": "JobGroupN"
   ```

   You can find an [example](https://learn.microsoft.com/en-us/graph/extensibility-overview?tabs=http#add-a-directory-extension-property-to-a-target-object) in the Microsoft Entra documentation.

3. Map the directory extension to a PingOne user attribute:

   1. In the PingOne admin console, go to **Integrations > External IdPs** and browse or search for the Microsoft IdP.

   2. Click the Microsoft IdP to open the details panel.

   3. On the **Attributes** tab, click the **Pencil** ([icon: pencil, set=fa]) icon.

      |   |                                                                    |
      | - | ------------------------------------------------------------------ |
      |   | To add a new attribute mapping, click **[icon: plus, set=fa]Add**. |

   4. Click the **Gear** ([icon: gear, set=fa]) icon next to an attribute mapping to open the **Build and Test Expression** modal. Learn more in [Using the expression builder](p1_use_expression_builder.html) and [Mapping attributes](../directory/p1_editsamlattributemapping.html).

   5. In the modal, enter an expression in the **Expression** field in the following format:

      `providerAttributes.<name>`

      where `<name>` is the property name from the response in the Microsoft Entra admin center.

      #### Example:

      For a directory extension property with the name of `extension_b7d8e648520f41d3b9c0fdeb91768a0a_jobGroupTracker`, use the following format:

      `providerAttributes.extension_b7d8e648520f41d3b9c0fdeb91768a0a_jobGroupTracker`

4. Click **Save**.

5. On the **Attributes** tab, click **Save**.

   ### Result

   PingOne populates the directory extension property value from Microsoft Entra, such as `JobGroupN`, for this user attribute.

|   |                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The user attribute in PingOne must have **Type** set to **STRING**, and **Multi-valued** can be set to **Yes** or **No**. Learn more in [Viewing user attributes](../directory/p1_viewuserattributes.html). |

#### Schema extensions

Schema extensions allow you to add custom data to a resource type. For example, you can add custom properties to a user resource type to identify additional attributes for users, such as assigning training course data to particular users.

Similar to directory extensions, you must first define a schema extension in Microsoft Entra and then target the schema extension to a specific resource, such as a group.

#### Before you begin

[Add Microsoft as an identity provider (IdP) in PingOne](../integrations/p1_add_idp_microsoft.html).

#### Steps

1. In the Microsoft Entra admin center, define a schema extension.

   Learn more in [Adding custom data to groups using schema extensions](https://learn.microsoft.com/en-us/graph/extensibility-schema-groups) in the Microsoft documentation.

2. Define the value of the schema extension to a target object, such as a specific user.

   Learn more in [Add a schema extension to a resource instance](https://learn.microsoft.com/en-us/graph/extensibility-overview?tabs=http#add-a-schema-extension-to-a-resource-instance) in the Microsoft documentation.

3. Map the schema extension to a PingOne user attribute:

   1. In the PingOne admin console, go to **Integrations > External IdPs** and browse or search for the Microsoft IdP.

   2. Click the Microsoft IdP to open the details panel.

   3. On the **Attributes** tab, click the **Pencil** ([icon: pencil, set=fa]) icon.

      |   |                                                                    |
      | - | ------------------------------------------------------------------ |
      |   | To add a new attribute mapping, click **[icon: plus, set=fa]Add**. |

   4. Click the **Gear** ([icon: gear, set=fa]) icon next to an attribute mapping to open the **Build and Test Expression** modal. Learn more in [Using the expression builder](p1_use_expression_builder.html) and [Mapping attributes](../directory/p1_editsamlattributemapping.html).

   5. In the modal, enter an expression in the **Expression** field in either of the following formats.

      #### Choose from:

      * **Single-valued attribute**: To map a schema extension and one of its properties to a PingOne user attribute, use the following format:

        `providerAttributes.<id>.<name>`

        where `<id>` is the ID of the schema extension, and `<name>` is the name of the specific property you want to map from the Microsoft Entra admin center.

        #### Example:

        For a schema extension named `graphLearnCourses`, Microsoft Entra returns an ID for the schema extension of `extkmpdyld2_graphLearnCourses` in the response. For this schema extension, you can define a property with the name of `courseId` to assign to a user. This ID and property name are used in the expression in PingOne as follows:

        `providerAttributes.extkmpdyld2_graphLearnCourses.courseId`

        Learn more in [Add a schema extension to a resource instance](https://learn.microsoft.com/en-us/graph/extensibility-overview?tabs=http#add-a-schema-extension-to-a-resource-instance) in the Microsoft Entra documentation.

        #### Result

        PingOne populates the schema extension data as the value of the user attribute in PingOne, such as `100` for `courseId`. You can find a [sample response](https://learn.microsoft.com/en-us/graph/extensibility-overview?tabs=http#add-a-schema-extension-to-a-resource-instance) in the Microsoft Entra documentation.

        |   |                                                                                                                                                                                                             |
        | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        |   | The user attribute in PingOne must have **Type** set to **STRING**, and **Multi-valued** can be set to **Yes** or **No**. Learn more in [Viewing user attributes](../directory/p1_viewuserattributes.html). |

      * **Multi-valued attribute**: To map a schema extension and all of its properties to a PingOne user attribute, use the following format:

        `providerAttributes.<id>`

        where `<id>` is the ID of the schema extension in the Microsoft Entra admin center.

        #### Example:

        For a schema extension named `graphLearnCourses`, Microsoft Entra returns an ID for the schema extension of `extkmpdyld2_graphLearnCourses` in the response. This ID is used in the expression in PingOne as follows:

        `providerAttributes.extkmpdyld2_graphLearnCourses`

        #### Result

        PingOne populates all properties for this schema extension as the values of this user attribute in PingOne, such as `100`, `Explore Microsoft Graph`, and `Online` from the [sample response](https://learn.microsoft.com/en-us/graph/extensibility-overview?tabs=http#add-a-schema-extension-to-a-resource-instance) in the Microsoft Entra documentation.

        |   |                                                                                                                                                                                                                                                                                                                                                                                                                    |
        | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
        |   | The user attribute in PingOne must have **Type** set to **STRING** and **Multi-valued** set to **Yes**. Learn more in [Viewing user attributes](../directory/p1_viewuserattributes.html).PingOne identity data limits for custom attributes apply when adding multiple user attributes. Learn more in [Standard platform limits](../getting_started_with_pingone/p1_platform_limits.html#p1-identity-data-limits). |

4. Click **Save**.

5. On the **Attributes** tab, click **Save**.

---

---
title: Maps and objects
description: Define and access maps and objects in PingOne Expression Language using JSON-style syntax, dot notation, and bracket access.
component: pingone
page_id: pingone:pingone_expression_language:p1_expressionlang_maps_objects
canonical_url: https://docs.pingidentity.com/pingone/pingone_expression_language/p1_expressionlang_maps_objects.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 3, 2024
---

# Maps and objects

Define a map or object in the same way as a JSON object. Access a map using `[]`, or access an object using dot notation. For example, `{'<key>': <value>}`.

If the property key contains any characters other than alphanumeric characters or underscores, you must access it using `[]`. Null keys are discarded.

Map or object keys can be quoted or unquoted. If an unquoted key only contains alphanumeric characters or underscores, it is considered a literal. Otherwise, it is treated as an expression or data model property reference.

If a top level root property needs to be used as a map key which doesn't have the dot operator, use the internal variables `#root` or `#this`, as shown in the examples.

|   |                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The following examples are formatted with line breaks for readability, however expressions cannot contain line breaks or new line characters. |

| Command                | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Define a map or object | * Using quoted keys```json
{
  'userId': 100001,
  'name': {
    'first': user.name.given,
    'last': user.name.family
  },
  'departmentIds': new int[] {101, 102}
}
```* Using unquoted keys```json
{
  userId: 100001,
  name: {
    first: user.name.given
  }
}
```* Using a top level property value as key using `#root````json
{
  #root.externalId: 100001
}
```* Using a top level property value as key using `#this````json
{
  #this.externalId: 100001
}
``` |
| Empty map or object    | `\{:}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Access a map           | ```json
{
  'userId': 100001,
  'name': {
    'first': user.name.given,
    'last': user.name.family
  },
  'departmentIds': new int[] {101, 102}
}['name']['first']
```                                                                                                                                                                                                                                                                                                    |
| Access an object       | ```json
{
  'userId': 100001,
  'name': {
    'first': user.name.given,
    'last': user.name.family
  },
  'departmentIds': new int[] {101, 102}
}.name.first
```&#xA;&#xA;Object access against literals causes an error if an incorrect or missing property is accessed, as shown in the following example:&#xA;&#xA;{&#xA;  'name': {&#xA;    'first': user.name.given,&#xA;    'last': user.name.family&#xA;  }&#xA;}.name.middle                                      |

---

---
title: Null safe usage
description: Handle null values safely in PingOne Expression Language with examples for string concatenation, arrays, and ternary operators.
component: pingone
page_id: pingone:pingone_expression_language:p1_expressionlang_null_safe_usage
canonical_url: https://docs.pingidentity.com/pingone/pingone_expression_language/p1_expressionlang_null_safe_usage.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 3, 2024
section_ids:
  string-concatenation: String concatenation
  creating-an-array-using-nullable-values: Creating an array using nullable values
  ternary-operator: Ternary operator
---

# Null safe usage

Using property references that might be null in expressions can lead to unexpected results. This topic contains examples and how to handle them.

The examples in this topic use the following data model:

```json
{
  "user": {
    "name": {
      "given": "John",
      "family": "Doe"
    }
}
```

## String concatenation

* Issue

  Because `user.name.middle` is null, the expression `user.name.given + ', ' + user.name.middle + ', ' + user.name.family` returns `John, null, Doe`.

* Solution to concatenate only non-null values

  `#string.join({user.name.given, user.name.middle, user.name.family}, ', ')` returns `John, Doe`.

* Issue

  Because `user.age` is null and the other operand is numeric, the expression `3 + user.age` returns an error.

* Solution to avoid errors using an Elvis operator to add a default value

  `3 + (user.age ?: '')` returns `3`.

## Creating an array using nullable values

* Issue

  The newly created array `{user.externalId}` returns `[ null ]`.

* Solution to remove nulls from the newly created array

  `#data.removeAll({user.externalId}, {null})` returns `[]`.

## Ternary operator

* Issue

  Because `user.enabled` is null, the expression `user.enabled ? 'Active' : 'Inactive'` returns an error.

* Solution to avoid errors using an Elvis operator to add a default value

  `(user.enabled ?: false) ? 'Active' : 'Inactive'` returns `Inactive`.

---

---
title: Operators
description: Operators in the PingOne Expression Language are used to manipulate individual data items and data sets.
component: pingone
page_id: pingone:pingone_expression_language:p1_expressionlang_operators
canonical_url: https://docs.pingidentity.com/pingone/pingone_expression_language/p1_expressionlang_operators.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 25, 2025
page_aliases: ["p1_expressionlang_relational_operators.adoc", "p1_expressionlang_logical_operators.adoc", "p1_expressionlang_mathematical_operators.adoc", "p1_expressionlang_ternary_operator.adoc", "p1_expressionlang_elvis_operator.adoc"]
section_ids:
  p1-exp-lang-rel-operators: Relational operators
  p1-exp-lang-logic-operators: Logical operators
  p1-exp-lang-math-operators: Mathematical operators
  p1-exp-lang-ternary-operators: Ternary operator
  p1-exp-lang-elvis-operators: Elvis operator
---

# Operators

Operators are constructs used to manipulate individual data items and data sets. These include arithmetic, comparison, and logical operations.

## Relational operators

The following relational operators are supported by using standard operator notation:

* Equal

* Not equal

* Less than

* Less than or equal to

* Greater than

* Greater than or equal to

Each symbolic operator can also be specified as a purely alphabetic equivalent that is case insensitive.

|   |                                                                             |
| - | --------------------------------------------------------------------------- |
|   | All operator notations except for `!` require a leading and trailing space. |

| Alphabetic relational operator | Examples                                                                                                                                        |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| * `lt`

* `<`                  | `5 lt 12``5 < 12``user.activeDays < 30`&#xA;&#xA;Because the operator is missing a leading and trailing space, user.activeDays<30 is incorrect. |
| - `le`

- `⇐`                  | `6 le 6``6 ⇐ 6``user.activeDays ⇐ 30`                                                                                                           |
| * `gt`

* `>`                  | `12 gt 5``12 > 5``user.activeDays > 30`                                                                                                         |
| - `ge`

- `>=`                 | `12 ge 5``12 >= 5``user.activeDays >= 30`                                                                                                       |
| * `eq`

* `==`                 | `5 eq 5``5 == 5``user.activeDays == 30`                                                                                                         |
| - `ne`

- `!=`                 | `6 ne 5``6 != 5``user.activeDays != 30`                                                                                                         |
| * `not`

* `!`                 | `not (4 > 3)``!(user.activeDays < 30)`                                                                                                          |
| `matches`                      | Checks if a value matches the regular expression pattern.`'name' matches '[a-z]+'`                                                              |

## Logical operators

|   |                                                                                     |
| - | ----------------------------------------------------------------------------------- |
|   | All logical operator notations except for `!` require a leading and trailing space. |

| Logical operator | Example                                      |
| ---------------- | -------------------------------------------- |
| `and`            | `5 > 3 and 4 ⇐ 4`                            |
| `or`             | `5 > 3 or 4 < 3`                             |
| * `not`

* `!`   | `5 < 13 and not (4 < 3)``5 > 6 and ! 4 < 14` |

## Mathematical operators

All the following operators used for binary operation require a leading and trailing space.

| Mathematical operator | Description                                                                                                                                                                                                                                                                                                   |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `+`                   | Add numbers or concatenate if one of the operands is a string.`5 + 6``'Test' + 3`&#xA;&#xA;Because one of the operands is a string, it will return a string concatenation.`user.loginAttempts + user.logoutAttempts`&#xA;&#xA;Because the operator is missing a leading and trailing space, 5+6 is incorrect. |
| `-`                   | Subtraction`7 - 5``user.totalLicenses - user.activeLicenses`&#xA;&#xA;Because the operator is missing a leading and trailing space, 7-5 is incorrect.                                                                                                                                                         |
| `*`                   | Multiplication`3 * 5``user.avgLoginsPerMonth * 12`                                                                                                                                                                                                                                                            |
| `/`                   | Division`12 / 3``user.totalLogins / 12`                                                                                                                                                                                                                                                                       |
| `%`                   | Modulus: Get remainder after division`7 % 4`                                                                                                                                                                                                                                                                  |
| `^`                   | Exponential Power`2 ^ 3`, which is equivalent to `(2 * 2 * 2)`                                                                                                                                                                                                                                                |

## Ternary operator

You can use the ternary operator to perform single line if-then-else logic expressions.

```
user.enabled ? 'Active' : 'Inactive'
```

## Elvis operator

The Elvis operator is a short form for the [Operators](p1_expressionlang_operators.html) for null checks. This operator requires a leading and trailing space.

You can rewrite `user.id != null ? user.id : 'N/A'` as `user.id ?: 'N/A'`.

---

---
title: PingOne Expression Language
description: The PingOne Expression Language is an augmentation of SpEL for querying and manipulating objects in expressions at runtime.
component: pingone
page_id: pingone:pingone_expression_language:p1_expression_language
canonical_url: https://docs.pingidentity.com/pingone/pingone_expression_language/p1_expression_language.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 07, 2025
---

# PingOne Expression Language

PingOne supports the Spring Expression Language (SpEL) version 5.1. SpEL is a powerful expression language used for querying and manipulating an object graph at runtime. Learn more in [SpEL framework](https://docs.spring.io/spring-framework/docs/3.0.x/reference/expressions.html).

The PingOne expression language is an augmentation of SpEL. The PingOne expression language syntax is similar to Unified EL and offers additional features, such as method invocation, through the libraries described in this section.

Learn more about SpEL functionality in PingOne in:

* [Using the expression builder](p1_use_expression_builder.html)

* [Samples](p1_pel_samples.html)

* [Expressions and concatenation](p1_expressionlang_expressions_concatenation.html)

* [Arrays and lists](p1_expressionlang_arrays_lists.html)

* [Maps and objects](p1_expressionlang_maps_objects.html)

* [Operators](p1_expressionlang_operators.html)

* [Collection operations](p1_expressionlang_collection_operations.html)

* [Disabled and restricted SpEL features](p1_disabled_spel_features.html)

* [Variables](p1_expressionlang_variables.html)

* [Custom library functions](p1_expressionlang_custom_library_functions.html)

* [Null safe usage](p1_expressionlang_null_safe_usage.html)

* [References](p1_expressionlang_references.html)

---

---
title: References
description: Find reference links for SpEL Language Reference and Java DateTimeFormatter pattern symbols used in PingOne Expression Language.
component: pingone
page_id: pingone:pingone_expression_language:p1_expressionlang_references
canonical_url: https://docs.pingidentity.com/pingone/pingone_expression_language/p1_expressionlang_references.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 3, 2024
section_ids:
  spring-expression-language: Spring Expression Language
  datetimeformatter-patterns: DateTimeFormatter patterns
---

# References

## Spring Expression Language

See the [SpEL Language Reference](https://docs.spring.io/spring-framework/docs/5.1.x/spring-framework-reference/core.html#expressions-language-ref).

## DateTimeFormatter patterns

The following common pattern symbols are extracted from Java documentation. For a complete list, see [Class DateTimeFormatter](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html).

| Symbol | Meaning                    | Examples                  |
| ------ | -------------------------- | ------------------------- |
| `y`    | year-of-era                | `2004`; `04`              |
| `D`    | day-of-year                | `189`                     |
| `M`    | month-of-year              | `07`; `Jul`; `July`; `J`  |
| `d`    | day-of-month               | `10`                      |
| `q`    | quarter-of-year            | `03`; `Q3`; `3rd quarter` |
| `W`    | week-of-month              | `4`                       |
| `E`    | day-of-week                | `Tue`; `Tuesday`; `T`     |
| `a`    | am-pm-of-day               | `PM`                      |
| `h`    | clock-hour-of-am-pm (1-12) | `12`                      |
| `K`    | hour-of-am-pm (0-11)       | `0`                       |
| `k`    | clock-hour-of-am-pm (1-24) | `1`                       |
| `H`    | hour-of-day (0-23)         | `0`                       |
| `m`    | minute-of-hour             | `30`                      |
| `s`    | second-of-minute           | `55`                      |

---

---
title: Samples
description: Use these sample expressions to build attribute mappings with the PingOne expression builder.
component: pingone
page_id: pingone:pingone_expression_language:p1_pel_samples
canonical_url: https://docs.pingidentity.com/pingone/pingone_expression_language/p1_pel_samples.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 29, 2025
section_ids:
  sample-user-model: Sample user model
  accessing-property-names-with-non-alphanumeric-characters: Accessing property names with non-alphanumeric characters
  p1_virtual_server_id: Sample expression for virtual server IDs
  example-scenario: Example scenario
---

# Samples

Use these sample expressions to build attribute mappings with the PingOne expression builder.

## Sample user model

The examples in this section use the following model:

```json
{
  "user": {
    "name": {
      "given": "John",
      "family": "Doe"
    },
    "role": "SA",
    "memberOfGroupNames": ["Admin", "User"],
    "groupDNs": [
      "CN=Devs,CN=Users,DC=malibu,DC=gl,DC=lab",
      "CN=Admins,CN=Users,DC=malibu,DC=gl,DC=lab"
    ]
  }
}
```

**Literal expressions**

| Expression              | Result                                  |
| ----------------------- | --------------------------------------- |
| `'FirstName'`           | ```
FirstName
```                       |
| `"User"`                | ```
User
```                            |
| `1`                     | ```
1
```                               |
| `true`                  | ```
true
```                            |
| `{'USER'}`              | ```
['USER']
```                        |
| `{'firstName': 'John'}` | ```json
{
    "firstName": "John"
}
``` |

**String concatenation**

| Expression                                  | Result                      |
| ------------------------------------------- | --------------------------- |
| `'FirstName' + ', ' + 'LastName'`           | ```
FirstName, LastName
``` |
| `user.name.given + ', ' + user.name.family` | ```
John, Doe
```           |

**Generate a user alias by concatenating parts of first and last name**

| Expression                                                                           | Result       |
| ------------------------------------------------------------------------------------ | ------------ |
| `#string.substring(user.name.given, 0, 1) #string.substring(user.name.family, 0, 4)` | ```
JDoe
``` |

**Extract the domain name from an email address**

| Expression                                               | Result         |
| -------------------------------------------------------- | -------------- |
| `#regex.findAllMatches('user01@test.com', '(?⇐@)[^.]+')` | ```
[test]
``` |

**Output the date as a string in a certain format**

| Expression                                                          | Result                               |
| ------------------------------------------------------------------- | ------------------------------------ |
| `#datetime.format('2021-01-01T10:15:00Z', 'EEEE, dd MMMM; h:mm a')` | ```
Friday, 01 January; 10:15 AM
``` |

**Replace a value based on a predefined set of options**

| Expression                                                                                                                         | Result                               |
| ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| `user.name.given + ' ' + user.name.family + ', ' + \{'PM': 'Product Manager', 'SA': 'Software Architect'}[user.role] ?: 'Unknown'` | ```
John Doe, Software Architect
``` |

**Change the contents of memberOfGroupNames array to upper case**

| Expression                                            | Result                              |
| ----------------------------------------------------- | ----------------------------------- |
| `user.memberOfGroupNames.![#string.upperCase(#this)]` | ```
[
    "ADMIN",
    "USER"
]
``` |

**Use string concatenation to transform the contents of memberOfGroupNames array to a group**

| Expression                                                      | Result                                                                        |
| --------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `user.memberOfGroupNames.!['CN=' + #this
',DC=example,DC=com']` | ```
[
    "CN=Admin,DC=example,DC=com",
    "CN=User,DC=example,DC=com"
]
``` |

**Extract group names from an array of group DNs**

| Expression                                                       | Result                               |
| ---------------------------------------------------------------- | ------------------------------------ |
| `user.groupDNs.![#regex.replaceAll(#this, '(CN=)(.?),.', '$2')]` | ```
[
    "Devs",
    "Admins"
]
``` |

## Accessing property names with non-alphanumeric characters

If a property name contains any characters other than alpha-numeric characters and underscores (`_`), use the map access format instead of dot notation.

The examples in this section use the following model:

```json
{
    "providerAttributes": {
        "full-name": "John Doe",
        "http://www.schema.com/samples/userId": "jdoe00",
        "Email Address": "johndoe00@test.com"
    },
    "custom-attributes": {
        "email": "johndoe00@test.com"
    }
}
```

**Property names with hyphens or dashes**

| Expression                        | Result           |
| --------------------------------- | ---------------- |
| `providerAttributes['full-name']` | ```
John Doe
``` |

**Properties with URI or URL based names**

| Expression                                                   | Result         |
| ------------------------------------------------------------ | -------------- |
| `providerAttributes['http://www.schema.com/samples/userId']` | ```
jdoe00
``` |

**Property names with blank spaces**

| Expression                            | Result                     |
| ------------------------------------- | -------------------------- |
| `providerAttributes['Email Address']` | ```
johndoe00@test.com
``` |

**Property roots with hyphens or dashes**

| Expression                         | Result                     |
| ---------------------------------- | -------------------------- |
| `#root['custom-attributes'].email` | ```
johndoe00@test.com
``` |

## Sample expression for virtual server IDs

This section outlines how to use an expression to safeguard against misuse of [virtual server IDs](../applications/p1_edit_application_saml.html#p1_allow_virtual_server_id) (VSIDs) between the identity provider (IdP) and the application, which acts as the service provider (SP). VSIDs allow your PingOne environment to identify itself differently for different purposes. You can define VSIDs on the **Configuration** tab of the SAML application.

When multiple VSIDs are defined in a SAML application, the application has multiple versions of the **Initiate Single Sign-On URL**, one for each respective VSID. You can obtain the URLs on the **Overview** tab for the application by selecting the applicable VSID in the **Display Virtual Server ID** list. Learn more about defining VSIDs in [Editing an application - SAML](../applications/p1_edit_application_saml.html#p1_allow_virtual_server_id).

### Example scenario

You can create a SAML application and define three VSIDs for Who's at Work (the IdP) and Widget (the SP) for the following purposes:

* Development

  * Who's at Work entity ID: `urn:widget:us:whosatwork:sso:dev` (VSID #1)

  * Widget entity ID: `https://whosatwork.widget.com`

* Testing

  * Who's at Work entity ID: `urn:widget:us:whosatwork:sso:test` (VSID #2)

  * Widget entity ID: `https://whosatwork.widget.com`

* Production

  * Who's at Work entity ID: `https://sso.whosatwork.com` (VSID #3, default)

  * Widget entity ID: `https://whosatwork.widget.com`

When you select one of the VSIDs on the **Overview** tab for the application, the **Initiate Single Sign-On URL** changes because the selected VSID is embedded in the URL.

You can use an expression to prevent unauthorized access and ensure only users from a certain department, such as the Engineering department, can connect to Widget (the SP) for development and testing purposes while allowing users from all departments to connect for production use.

When using multiple VSIDs to distinguish groups of users within one environment, such as different PingOne populations, you can add validation rules to make sure one group of users can't use SSO using the VSID for another group of users. To prevent unauthorized access, you can use the following example expression to fulfill the `saml_subject` attribute on the **Attribute Mappings** tab of the application:

```
 (
 (context.requestData.virtualServerId eq 'urn:widget:us:whosatwork:sso:dev' and
 user.population.id eq '560b3182-c947-4b53-9621-afbe8dbc2488')
 or
 (context.requestData.virtualServerId eq 'urn:widget:us:whosatwork:sso:test' and
 user.population.id eq '560b3182-c947-4b53-9621-afbe8dbc2488')
 or
 (context.requestData.virtualServerId eq 'https://sso.whosatwork.com')
 )? user.username : null
```

In this example, the expression allows all users to access Widget for production purposes and ensures only users whose PingOne user records are associated with a particular population can access Widget for development and testing purposes. The expression can also be used to validate other conditions, such as group membership.

If one of the conditions is met, PingOne populates the `saml_subject` attribute with the user's username in PingOne. If none of the conditions are met, PingOne determines that `saml_subject` is null and rejects the request. A SAML assertion can't be generated without this required attribute.

---

---
title: Using the expression builder
description: Use the expression builder in PingOne to create expressions and test the results of those expressions.
component: pingone
page_id: pingone:pingone_expression_language:p1_use_expression_builder
canonical_url: https://docs.pingidentity.com/pingone/pingone_expression_language/p1_use_expression_builder.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 29, 2025
section_ids:
  steps: Steps
---

# Using the expression builder

Use the expression builder to create expressions and test the results of those expressions. You can also use expressions to manipulate data, concatenate strings, and build arrays.

The expression builder uses the PingOne expression language to identify and access user attributes in the PingOne directory or other external applications or directories.

## Steps

1. In the PingOne admin console, go to **Applications > Applications** and browse or search for the application to which you want to add an attribute mapping.

2. Click the application entry to open the details panel.

3. On the **Attribute Mappings** tab, click the **Pencil** icon.

4. Click the **Gear** icon next to an attribute mapping to open the **Build and Test Expression** modal. Learn more in [Mapping attributes](../directory/p1_editsamlattributemapping.html).

   * Enter an expression that identifies the attribute you want to map.

   * To verify an expression and see sample data, click **Test Expression**.

   * To toggle between expression values and JSON, click **Edit JSON** or **Edit Values**.

   * For sample expressions and reference information, click **View Documentation**.

5. Click **Save**.

6. On the **Attribute Mappings** tab, click **Save**.

---

---
title: Variables
description: "Learn about variables available in PingOne Expression Language, including #root, #this, authentication JWT variables, and custom library references."
component: pingone
page_id: pingone:pingone_expression_language:p1_expressionlang_variables
canonical_url: https://docs.pingidentity.com/pingone/pingone_expression_language/p1_expressionlang_variables.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 07, 2025
section_ids:
  root-and-this-variables: "#root and #this variables"
  authentication-jwt-variables: Authentication JWT variables
  custom-properties: Custom properties
  custom-library-variables: Custom library variables
---

# Variables

## `#root` and `#this` variables

`#root` refers to the root context and `#this` refers to the current evaluation context object. Both are internal variables.

You can also use these variables to access any data model property references available to you. For example, `user.name.given`, `#root.user.name.given`, or `#this.user.name.given`.

`#root` is useful in the following scenarios:

* Defining a map key with a base property name's value. Learn more in [Maps and objects](p1_expressionlang_maps_objects.html).

* Accessing a property from the root context from within array or collection operations, such as projections or filtering, which is outside the current evaluation context. For example, `user.memberOfGroupNames.![#root.user.email + ' - ' + #this]`.

`#this` is useful within array or collection operations, such as projections or filtering, especially when the collections contain string, boolean, or number types instead of objects. For example, `user.memberOfGroupNames.![#string.upperCase(#this)]`.

Within the projection operator, `#this` refers to the array element being iterated. If `user.memberOfGroupNames` is a string array, `#this` represents each string element being iterated within the projection operator.

## Authentication JWT variables

You can use variables to retrieve information from the token endpoint authentication JSON Web Token (JWT) and authentication method itself for access token and ID token fulfillment. Expressions are supported when using the private key JWT and client secret JWT token endpoint authentication methods. Learn more in [Token endpoint authentication methods](../applications/p1_token_endpoint_authentication_methods.html).

Use variables in expressions to retrieve information in the following configurations:

* [Custom resources](../applications/p1_adding_custom_resource.html) to fulfill access tokens

* [OpenID Connect (OIDC) resources](../applications/p1_edit_oidc_resource.html) to fulfill ID tokens

* [OIDC-based applications](../applications/p1_editing_applications.html) to override ID token fulfillment

The following variables are available in the expression builder:

| Variable                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `#root.context.requestData.clientAssertion`                  | The authentication JWT payload sent by the application at the token endpoint.                                                                                                                                                                                                                                                                                                                                                              |
| `#root.context.requestData.clientAssertion.<property>`       | The value of `<property>` from the authentication JWT payload sent by the application at the token endpoint.                                                                                                                                                                                                                                                                                                                               |
| `#root.context.requestData.clientAssertionHeader`            | The authentication JWT header sent by the application at the token endpoint.                                                                                                                                                                                                                                                                                                                                                               |
| `#root.context.requestData.clientAssertionHeader.<property>` | The value of `<property>` from the header of the authentication JWT sent by the application at the token endpoint.                                                                                                                                                                                                                                                                                                                         |
| `#root.context.requestData`                                  | The authentication JWT header and payload sent by the application at the token endpoint.                                                                                                                                                                                                                                                                                                                                                   |
| `#root.context.appConfig.tokenEndpointAuthMethod`            | The token endpoint authentication method of the requesting application. Learn more in [Token endpoint authentication methods](../applications/p1_token_endpoint_authentication_methods.html).Possible values are:- `PRIVATE_KEY_JWT`

- `CLIENT_SECRET_JWT`

- `null` if the application isn't configured to use either `PRIVATE_KEY_JWT` or `CLIENT_SECRET_JWT`. Learn more in [Null safe usage](p1_expressionlang_null_safe_usage.html). |

### Custom properties

You can use the following custom property types with authentication JWT variables:

| Custom Property Type    | Description                                                                                                                                                                                                                               |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| String or numeric value | Add the custom property to the variable to access the value. For example, if the payload contains a property named custom1, add `custom1` to the payload variable: `#root.context.requestData.clientAssertion.custom1`.                   |
| Array                   | Add the custom property followed by `[n]` to the variable to access the nth element, where n starts with 0 for the first element. For example, `#root.context.requestData.clientAssertion.custom1[n]`.                                    |
| Nested JSON object      | Add the custom property followed by `.x` or `['x']` to the variable, where x is the nested property name. For example, `#root.context.requestData.clientAssertion.custom1.x` or `#root.context.requestData.clientAssertion.custom1['x']`. |

## Custom library variables

Additional internal variables are available for use in expressions, which are references to the custom libraries covered in [Custom library functions](p1_expressionlang_custom_library_functions.html).

The following variable references are available to custom libraries:

| Reference   | Description                                                                                          |
| ----------- | ---------------------------------------------------------------------------------------------------- |
| `#string`   | Function for string-based operations.                                                                |
| `#data`     | Functions for processing arrays.                                                                     |
| `#datetime` | Functions for parsing and processing date values. All input and output dates are in ISO 8601 format. |
| `#regex`    | Functions using regular expressions.                                                                 |
| `#crypto`   | Functions for crypto operations, such as hashing and more in the future.                             |