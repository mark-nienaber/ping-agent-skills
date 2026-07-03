---
title: Microsoft Edge for Business Connector
description: The Microsoft Edge for Business connector lets you use Microsoft Edge for Business to improve authentication security in your PingOne DaVinci flow.
component: connectors
page_id: connectors::microsoft_edge_connector
canonical_url: https://docs.pingidentity.com/connectors/microsoft_edge_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 10, 2025
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  setting-up-microsoft-edge-for-business: Setting up Microsoft Edge for Business
  configuring-the-microsoft-edge-for-business-connector: Configuring the Microsoft Edge for Business connector
  using-the-connector-in-a-flow: Using the connector in a flow
  device-trust: Device Trust
  capabilities: Capabilities
  initializeAuthorizationRequest: Device Trust
---

# Microsoft Edge for Business Connector

The Microsoft Edge for Business connector lets you use Microsoft Edge for Business to improve authentication security in your PingOne DaVinci flow.

Microsoft Edge for Business is a secure, high-performance browser built for enterprise needs, offering enhanced productivity, AI-powered features, and native integration with Microsoft 365—designed to protect corporate data while supporting modern workplace demands.

You can use the Microsoft Edge for Business connector to include operating system device signals collected by Microsoft Edge for Business in a PingOne DaVinci flow.

## Setup

### Resources

You can find information and setup help in the following:

* Microsoft Edge for Business documentation

  * [Microsoft Edge for Business](https://www.microsoft.com/en-us/edge/business/?form=MA13FJ)

  * [Register an application in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app)

* DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* Administrator access to Microsoft Azure

* An Azure App Registration for the Microsoft Edge for Business Device Trust integration.

* Administrator access to Microsoft 365 admin center for Microsoft Edge for Business policy configuration.

### Setting up Microsoft Edge for Business

To use the connector, you'll need:

* Administrator access to Microsoft Azure

* An Azure App Registration for the Microsoft Edge for Business Device Trust integration.

* Administrator access to Microsoft 365 admin center for Microsoft Edge for Business policy configuration.

To set up Azure App Registration:

1. Sign on to the [Azure portal](https://portal.azure.com/).

2. Create the application:

   1. Search for and select **Azure Active Directory**.

   2. Under **Manage**, select **App registrations > New registration**.

   3. Register a new **Application**.

   4. Select the application you registered in the previous step.

   5. On the **App Registration** page for the new application, configure the permissions required to allow the application to access the Device Trust API.

   6. On the **APIs my organization uses** tab, search for the **Microsoft Edge management service**.

   7. Select **Application permissions** and add the **DeviceTrust.Read.All** permission.

   8. Click the **Grant admin consent confirmation**.

   9. Click **Register**.

3. On your app's **Overview** page, note the **Application (client) ID** and **Directory (tenant) ID**. You'll use these in the connector configuration.

   ![A screen capture of the application details page in Microsoft Azure.](_images/connector-images/dvc-microsoft-teams-application-details.png)

4. Create a client secret:

   1. Under **Manage**, click **Certificates & secrets**.

   2. On the **Client secrets** tab, click **New client secret**.

   3. Enter a name and select an expiry time. Click **Add.**

   4. Note the **Value** of the secret. You'll use this in the connector configuration.

      ![A screen capture of the client secret in Microsoft Azure.](_images/connector-images/dvc-microsoft-teams-client-secret.png)

To configure Edge for Business for PingOne DaVinci:

1. Sign on to **Microsoft 365 admin center**.

2. Go to the Microsoft Edge configuration.

3. On the **Connectors** tab, click **Set up** under the Ping Identity Device Trust feature.

4. In the right panel, enter the following PingOne DaVinci domains:

   * auth.pingone.com

   * auth.pingone.ca

   * auth.pingone.eu

   * auth.pingone.asia

   * auth.pingone.au

5. Click **Save Configuration**

The Microsoft Edge for Business Device Trust is now configured.

### Configuring the Microsoft Edge for Business connector

1. [Add the connector in DaVinci](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html).

2. Configure it as follows:

   * **Azure Tenant ID**: The tenant ID of your Microsoft Azure Tenant.

   * **Client ID**: The client ID you created in Setting up Microsoft Edge for Business.

   * **Client Secret**: The client secret you created in Setting up Microsoft Edge for Business.

## Using the connector in a flow

### Device Trust

The **Device Trust** capability allows PingOne DaVinci to receive the Microsoft Edge for Business Device Signals, which include device attributes such as Serial Number, MAC Addresses, and Hostname. If the CrowdStrike agent is installed, the CrowdStrike agent ID is also included.

The following is an example of a PingOne DaVinci flow that blocks access to users who are not using the expected Microsoft Edge for Business enrolled browser:

![A PingOne DaVinci flow which blocks access to users who are not using the expected Microsoft Edge for Business enrolled browser."](_images/connector-images/dvc-microsoft-edge-example-flow.png)

## Capabilities

### Device Trust

Authenticate against Microsoft Edge for Business Device Trust API

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
> * output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * headers object
>
>   * deviceTrustEnabled boolean
>
>   * deviceId string
>
>   * tenantId string
>
>   * profileKeyTrustLevel string
>
>   * keyTrustLevel string
>
>   * deviceSignals object
>
>     * browserVersion string
>
>     * builtInDnsClientEnabled boolean
>
>     * crowdStrikeAgent object
>
>       * agentId string
>
>       * customerId string
>
>     * deviceManufacturer string
>
>     * deviceModel string
>
>     * diskEncrypted string
>
>     * displayName string
>
>     * hostname string
>
>     * imei array
>
>     * meid array
>
>     * macAddresses array
>
>     * operatingSystem string
>
>     * osFirewall string
>
>     * osVersion string
>
>     * passwordPotectionWarningTrigger string
>
>     * realtimeUrlCheckMode string
>
>     * screenLockSecured string
>
>     * secureBootEnabled string
>
>     * serialNumber string
>
>     * siteIsolationEnabled boolean
>
>     * systemDnsServers array
>
>     * trigger string
>
>     * windowsUserDomain string
