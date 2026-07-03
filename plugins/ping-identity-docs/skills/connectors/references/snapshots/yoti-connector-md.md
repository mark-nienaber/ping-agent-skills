---
title: Yoti Connector
description: The Yoti connector lets you provide customers with a safe way to prove who they are through Yoti's identity verification, age estimate, and age verification services in your PingOne DaVinci flow.
component: connectors
page_id: connectors::yoti_connector
canonical_url: https://docs.pingidentity.com/connectors/yoti_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 19, 2024
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  setting-up-yoti: Setting up Yoti
  configuring-the-yoti-connector: Configuring the Yoti connector
  connector-configuration: Connector configuration
  sdk-id: SDK ID
  api-key: API Key
  using-the-connector-in-a-flow: Using the connector in a flow
  age-estimation: Age estimation
  age-verification: Age verification
  capabilities: Capabilities
  thirdPartyRedirectAgeVerification: Estimate Age Using Live Photo
  thirdPartyRedirectDigitalVerification: Verify Age Using Digital ID Credential
  thirdPartyRedirectDocumentVerification: Verify Age Using Identity Document
  thirdPartyRedirectCreditCardVerification: Verify Age Using Credit Card
  thirdPartyRedirectMobileVerification: Verify Age Using Mobile Carrier Contract
  databaseVerification: Verify Age with Credit Agency
  finishProcess: Wait for Verification Result
---

# Yoti Connector

The Yoti connector lets you provide customers with a safe way to prove who they are through Yoti's identity verification, age estimate, and age verification services in your PingOne DaVinci flow.

You can use the Yoti connector to:

* Estimate a user's age with a selfie photo.

* Verify users with multiple different methods.

* Wait for verification results from Yoti.

## Setup

### Resources

Learn more in the following:

* Yoti:

  * [Yoti Developer Documentation](https://developers.yoti.com/)

  * [Age Verification Documentation](https://developers.yoti.com/age-verification/overview)

* DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* A Yoti license

* Your Yoti credentials

### Setting up Yoti

Follow the instructions in [Yoti Quick Start](https://developers.yoti.com/age-verification/quick-start).

### Configuring the Yoti connector

Add the connector in DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

##### SDK ID

Your Yoti client SDK ID.

##### API Key

Your Yoti client API key.

## Using the connector in a flow

### Age estimation

You can use the **Estimate Age Using Live Photo** capability to prompt the user to take a selfie photo and return an estimated age.

Following your **Estimate Age Using Live Photos** capability, add another Yoti connector node and select the **Wait for Verification Result** result.

|   |                                                                                              |
| - | -------------------------------------------------------------------------------------------- |
|   | You can customize the waiting page HTML or CSS in the **Wait for Verification Result** node. |

### Age verification

The connector has several capabilities that allow you to verify the user's age:

* **Verify Age Using Digital ID Credential**

* **Verify Age Using Identity Documentation**

* **Verify Age Using Credit Card**

* **Verify Age Using Mobile Carrier Contact**

* **Verify Age with Credit Agency**

Following your age verification capability, for all capabilities except the **Verify Age with Credit Agency** capability, add another Yoti connector node and select the **Wait for Verification Result** capability.

|   |                                                                                              |
| - | -------------------------------------------------------------------------------------------- |
|   | You can customize the waiting page HTML or CSS in the **Wait for Verification Result** node. |

## Capabilities

### Estimate Age Using Live Photo

Prompt the user to take a selfie photo. Yoti analyzes the photo and returns an estimated age, such as "25".

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Age Check Method dropDown required
>
>   Determines whether Yoti returns a true or false response or provides the user's numerical age.
>
>   * Must be over Age Threshold (Default)
>
>   * Must be under Age Threshold
>
>   * Get age from Yoti
>
> - Age Threshold textField required
>
>   Enter the required age, such as "21". The user must be over or under this age, depending on the Age Check Method.
>
> - Check for Liveness toggleSwitch required
>
>   When enabled, Yoti uses passive analysis to check the image for signs that it might be a 2D image, mask, or bot.
>
> - * Display Name button
>   * showPoweredBy toggleSwitch
>   * skipButtonPress toggleSwitch
>
> * default object
>
>   * type string
>
>   * ageEstimation boolean
>
>   * threshold number
>
>   * estimationLevel string
>
> - location string
>
> - output object
>
>   * sessionId string

### Verify Age Using Digital ID Credential

Prompt the user to scan a QR code and open a digital ID app, then provide Yoti with a verified age attribute from the app.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Age Check Method dropDown required
>
>   Determines whether Yoti returns a true or false response or provides the user's numerical age.
>
>   * Must be over Age Threshold (Default)
>
>   * Must be under Age Threshold
>
>   * Get age from Yoti
>
> - Age Threshold textField required
>
>   Enter the required age, such as "21". The user must be over or under this age, depending on the Age Check Method.
>
> - * Display Name button
>   * showPoweredBy toggleSwitch
>   * skipButtonPress toggleSwitch
>
> * default object
>
>   * properties object
>
>     * type string
>
>     * ageEstimation boolean
>
>     * threshold number
>
>     * estimationLevel string
>
> - location string
>
> - output object
>
>   * sessionId string

### Verify Age Using Identity Document

Prompt the user to scan a photo ID document and take an optional selfie photo. Yoti verifies the document ID and matches the photo to the document.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Age Check Method dropDown required
>
>   Determines whether Yoti returns a true or false response or provides the user's numerical age.
>
>   * Must be over Age Threshold (Default)
>
>   * Must be under Age Threshold
>
>   * Get age from Yoti
>
> - Age Threshold textField required
>
>   Enter the required age, such as "21". The user must be over or under this age, depending on the Age Check Method.
>
> - Additional Authenticity Check dropDown
>
>   Determines whether Yoti performs a visual check on the document. For more information, contact your Yoti representative.
>
>   * None
>
>   * Automatic
>
>   * Manual
>
> - Country Code textField
>
>   The user's three-digit country code, in ISO 3166 Alpha-3 format, such as "USA".
>
> - Check for Liveness toggleSwitch required
>
>   When enabled, Yoti uses passive analysis to check the image for signs that it might be a 2D image, mask, or bot.
>
> - * Display Name button
>   * showPoweredBy toggleSwitch
>   * skipButtonPress toggleSwitch
>
> * default object
>
>   * properties object
>
>     * type string
>
>     * ageEstimation boolean
>
>     * threshold number
>
>     * estimationLevel string
>
> - location string
>
> - output object
>
>   * sessionId string

### Verify Age Using Credit Card

Prompt the user to enter their credit card number, expiry, postal code, and CV number. Yoti verifies the information to prove that the user is old enough to possess a credit card.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - - Display Name button
>   - showPoweredBy toggleSwitch
>   - skipButtonPress toggleSwitch
>
> * default object
>
>   * properties object
>
>     * botton string
>
>     * showPoweredBy boolean
>
>     * skipButtonPress number
>
> - location string
>
> - output object
>
>   * sessionId string

### Verify Age Using Mobile Carrier Contract

Prompt the user to enter their name, date of birthday, mobile phone number, and address. Yoti sends an SMS confirmation message to prove the user is old enough to possess a mobile carrier contract.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - - Display Name button
>   - showPoweredBy toggleSwitch
>   - skipButtonPress toggleSwitch
>
> * default object
>
>   * properties object
>
>     * botton string
>
>     * showPoweredBy boolean
>
>     * skipButtonPress number
>
> - location string
>
> - output object
>
>   * sessionId string

### Verify Age with Credit Agency

Prompt the user to enter their name, address, and date of birth. Yoti verifies the information against credit bureau databases to prove the user's age.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
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
> - Country textField required
>
>   The user's country, in ISO 3166-1 alpha-2 format, such as "US".
>
> - Address Line 1 textField required
>
>   The first line of the user's address, such as "123 Main Street".
>
> - Address Line 2 textField
>
>   The second line of the user's address, such as "Unit 10".
>
> - Address Line 3 textField
>
>   The third line of the user's address.
>
> - Postal Code textField required
>
>   The user's postal code.
>
> - Date of Birth textField required
>
>   Date of birth in format "MM/DD/YYYY".
>
> * default object
>
> - output object
>
>   * status string
>
>   * result boolean
>
>   * age number
>
>   * method string
>
>   * type string

### Wait for Verification Result

Show a waiting page until Yoti sends the result of the age estimation or verification to the DaVinci webhook URL.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - - Session ID textField required
>   - HTML Template textArea
>
>   Default:
>
>   ```none
>   <div
>    class="bg-light d-flex flex-column justify-content-center align-items-center position-absolute top-0 start-0 bottom-0 end-0 overflow-auto">
>    <div class="mh-100" style="max-width: 400px; width: 100%">
>    <div class="card shadow mb-5">
>    <div class="card-body p-5 d-flex flex-column">
>    <img
>    class="align-self-center mb-5"
>    src="{{global.variables.logoUrl}}"
>    alt="{{global.variables.companyName}}"
>    style="{{global.variables.logoStyle}}"
>    />
>    <p class="text-muted text-center">
>    We're processing your request.
>    </p>
>    </div>
>    </div>
>    </div>
>   </div>
>   ```
>
> - CSS codeEditor
>
>   Default:
>
>   ```none
>   @import "https://assets.pingone.com/ux/astro-nano/0.1.0-alpha.1/astro-nano.min.css";
>   @import "https://assets.pingone.com/ux/astro-nano/0.1.0-alpha.1/icons.css";
>   ```
>
> * default object
>
>   * sessionId string
>
>   * customHTML string
>
>   * customCSS string
>
> - output object
>
>   * age number
>
>   * method string
>
>   * id string
>
>   * state string
>
>   * status string
>
>   * sessionId string
