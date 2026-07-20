---
title: BeyondTrust Privileged Remote Access Connector
description: Configure the BeyondTrust Privileged Remote Access connector to terminate PRA jump sessions by hostname or username in a PingOne DaVinci flow
component: connectors
page_id: connectors::beyondtrust_pra_connector
canonical_url: https://docs.pingidentity.com/connectors/beyondtrust_pra_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  configuring-the-beyondtrust-privileged-remote-access-connector: Configuring the BeyondTrust Privileged Remote Access connector
  connector-configuration: Connector configuration
  using-the-connector-in-a-flow: Using the connector in a flow
  terminating-remote-sessions-during-a-security-incident: Terminating remote sessions during a security incident
  capabilities: Capabilities
  closeSessionByHostname: Terminate PRA jump session by hostname
  closeSessionByUsername: Terminate PRA jump session by username
---

# BeyondTrust Privileged Remote Access Connector

The BeyondTrust Privileged Remote Access connector lets you terminate active [BeyondTrust](https://www.beyondtrust.com/) Privileged Remote Access (PRA) jump sessions in your PingOne DaVinci flow.

You can end all sessions on a specific host or all sessions for a specific user. This lets a flow respond to a security incident by cutting off remote access, and it returns a success or error result that downstream nodes can act on.

## Setup

### Resources

You can find more information and setup help in the following:

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

* BeyondTrust documentation:

  * [Privileged Remote Access API configuration](https://www.beyondtrust.com/docs/privileged-remote-access/getting-started/admin/api-configuration.htm)

  * [Privileged Remote Access cloud deployment](https://www.beyondtrust.com/docs/privileged-remote-access/getting-started/deployment/cloud/index.htm)

  * [Privileged Remote Access how-to guides](https://www.beyondtrust.com/docs/privileged-remote-access/how-to/index.htm)

  * [Privileged Remote Access integrations](https://www.beyondtrust.com/docs/integrations/index.htm?prod=Privileged-Remote-Access)

### Requirements

To use the connector, you'll need:

* A BeyondTrust Privileged Remote Access instance.

* An API account in Privileged Remote Access with full access to the command and reporting API.

* The OAuth client ID and client secret for that API account.

### Configuring the BeyondTrust Privileged Remote Access connector

Add the connector in PingOne DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

| Setting                 | Description                                                                                                 |
| ----------------------- | ----------------------------------------------------------------------------------------------------------- |
| **PRA Web API Address** | The URL of your Privileged Remote Access instance (for example, https\://customerpra.beyondtrustcloud.com). |
| **Client ID**           | The client ID of the API account you created in Privileged Remote Access.                                   |
| **Client Secret**       | The client secret of the API account you created in Privileged Remote Access.                               |

## Using the connector in a flow

### Terminating remote sessions during a security incident

When a security incident affects a host or a user account, you can use the connector to end the associated Privileged Remote Access jump sessions as part of an automated response flow. Another connector, such as a threat detection or SOAR connector, can supply the affected hostname or username, and the connector returns a success or error result that downstream nodes can act on, such as creating a ticket in an ITSM tool.

The connector provides two capabilities for this scenario:

* The **Terminate PRA jump session by hostname** capability ends a PRA jump session for a specified host.

* The **Terminate PRA jump session by username** capability ends all open sessions for a specific user across hosts.

|   |                                                  |
| - | ------------------------------------------------ |
|   | Hostname and username values are case-sensitive. |

## Capabilities

### Terminate PRA jump session by hostname

Terminate PRA jump session by hostname

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Hostname textField
>
>   Name of the machine you want to terminate the session
>
> * default object
>
>   * properties object
>
>     * hostName string required
>
>       Hostname of jump session
>
> Input Example
>
> ```json
> {
>   "properties": {
>     "hostName": "Server1"
>   }
> }
> ```
>
> * output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * headers object
>
>   * result string
>
>   * resultMessage string

### Terminate PRA jump session by username

Terminate PRA jump session by username

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
>   Username for which you would like to terminate all open sessions
>
> * default object
>
>   * properties object
>
>     * userName string required
>
>       Open sessions of a user account
>
> Input Example
>
> ```json
> {
>   "properties": {
>     "userName": "Server1"
>   }
> }
> ```
>
> * output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * headers object
>
>   * result string