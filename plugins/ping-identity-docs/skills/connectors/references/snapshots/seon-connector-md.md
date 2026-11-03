---
title: SEON Connector
description: Configure the SEON connector in PingOne DaVinci to detect fraud using device fingerprinting, request fraud scores, and send feedback to SEON
component: connectors
page_id: connectors::seon_connector
canonical_url: https://docs.pingidentity.com/connectors/seon_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-09T00:00:00Z
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  setting-up-seon: Setting up SEON
  configuring-the-seon-connector: Configuring the SEON connector
  connector-configuration: Connector configuration
  license-key: License Key
  api-base-url: API Base URL
  using-the-connector-in-a-flow: Using the connector in a flow
  fraud-score-request: Fraud score request
  feedback: Feedback
  creating-a-custom-api-call: Creating a custom API call
  capabilities: Capabilities
  request-fraud-score: Request Fraud Score
  send-feedback: Send Feedback
  make-custom-api-call: Make Custom API Call
---

# SEON Connector

The SEON connector lets you uncover fraud patterns through SEON's device fingerprinting and intelligent insights in your PingOne DaVinci flow.

You can use the SEON connector to:

* Request a fraud score from SEON.

* Send feedback to SEON.

## Setup

### Resources

Learn more in the following:

* SEON documentation:

  * [Getting Started](https://docs.seon.io/getting-started)

  * [API Reference](https://docs.seon.io/api-reference)

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* A SEON license

* Your SEON credentials

### Setting up SEON

Follow the instructions in [Getting Started](https://docs.seon.io/getting-started).

### Configuring the SEON connector

Add the connector in PingOne DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

##### License Key

Your SEON license key. Learn more in the [API Reference](https://docs.seon.io/api-reference).

##### API Base URL

The API URL to target.

## Using the connector in a flow

### Fraud score request

You can use the **Request Fraud Score** capability to get the fraud score for submitted data.

No special configuration is needed. Add the capability and populate its properties according to the help text.

### Feedback

You can use the **Send Feedback** capability to send feedback to SEON to improve their fraud identification.

No special configuration is needed. Add the capability and populate its properties according to the help text.

### Creating a custom API call

If you want to do something that isn't supported by one of the provided capabilities, you can use the **Make a Custom API Call** capability to define your own action.

This capability uses the credentials from your connector to make an API call with the HTTP method, headers, query parameters, and body you specify.

## Capabilities

### Request Fraud Score

Get the fraud score for data submitted.

> **Collapse: Show details**
>
> * * Properties
>   * Config Type `dropDown` `required`
>
>   The configuration type. Can be either Multiselect or JSON.
>
>   * Multiselect (Default)
>
>   * JSON
>
> * Config `dropDownMultiSelect`
>
>   * Email
>
>   * Phone Number (19 Digits Limit)
>
>   * IP
>
>   * AML
>
>   * Device Fingerprinting
>
> * Config Response Fields `dropDownMultiSelect`
>
>   * ID
>
>   * State
>
>   * Fraud Score
>
>   * IP Details
>
>   * Email Details
>
>   * Phone Details
>
>   * BIN Details
>
>   * Version
>
>   * Applied Rules
>
>   * Device Details
>
>   * Calculation Time
>
>   * SEON ID
>
>   * Rule Category Details
>
>   * Blackbox Score
>
>   * Geolocation Details
>
> * Config `textArea`
>
>   JSON config
>
> * User `selectNameValueListColumn`
>
>   * Email
>
>   * Phone Number (19 Digits Limit)
>
>   * Password Hash
>
>   * Email Address Domain
>
>   * User Full Name
>
>   * Username
>
>   * User First Name
>
>   * User Middle Name
>
>   * User Last Name
>
>   * User Place of Birth
>
>   * User Photo ID Number
>
>   * User ID
>
>   * User Created
>
>   * User Category
>
>   * User Account Status
>
>   * User Bank Account Number
>
>   * User Bank
>
>   * User Bank Account Balance
>
>   * User Verification Level
>
>   * User Date of Birth (YYYY-MM-DD)
>
>   * User Country
>
>   * User City
>
>   * User Region
>
>   * User Zip Code
>
>   * User Address Line 1
>
>   * User Address Line 2
>
>   * Action Type
>
>   * IP
>
>   * Affiliate ID
>
>   * Affiliate Name
>
>   * Session ID (64 Characters Limit)
>
>   * Session
>
>   * Device ID
>
> * Payment `selectNameValueListColumn`
>
>   * Receiver Full Name
>
>   * Receiver Bank Account Number
>
>   * Details URL
>
>   * Payment Method
>
>   * Payment Provider
>
>   * Card Full Name
>
>   * Card Bin (15 Characters Limit)
>
>   * Card Hash (500 Characters Limit)
>
>   * Card Expiration Date (YYYY-MM-DD)
>
>   * Card Last Four Digits
>
>   * AVS Result
>
>   * CVV Result
>
>   * Transaction Type
>
>   * Transaction Amount
>
>   * Transaction Currency (4 Characters Limit)
>
>   * Status of 3D Secure Results
>
>   * Payment ID
>
> * E-commerce `selectNameValueListColumn`
>
>   * Shipping Country
>
>   * Shipping City
>
>   * Shipping Region
>
>   * Shipping Zip Code
>
>   * Shipping Address
>
>   * Shipping Address Line 2
>
>   * Shipping Phone Number
>
>   * Shipping Full Name
>
>   * Shipping Method (50 Characters Limit)
>
>   * Gift
>
>   * Gift Message
>
>   * Merchant Category
>
>   * Merchant ID
>
>   * Merchant Created At
>
>   * Merchant Country
>
>   * Regulation
>
>   * Bonus Campaign ID
>
>   * Brand ID
>
>   * Order Memo
>
>   * Discount Code (50 Characters Limit)
>
>   * Items
>
> * Billing `selectNameValueListColumn`
>
>   * Billing Country
>
>   * Billing City
>
>   * Billing Region
>
>   * Billing Zip Code
>
>   * Billing Address Line
>
>   * Billing Address Line 2
>
>   * Billing Phone Number
>
> * Others `selectNameValueListColumn`
>
>   * Action Type
>
>   * Transaction ID (255 Characters Limit)
>
>   * SCA Method
>
> * Custom Fields `keyValueList`
>
>   You can use unlimited custom fields to inform our machine learning system and scoring engine. These can be string, boolean and numeric, for example is_intangible_item, is_pay_on_delivery, departure_airport, arrival_airport, days_to_board
>
> - - Output Schema
>   - output `object`
>   - rawResponse `object`
>   - properties `object`
>   - success `boolean`
>   - error `object`
>   - data `object`
>   - properties `object`
>
>   * * id `string`
>     * state `string`
>     * fraud_score `number`
>     * bin_details `object`
>     * properties `object`
>
> - * card_bin `string`
>   * bin_bank `string`
>   * bin_card `string`
>   * bin_type `string`
>   * bin_level `string`
>   * bin_country `string`
>   * bin_country_code `string`
>   * bin_website `string`
>   * bin_phone `string`
>   * bin_valid `boolean`
>   * card_issuer `string`
>
>   - - version `string`
>     - applied_rules `array`
>     - items `array`
>
> - * type `object`
>   * properties
>
>   - - calculation_time `number`
>     - seon_id `number`
>     - ip_details `object`
>     - properties `object`
>
> - * success `boolean`
>   * error `object`
>   * data `object`
>   * properties `object`
>   * ip `string`
>   * score `number`
>   * country `string`
>   * state_prov `string`
>   * city `string`
>   * timezone_offset `string`
>   * isp_name `string`
>   * latitude `number`
>   * longitude `number`
>   * type `string`
>   * open_ports `array`
>   * items `array`
>
>   - type `integer`
>
> - * tor `boolean`
>   * harmful `boolean`
>   * vpn `boolean`
>   * web_proxy `boolean`
>   * public_proxy `boolean`
>   * spam_number `integer`
>   * spam_urls `array`
>   * items `array`
>
>   - type `string`
>
> - * applied_rules `array`
>   * items `array`
>
>   - - type `object`
>     - properties
>
> - * history `object`
>   * properties `object`
>
>   - - hits `integer`
>     - customer_hits `integer`
>     - first_seen `integer`
>     - last_seen `integer`
>
> - * flags `array`
>   * items `array`
>
>   - - type `object`
>     - properties
>
> - id `string`
>
>   * * email_details `object`
>     * properties `object`
>
> - * email `string`
>   * score `number`
>   * deliverable `boolean`
>   * domain_details `object`
>   * properties `object`
>   * domain `string`
>   * tld `string`
>   * registered `boolean`
>   * created `string`
>   * updated `string`
>   * expires `string`
>   * registrar_name `string`
>   * registered_to `string`
>   * disposable `boolean`
>   * free `boolean`
>   * custom `boolean`
>   * dmarc_enforced `boolean`
>   * spf_strict `boolean`
>   * valid_mx `boolean`
>   * accept_all `boolean`
>   * suspicious_tld `boolean`
>   * website_exists `boolean`
>   * account_details `object`
>   * properties `object`
>   * apple `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * ebay `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * facebook `object`
>   * properties `object`
>
>   - - registered `boolean`
>     - url `string`
>     - name `string`
>     - photo `string`
>
> - * flickr `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * foursquare `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * github `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * google `object`
>   * properties `object`
>
>   - - registered `boolean`
>     - photo `string`
>
> - * gravatar `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * instagram `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * lastfm `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * linkedin `object`
>   * properties `object`
>
>   - - registered `boolean`
>     - url `string`
>     - name `string`
>     - company `string`
>     - title `string`
>     - location `string`
>     - website `string`
>     - twitter `string`
>     - photo `string`
>
> - * microsoft `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * myspace `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * pinterest `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * skype `object`
>   * properties `object`
>
>   - - registered `boolean`
>     - country `string`
>     - city `string`
>     - gender `string`
>     - name `string`
>     - id `string`
>     - handle `string`
>     - bio `string`
>     - age `number`
>     - language `string`
>     - state `string`
>     - photo `string`
>
> - * spotify `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * tumblr `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * twitter `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * vimeo `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * weibo `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * yahoo `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * breach_details `object`
>   * properties `object`
>   * haveibeenpwned_listed `boolean`
>   * number_of_breaches `integer`
>   * first_breach `string`
>   * breaches `array`
>   * items `array`
>
>   - - type `object`
>     - properties
>     - phone_details `object`
>     - properties `object`
>
> - * number `number`
>   * valid `boolean`
>   * type `string`
>   * country `string`
>   * carrier `string`
>   * score `number`
>   * account_details `object`
>   * properties `object`
>   * facebook `object`
>   * properties `object`
>
>   - - registered `boolean`
>     - photo `string`
>     - url `string`
>     - name `string`
>
> - * google `object`
>   * properties `object`
>
>   - - registered `boolean`
>     - photo `string`
>     - url `string`
>     - name `string`
>
> - * apple `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * twitter `object`
>   * properties `object`
>
>   - - registered `boolean`
>     - photo `string`
>     - url `string`
>
> - * microsoft `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * yahoo `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * ebay `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * gravatar `object`
>   * properties `object`
>
>   - - registered `boolean`
>     - photo `string`
>     - url `string`
>     - name `string`
>     - username `string`
>
> - * instagram `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * spotify `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * tumblr `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * linkedin `object`
>   * properties `object`
>
>   - - registered `boolean`
>     - photo `string`
>     - url `string`
>     - location `string`
>     - name `string`
>     - company `string`
>     - title `string`
>     - website `string`
>     - twitter `string`
>     - connection_count `number`
>
> - * weibo `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * github `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * vimeo `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * flickr `object`
>   * properties `object`
>
>   - - registered `boolean`
>     - photo `string`
>     - username `string`
>
> - * foursquare `object`
>   * properties `object`
>
>   - - registered `boolean`
>     - photo `string`
>     - url `string`
>     - name `string`
>     - bio `string`
>
> - * lastfm `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * myspace `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * pinterest `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * skype `object`
>   * properties `object`
>
>   - - registered `boolean`
>     - photo `string`
>     - location `string`
>     - name `string`
>     - country `string`
>     - city `string`
>     - gender `integer`
>     - id `string`
>     - handle `string`
>     - bio `string`
>     - age `integer`
>     - language `string`
>     - state `string`
>
> - * discord `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * ok `object`
>   * properties `object`
>
>   - - registered `boolean`
>     - city `string`
>     - gender `integer`
>     - age `integer`
>     - date_joined `integer`
>
> - * kakao `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * booking `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * airbnb `object`
>   * properties `object`
>
>   - - registered `boolean`
>     - image `string`
>     - url `string`
>     - location `string`
>     - name `string`
>     - about `string`
>     - first_name `string`
>     - created_at `string`
>     - reviewee_count `string`
>     - trips `integer`
>     - work `string`
>     - identity_verified `string`
>
> - * amazon `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * qzone `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * adobe `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * mailru `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * wordpress `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * imgur `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * disneyplus `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * netflix `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * jdid `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * flipkart `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * bukalapak `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * archiveorg `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * lazada `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * zoho `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * samsung `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * evernote `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * envato `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * patreon `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * tokopedia `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * rambler `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * quora `object`
>   * properties `object`
>
>   - registered `boolean`
>
> - * atlassian `object`
>   * properties `object`
>
>   - - registered `boolean`
>     - aml_details `object`
>     - properties `object`
>
> - * has_crimelist_match `boolean`
>   * has_pep_match `boolean`
>   * has_watchlist_match `boolean`
>   * has_sanction_match `boolean`
>   * result_payload `object`
>   * properties `object`
>   * searched_at `string`
>   * sanctionlist_sources `array`
>   * items `array`
>
>   - - type `object`
>     - properties
>
> - * crimelist_entries `array`
>   * items `array`
>
>   - - type `object`
>     - properties
>
> - * watchlist_entries `array`
>   * items `array`
>
>   - - type `object`
>     - properties
>
> - * sanctionlist_entries `array`
>   * items `array`
>
>   - - type `object`
>     - properties
>
> - * pep_entries `array`
>   * items `array`
>
>   - - type `object`
>     - properties
>     - device_details `object`
>     - properties `object`
>
> - * session_id `string`
>   * type `string`
>   * dns_ip `string`
>   * dns_ip_country `string`
>   * dns_ip_isp `string`
>   * source `string`
>   * device_hash `string`
>   * device_name `string`
>   * device_cellular_id `string`
>   * android_id `string`
>   * build_id `string`
>   * build_device `string`
>   * build_time `integer`
>   * build_number `string`
>   * build_manufacturer `string`
>   * app_guid `string`
>   * android_version `string`
>   * last_boot_time `integer`
>   * system_uptime `integer`
>   * sensor_hash `string`
>   * audio_volume_current `integer`
>   * audio_mute_status `boolean`
>   * battery_level `integer`
>   * battery_charging `boolean`
>   * battery_temperature `integer`
>   * battery_voltage `integer`
>   * battery_health `string`
>   * has_proximity_sensor `boolean`
>   * cpu_type `string`
>   * cpu_count `integer`
>   * cpu_speed `integer`
>   * cpu_hash `string`
>   * kernel_name `string`
>   * kernel_version `string`
>   * kernel_arch `string`
>   * physical_memory `integer`
>   * screen_brightness `integer`
>   * screen_height `integer`
>   * screen_width `integer`
>   * screen_scale `integer`
>   * total_storage `integer`
>   * free_storage `integer`
>   * network_config `string`
>   * wifi_mac_address `string`
>   * wifi_ssid `string`
>   * carrier_name `string`
>   * pasteboard_hash `string`
>   * region_timezone `string`
>   * region_language `string`
>   * region_country `string`
>   * carrier_country `string`
>   * is_emulator `boolean`
>   * is_rooted `boolean`
>   * device_ip_address `string`
>   * device_ip_country `string`
>   * device_ip_isp `string`
>
>   - - geolocation_details `object`
>     - properties `object`
>
> - * user_billing_distance `number`
>   * user_shipping_distance `number`
>   * billing_shipping_distance `number`
>   * ip_user_distance `number`
>   * ip_billing_distance `number`
>   * ip_shipping_distance `number`
>
>   - - rule_category_details `array`
>     - items `array`
>
> - * type `object`
>   * properties
>   * status `string`
>   * headers `object`

### Send Feedback

Send feedback to SEON to improve the fraud identification.

> **Collapse: Show details**
>
> * * Properties
>   * Transactions `keyValueList`
>
>   The list of transactions you want to label with the label texts.
>
> - - Output Schema
>   - output `object`
>   - rawResponse `object`
>   - properties `object`
>   - success `boolean`
>   - error `object`
>   - data `object`
>   - status `string`
>   - headers `object`

### Make Custom API Call

Define a custom API call to SEON.

> **Collapse: Show details**
>
> * * Properties
>   * Endpoint `textField` `required`
>
>   The SEON API endpoint, such as "SeonRestService/fraud-api/v2.0". This endpoint is added to the base API URL selected in the connector configuration.
>
> * HTTP Method `dropDown` `required`
>
>   The HTTP method of the API call.
>
>   * GET (Default)
>
>   * POST
>
>   * PUT
>
>   * DELETE
>
>   * PATCH
>
> * Query Parameters `keyValueList`
>
>   Define additional query parameters to send to SEON. Learn more in the SEON REST API documentation.
>
> * Additional Headers `keyValueList`
>
>   Define additional headers to send to SEON. Learn more in the SEON REST API documentation.
>
> * Body `textArea`
>
>   The raw JSON body of the API call.
>
> - - Output Schema
>   - output `object`
>   - rawResponse `object`
>   - properties `object`
>   - success `boolean`
>   - error `object`
>   - data `object`
>   - status `string`
>   - headers `object`
>   - properties `object`
>   - content-type `string`
>   - content-length `string`
>   - connection `string`
>   - date `string`
>   - x-amzn-requestid `string`
>   - x-xss-protection `string`
>   - access-control-allow-origin `string`
>   - x-frame-options `string`
>   - x-amzn-remapped-connection `string`
>   - x-amz-apigw-id `string`
>   - vary `string`
>   - cache-control `string`
>   - x-amzn-remapped-server `string`
>   - expires `string`
>   - x-content-type-options `string`
>   - pragma `string`
>   - x-amzn-remapped-date `string`
>   - x-cache `string`
>   - via `string`
>   - x-amz-cf-pop `string`
>   - x-amz-cf-id `string`