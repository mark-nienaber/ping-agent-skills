---
title: Adding a FIDO policy
description: To enable authentication with FIDO2 devices, first create one or more FIDO policies.
component: pingone
page_id: pingone:authentication:p1_creating_a_fido_policy
canonical_url: https://docs.pingidentity.com/pingone/authentication/p1_creating_a_fido_policy.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 6, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  choose-from-3: Choose from:
  choose-from-4: Choose from:
  result: Result:
  next-steps: Next steps
---

# Adding a FIDO policy

To enable authentication with FIDO2 devices, first create one or more FIDO policies.

## About this task

|   |                                                                                                                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | A small number of the options listed aren't available for use with PingID accounts that are integrated with **PingOne**.Learn more about [Updating a PingID account to use a PingOne FIDO2 policy](https://docs.pingidentity.com/pingid/pingid_service_management/pid_update_to_fido2_authentication_method.html). |

To enable authentication with FIDO2 devices:

1. Create a FIDO policy defining which FIDO devices are permitted and the desired behavior when registering and authenticating your users. This task is described in detail in this topic.

2. Include the FIDO policy in the relevant MFA policy. For PingOne MFA, you can find more information in [MFA policies](p1_mfa_policies.html) and for PingID, you can find more information in [Configuring an MFA policy for strong authentication](../strong_authentication_mfa/p1_creating_an_mfa_policy_for_strong_auth.html).

3. Ensure the MFA policy is included in the MFA step of the relevant Authentication policy. You can find more information in [Adding a multi-factor authentication or PingID step](p1_add_mfa_step.html).

|   |                                                                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | When creating an environment, the following out-of-the-box (OOTB) FIDO policies are created by default:- Passkeys (default)

- Security keyThese policies represent best practice configurations for registration and authentication of the relevant devices. You can change the default policy if required. |

## Steps

1. Go to **Authentication → FIDO**.

2. On the **FIDO Policies** page, click the **[icon: plus, set=fa]**icon.

3. In the **Name** field, enter a meaningful name for the policy.

   There is a 256 character maximum.

4. In the **Device Display Name**, select the format in which you want the device to be displayed on self-service registration and authentication windows.

   ### Choose from:

   * **Label**: Free text field. The device name that is not translated.

   * **Translatable Keys**: Select an option from the list of translatable keys. The key is translated into the relevant language.

     |   |                                                                                                                                                                                                                                                                                                  |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
     |   | The list of translatable keys can be modified on the **FIDO policy** page for the relevant language. The FIDO policy page should be updated in the **Self-Service** module and the **Sign On Policy**module. You can find more information in [Languages](../user_experience/p1_languages.html). |

5. In the **FIDO Device Aggregation** field, select either:

   ### Choose from:

   * **Yes**: During authentication, aggregate all FIDO devices paired with a user's account and present them to the user as a single authentication method. The user's OS selects the most appropriate FIDO device with which to authenticate.

   * **No**: Present each FIDO device to the user as a separate device during authentication.

6. In the **Relying Party ID **field, select the relevant Relying Party ID (RPID):

   * **PingOne** (default): Use the PingOne RPID (such as pingone.com).

   * **Custom Domain**: Use the active custom domain for the selected environment. Learn more about custom domains in [Domains](../settings/p1_domains.html).

     |   |                                                    |
     | - | -------------------------------------------------- |
     |   | This option is not currently available for PingID. |

   * **Other**: Enter a valid domain.

     |   |                                                                                  |
     | - | -------------------------------------------------------------------------------- |
     |   | For **Sandbox** environments in PingOne, you can also use the value `localhost`. |

7. In the **Discoverable Credentials** field, select one.

   Discoverable credentials make it possible for registered users to authenticate without providing credentials.

   ### Choose from:

   * **Discouraged**: Discoverable credentials are not used, even when supported by the FIDO device. In cases where use of discoverable credentials is required by the FIDO device itself, this setting does not override the device setting.

   * **Required**: Require the use of discoverable credentials. This option is required for usernameless authentication.

   * **Preferred** (default): Use discoverable credentials where possible.

8. In the **Authenticator Attachment** field, select the type of authenticator that can be used to register.

   ### Choose from:

   * **Platform**: Only allow the use of FIDO device authenticators that contain an internal authenticator (such as a face or fingerprint scanner).

   * **Cross-platform**: Allow use of cross-platform authenticators , that are external to the accessing device (such as a security key).

   * **Both** (default).

9. In the **Public Key Credential Hints** field, select the authenticator that you want to present to the user during pairing. The selection is considered as a 'hint' to the authenticator.

   |   |                                                                                                                                           |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When defining Public Key Credentials Hints, make sure the options you select do not conflict with the **Authenticator Attachment** value. |

   * **Security Key**: The user is likely to use a security key. If selected, **Authenticator Attachment** should be set to **Cross-platform**.

   * **Client Device**: The user is likely to use a platform authenticator attached to a client device (such as Touch ID, Face ID or Windows Hello). If selected, **Authenticator Attachment** should be set to **Platform**.

   * **Hybrid**: The user is likely to use a mobile device or tablet for cross-device authentication using a QR-code or bluetooth. If selected, **Authenticator Attachment** should be set to **Cross-platform**.

10. In the **Manage verification settings** section, configure the following.

    |   |                                                                                                                                                           |
    | - | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | User verification requires the user to perform a gesture (such as a public key credential, fingerprint scan, or a PIN code) when using their FIDO device. |

    1. In the **User Verification** field, select either:

       * **Discouraged**: User verification isn't performed, even when supported by the FIDO device. In cases where user verification is required by the FIDO device itself, this setting doesn't override the device setting.

       * **Required**: Only FIDO devices supporting user verification can be used.

       * **Preferred** (default): User verification is performed if the FIDO device supports it. Otherwise, it's skipped.

         |   |                                                                             |
         | - | --------------------------------------------------------------------------- |
         |   | For usernameless flows, you must set **User Verification** to **Required**. |

    2. If you selected **Required** or **Preferred** for **User Verification**, optionally configure the following fields.

       |   |                                                       |
       | - | ----------------------------------------------------- |
       |   | The PIN-related settings apply only to security keys. |

       * (Security keys only) In the **Enforce PIN Length** field select either:

         * **Enabled**: Requires security keys to support the `minPinLength` extension. Users must set a PIN that meets the configured **Minimum PIN length**. When enabled, also define:

           * **Minimum Number of Characters**: Enter the minimum number of characters for a valid PIN. Characters can include letters and numbers (minimum: 4 (default), maximum: 10).

           * (Optional) **Apply only if device supports PIN policy**: If selected, only enforces the PIN length if the security key supports the `minPinLength` extension and has a PIN that complies with the minimum length. Otherwise, this check is skipped.

         * **Disabled**: Doesn't check compliance with the **Minimum PIN length**.

       * To enforce user verification (and a device PIN, if configured) during authentication as well as registration, select the **Enforce during authentication** checkbox.

11. In the **Backup Eligibility** field, indicate whether you allow users to authenticate with a device that uses cloud-synced credentials, such as a passkey.

    Options are **Allow** or **Disallow**.

12. In the **User Display Name** area, do the following:

    1. Select up to six attributes that can be used to populate the **User Display Name** and place them in order of preference. The **User Display Name** is a human-readable name associated with the user's account.

       |   |                                                                                                                                                                                                                  |
       | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
       |   | You can select any OOTB user profile attributes. The first attribute that contains valid data is used to populate the **User Display Name**. It is displayed to the user during registration and authentication. |

    2. To help users identify their passkeys, you can include **Additional Display Information**. Select the relevant checkbox:

       * **Include Environment Name**

       * **Include Organization Name**

       This information displays on the popup window that appears when a user adds a passkey as an authentication method.

13. In the **Attestation Request** area:

    1. In the **Attestation Type** field, select specify the level of either:

       * **None**: Do not require attestation for FIDO devices.

       * **Direct**: Audit or allow FIDO devices that comply with the defined Attestation Requirements.

       * **Enterprise**: Verify that the device is an Enterprise FIDO device. Optionally, require the user to use a FIDO device that matches the **Custom Attribute Defining User's Serial Number**.

         * In the **Custom Attribute Defining User's Serial Number** field, select either:

           * **\<custom attribute>**: Only allow users to register FIDO devices with a serial number that matches the value defined by the custom user attribute.

             Learn more about custom attributes in [Add custom attributes to a user](../pingone_tutorials/p1_add_custom_attributes_to_a_user.html)

           * **Not Defined**: Allow users to register enterprise FIDO devices regardless of the serial number.

         |   |                                                                                           |
         | - | ----------------------------------------------------------------------------------------- |
         |   | Windows login doesn't support the use of FIDO2 security keys with enterprise attestation. |

    2. In the **Attestation Requirements** field, select one of the following.

       Choose from:

       * **None**: Allow all FIDO devices and don't request attestation.

       * **Audit only**: Request attestation for auditing purposes only.

       * **Allow All Global**: Allow use of all FIDO devices listed in the Global Authenticators table and request attestation.

       * **Allow FIDO Certified Authenticators**: Only allow use of FIDO Certified devices, and request attestation.

         |   |                                                                                                                                                                 |
         | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
         |   | To add a FIDO device to the **Global Authenticators Table**, see [Managing the Global Authenticators Table](p1_add_device_to_global_authenticators_table.html). |

       * **Allow Specific Authenticators**: Allow use of only the devices specified. Select this option and then select the devices you want to use in the **Allowed Authenticators table** below the list.

    3. To prevent users from authenticating with other devices that are already registered with their account, but are not included in the **Allow Specific Authenticators** list, select the **Enforce during authentication** check box.

       |   |                                                                                                               |
       | - | ------------------------------------------------------------------------------------------------------------- |
       |   | This option can be applied only to devices that included a FIDO resident key during the registration process. |

14. In the **User Presence Timeout** field, define the amount of time the user has to perform a user presence gesture with their FIDO device before the request expires (the default is two minutes). The value is considered a hint because the browser's FIDO authenticator defines the actual timeout value.

15. Click **Save**.

    ### Result:

    The policy is added to the **Policy** list.

    |   |                                                                                                                             |
    | - | --------------------------------------------------------------------------------------------------------------------------- |
    |   | In the **Policy** list, click a policy to see a summary of the policy details in the right pane or edit an existing policy. |

## Next steps

Add the FIDO policy to the MFA step in the relevant Authentication policy. For information, see [Adding a multi-factor authentication or PingID step](p1_add_mfa_step.html).

---

---
title: Adding a login authentication step
description: "A single-factor authentication step in PingOne requires only one piece of evidence to verify a user's identity."
component: pingone
page_id: pingone:authentication:p1_add_login_auth_step
canonical_url: https://docs.pingidentity.com/pingone/authentication/p1_add_login_auth_step.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 24, 2025
section_ids:
  steps: Steps
---

# Adding a login authentication step

A single-factor authentication step requires only one piece of evidence to verify a user's identity, such as a username and password.

## Steps

1. In the PingOne admin console, go to **Authentication > Authentication**.

2. Click **[icon: plus, set=fa]Add Policy** to create a new policy, or click the **Pencil** icon ([icon: pencil, set=fa]) to edit an existing one.

3. Click **[icon: plus, set=fa]Add Step**.

4. In the **Step Type** list, select **Login**.

5. Enter or edit the recovery and registration settings.

   | Setting                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   | -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Enable account recovery**                  | In case of a forgotten password, users can recover their accounts with a one-time passcode (OTP) *(tooltip: \<div class="paragraph">&#xA;\<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>&#xA;\</div>)* sent to the email address configured in the PingOne user directory.                                                                                                                 |
   | **Enable registration**                      | Users can register their own accounts whether or not a user record already exists.- Select **PingOne** to provision users to the PingOne user store.

   - Select **External Link** to provision users to an external user store. PingOne directs users to the **Registration Target URL** for registration, but PingOne is still used for authentication.                                                                                                                                                                      |
   | **Require confirmation of user information** | If registration is enabled, requires end users to confirm the data that is linked with the third-party identity provider (IdP) *(tooltip: \<div class="paragraph">&#xA;\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>&#xA;\</div>)*. The end user will have an opportunity to edit the information that the third-party IdP shares with PingOne, such as username, email address, first name, and last name. |

6. Enter or edit the requirement conditions. If this condition is met, the user will be required to sign on.

   * **Last sign-on older than**: Requires users to sign on again if their previous sign-on is older than the configured value.

7. Enter or edit an external IdP. Click **[icon: plus, set=fa]Add Provider** and then select an IdP in the list. If an IdP doesn't appear in the list, the IdP might not be enabled. Learn more in [Adding an external identity provider](../integrations/p1_adding_vendor_specific_idps.html).

8. To prevent users from signing on if their PingOne user account is locked, select **Block authentication of locked user accounts from Presented Identity Providers**. If this option is cleared, users can sign on with their configured IdP credentials, but not their PingOne credentials.

9. Click **Save**.

---

---
title: Adding a multi-factor authentication or PingID step
description: Add an MFA or PingID step to a PingOne authentication policy.
component: pingone
page_id: pingone:authentication:p1_add_mfa_step
canonical_url: https://docs.pingidentity.com/pingone/authentication/p1_add_mfa_step.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 2, 2024
section_ids:
  steps: Steps
  steps-2: Steps
---

# Adding a multi-factor authentication or PingID step

A multi-factor authentication (MFA) policy requires two pieces of evidence to verify a user's identity, such as a username and password, as well as MFA authentication methods, such as a passkey, a push notification sent to the user's mobile device, or a one-time passcode (OTP) sent over SMS, voice, or email. You can also use MFA to set up passwordless authentication. Learn more in [Setting up passwordless authentication](p1_set_up_paswordless_auth.html).

Follow the relevant instructions depending on the geography in which your environment is located.

* In the Singapore geography, all steps apply to both [Customer and Workforce](../strong_authentication_mfa/p1_pid_what_is_the_difference.html) environments.

* In all other geographies, some steps differ depending on whether the environment is for Customer or Workforce users.

- All other regions

- Singapore

### Steps

1. In the PingOne admin console, go to **Authentication > Authentication**.

2. Click **[icon: plus, set=fa]Add Policy** to create a new policy, or click the **Pencil** icon ([icon: pencil, set=fa]) to edit an existing one.

3. Click **[icon: plus, set=fa]Add step**.

4. In the **Step Type** list, select either:

   * (Customer only) **Multi-Factor Authentication**

   * (Workforce only) **PingID Authentication**

5. (Customer only) In the **MFA Policy** list, select an MFA policy that has been defined for the environment. Learn more about defining MFA policies in [MFA policies](p1_mfa_policies.html).

6. (Customer only) In the **None or incompatible methods** section:

   For MFA scenarios in which users attempt to sign on but don't have any enrolled MFA devices that comply with the permitted **Available Methods**, select a flow:

   * **Block**: Do not permit these users to sign on because they don't have a usable device for MFA.

   * **Bypass**: Allow users without a usable MFA device to bypass the MFA flow.

     To leverage the **Bypass** option, the user must already be authenticated, either by a password (login step) or by supplying a signed `login_hint_token` in the request object. Learn more about `login_hint_token` in the [GET Authorize (Non-redirect and MFA Only Flows)](https://developer.pingidentity.com/pingone-api/auth/openid-connect-oauth-2/authorize-browserless-and-mfa-only-flows.html) operation in the PingOne API documentation.

7. (Customer only) Enter or edit the requirement conditions. If one or more of the following conditions are met, the user is prompted to use a two-step authentication method.

   * **Last sign-on older than**: Requires users to sign on if their previous sign-on is older than the configured value.

   * **Accessing from IP out of range**: Requires users to sign on if the request comes from an IP address outside of the specified range. Use CIDR notation to specify the IP address range.

   * **Being a member of any of these populations**: Requires users to sign on if the user belongs to the specified population or populations.

   * **User attributes**: Requires users to sign on if they match a specified user attribute, such as postal code or user ID. For example, `Postal Code = 78750`. Select the checkbox, then click **[icon: plus, set=fa]Add attribute**. Enter the attribute and the appropriate value. If you have multiple attribute conditions, the policy will evaluate to true if any of the conditions are met (Boolean OR).

   * **IP reputation is high risk**: PingOne collects and analyzes IP address data of authentication requests from the user's accessing device. An IP address is considered high risk if it might have recently been involved in malicious activities, such as distributed denial-of-service (DDoS) attacks or spam activity. Select the checkbox to require MFA when authentication requests come from IP addresses with high risk scores.

     |   |                                                                                                                      |
     | - | -------------------------------------------------------------------------------------------------------------------- |
     |   | The **IP reputation** option is available only with a PingOne Protect or PingOne for Customers Passwordless license. |

   * **A geovelocity anomaly is detected**: PingOne analyzes location data from the user's accessing device. It determines whether travel time between a user's current sign-on location and their previous sign-on location is possible in the time frame that has elapsed since the previous sign-on. Select the checkbox to require MFA when a geovelocity anomaly is detected.

     |   |                                                                                                                            |
     | - | -------------------------------------------------------------------------------------------------------------------------- |
     |   | The **Geovelocity anomaly** option is only available with a PingOne Protect or PingOne for Customers Passwordless license. |

   * **Anonymous network detection**: PingOne collects and analyzes IP address data of authentication requests from the user's accessing device. Select the checkbox to require MFA when PingOne identifies an IP address as originating from an anonymous network such as an unknown VPN, proxy, or an anonymous communication tool such as Tor. Exclude IP addresses in the **Whitelist** by entering them in CIDR notation in a comma-separated list.

     |   |                                                                                                                                    |
     | - | ---------------------------------------------------------------------------------------------------------------------------------- |
     |   | The **Anonymous network detection** option is only available with a PingOne Protect or PingOne for Customers Passwordless license. |

8. Click **Save**.

### Steps

1. In the PingOne admin console, go to **Authentication > Authentication**.

2. Click **[icon: plus, set=fa]Add Policy** to create a new policy, or click the **Pencil** icon ([icon: pencil, set=fa]) to edit an existing one.

3. Click **[icon: plus, set=fa]Add step**.

4. In the **Step Type** list, select **Multi-Factor Authentication**

5. In the **MFA Policy** list, select an MFA policy that's been defined for the environment. Learn more about defining MFA policies in [MFA policies](p1_mfa_policies.html).

6. In the **None or incompatible methods** section:

   For MFA scenarios in which users attempt to sign on but don't have any enrolled MFA devices that comply with the permitted **Available Methods**, select a flow:

   * **Block**: Do not permit these users to sign on because they don't have a usable device for MFA.

   * **Bypass**: Allow users without a usable MFA device to bypass the MFA flow.

     To leverage the **Bypass** option, the user must already be authenticated, either by a password (login step) or by supplying a signed `login_hint_token` in the request object. Learn more about `login_hint_token` in the [GET Authorize (Non-redirect and MFA Only Flows)](https://developer.pingidentity.com/pingone-api/auth/openid-connect-oauth-2/authorize-browserless-and-mfa-only-flows.html) operation in the PingOne Platform API Reference.

7. Enter or edit the requirement conditions. If one or more of the following conditions are met, the user is prompted to use a two-step authentication method:

   * **Last sign-on older than**: Requires users to sign on if their previous sign-on is older than the configured value.

   * **Accessing from IP out of range**: Requires users to sign on if the request comes from an IP address outside of the specified range. Use CIDR notation to specify the IP address range.

   * **Being a member of any of these populations**: Requires users to sign on if the user belongs to the specified population or populations.

   * **User attributes**: Requires users to sign on if they match a specified user attribute, such as postal code or user ID. For example, `Postal Code = 78750`. Select the checkbox, then click **[icon: plus, set=fa]Add attribute**. Enter the attribute and the appropriate value. If you have multiple attribute conditions, the policy will evaluate to true if any of the conditions are met (Boolean OR).

   * **IP reputation is high risk**: PingOne collects and analyzes IP address data of authentication requests from the user's accessing device. An IP address is considered high risk if it might have recently been involved in malicious activities, such as distributed denial-of-service (DDoS) attacks or spam activity. Select the checkbox to require MFA when authentication requests come from IP addresses with high risk scores.

     |   |                                                                                                                                |
     | - | ------------------------------------------------------------------------------------------------------------------------------ |
     |   | The **IP reputation** option is a feature available only with a PingOne Protect or PingOne for Customers Passwordless license. |

   * **A geovelocity anomaly is detected**: PingOne analyzes location data from the user's accessing device. It determines whether travel time between a user's current sign-on location and their previous sign-on location is possible in the time frame that has elapsed since the previous sign-on. Select the checkbox to require MFA when a geovelocity anomaly is detected.

     |   |                                                                                                                                      |
     | - | ------------------------------------------------------------------------------------------------------------------------------------ |
     |   | The **Geovelocity anomaly** option is a feature available only with a PingOne Protect or PingOne for Customers Passwordless license. |

   * **Anonymous network detection**: PingOne collects and analyzes IP address data of authentication requests from the user's accessing device. Select the checkbox to require MFA when PingOne identifies an IP address as originating from an anonymous network such as an unknown VPN, proxy, or an anonymous communication tool such as Tor. Exclude IP addresses in the **Whitelist** by entering them in CIDR notation in a comma-separated list.

     |   |                                                                                                                                    |
     | - | ---------------------------------------------------------------------------------------------------------------------------------- |
     |   | The **Anonymous network detection** option is available only with a PingOne Protect or PingOne for Customers Passwordless license. |

8. Click **Save**.

---

---
title: Adding a progressive profiling step
description: Add a progressive profiling as part of a PingOne authentication policy.
component: pingone
page_id: pingone:authentication:p1_add_progressive_profiling
canonical_url: https://docs.pingidentity.com/pingone/authentication/p1_add_progressive_profiling.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 9, 2023
section_ids:
  steps: Steps
  related-links: Related links
---

# Adding a progressive profiling step

To use progressive profiling, add it as part of an authentication policy.

|   |                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Because progressive profiling requires the user to be authenticated, it can't be the first step in the authentication policy. Create a login or multi-factor authentication (MFA) step as the first step in the authentication policy. |

## Steps

1. In the PingOne admin console, go to **Authentication > Authentication**.

2. Click **[icon: plus, set=fa]Add Policy** to create a new policy, or click the **Pencil** icon ([icon: pencil, set=fa]) to edit an existing one.

3. Click **[icon: plus, set=fa]Add step**.

4. In the **Step Type** list, select **Progressive Profiling**.

5. In the **Attributes** section, select a user attribute that you want to request. You can select any standard or custom string type attribute, including nested standard attributes (such as `name.family`), but not core or JSON type attributes.

6. Select **Required** if appropriate. If selected, the user won't be able to skip the prompt for requested information. The Skip button won't appear, and users won't be able to sign on until they provide the requested information. Be aware that this option may prevent users from signing on.

7. (Optional) Click **[icon: plus, set=fa]Add attribute** to add another attribute.

8. Enter the following information:

   * **Prompting text**: The text that the user will see before the requested profile information.

   * **Re-prompt every**: If the user skips entering the requested information, determines how soon the user will be prompted again. PingOne checks when the attributes were last updated by any progressive profiling action, such as a progressive profiling action or a progressive profiling form action. If all the attributes of the form have been updated within the specified time frame then the prompt will not be shown. This option applies to optional attributes only, because required attributes cannot be skipped.

   * **Show when**: Select the **Another progressive profiling action has not already been shown** checkbox to show this step only if another progressive profiling step has not already been shown if an authentication policy has multiple progressive profiling steps. This includes progressive profiling actions and progressive profiling form actions.

9. Click **Save**.

## Related links

* [Progressive profiling](p1_progressive_profiling.html)

---

---
title: Adding a terms of service agreement prompt
description: You can require end users to consent to a terms of service agreement as part of a PingOne authentication policy.
component: pingone
page_id: pingone:authentication:p1_add_agreement_prompt
canonical_url: https://docs.pingidentity.com/pingone/authentication/p1_add_agreement_prompt.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 9, 2023
section_ids:
  steps: Steps
  result: Result
---

# Adding a terms of service agreement prompt

You can require end users to consent to a terms of service agreement as part of a sign-on policy. Learn more in [Agreements](../user_experience/p1_agreements.html).

## Steps

1. In the PingOne admin console, go to **Authentication > Authentication**.

2. Click **[icon: plus, set=fa]Add Policy** to create a new policy, or click the **Pencil** icon ([icon: pencil, set=fa]) to edit an existing one.

3. Click **[icon: plus, set=fa]Add step**.

4. In the **Step Type** list, select **Agreement Prompt**.

5. Select the appropriate terms of service agreement. Learn more about creating a terms of service agreement in [Agreements](../user_experience/p1_agreements.html). You can also preview the agreement to see how it will appear to end users.

6. Click **Save**.

## Result

PingOne updates the authentication policy to include the selected terms of service agreement.

---

---
title: Adding an authentication policy
description: You can add one or more authentication policies in PingOne.
component: pingone
page_id: pingone:authentication:p1_add_an_auth_policy
canonical_url: https://docs.pingidentity.com/pingone/authentication/p1_add_an_auth_policy.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 7, 2025
section_ids:
  steps: Steps
---

# Adding an authentication policy

You can add one or more authentication policies.

|   |                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The first step in a policy can't have population or user attribute conditions. Additionally, if the second step in a two-step policy has conditions set, and you delete the first step so that the second step becomes the first, those conditions will be removed. |

## Steps

1. In the PingOne admin console, go to **Authentication > Authentication**.

2. Click **[icon: plus, set=fa]Add Policy**.

3. Enter a policy name.

4. In the **Step Type** list, select the protocol for the first step:

   | Step Type                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
   | --------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Login**                                                                                     | Requires only one piece of evidence to verify a user's identity, such as a username and password.Learn more in [Adding a login authentication step](p1_add_login_auth_step.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | **Identifier First**                                                                          | Allows you to identify users before you authenticate them.Learn more in [Adding an identifier first authentication step](p1_add_identifier_first_auth.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
   | **Multi-factor Authentication** (Customer only) or **PingID Authentication** (Workforce only) | Requires two pieces of evidence to verify a user's identity, such as a username and password as well as a one-time passcode (OTP) *(tooltip: \<div class="paragraph">&#xA;\<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>&#xA;\</div>)*.You can also use multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">&#xA;\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>&#xA;\</div>)* to set up passwordless authentication.Learn more in [Adding a multi-factor authentication or PingID step](p1_add_mfa_step.html) and [Setting up passwordless authentication](p1_set_up_paswordless_auth.html). |
   | **External Identity Provider**                                                                | Allows end users to access your applications by authenticating with the external identity provider (IdP) *(tooltip: \<div class="paragraph">&#xA;\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>&#xA;\</div>)*.Learn more in [Adding an external identity provider sign-on step](p1_add_idp_signon_step.html).                                                                                                                                                                                                                                                                                                                                                                                                                            |

5. (Optional) Click **[icon: plus, set=fa]Add step** to add another step to the authentication policy.

   You can add any of the step types described previously as well as the following step types that can't be used for the first step in an authentication policy:

   | Step Type                 | Description                                                                                                                                                                                                                                                                                                                                                       |
   | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Progressive Profiling** | Allows you to prompt a user for information to be added to their profile after the initial registration step. For example, you could prompt users to add their mobile phone number the next time they sign on. Learn more in [Progressive profiling](p1_progressive_profiling.html) and [Adding a progressive profiling step](p1_add_progressive_profiling.html). |
   | **Agreement Prompt**      | Requires end users to consent to a terms of service agreement as part of a sign-on policy.Learn more in [Agreements](../user_experience/p1_agreements.html).                                                                                                                                                                                                      |

6. Continue adding steps as needed for your authentication policy.

7. Click **Save**.

---

---
title: Adding an external identity provider sign-on step
description: Allow end users to authenticate with an external IdP by configuring the IdP as part of an authentication policy in PingOne.
component: pingone
page_id: pingone:authentication:p1_add_idp_signon_step
canonical_url: https://docs.pingidentity.com/pingone/authentication/p1_add_idp_signon_step.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 6, 2025
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  next-steps: Next steps
  related-links: Related links
---

# Adding an external identity provider sign-on step

If you configure an external identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* as part of a sign-on policy, end users can access your applications by authenticating with the IdP.

An external IdP can be invoked in several ways to authenticate users. The external IdP sign-on step in an authentication policy invokes the external IdP through an administrator declared policy, and the user isn't given a choice. Learn more in [External IdPs](../integrations/p1_external_idps.html).

Depending on the sign-on policy, end users might bypass the PingOne sign-on prompt and be redirected to an external IdP to authenticate. A different sign-on policy could have end users use the PingOne sign-on prompt and then be redirected to an external IdP for second-factor authentication. The user must exist in PingOne, but the IdP manages authentication.

When using Microsoft as the external IdP, you must choose whether the policy is intended to authenticate users through the OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)* protocol or to support external multi-factor authentication (MFA), formerly known as external authentication methods (EAMs), in Microsoft Entra ID.

## Before you begin

* [Set up a connection to your IdP](../integrations/p1_external_idps.html).

* To support external MFA in Microsoft Entra ID, [set up a connection to Microsoft](../integrations/p1_add_idp_microsoft_entra.html).

## Steps

1. In the PingOne admin console, go to **Authentication > Authentication**.

2. Click **[icon: plus, set=fa]Add Policy** to create a new policy, or click the **Pencil** icon ([icon: pencil, set=fa]) to edit an existing one.

3. Click **[icon: plus, set=fa]Add Step**.

4. In the **Step type** list, select **External identity provider**.

5. In the **External Identity Provider** list, select the IdP that will handle user authentication.

6. If Microsoft is selected for **External Identity Provider**, for **Policy Purpose**, select a method for users to authenticate:

   * **OIDC Authentication**: Select this option if you want users to authenticate with Microsoft using the OIDC protocol.

   * **Entra ID External Authentication Method**: Select this option if you want users to authenticate first with Microsoft Entra ID and then with PingOne as the external provider for MFA. If you choose this option, skip to step 10.

7. Enter or edit the registration settings:

   | Setting                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
   | -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Enable registration**                      | Users can register their own accounts whether or not a user record already exists.                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | **Population**                               | Specify which population will contain the newly registered users.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | **Require confirmation of user information** | If registration is enabled, requires end users to confirm the data that is linked with the third-party IdP *(tooltip: \<div class="paragraph">&#xA;\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>&#xA;\</div>)*. The end user will have an opportunity to edit the information that the third-party IdP shares with PingOne, such as username, email address, first name, and last name. |

8. Enter or edit the requirement condition.

   If this condition is met, the user will be required to sign on.

   * **Last sign-on older than**: Requires users to sign on again if their previous sign on is older than the configured value.

9. Enter or edit the IdP settings.

   |   |                                                                                                                                 |
   | - | ------------------------------------------------------------------------------------------------------------------------------- |
   |   | These options are available only if you have an IdP sign-on step as a secondary step after a sign-on step that includes an IdP. |

   | Setting                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | **Required authentication level** | For SAML and OIDC identity providers, PingOne sends the `RequestedAuthnContext` or `acr_values` parameter to the specified IdP to indicate how the IdP should authenticate the user. This is commonly used to tell the IdP to use MFA, for example, to ensure the right level of authentication depending on the sensitivity of the target application.                                                                                                                                                                                                                                                                                                            |
   | **Pass user context to provider** | For SAML and OIDC identity providers, PingOne can be configured to include some user information in the authentication request. The information to include is determined as follows:- If the user is linked to the IdP, pass the `external id` for the user.

   - If the user isn't linked to the IdP and is identified in a previous sign-on step or existing session, pass the PingOne `username` for the user.

   - If the user doesn't have an existing session, either from a previous transaction or from completing a sign-on step before the external IdP step in the sign-on policy, pass the `loginHint` if it was received from the downstream application. |

10. If the **Entra ID External Authentication Method** option is selected for **Policy Purpose**, click **[icon: plus, set=fa]Add Step** and select **PingID Authentication** in the **Step Type** list.

11. Click **Save**.

## Next steps

If you're configuring external MFA in Microsoft Entra ID, add an OIDC application in PingOne and assign your authentication policy to your application. Learn more in [Editing an application for Microsoft Entra ID external MFA](../applications/p1_configure_oidc_application_microsoft_entra_eam.html).

## Related links

* [Adding a login authentication step](p1_add_login_auth_step.html)

* [Adding a multi-factor authentication or PingID step](p1_add_mfa_step.html)

* [Adding an identifier first authentication step](p1_add_identifier_first_auth.html)

---

---
title: Adding an identifier first authentication step
description: Add an identifier first authentication as part of an authentication policy in PingOne.
component: pingone
page_id: pingone:authentication:p1_add_identifier_first_auth
canonical_url: https://docs.pingidentity.com/pingone/authentication/p1_add_identifier_first_auth.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 9, 2025
section_ids:
  steps: Steps
  related-links: Related links
---

# Adding an identifier first authentication step

To use identifier first authentication, add it as part of an authentication policy.

## Steps

1. In the PingOne admin console, go to **Authentication > Authentication**.

2. Click **[icon: plus, set=fa]Add Policy** to create a new policy, or click the **Pencil** icon ([icon: pencil, set=fa]) to edit an existing one.

3. Click **[icon: plus, set=fa]Add step**.

4. In the **Step Type** list, select **Identifier First**.

5. Enter or edit the recovery and registration settings:

   | Setting                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Enable account recovery**                  | In case of a forgotten password, users can recover their accounts with a one-time passcode (OTP) *(tooltip: \<div class="paragraph">&#xA;\<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>&#xA;\</div>)* sent to the email address configured in the PingOne user directory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | **Enable registration**                      | Users can register their own accounts whether or not a user record already exists.- Select **PingOne** to provision users to the PingOne user store.

   - Select **External Link** to provision users to an external user store. PingOne directs users to the **Registration Target URL** for registration, but PingOne is still used for authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
   | **Require confirmation of user information** | If registration is enabled, requires end users to confirm the data that is linked with the third-party identity provider (IdP) *(tooltip: \<div class="paragraph">&#xA;\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>&#xA;\</div>)*. The end user will have an opportunity to edit the information that the third-party IdP shares with PingOne, such as username, email address, first name, and last name.                                                                                                                                                                                                                                                                                                                                                                                        |
   | **Discovery rules**                          | Click **[icon: plus, set=fa]Add Rule** to add a rule, or **Edit Rules** to modify an existing rule and complete the following fields:- **Username Contains**: Enter a domain name to be evaluated by this rule. The rule will evaluate to true if the string contains any part of the provided value.

     &#xA;&#xA;For increased security, be specific and enter multiple canonical domains, such as @marketing.example.com and @payroll.example.com. To add fewer entries, you could just enter example.com, and the rule would pick up both @marketing.example.com and @payroll.example.com, but that configuration might match users at unintended hosts.

   - **Identity Provider**: Select the IdP to use for authentication if the rule is matched. Discovery rules are evaluated in the order they appear in the list.

     &#xA;&#xA;Users that don't match a discovery rule are authenticated against PingOne. |

6. Enter or edit the requirement conditions.

   If this condition is met, the user will be required to sign on:

   * **Last sign-on older than**

     Requires users to sign on if their previous sign-on is older than the configured value.

   * **User attributes**

     Requires users to sign on if they match a specified user attribute, such as postal code or user ID. For example, `Postal Code = 78750`. Select the checkbox, then click **[icon: plus, set=fa]Add attribute**. Enter the attribute and the appropriate value. If you have multiple attribute conditions, the policy evaluates to true if any of the conditions are met (Boolean OR).

7. Enter or edit an external IdP. Click **[icon: plus, set=fa]Add Provider** and then select an identity provider in the list. If an IdP doesn't appear in the list, the IdP might not be enabled. Learn more in [Adding an external identity provider](../integrations/p1_adding_vendor_specific_idps.html).

8. To prevent users from signing on if their PingOne user account is locked, select **Block authentication of locked user accounts from Presented Identity Providers**. If this option is cleared, users can sign on with their configured IdP credentials, but not their PingOne credentials.

9. Click **Save**.

## Related links

* [Identifier first authentication](p1_idp_first_auth.html)

* [Progressive profiling](p1_progressive_profiling.html)

---

---
title: Adding an MFA policy
description: Create a multi-factor authentication (MFA) policy and then add it as a step to your authentication policy.
component: pingone
page_id: pingone:authentication:p1_creating_an_mfa_policy
canonical_url: https://docs.pingidentity.com/pingone/authentication/p1_creating_an_mfa_policy.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 5, 2024
---

# Adding an MFA policy

Create a multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)* policy and then add it as a step to your authentication policy.

For details about how to configure an MFA policy, see [Configuring an MFA policy for strong authentication](../strong_authentication_mfa/p1_creating_an_mfa_policy_for_strong_auth.html).

You can find more information in [Updating an existing MFA policy to use FIDO2](../strong_authentication_mfa/p1_updating_an_mfa_policy_to_fido2.html).

---

---
title: Authentication
description: The Authentication section in PingOne provides access to your Authentication, Password, MFA, and FIDO policies.
component: pingone
page_id: pingone:authentication:p1_main_authentication_menu
canonical_url: https://docs.pingidentity.com/pingone/authentication/p1_main_authentication_menu.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 13, 2023
---

# Authentication

The **Authentication** section provides access to the different types of policies in your environment:

* [Authentication policies](p1_authenticationpolicies.html)

* [Password policies](p1_passwordpolicies.html)

* [MFA policies](p1_mfa_policies.html)

* [FIDO policies](p1_fido_policies.html)

You can also manage your **MFA Settings** from this section. Learn more in [MFA Settings](p1_mfa_settings.html).

---

---
title: Authentication policies
description: Authentication policies dictate how the user's identity is verified. For example, a single-factor authentication policy requires a single piece of evidence to verify a user's identity, such as a password. A multi-factor policy could require evidence to verify a user's identity, such as a Time-based One-Time Password (TOTP) authenticator app, FIDO2 biometrics, a push notification sent to the user's mobile device, or a one-time passcode sent over SMS, voice or email. You can also use multi-factor authentication to set up passwordless authentication. You can determine whether users who don't have any enrolled multi-factor authentication (MFA) devices can bypass the MFA flow, or are blocked from sign-on.
component: pingone
page_id: pingone:authentication:p1_authenticationpolicies
canonical_url: https://docs.pingidentity.com/pingone/authentication/p1_authenticationpolicies.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 22, 2026
---

# Authentication policies

Authentication policies dictate how the user's identity is verified. For example, a single-factor authentication policy requires a single piece of evidence to verify a user's identity, such as a password. A multi-factor policy could require evidence to verify a user's identity, such as a Time-based One-Time Password (TOTP) authenticator app, FIDO2 biometrics, a push notification sent to the user's mobile device, or a one-time passcode sent over SMS, voice or email. You can also use multi-factor authentication to set up passwordless authentication. You can determine whether users who don't have any enrolled multi-factor authentication (MFA) devices can bypass the MFA flow, or are blocked from sign-on.

|   |                                                                                                                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Using a username and MFA as your primary authentication method can expose users to security risks like username enumeration, MFA fatigue attacks, targeted phishing, and denial-of-service incidents. To reduce exposure, use a passwordless method like FIDO2 biometrics for primary authentication. |

For each authentication policy, you can set a condition that determines when it applies. For example, the Single\_Factor policy can include a condition that requires users to sign on if the most recent sign-on occurred more than eight hours ago. If no conditions are specified, users are required to sign on every time they access the application.

---

---
title: Configuring MFA settings
description: You can define MFA settings for end users, such as the maximum number of methods that a user can set up for authentication, authentication method selection, as well as account lockout settings. These settings are applied at the environment level.
component: pingone
page_id: pingone:authentication:p1_configure_mfa_settings
canonical_url: https://docs.pingidentity.com/pingone/authentication/p1_configure_mfa_settings.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 21, 2024
section_ids:
  steps: Steps
  next-steps: Next steps
---

# Configuring MFA settings

You can define MFA settings for end users, such as the maximum number of methods that a user can set up for authentication, authentication method selection, as well as account lockout settings. These settings are applied at the environment level.

## Steps

1. Go to **Authentication > MFA Settings**.

2. For **MFA status for new users**, specify whether MFA should be enabled by default for a user when their account is created.

3. For **Maximum allowed methods**, select the maximum number of authentication methods that users can set up for their accounts. The default is 5. Users can have multiple authentication methods using the same device. For example, an end user could have SMS, voice, biometrics, and an authenticator app all on a single mobile device.

   |   |                                                                                                                                                                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you reduce the maximum value, existing methods are not affected. For example, if a user has four authentication methods set up, but you reduce the maximum number to three, the user won't have to remove an existing authentication method. |

4. If some of your users will be pairing devices that have phone numbers with extensions, set the **Phone numbers with extensions** option to **Enabled**.

5. For **Account lockout**, enter or edit the following:

   * **Account lockout**: The maximum number of incorrect MFA authorization actions a user can attempt (such as entering an incorrect OTP or declining a push confirmation on a mobile device) before the account is locked.

     |   |                                                                                |
     | - | ------------------------------------------------------------------------------ |
     |   | This value includes MFA authentication attempts across all configured devices. |

   * **Account lockout duration**: The amount of time (in seconds) to keep the account locked after the failure count is exceeded. The account will automatically unlock after the specified time passes.

6. Select the type of key to use for pairing of devices: **12-digit numeric** key or **16-character alphanumeric** key.

7. Click **Save**.

## Next steps

You can unlock or disable a user account on the user details page. Learn more in [Enabling or unlocking a user account or device](../directory/p1_enable_a_user.html).

---

---
title: Editing an authentication policy
description: Use the Authentication page to modify existing authentication policies in PingOne.
component: pingone
page_id: pingone:authentication:p1_edit_auth_policy
canonical_url: https://docs.pingidentity.com/pingone/authentication/p1_edit_auth_policy.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  editing-a-single-factor-authentication-policy: Editing a single-factor authentication policy
  editing-a-multi-factor-authentication-policy: Editing a multi-factor authentication policy
  next-steps: Next steps
---

# Editing an authentication policy

Use the **Authentication** page to modify existing authentication policies in PingOne.

## Editing a single-factor authentication policy

A single-factor authentication policy requires only one piece of evidence to verify a user's identity, such as a username and password.

1. In the PingOne admin console, go to **Authentication > Authentication**.

2. For **Single\_Factor**, click the **Details** icon to expand the policy and then click the **Pencil** icon ([icon: pencil, set=fa]).

3. Enter or edit the **Login** settings:

   | Setting                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   | --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Enable account recovery** | In case of a forgotten password, users can recover their accounts with a one-time passcode (OTP) *(tooltip: \<div class="paragraph">&#xA;\<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>&#xA;\</div>)* sent to the email address configured in the PingOne user directory.                                                                  |
   | **Enable registration**     | Users can register their own accounts whether or not a user record already exists.- Select **PingOne** to provision users to the PingOne user store.

   - Select **External Link** to provision users to an external user store. PingOne directs users to the **Registration Target URL** for registration, but PingOne is still used for authentication.                                                                                                                       |
   | **Last sign-on older than** | Requires users to sign on again if their previous sign-on is older than the configured value.&#xA;&#xA;The PingOne admin console uses a system policy that doesn't allow you to change this setting.&#xA;&#xA;The administrator must reauthenticate if they've been inactive for more than 30 minutes. If the administrator is active in the console within the 30-minute period, the session refreshes and reauthentication isn't necessary. MFA is required every 12 hours. |

4. Enter or edit an external identity provider (IdP) *(tooltip: \<div class="paragraph">
   \<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
   \</div>)*. Click **[icon: plus, set=fa]Add Provider** and then select an IdP from the list. If an IdP doesn't appear in the list, it might not be enabled. Learn more in [Adding an external identity provider](../integrations/p1_adding_vendor_specific_idps.html).

5. To prevent users from signing on if their PingOne user account is locked, select **Block authentication of locked user accounts from Presented Identity Providers**. If you leave this option cleared, users can sign on with their configured IdP credentials but not their PingOne credentials.

6. Click **Save**.

## Editing a multi-factor authentication policy

A multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)* policy requires two pieces of evidence to verify a user's identity, such as a username and password and a push notification to the user's mobile device or an OTP sent through SMS, voice, or email.

|   |                                                                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The first step in a policy can't have population or user attribute conditions. Additionally, if the second step in a two-step policy has conditions set, and you delete the first step so that the second step becomes first, those conditions are removed. |

1. In the PingOne admin console, go to **Authentication > Authentication**.

2. For **Multi\_Factor**, click the **Details** icon to expand the policy and then click [icon: pencil, set=fa].

3. Enter or edit the **Login** settings:

   | Setting                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
   | -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Enable account recovery**                  | In case of a forgotten password, users can recover their accounts with a OTP *(tooltip: \<div class="paragraph">&#xA;\<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>&#xA;\</div>)* sent to the email address configured in the PingOne user directory.                                                                                                                 |
   | **Enable registration**                      | Users can register their own accounts whether or not a user record already exists.- Select **PingOne** to provision users to the PingOne user store.

   - Select **External Link** to provision users to an external user store. PingOne directs users to the **Registration Target URL** for registration, but PingOne is still used for authentication.                                                                                                                                                  |
   | **Population**                               | If registration is enabled, select the population to which the end user will be added.                                                                                                                                                                                                                                                                                                                                                                                                                   |
   | **Require confirmation of user information** | If registration is enabled, requires end users to confirm the data that is linked with the third-party IdP *(tooltip: \<div class="paragraph">&#xA;\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>&#xA;\</div>)*. The end user will have an opportunity to edit the information that the third-party IdP shares with PingOne, such as username, email address, first name, and last name. |
   | **Last sign-on older than**                  | Requires users to sign on again if their previous sign-on is older than the configured value.                                                                                                                                                                                                                                                                                                                                                                                                            |

4. In the **MFA Policy** list, select an MFA policy. Learn more in [MFA policies](p1_mfa_policies.html).

5. For **None or incompatible methods**, choose the MFA flow to use for MFA scenarios when users attempt to sign on but don't have any enrolled MFA devices that comply with the permitted **Available Methods**:

   * **Block**: Don't permit these users to sign on because they don't have a usable device for MFA.

   * **Bypass**: Allow users without a usable MFA device to bypass the MFA flow.

     To leverage the **Bypass** option, the user must already be authenticated by a password (**Login** step) or by supplying a signed `login_hint_token` in the request object. Learn more about `login_hint_token` in the [GET Authorize (Non-redirect and MFA Only Flows)](https://developer.pingidentity.com/pingone-api/auth/openid-connect-oauth-2/authorize-browserless-and-mfa-only-flows.html) operation in the PingOne Platform API Reference.

6. Enter or edit the MFA conditions. If one or more of the following conditions are met, the user is prompted to use a two-step authentication method:

   * **Last sign-on older than**: The previous sign-on is older than the configured value.

   * **Accessing from IP out of range**: The request comes from an IP address outside of the specified range. Use CIDR notation to specify the IP address range.

   * **Being a member of any of these populations**: The user belongs to the specified population or populations.

   * **User Attributes**: Requires users to sign on if they match a specified user attribute, such as postal code or user ID. For example, `Postal Code = 78750`. Select the checkbox and enter the attribute and the appropriate value. To add additional attributes, click **[icon: plus, set=fa]Add attribute**. If you have multiple attribute conditions, the policy evaluates to true if any of the conditions are met (Boolean OR).

   * **IP reputation is high risk**: PingOne collects and analyzes IP address data of authentication requests from the user's accessing device. An IP address is considered high risk if it could have recently been involved in malicious activities, such as DDoS attacks or spam activity. Select the checkbox to require MFA when authentication requests come from IP addresses with high risk scores.

     |   |                                                                                                                                        |
     | - | -------------------------------------------------------------------------------------------------------------------------------------- |
     |   | The **IP reputation** option is a feature that is available only with a PingOne Protect or PingOne for Customers Passwordless license. |

   * **A geovelocity anomaly is detected**. PingOne analyzes location data from the user's accessing device. It determines whether travel time between a user's current sign-on location and their previous sign-on location is possible in the time frame that has elapsed since the previous sign-on. Select the checkbox to require MFA when a geovelocity anomaly is detected.

     |   |                                                                                                                                              |
     | - | -------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | The **Geovelocity anomaly** option is a feature that is available only with a PingOne Protect or PingOne for Customers Passwordless license. |

   * **Anonymous network detection**: PingOne collects and analyzes IP address data of authentication requests from the user's accessing device. Select the checkbox to require MFA when PingOne identifies an IP address as originating from an anonymous network, such as an unknown VPN, proxy, or an anonymous communication tool (for example, Tor). Exclude IP addresses in the **Whitelist** by entering them in CIDR notation in a comma-separated list.

     |   |                                                                                                                                              |
     | - | -------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | The **Anonymous network detection** option is a feature available only with a PingOne Protect or PingOne for Customers Passwordless license. |

7. Click **Save**.

## Next steps

You can add more steps to the authentication policy. Click **[icon: plus, set=fa]Add step**, select the step type, and enter the values for the selected type.

Learn more in:

* [Adding a login authentication step](p1_add_login_auth_step.html)

* [Adding a multi-factor authentication or PingID step](p1_add_mfa_step.html)

* [Adding an identifier first authentication step](p1_add_identifier_first_auth.html)

* [Adding a progressive profiling step](p1_add_progressive_profiling.html)

* [Adding a terms of service agreement prompt](p1_add_agreement_prompt.html)

* [Adding an external identity provider sign-on step](p1_add_idp_signon_step.html)

---

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