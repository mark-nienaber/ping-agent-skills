---
title: Accessing the PingOne Privilege admin console as an administrator
description: The admin console provides a centralized interface to configure settings, manage users, and monitor access activities.
component: privilege
page_id: privilege:getting-started:accessing-admin-console
canonical_url: https://docs.pingidentity.com/privilege/getting-started/accessing-admin-console.html
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
