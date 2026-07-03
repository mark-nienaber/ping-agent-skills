---
title: CrowdStrike Connector
description: The CrowdStrike connector lets you use CrowdStrike improve authentication security in your PingOne DaVinci flow.
component: connectors
page_id: connectors::crowdstrike_connector
canonical_url: https://docs.pingidentity.com/connectors/crowdstrike_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 21, 2024
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  setting-up-crowdstrike: Setting up CrowdStrike
  configuring-the-crowdstrike-connector: Configuring the CrowdStrike connector
  connector-configuration: Connector configuration
  crowdstrike-base-url: Crowdstrike Base URL
  client-id: Client ID
  client-secret: Client Secret
  using-the-connector-in-a-flow: Using the connector in a flow
  getting-device-details: Getting device details
  getting-device-management-status: Getting device management status
  quarantining-devices: Quarantining devices
  getting-incident-scores: Getting incident scores
  capabilities: Capabilities
  get-incident-score-by-device-id: Get Incident Score by Device ID
  get-zero-trust-assessment-scores-from-devices: Get Zero Trust Assessment Scores from Devices
  get-environment-crowdscore: Get Environment CrowdScore
  check-device-status-by-device-id: Check Device Status by Device ID
  check-device-status-by-ip: Check Device Status by IP
  get-devices-from-logins: Get Devices from Logins
  get-device-details: Get Device Details
  get-incidents-by-ip: Get Incidents by IP
  get-incidents-from-logins: Get Incidents from Logins
  get-incident-scores: Get Incident Scores
  set-containment-on-devices: Set Containment on Devices
  lift-containment-on-devices: Lift Containment on Devices
---

# CrowdStrike Connector

The CrowdStrike connector lets you use CrowdStrike improve authentication security in your PingOne DaVinci flow.

CrowdStrike protects the people, processes and technologies that drive modern enterprise. A single agent solution to stop breaches, ransomware, and cyberattacks powered by world-class security expertise and deep industry experience.

You can use the CrowdStrike connector to:

* Check whether a device is managed by CrowdStrike

* List the devices associated with a username or IP address

* Get the incident scores for a device

* Get the CrowdStrike scores from multiple incidents

* Get the CrowdStrike Zero Trust Assessment scores for a device

* Get the CrowdScore for an environment

* Managed quarantined devices

## Setup

### Resources

Learn more in the following:

* CrowdStrike documentation

  * [CrowdStrike OAuth2-Based APIs](https://www.crowdstrike.com/en-us/resources/guides/?lang=1)

* DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need a Crowdstrike license.

### Setting up CrowdStrike

Follow the steps in [Creating an API client](https://www.crowdstrike.com/en-us/resources/guides/?lang=1).

* Select the following API scopes:

  | Scope                 | Permissions |
  | --------------------- | ----------- |
  | Hosts                 | Read, Write |
  | Falcon Discover       | Read        |
  | Incidents             | Read        |
  | Zero Trust Assessment | Read        |

* Record your client ID and secret. You'll use them in the connector configuration.

### Configuring the CrowdStrike connector

Add the connector in DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

##### Crowdstrike Base URL

The base URL for your CrowdStrike environment.

##### Client ID

The client ID you created in Setting up CrowdStrike.

##### Client Secret

The client secret you created in Setting up CrowdStrike.

## Using the connector in a flow

### Getting device details

The **Get Device Details** capability allows you to get detailed information about one or more devices.

In the **Device IDs** field, you can click **{}** and select the `deviceIds` variable from a **Get Devices from Logins** node.

### Getting device management status

The **Check Device Status by Device ID** and **Check Device Status by IP** capabilities identify if a device is managed by CrowdStrike.

No special configuration is needed. Add the capability and populate its properties according to the help text.

### Quarantining devices

You can quarantine a device by applying CrowdStrike Network Containment on the device ID with the **Set Containment on Devices** capability.

When you determine a device is safe, you can remove the quarantine with the **Lift Containment on Devices** capability.

In the **Device IDs** field, you can click **{}** and select the `deviceIds` variable from a **Get Devices from Logins** node.

### Getting incident scores

The **Get Incident Scores** lets you find out the highest incident score from a list of incident IDs. In the **Incident IDs** field, you can click **{}** and select the `incidentIds` variable from a **Get Incidents from Logins** node.

The **Get Incident Scores by Device ID** capability lets you find out the highest incident score for a particular device. In the **Device ID** field, you can click **{}** and select a variable from your flow that includes the device ID.

## Capabilities

### Get Incident Score by Device ID

Get the maximum incident score from a single CrowdStrike device ID.

> **Collapse: Show details**
>
> * * Properties
>   * Device ID `textField`
>
>   The CrowdStrike device ID (also known as agent ID), such as "f69915c8a8b244a1a7c4e4a4d7870e2f".
>
> - - Input Schema
>   - default `object`
>   - deviceIdIncidentScore `string` `required`
>
>   A CrowdStrike device ID.
>
> * * Output Schema
>   * output `object`
>   * rawResponse `object`
>   * statusCode `number`
>   * maxIncidentScore `number`
>   * incidentsOnDevice `boolean`

### Get Zero Trust Assessment Scores from Devices

Use a list of device IDs to get the most recent Zero Trust Assessment scores.

> **Collapse: Show details**
>
> * * Properties
>   * Device IDs `textField` `required`
>
>   List of Device IDs (JSON Array formatted)
>
> - - Input Schema
>   - default `object`
>   - deviceIds `string` `required`
>
>   List of Device IDs
>
> * * Output Schema
>   * output `object`
>   * rawResponse `object`
>   * statusCode `number`
>   * maxOverallScore `number`
>
>   Maximum Overall Score from Devices
>
> * maxOSScore `number`
>
>   Maximum Operating System Score from Devices

### Get Environment CrowdScore

Get the most recent CrowdScore for the CrowdStrike environment.

> **Collapse: Show details**
>
> * * Output Schema
>   * output `object`
>   * rawResponse `object`
>   * statusCode `number`
>   * score `number`
>   * adjustedScore `number`

### Check Device Status by Device ID

Use the CrowdStrike Device ID to check whether a device is managed by CrowdStrike.

> **Collapse: Show details**
>
> * * Properties
>   * Device ID `textField`
>
>   The CrowdStrike device ID (also known as agent ID), such as "f69915c8a8b244a1a7c4e4a4d7870e2f".
>
> - - Input Schema
>   - default `object`
>   - deviceIdDeviceManaged `string` `required`
>
>   The CrowdStrike Device Id.
>
> * * Output Schema
>   * output `object`
>   * rawResponse `object`
>   * statusCode `number`
>   * deviceManaged `boolean`
>   * deviceDetails `object`

### Check Device Status by IP

Use an IP address to check whether a device is managed by CrowdStrike.

> **Collapse: Show details**
>
> * * Properties
>   * IP `textField`
>
>   The user's IP address
>
> * Username `textField`
>
>   The username associated with the device.
>
> * Last Seen Number of Days `textField`
>
>   The number of days to search back in time for a managed device.
>
>   Default:
>
>   ```
>   365
>   ```
>
> - - Input Schema
>   - default `object`
>   - ip `string` `required`
>
>   The IP address of the device
>
> - username `string`
>
>   The username associated with the device
>
> - lastSeenDays `string/number` `required`
>
>   The number of days to search back in time for a managed device
>
> * * Output Schema
>   * output `object`
>   * rawResponse `object`
>   * statusCode `number`
>   * deviceManaged `boolean`
>   * foundLoginMatch `boolean`

### Get Devices from Logins

Get a list of device IDs from CrowdStrike Logins that match a username, email address, or IP address.

> **Collapse: Show details**
>
> * * Properties
>   * Username `textField`
>
>   The username associated with the device.
>
> * Email `textField`
>
>   The email of the user associated with the device.
>
> * IP `textField`
>
>   The user's IP address
>
> * Search Back Number of Days `textField`
>
>   The number of days to search back in time for a login
>
>   Default:
>
>   ```
>   365
>   ```
>
> - - Input Schema
>   - default `object`
>   - username `string`
>
>   The username associated with the device
>
> - email `string`
>
>   The email of the user associated with the device
>
> - ip `string`
>
>   The user's IP address
>
> - searchLoginDays `string/number` `required`
>
>   The number of days to search back in time for a login
>
> * * Output Schema
>   * output `object`
>   * rawResponse `object`
>   * statusCode `number`
>   * deviceIds `array`

### Get Device Details

Get device details from a list of devices.

> **Collapse: Show details**
>
> * * Properties
>   * Device IDs `textField` `required`
>
>   List of Device IDs (JSON Array formatted)
>
> - - Input Schema
>   - default `object`
>   - deviceIds `string` `required`
>
>   List of Device IDs (JSON Array formatted)
>
> * * Output Schema
>   * output `object`
>   * rawResponse `object`
>   * statusCode `number`
>   * devices `array`

### Get Incidents by IP

Use an IP address to get a list of incidents associated with the device.

> **Collapse: Show details**
>
> * * Properties
>   * IP `textField`
>
>   The user's IP address
>
> * Last Seen Number of Days `textField`
>
>   The number of days to search back in time for a managed device.
>
>   Default:
>
>   ```
>   365
>   ```
>
> - - Input Schema
>   - default `object`
>   - ip `string` `required`
>
>   The IP address of the device
>
> - lastSeenDays `string/number` `required`
>
>   The number of days to search back in time for a managed device
>
> * * Output Schema
>   * output `object`
>   * rawResponse `object`
>   * statusCode `number`
>   * incidentsOnDevice `boolean`
>   * incidentIds `array`

### Get Incidents from Logins

Get a list of incidents from CrowdStrike Logins that match a username, email address, or IP address.

> **Collapse: Show details**
>
> * * Properties
>   * Username `textField`
>
>   The username associated with the device.
>
> * Email `textField`
>
>   The email of the user associated with the device.
>
> * IP `textField`
>
>   The user's IP address
>
> * Search Back Number of Days `textField`
>
>   The number of days to search back in time for a login
>
>   Default:
>
>   ```
>   365
>   ```
>
> - - Input Schema
>   - default `object`
>   - username `string`
>
>   The username associated with the device
>
> - email `string`
>
>   The email of the user associated with the device
>
> - ip `string`
>
>   The user's IP address
>
> - searchLoginDays `string/number` `required`
>
>   The number of days to search back in time for a login
>
> * * Output Schema
>   * output `object`
>   * rawResponse `object`
>   * statusCode `number`
>   * loginsWithIncidents `boolean`
>   * incidentIds `array`

### Get Incident Scores

Get the maximum incident score from a list of incident IDs.

> **Collapse: Show details**
>
> * * Properties
>   * Incident IDs `textField`
>
>   List of Incident IDs (JSON Array formatted)
>
> - - Input Schema
>   - default `object`
>   - incidentIds `string` `required`
>
>   List of Incident IDs
>
> * * Output Schema
>   * output `object`
>   * rawResponse `object`
>   * statusCode `number`
>   * maxIncidentScore `number`
>   * incidents `array`

### Set Containment on Devices

Apply CrowdStrike Network Containment on the Device IDs.

> **Collapse: Show details**
>
> * * Properties
>   * Device IDs `textField` `required`
>
>   List of Device IDs (JSON Array formatted)
>
> - - Input Schema
>   - default `object`
>   - deviceIds `string` `required`
>
>   List of Device IDs
>
> * * Output Schema
>   * output `object`
>   * rawResponse `object`
>   * statusCode `number`

### Lift Containment on Devices

Remove CrowdStrike Network Containment on the Device IDs.

> **Collapse: Show details**
>
> * * Properties
>   * Device IDs `textField` `required`
>
>   List of Device IDs (JSON Array formatted)
>
> - - Input Schema
>   - default `object`
>   - deviceIds `string` `required`
>
>   List of Device IDs
>
> * * Output Schema
>   * output `object`
>   * rawResponse `object`
>   * statusCode `number`