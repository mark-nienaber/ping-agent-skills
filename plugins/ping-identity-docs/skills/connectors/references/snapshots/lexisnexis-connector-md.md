---
title: LexisNexis Connector
description: Configure the LexisNexis connector in PingOne DaVinci to assess risk with ThreatMetrix, send OTPs, and authenticate with security questions
component: connectors
page_id: connectors::lexisnexis_connector
canonical_url: https://docs.pingidentity.com/connectors/lexisnexis_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  configuring-lexisnexis: Configuring LexisNexis
  configuring-the-lexisnexis-connector: Configuring the LexisNexis connector
  connector-configuration: Connector configuration
  api-url: API URL
  custom-api-url: Custom API URL
  organization-id: Organization ID
  api-key: API Key
  using-the-connector-in-a-flow: Using the connector in a flow
  get-a-risk-assessment-for-threatmetrix: Get a risk assessment for ThreatMetrix
  dynamic-decision-platform-ddp: Dynamic Decision Platform (DDP)
  prompt-a-user-for-a-one-time-passcode: Prompt a user for a one-time passcode
  prompt-a-user-with-security-questions: Prompt a user with security questions
  handling-unknown-sessions: Handling unknown sessions
  capabilities: Capabilities
  initialize: "ThreatMetrix: Send Device Profile"
  getCdnUrl: "ThreatMetrix: Get Profiling URL"
  idVerification: Instant Verify International
  threatMetrix: "ThreatMetrix: Get Risk Assessment"
  phoneFinder: Phone Finder
  emailage: Emailage
  kba: Knowledge-Based Authentication
  otpVerificationAuthProject: One Time Password
  kbaAuthProject: Knowledge-Based Authentication (Authentication Project)
  trueId: "TrueID: Verify Document"
  deleteDocuments: "TrueID: Delete Document"
---

# LexisNexis Connector

The LexisNexis connector lets you create a PingOne DaVinci flow that performs risk assessments with ThreatMetrix and other Dynamic Decision Platform services, sends a one-time passcode (OTP) *(tooltip: \<div class="paragraph">
\<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>
\</div>)*, and prompts users with security questions.

You can use the LexisNexis connector to:

* Get risk assessments from ThreatMetrix with the LexisNexis Dynamic Decision Platform

* Use the LexisNexis Dynamic Decision Platform to access services defined by your LexisNexis policy

* Get insights into identity data associated with phone numbers and email addresses

* Authenticate users with OTPs

* Authenticate users with security questions

## Setup

### Resources

Learn more in the following:

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* A LexisNexis account

* Credentials and access details for the LexisNexis services that you want to use

### Configuring LexisNexis

To configure the LexisNexis connector in PingOne DaVinci, you must create an API Key in PingOne DaVinci

To create an API Key:

1. From the **Applications** tab, click **Add Application**.

2. Enter a name for the application in the **Name** field, then click **Create**.

3. Find the application you created and click **Edit**.

4. From the **General** tab, copy the **API Key**.

### Configuring the LexisNexis connector

Add the connector in PingOne DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

##### API URL

The API URL to target. For a custom value, select **Use Custom API URL** and enter a value in the **Custom API URL** field.

##### Custom API URL

The API URL to target, such as `https://h.online-metrix.net`.

##### Organization ID

Your LexisNexis organization ID, such as `4en6ll2s`.

##### API Key

Your LexisNexis API key, such as `3x9ywfs26rm1zvl`.

## Using the connector in a flow

### Get a risk assessment for ThreatMetrix

![Screen capture of the spinner page created by the Get Device Profile capability.](_images/connector-images/dvc-lexisnexis-spinner-page.png)

Use the **Get Device Profile** capability followed by the **Dynamic Decision Platform (DDP)**capability to point to a ThreatMetrix policy name. Use the `review_status` and `risk_rating` results from the output to branch your flow.

The **Get Device Profile** capability presents an interim spinner page while gathering the device profile.

|   |                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------- |
|   | On the **UI** tab, you can customize the appearance of the spinner page with the **HTML**, **CSS**, and **Script** fields. |

### Dynamic Decision Platform (DDP)

You can use the **Dynamic Decision Platform (DDP)** to access services defined by your LexisNexis policy.

1. From the **General** tab, select a **Query Type**.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | **Session Query** requires a session ID obtained through the **Get Device Profile** capability and is used for the device-centric operations. You must provide at least one **Additional Parameter**.**Attribute Query** requires personally identifiable information (PII) to provide a risk rating and is used to trigger the DDP Rules Engine with a policy. You must provide at least one **Additional Parameter**. |

2. Select a **Service Type**.

3. (Optional) Select an **Event Type**.

4. In the **Policy** field, type the name of the Dynamic Decision Platform policy to use for this capability.

   |   |                                                                                                                                                                     |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The policy name entered in the **Policy** field must match exactly with the policy name defined in LexisNexis. To modify a policy, reach out to LexisNexis support. |

5. Define any additional parameters to send to LexisNexis, such as user attributes.

6. Click **Apply**.

### Prompt a user for a one-time passcode

![Screen capture of the OTP user-facing page created by the OTP Prompt capability.](_images/connector-images/dvc-lexisnexis-otp-page.png)

You can use the **OTP Prompt** capability to prompt users for a one-time passcode. On the **UI** tab, you can customize the appearance of the prompt with the **HTML**, **CSS**, and **Script** fields.

|   |                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The **$\[ExpirePeriod]** variable in the **Email Body** and **SMS Body** uses the policy default instead of the value from the **OTP Timeout** field. |

### Prompt a user with security questions

![Screen capture of the user-facing page created by the InstantID Q\&A capability.](_images/connector-images/dvc-lexisnexis-id-verification.png)

You can use the **InstantID Q\&A** capability to prompt a user with security questions. On the **UI** tab, you can customize the appearance of the prompt with the **HTML**, **CSS**, and **Script** fields.

### Handling unknown sessions

Unknown sessions occur when the **Get Device Profile** capability tries to get a risk evaluation due to a device profiling failure, therefore causing LexisNexis to not return a review status. Device profiling can be blocked for various reasons, including ad blockers and browsers (such as Firefox). PingOne DaVinci attempts to fingerprint the user's device until the time limit defined by the **Timeout** property is reached.

The **Get Device Profile** capability allows the end user to continue through the flow whether the device profiling succeeded or failed. The **Review Status for Unknown Sessions** property in the **Dynamic Decision Policy** capability allows you to pre-define how unknown sessions are treated. With this property, you assign a static review status, such as **Pass**, **Review**, **Challenge**, or **Reject**, allowing users with unknown sessions to proceed through the flow following the same branching rules as users that received a realtime review status from LexisNexis.

## Capabilities

### ThreatMetrix: Send Device Profile

Run the device profiling script, submit the profile, and get a session ID.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Initialization Loading text textField
>
> * default object
>
>   * properties object
>
>     * javascriptCdnUrl string required
>
>     * orgId string required
>
> - output object
>
>   * sessionId string

### ThreatMetrix: Get Profiling URL

Get a unique URL and session ID to use for device profiling in a custom page.

> **Collapse: Show details**
>
> * Input Schema
>
> * Output Schema
>
> - default object
>
>   * properties object
>
>     * javascriptCdnUrl string required
>
>     * orgId string required
>
> * output object
>
>   * cdnUrl string
>
>   * sessionId string

### Instant Verify International

Use LexisNexis DDP for multi-faceted fraud and risk assessment.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Policy textField required
>
>   The name of your policy in the Dynamic Decision Platform (DDP).
>
> - Service Type dropDown
>
>   Restricts which output fields are returned based on the level of access that a customer has. The service type is linked to your API key.
>
>   * Basic
>
>   * Session Policy
>
>   * Device
>
>   * DID
>
>   * IP
>
>   * Session
>
>   * All (Default)
>
>   * 3ds
>
> - First Name textField
>
>   The primary account holder's first name.
>
> - Middle Name textField
>
>   The primary account holder's middle name
>
> - Last Name textField
>
>   The primary account holder's last name
>
> - Street Address 1 textField
>
>   The primary account holder's street address 1
>
> - Street Address 2 textField
>
>   The primary account holder's street address 2
>
> - City textField
>
>   The primary account holder's city
>
> - State textField
>
>   The primary account holder's State
>
> - ZIP textField
>
>   The primary account holder's ZIP
>
> - Country textField
>
>   The primary account holder's country, in ISO 3166-1 alpha-2 format, such as "US".
>
> - Account Email textField
>
>   The primary account holder's email address.
>
> - Telephone Number textField
>
>   The primary account holder's telephone number. Can contain the following characters: 0-9 , . ; { } ( and ). All braces must be in pairs. White space is removed automatically.
>
> - Account Work Phone textField
>
>   The primary account holder's work telephone number. This field is not an entity.
>
> - Date of Birth textField
>
>   The primary account holder's date of birth, formatted as YYYYMMDD.
>
> - Gender textField
>
>   The primary account holder's gender.
>
> - * National ID Number textField
>   * National ID Type dropDown
>
>   The Type of National Id that will be used for verification.
>
>   * US\_SSN
>
>   * US\_SSN\_HASH
>
>   * US\_SSN4
>
>   * US\_SSN\_FIRST5
>
>   * BR\_CPF
>
>   * MX\_CURP
>
>   * CO\_CEDULA
>
> - Driver License Number textField
>
>   The primary account holder's driver license number.
>
> - Driver License Issuer textField
>
>   Primary account driver license issuer
>
> - Routing Address textField
>
>   The primary account holder's routing address.
>
> - Routing Standard textField
>
>   The primary account holder's routing standard.
>
> - Account Number textField
>
>   The primary account holder's account number.
>
> - Passport Number textField
>
>   The primary account holder's passport number.
>
> - Passport machine Readable Line 1 textField
>
>   The primary account holder's passport information in machine-readable format, line 1.
>
> - Passport machine Readable Line 2 textField
>
>   The primary account holder's passport information in machine-readable format, line 2.
>
> - Passport Expiration Date textField
>
>   The primary account holder's passport expiration date, formatted as YYYY-MM-DD.
>
> - Passport Country textField
>
>   The primary account holder's passport country, in ISO 3166-1 alpha-2 format, such as "US".
>
> - Transaction ID textField
>
>   The identifier used by the merchant to identify the transaction, such as a purchase order number.
>
> - Credit Card Number textField
>
>   The credit card number used in the transaction.
>
> - Online TLD textField
>
>   The description of the online TLD handle source. Used to prevent collisions between different online TLD handles. For help determining the correct online TLD for the ID you wish to send with your query, speak to a LexisNexis representative. This field is required if the Online TLD Handle field is populated.
>
> - Online TLD Handle textField
>
>   A unique third-party identifier, such as a LexID or a DUNS Number. Used for rule creation and investigation. This field is required if the Online TLD field is populated.
>
> - Line of Business textField
>
>   The line of business specified by the customer.
>
> - Application Name textField
>
>   The name of the application sending the event.
>
> - Shipping Account Holder's Street Address 1 textField
>
>   The shipping account holder's street address, line 1.
>
> - Shipping Account Holder's Street Address 2 textField
>
>   The shipping account holder's street address, line 2.
>
> - Shipping Account Holder's City textField
>
>   The shipping account holder's city.
>
> - Shipping Account Holder's State textField
>
>   The shipping account holder's state.
>
> - Shipping Account Holder's ZIP or Postal Code textField
>
>   The shipping account holder's ZIP or postal code.
>
> - Shipping Account Holder's Country textField
>
>   ﻿The shipping account holder's country, in ISO 3166-1 alpha-2 format, such as "US".
>
> - Routing Number textField
>
>   The routing number for the account. When using this attribute in a Condition/Expression Condition rule or Expression variable, the value will be treated as a string if quotes are used to enclose it and as a number if no quotes are used.
>
> - Transaction Amount textField
>
>   The numeric currency amount. If a decimal is used, exactly two digits must follow it.
>
> - Transaction Currency textField
>
>   The currency used for the transaction, formatted in ISO 4217 currency code, such as "USD". This field is required when Transaction Amount is populated.
>
> - Account Login textField
>
>   A unique identifier for the customer, such as a username or account ID. Used to check whether the customer is on a watch list.
>
> - Password textField
>
>   The password associated with the Account Login. This is hashed and sent to LexisNexis. Used to check whether the customer is on a watch list.
>
> - Social Security Number textField
>
>   The customer's social security number.
>
> - Account Number (Hash) textField
>
>   The customer's account number. This is hashed and sent to LexisNexis.
>
> - Driver License Number (Hash) textField
>
>   The customer's driver license number. This is hashed and sent to LexisNexis.
>
> - IP Address textField
>
>   The customer's IP address as detected by a web server. This must be a valid external address.
>
> - Page FingerPrint textField
>
>   The page fingerprint. This is hashed and sent to LexisNexis.
>
> - Device ID textField
>
>   The ExactID persistent global identifier, which relies on a variety of persistent markers (browser cookies, Adobe Flash cookies, HTML 5 local storage) to allow ThreatMetrix to 100% accurately identify a device.
>
> - Fuzzy Device ID textField
>
>   The SmartID device identifier, which is cookieless, and is based exclusively on device attributes to improve detection of returning visitors, especially those trying to elude identification, and reduces false positives.
>
> - HTTP Referer Domain textField
>
>   For TD Cloud, the domain of the HTTP referrer detected during profiling. For TD Mobile, this field can be optionally populated by the 'Custom URL' option in the TrustDefender Mobile Library. This relates to the Profiled Domain property below but only includes the domain portion of the passed URL as opposed to the whole URL which is present in the Profiled Domain property. This is passed to the library by the customer's native application. Described in more detail in the TMX Knowledgebase, Article ID 378.
>
> - Profiled Domain textField
>
>   For TD Cloud, the URL (i.e. domain + path + querystring) of the referring page. For TD Mobile, the same as the HTTP Referer Domain property.
>
> * default object
>
>   * properties object
>
>     * apiUrl string required
>
>     * apiKey string required
>
>     * orgId string required
>
>     * policy string required
>
>     * service\_type string required
>
>     * account\_first\_name string
>
>     * account\_middle\_name string
>
>     * account\_last\_name string
>
>     * account\_address\_street1 string
>
>     * account\_address\_street2 string
>
>     * account\_address\_city string
>
>     * account\_address\_state string
>
>     * account\_address\_zip string
>
>     * account\_address\_country string
>
>     * account\_email string
>
>     * account\_telephone string
>
>     * account\_work\_phone string
>
>     * account\_date\_of\_birth string
>
>     * account\_gender string
>
>     * national\_id\_number string
>
>     * national\_id\_type string
>
>     * account\_drivers\_license\_number string
>
>     * account\_drivers\_license\_issuer string
>
>     * account\_routing\_address string
>
>     * account\_routing\_standard string
>
>     * account\_number string
>
>     * account\_passport\_number string
>
>     * account\_passport\_machine\_readable\_line1 string
>
>     * account\_passport\_machine\_readable\_line2 string
>
>     * account\_passport\_expiration\_date string
>
>     * account\_passport\_country string
>
>     * transaction\_id string
>
>     * cc\_number\_hash string
>
>     * online\_tld string
>
>     * online\_tld\_handle string
>
>     * line\_of\_business string
>
>     * application\_name string
>
>     * shipping\_account\_address\_street1 string
>
>     * shipping\_account\_address\_street2 string
>
>     * shipping\_account\_address\_city string
>
>     * shipping\_account\_address\_state string
>
>     * shipping\_account\_address\_zip string
>
>     * shipping\_account\_address\_country string
>
>     * ach\_routing\_number string
>
>     * transaction\_amount number
>
>     * transaction\_currency string
>
>     * account\_login string
>
>     * password\_hash string
>
>     * ssn\_hash string
>
>     * ach\_account\_hash string
>
>     * drivers\_licence\_number\_hash string
>
>     * input\_ip\_address string
>
>     * page\_fingerprint string
>
>     * device\_id string
>
>     * fuzzy\_device\_id string
>
>     * http\_referer\_domain string
>
>     * profiled\_domain string
>
> - output object
>
>   * rawResponse object
>
>     * account\_address\_city string
>
>     * account\_address\_state string
>
>     * account\_address\_street1 string
>
>     * account\_address\_zip string
>
>     * account\_date\_of\_birth string
>
>     * account\_first\_name string
>
>     * account\_last\_name string
>
>     * account\_telephone string
>
>     * account\_telephone\_is\_possible string
>
>     * account\_telephone\_is\_valid string
>
>     * account\_telephone\_type string
>
>     * api\_call\_datetime string
>
>     * api\_type string
>
>     * api\_version string
>
>     * champion\_request\_duration string
>
>     * custom\_count\_10 string
>
>     * custom\_count\_12 string
>
>     * custom\_count\_15 string
>
>     * custom\_count\_8 string
>
>     * custom\_count\_9 string
>
>     * custom\_output\_11 array
>
>     * custom\_output\_12 array
>
>     * custom\_output\_13 array
>
>     * custom\_output\_14 array
>
>     * custom\_output\_15 array
>
>     * custom\_output\_16 array
>
>     * custom\_output\_7 array
>
>     * custom\_output\_9 array
>
>     * event\_datetime string
>
>     * event\_type string
>
>     * integration\_hub\_results object
>
>       * 3c8qvza7:DIIG Identity Verification object
>
>         * Execute DIIG object
>
>           * rule\_id string
>
>           * tps\_datetime string
>
>           * tps\_duration string
>
>           * tps\_result string
>
>           * tps\_type string
>
>           * tps\_vendor string
>
>           * tps\_vendor\_raw\_response string
>
>           * tps\_was\_timeout string
>
>     * national\_id\_number string
>
>     * national\_id\_type string
>
>     * org\_id string
>
>     * policy string
>
>     * policy\_details\_api object
>
>       * policy\_detail\_api array
>
>     * policy\_engine\_version string
>
>     * policy\_score string
>
>     * reason\_code array
>
>     * request\_id string
>
>     * request\_result string
>
>     * review\_status string
>
>     * risk\_rating string
>
>     * service\_type string
>
>     * tps\_was\_timeout string
>
>   * transactionStatus string
>
> Output Example
>
> ```json
>  { "rawResponse" :
>   { "account_address_city" : "Los Angeles",
>    "account_address_state" : "ca",
>    "account_address_street1" : "123 san marino ave",
>    "account_address_zip" : "95014",
>    "account_date_of_birth" : "19890625",
>    "account_first_name" : "John",
>    "account_last_name" : "Doe",
>    "account_telephone" : "+14579345754568",
>    "account_telephone_is_possible" : "yes",
>    "account_telephone_is_valid" : "yes",
>    "account_telephone_type" : "FIXED_LINE_OR_MOBILE",
>    "api_call_datetime" : "2021-08-18 10:34:31.214",
>    "api_type" : "session-query",
>    "api_version" : "12.3.2",
>    "champion_request_duration" : "1380",
>    "custom_count_10" : "8",
>    "custom_count_12" : "0",
>    "custom_count_15" : "1",
>    "custom_count_8" : "40",
>    "custom_count_9" : "8",
>    "custom_output_11" :
>    [ "1" ],
>    "custom_output_12" :
>    [ "1" ],
>    "custom_output_13" :
>    [ "1" ],
>    "custom_output_14" :
>    [ "1" ],
>    "custom_output_15" :
>    [ "1" ],
>    "custom_output_16" :
>    [ "1",
>     "1" ],
>    "custom_output_7" :
>    [ "1" ],
>    "custom_output_9" :
>    [ "1" ],
>    "event_datetime" : "2021-08-18 10:34:31.214",
>    "event_type" : "payment",
>    "integration_hub_results" :
>    { "3c8qvza7:DIIG Identity Verification" :
>     { "Execute DIIG" :
>      { "rule_id" : "198399037",
>       "tps_datetime" : "2021-08-18 10:34:31.225",
>       "tps_duration" : "1372",
>       "tps_result" : "ok",
>       "tps_type" : "LexisNexis_DIIG",
>       "tps_vendor" : "LexisNexis - Connectors",
>       "tps_vendor_raw_response" : "<raw_response>",
>       "tps_was_timeout" : "no" } } },
>    "national_id_number" : "1234",
>    "national_id_type" : "us_ssn4",
>    "org_id" : "3c8qvza7",
>    "policy" : "master",
>    "policy_details_api" :
>    { "policy_detail_api" :
>     [
>      { "type" : "champion",
>       "id" : "0",
>       "customer" :
>       { "score" : "8",
>        "pvid" : "1493214",
>        "review_status" : "reject",
>        "risk_rating" : "high",
>        "rules" :
>        [
>         { "rid" : "198140113",
>          "reason_code" : "ThreatMetrix",
>          "score" : "8",
>          "pvid" : "1493221",
>          "rules" :
>          [
>           { "rid" : "198140834",
>            "reason_code" : "INPUT ERROR: NO WEB SESSION ID",
>            "score" : "0" },
>
>           { "rid" : "198140836",
>            "reason_code" : "UNKNOWN SESSION",
>            "score" : "0" },
>
>           { "rid" : "198140859",
>            "reason_code" : "Email Agt GT 3Months (Global)",
>            "score" : "8" } ] },
>
>         { "rid" : "198140114",
>          "reason_code" : "Call DIIG",
>          "score" : "0",
>          "pvid" : "1493699",
>          "rules" :
>          [
>           { "rid" : "198399037",
>            "reason_code" : "Execute DIIG",
>            "score" : "0" },
>
>           { "rid" : "198399051",
>            "reason_code" : "DIIG Fail",
>            "score" : "0" },
>
>           { "rid" : "198399053",
>            "reason_code" : "IF DIIG Fails",
>            "score" : "0" },
>
>           { "rid" : "198399054",
>            "reason_code" : "Terminate - Identity Verification Failed",
>            "score" : "0" } ] } ] } } ] },
>    "policy_engine_version" : "12.3.1",
>    "policy_score" : "8",
>    "reason_code" :
>    [ "INPUT ERROR: NO WEB SESSION ID",
>     "UNKNOWN SESSION",
>     "Email Agt GT 3Months (Global)",
>     "ThreatMetrix",
>     "Execute DIIG",
>     "DIIG Fail",
>     "IF DIIG Fails",
>     "Terminate - Identity Verification Failed",
>     "Call DIIG" ],
>    "request_id" : "26895134-7b20-4c02-8d68-dfa76c7b32a1",
>    "request_result" : "success",
>    "review_status" : "reject",
>    "risk_rating" : "high",
>    "service_type" : "basic",
>    "tps_was_timeout" : "no" } }
> ```

### ThreatMetrix: Get Risk Assessment

Get a risk assessment from ThreatMetrix using a session ID and optional attributes.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Service Type dropDown
>
>   Restricts which output fields are returned based on the level of access that a customer has. The service type is linked to your API key.
>
>   * Basic
>
>   * Session Policy
>
>   * Device
>
>   * DID
>
>   * IP
>
>   * Session
>
>   * All (Default)
>
>   * 3ds
>
> - Event Type dropDown
>
>   NOTE: If event\_type is passed to attribute query, it WILL increment velocity counters etc just like a session query. if there is no event\_type on attribute query, it will run but not increment velocity etc counters.
>
>   * Login
>
>   * Payment
>
>   * Account Creation (Default)
>
>   * Transfer
>
>   * Transaction Other
>
>   * Auction Bid
>
>   * Details Change
>
>   * Add Listing
>
>   * Account Balance
>
>   * Transaction History
>
>   * Digital Download
>
>   * Digital Stream
>
> - Session ID textField
>
>   LexisNexis Session ID.
>
> - First Name textField
>
>   The primary account holder's first name.
>
> - Middle Name textField
>
>   The primary account holder's middle name
>
> - Last Name textField
>
>   The primary account holder's last name
>
> - Street Address 1 textField
>
>   The primary account holder's street address 1
>
> - Street Address 2 textField
>
>   The primary account holder's street address 2
>
> - City textField
>
>   The primary account holder's city
>
> - State textField
>
>   The primary account holder's State
>
> - ZIP textField
>
>   The primary account holder's ZIP
>
> - Country textField
>
>   The primary account holder's country, in ISO 3166-1 alpha-2 format, such as "US".
>
> - Account Email textField
>
>   The primary account holder's email address.
>
> - Telephone Number textField
>
>   The primary account holder's telephone number. Can contain the following characters: 0-9 , . ; { } ( and ). All braces must be in pairs. White space is removed automatically.
>
> - Account Work Phone textField
>
>   The primary account holder's work telephone number. This field is not an entity.
>
> - Date of Birth textField
>
>   The primary account holder's date of birth, formatted as YYYYMMDD.
>
> - Gender textField
>
>   The primary account holder's gender.
>
> - National ID Number textField
>
>   The primary account holder's national ID number. Used for identity verification.
>
> - National ID Type dropDown
>
>   The primary account holder's national ID type. Used for identity verification.
>
>   * US SSN
>
>   * US SSN HASH
>
>   * US SSN4
>
>   * US SSN FIRST5
>
>   * BR CPF
>
>   * MX CURP
>
>   * CO CEDULA
>
> - Driver License Number textField
>
>   The primary account holder's driver license number.
>
> - Driver License Issuer textField
>
>   Primary account driver license issuer
>
> - Routing Address textField
>
>   The primary account holder's routing address.
>
> - Routing Standard textField
>
>   The primary account holder's routing standard.
>
> - Account Number textField
>
>   The primary account holder's account number.
>
> - Passport Number textField
>
>   The primary account holder's passport number.
>
> - Passport machine Readable Line 1 textField
>
>   The primary account holder's passport information in machine-readable format, line 1.
>
> - Passport machine Readable Line 2 textField
>
>   The primary account holder's passport information in machine-readable format, line 2.
>
> - Passport Expiration Date textField
>
>   The primary account holder's passport expiration date, formatted as YYYY-MM-DD.
>
> - Passport Country textField
>
>   The primary account holder's passport country, in ISO 3166-1 alpha-2 format, such as "US".
>
> - Transaction ID textField
>
>   The identifier used by the merchant to identify the transaction, such as a purchase order number.
>
> - Credit Card Number textField
>
>   The credit card number used in the transaction.
>
> - Online TLD textField
>
>   The description of the online TLD handle source. Used to prevent collisions between different online TLD handles. For help determining the correct online TLD for the ID you wish to send with your query, speak to a LexisNexis representative. This field is required if the Online TLD Handle field is populated.
>
> - Online TLD Handle textField
>
>   A unique third-party identifier, such as a LexID or a DUNS Number. Used for rule creation and investigation. This field is required if the Online TLD field is populated.
>
> - Line of Business textField
>
>   The line of business specified by the customer.
>
> - Application Name textField
>
>   The name of the application sending the event.
>
> - Shipping Account Holder's Street Address 1 textField
>
>   The shipping account holder's street address, line 1.
>
> - Shipping Account Holder's Street Address 2 textField
>
>   The shipping account holder's street address, line 2.
>
> - Shipping Account Holder's City textField
>
>   The shipping account holder's city.
>
> - Shipping Account Holder's State textField
>
>   The shipping account holder's state.
>
> - Shipping Account Holder's ZIP or Postal Code textField
>
>   The shipping account holder's ZIP or postal code.
>
> - Shipping Account Holder's Country textField
>
>   ﻿The shipping account holder's country, in ISO 3166-1 alpha-2 format, such as "US".
>
> - Routing Number textField
>
>   The routing number for the account. When using this attribute in a Condition/Expression Condition rule or Expression variable, the value will be treated as a string if quotes are used to enclose it and as a number if no quotes are used.
>
> - Transaction Amount textField
>
>   The numeric currency amount. If a decimal is used, exactly two digits must follow it.
>
> - Transaction Currency textField
>
>   The currency used for the transaction, formatted in ISO 4217 currency code, such as "USD". This field is required when Transaction Amount is populated.
>
> - Account Login textField
>
>   A unique identifier for the customer, such as a username or account ID. Used to check whether the customer is on a watch list.
>
> - Password textField
>
>   The password associated with the Account Login. This is hashed and sent to LexisNexis. Used to check whether the customer is on a watch list.
>
> - Social Security Number textField
>
>   The customer's social security number.
>
> - Account Number (Hash) textField
>
>   The customer's account number. This is hashed and sent to LexisNexis.
>
> - Driver License Number (Hash) textField
>
>   The customer's driver license number. This is hashed and sent to LexisNexis.
>
> - IP Address textField
>
>   The customer's IP address as detected by a web server. This must be a valid external address.
>
> - Page FingerPrint textField
>
>   The page fingerprint. This is hashed and sent to LexisNexis.
>
> - Device ID textField
>
>   The ExactID persistent global identifier, which relies on a variety of persistent markers (browser cookies, Adobe Flash cookies, HTML 5 local storage) to allow ThreatMetrix to 100% accurately identify a device.
>
> - Fuzzy Device ID textField
>
>   The SmartID device identifier, which is cookieless, and is based exclusively on device attributes to improve detection of returning visitors, especially those trying to elude identification, and reduces false positives.
>
> - HTTP Referer Domain textField
>
>   For TD Cloud, the domain of the HTTP referrer detected during profiling. For TD Mobile, this field can be optionally populated by the 'Custom URL' option in the TrustDefender Mobile Library. This relates to the Profiled Domain property below but only includes the domain portion of the passed URL as opposed to the whole URL which is present in the Profiled Domain property. This is passed to the library by the customer's native application. Described in more detail in the TMX Knowledgebase, Article ID 378.
>
> - Profiled Domain textField
>
>   For TD Cloud, the URL (i.e. domain + path + querystring) of the referring page. For TD Mobile, the same as the HTTP Referer Domain property.
>
> * default object
>
>   * properties object
>
>     * apiUrl string required
>
>     * apiKey string required
>
>     * orgId string required
>
>     * service\_type string required
>
>     * account\_first\_name string
>
>     * account\_middle\_name string
>
>     * account\_last\_name string
>
>     * account\_address\_street1 string
>
>     * account\_address\_street2 string
>
>     * account\_address\_city string
>
>     * account\_address\_state string
>
>     * account\_address\_zip string
>
>     * account\_address\_country string
>
>     * account\_email string
>
>     * account\_telephone string
>
>     * account\_work\_phone string
>
>     * account\_date\_of\_birth string
>
>     * account\_gender string
>
>     * account\_national\_id\_number string
>
>     * account\_national\_id\_type string
>
>     * account\_drivers\_license\_number string
>
>     * account\_drivers\_license\_issuer string
>
>     * account\_routing\_address string
>
>     * account\_routing\_standard string
>
>     * account\_number string
>
>     * account\_passport\_number string
>
>     * account\_passport\_machine\_readable\_line1 string
>
>     * account\_passport\_machine\_readable\_line2 string
>
>     * account\_passport\_expiration\_date string
>
>     * account\_passport\_country string
>
>     * event\_type string
>
>     * transaction\_id string
>
>     * cc\_number\_hash string
>
>     * online\_tld string
>
>     * online\_tld\_handle string
>
>     * line\_of\_business string
>
>     * application\_name string
>
>     * shipping\_account\_address\_street1 string
>
>     * shipping\_account\_address\_street2 string
>
>     * shipping\_account\_address\_city string
>
>     * shipping\_account\_address\_state string
>
>     * shipping\_account\_address\_zip string
>
>     * shipping\_account\_address\_country string
>
>     * ach\_routing\_number string
>
>     * transaction\_amount number
>
>     * transaction\_currency string
>
>     * sessionId string
>
>     * account\_login string
>
>     * password\_hash string
>
>     * ssn\_hash string
>
>     * ach\_account\_hash string
>
>     * drivers\_licence\_number\_hash string
>
>     * input\_ip\_address string
>
>     * page\_fingerprint string
>
>     * device\_id string
>
>     * fuzzy\_device\_id string
>
>     * http\_referer\_domain string
>
>     * profiled\_domain string
>
> - output object
>
>   * rawResponse object
>
>     * account\_address\_city string
>
>     * account\_address\_state string
>
>     * account\_address\_street1 string
>
>     * account\_address\_zip string
>
>     * account\_date\_of\_birth string
>
>     * account\_first\_name string
>
>     * account\_last\_name string
>
>     * account\_telephone string
>
>     * account\_telephone\_is\_possible string
>
>     * account\_telephone\_is\_valid string
>
>     * account\_telephone\_type string
>
>     * api\_call\_datetime string
>
>     * api\_type string
>
>     * api\_version string
>
>     * champion\_request\_duration string
>
>     * custom\_count\_15 string
>
>     * event\_datetime string
>
>     * event\_type string
>
>     * national\_id\_number string
>
>     * national\_id\_type string
>
>     * org\_id string
>
>     * policy string
>
>     * policy\_details\_api object
>
>       * policy\_detail\_api array
>
>     * policy\_engine\_version string
>
>     * policy\_score string
>
>     * reason\_code array
>
>     * request\_id string
>
>     * request\_result string
>
>     * review\_status string
>
>     * risk\_rating string
>
>     * service\_type string
>
> Output Example
>
> ```json
>  { "rawResponse" :
>   { "account_address_city" : "cupertino",
>    "account_address_state" : "ca",
>    "account_address_street1" : "1234 Example ave",
>    "account_address_zip" : "84101",
>    "account_date_of_birth" : "19850515",
>    "account_first_name" : "John",
>    "account_last_name" : "Doe",
>    "account_telephone" : "+13684940396",
>    "account_telephone_is_possible" : "yes",
>    "account_telephone_is_valid" : "yes",
>    "account_telephone_type" : "FIXED_LINE_OR_MOBILE",
>    "api_call_datetime" : "2021-08-19 06:04:21.106",
>    "api_type" : "session-query",
>    "api_version" : "12.3.2",
>    "champion_request_duration" : "5",
>    "custom_count_15" : "1",
>    "event_datetime" : "2021-08-19 06:04:21.106",
>    "event_type" : "payment",
>    "national_id_number" : "1234",
>    "national_id_type" : "us_ssn4",
>    "org_id" : "3c8qvza7",
>    "policy" : "account_registration_v1",
>    "policy_details_api" :
>    { "policy_detail_api" :
>     [
>      { "type" : "champion",
>       "id" : "0",
>       "customer" :
>       { "score" : "8",
>        "pvid" : "1493221",
>        "review_status" : "pass",
>        "risk_rating" : "trusted",
>        "rules" :
>        [
>         { "rid" : "198140834",
>          "reason_code" : "INPUT ERROR: NO WEB SESSION ID",
>          "score" : "0" },
>
>         { "rid" : "198140836",
>          "reason_code" : "UNKNOWN SESSION",
>          "score" : "0" },
>
>         { "rid" : "198140859",
>          "reason_code" : "Email Agt GT 3Months (Global)",
>          "score" : "8" } ] } } ] },
>    "policy_engine_version" : "12.3.1",
>    "policy_score" : "8",
>    "reason_code" :
>    [ "INPUT ERROR: NO WEB SESSION ID",
>     "UNKNOWN SESSION",
>     "Email Agt GT 3Months (Global)" ],
>    "request_id" : "85b47c80-0ac6-4fea-adb3-654677bdc30a",
>    "request_result" : "success",
>    "review_status" : "pass",
>    "risk_rating" : "trusted",
>    "service_type" : "basic" } }
> ```

### Phone Finder

Search by phone number or identity to get ranked results with data insights like phone type, status, CallerID, and portability.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Service Type dropDown
>
>   Restricts which output fields are returned based on the level of access that a customer has. The service type is linked to your API key.
>
>   * Basic
>
>   * Session Policy
>
>   * Device
>
>   * DID
>
>   * IP
>
>   * Session
>
>   * All (Default)
>
>   * 3ds
>
> - Telephone Number textField
>
>   The primary account holder's telephone number. Can contain the following characters: 0-9 , . ; { } ( and ). All braces must be in pairs. White space is removed automatically.
>
> - First Name textField
>
>   The primary account holder's first name.
>
> - Middle Name textField
>
>   The primary account holder's middle name
>
> - Last Name textField
>
>   The primary account holder's last name
>
> - Street Address 1 textField
>
>   The primary account holder's street address 1
>
> - Street Address 2 textField
>
>   The primary account holder's street address 2
>
> - City textField
>
>   The primary account holder's city
>
> - State textField
>
>   The primary account holder's State
>
> - ZIP textField
>
>   The primary account holder's ZIP
>
> - Country textField
>
>   The primary account holder's country, in ISO 3166-1 alpha-2 format, such as "US".
>
> - Account Email textField
>
>   The primary account holder's email address.
>
> - Account Work Phone textField
>
>   The primary account holder's work telephone number. This field is not an entity.
>
> - Date of Birth textField
>
>   The primary account holder's date of birth, formatted as YYYYMMDD.
>
> - Gender textField
>
>   The primary account holder's gender.
>
> - National ID Number textField
>
>   The primary account holder's national ID number. Used for identity verification.
>
> - National ID Type dropDown
>
>   The primary account holder's national ID type. Used for identity verification.
>
>   * US SSN
>
>   * US SSN HASH
>
>   * US SSN4
>
>   * US SSN FIRST5
>
>   * BR CPF
>
>   * MX CURP
>
>   * CO CEDULA
>
> - Driver License Number textField
>
>   The primary account holder's driver license number.
>
> - Driver License Issuer textField
>
>   Primary account driver license issuer
>
> - Routing Address textField
>
>   The primary account holder's routing address.
>
> - Routing Standard textField
>
>   The primary account holder's routing standard.
>
> - Account Number textField
>
>   The primary account holder's account number.
>
> - Passport Number textField
>
>   The primary account holder's passport number.
>
> - Passport machine Readable Line 1 textField
>
>   The primary account holder's passport information in machine-readable format, line 1.
>
> - Passport machine Readable Line 2 textField
>
>   The primary account holder's passport information in machine-readable format, line 2.
>
> - Passport Expiration Date textField
>
>   The primary account holder's passport expiration date, formatted as YYYY-MM-DD.
>
> - Passport Country textField
>
>   The primary account holder's passport country, in ISO 3166-1 alpha-2 format, such as "US".
>
> - Transaction ID textField
>
>   The identifier used by the merchant to identify the transaction, such as a purchase order number.
>
> - Credit Card Number textField
>
>   The credit card number used in the transaction.
>
> - Online TLD textField
>
>   The description of the online TLD handle source. Used to prevent collisions between different online TLD handles. For help determining the correct online TLD for the ID you wish to send with your query, speak to a LexisNexis representative. This field is required if the Online TLD Handle field is populated.
>
> - Online TLD Handle textField
>
>   A unique third-party identifier, such as a LexID or a DUNS Number. Used for rule creation and investigation. This field is required if the Online TLD field is populated.
>
> - Line of Business textField
>
>   The line of business specified by the customer.
>
> - Application Name textField
>
>   The name of the application sending the event.
>
> - Shipping Account Holder's Street Address 1 textField
>
>   The shipping account holder's street address, line 1.
>
> - Shipping Account Holder's Street Address 2 textField
>
>   The shipping account holder's street address, line 2.
>
> - Shipping Account Holder's City textField
>
>   The shipping account holder's city.
>
> - Shipping Account Holder's State textField
>
>   The shipping account holder's state.
>
> - Shipping Account Holder's ZIP or Postal Code textField
>
>   The shipping account holder's ZIP or postal code.
>
> - Shipping Account Holder's Country textField
>
>   ﻿The shipping account holder's country, in ISO 3166-1 alpha-2 format, such as "US".
>
> - Routing Number textField
>
>   The routing number for the account. When using this attribute in a Condition/Expression Condition rule or Expression variable, the value will be treated as a string if quotes are used to enclose it and as a number if no quotes are used.
>
> - Transaction Amount textField
>
>   The numeric currency amount. If a decimal is used, exactly two digits must follow it.
>
> - Transaction Currency textField
>
>   The currency used for the transaction, formatted in ISO 4217 currency code, such as "USD". This field is required when Transaction Amount is populated.
>
> - Account Login textField
>
>   A unique identifier for the customer, such as a username or account ID. Used to check whether the customer is on a watch list.
>
> - Password textField
>
>   The password associated with the Account Login. This is hashed and sent to LexisNexis. Used to check whether the customer is on a watch list.
>
> - Social Security Number textField
>
>   The customer's social security number.
>
> - Account Number (Hash) textField
>
>   The customer's account number. This is hashed and sent to LexisNexis.
>
> - Driver License Number (Hash) textField
>
>   The customer's driver license number. This is hashed and sent to LexisNexis.
>
> - IP Address textField
>
>   The customer's IP address as detected by a web server. This must be a valid external address.
>
> - Page FingerPrint textField
>
>   The page fingerprint. This is hashed and sent to LexisNexis.
>
> - Device ID textField
>
>   The ExactID persistent global identifier, which relies on a variety of persistent markers (browser cookies, Adobe Flash cookies, HTML 5 local storage) to allow ThreatMetrix to 100% accurately identify a device.
>
> - Fuzzy Device ID textField
>
>   The SmartID device identifier, which is cookieless, and is based exclusively on device attributes to improve detection of returning visitors, especially those trying to elude identification, and reduces false positives.
>
> - HTTP Referer Domain textField
>
>   For TD Cloud, the domain of the HTTP referrer detected during profiling. For TD Mobile, this field can be optionally populated by the 'Custom URL' option in the TrustDefender Mobile Library. This relates to the Profiled Domain property below but only includes the domain portion of the passed URL as opposed to the whole URL which is present in the Profiled Domain property. This is passed to the library by the customer's native application. Described in more detail in the TMX Knowledgebase, Article ID 378.
>
> - Profiled Domain textField
>
>   For TD Cloud, the URL (i.e. domain + path + querystring) of the referring page. For TD Mobile, the same as the HTTP Referer Domain property.
>
> * default object
>
>   * properties object
>
>     * apiUrl string required
>
>     * apiKey string required
>
>     * orgId string required
>
>     * service\_type string required
>
>     * account\_first\_name string
>
>     * account\_middle\_name string
>
>     * account\_last\_name string
>
>     * account\_address\_street1 string
>
>     * account\_address\_street2 string
>
>     * account\_address\_city string
>
>     * account\_address\_state string
>
>     * account\_address\_zip string
>
>     * account\_address\_country string
>
>     * account\_email string
>
>     * account\_telephone string required
>
>     * account\_work\_phone string
>
>     * account\_date\_of\_birth string
>
>     * account\_gender string
>
>     * account\_national\_id\_number string
>
>     * account\_national\_id\_type string
>
>     * account\_drivers\_license\_number string
>
>     * account\_drivers\_license\_issuer string
>
>     * account\_routing\_address string
>
>     * account\_routing\_standard string
>
>     * account\_number string
>
>     * account\_passport\_number string
>
>     * account\_passport\_machine\_readable\_line1 string
>
>     * account\_passport\_machine\_readable\_line2 string
>
>     * account\_passport\_expiration\_date string
>
>     * account\_passport\_country string
>
>     * transaction\_id string
>
>     * cc\_number\_hash string
>
>     * online\_tld string
>
>     * online\_tld\_handle string
>
>     * line\_of\_business string
>
>     * application\_name string
>
>     * shipping\_account\_address\_street1 string
>
>     * shipping\_account\_address\_street2 string
>
>     * shipping\_account\_address\_city string
>
>     * shipping\_account\_address\_state string
>
>     * shipping\_account\_address\_zip string
>
>     * shipping\_account\_address\_country string
>
>     * ach\_routing\_number string
>
>     * transaction\_amount number
>
>     * transaction\_currency string
>
>     * account\_login string
>
>     * password\_hash string
>
>     * ssn\_hash string
>
>     * ach\_account\_hash string
>
>     * drivers\_licence\_number\_hash string
>
>     * input\_ip\_address string
>
>     * page\_fingerprint string
>
>     * device\_id string
>
>     * fuzzy\_device\_id string
>
>     * http\_referer\_domain string
>
>     * profiled\_domain string
>
> - output object
>
>   * rawResponse object
>
>     * account\_address\_city string
>
>     * account\_address\_state string
>
>     * account\_address\_street1 string
>
>     * account\_address\_zip string
>
>     * account\_date\_of\_birth string
>
>     * account\_first\_name string
>
>     * account\_last\_name string
>
>     * account\_lex\_id string
>
>     * account\_lex\_id\_region string
>
>     * account\_telephone string
>
>     * account\_telephone\_is\_possible string
>
>     * account\_telephone\_is\_valid string
>
>     * account\_telephone\_type string
>
>     * api\_call\_datetime string
>
>     * api\_type string
>
>     * api\_version string
>
>     * champion\_request\_duration string
>
>     * event\_datetime string
>
>     * event\_type string
>
>     * integration\_hub\_results object
>
>       * 3c8qvza7:Phone Finder object
>
>         * Execute Phone Finder object
>
>           * rule\_id string
>
>           * tps\_datetime string
>
>           * tps\_duration string
>
>           * tps\_result string
>
>           * tps\_type string
>
>           * tps\_vendor string
>
>           * tps\_vendor\_raw\_response object
>
>             * Status object
>
>               * ConversationId string
>
>               * RequestId string
>
>               * TransactionStatus string
>
>             * Products array
>
>           * tps\_was\_timeout string
>
>     * national\_id\_number string
>
>     * national\_id\_type string
>
>     * org\_id string
>
>     * policy string
>
>     * policy\_details\_api object
>
>       * policy\_detail\_api array
>
>     * policy\_engine\_version string
>
>     * policy\_score string
>
>     * reason\_code array
>
>     * request\_id string
>
>     * request\_result string
>
>     * review\_status string
>
>     * risk\_rating string
>
>     * service\_type string
>
>     * tps\_was\_timeout string
>
> Output Example
>
> ```json
>  { "rawResponse" :
>   { "account_address_city" : "Los Angeles",
>    "account_address_state" : "ca",
>    "account_address_street1" : "1234 example ave",
>    "account_address_zip" : "91243",
>    "account_date_of_birth" : "19830421",
>    "account_first_name" : "John",
>    "account_last_name" : "Doe",
>    "account_lex_id" : "US|1319573870",
>    "account_lex_id_region" : "US",
>    "account_telephone" : "+134586439734",
>    "account_telephone_is_possible" : "yes",
>    "account_telephone_is_valid" : "yes",
>    "account_telephone_type" : "FIXED_LINE_OR_MOBILE",
>    "api_call_datetime" : "2021-08-19 05:46:35.088",
>    "api_type" : "session-query",
>    "api_version" : "12.3.2",
>    "champion_request_duration" : "2465",
>    "event_datetime" : "2021-08-19 05:46:35.088",
>    "event_type" : "payment",
>    "integration_hub_results" :
>    { "3c8qvza7:Phone Finder" :
>     { "Execute Phone Finder" :
>      { "rule_id" : "198139573",
>       "tps_datetime" : "2021-08-19 05:46:35.098",
>       "tps_duration" : "2457",
>       "tps_result" : "ok",
>       "tps_type" : "LexisNexisPhoneFinderProduction_v3_FirstClass",
>       "tps_vendor" : "LexisNexis - Connectors",
>       "tps_vendor_raw_response" :
>       { "Status" :
>        { "ConversationId" : "31000689434669",
>         "RequestId" : "1117166609",
>         "TransactionStatus" : "passed" },
>        "Products" :
>        [
>         { "ProductType" : "PhoneFinder",
>          "ExecutedStepName" : "Phone Finder",
>          "ProductConfigurationName" : "GSA_GIVE_PF",
>          "ProductStatus" : "pass",
>          "Items" :
>          [
>           { "ItemName" : "PrepaidPhoneNumber",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "LastChangeDateIMEI",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "NoContractCarrier",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "VOIPPhone",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "LastChangeDateIMSI",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "SurnameMismatch",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "LostStolen",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "PhoneReturnedOften",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "WirelessServiceType",
>            "ItemStatus" : "fail",
>            "ItemReason" :
>            { "Code" : "WirelessServiceType.LOW",
>             "Description" : "Phone Service Type is Wireless" } },
>
>           { "ItemName" : "SourceSelfReported",
>            "ItemStatus" : "fail",
>            "ItemReason" :
>            { "Code" : "SourceSelfReported.MEDIUM",
>             "Description" : "Phone linked to identity by self-reported sources only" } },
>
>           { "ItemName" : "LandlineServiceType",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "CableServiceType",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "UnknownServiceType",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "1stFirstSeenDate",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "2ndFirstSeenDate",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "PhonePorted2ndRange",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "3rdFirstSeenDate",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "PhonePorted3rdRange",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "PhonePorted",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "FrequentlyPhonePorted",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "PhoneSpoofedNumOfDays",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "SpoofingPhoneNumber",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "SpoofingDestination",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "PhoneAssociatedWithMoreThanXIdentities",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "EmailCount(Month)",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "DeviceCount(Month)",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "PhoneHighCountryCount",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "RecentPhoneFirstSeen",
>            "ItemStatus" : "fail",
>            "ItemReason" :
>            { "Code" : "RecentPhoneFirstSeen.LOW",
>             "Description" : "Phone Number First Seen Recently in Digital Identity Network" } },
>
>           { "ItemName" : "DigitalIDBadReputation",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "PhoneNumberAssociatedWithFraud",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "PhoneInRejectedTransaction",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "PhoneSearch",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "PhoneOnGlobalBlacklist",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "PhoneOTPRequest",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "PhoneNotActive",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "SpoofedPhoneNumber",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "SubjectIsBusiness",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "PhoneForwarding",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "SubjectDeceased",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "NoFirstSeenDate",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "CommercialAddress",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "NoLastSeenDate",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "MismatchAreaCodeAndAddressArea",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "NoFirstAndLastSeenDate",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "NotCurrentAddress",
>            "ItemStatus" : "pass" },
>
>           { "ItemName" : "LastSeenDateAge",
>            "ItemStatus" : "fail",
>            "ItemReason" :
>            { "Code" : "LastSeenDateAge.MEDIUM",
>             "Description" : "Last Seen Date is older than \"365\" days" } } ],
>          "ParameterDetails" :
>          [
>           { "Group" : "IDENTITY_RECORDS",
>            "Name" : "Consumer_LexIDs",
>            "Values" :
>            [
>             { "Value" : "1319573870" } ] },
>
>           { "Group" : "IDENTITY_RECORDS",
>            "Name" : "Deceased_Indicators",
>            "Values" :
>            [
>             { "Value" : "N" } ] },
>
>           { "Group" : "IDENTITY_RECORDS",
>            "Name" : "Consumer_Full_Names",
>            "Values" :
>            [
>             { "Value" : "John Doe" } ] },
>
>           { "Group" : "IDENTITY_RECORDS",
>            "Name" : "Consumer_Street_1s",
>            "Values" :
>            [
>             { "Value" : "54345 san mario ave" } ] },
>
>           { "Group" : "IDENTITY_RECORDS",
>            "Name" : "Consumer_Street_2s",
>            "Values" :
>            [
>             { "Value" : "" } ] },
>
>           { "Group" : "IDENTITY_RECORDS",
>            "Name" : "Consumer_StateCityZIPs",
>            "Values" :
>            [
>             { "Value" : "CUPERTINO, CA 95014" } ] },
>
>           { "Group" : "IDENTITY_RECORDS",
>            "Name" : "Consumer_Time_With_Phones",
>            "Values" :
>            [
>             { "Value" : "0" } ] },
>
>           { "Group" : "IDENTITY_RECORDS",
>            "Name" : "Consumer_Time_Last_Seen_With_Phones",
>            "Values" :
>            [
>             { "Value" : "302" } ] },
>
>           { "Group" : "IDENTITY_RECORDS",
>            "Name" : "Consumer_Address_Types",
>            "Values" :
>            [
>             { "Value" : "Residential" } ] },
>
>           { "Group" : "IDENTITY_RECORDS",
>            "Name" : "Consumer_Address_Statuses",
>            "Values" :
>            [
>             { "Value" : "C" } ] },
>
>           { "Group" : "PRIMARY_PHONE",
>            "Name" : "Primary_Phone_Number",
>            "Values" :
>            [
>             { "Value" : "4085555568" } ] },
>
>           { "Group" : "PRIMARY_PHONE",
>            "Name" : "Primary_Phone_Type",
>            "Values" :
>            [
>             { "Value" : "POSSIBLE WIRELESS" } ] },
>
>           { "Group" : "PRIMARY_PHONE",
>            "Name" : "Primary_Phone_Carrier",
>            "Values" :
>            [
>             { "Value" : "NEW CINGULAR WIRELESS PCS, LLC" } ] },
>
>           { "Group" : "PRIMARY_PHONE",
>            "Name" : "Primary_Phone_Listing_Name",
>            "Values" :
>            [
>             { "Value" : "Doe John" } ] },
>
>           { "Group" : "PRIMARY_PHONE",
>            "Name" : "Primary_Phone_Status",
>            "Values" :
>            [
>             { "Value" : "ACTIVE" } ] },
>
>           { "Group" : "PRIMARY_PHONE",
>            "Name" : "Primary_Phone_Listing_Type",
>            "Values" :
>            [
>             { "Value" : "RESIDENTIAL" } ] },
>
>           { "Group" : "PRIMARY_PHONE",
>            "Name" : "Primary_Phone_Address_Type",
>            "Values" :
>            [
>             { "Value" : "" } ] },
>
>           { "Group" : "PRIMARY_PHONE",
>            "Name" : "Primary_Phone_Port_Code",
>            "Values" :
>            [
>             { "Value" : "Ported" } ] },
>
>           { "Group" : "PRIMARY_PHONE",
>            "Name" : "Primary_Phone_Caller_ID",
>            "Values" :
>            [
>             { "Value" : "Doe John" } ] },
>
>           { "Group" : "PRIMARY_PHONE",
>            "Name" : "Primary_Phone_Port_Count",
>            "Values" :
>            [
>             { "Value" : "1" } ] },
>
>           { "Group" : "PRIMARY_PHONE",
>            "Name" : "Phone_Verification_Indicator",
>            "Values" :
>            [
>             { "Value" : "1" } ] },
>
>           { "Group" : "PRIMARY_PHONE",
>            "Name" : "Primary_Phone_No_Contract_Carrier",
>            "Values" :
>            [
>             { "Value" : "0" } ] },
>
>           { "Group" : "PRIMARY_PHONE",
>            "Name" : "Phone_Verification_Msg",
>            "Values" :
>            [
>             { "Value" : "Input phone number matches name" } ] },
>
>           { "Group" : "PRIMARY_PHONE",
>            "Name" : "Origination_Spoof_Count",
>            "Values" :
>            [
>             { "Value" : "0" } ] },
>
>           { "Group" : "PRIMARY_PHONE",
>            "Name" : "Spoofed_Count",
>            "Values" :
>            [
>             { "Value" : "0" } ] },
>
>           { "Group" : "PRIMARY_PHONE",
>            "Name" : "Destination_Spoof_Count",
>            "Values" :
>            [
>             { "Value" : "0" } ] },
>
>           { "Group" : "PRIMARY_PHONE",
>            "Name" : "Primary_Phone_Risk_Indicator_Status",
>            "Values" :
>            [
>             { "Value" : "WARN" } ] },
>
>           { "Group" : "PRIMARY_PHONE",
>            "Name" : "Primary_Phone_Risk_Indicator_Messages",
>            "Values" :
>            [
>             { "Value" : "Phone Number First Seen Recently in Digital Identity Network" },
>
>             { "Value" : "Last Seen Date is older than \"365\" days" },
>
>             { "Value" : "Phone linked to identity by self-reported sources only" },
>
>             { "Value" : "Phone Service Type is Wireless" } ] },
>
>           { "Group" : "PRIMARY_PHONE",
>            "Name" : "Primary_Phone_Prepaid",
>            "Values" :
>            [
>             { "Value" : "0" } ] },
>
>           { "Group" : "PRIMARY_PHONE",
>            "Name" : "OTP_Count",
>            "Values" :
>            [
>             { "Value" : "1" } ] },
>
>           { "Group" : "IDENTITY_RECORDS",
>            "Name" : "Consumer_Ownership_at_Carrier_Indicators",
>            "Values" :
>            [
>             { "Value" : "0" } ] },
>
>           { "Group" : "PRIMARY_PHONE",
>            "Name" : "OTP_Last_Year",
>            "Values" :
>            [
>             { "Value" : "2019" } ] },
>
>           { "Group" : "PRIMARY_PHONE",
>            "Name" : "OTP_Last_Month",
>            "Values" :
>            [
>             { "Value" : "07" } ] },
>
>           { "Group" : "PRIMARY_PHONE",
>            "Name" : "OTP_Last_Day",
>            "Values" :
>            [
>             { "Value" : "11" } ] },
>
>           { "Group" : "PRIMARY_PHONE",
>            "Name" : "OTP_Last_Status",
>            "Values" :
>            [
>             { "Value" : "1" } ] },
>
>           { "Group" : "IDENTITY_RECORDS",
>            "Name" : "Consumer_Source_Counts",
>            "Values" :
>            [
>             { "Value" : "1" } ] },
>
>           { "Group" : "IDENTITY_RECORDS",
>            "Name" : "Consumer_Self_Reported_Only",
>            "Values" :
>            [
>             { "Value" : "1" } ] },
>
>           { "Group" : "IDENTITY_RECORDS",
>            "Name" : "Consumer_to_Phone_Sources",
>            "Values" :
>            [
>             { "Value" : "CreditInquiry" } ] },
>
>           { "Group" : "PRIMARY_PHONE",
>            "Name" : "Primary_Phone_Source_Count",
>            "Values" :
>            [
>             { "Value" : "0" } ] },
>
>           { "Group" : "PRIMARY_PHONE",
>            "Name" : "Primary_Phone_Self_Reported_Only",
>            "Values" :
>            [
>             { "Value" : "0" } ] } ] } ] },
>       "tps_was_timeout" : "no" } } },
>    "national_id_number" : "1234",
>    "national_id_type" : "us_ssn4",
>    "org_id" : "3c8qvza7",
>    "policy" : "phone finder",
>    "policy_details_api" :
>    { "policy_detail_api" :
>     [
>      { "type" : "champion",
>       "id" : "0",
>       "customer" :
>       { "score" : "0",
>        "pvid" : "1493204",
>        "review_status" : "pass",
>        "risk_rating" : "neutral",
>        "rules" :
>        [
>         { "rid" : "198139573",
>          "reason_code" : "Execute Phone Finder",
>          "score" : "0" } ] } } ] },
>    "policy_engine_version" : "12.3.1",
>    "policy_score" : "0",
>    "reason_code" :
>    [ "Execute Phone Finder" ],
>    "request_id" : "5c4910b9-7018-4200-8b3b-11de65ff91aa",
>    "request_result" : "success",
>    "review_status" : "pass",
>    "risk_rating" : "neutral",
>    "service_type" : "basic",
>    "tps_was_timeout" : "no" } }
> ```

### Emailage

Evaluate email address metadata points such as domain details, email details, risk indicators, and other PII.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Email textField
>
>   Email of the user
>
> - IP Address textField
>
>   IP Address of the user
>
> - First Name textField
>
>   The customer's first name.
>
> - Last Name textField
>
>   The customer's last name.
>
> - Phone textField
>
>   The customer's phone number, including area code and local exchange. This is used to verify that the customer's phone number is in the same billing location as the cardholder. Most formats are accepted, but ISO E.164 format is highly recommended.
>
> - Secondary Email textField
>
>   If an additional email is available for the transaction, it is sent under this input field. Example: For money transfers, this is the recipient's email. NOTE: We do not provide a score for this email. It is mainly used as supporting data for risk assessment, similar to phone, address, name, etc.
>
> - Is Existing Customer? toggleSwitch
>
>   Indicates if the customer is a repeat customer.
>
> - Customer ID textField
>
>   This parameter can be used as an unique identifier for the customer.
>
> - Tracking ID textField
>
>   The trackingId associated with the original scoring request. This parameter can be used when you want to add an internal system identifier for a query. This identifier will be returned with the results.
>
> - Partner ID textField
>
>   ID used to identify an Emailage Partner.
>
> - Customer Identifier textField
>
>   ID used to identify an Emailage Partner's customer.
>
> - Billing Address textField
>
>   The billing address for the customer.
>
> - Billing City textField
>
>   The billing city for the customer.
>
> - Billing State or Region textField
>
>   The billing state or region for the customer.
>
> - Billing Postal Code textField
>
>   The billing postal (ZIP) code for the customer.
>
> - Billing Country textField
>
>   The billing country for the customer. This can be passed as the full country name or as an ISO 3166-1 alpha-2
>
> - Shipping Address textField
>
>   The shipping address for the customer.
>
> - Shipping City textField
>
>   The shipping city for the customer.
>
> - Shipping State or Region textField
>
>   The shipping state or region for the customer.
>
> - Shipping Postal Code textField
>
>   The shipping postal (ZIP) code for the customer.
>
> - Shipping Country textField
>
>   The shipping country for the customer. This can be passed as the full country name or as an ISO 3166-1 alpha-2
>
> - Card First 6 textField
>
>   The first six digits of a bank card number or payment card number and it is part of ISO/IEC 7812. Used to identify a card brand, issuing institution or bank, country of issuance, card type, and category of cards.
>
> - Transaction Amount textField
>
>   The customer's transaction amount.
>
> - Transaction Currency textField
>
>   The currency used for the customer's transaction as an ISO 4217 code.
>
> - Transaction Origin textField
>
>   Indicates who initiated the transaction. Inbound is where the customer initiates the transaction, and outbound is where the company initiated the transaction.
>
> - User Record ID textField
>
>   This is a user defined Record ID. This parameter can be used when you want to add an identifier for a query. This identifier will be returned with the results.
>
> - Transaction Type ID dropDown
>
>   The Transaction Type ID of the event being scored. Can be used instead of the transactionTypeDescription. Do not enter both the transactionTypeId and the transactionTypeDescription.
>
>   * Account creation (Default)
>
>   * Account login (Default)
>
>   * Email change (Default)
>
>   * Password reset (Default)
>
>   * Purchase (Default)
>
>   * Recurring purchase (Default)
>
>   * Referral (Default)
>
>   * Survey (Default)
>
>   * Job posting (Default)
>
>   * Job application (Default)
>
>   * Promotions (Default)
>
>   * Payment (Default)
>
>   * Banking (Default)
>
>   * Digital (Default)
>
>   * Comment (Default)
>
>   * Insurance (Default)
>
>   * Transaction Other (Default)
>
> - Transaction Type Description dropDown
>
>   The Transaction Type Description of event being scored. Can be used instead of the transactionTypeId. Do not enter both the transactionTypeId and the transactionTypeDescription.
>
>   * Account creation
>
>   * Account login
>
>   * Email change
>
>   * Password reset
>
>   * Purchase
>
>   * Recurring purchase
>
>   * Referral
>
>   * Survey
>
>   * Job posting
>
>   * Job application
>
>   * Promotions
>
>   * Payment
>
>   * Banking
>
>   * Digital
>
>   * Comment
>
>   * Insurance
>
>   * Transaction Other
>
> - Time of Service textField
>
>   Number of days until service.
>
> - Service Date textField
>
>   The date and time of the service. Examples: Traveling - Date of flight, Hospitality - Date of stay, Ticketing - Date of event, Technology/Finance/eCommerce - Date of the service. Date/time parameter must be specified in UTC (Zulu) and be formatted in the ISO8601 style as below: yyyy-mm-ddThh:mm:ssZ (e.g: 2008-09-15T15:53:00Z)
>
> - Service Location textField
>
>   The location of the final service/transaction.
>
> - Service Details textField
>
>   Further detail of the service or transaction.
>
> - Service Category textField
>
>   The general category of the service
>
> - Delivery Type textField
>
>   The type of delivery of the goods or service.
>
> - Useragent textField
>
>   The User-Agent HTTP header.
>
> - Device ID textField
>
>   Vendor code representing the device ID manufacturer used to determine the device ID. NOTE: Send only the 3 digit code. The vendor codes are as follows: 100 - Emailage 110 - 41st Parameter 120 - ThreatMetrix 130 - Iovation 140 - RiskFort 150 - DigitalResolve 160 - RSA 170 - Symantec (Verisign) 180 - Nudata 190 - Kount 200 - InAuth 990 - Other
>
> - Device Source textField
>
>   Vendor code representing the device ID manufacturer used to determine the device ID. NOTE: Send only the 3 digit code. The vendor codes are as follows: 100 - Emailage 110 - 41st Parameter 120 - ThreatMetrix 130 - Iovation 140 - RiskFort 150 - DigitalResolve 160 - RSA 170 - Symantec (Verisign) 180 - Nudata 190 - Kount 200 - InAuth 990 - Other
>
> - User Email textField
>
>   The Emailage username used to make the query. By default, if user\_email is not specified, we use the account's default user and the associated department. If this value is applied, we use the specified user and department. NOTE: This is NOT the email address being queried. If this field is populated with an email other than one authorized to run queries, 3001 errors will be generated
>
> - accept-language HTTP header textField
>
>   The accept-language HTTP header (Language Culture Name).
>
> - Response Language textField
>
>   The language returned in the API response.
>
> * default object
>
>   * properties object
>
>     * apiUrl3 string required
>
>     * clientId string required
>
>     * clientSecret string required
>
>     * email string required
>
>     * ip string
>
>     * firstname string
>
>     * lastname string
>
>     * phone string
>
>     * secondary\_email string
>
>     * existingcustomer boolean
>
>     * customerid string
>
>     * trackingId string
>
>     * partnerid string
>
>     * customeridentifier string
>
>     * billaddress string
>
>     * billcity string
>
>     * billregion string
>
>     * billpostal string
>
>     * billcountry string
>
>     * shipaddress string
>
>     * shipcity string
>
>     * shipregion string
>
>     * shippostal string
>
>     * shipcountry string
>
>     * cardFirstSix string
>
>     * transamount string
>
>     * transcurrency string
>
>     * transorigin string
>
>     * urid string
>
>     * transactionTypeID string/number
>
>     * transactionTypeDescription string
>
>     * time\_to\_service string
>
>     * service\_date string
>
>     * service\_location string
>
>     * service\_detail string
>
>     * service\_category string
>
>     * delivery\_type string
>
>     * useragent string
>
>     * deviceid string
>
>     * devicesource string
>
>     * user\_email string
>
>     * acceptlang string
>
>     * response\_language string
>
> - output object
>
>   * rawResponse object
>
>     * query object
>
>       * email string
>
>       * queryType string
>
>       * count integer
>
>       * created string
>
>       * lang string
>
>       * responseCount integer
>
>       * firstname string
>
>       * lastname string
>
>       * phone string
>
>       * billaddress string
>
>       * billcity string
>
>       * billregion string
>
>       * billpostal string
>
>       * billcountry string
>
>       * results array
>
>     * responseStatus object
>
>       * status string
>
>       * errorCode string
>
>       * description string
>
> Output Example
>
> ```json
>  { "rawResponse" :
>   { "query" :
>    { "email" : "johndoe@example.com",
>     "queryType" : "EmailAgeVerification",
>     "count" : 1,
>     "created" : "2021-10-01T10:44:54Z",
>     "lang" : "en-US",
>     "responseCount" : 1,
>     "firstname" : "John",
>     "lastname" : "Doe",
>     "phone" : "+14055555968",
>     "billaddress" : "1234 asdf asdf",
>     "billcity" : "Los Angeles",
>     "billregion" : "CA",
>     "billpostal" : "23464",
>     "billcountry" : "US",
>     "results" :
>     [
>      { "userdefinedrecordid" : "",
>       "email" : "johndoe@example.com",
>       "eName" : "",
>       "emailAge" : "",
>       "email_creation_days" : "",
>       "domainAge" : "1995-08-13T00:00:00Z",
>       "domain_creation_days" : "9546",
>       "firstVerificationDate" : "2010-07-19T00:00:00Z",
>       "first_seen_days" : "4092",
>       "lastVerificationDate" : "2021-10-01T10:43:02Z",
>       "status" : "Verified",
>       "country" : "",
>       "fraudRisk" : "065 Very Low",
>       "EAScore" : "65",
>       "EAReason" : "Email Created at least 11.2 Years Ago",
>       "EAStatusID" : "2",
>       "EAReasonID" : "14",
>       "EAAdviceID" : "3",
>       "EAAdvice" : "Lower Fraud Risk",
>       "EARiskBandID" : "1",
>       "EARiskBand" : "Fraud Score 1 to 100",
>       "source_industry" : "",
>       "fraud_type" : "",
>       "lastflaggedon" : "",
>       "location" : "",
>       "smfriends" : "",
>       "totalhits" : "4",
>       "uniquehits" : "1",
>       "imageurl" : "",
>       "emailExists" : "Yes",
>       "domainExists" : "Yes",
>       "company" : "",
>       "title" : "",
>       "domainname" : "example.com",
>       "domaincompany" : "Google",
>       "domaincountryname" : "",
>       "domaincategory" : "Webmail",
>       "domaincorporate" : "No",
>       "domainrisklevel" : "Moderate",
>       "domainrelevantinfo" : "Valid Domain",
>       "domainrisklevelID" : "3",
>       "domainrelevantinfoID" : "509",
>       "domaincountrymatch" : "No",
>       "domainriskcountry" : "No",
>       "smlinks" :
>       [  ],
>       "phone_status" : "Valid",
>       "shipforward" : "",
>       "billriskcountry" : "No",
>       "namematch" : "U",
>       "phoneowner" : "",
>       "phoneownertype" : "",
>       "phonecarriertype" : "",
>       "phonecarriernetworkcode" : "",
>       "phonecarriername" : "",
>       "phoneownermatch" : "",
>       "correlationId" : "1ef2273f-bc5b-4949-bcd5-efc681ed1623",
>       "transAmount" : "",
>       "transCurrency" : "" } ] },
>    "responseStatus" :
>    { "status" : "success",
>     "errorCode" : "0",
>     "description" : "" } } }
> ```

### Knowledge-Based Authentication

Challenge users with knowledge-based questions.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Mode dropDown
>
>   Mode in which the transaction should run
>
>   * live
>
>   * testing (Default)
>
>   * simulated
>
> - Locale dropDown
>
>   Language in which the customer wants to receive the response
>
>   * US English
>
>   * Formal Spanish
>
>   * Haitian Creole (only for authentication
>
> - First Name textField
>
>   The primary account holder's first name.
>
> - Middle Name textField
>
>   The primary account holder's middle name
>
> - Last Name textField
>
>   The primary account holder's last name
>
> - Telephone Number textField
>
>   The primary account holder's telephone number. Can contain the following characters: 0-9 , . ; { } ( and ). All braces must be in pairs. White space is removed automatically.
>
> - Account Email textField
>
>   The primary account holder's email address.
>
> - Street Address 1 textField
>
>   The primary account holder's street address 1
>
> - Street Address 2 textField
>
>   The primary account holder's street address 2
>
> - City textField
>
>   The primary account holder's city
>
> - State textField
>
>   The primary account holder's State
>
> - ZIP textField
>
>   The primary account holder's ZIP
>
> - Country textField
>
>   The primary account holder's country, in ISO 3166-1 alpha-2 format, such as "US".
>
> - SSN textField
>
>   Social Security Number
>
> - SSN Type dropDown
>
>   Type of SSN provided
>
>   * ssn4
>
>   * ssn9
>
>   * ssn-first5
>
>   * nossn
>
>   * other
>
> - Day of Birth textField
>
>   Day (DD) Possible values are 1 – 31 .
>
> - Month of Birth textField
>
>   Month (MM) Possible values are numbers 1 – 12 .
>
> - Year of Birth textField
>
>   Year of Birth (YYYY) e.g. 1985, 1958, 2001
>
> - Lex ID textField
>
>   Unique identifier that is assigned to a subject by LexisNexis®. A LexID® number does not include any SPII (sensitive personally identifiable information). Either the LexID number or the indicated name elements are required.
>
> - Simulation Mode dropDown
>
>   An element that governs the response given by RDP This element is required only when Mode is set to simulated .
>
>   * Random
>
>   * Error Simulation Values
>
>   * Communications Error
>
>   * Internal Application\_Error
>
>   * Invalid Information
>
>   * Invalid Login
>
>   * Invalid Mode
>
> - Reference textField
>
>   Internal tracking number that your organization can assign to a transaction.
>
> - GLBA textField
>
>   Integer value based on the GLBA (Gramm-Leach-Bliley Act) that indicates the reason for the request
>
> - DPPA textField
>
>   Integer value pursuant to the DPPA (Driver's Privacy Protection Act) of 1994 that indicates the reason for the request
>
> - Venue dropDown
>
>   Type of environment where the transaction takes place
>
>   * online
>
>   * callcenter
>
>   * batch
>
>   * point-of-sale
>
>   * customer-service
>
>   * ivr
>
> - * Use Custom Screens toggleSwitch
>   * HTML Template textArea
>   * CSS codeEditor
>   * Script codeEditor
>
> * default object
>
>   * properties object
>
>     * apiUrl2 string required
>
>     * username string required
>
>     * password string required
>
>     * accountId string required
>
>     * settingsMode string required
>
>     * SimulationType string
>
>     * Reference string
>
>     * GLBA string
>
>     * DPPA string
>
>     * Locale string required
>
>     * Venue string
>
>     * LexID string
>
>     * day string
>
>     * month string
>
>     * year string
>
>     * account\_first\_name string
>
>     * account\_middle\_name string
>
>     * account\_last\_name string
>
>     * account\_address\_street1 string
>
>     * account\_address\_street2 string
>
>     * account\_address\_city string
>
>     * account\_address\_state string
>
>     * account\_address\_zip string
>
>     * account\_address\_country string
>
>     * account\_email string
>
>     * account\_telephone string
>
>     * ssnNumber string
>
>     * ssnType string
>
> - output object
>
>   * rawResponse object
>
>     * Status object
>
>       * ConversationId string
>
>       * RequestId string
>
>       * TransactionStatus string
>
>       * TransactionReasonCode object
>
>         * Code string
>
>       * LexID string
>
>     * Products array
>
> Output Example
>
> ```json
>  { "rawResponse" :
>   { "Status" :
>    { "ConversationId" : "31000761962129",
>     "RequestId" : "1205338429",
>     "TransactionStatus" : "failed",
>     "TransactionReasonCode" :
>     { "Code" : "failed_iauth_questions" },
>     "LexID" : "1319573870" },
>    "Products" :
>    [
>     { "ProductType" : "Velocity",
>      "ExecutedStepName" : "pre_id_velocity",
>      "ProductConfigurationName" : "GSA_PreID",
>      "ProductStatus" : "pass",
>      "Items" :
>      [
>       { "ItemName" : "FUTILITY",
>        "ItemStatus" : "pass" } ] },
>
>     { "ProductType" : "Discovery",
>      "ExecutedStepName" : "discovery",
>      "ProductConfigurationName" : "GIVE_Discovery",
>      "ProductStatus" : "pass" },
>
>     { "ProductType" : "Velocity",
>      "ExecutedStepName" : "post_id_velocity",
>      "ProductConfigurationName" : "GIVE_PostID",
>      "ProductStatus" : "pass",
>      "Items" :
>      [
>       { "ItemName" : "FREQUENCY",
>        "ItemStatus" : "pass" },
>
>       { "ItemName" : "QUIZ",
>        "ItemStatus" : "pass" } ] },
>
>     { "ProductType" : "IdentityEvent",
>      "ExecutedStepName" : "identity_events",
>      "ProductConfigurationName" : "GIVE_IE",
>      "ProductStatus" : "pass" },
>
>     { "ProductType" : "IIDQA",
>      "ExecutedStepName" : "authentication",
>      "ProductConfigurationName" : "GIVE_KBA",
>      "ProductStatus" : "fail",
>      "ProductReason" :
>      { "Code" : "failed_iauth_questions" } } ] } }
> ```

### One Time Password

Send a one-time password.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Delivery method for the OTP dropDown
>
>   Delivery method for the OTP
>
>   * Text
>
>   * Email
>
> - SMS Body textField
>
>   Defines the custom SMS text body.
>
>   Default:
>
>   ```none
>   Your One Time Password is ${OTP}.${LineBreak}We will never call you for this code.${LineBreak}Your passcode will expire in ${ExpirePeriod} minutes
>   ```
>
> - Email Title textField
>
>   Defines the custom OTP Email Header.
>
>   Default:
>
>   ```none
>   Please, check out this email! It's your one time passcode!
>   ```
>
> - Email Title textField
>
>   Defines the custom OTP Email Body.
>
>   Default:
>
>   ```none
>   Your One Time Passcode is ${OTP}.${LineBreak}We will never call you for this code.${LineBreak}Your passcode will expire in ${ExpirePeriod} minutes
>   ```
>
> - Delivery language for the OTP message dropDown
>
>   Delivery language for the OTP message
>
>   * English
>
>   * French
>
>   * Spanish
>
> - Telephone Number textField
>
>   The primary account holder's telephone number. Can contain the following characters: 0-9 , . ; { } ( and ). All braces must be in pairs. White space is removed automatically.
>
> - Account Email textField
>
>   The primary account holder's email address.
>
> - First Name textField
>
>   The primary account holder's first name.
>
> - Middle Name textField
>
>   The primary account holder's middle name
>
> - Last Name textField
>
>   The primary account holder's last name
>
> - Date of Birth textField
>
>   The primary account holder's date of birth, formatted as YYYYMMDD.
>
> - Gender textField
>
>   The primary account holder's gender.
>
> - Street Address 1 textField
>
>   The primary account holder's street address 1
>
> - Street Address 2 textField
>
>   The primary account holder's street address 2
>
> - City textField
>
>   The primary account holder's city
>
> - State textField
>
>   The primary account holder's State
>
> - ZIP textField
>
>   The primary account holder's ZIP
>
> - Country textField
>
>   The primary account holder's country, in ISO 3166-1 alpha-2 format, such as "US".
>
> - National ID Number textField
>
>   The primary account holder's national ID number. Used for identity verification.
>
> - National ID Type dropDown
>
>   The primary account holder's national ID type. Used for identity verification.
>
>   * US SSN
>
>   * US SSN HASH
>
>   * US SSN4
>
>   * US SSN FIRST5
>
>   * BR CPF
>
>   * MX CURP
>
>   * CO CEDULA
>
> - Telephone Context textField
>
>   The context of the telephone, for e.g.: Mobile
>
> - Telephone GEO textField
>
>   Telephone geolocation, for e.g.: US
>
> - Event Type dropDown
>
>   NOTE: If event\_type is passed to attribute query, it WILL increment velocity counters etc just like a session query. if there is no event\_type on attribute query, it will run but not increment velocity etc counters.
>
>   * Login
>
>   * Payment
>
>   * Account Creation (Default)
>
>   * Transfer
>
>   * Transaction Other
>
>   * Auction Bid
>
>   * Details Change
>
>   * Add Listing
>
>   * Account Balance
>
>   * Transaction History
>
>   * Digital Download
>
>   * Digital Stream
>
> - * Use Custom Screens toggleSwitch
>   * HTML Template textArea
>   * CSS codeEditor
>   * Script codeEditor
>
> * default object
>
>   * properties object
>
>     * apiUrl4 string required
>
>     * orgId2 string required
>
>     * apiKey2 string required
>
>     * event\_type string
>
>     * Method string required
>
>     * SmsBody string
>
>     * EmailTitle string
>
>     * EmailBody string
>
>     * Language string required
>
>     * account\_first\_name string
>
>     * account\_middle\_name string
>
>     * account\_last\_name string
>
>     * account\_date\_of\_birth string
>
>     * account\_gender string
>
>     * account\_address\_street1 string
>
>     * account\_address\_street2 string
>
>     * account\_address\_city string
>
>     * account\_address\_state string
>
>     * account\_address\_zip string
>
>     * account\_address\_country string
>
>     * account\_national\_id\_number string
>
>     * account\_national\_id\_type string
>
>     * account\_email string
>
>     * account\_telephone string
>
>     * account\_telephone\_context string
>
>     * account\_telephone\_geo string
>
> * complete object
>
>   * properties object
>
>     * apiUrl4 string required
>
>     * orgId2 string required
>
>     * apiKey2 string required
>
>     * Method string required
>
>     * Language string required
>
>   * parameters object
>
>     * otp string required
>
> - output object
>
>   * rawResponse object
>
>     * account\_address\_country string
>
>     * account\_email string
>
>     * account\_email\_activities array
>
>     * account\_email\_attributes array
>
>     * account\_email\_first\_seen string
>
>     * account\_email\_last\_event string
>
>     * account\_email\_last\_update string
>
>     * account\_email\_result string
>
>     * account\_email\_score string
>
>     * account\_email\_worst\_score string
>
>     * account\_first\_name string
>
>     * account\_last\_name string
>
>     * account\_middle\_name string
>
>     * account\_name\_activities array
>
>     * account\_name\_attributes array
>
>     * account\_name\_first\_seen string
>
>     * account\_name\_last\_event string
>
>     * account\_name\_last\_update string
>
>     * account\_name\_result string
>
>     * account\_name\_score string
>
>     * account\_name\_worst\_score string
>
>     * action string
>
>     * action\_template string
>
>     * api\_call\_datetime string
>
>     * api\_caller\_ip string
>
>     * api\_type string
>
>     * auth\_method string
>
>     * auth\_status string
>
>     * champion\_request\_duration string
>
>     * enabled\_services array
>
>     * event\_date string
>
>     * event\_datetime string
>
>     * event\_last\_update string
>
>     * event\_type string
>
>     * input\_request\_id string
>
>     * integration\_hub\_results object
>
>       * 11jr7q70:Authentication object
>
>         * Authentication object
>
>           * rule\_id string
>
>           * tps\_datetime string
>
>           * tps\_duration string
>
>           * tps\_error string
>
>           * tps\_result string
>
>           * tps\_type string
>
>           * tps\_vendor string
>
>           * tps\_vendor\_raw\_response object
>
>             * Status object
>
>               * ConversationId string
>
>               * RequestId string
>
>               * TransactionStatus string
>
>               * Reference string
>
>             * InputEcho array
>
>             * Products array
>
>           * tps\_was\_timeout string
>
>     * national\_id\_type null
>
>     * org\_id string
>
>     * original\_event\_created string
>
>     * original\_event\_updated string
>
>     * policy string
>
>     * policy\_details\_api object
>
>       * policy\_detail\_api array
>
>     * policy\_engine\_version string
>
>     * policy\_score string
>
>     * primary\_industry string
>
>     * reason\_code array
>
>     * request\_duration string
>
>     * request\_id string
>
>     * request\_id\_activities array
>
>     * request\_result string
>
>     * review\_status string
>
>     * risk\_rating string
>
>     * secondary\_industry string
>
>     * service\_type string
>
>     * summary\_risk\_score string
>
>     * tmx\_reason\_code array
>
>     * tmx\_risk\_rating string
>
>     * tps\_datetime string
>
>     * tps\_duration string
>
>     * tps\_error string
>
>     * tps\_result string
>
>     * tps\_type string
>
>     * tps\_vendor string
>
>     * tps\_vendor\_raw\_response string
>
>     * tps\_was\_timeout string
>
> Output Example
>
> ```json
>  { "rawResponse" :
>   { "account_address_country" : "us",
>    "account_email" : "john@doe.com",
>    "account_email_activities" :
>    [ "_CHALLENGED" ],
>    "account_email_attributes" :
>    [ "_CHALLENGED" ],
>    "account_email_first_seen" : "2021-10-12",
>    "account_email_last_event" : "2021-10-18",
>    "account_email_last_update" : "2021-10-18",
>    "account_email_result" : "success",
>    "account_email_score" : "0",
>    "account_email_worst_score" : "0",
>    "account_first_name" : "John",
>    "account_last_name" : "Doe",
>    "account_middle_name" : "",
>    "account_name_activities" :
>    [ "_CHALLENGED" ],
>    "account_name_attributes" :
>    [ "_CHALLENGED" ],
>    "account_name_first_seen" : "2020-07-30",
>    "account_name_last_event" : "2021-10-18",
>    "account_name_last_update" : "2021-10-18",
>    "account_name_result" : "success",
>    "account_name_score" : "0",
>    "account_name_worst_score" : "0",
>    "action" : "response",
>    "action_template" : "default_accept",
>    "api_call_datetime" : "2021-10-18 10:43:50.321",
>    "api_caller_ip" : "44.240.16.43",
>    "api_type" : "authentication",
>    "auth_method" : "otp",
>    "auth_status" : "authentication_success",
>    "champion_request_duration" : "631",
>    "enabled_services" :
>    [ "TMX100" ],
>    "event_date" : "2021-10-18 10:00:00",
>    "event_datetime" : "2021-10-18 10:43:50.321",
>    "event_last_update" : "2021-10-18 10:00:00",
>    "event_type" : "init_auth",
>    "input_request_id" : "5120df86-801e-450f-b854-abbc85225590",
>    "integration_hub_results" :
>    { "11jr7q70:Authentication" :
>     { "Authentication" :
>      { "rule_id" : "206676243",
>       "tps_datetime" : "2021-10-18 10:43:50.326",
>       "tps_duration" : "629",
>       "tps_error" : "passed",
>       "tps_result" : "ok",
>       "tps_type" : "LN_RDP_Auth_Hub_Continue",
>       "tps_vendor" : "LexisNexis - Connectors",
>       "tps_vendor_raw_response" :
>       { "Status" :
>        { "ConversationId" : "31000768645499",
>         "RequestId" : "1217029359",
>         "TransactionStatus" : "passed",
>         "Reference" : "Reference1" },
>        "InputEcho" :
>        [
>         { "Type" : "Initiate",
>          "Persons" :
>          [
>           { "Addresses" :
>            [
>             { "Context" : "primary",
>              "Country" : "us" } ],
>            "Context" : "primary",
>            "Emails" :
>            [ "john@doe.com" ],
>            "Name" :
>            { "FirstName" : "John",
>             "LastName" : "Doe",
>             "MiddleName" : "" } } ] } ],
>        "Products" :
>        [
>         { "ProductType" : "OTP",
>          "ExecutedStepName" : "auth_select",
>          "ProductConfigurationName" : "TMX_Test_OTP",
>          "ProductStatus" : "pass" } ] },
>       "tps_was_timeout" : "no" } } },
>    "national_id_type" : null,
>    "org_id" : "2234ds24f",
>    "original_event_created" : "2021-10-18 10:00:00",
>    "original_event_updated" : "2021-10-18 10:00:00",
>    "policy" : "authentication",
>    "policy_details_api" :
>    { "policy_detail_api" :
>     [
>      { "type" : "champion",
>       "id" : "0",
>       "customer" :
>       { "score" : "0",
>        "pvid" : "1512519",
>        "review_status" : "pass",
>        "risk_rating" : "neutral",
>        "rules" :
>        [
>         { "rid" : "206676243",
>          "reason_code" : "Authentication",
>          "score" : "0" } ] } } ] },
>    "policy_engine_version" : "12.5",
>    "policy_score" : "0",
>    "primary_industry" : "fintech",
>    "reason_code" :
>    [ "Authentication" ],
>    "request_duration" : "636",
>    "request_id" : "ef94941c-8c6a-4295-aa37-18a840dff665",
>    "request_id_activities" :
>    [ "_CHALLENGED" ],
>    "request_result" : "success",
>    "review_status" : "pass",
>    "risk_rating" : "neutral",
>    "secondary_industry" : "platform",
>    "service_type" : "all",
>    "summary_risk_score" : "0",
>    "tmx_reason_code" :
>    [ "_ACC_EMAIL_GBL_VEL_6_7_8_8",
>     "_ACC_EMAIL_GBL_AGE_GT_DY",
>     "_ACC_NAME_GBL_VEL_6_7_8_8",
>     "_ACC_NAME_GBL_AGE_GT_3MTHS",
>     "_ACC_EMAIL_LCL_VEL_6_7_8_8",
>     "_ACC_EMAIL_LCL_AGE_GT_DY",
>     "_ACC_NAME_LCL_VEL_6_7_8_8",
>     "_ACC_NAME_LCL_AGE_GT_DY",
>     "_EXPRESSION_ERROR" ],
>    "tmx_risk_rating" : "neutral",
>    "tps_datetime" : "2021-10-18 10:43:50.326",
>    "tps_duration" : "629",
>    "tps_error" : "passed",
>    "tps_result" : "ok",
>    "tps_type" : "LN_RDP_Auth_Hub_Continue",
>    "tps_vendor" : "LexisNexis - Connectors",
>    "tps_vendor_raw_response" : "{\"Status\":{\"ConversationId\":\"31000768645499\",\"RequestId\":\"1217029359\",\"TransactionStatus\":\"passed\",\"Reference\":\"Reference1\"},\"InputEcho\":[{\"Type\":\"Initiate\",\"Persons\":[{\"Addresses\":[{\"Context\":\"primary\",\"Country\":\"us\"}],\"Context\":\"primary\",\"Emails\":[\"johndoe@example.com\"],\"Name\":{\"FirstName\":\"John\",\"LastName\":\"Doe\",\"MiddleName\":\"Joe\"}}]}],\"Products\":[{\"ProductType\":\"OTP\",\"ExecutedStepName\":\"auth_select\",\"ProductConfigurationName\":\"TMX_Test_OTP\",\"ProductStatus\":\"pass\"}]}",
>    "tps_was_timeout" : "no" } }
> ```

### Knowledge-Based Authentication (Authentication Project)

Challenge users with knowledge-based questions.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - First Name textField
>
>   The primary account holder's first name.
>
> - Middle Name textField
>
>   The primary account holder's middle name
>
> - Last Name textField
>
>   The primary account holder's last name
>
> - Telephone Number textField
>
>   The primary account holder's telephone number. Can contain the following characters: 0-9 , . ; { } ( and ). All braces must be in pairs. White space is removed automatically.
>
> - Account Email textField
>
>   The primary account holder's email address.
>
> - Date of Birth textField
>
>   The primary account holder's date of birth, formatted as YYYYMMDD.
>
> - Gender textField
>
>   The primary account holder's gender.
>
> - Street Address 1 textField
>
>   The primary account holder's street address 1
>
> - Street Address 2 textField
>
>   The primary account holder's street address 2
>
> - City textField
>
>   The primary account holder's city
>
> - State textField
>
>   The primary account holder's State
>
> - ZIP textField
>
>   The primary account holder's ZIP
>
> - Country textField
>
>   The primary account holder's country, in ISO 3166-1 alpha-2 format, such as "US".
>
> - National ID Number textField
>
>   The primary account holder's national ID number. Used for identity verification.
>
> - National ID Type dropDown
>
>   The primary account holder's national ID type. Used for identity verification.
>
>   * US SSN
>
>   * US SSN HASH
>
>   * US SSN4
>
>   * US SSN FIRST5
>
>   * BR CPF
>
>   * MX CURP
>
>   * CO CEDULA
>
> - Telephone Context textField
>
>   The context of the telephone, for e.g.: Mobile
>
> - Telephone GEO textField
>
>   Telephone geolocation, for e.g.: US
>
> - Event Type dropDown
>
>   NOTE: If event\_type is passed to attribute query, it WILL increment velocity counters etc just like a session query. if there is no event\_type on attribute query, it will run but not increment velocity etc counters.
>
>   * Login
>
>   * Payment
>
>   * Account Creation (Default)
>
>   * Transfer
>
>   * Transaction Other
>
>   * Auction Bid
>
>   * Details Change
>
>   * Add Listing
>
>   * Account Balance
>
>   * Transaction History
>
>   * Digital Download
>
>   * Digital Stream
>
> - * Use Custom Screens toggleSwitch
>   * HTML Template textArea
>   * CSS codeEditor
>   * Script codeEditor
>
> * default object
>
>   * properties object
>
>     * apiUrl4 string required
>
>     * orgId2 string required
>
>     * apiKey2 string required
>
>     * event\_type string
>
>     * account\_first\_name string
>
>     * account\_middle\_name string
>
>     * account\_last\_name string
>
>     * account\_date\_of\_birth string
>
>     * account\_gender string
>
>     * account\_address\_street1 string
>
>     * account\_address\_street2 string
>
>     * account\_address\_city string
>
>     * account\_address\_state string
>
>     * account\_address\_zip string
>
>     * account\_address\_country string
>
>     * account\_national\_id\_number string
>
>     * account\_national\_id\_type string
>
>     * account\_email string
>
>     * account\_telephone string
>
>     * account\_telephone\_context string
>
>     * account\_telephone\_geo string
>
> - output object
>
>   * rawResponse object
>
>     * account\_address\_city string
>
>     * account\_address\_country string
>
>     * account\_address\_state string
>
>     * account\_address\_street1 string
>
>     * account\_email string
>
>     * account\_first\_name string
>
>     * account\_last\_name string
>
>     * auth\_method string
>
>     * auth\_status string
>
>     * event\_datetime string
>
>     * event\_type string
>
>     * answers object
>
>       * QuestionSetId string
>
>       * Questions array
>
>     * input\_request\_id string
>
>     * original\_event\_created string
>
>     * original\_event\_updated string
>
>     * policy string
>
>     * policy\_engine\_version string
>
>     * policy\_site\_id string
>
>     * request\_duration string
>
>     * request\_id string
>
>     * request\_result string
>
>     * review\_status string
>
> Output Example
>
> ```json
>  { "rawResponse" :
>   { "account_address_city" : "Los Angeles",
>    "account_address_country" : "us",
>    "account_address_state" : "ca",
>    "account_address_street1" : "12434 SOmething ave",
>    "account_email" : "jon@doe.com",
>    "account_first_name" : "jon",
>    "account_last_name" : "doe",
>    "auth_method" : "kba",
>    "auth_status" : "authentication_success",
>    "event_datetime" : "2021-10-22 06:41:27.055",
>    "event_type" : "init_auth",
>    "answers" :
>    { "QuestionSetId" : "2331385118",
>     "Questions" :
>     [
>      { "QuestionId" : "3054678218",
>       "Choices" :
>       [
>        { "Choice" : "6178344158" } ] } ] },
>    "input_request_id" : "257f5956-68c2-4f2e-b932-391f6aebe2b8",
>    "original_event_created" : "2021-10-22 06:00:00",
>    "original_event_updated" : "2021-10-22 06:00:00",
>    "policy" : "authentication",
>    "policy_engine_version" : "12.5",
>    "policy_site_id" : "P2/otin102.prod.sac",
>    "request_duration" : "427",
>    "request_id" : "471df61e-b1ac-4fb0-b5d5-5cfc24ffeb91",
>    "request_result" : "success",
>    "review_status" : "pass" } }
> ```

### TrueID: Verify Document

Verify user identities with government ID validation and selfie liveness checks.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Mode dropDown
>
>   Mode in which the transaction should run
>
>   * live
>
>   * testing (Default)
>
>   * simulated
>
> - Locale dropDown
>
>   Language in which the customer wants to receive the response
>
>   * US English
>
>   * Formal Spanish
>
>   * Haitian Creole (only for authentication
>
> - Simulation Mode dropDown
>
>   An element that governs the response given by RDP This element is required only when Mode is set to simulated .
>
>   * Random
>
>   * Error Simulation Values
>
>   * Communications Error
>
>   * Internal Application\_Error
>
>   * Invalid Information
>
>   * Invalid Login
>
>   * Invalid Mode
>
> - Venue dropDown
>
>   Type of environment where the transaction takes place
>
>   * online
>
>   * callcenter
>
>   * batch
>
>   * point-of-sale
>
>   * customer-service
>
>   * ivr
>
> - Workflow dropDown
>
>   Type of workflow
>
>   * ID (Default)
>
>   * ID + Selfie
>
> - * Use Custom Screens toggleSwitch
>   * HTML Template textArea
>   * CSS codeEditor
>   * Script codeEditor
>   * HTML Template textArea
>   * CSS codeEditor
>   * Script codeEditor
>
> * default object
>
>   * properties object
>
>     * trueIdUsername string
>
>     * trueIdPassword string
>
>     * acasEndpoint string
>
>     * acuantJavascriptWebSdkScriptSource string
>
>     * acuantConfigurationScript string
>
>     * acuantJavascriptWebSdkScript string
>
>     * acuantCameraScript string
>
>     * acuantPassiveLivenessScript string
>
>     * openCvScript string
>
>     * apiUrl2 string
>
>     * username string
>
>     * password string
>
>     * accountId string
>
>     * settingsMode string
>
>     * SimulationType string
>
>     * Reference string
>
>     * Locale string
>
>     * Venue string
>
>     * workflowType string
>
> - output object
>
>   * rawResponse object
>
>     * Status object
>
>       * ConversationId string
>
>       * RequestId string
>
>       * TransactionStatus string
>
>     * Products array
>
>   * frontImageFileName string
>
>   * backImageFileName string
>
>   * selfieImageFileName string
>
> Output Example
>
> ```json
>  { "rawResponse" :
>   { "Status" :
>    { "ConversationId" : "31000804638459",
>     "RequestId" : "1275210509",
>     "TransactionStatus" : "passed" },
>    "Products" :
>    [
>     { "ProductType" : "TrueID",
>      "ExecutedStepName" : "True_ID_Step",
>      "ProductConfigurationName" : "GIVE_TrueID",
>      "ProductStatus" : "pass",
>      "ParameterDetails" :
>      [
>       { "Group" : "AUTHENTICATION_RESULT",
>        "Name" : "DocumentName",
>        "Values" :
>        [
>         { "Value" : "US Passport" } ] },
>
>       { "Group" : "AUTHENTICATION_RESULT",
>        "Name" : "DocAuthResult",
>        "Values" :
>        [
>         { "Value" : "Passed" } ] },
>
>       { "Group" : "AUTHENTICATION_RESULT",
>        "Name" : "DocIssuerCode",
>        "Values" :
>        [
>         { "Value" : "USA" } ] },
>
>       { "Group" : "AUTHENTICATION_RESULT",
>        "Name" : "DocIssuerName",
>        "Values" :
>        [
>         { "Value" : "USA" } ] },
>
>       { "Group" : "AUTHENTICATION_RESULT",
>        "Name" : "DocIssuerType",
>        "Values" :
>        [
>         { "Value" : "Country" } ] },
>
>       { "Group" : "AUTHENTICATION_RESULT",
>        "Name" : "DocClassCode",
>        "Values" :
>        [
>         { "Value" : "Passport" } ] },
>
>       { "Group" : "AUTHENTICATION_RESULT",
>        "Name" : "DocClass",
>        "Values" :
>        [
>         { "Value" : "Passport" } ] },
>
>       { "Group" : "AUTHENTICATION_RESULT",
>        "Name" : "DocClassName",
>        "Values" :
>        [
>         { "Value" : "Passport" } ] },
>
>       { "Group" : "AUTHENTICATION_RESULT",
>        "Name" : "DocIsGeneric",
>        "Values" :
>        [
>         { "Value" : "false" } ] },
>
>       { "Group" : "AUTHENTICATION_RESULT",
>        "Name" : "DocIssue",
>        "Values" :
>        [
>         { "Value" : "2014" } ] },
>
>       { "Group" : "AUTHENTICATION_RESULT",
>        "Name" : "DocIssueType",
>        "Values" :
>        [
>         { "Value" : "Passport" } ] },
>
>       { "Group" : "AUTHENTICATION_RESULT",
>        "Name" : "DocSize",
>        "Values" :
>        [
>         { "Value" : "ID3" } ] },
>
>       { "Group" : "AUTHENTICATION_RESULT",
>        "Name" : "ClassificationMode",
>        "Values" :
>        [
>         { "Value" : "Automatic" } ] },
>
>       { "Group" : "AUTHENTICATION_RESULT",
>        "Name" : "OrientationChanged",
>        "Values" :
>        [
>         { "Value" : "false" } ] },
>
>       { "Group" : "AUTHENTICATION_RESULT",
>        "Name" : "PresentationChanged",
>        "Values" :
>        [
>         { "Value" : "false" } ] },
>
>       { "Group" : "IMAGE_METRICS_RESULT",
>        "Name" : "Side",
>        "Values" :
>        [
>         { "Value" : "Front" } ] },
>
>       { "Group" : "IMAGE_METRICS_RESULT",
>        "Name" : "GlareMetric",
>        "Values" :
>        [
>         { "Value" : "99" } ] },
>
>       { "Group" : "IMAGE_METRICS_RESULT",
>        "Name" : "SharpnessMetric",
>        "Values" :
>        [
>         { "Value" : "78" } ] },
>
>       { "Group" : "IMAGE_METRICS_RESULT",
>        "Name" : "IsTampered",
>        "Values" :
>        [
>         { "Value" : "0" } ] },
>
>       { "Group" : "IMAGE_METRICS_RESULT",
>        "Name" : "IsCropped",
>        "Values" :
>        [
>         { "Value" : "0" } ] },
>
>       { "Group" : "IMAGE_METRICS_RESULT",
>        "Name" : "HorizontalResolution",
>        "Values" :
>        [
>         { "Value" : "454" } ] },
>
>       { "Group" : "IMAGE_METRICS_RESULT",
>        "Name" : "VerticalResolution",
>        "Values" :
>        [
>         { "Value" : "454" } ] },
>
>       { "Group" : "IMAGE_METRICS_RESULT",
>        "Name" : "Light",
>        "Values" :
>        [
>         { "Value" : "White" } ] },
>
>       { "Group" : "IMAGE_METRICS_RESULT",
>        "Name" : "MimeType",
>        "Values" :
>        [
>         { "Value" : "image/jpeg" } ] },
>
>       { "Group" : "IDAUTH_FIELD_DATA",
>        "Name" : "Fields_DOB_Month",
>        "Values" :
>        [
>         { "Value" : "8" } ] },
>
>       { "Group" : "IDAUTH_FIELD_DATA",
>        "Name" : "Fields_DOB_Day",
>        "Values" :
>        [
>         { "Value" : "16" } ] },
>
>       { "Group" : "IDAUTH_FIELD_DATA",
>        "Name" : "Fields_BirthPlace",
>        "Values" :
>        [
>         { "Value" : "Los Angeles" } ] },
>
>       { "Group" : "IDAUTH_FIELD_DATA",
>        "Name" : "Fields_DocumentClassCode",
>        "Values" :
>        [
>         { "Value" : "P" } ] },
>
>       { "Group" : "IDAUTH_FIELD_DATA",
>        "Name" : "Fields_DocumentClassName",
>        "Values" :
>        [
>         { "Value" : "Passport" } ] },
>
>       { "Group" : "IDAUTH_FIELD_DATA",
>        "Name" : "Fields_DocumentNumber",
>        "Values" :
>        [
>         { "Value" : "234345354" } ] },
>
>       { "Group" : "IDAUTH_FIELD_DATA",
>        "Name" : "Fields_ExpirationDate_Year",
>        "Values" :
>        [
>         { "Value" : "2023" } ] },
>
>       { "Group" : "IDAUTH_FIELD_DATA",
>        "Name" : "Fields_ExpirationDate_Month",
>        "Values" :
>        [
>         { "Value" : "2" } ] },
>
>       { "Group" : "IDAUTH_FIELD_DATA",
>        "Name" : "Fields_xpirationDate_Day",
>        "Values" :
>        [
>         { "Value" : "21" } ] },
>
>       { "Group" : "IDAUTH_FIELD_DATA",
>        "Name" : "Fields_IssuingAuthority",
>        "Values" :
>        [
>         { "Value" : "DEPARTMENT OF PASSPORT" } ] },
>
>       { "Group" : "IDAUTH_FIELD_DATA",
>        "Name" : "Fields_IssuingStateCode",
>        "Values" :
>        [
>         { "Value" : "USA" } ] },
>
>       { "Group" : "IDAUTH_FIELD_DATA",
>        "Name" : "Fields_IssuingStateName",
>        "Values" :
>        [
>         { "Value" : "USA" } ] },
>
>       { "Group" : "IDAUTH_FIELD_DATA",
>        "Name" : "Fields_CountryCode",
>        "Values" :
>        [
>         { "Value" : "USA" } ] },
>
>       { "Group" : "IDAUTH_FIELD_DATA",
>        "Name" : "Fields_Sex",
>        "Values" :
>        [
>         { "Value" : "M" } ] },
>
>       { "Group" : "IDAUTH_FIELD_DATA",
>        "Name" : "Fields_IssueDate_Year",
>        "Values" :
>        [
>         { "Value" : "2018" } ] },
>
>       { "Group" : "IDAUTH_FIELD_DATA",
>        "Name" : "Fields_IssueDate_Month",
>        "Values" :
>        [
>         { "Value" : "6" } ] },
>
>       { "Group" : "IDAUTH_FIELD_DATA",
>        "Name" : "Fields_IssueDate_Day",
>        "Values" :
>        [
>         { "Value" : "10" } ] },
>
>       { "Group" : "IDAUTH_FIELD_DATA",
>        "Name" : "Fields_MRZ",
>        "Values" :
>        [
>         { "Value" : "P<DOFO)#<<Doe<Joe<<<<<<<<<<<<<<<<<<<<<<e3rert<324fc9f8gj3bve <<<42" } ] },
>
>       { "Group" : "IDAUTH_FIELD_DATA",
>        "Name" : "Fields_NationalityCode",
>        "Values" :
>        [
>         { "Value" : "USA" } ] },
>
>       { "Group" : "IDAUTH_FIELD_DATA",
>        "Name" : "Fields_NationalityName",
>        "Values" :
>        [
>         { "Value" : "US" } ] },
>
>       { "Group" : "IDAUTH_FIELD_DATA",
>        "Name" : "Fields_PersonalNumber",
>        "Values" :
>        [
>         { "Value" : "345456456" } ] },
>
>       { "Group" : "PORTRAIT_MATCH_RESULT",
>        "Name" : "FaceMatchResult",
>        "Values" :
>        [
>         { "Value" : "Pass" } ] },
>
>       { "Group" : "PORTRAIT_MATCH_RESULT",
>        "Name" : "FaceMatchScore",
>        "Values" :
>        [
>         { "Value" : "95" } ] },
>
>       { "Group" : "PORTRAIT_MATCH_RESULT",
>        "Name" : "FaceStatusCode",
>        "Values" :
>        [
>         { "Value" : "1" } ] },
>
>       { "Group" : "PORTRAIT_MATCH_RESULT",
>        "Name" : "FaceErrorMessage",
>        "Values" :
>        [
>         { "Value" : "Successful. Liveness: Live" } ] } ] } ] } }
> ```

### TrueID: Delete Document

Delete government documents from LexisNexis.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Delete Front Image dropDown
>
>   * Yes (Default)
>
>   * No
>
> - Delete Back Image dropDown
>
>   * Yes (Default)
>
>   * No
>
> - Delete Selfie Image dropDown
>
>   * Yes (Default)
>
>   * No
>
> * default object
>
>   * properties object
>
>     * deleteFrontImage string
>
>     * deleteBackImage string
>
>     * deleteSelfieImage string
>
> - output object
>
>   * rawResponse object
>
>     * frontImageDeleted boolean
>
>     * backImageDeleted boolean
>
>     * selfieImageDeleted boolean
>
> Output Example
>
> ```json
>  { "rawResponse" :
>   { "frontImageDeleted" : true,
>    "backImageDeleted" : true,
>    "selfieImageDeleted" : true } }
> ```