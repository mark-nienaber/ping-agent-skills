---
title: Integrations
description: PingOne Privilege integrates with common systems. Supported integrations include:
component: privilege
page_id: privilege:integrations:index
canonical_url: https://docs.pingidentity.com/privilege/integrations/index.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Integrations

PingOne Privilege integrates with common systems. Supported integrations include:

![](_images/jiraatlassian-logo.png)

#### [Jira](jira.html)

Integrate PingOne Privilege with Jira to manage privileged access through Jira.

![](_images/microsoft-teams-logo.png)

#### [Microsoft Teams](microsoft-teams.html)

Integrate PingOne Privilege with Microsoft Teams to manage access requests and approvals.

![](_images/servicenow-logo.png)

#### [ServiceNow](servicenow.html)

Integrate PingOne Privilege with ServiceNow to create and manage access request tickets.

![](_images/slack-logo.png)

#### [Slack](slack.html)

Integrate PingOne Privilege with Slack to manage privileged access through Slack.

---

---
title: Jira integration
description: The Jira integration automatically creates and updates Jira issues to track just-in-time access requests.
component: privilege
page_id: privilege:integrations:jira
canonical_url: https://docs.pingidentity.com/privilege/integrations/jira.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2026
section_ids:
  step-1-configure-jira-integration-in-pingone-privilege: "Step 1: Configure Jira integration in PingOne Privilege"
  step-2-configure-jira-projects-for-jit-requests: "Step 2: Configure Jira projects for JIT requests"
  jira-task-lifecycle: Jira task lifecycle
---

# Jira integration

The PingOne Privilege Jira integration automatically creates and updates Jira issues to track just-in-time (JIT) access requests. When a user submits a JIT request, a corresponding task is created in the configured Jira project. The task then updates automatically when the request is approved or denied.

## Step 1: Configure Jira integration in PingOne Privilege

1. In the PingOne Privilege admin console, go to **Connections > Integrations**.

2. Click on the **All Integrations** tab.

3. On the **Jira** tile, click **Integrate**.

4. Enter a descriptive **Name** for the integration.

5. Enter **Project Keys** separated by commas or select **Fetch All Project**.

6. Click **Continue**.

   You'll be redirected to the Atlassian authorization page.

7. Review the requested permissions and click Accept to grant access.

## Step 2: Configure Jira projects for JIT requests

After setting up the integration, associate your Jira projects with the cloud accounts they'll track:

1. In the PingOne Privilege admin console, go to **Connections > Integrations**.

2. Find your Jira integration, and then click **Manage**.

   PingOne Privilege displays your available Jira projects.

3. Select the desired Jira project in the list and click **Manage**.

4. Associate one or more cloud accounts with this project.

   JIT requests for the selected accounts will now create issues in this Jira project.

5. Click **Update** to save the configuration.

## Jira task lifecycle

After configuration, the integration performs the following actions:

* When a user creates a JIT request for a resource in a linked cloud account, a new task is created in the associated Jira project.

* The Jira task description contains details about the requested resources, the access duration, and a link to the approval page in PingOne Privilege.

* When the request is approved or denied in PingOne Privilege, the Jira task is automatically updated to reflect the new status (for example, moved to "Done").

---

---
title: Microsoft Teams
description: The PingOne Privilege Microsoft Teams integration allows your teams to receive notifications of access requests or approvals.
component: privilege
page_id: privilege:integrations:microsoft-teams
canonical_url: https://docs.pingidentity.com/privilege/integrations/microsoft-teams.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 5, 2026
section_ids:
  configuring-notifications-for-approvals: Configuring notifications for approvals
  step-1-create-an-incoming-webhook-in-microsoft-teams: "Step 1: Create an incoming webhook in Microsoft Teams"
  step-2-add-the-webhook-to-pingone-privilege: "Step 2: Add the webhook to PingOne Privilege"
---

# Microsoft Teams

The PingOne Privilege Microsoft Teams integration allows your teams to receive notifications of access requests or approvals.

## Configuring notifications for approvals

To send approval notifications to a Microsoft Teams channel, you must first create an incoming webhook in Microsoft Teams and then add it to PingOne Privilege.

### Step 1: Create an incoming webhook in Microsoft Teams

1. In Microsoft Teams, go to the team channel where you want to create an incoming webhook.

2. Select **More options**.

3. Select **Workflows**.

4. Search for and select a template such as **Send webhook alerts to a channel**.

5. Configure the workflow parameters.

6. Click **Save**.

7. Copy the webhook link.

### Step 2: Add the webhook to PingOne Privilege

1. In the PingOne Privilege admin console, go to **Connections > Integrations**.

2. Click on the **All Integrations** tab.

3. In the **Microsoft Teams** tile, click **Integrate**.

4. Enter a descriptive **Integration Name**, such as `DevOps Team Approvals`.

5. Paste the webhook URL you copied from Microsoft Teams into the **Webhook Url** field.

6. Click **Continue** to create the integration.

7. On the **Active**, locate your new **Microsoft Teams** integration and click **Manage Integration**.

8. In the **Channel-Account linking** section, click the menu button. Click **Manage**.

9. Add the cloud accounts whose JIT notifications should be handled by this integration and click **Update**.

10. In the **Notification** section, click **Select** to configure the **GateWay Notification Channel** and the **Private Server Notification Channel**.

You can create multiple integrations to send notifications for different sets of accounts to different Microsoft Teams channels.

---

---
title: ServiceNow
description: You can integrate PingOne Privilege with ServiceNow to create access request tickets.
component: privilege
page_id: privilege:integrations:servicenow
canonical_url: https://docs.pingidentity.com/privilege/integrations/servicenow.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 5, 2026
section_ids:
  step-1-create-an-oauth-2-0-endpoint-in-servicenow: "Step 1: Create an OAuth 2.0 endpoint in ServiceNow"
  step-2-configure-the-integration-in-pingone-privilege: "Step 2: Configure the integration in PingOne Privilege"
  validation: Validation
---

# ServiceNow

You can integrate PingOne Privilege with ServiceNow to create tickets for access requests, approvals, and other events. This guide shows you how to set up the integration.

You'll need administrator access to both ServiceNow and PingOne Privilege to complete these steps.

## Step 1: Create an OAuth 2.0 endpoint in ServiceNow

First, you'll create an OAuth application in your ServiceNow instance to get the credentials PingOne Privilege needs.

1. Sign in to your ServiceNow instance with an administrator account.

2. In the navigation filter, search for `Application Registry`.

3. Click **New**, and then select **Create an OAuth API endpoint for external clients**.

4. On the registration form, fill in the following details:

   * **Name**: Enter a descriptive name, such as `PingOne Privilege Integration`.

   * **Redirect URL**: Enter the specific redirect URL for your PingOne Privilege tenant.

     |   |                                                                                                                                                                                                                                        |
     | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | The **Redirect URL** is required for the OAuth flow to complete successfully. The format is typically `https://<YOUR_P1P_TENANT_URL>/integrations/callback`. Refer to the PingOne Privilege console for the exact URL for your tenant. |

5. Click **Submit**.

6. After the application is created, ServiceNow displays the **Client ID** and **Client Secret**.

7. Copy both the **Client ID** and **Client Secret** values.

## Step 2: Configure the integration in PingOne Privilege

Now, you'll enter the credentials from ServiceNow into PingOne Privilege.

1. In the PingOne Privilege admin console, go to **Connections > Integrations**.

2. Click on the **All Integrations** tab.

3. In the **ServiceNow** tile, click **Integrate**.

4. In the **Setup ServiceNow Integration** form, fill in the following fields:

   * **Integration Name**: Provide a user-friendly name for the integration, such as `Corporate ServiceNow`.

   * **Instance URL**: Enter the full URL of your ServiceNow instance, such as `https://your-instance.service-now.com`.

   * **Client ID**: Paste the Client ID you copied from ServiceNow in the previous step.

   * **Client Secret**: Paste the Client Secret you copied from ServiceNow.

5. Click **Continue**.

## Validation

After you configure the integration, PingOne Privilege attempts to connect to your ServiceNow instance using the provided details. If the connection is successful, the integration is saved and displays in your list of active integrations. You can now select ServiceNow as a target for approval workflows in your access policies.

---

---
title: Slack integration
description: The PingOne Privilege Slack integration allows your teams to receive notifications of access requests or approvals.
component: privilege
page_id: privilege:integrations:slack
canonical_url: https://docs.pingidentity.com/privilege/integrations/slack.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2026
section_ids:
  configuring-notifications-for-approvals: Configuring notifications for approvals
  step-1-create-an-incoming-webhook-in-slack: "Step 1: Create an incoming webhook in Slack"
  step-2-add-the-webhook-to-pingone-privilege: "Step 2: Add the webhook to PingOne Privilege"
---

# Slack integration

The PingOne Privilege Slack integration allows your teams to receive notifications of access requests or approvals.

## Configuring notifications for approvals

To send approval notifications to a Slack channel, you must first create an incoming webhook in Slack and then add it to PingOne Privilege.

### Step 1: Create an incoming webhook in Slack

1. In a web browser, go to the Slack Marketplace and search for `Incoming webhooks`.

2. Click **Add to Slack**.

3. In the list, select the channel where PingOne Privilege notifications should be posted.

4. Click Add Incoming WebHooks Integration.

   ![The Incoming Webhooks integration page in the Slack App Directory](_images/slack-1.webp)![The Post to Channel dialogue box. The channel name #oncall is entered in the channel field and the Add Incoming Webhooks integration button is indicated with an arrow.](_images/slack-2.png)

5. Copy the generated **Webhook URL**. You will need this in the next step.

6. Click **Save Settings**.

   ![The Integration Settings menu. The Webhook URL and Save Settings buttons are indicated by arrows.](_images/slack-3.webp)

### Step 2: Add the webhook to PingOne Privilege

1. In the PingOne Privilege admin console, go to **Connections > Integrations**.

2. Click on the **All Integrations** tab.

3. In the **Slack** tile, click **Integrate**.

4. Enter a descriptive **Integration Name**, such as `DevOps Team Approvals`.

5. Paste the webhook URL you copied from Slack into the **Webhook Url** field.

6. Click **Continue** to create the integration.

7. On the **Active**, locate your new Slack integration and click **Manage Integration**.

8. In the **Channel-Account linking** section, click the menu button. Click **Manage**.

9. Add the cloud accounts whose JIT notifications should be handled by this integration and click **Update**.

10. In the **Notification** section, click **Select** to configure the **Gateway Notification Channel** and the **Private Server Notification Channel**.

You can create multiple integrations to send notifications for different sets of accounts to different Slack channels.