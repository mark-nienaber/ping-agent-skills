---
title: Adding credentials as a user
description: The Symantec VIP IdP adapter allows users to add credentials as a self-service by default.
component: symantec-vip
page_id: symantec-vip:user_credential_management:pf_symantec_vip_ik_adding_credentials_as_a_user
canonical_url: https://docs.pingidentity.com/integrations/symantec-vip/user_credential_management/pf_symantec_vip_ik_adding_credentials_as_a_user.html
revdate: June 24, 2025
section_ids:
  steps: Steps
---

# Adding credentials as a user

The Symantec VIP IdP adapter allows users to add credentials as a self-service by default.

## Steps

1. Open the VIP Access app on your mobile device.

2. Start the PingFederate authentication flow by signing on to the first-factor authentication adapter.

   For example, this could be an HTML Form Adapter or OpenToken Adapter instance.

3. On the Symantec VIP IdP adapter, sign on with the same username and password.

4. Click **Add Credential**.

   ![The Symantec VIP Adapter Add Credential button](_images/addCredentialButton.png)

5. On the **Add Credentials** page, enter the credential ID and security code shown on your VIP Access mobile app, or on your physical VIP security token or card. Click **Submit**.

6. On the sign-on screen, select **Security Code**, and enter the next security code that appears on your device. Click **Submit**.

   ![The Symantec VIP Adapter sign on page](../_images/symantecVIPsignon.jpg)
