---
title: FIDO policies
description: FIDO policies define which FIDO devices and authenticators can be used for registration and authentication purposes. FIDO allows you to authenticate users using public key-based credentials.
component: pingone
page_id: pingone:authentication:p1_fido_policies
canonical_url: https://docs.pingidentity.com/pingone/authentication/p1_fido_policies.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 6, 2024
section_ids:
  fido2-integration-modes: FIDO2 integration modes
  related-links: Related links
---

# FIDO policies

FIDO policies define which FIDO devices and authenticators can be used for registration and authentication purposes. FIDO allows you to authenticate users using public key-based credentials.

PingOne supports the use of the WebAuthn standard, and the PingOne FIDO2 server is a FIDO2-certified product.

![FIDO alliance FIDO certified icon](_images/nvt1619329318642.png)

FIDO2 with PingOne provides many security benefits, such as protection against phishing and replay attacks. PingOne includes the following security measures from the FIDO2 specification:

* Based on public key cryptography

* Does not employ server-side shared secrets that could otherwise be compromised

* Isolates services from accounts

FIDO2 devices can include:

* FIDO2 biometrics and security keys.

* Passkeys. Passkeys allow cloud-synched credentials so that users can access their FIDO sign-in credentials on many of their accessing devices, even new ones, without having to re-enroll every device on every account.

FIDO2 devices and authenticators can be used for registration and authentication purposes and to enable usernameless and passwordless authentication.

You can also view, search, add, or delete FIDO devices in the **Global Authenticators Table**. Learn more in [Managing the Global Authenticators Table](p1_add_device_to_global_authenticators_table.html).

## FIDO2 integration modes

PingID supports the following FIDO2 integration modes:

* PingID's out of the box solution, using the PingID UI and the pingone.com domain. Learn more in:

  * [Using Windows Hello for authentication](https://docs.pingidentity.com/pingid-user-guide/secure_authentication_with_pingid/pid_using_windows_hello_auth.html)

  * [Using Apple Mac Touch ID for authentication](https://docs.pingidentity.com/pingid-user-guide/secure_authentication_with_pingid/pid_using_mac_touchid_auth.html)

  * [Using a security key (FIDO2) for authentication](https://docs.pingidentity.com/pingid-user-guide/secure_authentication_with_pingid/pid_using_security_key_auth.html)

  * [Using Android biometrics for authentication](https://docs.pingidentity.com/pingid-user-guide/secure_authentication_with_pingid/pid_using_android_biometrics_auth.html)

* API-based, using a custom UI that is not hosted by PingID, and a custom domain. Learn more in:

  * [FIDO pairing workflow](https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiUserManagement.html#fido-pairing-workflow)

  * [FIDO authentication workflow](https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiAuthentication.html#fido-authentication-workflow)

  * [FIDO passwordless authentication workflow](https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiAuthentication.html#fido-passwordless-authentication-workflow)

* Hybrid mode, also API-based using a custom UI for registration that is not hosted by PingID, and PingID's default UI for authentication. This mode leverages the pingone.com domain. Learn more in [PPM request for FIDO authentication with a hybrid UI](https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiPpmrequest.html#ppm-request-for-fido-authentication-with-a-hybrid-ui).

## Related links

* [Adding a FIDO policy](p1_creating_a_fido_policy.html)

---

---
title: FIDO2
description: FIDO2 (Fast IDentity Online) allows your applications to authenticate users using public key-based credentials.
component: pingone
page_id: pingone:authentication:p1_fido2
canonical_url: https://docs.pingidentity.com/pingone/authentication/p1_fido2.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 30, 2023
section_ids:
  fido2-biometrics: FIDO2 biometrics
  fido2-security-keys: FIDO2 security keys
  fido-policy: FIDO policy
  related-links: Related links
---

# FIDO2

FIDO2 (Fast IDentity Online) allows your applications to authenticate users using public key-based credentials.

PingOne supports the use of the FIDO2 protocol, and the PingOne FIDO2 server is a FIDO2 certified product.

![nvt1619329318642](_images/nvt1619329318642.png)

You can add FIDO2 as an authentication method for your end users. To set up FIDO2, edit an existing authentication policy or create a new one. For more information, see [Editing an authentication policy](p1_edit_auth_policy.html) and [Adding a multi-factor authentication or PingID step](p1_add_mfa_step.html).

FIDO2 with PingOne provides many security benefits, such as protection against phishing, man-in-the-middle, and replay attacks. PingOne includes the following security measures from the FIDO2 specification:

* Based on public key cryptography

* Ensures that private keys remain on the FIDO2 device only

* Does not employ server-side shared secrets that could otherwise be compromised

* Isolates services from accounts

Users can authenticate with:

* FIDO2 biometrics, by using a gesture in a compatible device

* FIDO2 security keys

## FIDO2 biometrics

With FIDO2 biometrics, end users can authenticate using biometrics on compatible devices. Supported devices include Windows Hello, Android OS 7.0 or later, MacOS, and iOS. For FIDO2 biometrics, the authentication method is bound to a particular device, unlike other methods such as SMS, voice and email.

|   |                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------- |
|   | FIDO2 biometrics can be used for web-based authentication only through browsers that support platform authenticators. |

## FIDO2 security keys

A hardware-based security key can be used to authenticate users, often in sensitive environments or environments with limited device or phone access, such as hospitals, financial institutions, or federal buildings. FIDO2 security keys are backward compatible with U2F, enabling PingOne to support both FIDO2 and U2F security keys.

After you enable a security key as part of an authentication policy, the user can use it to authenticate. Pairing the device creates a trust between the security key and the user account, so it can be used for authentication.

|   |                                                                                                     |
| - | --------------------------------------------------------------------------------------------------- |
|   | Security keys can be used for web-based authentication only through browsers that support WebAuthn. |

## FIDO policy

You can configure one or more FIDO policy and include it in your MFA policy. You can create a FIDO policy for the use of FIDO2 Biometrics and FIDO2 security keys. Create a FIDO policy to define which FIDO devices and authenticators can be used for registration and authentication purposes, and to enable usernameless and passwordless authentication. For more information, see [FIDO policies](p1_fido_policies.html).

## Related links

* [Adding a multi-factor authentication or PingID step](p1_add_mfa_step.html)

* [Editing an authentication policy](p1_edit_auth_policy.html)

---

---
title: Identifier first authentication
description: With identifier first authentication, also known as identity discovery, you can identify users before you authenticate them. You can set up rules that will take different authentication actions based on who the user is.
component: pingone
page_id: pingone:authentication:p1_idp_first_auth
canonical_url: https://docs.pingidentity.com/pingone/authentication/p1_idp_first_auth.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 9, 2025
---

# Identifier first authentication

With identifier first authentication, also known as identity discovery, you can identify users before you authenticate them. You can set up rules that will take different authentication actions based on who the user is.

If the user name matches a configured rule, the system sends the user to a particular external identity provider. If the user name doesn't match a configured rule, the system sends the user to the regular password flow. For example, you could set up a rule to send employees to one identity provider, and contractors to another identity provider.

For more information, see [Adding an authentication policy](p1_add_an_auth_policy.html).

---

---
title: Managing FIDO policies
description: You can edit, rename, or delete a FIDO policy. You can also change the default policy.
component: pingone
page_id: pingone:authentication:p1_managing__fido_policies
canonical_url: https://docs.pingidentity.com/pingone/authentication/p1_managing__fido_policies.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
---

# Managing FIDO policies

You can edit, rename, or delete a FIDO policy. You can also change the default policy.

## About this task

## Steps

1. Go to **Authentication > FIDO**.

   ### Result:

   The **FIDO Policies** window opens showing a list of FIDO policies.

2. In the FIDO policies list, in the relevant row do any of the following:

   | Option                | Description                                                                                                     |
   | --------------------- | --------------------------------------------------------------------------------------------------------------- |
   | Edit a policy         | Select **More Options (⋮)** and edit the relevant fields.                                                       |
   | Change default policy | Next to the policy you want to make the default policy, select **More Options (⋮)** and click **Make Default**. |
   | Rename a policy       | Select **More Options (⋮)** click **Rename**.                                                                   |
   | Delete a FIDO policy  | Select **More Options (⋮)** and click **Delete**.                                                               |

3. Click **Save**.

   |   |                                                                                                                         |
   | - | ----------------------------------------------------------------------------------------------------------------------- |
   |   | In the policy list, click a policy to see a summary of the policy details in the right pane or edit an existing policy. |

---

---
title: Managing password policies
description: Use the Password page to manage password requirements and rules for your PingOne environment.
component: pingone
page_id: pingone:authentication:p1_selectpasswordpolicy
canonical_url: https://docs.pingidentity.com/pingone/authentication/p1_selectpasswordpolicy.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 23, 2025
page_aliases: ["p1_add_password_policy.adoc", "p1_delete_password_policy.adoc", "p1_edit_password_policy.adoc", "p1_view_passowrd_policies.adoc"]
section_ids:
  p1-view-pw-policies: Viewing password policies
  steps: Steps
  p1-add-pw-policy: Adding a password policy
  steps-2: Steps
  choose-from: Choose from:
  p1-edit-pw-policy: Editing a password policy
  steps-3: Steps
  p1-delete-pw-policy: Deleting a password policy
  steps-4: Steps
---

# Managing password policies

Use the **Password** page to manage password requirements and rules for your environment.

Click the corresponding tab for instructions about:

* Viewing all policies and policy details

* Adding a policy

* Modifying a policy

* Deleting a policy

- View password policies

- Add a password policy

- Edit a password policy

- Delete a password policy

## Viewing password policies

Use the **Password** page to view existing password policies in your environment.

### Steps

1. In the PingOne admin console, go to **Authentication > Password**.

2. Click a policy to view the policy details.

   * The **Overview** panel shows a count of populations using the policy and provides a link to the **Populations** page.

   * The **Configuration** panel shows the configured rules and requirements for the policy.

## Adding a password policy

Use the **Password** page to add a password policy to your environment.

### Steps

1. In the PingOne admin console, go to **Authentication > Password**.

2. Click the **[icon: plus, set=fa]**icon to add a policy.

3. Enter a **Name** and **Description** for the policy, then click **Next**.

4. Choose a template for the policy and modify to fit password requirements for users in the population, if applicable.

   #### Choose from:

   * Standard

   * Passphrase

   * Advanced

     Learn more about the password rules and character restrictions included in each of the built-in password policies in [Password policies](p1_passwordpolicies.html).

   |   |                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------- |
   |   | Modifying the **Standard** and **Passphrase** templates automatically creates an **Advanced** policy. |

5. Click **Save**.

## Editing a password policy

Use the **Password Policies** page to edit existing password policies in your environment.

### Steps

1. In the PingOne admin console, go to **Authentication > Password** and browse or search for the policy that you want to edit.

2. Click the **More Options** (⋮) icon for the policy and select **Edit Password Policy**.

3. Make the appropriate changes. Learn more about password policy settings in [Password policies](p1_passwordpolicies.html).

4. (Optional) Select **Set as default policy** to assign this password policy to any population for which a password policy is not explicitly selected.

5. Click **Save**.

## Deleting a password policy

Use the **Password** page to remove existing password policies from your environment.

### Steps

1. In the PingOne admin console, go to **Authentication > Password** and browse or search for the policy that you want to delete.

2. In the list on the right, select **Delete**.

3. When prompted, click **Delete** to confirm.

   |   |                                                                                                                                                                         |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You cannot delete a policy that is assigned to a population. If the password policy is in use, you must first assign a new password policy to the affected populations. |

---

---
title: Managing the Global Authenticators Table
description: The Global Authenticators Table includes a list of devices obtained and regularly updated through the FIDO Alliance Metadata Service (MDS). Only devices listed in the Global Authenticators Table can be used in a FIDO policy.
component: pingone
page_id: pingone:authentication:p1_add_device_to_global_authenticators_table
canonical_url: https://docs.pingidentity.com/pingone/authentication/p1_add_device_to_global_authenticators_table.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Managing the Global Authenticators Table

The **Global Authenticators Table** includes a list of devices obtained and regularly updated through the [FIDO Alliance Metadata Service (MDS)](https://fidoalliance.org/metadata/). Only devices listed in the **Global Authenticators Table** can be used in a FIDO policy.

## About this task

The table also indicates which devices are **FIDO Certified** and the protocol supported for each device. You can add your own custom devices to the list. You can also download the metadata of an existing FIDO device and use it to create a custom entry.

![The Global Authenticators Table showing the search bar, and the option to Add Custom Metadata](_images/smz1676314413303.png)

## Steps

1. Go to **Authentication > FIDO** and click the **Global Authenticators Table** link.

2. Do any of the following:

   | Option                  | Description                                                                                                                                                                                                                          |
   | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | View device details     | * In the relevant row, click the **More Options** (⋮) menu and select **View**.

     A popup window opens displaying the JSON for that device.                                                                                         |
   | Download device details | - In the relevant row, click the **More Options** (⋮) menu, select **Download**, and save the JSON file that is created.                                                                                                             |
   | Add custom metadata     | * Click **[icon: plus, set=fa]Add Custom Metadata** and select the JSON file that you want to add. Click **Open**.

     The device is added to the table. In the **Custom** column, a check mark indicates that it is a custom device. |
   | Delete a custom device  | - In the relevant row, click the **More Options** (⋮) menu and select **Delete**.

     &#xA;&#xA;You can delete only custom devices from the Global Authenticators Table.                                                              |

---

---
title: MFA policies
description: Use the MFA Policies page to create, update, or delete MFA policies. After creating an MFA policy, you can refer to it in any authentication or registration flow designed in PingOne, PingOne DaVinci, PingID, or the PingOne MFA API.
component: pingone
page_id: pingone:authentication:p1_mfa_policies
canonical_url: https://docs.pingidentity.com/pingone/authentication/p1_mfa_policies.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 6, 2024
section_ids:
  default-mfa-policy: Default MFA policy
---

# MFA policies

Use the **MFA Policies** page to create, update, or delete MFA policies. After creating an MFA policy, you can refer to it in any authentication or registration flow designed in PingOne, PingOne DaVinci, PingID, or the PingOne MFA API.

An MFA policy allows you to define and configure the authentication methods that you want to use in your authentication policy. The MFA policy is then added as an MFA step in your authentication policy.

An MFA policy includes the following configuration information:

* The authentication methods that the policy allows

* The configurations specific to the authentication method, such as how many failed passcode attempts are allowed and how long users should be blocked after passcode failure

## Default MFA policy

When you create a new environment, a default MFA policy is added to the **MFA Policies** page automatically.

You can modify the default policy. You can also create additional MFA policies.

|   |                                                                                                                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Workforce environments don't support the use of legacy PingID security key or FIDO2 biometrics. To create additional MFA policies, make sure you update your MFA policy to support FIDO2 authentication. Learn more in [Updating an existing MFA policy to use FIDO2](../strong_authentication_mfa/p1_updating_an_mfa_policy_to_fido2.html). |

The default policy serves the following purposes:

* When defining an authentication policy in PingOne, you can add an MFA step and select the **Use Default Policy** option. This means that the authentication policy will use whatever MFA policy is currently set to be the default MFA policy for the environment.

* The DaVinci PingOne MFA connector includes a policy ID in its configuration. If you do not specify an MFA policy, the connector will use whatever MFA policy is currently set to be the default MFA policy for the environment.

* In the PingOne MFA API, there are calls that allow you to specify a particular MFA policy to use. In these situations, if you do not specify an MFA policy, the flow will use whatever MFA policy is currently set to be the default MFA policy for the environment.

* If you configure the **Self Service** page to let users add authentication methods by themselves, the available methods displayed to the user are those that are allowed by the default MFA policy.

---

---
title: MFA Settings
description: Use the MFA Settings page to configure the maximum number of MFA methods that a user can set up for authentication, authentication method selection, and account lockout settings.
component: pingone
page_id: pingone:authentication:p1_mfa_settings
canonical_url: https://docs.pingidentity.com/pingone/authentication/p1_mfa_settings.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 3, 2024
---

# MFA Settings

Use the **MFA Settings** page to configure the maximum number of MFA methods that a user can set up for authentication, authentication method selection, and account lockout settings.

---

---
title: Password policies
description: A password policy dictates the strength and complexity requirements for a password or passphrase. You can choose or define a policy that fits the needs of your organization.
component: pingone
page_id: pingone:authentication:p1_passwordpolicies
canonical_url: https://docs.pingidentity.com/pingone/authentication/p1_passwordpolicies.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 22, 2024
section_ids:
  password-policy-comparisons: Password policy comparisons
  section_ey4_bb3_fsb: Password Character Restrictions
  section_password_policy_rules: Password Policy Rules
  section_password_policy_lockout_rules: Account Lockout Rules
---

# Password policies

A password policy dictates the strength and complexity requirements for a password or passphrase. You can choose or define a policy that fits the needs of your organization.

PingOne allows you to assign password policies to populations and includes three built-in policy types. You can customize these policies or create new policies to meet the password requirements for users in the population. Learn more in the following tables.

The built-in password policies include:

* Standard (default): The standard password policy incorporates industry best practices for a typical password policy. The standard policy is the default policy when the environment is created. The default policy is applied to populations for which another password policy has not been selected. You can later choose a different password policy to use as the default.

* Passphrase: The passphrase policy encourages users to use a passphrase instead of a password for stronger authentication. A passphrase can be easier to remember and more secure because of its length.

* Basic: The basic password policy is a more relaxed standard that allows for maximum customer flexibility. Because users are not required to change their passwords, the basic policy can be less secure.

Learn more about viewing, adding, modifying, or deleting password policies in [Managing password policies](p1_selectpasswordpolicy.html).

## Password policy comparisons

Review the following tables to compare the different rules and restrictions applied by each built-in policy.

### Password Character Restrictions

| Character Restriction                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Standard Policy | Passphrase Policy | Basic Policy |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | ----------------- | ------------ |
| Not the same as current password (always enabled).                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Yes             | Yes               | Yes          |
| Is not an exact match for any of the attribute values in the user profile.                                                                                                                                                                                                                                                                                                                                                                                                                                             | Yes             | Yes               | No           |
| Not similar to current password.&#xA;&#xA;PingOne checks the Levenshtein distance between the two passwords to ensure they are not too similar. The Levenshtein distance counts the number of characters added to, removed from, or replaced from the old password to the new password. If the Levenshtein distance is less than 3, then the password will be rejected as too similar. For example, changing a password from kitten to smitten would have a Levenshtein distance of 2, and be rejected as too similar. | Yes             | Yes               | No           |
| Not a common password.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Yes             | Yes               | Yes          |
| Has a computational complexity of at least 7 days, based on the Gibson Research Corporation Password Haystacks concept.                                                                                                                                                                                                                                                                                                                                                                                                | No              | Yes               | No           |
| No more than two consecutive repeated characters.For example, `good-apple` is acceptable but `goood-appple` is not.                                                                                                                                                                                                                                                                                                                                                                                                    | Yes             | No                | No           |
| At least five unique characters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Yes             | No                | No           |
| Between 8 and 255 characters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Yes             | No                | Yes          |
| At least one of the following special characters:\~!@#$%^&\*()-\_=+\[]\\{}\|;:,.<>/?                                                                                                                                                                                                                                                                                                                                                                                                                                   | Yes             | No                | Yes          |
| At least one number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Yes             | No                | Yes          |
| At least one uppercase letter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Yes             | No                | Yes          |
| At least one lowercase letter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Yes             | No                | Yes          |
| No more than two or three sequential numbers (configurable).For example, `123` or `432` are not acceptable if set to `2`, but would be acceptable if set to `3`.                                                                                                                                                                                                                                                                                                                                                       | No              | No                | No           |
| No more than two or three sequential letters (configurable).For example, `abc` or `dcb` are not acceptable if set to `2`, but would be acceptable if set to `3`.                                                                                                                                                                                                                                                                                                                                                       | No              | No                | No           |
| No more than three sequential QWERTY keyboard characters.For example, `qwer`, `rewq`, `zxcv`, or `vcxz` are not acceptable.                                                                                                                                                                                                                                                                                                                                                                                            | No              | No                | No           |
| No more than three sequential symbol row characters.For example, `~!@#` or `#@!~` are not acceptable.                                                                                                                                                                                                                                                                                                                                                                                                                  | No              | No                | No           |
| Supports all printable UTF-8 characters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Yes             | Yes               | Yes          |

### Password Policy Rules

| Policy Rule                                         | Standard Policy | Passphrase Policy | Basic Policy |
| --------------------------------------------------- | --------------- | ----------------- | ------------ |
| Previous passwords maintained in history for 1 year | 6               | 6                 | None         |
| Password expires after                              | 182 days        | Never             | 182 days     |
| User can change their password after                | 1 day           | 1 day             | Never        |

### Account Lockout Rules

| Lockout Rule            | Standard Policy                                                             | Passphrase Policy | Basic Policy |
| ----------------------- | --------------------------------------------------------------------------- | ----------------- | ------------ |
| Allowed failed attempts | After five failed attempts, the user is locked out                          | 5                 | 5            |
| Automatic unlock period | Accounts locked after maximum failed attempts are unlocked after 15 minutes | 15 minutes        | 15 minutes   |

---

---
title: Progressive profiling
description: With progressive profiling, you can prompt a user for information to be added to their profile after the initial registration step. For example, you could prompt users to add their mobile phone number the next time they sign in.
component: pingone
page_id: pingone:authentication:p1_progressive_profiling
canonical_url: https://docs.pingidentity.com/pingone/authentication/p1_progressive_profiling.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 10, 2023
---

# Progressive profiling

With progressive profiling, you can prompt a user for information to be added to their profile after the initial registration step. For example, you could prompt users to add their mobile phone number the next time they sign in.

You can use progressive profiling to minimize the amount of information you request during initial registration. After registration is complete, you can require or request additional information from the user.

You can also set up multiple progressive profiling steps within the same authentication policy to separate the steps by priority or by type. For example, the first step might request a single higher priority item, like a mobile phone number, with a more frequent prompt. The second step might request more lower priority items, with a less frequent prompt. You can set up each item to be required or optional.

For more information, see [Adding an authentication policy](p1_add_an_auth_policy.html).

---

---
title: Resolving a lockout
description: In most cases, PingOne will not allow you to create an authentication policy that would lock you out of your account. However, if you find yourself locked out of your account or otherwise blocked, you can contact Ping Identity to unlock it.
component: pingone
page_id: pingone:authentication:p1_resolve_lockout
canonical_url: https://docs.pingidentity.com/pingone/authentication/p1_resolve_lockout.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 9, 2023
section_ids:
  steps: Steps
---

# Resolving a lockout

In most cases, PingOne will not allow you to create an authentication policy that would lock you out of your account. However, if you find yourself locked out of your account or otherwise blocked, you can contact Ping Identity to unlock it.

## Steps

* If you are unable to access your account, contact <support@pingidentity.com>.

---

---
title: Setting the default authentication policy
description: Use the Authentication policies page to configure the default authentication policy in PingOne.
component: pingone
page_id: pingone:authentication:p1_set_default_auth_policy
canonical_url: https://docs.pingidentity.com/pingone/authentication/p1_set_default_auth_policy.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 23, 2025
section_ids:
  steps: Steps
---

# Setting the default authentication policy

Use the **Authentication** page to configure the default authentication policy in PingOne.

|   |                                                                                                                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The default authentication policy doesn't apply to the PingOne admin console. The admin console uses a system policy configured in **Settings > Administrator Security** instead of the default policy. You can't assign a different policy to the admin console. |

## Steps

1. In the PingOne admin console, go to **Authentication > Authentication** and browse or search for the policy that you want to set as the default.

2. Click the **Expand** icon to expand the policy, and then click the **Pencil** icon.

3. At the top of the page, under the policy name, click **Make Default**.

---

---
title: Setting up passwordless authentication
description: Use passwordless authentication in PingOne to enable a users to sign on without remembering complex passwords.
component: pingone
page_id: pingone:authentication:p1_set_up_paswordless_auth
canonical_url: https://docs.pingidentity.com/pingone/authentication/p1_set_up_paswordless_auth.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 3, 2024
---

# Setting up passwordless authentication

You can use passwordless authentication to enable a higher level of assurance for users without requiring them to remember complex passwords. With a passwordless authentication policy, users can sign in with only a username and a one-time passcode that's delivered over email or text message, or a mobile push notification.

|   |                                                                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * Before enabling passwordless authentication, ensure that you have set up and validated a MFA device for you and your users, because they won't be able to sign on without a second factor.

* We strongly discourage selecting a passwordless policy as the default password policy. |

1. In the PingOne admin console, go to **Authentication > Authentication**.

2. Click **[icon: plus, set=fa]Add Policy**.

3. Enter a descriptive name for the policy, such as `Passwordless`.

4. From the **Step Type** list, select **Multi-Factor Authentication**.

5. In the **MFA policy** list, select the appropriate MFA policy. Learn more about setting up MFA policies in [MFA policies](p1_mfa_policies.html).

6. Click **Save**.

---

---
title: Setting up step-up authentication for APIs
description: Use step-up authentication in applications that require stronger authentication methods for access to sensitive resources.
component: pingone
page_id: pingone:authentication:p1_set_up_stepup_auth_for_apis
canonical_url: https://docs.pingidentity.com/pingone/authentication/p1_set_up_stepup_auth_for_apis.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 9, 2024
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  next-steps: Next steps
---

# Setting up step-up authentication for APIs

Use step-up authentication in applications that require stronger authentication methods for access to sensitive resources.

To access an API resource, applications provide an access token. Step-up authentication uses the `acr` claim in the access token to ensure that users authenticate with a higher level of assurance when they access a sensitive API resource and the `auth_time` claim in the access token to ensure that they've authenticated recently. Learn more about [step-up authentication for APIs](p1_stepup_authentication_for_apis.html).

Complete these high-level steps to set up step-up authentication.

## Before you begin

To set up step-up authentication, you'll need:

* An API gateway that's integrated with PingOne Authorize. Learn more in [PingOne Authorize API gateway integrations](../authorization_using_pingone_authorize/p1az_api_gateway_is.html).

* A PingOne environment that includes the PingOne SSO and PingOne Authorize services.

* If you're using DaVinci authentication policies, your environment must include DaVinci.

## Steps

1. [Register your application](../applications/p1_applications_add_applications.html) in PingOne.

   |   |                                                                                                                                                                                          |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The **Application Type** must be **OIDC Web App**, **Native**, or **Single-Page**. Step-up authentication isn't supported for client applications that use the SAML or WS-Fed protocols. |

2. Add the authentication policies you want to use for identity verification.

   Ensure that you have policies for basic authentication and for higher levels, such as MFA. You can use DaVinci or PingOne policies. Learn more in:

   * [Adding a PingOne authentication policy](p1_add_an_auth_policy.html)

   * [Creating a DaVinci authentication flow](https://docs.pingidentity.com/davinci/use_cases/davinci_use_cases_creating_an_authentication_flow.html)

3. [Assign authentication policies](../applications/p1_apply_auth_policy_to_applications.html) to your application.

   |   |                                                                                                             |
   | - | ----------------------------------------------------------------------------------------------------------- |
   |   | You can assign either DaVinci or PingOne policies to your application, but not both types at the same time. |

4. [Add an API service](../authorization_using_pingone_authorize/p1az_add_api_service.html) to register your protected API resources in PingOne.

   If you'll use custom policies for step-up authentication instead of basic rules, make sure that you enable custom policies for the API service.

5. [Define API operations](../authorization_using_pingone_authorize/p1az_add_api_service_operations.html) with basic rules for authentication policies and time since last authentication.

6. [Deploy the API service](../authorization_using_pingone_authorize/p1az_deploying_api_services.html).

## Next steps

Configure your client application to handle 401 challenge responses with authentication policy (`acr_values`) and maximum authentication age (`max_age`) requirements. Your application should parse the challenge response, construct an appropriate OAuth 2.0 request, then try again with the new access token.

|   |                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------- |
|   | Avoid getting caught in a loop if requests are repeatedly denied when authentication requirements aren't met. |

---

---
title: Step-up authentication for APIs
description: Step-up authentication enables you to require users to provide additional levels of authentication when they access sensitive API resources or perform high-risk actions.
component: pingone
page_id: pingone:authentication:p1_stepup_authentication_for_apis
canonical_url: https://docs.pingidentity.com/pingone/authentication/p1_stepup_authentication_for_apis.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 9, 2025
section_ids:
  when-to-use-step-up-authentication: When to use step-up authentication
  how-is-step-up-authentication-different-from-mfa: How is step-up authentication different from MFA?
  how-it-works: How it works
---

# Step-up authentication for APIs

Step-up authentication enables you to require users to provide additional levels of authentication when they access sensitive API resources or perform high-risk actions.

Step-up authentication is also known as just-in-time authentication or route-based authentication. It allows your organization to reduce friction during the authentication experience while ensuring that sensitive resources are protected. For example, a bank might require only a basic level of authentication when customers view available banking products, but require an additional authentication method when they view their account balance or transaction history.

Step-up authentication has the following benefits:

* Balances a frictionless authentication experience with the need for increased security

* Limits MFA fatigue by asking for additional authentication only when it's needed

* Protects critical assets or high-risk resources that only certain users need to access

* Reassures users that their sensitive data is safe

## When to use step-up authentication

Use step-up authentication when you want to guarantee that users are always required to provide an additional authentication factor when they try to access sensitive data or perform high-risk actions.

Specific kinds of API resources can be more sensitive than others, such as salary data, health records, or premium content. Before you allow a client to access these resources, you can use step-up authentication to require that:

* The user authenticated with a higher-level authentication policy

* The user authenticated recently

## How is step-up authentication different from MFA?

With MFA, users must always present two or more authentication factors to verify their identity, such as a password and a one-time passcode (OTP) sent to their device.

With step-up authentication, users are allowed to access certain resources with one level of authentication, while more sensitive resources are protected by an additional level of authentication. Higher-level authentication is required only when it's needed.

You can learn more about authentication levels in [NIST authenticator assurance levels](https://pages.nist.gov/800-63-3-Implementation-Resources/63B/AAL/).

## How it works

Step-up authentication uses PingOne in combination with your API gateway to require higher-level authentication for sensitive resources. You define authentication policies for an application with [DaVinci](https://docs.pingidentity.com/davinci/use_cases/davinci_use_cases_creating_an_authentication_flow.html) or [PingOne SSO](p1_add_an_auth_policy.html), then use PingOne API Access Management in conjunction with your API gateway to protect your sensitive resources.

The following diagram and steps represent a typical step-up authentication flow:

![Diagram showing initial authorization, an additional prompt condition met, additional authorization required, and access granted or denied.](_images/p1-stepup-auth-flow-diagram.png)

1. A user accesses an application with a basic level of authentication.

   The authorization server issues an access token that the client application uses to request resources. For example:

   ```
   GET /secrets HTTP/1.1
   Host: example.com
   Authorization: Bearer eyJ0eX
   ```

   The access token includes claims related to authentication requirements:

   * `acr`: The name of the authentication policy used to satisfy the authentication event.

   * `auth_time`: The timestamp of the authentication event, expressed in epoch seconds.

2. []()The user requests access to a sensitive resource, meeting a condition that requires additional authentication.

   The resource server checks the `acr` and `auth_time` claims in the client's access token and determines that authentication requirements are not met. The resource server rejects the request and issues a challenge response. For example:

   ```
   HTTP/1.1 401 Unauthorized
   WWW-Authenticate: Bearer error="insufficient_user_authentication",
     error_description="A different authentication level is required",
     acr_values="strong_authentication_policy", max_age=300
   ```

   The challenge response includes the following details about authentication requirements:

   * `insufficient_user_authentication` error code: Tells the client that the user needs to reauthenticate.

   * `acr_values`: A list of acceptable authentication policies.

   * `max_age`: The allowable elapsed time in seconds since the last active authentication event associated with the access token.

3. The user is prompted to reauthenticate with higher-level factors.

   * The client parses the challenge response. The error code indicates that the user needs to reauthenticate.

   * The client requests a new access token from the authorization server based on the `acr_values` and `max_age` provided in the challenge response. For example:

     ```
     GET /<envId>/as/authorize?client_id=<clientId>&scope=secret&response_type=code&redirect_uri=<redirectUri>&state=<state>&acr_values=strong_authentication_policy&max_age=300
     Host: auth.pingone.com
     ```

   * The authorization server prompts the user to reauthenticate with the policy named in `acr_values`.

4. The user reauthenticates.

   If authentication is successful, the authorization server issues a new access token that includes the necessary claims.

5. If authentication is successful, the user requests access to the sensitive resource.

   * The client requests access to the sensitive resource with the new access token.

   * The resource server fulfills the request if the authentication policy matches the `acr_values` requested in the challenge response, or `max_age` is not exceeded.

   * The resource server denies the request if the authentication policy doesn't match the `acr_values` requested in the challenge response, or `max_age` is exceeded.

You can learn more about authentication challenges and bearer token usage in [RFC 9470](https://datatracker.ietf.org/doc/rfc9470/) and [RFC 6750](https://datatracker.ietf.org/doc/html/rfc6750).

When you use PingOne for step-up authentication, PingOne SSO acts as the authorization server. PingOne API Access Management acts on behalf of the resource server to enforce authentication requirements and issue challenge responses when requirements aren't met.

Learn more in [Setting up step-up authentication for APIs](p1_set_up_stepup_auth_for_apis.html).

---

---
title: Viewing authentication policies
description: View the currently configured authentication policies in PingOne.
component: pingone
page_id: pingone:authentication:p1_view_auth_policies
canonical_url: https://docs.pingidentity.com/pingone/authentication/p1_view_auth_policies.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 9, 2023
section_ids:
  steps: Steps
  result: Result
---

# Viewing authentication policies

View the currently configured authentication policies.

## Steps

1. In the PingOne admin console, go to **Authentication > Authentication**.

   ## Result

   The **Authentication Policies** page shows a list of current authentication policies, including details for single-factor and multi-factor authentication (MFA) by default.

2. Click the **Details** icon to expand an entry and see details about the authentication policy.