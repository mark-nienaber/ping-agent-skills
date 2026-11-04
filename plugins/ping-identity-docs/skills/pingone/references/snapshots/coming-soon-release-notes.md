---
title: Coming Soon to PingOne
description: PingOne platform and PingOne services coming soon announcements provide advance notice of changes that can help you prepare for updates.
component: pingone
page_id: pingone:coming_soon_release_notes:index
canonical_url: https://docs.pingidentity.com/pingone/coming_soon_release_notes/index.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-23T21:01:18Z
section_ids:
  2026: 2026
  october-2026: October 2026
  october-29: October 29
  configuration-management-and-promotion-moving-from-ea-to-ga: Configuration management and promotion moving from EA to GA
  october-22: October 22
  configurable-timeout-settings-for-administrator-security: Configurable timeout settings for Administrator Security
  october-15: October 15
  cross-protocol-logout-and-other-logout-enhancements: Cross-protocol logout and other logout enhancements
  allow-large-kerberos-tickets: Allow large Kerberos tickets
  october-13: October 13
  dkim-requirement-for-email-trust: DKIM requirement for email trust
  october-12: October 12
  new-trusted-email-domain-requirement-for-customizing-notification-templates: New trusted email domain requirement for customizing notification templates
  october-1: October 1
  support-for-microsoft-entra-id-hybrid-join-in-all-geographies: Support for Microsoft Entra ID hybrid join in all geographies
  september-2026: September 2026
  september-30: September 30
  new-default-lock-duration-for-mfa-policies: New default lock duration for MFA policies
  september-18: September 18
  account-updated-notifications: Account updated notifications
  account-lockout-notifications: Account lockout notifications
---

# Coming Soon to PingOne

PingOne platform and PingOne services coming soon announcements provide advance notice of changes that can help you prepare for updates.

|   |                                                                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Features listed on this page are subject to change and are not guaranteed to be included in future releases. The information is provided for planning purposes only and does not represent a commitment by Ping Identity to deliver any specific feature or functionality. |

Subscribe to the [icon: rss-square, set=fa][Coming Soon to PingOne RSS feed](index.xml) to get automatic updates.

|   |                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | A Released label indicates the feature is available in the PingOne platform or PingOne services.You can read more about released features in the [PingOne release notes](../release_notes/index.html). |

## 2026

### October 2026

#### October 29

##### Configuration management and promotion moving from EA to GA

Coming soon PingOne

We'll soon move the new native PingOne configuration promotion capabilities in PingOne from early access to general availability. These tools will allow you to automate the promotion of configuration resources (such as applications, PingOne DaVinci flows, and policies) from one environment to another environment from the PingOne admin console of the source environment.

You'll also be able to use the PingOne configuration management APIs to perform promotions.

Learn more in [Early Access Features in PingOne](../early-access-features/p1_early_access_features.html) and in the [Early Access](https://developer.pingidentity.com/pingone-api-ea/platform/early-access.html) API documentation.

#### October 22

##### Configurable timeout settings for Administrator Security

Coming soon PingOne

When this feature is available, you will be able to configure timeout settings that determine when and how administrators must reauthenticate in the PingOne admin console after periods of inactivity.

#### October 15

##### Cross-protocol logout and other logout enhancements

Coming soon PingOne PingOne SSO

You'll soon be able to trigger cross-protocol logouts and define valid post-logout destinations in one place:

* **`/xp/signoff` endpoint**: Explicitly triggers cross-protocol logout requests to be sent to applicable applications and SAML identity providers.

* **Cross-protocol logout option**: Triggers cross-protocol logout requests based on logout requests from supported protocols. This is disabled by default to preserve existing behavior, ensuring a logout request from one protocol doesn't automatically trigger logouts for partners using other protocols.

* **Centralized OIDC post-logout redirect URI validation method**: Validates `post_logout_redirect_uri` parameter values found in OpenID Connect (OIDC) relying party (RP)-initiated logout requests against a centralized list of valid destinations. This is disabled by default to preserve existing validation behavior.

* **Centralized post-logout redirect URIs**: Defines valid post-logout redirect URIs in one place. These are applicable to cross-protocol, SAML 2.0, and WS-Federation logout requests, and optionally to OIDC RP-initiated logout requests.

##### Allow large Kerberos tickets

Released Oct 28, 2026 PingOne PingOne SSO DaVinci

Authentication policies and PingOne DaVinci flows using the PingOne connector **Authenticate User via Kerberos** capability will soon support Kerberos-based Integrated Windows Authentication (IWA) for users who are members of large numbers of groups. Previously, these users would experience a form-based sign-on because their Kerberos header exceeded the 6 KB platform limit for request headers. For customers using Cloudflare-based custom domains, this capability will increase the Kerberos header size limit to 64 KB.

#### October 13

##### DKIM requirement for email trust

Coming soon PingOne MFA

When this feature becomes available, you'll be required to configure DKIM for your email domain. Use of DKIM enhances email trust and improves email delivery rates. You won't be able to add new trusted email addresses until DKIM is configured.

|   |                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------- |
|   | Add DKIM configurations by October 31, 2026 to ensure you can add and make changes in your current email trust configuration. |

Learn how to configure DKIM in [Setting up a trusted email domain](../settings/p1_set_up_trusted_email_domain.html).

#### October 12

##### New trusted email domain requirement for customizing notification templates

Coming soon PingOne

When this feature is available, a validated trusted email domain or a custom email sender will be required to customize email notification templates to help protect email reputation. Customized emails won't be sent from the PingOne sender domain, and the template editor will be read-only for email templates.

In existing environments, any already customized email templates will be retained. However, a validated trusted email domain or a custom email sender will be required to further customize existing customized templates.

#### October 1

##### Support for Microsoft Entra ID hybrid join in all geographies

Released Oct 27, 2026 PingOne SSO

You'll soon be able to use PingOne to support the Microsoft Entra ID hybrid join use case in all geographies. This capability is currently available in the North American (US) geography only. It enables hybrid-joined Windows devices to obtain and renew primary refresh tokens (PRTs) whether users sign on with PingID Windows Login Passwordless or standard usernames and passwords.

This new feature will require a PingOne for Workforce Plus or Premium license. Contact your account team if you need to upgrade.

### September 2026

#### September 30

##### New default lock duration for MFA policies

Coming soon PingOne MFA

When this feature is available, the default **Lock duration** in **MFA policies** for SMS, Voice, and Email will change from 0 to 2 minutes in new environments only. This helps protect against brute-force attacks.

#### September 18

##### Account updated notifications

Released Oct 1, 2026 PingOne

You'll be able to use a DaVinci flow to send **Account Updated** email notifications to users when their account details change. When this feature is available, you'll have the option to configure an **Account Updated** template on the **Notification Templates** page using the standard template workflows.

##### Account lockout notifications

Coming soon PingOne

You'll be able to use a DaVinci flow to send **Account Disabled** email notifications to users when their account is locked. When this feature is available, you'll have the option to configure an **Account Disabled** template on the **Notification Templates** page using the standard template workflows.