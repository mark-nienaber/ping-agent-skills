---
title: CrowdStrike Connector
description: Configure the CrowdStrike connector in PingOne DaVinci to check device management status, assess Zero Trust scores, manage quarantined devices, and analyze user risk
component: connectors
page_id: connectors::crowdstrike_connector
canonical_url: https://docs.pingidentity.com/connectors/crowdstrike_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-14T00:00:00Z
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  setting-up-crowdstrike: Setting up CrowdStrike
  configuring-the-crowdstrike-connector: Configuring the CrowdStrike connector
  connector-configuration: Connector configuration
  using-the-connector-in-a-flow: Using the connector in a flow
  getting-device-details: Getting device details
  getting-device-management-status: Getting device management status
  quarantining-devices: Quarantining devices
  getting-alerts-for-a-device: Getting alerts for a device
  getting-user-risk-analysis: Getting user risk analysis
  capabilities: Capabilities
  zeroTrustAssessmentScore: Get Zero Trust Assessment Scores from Devices
  deviceManagedById: Check Device Status by Device ID
  deviceManaged: Check Device Status by IP
  devicesByLogins: Get Devices from Logins
  deviceDetails: Get Device Details
  setContainment: Set Containment on Devices
  liftContainment: Lift Containment on Devices
  getUserRiskAnalysis: Get User Risk Analysis
  alertRiskByDeviceId: Get Alerts by Device ID
---

# CrowdStrike Connector

The CrowdStrike connector lets you use CrowdStrike to improve authentication security in your PingOne DaVinci flow.

CrowdStrike protects the people, processes, and technologies that drive modern enterprise. A single agent solution to stop breaches, ransomware, and cyberattacks powered by world-class security expertise and deep industry experience.

You can use the CrowdStrike connector to:

* Check whether a device is managed by CrowdStrike

* List the devices associated with a username or IP address

* Get the CrowdStrike Zero Trust Assessment scores for a device

* Get alert details for a device

* Get a risk analysis for a user

* Manage quarantined devices

## Setup

### Resources

Learn more in the following:

* CrowdStrike documentation

  * [CrowdStrike OAuth2-Based APIs](https://www.crowdstrike.com/en-us/resources/guides/?lang=1)

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need a CrowdStrike license.

### Setting up CrowdStrike

Follow the steps in [Creating an API client](https://www.crowdstrike.com/en-us/resources/guides/?lang=1).

* Select the following API scopes:

  | Scope                 | Permissions |
  | --------------------- | ----------- |
  | Hosts                 | Read, Write |
  | Falcon Discover       | Read        |
  | Zero Trust Assessment | Read        |
  | Alerts                | Read        |
  | Identity Protection   | Read        |

* Record your client ID and secret. You'll use them in the connector configuration.

### Configuring the CrowdStrike connector

Add the connector in PingOne DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

| Setting              | Description                                                                                                                                                                                                                                                                                                       |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CrowdStrike Base URL | The base URL for your CrowdStrike environment. Select from the provided options or enter a custom URL.+ Available options:- <https://api.crowdstrike.com> (US-1)

- <https://api.us-2.crowdstrike.com> (US-2)

- <https://api.eu-1.crowdstrike.com> (EU-1)

- <https://api.laggar.gcw.crowdstrike.com> (US-GOV-1) |
| Client ID            | The client ID you created in Setting up CrowdStrike.                                                                                                                                                                                                                                                              |
| Client Secret        | The client secret you created in Setting up CrowdStrike.                                                                                                                                                                                                                                                          |

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

### Getting alerts for a device

The **Get Alerts by Device ID** capability returns open endpoint protection alerts for a specific device. In the **Device ID** field, enter or reference the CrowdStrike device ID (also known as the agent ID).

Use the **Alert Limit** field to control the maximum number of alerts returned. The default is 100.

### Getting user risk analysis

The **Get User Risk Analysis** capability retrieves risk score and risk factor details for an individual user. In the **Username** and **Domain** fields, provide the user's credentials to scope the analysis.

The output includes a `riskScore`, a `riskScoreSeverity` string, and a `riskFactors` array. When no matching user is found, the capability returns a `riskScore` of -1 and a `riskScoreSeverity` of UNKNOWN.

## Capabilities

### Get Zero Trust Assessment Scores from Devices

Use a list of device IDs to get the most recent Zero Trust Assessment scores.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Device IDs textField required
>
>   List of Device IDs (JSON Array formatted)
>
> * default object
>
>   * properties object
>
>     * deviceIds string required
>
>       List of Device IDs
>
> - output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * maxOverallScore number
>
>     Maximum Overall Score from Devices
>
>   * maxOSScore number
>
>     Maximum Operating System Score from Devices

### Check Device Status by Device ID

Use the CrowdStrike Device ID to check whether a device is managed by CrowdStrike.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Device ID textField
>
>   The CrowdStrike device ID (also known as agent ID), such as "f69915c8a8b244a1a7c4e4a4d7870e2f".
>
> * default object
>
>   * properties object
>
>     * deviceIdDeviceManaged string required
>
>       The CrowdStrike Device Id.
>
> - output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * deviceManaged boolean
>
>   * deviceDetails object

### Check Device Status by IP

Use an IP address to check whether a device is managed by CrowdStrike.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - IP textField
>
>   The user's IP address
>
> - Username textField
>
>   The username associated with the device.
>
> - Last Seen Number of Days textField
>
>   The number of days to search back in time for a managed device.
>
>   Default: `365`
>
> * default object
>
>   * properties object
>
>     * ip string required
>
>       The IP address of the device
>
>     * username string
>
>       The username associated with the device
>
>     * lastSeenDays string/number required
>
>       The number of days to search back in time for a managed device
>
> - output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * deviceManaged boolean
>
>   * foundLoginMatch boolean

### Get Devices from Logins

Get a list of device IDs from CrowdStrike Logins that match a username, email address, or IP address.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Username textField
>
>   The username associated with the device.
>
> - Email textField
>
>   The email of the user associated with the device.
>
> - IP textField
>
>   The user's IP address
>
> - Search Back Number of Days textField
>
>   The number of days to search back in time for a login
>
>   Default: `365`
>
> * default object
>
>   * properties object
>
>     * username string
>
>       The username associated with the device
>
>     * email string
>
>       The email of the user associated with the device
>
>     * ip string
>
>       The user's IP address
>
>     * searchLoginDays string/number required
>
>       The number of days to search back in time for a login
>
> - output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * deviceIds array

### Get Device Details

Get device details from a list of devices.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Device IDs textField required
>
>   List of Device IDs (JSON Array formatted)
>
> * default object
>
>   * properties object
>
>     * deviceIds string required
>
>       List of Device IDs (JSON Array formatted)
>
> - output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * devices array

### Set Containment on Devices

Apply CrowdStrike Network Containment on the Device IDs.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Device IDs textField required
>
>   List of Device IDs (JSON Array formatted)
>
> * default object
>
>   * properties object
>
>     * deviceIds string required
>
>       List of Device IDs
>
> - output object
>
>   * rawResponse object
>
>   * statusCode number

### Lift Containment on Devices

Remove CrowdStrike Network Containment on the Device IDs.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Device IDs textField required
>
>   List of Device IDs (JSON Array formatted)
>
> * default object
>
>   * properties object
>
>     * deviceIds string required
>
>       List of Device IDs
>
> - output object
>
>   * rawResponse object
>
>   * statusCode number

### Get User Risk Analysis

Retrieve details from an individual user's risk analysis.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Username textField
>
>   Target username for risk analysis.
>
> - Domain textField
>
>   Target domain for risk analysis.
>
> * default object
>
>   * properties object
>
>     * usernameForAnalysis string required
>
>       Target username for risk analysis.
>
>     * domainForAnalysis string required
>
>       Target domain for risk analysis.
>
> - output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * riskScore number
>
>   * riskScoreSeverity string
>
>   * riskFactors array

### Get Alerts by Device ID

Get the CrowdStrike alert details for a single CrowdStrike device ID.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Device ID textField
>
>   The CrowdStrike device ID (also known as agent ID), such as "f69915c8a8b244a1a7c4e4a4d7870e2f".
>
> - Alert Limit textField
>
>   The maximum number of CrowdStrike alerts to return for the device. Default is 100.
>
>   Default: `100`
>
> * default object
>
>   * properties object
>
>     * deviceIdAlertRisk string required
>
>       A CrowdStrike device ID (also known as agent ID).
>
> - output object
>
>   * statusCode number
>
>   * meta object
>
>   * errors array
>
>   * resources array