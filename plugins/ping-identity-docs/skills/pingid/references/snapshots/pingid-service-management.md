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

---

---
title: (Legacy) Configuring FIDO2 biometrics for PingID
description: Overview of legacy PingID FIDO2 platform biometrics, including supported devices and high-level steps to enable passwordless or MFA authentication.
component: pingid
page_id: pingid:pingid_service_management:pid_configuring_fido2_biometrics_for_pid
canonical_url: http://docs.pingidentity.com/pingid/pingid_service_management/pid_configuring_fido2_biometrics_for_pid.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 16, 2026
section_ids:
  about-this-task: About this task
  steps: Steps
  legacy-fido2-biometrics-authentication-requirements-and-limitations: (Legacy) FIDO2 biometrics authentication requirements and limitations
  general-requirements: General requirements:
  fido-passkey-requirements: FIDO Passkey requirements:
  passwordless-authentication-requirements: Passwordless authentication requirements:
  general-limitations: General limitations:
  second-factor-authentication-limitations: Second factor authentication limitations:
  legacy-configuring-fido2-passwordless-authentication: (Legacy) Configuring FIDO2 passwordless authentication
  about-this-task-2: About this task
  steps-2: Steps
  result: Result
  legacy-configuring-fido2-biometrics-for-mfa-authentication: (Legacy) Configuring FIDO2 biometrics for MFA authentication
  about-this-task-3: About this task
  steps-3: Steps
  result-2: Result
  legacy-fido2-biometrics-use-cases: (Legacy) FIDO2 biometrics use cases
---

# (Legacy) Configuring FIDO2 biometrics for PingID

PingID supports FIDO2 platform biometrics. Users can authenticate on their FIDO2-compatible accessing device using a gesture that is enabled by the device's built-in biometrics.

## About this task

Supported devices include Windows Hello, iOS and iPadOS devices 14 and later, Android devices 7.0 and later, and Apple Mac machines with fingerprint authentication capabilities.

If a passwordless flow is configured, the passwordless flow is enabled by FIDO2 platform biometrics. Learn more in [(Legacy) Configuring FIDO2 passwordless authentication](pid_configuring_fido2_passwordless_auth.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingID receives confirmation that a device has the relevant WebAuthn FIDO2 capabilities with the authenticating browser. If the capabilities are not sufficient, such as the browser is not supported, the OS does not support biometric authentication, or a compatible authentication method is not defined, the user will be unable to authenticate with the FIDO2 biometrics device and might be unable to authenticate at all if that is their only authenticating device. |

* To enable users to authenticate using FIDO2 platform biometrics, the high-level flow is as follows

## Steps

1. In the Admin portal, enable FIDO2 platform biometrics.

   Learn more in [(Legacy) Configuring FIDO2 passwordless authentication](pid_configuring_fido2_passwordless_auth.html) or [(Legacy) Configuring FIDO2 biometrics for MFA authentication](pid_configuring_fido2_biometrics_mfa_authentication.html).

2. **Optional:** If required, define a PingID policy.

   Learn more in [Authentication policy](pid_authentication_policy.html).

3. Have the user register their FIDO2 biometrics device and pair it with their PingID account to create a trust between the device and the user's account, so they can use it authenticate during the sign-on process.

   Learn more in the following sections in the PingID User Guide:

   * [Using Windows Hello for authentication](http://docs.pingidentity.com/pingid-user-guide/secure_authentication_with_pingid/pid_using_windows_hello_auth.html)

   * [Using Apple Mac Touch ID for authentication](http://docs.pingidentity.com/pingid-user-guide/secure_authentication_with_pingid/pid_using_mac_touchid_auth.html)

   * [Using a security key (FIDO2) for authentication](http://docs.pingidentity.com/pingid-user-guide/secure_authentication_with_pingid/pid_using_security_key_auth.html)

   * [Using Android biometrics for authentication](http://docs.pingidentity.com/pingid-user-guide/secure_authentication_with_pingid/pid_using_android_biometrics_auth.html)

## (Legacy) FIDO2 biometrics authentication requirements and limitations

The following list details the requirements and limitations when using FIDO2 platform biometrics with PingID.

### General requirements:

|   |                                                                                                                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For PingID environments that are integrated with PingOne: From April 15th 2024, the FIDO2 Biometrics and Security Key authentication methods are deprecated and replaced by the more advanced FIDO2 authentication method. Learn more: [Updating a PingID account to use PingOne FIDO2 policy for Passkey support](pid_update_to_fido2_authentication_method.html). |

* FIDO2 biometrics authentication is supported for web authentication only.

* Define an appropriate FIDO2 platform authentication method on the accessing device to pair the device, such as fingerprint or Face ID. If no platform authentication method is defined, the user will not be able to pair the device or authenticate with PingID.

* Perform registration and authentication with a WebAuthn supported browser, such as the latest versions of Google Chrome, Safari, or Microsoft Edge.

* Avoid the use of the same FIDO2 biometrics device by more than one user.

* Passwordless authentication using Mac Touch ID through a Chrome browser is only supported for devices paired after February 23, 2021. Users with devices that were paired to PingID before February 23, 2021 should unpair their device and then pair it again, in order to use passwordless authentication with a Chrome browser.

### FIDO Passkey requirements:

FIDO passkey requirements and limitations are constantly evolving. For a list of the most up-to-date operating systems and browsers supported, see [Device support](https://passkeys.dev/device-support/).

### Passwordless authentication requirements:

* When creating a [PingFederate policy for passwordless authentication with FIDO2 biometrics](../pingid_integrations/pid_configuring_pf_policy_for_passwordless_authentication_fido_biometrics.html), you must use PingID Integration kit 2.7 or later, with PingFederate v9.3 or later.

### General limitations:

* WebAuthn timeout is defined for 2 minutes. The actual timeout value might vary depending on the browser used.

* PingID does not support Android-key attestation.

* A user can pair more than one FIDO2 biometrics device with their account, however, they cannot pair the same FIDO2 biometrics device with their account more than once.

* Some older browser versions might not support FIDO2 biometrics when using incognito or private mode.

* If an an iOS or Mac Touch ID device is paired with PingID, clearing history and website data from the device's Safari settings will prevent a user from using PingID to authenticate. The user must unpair their device and then pair the device again to authenticate with PingID.

### Second factor authentication limitations:

* Android devices that are paired within a workspace can only be used to authenticate in the same workspace.

For troubleshooting, see the relevant section in the PingID User Guide.

## (Legacy) Configuring FIDO2 passwordless authentication

FIDO2 passwordless authentication enables you to identify and authenticate a user based on the FIDO2 protocol without requiring the user to enter their username and password.

### About this task

|   |                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This topic is for passwordless authentication using legacy FIDO2 biometrics. For FIDO2 authentication method, see [Configuring passwordless authentication for passkeys](pid_configuring_fido2_passwordless_auth_passkeys.html). |

To configure FIDO2 passwordless authentication, you must configure a PingFederate policy for a passwordless authentication flow. FIDO2 biometrics must then be enabled in the administrative console.

The process of registering a FIDO2 device is the same for both passwordless and secondary authentication flows. The user is directed to the relevant flow, according to your organization's configuration. Once registered, the same FIDO2-compliant device can be used to authenticate with either flow. For more information, see [Setting up Windows Hello authentication](http://docs.pingidentity.com/pingid-user-guide/secure_authentication_with_pingid/pid_using_windows_hello_auth.html).

|   |                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This feature requires PingFederate 9.3 or later. For more information, see [(Legacy) FIDO2 biometrics authentication requirements and limitations](fido2_biometrics_auth_requirements_and_limitations.html). |

### Steps

1. In the PingFederate administrative console, create a policy for passwordless authentication.

   For more information, see [(Legacy) Configuring a PingFederate policy for passwordless authentication with FIDO biometrics](../pingid_integrations/pid_configuring_pf_policy_for_passwordless_authentication_fido_biometrics.html).

2. Sign on to the PingOne for Enterprise admin console and enable FIDO2 biometrics.

   1. Go to **Setup → PingID → Configuration**.

   2. Go to the **Alternate Authentication Methods** section, and in the **FIDO2 Biometrics** row, select the **Enable** check box.

      ![A screen capture of the Alternate Authentication Methods section.](_images/vkb1564020562147.png)

   3. Click **Save**.

### Result

The changes are saved, and users can pair and authenticate with gestures defined on their FIDO2 biometrics accessing device. For more information, see [Using Windows Hello for authentication](http://docs.pingidentity.com/pingid-user-guide/secure_authentication_with_pingid/pid_using_windows_hello_auth.html).

## (Legacy) Configuring FIDO2 biometrics for MFA authentication

To allow users to pair and authenticate using the built-in biometrics on their device for MFA (Multi-factor authentication), enable FIDO2 biometrics in the admin portal.

### About this task

Users must enter their username (and password, if required), and are then prompted to authenticate with their device biometrics.

|   |                                                                                                                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This topic is for authentication using legacy FIDO2 biometrics. To configure passwordless authentication for passkeys using the FIDO2 authentication method, see [Configuring passwordless authentication for passkeys](pid_configuring_fido2_passwordless_auth_passkeys.html). |

### Steps

1. Sign on to the admin portal.

2. Go to **Setup → PingID → Configuration**.

3. Go to the **Alternate Authentication Methods** section, and in the **FIDO2 Biometrics** row, select the **Enable** check box. ![A screen capture of the Alternate Authentication Methods section.](_images/vkb1564020562147.png)

4. Click **Save**.

### Result

Users can pair and authenticate with gestures defined on their FIDO2 biometrics accessing device. For more information, see [Using Windows Hello for authentication](http://docs.pingidentity.com/pingid-user-guide/secure_authentication_with_pingid/pid_using_windows_hello_auth.html), [Using Apple Mac Touch ID for authentication](http://docs.pingidentity.com/pingid-user-guide/secure_authentication_with_pingid/pid_using_mac_touchid_auth.html), and [Using Android biometrics for authentication](http://docs.pingidentity.com/pingid-user-guide/secure_authentication_with_pingid/pid_using_android_biometrics_auth.html) in the [PingID End User Guide](http://docs.pingidentity.com/pingid-user-guide/).

## (Legacy) FIDO2 biometrics use cases

The following table outlines several common use cases and their expected behaviors when using FIDO2 biometrics authentication.

|   |                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If policy rules are configured, the results might vary from those described in the table. For more information, see [PingID authentication policy](pid_authentication_policy.html). |

| Paired devices                                                                                    | Browser                         | Results                                                                                                                                                                                                                                                            | Reason                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| FIDO2 biometrics device only                                                                      | WebAuthn Platform compliant     | The browser prompts the user to authenticate using their FIDO2 biometrics device.                                                                                                                                                                                  | FIDO2 biometrics is the only authentication method, and the browser supports WebAuthn platform, so the user can authenticate using their FIDO2 biometrics device.                                                                                                          |
| * FIDO2 biometrics (primary)

* Email

* SMS                                                      | WebAuthn platform compliant     | The browser prompts the user to authenticate using their FIDO2 biometrics device. If the **Prompt to Select** setting is enabled, FIDO2 Biometrics appears in the list of authentication options.                                                                  | The browser supports FIDO2 biometrics, which is the user's primary device.                                                                                                                                                                                                 |
| - FIDO2 biometrics - Windows Hello (primary)

- FIDO2 biometrics - Android device

- Email

- SMS | WebAuthn platform complaint     | If the user tries to access their account with their Android device, they are prompted to authenticate using that device, even though it is not their primary device.                                                                                              | If more than one FIDO2 biometrics device is paired with a user's account, when accessing with a FIDO2 device, the browser prompts the user to authenticate with the current accessing device, regardless of which FIDO2 device is the primary device.                      |
| FIDO2 biometrics only                                                                             | Not WebAuthn Platform compliant | The browser displays the following message: `This browser doesn't support your current authentication method. Try a different browser or contact your administrator.`                                                                                              | The browser doesn't support the user's current authentication method. The user must either use a different browser that is WebAuthn compliant, such as the latest version of Chrome or Microsoft Edge, or use a FIDO2 biometrics device that is paired with their account. |
| * FIDO2 biometrics (primary)

* Email

* SMS                                                      | Not WebAuthn platform compliant | The browser prompts the user to authenticate using the next paired device. In this example, the user must authenticate using email or SMS. If the **Prompt to Select** setting is enabled, FIDO2 biometrics does not appear in the list of authentication options. | The browser is not Webauthn platform compliant and does not support the user of a FIDO2 biometrics device. The FIDO2 biometrics option is not shown and only the secondary authentication methods are presented to the user.                                               |

---

---
title: (Legacy) Configuring FIDO2 passwordless authentication
description: FIDO2 passwordless authentication enables you to identify and authenticate a user based on the FIDO2 protocol without requiring the user to enter their username and password.
component: pingid
page_id: pingid:pingid_service_management:pid_configuring_fido2_passwordless_auth
canonical_url: http://docs.pingidentity.com/pingid/pingid_service_management/pid_configuring_fido2_passwordless_auth.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 18, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result
---

# (Legacy) Configuring FIDO2 passwordless authentication

FIDO2 passwordless authentication enables you to identify and authenticate a user based on the FIDO2 protocol without requiring the user to enter their username and password.

## About this task

|   |                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This topic is for passwordless authentication using legacy FIDO2 biometrics. For FIDO2 authentication method, see [Configuring passwordless authentication for passkeys](pid_configuring_fido2_passwordless_auth_passkeys.html). |

To configure FIDO2 passwordless authentication, you must configure a PingFederate policy for a passwordless authentication flow. FIDO2 biometrics must then be enabled in the administrative console.

The process of registering a FIDO2 device is the same for both passwordless and secondary authentication flows. The user is directed to the relevant flow, according to your organization's configuration. Once registered, the same FIDO2-compliant device can be used to authenticate with either flow. For more information, see [Setting up Windows Hello authentication](http://docs.pingidentity.com/pingid-user-guide/secure_authentication_with_pingid/pid_using_windows_hello_auth.html).

|   |                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This feature requires PingFederate 9.3 or later. For more information, see [(Legacy) FIDO2 biometrics authentication requirements and limitations](fido2_biometrics_auth_requirements_and_limitations.html). |

## Steps

1. In the PingFederate administrative console, create a policy for passwordless authentication.

   For more information, see [(Legacy) Configuring a PingFederate policy for passwordless authentication with FIDO biometrics](../pingid_integrations/pid_configuring_pf_policy_for_passwordless_authentication_fido_biometrics.html).

2. Sign on to the PingOne for Enterprise admin console and enable FIDO2 biometrics.

   1. Go to **Setup → PingID → Configuration**.

   2. Go to the **Alternate Authentication Methods** section, and in the **FIDO2 Biometrics** row, select the **Enable** check box.

      ![A screen capture of the Alternate Authentication Methods section.](_images/vkb1564020562147.png)

   3. Click **Save**.

## Result

The changes are saved, and users can pair and authenticate with gestures defined on their FIDO2 biometrics accessing device. For more information, see [Using Windows Hello for authentication](http://docs.pingidentity.com/pingid-user-guide/secure_authentication_with_pingid/pid_using_windows_hello_auth.html).

---

---
title: (Legacy) Configuring security key authentication
description: Use the FIDO2 security key for web-based authentication only. The browser with which the user is accessing their resources must support WebAuthn, such as the latest version of Google Chrome or Mozilla Firefox.
component: pingid
page_id: pingid:pingid_service_management:configuring_security_key_auth
canonical_url: http://docs.pingidentity.com/pingid/pingid_service_management/configuring_security_key_auth.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 18, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
  choose-from: Choose from:
  result-2: Result
---

# (Legacy) Configuring security key authentication

Use the FIDO2 security key for web-based authentication only. The browser with which the user is accessing their resources must support WebAuthn, such as the latest version of Google Chrome or Mozilla Firefox.

## About this task

|   |                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------- |
|   | Define the use of security keys for offline authentication when installing the PingID Integration for Windows Login. |

|   |                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If the browser does not support WebAuthn, the user will be unable to authenticate with the security key and might be unable to authenticate if that is their only authenticating device. |

## Steps

1. Sign on to the admin console.

2. Go to **Setup → PingID → Configuration**.

3. Go to the **Alternate Authentication Methods** section, and in the **Security Key** row, select the **Enable** check box. ![A screen capture of the Alternate Authentication Methods section.](_images/vkb1564020562147.png)

   ### Result:

   The ability to pair and authenticate with a security key is enabled for all users in that organization, and additional security key configuration fields are shown.

   ![mage showing Resident Key and User Verification configuration options for use with a security key.](_images/qzv1668444741877.png)

4. In the **Enable** column, select the **Security Key** check box.

5. **Optional:** In the **Security Key** section, configure the following fields:

   * **Resident Key**. When set to Required, the private key is saved on the security key. To enforce [passwordless authentication](../pingid_integrations/pid_configuring_pf_policy_for_passwordless_authentication_security_key.html) on all authentication attempts, set this field to **Required**.

   * **User Verification**. This option requires the user to perform a gesture using their security key, to validate their identity (for example, using their fingerprint, or entering a PIN code). Select either:

     ### Choose from:

   * **Required**: only security keys that support user verification can be used to authenticate. When the **Resident Key** field is set to **Required**, this option is automatically set to **Required**.

   * **Preferred** (default): user verification is performed if the user's security key supports it, and is skipped if not supported.

   * **Discouraged**: user verification is not performed, even when supported by the user's security key. In cases where user verification is required by the security key itself, this setting does not override the device setting.

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
     | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | When user verification is changed from preferred to required, it will automatically unpair all security keys that have not undergone user verification during registration or authentication in the past. To identify security keys that have not been registered as security keys that support user verification, see the `fidoUserVerification` field in the [PingID User Detailed Status Report fields](pid_user_detailed_status_report_fields.html). |

     |   |                                                                                                                                                                                                                                                                     |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | To enable passwordless authentication with a security key, you also need to [create a PingFederate policy for passwordless authentication with a security key](../pingid_integrations/pid_configuring_pf_policy_for_passwordless_authentication_security_key.html). |

6. To enforce the PingOne FIDO policy during authentication and registration, select the**Enforce PingOne FIDO Policy** check box.

   |   |                                                                                                                                                                                                                                                                                                                                                                        |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | * This feature is only available for organizations that are using a PingID environment that is integrated with PingOne or created by PingOne.

   * Only the default PingOne FIDO policy is enforced. To edit the policy or change the default policy, see [Managing FIDO policies](http://docs.pingidentity.com/pingone/authentication/p1_managing__fido_policies.html). |

7. Click **Save**.

## Result

Users can pair and authenticate with their security keys.

---

---
title: (Legacy) Configuring the FIDO2 security key for PingID
description: How to configure PingID FIDO2 security key authentication, including passwordless and manual authentication use cases, setup steps, and supported devices.
component: pingid
page_id: pingid:pingid_service_management:configuring_fido2_security_key
canonical_url: http://docs.pingidentity.com/pingid/pingid_service_management/configuring_fido2_security_key.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 16, 2026
section_ids:
  passwordless-security-key: Passwordless security key
  manual-authentication-with-a-fido2-security-key: Manual authentication with a FIDO2 security key
  legacy-security-key-authentication-requirements-and-limitations: (Legacy) Security key authentication requirements and limitations
  passwordless-security-key-2: Passwordless security key
  security-keys-supported: Security keys supported
  legacy-configuring-security-key-authentication: (Legacy) Configuring security key authentication
  about-this-task: About this task
  steps: Steps
  result: Result:
  choose-from: Choose from:
  result-2: Result
  legacy-security-key-use-cases: (Legacy) Security key use cases
---

# (Legacy) Configuring the FIDO2 security key for PingID

Configure FIDO2 security key for PingID authentication. FIDO2 and U2F-compatible security keys enable relying parties to offer a strong cryptographic authentication option for end user security.

Use a security key hardware authenticator to cover many use cases, including those of sensitive environments or users working in environment with limited device or phone access, such as hospitals, financial institutions, or federal buildings.

FIDO2 security keys are fully backward compatible with U2F, enabling PingID to support both FIDO2 and U2F security keys.

When security key authentication is enabled, the user registers the security key and pairs it with their PingID account. This creates a trust between the security key and the user's account, so they can use the security key to authenticate during the sign-on process.

|   |                                                                                           |
| - | ----------------------------------------------------------------------------------------- |
|   | Use security keys for web-based authentication through WebAuthn supporting browsers only. |

## Passwordless security key

You can configure a PingFederate policy to allow users to authenticate with their security key as a first factor authentication, eliminating the need to enter a users name or password, and providing a frictionless and secure sign on experience.

To configure passwordless authentication using a security key:

1. [(Legacy) Configuring security key authentication](configuring_security_key_auth.html) with Resident Key set to **Required**.

2. Configure a PingFederate policy for passwordless authentication with a security key (see [(Legacy) Configuring a PingFederate policy for passwordless authentication with a security key](../pingid_integrations/pid_configuring_pf_policy_for_passwordless_authentication_security_key.html)).

For information about security key requirements and limitations, see [(Legacy) Security key authentication requirements and limitations](security_key_auth_requirements_and_limitations.html).The process of registering a security key is the same for both passwordless and secondary authentication flows. The user is directed to the relevant flow, according to your organization's configuration. Once registered, the same security key can be used to authenticate using either flow. Learn more in [Setting up your security key](http://docs.pingidentity.com/pingid-user-guide/secure_authentication_with_pingid/pid_using_security_key_auth.html) in the PingID User Guide).

## Manual authentication with a FIDO2 security key

PingID integration with Windows login supports the use of FIDO2 security keys for manual authentication, such as if a user does not have an internet or network connection when signing on.

* FIDO2 security key for manual authentication is supported by PingID Integration for Windows login 2.3 or later.

* U2F security key for manual authentication is only supported by PingID Integration for Windows login 2.3 - 2.7.x.

Users must pair a security key and authenticate successfully at least once online, to use it when offline. Learn more in the [PingID End User Guide](http://docs.pingidentity.com/pingid-user-guide/).

## (Legacy) Security key authentication requirements and limitations

When using security keys with PingID, the following requirements and limitations apply:

|   |                                                                                                                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For PingID environments that are integrated with PingOne: From April 15th 2024, the FIDO2 Biometrics and Security Key authentication methods are deprecated and replaced by the more advanced FIDO2 authentication method. Learn more: [Updating a PingID account to use PingOne FIDO2 policy for Passkey support](pid_update_to_fido2_authentication_method.html). |

* Security keys are supported for Web authentication only.

* PingID supports FIDO2 and U2F security keys.

  |   |                                                                                                                         |
  | - | ----------------------------------------------------------------------------------------------------------------------- |
  |   | U2F security keys can only generate a single credential per domain. A device can only be paired by one user per domain. |

* Security keys can be used for web-based authentication through WebAuthn supporting browsers only.

  |   |                                                                                      |
  | - | ------------------------------------------------------------------------------------ |
  |   | If a browser supports the use of a security key, the browser also supports WebAuthn. |

* When authenticating with a mobile device, use of FIDO2 and U2F security keys with PingID:

  * Is supported on Android 7 and later

  * Is supported on iOS 13.3 and later

* Registration and authentication must be performed with a WebAuthn supported browser, such as the latest versions of Google Chrome or Microsoft Edge.

* The use of FIDO2 security keys for manual (offline) authentication:

  * Requires PingID Integration for Windows login 2.3 or later.

* WebAuthn timeout is defined for 2 minutes. The actual timeout value might vary depending on the browser used.

* PingID does not support security keys that require a signed attestation using ECDAA in packed attestation format.

* A user can pair more than one security key with their account.

* The same security key can be used by more than one user if each user is pairing the security key to a different account.

* A user cannot pair the same security key with their account more than once.

* YubiKeys can be paired for either:

  * Security Key FIDO2 authentication

  * YubiKey OTP authentication

  PingID YubiKeys that feature one-time passcode (OTP) support only, or for which you only want to use OTP authentication, should be paired as a YubiKey authentication method rather than as a security key. For more information, see [Configuring YubiKey authentication (Yubico OTP) for PingID](pid_configuring_yubikey_authentication_yubico_otp.html).

* The following limitations should be considered when configuring security key authentication with PingID:

  * Some browsers do not support the use of a FIDO2 security key when **User Verification**is set to **Required**.

  * Some browsers do not allow authentication with a security key when the security key is paired as a resident key.

  * Some browsers do not support security key registration when**Resident Key** is set to **Required**.

* Windows login supports the use of FIDO2 security keys.

  |   |                                                                                                                                                                                                                                          |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If user verification has been set to Required for security keys in the admin portal, this will not affect offline authentication, and users will be able to use their security key for offline authentication without user verification. |

### Passwordless security key

To use a security key for passwordless authentication:

* The security key must support the use of a resident key, and be paired as a resident key.

* When creating a [PingFederate policy for passwordless authentication with a security key](../pingid_integrations/pid_configuring_pf_policy_for_passwordless_authentication_security_key.html) you must use PingID Integration kit 2.10 or later, with PingFederate v9.3 or later.

Some browsers do not support the security key passwordless authentication flow. Passwordless authentication with a security key has been successfully tested on:

* Windows 10 machines running the latest version of Windows Edge, FireFox, Opera, and Chrome.

* Apple Mac 10.15 (Catalina) machines running the latest versions of Windows Edge, Opera, and Chrome.

* Testing has also been performed successfully on Apple Mac 11 (Big Sur), and Mac 12.4 (Monterey).

### Security keys supported

PingID is a FIDO2-certified service and supports any FIDO2 key that complies with the FIDO2 standard.

## (Legacy) Configuring security key authentication

Use the FIDO2 security key for web-based authentication only. The browser with which the user is accessing their resources must support WebAuthn, such as the latest version of Google Chrome or Mozilla Firefox.

### About this task

|   |                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------- |
|   | Define the use of security keys for offline authentication when installing the PingID Integration for Windows Login. |

|   |                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If the browser does not support WebAuthn, the user will be unable to authenticate with the security key and might be unable to authenticate if that is their only authenticating device. |

### Steps

1. Sign on to the admin console.

2. Go to **Setup → PingID → Configuration**.

3. Go to the **Alternate Authentication Methods** section, and in the **Security Key** row, select the **Enable** check box. ![A screen capture of the Alternate Authentication Methods section.](_images/vkb1564020562147.png)

   #### Result:

   The ability to pair and authenticate with a security key is enabled for all users in that organization, and additional security key configuration fields are shown.

   ![mage showing Resident Key and User Verification configuration options for use with a security key.](_images/qzv1668444741877.png)

4. In the **Enable** column, select the **Security Key** check box.

5. **Optional:** In the **Security Key** section, configure the following fields:

   * **Resident Key**. When set to Required, the private key is saved on the security key. To enforce [passwordless authentication](../pingid_integrations/pid_configuring_pf_policy_for_passwordless_authentication_security_key.html) on all authentication attempts, set this field to **Required**.

   * **User Verification**. This option requires the user to perform a gesture using their security key, to validate their identity (for example, using their fingerprint, or entering a PIN code). Select either:

     #### Choose from:

   * **Required**: only security keys that support user verification can be used to authenticate. When the **Resident Key** field is set to **Required**, this option is automatically set to **Required**.

   * **Preferred** (default): user verification is performed if the user's security key supports it, and is skipped if not supported.

   * **Discouraged**: user verification is not performed, even when supported by the user's security key. In cases where user verification is required by the security key itself, this setting does not override the device setting.

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
     | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | When user verification is changed from preferred to required, it will automatically unpair all security keys that have not undergone user verification during registration or authentication in the past. To identify security keys that have not been registered as security keys that support user verification, see the `fidoUserVerification` field in the [PingID User Detailed Status Report fields](pid_user_detailed_status_report_fields.html). |

     |   |                                                                                                                                                                                                                                                                     |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | To enable passwordless authentication with a security key, you also need to [create a PingFederate policy for passwordless authentication with a security key](../pingid_integrations/pid_configuring_pf_policy_for_passwordless_authentication_security_key.html). |

6. To enforce the PingOne FIDO policy during authentication and registration, select the**Enforce PingOne FIDO Policy** check box.

   |   |                                                                                                                                                                                                                                                                                                                                                                        |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | * This feature is only available for organizations that are using a PingID environment that is integrated with PingOne or created by PingOne.

   * Only the default PingOne FIDO policy is enforced. To edit the policy or change the default policy, see [Managing FIDO policies](http://docs.pingidentity.com/pingone/authentication/p1_managing__fido_policies.html). |

7. Click **Save**.

### Result

Users can pair and authenticate with their security keys.

## (Legacy) Security key use cases

The following table outlines common use cases and their expected behaviors when using security key authentication.

|   |                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The results can vary from those described in the table if policy rules are applied. For more information, see [PingID authentication policy](pid_authentication_policy.html). |

| Paired devices                           | Browser                | Results                                                                                                                                                                                               | Reason                                                                                                                                                                                                            |
| ---------------------------------------- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Security key only                        | WebAuthn compliant     | The user is prompted to authenticate using their security key.                                                                                                                                        | Security key is the only allowed authentication method and the browser supports WebAuthn, so the user can authenticate using their security key.                                                                  |
| * Security key (primary)

* Email

* SMS | WebAuthn compliant     | The user is prompted to authenticate using their security key. If **Prompt to Select** is enabled, security key appears in the list of authentication options.                                        | The browser supports security key, which is the user's primary device.                                                                                                                                            |
| Security key only                        | WebAuthn compliant     | `Something went wrong. Try again later.` displays.                                                                                                                                                    | The user did not tap the security key within the required time, or the relevant browser window was not selected when they tapped the security key button. The user should click **Retry** and authenticate again. |
| Security key only                        | Not WebAuthn compliant | `Cannot authenticate with this device` displays.                                                                                                                                                      | The browser does not support the user's current authentication method. The user should try a different browser that is WebAuthn compliant, such as the latest version of Chrome.                                  |
| - Security key (primary)

- Email

- SMS | Not WebAuthn compliant | The user is prompted to authenticate using the next paired device, in this case email or SMS. If **Prompt to Select** is enabled, security key does not appear in the list of authentication options. | The browser is not WebAuthn compliant and does not support the use of a security key. Secondary authentication method is presented to the user.                                                                   |

---

---
title: (Legacy) FIDO2 biometrics authentication requirements and limitations
description: The following list details the requirements and limitations when using FIDO2 platform biometrics with PingID.
component: pingid
page_id: pingid:pingid_service_management:fido2_biometrics_auth_requirements_and_limitations
canonical_url: http://docs.pingidentity.com/pingid/pingid_service_management/fido2_biometrics_auth_requirements_and_limitations.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 18, 2024
section_ids:
  general-requirements: General requirements:
  fido-passkey-requirements: FIDO Passkey requirements:
  passwordless-authentication-requirements: Passwordless authentication requirements:
  general-limitations: General limitations:
  second-factor-authentication-limitations: Second factor authentication limitations:
---

# (Legacy) FIDO2 biometrics authentication requirements and limitations

The following list details the requirements and limitations when using FIDO2 platform biometrics with PingID.

## General requirements:

|   |                                                                                                                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For PingID environments that are integrated with PingOne: From April 15th 2024, the FIDO2 Biometrics and Security Key authentication methods are deprecated and replaced by the more advanced FIDO2 authentication method. Learn more: [Updating a PingID account to use PingOne FIDO2 policy for Passkey support](pid_update_to_fido2_authentication_method.html). |

* FIDO2 biometrics authentication is supported for web authentication only.

* Define an appropriate FIDO2 platform authentication method on the accessing device to pair the device, such as fingerprint or Face ID. If no platform authentication method is defined, the user will not be able to pair the device or authenticate with PingID.

* Perform registration and authentication with a WebAuthn supported browser, such as the latest versions of Google Chrome, Safari, or Microsoft Edge.

* Avoid the use of the same FIDO2 biometrics device by more than one user.

* Passwordless authentication using Mac Touch ID through a Chrome browser is only supported for devices paired after February 23, 2021. Users with devices that were paired to PingID before February 23, 2021 should unpair their device and then pair it again, in order to use passwordless authentication with a Chrome browser.

## FIDO Passkey requirements:

FIDO passkey requirements and limitations are constantly evolving. For a list of the most up-to-date operating systems and browsers supported, see [Device support](https://passkeys.dev/device-support/).

## Passwordless authentication requirements:

* When creating a [PingFederate policy for passwordless authentication with FIDO2 biometrics](../pingid_integrations/pid_configuring_pf_policy_for_passwordless_authentication_fido_biometrics.html), you must use PingID Integration kit 2.7 or later, with PingFederate v9.3 or later.

## General limitations:

* WebAuthn timeout is defined for 2 minutes. The actual timeout value might vary depending on the browser used.

* PingID does not support Android-key attestation.

* A user can pair more than one FIDO2 biometrics device with their account, however, they cannot pair the same FIDO2 biometrics device with their account more than once.

* Some older browser versions might not support FIDO2 biometrics when using incognito or private mode.

* If an an iOS or Mac Touch ID device is paired with PingID, clearing history and website data from the device's Safari settings will prevent a user from using PingID to authenticate. The user must unpair their device and then pair the device again to authenticate with PingID.

## Second factor authentication limitations:

* Android devices that are paired within a workspace can only be used to authenticate in the same workspace.

For troubleshooting, see the relevant section in the PingID User Guide.

---

---
title: (Legacy) FIDO2 biometrics use cases
description: The following table outlines several common use cases and their expected behaviors when using FIDO2 biometrics authentication.
component: pingid
page_id: pingid:pingid_service_management:pid_fido2_biometrics_use_cases
canonical_url: http://docs.pingidentity.com/pingid/pingid_service_management/pid_fido2_biometrics_use_cases.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 18, 2024
---

# (Legacy) FIDO2 biometrics use cases

The following table outlines several common use cases and their expected behaviors when using FIDO2 biometrics authentication.

|   |                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If policy rules are configured, the results might vary from those described in the table. For more information, see [PingID authentication policy](pid_authentication_policy.html). |

| Paired devices                                                                                    | Browser                         | Results                                                                                                                                                                                                                                                            | Reason                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| FIDO2 biometrics device only                                                                      | WebAuthn Platform compliant     | The browser prompts the user to authenticate using their FIDO2 biometrics device.                                                                                                                                                                                  | FIDO2 biometrics is the only authentication method, and the browser supports WebAuthn platform, so the user can authenticate using their FIDO2 biometrics device.                                                                                                          |
| * FIDO2 biometrics (primary)

* Email

* SMS                                                      | WebAuthn platform compliant     | The browser prompts the user to authenticate using their FIDO2 biometrics device. If the **Prompt to Select** setting is enabled, FIDO2 Biometrics appears in the list of authentication options.                                                                  | The browser supports FIDO2 biometrics, which is the user's primary device.                                                                                                                                                                                                 |
| - FIDO2 biometrics - Windows Hello (primary)

- FIDO2 biometrics - Android device

- Email

- SMS | WebAuthn platform complaint     | If the user tries to access their account with their Android device, they are prompted to authenticate using that device, even though it is not their primary device.                                                                                              | If more than one FIDO2 biometrics device is paired with a user's account, when accessing with a FIDO2 device, the browser prompts the user to authenticate with the current accessing device, regardless of which FIDO2 device is the primary device.                      |
| FIDO2 biometrics only                                                                             | Not WebAuthn Platform compliant | The browser displays the following message: `This browser doesn't support your current authentication method. Try a different browser or contact your administrator.`                                                                                              | The browser doesn't support the user's current authentication method. The user must either use a different browser that is WebAuthn compliant, such as the latest version of Chrome or Microsoft Edge, or use a FIDO2 biometrics device that is paired with their account. |
| * FIDO2 biometrics (primary)

* Email

* SMS                                                      | Not WebAuthn platform compliant | The browser prompts the user to authenticate using the next paired device. In this example, the user must authenticate using email or SMS. If the **Prompt to Select** setting is enabled, FIDO2 biometrics does not appear in the list of authentication options. | The browser is not Webauthn platform compliant and does not support the user of a FIDO2 biometrics device. The FIDO2 biometrics option is not shown and only the secondary authentication methods are presented to the user.                                               |

---

---
title: (Legacy) Security key authentication requirements and limitations
description: When using security keys with PingID, the following requirements and limitations apply:
component: pingid
page_id: pingid:pingid_service_management:security_key_auth_requirements_and_limitations
canonical_url: http://docs.pingidentity.com/pingid/pingid_service_management/security_key_auth_requirements_and_limitations.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 18, 2024
section_ids:
  passwordless-security-key: Passwordless security key
  security-keys-supported: Security keys supported
---

# (Legacy) Security key authentication requirements and limitations

When using security keys with PingID, the following requirements and limitations apply:

|   |                                                                                                                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For PingID environments that are integrated with PingOne: From April 15th 2024, the FIDO2 Biometrics and Security Key authentication methods are deprecated and replaced by the more advanced FIDO2 authentication method. Learn more: [Updating a PingID account to use PingOne FIDO2 policy for Passkey support](pid_update_to_fido2_authentication_method.html). |

* Security keys are supported for Web authentication only.

* PingID supports FIDO2 and U2F security keys.

  |   |                                                                                                                         |
  | - | ----------------------------------------------------------------------------------------------------------------------- |
  |   | U2F security keys can only generate a single credential per domain. A device can only be paired by one user per domain. |

* Security keys can be used for web-based authentication through WebAuthn supporting browsers only.

  |   |                                                                                      |
  | - | ------------------------------------------------------------------------------------ |
  |   | If a browser supports the use of a security key, the browser also supports WebAuthn. |

* When authenticating with a mobile device, use of FIDO2 and U2F security keys with PingID:

  * Is supported on Android 7 and later

  * Is supported on iOS 13.3 and later

* Registration and authentication must be performed with a WebAuthn supported browser, such as the latest versions of Google Chrome or Microsoft Edge.

* The use of FIDO2 security keys for manual (offline) authentication:

  * Requires PingID Integration for Windows login 2.3 or later.

* WebAuthn timeout is defined for 2 minutes. The actual timeout value might vary depending on the browser used.

* PingID does not support security keys that require a signed attestation using ECDAA in packed attestation format.

* A user can pair more than one security key with their account.

* The same security key can be used by more than one user if each user is pairing the security key to a different account.

* A user cannot pair the same security key with their account more than once.

* YubiKeys can be paired for either:

  * Security Key FIDO2 authentication

  * YubiKey OTP authentication

  PingID YubiKeys that feature one-time passcode (OTP) support only, or for which you only want to use OTP authentication, should be paired as a YubiKey authentication method rather than as a security key. For more information, see [Configuring YubiKey authentication (Yubico OTP) for PingID](pid_configuring_yubikey_authentication_yubico_otp.html).

* The following limitations should be considered when configuring security key authentication with PingID:

  * Some browsers do not support the use of a FIDO2 security key when **User Verification**is set to **Required**.

  * Some browsers do not allow authentication with a security key when the security key is paired as a resident key.

  * Some browsers do not support security key registration when**Resident Key** is set to **Required**.

* Windows login supports the use of FIDO2 security keys.

  |   |                                                                                                                                                                                                                                          |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If user verification has been set to Required for security keys in the admin portal, this will not affect offline authentication, and users will be able to use their security key for offline authentication without user verification. |

## Passwordless security key

To use a security key for passwordless authentication:

* The security key must support the use of a resident key, and be paired as a resident key.

* When creating a [PingFederate policy for passwordless authentication with a security key](../pingid_integrations/pid_configuring_pf_policy_for_passwordless_authentication_security_key.html) you must use PingID Integration kit 2.10 or later, with PingFederate v9.3 or later.

Some browsers do not support the security key passwordless authentication flow. Passwordless authentication with a security key has been successfully tested on:

* Windows 10 machines running the latest version of Windows Edge, FireFox, Opera, and Chrome.

* Apple Mac 10.15 (Catalina) machines running the latest versions of Windows Edge, Opera, and Chrome.

* Testing has also been performed successfully on Apple Mac 11 (Big Sur), and Mac 12.4 (Monterey).

## Security keys supported

PingID is a FIDO2-certified service and supports any FIDO2 key that complies with the FIDO2 standard.

---

---
title: (Legacy) Security key use cases
description: The following table outlines common use cases and their expected behaviors when using security key authentication.
component: pingid
page_id: pingid:pingid_service_management:pid_security_key_use_cases
canonical_url: http://docs.pingidentity.com/pingid/pingid_service_management/pid_security_key_use_cases.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 18, 2024
---

# (Legacy) Security key use cases

The following table outlines common use cases and their expected behaviors when using security key authentication.

|   |                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The results can vary from those described in the table if policy rules are applied. For more information, see [PingID authentication policy](pid_authentication_policy.html). |

| Paired devices                           | Browser                | Results                                                                                                                                                                                               | Reason                                                                                                                                                                                                            |
| ---------------------------------------- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Security key only                        | WebAuthn compliant     | The user is prompted to authenticate using their security key.                                                                                                                                        | Security key is the only allowed authentication method and the browser supports WebAuthn, so the user can authenticate using their security key.                                                                  |
| * Security key (primary)

* Email

* SMS | WebAuthn compliant     | The user is prompted to authenticate using their security key. If **Prompt to Select** is enabled, security key appears in the list of authentication options.                                        | The browser supports security key, which is the user's primary device.                                                                                                                                            |
| Security key only                        | WebAuthn compliant     | `Something went wrong. Try again later.` displays.                                                                                                                                                    | The user did not tap the security key within the required time, or the relevant browser window was not selected when they tapped the security key button. The user should click **Retry** and authenticate again. |
| Security key only                        | Not WebAuthn compliant | `Cannot authenticate with this device` displays.                                                                                                                                                      | The browser does not support the user's current authentication method. The user should try a different browser that is WebAuthn compliant, such as the latest version of Chrome.                                  |
| - Security key (primary)

- Email

- SMS | Not WebAuthn compliant | The user is prompted to authenticate using the next paired device, in this case email or SMS. If **Prompt to Select** is enabled, security key does not appear in the list of authentication options. | The browser is not WebAuthn compliant and does not support the use of a security key. Secondary authentication method is presented to the user.                                                                   |

---

---
title: Add your branding to PingID
description: About branding customization options in the PingID admin portal and where to learn how to set it up.
component: pingid
page_id: pingid:pingid_service_management:pid_add_your_branding_to_pid
canonical_url: http://docs.pingidentity.com/pingid/pingid_service_management/pid_add_your_branding_to_pid.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 16, 2026
---

# Add your branding to PingID

Customize PingID to include custom colors, logo, and background.

You can customize your end users' PingID experience to complement your organization's brand by applying your organizations branding elements to the PingID enrollment screens and selected mobile application elements. You can define your organization's custom colors, logo, and background.

The benefits of customizing PingID with your branding include:

* Alignment with the organization's "look and feel"

* A customized and familiar end-user experience

* Reduced end-user confusion and suspicion

Apply your organization's branding to the following elements:

* Out-of-the-box user enrollment screens. Learn more in [Customizing the PingID enrollment page (legacy)](pid_customizing_enrollment_page_legacy.html).

* End-user mobile authenticating devices, such as smart phones, swipe screen. Learn more in [Customizing the PingID mobile app swipe screen](pid_customizing_mobile_app_swipe_screen.html).

  |   |                                                                                                                            |
  | - | -------------------------------------------------------------------------------------------------------------------------- |
  |   | In PingID mobile app 2.0 and later, swipe screen settings aren't applied because the swipe screen feature is discontinued. |

* PingID App home screen. Learn more in [Customizing the PingID mobile app home screen](pid_customizing_mobile_app_home_screen.html).

  |   |                                                                                                                                                                                                                                                                            |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | In PingID mobile app 2.0 and later, the branding configured under **PingID Home** is applied to the **My Organizations** screen. The logo from this section is only used if a corporate logo isn't defined on the [Enrollment page](pid_customizing_enrollment_page.html). |

  ![A screen capture of a custom branding for the PingID app home screen.](_images/ogh1564020971023.png)

---

---
title: Adding a new MDM token
description: Add a new MDM token in PingID.
component: pingid
page_id: pingid:pingid_service_management:pid_adding_new_mdm_token
canonical_url: http://docs.pingidentity.com/pingid/pingid_service_management/pid_adding_new_mdm_token.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 30, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding a new MDM token

Add a new MDM token in PingID.

## About this task

Multiple keys can coexist, for example, for allowing time for rotating keys and the time it takes to phase in new keys and retire old ones. PingID checks all listed keys to verify a match with the key submitted in the authentication request.

|   |                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------- |
|   | The MDM does not retain multiple values for the same token. Support for multiple keys is provided through PingID. |

## Steps

1. Go to **Setup → PingID → DEVICE & PAIRING**.

2. In the **DEVICE REQUIREMENTS** section, click **+Add**.

   ![Screen capture of the PingID admin console showing the Device & Pairing tab after clicking +Add.](_images/fov1564020701514.png)

3. From the **Select a Condition** list, select **Mobile Device Management**.

4. Click the **Expand** icon for **MOBILE DEVICE MANAGEMENT REQUIRED**.

5. Click **[icon: plus, set=fa]Generate New Token** to create a new PingID key for MDM.

   ![Screen capture of the expanded Mobile Device Management Required section.](_images/zon1564020719034.png)

   |   |                                                                                      |
   | - | ------------------------------------------------------------------------------------ |
   |   | The generated date following each token indicates the date and time of its creation. |

6. Click **Save**.

7. Copy the value of the new **SHARED TOKEN** key.

8. Update the token key in the MDM system:

   1. Sign on to the MDM system, and go to the app configuration settings page.

   2. Update the `PINGID_MDM_TOKEN` token key.

   3. Delete the existing key value. In its place, paste the value of the new **SHARED TOKEN** key that you copied from the PingID admin portal.

   See the following examples for the supported MDM systems:

   * [Updating a PingID token in Workspace ONE UEM](pid_updating_token_workspace_one_uem.html)

   * [Updating a PingID token in MobileIron](pid_updating_token_in_mobileiron.html)

   * [Updating a PingID token in Microsoft Intune](pid_updating_token_in_microsoft_intune.html)

---

---
title: Adding a PingFederate application
description: You can add PingFederate applications to the applications list while creating a new policy.
component: pingid
page_id: pingid:pingid_service_management:pid_adding_pf_applicating
canonical_url: http://docs.pingidentity.com/pingid/pingid_service_management/pid_adding_pf_applicating.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 25, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
  result-2: Result:
  result-3: Result:
  result-4: Result:
---

# Adding a PingFederate application

You can add PingFederate applications to the applications list while creating a new policy.

## About this task

By default, the applications list includes the following applications:

* **Device Management**: This application enables a user to manage their own devices, including adding, editing, or deleting multiple devices through the **Devices** page.

* **Password Reset**: This application enables users to reset their own password.

|   |                                                            |
| - | ---------------------------------------------------------- |
|   | App-specific policies require PingID Adapter 1.4 or later. |

## Steps

1. In the admin portal, go to **Setup → PingID → Policy**, and click the **Web** tab.

   ### Result:

   A list of all the existing policies displays.

   ![A screen capture of the Policy page displaying a lit of the existing policies.](_images/ttv1564020580517.png)

2. Click **[icon: plus, set=fa]Add Policy**.

   ### Result:

   The **New Policy** window displays with the **Applications** list.

   ![A screen capture of the Target section displaying the Applications and Groups sections and listing.](_images/btr1564020583331.png)

3. In the **PingFederate Applications** section, click **[icon: plus, set=fa]Add Application**.

   ### Result:

   The **PingFederate Application** window appears.

   ![A screen capture of the PingFederate Application window.](_images/bth1564020583950.png)

4. In the **PingFederate Application** window, enter the following information:

   * **Name**: Enter the name of the application (max. 20 characters).

   * **ID**: Enter the application ID for the application. See [unique application ID](pid_defining_pf_application_id_attributes.html).

   * **Add application to target**: Select this check box to add the application to the new policy that you just created.

5. Click **Save**.

   ### Result:

   The new application is saved and appears in the **Applications** list.

---

---
title: Adding the PingID app for Android in Microsoft Intune
description: To ensure that PingID app configurations can be pushed to Android devices, configure Android for Work for the organization's mobile device management (MDM).
component: pingid
page_id: pingid:pingid_service_management:pid_adding_app_for_android_in_microsott_intune
canonical_url: http://docs.pingidentity.com/pingid/pingid_service_management/pid_adding_app_for_android_in_microsott_intune.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 28, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  result: Result:
  result-2: Result:
  result-3: Result:
  next-steps: Next steps
---

# Adding the PingID app for Android in Microsoft Intune

To ensure that PingID app configurations can be pushed to Android devices, configure Android for Work for the organization's mobile device management (MDM).

## Before you begin

In the Intune dashboard, configure Android work profile devices. Find more information on the [InTune documentation](https://learn.microsoft.com/en-us/intune/intune-service/user-help/enroll-device-android-work-profile).

## About this task

This is an example configuration of Android for Work without G Suite. You can configure Android for Work for MDM with G Suite.

## Steps

1. Go to the Microsoft Azure portal at [https://portal.azure.com](https://portal.azure.com/).

2. Go to **Intune → Home → Client Apps → Managed Google Play**.

3. In the **Client Apps - Managed Google Play** window, click **Open the Managed Google Play Store**.

   ![A screen capture of the Client Apps - Managed Google Play window, highlighting the Open the Managed Google Play Store app.](_images/kek1564020746340.png)

   ### Result:

   Google Play opens in a new browser tab or window.

4. Search for the PingID app and select it.

   ![A screen capture of Google Play search results, showing the PingID app.](_images/vks1564020747191.png)

5. Click **Approve**.

   ![A screen capture of the PingID app in Google Play.](_images/fsn1564020748917.png)

   |   |                                                                       |
   | - | --------------------------------------------------------------------- |
   |   | You might be asked to sign on as a managed Google Play administrator. |

   ### Result:

   The **Client Apps - Apps** window is displayed.

6. From the **Apps** list, select the PingID Managed Google Play app, and then from the left-hand menu, click **Assignments**.

   ![A screen capture of the Client Apps - Apps window, highlighting the PingID Managed Google Play App entry.](_images/azj1564020749604.png)

   ### Result:

   The **PingID - Assignments** window is displayed.

7. In the **PingID - Assignments** window, assign the PingID Android app to user groups.

   To create, manage and assign apps to groups, consult the relevant Intune documentation.

   ![A screen capture of the PingID - Assignments window.](_images/gby1564020750402.png)

## Next steps

See [Setting PingID app configuration policies for Microsoft Intune](pid_setting_app_configuration_policies_for_microsoft_intune.html).

---

---
title: Adding the PingID app for iOS in Microsoft Intune
description: Configure PingID as an MDM-managed app for iOS devices in Microsoft Intune.
component: pingid
page_id: pingid:pingid_service_management:pid_adding_pid_app_ios_in_microsoft_intune
canonical_url: http://docs.pingidentity.com/pingid/pingid_service_management/pid_adding_pid_app_ios_in_microsoft_intune.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 26, 2024
section_ids:
  steps: Steps
  result: Result:
  result-2: Result:
  result-3: Result:
  result-4: Result:
  result-5: Result:
  next-steps: Next steps
---

# Adding the PingID app for iOS in Microsoft Intune

Configure PingID as an MDM-managed app for iOS devices in Microsoft Intune.

## Steps

1. Go to the Microsoft Azure portal at [https://portal.azure.com](https://portal.azure.com/).

2. Go to **Intune → Client Apps → Apps → +Add → Add App**.

3. From the **App Type** list, select **iOS**.

   ![A screen capture of the Add App window and the App Type list. The list has multiple sections of apps: Store App, which has Android, iOS, Windows Phone 8.1, and Windows; Office 365 Suite, which has Windows 10 and macOS; and Other, which has Web link, Built-in app, Line-of-business app, and Windows app (Win32) - preview.](_images/xhb1564020693727.png)

4. In the **Search the App Store** section, click **Select App**.

   ![A screen capture of the Add App window and the Search the App Store section.](_images/wsh1564020694371.png)

   ### Result:

   The **Search the App Store** window opens.

   ![A screen capture of the Search the App Store window.](_images/cir1564020694939.png)

5. In the search field, enter th e PingID mobile app's iTunes App Store URL: <https://itunes.apple.com/us/app/pingid/id891247102?mt=8>.

   ### Result:

   The PingID app is displayed.

   ![A screen capture of the Search the App Store window showing the PingID app in the search results.](_images/lwh1564020695575.png)

6. Click the PingID app.

   ### Result:

   You are returned to the **Add App** window with the **Configure** option enabled.

7. To open the **App Information** window, click **Configure**.

8. In the **App Information** window, make any required changes, and then click **OK**.

   ![A screen capture of the App Information window. Required fields are marked by an asterisk.](_images/bpb1564020696261.png)

   ### Result:

   In the **Add App** window, the **Add** button is enabled.

9. In the **Add App** window, click **Add**.

   ### Result:

   Your app appears in the list of client apps.

   ![A screen capture of the Client Apps - Apps window, highlighting the PingID iOS store app.](_images/xqi1564020697024.png)

## Next steps

See [Setting PingID app configuration policies for Microsoft Intune](pid_setting_app_configuration_policies_for_microsoft_intune.html).

---

---
title: Allowed authentication methods
description: Define the authentication methods you want to make available for the policy in the Allowed Authentication Methods section. Only the selected allowed authentication methods are listed as options in the authentication rule Action list.
component: pingid
page_id: pingid:pingid_service_management:pid_allowed_auth_methods
canonical_url: http://docs.pingidentity.com/pingid/pingid_service_management/pid_allowed_auth_methods.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 8, 2023
---

# Allowed authentication methods

Define the authentication methods you want to make available for the policy in the **Allowed Authentication Methods** section. Only the selected allowed authentication methods are listed as options in the authentication rule **Action** list.

|   |                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If a new authentication method is added as a PingID capability and the **All Methods** check box is not selected in the **Allowed Authentication Methods** section, you must edit each policy and select the check box of the new authentication method manually to include it in a policy. |

A description of the allowed authentication methods is shown in the following table.

**Authentication methods allowed per policy**

| Allowed Authentication Method | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **All Methods**               | Permit the use of all authentication methods currently configured for the organization.When the **All methods** check box is selected:- All available authentication methods are permitted at the policy level.

- If additional authentication methods are added to PingID in the future, they are automatically applied to the policy.

- Within a policy rule, all available authentication methods are listed in the rule **Actions** list.

- Deprecated authentication actions appear and can be selected in policy rule **Actions** list. See [Deprecated authentication actions](pid_deprecated_actions.html).If the **All methods** check box is not selected:- Only the specific authentication methods selected in the **Allowed Authentication Methods** list are available for the user to authenticate.

- If additional authentication methods are added to PingID in the future, they are not applied to existing policies automatically. Existing policies must be edited individually and the new authentication method added manually in order to apply it to the policy.

- Within a rule, only the selected authentication methods are listed in the authentication actions in addition to relevant default actions, such as **Approve**, **Deny**, and **Authenticate**.

- Deprecated authentication actions are not available in the policy rule **Actions** list. |
| **Authenticator app**         | Authentication using an authenticator app, such as Google authenticator, is permitted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Backup Authentication**     | Authentication using a backup authentication method is permitted. This option is useful if a user forgets their device, or it is lost or stolen.The **Forgot your device?** link only appears if:- Either the **Authenticate** rule action, or a rule action that includes a mobile device authentication method such as **Mobile App Biometrics**, is configured.

- At least one backup authentication method is defined. See [Configuring backup authentication methods](pid_configuring_backup_authentication_methods.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Desktop**                   | Authentication by a desktop app is permitted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Email**                     | Authentication by email is permitted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **FIDO2 Biometrics**          | Authentication by a FIDO2 biometrics device is permitted for web-based policies only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Mobile App Biometrics**     | Authentication by a supported biometrics devices is permitted and applied according to the configuration defined in the Admin portal.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Number matching**           | Authenticate by number matching is permitted.- Number matching has priority over**Mobile App Biometrics** and**Swipe** authentication methods.

- If **Mobile app biometrics** is set to **Require** in the **Configuration** tab, the user must authenticate successfully using biometrics and then authenticate using number matching.

- Number matching is only supported by apps that are using web-based authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Oath Token**                | Authentication using an OATH Token is permitted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **One-time passcode**         | Authentication using a one-time passcode (OTP) obtained using PingID mobile app is permitted.&#xA;&#xA;If this option is not selected, fallback to a OTP and direct passcode usage are not allowed, even if it is enabled in the Configuration page.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **SMS**                       | Authentication using an OTP obtained through SMS is permitted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Security Key**              | Authentication using a security key is permitted for web-based policies only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Swipe**                     | Authentication using swipe is permitted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Voice**                     | Authentication using an OTP obtained through voice message is permitted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **YubiKey**                   | Authentication using a YubiKey is permitted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

---

---
title: Authentication method selection and priority - use cases
description: See the following table for detailed examples of use cases where the configuration at the organization level can affect the implementation of an authentication policy.
component: pingid
page_id: pingid:pingid_service_management:pid_auth_methods_use_cases
canonical_url: http://docs.pingidentity.com/pingid/pingid_service_management/pid_auth_methods_use_cases.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 9, 2023
---

# Authentication method selection and priority - use cases

See the following table for detailed examples of use cases where the configuration at the organization level can affect the implementation of an authentication policy.

**Authentication method selection by specific use cases**

| Use Case | User Paired Devices                                                                                                                                                                                    | Allowed Authentication Methods                   | Rule Action                      | Result                                                                                                                                         | Reason                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------ | -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1        | * SMS (primary)

* Email                                                                                                                                                                               | All methods                                      | Email                            | User is requested to authenticate through email                                                                                                | Although the primary is SMS, the user is requested to authenticate using email as the rule action requires email.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 2        | - Desktop (primary)

- Email

- YubiKey                                                                                                                                                                | YubiKey                                          | Authenticate                     | User is requested to authenticate with YubiKey                                                                                                 | User is automatically prompted to authenticate using a YubiKey, regardless of whether the configuration is set to **Default to Primary** or **Prompt user to select**. This is because the user only has one allowed authentication method paired with their account.                                                                                                                                                                                                                                                                                                       |
| 3        | * The PingID mobile app (primary)

* SMS

* Voice                                                                                                                                                      | SMS/ Voice/ Email                                | Authenticate                     | User is unable to authenticate                                                                                                                 | - **Default to Primary**: Even though the user's primary device is disallowed (PingID Mobile app), the user is prompted to authenticate with the device that was enrolled first out of the list of allowed secondary devices.

- **Prompt user to select:** the user is presented with a list of secondary devices. The user selects the secondary device with which they want to authenticate.                                                                                                                                                                             |
| 4        | * SMS (primary)

* YubiKey

* Email                                                                                                                                                                    | Mobile App Biometrics/ Swipe / One-time passcode | Authenticate                     | Authentication denied                                                                                                                          | User does not have one of the allowed authentication methods paired with their account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 5        | - The PingID mobile app (primary)

- Desktop

- Voice                                                                                                                                                  | All methods                                      | SMS                              | Authentication denied                                                                                                                          | User does not have the required authentication method paired with their account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 6        | The PingID mobile app (Swipe disabled)                                                                                                                                                                 | Mobile App Biometrics/ Swipe                     | Authenticate                     | Authentication denied                                                                                                                          | Swipe is disabled in the PingID mobile app and the user is unable to receive a push notification.As a one-time passcode (OTP) is not included in the **Allowed Authentication Methods**, the user cannot use an OTP, even if OTP Fallback is enabled.                                                                                                                                                                                                                                                                                                                       |
| 7        | The PingID mobile app (Swipe disabled)                                                                                                                                                                 | All methods                                      | Mobile App Biometrics (required) | Authentication denied                                                                                                                          | Mobile App Biometrics (required) permits authentication with biometrics only, and does not allow use of an OTP."Swipe disabled" prevents the user from receiving a push notification to their device, preventing the user from authenticating with biometrics.                                                                                                                                                                                                                                                                                                              |
| 8        | The PingID mobile app where:- Device supports biometrics

- Biometrics not defined on device                                                                                                           | Mobile App Biometrics                            | Mobile App Biometrics (required) | The user is able to authenticate using swipe or their device passcode in the event that their device screen is locked.                         | If a device does not support biometrics, PingID allows the user to authenticate using swipe as an exception. If the device supports biometrics, but biometrics are not defined on the device, the user can use swipe.This is possible because biometrics is enabled (and not required) by the biometrics configuration                                                                                                                                                                                                                                                      |
| 9        | The PingID mobile app where:- Device does not support biometrics

- Biometrics required at configuration level                                                                                         | Mobile App Biometrics                            | Mobile App Biometrics (required) | The user is able to authenticate using swipe or their device passcode in the event that their device screen is locked.                         | Although biometrics is required, because the user's device does not support biometrics, the user is still able to authenticate with swipe (if device unlocked), or using their device passcode (if device is locked).                                                                                                                                                                                                                                                                                                                                                       |
| 10       | The PingID mobile app where:- Device supports biometrics

- Biometrics not defined on device

- Biometrics required at configuration level                                                             | Mobile App Biometrics                            | Mobile App Biometrics (required) | The user is not able to authenticate                                                                                                           | Biometrics are required at the configuration level, and biometrics authentication is possible on the user's device. The user is not able to authenticate because they have not defined biometrics on the device.                                                                                                                                                                                                                                                                                                                                                            |
| 11       | The PingID mobile app where:- Device supports biometrics

- Biometrics are defined on device

- Biometrics required at configuration level                                                             | Mobile App Biometrics / Swipe                    | Authenticate                     | User is able to authenticate with biometrics                                                                                                   | Biometrics have a higher priority over swipe, and the user is prompted to authenticate with biometrics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 12       | * Security key (primary)

* Email

* SMSWhere the browser used does not provide WebAuthn support required for security key.                                                                            | All methods                                      | Authenticate                     | User is able to authenticate with email or SMS                                                                                                 | - **Default to Primary**: Even though the user's primary device is disallowed because the browser does not support WebAuthn, the user is prompted to authenticate with the secondary device that was enrolled first out of the list of allowed secondary devices.

- **Prompt user to select:** A security key is not included in the list of devices, as the browser does not support WebAuthn. The user is presented with a list of secondary devices only. The user selects the secondary device with which they want to authenticate.                                   |
| 13       | * Security key (primary)

* Email

* SMS Where the browser used does not provide WebAuthn support required for security key.                                                                           | All methods                                      | Security Key                     | User is unable to authenticate                                                                                                                 | Even though the user has a security key paired with their account, they are signing on using a browser that does not support WebAuthn.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 14       | - The PingID mobile app (primary)

- Security key

- EmailWhere the browser supports WebAuthn. Policy rule **authenticating from a new device** is applied and requires a security key.                | All methods                                      | Security key                     | User is able to authenticate with a Security key only. In the case of a phishing attack, the user is not able to authenticate with any device. | * If authenticating from a new device a security key is required.

* If the user is subject to a phishing attack, PingID can distinguish between a known and a fraudulent copy of a web page. If fraudulent, PingID does not recognize the source and triggers the **accessing from new device** policy rule. Even though the user has other devices paired, they are prompted to authenticate using a security key only, and cannot change device due to the policy rule restrictions.This configuration guards all devices against a phishing attack.                     |
| 15       | - FIDO2 biometrics (primary)

- Email

- SMSWhere the browser used does not provide WebAuthn Platform support.                                                                                         | All methods                                      | FIDO2 Biometrics                 | User is unable to authenticate                                                                                                                 | Even though the user has a FIDO2 biometrics device paired with their account, they are signing on using a browser that does not support WebAuthn.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 16       | * The PingID mobile app (primary)

* FIDO2 Biometrics

* EmailWhere the browser supports a WebAuthn Platform. Policy rule **authenticating from a new device** is applied and requires a security key. | All methods                                      | FIDO2                            | User is able to authenticate with FIDO2 only. In the case of a phishing attack, the user is not able to authenticate with any device.          | - If authenticating from a new device, FIDO2 biometrics device is required.

- If the user is subject to a phishing attack, PingID can distinguish between a known and a fraudulent copy of a web page. If fraudulent, PingID does not recognize the source and triggers the **accessing from new device** policy rule. Even though the user has other devices paired, they are prompted to authenticate using a FIDO2 biometrics device only and cannot change device due to the policy rule restrictions.This configuration guards all devices against a phishing attack. |

---

---
title: Authentication policy
description: Overview of PingID authentication policy configuration, including per-app, per-group, web, and VPN/SSH policy options.
component: pingid
page_id: pingid:pingid_service_management:pid_authentication_policy
canonical_url: http://docs.pingidentity.com/pingid/pingid_service_management/pid_authentication_policy.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 16, 2026
---

# Authentication policy

Define policies per application or per group of applications for any application defined in PingFederate. You can also apply a policy to one or more user groups.

Define your PingID authentication policy in the **PingID > POLICY** tab, according to your unique security needs.

You can define a policy for high security applications and a separate policy for low security applications. You can apply a separate policy to your HR user group, IT user group, or Finance group.

Allowed authentication methods:

* Define or limit the authentication methods that can be used per policy. Learn more in [Policy and rule authentication methods](pid_policy_and_rule_authentication_methods.html). For example, define stronger authentication methods, such as fingerprint authentication, for high security apps and a wider range of allowed authentication methods for less sensitive apps.

Different subsets of rules can be configured, depending on whether the protected application is accessed through the web or a VPN or SSH.

The VPN and SSH policy can be applied globally by configuring one or more rules in the default policy. Learn more in [VPN and SSH policy](pid_configuring_radius_pcv_and_ssh_policy.html).

The web authentication policy can be applied either:

* Globally using the default policy: The global (default) policy is only applied if no other web policy is defined or if no other web policy is applied during the authentication session. Learn more in [Globally using the default policy](pid_configuring_global_authentication_policy_default.html).

* Per application or group: for PingFederate applications, you can apply a policy to one or more applications or to one or more user groups or both. If more than one policy exists for an application or user group, the policies are applied in the order that they appear in the **POLICY** list, as outlined in the policy rules. For more information, see [Per application or group](pid_configuring_app_group_authentication_policy.html).

Learn more in [Web authentication policy](pid_web_authentication_policy_configuration.html).

---

---
title: Authentications by type
description: The Authentications by Type chart shows the distribution of authentications by authentication method over the specified period.
component: pingid
page_id: pingid:pingid_service_management:pid_dashboard_authentications_by_type
canonical_url: http://docs.pingidentity.com/pingid/pingid_service_management/pid_dashboard_authentications_by_type.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 30, 2022
---

# Authentications by type

The **Authentications by Type** chart shows the distribution of authentications by authentication method over the specified period.

![Authentications by type chart](_images/sdm1593522043406.png)

For more information, see:

* [Overview of PingID authentication types](../introduction_to_pingid/pid_overview_of_authentication_types.html)

* [Configure PingID authentication](pid_configure_authentication.html)

---

---
title: Branding fields
description: The branding fields are on the left of the page. On the right is the Preview Full Size image.
component: pingid
page_id: pingid:pingid_service_management:pid_branding_fields
canonical_url: http://docs.pingidentity.com/pingid/pingid_service_management/pid_branding_fields.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 10, 2024
section_ids:
  preview-image: Preview Image
  logo: Logo
  button-link-color-button-text: Button & Link Color, Button Text
  background-color: Background Color
  background-image: Background Image
  text-color: Text Color
---

# Branding fields

## Preview Image

The branding fields are on the left of the page. On the right is the **Preview Full Size** image.

![A screen capture of the New Enrollment Page window, the logo branding fields, and the Preview Full Size image.](_images/aqe1586172556199.png)

The **Preview Full Size** section reflects your current edits. To enlarge the preview, click anywhere inside the image. Click the image again to restore it to its original size.

|   |                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The branding fields can be entered all or in parts and in any order. Click **Save** to save your changes. Click **Discard Changes** to revert to the previous state. |

## Logo

|                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![A screen capture of the Logo section with options to decline a logo or upload your logo.](_images/gdm1586172908324.png) | **No Logo**This is the default.**Corporate Logo**This option is available after the admin uploads the organization logo to the dock settings. For more information, see [Assign branding and design](http://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_assign_branding_designn.html) in the PingOne for Enterprise Administration Guide.**Upload Logo**When you select this option, the **Select File** button appears. Click **Select File** to select the logo image file.&#xA;&#xA;The logo can be a JPEG, JPG, GIF, or PNG file with a maximum size of 5 MB.&#xA;&#xA;The logo is shared with Swipe Screen. |

## Button & Link Color, Button Text

|                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![A screen capture of Button & Link Color and Button Text fields.](_images/diw1586189512055.png) | These fields relate to the **Start** and **Skip** fields in the preview.![A screen capture of the Welcome to PingID preview page with the customized Start and Skip buttons.](_images/rpx1586189760167.png)Click these and all subsequent color fields to open a standard color selector.![An image of a standard color selector.](_images/efl1586189867746.png)The color you select displays in hexadecimal format in the **Button & Link Color** and **Button Text** fields. You can also enter a hexadecimal number directly in the fields.- The **Button & Link** color setting applies to the **Start** button background color and the **Skip** text color.

- The **Button Text** color applies to the **Start** button text color only.Click **Reset** to revert to the default value. |

## Background Color

Click **Background Color** to open a standard color selector. Click **Reset** to restore the default setting.

|   |                                                                             |
| - | --------------------------------------------------------------------------- |
|   | If you are using a background image, the background color does not display. |

## Background Image

In the **Background Image** section, click **Remove File** to remove the default image and reveal the **Select File** icon.

![A screen capture of the Background Image section with the reset or upload options.](_images/tbq1586190507329.png)

Click the **Select File** icon to select a background image. Click **Reset** to restore the default setting.

|   |                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If your image is truncated or distorted, you might need to physically re-size it before uploading. The PingID enrollment message background assumes a display aspect ratio of 16:9. |

## Text Color

Click **Text color** opens the standard color selector. This color applies to the text of the Welcome message. Click **Reset** to restore the default setting.

---

---
title: Configure PingID authentication
description: Overview of PingID authentication configuration options section with links to configuring mobile app, desktop app, FIDO2, YubiKey, OATH, email, and SMS/voice methods.
component: pingid
page_id: pingid:pingid_service_management:pid_configure_authentication
canonical_url: http://docs.pingidentity.com/pingid/pingid_service_management/pid_configure_authentication.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 16, 2026
section_ids:
  pingid-mobile-app-authentication: PingID mobile app authentication
  pingid-desktop-app-authentication: PingID desktop app authentication
  fido2-biometrics: FIDO2 biometrics
  fido2-security-key: FIDO2 security key
  yubikey-authentication: YubiKey authentication
  oath-token-authentication: OATH token authentication
  email-authentication: Email authentication
  sms-and-voice-authentication: SMS and voice authentication
  additional-options: Additional options
  next-steps: Next steps…​
---

# Configure PingID authentication

You can configure PingID authentication options according to your organization's security policy and the different use cases relevant to your organization.

## PingID mobile app authentication

* [Configure biometrics authentication for the PingID mobile app](pid_configuring_biometrics_auth_pidma.html)

* [Configure the duration of new authentication requests](pid_configuring_duration_new_auth_request_pidma.html)

* [Configure one-time passcode fallback](pid_configuring_otp_fallback_pidma.html)

* [Configure direct passcode usage](pid_configuring_direct_passcode_usage_pidma.html)

* [Configure authentication when the device is locked](pid_configuring_auth_settings_for_locked_device_pidma.html)

* [Enable or disable location collection](pid_enabling_location_collection.html)

* [Define the authenticating app appearance](pid_defining_auth_app_appearance_pidma.html)

## PingID desktop app authentication

* [Configure the PingID desktop app](pid_configuring_desktop_app_.html)

* [Configure the PingID desktop app PIN](pid_desktop_app_pin.html)

* [Reset a user's desktop app PIN](pid_reset_desktop_app_pin.html)

* [Enable or disabling automatic updates](pid_desktop_app_auto_updates.html)

* [Configure PingID Proxy for the PingID desktop app](configuring_pid_desktop_app_proxy.html)

* [Configure Proxy Auto Configuration](pid_configuring_proxy_auto_for_pid_desktop_app.html)

* [Configure Kerberos proxy authentication](pid_configuring_kerberos_proxy_authentication_for_desktop_app.html)

* [Setting up PingID desktop authentication on Windows](http://docs.pingidentity.com/pingid-user-guide/secure_authentication_with_pingid/ug_pid_desktop_app_web.html)

* [Install the desktop app using the Windows CLI](installing_pid_desktop_app_using_windows_cli.html)

* [Set up PingID desktop app on a Mac using the UI](http://docs.pingidentity.com/pingid-user-guide/managing_your_devices/pid_manage_pid_desktop_app_on_mac.html)

* [Install the desktop app using the Mac CLI](installing_pid_desktop_app_using_mac_cli.html)

* [Troubleshoot the desktop app](pid_troubleshoot_desktop_app.html)

## FIDO2 biometrics

(Apple Touch ID, iOS biometrics, Windows Hello, and Android biometrics capabilities)

* [FIDO2 biometrics requirements and limitations](fido2_biometrics_auth_requirements_and_limitations.html)

* [Configure passwordless authentication](pid_configuring_fido2_passwordless_auth.html)

* [Configure MFA authentication](pid_configuring_fido2_biometrics_mfa_authentication.html)

* [FIDO2 biometrics use cases](pid_fido2_biometrics_use_cases.html)

## FIDO2 security key

* [FIDO2 security key requirements and limitations](pid_fido2_biometrics_use_cases.html)

* [Configure security key authentication](configuring_security_key_auth.html)

* [FIDO2 security key use cases](pid_security_key_use_cases.html)

## YubiKey authentication

* [Configure YubiKey authentication](pid_configuring_yubikey_authentication.html)

## OATH token authentication

* [Configure OATH token authentication](pid_configuring_oath_token_authentication.html)

## Email authentication

* [Configure email authentication](pid_configuring_email_authentication.html)

* [Customize emails](pid_email_customization.html)

## SMS and voice authentication

* [Configure SMS and voice authentication](pid_configuring_sms_and_voice_authentication.html)

* [Language localization for voice authentication](pid_enabling_language_localization_voice_authentication.html)

* [Language localization for SMS authentication](pid_enabling_customizing_localization_sms_authentication.html)

* [Using a custom Twilio account with PingID](pid_using_custom_twilio_account.html)

* [SMS and voice usage limits](pid_sms_voice_usage_limits.html)

## Additional options

* [Pre-populate or restrict user registration data](pid_prepopulating_or_restricting_user_registration_data.html)

* [Configure backup authentication methods](pid_prepopulating_or_restricting_user_registration_data.html)

* [Enable advanced authentication policy](pid_enabling_advanced_authentication_policy.html)

* [Configure the phone number attribute in PingOne](pid_configuring_phone_number_attribute_in_p1.html)

* [Configure LDAP attributes in PingFederate](pid_configuring_ldap_attributes_in_pf.html)

* [Disable pairing for a specific authentication method](pid_disabling_pairing_specific_authentication_method.html)

* [Remove authentication methods](pid_removing_authentication_methods.html)

## Next steps…​

Learn more about how apply policies to authentication methods in [PingID policy settings](pid_policy_settings.html).