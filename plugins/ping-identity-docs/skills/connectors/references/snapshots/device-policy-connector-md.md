---
title: Device Policy Connector
description: The Device Policy connector lets you check the user agent, browser information, and operating system version in your PingOne DaVinci flow.
component: connectors
page_id: connectors::device_policy_connector
canonical_url: https://docs.pingidentity.com/connectors/device_policy_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 19, 2024
section_ids:
  setup: Setup
  resources: Resources
  configuring-the-device-policy-connector: Configuring the Device Policy connector
  using-the-connector-in-a-flow: Using the connector in a flow
  allow-requests-from-specified-devices: Allow requests from specified devices
  deny-requests-from-specified-devices: Deny requests from specified devices
  get-information-about-a-device: Get information about a device
  capabilities: Capabilities
  trustedDeviceOS: Trusted Device OS
  untrustedDeviceOS: Blacklisted Device OS
  trustedUserAgent: Trusted User Agent
  untrustedUserAgent: Blacklisted User Agent
  getDeviceOS: Get Device OS
  getBrowser: Get Browser
  getPlatform: Get Platform
---

# Device Policy Connector

The Device Policy connector lets you check the user agent, browser information, and operating system version in your PingOne DaVinci flow.

You can use the Device Policy connector to:

* Enable mobile device management.

  * Selected devices, browsers, and operating systems included in the allow list grants access to users.

  * Selected devices, browsers, and operating systems included in the deny list will prevent access to users.

* Implement risk intelligence by creating a device policy.

|   |                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This connector relies on information provided by the device's user agent. Because the implementation of user agent varies, the information might |

## Setup

### Resources

Learn more in the following:

* DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Configuring the Device Policy connector

In DaVinci, add a Device Policy connector. Learn more in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html).

This connector doesn't have a configuration at the environment level. You configure it in your flow instead.

## Using the connector in a flow

### Allow requests from specified devices

The connector has several capabilities to select allowed devices:

* **Allow selected OS**

* **Allow selected user agent**

No special configuration is needed. Add the capability and populate its properties according to the help text.

### Deny requests from specified devices

The connector has several capabilities to select denied devices:

* **Deny selected OS**

* **Deny selected user agent**

No special configuration is needed. Add the capability and populate its properties according to the help text.

### Get information about a device

The connector has several capabilities to get information about a user's device:

* **Get operating system**

* **Get browser**

* **Get platform**

No special configuration is needed. Add the capability and populate its properties according to the help text.

## Capabilities

### Trusted Device OS

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - deviceOSName dropDownMultiSelect
>
> * default object
>
>   * userAgent string required
>
>   * properties object
>
>     * deviceOSName array required
>
> - output object
>
>   * deviceOSName string
>
> Output Example
>
> ```json
> {
>   "deviceOSName": "MacOS"
> }
> ```

### Blacklisted Device OS

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - deviceOSName dropDownMultiSelect
>
> * default object
>
>   * userAgent string required
>
>   * properties object
>
>     * deviceOSName array required
>
> - output object
>
>   * deviceOSName string
>
> Output Example
>
> ```json
> {
>   "deviceOSName": "MacOS"
> }
> ```

### Trusted User Agent

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - browserNames dropDownMultiSelect
>
> * default object
>
>   * userAgent string required
>
>   * properties object
>
>     * browserNames array required
>
> - output object
>
>   * browserName string
>
> Output Example
>
> ```json
> {
>   "browserName": "chrome"
> }
> ```

### Blacklisted User Agent

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - browserNames dropDownMultiSelect
>
> * default object
>
>   * userAgent string required
>
>   * properties object
>
>     * browserNames array required
>
> - output object
>
>   * browserName string
>
> Output Example
>
> ```json
> {
>   "browserName": "chrome"
> }
> ```

### Get Device OS

Return the Device OS name

> **Collapse: Show details**
>
> * Input Schema
>
> * Output Schema
>
> - default object
>
>   * userAgent string required
>
> * output object
>
>   * deviceOSName string
>
> Output Example
>
> ```json
> {
>   "deviceOSName": "MacOS"
> }
> ```

### Get Browser

Returns the Name of the Browser that is used.

> **Collapse: Show details**
>
> * Input Schema
>
> * Output Schema
>
> - default object
>
>   * userAgent string required
>
> * output object
>
>   * browserName string
>
> Output Example
>
> ```json
> {
>   "browserName": "Chrome"
> }
> ```

### Get Platform

Returns whether the flow is running in mobile or desktop.

> **Collapse: Show details**
>
> * Input Schema
>
> * Output Schema
>
> - default object
>
>   * userAgent string required
>
> * output object
>
>   * platform string
>
> Output Example
>
> ```json
> {
>   "platform": "mobile"
> }
> ```
