---
title: Accessing the admin console
description: Administrators access the admin console to manage and monitor privileged access across their organization.
component: privilege
page_id: privilege:privileged-access-management:admin-tasks/getting-started/accessing-admin-console
canonical_url: https://docs.pingidentity.com/privilege/privileged-access-management/admin-tasks/getting-started/accessing-admin-console.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2026
section_ids:
  launching-the-admin-console-agent-based: Launching the admin console (Agent-based)
  launching-the-admin-console-agentless: Launching the admin console (Agentless)
---

# Accessing the admin console

Administrators access the admin console to manage and monitor privileged access across their organization. There are two ways to get to the admin console, depending on whether you are using the agent-based or agentless deployment method.

## Launching the admin console (Agent-based)

1. Click the PingOne Privilege agent icon located in the system tray on Windows devices or in the menu bar on macOS devices to toggle the visibility of the PingOne Privilege App window.

2. When the PingOne Privilege app window is open, ensure that the PingOne Privilege agent is in a connected state.

3. Click **Open Console**.

4. A web browser tab will open `https://console.tun.procyon.ai` or `https://local.procyon.ai:8643` (when VPN interop mode is enabled). You can also open these URLs directly from your web browser.

## Launching the admin console (Agentless)

In agentless deployments, administrators can access the admin console directly through their PingOne environment.

---

---
title: Accessing the user console
description: Administrators access the admin console to manage and monitor privileged access across their organization.
component: privilege
page_id: privilege:privileged-access-management:user-tasks/getting-started/accessing-user-console
canonical_url: https://docs.pingidentity.com/privilege/privileged-access-management/user-tasks/getting-started/accessing-user-console.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2026
section_ids:
  launching-the-user-console-agent-based: Launching the User Console (Agent-based)
  launching-the-user-console-agentless: Launching the User Console (Agentless)
---

# Accessing the user console

Administrators access the admin console to manage and monitor privileged access across their organization. There are two ways to get to the admin console, depending on whether you are using the agent-based or agentless deployment method.

## Launching the User Console (Agent-based)

1. Click the PingOne Privilege agent icon located in the system tray on Windows devices or in the menu bar on macOS devices to toggle the visibility of the PingOne Privilege App window.

2. When the PingOne Privilege app window is open, ensure that the PingOne Privilege agent is in a connected state.

3. Click **Open Console**.

4. A web browser tab will open `https://console.tun.procyon.ai` or `https://local.procyon.ai:8643` (when VPN interop mode is enabled). You can also open these URLs directly from your web browser.

## Launching the User Console (Agentless)

In agentless deployments, users can access the user console directly through their PingOne environment.

---

---
title: Administration and Monitoring
description: The following topics show how to manage daily operations.
component: privilege
page_id: privilege:privileged-access-management:admin-tasks/index
canonical_url: https://docs.pingidentity.com/privilege/privileged-access-management/admin-tasks/index.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2026
---

# Administration and Monitoring

The following topics show how to manage daily operations, such as handling access requests, monitoring logs, and onboarding your users, devices, and critical cloud accounts:

* [Administration and Monitoring](index.html)

* [Dashboard](getting-started/dashboard.html)

* [Managing cloud resources](cloud-accounts.html)

* [Managing devices](directory/devices.html)

* [Managing users](directory/users.html)

* [Managing access requests](access-requests.html)

* [Managing groups](directory/groups.html)

* [Managing activity logs](activity/activity-logs.html)

* [Managing session logs](activity/session-logs.html)

* [Managing access requests](activity/access-request-approval-logs.html)

* [Managing passwordless access](access-management/passwordless-access.html)

* [Managing policies](access-management/policies.html)

* [Managing users](directory/users.html)

---

---
title: Administrator UI
description: PingOne Privilege provides a centralized user interface to manage and monitor privileged access across your organization.
component: privilege
page_id: privilege:privileged-access-management:admin-tasks/getting-started/admin-ui
canonical_url: https://docs.pingidentity.com/privilege/privileged-access-management/admin-tasks/getting-started/admin-ui.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2026
section_ids:
  directory: Directory
  cloud: Cloud
  access-management: Access Management
  activity: Activity
  settings: Settings
---

# Administrator UI

When an administrator accesses the admin console, PingOne Privilege provides a centralized user interface to manage and monitor privileged access across your organization.

## Directory

* **Service Accounts**: Review and approve service account requests for when users need programmatic or automation-based access.

* **Users**: Provides a centralized view to manage users, including `Administrator` and `DevOps` roles.

* **Groups**: Provides a centralized view to manage groups for organizing collections of users.

* **Devices**: Enables management of devices registered to particular users, including viewing device details and activating or deactivating an existing device.

## Cloud

* **Clouds**: Onboard cloud accounts from AWS, Azure, and GCP to manage access to cloud resources.

* **Gateways**: Configure and manage private gateways that facilitate secure access to resources in private networks.

## Access Management

* **Targets**: View and manage targets discovered from connected cloud accounts.

* **Resources**: View and manage resources discovered from connected cloud accounts.

* **SaaS Apps**: View and manage software as a service (SaaS) apps, such as GSuite.

* **Agentic Apps**: View and manage agentic apps, such as Git Server and MCP Server apps.

* **IAM Roles**: Import Amazon Web Services (AWS)-managed and custom policies for just-in-time (JIT) access.

* **Access Requests**: View, approve, or reject access requests submitted by users.

* **Policies**: Create and manage access policies that define rules for granting access to resources.

* **Bundles**: View and manage bundles that group related resources for simplified access management.

* **Tags Policies**: View and manage tags policies.

## Activity

* **Activity Logs**: View comprehensive activity records of all user actions.

* **Session Logs**: View your own SSH, database, RDP, Kubernetes, ECS, and MCP session records

## Settings

* **Integrations**: Configure integrations with third-party applications and services.

* **RDP User Management**: Create new RDP users.

* **Service Management**: Create and manage service controllers that facilitate access to services running in private networks.

* **Proxy Management**: Create and manage proxy controllers that enable secure access to resources behind firewalls.

---

---
title: Applications
description: Request just-in-time access to SAML applications.
component: privilege
page_id: privilege:privileged-access-management:user-tasks/cloud/applications
canonical_url: https://docs.pingidentity.com/privilege/privileged-access-management/user-tasks/cloud/applications.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2026
---

# Applications

In the PingOne Privilege user console, you can request access to applications in **Cloud > SaaS Apps** or **Cloud > Agentic Apps** depending on the type of application you need.

To request access, find the application in the **Active Applications** tab and click **Request**.

After the admin approves the request, you can access the application without a password for the granted duration.

---

---
title: Cloud
description: The Cloud section of the admin console provides a catalog of resources for users.
component: privilege
page_id: privilege:privileged-access-management:user-tasks/cloud/cloud
canonical_url: https://docs.pingidentity.com/privilege/privileged-access-management/user-tasks/cloud/cloud.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 8, 2026
---

# Cloud

The **Cloud** section of the admin console provides a catalog of resources for users.

In the PingOne Privilege user console, go to **Access Management > Targets** to:

* View the list of cloud accounts.

* Select an account to view all the resources within that account.

  |   |                                                                                                                              |
  | - | ---------------------------------------------------------------------------------------------------------------------------- |
  |   | Resources are only visible in **Access Management > Targets** if an administrator has managed them within the admin console. |

* View granted and ungranted resources using the checkbox selection.

* Request just-in-time access to one or more resources.

* Click the **Policies** tab to view the policy associated with the resource grant.

---

---
title: Cloud resources
description: Request just-in-time access to Azure subscriptions.
component: privilege
page_id: privilege:privileged-access-management:user-tasks/cloud/cloud-resources
canonical_url: https://docs.pingidentity.com/privilege/privileged-access-management/user-tasks/cloud/cloud-resources.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2026
---

# Cloud resources

Request just-in-time (JIT) access to Azure subscriptions.

1. In the PingOne Privilege admin console, go to **Access Management > Resources**.

2. Select the icon for the onboarded cloud infrastructure.

3. (Optional) Filter by **Access Status** and **Resource Types**.

4. Find the subscription and request access.

---

---
title: Dashboard
description: The dashboard provides quick insights into system activity.
component: privilege
page_id: privilege:privileged-access-management:admin-tasks/getting-started/dashboard
canonical_url: https://docs.pingidentity.com/privilege/privileged-access-management/admin-tasks/getting-started/dashboard.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2026
---

# Dashboard

The dashboard provides quick insights into system activity. Use the dashboard to discover:

* How many cloud accounts the system has in the **Accounts** widget

* How many users, groups, and devices are onboarded in the **Identity & Devices** widget

* How many resources the system has in the **Resources** widget

* The most active users, devices, and resources, including number of sessions

* The distribution of access to resource types

In addition, the dashboard displays an activity graph showing the number of users and resources accessed across time. You can filter a global time list at the top right of the dashboard that updates the metrics across all widgets on the page, including **Activity**.

---

---
title: Databases
description: Request just-in-time access to MySQL and Postgres databases.
component: privilege
page_id: privilege:privileged-access-management:user-tasks/cloud/databases
canonical_url: https://docs.pingidentity.com/privilege/privileged-access-management/user-tasks/cloud/databases.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2026
---

# Databases

Request just-in-time (JIT) access to MySQL and Postgres databases:

1. In the PingOne Privilege user console, go to **Access Management > Targets**.

2. Select the cloud and the account.

3. Select the appropriate principal from the list. This list is configured by a PingOne Privilege administrator.

4. Add more resources as needed and submit the request.

5. After the access request is granted by the admin, the user can access the database by copying the connection command directly from the agent UI.

---

---
title: Devices
description: Every registered device is associated with a user.
component: privilege
page_id: privilege:privileged-access-management:user-tasks/devices/devices
canonical_url: https://docs.pingidentity.com/privilege/privileged-access-management/user-tasks/devices/devices.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2026
section_ids:
  viewing-devices: Viewing devices
  activating-and-deactivating-a-device: Activating and deactivating a device
  removing-a-device: Removing a device
---

# Devices

On the PingOne Privilege platform, every registered device is associated with a user. Users can manage their devices through the user console.

## Viewing devices

To view your devices:

1. In the PingOne Privilege user console, go to **Devices > Devices**.

2. Click on a device in the list to view its details and activities.

## Activating and deactivating a device

Deactivating a device temporarily prevents it from being used to access resources.

To activate or deactivate a device:

1. In the PingOne Privilege admin console, go to **Devices > Devices**.

2. In the list, select a device to open its details.

3. Toggle **Active** to activate or deactivate the device.

## Removing a device

Removing a device permanently unregisters it from the PingOne Privilege platform. The user must onboard the device again to use it.

|   |                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------ |
|   | Deactivating or removing a device will instantly terminate all active sessions originating from that device. |

To remove a device:

1. In the PingOne Privilege admin console, go to **Devices > Devices**.

2. In the list, select a device to open its details.

3. Click **Remove Device**. Confirm the action.

---

---
title: Integrating internal applications
description: Onboard internal web apps and SAML applications for just-in-time access.
component: privilege
page_id: privilege:privileged-access-management:admin-tasks/access-management/internal-applications
canonical_url: https://docs.pingidentity.com/privilege/privileged-access-management/admin-tasks/access-management/internal-applications.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2026
section_ids:
  setting-up-an-internal-web-app: Setting up an internal web app
---

# Integrating internal applications

Onboard internal web apps and SAML applications to PingOne Privilege for just-in-time access.

## Setting up an internal web app

To configure an internal web application for proxied access, follow these steps:

1. In the PingOne Privilege admin console sidebar, go to **Applications**.

2. On the **Add Applications** tab on the **Web API (HTTP)** card, click **Integrate**.

3. Enter the **Application Name** and **Frontend URL**.

   These values are displayed to users when they access the application through the user portal.

4. In the **Backend URL** field, enter the internal DNS name or IP address of the application.

5. In the **Mesh Cluster** list, select the cluster to proxy the connection.

   The PingOne Privilege gateway associated with the selected cluster must have network access to the application's backend URL. If required, provision a new gateway before proceeding.

6. Click **Create**.

The application is now available in the inventory and can be assigned to users through a just-in-time access policy.

---

---
title: Kubernetes clusters
description: Users can request just-in-time access at the cluster, namespace, or pod level.
component: privilege
page_id: privilege:privileged-access-management:user-tasks/cloud/kubernetes-clusters
canonical_url: https://docs.pingidentity.com/privilege/privileged-access-management/user-tasks/cloud/kubernetes-clusters.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2026
section_ids:
  requsting-access-cluster: Requesting access to a cluster
  requesting-access-namespace: Requesting access to a namespace
---

# Kubernetes clusters

Users can request just-in-time (JIT) access at the cluster, namespace, or pod level.

1. In the PingOne Privilege user console, go to **Cloud > Targets**.

2. Select the cloud and the account.

3. Choose **Kube Clusters**.

4. Select the cloud type and account to find the Kube Clusters, or search by name.

## Requesting access to a cluster

To request access to a cluster:

1. Click **Request**.

2. Select the cluster-level permissions from the list:

   * `ProcyonKubectlAdmin`

   * `ProcyonKubectlClusterAdmin`

   * `ProcyonKubectlEdit`

   * `ProcyonKubectlView`

3. Choose the duration and submit the request.

## Requesting access to a namespace

To request access to a specific namespace:

1. Click **More Info** for the cluster.

2. On the **Resources** tab, select the desired namespace.

3. Select permissions, choose duration, and submit the request.

---

---
title: Managing access requests
description: "An organization administrator can perform the following actions on a user's just-in-time access requests."
component: privilege
page_id: privilege:privileged-access-management:admin-tasks/access-requests
canonical_url: https://docs.pingidentity.com/privilege/privileged-access-management/admin-tasks/access-requests.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2026
section_ids:
  approving-requests: Manually approving pending requests
  viewing-approved-requests: Viewing approved requests
  revoking-access: Revoking access
  viewing-request-history: Viewing request history
  auto-approval-policies: Managing auto-approval policies
  configuring-approval-policy: Configuring an auto-approval policy
  deleting-approval-policy: Deleting an auto-approval policy
  removing-access-one: Removing access to a resource
  removing-access-all: Revoking access to all resources
---

# Managing access requests

An organization administrator can perform the following actions on a user's just-in-time (JIT) access requests:

* [Approve or reject](#approving-requests)

* [Revoke](#revoking-access)

Additionally,

* [Manage auto-approval policies](#auto-approval-policies)

* [Remove a user's access to one resource](#removing-access-one)

* [Remove a user's access to all resources](#removing-access-all)

To manage requests, click Access Requests.

The page is organized into several tabs: Pending Requests, Approved Requests, History, and Auto Approve.

## Manually approving pending requests

The Pending Requests tab lists all submitted requests that are awaiting a decision.

1. In the PingOne Privilege admin console, click the Pending Requests tab.

2. Click View Details on a request to examine its contents.

3. Review the request details:

   * Requester name and email

   * Requested resources

   * Requested duration

   * User comments

4. Click Approve or Reject.

   The user is notified of the decision in their user portal. If Slack notifications are enabled, a message is also sent to the configured Slack channel.

## Viewing approved requests

The Approved Requests tab displays all active sessions. Click any request to view its details.

### Revoking access

An administrator can end an approved session manually before its scheduled expiration.

1. On the Approved Requests tab, find the active request you want to revoke.

2. Click View Details to open the request.

3. Click Close to terminate the session. Access to the resources is instantly revoked.

## Viewing request history

The History tab lists all past requests, including approved, closed, and expired ones. The available filters are time and user.

## Managing auto-approval policies

The Auto Approve tab lists all active auto-approval policies.

### Configuring an auto-approval policy

While approving a user's requests, you can to create a policy to automatically approve similar requests:

1. During the manual approval process for a user's request, select the Auto-approve future requests checkbox.

2. Specify the maximum duration for which future requests can be auto-approved.

3. Add any comments for auditing purposes and click Approve.

An auto-approval policy is generated for that user and is listed in the Auto Approve tab.

### Deleting an auto-approval policy

To delete an auto-approval policy:

1. On the Auto Approve tab, find the policy you want to remove.

2. Click View Details to open the policy.

3. Click Delete Auto-Approve Policy to remove the policy.

## Removing access to a resource

The following process removes a user's access to an individual resource:

1. Delete the approval request associated with the resource.

2. Delete the policy associated with the approval. Learn more about policies in [Managing policies](access-management/policies.html).

3. Delete the auto-approval policy if the access is granted through an auto-approval process.

## Revoking access to all resources

A user's access to all resources can revoked both permanently and temporarily. Access might be permanently revoked if, for example, a user reports their device stolen. Access might be temporarily revoked while, for example, the device's operating system is being patched.

To revoke a user's access to all resources **permanently**, find the user's device in Devices and [remove the device](directory/devices.html#removing-device). This instantly terminates all access for that user from that device.

To revoke a user's access to all resources **temporarily**, find the user's device in Devices and [deactivate the device](directory/devices.html#activating-deactivating-devices). This deactivates all access for that user from that device until it is reactivated.

|   |                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Users can be deactivated or deleted, as well. Deactivating or deleting a user terminates access from all devices associated with that user. |

---

---
title: Managing access requests
description: Review, approve, and manage the lifecycle of user access requests for resources.
component: privilege
page_id: privilege:privileged-access-management:admin-tasks/activity/access-request-approval-logs
canonical_url: https://docs.pingidentity.com/privilege/privileged-access-management/admin-tasks/activity/access-request-approval-logs.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 17, 2026
section_ids:
  reviewing-pending-requests: Reviewing pending requests
  viewing-approved-requests: Viewing approved requests
  viewing-auto-approval-requests: Viewing auto-approval requests
  viewing-access-request-history: Viewing access request history
---

# Managing access requests

The **Access Requests** page in the PingOne Privilege admin console is where administrators manage the lifecycle of user requests for access to resources. This includes reviewing pending requests, approving or rejecting them, and viewing the history of all access-related decisions.

## Reviewing pending requests

The **Pending** tab displays all incoming access requests that require administrative action.

1. In the PingOne Privilege admin console, go to **Access Management > Access Requests**.

2. Select the **Pending** tab.

3. For each request, you can review the user, the requested resource, and the time of the request.

4. To action a request, select it and choose one of the following options:

   * **Approve**: Grants the user access to the resource for a specified duration.

   * **Auto Approve**: Grants this and future requests from the user for this resource, based on a defined schedule.

   * **Reject**: Denies the access request.

## Viewing approved requests

The **Approved** tab shows all currently active user sessions that have been approved.

1. In the PingOne Privilege admin console, go to **Access Management > Access Requests**.

2. Select the **Approved** tab.

3. This view provides a real-time list of active sessions, including the user, resource, and the time the approval expires.

## Viewing auto-approval requests

The **Auto Approve** tab shows all requests that were approved automatically based on pre-configured policies.

1. In the PingOne Privilege admin console, go to **Access Management > Access Requests**.

2. Select the **Auto Approve** tab.

3. This view allows you to audit and review all automatically approved requests.

## Viewing access request history

The **History** tab provides a complete audit trail of all past access requests, including when they were requested, approved, or denied.

1. In the PingOne Privilege admin console, go to **Access Management > Access Requests**.

2. Select the **History** tab.

3. You can search and filter the list to find specific approval logs.

---

---
title: Managing access requests
description: Create, view, and manage your just-in-time access requests in the user portal.
component: privilege
page_id: privilege:privileged-access-management:user-tasks/access-management/access-requests
canonical_url: https://docs.pingidentity.com/privilege/privileged-access-management/user-tasks/access-management/access-requests.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2026
section_ids:
  managing-pending: Managing pending requests
  updating-pending: Updating or canceling a pending request
  managing-approved: Managing approved requests
  closing-approved: Closing an approved request
  viewing-history: Viewing request history
---

# Managing access requests

Create, view, and manage your just-in-time (JIT) access requests in the user portal.

To view your requests, click Access Requests.

The page is organized into three tabs:

* [Pending](#managing-pending)

* [Approved](#managing-approved)

* [History](#viewing-history)

## Managing pending requests

The Pending tab displays all your submitted requests that are awaiting approval. Filter the list by time or click a request to view its details.

### Updating or canceling a pending request

To update or cancel a pending request:

1. In the PingOne Privilege user console, go to the Pending tab.

2. Click View Details to open the request to update.

3. Click Edit Request and make your changes.

|   |                                                    |
| - | -------------------------------------------------- |
|   | Click Cancel Request to cancel a request entirely. |

## Managing approved requests

The Approved tab lists all requests that have been approved, granting you active access to resources. Click **View Details** on any entry for more information.

### Closing an approved request

Manually end an approved session before its scheduled expiration time:

1. In the PingOne Privilege user console, go to the **Approved** tab

2. Click View Details on the active session you want to end to open it.

3. Click Close to end the session.

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | When you close a request, your access to the associated resources is instantly and permanently revoked for that session. |

## Viewing request history

The **History** tab provides a complete audit trail of all your past requests, including those that were approved, closed, expired, or canceled. If necessary, filter this view by time and users. Click View Details to review the specifics of any past request.

---

---
title: Managing activity logs
description: Gain full visibility into user activity and system events.
component: privilege
page_id: privilege:privileged-access-management:admin-tasks/activity/activity-logs
canonical_url: https://docs.pingidentity.com/privilege/privileged-access-management/admin-tasks/activity/activity-logs.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2026
section_ids:
  viewing-general-activity-logs: Viewing general activity logs
  reviewing-a-specific-users-activity-log: Reviewing a specific user's activity log
  reviewing-a-specific-devices-activity-log: Reviewing a specific device's activity log
---

# Managing activity logs

Comprehensive activity records are available in **Activity > Activity Logs**. These logs provide a detailed record of all actions performed by users on the PingOne Privilege platform. Because the PingOne Privilege authenticator app is bound to the device's Trusted Platform Module (TPM), every action is cryptographically signed, creating a non-spoofable audit trail of all user activity.

## Viewing general activity logs

Each log entry provides details on the event, the user, the user's device, and resource details, along with a timestamp.

1. In the PingOne Privilege admin console, go to **Activity > Activity Logs**

2. The logs can be filtered by time, events, resources, and users.

## Reviewing a specific user's activity log

Administrators can also review a detailed log of all actions performed by a specific user from their user profile:

1. In the PingOne Privilege admin console, go to **Directory > Users**.

2. Find the target user in the list and click their username to open their profile.

3. On the **Activity Logs** tab, use the available filters to search the logs or narrow the results by a specific time frame or resource.

## Reviewing a specific device's activity log

1. In the PingOne Privilege admin console, go to **Directory > Devices**.

2. Find the target device in the list and click **View Details**.

3. In the **Activity Logs** tab, use the available filters to search the logs or narrow the results by a specific time frame, event type, or resource.

---

---
title: Managing cloud resources
description: When you register a cloud account the PingOne Privilege controller periodically scans the account to discover its resources.
component: privilege
page_id: privilege:privileged-access-management:admin-tasks/cloud-accounts
canonical_url: https://docs.pingidentity.com/privilege/privileged-access-management/admin-tasks/cloud-accounts.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2026
section_ids:
  targets: Targets
  configuring-targets: Configuring targets for access
  onboarding-target-resources: Onboarding target resources
  with-cloud-tags: Register using cloud provider tags
  with-admin-portal: Register using the admin portal
  resources: Resources
---

# Managing cloud resources

When you register an Amazon Web Services (AWS), Google Cloud Platform (GCP), or Azure account, the PingOne Privilege controller periodically scans the account to discover its resources.

These discovered cloud assets are categorized and displayed in two sections of the PingOne Privilege admin console:

* [Targets](#targets)

* [Resources](#resources)

## Targets

The Targets section of the admin console contains resources that users sign on to, including:

* Servers, via SSH

* Windows servers, via RDP

* Databases

* Kubernetes clusters

* Kafka clusters

* Application roles

### Configuring targets for access

Target resources must be regiastered and configured before users can access them using the self-service portal.

This involves several key configuration steps:

* Register [target resources](#onboarding-target-resources) to make them visible and manageable.

* Configure [gateways and relays](../../configuration/network-infrastructure.html) to provide secure access paths.

* Enable [certificate-based SSH](../../configuration/access-protocols/ssh.html) for Linux and macOS servers.

* Set up [database access](../../configuration/cloud-accounts/database-access.html) for supported database types.

### Onboarding target resources

Register target resources with PingOne Privilege to make them available for self-service. When you register a resource, it appears in the Targets menu of the admin console.

Register target resources using:

* [Cloud provider tags](#with-cloud-tags)

* [PingOne Privilege admin console](#with-admin-portal)

#### Register using cloud provider tags

You can automatically register target resources by assigning a specific tag to resources within your AWS, GCP, or Azure accounts.

The PingOne Privilege platform discovers and manages resources with the following tag and value pair:

* **Tag**: `PingOne Privilege`

* **Value**: `managed`

#### Register using the admin portal

To use the admin console to register individual target resources:

1. In the PingOne Privilege admin console, click Targets.

2. (Optional) Filter resources using any of the following:

   **Access status:** Select the Ungranted filter checkbox and ensure the Granted filter checkbox is cleared.

   **Target type:** Select a target type checkbox, such as server or database.

   **Cloud provider:** Select a Cloud Provider icon.

   **Cloud account:** Select the specific account from the Account list.

3. Use the list to locate the resource to register and then click **More Info**.

4. On the resource details page, click the **Managed** toggle in the upper-right corner.

|   |                                                                                                |
| - | ---------------------------------------------------------------------------------------------- |
|   | Use the search bar to find a specific resource quickly before clicking More Info to manage it. |

## Resources

The Resources section of the admin console displays cloud assets that do not require users to sign on, such as:

* Storage buckets

* Serverless functions

* Related platform services

Access to these resources is managed using temporary cloud provider identity and access management (IAM) roles. Once access is allowed, you can use resources via a command-line interface (CLI) or the cloud provider's web console.

---

---
title: Managing devices
description: Every registered device is uniquely associated with a single user, and each user can have one or more registered devices.
component: privilege
page_id: privilege:privileged-access-management:admin-tasks/directory/devices
canonical_url: https://docs.pingidentity.com/privilege/privileged-access-management/admin-tasks/directory/devices.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2026
section_ids:
  before-you-begin: Before you begin
  device-onboarding-process: Device onboarding process
  viewing-and-searching-for-devices: Viewing and searching for devices
  viewing-devices-owned-by-a-specific-user: Viewing devices owned by a specific user
  activating-deactivating-devices: Activating and deactivating a device
  removing-device: Removing a device
---

# Managing devices

On the PingOne Privilege platform, every registered device is uniquely associated with a single user, and each user can have one or more registered devices.

## Before you begin

Users must onboard devices before they can use them to access resources with PingOne Privilege. For information about onboarding devices, see the following topics:

## Device onboarding process

When a user onboards a device, the following sequence of events occurs:

1. The PingOne Privilege authenticator app creates a new public/private key pair on the user's device.

2. The private key is stored securely within the device's TPM and is configured to be non-exportable. The corresponding public key is sent to the PingOne Privilege controller.

3. A device certificate is generated locally and signed by the new private key. The device, now identified by this certificate, is registered with the PingOne Privilege controller.

4. On laptops, a persistent mutual TLS (mTLS) connection is established with the PingOne Privilege controller.

   This connection is required for passwordless resource access and has the following characteristics:

   * The mTLS connection remains active as long as the laptop is running.

   * If the laptop wakes from a sleep state, the connection is automatically re-established.

   * The connection can be manually disconnected using a toggle switch in the authenticator app.

## Viewing and searching for devices

To view and search for devices registered on the PingOne Privilege platform:

1. In the PingOne Privilege admin console, go to **Directory > Devices**.

2. Use the search bar to find a specific device by username, device model, OS version, or device name.

3. Click any device in the list to view its detailed information.

## Viewing devices owned by a specific user

To view all devices registered to a specific user:

1. In the PingOne Privilege admin console, go to **Directory > Users**.

2. Find the target user in the list and click their name to open their profile.

3. The **Overview** section displays a list of all devices registered to that user.

## Activating and deactivating a device

Deactivating a device temporarily prevents it from being used to access resources.

To activate or deactivate a device:

1. In the PingOne Privilege admin console, go to **Directory > Devices**.

2. In the list, select a device to open its details.

3. Toggle **Active** to activate or deactivate the device.

## Removing a device

Removing a device permanently unregisters it from the PingOne Privilege platform. The user must onboard the device again to use it.

|   |                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------ |
|   | Deactivating or removing a device will instantly terminate all active sessions originating from that device. |

To remove a device:

1. In the PingOne Privilege admin console, go to **Directory > Devices**.

2. In the list, select a device to open its details.

3. Click **Remove Device**. Confirm the action.

---

---
title: Managing groups
description: Groups are collections of users that can be used to assign access policies efficiently.
component: privilege
page_id: privilege:privileged-access-management:admin-tasks/directory/groups
canonical_url: https://docs.pingidentity.com/privilege/privileged-access-management/admin-tasks/directory/groups.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 8, 2026
---

# Managing groups

Group management for PingOne Privilege is centralized within the PingOne platform. Groups are collections of users that can be used to assign access policies efficiently.

Administrators should use the PingOne admin console to create groups and manage their memberships. Learn more in [Groups](https://docs.pingidentity.com/pingone/directory/p1_groups.html) in the PingOne documentation.

---

---
title: Managing passwordless access
description: This feature eliminates the need for users to manage or directly handle static credentials, such as passwords or SSH keys, for the target systems.
component: privilege
page_id: privilege:privileged-access-management:admin-tasks/access-management/passwordless-access
canonical_url: https://docs.pingidentity.com/privilege/privileged-access-management/admin-tasks/access-management/passwordless-access.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2026
section_ids:
  passwordless-admins: Passwordless SSH access for administrators
  procedure: Procedure
---

# Managing passwordless access

PingOne Privilege enables passwordless access to onboarded resources for both administrators and end users. This feature eliminates the need for users to manage or directly handle static credentials, such as passwords or SSH keys, for the target systems.

Access is brokered through short-lived certificates or tokens, that are automatically generated and managed by the platform.

To use this feature, resources must first be onboarded. Learn more in [Onboarding target resources](../cloud-accounts.html#onboarding-target-resources).

## Passwordless SSH access for administrators

Admins have passwordless access to all the resources within the tenant. To connect to a resource using passwordless SSH:

### Procedure

If you are using the PingOne Privilege agent:

1. Open the PingOne Privilege agent.

2. Click on the **Stack icon**.

3. Find the target in the list. Copy the SSH command.

4. Run the SSH command in your terminal.

If you are using the `pcli` command line tool:

1. If necessary, log in to your tenant by running `pcli auth login <your-tenant-name>`.

2. Confirm your server is available by running `pcli server list`.

3. Run `pcli server checkout <your-server-name> <your-ssh-user> --connect=true`.