---
title: Federated SSO with PingID and PingFederate
description: If you're using PingFederate for single sign-on (SSO) within your organization, you can add PingID as your secondary or primary authentication solution by installing the PingID Integration Kit and adding the PingID adapter to your PingFederate configuration.
component: pingid
page_id: pingid:introduction_to_pingid:pid_federated_sso_with_pid_and_pf
canonical_url: http://docs.pingidentity.com/pingid/introduction_to_pingid/pid_federated_sso_with_pid_and_pf.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 28, 2024
---

# Federated SSO with PingID and PingFederate

If you're using PingFederate for single sign-on (SSO) within your organization, you can add PingID as your secondary or primary authentication solution by installing the PingID Integration Kit and adding the PingID adapter to your PingFederate configuration.

The following diagram shows your enterprise users' standard SSO process using the PingID adapter.

![Diagram of enterprise SSO initiated at the service provider with PingID as the secondary authentication source](_images/oxh1564020848922.png)

For more information on installing and configuring PingID, see [Integrate with PingID for PingFederate SSO](../pingid_integrations/pid_integrate_pf_sso.html).

---

---
title: Introduction to PingID
description: PingID is a cloud-based authentication service that binds user identities to mobile devices.
component: pingid
page_id: pingid:introduction_to_pingid:pid_introduction
canonical_url: http://docs.pingidentity.com/pingid/introduction_to_pingid/pid_introduction.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 9, 2022
---

# Introduction to PingID

PingID is a cloud-based authentication service that binds user identities to mobile devices.

During the PingID authentication process, the PingID service sends an authentication request to the user's mobile device. No password response is required: the user just swipes to authenticate.

You can use PingID for any of these solutions:

* PingOne SSO

  Use PingID as a secondary authentication solution for PingOne single sign-on (SSO) in the cloud. A PingOne administrator can enable PingID in minutes.

* PingFederate SSO

  Use PingID as either a secondary or primary authentication solution for federated SSO through PingFederate. A PingFederate administrator can install and configure a PingID adapter that negotiates with the PingID service.

* VPNs

  Use PingFederate and PingID for multi-factor authentication (MFA) from your VPN. This solution uses PingFederate with a password credential validator (PCV) for PingID for identity access management, and PingOne for user management. You need only a few additional settings to enable PingID authentication for your VPN.

* Passwordless authentication

  * Use PingID with biometrics or a security key to provide passwordless authentication for Web authentication through PingFederate.

  * Use PingID mobile application to provide passwordless authentication for Windows login.

You can configure your SSO infrastructure for PingID authentication to:

* Use primary authentication only for SSO to PingOne, and then use PingID as secondary authentication whenever a user attempts to access certain applications.

* Use PingID when a user is outside of your organization's intranet.

* Use PingID only for customers that use SSO to connect to your Managed Service Provider (MSP) account on PingOne.

* Use the PingID API and PingID client integration settings to integrate PingID with your VPN or remote access system and authenticate remote SSO.

PingID is a service that runs on the PingOne platform, a mobile app for Apple® iOS or Google Android™ devices, and an adapter and PCV for PingFederate. These components work together to provide a secure means of authentication for members of your organization, partners, or customers.

If you have a PingOne SSO account, PingID is ready for you to use. To use the PingID service solely for PingFederate federated SSO, SSO through your VPN, or for custom client integrations, you need to register for the PingID Enterprise service with PingOne. You configure and manage the PingID service using the PingOne admin portal.

Try PingID for free and see the value it can bring to your organization. For more information, see [Starting a PingOne trial](http://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_start_a_p1_trial.html).

|   |                                                                                                                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Consider the security guidelines outlined in the PingID Hardening Guide ​when configuring your implementation of PingID. For more information, see [PingID Security Hardening Guide](https://support.pingidentity.com/s/article/PingID-Security-Hardening-Guide). |

![An image of the PingID desktop sign-on workflow.](_images/cjc1564020839312.png)

Your PingID setup depends on your SSO infrastructure. For more information, see:

* [SSO with PingID and PingOne](pid_sso_with_p1.html)

* [Federated SSO with PingID and PingFederate](pid_federated_sso_with_pid_and_pf.html)

* [PingID authentication for PingOne using PingFederate as the identity bridge](pid_authentication_for_p1_using_pf.html)

* [PingID authentication for VPNs](pid_authentication_for_vpns.html)

---

---
title: Overview of PingID authentication types
description: After defining user groups and end-user accounts in your organization, determine which authentication method they'll use.
component: pingid
page_id: pingid:introduction_to_pingid:pid_overview_of_authentication_types
canonical_url: http://docs.pingidentity.com/pingid/introduction_to_pingid/pid_overview_of_authentication_types.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 18, 2026
section_ids:
  AuthType_PID_MobileApp: PingID Mobile App
  AuthType_FIDO2Biometrics: FIDO2 biometrics
  AuthType_Securitykey: Security key
  AuthType_DesktopSoftToken: Desktop Soft Token
  AuthType_AuthApp: Authentication app
  AuthType_OATHToken: OATH token
  AuthType_YubiKey: YubiKey - Yubico OTP
  AuthType_EmailOTP: Email OTP
  AuthType_SMSvoice: SMS and Voice
---

# Overview of PingID authentication types

After defining user groups and end-user accounts in your organization, determine which authentication method they'll use.

PingID supports several types of authentication for users:

* [PingID Mobile App](#AuthType_PID_MobileApp). This includes the fingerprint biometrics, facial recognition, swipe, mobile soft token, and Apple Watch authentication methods.

* [FIDO2 biometrics](#AuthType_FIDO2Biometrics)

* [Security key](#AuthType_Securitykey)

* [Desktop Soft Token](#AuthType_DesktopSoftToken)

* [Authentication app](#AuthType_AuthApp)

* [OATH token](#AuthType_OATHToken)

* [YubiKey - Yubico OTP](#AuthType_YubiKey)

* [Email OTP](#AuthType_EmailOTP)

* [SMS and Voice](#AuthType_SMSvoice)

As an administrator, you determine which authentication methods the users in your organization use. For example, you can use a lenient method such as SMS and move to stricter methods at a later stage, such as biometrics authentication.

|   |                                                                                                                                                                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Using a username and multi-factor authentication (MFA) method as your primary authentication method can expose users to security risks like username enumeration, MFA fatigue attacks, targeted phishing, and denial-of-service incidents. To reduce exposure, use a passwordless method such as FIDO2 biometrics for primary authentication. |

## PingID Mobile App

**Biometrics: Fingerprint**

The fingerprint authentication uses a device's native capability to scan and authenticate the user's fingerprint.

The PingID mobile app supports fingerprint authentication on devices with biometric support. Learn more in [Supported operating systems](http://docs.pingidentity.com/pingid-user-guide/managing_your_devices/pid_supported_operating_systems.html).

You can set the fingerprint authentication rollout mode with the following settings:

* Disable fingerprint authentication.

* Enable for iOS, Android, or both, in one of the following modes:

  * **Enable**: If the user has a supporting device and enables the fingerprint scan option, they can authenticate by fingerprint.

  * **Require**: Users with supporting devices must set up and authenticate with their fingerprint scan option.

  * **Enforce**: Every authentication requires fingerprint scanning by the PingID app, even if the user unlocked the device using their fingerprint.

![An image showing the PingID authentication prompt for Touch ID on an iPhone.](_images/cxz1564020891858.png)

Learn more in [Configuring biometrics authentication for the PingID mobile app](../pingid_service_management/pid_configuring_biometrics_auth_pidma.html).

**Biometrics: Facial Recognition**

PingID supports facial recognition. Authentication by facial recognition is model dependent for Apple and Android devices.

Both facial recognition and fingerprint authentication results pass through to the PingID app transparently. Find configuration information in [Configuring biometrics authentication for the PingID mobile app](../pingid_service_management/pid_configuring_biometrics_auth_pidma.html).

* **Apple**: Apple uses Face ID for some iPhone and iPad devices. These devices are configured for Face ID or Touch ID, but not both. Devices that support Face ID include:

  * iPhone: iPhone XS Max, iPhone XS, iPhone XR, iPhone X

  * iPad: iPad Pro 12.9" (third generation), iPad Pro 11"

  You can find the most recent information from Apple in [iPhone and iPad models that support Face ID](https://support.apple.com/en-il/HT209183).

* **Android Platforms**: The device camera acquires facial data. If the user tries to authenticate with an unlocked screen, only fingerprint authentication is available. On a locked screen, fingerprint authentication and facial recognition are both available on supported devices.

**Approve a notification or Approve from Lock Screen**

A push notification is sent to the user's device to let them know they need to authenticate. If PingID mobile app is open, they can tap **Yes** to authenticate. If their phone is locked, or if PingID mobile app is locked, the user might be able to authenticate from the lock screen. Long-tap the notification or swipe down and tap **Yes**.

![An image of the PingID Approve Yes button on an iPhone. it also shows the option to select No it's not me for fraudulent requests.](_images/etj1707744677574.png)![An image of a PingID push notification on an iPhone. The user has the option to approve or deny the request.](_images/lca1708866869142.png)

**Mobile Soft Token**

A user can generate a one-time passcode (OTP) with the PingID app for iOS or Android. This OTP can be used for authentication in cases when the user's mobile is offline, such as when there is no network connection, or in any other use case set by the administrator as an organization's policy.

![An image of an OTP on the PingID app for iPhone.](_images/lmw1564020894142.png)

**Apple Watch**

If a user has an Apple Watch connected to their iPhone, the PingID app automatically presents the **Approve** or **Deny** authentication actions on the Apple Watch, so the user can authenticate without needing to access their device.

![An image of the PingID app on an Apple Watch.](_images/thi1564020897774.png)

## FIDO2 biometrics

The user can use FIDO2 strong cryptographic authentication, using built-in FIDO2 platform biometrics on their device.

Biometrics are supported for the following devices:

* Windows Hello

* Apple Mac (Touch ID)

* iOS biometrics

* Android biometrics

Learn more in [(Legacy) Configuring FIDO2 biometrics for PingID](../pingid_service_management/pid_configuring_fido2_biometrics_for_pid.html).

## Security key

The user can authenticate with any FIDO2 compliant security key or wearable device. The security key offers a strong cryptographic authentication option for end-user security. Learn more in [(Legacy) Configuring the FIDO2 security key for PingID](../pingid_service_management/configuring_fido2_security_key.html).

![An image of a Yubico security key.](_images/pxn1564020898436.png)

## Desktop Soft Token

If the organization has approved the use of the PingID desktop app, users can generate an OTP from the local installation of the desktop app on their Windows or Mac computer. Learn more in [Configuring PingID desktop app authentication](../pingid_service_management/pid_desktop_app_authentication.html).

![An image of an OTP on the PingID desktop app.](_images/jvr1564020899152.png)

## Authentication app

If the organization has approved the use of external Time-based One-time Password (TOTP) authenticator apps, such as Google authenticator, a user can generate an OTP from the authenticator app on their device. Learn more in [Configuring authenticator app authentication for PingID](../pingid_service_management/pid_configuring_authenticator_app_authentication_for_pid.html).

## OATH token

An Open Authentication (OATH) token is a secure OTP used for two-factor authentication and is OATH compliant. Learn more in the [OATH (Initiative for Open Authentication)](https://openauthentication.org/) documentation.

Use hardware OATH tokens where there are no provisions for connection to the Internet, USB connections, or mobile phones. Such connections might be disallowed for security reasons. Learn more in [Configuring OATH token authentication for PingID](../pingid_service_management/cxe1564020450447.html).

![An image of a hand-held OTP generator.](_images/pni1564020899825.png)

## YubiKey - Yubico OTP

The user must click a YubiKey that supports Yubico OTP capabilities to authenticate. Select this method of authentication if you've distributed YubiKey hardware tokens to users who aren't authenticating using a mobile device.

YubiKeys that are FIDO2 compliant can be used as either a YubiKey or a Security key. Learn more in [Configuring YubiKey authentication (Yubico OTP) for PingID](../pingid_service_management/pid_configuring_yubikey_authentication_yubico_otp.html).

![An image of a YubiKey.](_images/ymm1564020900701.png)

## Email OTP

If you have users who aren't using devices that support the PingID mobile application, you can choose to enable this method of authentication. The user is authenticated by providing a 6-digit OTP sent by email to their email address. Learn more in [Configuring email authentication for PingID](../pingid_service_management/pid_configuring_email_authentication_for_pid.html).

![An image of an OTP being entered during sign-on.](_images/rdo1564020902183.jpg)

## SMS and Voice

If you have users who aren't using devices that support the PingID mobile application, you can enable this method of authentication. The user is authenticated by providing a 6-digit OTP sent to the user's mobile device or landline phone, using SMS or voice channels.

![An image of an SMS containing a PingID authentication code.](../_images/wrd1564020565457.png)

Learn more about SMS and voice, including about usage limits, in [SMS and voice authentication](../pingid_service_management/pid_sms_voice_authentication.html).

---

---
title: PingID authentication for PingOne using PingFederate as the identity bridge
description: When you're using PingFederate as your PingOne identity bridge, you can use PingID for authentication on either the PingOne side or the PingFederate side.
component: pingid
page_id: pingid:introduction_to_pingid:pid_authentication_for_p1_using_pf
canonical_url: http://docs.pingidentity.com/pingid/introduction_to_pingid/pid_authentication_for_p1_using_pf.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 23, 2024
---

# PingID authentication for PingOne using PingFederate as the identity bridge

When you're using PingFederate as your PingOne identity bridge, you can use PingID for authentication on either the PingOne side or the PingFederate side.

Using PingID on the PingFederate side is useful when:

* You want to apply advanced PingFederate policy settings (for example, a custom adapter selector) to your PingID authentication.

* You want to use PingID for primary authentication.

For more information on configuring PingID for PingFederate, see [Integrate with PingID for PingFederate SSO](../pingid_integrations/pid_integrate_pf_sso.html).

For more information on configuring PingID for PingOne, see [Integrate with PingID for PingOne SSO](../pingid_integrations/pid_integrate_p1_sso.html).

---

---
title: PingID authentication for VPNs
description: You can use PingFederate and PingID for multi-factor authentication (MFA) from your VPN.
component: pingid
page_id: pingid:introduction_to_pingid:pid_authentication_for_vpns
canonical_url: http://docs.pingidentity.com/pingid/introduction_to_pingid/pid_authentication_for_vpns.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 29, 2024
---

# PingID authentication for VPNs

You can use PingFederate and PingID for multi-factor authentication (MFA) from your VPN.

Configure your VPN for PingID and use PingFederate for identity access management for your users. You'll use PingOne for user management. For more information and instructions, see [Integration for devices using a RADIUS server](../pingid_integrations/pid_integration_devices_radius_server.html).

PingID supports the following VPNs:

* Cisco® Adaptive Security Appliance (ASA)

* Checkpoint® VPN

* Juniper® SA Series SSL VPN Appliances

* Palo Alto GlobalProtect®

You can integrate your VPN for PingID using RADIUS or SAML, these are standard protocols and any VPN that supports them, can be integrated. For more information, see [Integration for devices using a RADIUS server](../pingid_integrations/pid_integration_devices_radius_server.html).

---

---
title: PingID regional data centers
description: When you create your organization in PingOne, choose the PingID regional data center location for your organization.
component: pingid
page_id: pingid:introduction_to_pingid:pid_regional_data_centers
canonical_url: http://docs.pingidentity.com/pingid/introduction_to_pingid/pid_regional_data_centers.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 29, 2024
section_ids:
  limitations: Limitations
---

# PingID regional data centers

When you create your organization in PingOne, choose the PingID regional data center location for your organization.

The PingID service is currently installed at the following regional data centers:

* North America (East and West Coasts)

* Europe

* Australia

All PingID service installations are hosted in the Amazon cloud.

Although each data center can service PingID users from any location, the location of your data center is important. It provides additional benefits, including:

* Better compliance with European, Australian, and New Zealand regulations and companies' standards.

* Users' personally identifiable information (PII) is stored in the specified regional hosting facility only.

* Optimized network speed for regional users.

For more information on registering a PingOne account and defining the data center location for your organization, see [Creating an organization](http://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_mfa_creating_an_organization.html).

## Limitations

* After you create and register your organization in PingOne, it is not possible to migrate from one data center to another.

* A user must have the PingID mobile app v1.9 or later installed to pair the PingID mobile app to two or more organizations that are not using the same data center.

---

---
title: SSO with PingID and PingOne
description: If you're using PingOne for single sign-on (SSO), adding PingID as your secondary authentication solution is a simple process of creating an authentication policy and assigning PingID as the authenticating entity.
component: pingid
page_id: pingid:introduction_to_pingid:pid_sso_with_p1
canonical_url: http://docs.pingidentity.com/pingid/introduction_to_pingid/pid_sso_with_p1.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 4, 2023
section_ids:
  federated-sso: Federated SSO
  basic-sso: Basic SSO
---

# SSO with PingID and PingOne

If you're using PingOne for single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)*, adding PingID as your secondary authentication solution is a simple process of creating an authentication policy and assigning PingID as the authenticating entity.

For more information about creating an authentication policy, see [Creating or updating an authentication policy](../pingid_integrations/pid_creating_updating_authentication_policy.html).

For more information about configuring PingID, see [Integrate with PingID for PingOne SSO](../pingid_integrations/pid_integrate_p1_sso.html).

## Federated SSO

For federated SSO, the following diagram shows your users' standard SSO process with PingID.

![Diagram of federated SSO with PingID MFA showing the services and steps used for authentication.](_images/muc1564020845156.png)

For more information, see [Federated SSO with PingOne](http://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_federated_sso.html).

## Basic SSO

For basic SSO, the following diagram shows your users' standard sign-on process with PingID as a second authentication solution.

![Diagram of basic SSO with PingID MFA showing the services and steps used for authentication.](_images/sht1564020846187.png)

For more information, see [Basic SSO (password vaulting)](http://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_basic_sso.html).