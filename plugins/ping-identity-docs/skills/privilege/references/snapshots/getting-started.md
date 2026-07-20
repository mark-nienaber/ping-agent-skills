---
title: Accessing the PingOne Privilege admin console as an administrator
description: The admin console provides a centralized interface to configure settings, manage users, and monitor access activities.
component: privilege
page_id: privilege:getting-started:accessing-admin-console
canonical_url: https://docs.pingidentity.com/privilege/getting-started/accessing-admin-console.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 8, 2026
section_ids:
  accessing-the-admin-console-agent-based: Accessing the admin console (agent-based)
  accessing-the-admin-console-agentless: Accessing the admin console (agentless)
---

# Accessing the PingOne Privilege admin console as an administrator

The PingOne Privilege admin console provides a centralized interface to configure settings, manage users, and monitor access activities.

## Accessing the admin console (agent-based)

After completing the initial setup of your PingOne Privilege environment in PingOne, you must onboard your device.

To access the admin console:

1. In the PingOne admin console, go to **Directory > Users**.

2. Click the user you would like to provide initial access to the PingOne Privilege admin console.

3. In the **Services** list, select **PingOne Privilege**.

4. Click **Generate Onboarding Link**.

   A link is automatically sent through email if an email address is configured for the PingOne admin user.

5. Open the link sent to email or copy the generated onboarding link and open it in a new browser tab.

6. In the new tab, download the PingOne Privilege agent and complete the installation on your computer.

7. Click the PingOne Privilege agent icon in your system tray. Click **Open Console**.

   ![The PingOne Privilege agent icon menu with the Open Console option visible.](_images/p1p_open_console.png)

   The PingOne Privilege admin console will open in a new browser tab.

You can now use the PingOne Privilege environment to onboard users.

## Accessing the admin console (agentless)

After completing the initial setup of your PingOne Privilege environment in PingOne, you must authenticate into the PingOne Privilege admin console.

1. In the PingOne admin console, go to **Settings > Environment Properties**.

2. In the **URLs** section, click the **PingOne Privilege Console Url** link.

   A new tab opens to provide credentials for the PingOne Privilege admin console.

3. Enter the **Username** and **Password** for the PingOne admin user.

4. Click **Sign On**.

---

---
title: Choosing a deployment model
description: PingOne Privilege offers both agent-based and agentless deployment models to meet different organizational needs and security requirements.
component: privilege
page_id: privilege:getting-started:choosing-deployment-model
canonical_url: https://docs.pingidentity.com/privilege/getting-started/choosing-deployment-model.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 8, 2026
section_ids:
  agent-based-deployment: Agent-based deployment
  agentless-deployment: Agentless deployment
  gateways-and-resource-access: Gateways and resource access
---

# Choosing a deployment model

PingOne Privilege offers agent-based and agentless deployment models. Choosing the right model depends on your organization's priorities for security, ease of deployment, and user experience.

## Agent-based deployment

The agent-based model is recommended for organizations requiring the highest level of device and user identity assurance. In this model, users install the PingOne Privilege agent on their device. The agent leverages the device's Trusted Platform Module (TPM) to create a strong, hardware-backed identity.

![Diagram showing agent-based deployment architecture](_images/p1p_agent_based_deployment.png)

Key features of this model include:

* Strong device and user identity verification.

* Continuous authorization and session monitoring.

* Enhanced security for sensitive environments.

## Agentless deployment

The agentless model is ideal for organizations seeking a fast, low-friction rollout, or for environments where agents can't be installed. Users access resources like SSH, cloud CLIs, and Kubernetes using the PingOne Privilege CLI (PCLI) shell utility.

![Diagram showing agentless deployment architecture](_images/p1p_agentless_deployment.png)

Key features of this model include:

* Rapid deployment with no client-side software installation.

* Flexibility for organizations with diverse device management policies.

* A phased approach to privileged access management (PAM).

* Some trade-offs in device identity assurance compared to the agent-based model.

## Gateways and resource access

Both deployment models require gateways to access on-premises resources like servers, databases, and Kubernetes clusters. Direct access to cloud accounts (such as AWS, GCP, and Azure) is supported without a gateway. For resources behind a firewall, session logs are captured at the gateway for both models.

---

---
title: Key concepts
description: Understand the foundational concepts of PingOne Privilege, including PAM, the role of the agent, and how it secures access to cloud infrastructure.
component: privilege
page_id: privilege:getting-started:key-concepts
canonical_url: https://docs.pingidentity.com/privilege/getting-started/key-concepts.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2026
section_ids:
  core-concepts: Core concepts
  privileged-access-management-pam: Privileged access management (PAM)
  trusted-platform-module-tpm-and-secure-enclave: Trusted Platform Module (TPM) and Secure Enclave
  how-pingone-privilege-works: How PingOne Privilege works
  pingone-privilege-agent: PingOne Privilege agent
  agentless-cli: Agentless CLI
---

# Key concepts

This section introduces the foundational ideas behind PingOne Privilege. These topics explain the challenges of securing cloud infrastructure and how PingOne Privilege addresses these with modern, identity-based solutions. Use this section to understand the principles and practices that guide secure access for both human and non-human identities.

## Core concepts

### Privileged access management (PAM)

PAM is a set of principles and practices to control, monitor, and secure access to critical resources by both human and machine identities. In short, PAM ensures that users have the right-sized permissions essential to access critical resources, such as infrastructures, applications, or data essential to an organization's operations.

In simpler terms, PAM ensures that privileged users have access with the right-sized permissions to access critical resources. Critical resources are infrastructures, applications, or data essential to an organization's operations, and could cause significant harm if compromised or unavailable.

### Trusted Platform Module (TPM) and Secure Enclave

Modern Windows and Mac laptops include hardware-based security features like the TPM chip or Apple's Secure Enclave. These provide a secure, tamper-resistant location for storing private keys, offering stronger security than file-based credentials because the keys can't be directly read or extracted.

## How PingOne Privilege works

![Logical architecture diagram showing the components of the product and how they interact](_images/p1p_logical_architecture.png)

PingOne Privilege acts as an infrastructure access platform. Administrators use the self-service portal to provision access for users by setting policies or approving requests. When a user requests access, the workflow engine generates an on-demand, short-term token, granting secure access to the cloud infrastructure for a limited duration.

## PingOne Privilege agent

The PingOne Privilege agent, installed during setup, creates and stores a non-exportable private key in the device's TPM or Secure Enclave. The agent uses this key to establish a secure mutual TLS (mTLS) connection with PingOne Privilege, which verifies the identity of both the user and the device.

## Agentless CLI

For situations where the agent can't be installed, the agentless CLI provides secure access to resources like SSH, cloud CLIs, and Kubernetes. When a user authenticates with the agentless CLI, they're redirected to PingOne SSO for authentication. After successful authentication, the user can access resources based on their permissions.

---

---
title: Onboarding users
description: This topic describes how organization administrators can onboard users to the PingOne Privilege user console.
component: privilege
page_id: privilege:getting-started:onboarding-users
canonical_url: https://docs.pingidentity.com/privilege/getting-started/onboarding-users.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2026
section_ids:
  onboarding-users-agent-based: Onboarding users (agent-based)
  onboarding-users-agentless: Onboarding users (agentless)
---

# Onboarding users

How admins onboard users to PingOne Privilege depends on the [deployment model](choosing-deployment-model.html) your organization uses. The process involves sending a link to users so they can access the user console.

## Onboarding users (agent-based)

For agent-based deployment models, users must first install the PingOne Privilege agent. You can onboard users by sending them the agent download link:

1. In the PingOne Privilege admin console, open the navigation menu in the upper-right corner. Select **Settings**.

2. Click the **App Downloads** tab.

   ![A screenshot showing the App Downloads tab with the Desktop Applications section visible.](_images/p1p_authenticator_app_install.png)

3. On the **Privilege App** tile, select the appropriate operating system for the user.

4. Copy the download link and send it to the user.

## Onboarding users (agentless)

For agentless deployment models, users must first install the Agentless CLI. You can onboard users by sending them the agentless CLI download link:

1. In the PingOne Privilege admin console, open the navigation menu in the upper-right corner. Select **Settings**.

2. Click the **App Downloads** tab.

   ![A screenshot showing the App Downloads tab with the Agentless CLI section visible.](_images/p1p_agentless_cli_install.png)

3. On the **Agentless CLI** tile, select the appropriate operating system for the user.

4. Copy the download link and send it to the user.

---

---
title: Setting up your environment in PingOne
description: This topic guides administrators through the process of setting up a new environment for PingOne Privilege.
component: privilege
page_id: privilege:getting-started:setting-up-environment
canonical_url: https://docs.pingidentity.com/privilege/getting-started/setting-up-environment.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 8, 2026
section_ids:
  before-you-begin: Before you begin
  step-1-add-the-pingone-privilege-service: "Step 1: Add the PingOne Privilege service"
  step-2-create-and-configure-an-administrator-group: "Step 2: Create and configure an administrator group"
  step-3-assign-roles-and-add-users-to-the-administrator-group: "Step 3: Assign roles and add users to the administrator group"
---

# Setting up your environment in PingOne

This topic guides administrators through setting up a new environment for PingOne Privilege, which is the first step to enabling secure, centralized privileged access management (PAM) for your organization.

|   |                                                                                                                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingOne Privilege is currently part of a controlled release. The application and required roles are feature-flagged for new tenants. If you don't see the PingOne Privilege application or the required roles in your tenant, contact Ping Identity support to have them enabled. |

## Before you begin

* You must have access to the PingOne admin console.

* Your account must have the following administrator roles assigned for the initial setup: **Identity Data Admin**, **PingOne Privilege Administrator**, and **Application Owner**.

* You need a PingOne environment and a solution built with PingOne SSO and PingID. Learn more in [Building solutions](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_building_solutions.html) in the PingOne documentation.

## Step 1: Add the PingOne Privilege service

First, add the PingOne Privilege service to your PingOne environment. Learn more in [Adding a service to an environment](https://docs.pingidentity.com/pingone/settings/p1_add_a_service.html) in the PingOne documentation.

1. In the PingOne admin console, go to **Overview**.

2. In the **Services** section, click the **[icon: plus, set=fa]**icon.

3. In the **Add a Service** list, select **PingOne Privilege**.

   ![A screenshot showing the Add a Service list with p1privilege selected.](_images/p1p_add_privilege.png)

4. Select the **Authentication Mode**.

   |   |                                                                                                                                                                                                                                                                                                                                 |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The authentication mode determines how you deploy PingOne Privilege and how users authenticate.- For agentless deployments, users authenticate via PingOne SSO.

   - For agent-based deployments, users authenticate via the PingOne Privilege agent.Learn more in [Choosing a deployment model](choosing-deployment-model.html). |

5. Click **Finish**.

## Step 2: Create and configure an administrator group

Next, create a group for your PingOne Privilege administrators and grant it access to the application. Learn more in [Managing groups](https://docs.pingidentity.com/pingone/directory/p1_managing_groups.html) in the PingOne documentation.

1. In the PingOne admin console, go to **Directory > Groups**.

2. Click the **[icon: plus, set=fa]**icon and create a new group for PingOne Privilege administrators, for example, `Privilege Admins`.

3. Go to **Applications > Applications** and click the **PingOne Privilege** application.

4. In the **Access** tab, click the **Pencil** icon.

5. In the **Edit Access** window, add the administrator group you just created. Click **Save**.

## Step 3: Assign roles and add users to the administrator group

Finally, add users to the administrator group and assign them the necessary roles. Learn more in [Managing administrator roles](https://docs.pingidentity.com//pingone/getting_started_with_pingone/p1_manage_admin_roles.html) in the PingOne documentation.

1. In the PingOne admin console, go to **Directory > Users**.

2. Select a user to be a PingOne Privilege administrator.

3. In the user's profile, go to the **Groups** tab and add the user to the PingOne Privilege administrator group you created.

4. Go to the **Roles** tab and assign the following roles to the user:

   |   |                                                                                                                                                                                                                                                                                                                                                                    |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | The following roles are required for the initial setup of PingOne Privilege:- **PingOne Privilege Administrator**: Required to create onboarding links and manage PingOne Privilege resources.

   - **Identity Data Administrator**: Required to manage users and groups in the directory.

   - **Application Owner**: Required to grant application access to groups. |

5. Click **Save**.

6. Repeat these steps for each user who will be a PingOne Privilege administrator.

---

---
title: Start here
description: This guide provides the steps for administrators to set up and configure PingOne Privilege.
component: privilege
page_id: privilege:getting-started:getting-started-admins
canonical_url: https://docs.pingidentity.com/privilege/getting-started/getting-started-admins.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 8, 2026
keywords: ["Getting started"]
---

# Start here

This guide provides the steps for administrators to set up and configure PingOne Privilege.

[icon: user-key, set=far, size=3x]

#### [Task 1: Choose a deployment model](choosing-deployment-model.html)

Decide how to deploy PingOne Privilege for your organization.

[icon: desktop, set=far, size=3x]

#### [Task 2: Set up your environment](setting-up-environment.html)

Set up the PingOne Privilege application in PingOne.

[icon: arrow-right-to-bracket, set=far, size=3x]

#### [Task 3: Access the admin console](accessing-admin-console.html)

Access the admin console to manage your PingOne Privilege tenant.

[icon: users, set=far, size=3x]

#### [Task 4: Onboard users](onboarding-users.html)

Add users to your PingOne Privilege environment.

---

---
title: What is PingOne Privilege?
description: PingOne Privilege is a cloud-based PAM solution that provides secure access for developers and DevOps teams to cloud infrastructure and applications.
component: privilege
page_id: privilege:getting-started:introduction
canonical_url: https://docs.pingidentity.com/privilege/getting-started/introduction.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2026
---

# What is PingOne Privilege?

PingOne Privilege is a cloud-based privileged access management (PAM) solution that provides secure, frictionless access for developers and DevOps teams to cloud infrastructure and applications. PingOne Privilege improves security by leveraging just-in-time (JIT) access to replace long-standing credentials and secrets with dynamic, targeted permissions that are revoked when they expire.

![Overview of how the product works showing different users accessing cloud resources through the product](_images/p1p_intro_overview.png)

Key features include:

* Passwordless access

  Using Trusted Platform Module (TPM) technology, PingOne Privilege eliminates passwords and shared credentials by storing cryptographic keys in a user's device, ensuring only authorized users can authenticate and access resources.

* Self-service portal

  Developers can request access to specific resources and permissions through a streamlined self-service portal, simplifying and speeding up access management.

* Multi-cloud identity governance

  PingOne Privilege automates risk analysis and manages dynamic permissions across multi-cloud environments.

* Real-time monitoring and control

  Admins gain real-time visibility into who is accessing resources, as well as their device, their location, and the duration of their session. Admins can also instantly terminate suspicious sessions.

* Universal service

  PingOne Privilege integrates with the PingOne cloud platform and PingOne Advanced Identity Cloud, providing unified access management and identity governance. Organizations leveraging the PingOne ecosystem benefit from consistent security policies, centralized administration, and a streamlined user experience.