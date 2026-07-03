---
title: Additional reference
description: The subsequent sections explore additional features of Enterprise Connect Windows RADIUS proxy:
component: enterprise-connect
version: latest
page_id: enterprise-connect:windows-radius-proxy-3.0.2:radius-additional-reference
canonical_url: https://docs.pingidentity.com/enterprise-connect/latest/windows-radius-proxy-3.0.2/radius-additional-reference.html
---

# Additional reference

The subsequent sections explore additional features of Enterprise Connect Windows RADIUS proxy:

* [Configure Linux SSH to use Enterprise Connect Windows RADIUS proxy for MFA](configure-ssh-linux-pam.html)

* [Uninstall Enterprise Connect Windows RADIUS proxy](uninstalling-radius-proxy.html)

* [Log files with Enterprise Connect Windows RADIUS proxy](logging.html)

---

---
title: Additional reference
description: The subsequent sections explore additional features of Enterprise Connect Mac Workstation Authentication:
component: enterprise-connect
version: latest
page_id: enterprise-connect:workstation-mac-guide-3.0.3:mac-additional-reference
canonical_url: https://docs.pingidentity.com/enterprise-connect/latest/workstation-mac-guide-3.0.3/mac-additional-reference.html
---

# Additional reference

The subsequent sections explore additional features of Enterprise Connect Mac Workstation Authentication:

* [Perform Enterprise Connect Mac Workstation Authentication upgrade](performing-mac-upgrade.html)

* [Log files](logging.html)

* [Modify Enterprise Connect Mac Workstation Authentication](modify-mac-client.html)

---

---
title: Additional reference
description: The subsequent sections explore additional uses of the Enterprise Connect Windows Workstation Authentication.
component: enterprise-connect
version: latest
page_id: enterprise-connect:workstation-windows-guide-3.7.2.7293:windows-additional-reference
canonical_url: https://docs.pingidentity.com/enterprise-connect/latest/workstation-windows-guide-3.7.2.7293/windows-additional-reference.html
---

# Additional reference

The subsequent sections explore additional uses of the Enterprise Connect Windows Workstation Authentication.

Enterprise Connect Windows Workstation Authentication installation/configuration checklist

* [icon: check-square-o, set=fa]Download and install the binaries from [Backstage](https://backstage.forgerock.com/downloads/browse/ig/all/productId:enterprise-connect) (you must be logged in). This includes the base MSI file as well as the MSI Updater client.

* [icon: check-square-o, set=fa]Pre-configure the relevant [journey(s)](creating-authentication-journey.html).

* [icon: check-square-o, set=fa][Install](installing-windows-msiupdater.html) the MSI Updater client on an administrative Windows machine.

* [icon: check-square-o, set=fa][Configure](configuring-windows-msiupdater.html) the MSI Updater client specific to your organization's needs.

* [icon: check-square-o, set=fa]\(Optional) Consider [additional configurations](windows-additional-reference.html).

* [icon: square-o, set=fa]*[Deploy](deploying-msi.html#msi_deployment_of_workstation_authentication) the generated MSI file through your desired mechanism.*

* [icon: square-o, set=fa][Verify and test](verify-windows-authentication.html) your deployment.

---

---
title: Changelog
description: Review the release notes in Ping Enterprise Connect Passwordless software.
component: enterprise-connect
version: latest
page_id: enterprise-connect:release-notes:passwordless/ec-passwordless-changelog
canonical_url: https://docs.pingidentity.com/enterprise-connect/latest/release-notes/passwordless/ec-passwordless-changelog.html
section_ids:
  latest: Latest
  2026_january: 2026 January
  2025_april: 2025 April
  2023_september: 2023 September
  2023_may: 2023 May
---

# Changelog

Review the release notes in Ping Enterprise Connect Passwordless software.

Subscribe to get automatic updates: [icon: rss-square, set=fa][Ping Enterprise Connect Passwordless changelog RSS feed](../../release-notes/passwordless/ec-passwordless-changelog.xml)

## Latest

### 2026 January

Initial release of Ping Enterprise Connect Passwordless 6.8

* SSA-17134: Report templates

* SSA-17395/SSA-17400: Microsoft Office 365 federation for Entra ID

* SSA-36/SSA-17222: OpenID Connect service

* SSA-16968: PingID mobile app plugin

* SSA-17071: `externalSsoUrl` custom parameter for SAML

* SSA-17393: FIDO metadata update

### 2025 April

Initial release of Ping Enterprise Connect Passwordless 5.8.2.

### 2023 September

Initial release of Ping Enterprise Connect Passwordless 5.4.8

* SSA-11986: Sign-on failures when working with many machine types, such as Windows and Macs

* SSA-11972: Nginx pool size and database connection issues

* SSA-11537: Ping Identity journey session not captured during authentication flow

### 2023 May

Initial release of Ping Enterprise Connect Passwordless 5.4.4.

---

---
title: Changelog
description: Review the release notes in Ping Enterprise Connect Passwordless Mac Agent software.
component: enterprise-connect
version: latest
page_id: enterprise-connect:release-notes:passwordless-mac/ec-passwordless-mac-changelog
canonical_url: https://docs.pingidentity.com/enterprise-connect/latest/release-notes/passwordless-mac/ec-passwordless-mac-changelog.html
section_ids:
  latest: Latest
  2026_january: 2026 January
  new_features: New features
  2024_april: 2024 April
  fixes: Fixes
  2023_september: 2023 September
  fixes_2: Fixes
---

# Changelog

Review the release notes in Ping Enterprise Connect Passwordless Mac Agent software.

Subscribe to get automatic updates: [icon: rss-square, set=fa][Ping Enterprise Connect Passwordless Mac agent changelog RSS feed](../../release-notes/passwordless-mac/ec-passwordless-mac-changelog.xml)

## Latest

### 2026 January

Initial release of Enterprise Connect Passwordless Mac Agent 4.3.

#### New features

* SSA-18562: Enterprise Connect Passwordless Mac Agent features a custom sign-on screen that enables users to select their preferred authentication method. The option to sign on with the username and password is also provided.

### 2024 April

Initial release of Enterprise Connect Passwordless Mac Agent 2.7.1.

#### Fixes

* SSA-13862: FIDO authentication setup fails when users are enabled with FIDO as the first and only authenticator

### 2023 September

Initial release of Enterprise Connect Passwordless Mac Agent 2.6.7.

#### Fixes

* SSA-11701: Agent conﬂict with CyberArk EPM Agent

* SSA-12259: FileVault set up fails for a second user on the same machine

* SSA-11915: FileVault password operation fails in rare instances

---

---
title: Changelog
description: Review the release notes in Ping Enterprise Connect Passwordless Windows Agent software.
component: enterprise-connect
version: latest
page_id: enterprise-connect:release-notes:passwordless-windows/ec-passwordless-windows-changelog
canonical_url: https://docs.pingidentity.com/enterprise-connect/latest/release-notes/passwordless-windows/ec-passwordless-windows-changelog.html
section_ids:
  latest: Latest
  2026_january: 2026 January
  new_features: New features
  2024_april: 2024 April
  fixes: Fixes
  2023_september: 2023 September
  fixes_2: Fixes
  2023_may: 2023 May
---

# Changelog

Review the release notes in Ping Enterprise Connect Passwordless Windows Agent software.

Subscribe to get automatic updates: [icon: rss-square, set=fa][Ping Enterprise Connect Passwordless Windows agent changelog RSS feed](../../release-notes/passwordless-windows/ec-passwordless-windows-changelog.xml)

## Latest

### 2026 January

Initial release of Enterprise Connect Passwordless Windows Agent 4.3.1.

#### New features

* Passwordless authentication support.

### 2024 April

Initial release of Enterprise Connect Passwordless Windows Agent 3.9.3.

#### Fixes

* SSA-12158: In certain circumstances, the SSO portal launches in a browser with maximum user privileges

* SSA-12709: When performing RDP authentication, Network Login Type is logged as Interactive Login Type

* SSA-12400: Smart card authentication failure following an offline reboot

* SSA-13408: Incorrect text for shared account sign on for first interaction

* SSA-13446: Authentication failures related to FIDO PIN length

* SSA-13948: Systray app not executed automatically following MSI installation

### 2023 September

Initial release of Enterprise Connect Passwordless Windows Agent 3.8.4.

#### Fixes

* SSA-11445: When you enable Enforce Adaptive Authentication, offline sign on with BLE succeeds only after two online sign ons

### 2023 May

Initial release of Enterprise Connect Passwordless Windows Agent 3.8.2.

---

---
title: Changelog
description: Review the release notes in Ping Enterprise Connect Windows RADIUS proxy software.
component: enterprise-connect
version: latest
page_id: enterprise-connect:release-notes:windows-radius/ec-windows-radius-changelog
canonical_url: https://docs.pingidentity.com/enterprise-connect/latest/release-notes/windows-radius/ec-windows-radius-changelog.html
section_ids:
  latest: Latest
  2025_january: 2025 January
  2022_september: 2022 September
---

# Changelog

Review the release notes in Ping Enterprise Connect Windows RADIUS proxy software.

Subscribe to get automatic updates: [icon: rss-square, set=fa][Ping Enterprise Connect Windows Radius changelog RSS feed](../../release-notes/windows-radius/ec-windows-radius-changelog.xml)

## Latest

### 2025 January

Initial release of Enterprise Connect Windows RADIUS proxy 3.0.2.

### 2022 September

Initial release of Enterprise Connect Windows RADIUS proxy 2.7.1.

---

---
title: Changelog
description: Review the release notes in Ping Enterprise Connect Mac Workstation Authentication software.
component: enterprise-connect
version: latest
page_id: enterprise-connect:release-notes:workstation-mac/ec-workstation-mac-changelog
canonical_url: https://docs.pingidentity.com/enterprise-connect/latest/release-notes/workstation-mac/ec-workstation-mac-changelog.html
section_ids:
  latest: Latest
  2025_january: 2025 January
  2023_april: 2023 April
---

# Changelog

Review the release notes in Ping Enterprise Connect Mac Workstation Authentication software.

Subscribe to get automatic updates: [icon: rss-square, set=fa][Ping Enterprise Connect Mac Workstation changelog RSS feed](../../release-notes/workstation-mac/ec-workstation-mac-changelog.xml)

## Latest

### 2025 January

Initial release of Enterprise Connect Mac Workstation Authentication 3.0.3.

### 2023 April

Initial release of Enterprise Connect Mac Workstation Authentication 2.7.2.

---

---
title: Changelog
description: Review the release notes in Ping Enterprise Connect Windows Workstation Authentication software.
component: enterprise-connect
version: latest
page_id: enterprise-connect:release-notes:workstation-windows/ec-workstation-windows-changelog
canonical_url: https://docs.pingidentity.com/enterprise-connect/latest/release-notes/workstation-windows/ec-workstation-windows-changelog.html
section_ids:
  latest: Latest
  2025_january: 2025 January
  2022_september: 2022 September
---

# Changelog

Review the release notes in Ping Enterprise Connect Windows Workstation Authentication software.

Subscribe to get automatic updates: [icon: rss-square, set=fa][Ping Enterprise Connect Windows Workstation changelog RSS feed](../../release-notes/workstation-windows/ec-workstation-windows-changelog.xml)

## Latest

### 2025 January

Updated the release of Enterprise Connect Windows Workstation Authentication 3.7.2.7293 with Ping branding.

### 2022 September

Initial release of Enterprise Connect Windows Workstation Authentication 3.7.2 with Ping branding. Updated the version number to 3.7.2.7291.

---

---
title: Configure Linux SSH to use Enterprise Connect Windows RADIUS proxy for MFA
description: With the Enterprise Connect Windows RADIUS proxy installed and configured on a Windows machine, you're ready to add MFA to an SSH login on Linux.
component: enterprise-connect
version: latest
page_id: enterprise-connect:windows-radius-proxy-3.0.2:configure-ssh-linux-pam
canonical_url: https://docs.pingidentity.com/enterprise-connect/latest/windows-radius-proxy-3.0.2/configure-ssh-linux-pam.html
section_ids:
  prerequisites: Prerequisites
  install-required-packages: Install required packages
  configure-pam-radius: Configure PAM RADIUS
  configure-ssh-daemon: Configure SSH Daemon
  verify-test-functionality: Verify and test functionality
  add_a_linux_user: Add a Linux user
  perform_ssh_login: Perform SSH login
---

# Configure Linux SSH to use Enterprise Connect Windows RADIUS proxy for MFA

With the Enterprise Connect Windows RADIUS proxy installed and configured on a Windows machine, you're ready to add MFA to an SSH login on Linux.

This use case is explored in this section.

|   |                                                                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The subsequent sections and examples utilize the Red Hat Enterprise Linux (RHEL) distribution. The commands can vary slightly. For example, RHEL uses `yum` to install packages while the Debian Linux distribution uses `apt`.The following subsections assume you're logged into the Linux terminal as the **root** user or equivalent. |

## Prerequisites

Before setting up the SSH sign on to use MFA on a Linux machine using the Enterprise Connect Windows RADIUS proxy, you must:

* [Install](installing-windows-radius-proxy.html) the Enterprise Connect Windows RADIUS proxy.

* [Validate and test](post-installation-steps.html) the Enterprise Connect Windows RADIUS proxy.

* Establish network connectivity between the Linux machine(s) and the Windows machine(s).

* Confirm all usernames (profiles and accounts) match from the *Linux machine(s)> Ping Identity* and vice versa.

  * Set up a connector from Ping Identity to the datastore and sync the data.

  * The Ping Identity journey validates the credentials when you configure MFA on an SSH login for Linux.

* Confirm users pre-register in the appropriate journey if required. For example, for the push MFA method, users download the PingID mobile app. Learn more in [Enterprise Connect Windows RADIUS proxy prerequisites](prereqs.html).

|   |                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------- |
|   | Ensure you properly patch, lock down, and harden the Linux machine(s) you expose to the Enterprise Connect Windows RADIUS proxy. |

## Install required packages

Packages are required to install relevant RADIUS configurations.

1. Install the EPEL release by running the following command:

   ```bash
   sudo yum install epel-release
   ```

2. Install the PAM RADIUS client by running the following command:

   ```bash
   sudo yum install pam_radius.x86_64
   ```

3. Using an RPM command, verify that the installations were successful.

   |   |                                                                                                                                                                                                                                           |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If any of the install commands return aren't found by the package manager, locate the appropriate package name using an internet search because the install commands are subject to change slightly depending on your Linux distribution. |

## Configure PAM RADIUS

After you install the [required](#install-required-packages) packages (which installs the PAM RADIUS), you must configure the PAM RADIUS module.

1. Edit the `/etc/pam_radius.conf` file (using vim or an equivalent text editor).

2. In the file, remove all entries below the `127.0.0.1` entry, under the table `# server[:port] shared_secret timeout (s)`.

3. Add an entry using the syntax `<WindowsRADIUSProxyIPAddress>:<portOfProxy> <Windows RADIUS Secret> <timeoutInSeconds>`.

   ![Linux PAM RADIUS configuration](../_images/windows-radius-proxy/linux-radius-pam-config.png)Figure 1. Linux PAM RADIUS configuration

## Configure SSH Daemon

After the PAM RADIUS configurations are complete, the `sshd` configuration must be updated to utilize the RADIUS settings on SSH login.

1. Edit the `/etc/pam.d/sshd` file (using vim or an equivalent text editor).

2. Add the following line to the top of the file:

   ```bash
   auth required /usr/lib64/security/pam_radius_auth.so
   ```

   For authentication, this line instructs Linux to use the PAM RADIUS configurations. It requires the authentication service to enforce users to sign on using the Enterprise Connect Windows RADIUS proxy. Learn more in RHEL's [documentation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/managing_smart_cards/pam_configuration_files).

3. Save changes and exit the file.

4. Restart the `sshd` service:

   ```bash
   sudo systemctl restart sshd.service
   ```

|   |                                                                                                                                                                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Verify these changes with a test user and machine before applying them to your environments. Ensure the selected MFA method (defined in [Install Enterprise Connect Windows RADIUS proxy](installing-windows-radius-proxy.html#install_the_ping_radius_proxy)) works with the test user.Failure to confirm this successfully can result in users being locked out of the Linux machine(s). |

## Verify and test functionality

With the Enterprise Connect Windows RADIUS proxy installed and tested, the required packages installed on the Linux machines, and relevant configuration changes to PAM RADIUS and the SSH Daemon, you're ready to verify and test SSH sign on with a user.

|   |                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------- |
|   | Ensure the user you test in your Linux environment matches what is in your Ping Identity environment. |

### Add a Linux user

To add a user on a Linux machine:

1. Create the user:

   `adduser <username>`

2. Modify the password of the newly created user:

   `passwd <username>`

   You will be prompted to enter and re-enter the password of the user.

   |   |                                                                                                                                                        |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Create the user in your Ping Identity environment with the same username and password for testing. In a production scenario, syncing should be set up. |

### Perform SSH login

After you create a test user in the Linux environment with an equivalent account in the Ping Identity environment, you're ready to perform an SSH sign on test. The following steps assume the push MFA method was configured in the Enterprise Connect Windows RADIUS proxy setup.

1. Initiate an SSH connection to the target Linux machine.

2. Enter the username and password as prompted. A push notification should appear on your phone.

3. Tap Approve on the PingID mobile app.

4. Verify that you have successfully logged into the Linux terminal with a valid session.

---

---
title: Configure the management console
description: Use the management console (MC) to centrally manage settings, devices, and users for Enterprise Connect Passwordless.
component: enterprise-connect
version: latest
page_id: enterprise-connect:passwordless-servers:configure-mgmt-console
canonical_url: https://docs.pingidentity.com/enterprise-connect/latest/passwordless-servers/configure-mgmt-console.html
section_ids:
  guides: Guides
---

# Configure the management console

Use the management console (MC) to centrally manage settings, devices, and users for Enterprise Connect Passwordless.

|   |                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------- |
|   | Learn more about installing the management console server in [Install Enterprise Connect Passwordless Servers](install-servers.html). |

![mc server overview](../_images/ec-passwordless/mc-server-overview.png)

It enables you to configure and manage:

* System settings: Enables you to view and update system configuration settings, such as authenticators, mail server settings, and more.

* Directories: Allows you to integrate corporate directories with the system and configure settings for each directory.

* Manage users: Lists your users according to their associated directories and enables you to add, remove, and perform other administrative actions on users.

* Devices: Lists the workstations in the system, provides detailed information about them and allows you to perform administrative operations on them.

* Services: Lists the services integrated with the MC and enables you to add and update services.

* Portal: Allows you to control settings for the user portal.

* Auditing: Displays a log of every administrative action performed by the system or by users.

## Guides

For configuration instructions of the MC, refer to the following table:

| Version                                      | PDF                                                                                                 |
| -------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Enterprise Connect Passwordless Server 6.8   | [6.8 Management Console Admin guide](../_attachments/admin_ec_passwordless_mgmt_server_6.8.pdf)     |
| Enterprise Connect Passwordless Server 5.8.2 | [5.8.2 Management Console Admin guide](../_attachments/admin_ec_passwordless_mgmt_server_5.8.2.pdf) |
| Enterprise Connect Passwordless Server 5.4.8 | [5.4.8 Management Console Admin guide](../_attachments/admin_ec_passwordless_mgmt_server_5.4.8.pdf) |
| Enterprise Connect Passwordless Server 5.4.4 | [5.4.4 Management Console Admin guide](../_attachments/admin_ec_passwordless_mgmt_server_5.4.4.pdf) |

---

---
title: Configure the MSI Updater client
description: The MSI Updater client can launch automatically (if the option is selected at the last installation screen) after you exit the installer and updates the Enterprise Connect Windows Workstation Authentication MSI with relevant Ping Identity environment details. You can then configure various settings related to authentication and the Windows login experience.
component: enterprise-connect
version: latest
page_id: enterprise-connect:workstation-windows-guide-3.7.2.7293:configuring-windows-msiupdater
canonical_url: https://docs.pingidentity.com/enterprise-connect/latest/workstation-windows-guide-3.7.2.7293/configuring-windows-msiupdater.html
---

# Configure the MSI Updater client

The MSI Updater client can launch automatically (if the option is selected at the last installation screen) after you exit the installer and updates the Enterprise Connect Windows Workstation Authentication MSI with relevant Ping Identity environment details. You can then configure various settings related to authentication and the Windows login experience.

Before you begin working with the MSI Updater, verify the following information is available:

* **Server URL:** Environment URL for the Ping Identity environment.

* **Realm:** The realm in Ping Identity that corresponds to where the journeys reside.

* **Push journey name:** Name of the journey for push notifications. Learn more in [Example of push journey](creating-authentication-journey.html#example_push_journey).

* **OTP journey Name:** Name of the journey for TOTPs (OATH). Learn more in [Example of OTP journey](creating-authentication-journey.html#example_otp_journey).

* **SMS/email/voice journey name:** Name of the journey for SMS/email/voice. Learn more in [Example of SMS/email journey](creating-authentication-journey.html#example_sms_email_journey).

* **SSO URL (optional):** Ping Identity SSO URL. If enabled and supplied, on successful login to the Windows machine, the default browser opens a logged-in session into the specified Ping Identity environment.

  * With this URL, an additional journey can be referenced. For example, to check for an existing session. Learn more in [Example of SSO journey](creating-authentication-journey.html#example_sso_url_journey).

**MSI Updater client tab overview**

| **Tab name**                                   | **Description**                                                                                                                     |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| [**Parameters**](#msiupdater_parameters_tab)   | Select the base MSI file to update, as well as which MFA methods to allow on Windows login.                                         |
| [**Settings**](#msiupdater_settings_tab)       | Configure various settings, such as caching the last used username to pre-populate on next login or enabling trace logs by default. |
| [**MFA**](#msiupdater_mfa_tab)                 | Enable MFA settings, such as allowing a Windows group to bypass MFA login or enabling Offline OTP (TOTP/OATH).                      |
| [**Advanced**](#msiupdater_advanced_tab)       | Change the UI text of the MFA method(s) that users select on Windows login.                                                         |
| [**CredUI**](#msiupdater_credui_tab)           | Select scenarios in which you can bypass MFA on Windows login.                                                                      |
| [**Ping Identity**](#msiupdater_forgerock_tab) | Ping Identity specific settings, such as the Ping Identity URL or the names of the journeys that correspond to each MFA method.     |

To begin the configurations, launch the MSI Updater client as an **administrator**.

To configure the MSI Updater client:

In the Parameters tab, configure the relevant settings:

1. With the MSI Updater client launched, at the top of the Parameters tab, click Browse and upload the workstation authentication MSI file to be updated. This is the base MSI file that came with the downloads.

2. If preferred, enter an uninstall password in the **Uninstall** field.

   |   |                                                                                                                       |
   | - | --------------------------------------------------------------------------------------------------------------------- |
   |   | Entering an uninstall password ensures end users cannot uninstall the MSI package without the administrator password. |

3. Select one or more of the following authentication options:

   | Authenticator      | **Description**                                                                                                                                                                                                       |
   | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Ping Identity Push | Select this checkbox to enable login to Windows using Ping Identity's push notification authentication.This is used in conjunction with the PingID mobile app.                                                        |
   | OTP                | Select this checkbox to enable authentication with TOTP (OATH). This corresponds to the journey used for TOTP (OATH).This is also referred to as Offline OTP. This is used in conjunction with the PingID mobile app. |
   | SMS                | Select this checkbox to enable authentication with OTP via SMS. This corresponds to the journey used for OTP over SMS.                                                                                                |
   | Email              | Select this checkbox to enable authentication with OTP via email. This corresponds to the journey used for OTP via email.                                                                                             |
   | Voice Call         | Select this checkbox to enable a two-factor authentication voice call. This corresponds to the journey used for OTP via a voice call.                                                                                 |

   |   |                                                                        |
   | - | ---------------------------------------------------------------------- |
   |   | SMS, email, and voice call all utilize the same journey configuration. |

4. Click Next to open the Settings tab.

5) In the Settings tab, configure the relevant settings:

   |   |                                                        |
   | - | ------------------------------------------------------ |
   |   | The MSI Updater version appears at the top of the tab. |

   | Setting                           | Description                                                                                                                                                                                                                                                            |
   | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Show Default Credential Providers | Determines whether Windows default credential providers (Windows and Active Directory) are displayed when logging into Windows.&#xA;&#xA;Select this option for testing or debugging. Do not use this in production (the MSI deployed on your end user's workstation). |
   | Use Last Username                 | When selected, the username of the user who logged in most recently is saved and automatically presented for the next login.                                                                                                                                           |
   | TPM Support                       | If TPM 2.0 is enabled, selecting this option allows TPM to store the private key for BLE password encryption.                                                                                                                                                          |
   | Local User Support                | When selected, workstation authentication for Windows will be enabled for local users and will verify that the local user matches with the corresponding user in Ping Identity.&#xA;&#xA;This setting is relevant for non-domain users only.                           |
   | POC Mode                          | When selected, workstation authentication for Windows will not check the certificate with the server. This setting is used mainly for POC.                                                                                                                             |
   | Azure AD Joined Machine           | Select this checkbox when the workstations are configured to connect with the Azure AD domain. When the setting is selected, users will be prompted to log in with UPN and not their username.                                                                         |
   | Enable Trace                      | Select this checkbox to enable the logs by default immediately after installation. Learn more in [Log files with Enterprise Connect Windows Workstation Authentication](logging.html).                                                                                 |

6. Click Next.

7) In the MFA tab, configure the relevant settings:

   | **Setting**                               | **Description**                                                                                                                                                                                                                                                                                                                                                                                                         |
   | ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | MFA Change Password Support               | When selected, users are able to change the password on the Windows workstation without the Workstation Authentication credential provider (CP) intercepting the process. When the checkbox is cleared, the workstation authentication CP controls the password change process.                                                                                                                                         |
   | Bypass Local User Login                   | When selected, administrators with a local user account can bypass workstation authentication and log in with their username and password.                                                                                                                                                                                                                                                                              |
   | Use Offline OTP                           | When selected, users are able to log into Windows using a one time password that is stored locally. When Offline OTP is activated, a list of OTPs is securely stored on the Windows workstation to allow users to authenticate to the workstation when not connected to the network. The OTPs are timed-based and use the standard TOTP mechanism. Learn more in [Offline OTP enrollment](offline-otp-enrollment.html). |
   | Force Offline OTP After Installation      | When selected, users are unable to perform offline authentication until they complete at least one online login successfully.                                                                                                                                                                                                                                                                                           |
   | Bypass MFA on Unlock when Connected to AD | When selected, users connected to the organization network who have already authenticated with MFA are not required to authenticate with 2nd factor again when unlocking the workstation. This will work as long as you are inside the network (no time limit).&#xA;&#xA;When selecting this option, verify that the Bypass MFA Groups checkbox is NOT selected.                                                        |
   | Force Lock After Offline OTP              | When selected, workstations that were unlocked using an Offline OTP and then connected back to the organization network (online) are automatically locked, and the user is asked to authenticate. This setting prevents users from using weak authentication to log into the organization network (online).                                                                                                             |
   | Bypass MFA from NLA Login                 | When selected, users who are members of the Bypass MFA Group will not require MFA authentication when using a Network Level Authentication (NLA) login.                                                                                                                                                                                                                                                                 |
   | Bypass MFA Groups                         | When selected, you can specify ONE group in the AD that will not require MFA authentication. Enter *\<Domain>\\>Group Name>* in the field to the right.&#xA;&#xA;When selecting this option, verify that the Bypass MFA on Unlock when Connected to AD checkbox is NOT selected.                                                                                                                                        |
   | Offline OTP Buffer Period                 | If Use Offline OTP is selected, enter the maximum period of time (in days) that users will be able to continue authenticating offline without performing an online login. After an expired authentication, users are forced to authenticate online before using the Offline OTP option again.                                                                                                                           |

8. Click Next.

9) In the Advanced tab, configure the relevant settings:

   | **Setting**                    | **Description**                                                                                                                                                                                                                                                                                                                                              |
   | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | Change OTP Name                | Allows you to change the default name of the TOTP (OATH or Offline OTP) displayed in the Windows credential provider's login authentication method selection list. After selecting the checkbox, enter the desired name in the field (for example, *ForgeRock OTP*). This setting is available only when the OTP checkbox in the Parameters tab is selected. |
   | Change Ping Identity Push Name | Allows you to change the default name of the authenticator displayed in the Windows credential provider's login authentication method selection list. After selecting the checkbox, enter the desired name in the field. This setting is available only when the Ping Identity Push checkbox in the Parameters tab is selected.                              |
   | Change SMS Name                | Allows you to change the default name of the SMS option displayed in the Windows credential provider's login authentication method selection list. After selecting the checkbox, enter the desired name in the field.                                                                                                                                        |
   | Change Email Name              | Allows you to change the default name of the Email option displayed in the Windows credential provider's login authentication method selection list. After selecting the checkbox, enter the desired name in the field.                                                                                                                                      |
   | Change Voice Call Name         | Allows you to change the default name of the Voice Call option displayed in the Windows credential provider's login authentication method selection list. After selecting the checkbox, enter the desired name in the field.                                                                                                                                 |
   | Enable CP Bypass List          | Allows you to specify credential providers (in addition to Ping Identity) that will be available for Windows login. After selecting the checkbox, paste the registry key(s) representing the relevant credential provider(s) in the field to the right. The specified providers will be displayed as login options on the Windows Login screen.              |

10. If desired, customize the Windows login experience by replacing the default organization logo with your own image.

    |   |                                                                                                                                            |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------ |
    |   | The images must be 448x448 in 24-bit BMP (bitmap image file) format. For Windows Servers, the images must be 448x448 in 16-bit BMP format. |

11. Click Next.

12) In the CredUI tab, select the scenarios in which an additional MFA credential, for example, push or OTP, will **not** be required. When a Bypass is selected, the default Windows login screen is presented and end users authenticate by entering their username and password.

    Selecting Bypass All activates MFA bypass for all the scenarios listed below in the tab.

13) Click Next.

14. In the Ping Identity tab, configure the relevant settings:

    | **Setting**                      | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
    | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Use credentials                  | When selected, user credentials are sent to Ping Identity for validation. You must configure the journey to support the validation of the user credentials.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
    | Use failureUrl for error message | When selected, error descriptions are displayed on the Windows Login screen (in the event of error/authentication failure). This means that your journey, in the event of a failure, must reference the Failure URL node.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
    | Server URL                       | Enter the URL of your Ping Identity authentication server. For example, `https://<tenant-env-fqdn>/openam`.Ensure to include the path to AM in the URL.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
    | Realms                           | Enter the name of the Ping Identity realm to authenticate to.For example, `alpha`.&#xA;&#xA;There is no leading / when defining the realm for Enterprise Connect Windows Workstation Authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
    | Push Tree Name                   | Enter the name of the push journey.For example, `windows-push`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
    | OTP Tree Name                    | Enter the name of the OTP journey.For example, `windows-otp`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
    | SMS/Email Tree Name              | Enter the name of the SMS/email/voice call journey.For example, `windows-sms-email-voice`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
    | Enable SSO                       | When selected, the SSO Portal opens automatically upon successful login to Windows. This will open, in the default browser on the Windows machine, a logged in instance to the specified Ping Identity environment. Enter the SSO URL in the field to the right. If this box is selected, the URL box becomes available for editing. This is also known as a transfer of trust.An example SSO URL to enter in this box is `https://<tenant-env-fqdn>/am/XUI/?realm=alpha&authIndexType=service&authIndexValue=sso-journey&ForceAuth=true`.	The authIndexValue references the journey to use for SSO. Ensure to add ForceAuth=true to the end of your SSO URL. |

    |   |                                                                                                                                                                  |
    | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | For examples of the pre-configured journeys to have in your environment, learn more in [Create authentication journey(s)](creating-authentication-journey.html). |

15) At the bottom of the Ping Identity tab, click Apply.

    A confirmation screen will appear.

    ![msiupdater configure confirmation](../_images/workstation-windows-guide/msiupdater-configure-confirmation.png)

A new modified MSI file is created in the same location as the original MSI file. The name of the new file will include Workstation Authentication for Windows 64-bit and the timestamp of file creation.

|   |                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The base (original) MSI file will not be updated and can be reused. **Do not use** the base MSI file for deployment. Use the deployment specific MSI file generated as the output of the MSI Updater configurations. |

Enterprise Connect Windows Workstation Authentication installation/configuration checklist

* [icon: check-square-o, set=fa]Download and install the binaries from [Backstage](https://backstage.forgerock.com/downloads/browse/ig/all/productId:enterprise-connect) (you must be logged in). This includes the base MSI file as well as the MSI Updater client.

* [icon: check-square-o, set=fa]Pre-configure the relevant [journey(s)](creating-authentication-journey.html).

* [icon: check-square-o, set=fa][Install](installing-windows-msiupdater.html) the MSI Updater client on an administrative Windows machine.

* [icon: check-square-o, set=fa][Configure](configuring-windows-msiupdater.html) the MSI Updater client specific to your organization's needs.

* [icon: square-o, set=fa]*\(Optional) Consider [additional configurations](windows-additional-reference.html).*

* [icon: square-o, set=fa][Deploy](deploying-msi.html#msi_deployment_of_workstation_authentication) the generated MSI file through your desired mechanism.

* [icon: square-o, set=fa][Verify and test](verify-windows-authentication.html) your deployment.

---

---
title: Create authentication journey(s)
description: To enable workstation authentication integration, you need to create relevant journeys to support the MFA authentication method(s) you want. These journeys allow workstation authentication to work directly with the Ping Identity environment.
component: enterprise-connect
version: latest
page_id: enterprise-connect:workstation-windows-guide-3.7.2.7293:creating-authentication-journey
canonical_url: https://docs.pingidentity.com/enterprise-connect/latest/workstation-windows-guide-3.7.2.7293/creating-authentication-journey.html
section_ids:
  example_push_journey: Example of push journey
  example_otp_journey: Example of OTP from authenticator app journey
  example_sms_email_journey: Example of OTP SMS/email/voice call journey
  example_sso_url_journey: Example of SSO journey
---

# Create authentication journey(s)

To enable workstation authentication integration, you need to create relevant journeys to support the MFA authentication method(s) you want. These journeys allow workstation authentication to work directly with the Ping Identity environment.

Since Enterprise Connect integrates with PingOne Advanced Identity Cloud or self-managed PingAM, the examples that follow depict the various UI changes between the two.

|   |                                                                                                                                                                                                                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Do not deviate from the following journeys when you configure Enterprise Connect or use the journeys you create for any other purpose (including repurposing the journeys). You must strictly follow the placement of the nodes to ensure the product works correctly.Failure to do so or the addition of other nodes could result in unexpected behavior. |

## Example of push journey

The push journeys for Enterprise Connect allow users to approve a push notification from the PingID mobile app. End users must download the PingID mobile app and pre-register (from another journey you define) to be able to use the push journeys.

* PingOne Advanced Identity Cloud

* PingAM

![create journey push identity cloud](../_images/workstation-windows-guide/create-journey-push-identity-cloud.png)

If you configure [Use credentials](configuring-windows-msiupdater.html#msiupdater_forgerock_tab) in the MSI Updater client, then you must include the *Platform Password* and *Data Store Decision* nodes. Otherwise, you must omit these nodes in your journey configuration.

|   |                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When configuring the push journey in PingOne Advanced Identity Cloud, you must enable services in the AM admin UI (native console). Learn more in [Create a push authentication journey](https://docs.pingidentity.com/pingoneaic/planning/plan-security.html#proc-authn-mfa-tree-push). |

![create journey push am](../_images/workstation-windows-guide/create-journey-push-am.png)

If you configure [Use credentials](configuring-windows-msiupdater.html#msiupdater_forgerock_tab) in the MSI Updater client, then you must include the *Platform Password* and *Data Store Decision* nodes. Otherwise, you must omit these nodes in your journey configuration.

|   |                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When configuring the push journey in PingAM, you must enable services in the AM admin UI (self managed). Learn more in [Create a push authentication journey](https://docs.pingidentity.com/pingoneaic/planning/plan-security.html#proc-authn-mfa-tree-push). |

## Example of OTP from authenticator app journey

The following journeys show the OTP that is presented from the PingID mobile app. End users must download the PingID mobile app and pre-register (from another journey you define) to be able to use the OTP journeys.

* PingOne Advanced Identity Cloud

* PingAM

![create journey otp identity cloud](../_images/workstation-windows-guide/create-journey-otp-identity-cloud.png)

If you configure [Use credentials](configuring-windows-msiupdater.html#msiupdater_forgerock_tab) in the MSI Updater client, then you must include the *Platform Password* and *Data Store Decision* nodes. Otherwise, you must omit these nodes in your journey configuration.

![create journey otp am](../_images/workstation-windows-guide/create-journey-otp-am.png)

If you configure [Use credentials](configuring-windows-msiupdater.html#msiupdater_forgerock_tab) in the MSI Updater client, then you must include the *Platform Password* and *Data Store Decision* nodes. Otherwise, you must omit these nodes in your journey configuration.

## Example of OTP SMS/email/voice call journey

The following journeys show the OATH OTP (HOTP) that can be presented to an end user via SMS/email/voice. Ensure end users have the appropriate data in their user profile to facilitate the MFA method(s) you allow an end user to select.

* PingOne Advanced Identity Cloud

* PingAM

![create journey sms email identity cloud](../_images/workstation-windows-guide/create-journey-sms-email-identity-cloud.png)

If you configure [Use credentials](configuring-windows-msiupdater.html#msiupdater_forgerock_tab) in the MSI Updater client, then you must include the *Platform Password* and *Data Store Decision* nodes. Otherwise, you must omit these nodes in your journey configuration.

|   |                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | In the Choice Collector node, the options correlate to the following MFA methods within Enterprise Connect Windows Workstation Authentication:1) SMS

2) Email

3) VoiceTherefore, ensure SMS is the first choice in the node, followed by email. If voice call is a method you configure, it must be the third option.Do not deviate from this order. |

If you choose to use the *voice* option, you could use the [Twilio](https://backstage.forgerock.com/docs/auth-node-ref/latest/cloud/auth-node-twilio-verify-collector-decision.html#twilio-examples) nodes (you must have a valid subscription with Twilio).

![create journey sms email am](../_images/workstation-windows-guide/create-journey-sms-email-am.png)

If you configure [Use credentials](configuring-windows-msiupdater.html#msiupdater_forgerock_tab) in the MSI Updater client, then you must include the *Platform Password* and *Data Store Decision* nodes. Otherwise, you must omit these nodes in your journey configuration.

|   |                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | In the Choice Collector node, the options correlate to the following MFA methods within Enterprise Connect Windows Workstation Authentication:1) SMS

2) Email

3) VoiceTherefore, ensure SMS is the first choice in the node, followed by email. If voice call is a method you configure, it must be the third option.Do not deviate from this order. |

If you choose to use the *voice* option, you could use the [Twilio](https://marketplace.pingone.com/item/twilio-verify-auth-tree-notes) nodes (you must have a valid subscription with Twilio).

## Example of SSO journey

The following journeys depict the flow that Enterprise Connect uses after a user authenticates to their workstation. The end user Ping Identity environment opens in a default browser.

If you configure the [Enable SSO](configuring-windows-msiupdater.html#msiupdater_forgerock_tab) setting in the MSI Updater client, then this journey applies to you. In this setting, you must supply the journey URL.

An example SSO URL to enter in this field is `https://<tenant-env-fqdn>/am/XUI/?realm=alpha&authIndexType=service&authIndexValue=sso-journey&ForceAuth=true`.

|   |                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------- |
|   | The `authIndexValue` references the journey to use for SSO. Ensure to add `ForceAuth=true` to the end of your SSO URL. |

* PingOne Advanced Identity Cloud

* PingAM

![create journey sso url identity cloud](../_images/workstation-windows-guide/create-journey-sso-url-identity-cloud.png)

The Check for ValidSession node (shown in the image above) is the Scripted Decision node. In this example, it references a simple authentication JavaScript script:

```java
if (typeof existingSession !== 'undefined')
{
  outcome = "hasSession";
}
else
{
  outcome = "noSession";
}
```

![create journey sso url am](../_images/workstation-windows-guide/create-journey-sso-url-am.png)

The Check for ValidSession node (shown in the image above) is the Scripted Decision node. In this example, it references a simple authentication JavaScript script:

```java
if (typeof existingSession !== 'undefined')
{
  outcome = "hasSession";
}
else
{
  outcome = "noSession";
}
```

Enterprise Connect Windows Workstation Authentication installation/configuration checklist

* [icon: check-square-o, set=fa]Download and install the binaries from [Backstage](https://backstage.forgerock.com/downloads/browse/ig/all/productId:enterprise-connect) (you must be logged in). This includes the base MSI file as well as the MSI Updater client.

* [icon: check-square-o, set=fa]Pre-configure the relevant [journey(s)](creating-authentication-journey.html).

* [icon: square-o, set=fa]*[Install](installing-windows-msiupdater.html) the MSI Updater client on an administrative Windows machine.*

* [icon: square-o, set=fa][Configure](configuring-windows-msiupdater.html) the MSI Updater client specific to your organization's needs.

* [icon: square-o, set=fa]\(Optional) Consider [additional configurations](windows-additional-reference.html).

* [icon: square-o, set=fa][Deploy](deploying-msi.html#msi_deployment_of_workstation_authentication) the generated MSI file through your desired mechanism.

* [icon: square-o, set=fa][Verify and test](verify-windows-authentication.html) your deployment.

---

---
title: Doc updates
description: In addition to the changes described in these notes, the published documentation for this version includes the following important changes.
component: enterprise-connect
version: latest
page_id: enterprise-connect:release-notes:passwordless/doc-updates
canonical_url: https://docs.pingidentity.com/enterprise-connect/latest/release-notes/passwordless/doc-updates.html
---

# Doc updates

In addition to the changes described in these notes, the published documentation for this version includes the following important changes.

| Date               | Description                                               |
| ------------------ | --------------------------------------------------------- |
| January, 2026      | Release of Enterprise Connect Passwordless Servers 6.8.   |
| September 29, 2025 | Add an RSS feed link to the changelog.                    |
| April 2024         | Release of Enterprise Connect Passwordless Servers 5.8.2. |
| September 2023     | Release of Enterprise Connect Passwordless Servers 5.4.8. |
| May 2023           | Release of Enterprise Connect Passwordless Servers 5.4.4. |

---

---
title: Doc updates
description: In addition to the changes described in these notes, the published documentation for this version includes the following important changes.
component: enterprise-connect
version: latest
page_id: enterprise-connect:release-notes:passwordless-mac/doc-updates
canonical_url: https://docs.pingidentity.com/enterprise-connect/latest/release-notes/passwordless-mac/doc-updates.html
---

# Doc updates

In addition to the changes described in these notes, the published documentation for this version includes the following important changes.

| Date               | Description                                                 |
| ------------------ | ----------------------------------------------------------- |
| January 2026       | Release of Enterprise Connect Passwordless Mac Agent 4.3.   |
| September 29, 2025 | Add an RSS feed link to the changelog.                      |
| April 2024         | Release of Enterprise Connect Passwordless Mac Agent 2.7.1. |
| September 2023     | Release of Enterprise Connect Passwordless Mac Agent 2.6.7. |

---

---
title: Doc updates
description: In addition to the changes described in these notes, the published documentation for this version includes the following important changes.
component: enterprise-connect
version: latest
page_id: enterprise-connect:release-notes:passwordless-windows/doc-updates
canonical_url: https://docs.pingidentity.com/enterprise-connect/latest/release-notes/passwordless-windows/doc-updates.html
---

# Doc updates

In addition to the changes described in these notes, the published documentation for this version includes the following important changes.

| Date               | Description                                                     |
| ------------------ | --------------------------------------------------------------- |
| January 2026       | Release of Enterprise Connect Passwordless Windows Agent 4.3.1. |
| September 29, 2025 | Add an RSS feed link to the changelog.                          |
| April 2024         | Release of Enterprise Connect Passwordless Windows Agent 3.9.3. |
| September 2023     | Release of Enterprise Connect Passwordless Windows Agent 3.8.4. |
| May 2023           | Release of Enterprise Connect Passwordless Windows Agent 3.8.2. |

---

---
title: Doc updates
description: In addition to the changes described elsewhere in these notes, the published documentation for this version includes the following important changes.
component: enterprise-connect
version: latest
page_id: enterprise-connect:release-notes:windows-radius/doc-updates
canonical_url: https://docs.pingidentity.com/enterprise-connect/latest/release-notes/windows-radius/doc-updates.html
---

# Doc updates

In addition to the changes described elsewhere in these notes, the published documentation for this version includes the following important changes.

| Date               | Description                                               |
| ------------------ | --------------------------------------------------------- |
| September 29, 2025 | Add an RSS feed link to the changelog.                    |
| January 2025       | Release of Enterprise Connect Windows RADIUS proxy 3.0.2  |
| September 2022     | Release of Enterprise Connect Windows RADIUS proxy 2.7.1. |

---

---
title: Doc updates
description: In addition to the changes described elsewhere in these notes, the published documentation for this version includes the following important changes.
component: enterprise-connect
version: latest
page_id: enterprise-connect:release-notes:workstation-mac/doc-updates
canonical_url: https://docs.pingidentity.com/enterprise-connect/latest/release-notes/workstation-mac/doc-updates.html
---

# Doc updates

In addition to the changes described elsewhere in these notes, the published documentation for this version includes the following important changes.

| Date               | Description                                                         |
| ------------------ | ------------------------------------------------------------------- |
| September 29, 2025 | Add an RSS feed link to the changelog.                              |
| January 2025       | Release of Enterprise Connect Mac Workstation Authentication 3.0.3  |
| April 2023         | Release of Enterprise Connect Mac Workstation Authentication 2.7.2. |

---

---
title: Doc updates
description: In addition to the changes described elsewhere in these notes, the published documentation for this version includes the following important changes.
component: enterprise-connect
version: latest
page_id: enterprise-connect:release-notes:workstation-windows/doc-updates
canonical_url: https://docs.pingidentity.com/enterprise-connect/latest/release-notes/workstation-windows/doc-updates.html
---

# Doc updates

In addition to the changes described elsewhere in these notes, the published documentation for this version includes the following important changes.

| Date               | Description                                                                                                                                                                                            |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| September 29, 2025 | Add an RSS feed link to the changelog.                                                                                                                                                                 |
| January 2025       | Updated Enterprise Connect Windows Workstation Authentication 3.7.2.7293 with Ping Identity branding.                                                                                                  |
| September 2022     | * Updated the Enterprise Connect Windows Workstation Authentication version 3.7.2 to 3.7.2.7291 with Ping Identity.

* Initial release of Enterprise Connect Windows Workstation Authentication 3.7.2. |

---

---
title: ECP Windows Agent
description: You must install and configure Enterprise Connect Passwordless Servers before you can configure and deploy the Enterprise Connect Passwordless Windows Agent.
component: enterprise-connect
version: latest
page_id: enterprise-connect:passwordless-windows:preface
canonical_url: https://docs.pingidentity.com/enterprise-connect/latest/passwordless-windows/preface.html
section_ids:
  guides: Guides
---

# ECP Windows Agent

You must [install](../passwordless-servers/install-servers.html) and [configure](../passwordless-servers/configure-mgmt-console.html) Enterprise Connect Passwordless Servers before you can configure and deploy the Enterprise Connect Passwordless Windows Agent.

Ping Identity and Secret Double Octopus (SDO) replace passwords altogether with a high assurance, password-free authentication paradigm.

You use Enterprise Connect Passwordless Windows Agent (ECP Windows Agent) Windows Credential Provider with standard Active Directory (AD) interfaces, replacing AD passwords seamlessly with a stronger, more secure alternative. This approach strengthens the AD domain's security, improves user experience and productivity, and significantly reduces password management costs.

## Guides

For installation instructions of the ECP Windows Agent, refer to the following table:

| Version                                             | PDF                                                                                       |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Enterprise Connect Passwordless Windows Agent 4.3.1 | [4.3.1 Windows agent install guide](../_attachments/windows_agent_passwordless_4.3.1.pdf) |
| Enterprise Connect Passwordless Windows Agent 3.9.3 | [3.9.3 Windows agent install guide](../_attachments/windows_agent_passwordless_3.9.3.pdf) |
| Enterprise Connect Passwordless Windows Agent 3.8.4 | [3.8.4 Windows agent install guide](../_attachments/windows_agent_passwordless_3.8.4.pdf) |
| Enterprise Connect Passwordless Windows Agent 3.8.2 | [3.8.2 Windows agent install guide](../_attachments/windows_agent_passwordless_3.8.2.pdf) |