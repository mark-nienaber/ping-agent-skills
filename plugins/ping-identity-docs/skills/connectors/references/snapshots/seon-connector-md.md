---
title: SEON Connector
description: Configure the SEON connector in PingOne DaVinci to detect fraud using device fingerprinting, request fraud scores, and send feedback to SEON
component: connectors
page_id: connectors::seon_connector
canonical_url: https://docs.pingidentity.com/connectors/seon_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
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
>   You can use unlimited custom fields to inform our machine learning system and scoring engine. These can be string, boolean and numeric, for example is\_intangible\_item, is\_pay\_on\_delivery, departure\_airport, arrival\_airport, days\_to\_board
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
>     * fraud\_score `number`
>     * bin\_details `object`
>     * properties `object`
>
> - * card\_bin `string`
>   * bin\_bank `string`
>   * bin\_card `string`
>   * bin\_type `string`
>   * bin\_level `string`
>   * bin\_country `string`
>   * bin\_country\_code `string`
>   * bin\_website `string`
>   * bin\_phone `string`
>   * bin\_valid `boolean`
>   * card\_issuer `string`
>
>   - - version `string`
>     - applied\_rules `array`
>     - items `array`
>
> - * type `object`
>   * properties
>
>   - - calculation\_time `number`
>     - seon\_id `number`
>     - ip\_details `object`
>     - properties `object`
>
> - * success `boolean`
>   * error `object`
>   * data `object`
>   * properties `object`
>   * ip `string`
>   * score `number`
>   * country `string`
>   * state\_prov `string`
>   * city `string`
>   * timezone\_offset `string`
>   * isp\_name `string`
>   * latitude `number`
>   * longitude `number`
>   * type `string`
>   * open\_ports `array`
>   * items `array`
>
>   - type `integer`
>
> - * tor `boolean`
>   * harmful `boolean`
>   * vpn `boolean`
>   * web\_proxy `boolean`
>   * public\_proxy `boolean`
>   * spam\_number `integer`
>   * spam\_urls `array`
>   * items `array`
>
>   - type `string`
>
> - * applied\_rules `array`
>   * items `array`
>
>   - - type `object`
>     - properties
>
> - * history `object`
>   * properties `object`
>
>   - - hits `integer`
>     - customer\_hits `integer`
>     - first\_seen `integer`
>     - last\_seen `integer`
>
> - * flags `array`
>   * items `array`
>
>   - - type `object`
>     - properties
>
> - id `string`
>
>   * * email\_details `object`
>     * properties `object`
>
> - * email `string`
>   * score `number`
>   * deliverable `boolean`
>   * domain\_details `object`
>   * properties `object`
>   * domain `string`
>   * tld `string`
>   * registered `boolean`
>   * created `string`
>   * updated `string`
>   * expires `string`
>   * registrar\_name `string`
>   * registered\_to `string`
>   * disposable `boolean`
>   * free `boolean`
>   * custom `boolean`
>   * dmarc\_enforced `boolean`
>   * spf\_strict `boolean`
>   * valid\_mx `boolean`
>   * accept\_all `boolean`
>   * suspicious\_tld `boolean`
>   * website\_exists `boolean`
>   * account\_details `object`
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
> - * breach\_details `object`
>   * properties `object`
>   * haveibeenpwned\_listed `boolean`
>   * number\_of\_breaches `integer`
>   * first\_breach `string`
>   * breaches `array`
>   * items `array`
>
>   - - type `object`
>     - properties
>     - phone\_details `object`
>     - properties `object`
>
> - * number `number`
>   * valid `boolean`
>   * type `string`
>   * country `string`
>   * carrier `string`
>   * score `number`
>   * account\_details `object`
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
>     - connection\_count `number`
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
>     - date\_joined `integer`
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
>     - first\_name `string`
>     - created\_at `string`
>     - reviewee\_count `string`
>     - trips `integer`
>     - work `string`
>     - identity\_verified `string`
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
>     - aml\_details `object`
>     - properties `object`
>
> - * has\_crimelist\_match `boolean`
>   * has\_pep\_match `boolean`
>   * has\_watchlist\_match `boolean`
>   * has\_sanction\_match `boolean`
>   * result\_payload `object`
>   * properties `object`
>   * searched\_at `string`
>   * sanctionlist\_sources `array`
>   * items `array`
>
>   - - type `object`
>     - properties
>
> - * crimelist\_entries `array`
>   * items `array`
>
>   - - type `object`
>     - properties
>
> - * watchlist\_entries `array`
>   * items `array`
>
>   - - type `object`
>     - properties
>
> - * sanctionlist\_entries `array`
>   * items `array`
>
>   - - type `object`
>     - properties
>
> - * pep\_entries `array`
>   * items `array`
>
>   - - type `object`
>     - properties
>     - device\_details `object`
>     - properties `object`
>
> - * session\_id `string`
>   * type `string`
>   * dns\_ip `string`
>   * dns\_ip\_country `string`
>   * dns\_ip\_isp `string`
>   * source `string`
>   * device\_hash `string`
>   * device\_name `string`
>   * device\_cellular\_id `string`
>   * android\_id `string`
>   * build\_id `string`
>   * build\_device `string`
>   * build\_time `integer`
>   * build\_number `string`
>   * build\_manufacturer `string`
>   * app\_guid `string`
>   * android\_version `string`
>   * last\_boot\_time `integer`
>   * system\_uptime `integer`
>   * sensor\_hash `string`
>   * audio\_volume\_current `integer`
>   * audio\_mute\_status `boolean`
>   * battery\_level `integer`
>   * battery\_charging `boolean`
>   * battery\_temperature `integer`
>   * battery\_voltage `integer`
>   * battery\_health `string`
>   * has\_proximity\_sensor `boolean`
>   * cpu\_type `string`
>   * cpu\_count `integer`
>   * cpu\_speed `integer`
>   * cpu\_hash `string`
>   * kernel\_name `string`
>   * kernel\_version `string`
>   * kernel\_arch `string`
>   * physical\_memory `integer`
>   * screen\_brightness `integer`
>   * screen\_height `integer`
>   * screen\_width `integer`
>   * screen\_scale `integer`
>   * total\_storage `integer`
>   * free\_storage `integer`
>   * network\_config `string`
>   * wifi\_mac\_address `string`
>   * wifi\_ssid `string`
>   * carrier\_name `string`
>   * pasteboard\_hash `string`
>   * region\_timezone `string`
>   * region\_language `string`
>   * region\_country `string`
>   * carrier\_country `string`
>   * is\_emulator `boolean`
>   * is\_rooted `boolean`
>   * device\_ip\_address `string`
>   * device\_ip\_country `string`
>   * device\_ip\_isp `string`
>
>   - - geolocation\_details `object`
>     - properties `object`
>
> - * user\_billing\_distance `number`
>   * user\_shipping\_distance `number`
>   * billing\_shipping\_distance `number`
>   * ip\_user\_distance `number`
>   * ip\_billing\_distance `number`
>   * ip\_shipping\_distance `number`
>
>   - - rule\_category\_details `array`
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