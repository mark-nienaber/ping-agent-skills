---
title: Access request integrations
description: Connect PingOne Privilege with Jira, Microsoft Teams, ServiceNow, and Slack to manage access requests, approvals, and notifications where your teams work.
component: privilege
page_id: privilege:integrations:access-request-integrations/index
canonical_url: https://docs.pingidentity.com/privilege/integrations/access-request-integrations/index.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 11, 2026
section_ids:
  supported-access-request-integrations: Supported access request integrations
---

# Access request integrations

PingOne Privilege connects with the collaboration and ticketing services your teams already use, so access requests and approvals happen where your users work instead of only in the PingOne Privilege consoles.

## Supported access request integrations

![](../_images/p1p-integrations-jira-logo.png)

#### [Jira](jira.html)

Integrate PingOne Privilege with Jira to manage privileged access requests through Jira.

![](../_images/p1p-integrations-microsoft-teams-logo.png)

#### [Microsoft Teams](microsoft-teams.html)

Integrate PingOne Privilege with Microsoft Teams to manage access requests and approvals.

![](../_images/p1p-integrations-servicenow-logo.png)

#### [ServiceNow](servicenow.html)

Integrate PingOne Privilege with ServiceNow to create and manage access request tickets.

![](../_images/p1p-integrations-slack-logo.png)

#### [Slack](slack.html)

Integrate PingOne Privilege with Slack to manage privileged access through Slack.

---

---
title: AWS Secrets Manager integration
description: Connect AWS Secrets Manager to PingOne Privilege as a secrets hub so users can use secrets stored in AWS secrets manager.
component: privilege
page_id: privilege:integrations:secrets-hubs/aws-secrets-manager
canonical_url: https://docs.pingidentity.com/privilege/integrations/secrets-hubs/aws-secrets-manager.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 12, 2026
section_ids:
  configure-aws-secrets-manager-integration: Configure AWS Secrets Manager integration
  before-you-begin: Before you begin
  add-aws-secrets-manager-as-a-secrets-hub: Add AWS Secrets Manager as a secrets hub
  use-cases: Use cases
  rotating-secrets: Rotating secrets
  auditing-secret-usage: Auditing secret usage
---

# AWS Secrets Manager integration

Connect AWS Secrets Manager to PingOne Privilege as a secrets hub so that users can use secrets stored in AWS Secrets Manager.

## Configure AWS Secrets Manager integration

### Before you begin

Ensure you have the following:

* The required permissions in AWS to deploy the provided CloudFormation template.

* Your AWS administrator can provide the **Role ARN** generated in the CloudFormation stack outputs.

### Add AWS Secrets Manager as a secrets hub

1. In the PingOne Privilege admin console, go to **Secrets > Hubs**.

2. On the **Secrets Hubs** page, click the **Add Hubs** tab.

3. In the **AWS** tile, click **Integrate [icon: plus, set=fa]**.

4. Enter a **Name** and optional **Description** for the **Hub**. Click **Next**.

5. To access the AWS console, either copy and paste the **CloudFormation Template URL** in a new browser tab or click the **Open CF Template In AWS Console** button.

6. In the AWS console, create the **CloudFormation** stack using the provided template.

7. When prompted, enter the **External ID** copied from PingOne Privilege.

8. Verify that you copied the Role ARN from the completed stack outputs, then paste it into the configuration window.

   PingOne Privilege validates the ARN format before allowing you to continue.

9. Click **Next**.

10. On the **Filters** step, optionally select **AWS Regions** or secret tag key-value pairs. Leave both empty to synchronize all secrets. Click **Next**.

11. Review the summary, including any filters, and submit the configuration.

    PingOne Privilege validates duplicate Hub names before submission.

12. Validate the connection:

    1. In the **Active Hubs** tab, locate the new hub.

    2. Open the hub and verify that its connection status is **Synced**.

       |   |                                                                                                                                                                                     |
       | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
       |   | A new or resynchronizing hub might temporarily display a pending status or a **Syncing…​** indicator. If the status is **Error**, review the hub configuration and AWS permissions. |

## Use cases

You can use the AWS Secrets Manager hub for the following use cases.

### Rotating secrets

When a session that used an injected secret checks in, PingOne Privilege triggers the configured rotation operation for that secret in AWS Secrets Manager.

This means:

* The secret used by the checked-in session is rotated in AWS Secrets Manager without manual intervention.

* The next session that requests the secret receives the current value.

Automatic rotation must be configured for the secret in AWS Secrets Manager, and the role used by PingOne Privilege must have the permissions required for the configured rotation operation.

### Auditing secret usage

Each use of a secret is recorded as an audit event in the PingOne Privilege audit trail. The event includes the secret name as metadata.

1. In the PingOne Privilege admin console, go to **Activity > Activity Logs**.

2. Use the available filters to locate the session or user activity.

3. Review the audit event and confirm that it includes the name of the secret that was used.

---

---
title: Azure Key Vault integration
description: "Connect Azure Key Vault to PingOne Privilege as a secrets hub for users' secure credentials."
component: privilege
page_id: privilege:integrations:secrets-hubs/azure-key-vault
canonical_url: https://docs.pingidentity.com/privilege/integrations/secrets-hubs/azure-key-vault.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 12, 2026
section_ids:
  setup: Setup
  requirements: Requirements
  configure-azure-key-vault-integration: Configure Azure Key Vault integration
  before-you-begin: Before you begin
  add-azure-key-vault-as-a-secrets-hub: Add Azure Key Vault as a secrets hub
  use-cases: Use cases
  rotating-secrets: Rotating secrets
  auditing-secret-usage: Auditing secret usage
---

# Azure Key Vault integration

Connect Azure Key Vault to PingOne Privilege as a secrets hub so that users can use secrets stored in Azure Key Vault.

## Setup

### Requirements

## Configure Azure Key Vault integration

### Before you begin

Ensure you have the following:

* A deployed Azure Key Vault set up with the policies and permissions your organization requires.

* Azure credentials that PingOne Privilege can use to read the secrets it injects.

### Add Azure Key Vault as a secrets hub

1. In the PingOne Privilege admin console, go to **Secrets > Hubs**.

2. On the **Secrets Hubs** page, click the **Add Hubs** tab.

3. In the **Azure** tile, click **Integrate [icon: plus, set=fa]**.

4. Enter a **Name** and optional **Description** for the **Hub**. Click **Next**.

5. Follow the instructions in the wizard for creating an **App Registration** in Azure Active Directory.

6. Return to the setup wizard, click **Next**, and enter the required fields from the **App Registration** creation:

   * **Tenant ID**

   * **Client ID**

   * **Client Secret**

   * **Subscription ID**

7. Click **Next**.

8. Review the summary, including any filters, and submit the configuration.

9. Validate the connection:

   1. In the **Active Hubs** tab, locate the new hub.

   2. Open the hub and verify that its connection status is **Synced**.

      |   |                                                                                                                                                                                       |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | A new or resynchronizing hub might temporarily display a pending status or a **Syncing…​** indicator. If the status is **Error**, review the hub configuration and Azure permissions. |

## Use cases

You can use the Azure Key Vault hub for the following use cases.

### Rotating secrets

When a session that used an injected secret checks in, PingOne Privilege triggers the configured rotation operation for that secret in Azure Key Vault.

This means:

* The secret used by the checked-in session is rotated in Azure Key Vault without manual intervention.

* The next session that requests the secret receives the current value.

Automatic rotation must be configured for the secret in Azure Key Vault, and the credentials used by PingOne Privilege must have the permissions required for the configured rotation operation.

### Auditing secret usage

Each use of a secret is recorded as an audit event in the PingOne Privilege audit trail. The event includes the secret name as metadata.

1. In the PingOne Privilege admin console, go to **Activity > Activity Logs**.

2. Use the available filters to locate the session or user activity.

3. Review the audit event and confirm that it includes the name of the secret that was used.

---

---
title: Delinea Secret Server integration
description: Connect Delinea Secret Server to PingOne Privilege as a secrets hub for secure credential injection.
component: privilege
page_id: privilege:integrations:secrets-hubs/delinea-secret-server
canonical_url: https://docs.pingidentity.com/privilege/integrations/secrets-hubs/delinea-secret-server.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 12, 2026
section_ids:
  configure-delinea-secret-server-integration: Configure Delinea Secret Server integration
  before-you-begin: Before you begin
  add-delinea-secret-server-as-a-secrets-hub: Add Delinea Secret Server as a secrets hub
  use-cases: Use cases
  rotating-secrets: Rotating secrets
  auditing-secret-usage: Auditing secret usage
---

# Delinea Secret Server integration

Connect Delinea Secret Server to PingOne Privilege as a secrets hub so that users can use secrets stored in Delinea Secret Server.

## Configure Delinea Secret Server integration

### Before you begin

Ensure you have the following:

* A deployed Delinea Secret Server set up with the policies and permissions your organization requires.

* Delinea credentials that PingOne Privilege can use to read the secrets it will inject, such as an API user account.

* Your Delinea credentials have read access to the secrets you'll map to targets, as well as rotation permissions if you want automatic rotation on session check-in.

### Add Delinea Secret Server as a secrets hub

1. In the PingOne Privilege admin console, go to **Secrets > Hubs**.

2. On the **Secrets Hubs** page, click the **Add Hubs** tab.

3. In the **Delinea** tile, click **Integrate [icon: plus, set=fa]**.

4. Enter a **Name** and optional **Description** for the **Hub**. Click **Next**.

5. Follow the instructions in the wizard for the configuration steps in Delinea. Click **Next**.

6. Complete the following required credentials from your Delinea Secret Server instance:

   * **Server URL**

   * **Client ID**

   * **Client Secret**

7. Click **Next**.

8. Review the summary, including any filters, and submit the configuration.

9. Validate the connection:

   1. In the **Active Hubs** tab, locate the new hub.

   2. Open the hub and verify that its connection status is **Synced**.

      |   |                                                                                                                                                                                         |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | A new or resynchronizing hub might temporarily display a pending status or a **Syncing…​** indicator. If the status is **Error**, review the hub configuration and Delinea permissions. |

## Use cases

You can use the Delinea Secret Server hub for the following use cases.

### Rotating secrets

When a session that used an injected secret checks in, PingOne Privilege triggers the configured rotation operation for that secret in Delinea Secret Server.

This means:

* The secret used by the checked-in session is rotated in Delinea Secret Server without manual intervention.

* The next session that requests the secret receives the current value.

Automatic rotation must be configured for the secret in Delinea Secret Server, and the credentials used by PingOne Privilege must have the permissions required for the configured rotation operation.

### Auditing secret usage

Each use of a secret is recorded as an audit event in the PingOne Privilege audit trail. The event includes the secret name as metadata.

1. In the PingOne Privilege admin console, go to **Activity > Activity Logs**.

2. Use the available filters to locate the session or user activity.

3. Review the audit event and confirm that it includes the name of the secret that was used.

---

---
title: GCP Secrets Manager integration
description: Connect GCP Secrets Manager to PingOne Privilege as a secrets hub for secure credential injection.
component: privilege
page_id: privilege:integrations:secrets-hubs/gcp-secrets-manager
canonical_url: https://docs.pingidentity.com/privilege/integrations/secrets-hubs/gcp-secrets-manager.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 12, 2026
section_ids:
  configure-gcp-secrets-manager-integration: Configure GCP Secrets Manager integration
  before-you-begin: Before you begin
  add-gcp-secrets-manager-as-a-secrets-hub: Add GCP Secrets Manager as a secrets hub
  use-cases: Use cases
  rotating-secrets: Rotating secrets
  auditing-secret-usage: Auditing secret usage
---

# GCP Secrets Manager integration

Connect GCP Secrets Manager to PingOne Privilege as a secrets hub so that users can use secrets stored in GCP Secrets Manager.

## Configure GCP Secrets Manager integration

### Before you begin

Ensure you have the following:

* A deployed GCP Secrets Manager set up with the policies and permissions your organization requires.

* GCP credentials that PingOne Privilege can use to read the secrets it injects, such as a service account.

* Your GCP credentials have read access to the secrets you map to targets, as well as rotation permissions if you want automatic rotation on session check-in.

### Add GCP Secrets Manager as a secrets hub

1. In the PingOne Privilege admin console, go to **Secrets > Hubs**.

2. On the **Secrets Hubs** page, click the **Add Hubs** tab.

3. In the **GCP** tile, click **Integrate [icon: plus, set=fa]**.

4. Enter a **Name** and optional **Description** for the **Hub**. Click **Next**.

5. Select the type of GCP account you want to add as a **Hub**:

   * **Organization**

   * **Folder**

   * **Project**

6. Follow the setup wizard for the account type selected. Click **Next**.

7. Paste the Key JSON for the account type configured in the previous step. Click **Next**.

8. Review the summary, including any filters, and submit the configuration.

9. Validate the connection:

   1. In the **Active Hubs** tab, locate the new hub.

   2. Open the hub and verify that its connection status is **Synced**.

      |   |                                                                                                                                                                                     |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | A new or resynchronizing hub might temporarily display a pending status or a **Syncing…​** indicator. If the status is **Error**, review the hub configuration and GCP permissions. |

## Use cases

You can use the GCP Secrets Manager hub for the following use cases.

### Rotating secrets

When a session that used an injected secret checks in, PingOne Privilege triggers the configured rotation operation for that secret in GCP Secrets Manager.

This means:

* The secret used by the checked-in session is rotated in GCP Secrets Manager without manual intervention.

* The next session that requests the secret receives the current value.

Automatic rotation must be configured for the secret in GCP Secrets Manager, and the credentials used by PingOne Privilege must have the permissions required for the configured rotation operation.

### Auditing secret usage

Each use of a secret is recorded as an audit event in the PingOne Privilege audit trail. The event includes the secret name as metadata.

1. In the PingOne Privilege admin console, go to **Activity > Activity Logs**.

2. Use the available filters to locate the session or user activity.

3. Review the audit event and confirm that it shows the secret name.

---

---
title: Integrations
description: Integrate PingOne Privilege with collaboration services and external secrets hubs to manage privileged access where your teams work
component: privilege
page_id: privilege:integrations:index
canonical_url: https://docs.pingidentity.com/privilege/integrations/index.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 11, 2026
---

# Integrations

If you're using Human Privilege or Agent Privilege, PingOne Privilege integrates with the systems your organization already uses:

* [Access request integrations](access-request-integrations/index.html)

  Connect PingOne Privilege with Jira, Microsoft Teams, ServiceNow, and Slack to manage access requests, approvals, and notifications where your teams work.

* [Secrets hubs](secrets-hubs/index.html)

  Connect external vaults, such as AWS Secrets Manager, Azure Key Vault, Delinea Secret Server, and GCP Secrets Manager, for secure credential injection into privileged sessions.

---

---
title: Jira integration
description: The Jira integration automatically creates and updates Jira issues to track just-in-time access requests.
component: privilege
page_id: privilege:integrations:access-request-integrations/jira
canonical_url: https://docs.pingidentity.com/privilege/integrations/access-request-integrations/jira.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2026
page_aliases: ["integrations:jira.adoc"]
section_ids:
  configure-jira-integration: Configure Jira integration
  step-1-add-a-jira-integration-in-pingone-privilege: "Step 1: Add a Jira integration in PingOne Privilege"
  step-2-configure-jira-projects-for-jit-requests: "Step 2: Configure Jira projects for JIT requests"
  jira-task-lifecycle: Jira task lifecycle
---

# Jira integration

The PingOne Privilege Jira integration automatically creates and updates Jira issues to track just-in-time (JIT) access requests. When a user submits a JIT request, a corresponding task is created in the configured Jira project. The task then updates automatically when the request is approved or denied.

## Configure Jira integration

### Step 1: Add a Jira integration in PingOne Privilege

1. In the PingOne Privilege admin console, go to **Infrastructure > Integrations**.

2. Click the **All Integrations** tab.

3. On the **Jira** tile, click **Integrate [icon: plus, set=fa]**.

4. Enter a descriptive **Name** for the integration.

5. Enter **Project Keys** separated by commas or select **Fetch All Project**.

6. Click **Continue**.

   You'll be redirected to the Atlassian authorization page.

7. Review the requested permissions and click **Accept** to grant access.

### Step 2: Configure Jira projects for JIT requests

After setting up the integration, associate your Jira projects with the cloud accounts they'll track:

1. In the PingOne Privilege admin console, go to **Infrastructure > Integrations**.

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
page_id: privilege:integrations:access-request-integrations/microsoft-teams
canonical_url: https://docs.pingidentity.com/privilege/integrations/access-request-integrations/microsoft-teams.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 5, 2026
page_aliases: ["integrations:microsoft-teams.adoc"]
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

1. In the PingOne Privilege admin console, go to **Infrastructure > Integrations**.

2. Click the **All Integrations** tab.

3. In the **Microsoft Teams** tile, click **Integrate [icon: plus, set=fa]**.

4. Enter a descriptive **Integration Name**, such as `DevOps Team Approvals`.

5. Paste the webhook URL you copied from Microsoft Teams into the **Webhook Url** field.

6. Click **Continue** to create the integration.

7. On the **Active**, locate your new **Microsoft Teams** integration and click **Manage Integration**.

8. In the **Channel-Account linking** section, click the menu button. Click **Manage**.

9. Add the cloud accounts whose JIT notifications should be handled by this integration and click **Update**.

10. In the **Notification** section, click **Select** to configure the **GateWay Notification Channel** and the **Private Server Notification Channel**.

|   |                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------- |
|   | You can create multiple integrations to send notifications for different sets of accounts to different Microsoft Teams channels. |

---

---
title: Secrets hubs
description: Connect external vaults to PingOne Privilege as secrets hubs for secrets management.
component: privilege
page_id: privilege:integrations:secrets-hubs/index
canonical_url: https://docs.pingidentity.com/privilege/integrations/secrets-hubs/index.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 11, 2026
section_ids:
  supported-secrets-hubs: Supported secrets hubs
---

# Secrets hubs

PingOne Privilege can use external vaults as secrets hubs, enabling administrators to control and manage access to secrets stored within those external vaults. Users can check out these secrets based on granular policy. Every secret use is recorded as an audit event with the secret name as metadata.

## Supported secrets hubs

![](../_images/p1p-integrations-aws-secrets-manager.svg)

#### [AWS Secrets Manager](aws-secrets-manager.html)

Connect AWS Secrets Manager to PingOne Privilege as a secrets hub for secure credential injection into privileged sessions.

![](../_images/p1p-integrations-azure.svg)

#### [Azure Key Vault](azure-key-vault.html)

Connect Azure Key Vault to PingOne Privilege as a secrets hub for secure credential injection into privileged sessions.

![](../_images/p1p-integrations-delinea.svg)

#### [Delinea Secret Server](delinea-secret-server.html)

Connect Delinea Secret Server to PingOne Privilege as a secrets hub for secure credential injection into privileged sessions.

![](../_images/p1p-integrations-gcp.png)

#### [GCP Secrets Manager](gcp-secrets-manager.html)

Connect GCP Secrets Manager to PingOne Privilege as a secrets hub for secure credential injection into privileged sessions.

---

---
title: ServiceNow
description: You can integrate PingOne Privilege with ServiceNow to create access request tickets.
component: privilege
page_id: privilege:integrations:access-request-integrations/servicenow
canonical_url: https://docs.pingidentity.com/privilege/integrations/access-request-integrations/servicenow.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 5, 2026
page_aliases: ["integrations:servicenow.adoc"]
section_ids:
  configure-servicenow-integration: Configure ServiceNow integration
  before-you-begin: Before you begin
  step-1-create-an-oauth-2-0-endpoint-in-servicenow: "Step 1: Create an OAuth 2.0 endpoint in ServiceNow"
  step-2-create-a-servicenow-integration-in-pingone-privilege: "Step 2: Create a ServiceNow integration in PingOne Privilege"
  result: Result
---

# ServiceNow

You can integrate PingOne Privilege with ServiceNow to create tickets for access requests, approvals, and other events.

## Configure ServiceNow integration

### Before you begin

Ensure you have administrator access to both ServiceNow and PingOne Privilege.

### Step 1: Create an OAuth 2.0 endpoint in ServiceNow

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

### Step 2: Create a ServiceNow integration in PingOne Privilege

Now, you'll enter the credentials from ServiceNow into PingOne Privilege.

1. In the PingOne Privilege admin console, go to **Infrastructure > Integrations**.

2. Click the **All Integrations** tab.

3. In the **ServiceNow** tile, click **Integrate [icon: plus, set=fa]**.

4. In the **Setup ServiceNow Integration** form, fill in the following fields:

   * **Integration Name**: Provide a user-friendly name for the integration, such as `Corporate ServiceNow`.

   * **Instance URL**: Enter the full URL of your ServiceNow instance, such as `https://your-instance.service-now.com`.

   * **Client ID**: Paste the Client ID you copied from ServiceNow in the previous step.

   * **Client Secret**: Paste the Client Secret you copied from ServiceNow.

5. Click **Continue**.

### Result

After you configure the integration, PingOne Privilege attempts to connect to your ServiceNow instance using the provided details. If the connection is successful, the integration is saved and displays in your list of active integrations. You can now select ServiceNow as a target for approval workflows in your access policies.

---

---
title: Slack integration
description: The PingOne Privilege Slack integration allows your teams to receive notifications of access requests or approvals.
component: privilege
page_id: privilege:integrations:access-request-integrations/slack
canonical_url: https://docs.pingidentity.com/privilege/integrations/access-request-integrations/slack.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2026
page_aliases: ["integrations:slack.adoc"]
section_ids:
  configuring-notifications-for-approvals: Configuring notifications for approvals
  step-1-create-an-incoming-webhook-in-slack: "Step 1: Create an incoming webhook in Slack"
  step-2-add-the-webhook-to-pingone-privilege: "Step 2: Add the webhook to PingOne Privilege"
  result: Result
---

# Slack integration

The PingOne Privilege Slack integration allows your teams to receive notifications of access requests or approvals.

## Configuring notifications for approvals

To send approval notifications to a Slack channel, you must first create an incoming webhook in Slack and then add it to PingOne Privilege.

### Step 1: Create an incoming webhook in Slack

1. In a web browser, go to the Slack Marketplace.

2. Sign on with your Slack credentials.

3. In the search bar, type `Incoming webhooks`.

4. Click **Add to Slack**.

5. In the list, select the channel where PingOne Privilege notifications should be posted.

6. Click **Add Incoming WebHooks Integration**.

   ![The Incoming Webhooks integration page in the Slack App Directory.](../_images/p1p-integrations-slack-incoming-webhooks.webp)![The Post to Channel dialogue box. The channel name #oncall is entered in the channel field and the Add Incoming Webhooks integration button is indicated with an arrow.](../_images/p1p-integrations-slack-incoming-webhooks-add.png)

7. Copy the generated **Webhook URL**. Save this for the next step.

8. Click **Save Settings**.

   ![The Integration Settings menu. The Webhook URL and Save Settings buttons are indicated by arrows.](../_images/p1p-integrations-slack-integration-settings.webp)

### Step 2: Add the webhook to PingOne Privilege

1. In the PingOne Privilege admin console, go to **Infrastructure > Integrations**.

2. Click the **All Integrations** tab.

3. In the **Slack** tile, click **Integrate [icon: plus, set=fa]**.

4. Enter a descriptive **Integration Name**, such as `DevOps Team Approvals`.

5. Paste the webhook URL you copied from Slack into the **Webhook Url** field.

6. Click **Continue** to create the integration.

7. On the **Active**, locate your new Slack integration and click **Manage Integration**.

8. In the **Channel-Account linking** section, click the menu button. Click **Manage**.

9. Add the cloud accounts whose JIT notifications should be handled by this integration and click **Update**.

10. In the **Notification** section, click **Select** to configure the **Gateway Notification Channel** and the **Private Server Notification Channel**.

### Result

You can create multiple integrations to send notifications for different sets of accounts to different Slack channels.