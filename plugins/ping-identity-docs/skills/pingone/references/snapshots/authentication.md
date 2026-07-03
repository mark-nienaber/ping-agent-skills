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
