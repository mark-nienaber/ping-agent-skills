---
title: (Legacy) Configuring FIDO2 biometrics for MFA authentication
description: To allow users to pair and authenticate using the built-in biometrics on their device for MFA (Multi-factor authentication), enable FIDO2 biometrics in the admin portal.
component: pingid
page_id: pingid:pingid_service_management:pid_configuring_fido2_biometrics_mfa_authentication
canonical_url: http://docs.pingidentity.com/pingid/pingid_service_management/pid_configuring_fido2_biometrics_mfa_authentication.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 14, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result
---

# (Legacy) Configuring FIDO2 biometrics for MFA authentication

To allow users to pair and authenticate using the built-in biometrics on their device for MFA (Multi-factor authentication), enable FIDO2 biometrics in the admin portal.

## About this task

Users must enter their username (and password, if required), and are then prompted to authenticate with their device biometrics.

|   |                                                                                                                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This topic is for authentication using legacy FIDO2 biometrics. To configure passwordless authentication for passkeys using the FIDO2 authentication method, see [Configuring passwordless authentication for passkeys](pid_configuring_fido2_passwordless_auth_passkeys.html). |

## Steps

1. Sign on to the admin portal.

2. Go to **Setup → PingID → Configuration**.

3. Go to the **Alternate Authentication Methods** section, and in the **FIDO2 Biometrics** row, select the **Enable** check box. ![A screen capture of the Alternate Authentication Methods section.](_images/vkb1564020562147.png)

4. Click **Save**.

## Result

Users can pair and authenticate with gestures defined on their FIDO2 biometrics accessing device. For more information, see [Using Windows Hello for authentication](http://docs.pingidentity.com/pingid-user-guide/secure_authentication_with_pingid/pid_using_windows_hello_auth.html), [Using Apple Mac Touch ID for authentication](http://docs.pingidentity.com/pingid-user-guide/secure_authentication_with_pingid/pid_using_mac_touchid_auth.html), and [Using Android biometrics for authentication](http://docs.pingidentity.com/pingid-user-guide/secure_authentication_with_pingid/pid_using_android_biometrics_auth.html) in the [PingID End User Guide](http://docs.pingidentity.com/pingid-user-guide/).
