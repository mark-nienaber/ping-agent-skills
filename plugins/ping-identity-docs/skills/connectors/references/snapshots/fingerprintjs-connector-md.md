---
title: FingerprintJS Connector
description: The FingerprintJS connector lets you create a unique visitor ID based on browser attributes for use in fraud and analytics in your PingOne DaVinci flow.
component: connectors
page_id: connectors::fingerprintjs_connector
canonical_url: https://docs.pingidentity.com/connectors/fingerprintjs_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 19, 2024
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  configuring-the-fingerprintjs-connector: Configuring the FingerprintJS connector
  connector-configuration: Connector configuration
  fingerprint-subscription-browser-token: Fingerprint Subscription Browser Token
  fingerprint-subscription-api-token: Fingerprint Subscription API Token
  javascript-cdn-url: JavaScript CDN URL
  using-the-connector-in-a-flow: Using the connector in a flow
  visitor-id-creation: Visitor ID creation
  information-through-visitors-id: Information through visitor's ID
  capabilities: Capabilities
  getVisitorId: Get Visitor's ID
  getVisitorInfo: Get Visitor's Info based on ID
---

# FingerprintJS Connector

The FingerprintJS connector lets you create a unique visitor ID based on browser attributes for use in fraud and analytics in your PingOne DaVinci flow.

This connector enables browser fingerprinting to stop fraud, spam, and account takeovers.

You can use the FingerprintJS connector to:

* Provide a single sign-on (SSO) *(tooltip: \<div class="paragraph">
  \<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
  \</div>)*-like experience across multiple nodes in a flow.

* Implement risk intelligence through browser fingerprinting.

## Setup

### Resources

Learn more in the following:

* DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* A configured FingerprintJS environment

* Your FingerprintJS API keys

### Configuring the FingerprintJS connector

Add the connector in DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

##### Fingerprint Subscription Browser Token

A public API key from FingerprintJS. This key can be found in your FingerprintJS environment under App Settings > API Keys.

##### Fingerprint Subscription API Token

TA secret API key from FingerprintJS. This key can be found in your FingerprintJS environment under App Settings > API Keys.

##### JavaScript CDN URL

A CDN URL for the FingerprintJS element.

## Using the connector in a flow

### Visitor ID creation

You can use the **Get a visitor's ID** capability to create a unique ID for a user. No special flow configuration is needed. Add the capability and populate its properties according to the help text.

### Information through visitor's ID

You can use the **Get visitor's info based on ID** capability to get visitor information, such as their ID, IP address, browser, and whether incognito mode is being used. No special flow configuration is needed. Add the capability and populate its properties according to the help text.

## Capabilities

### Get Visitor's ID

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
>     * token string required minLength: 0 maxLength: 100
>
>       Fingerprint JS Subscriber Token
>
>     * javascriptCdnUrl string required
>
>       Fingerprint JS javascript URL
>
> Input Example
>
> ```json
> {
>   "properties": {}
> }
> ```
>
> * output object
>
>   * requestId string required
>
>   * visitorId string required
>
>   * visitorFound boolean required
>
>   * meta null required
>
> Output Example
>
> ```json
> {
>   "requestId": "1619596982579.qsyvOp",
>   "visitorId": "oUT1HXUBaQZ9RwdF5xCX",
>   "visitorFound": true,
>   "meta": null
> }
> ```

### Get Visitor's Info based on ID

Get Visitor information such as ID, incognito mode, IP, browser, etc.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Visitor ID textField required
>
> * default object
>
>   * properties object
>
>     * apiToken string required minLength: 0 maxLength: 100
>
>       Fingerprint JS Subscriber API Token
>
>     * visitorId string required minLength: 0 maxLength: 100
>
>       Fingerprint JS visitor id
>
> Input Example
>
> ```json
> {
>   "properties": {
>     "visitorId": "visitor-id"
>   }
> }
> ```
>
> * output object
>
>   * visitorId string required
>
>   * visits array required
>
>     * Array Item Schema object
>
>       * requestId string required
>
>       * incognito boolean required
>
>       * linkedId string required
>
>       * time string required
>
>       * timestamp integer required
>
>       * url string required
>
>       * ip string required
>
>       * ipLocation object required
>
>         * accuracyRadius integer required
>
>         * latitude number required
>
>         * longitude number required
>
>         * postalCode string required
>
>         * timezone string required
>
>         * city object required
>
>           * name string required
>
>         * continent object required
>
>           * code string required
>
>           * name string required
>
>         * country object required
>
>           * code string required
>
>           * name string required
>
>         * subdivisions array required
>
>           * Array Item Schema object
>
>             * isoCode string required
>
>             * name string required
>
>       * browserDetails object required
>
>         * browserName string required
>
>         * browserMajorVersion string required
>
>         * browserFullVersion string required
>
>         * os string required
>
>         * osVersion string required
>
>         * device string required
>
>         * userAgent string required
>
>   * lastTimestamp integer required
>
> Output Example
>
> ```json
> {
>   "visitorId": "Ibk1527CUFmcnjLwIs4A9",
>   "visits": [
>     {
>       "requestId": "0KSh65EnVoB85JBmloQK",
>       "incognito": true,
>       "linkedId": "somelinkedId",
>       "time": "2019-05-21T16:40:13Z",
>       "timestamp": 1582299576512,
>       "url": "https://www.example.com/login",
>       "ip": "61.127.217.15",
>       "ipLocation": {
>         "accuracyRadius": 10,
>         "latitude": 49.982,
>         "longitude": 36.2566,
>         "postalCode": "61202",
>         "timezone": "Europe/Dusseldorf",
>         "city": {
>           "name": "Dusseldorf"
>         },
>         "continent": {
>           "code": "EU",
>           "name": "Europe"
>         },
>         "country": {
>           "code": "DE",
>           "name": "Germany"
>         },
>         "subdivisions": [
>           {
>             "isoCode": "63",
>             "name": "North Rhine-Westphalia"
>           }
>         ]
>       },
>       "browserDetails": {
>         "browserName": "Chrome",
>         "browserMajorVersion": "74",
>         "browserFullVersion": "74.0.3729",
>         "os": "Windows",
>         "osVersion": "7",
>         "device": "Other",
>         "userAgent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) ...."
>       }
>     }
>   ],
>   "lastTimestamp": 1582299576512
> }
> ```