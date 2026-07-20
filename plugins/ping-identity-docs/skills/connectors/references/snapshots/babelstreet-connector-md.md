---
title: Babel Street Connector
description: Configure the Babel Street connector in PingOne DaVinci to compare name and address similarity, transliterate names, and identify text language
component: connectors
page_id: connectors::babelstreet_connector
canonical_url: https://docs.pingidentity.com/connectors/babelstreet_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  configuring-the-babel-street-connector: Configuring the Babel Street connector
  connector-configuration: Connector configuration
  api-key: API Key
  using-the-connector-in-a-flow: Using the connector in a flow
  comparing-name-similarity: Comparing name similarity
  comparing-address-similarity: Comparing address similarity
  converting-a-name-from-one-writing-system-to-another: Converting a name from one writing system to another
  identifying-the-language-of-a-text-sample: Identifying the language of a text sample
  capabilities: Capabilities
  nameSimilarity: Name Similarity
  addressSimilarity: Address Similarity
  nameTransliteration: Name Transliteration
  languageIdentification: Language Identification
---

# Babel Street Connector

The Babel Street connector lets you use the [Babel Street Analytics API](https://docs.babelstreet.com/API/en/using-the-analytics-api.html) in your PingOne DaVinci flow.

The connector offers a suite of tools for name and address similarity, name transliteration, and language identification.

## Setup

### Resources

You can find more information and setup help in the following:

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need a Babel Street API Key.

### Configuring the Babel Street connector

Add the connector in PingOne DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

##### API Key

The API Key for the Babel Street Analytics API.

## Using the connector in a flow

### Comparing name similarity

![A screen capture of the complete name similarity flow.](_images/connector-images/tap-babelstreet-namesimilarity-flow.png)

This flow prompts a user to enter two names into a form, optionally specifying the language for each. For greater accuracy, the node can also be configured with an expected entity type and gender. The node then compares the names and outputs a similarity score from 0 to 1.

Test the flow by clicking **Save**, **Deploy**, and **Try Flow**.

### Comparing address similarity

![A screen capture of the complete address similarity flow.](_images/connector-images/tap-babelstreet-addresssimilarity-flow.png)

This flow prompts a user to enter the details of two addresses into a form. The accuracy of the comparison improves as more fields are completed. The node then compares the two addresses and outputs a similarity score from 0 to 1.

Test the flow by clicking **Save**, **Deploy**, and **Try Flow**.

### Converting a name from one writing system to another

![A screen capture of the complete name transliteration flow.](_images/connector-images/tap-babelstreet-nametransliteration-flow.png)

This flow prompts a user to enter a name and a target language. For a more accurate transliteration, the user can optionally provide the name's source language and configure the node to expect a specific entity type. The node then outputs the transliterated name in the target language, along with a confidence score.

Test the flow by clicking **Save**, **Deploy**, and **Try Flow**.

### Identifying the language of a text sample

![A screen capture of the complete language identification flow.](_images/connector-images/tap-babelstreet-languageidentification-flow.png)

This flow prompts a user to enter a text sample. The node then outputs the language detected, along with a confidence score.

Test the flow by clicking **Save**, **Deploy**, and **Try Flow**.

## Capabilities

### Name Similarity

Name Similarity compares two entity names (Person, Location, or Organization) and returns a match score from 0 to 1.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Name 1 textField required
>
>   The first name to be compared
>
> - Name 1 - Language textField
>
>   The language of the first name
>
> - Name 1 - Entity Type dropDown
>
>   The type of the first name
>
>   * Person (Default)
>
>   * Location
>
>   * Organization
>
> - Name 1 - Gender dropDown
>
>   The gender associated with the first name
>
>   * Male
>
>   * Female
>
>   * Nonbinary
>
> - Name 2 textField required
>
>   The second name to be compared
>
> - Name 2 - Language textField
>
>   The language of the second name
>
> - Name 2 - Entity Type dropDown
>
>   The type of the second name
>
>   * Person (Default)
>
>   * Location
>
>   * Organization
>
> - Name 2 - Gender dropDown
>
>   The gender associated with the second name
>
>   * Male
>
>   * Female
>
>   * Nonbinary
>
> * default object
>
>   * properties object
>
>     * textName1 string required
>
>       The first name to be compared. This can be the name of a person, location, or organization (e.g., "Barbara Jensen", "New York City", or "Babel Street").
>
>     * languageName1 string
>
>       The first name's language specified by the three-letter ISO 639-3 code.
>
>     * entityTypeName1 string
>
>       The type of the first name (use "PERSON", "LOCATION", or "ORGANIZATION").
>
>     * genderName1 string
>
>       The gender associated with the first name (use "MALE", "FEMALE", or "NONBINARY").
>
>     * textName2 string required
>
>       The second name to be compared. This can be the name of a person, location, or organization (e.g., "Barbara Jensen", "New York City", or "Babel Street").
>
>     * languageName2 string
>
>       The second name's language specified by the three-letter ISO 639-3 code.
>
>     * entityTypeName2 string
>
>       The type of the second name (use "PERSON", "LOCATION", or "ORGANIZATION").
>
>     * genderName2 string
>
>       The gender associated with the second name (use "MALE", "FEMALE", or "NONBINARY").
>
> Input Example
>
> ```json
> {
>   "properties": {
>     "textName1": "Barbara Jensen",
>     "languageName1": "eng",
>     "entityTypeName1": "PERSON",
>     "genderName1": "FEMALE",
>     "textName2": "Hanson Dolores",
>     "languageName2": "eng",
>     "entityTypeName2": "PERSON",
>     "genderName2": "MALE"
>   }
> }
> ```
>
> * output object
>
>   * rawResponse object
>
>     The full, unmodified JSON object returned directly from the external API call.
>
>   * statusCode number
>
>     The HTTP status code returned by the API request.
>
>   * score number
>
>     A numerical score from 0.0 (no similarity) to 1.0 (a perfect match) indicating how similar the two names are.
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "score": 0.43314963
>   },
>   "statusCode": 200,
>   "score": 0.43314963
> }
> ```

### Address Similarity

Address Similarity compares two addresses and returns a match score from 0 to 1.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Address 1 - Unit textField
>
>   The unit, apartment, or suite number for the first address
>
> - Address 1 - House Number textField
>
>   The house or building number on the street for the first address
>
> - Address 1 - Street textField
>
>   The street name for the first address
>
> - Address 1 - City textField
>
>   The city or town for the first address
>
> - Address 1 - State textField
>
>   The state, province, or primary administrative region for the first address
>
> - Address 1 - Postal Code textField
>
>   The postal code or ZIP code for the first address
>
> - Address 1 - Country textField
>
>   The country for the first address
>
> - Address 2 - Unit textField
>
>   The unit, apartment, or suite number for the second address
>
> - Address 2 - House Number textField
>
>   The house or building number on the street for the second address
>
> - Address 2 - Street textField
>
>   The street name for the second address
>
> - Address 2 - City textField
>
>   The city or town for the second address
>
> - Address 2 - State textField
>
>   The state, province, or primary administrative region for the second address
>
> - Address 2 - Postal Code textField
>
>   The postal code or ZIP code for the second address
>
> - Address 2 - Country textField
>
>   The country for the second address
>
> * default object
>
>   * address1Unit string
>
>     The unit, apartment, or suite number for the first address (e.g., "4B" or "Suite 1200").
>
>   * address1HouseNo string
>
>     The house or building number on the street for the first address (e.g., "123").
>
>   * address1Road string
>
>     The street name for the first address (e.g., "Main St").
>
>   * address1City string
>
>     The city or town for the first address (e.g., "Victoria").
>
>   * address1State string
>
>     The state, province, or primary administrative region for the first address (e.g., "BC" or "California").
>
>   * address1PostCode string
>
>     The postal code or ZIP code for the first address (e.g., "V8W 1A1" or "90210").
>
>   * address1Country string
>
>     The country for the first address. Can be a full name or a code (e.g., "Canada" or "CAN").
>
>   * address2Unit string
>
>     The unit, apartment, or suite number for the second address.
>
>   * address2HouseNo string
>
>     The house or building number on the street for the second address.
>
>   * address2Road string
>
>     The street name for the second address.
>
>   * address2City string
>
>     The city or town for the second address.
>
>   * address2State string
>
>     The state, province, or primary administrative region for the first address.
>
>   * address2PostCode string
>
>     The postal code or ZIP code for the second address.
>
>   * address2Country string
>
>     The country for the second address.
>
> Input Example
>
> ```json
> {
>   "properties": {
>     "address1Unit": "Suite 300",
>     "address1HouseNo": "721",
>     "address1Road": "Government Street",
>     "address1City": "Victoria",
>     "address1State": "BC",
>     "address1PostCode": "V8W 1W5",
>     "address1Country": "Canada",
>     "address2Unit": "300",
>     "address2HouseNo": "721",
>     "address2Road": "Government St",
>     "address2City": "Victoria",
>     "address2State": "British Columbia",
>     "address2PostCode": "V8W 1W5",
>     "address2Country": "CA"
>   }
> }
> ```
>
> * output object
>
>   * rawResponse object
>
>     The full, unmodified JSON object returned directly from the external API call.
>
>   * statusCode number
>
>     The HTTP status code returned by the API request.
>
>   * score number
>
>     A numerical score from 0.0 (no similarity) to 1.0 (a perfect match) indicating how similar the two addresses are.
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "score": 0.86834957
>   },
>   "statusCode": 200,
>   "score": 0.86834957
> }
> ```

### Name Transliteration

Name Transliteration converts a name from one writing system to another, preserving its approximate pronunciation.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Name textField required
>
>   The name to be transliterated
>
> - Target Language textField required
>
>   The language to transliterate the name into
>
> - Entity Type dropDown required
>
>   The type of entity: Person, Location, or Organization
>
>   * Person (Default)
>
>   * Location
>
>   * Organization
>
> - Source Language of Origin textField
>
>   The name's original language
>
> * default object
>
>   * properties object
>
>     * name string required
>
>       The name of the entity to transliterate (e.g., "Barbara Jensen" or "北京").
>
>     * targetLanguage string required
>
>       The three-letter ISO 639-3 code for the target language (e.g., "eng" or "kor").
>
>     * entityType string required
>
>       Specifies the entity's type to improve accuracy (use "PERSON", "LOCATION", or "ORGANIZATION").
>
>     * sourceLanguageOfOrigin string
>
>       The name's native language, as a three-letter ISO 639-3 code.
>
> Input Example
>
> ```json
> {
>   "properties": {
>     "name": "Борис Петров",
>     "targetLanguage": "eng",
>     "entityType": "PERSON",
>     "sourceLanguageOfOrigin": "rus"
>   }
> }
> ```
>
> * output object
>
>   * rawResponse object
>
>     The full, unmodified JSON object returned directly from the external API call.
>
>   * statusCode number
>
>     The HTTP status code returned by the API request.
>
>   * translation string
>
>     The transliterated name in the target language.
>
>   * confidence number
>
>     A numerical score from 0.0 (lowest) to 1.0 (highest) indicating the API's certainty in the accuracy of the transliteration.
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "extendedInformation": {
>       "processedByBabel": true
>     },
>     "sourceScript": "Cyrl",
>     "sourceLanguageOfOrigin": "rus",
>     "sourceLanguageOfUse": "rus",
>     "targetLanguage": "eng",
>     "targetScript": "Latn",
>     "targetScheme": "IC",
>     "translation": "Boris Petrov",
>     "confidence": 1
>   },
>   "statusCode": 200,
>   "translation": "Boris Petrov",
>   "confidence": 1
> }
> ```

### Language Identification

Language Identification identifies the language of a given text sample, returning the language code and a confidence score.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Content textArea required
>
>   The text sample to be analyzed for language identification
>
> * default object
>
>   * properties object
>
>     * content string required
>
>       The text sample to be analyzed for language identification.
>
> Input Example
>
> ```json
> {
>   "properties": {
>     "content": "明日は明日の風が吹く"
>   }
> }
> ```
>
> * output object
>
>   * rawResponse object
>
>     The full, unmodified JSON object returned directly from the external API call.
>
>   * statusCode number
>
>     The HTTP status code returned by the API request.
>
>   * language string
>
>     The three-letter ISO 639-3 code for the detected language (e.g., "eng" for English).
>
>   * confidence number
>
>     A numerical score from 0.0 (lowest) to 1.0 (highest) indicating the API's certainty in the accuracy of the language identification.
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "languageDetections": [
>       {
>         "language": "jpn",
>         "confidence": 1
>       }
>     ]
>   },
>   "statusCode": 200,
>   "language": "jpn",
>   "confidence": 1
> }
> ```