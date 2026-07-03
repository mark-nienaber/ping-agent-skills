---
title: Get help using PingID for authentication and verification
description: "PingID FAQ for end users. Covers pairing PingID mobile app, finding a QR code, a lost or stolen device, and when to contact their company's help desk."
component: pingid-user-guide
page_id: pingid-user-guide::index
canonical_url: https://docs.pingidentity.com/pingid-user-guide/index.html
llms_txt: https://docs.pingidentity.com/pingid-user-guide/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 28, 2026
section_ids:
  common-questions: Common questions
  pingid-mobile-app-faqs: PingID mobile app FAQs
  backup-and-other-sign-on-methods: Backup and other sign-on methods
  troubleshooting: Troubleshooting
  im-still-having-problems-using-pingid-where-can-i-get-help: I'm still having problems using PingID. Where can I get help?
---

# Get help using PingID for authentication and verification

Need help with your account? Contact your organization's IT help desk.

Every organization implements PingID differently. If you have further questions or need more specific help, you must contact your organization directly. Ping Identity provides the PingID software, but we can't access or reset your account, unpair your device, or provide a QR code.

PingID enables you to securely sign on to your work account using multi-factor authentication (MFA), verify your identity, and share your credentials. MFA is also known as two-factor authentication (2FA) or two-step verification.

The PingID mobile app is the most common way to sign on to work accounts, but your organization might also set you up with a passkey, PingID desktop app, email, or another method. You can also use PingID mobile app as an authenticator app for your third-party accounts, such as Google, Facebook, or PayPal.

## Common questions

* [Lost or stolen device](ma_lost_or_stolen_mobile.html)

  What to do if your mobile with PingID mobile app is lost or stolen

* [Find a QR code or pairing key](ma_where_find_qr_code.html)

  Where to find a QR code or pairing key for PingID mobile app

## PingID mobile app FAQs

> **Collapse: What is PingID mobile app and how do I use it?**
>
> Your organization wants you to use PingID mobile app to help keep your work account and applications safe.
>
> To start, you'll need to pair your phone or other mobile device with PingID. This connects your device so you can use it for sign-on.
>
> When you sign on, you'll get a notification on your device. Open the PingID mobile app and tap **Approve**, or use your fingerprint or face if asked. Sometimes, your organization might require you to enter a one-time passcode (OTP) from the app. You might also be able to use the PingID mobile app to sign on to other apps that support OTPs.
>
> |   |                                                                                                                                                                                             |
> | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | Different organizations set up PingID in different ways. Ping Identity can't help with your account. If you're not sure what to do or you get stuck, contact your organization's help desk. |

> **Collapse: How do I register PingID mobile app for the first time?**
>
> 1. Download [PingID mobile app for iOS](https://apps.apple.com/us/app/pingid/id891247102) or [PingID mobile app for Android](https://play.google.com/store/apps/details?id=prod.com.pingidentity.pingid\&hl=iw\&gl=US).
>
> 2. Scan the [QR code](ma_where_find_qr_code.html) or enter the pairing key that you received from your organization.
>
> 3. Follow the instructions and accept all permissions when asked to do so.
>
> 4. If your organization requires it, you'll need to set up biometrics (such as fingerprint or face recognition) on your mobile device.
>
> |   |                                                                                                              |
> | - | ------------------------------------------------------------------------------------------------------------ |
> |   | If you need further help, including finding a QR code or pairing key, contact your organization's help desk. |

> **Collapse: Where can I download the PingID mobile app?**
>
> You can download PingID mobile app for iOS or for Android from the relevant app store, or using the relevant link:
>
> * [PingID mobile app for iOS](https://apps.apple.com/us/app/pingid/id891247102).
>
> * [PingID mobile app for Android](https://play.google.com/store/apps/details?id=prod.com.pingidentity.pingid\&hl=iw\&gl=US).

> **Collapse: How to move PingID mobile app to a new phone (I have the old phone)**
>
> If you still have your old phone, you can move your account without registering again using **Change Device**.
>
> 1. On your new phone, install the PingID mobile app.
>
> 2. On your old phone, open PingID mobile app and tap **Settings > Change Device**.
>
> 3. Use your new phone to scan the QR code shown on your old phone.
>
>    ![An animation showing the process of changing the device pairing an old mobile device with a new mobile device through the PingID mobile app](_images/mobile-pairing-animation.gif)
>
>    |   |                                                                                                                                                                                                                                        |
>    | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>    |   | Ping Identity has no access to your account and therefore can't help you change your device. If you don't see the **Change Device** option, your organization might have disabled it. Please contact your IT help desk for assistance. |

> **Collapse: How to move PingID mobile app to a new device (I don't have my old phone or mobile device)**
>
> If you no longer have your old phone or mobile device, or it's broken, you must unpair it before you can register a new device.
>
> 1. **Unpair the old phone**
>
>    * **If you have a backup method**: Sign on to your account using your backup device (like a security key or the desktop app) and unpair your old phone from your **My Account** page.
>
>    * **If you don't have a backup method**: You **must** contact your company's IT help desk. They are the only ones who can unpair the device for you.
>
>      |   |                                                                                                                                                                                                                       |
>      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>      |   | **Ping Identity can't unpair your device.** For security reasons, only your organization's IT team can manage your account or reset your devices. Ping Identity doesn't have access to your personal account details. |
>
> 2. Download PingID mobile app and register it on your new phone.

> **Collapse: My phone or mobile device with PingID mobile app is lost or stolen**
>
> 1. If an old device with PingID is lost, broken, stolen, or you just no longer have it, **and** you don't have a backup device, you must unpair PingID before you can pair (register) it on a new device.
>
>    * **If you have a backup method**: Sign on to your account using your backup device (like a security key or the desktop app) and remove PingID mobile app from the list of authentication methods on your **My Account** page.
>
>    * **If you don't have a backup method**: You **must** contact your company's IT help desk. They are the only ones who can unpair the device for you.

> **Collapse: Why does PingID need my location**
>
> Some organizations configure their account so that you must enable location permissions to use PingID. PingID only uses your location to verify your identity and to prevent fraudulent sign-on attempts from unexpected locations.

## Backup and other sign-on methods

> **Collapse: Can I add a backup way to sign on if I forget my mobile?**
>
> Yes, and as long as your organization allows it, it's advisable to do so.
>
> A backup method enables you to sign on if your phone is lost, replaced, out of battery, or not with you.
>
> Your organization decides which options are available. You might be able to use:
>
> * PingID desktop app
>
> * Passkey (for example, Windows Hello, Touch ID, or a security key)
>
> * Authenticator app
>
> * YubiKey
>
> * Hardware token
>
> |   |                                                                                                                                        |
> | - | -------------------------------------------------------------------------------------------------------------------------------------- |
> |   | Ask your organization's IT help desk how to add a backup sign-on method. They might give you a link or portal where you can set it up. |
>
> If you lose or replace your phone, a backup method can help you sign on and remove your old device without contacting support.

> **Collapse: I need help with PingID sign-on methods**
>
> If you need help with any of these sign-on methods, contact your organization's help desk. Your organization manages how these methods are configured, so only they can assist you.
>
> * PingID desktop app
>
> * Passkey (such as Windows Hello, Apple Mac Touch ID, device biometrics, or a FIDO2 security key)
>
> * Authenticator app
>
> * YubiKey
>
> * Hardware token
>
> * SMS, Voice, or Email

## Troubleshooting

> **Collapse: Why can't I pair PingID mobile app on my new device?**
>
> * If PingID mobile app is paired to another mobile device, you won't be able to pair it on your new device until you unpair it from your old device.
>
> * If your old device is unavailable, you'll need to contact the organization to which PingID is paired and ask them to unpair it for you.
>
> * Your organization might have a policy that's blocking you from pairing your mobile device with PingID mobile app.
>
>   |   |                                                                                                                                               |
>   | - | --------------------------------------------------------------------------------------------------------------------------------------------- |
>   |   | Ping Identity has no access to your account and therefore can't help. If you're still having problems, contact your organization's help desk. |

> **Collapse: I can't scan the QR code when trying to pair an account**
>
> * In your phone or mobile device settings, make sure that PingID mobile app has access to your camera permissions.
>
> * Each QR code usually has a pairing key that you can use in place of the QR code.
>
>   To enter the pairing code, on the PingID mobile app **Authentication tab**, tap **+**, tap **Enter Pairing Key** and then enter the pairing key.
>
> |   |                                                                                                                                               |
> | - | --------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | Ping Identity has no access to your account and therefore can't help. If you're still having problems, contact your organization's help desk. |

> **Collapse: I received an approval request I didn't initiate**
>
> **Deny the request immediately.** If you get a PingID approval request that you didn't trigger, someone else might be trying to access your account.
>
> 1. Tap **Deny** on the request.
>
> 2. Contact your organization's IT help desk right away and let them know what happened.
>
> |   |                                                                                                                                     |
> | - | ----------------------------------------------------------------------------------------------------------------------------------- |
> |   | Never approve a request unless you are the one signing on. If you're unsure, always deny and contact your organization's help desk. |

> **Collapse: My account is locked or suspended**
>
> Account access and any locks or suspensions are controlled entirely by your organization. You must contact your organization's IT help desk to unlock your account. Ping Identity has no access to your account and cannot unlock it on your behalf.

> **Collapse: I'm not receiving a notification to my phone when I try to sign on**
>
> * Check that your phone has an internet connection (Wi-Fi or mobile data).
>
> * In your phone or mobile device settings, check that notifications are enabled for PingID mobile app.
>
> * If the notification still doesn't arrive, open the PingID mobile app manually and look for a pending authentication request.
>
> * If none of these steps work, contact your organization's IT help desk.
>
> |   |                                                                                                                          |
> | - | ------------------------------------------------------------------------------------------------------------------------ |
> |   | Ping Identity has no access to your account and therefore only your organization's IT team can troubleshoot your access. |

> **Collapse: The one-time passcode in my app isn't working**
>
> * Make sure you're entering the code before it expires. One-time passcodes (OTPs) refresh every 30 seconds.
>
> * Check that your phone's date and time are set to automatic (not manually set). An incorrect clock can cause OTPs to fail.
>
> * If the OTP keeps failing after trying the above, contact your organization's IT help desk.
>
> |   |                                                                                                                          |
> | - | ------------------------------------------------------------------------------------------------------------------------ |
> |   | Ping Identity has no access to your account and therefore only your organization's IT team can troubleshoot your access. |

> **Collapse: Why are some of my third-party accounts missing in PingID mobile app?**
>
> If you move PingID mobile app to a new phone, your third-party accounts (like Google or Facebook) won't automatically show in the PingID mobile app on your new phone. Only accounts from the organization (indicated by an office icon ![Image showing an office icon](_images/icon-organization.png)) move automatically.
>
> You have to remove each account from your old phone or mobile device and then add it to your new device, one by one.
>
> If you don't have your old phone or mobile device, you'll need to use the relevant recovery codes or contact the third-party organization (like Google or Facebook) if you need help adding the account to your new device.
>
> |   |                                                                                                                                                                    |
> | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
> |   | Ping Identity doesn't have access to your third-party accounts and therefore can't help you. If you get stuck, reach out to the relevant third-party organization. |

## I'm still having problems using PingID. Where can I get help?

**Ping Identity doesn't have access to your account and therefore can't help you.** For security reasons, only your organization's IT help desk can reset your account, unpair a lost device, or help you if you're stuck.

Ping Identity makes the software, but every organization implements it differently, so you must contact your organization if you need further help.

If your account is a third-party account (such as Google or Facebook), use the recovery codes they supplied to you, or contact the third-party organization directly.

You can also find more general help and information about the PingID mobile app in the in-app help.
