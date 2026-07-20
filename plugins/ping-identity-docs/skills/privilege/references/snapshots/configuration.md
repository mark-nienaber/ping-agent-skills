---
title: Access protocols
description: PingOne Privilege supports certificate-based SSH and Remote Desktop Protocol for secure access to your resources.
component: privilege
page_id: privilege:configuration:access-protocols
canonical_url: https://docs.pingidentity.com/privilege/configuration/access-protocols.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 4, 2026
---

# Access protocols

PingOne Privilege provides secure access to your resources using industry-standard protocols. As an administrator, you can configure how these protocols are used within your environment.

The following access protocols are supported:

* [Certificate-based SSH](access-protocols/ssh.html)

  Configure how PingOne Privilege uses short-lived SSH certificates to provide secure, passwordless access to your Linux servers.

* [Remote Desktop Protocol (RDP)](access-protocols/rdp.html)

  Set up secure access to your Windows servers using RDP, with sessions managed and audited through PingOne Privilege.

---

---
title: Agent commit tracking
description: A Git Server is a system used to host and manage Git repositories, allowing teams to collaborate on code and track changes effectively.
component: privilege
page_id: privilege:configuration:git-server
canonical_url: https://docs.pingidentity.com/privilege/configuration/git-server.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 28, 2026
section_ids:
  goals: Goals
  what-youll-do: What you'll do
  preparation: Preparation
  preparation-task-1-environment-and-access: "Preparation task 1: Environment and access"
  preparation-task-2-git-providers: "Preparation task 2: Git providers"
  configure-git-integration-for-ai-agent-commit-tracking: Configure Git integration for AI agent commit tracking
  create-git-server-application: "Step 1: Create a Git Server application in PingOne Privilege"
  trust-privilege-ssh-ca: "Step 2: Trust PingOne Privilege SSH CA in GitHub"
  step-3-trust-pingone-privilege-ssh-ca-in-gitlab-saas: "Step 3: Trust PingOne Privilege SSH CA in GitLab SaaS"
  configure-git-policies: "Step 4: Configure Git policies for users and AI agents"
  validation: Validation
---

# Agent commit tracking

A Git Server is a system used to host and manage Git repositories, allowing teams to collaborate on code and track changes effectively.

To protect sensitive Git servers, you need just-in-time, least-privilege access with full session visibility and control in front of Git servers. PingOne Privilege acts as an in-line security gateway to meet this need.

You can use PingOne Privilege to:

* Enforce time-bound privileged access to Git.

* Insert the credentials that Git servers need.

* Audit and review Git activity.

* Apply fine-grained access control at the level of individual tools, prompts, and resources.

## Goals

When you complete this tutorial, you'll know:

* How to use PingOne Privilege to front Git servers for AI-driven access.

* How to configure Git integration so AI agents use SSH certificate authority (CA) authentication and their commits are attributable.

* How to use **Session Logs** and **Activity Logs** to audit Git access.

## What you'll do

1. Prepare Git integration for AI agent commit tracking:

   * [Create a Git Server application in PingOne Privilege.](#create-git-server-application)

   * [Trust PingOne Privilege's SSH CA in GitHub or GitLab.](#trust-privilege-ssh-ca)

   * [Configure policies that map users to Git identities and optionally block AI-initiated pushes.](#configure-git-policies)

## Preparation

Before getting started, complete the preparation tasks in this section.

### Preparation task 1: Environment and access

Ensure that:

1. You have a PingOne tenant with the PingOne Privilege service added.

2. You can [access the PingOne Privilege admin console as an administrator](../getting-started/accessing-admin-console.html).

### Preparation task 2: Git providers

For Git integration, you'll need one of the following:

* A GitHub Enterprise organization where you are an organization admin, so you can:

  * Manage SSH certificate authorities under **Settings > Authentication Security > SSH and GPG keys > SSH certificate authorities**.

* A GitLab SaaS group where you can:

  * Generate a **Personal Access Token (PAT)** with the `api` scope.

  * Call the **Group SSH certificates** REST API:

    ```shell
    curl --header "PRIVATE-TOKEN: <YOUR_PRIVATE_TOKEN>"
    --url "https://gitlab.com/api/v4/groups/<YOUR_GROUP_PATH>/ssh_certificates?title=Procyon-CA&key=<YOUR_PROCYON_SSH_CA_KEY>"
    ```

You'll use these permissions to trust the PingOne Privilege SSH CA in your Git providers so that SSH certificates minted by PingOne Privilege for AI agents are accepted.

## Configure Git integration for AI agent commit tracking

This task configures GitHub or GitLab to trust PingOne Privilege's SSH CA and sets up a Git Server application in PingOne Privilege.

### Step 1: Create a Git Server application in PingOne Privilege

1. In the PingOne Privilege admin console, go to **AI Security > Agentic Apps**.

2. Click **Add Application**.

3. Select **Git Server** as the application type.

4. Configure the application:

   * **Name**: Choose a recognizable internal name.

   * **Type**: Choose GitHub or GitLab.

   * Leave advanced options at default values unless you have specific internal requirements.

5. Save the application.

This application represents Git access mediated by PingOne Privilege, using SSH CA authentication instead of user-managed private-keys.

### Step 2: Trust PingOne Privilege SSH CA in GitHub

1. In the PingOne Privilege admin console, go to **AI Security > Agentic Apps**.

2. In the **Git Server** app you created, copy the public key.

3. In GitHub Enterprise:

   1. Go to **Settings > SSH and GPG keys**.

   2. Click **New SSH Key**.

   3. Enter a **Title** for the SSH key.

   4. Paste the public key into the **Key** field.

   5. Click **Add SSH key**.

GitHub now treats certificates issued by PingOne Privilege as trusted for SSH operations.

### Step 3: Trust PingOne Privilege SSH CA in GitLab SaaS

1. In the PingOne Privilege admin console, go to **AI Security > Agentic Apps**.

2. In the **Git Server** app you created, copy the public key.

3. In GitLab SaaS, create a **Personal Access Token (PAT)** with `api` scope.

4. Use the GitLab Group API to register the CA:

   ```shell
   curl --request POST \
       --header "PRIVATE-TOKEN: <YOUR_PRIVATE_TOKEN" \
       --url "https://gitlab.com/api/v4/groups/<YOUR_GROUP_PATH>/ssh_certificates?title=Procyon-CA&key=<YOUR_PRIVILEGE_SSH_CA_KEY>"
   ```

   |   |                                                                                                                                               |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Replace `<YOUR_GROUP_PATH>` with your group path and `<YOUR_PRIVILEGE_SSH_CA_KEY>` with the SSH public key you copied from PingOne Privilege. |

### Step 4: Configure Git policies for users and AI agents

1. In the PingOne Privilege admin console, go to **AI Security > Agentic Apps**.

2. In the **Active Applications** tab, click **More Info** in your **Git Server** application.

3. Create or edit a policy and configure:

   * **User mapping:**

     * For each user, specify their GitHub or GitLab username.

     * The username must match exactly what is configured in the Git provider.

   * **Time-bound access**:

     * Configure how long an approval or session remains valid.

   * Optional: **AI push blocking**

     * If required by your security model, enable the option to block code pushes for AI agents.

4. Save the policy.

Git access through this application now satisfies PingOne Privilege policy decisions.

## Validation

To confirm the integration:

1. In the PingOne Privilege agent on the local machine that's connected to PingOne Privilege, open the **Agent Resources** tab.

2. Copy the generated **git clone** command for GitHub or GitLab.

3. Adjust the command to reference the target organization or group and repository.

4. Paste and run the command in an AI agent terminal.

5. Verify that:

   * The clone succeeds when a matching policy exists.

   * If no policy exists, the request is denied and logged, prompting policy creation.

6. Perform a small test change and push from the AI agent terminal.

7. In your Git provider's commit user interface, verify that:

   * The commit is associated with the correct user.

   * The commit can be identified as coming from the AI agent flow based on your configured conventions.

8. In the PingOne Privilege admin console:

   1. Go to **Activity > Activity Logs**.

   2. Filter by **User** and **Event Time** to see individual Git operations.

---

---
title: Configuring a private gateway
description: Add a private gateway to an on-premises or non-AWS cloud network to enable secure access to resources within that network.
component: privilege
page_id: privilege:configuration:network-infrastructure/configuring-private-gateways
canonical_url: https://docs.pingidentity.com/privilege/configuration/network-infrastructure/configuring-private-gateways.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 4, 2026
section_ids:
  prerequisites: Prerequisites
  procedure: Procedure
  validation: Validation
---

# Configuring a private gateway

This guide explains how to add a private gateway to an on-premises or non-AWS cloud network. Private gateways act as a secure entry point, allowing PingOne Privilege to manage and audit access to your internal resources.

## Prerequisites

Before you begin, ensure the following inbound ports are open on the host where you will install the gateway: `22`, `443`, `3389`, `8640`, and `8690`.

## Procedure

To add a private gateway:

1. In the PingOne Privilege admin console, go to **Cloud > Gateways**.

2. Click **Add New**, and then click **Add via Docker**.

3. Select **Private Proxy**.

4. Enter a unique **Cluster ID** to identify this gateway group, and provide the **Host IP** of the server where the gateway will be installed.

5. Click **Get Docker Command** and copy the generated command.

6. On your designated host within your on-premises network, run the Docker command you just copied.

The gateway will start and automatically register with the PingOne Privilege controller.

|   |                                                                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The PingOne Privilege controller does not have automatic visibility into on-premises network topology. After deploying the gateway, you must manually configure which resources are accessible through it. |

## Validation

After adding the gateway, go to the **Cloud > Gateways** page in the admin console. Your new private gateway should be listed with a "Verified" status.

---

---
title: Configuring an AWS gateway
description: Add an AWS gateway using either the admin console wizard or a Docker command.
component: privilege
page_id: privilege:configuration:network-infrastructure/configuring-aws-gateways
canonical_url: https://docs.pingidentity.com/privilege/configuration/network-infrastructure/configuring-aws-gateways.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 4, 2026
section_ids:
  method-1-adding-a-gateway-using-the-wizard: "Method 1: Adding a Gateway Using the Wizard"
  method-2-adding-a-gateway-using-docker: "Method 2: Adding a Gateway Using Docker"
  validation: Validation
---

# Configuring an AWS gateway

You can add an AWS gateway in PingOne Privilege using one of two methods. After a gateway is added, the PingOne Privilege controller automatically discovers which cloud resources can be reached through it.

|   |                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------ |
|   | Before you can configure an AWS gateway, you must first [onboard an AWS EKS account](../configuring-kubernetes-access/aws-eks.html). |

## Method 1: Adding a Gateway Using the Wizard

The wizard provides a guided, step-by-step experience for adding an AWS gateway. This is the recommended method for most users.

1. In the PingOne Privilege admin console, go to **Cloud > Gateways**.

2. Click **Add New**, and then click **Add via Wizard**.

3. Follow the on-screen instructions to configure the gateway details.

4. Click **Finish** to complete the setup.

## Method 2: Adding a Gateway Using Docker

This method involves generating a Docker command from the PingOne Privilege admin console and running it in your AWS environment. This is suitable for automated or scripted deployments.

1. In the PingOne Privilege admin console, go to **Cloud > Gateways**.

2. Click **Add New**, and then click **Add via Docker**.

3. Select the gateway type:

   * **Private Proxy**: For networks that allow inbound connections.

   * **Relay**: For networks that only allow outbound connections.

4. Enter the **Cluster ID** for your EKS cluster.

5. Depending on the gateway type, provide the following:

   * For a **Private Proxy**, enter the **Host IP**.

   * For a **Relay**, enter the **Host Name**.

6. Click **Get Docker Command** to generate the command.

7. Copy the generated command and run it in your EKS environment to start the gateway container.

## Validation

After adding the gateway, go to the **Cloud > Gateways** page. Your new AWS gateway should be listed with a **Verified** status.

---

---
title: Configuring AWS Elastic Kubernetes Service (Amazon EKS) access
description: The steps to configure your Amazon EKS clusters to allow access management through the PingOne Privilege platform.
component: privilege
page_id: privilege:configuration:configuring-kubernetes-access/aws-eks
canonical_url: https://docs.pingidentity.com/privilege/configuration/configuring-kubernetes-access/aws-eks.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 4, 2026
section_ids:
  onboard-the-cluster-in-pingone-privilege: Onboard the cluster in PingOne Privilege
  additional-considerations: Additional considerations
  private-clusters: Private clusters
  default-permissions: Default permissions
---

# Configuring AWS Elastic Kubernetes Service (Amazon EKS) access

After you onboard an AWS account to PingOne Privilege, you can manage access to your EKS clusters and namespaces at a granular level.

|   |                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If an EKS cluster is configured to use the EKS API for authentication in combination with the `aws-auth` ConfigMap, PingOne Privilege automatically falls back to using the EKS API. |

## Onboard the cluster in PingOne Privilege

1. In the PingOne Privilege admin console, on your AWS account's **Resource** tab, click **Rescan**.

2. After the rescan completes, go to **Targets**.

3. Find the newly discovered cluster, click **More Info**, and enable the **Manage** toggle to onboard it. For more details, see [Onboarding target resources](../../privileged-access-management/admin-tasks/cloud-accounts.html#onboarding-target-resources).

## Additional considerations

### Private clusters

If your EKS cluster is in a private VPC with no inbound internet access, you must deploy a PingOne Privilege gateway or relay within the same VPC. Learn more in [Configure network infrastructure](../network-infrastructure.html).

### Default permissions

By default, an administrative user is granted the `ProcyonKubeCtlView` permission. After connecting to PingOne Privilege using the agent, the user's Kubernetes context will be automatically available in their local `~/.kube/config` file.

---

---
title: Configuring Azure AKS access
description: The required configurations within the Azure portal to allow PingOne Privilege to discover and manage your Azure Kubernetes Service (AKS) clusters.
component: privilege
page_id: privilege:configuration:configuring-kubernetes-access/azure-aks
canonical_url: https://docs.pingidentity.com/privilege/configuration/configuring-kubernetes-access/azure-aks.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 4, 2026
section_ids:
  step-1-configure-authentication-on-the-aks-cluster: "Step 1: Configure authentication on the AKS Cluster"
  step-2-assign-iam-roles-to-the-connector-app: "Step 2: Assign IAM roles to the connector app"
  step-3-onboard-the-cluster-in-pingone-privilege: "Step 3: Onboard the cluster in PingOne Privilege"
  validation: Validation
---

# Configuring Azure AKS access

This topic describes the required configurations within the Azure portal to allow PingOne Privilege to discover and manage your Azure Kubernetes Service (AKS) clusters. The process involves configuring the cluster's authentication method and assigning the necessary roles to the PingOne Privilege connector application.

## Step 1: Configure authentication on the AKS Cluster

First, configure your AKS cluster to use Microsoft Entra ID for authentication while still allowing local accounts.

1. In the Azure portal, navigate to your Kubernetes services.

2. Select your target AKS cluster to open its management blade.

3. In the sidebar under **Settings**, select **Security configuration**.

4. In **Authentication and authorization**, select **Microsoft Entra ID authentication with Azure RBAC**.

5. Ensure the **Kubernetes local accounts** checkbox is also enabled.

   This allows PingOne Privilege to manage access.

6. Click **Apply** to save the changes.

## Step 2: Assign IAM roles to the connector app

Next, grant the PingOne Privilege connector application the required permissions to manage the cluster.

|   |                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------ |
|   | These steps might not be necessary if the connector app already inherits the required roles from its subscription-level permissions. |

1. From the AKS cluster's management blade, go to **Access control (IAM)**.

2. Click **Add > Add role assignment**.

3. On the **Role** tab, search for and select the role.

4. On the **Members** tab, click **Select members**, search for your **PingOne Privilege Connector App**, and select it.

5. Click **Review + assign** to complete the assignment.

6. Repeat this process to assign the following two roles:

   * **Azure Kubernetes Service Cluster Admin Role**

   * **Azure Kubernetes Service RBAC Cluster Admin**

## Step 3: Onboard the cluster in PingOne Privilege

After completing the configuration in the Azure portal, rescan your Azure account in PingOne Privilege to discover the cluster.

1. In the PingOne Privilege admin console, go to **Cloud > Clouds**.

2. Find your Azure account and click **More Info**.

3. Go to the **Resources** tab and click **Rescan**.

## Validation

After the rescan is complete, the AKS cluster will be available to manage.

1. In the PingOne Privilege admin console, go to **Access Management > Targets**.

2. Find the newly discovered cluster, click **More Info**, and enable the **Manage** toggle to onboard it.

The AKS cluster is now managed by PingOne Privilege.

---

---
title: Configuring certificate-based SSH
description: Configure your managed servers to accept SSH connections that are authenticated by short-lived certificates issued by PingOne Privilege.
component: privilege
page_id: privilege:configuration:access-protocols/ssh
canonical_url: https://docs.pingidentity.com/privilege/configuration/access-protocols/ssh.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 4, 2026
section_ids:
  step-1-retrieve-the-pingone-privilege-ssh-ca-public-key: "Step 1: Retrieve the PingOne Privilege SSH CA Public Key"
  method-a-using-the-admin-console: "Method A: Using the Admin Console"
  method-b-using-the-api: "Method B: Using the API"
  step-2-configure-the-target-server: "Step 2: Configure the Target Server"
---

# Configuring certificate-based SSH

To enable passwordless access, you can configure your managed servers to trust SSH connections that are authenticated by short-lived certificates issued by PingOne Privilege. This process must be completed on each target server that you want to access via SSH.

|   |                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------- |
|   | Automation tools such as Ansible, Terraform, or custom scripting can help you apply these changes consistently across all your servers. |

## Step 1: Retrieve the PingOne Privilege SSH CA Public Key

First, you need to get the SSH Certificate Authority (CA) public key for your tenant. You can do this through the admin console or via an API call.

### Method A: Using the Admin Console

1. In the PingOne Privilege admin console, go to **Accounts**.

2. Select the appropriate account and click **View Public Key**.

3. Copy the public key content.

### Method B: Using the API

You can use a `curl` command to fetch the key from the API endpoint. This method is ideal for automation.

* For standard environments:

  ```bash
  $ curl https://console.tun.procyon.ai/api/{tenant}/v1/sshca
  ```

* If **VPN interop mode** is enabled:

  ```bash
  $ curl https://local.procyon.ai:8643/api/{tenant}/v1/sshca
  ```

|   |                                                             |
| - | ----------------------------------------------------------- |
|   | Replace `{tenant}` with your actual tenant name in the URL. |

## Step 2: Configure the Target Server

Next, apply the configuration to each target server.

1. Connect to the server using a standard SSH client.

2. Create a file to store the public key, for example `/etc/ssh/ca.pub`), and paste the CA public key you retrieved in the previous step into it.

3. Open the SSH daemon's configuration file for editing. On most Linux distributions, this file is located at `/etc/ssh/sshd_config`\`.

   ```bash
   $ sudo vi /etc/ssh/sshd_config
   ```

4. Add the `TrustedUserCAKeys` directive to the file, pointing to the CA public key file you just created.

   ```text
   # Add this line to sshd_config
   TrustedUserCAKeys /etc/ssh/ca.pub
   ```

   |   |                                                                                                   |
   | - | ------------------------------------------------------------------------------------------------- |
   |   | Ensure the path in this directive exactly matches the location where you saved the `ca.pub` file. |

5. Save your changes to the `sshd_config` file.

6. Restart the SSH daemon to apply the new configuration. The command can vary depending on your operating system.

   For systems using `systemd`:

   ```bash
   $ sudo systemctl restart sshd
   ```

   For older systems, you might use:

   ```bash
   $ sudo service sshd restart
   ```

Your server is now configured to trust SSH certificates from PingOne Privilege.

---

---
title: Configuring database access
description: After a database has been discovered, configure its access credentials in PingOne Privilege to enable just-in-time access for your users.
component: privilege
page_id: privilege:configuration:cloud-accounts/database-access
canonical_url: https://docs.pingidentity.com/privilege/configuration/cloud-accounts/database-access.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 4, 2026
section_ids:
  method-1-using-stored-credentials: "Method 1: Using Stored Credentials"
  method-2-using-cloud-iam: "Method 2: Using Cloud IAM"
---

# Configuring database access

After PingOne Privilege discovers a database in your cloud environment, you must configure its access credentials to enable just-in-time (JIT) access. You can configure access using either stored credentials or by leveraging cloud provider Identity and Access Management (IAM).

## Method 1: Using Stored Credentials

In this method, you store the database's username and password in PingOne Privilege. The gateway uses these credentials to connect to the database on behalf of the user.

1. In the PingOne Privilege admin console, go to the **Targets** page.

2. Locate your database in the list of discovered resources. You can filter by type to find it more easily.

3. Click the **More Info** button for the database.

4. Click the **Run Check** button. If the gateway has connectivity to the database, the cluster information will be automatically populated.

5. In the credentials section, enter the **username** and **password** required for database access.

6. Save the configuration.

## Method 2: Using Cloud IAM

Alternatively, you can connect to the database using cloud provider Identity and Access Management (IAM) permissions. This method is more secure as it does not require storing static credentials. The specific configuration steps vary depending on the cloud provider (AWS, GCP, Azure).

---

---
title: Configuring gateways
description: Gateways are entry points for accessing resources on a private network, enabling secure sessions and intelligent routing.
component: privilege
page_id: privilege:configuration:network-infrastructure/gateways
canonical_url: https://docs.pingidentity.com/privilege/configuration/network-infrastructure/gateways.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 4, 2026
---

# Configuring gateways

Gateways are fundamental components that act as entry points for accessing resources on a private network. The PingOne Privilege agent connects to a private gateway to establish a secure session. A gateway deployed in a Virtual Private Cloud (VPC), for example, can provide access to all resources within that VPC and any connected VPCs.

The PingOne Privilege controller intelligently determines the optimal gateway path to connect a user with a resource, ensuring efficient and secure access.

|   |                                                                                        |
| - | -------------------------------------------------------------------------------------- |
|   | To ensure high availability, we recommend deploying at least two gateways per network. |

PingOne Privilege supports different types of gateways depending on your environment. As an administrator, you can configure the following:

* [AWS Gateways](configuring-aws-gateways.html)

  Choose this option if you are deploying gateways within an Amazon Web Services (AWS) environment. This process is streamlined for AWS.

* [Private Gateways](configuring-private-gateways.html)

  Choose this option for non-AWS environments, such as Google Cloud Platform (GCP), Microsoft Azure, or your own on-premises data centers.

---

---
title: Configuring GCP GKE access
description: The required configurations within your GCP project to allow PingOne Privilege to discover and manage your GKE clusters.
component: privilege
page_id: privilege:configuration:configuring-kubernetes-access/gcp-gke
canonical_url: https://docs.pingidentity.com/privilege/configuration/configuring-kubernetes-access/gcp-gke.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 4, 2026
section_ids:
  step-1-verify-service-account-permissions: "Step 1: Verify service account permissions"
  step-2-onboard-the-cluster-in-pingone-privilege: "Step 2: Onboard the cluster in PingOne Privilege"
  validation: Validation
---

# Configuring GCP GKE access

This topic describes the required configurations within your Google Cloud Platform (GCP) project to allow PingOne Privilege to discover and manage your Google Kubernetes Engine (GKE) clusters. The process involves verifying service account permissions, configuring Role-Based Access Control (RBAC) on the GKE cluster, and then onboarding the cluster in PingOne Privilege.

## Step 1: Verify service account permissions

First, ensure the service account used to onboard your GCP project to PingOne Privilege has the necessary permissions to manage Kubernetes resources.

1. In the Google Cloud console, go to **IAM & Admin > IAM**.

2. Find the service account associated with your PingOne Privilege integration.

3. Verify that the service account has the **Kubernetes Engine Admin** role.

   This role allows PingOne Privilege to discover and interact with your GKE clusters. If it doesn't, edit the principal's permissions and add this role.

## Step 2: Onboard the cluster in PingOne Privilege

After completing the configuration in the GCP console, rescan your account in PingOne Privilege to discover and manage the cluster.

1. In the PingOne Privilege admin console, go to **Clouds**.

2. Find your GCP cloud account, and click **More Info**.

3. Go to the **Resources** tab and click **Rescan**.

## Validation

After the rescan is complete, the GKE cluster will be available to manage.

1. In the PingOne Privilege admin console, go to **Targets**.

2. Find the newly discovered cluster, click **More Info**, and enable the **Manage** toggle to onboard it.

The GKE cluster is now managed by PingOne Privilege.

---

---
title: Configuring Kubernetes access
description: Administrators can configure Kubernetes access for onboarded cloud accounts to enable just-in-time access for teams running containerized workloads.
component: privilege
page_id: privilege:configuration:configuring-kubernetes-access/index
canonical_url: https://docs.pingidentity.com/privilege/configuration/configuring-kubernetes-access/index.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 4, 2026
---

# Configuring Kubernetes access

Administrators can configure Kubernetes access for onboarded cloud accounts to enable just-in-time (JIT) access for teams running containerized workloads. This integration allows organizations to enforce least-privilege, time-bound access to Kubernetes resources, centralized in the PingOne Privilege platform.

PingOne Privilege supports the following Kubernetes services:

* [AWS Elastic Kubernetes Service (EKS)](aws-eks.html)

* [Azure Kubernetes Service (AKS)](azure-aks.html)

* [Google Kubernetes Engine (GKE)](gcp-gke.html)

Select the appropriate guide for your cloud provider to continue.

---

---
title: Configuring MCP gateways
description: The PingOne Privilege MCP gateway provides just-in-time access, least-privilege access, and full session visibility and control for MCP servers.
component: privilege
page_id: privilege:configuration:mcp-gateway
canonical_url: https://docs.pingidentity.com/privilege/configuration/mcp-gateway.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 28, 2026
section_ids:
  goals: Goals
  what-youll-do: What you'll do
  preparation: Preparation
  preparation-task-1-environment-and-access: "Preparation task 1: Environment and access"
  preparation-task-2-mcp-servers-and-clients: "Preparation task 2: MCP servers and clients"
  tutorial: Tutorial
  deploy-mcpgw: "Tutorial Task 1: Deploy the MCP Gateway (MCPGW)"
  step-1-add-an-mcpgw-application: "Step 1: Add an MCPGW application"
  step-2-prepare-directories-and-environment-file: "Step 2: Prepare directories and environment file"
  step-2-install-tls-certificates: "Step 2: Install TLS certificates"
  step-3-register-the-mcp-gateway-in-pingone-privilege: "Step 3: Register the MCP Gateway in PingOne Privilege"
  create-mcp-server-privilege: "Tutorial task 2: Configure MCP Server applications in PingOne Privilege"
  step-1-create-an-mcp-server-application: "Step 1: Create an MCP Server application"
  step-2-attach-the-mcpgw-to-the-mcp-server-application: "Step 2: Attach the MCPGW to the MCP Server application"
  configure-access: "Tutorial task 4: Configure policy for MCP tools, prompts, and resources"
  step-1-open-the-mcp-policy-configuration: "Step 1: Open the MCP policy configuration"
  step-2-select-allowed-tools-prompts-and-resources: "Step 2: Select allowed tools, prompts, and resources"
  step-3-bind-policies-to-identities-and-approvals: "Step 3: Bind policies to identities and approvals"
  validate: Validation
  validation-step-1-connect-an-mcp-client-through-the-frontend-url: "Validation Step 1: Connect an MCP client through the Frontend URL"
  validation-step-2-review-mcp-session-logs: "Validation step 2: Review MCP Session logs"
  validation-step-3-review-mcp-activity-logs: "Validation step 3: Review MCP Activity logs"
---

# Configuring MCP gateways

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro) is an open standard for connecting artificial intelligence (AI) agents and IDEs to backend services through tools, prompts, and resources. Exposing services over MCP makes them available to AI agents.

To protect sensitive admin APIs, you need just-in-time, least-privilege access with full session visibility and control for your MCP servers. PingOne Privilege acts as an inline MCP security gateway to meet this need.

You can use PingOne Privilege to:

* Enforce time-bound privileged access to MCP tools.

* Insert credentials that MCP servers need, without exposing them to AI agents.

* Audit and review MCP activity.

* Apply fine-grained access control to individual tools, prompts, and resources.

## Goals

When you complete this tutorial, you'll be able to:

* Use PingOne Privilege to front MCP servers for AI-driven access.

* Deploy and configure the Privilege MCP Gateway and MCP Server applications.

* Define policies that control which MCP tools, prompts, and resources are available and under what conditions.

* Use **Session Logs** and **Activity Logs** to audit MCP access.

## What you'll do

1. Prepare the MCP Gateway and MCP Server applications:

   * [Deploy the MCP Gateway with OpenID Connect (OIDC) integration to PingOne.](#deploy-mcpgw)

   * [Create an MCP Server application in PingOne Privilege that fronts a backend MCP server.](#create-mcp-server-privilege)

   * [Configure a tool, prompt, or resource-level policy for MCP access.](#configure-access)

   * [Validate that MCP traffic flows through the gateway and is logged in PingOne Privilege.](#validate)

## Preparation

Before you start, complete the preparation tasks in this section.

### Preparation task 1: Environment and access

Ensure that:

1. You have a PingOne tenant with the PingOne Privilege service added.

2. You can [access the PingOne Privilege admin console as an administrator](../getting-started/accessing-admin-console.html).

3. Your network allows:

   * Outbound access from your MCPGW host to PingOne endpoints, such as `grpc.pingone.com`.

   * Access from your MCP clients to the MCPGW ports.

     * Add port `8623` and remove RDP port `3389` in the MGCPGW VM.

### Preparation task 2: MCP servers and clients

To configure MCP support, ensure:

1. You have at least one MCP server you want to protect, such as a remote MCP server exposing tools for various internal services.

2. You have one or more MCP clients that your users will run, such as Claude Desktop, Cursor, VS Code Copilot Chat, Zed, or other MCP-compatible IDEs.

3. For the MCP Gateway, you have:

   * A virtual machine (VM) or host where you can install Docker and run the MCPGW container.

   * A DNS name for the gateway, such as `mcpgw.example.com`.

## Tutorial

After you prepare the environment, follow these tutorial tasks to configure MCP applications with PingOne Privilege.

### Tutorial Task 1: Deploy the MCP Gateway (MCPGW)

Deploy the MCP Gateway host and configure it to authenticate users through PingOne and broker access to MCP servers.

#### Step 1: Add an MCPGW application

1. In the PingOne admin console, go to **AI Security > Agentic Apps**.

2. Click **[icon: plus, set=fa]**to add a new agent.

3. Provide a **Name**, such as `MCPGW`, and click **Save**.

   The agent is added to the list of **AI Agents**.

4. Toggle on the application.

5. Click **More options ( [icon: ellipsis-v, set=fa])**.

6. In the **Configuration** tab, click the **[icon: pencil, set=fa]**icon.

7. Enter `http://<mcpgwdns>:<port>/callback` in the **Redirect URIs** field and click **Save.**

8. In the **Resources** tab, click the **[icon: pencil, set=fa]**icon and add the following scopes by selecting their checkboxes:

   * **openid**

   * **email**

   * **profile**

9. Click **Save**.

#### Step 2: Prepare directories and environment file

On your MCPGW VM:

1. Create configuration and SSL directories:

   ```shell
   sudo mkdir -p /var/lib/procyon/config
   sudo mkdir -p /var/lib/procyon/ssl
   ```

2. Create `/var/lib/procyon/config/pingone.env` and add:

   ```shell
   SERVER_URL=https://<mcpgw-dns>:<port>

   # PingOne-specific configuration
   OIDC_CLIENT_ID=<id>
   OIDC_CLIENT_SECRET=<secret>
   OIDC_AUTH_URL=https://auth.<pingurl>pingone.com/<env>/as/authorize
   OIDC_TOKEN_URL=https://auth.<pingurl>pingone.com/<env>/as/token
   OIDC_USER_URL=https://auth.<pingurl>pingone.com/<env>/as/userinfo
   OIDC_SCOPES=openid profile email
   ```

   |   |                                                                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Replace `<mcpgw-dns>` and `<port>` with the public DNS name and port of your MCPGW. Replace `<pingurl>` and `<env>` with your PingOne tenant and environment. |

#### Step 2: Install TLS certificates

1. Obtain a certificate whose CN/SAN matches `*.<mcpgw-dns>`.

2. Copy the certificate and key to:

   * `/var/lib/procyon/ssl/mcpgw-cert.pem`

   * `/var/lib/procyon/ssl/mcpgw-key.pem`

#### Step 3: Register the MCP Gateway in PingOne Privilege

1. In the PingOne Privilege admin console, go to **Cloud > Gateways**.

2. Click **Add New**, then click **Add via Wizard**.

3. Follow the wizard to:

   * Review the minimum required specifications of your machine and supported operating systems.

   * Install Docker and verify that it's running.

   * Provide a **Proxy Cluster Name** and **FQDN / Host IP**.

   * Create the environment file.

   * Install the proxy guest agent based on your operating system and architecture.

4. On the VM, run the generated Docker command to start MCPGW.

The MCP Gateway is now registered with PingOne Privilege and ready to be attached to the MCP Server applications.

### Tutorial task 2: Configure MCP Server applications in PingOne Privilege

This task creates an MCP Server application in PingOne Privilege and attaches it to the MCPGW.

#### Step 1: Create an MCP Server application

1. In the PingOne Privilege admin console, go to **AI Security > Agentic Apps**.

2. Click the **Add Application** tab.

3. In the **MCP Server** tile, click **Integrate**.

4. Configure the following fields:

   * **Application Name**: A name for the application, for example, `mcp-pingone-admin`.

   * **Frontend URL**: The URL MCP that clients will use to access the MCPGW, for example, `https://<mcpgw-dns>`.

   * **MCP Server URL**: The actual backend MCP server endpoint, including port and path, for example, `https://mcp-server-internal:8080/mcp`.

   * **Headers**: Optional custom HTTP headers to send when connecting to the MCP server.

   * **Mesh Cluster**: Leave this field empty for now. You'll set it after associating the MCPGW.

5. Click **Create**.

#### Step 2: Attach the MCPGW to the MCP Server application

1. In the PingOne Privilege admin console, go to **AI Security > Agentic Apps**.

2. Select the **MCP Server** application in the **Active Applications** tab.

3. In the **Mesh Cluster** field, select the one you created in step 1.

4. Save the configuration.

MCP clients that connect through the **Frontend URL** are now routed through the MCPGW, which authenticates users through PingOne and enforces PingOne Privilege policies.

### Tutorial task 4: Configure policy for MCP tools, prompts, and resources

This task configures fine-grained access control for the MCP Server application.

#### Step 1: Open the MCP policy configuration

1. In the PingOne Privilege admin console, go to **AI Security > Agentic Apps**.

2. Select the **MCP Server** application.

3. Go to the **Access Control / Policy** configuration for that application.

The UI provides controls to select specific tools, prompts, and resources from the MCP server's capabilities.

#### Step 2: Select allowed tools, prompts, and resources

1. In the PingOne Privilege admin console, go to **AI Security > Agentic Apps**.

2. Select the **MCP Server** application.

3. Go to the **Access Control / Policy** configuration for that application.

4. Use the **Tool selector** to choose which tools should be available.

   |   |                                                                                |
   | - | ------------------------------------------------------------------------------ |
   |   | Use the search with available RegEx support to quickly select groups or tools. |

5. (Optional) Enable particular prompts for guided flows.

6. (Optional) Restrict resources by pattern, for example, by index names or environment tags.

#### Step 3: Bind policies to identities and approvals

1. Configure which users or groups from PingOne can access the MCP Server application, and specific tools, prompts, and resources.

2. Define approval requirements, such as:

   * Just-in-time approvals for high-risk tools.

   * Multi-level approvals for production-critical actions.

3. Configure time-bound access:

   * How long after approval the user can call the selected tools.

   * When access must be requested again.

4. Save the policy.

MCP access now follows the standard PingOne Privilege approval request flow for that application. Additionally, only permitted tools are visible and callable from MCP clients.

## Validation

This task verifies that MCP clients are using the MCPGW and that traffic is audited.

### Validation Step 1: Connect an MCP client through the Frontend URL

1. In a supported MCP client (such as Claude Desktop, Cursor, or a command-line interface (CLI)-based MCP inspector), configure an MCP server entry that points to the MCP Server application's **Frontend URL**.

2. Initiate a connection or call a tool.

3. On first use in a session, the user is redirected through an OAuth 2.1 or OIDC flow with PingOne or another flow depending on your setup.

4. After authentication and policy checks:

   * Only authorized tools appear in the MCP client.

   * Tool invocations are routed through the MCPGW to the backend MCP server.

### Validation step 2: Review MCP Session logs

1. In the PingOne Privilege admin console, go to **Activity > Session Logs**.

2. Verify that:

   * Sessions list the user, device, service, and a resource type of MCP.

   * You can mark sessions as audited after review.

### Validation step 3: Review MCP Activity logs

1. In the PingOne Privilege admin console, go to **Activity > Activity Logs**.

2. Filter by:

   * The MCP Server application.

   * The user who ran the test.

3. Inspect individual events:

   * Confirm that you see the tool name, any arguments, and progress tokens.

   * Use the **Event Information** and **Resources** views to see more context about what was accessed.

4. Confirm that logs match the behavior you saw in the MCP client.

---

---
title: Configuring network infrastructure
description: To provide access to servers and databases in your cloud environment, you might need to configure network infrastructure.
component: privilege
page_id: privilege:configuration:network-infrastructure
canonical_url: https://docs.pingidentity.com/privilege/configuration/network-infrastructure.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 4, 2026
---

# Configuring network infrastructure

To provide secure access to servers and databases in your cloud environment, you might need to configure a combination of the following components:

* [Gateways](network-infrastructure/gateways.html)

  Gateways are the primary entry points for accessing resources on a private network. They act as a secure proxy, allowing PingOne Privilege to manage and audit access to your internal systems.

* [Private Relays](network-infrastructure/private-relays.html)

  Private relays are used in networks that do not allow inbound connections. They establish an outbound connection to a gateway, creating a secure tunnel for traffic without requiring you to open firewall ports.

Together, these components create a flexible and secure network infrastructure that allows PingOne Privilege to manage access to any resource, regardless of its location or network configuration.

---

---
title: Configuring PingOne Privilege
description: "Learn how to set up and customize the PingOne Privilege platform to suit your organization's requirements."
component: privilege
page_id: privilege:configuration:index
canonical_url: https://docs.pingidentity.com/privilege/configuration/index.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 4, 2026
---

# Configuring PingOne Privilege

This section provides guidance for administrators on configuring the PingOne Privilege platform.

Learn how to configure the following:

* Onboarding cloud accounts for just-in-time (JIT) access to resources:

  * [AWS](cloud-accounts/aws.html)

  * [Azure](cloud-accounts/azure.html)

  * [GCP](cloud-accounts/gcp.html)

* Configuring Kubernetes access for your onboarded cloud accounts:

  * [AWS EKS](configuring-kubernetes-access/aws-eks.html)

  * [Azure AKS](configuring-kubernetes-access/azure-aks.html)

  * [GCP GKE](configuring-kubernetes-access/gcp-gke.html)

* Configuring network infrastructure for access to servers and databases:

  * [Gateways](network-infrastructure/gateways.html)

  * [Private relays](network-infrastructure/private-relays.html)

* Configuring access protocols for secure connections:

  * [SSH](access-protocols/ssh.html)

  * [RDP](access-protocols/rdp.html)

---

---
title: Configuring private relays
description: "A private relay is designed for deployment in networks that don't allow inbound connections, enabling access to resources within that private network."
component: privilege
page_id: privilege:configuration:network-infrastructure/private-relays
canonical_url: https://docs.pingidentity.com/privilege/configuration/network-infrastructure/private-relays.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 4, 2026
section_ids:
  validation: Validation
---

# Configuring private relays

A private relay is a component designed for deployment in networks that don't allow inbound connections from the internet. The relay, deployed as a Docker container, establishes a secure, egress-only connection to a PingOne Privilege gateway, enabling access to resources located within its private network.

To add a private relay:

1. In the PingOne Privilege admin console, go to **Cloud > Gateways**.

2. Click **Add New**, and then select the **Docker** icon.

3. Select **Relay**.

4. Enter a unique **Cluster ID** to identify this relay group, and provide the **Hostname** of the server where the relay will be installed.

5. Click **Get Docker Command** and copy the generated command.

6. On a server within your private network, run the Docker command you just copied.

## Validation

After you deploy the private relay, it registers with the PingOne Privilege controller and connects to an available gateway. PingOne Privilege will then automatically discover the cloud resources that are reachable through that relay. You can view the status of the relay on the **Cloud > Gateways** page.

---

---
title: Configuring remote desktop access
description: When you onboard a cloud account, PingOne Privilege automatically discovers all remote desktop protocol (RDP) instances.
component: privilege
page_id: privilege:configuration:access-protocols/rdp
canonical_url: https://docs.pingidentity.com/privilege/configuration/access-protocols/rdp.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 4, 2026
section_ids:
  step-1-create-a-domain-controller-configuration: "Step 1: Create a Domain Controller Configuration"
  method-a-for-non-domain-joined-machines: "Method A: For Non-Domain-Joined Machines"
  method-b-for-domain-joined-machines: "Method B: For Domain-Joined Machines"
  step-2-bind-the-rdp-instance-to-the-configuration: "Step 2: Bind the RDP Instance to the Configuration"
---

# Configuring remote desktop access

When you onboard a cloud account, PingOne Privilege automatically discovers all Remote Desktop Protocol (RDP) instances, which are then listed as targets. To enable passwordless access to these targets, you must configure an access method based on whether the target machine is joined to an Active Directory (AD) domain.

First, you will create a Domain Controller configuration, which acts as a template for RDP connections. Then, you will bind individual RDP targets to this configuration.

## Step 1: Create a Domain Controller Configuration

Choose one of the following methods depending on your target environment.

### Method A: For Non-Domain-Joined Machines

For standalone Windows servers, use the Local User mode to store and manage a local administrator account.

1. In the PingOne Privilege admin console, go to **Connections > RDP User Management**.

2. Click **Create**.

3. Enter a **Name** for this configuration, such as `Standalone Web Servers`.

4. Enable the **Local User Mode** toggle.

5. In the **Username** and **Password** fields, enter the credentials for a local administrator account on the target machine. These credentials will be stored securely in the PingOne Privilege vault.

6. Click **Create**.

### Method B: For Domain-Joined Machines

For Windows servers joined to an Active Directory domain, create a configuration that stores domain credentials.

1. In the PingOne Privilege admin console, go to **Connections > RDP User Management**.

2. Click **Create**.

3. Enter a **Name** for this configuration, such as `Corporate AD Domain`.

4. Ensure the **Local User Mode** toggle is disabled.

5. Enter the credentials for a privileged **Domain Admin** account.

   This service account is used by PingOne Privilege to manage other users' passwords within the domain.

6. For each standard domain user account you want to manage, click **Add User** and enter their `Username` and `Password`.

7. Select the **Cloud Type** (AWS, GCP, or Azure). This makes the domain controller configuration the default for RDP targets in that cloud provider.

8. (Optional) Enable the **Rotate Passwords** feature.

9. Click **Create**.

## Step 2: Bind the RDP Instance to the Configuration

After creating a configuration, you must bind each RDP target to it.

1. In the PingOne Privilege admin console, go to **Access Management > Targets**.

2. Find the target RDP instance and click **More Info**.

3. From the **RDP User Management** list, select the configuration you created in the previous step.

4. Enable the **Managed** toggle for the RDP instance. Click **Save**.

5. Click **Create**.

---

---
title: Onboarding Amazon Web Services (AWS) accounts
description: When you add an AWS account to PingOne Privilege, its resources are discovered automatically and can be managed for just-in-time (JIT) developer access.
component: privilege
page_id: privilege:configuration:cloud-accounts/aws
canonical_url: https://docs.pingidentity.com/privilege/configuration/cloud-accounts/aws.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 4, 2026
section_ids:
  step-1-start-the-add-account-wizard: "Step 1: Start the Add Account wizard"
  step-2-deploy-the-cloudformation-template-in-aws: "Step 2: Deploy the CloudFormation template in AWS"
  step-3-complete-the-configuration-in-pingone-privilege: "Step 3: Complete the configuration in PingOne Privilege"
  result: Result
  validation: Validation
---

# Onboarding Amazon Web Services (AWS) accounts

When you add an AWS account to PingOne Privilege, its resources are automatically discovered and can be managed for just-in-time (JIT) access. You can onboard either a single AWS account or an entire AWS Organization Unit (OU).

## Step 1: Start the Add Account wizard

1. In the PingOne Privilege admin console, go to **Cloud > Clouds**.

2. Click **Add Account Wizard**.

3. In the **Add Account** modal, ensure the AWS icon is selected.

4. Enter a **Name** and **Description** for the connection. Click **Next**.

5. When asked if you are onboarding an Organization Unit (OU), select **Yes** or **No**. Click **Next**.

## Step 2: Deploy the CloudFormation template in AWS

1. Copy the provided CloudFormation (CFN) template or click **Open CF Template** to open it in your AWS account.

2. In your AWS management account, deploy the CloudFormation template.

   |   |                                                                                                                                                                                                                                                                                                                                                                                     |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You must have sufficient IAM permissions to create the required resources. During deployment, provide the following parameters when prompted:- **ExternalID**: Enter a unique, memorable string that acts as a shared secret. You can copy this value directly from the PingOne Privilege UI.

   - **OrgID** (OU Only): Enter the ID of the AWS Organization Unit you are onboarding. |

3. After the CloudFormation stack is successfully created, go to its **Outputs** tab and copy the generated values.

## Step 3: Complete the configuration in PingOne Privilege

1. In the PingOne Privilege admin console, return to the **Add Account** wizard.

2. Enter the values you copied from the CloudFormation stack outputs:

   * **Cross Account Role ARN**: The ARN of the role created by the template.

   * **Organization Unit (OU) ID** (For OUs only): The ID of the onboarded OU.

   * **Advanced Discovery TAGS** (Optional): Limit discovery to resources with matching tags.

   * **Advanced Discovery REGION** (Optional): By default, all enabled regions are scanned. Select specific regions to limit the discovery scope.

3. Click **Verify & Add Account**.

## Result

The AWS account or OU will now appear in the Cloud Accounts list.

## Validation

To ensure the onboarding process was successful:

1. Sign in to the AWS console for the onboarded account.

2. Go to the **IAM** service.

3. Select **Identity providers**.

4. Verify that an identity provider exists with the name `Procyon-<YourTenantName>-<YourAWSAccountName>`, where `<YourTenantName>` is your PingOne Privilege tenant name and `<YourAWSAccountName>` is the name you provided in the wizard.

---

---
title: Onboarding Azure accounts
description: When an Azure subscription is added to PingOne Privilege, its resources are automatically discovered and can be managed for just-in-time developer access.
component: privilege
page_id: privilege:configuration:cloud-accounts/azure
canonical_url: https://docs.pingidentity.com/privilege/configuration/cloud-accounts/azure.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 4, 2026
section_ids:
  step-1-create-the-connector-app-in-azure: "Step 1: Create the Connector App in Azure"
  step-2-assign-required-roles: "Step 2: Assign Required Roles"
  step-3-grant-api-permissions: "Step 3: Grant API Permissions"
  step-4-add-the-azure-account-to-pingone-privilege: "Step 4: Add the Azure Account to PingOne Privilege"
  validation: Validation
---

# Onboarding Azure accounts

Onboarding an Azure subscription allows PingOne Privilege to automatically discover its resources and manage them for just-in-time access. The process involves creating a connector application in Azure, assigning it the necessary permissions, and then adding the account to PingOne Privilege.

## Step 1: Create the Connector App in Azure

First, create an Azure App Registration to act as a service principal.

1. In the Azure Portal, go to **Azure Active Directory > App Registrations** and select **New registration**.

2. Name the application (e.g., `ProcyonConnectorApp`) and click **Register**.

3. From the application's **Overview** page, copy and save the **Application (client) ID** and the **Directory (tenant) ID**. You will need these later.

4. Go to **Certificates & secrets** and select **New client secret**.

5. Provide a description, set an expiration period, and click **Add**.

6. Immediately copy and save the secret's **Value**. This is the **App Key** you will need later.

   |   |                                                                                            |
   | - | ------------------------------------------------------------------------------------------ |
   |   | The client secret value is only displayed once. If you lose it, you must create a new one. |

## Step 2: Assign Required Roles

For each Azure subscription you intend to manage, you must assign the `ProcyonConnectorApp` several roles.

1. In the Azure portal, navigate to the target **Subscription** and select **Access control (IAM)**.

2. Select **Add > Add role assignment**.

3. On the **Role** tab, find and select the role. For privileged roles, you must first select the **Privileged administrator roles** tab.

4. On the **Members** tab, click **+ Select members**, search for your `ProcyonConnectorApp`, and select it.

5. Click **Review + assign** to complete the assignment.

6. Repeat this process to assign the following roles:

   * `Reader`

   * `User Access Administrator` (Privileged role)

   * `Azure Kubernetes Service Cluster Admin Role`

   * `Azure Kubernetes Service RBAC Cluster Admin`

## Step 3: Grant API Permissions

Next, grant the `ProcyonConnectorApp` the necessary Microsoft Graph API permissions.

1. In the Azure portal, go to **Azure Active Directory > App Registrations** and select your `ProcyonConnectorApp`.

2. In the sidebar, select **API permissions**.

3. Click **+ Add a permission**, select **Microsoft Graph**, and then choose **Application permissions**.

4. Search for and add the following permissions:

   ```text
   Application.ReadWrite.OwnedBy
   Directory.Read.All
   Domain.ReadWrite.All
   IdentityProvider.ReadWrite.All
   RoleManagement.ReadWrite.Directory
   User.ReadWrite.All
   ```

5. After adding the permissions, click **Grant admin consent for \<Your Directory>**.

6. Verify that all permissions have a green checkmark in the **Status** column.

## Step 4: Add the Azure Account to PingOne Privilege

Finally, use the credentials from the `ProcyonConnectorApp` to add the account to PingOne Privilege.

1. In the PingOne Privilege admin console, go to **Cloud > Clouds**.

2. Click **Add Account Wizard** and select the **Azure** icon.

3. Enter a **Name** and **Description** for the account. Click **Next**.

4. (Optional) Adjust the SAML and guest user settings if needed. Click **Next**.

5. Enter the **Tenant ID**, **App ID**, and **App Key** that you recorded earlier. Click **Next**.

6. Verify the details and click **Verify & Add Account**.

## Validation

After adding the account, go to the **Cloud > Clouds** page in the PingOne Privilege admin console. Your new Azure account should be listed with a "Verified" status. You can click on the account to see the discovered resources.

---

---
title: Onboarding cloud accounts
description: Enable passwordless, just-in-time access to resources across various cloud infrastructures.
component: privilege
page_id: privilege:configuration:cloud-accounts
canonical_url: https://docs.pingidentity.com/privilege/configuration/cloud-accounts.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 4, 2026
section_ids:
  primary-supported-resources: Primary supported resources
  resources-available-through-cli-and-assumed-roles: Resources available through CLI and assumed roles
---

# Onboarding cloud accounts

PingOne Privilege enables passwordless, just-in-time (JIT) access to resources across the following cloud infrastructures:

* [Amazon Web Services (AWS)](cloud-accounts/aws.html)

* [Azure](cloud-accounts/azure.html)

* [Google Cloud Platform (GCP)](cloud-accounts/gcp.html)

While cloud providers offer many predefined roles, they can often be overly permissive. PingOne Privilege helps enforce least-privileged access by creating and deleting dynamic roles on-demand through automation.

## Primary supported resources

The following table summarizes the primary resources supported for each cloud provider.

| Cloud | Servers               | RDP Servers           | Databases             | Kubernetes Clusters | Cloud CLI  | Console Login         |
| ----- | --------------------- | --------------------- | --------------------- | ------------------- | ---------- | --------------------- |
| AWS   | [icon: check, set=fa] | [icon: check, set=fa] | [icon: check, set=fa] | EKS                 | AWS CLI    | [icon: check, set=fa] |
| Azure | [icon: check, set=fa] | [icon: check, set=fa] | [icon: check, set=fa] | AKS                 | Azure CLI  | [icon: check, set=fa] |
| GCP   | [icon: check, set=fa] | [icon: check, set=fa] | [icon: check, set=fa] | GKE                 | gcloud CLI | [icon: check, set=fa] |

## Resources available through CLI and assumed roles

The following resources are accessible through the command-line interface (CLI) or by using `assume-role` functionality.

| Cloud                                 | Resources                                                                                                                                                                                                                     |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![AWS logo](_images/aws-logo.png)     | * EC2 Instance

* EC2 Key Pair

* EC2 Network Interface

* EC2 EBS Volume

* EC2 Security Group

* EC2 Elastic IP

* EKS Namespace

* KMS Key

* RDS DB Instance

* S3 Bucket

* VPC                                          |
| ![Azure logo](_images/azure-logo.png) | - AKS Namespace

- Load Balancer

- Managed Cluster

- Microsoft Entra ID

- MySQL Flexible Server

- PostgreSQL Flexible Server

- Resource Group

- SQL Server

- SQL Server Database

- Subscription

- Virtual Machine    |
| ![GCP logo](_images/gcp-logo.png)     | * BigQuery Table

* Cloud Bigtable Instance

* Cloud Functions

* Compute Instance

* Folder

* GKE Namespace

* Organization

* Project

* Pub/Sub Topic

* Service Account

* SQL Instance

* Storage Bucket

* VPC Network |

---

---
title: Onboarding GCP accounts
description: Onboard a GCP organization, folder, or project to manage its resources in PingOne Privilege with Just-In-Time (JIT) access.
component: privilege
page_id: privilege:configuration:cloud-accounts/gcp
canonical_url: https://docs.pingidentity.com/privilege/configuration/cloud-accounts/gcp.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 4, 2026
section_ids:
  step-1-create-a-service-account-in-gcp: "Step 1: Create a service account in GCP"
  step-2-add-the-gcp-account-to-pingone-privilege: "Step 2: Add the GCP account to PingOne Privilege"
  validation: Validation
---

# Onboarding GCP accounts

You can onboard a Google Cloud Platform (GCP) organization, folder, or project to manage its resources in PingOne Privilege with Just-In-Time (JIT) access. The process involves creating a service account with the necessary permissions in GCP, and then adding the account to PingOne Privilege.

## Step 1: Create a service account in GCP

1. In the GCP console, create a new service account.

2. Grant the service account the required IAM permissions.

   These permissions allow PingOne Privilege to discover resources and manage access. The necessary permissions depend on whether you are onboarding an organization, folder, or project:

   | Onboarding level | Required Permissions                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Organization     | * **Browser**

   * **Cloud SQL Admin**

   * **Cloud SQL Client**

   * **Role Administrator**

   * **Security Admin**

   * **Viewer**

   * **Service Account Key Admin**

   * **Service Account Admin**

   * **Service Account Token Creator**

   * **Kubernetes Engine Admin**

   * **IAM Recommender Admin**

   * **AlloyDB Admin**

   * **BigQuery Data Owner**                                                                                                    |
   | Folder           | - **Browser**

   - **Cloud SQL Admin**

   - **Cloud SQL Client**

   - **Security Admin**

   - **Viewer**

   - **Service Account Key Admin**

   - **Service Account Admin**

   - **Service Account Token Creator**

   - **Kubernetes Engine Admin**

   - **IAM Recommender Admin**

   - **AlloyDB Admin**

   - **BigQuery Data Owner**&#xA;&#xA;For each project in the folder, include "Role Administrator" or include "owner" permission at the top folder level. |
   | Project          | * **Browser**

   * **Cloud SQL Admin**

   * **Cloud SQL Client**

   * **Role Administrator**

   * **Security Admin**

   * **Viewer**

   * **Service Account Key Admin**

   * **Service Account Admin**

   * **Service Account Token Creator**

   * **Kubernetes Engine Admin**

   * **IAM Recommender Admin**

   * **AlloyDB Admin**

   * **BigQuery Data Owner**                                                                                                    |

3. [Create a service account key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating) for the service account and download it in JSON format. You will need this file later.

4. Enable the [Cloud Resource Manager API](https://console.cloud.google.com/apis/library/cloudresourcemanager.googleapis.com) in the project that contains the service account.

## Step 2: Add the GCP account to PingOne Privilege

1. In the PingOne Privilege admin console, go to **Cloud > Clouds**.

2. Click **Add Account Wizard**.

3. Click the **GCP icon**.

4. Select whether you are onboarding an **Organization**, **Folder**, or **Project**. Click **Next**.

5. Enter the **Provider ID** (this is your Organization ID, Folder ID, or Project ID). Click **Next**.

6. Upload or paste the content of the JSON service account key file you downloaded earlier. Click **Next**.

7. Verify the account details are correct and click **Verify And Add**.

## Validation

After adding the account, go to the **Cloud > Clouds** page in the PingOne Privilege admin console. Your new GCP account should be listed with a **Verified** status. You can click on the account to see the discovered resources.