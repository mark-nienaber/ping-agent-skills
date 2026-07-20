---
title: PingOne administrators MFA requirement - FAQ
description: As part of our ongoing commitment to enterprise security and supporting best practices, multi-factor authentication (MFA) will become mandatory for all PingOne administrators on June 1, 2025.
component: pingone-admin-mfa-faq
page_id: pingone-admin-mfa-faq::p1_mfa_required_for_admins_faq
canonical_url: https://docs.pingidentity.com/pingone-admin-mfa-faq/p1_mfa_required_for_admins_faq.html
revdate: April 8, 2025
section_ids:
  how-is-authentication-to-the-pingone-administrator-console-changing: How is authentication to the PingOne administrator console changing?
  what-mfa-product-is-being-used-and-what-methods-are-provided: What MFA product is being used, and what methods are provided?
  environments-without-pingid: Environments without PingID
  what-if-i-am-not-licensed-for-pingone-mfa: What if I am not licensed for PingOne MFA?
  what-are-the-new-default-mfa-policy-settings-for-administrators: What are the new default MFA policy settings for administrators?
  environments-with-pingid: Environments with PingID
  who-will-be-impacted-by-this-change: Who will be impacted by this change?
  can-you-make-exceptions-to-this-requirement: Can you make exceptions to this requirement?
  can-i-turn-off-the-new-administrator-security-setting-after-i-opt-in-to-preview-the-feature: Can I turn off the new administrator security setting after I opt in to preview the feature?
  how-do-i-prepare-my-organization-to-support-mandatory-mfa: How do I prepare my organization to support mandatory MFA?
  how-do-i-enable-mandatory-mfa-for-my-organization-and-pingone-environments: How do I enable mandatory MFA for my organization and PingOne environments?
  what-if-im-using-an-external-identity-provider-as-my-authentication-source: What if I'm using an external identity provider as my authentication source?
  how-will-existing-sign-on-policies-map-to-the-new-2-factor-verification-policy-when-the-migration-occurs: How will existing sign-on policies map to the new 2-factor verification policy when the migration occurs?
  what-will-the-new-sign-on-experience-look-like-for-administrators: What will the new sign-on experience look like for administrators?
  how-long-is-the-transition-period-when-will-it-end: How long is the transition period? When will it end?
  what-if-i-am-using-the-ping-identity-pingone-terraform-providers: What if I am using the Ping Identity PingOne Terraform Providers?
  more-questions: More questions?
---

# PingOne administrators MFA requirement - FAQ

As part of our ongoing commitment to enterprise security and supporting best practices, multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)* will become mandatory for all PingOne administrators on June 1, 2025.

## How is authentication to the PingOne administrator console changing?

PingOne administrators currently using PingOne sign-on policies to authenticate to the admin console will be required to enable MFA.

During the transition period, when administrators sign on to the console, they will be presented with the option to enable mandatory MFA for administrators on a per-environment basis. After June 1, 2025, an updated default sign-on policy that requires a second authentication method to be registered and used will be automatically applied to all PingOne environments that do not have mandatory MFA for administrators enabled.

## What MFA product is being used, and what methods are provided?

### Environments without PingID

For environments that do not use PingID for authentication, we are making the following methods from the PingOne MFA service (Ping Identity's customer identity MFA product) available for all PingOne administrators in the Administrators environment:

* Email

* Push notifications (TOTP)

* FIDO2

PingOne environments still using FIDO must update to a FIDO2 policy to enable FIDO2 for administrator sign-on. Because it can introduce breaking changes, this is a manual opt-in. Customers must follow these [steps to enable FIDO2](https://docs.pingidentity.com/pingone/strong_authentication_mfa/p1_updating_an_mfa_policy_to_fido2.html). FIDO (original) devices will continue to work for administrator authentication, but the new administrator MFA policy will not allow just-in-time (JIT) registration of new FIDO (original) devices. After the new policy has been enabled, it will allow JIT registration of FIDO2 devices.

Only email and push notifications will be available for environments that do not have an administrator license and that are not licensed for PingOne MFA.

#### What if I am not licensed for PingOne MFA?

Customers do not need to be licensed for PingOne MFA to use MFA for administrator sign-on.

If you are licensed for PingOne MFA, you can add additional methods for authentication, such as FIDO2, to the applicable sign-on policy.

Ping recommends creating and managing all administrator identities in the Administrators environment and enforcing phishing-resistant verification methods, such as push notifications or FIDO2.

|   |                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For tenants created prior to July 2020, there might not be an Administrators environment and corresponding license. We will be making administrative licenses available to all tenants during the transition period. |

#### What are the new default MFA policy settings for administrators?

* Restricted methods:

  * SMS

  * Voice

  * Mobile

* Method selection: user selected default

* Notification: send email notification when new method or device is paired

* Allowed authentication methods:

  * Email

    * Passcode failure limit: 3

    * Lock duration: 0 min

    * Passcode lifetime: 30 min

  * Authenticator App (TOTP)

    * Passcode failure limit: 3

    * Lock duration: 2 min

    * Allow pairing: Yes

  * FIDO2

    * Uses the default policy assigned in PingOne

### Environments with PingID

If your environment includes PingID and the environment was created before January 7, 2025, the authentication policy and allowed MFA methods are configured from the PingID admin portal.

If the environment was created after January 7, 2025, or if your PingID tenant was migrated to PingOne after March 31, 2025, the default MFA policy and allowable MFA methods are managed from the PingOne admin console in **Authentication > MFA**. Learn more in [Configuring strong authentication methods](https://docs.pingidentity.com/pingone/strong_authentication_mfa/p1_move_pid_management_to_p1.html).

## Who will be impacted by this change?

All administrator users of PingOne.

|   |                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------- |
|   | This change does not apply to PingOne for Enterprise (Legacy) or PingOne for SaaS Apps (Legacy) customers. |

## Can you make exceptions to this requirement?

We strongly believe that security is paramount and are taking steps to ensure that this process is seamless for all our customers. As such, no exceptions will be made. Ping Identity will require MFA for all PingOne administrators as of June 1, 2025.

## Can I turn off the new administrator security setting after I opt in to preview the feature?

If you enabled mandatory MFA during the transition period and did not disable it before January 27, 2025, you must contact Support to disable the enhanced security.

After June 1, 2025, an updated default sign-on policy requiring the registration of a second authentication method will be automatically applied to all PingOne environments that did not previously have mandatory MFA enabled for administrators. You won't be able to disable this policy.

## How do I prepare my organization to support mandatory MFA?

Ensure all administrators have MFA devices registered (email, TOTP, FIDO2).

Enable the new settings early so that all changes are transparent when the transition deadline passes.

## How do I enable mandatory MFA for my organization and PingOne environments?

* PingOne administrators with the Organization Admin or Environment Admin roles can enable the new administrator security settings from **Settings > Administrator Security** or from the **Update Admin MFA Settings** modal presented when you sign on to an environment. You can disable the settings from **Settings > Administrator Security** until January 27, 2025. After January 27 you must contact Support to disable the enhanced security.

  After June 1, 2025 these settings are required for all environments and can't be disabled.

* PingOne administrator roles without the appropriate permissions will not see the **Administrator Security** menu item.

* Environments that do not have the new MFA policy enabled will be automatically migrated June 1, 2025.

## What if I'm using an external identity provider as my authentication source?

If you are using an external identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* as your primary authentication source, you do not need to set up MFA in PingOne because you can set up MFA in your external IdP.

When the administrator MFA security setting is enabled, PingOne will update the location where the authentication policy is configured but no additional changes will be needed. Authentication using the external IdP will remain unchanged.

A new chip will appear on the external IdP connection in **Integrations > External IdPs**. Deleting or disabling the connection will be prevented when assigned to the PingOne Admin Console system application.

![Screen capture of an external IdP that has the Administrator IdP chip](_images/lek1715026276892.png)

## How will existing sign-on policies map to the new 2-factor verification policy when the migration occurs?

The table below describes how existing sign-on policy configurations will map to the new platform sign-on policy for administrators.

| Current Configuration                                         | New Configuration                             |
| ------------------------------------------------------------- | --------------------------------------------- |
| Username and Password Only (no MFA)                           | PingOne System Policy: UN, PW, + MFA          |
| Username and Password + MFA (multi-step sign-on policy)       | PingOne System Policy: UN, PW, + MFA          |
| Username and Password (PingOne) or External Identity Provider | Authentication source: PingOne & External IDP |
| External Identity Provider                                    | External Identity Provider (no change)        |

## What will the new sign-on experience look like for administrators?

The sign-on experience for administrators authenticating to PingOne will look and function the same as it does today with one exception: administrators who are used to authenticating with an identifier-first sign-on page (username only) will now be presented with a form to enter username and password.

If the administrator does not already have a relevant MFA method registered (email, FIDO2, or TOTP), they will be walked through the process of registering an MFA method at their next sign-on attempt.

Subsequent sign-on attempts will require a second factor for verification.

## How long is the transition period? When will it end?

Ping Identity will require MFA for all PingOne administrators as of June 1, 2025.

## What if I am using the Ping Identity PingOne Terraform Providers?

All Terraform providers distributed and managed by Ping Identity will be updated before the new security settings are required for all environments on June 1, 2025.

## More questions?

Contact your customer success representative or account executive.