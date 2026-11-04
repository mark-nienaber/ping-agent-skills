---
title: Access protocols
description: PingOne Privilege supports certificate-based SSH and Remote Desktop Protocol for secure access to your resources.
component: privilege
page_id: privilege:human-privilege:configuration/access-protocols/index
canonical_url: https://docs.pingidentity.com/privilege/human-privilege/configuration/access-protocols/index.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 4, 2026
page_aliases: ["configuration:access-protocols.adoc"]
---

# Access protocols

PingOne Privilege provides secure access to your resources using industry-standard protocols. As an administrator, you can configure how these protocols are used within your environment.

The following access protocols are supported:

* [Certificate-based SSH](ssh.html)

  Configure how PingOne Privilege uses short-lived Secure Shell (SSH) *(tooltip: \<div class="paragraph">
  \<p>Protocol for secure operation of network services over an unsecured network.\</p>
  \</div>)* certificates to provide secure, passwordless access to your Linux servers.

* [Remote Desktop Protocol (RDP)](rdp.html)

  Set up secure access to your Windows servers using RDP, with sessions managed and audited through PingOne Privilege.

---

---
title: Accessing the user console
description: Users access the user console to manage and monitor privileged access across their organization.
component: privilege
page_id: privilege:human-privilege:getting-started-users/accessing-user-console
canonical_url: https://docs.pingidentity.com/privilege/human-privilege/getting-started-users/accessing-user-console.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2026
page_aliases: ["human-privilege:user-tasks/getting-started/accessing-user-console.adoc"]
section_ids:
  accessing-the-user-console-in-endpoint-controller-based-deployments: Accessing the user console in Endpoint Controller-based deployments
  accessing-the-user-console-in-no-endpoint-controller-based-deployments: Accessing the user console in No Endpoint Controller-based deployments
---

# Accessing the user console

Users access the user console to manage and monitor privileged access across their organization. There are two ways to get to the user console, depending on whether you're using the Endpoint Controller-based or No Endpoint Controller-based deployment method.

## Accessing the user console in Endpoint Controller-based deployments

1. Click the Endpoint Controller icon located in the system tray on Windows devices or in the menu bar on macOS devices to toggle the visibility of the PingOne Privilege App window.

2. When the PingOne Privilege app window is open, ensure that the Endpoint Controller is in a connected state.

3. Click **Open Console**.

4. A web browser tab opens `https://console.tun.procyon.ai` or `https://local.procyon.ai:8643` (when VPN interop mode is enabled). You can also open these URLs directly from your web browser.

## Accessing the user console in No Endpoint Controller-based deployments

In No Endpoint Controller-based deployments, users can access the user console directly through their PingOne environment.

---

---
title: Applications
description: Request just-in-time access to SAML applications.
component: privilege
page_id: privilege:human-privilege:user-use-cases/request-access/applications
canonical_url: https://docs.pingidentity.com/privilege/human-privilege/user-use-cases/request-access/applications.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2026
page_aliases: ["human-privilege:user-tasks/cloud/applications.adoc"]
---

# Applications

In the PingOne Privilege user console, you can request access to applications in **Permission Management > SaaS Apps**.

To request access, find the application in the **Active Applications** tab and click **Request**.

After the admin approves the request, you can access the application without a password for the granted duration.

---

---
title: Cloud resources
description: Request just-in-time access to Azure subscriptions.
component: privilege
page_id: privilege:human-privilege:user-use-cases/request-access/cloud-resources
canonical_url: https://docs.pingidentity.com/privilege/human-privilege/user-use-cases/request-access/cloud-resources.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2026
page_aliases: ["human-privilege:user-tasks/cloud/cloud-resources.adoc"]
---

# Cloud resources

Request just-in-time (JIT) access to Azure subscriptions.

1. In the PingOne Privilege user console, go to **Cloud > Resources**.

2. Select the icon for the onboarded cloud infrastructure.

3. (Optional) Filter by **Access Status** and **Resource Types**.

4. Find the subscription and request access.

---

---
title: Configuring a private proxy
description: Add a private proxy to an on-premise or non-AWS cloud network to enable secure access to resources within that network.
component: privilege
page_id: privilege:human-privilege:configuration/gateways/private-proxies
canonical_url: https://docs.pingidentity.com/privilege/human-privilege/configuration/gateways/private-proxies.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 4, 2026
page_aliases: ["configuration:network-infrastructure/configuring-private-gateways.adoc"]
section_ids:
  configure-a-private-proxy-using-the-setup-wizard: Configure a private proxy using the setup wizard
  before-you-begin: Before you begin
  steps: Steps
  next-steps: Next steps
  configure-a-private-proxy-using-docker: Configure a private proxy using Docker
  before-you-begin-2: Before you begin
  steps-2: Steps
  next-steps-2: Next steps
---

# Configuring a private proxy

Private proxies act as a secure entry point, allowing PingOne Privilege to manage and audit access to your internal resources.

PingOne Privilege allows you to add a private proxy using a setup wizard or through Docker.

## Configure a private proxy using the setup wizard

### Before you begin

* In the PingOne admin console, create an OIDC web application. For instructions, refer to [Creating a web application](https://docs.pingidentity.com/pingone/applications/p1_mfa_creating_a_web_application.html) in the PingOne documentation.

* Before you add a private proxy, create a new Virtual Machine (VM) to deploy the proxy container. Ensure the VM meets the required specifications for optimal performance and connectivity:

  * **CPU**: 2 cores, sufficient for processing proxy operations efficiently.

  * **RAM**: 4 GB ensures smooth container operation.

  * **Storage**: 20 GB accommodates system files and application data.

  * **Firewall Policy**:

    * **Outbound**: Allow all traffic.

    * **Inbound**: Open ports `8680`, and `8690` for application communication.

* Supported Operating Systems:

  * `RHEL / CentOS (RPM x86_64)`

  * `Debian / Ubuntu AMD64`

  * `Debian / Ubuntu ARM64`

### Steps

To add a private proxy using the setup wizard:

1. In the PingOne Privilege admin console, go to **Directory > Nodes**.

2. Click **Add New**, and then click **Add via Wizard**.

3. Review the requirements for your VM, then click **Next**.

4. Install Docker based on the official [Docker installation guide for your OS](https://docs.docker.com/engine/install/).

5. Verify Docker is running using the following command in your CLI:

   `sudo docker ps`

   If the command runs without errors, Docker is ready to use.

6. Select **Private Proxy** as your deployment mode. Click **Next**.

7. In the following **Gateway Config** wizard, ensure **Private Proxy** is selected.

8. Enter a unique **Proxy Cluster Name** to identify the private proxy group.

9. Enter the **FQDN / Host IP** of the server where you plan to install the proxy.

10. Click **Next**.

11. **(Optional)**: Click the **Deploy RDP** checkbox if you're deploying a remote desktop.

12. Create the environment file with the following commands:

    1. To create the directory, if not already present:

       `sudo mkdir -p /var/lib/procyon`

    2. To create the file and open it:

       `sudo vi /var/lib/procyon/procyon-guest-agent.env`

    3. Copy the generated content from your setup tasks and paste it inside the newly created file and save it.

    4. In the setup wizard, click **Next**.

13. Select your operating system from the list. Click **Show Instructions** for the detailed steps for installing the package for your operating system.

14. Click **Finish**.

### Next steps

After adding the private proxy, go to the **Nodes** page in the admin console. Your new private proxy should be listed with a `Verified` status.

## Configure a private proxy using Docker

### Before you begin

* In the PingOne admin console, create an OIDC web application. For instructions, refer to [Creating a web application](https://docs.pingidentity.com/pingone/applications/p1_mfa_creating_a_web_application.html) in the PingOne documentation.

* Ensure the following inbound ports are open on the host where you will install the private proxy:

  * `22`

  * `443`

  * `3389`

  * `8680`

  * `8690`

### Steps

To add a private proxy through Docker:

1. In the PingOne Privilege admin console, go to **Directory > Nodes**.

2. Click **Add New**, and then click **Add via Docker**.

3. Select **Private Proxy**.

4. Enter a unique **Cluster ID** to identify this proxy group.

5. Enter the **Host IP** of the server where you installed the proxy.

6. Click **Get Docker Command**.

7. Click **Copy Docker Command** to copy the command to your clipboard.

8. On your designated host within your on-premise network, run the Docker command you copied in the previous step.

   The proxy starts and automatically registers with the Endpoint Controller.

|   |                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The Endpoint Controller doesn't have automatic visibility into on-premise network topology. After deploying the proxy, you must manually configure which resources are accessible through it. |

### Next steps

After adding the private proxy, go to the **Nodes** page in the admin console. Your new private proxy should be listed with a `Verified` status.

---

---
title: Configuring a relay
description: "A relay is designed for deployment in networks that don't allow inbound connections, enabling access to resources within that private network."
component: privilege
page_id: privilege:human-privilege:configuration/gateways/relays
canonical_url: https://docs.pingidentity.com/privilege/human-privilege/configuration/gateways/relays.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 4, 2026
page_aliases: ["configuration:network-infrastructure/private-relays.adoc"]
section_ids:
  configure-a-relay-using-the-setup-wizard: Configure a relay using the setup wizard
  before-you-begin: Before you begin
  steps: Steps
  configure-a-relay-through-docker: Configure a relay through Docker
  before-you-begin-2: Before you begin
  steps-2: Steps
  result: Result:
  next-steps: Next steps
---

# Configuring a relay

Relays allow you to deploy in networks that don't allow inbound connections from the internet. The relay, deployed as a Docker container, establishes a secure, egress-only connection to a PingOne Privilege gateway, enabling access to resources located within its private network.

PingOne Privilege allows you to add a relay using a setup wizard or through Docker.

## Configure a relay using the setup wizard

### Before you begin

* In the PingOne admin console, create an OIDC web application. For instructions, refer to [Creating a web application](https://docs.pingidentity.com/pingone/applications/p1_mfa_creating_a_web_application.html) in the PingOne documentation.

* Before you add a relay, create a new Virtual Machine (VM) to deploy the proxy container. Ensure the VM meets the required specifications for optimal performance and connectivity:

  * **CPU**: 2 cores, sufficient for processing proxy operations efficiently.

  * **RAM**: 4 GB ensures smooth container operation.

  * **Storage**: 20 GB accommodates system files and application data.

  * **Firewall Policy**:

    * **Outbound**: Allow all traffic.

* Supported Operating Systems:

  * `RHEL / CentOS (RPM x86_64)`

  * `Debian / Ubuntu AMD64`

  * `Debian / Ubuntu ARM64`

### Steps

To add a relay using the setup wizard:

1. In the PingOne Privilege admin console, go to **Directory > Nodes**.

2. Click **Add New**, and then click **Add via Wizard**.

3. Review the requirements for your VM, then click **Next**.

4. Install Docker based on the official [Docker installation guide for your OS](https://docs.docker.com/engine/install/).

5. Verify Docker is running using the following command in your CLI:

   `sudo docker ps`

   If the command runs without errors, Docker is ready to use.

6. Select **Private Proxy** as your deployment mode. Click **Next**

7. In the following **Gateway Config** wizard, ensure **Relay** is selected.

8. Enter a **Relay Name** to identify your relay.

9. Enter the **Host Name** of the server where you plan to install the relay.

10. **(Optional)**: Click the **Deploy RDP** checkbox to deploy a remote desktop.

11. Click **Next**.

12. Create the environment file with the following commands:

    1. To create the directory, if not already present:

       `sudo mkdir -p /var/lib/procyon`

    2. To create the file and open it:

       `sudo vi /var/lib/procyon/procyon-guest-agent.env`

    3. Copy the generated content from your setup tasks and paste it inside the newly created file and save it.

    4. In the setup wizard, click **Next**.

13. Select your operating system from the list. Click **Show Instructions** for the detailed steps for installing the package for your operating system.

14. Click **Finish**.

## Configure a relay through Docker

### Before you begin

* In the PingOne admin console, create an OIDC web application. For instructions, refer to [Creating a web application](https://docs.pingidentity.com/pingone/applications/p1_mfa_creating_a_web_application.html) in the PingOne documentation.

* Ensure the following inbound ports are open on the host where you will install the relay:

  * `22`

  * `443`

  * `3389`

  * `8680`

  * `8690`

### Steps

To add a relay through Docker:

1. In the PingOne Privilege admin console, go to **Directory > Nodes**.

2. Click **Add New**, and then click **Add via Docker**.

3. Select **Relay**.

4. Enter a unique **Cluster ID** to identify this relay group.

5. Enter the **Host Name** of the server where you installed the relay.

6. Click **Copy Docker Command** to copy the command to your clipboard.

7. On your designated host within your on-premise network, run the Docker command you just copied.

   ### Result:

   The relay starts and automatically registers with the Endpoint Controller.

|   |                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The Endpoint Controller doesn't have automatic visibility into on-premise network topology. After deploying the relay, you must manually configure which resources are accessible through it. |

### Next steps

After adding the relay, go to the **Nodes** page in the admin console. Your new relay should be listed with **Verified** status.

---

---
title: Configuring Amazon EKS access
description: The steps to configure your Amazon EKS clusters to allow access management through the PingOne Privilege platform.
component: privilege
page_id: privilege:human-privilege:configuration/configuring-kubernetes-access/aws-eks
canonical_url: https://docs.pingidentity.com/privilege/human-privilege/configuration/configuring-kubernetes-access/aws-eks.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 4, 2026
page_aliases: ["configuration:configuring-kubernetes-access/aws-eks.adoc"]
section_ids:
  onboard-the-cluster-in-pingone-privilege: Onboard the cluster in PingOne Privilege
  additional-considerations: Additional considerations
  private-clusters: Private clusters
  default-permissions: Default permissions
---

# Configuring Amazon EKS access

After you onboard an Amazon Web Services (AWS) *(tooltip: \<div class="paragraph">
\<p>An Amazon subsidiary providing cloud computing platforms.\</p>
\</div>)* account to PingOne Privilege, you can manage access to your Amazon Elastic Kubernetes Service (EKS) clusters and namespaces at a granular level.

|   |                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If an EKS cluster is configured to use the EKS API for authentication in combination with the `aws-auth` ConfigMap, PingOne Privilege automatically falls back to using the EKS API. |

## Onboard the cluster in PingOne Privilege

1. In the PingOne Privilege admin console, go to **Cloud > Clouds**.

2. On the tile for your AWS account, click **More Info**.

3. Click **Rescan**.

4. After the rescan completes, go to **Cloud > Targets**.

5. Find the newly discovered cluster and click **More Info**.

6. Click the **Manage** toggle to the right (blue) to onboard it.

For more details, see [Onboarding target resources](../../admin-use-cases/access-management/cloud-accounts.html#onboarding-target-resources).

## Additional considerations

### Private clusters

If your EKS cluster is in a private VPC with no inbound internet access, you must deploy a PingOne Privilege gateway or relay within the same VPC. Learn more in [Configuring gateways](../gateways/index.html).

### Default permissions

By default, an administrative user is granted the `ProcyonKubeCtlView` permission. After connecting to PingOne Privilege using the Endpoint Controller, the user's Kubernetes context will be automatically available in their local `~/.kube/config` file.

---

---
title: Configuring Azure AKS access
description: The required configurations within the Azure portal to allow PingOne Privilege to discover and manage your Azure Kubernetes Service (AKS) clusters.
component: privilege
page_id: privilege:human-privilege:configuration/configuring-kubernetes-access/azure-aks
canonical_url: https://docs.pingidentity.com/privilege/human-privilege/configuration/configuring-kubernetes-access/azure-aks.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 4, 2026
page_aliases: ["configuration:configuring-kubernetes-access/azure-aks.adoc"]
section_ids:
  step-1-configure-authentication-on-the-aks-cluster: "Step 1: Configure authentication on the AKS cluster"
  step-2-assign-iam-roles-to-the-connector-app: "Step 2: Assign IAM roles to the connector app"
  step-3-onboard-the-cluster-in-pingone-privilege: "Step 3: Onboard the cluster in PingOne Privilege"
  next-steps: Next steps
---

# Configuring Azure AKS access

This topic describes the required configurations within the Azure portal to allow PingOne Privilege to discover and manage your Azure Kubernetes Service (AKS) clusters. The process involves configuring the cluster's authentication method and assigning the necessary roles to the PingOne Privilege connector application.

## Step 1: Configure authentication on the AKS cluster

First, configure your AKS cluster to use Microsoft Entra ID for authentication while still allowing local accounts.

1. In the Azure portal, go to your Kubernetes services.

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

## Next steps

After the rescan is complete, the AKS cluster will be available to manage.

1. In the PingOne Privilege admin console, go to **Cloud > Targets**.

2. Find the newly discovered cluster, then click **More Info**.

3. Click the **Manage** toggle to the right (blue) to onboard it.

The AKS cluster is now managed by PingOne Privilege.

---

---
title: Configuring certificate-based SSH
description: Configure your managed servers to accept SSH connections that are authenticated by short-lived certificates issued by PingOne Privilege.
component: privilege
page_id: privilege:human-privilege:configuration/access-protocols/ssh
canonical_url: https://docs.pingidentity.com/privilege/human-privilege/configuration/access-protocols/ssh.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 4, 2026
page_aliases: ["configuration:access-protocols/ssh.adoc"]
section_ids:
  step-1-retrieve-the-pingone-privilege-ssh-ca-public-key: "Step 1: Retrieve the PingOne Privilege SSH CA public key"
  method-a-using-the-pingone-privilege-admin-console: "Method A: Using the PingOne Privilege admin console"
  method-b-using-the-api: "Method B: Using the API"
  step-2-configure-the-target-server: "Step 2: Configure the target server"
---

# Configuring certificate-based SSH

To enable passwordless access, you can configure your managed servers to trust Secure Shell (SSH) *(tooltip: \<div class="paragraph">
\<p>Protocol for secure operation of network services over an unsecured network.\</p>
\</div>)* connections that are authenticated by short-lived certificates issued by PingOne Privilege. This process must be completed on each target server that you want to access through SSH.

|   |                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Instead of configuring target servers manually, you can install the Endpoint Controller on them from your **Settings** in the PingOne Privilege admin console. Learn more in [Onboarding users](../../../getting-started/onboarding-users.html). |

|   |                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------- |
|   | Automation tools such as Ansible, Terraform, or custom scripting can help you apply these changes consistently across all your servers. |

## Step 1: Retrieve the PingOne Privilege SSH CA public key

First, you need to get the SSH Certificate Authority (CA) public key for your tenant. You can do this through the admin console or through an API call.

### Method A: Using the PingOne Privilege admin console

1. In the PingOne Privilege admin console, go to **Cloud > Clouds**.

2. Select the relevant account.

3. Copy the **SSH Public Key**.

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

## Step 2: Configure the target server

Next, apply the configuration to each target server.

1. Connect to the server using a standard SSH client.

2. Create a file to store the public key, such as `/etc/ssh/ca.pub`.

3. Paste the CA public key you retrieved in the previous step into the new file.

4. Open the SSH daemon's configuration file for editing. On most Linux distributions, this file is located at `/etc/ssh/sshd_config`.

   ```bash
   $ sudo vi /etc/ssh/sshd_config
   ```

5. Add the `TrustedUserCAKeys` directive to the file, pointing to the CA public key file you just created.

   ```text
   # Add this line to sshd_config
   TrustedUserCAKeys /etc/ssh/ca.pub
   ```

   |   |                                                                                                   |
   | - | ------------------------------------------------------------------------------------------------- |
   |   | Ensure the path in this directive exactly matches the location where you saved the `ca.pub` file. |

6. Save your changes to the `sshd_config` file.

7. Restart the SSH daemon to apply the new configuration. The command can vary depending on your operating system.

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
title: Configuring gateways for Human Privilege
description: Gateways are entry points for accessing resources on a private network, enabling secure sessions and intelligent routing.
component: privilege
page_id: privilege:human-privilege:configuration/gateways/index
canonical_url: https://docs.pingidentity.com/privilege/human-privilege/configuration/gateways/index.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 4, 2026
page_aliases: ["configuration:network-infrastructure/gateways.adoc", "human-privilege:configuration/gateways/gateways.adoc", "configuration:network-infrastructure.adoc"]
---

# Configuring gateways for Human Privilege

Gateways are fundamental components that act as entry points for accessing resources on a private network. The Endpoint Controller intelligently determines the optimal gateway path to connect a user with a resource, ensuring efficient and secure access.

Human Privilege supports different types of gateways depending on your environment. As an administrator, you can configure the following:

* [Private Proxies](private-proxies.html)

  Choose this option to deploy a gateway on your own infrastructure, such as Google Cloud Platform (GCP), Microsoft Azure, or your own on-premise data centers.

* [Relays](relays.html)

  Relays are used in networks that don't allow inbound connections. They establish an outbound connection to a gateway, creating a secure tunnel for traffic without requiring you to open firewall ports.

Together, these components create a flexible and secure network infrastructure that allows Human Privilege to manage access to any resource, regardless of its location or network configuration.

|   |                                                                                        |
| - | -------------------------------------------------------------------------------------- |
|   | To ensure high availability, we recommend deploying at least two gateways per network. |

---

---
title: Configuring GCP GKE access
description: The required configurations within your GCP project to allow PingOne Privilege to discover and manage your GKE clusters.
component: privilege
page_id: privilege:human-privilege:configuration/configuring-kubernetes-access/gcp-gke
canonical_url: https://docs.pingidentity.com/privilege/human-privilege/configuration/configuring-kubernetes-access/gcp-gke.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 4, 2026
page_aliases: ["configuration:configuring-kubernetes-access/gcp-gke.adoc"]
section_ids:
  step-1-verify-service-account-permissions: "Step 1: Verify service account permissions"
  step-2-onboard-the-cluster-in-pingone-privilege: "Step 2: Onboard the cluster in PingOne Privilege"
  next-steps: Next steps
---

# Configuring GCP GKE access

This topic describes the required configurations within your Google Cloud Platform (GCP) project to allow PingOne Privilege to discover and manage your Google Kubernetes Engine (GKE) clusters. The process involves verifying service account permissions, configuring Role-Based Access Control (RBAC) on the Kubernetes *(tooltip: \<div class="paragraph">
\<p>An open-source system for automating deployment and management of containerized applications.\</p>
\</div>)* cluster, and then onboarding the cluster in PingOne Privilege.

## Step 1: Verify service account permissions

First, ensure the service account used to onboard your GCP project to PingOne Privilege has the necessary permissions to manage Kubernetes resources.

1. In the PingOne Privilege admin console, go to **Cloud > IAM Roles**.

2. Find the service account associated with your PingOne Privilege integration.

3. Verify that the service account has the **Kubernetes Engine Admin** role.

   This role allows PingOne Privilege to discover and interact with your GKE clusters. If it doesn't, edit the principal's permissions and add this role.

## Step 2: Onboard the cluster in PingOne Privilege

After completing the configuration in the GCP console, rescan your account in PingOne Privilege to discover and manage the cluster.

1. In the PingOne Privilege admin console, go to **Cloud > Clouds**.

2. Find your GCP cloud account, and click **More Info**.

3. Go to the **Resources** tab and click **Rescan**.

## Next steps

After the rescan is complete, the GKE cluster is available to manage in PingOne Privilege.

1. In the PingOne Privilege admin console, go to **Cloud > Targets**.

2. Find the newly discovered cluster, then click **More Info**.

3. Click the **Manage** toggle to the right (blue) to onboard it.

---

---
title: Configuring Human Privilege
description: "Learn how to set up and customize Human Privilege to suit your organization's requirements."
component: privilege
page_id: privilege:human-privilege:configuration/index
canonical_url: https://docs.pingidentity.com/privilege/human-privilege/configuration/index.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 28, 2026
page_aliases: ["configuration:index.adoc"]
section_ids:
  access-cloud-resources-directly: Access cloud resources directly
  access-kubernetes-clusters: Access Kubernetes clusters
  access-on-premise-servers-and-databases: Access on-premise servers and databases
  add-mfa-challenges: Add MFA challenges
---

# Configuring Human Privilege

This section provides guidance for administrators on configuring Human Privilege. Which configuration steps you need depends on the resources your organization uses and how users connect to them. Find your scenario in the following topics, then follow the linked pages in the order shown.

|   |                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you're securing AI agent access instead of human access, refer to [Configuring Agent Privilege](../../agent-privilege/index.html). |

## Access cloud resources directly

Choose this path to configure just-in-time (JIT) access to cloud resources, including:

* [AWS](cloud-accounts/aws.html)

* [Azure](cloud-accounts/azure.html)

* [GCP](cloud-accounts/gcp.html)

## Access Kubernetes clusters

Choose this path to configure just-in-time access to Kubernetes *(tooltip: \<div class="paragraph">
\<p>An open-source system for automating deployment and management of containerized applications.\</p>
\</div>)* clusters. You must first onboard the cloud account before configuring access to Kubernetes clusters:

* [Configure AWS EKS access](configuring-kubernetes-access/aws-eks.html)

* [Configure Azure AKS access](configuring-kubernetes-access/azure-aks.html)

* [Configure GCP GKE access](configuring-kubernetes-access/gcp-gke.html)

If the cluster is in a private VPC with no inbound internet access, you must also deploy a gateway or relay. Learn more in [Gateways](gateways/index.html).

## Access on-premise servers and databases

Choose this path to configure access to resources on a private network, such as on-premise servers, databases, or applications. You must first configure the network infrastructure, since resources are only reachable through a gateway.

The basic flow for this path involves:

1. Configure the necessary network infrastructure based on your organization's needs:

   * [Deploy a gateway](gateways/index.html) on your own infrastructure.

   * If your network doesn't allow inbound connections, [deploy private relays](gateways/relays.html) instead.

2. After configuring a **Private Proxy** or **Relay**, you can:

   * [Configure certificate-based SSH](access-protocols/ssh.html) for passwordless access on Linux servers.

   * [Configure RDP access](access-protocols/rdp.html) for Windows servers.

## Add MFA challenges

Choose this path to challenge onboarded users with MFA when they connect to PingOne Privilege or escalate privileges. Based on your PingOne Privilege deployment model, you can:

1. [Require PingID Workforce Authentication when users connect to the Endpoint Controller](multi-factor-authentication/pingid-mfa-app-connect.html) in Endpoint Controller-based deployments.

2. [Require step-up authentication for sudo commands](multi-factor-authentication/step-up-authentication-sudo.html) in No Endpoint Controller deployments.

---

---
title: Configuring Kubernetes access
description: Configure Kubernetes access for onboarded cloud accounts to enable just-in-time access for teams running containerized workloads.
component: privilege
page_id: privilege:human-privilege:configuration/configuring-kubernetes-access/index
canonical_url: https://docs.pingidentity.com/privilege/human-privilege/configuration/configuring-kubernetes-access/index.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 28, 2026
page_aliases: ["configuration:configuring-kubernetes-access/index.adoc"]
---

# Configuring Kubernetes access

You can configure Kubernetes *(tooltip: \<div class="paragraph">
\<p>An open-source system for automating deployment and management of containerized applications.\</p>
\</div>)* access for onboarded cloud accounts to enable just-in-time (JIT) access for teams running containerized workloads. This integration allows organizations to enforce least-privilege, time-bound access to Kubernetes resources, centralized in the PingOne Privilege platform.

PingOne Privilege supports the following Kubernetes services:

* [AWS Elastic Kubernetes Service (EKS)](aws-eks.html)

* [Azure Kubernetes Service (AKS)](azure-aks.html)

* [Google Kubernetes Engine (GKE)](gcp-gke.html)

Select the appropriate guide for your cloud provider to continue.

---

---
title: Configuring remote desktop access
description: When you onboard a cloud account, PingOne Privilege automatically discovers all remote desktop protocol (RDP) instances.
component: privilege
page_id: privilege:human-privilege:configuration/access-protocols/rdp
canonical_url: https://docs.pingidentity.com/privilege/human-privilege/configuration/access-protocols/rdp.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 28, 2026
page_aliases: ["configuration:access-protocols/rdp.adoc"]
section_ids:
  before-you-begin: Before you begin
  step-1-create-rdp-user-management: "Step 1: Create RDP user management"
  method-a-for-non-domain-joined-machines: "Method A: For Non-Domain-Joined Machines"
  method-b-for-domain-joined-machines: "Method B: For Domain-Joined Machines"
  step-2-bind-the-rdp-instance-to-the-configuration: "Step 2: Bind the RDP instance to the configuration"
  editing-a-principal-in-rdp-user-management: Editing a principal in RDP user management
---

# Configuring remote desktop access

When you onboard a cloud account, PingOne Privilege automatically discovers all Remote Desktop Protocol (RDP) instances, which are then listed as targets. To enable passwordless access to these targets, you must configure an access method based on whether the target machine is or isn't joined to an Active Directory (AD) domain.

## Before you begin

To set up remote desktop access, ensure you have either a **Private Proxy** or a **Relay**, configured under **Directory > Nodes**.

## Step 1: Create RDP user management

Choose one of the following methods depending on your target environment.

### Method A: For Non-Domain-Joined Machines

For standalone Windows servers, use the Local User mode to store and manage a local administrator account.

1. In the PingOne Privilege admin console, go to **Infrastructure > RDP User Management**.

2. Click **Create**.

3. Enter a **Name** for this configuration, such as `Standalone Web Servers`.

   * If you select **Password** as your **Authentication Type**, follow these steps:

     1. Click the **Local User Mode** toggle to the right (blue) to enable it.

     2. In the **Admin Username** and **Admin Password** fields, enter the credentials for a local administrator account on the target machine.

     3. (Optional) Enable the **Rotate Passwords** feature.

     4. For each standard domain user account you want to manage, enter their **Username / Password**.

     5. Click the blue **User** icon.

     6. In the **Select User** window, associate the user with their credentials.

        These credentials are securely stored in the PingOne Privilege vault.

   * If you select **Smart Card** as your **Authentication Type**, follow these steps:

     1. In the **Username** field enter the username for a local administrator account on the target machine.

     2. Click the blue **User** icon.

     3. In the **Select User** window, associate the user with their credentials.

4. To make the domain controller configuration the default for RDP targets in that cloud provider, select the **Cloud Type**

   * **AWS**

   * **AZURE**

   * **GCP**

   * **PRIVATE**

5. Click **Create**.

### Method B: For Domain-Joined Machines

For Windows servers joined to an Active Directory domain, create a configuration that stores domain credentials.

1. In the PingOne Privilege admin console, go to **Infrastructure > RDP User Management**.

2. Click **Create**.

3. Enter a **Name** for this configuration, such as `Corporate AD Domain`.

   * If you select **Password** as your **Authentication Type**, follow these steps:

     1. Ensure the **Local User Mode** toggle is disabled.

     2. Enter the **Admin Username** and **Admin Password** for a privileged **Domain Admin** account.

        This service account is used by PingOne Privilege to manage other users' passwords within the domain.

     3. **(Optional)** Enable the **Rotate Passwords** feature.

     4. For each standard domain user account you want to manage, enter their **Username / Password**.

     5. Click the blue **User** icon.

     6. In the **Select User** window, associate the user with their credentials.

        |   |                                                           |
        | - | --------------------------------------------------------- |
        |   | Use `user@domain` as the username for the domain account. |

   * If you select **Smart Card** as your **Authentication Type**, follow these steps:

     1. In the **Username** field, enter the username for a local administrator account on the target machine.

        |   |                                                           |
        | - | --------------------------------------------------------- |
        |   | Use `user@domain` as the username for the domain account. |

     2. Click the blue **User** icon.

     3. In the **Select User** window, associate the user with their credentials.

4. To make the domain controller configuration the default for RDP targets in that cloud provider, select the **Cloud Type**

   * **AWS**

   * **AZURE**

   * **GCP**

   * **PRIVATE**

5. Click **Create**.

## Step 2: Bind the RDP instance to the configuration

After creating a configuration, you must bind it to each RDP target.

1. In the PingOne Privilege admin console, go to **Cloud > Targets**.

2. Find the target RDP instance and click **More Info**.

3. From the **RDP User Management** list, select the configuration you created in the previous step.

4. Click the **Managed** toggle for the RDP instance to the right (blue) to enable it. Click **Save**.

5. Click **Create**.

## Editing a principal in RDP user management

After you create an RDP user management configuration, you can edit the principal associations in it to change which user is mapped to which stored credential.

1. In the PingOne Privilege admin console, go to **Infrastructure > RDP User Management**.

2. Find the configuration you want to change and click **More Info**.

3. Update the **Username / Password** entries or their **User** associations as needed.

4. Click **Save**.

---

---
title: Configuring step-up authentication for sudo commands
description: Require step-up multi-factor authentication when users run sudo commands on Unix/Linux servers with just-in-time (JIT) access.
component: privilege
page_id: privilege:human-privilege:configuration/multi-factor-authentication/step-up-authentication-sudo
canonical_url: https://docs.pingidentity.com/privilege/human-privilege/configuration/multi-factor-authentication/step-up-authentication-sudo.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 10, 2026
page_aliases: ["configuration:multi-factor-authentication/step-up-authentication-sudo.adoc"]
section_ids:
  how-step-up-authentication-works: How step-up authentication works
  mfa-methods-supported: MFA methods supported
  configuring-a-step-up-authentication-policy: Configuring a step-up authentication policy
  before-you-begin: Before you begin
  steps: Steps
  step-up-authentication-and-jit-access: Step-up authentication and JIT access
---

# Configuring step-up authentication for sudo commands

Step-up authentication adds a multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)* challenge when a user runs the `sudo` command on a Unix/Linux server accessed through PingOne Privilege. The challenge is presented directly in the user's terminal session.

Without step-up authentication, users with just-in-time (JIT) access can execute allowed `sudo` commands after signing on without any additional verification. If a user's session is compromised, an attacker can escalate privileges unchecked. Step-up authentication confirms the human presence of the user at the moment of privilege escalation.

Consider requiring step-up authentication when your organization must comply with regulatory frameworks such as PCI, HIPAA, or SOX, which call for additional verification for privileged command execution.

## How step-up authentication works

1. A user with JIT access opens a session on a Unix/Linux server.

2. The user runs a `sudo` command.

3. If a step-up authentication policy applies, PingOne Privilege triggers an MFA challenge in the terminal session.

4. The user completes the challenge using an approved MFA method.

5. If the challenge succeeds, the `sudo` command proceeds. If it fails or times out, PingOne Privilege denies the command.

PingOne Privilege logs every step-up challenge and response for audit and compliance purposes. You can review these events in the session and activity logs. Learn more in [Managing session logs](../../admin-use-cases/activity/session-logs.html) and [Managing activity logs](../../admin-use-cases/activity/activity-logs.html).

## MFA methods supported

Step-up authentication supports the MFA methods configured in your PingOne environment, including:

* PingID mobile app (push notification or one-time passcode (OTP) *(tooltip: \<div class="paragraph">
  \<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>
  \</div>)*)

* PingID desktop app

* Other MFA methods supported by PingOne, such as biometric or device-bound passwordless authentication

To challenge users when they connect the PingOne Privilege app, learn more in [Requiring PingID Workforce Authentication for PingOne Privilege app connections](pingid-mfa-app-connect.html).

## Configuring a step-up authentication policy

Configure step-up authentication policies in the PingOne admin console. A policy defines when a `sudo` command requires an MFA challenge, such as every `sudo` attempt, specific commands, or time-based conditions.

### Before you begin

* Users have JIT access to Unix/Linux servers through PingOne Privilege. Learn more in [Managing policies](../../admin-use-cases/access-management/policies.html).

* MFA is configured for your PingOne environment.

### Steps

To require step-up authentication for `sudo` commands:

1. In the PingOne admin console, go to the MFA policy settings for PingOne Privilege.

2. Create or edit a policy that targets the Unix/Linux servers in scope.

3. Select the option to require step-up authentication for privileged commands, and choose when the challenge applies.

4. Save the policy.

The policy takes effect for new `sudo` commands in active sessions. Users already running an interactive session aren't challenged until their next `sudo` attempt.

## Step-up authentication and JIT access

Step-up authentication works with your existing JIT access policies. A user must still hold valid JIT access to the server before they can open a session. Step-up authentication adds verification at the moment of privilege escalation, not at session start.

If you use both JIT access policies and step-up authentication, users experience the following:

1. The user requests access through the self-service portal, or a policy grants the user access.

2. The user connects to the server using passwordless access.

3. The user runs `sudo`, which triggers the MFA challenge defined by the step-up authentication policy.

---

---
title: Databases
description: Request just-in-time access to MySQL and Postgres databases.
component: privilege
page_id: privilege:human-privilege:user-use-cases/request-access/databases
canonical_url: https://docs.pingidentity.com/privilege/human-privilege/user-use-cases/request-access/databases.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2026
page_aliases: ["human-privilege:user-tasks/cloud/databases.adoc"]
---

# Databases

Request just-in-time (JIT) access to MySQL and Postgres databases:

1. In the PingOne Privilege user console, go to **Cloud > Targets**.

2. Select the cloud and the account.

3. Select the appropriate principal from the list. This list is configured by a PingOne Privilege administrator.

4. Add more resources as needed and submit the request.

5. After the access request is granted by the admin, the user can access the database by copying the connection command directly from the Endpoint Controller.

---

---
title: Devices
description: Every registered device is associated with a user.
component: privilege
page_id: privilege:human-privilege:user-use-cases/devices
canonical_url: https://docs.pingidentity.com/privilege/human-privilege/user-use-cases/devices.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2026
page_aliases: ["human-privilege:user-tasks/devices/devices.adoc", "privileged-access-management:user-tasks/devices/devices.adoc"]
section_ids:
  viewing-devices: Viewing devices
  activating-and-deactivating-a-device: Activating and deactivating a device
  removing-a-device: Removing a device
---

# Devices

On the PingOne Privilege platform, every registered device is associated with a user. Users can manage their devices through the user console.

## Viewing devices

To view your devices:

1. In the PingOne Privilege user console, go to **Directory > Devices**.

2. In the list, locate a device and click **View Details**.

   The device details page includes an overview of the device, such as **Operating System**, **Model**, and **Device Identifier**.

## Activating and deactivating a device

Deactivating a device temporarily prevents it from being used to access resources.

To activate or deactivate a device:

1. In the PingOne Privilege user console, go to **Directory > Devices**.

2. In the list, locate the device to deactivate and click **View Details**.

3. Click the **Active Device** toggle to activate or deactivate the device.

## Removing a device

Removing a device permanently unregisters it from the PingOne Privilege platform. The user must onboard the device again to use it.

|   |                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------ |
|   | Deactivating or removing a device will instantly terminate all active sessions originating from that device. |

To remove a device:

1. In the PingOne Privilege user console, go to **Directory > Devices**.

2. In the list, locate the device to remove and click **View Details**.

3. Click **Remove Device**.

4. Confirm the action by clicking **Remove**.

---

---
title: Getting started with Human Privilege
description: "Get started with Human Privilege: sign on to the console, then jump to the use cases for administrators or users."
component: privilege
page_id: privilege:human-privilege:getting-started
canonical_url: https://docs.pingidentity.com/privilege/human-privilege/getting-started.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 28, 2026
section_ids:
  sign-on: Sign on
  use-human-privilege: Use Human Privilege
  next-steps: Next steps
---

# Getting started with Human Privilege

Human Privilege secures how people in your organization reach servers, databases, Kubernetes *(tooltip: \<div class="paragraph">
\<p>An open-source system for automating deployment and management of containerized applications.\</p>
\</div>)* clusters, and cloud consoles and CLIs. This topic covers accessing the PingOne Privilege console and points you to the use cases for your role.

## Sign on

How you sign on depends on your organization's deployment model:

* **Endpoint Controller-based:** Launch the Endpoint Controller on your managed device and connect. You open the admin or user console through the Endpoint Controller. Learn more in [Onboarding users](../getting-started/onboarding-users.html).

* **No Endpoint Controller-based:** In PingOne, go to the console URL directly and sign on through PingOne SSO.

Learn more in [Choosing a deployment model](../getting-started/choosing-deployment-model.html).

## Use Human Privilege

After signing on, the console you see depends on your role:

* **Administrators**

  Work in the admin console, where they can manage the directory, access policies, access requests, and activity monitoring. Explore [use cases for admins](admin-use-cases/index.html).

* **Users**

  Work in the user console, where they can request access to resources and manage your requests, devices, and activity. Explore [use cases for users](user-use-cases/index.html).

## Next steps

PingOne Privilege provides a catalog of [Integrations](../integrations/index.html) to connect the services your teams already use, such as Jira, Microsoft Teams, ServiceNow, and Slack.

---

---
title: Kubernetes clusters
description: Users can request just-in-time access at the cluster, namespace, or pod level.
component: privilege
page_id: privilege:human-privilege:user-use-cases/request-access/kubernetes-clusters
canonical_url: https://docs.pingidentity.com/privilege/human-privilege/user-use-cases/request-access/kubernetes-clusters.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 28, 2026
page_aliases: ["human-privilege:user-tasks/cloud/kubernetes-clusters.adoc"]
section_ids:
  requesting-access-cluster: Requesting access to a cluster
  requesting-access-namespace: Requesting access to a namespace
---

# Kubernetes clusters

Users can request just-in-time (JIT) access at the Kubernetes *(tooltip: \<div class="paragraph">
\<p>An open-source system for automating deployment and management of containerized applications.\</p>
\</div>)* cluster, namespace, or pod level.

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
page_id: privilege:human-privilege:admin-use-cases/access-management/access-requests
canonical_url: https://docs.pingidentity.com/privilege/human-privilege/admin-use-cases/access-management/access-requests.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2026
page_aliases: ["human-privilege:admin-tasks/access-requests.adoc"]
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

You can also:

* [Manage auto-approval policies](#auto-approval-policies)

* [Remove a user's access to one resource](#removing-access-one)

* [Remove a user's access to all resources](#removing-access-all)

To manage requests, click **Access Requests**.

The page is organized into several tabs: **Pending Requests**, **Approved Requests**, **History**, and **Auto Approve**.

## Manually approving pending requests

The **Pending Requests** tab lists all submitted requests that are awaiting a decision.

1. In the PingOne Privilege admin console, go to **Access Management > Access Requests**.

2. Click the **Pending** tab.

3. Click **View Details** on a request to examine its contents.

4. Review the request details:

   * Requester name and email

   * Requested resources

   * Requested duration

   * User comments

5. Click **Approve** or **Reject**.

   The user is notified of the decision in their user portal. If Slack notifications are enabled, a message is also sent to the configured Slack channel.

## Viewing approved requests

The **Approved Requests** tab displays all active sessions. Click any request to view its details.

### Revoking access

An administrator can end an approved session manually before its scheduled expiration.

1. In the PingOne Privilege admin console, go to **Access Management > Access Requests**.

2. Click the **Approved** tab.

3. In the list, find the active request you want to revoke.

4. Click **View Details** to open the request.

5. Click **Close** to terminate the session. Access to the resources is instantly revoked.

## Viewing request history

The **History** tab lists all past requests, including approved, closed, and expired ones. The available filters are time and user.

## Managing auto-approval policies

The **Auto Approve** tab lists all active auto-approval policies.

### Configuring an auto-approval policy

While approving a user's requests, you can create a policy to automatically approve similar requests:

1. During the manual approval process for a user's request, select the **Auto-approve future requests** checkbox.

2. Specify the maximum duration for which future requests can be auto-approved.

3. Add any comments for auditing purposes and click **Approve**.

An auto-approval policy is generated for that user and is listed in the **Auto Approve** tab.

### Deleting an auto-approval policy

To delete an auto-approval policy:

1. In the PingOne Privilege admin console, go to **Access Management > Access Requests**.

2. Click the **Auto Approve** tab.

3. In the list, find the auto-approval you want to delete.

4. Click **View Details** to open the policy.

5. Click **Delete Auto-Approve Policy** to remove the policy.

## Removing access to a resource

The following process removes a user's access to an individual resource:

1. Delete the approval request associated with the resource.

2. Delete the policy associated with the approval. Learn more about policies in [Managing policies](policies.html).

3. Delete the auto-approval policy if the access is granted through an auto-approval process.

## Revoking access to all resources

You can revoke a user's access to all resources either permanently or temporarily. You may want to permanently revoke access if a user reports their device stolen. Otherwise, you may want to temporarily revoke access while the operating system of the device associated with a user is being patched.

To revoke a user's access to all resources:

* **Permanently**:

  1. In the PingOne Privilege admin console, go to **Directory > Devices**.

  2. In the list, find the device to delete and click **View Details**.

  3. Click **Remove Device**.

  4. Confirm the action by clicking **Remove**.

* **Temporarily**:

  1. In the PingOne Privilege admin console, go to **Directory > Devices**.

  2. In the list, find the device to delete and click **View Details**.

  3. Click the **Active Device** toggle to turn it off.

     This deactivates all access for that user from that device.

  4. When you want to reactivate, click the **Active Device** toggle to turn it on again.