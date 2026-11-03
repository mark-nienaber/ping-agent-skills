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
  accessing-the-admin-console-in-endpoint-controller-based-models: Accessing the admin console in Endpoint Controller-based models
  result: Result:
  result-2: Result
  accessing-the-admin-console-in-no-endpoint-controller-based-models: Accessing the admin console in No Endpoint Controller-based models
  result-3: Result:
  result-4: Result
---

# Accessing the PingOne Privilege admin console as an administrator

The PingOne Privilege admin console provides a centralized interface to configure settings, manage users, and monitor access activities.

## Accessing the admin console in Endpoint Controller-based models

After completing the initial setup of your PingOne Privilege environment in PingOne, you can authenticate into the PingOne Privilege admin console.

To access the admin console:

1. In the PingOne admin console, go to **Directory > Users**.

2. Click the user you created with admin privileges.

3. In the **Services** list, select **PingOne Privilege**.

4. Click **Generate Onboarding Link**.

   ### Result:

   A link is automatically sent through email if an email address is configured for the PingOne admin user.

5. Open the link sent to email or copy the generated onboarding link and open it in a new browser tab.

6. In the new tab, download the Endpoint Controller and complete the installation on your computer.

7. Click the Endpoint Controller icon in your system tray. Click **Open Console**.

   ![The Endpoint Controller icon menu with the Open Console option visible.](_images/p1p_open_console.png)

   The PingOne Privilege admin console opens in a new browser tab.

8. Enter your admin **Username** and **Password**.

9. Click **Sign On**.

### Result

You can now use the PingOne Privilege console to [onboard users](onboarding-users.html).

## Accessing the admin console in No Endpoint Controller-based models

After completing the initial setup of your PingOne Privilege environment in PingOne, you can authenticate into the PingOne Privilege admin console.

1. In the PingOne admin console, go to **Settings > Environment Properties**.

2. In the **URLs** section, click the **PingOne Privilege Console Url** link.

   ### Result:

   A new tab opens to provide credentials for the PingOne Privilege admin console.

3. Enter your admin **Username** and **Password**.

4. Click **Sign On**.

### Result

You can now use the PingOne Privilege admin console to [onboard users](onboarding-users.html).

---

---
title: Choosing a deployment model
description: PingOne Privilege offers both Endpoint Controller-based and No Endpoint Controller-based deployment models to meet different organizational needs.
component: privilege
page_id: privilege:getting-started:choosing-deployment-model
canonical_url: https://docs.pingidentity.com/privilege/getting-started/choosing-deployment-model.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 8, 2026
section_ids:
  endpoint-controller-based-model: Endpoint Controller-based model
  no-endpoint-controller-based-model: No Endpoint Controller-based model
---

# Choosing a deployment model

PingOne Privilege offers Endpoint Controller-based and No Endpoint Controller-based deployment models. Choosing the right model depends on your organization's priorities for security, ease of deployment, and user experience.

## Endpoint Controller-based model

The Endpoint Controller-based model is recommended for organizations requiring the highest level of device and user identity assurance. In this model, users install the Endpoint Controller on their device. The Endpoint Controller leverages the device's Trusted Platform Module (TPM) to create a strong, hardware-backed identity.

![Diagram showing TPM-secured laptop connecting to PingOne Privilege and gateways to access cloud resources and databases.](_images/p1p_controller_diagram.png)

Key features of this model include:

* Strong device and user identity verification.

* Continuous authorization and session monitoring.

* Enhanced security for sensitive environments.

## No Endpoint Controller-based model

The No Endpoint Controller-based model is ideal for organizations seeking a fast, low-friction rollout, or for environments where the Endpoint Controller can't be installed. Users access resources like Secure Shell (SSH) *(tooltip: \<div class="paragraph">
\<p>Protocol for secure operation of network services over an unsecured network.\</p>
\</div>)*, cloud CLIs, and Kubernetes using the No Endpoint Controller.

![Diagram showing Agentless CLI on laptop connecting to PingOne Privilege to access cloud resources through IaaS CLI and the gateway connected to servers](_images/p1p_no_controller_diagram.png)

Key features of this model include:

* Rapid deployment without the Endpoint Controller.

* Flexibility for organizations with diverse device management policies.

* A phased approach to privileged access management (PAM).

* Some trade-offs in device identity assurance compared to the Endpoint Controller-based model.

---

---
title: Deploying the Endpoint Controller on macOS with Jamf Pro
description: Deploy the Endpoint Controller to managed macOS computers with Jamf Pro for silent installation and automated onboarding.
component: privilege
page_id: privilege:getting-started:deploying-controller-jamf
canonical_url: https://docs.pingidentity.com/privilege/getting-started/deploying-controller-jamf.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 22, 2026
section_ids:
  before-you-begin: Before you begin
  deployment-overview: Deployment overview
  create-configuration-profiles: Create configuration profiles
  create-the-system-extensions-profile: Create the System Extensions profile
  create-the-content-filter-profile: Create the Content Filter profile
  create-the-privacy-preferences-policy-control-profile: Create the Privacy Preferences Policy Control profile
  create-the-onboard-preference-plist: Create the Onboard preference plist
  create-the-policies: Create the policies
  create-the-agent-installation-policy: Create the agent installation policy
  create-the-configuration-creation-policy: Create the configuration-creation policy
  enroll-devices-and-deploy: Enroll devices and deploy
  verify-mdm-onboarding-in-pingone-privilege: Verify MDM onboarding in PingOne Privilege
  verify-the-deployment: Verify the deployment
---

# Deploying the Endpoint Controller on macOS with Jamf Pro

Deploy the Endpoint Controller to managed macOS computers with Jamf Pro to install and configure the Endpoint Controller centrally instead of sending download links to individual users.

The Jamf Pro deployment:

* Installs the PingOne Privilege Endpoint Controller.

* Preapproves the macOS system extensions and full disk access.

* Generates the client configuration that the Endpoint Controller needs to register the device with PingOne Privilege.

|   |                                                                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This guide only applies to [Endpoint Controller-based deployments](choosing-deployment-model.html). After deployment, users open their onboarding link to complete registration and access the PingOne Privilege user console. Learn more in [Onboarding users](onboarding-users.html). |

## Before you begin

Ensure the following:

* You can access the Jamf Pro admin console, and the target computers are enrolled in Jamf Pro.

* You've installed the Endpoint Controller. You need its **Controller URL** and **Tenant ID**.

* You've generated a key pair *(tooltip: \<div class="paragraph">
  \<p>The private key and public key represented by a certificate.\</p>
  \</div>)* for MDM onboarding:

  * You've uploaded the public key *(tooltip: \<div class="paragraph">
    \<p>In public key cryptography, a public key is the part of an asymmetric key pair that the owner shares with others to allow them to decrypt digital signatures or encrypted data.\</p>
    \</div>)* to your PingOne Privilege tenant under **Settings > MDM Onboarding**. Learn more in [Verifying MDM onboarding in PingOne Privilege](#verify-mdm-onboarding).

  * You've added the private key *(tooltip: \<div class="paragraph">
    \<p>In public key cryptography, a private key is the secret part of an asymmetric key pair that is typically used to digitally sign or decrypt data. The private key is kept secret by its owner, similar to a password.\</p>
    \</div>)* in Base64 format to your Jamf portal, typically through an extension attribute.

    |   |                                                                    |
    | - | ------------------------------------------------------------------ |
    |   | PingOne Privilege supports the RSA, ECDSA, and Ed25519 algorithms. |

|   |                                                                                                                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | MDM deployment doesn't replace PingOne group access. A computer can be successfully managed by Jamf Pro and still require its user to belong to a group with access to the PingOne Privilege application. Confirm group access in [Setting up your environment in PingOne](setting-up-environment.html) before you deploy. |

## Deployment overview

You perform most of this deployment in the Jamf Pro admin console. The enrollment and Endpoint Controller verification steps take place on each target Mac, and the MDM onboarding verification takes place in the PingOne Privilege admin console.

Deployment consists of the following tasks:

1. [Create configuration profiles](#create-profiles) to preapprove system extensions, activate the network extension, grant full disk access, and push the onboarding configuration.

2. [Create the policies](#create-policies) for installing the Endpoint Controller and generate the client configuration.

3. [Enroll devices and deploy](#enroll-and-deploy) to trigger automated deployment of the Endpoint Controller.

4. [Verify the deployment](#verify-deployment) of the Endpoint Controller.

## Create configuration profiles[]()

Create the following configuration profiles in Jamf Pro. Each profile uses **Computer Level** as the level and **Install Automatically** as the distribution method.

### Create the System Extensions profile

This profile preapproves the PingOne Privilege system extensions so users aren't prompted in **System Settings**.

1. In Jamf Pro, go to **Computers > Configuration Profiles**.

2. Click **New**.

3. In the **General** section:

   1. Enter a **Name** for the profile, such as `PingOne Privilege System Extensions`.

   2. Set **Level** to **Computer Level**.

   3. Set **Distribution Method** to **Install Automatically**.

4. In the left sidebar, click **System Extensions**, then click **Configure**.

5. Clear the **Allow users to approve system extensions** checkbox.

6. In the **Allowed System Extensions and Teams IDs** section:

   1. Enter a **Display name** for the entry.

   2. In the **System extension types** list, select **Non-removable system extensions**.

   3. In the **Team identifier** field, enter `6U3RF4C84N`.

   4. Under **Non-removable system extensions**, click **Add** and paste `com.pingidentity.AgentLauncher.EndpointSecurity`.

   5. Click **Add** again and paste `com.pingidentity.AgentLauncher.NetworkFilter`.

7. Click **Save**.

### Create the Content Filter profile

This profile activates the network extension.

1. In Jamf Pro, go to **Computers > Configuration Profiles**.

2. Click **New**.

3. In the **General** section:

   1. Enter a **Name** for the profile, such as `PingOne Privilege Content Filter`.

   2. Set **Level** to **Computer Level**.

   3. Set **Distribution Method** to **Install Automatically**.

4. In the left sidebar, click **Content Filter**, then click **Configure**.

   1. Enter a **Filter name**, such as `PingOne Privilege`.

   2. For **Identifier**, enter `com.procyon.ai`

   3. Under **Filter type**, select **Plug-in**.

   4. Under **Socket Filter**, select the **Enabled** checkbox.

   5. For **Socket filter bundle identifier**, enter `com.pingidentity.AgentLauncher.NetworkFilter`

   6. In **Socket filter designated requirement**, paste the following string:

      ```
      identifier "com.pingidentity.AgentLauncher.NetworkFilter" and anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = "6U3RF4C84N"
      ```

5. Click **Save**.

### Create the Privacy Preferences Policy Control profile

This profile grants full disk access to the endpoint security extension, which the Endpoint Controller needs to discover personal agents.

1. In Jamf Pro, go to **Computers > Configuration Profiles**.

2. Click **New**.

3. In the **General** section:

   1. Enter a **Name** for the profile, such as `PingOne Privilege PPPC`.

   2. Set **Level** to **Computer Level**.

   3. Set **Distribution Method** to **Install Automatically**.

4. In the left sidebar, click **Privacy Preferences Policy Control**, then click **Configure**.

5. Under **App Access**, click **Add**.

   1. For **Identifier**, enter `com.pingidentity.AgentLauncher.EndpointSecurity`

   2. Under **Identifier type**, select **Bundle ID**.

   3. In **Code requirement**, paste the following string:

      ```
      identifier "com.pingidentity.AgentLauncher.EndpointSecurity" and anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = "6U3RF4C84N"
      ```

6. In the **App or Service** list, find **SystemPolicyAllFiles** and change the list to **Allow**.

7. Click **Save**.

### Create the Onboard preference plist

This profile pushes the custom configuration variables, such as the tenant ID and user information, to the Mac.

1. In Jamf Pro, go to **Computers > Configuration Profiles**.

2. Click **New**.

3. In the **General** section:

   1. Enter a **Name** for the profile, such as `PingOne Privilege Onboard`.

   2. Set **Level** to **Computer Level**.

   3. Set **Distribution Method** to **Install Automatically**.

4. In the left sidebar, click **Application & Custom Settings**, then click **Configure**.

5. Choose the option to enter Extensible Markup Language (XML) *(tooltip: \<div class="paragraph">
   \<p>A structured, hierarchical text format, based on SGML, for the flexible and organized exchange of data.\</p>
   \</div>)* manually, or upload a PLIST, and paste the following plist, replacing the placeholders with your environment values:

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
     "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
       <key>tenant</key>
       <string>[Insert Tenant ID]</string>

       <key>macuser</key>
       <string>$USERNAME</string>

       <key>privuser</key>
       <string>$USERNAME</string>

       <key>expiryHours</key>
       <string>$EXTENSIONATTRIBUTE_4</string>

       <key>privateKeyBase64</key>
       <string>$EXTENSIONATTRIBUTE_2</string>

       <key>controllerURL</key>
       <string>[Insert Controller URL]</string>
   </dict>
   </plist>
   ```

   |   |                                                                                                                                                                                                                                                              |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | The $EXTENSIONATTRIBUTE\_\* placeholders refer to the Jamf extension attributes that hold the private key in Base64 format and the onboarding expiry, in hours. Adjust the attribute numbers to match the extension attributes in your Jamf Pro environment. |

6. Click **Save**.

## Create the policies[]()

In the Jamf Pro admin console, create the policies that install the Endpoint Controller and build the user's client configuration.

### Create the agent installation policy

This policy installs the Endpoint Controller.

1. In the Jamf Pro admin console, go to **Computers > Policies** and click **New**.

2. In the **General** section:

   1. Enter a **Display name**, such as `PingOne Privilege Agent Install`.

   2. Set **Trigger** to **Custom** and enter `procyon-agent-install` in the text box.

   3. Set **Execution frequency** to **Once per computer**.

3. In the left sidebar, click **Packages**, then click **Configure**.

4. Find the PingOne Privilege `.pkg` file you uploaded to Jamf Pro and click **Add**.

5. Click **Save**.

### Create the configuration-creation policy

This policy is the main deployment policy. It calls the installation policy, waits for the Endpoint Controller to install, and then builds the user's client configuration file.

1. In Jamf Pro, go to **Computers > Policies**.

2. Click **New**.

3. In the **General** section:

   1. Enter a **Display name**, such as `procyon-onboard`.

   2. Select the **Enabled** checkbox.

   3. Set **Trigger** to **Recurring Check-in** (or your preferred deployment trigger).

   4. Set **Execution frequency** to **Once per computer**.

4. In the left sidebar, click **Scripts**, then click **Configure**.

5. Add a new script, set the priority to **After**, and paste the following script:

   ```bash
   #!/bin/sh
   # PingOne Privilege config-creation policy
   # Triggers the agent install policy, then runs until config.json is created.

   LOG=/var/log/pingone-privilege-postinstall.log
   log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG"; }

   APP="/Applications/PingOne Privilege.app"
   APP_BIN="/usr/local/bin/cyononboard"
   PREFS="/Library/Managed Preferences/com.pingidentity.privilege.onboard.plist"

   # Trigger the installation policy
   log "config-policy: calling custom event procyon-agent-install..."
   /usr/local/bin/jamf policy -event procyon-agent-install

   if [ ! -d "$APP" ]; then
       log "config-policy: agent app not installed yet - exiting 1, will retry"
       exit 1
   fi

   CONSOLE_USER=$(/usr/bin/stat -f%Su /dev/console 2>/dev/null)
   if [ -z "$CONSOLE_USER" ]; then
       TARGET_USER=$(/usr/libexec/PlistBuddy -c 'Print :macuser' "$PREFS" 2>/dev/null)
   else
       TARGET_USER=$CONSOLE_USER
   fi

   if [ -z "$TARGET_USER" ]; then
       log "config-policy: no console user and no macuser in profile - exiting 1, will retry"
       exit 1
   fi

   CONFIG="/Users/$TARGET_USER/.config/procyon/config.json"

   if [ -s "$CONFIG" ]; then
       log "config-policy: $CONFIG exists - nothing to do"
       exit 0
   fi

   ATTEMPTS=0
   until "$APP_BIN" >> "$LOG" 2>&1; do
       ATTEMPTS=$((ATTEMPTS + 1))
       log "config-policy: attempt $ATTEMPTS failed (MDM profile may not be installed yet)"
       if [ "$ATTEMPTS" -ge 20 ]; then
           log "config-policy: profile still missing after 20 attempts - exiting 1, Jamf will retry"
           exit 1
       fi
       sleep 30
   done

   if [ -s "$CONFIG" ]; then
       log "config-policy: created $CONFIG for $TARGET_USER"
       exit 0
   fi

   log "config-policy: cyononboard exited 0 but $CONFIG missing - exiting 1, will retry"
   exit 1
   ```

6. Click **Save**.

## Enroll devices and deploy[]()

To trigger the automated deployment on a user's Mac:

1. On the target Mac, go to `https://<your-jamf-instance>.jamfcloud.com/enroll/`.

2. Download and install the MDM profile onto the system.

After the Mac is successfully enrolled, the entire process takes place automatically in the background:

* The configuration profiles are applied.

* The Endpoint Controller is installed.

* The personalized configuration file is securely generated.

On first launch, the Endpoint Controller opens, the extensions activate without prompting for manual approval in **System Settings**, and the users are registered when they open the application.

## Verify MDM onboarding in PingOne Privilege[]()

1. In the PingOne Privilege admin console, go to **Settings**.

2. In the **MDM Onboarding** section, confirm that it displays the public key from the key pair you generated. Computers use this key to enroll and verify with PingOne Privilege.

## Verify the deployment[]()

After Jamf Pro deploys the profiles and policies:

1. In Jamf Pro, confirm that Jamf Pro installed the configuration profiles on the target computers.

2. On a target Mac, confirm that the Endpoint Controller created the client configuration file for the user at `~/.config/procyon/config.json`.

3. On the target Mac, open the Endpoint Controller and confirm the **Connection Status** reports **Connected**.

   |   |                                                                       |
   | - | --------------------------------------------------------------------- |
   |   | The **General** page also displays the tenant and device information. |

|   |                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If the Endpoint Controller displays a QR code, the device isn't registered. Verify that the configuration-creation policy completed successfully, then have the user open the onboarding link again. |

---

---
title: Key concepts
description: Understand the foundational concepts of PingOne Privilege.
component: privilege
page_id: privilege:getting-started:key-concepts
canonical_url: https://docs.pingidentity.com/privilege/getting-started/key-concepts.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 20, 2026
section_ids:
  core-concepts: Core concepts
  deployment-models: Deployment models
  pingone-privilege-products: PingOne Privilege products
  human-privilege-concepts: Human Privilege concepts
  agent-privilege-concepts: Agent Privilege concepts
---

# Key concepts

Learn about the foundational concepts and terms for PingOne Privilege.

## Core concepts

* Privileged access management (PAM)

  PAM is a set of principles and practices to control, monitor, and secure access to critical resources by both human and machine identities. PAM ensures that users have the right-sized permissions to access critical resources, such as infrastructures, applications, or data essential to an organization's operations, and that could cause significant harm if compromised or unavailable.

* Just-in-time access

  PingOne Privilege replaces long-lived, standing privileges with just-in-time (JIT) access: temporary permissions that are granted when needed, expire automatically, and are revoked when they expire. Users request access through the self-service portal, or policies grant it, and every grant is time-bound and auditable.

* Trusted Platform Module (TPM) and Secure Enclave

  Modern Windows and Mac laptops include hardware-based security features like the TPM chip or Apple's Secure Enclave. These provide a secure, tamper-resistant location for storing private keys, offering stronger security than file-based credentials because the keys can't be directly read or extracted.

## Deployment models

PingOne Privilege offers Endpoint Controller-based and No Endpoint Controller-based deployment models. In the Endpoint Controller-based model, users install the Endpoint Controller on their device for hardware-backed identity assurance. In the No Endpoint Controller-based model, users authenticate through PingOne SSO without installing the Endpoint Controller.

* Endpoint Controller

  The Endpoint Controller, installed during setup, creates, and stores a non-exportable private key in the device's TPM or Secure Enclave. The Endpoint Controller uses this key to establish a secure mutual TLS (mTLS) connection with PingOne Privilege, which verifies the identity of both the user and the device.

  The Endpoint Controller also serves Agent Privilege by hosting the sensors that report personal agent discovery findings from managed devices.

* No Endpoint Controller

  For situations where the Endpoint Controller can't be installed, the No Endpoint Controller provides secure access to resources like SSH, cloud CLIs, and Kubernetes. When a user authenticates through the No Endpoint Controller, they're redirected to PingOne SSO for authentication. After successful authentication, the user can access resources based on their permissions.

Learn more in [Choosing a deployment model](choosing-deployment-model.html).

## PingOne Privilege products

PingOne Privilege includes two complementary products with their own unique concepts.

### Human Privilege concepts

* Gateways

  Gateways are entry points for accessing resources on a private network. The Endpoint Controller connects to a private proxy to establish a secure session, and the Endpoint Controller determines the optimal gateway path between the user and the resource. Relays extend gateways to networks that don't allow inbound connections.

  Learn more in [Configuring gateways](../human-privilege/configuration/gateways/index.html).

* Access protocols

  Human Privilege secures access to resources through industry-standard protocols: certificate-based SSH for Linux servers, with short-lived certificates issued per session, and RDP for Windows servers, with sessions managed and audited through PingOne Privilege.

  Learn more in [Access protocols](../human-privilege/configuration/access-protocols/index.html).

### Agent Privilege concepts

* AI gateway

  The AI gateway is the enforcement point for agent traffic. Agent credentials and tokens are validated and terminate at the gateway and are never forwarded to backend services. At each request, the gateway injects the credential needed for the resource being accessed. The gateway hosts MCP Gateway, LLM Gateway and AI Guard functionality. Learn more in [AI gateways](../agent-privilege/configuration/ai-gateways.html).

* Agentic Apps

  Agentic Apps are the applications agents reach through PingOne Privilege: MCP Server, MCP Aggregate, OpenAPI MCP, and Remote Agent applications, integrations from the MCP Catalog, and Git Servers. Each application is associated with an AI gateway that enforces policy on the agent's traffic.

  Learn more in [Agentic apps](../agent-privilege/configuration/agentic-apps/index.html).

* AI Guard

  AI Guard inspects agent traffic across MCP, A2A, and LLM connections for threats such as prompt injection, data exfiltration, and tool abuse, and enforces allow, alert, sanitize, or block responses for each detection.

  Learn more in [Agent registry](../agent-privilege/configuration/agent-registry.html)

* {p1priv-ai-discovery}

  {p1priv-ai-discovery} builds an inventory of the AI in your organization. Personal agent discovery observes the agents users run on their devices and browsers. Workload agent discovery inventories the agents in your cloud platforms. NHI discovery finds the agents, LLMs, and MCP servers deployed in Kubernetes clusters and on Docker hosts.

  Learn more in [Workload agents](../agent-privilege/use-cases/workload-agents.html), [Personal agents](../agent-privilege/use-cases/personal-agents.html), and [Discover and manage NHI agents](../agent-privilege/use-cases/nhi-agents.html)

---

---
title: Onboarding users
description: This topic describes how organization administrators can onboard users to the PingOne Privilege user console.
component: privilege
page_id: privilege:getting-started:onboarding-users
canonical_url: https://docs.pingidentity.com/privilege/getting-started/onboarding-users.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 8, 2026
section_ids:
  onboarding-users-in-endpoint-controller-based-deployments: Onboarding users in Endpoint Controller-based deployments
  agent-mdm-distribution: Deploying the Endpoint Controller with an MDM platform
  onboarding-users-in-no-endpoint-controller-based-deployments: Onboarding users in No Endpoint Controller-based deployments
---

# Onboarding users

How admins onboard users to PingOne Privilege depends on the [deployment model](choosing-deployment-model.html) your organization uses. The process involves sending a link to users so they can access the user console.

|   |                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Before you onboard a user, the user must belong to a group that has access to the PingOne Privilege application in PingOne. For more information, see [Setting up your environment in PingOne](setting-up-environment.html). |

## Onboarding users in Endpoint Controller-based deployments

For Endpoint Controller-based deployment models, users must first install the Endpoint Controller. You can onboard users by sending them the Endpoint Controller download link:

1. In the PingOne admin console, open the navigation menu in the upper-right corner. Select **Settings**.

2. Click the **App Downloads** tab.

   ![A screenshot showing the App Downloads tab with the Desktop Applications section visible.](_images/p1p_controller_download.png)

3. On the **Privilege App** tile, select the appropriate operating system for the user.

4. Copy the download link.

5. Send the download link to the user, along with the user's onboarding link.

The user installs the Endpoint Controller, then opens the onboarding link to register their device and access the user console. You generate onboarding links in the PingOne admin console. Learn more in [Accessing the PingOne Privilege admin console as an administrator](accessing-admin-console.html).

|   |                                                                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To install the Endpoint Controller on many devices at once, distribute it with your Mobile Device Management (MDM) platform, such as Jamf Pro or Intune. For more information, see [Deploying the Endpoint Controller with an MDM platform](#agent-mdm-distribution). |

### Deploying the Endpoint Controller with an MDM platform

Sending download links works for small teams, but doesn't scale to organization-wide rollouts. If you manage many devices, deploy the Endpoint Controller with your organization's Mobile Device Management (MDM) platform instead. MDM deployment applies to Endpoint Controller-based deployments only.

Follow the steps for your platform:

* [Deploying the Endpoint Controller on macOS with Jamf Pro](deploying-controller-jamf.html)

You'll configure the operating-system permissions, install the Endpoint Controller, and apply the PingOne Privilege onboarding configuration. After deployment, users complete the required registration steps by opening their onboarding link.

|   |                                                                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | MDM deployment doesn't replace PingOne group access. Before you deploy, confirm that your users belong to a group with access to the PingOne Privilege application. Learn more in [Setting up your environment in PingOne](setting-up-environment.html). |

## Onboarding users in No Endpoint Controller-based deployments

For No Endpoint Controller-based deployment models, users install the No Endpoint Controller, then open the onboarding link to access the user console. You generate onboarding links in the PingOne admin console. Learn more in [Accessing the PingOne Privilege admin console as an administrator](accessing-admin-console.html).

1. In the PingOne admin console, open the navigation menu in the upper-right corner. Select **Settings**.

2. Click the **App Downloads** tab.

   ![A screenshot showing the App Downloads tab with the Agentless CLI section visible.](_images/p1p_agentless_cli_download.png)

3. On the **Agentless CLI** tile, select the appropriate operating system for the user.

4. Copy the download link.

5. Send the download link to the user, along with the user's onboarding link.

---

---
title: Setting up your environment in PingOne
description: This topic guides administrators through the process of setting up a new environment for PingOne Privilege.
component: privilege
page_id: privilege:getting-started:setting-up-environment
canonical_url: https://docs.pingidentity.com/privilege/getting-started/setting-up-environment.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 5, 2026
section_ids:
  before-you-begin: Before you begin
  step-1-add-the-pingone-privilege-service: "Step 1: Add the PingOne Privilege service"
  step-2-create-and-configure-user-groups: "Step 2: Create and configure user groups"
  step-3-grant-access-to-groups: "Step 3: Grant access to groups"
  step-4-assign-roles-and-add-users-to-the-administrator-group: "Step 4: Assign roles and add users to the administrator group"
---

# Setting up your environment in PingOne

This topic guides administrators through setting up a new environment for PingOne Privilege, which is the first step to enabling secure, centralized privileged access management (PAM) for your organization.

## Before you begin

* You must have access to the PingOne admin console.

* Your account must have the following administrator roles assigned for the initial setup: **Identity Data Admin**, **PingOne Privilege Administrator**, and **Application Owner**.

* You need a PingOne environment and a solution built with PingOne SSO. Learn more in [Building solutions](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_building_solutions.html) in the PingOne documentation.

* (Optional) In Endpoint Controller-based models, you can also add PingID to your environment to require multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
  \<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
  \</div>)* when users connect through the Endpoint Controller. Learn more in [Requiring PingID Workforce Authentication for PingOne Privilege app connections](../human-privilege/configuration/multi-factor-authentication/pingid-mfa-app-connect.html).

## Step 1: Add the PingOne Privilege service

First, add the PingOne Privilege service to your PingOne environment. Learn more in [Adding a service to an environment](https://docs.pingidentity.com/pingone/settings/p1_add_a_service.html) in the PingOne documentation.

1. In the PingOne admin console, go to **Overview**.

2. In the **Services** section, click the **[icon: plus, set=fa]**icon.

3. In the **Add a Service** list, select **PingOne Privilege**.

   ![A screenshot showing the Add a Service list with p1privilege selected.](_images/p1p_add_privilege.png)

4. Select the **Authentication Mode**.

   |   |                                                                                                                                                                                                                                                                                                                                                                      |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The authentication mode determines how you deploy PingOne Privilege and how users authenticate.- For No Endpoint Controller-based deployments, users authenticate through PingOne SSO.

   - For Endpoint Controller-based deployments, users authenticate through the Endpoint Controller.Learn more in [Choosing a deployment model](choosing-deployment-model.html). |

5. Click **Finish**.

## Step 2: Create and configure user groups

Next, create the groups that need access to PingOne Privilege and grant them access to the application. Learn more in [Managing groups](https://docs.pingidentity.com/pingone/directory/p1_managing_groups.html) in the PingOne documentation.

1. In the PingOne admin console, go to **Directory > Groups**.

2. Click the **[icon: plus, set=fa]**icon and create the following groups:

   * `Privilege Admins` for PingOne Privilege administrators.

   * `Privilege Users` for users who access resources through PingOne Privilege.

3. Click **Save**.

## Step 3: Grant access to groups

Users can only access PingOne Privilege if they belong to a group that has access to the PingOne Privilege application.

1. In the PingOne admin console, go to **Applications > Applications**.

2. In the list, click the **PingOne Privilege** application.

3. In the **Access** tab, click the **Pencil** ([icon: pencil, set=fa]) icon.

4. Select the PingOne Privilege groups that need access.

5. Click **Save**.

## Step 4: Assign roles and add users to the administrator group

Finally, add users to the administrator group and assign them the necessary roles. Learn more in [Managing administrator roles](https://docs.pingidentity.com//pingone/getting_started_with_pingone/p1_manage_admin_roles.html) in the PingOne documentation.

1. In the PingOne admin console, go to **Directory > Users**.

2. Select a user to be a PingOne Privilege administrator.

3. In the user's profile, go to the **Groups** tab and add the user to the PingOne Privilege administrator group you created.

4. Go to the **Roles** tab and assign the following roles to the user:

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The following roles are required for the initial setup of PingOne Privilege:- **PingOne Privilege Administrator**: Required to create onboarding links and manage PingOne Privilege resources. Assign this role to the administrator group, for example, `Privilege Admins`, or to individual administrators.

   - **Identity Data Administrator**: Required to manage users and groups in the directory.

   - **Application Owner**: Required to grant application access to groups. |

5. Click **Save**.

6. Repeat these steps for each user who needs to be a PingOne Privilege administrator.

---

---
title: Start here
description: Get started with PingOne Privilege.
component: privilege
page_id: privilege:getting-started:start-here
canonical_url: https://docs.pingidentity.com/privilege/getting-started/start-here.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 8, 2026
keywords: ["Getting started"]
---

# Start here

This guide provides the steps for administrators to set up and access PingOne Privilege.

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

[icon: hand-pointer, set=far, size=3x]

#### [Task 5: Use PingOne Privilege](use-privilege.html)

Learn how administrators and users work with Human Privilege and Agent Privilege.

---

---
title: Use PingOne Privilege
description: Learn how administrators and users work with Human Privilege and Agent Privilege after setup.
component: privilege
page_id: privilege:getting-started:use-privilege
canonical_url: https://docs.pingidentity.com/privilege/getting-started/use-privilege.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 10, 2026
section_ids:
  choose-your-path: Choose your path
---

# Use PingOne Privilege

PingOne Privilege includes two complementary products, and how you use it depends on which one you're securing:

* [Human Privilege](../human-privilege/getting-started.html) secures human access to servers, databases, Kubernetes clusters, and cloud consoles and CLIs. Administrators manage directory entries, access policies, and activity monitoring, while users request access to resources, manage access requests, manage their devices, and view their activity.

* [Agent Privilege](../agent-privilege/what-is-agent-privilege.html) secures AI agents acting on behalf of your users, covering personal agents such as coding assistants, workload agents, and non-human identities that reach agentic apps, LLM providers, and Git repositories.

## Choose your path

If you're securing human access:

* Learn the basics in [What is Human Privilege?](../human-privilege/what-is-human-privilege.html)

* Review [Getting started with Human Privilege](../human-privilege/getting-started.html) for setup tasks.

* Follow the guide in [Configuring Human Privilege](../human-privilege/configuration/index.html) for tailoring Human Privilege to your needs.

* Learn how to use Human Privilege by reviewing the [Admin use cases](../human-privilege/admin-use-cases/index.html) and [User use cases](../human-privilege/user-use-cases/index.html).

* Check out the common [Integrations](../integrations/index.html) PingOne Privilege offers to connect with the services your teams already use.

If you're securing AI agents:

* Learn the basics in [What is Agent Privilege?](../agent-privilege/what-is-agent-privilege.html)

* Review [Getting started with Agent Privilege](../agent-privilege/getting-started/index.html) for setup tasks.

* Follow the guide in [Configuring Agent Privilege](../agent-privilege/index.html) to tailor Agent Privilege to your needs.

* Learn how to use Agent Privilege by reviewing the [Agent Privilege use cases](../agent-privilege/use-cases/index.html).

* Check out the common [Integrations](../integrations/index.html) PingOne Privilege offers to connect with the services your teams already use.

---

---
title: What is PingOne Privilege?
description: PingOne Privilege provides secure, passwordless, just-in-time access to cloud infrastructure for people, and secures the AI agents acting on their behalf.
component: privilege
page_id: privilege:getting-started:introduction
canonical_url: https://docs.pingidentity.com/privilege/getting-started/introduction.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 10, 2026
---

# What is PingOne Privilege?

PingOne Privilege is a unified privileged-access solution for securing both human and AI-driven work. PingOne Privilege improves security by leveraging just-in-time (JIT) access to replace long-standing credentials and secrets with dynamic, targeted permissions that are revoked when they expire.

PingOne Privilege includes two complementary products:

* [Human Privilege](../human-privilege/what-is-human-privilege.html): Provides administrators and developers with policy-based, secretless, just-in-time access to servers, databases, Kubernetes clusters, cloud accounts, and other privileged resources.

  ![Overview of how human privilege works showing different users accessing cloud resources through the product](_images/p1p_human_privilege_diagram.png)

* [Agent Privilege](../agent-privilege/what-is-agent-privilege.html): Discovers and manages personal and workload agents as they access models, tools, APIs, MCP, and A2A connections, applying the same policy-based control and auditability to agent activity.

  ![Overview of how agent privilege works showing different users accessing resources through the AI Gateway](_images/p1p_agent_privilege_diagram.png)

|   |                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Agent Privilege and Human Privilege each have their own getting started, configuration, and use cases guides, so you can find everything relevant to your product in one place. |