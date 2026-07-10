---
title: (Customer Only) Configuring WhatsApp authentication
description: How to enable and configure WhatsApp authentication in PingOne to let users receive a one-time passcode via WhatsApp.
component: pingone
page_id: pingone:strong_authentication_mfa:p1-strong-auth_whatsapp
canonical_url: https://docs.pingidentity.com/pingone/strong_authentication_mfa/p1-strong-auth_whatsapp.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
---

# (Customer Only) Configuring WhatsApp authentication

Enable and configure WhatsApp authentication to allow your users to receive a one-time passcode (OTP) by WhatsApp.

![WhatsApp message showing a one-time passcode. The message includes a security message, and the copy code button.](_images/whatsapp-message-example.png)

## Before you begin

To enable WhatsApp authentication, make sure you have a WhatsApp Business account that includes one or more WhatsApp messaging templates. You can find more details in [Configuring a custom WhatsApp sender account](../settings/p1-using-a-custom-whatsapp-sender-account.html).

## About this task

To configure WhatsApp authentication:

1. Add your WhatsApp Business account as a Sender in PingOne. Learn more in [Configuring a custom WhatsApp sender account](../settings/p1-using-a-custom-whatsapp-sender-account.html).

2. For each language you want to support, link a WhatsApp messaging template to the relevant PingOne Notification templates. Learn more in [Notification Templates](../user_experience/p1_edit_notification.html).

3. In the PingOne **MFA policy** enable WhatsApp as an authentication method. Learn more in [Configuring an MFA policy for strong authentication](p1_creating_an_mfa_policy_for_strong_auth.html).

4. (Optional) Configure a notification policy to limit the number of WhatsApp messages that can be sent per day or to limit their target locations. Learn more in [Notification Polices](../user_experience/p1_creating_a_notification_policy.html).

---

---
title: (Workforce only) Configuring the PingID desktop application
description: Learn how to configure the PingID desktop app to provide passwordless authentication using device biometrics on Mac and Windows machines.
component: pingone
page_id: pingone:strong_authentication_mfa:p1_pid_desktop_app_start
canonical_url: https://docs.pingidentity.com/pingone/strong_authentication_mfa/p1_pid_desktop_app_start.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 28, 2025
section_ids:
  whats-involved: What's involved?
  1-before-you-begin: 1. Before you begin
  2-configure-pingone: 2. Configure PingOne
  3-configure-additional-components: 3. Configure additional components:
  4-install-the-pingid-desktop-app: 4. Install the PingID desktop app
  troubleshooting: Troubleshooting
---

# (Workforce only) Configuring the PingID desktop application

|   |                                                                                                                                                                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This section documents the new PingID desktop application.- To understand the difference between the **PingID desktop app** and the **PingID desktop app (legacy)**, go to [PingID desktop app (workforce only)](p1_pid_desktop_app_version_overview.html).

- For the legacy PingID desktop application, go to [PingID desktop app (legacy)](p1_pid_desktop_app_v1.html). |

PingID desktop app provides users with a consistent passwordless authentication experience across different browsers from a Mac or Windows machine using the machine's device biometrics.

## What's involved?

Configuring PingID desktop app as an authentication method involves several steps.

### 1. Before you begin

* [Review the requirements and limitations for PingID desktop app](p1_pid_desktop_app_prereq.html).

### 2. Configure PingOne

In the relevant PingOne environment:

1. [Enable and configure PingID desktop app as an authentication method](p1_pid_desktop_app_enable_and_configure.html).

2. Configure a targeted PingOne risk policy, and select the MFA policy you want to apply to authentication and registration flows.

   * If you have a PingOne Protect license, go to [Configuring a targeted PingOne risk policy](../threat_protection_using_pingone_protect/p1_protect_adding_risk_policy.html).

   * If you have an MFA-only license, go to [Creating a risk policy with an MFA-only license](../threat_protection_using_pingone_protect/p1_creating_risk_policies_for_mfa_only.html).

### 3. Configure additional components:

* When using DaVinci:

  [Configure the DaVinci authentication subflow to use PingOne risk policy](p1_desktop_app_davinci_flow_configuration.html)

* When using PingFederate:

  [Configure a PingFederate policy for a consistent passwordless experience](https://docs.pingidentity.com/pingid/pingid_integrations/pid_configuring_pf_policy_for_passwordless_authentication.html)

* (Optional) Browser configurations:

  To ensure a seamless passwordless sign-in experience for users authenticating from common browsers, do the following:

  * [Suppress the Local Network Access Prompt](p1_pid_desktop_app_v2_windows_manage_lna_prompt.html).

  * [(macOS only): Configure PingID desktop app for Safari on macOS](p1_pid_desktop_app_v2_mac_sso_extension_integration.html)

### 4. Install the PingID desktop app

* [Install the PingID desktop app using the CLI or UI](p1_pid_desktop_app_v2_installation.html).

## Troubleshooting

Find troubleshooting information in [Troubleshooting PingID desktop app](p1_pid_troubleshooting_desktop_app.html).

---

---
title: (Workforce Only) Configuring the PingID mobile application settings
description: How to configure PingID mobile app for Workforce MFA, including biometrics, number matching, device requirements, and MDM integration.
component: pingone
page_id: pingone:strong_authentication_mfa:p1_configuring_pid_mobile_application
canonical_url: https://docs.pingidentity.com/pingone/strong_authentication_mfa/p1_configuring_pid_mobile_application.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 29, 2024
page_aliases: ["p1_mfa_configuring_authentication.adoc"]
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
---

# (Workforce Only) Configuring the PingID mobile application settings

In a Workforce environment, users can download PingID mobile app to their mobile device and use it to sign on to your company services and applications with the added security of multi-factor authentication (MFA). They can also use it to verify their identity to an employer and share verified credentials.

## Before you begin

To add PingID mobile app as an authentication method, you need:

* A PingOne environment with a Workforce license. Learn more in [Setting up an environment for strong authentication (MFA)](p1_create_environment_strong_authentication_start.html)

## About this task

Configuring PingID mobile app as an authentication method for MFA includes the following steps:

1. Configure the MFA policy, including the PingID mobile app-specific configurations. Learn more in [Configuring an MFA policy for strong authentication](p1_creating_an_mfa_policy_for_strong_auth.html).

2. Configure the PingID mobile application in the **Applications** section of PingOne, as described in this procedure.

## Steps

1. Go to **Applications > Applications**.

2. In the **Applications** list, select **PingID Mobile**.

3. On the **Configuration** tab, click the **Pencil** icon and edit the relevant fields described in the steps that follow this one.

4. In the **Mobile App authentication** area, under **Mobile Biometrics**, select the authentication behavior based on whether the user has biometrics (Fingerprint or Face). Select either:

   ### Choose from:

   * **Preferred**: If mobile biometrics are defined on the user's device, the user must use them to authenticate.

   * **Required**: Users must configure mobile biometrics on a supported device and can only use biometrics to authenticate.

   * (Optional) Select **Enable FaceID Consent on iOS:** to prevent users with FaceID defined from authenticating by mistake. When selected, the user is prompted to consent explicitly before each face scan is taken.

   * Select **Enable Notification Actions** to allow users to approve a notification request from the lock screen.

   * Select **Enable Device Passcode Fallback on iOS** to allow users to authenticate using the device passcode if biometrics authentication fails.

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                        |
     | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | * **Mobile Biometrics** configurations require **Biometrics** to be selected in the MFA policy. Learn more in [MFA policy](p1_creating_an_mfa_policy_for_strong_auth.html)

     * For PingID mobile app 1.x users only, optionally select **Enable FaceID Consent on iOS:** to prevent users with FaceID defined from authenticating by mistake. When selected, the user is prompted to consent explicitly before each face scan is taken. |

5. In the **Mobile App authentication** area, use **Passcode Grace Period** to cover time synchronization issues by defining a grace period of between 1 and 10 windows during which the passcode can still be used even after the passcode has been refreshed. In this context, a window is equal to the passcode refresh period (30 seconds) in either direction. For example, if you defined a grace period of 2 windows, the passcode is valid for 150 seconds (from 60 seconds behind the time of issue until 60 seconds past the expiration time).

6. In the **Mobile App authentication** area, under **Number Matching Options**, select either:

   * **Select Number**: Display three numbers in PingID mobile app and prompt the user to tap the correct number.

   * **Enter Manually**: Display a text field in PingID mobile app and prompt the user to manually enter the correct number.

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                              |
     | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | * To enable this feature, **Number Matching** must be enabled in the MFA Policy. Learn more in [Configuring an MFA policy for strong authentication](p1_creating_an_mfa_policy_for_strong_auth.html).

     * This feature is supported by PingID mobile app 2.4 or later. Users running an earlier version are prompted to select a number, rather than entering the text manually.

     * Manual number matching is not supported by smart watches. |

7. (Optional) In the **Mobile App authentication** area, enable the following options:

   * **Enable OTP Push Notification**: Send a push notification to users when they can only authenticate with an OTP. When they tap the notification, PingID mobile app opens automatically, displaying the current OTP.

   * **Display Authentication Information map**: Include a map with supporting information about the origin of the authentication request they receive with the push notification.

8. (Optional) In the **Mobile Management** area, enable the following options:

   * **Allow users to unpair or change device from the PingID mobile app**

   * **Allow authentication from lock screen for legacy Android devices** (Android Q or earlier)

   * **Require mobile app security PIN**: When selected, the user must enter a security PIN to access PingID mobile app. If selected, you must also define the security PIN-requirements, defining whether the security PIN must be 4 or 6 digits in length, and whether PingID mobile app PIN is always required or only when a device PIN or biometrics are not defined on the user's device. Learn more about PingID mobile app PIN requirements in [PingID mobile app PIN requirements](p1_pid_mobile_app_pin_requirements.html)

9. In the **Mobile Notifications** section, you can choose to notify users when new PingID mobile app versions become available.

   Choose whether to make updates optional or mandatory and define from which version they appear.

   ### Choose from:

   * **Notify users of required mobile version updates**: Notify the user when a new version is available. The user must update to the new version to continue using PingID mobile app and cannot skip the update. If selected, for each OS, specify the minimum version from which update notifications should be sent. The default is **Latest**.

   * **Notify users of optional version mobile updates**: Notify the user when a new version is available. The notification includes the option to skip the update and install it at a later date. If selected, for each OS, specify the minimum version from which update notifications should be sent. The default is **Latest**.

10. (Optional) To restrict the brand and model of mobile devices that can be used with PingID mobile app:

    1. In the **Mobile requirements** section, select **Select allowed and disallowed devices**.

    2. In the relevant **Brands** field, add one or more brands, and in the corresponding **Models** field, specify one or more models. If no model is selected, all models for that brand are selected.

       |   |                                                                                                                                                                                                                                           |
       | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
       |   | * If you choose the same device brand and model under both allowed and disallowed devices, then the disallowed selection takes precedence.

       * These lists are continuously updated as new brands and models are introduced to the market. |

11. To define the minimum operating system that a user's device (Android or iOS) must be running to authenticate with PingID mobile app:

    1. In the **Mobile requirements** section, select **Require device minimum operating system**.

    2. In the relevant list (**iOS** or **Android**), select the minimum OS version you want to allow.

       |   |                                                                                                                                                                                            |
       | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
       |   | The list of supported operating systems is dynamic and can change as new versions are introduced. Discontinued support of older versions can also impact the minimum supported OS version. |

12. To define the minimum version of PingID mobile app that a user must be running to authenticate:

    1. In the **Mobile requirements** area, select **Require minimum PingID version**

    2. In the relevant list (**iOS** or **Android**), select the minimum PingID mobile app version you want to allow.

       |   |                                                                                                                                                                                                                                                                                                                          |
       | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
       |   | * Use this option if you want to require that your users have access to new features and the latest security benefits, or to disallow older versions of the PingID mobile app.

       * The list of supported versions is dynamic and can change as new versions are introduced and support of older versions is discontinued. |

13. To require a user's device to have a device lock enabled on their device to authenticate with PingID mobile app, in the **Mobile requirements** section, select **Require device lock to be enabled on device**.

14. To prevent users from authenticating with a rooted or jailbroken device, in the **Mobile requirements** section, select **Require the device not to be rooted or jailbroken**.

15. To enforce the use of a device that includes a hardware biometrics sensor, when pairing or authenticating with PingID mobile app, in the **Mobile requirements** section, select **Require the device to have biometric capabilities**.

16. To allow your organization's Mobile Device Management (MDM) to control activities of your users when using PingID mobile app:

    1. In the **Mobile requirements** section, select **Require Mobile Device Management**. A token is automatically generated in UUID format. Administrators can edit the key value if required.

    2. In the **Effective Date** field, enter a date by which you want the MDM requirement to be applied. Users are blocked from authenticating until the MDM system has distributed the token to all managed devices. The effective date should allow enough time for the MDM system to complete the distribution.

    3. Configure the organization's MDM system. You can find third-party MDM system configuration examples in [Third-party MDM system configuration for PingID integration](p1_third_party_mdm_configuration_for_pid.html).

       |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
       | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
       |   | * You can also generate a new token, rotate a token, or revoke a token.

       * Multiple keys can coexist, for example, for allowing time for rotating keys and the time it takes to phase in new keys and retire old ones. PingID checks all listed keys to verify a match with the key submitted in the authentication request. The MDM does not retain multiple values for the same token. Support for multiple keys is provided through PingID.Learn more in [Managing MDM tokens](p1_pid_managing_mdm_tokens.html). |

17. Click **Save**.

---

---
title: (Workforce Only) Configuring YubiKey OTP authentication for PingID
description: How to configure YubiKey OTP authentication for PingID in Workforce environments, including hardware requirements and pairing.
component: pingone
page_id: pingone:strong_authentication_mfa:p1_pid_yubikey
canonical_url: https://docs.pingidentity.com/pingone/strong_authentication_mfa/p1_pid_yubikey.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 5, 2024
---

# (Workforce Only) Configuring YubiKey OTP authentication for PingID

YubiKey hard tokens can be used to generate a one-time passcode (OTP) with which to authenticate. YubiKeys can be paired for Yubico OTP authentication.

|   |                                                                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If your YubiKey is FIDO2 compliant, you can pair it as a passkey (FIDO2/U2F Security Key). For information about configuring a YubiKey as a passkey for FIDO2 authentication, see [Configuring FIDO2 authentication (Passkeys)](p1_strong_auth_configuring_fido.html) |

A YubiKey hardware authenticator can be used in sensitive environments or for users working in environment with limited device or phone access, such as hospitals, financial institutions, or federal buildings.

The YubiKey hardware gives your enterprise a variety of form factors to allow the user to authenticate combined with the contextual awareness of PingID. YubiKey doesn't require a battery or network connectivity, so it's always on and accessible for MFA.

When YubiKey authentication is enabled, the user registers their personal YubiKey and pairs it with their PingID account. This creates a trust between the YubiKey and the user's account so they can use the YubiKey to authenticate during the sign on process.

Learn how to configure a YubiKey for use with PingID in PingOne in [Configuring an MFA policy for strong authentication](p1_creating_an_mfa_policy_for_strong_auth.html).

|   |                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------- |
|   | Find the YubiKey models that support Yubico OTP in the [YubiKey products page](https://www.yubico.com/products/yubikey-hardware). |

---

---
title: Accessing the legacy PingID admin portal from PingOne
description: How to access the legacy PingID admin portal from your PingOne environment for configurations not yet available in PingOne.
component: pingone
page_id: pingone:strong_authentication_mfa:p1_access_legacy_pid_admin_portal
canonical_url: https://docs.pingidentity.com/pingone/strong_authentication_mfa/p1_access_legacy_pid_admin_portal.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 10, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Accessing the legacy PingID admin portal from PingOne

## About this task

If you have a PingID account integrated with a PingOne environment, most configurations are done in PingOne. However there are a limited number of administrative configurations (such as PingID policy) that are currently configured in the legacy PingID admin portal.

You can access the PingID admin poral directly from the PingOne environment home page.

## Steps

* In PingOne, go to **Overview** and under **Services**, click the PingID icon. The legacy PingID admin portal opens.

  |   |                                                                                                                                                          |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Fields that should be configured in PingOne are greyed out in the legacy PingID admin portal, and a link to the equivalent field in PingOne is provided. |

---

---
title: Adding the PingID mobile app for Android in Microsoft Intune
description: How to add the PingID mobile app for Android as an MDM-managed app in Microsoft Intune to push configurations to Android devices.
component: pingone
page_id: pingone:strong_authentication_mfa:p1_pid_adding_pid_mobile_app_android_in_intune
canonical_url: https://docs.pingidentity.com/pingone/strong_authentication_mfa/p1_pid_adding_pid_mobile_app_android_in_intune.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 1, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  result: Result:
  result-2: Result:
  result-3: Result:
  next-steps: Next steps
---

# Adding the PingID mobile app for Android in Microsoft Intune

Configure PingID mobile app as an MDM-managed app for Android devices in Microsoft Intune to ensure that PingID mobile app configurations can be pushed to Android devices.

## Before you begin

In the Intune dashboard, configure Android work profile devices. Learn more in [Enroll Android devices in Microsoft Intune](http://learn.microsoft.com/en-us/intune/intune-service/fundamentals/deployment-guide-enrollment-android) in the Microsoft Intune documentation.

## About this task

This is an example configuration of Android for Work without G Suite. You can configure Android for Work for MDM with G Suite.

## Steps

1. Go to the [Microsoft Azure portal](https://portal.azure.com/) and sign on.

2. Go to **Intune > Home > Client Apps > Managed Google Play**.

3. In the **Client Apps - Managed Google Play** window, click **Open the Managed Google Play Store**.

   ![A screen capture of the Client Apps - Managed Google Play window, highlighting the Open the Managed Google Play Store app.](_images/kek1564020746340.png)

   ### Result:

   Google Play opens in a new browser tab or window.

4. Search for the PingID mobile app and select it.

   ![A screen capture of Google Play search results, showing the PingID mobile app.](_images/vks1564020747191.png)

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

Learn more in [Setting the PingID mobile app configuration policies for Microsoft Intune](p1_pid_setting_pid_configuration_policies_for_intune.html).

---

---
title: Adding the PingID mobile app for iOS in Microsoft Intune
description: How to add the PingID mobile app for iOS as an MDM-managed app in Microsoft Intune to enable configuration management for iOS devices.
component: pingone
page_id: pingone:strong_authentication_mfa:p1_pid_adding_pid_mobile_app_ios_in_intune
canonical_url: https://docs.pingidentity.com/pingone/strong_authentication_mfa/p1_pid_adding_pid_mobile_app_ios_in_intune.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 1, 2024
section_ids:
  steps: Steps
  result: Result:
  result-2: Result:
  result-3: Result:
  result-4: Result:
  result-5: Result:
  next-steps: Next steps
---

# Adding the PingID mobile app for iOS in Microsoft Intune

Configure PingID mobile app as an MDM-managed app for iOS devices in Microsoft Intune.

## Steps

1. Go to the [Microsoft Azure portal](https://portal.azure.com/) and sign on.

2. Go to **Intune → Client Apps > Apps > +Add > Add App**.

3. In the **App Type** list, select **iOS**.

   ![A screen capture of the Add App window and the App Type list. The list has multiple sections of apps: Store App, which has Android, iOS, Windows Phone 8.1, and Windows; Office 365 Suite, which has Windows 10 and macOS; and Other, which has Web link, Built-in app, Line-of-business app, and Windows app (Win32) - preview.](_images/xhb1564020693727.png)

4. In the **Search the App Store** section, click **Select App**.

   ![A screen capture of the Add App window and the Search the App Store section.](_images/wsh1564020694371.png)

   ### Result:

   The **Search the App Store** window opens.

   ![A screen capture of the Search the App Store window.](_images/cir1564020694939.png)

5. In the search field, enter the App Store URL for PingID mobile app: https\://itunes.apple.com/us/app/pingid/id891247102?mt=8\[].

   ### Result:

   The PingID mobile app app is displayed.

   ![A screen capture of the Search the App Store window showing the PingID mobile app in the search results.](_images/lwh1564020695575.png)

6. Click the PingID mobile app.

   ### Result:

   The **Add App** window opens with the **Configure** option enabled.

7. To open the **App Information** window, click **Configure**.

8. In the **App Information** window, make any required changes, and then click **OK**.

   ![A screen capture of the App Information window. Required fields are marked by an asterisk.](_images/bpb1564020696261.png)

   ### Result:

   In the **Add App** window, the **Add** button is enabled.

9. In the **Add App** window, click **Add**.

   ### Result:

   Your app appears in the list of client apps.

   ![A screen capture of the Client Apps - Apps window, highlighting the PingID mobile app for iOS.](_images/xqi1564020697024.png)

## Next steps

See [Setting the PingID mobile app configuration policies for Microsoft Intune](p1_pid_setting_pid_configuration_policies_for_intune.html).

---

---
title: Configure a DaVinci authentication flow to use a risk policy
description: To use authentication policy evaluation with PingID desktop app, you must configure the PingOne DaVinci authentication subflow to use PingOne risk policy:
component: pingone
page_id: pingone:strong_authentication_mfa:p1_desktop_app_davinci_flow_configuration
canonical_url: https://docs.pingidentity.com/pingone/strong_authentication_mfa/p1_desktop_app_davinci_flow_configuration.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Configure a DaVinci authentication flow to use a risk policy

To use authentication policy evaluation with PingID desktop app, you must configure the PingOne DaVinci authentication subflow to use PingOne risk policy:

1. In DaVinci:

   1. Download the latest out-of-the-box (OOTB) PingID authentication subflow from the [Ping Identity Marketplace](https://marketplace.pingone.com/item/pingid-authentication-subflow) and customize as required.

   2. In the PingID Authentication subflow **Flow Settings node**, set the `useProtectPolicyEvaluation` property to `True`.

---

---
title: Configuring an MFA policy for strong authentication
description: How to create and configure an MFA policy for strong authentication, including the authentication methods users can use and the settings for each method.
component: pingone
page_id: pingone:strong_authentication_mfa:p1_creating_an_mfa_policy_for_strong_auth
canonical_url: https://docs.pingidentity.com/pingone/strong_authentication_mfa/p1_creating_an_mfa_policy_for_strong_auth.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 30, 2026
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  result: Result:
  next-steps: Next steps
---

# Configuring an MFA policy for strong authentication

Configure the multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)* policy. Add and configure the relevant authentication methods, then add the MFA policy as a step to your authentication policy.

## Before you begin

* Optionally configure MFA general settings, including the maximum number of MFA methods allowed per user, authentication method selection, and account lockout settings. Learn more in [MFA Settings](../authentication/p1_mfa_settings.html).

* Workforce environments with legacy FIDO2 implementation: When creating a new MFA policy, legacy FIDO2 security key and FIDO2 biometrics authentication aren't supported. Learn about how to update your MFA policy to support FIDO2 authentication in [Updating an existing MFA policy to use FIDO2](p1_updating_an_mfa_policy_to_fido2.html).

* (Customer only) Configure an authentication policy with an MFA step. Learn more in [Authentication policies](../authentication/p1_authenticationpolicies.html).

  |   |                                                                                      |
  | - | ------------------------------------------------------------------------------------ |
  |   | In a Workforce environment, PingOne automatically creates the authentication policy. |

* Some authentication methods have configuration steps that you must complete in addition to configuring the MFA policy. Some of these additional configuration steps are compulsory (such as configuring an application for PingID mobile app or configuring a FIDO policy for FIDO2 authentication), and some are optional (such as configuring a notification template for SMS and voice authentication).

  Learn more about the configuration options, as well as any limitations or requirements for each authentication method, in [Configuring strong authentication methods (MFA)](p1_configuring_strong_authentication_start.html).

To create an MFA policy:

* Configure the relevant MFA policy settings for the authentication methods that you want to enable.

* If the authentication method requires additional configuration, make sure to complete the additional configuration steps, as outlined in this procedure.

## Steps

1. Go to **Authentication > MFA**.

2. On the **MFA Policies** page, click the **[icon: plus, set=fa]**icon.

3. In the **Name** field, enter a meaningful name for the policy.

   The maximum length is 256 characters.

4. In the **Method Selection** list, select which authentication device is presented first to users with more than one paired device.

   ### Choose from:

   * **User selected default**: Allow the user to authenticate with the device they selected as their default device.

   * **Prompt user to select**: If more than one method is available, at the authentication prompt, the user must select which paired authentication device to use.

   * **Always display devices**: Even if the user has only one permitted authentication method paired with their account, the user is prompted to select an authentication method.

     |   |                                                                                                                                                                                                                                                                                                                                                            |
     | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | PingOne doesn't apply the **Method Selection** setting if you've enabled device authorization, and the user is accessing an application from a trusted mobile device. Similarly, PingOne doesn't apply the setting if the user tries to access the application with a browser they previously used for FIDO2 authentication. In such cases, FIDO2 is used. |

5. In the **Notification Policy** list, select the notification policy you want to apply to the MFA policy, or select **Use the default policy** to select the default notification policy defined for the environment. Learn more in [Notification Policies](../user_experience/p1_creating_a_notification_policy.html).

6. In the **Send notification when new device paired** list, select how to notify the user when a new device is added to their account.

   ### Choose from:

   * **No notification**: User shouldn't be notified.

   * **By email, else SMS**: By email (or by SMS if no email address available in the user profile).

   * **By SMS, else email**: By SMS (or by email if no phone number available in the user profile).

7. In the **User Access Configuration** section select any of the following:

   * **Skip account lockout verification**: When selected, applies the MFA policy during authentication, even if the user is locked out of their account.

   * **Block authentication when user status is disabled**: When selected, prevents users whose accounts are disabled from authenticating with MFA.

   * **Block authentication when user's MFA is disabled**: When selected, prevents users from authenticating when their MFA is disabled. When deselected the user can bypass MFA if their MFA is disabled.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The **Block authentication when user's MFA is disabled** setting is ignored by the following flow types:- **[PingID Authentication Subflow](https://marketplace.pingone.com/item/pingid-authentication-subflow)**: This has its own internal logic for handling MFA bypass checks. Disable the subflow's internal bypass check to allow this setting to take effect.

- **[Custom sign-on policy flows](../pingone_tutorials/p1_p1tutorial_build_custom_policy.html)**: These are designed to always block MFA bypass attempts. |

1. **Remember me**: This feature allows users that have authenticated successfully at least once to skip MFA on their next authentication for a specified time period.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The workflow for this feature depends on your use case:- Customer use cases: you'll need to use the PingOne API to implement "remember me" functionality in your web applications. Learn more in [Remembered Devices](https://developer.pingidentity.com/pingone-api/mfa/users/remembered-devices.html).

   - Workforce use cases:

     * This feature is only available in environments that include the PingID service and requires PingID adapter 2.17 or later.

     * For the Singapore geography, use DaVinci to create this functionality.

     * When using PingID with PingOne for authentication and registration flows, enable the "remember me" option in the MFA policy and then reference the relevant MFA policy in your risk policy. For an example, see [Using predictors to recreate legacy PingID policy rules](../threat_protection_using_pingone_protect/p1_protect_recreating_legacy_pingid_rules.html). |

   1. Under **Remember Me Configurations**, select **Web Session**.

   2. Set how long the system should remember a device after a user authenticates (minimum 1 hour, maximum 90 days).

2. Enable and configure the authentication methods you want to provide for your users:

   > **Collapse: (Customer only) Mobile applications**
   >
   > 1. Click **[icon: plus, set=fa]\(Add Applications)**, select the name of the mobile application to use from those you have defined for the environment, and click **Save**. Learn more about creating an application in [Applications](../applications/p1_applications_menu.html).
   >
   >    1. Define the following fields for the application:
   >
   >       * **OTP & Push**: The mechanism to use to allow the user to authenticate.
   >
   >         Choose from:
   >
   >         * **Push**: Use only the standard push mechanism.
   >
   >         * **OTP**: Use only OTPs.
   >
   >         * **Push & OTP**: Use the standard push mechanism and allow OTP as a backup mechanism.
   >
   >       * **Push Notification Timeout**: The amount of time that a user has to respond to a push notification before it expires.
   >
   >       * **Allow Pairing**: To prevent users from pairing their device with this authentication method, clear the checkbox.
   >
   >       * **Device Integrity**: Define how authentication and registration attempts should proceed in the event that a device integrity check yields inconclusive results. Select **Permissive** if you want to allow the process to continue. Select **Restrictive** if you want to block the user in such situations.
   >
   >         |   |                                                                                                                                                                                |
   >         | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   >         |   | The **Permissive/Restrictive** buttons display only if you enable device integrity checking for the application on the **Mobile** tab of the **Applications** definition page. |
   >
   >       * **Number Matching**: Enable this option if you want the mobile push to require the user to match a number that they were shown when requesting access. To specify how matching is carried out, select one of the number matching options on the **Mobile** tab of the **[Application](../applications/p1_edit_application_native.html)** page for the relevant application.
   >
   >       * **Auto Enrollment**: Auto Enrollment means that the user can authenticate from an unpaired device, and the successful authentication results in the pairing of the device for MFA. To enable, select the checkbox.
   >
   >         |   |                                                                                                                                                                                                                                                                                                                              |
   >         | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   >         |   | To allow automatic enrollment even if the user doesn't have any existing paired devices, go to the authentication policy that you created. In the MFA step, verify that **None or Incompatible Methods** is set to **Bypass**. Learn more in [Editing an authentication policy](../authentication/p1_edit_auth_policy.html). |
   >
   >       * **Device Authorization**: When enabled, the trusted device handles the authentication automatically without user involvement. This automatic mechanism is used only if the user is requesting access from the same device. To enable, select the checkbox.
   >
   >         Select the **Device Authorization** checkbox and then choose one of the following options for **Extra Verification**:
   >
   >         * **Disabled**: Don't use an extra verification step.
   >
   >         * **Permissive**: The system sends a push to the device for automatic handling. If the device doesn't receive the push, the system still grants access.
   >
   >         * **Restrictive**: The system sends a push to the device for automatic handling. If the device doesn't receive the push, the system doesn't grant access.
   >
   >       * **Pairing Key Lifetime**: Indicate how much time an issued pairing key can be used until it expires.
   >
   >       * **Limit Push Notifications**: Use this option to help you prevent attacks based on repeated push notifications that lead users to eventually accept the request. Define the number of consecutive push notifications a user can ignore or reject within a defined period before push notifications are blocked for the application:
   >
   >         * **Push Limit**: The number of notifications that a user can decline or ignore (1 - 50).
   >
   >         * **Time Period**: Time period during which the notifications are counted towards the limit (1 minute - 120 minutes).
   >
   >         * **Lock Duration**: Duration for which the device is blocked (2 - 30 minutes).

   > **Collapse: (Workforce only)**
   >
   > |   |                                                                                                                                                                                                                                                                     |
   > | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > |   | If you haven't already done so, configure the PingID mobile app. You can also do this after you finish configuring the MFA policy. Learn more in [(Workforce Only) Configuring the PingID mobile application settings](p1_configuring_pid_mobile_application.html). |
   >
   > 1. In the **Mobile Applications** section, configure the following fields:
   >
   >    * **Passcode Failure Limit**: The maximum number of times that an one-time passcode (OTP) *(tooltip: \<div class="paragraph">
   >      \<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>
   >      \</div>)* entry can fail.
   >
   >    * **Lock Duration**: The amount of time PingOne locks the authentication method if the user exceeds the **Passcode Failure Limit** (2 - 30 minutes).
   >
   >    * **Rename device during pairing**: Select the checkbox to allow users to define a device nickname during the pairing flow.
   >
   > 2. Under **Add Applications**, **PingID mobile**, configure the following PingID mobile app-specific fields:
   >
   >    * **Authentication request timeout**: Define the amount of time given before an authentication request times out.
   >
   >      * **Device Timeout**: Defines the amount of time until the push notification reaches the device. The default is 25 seconds.
   >
   >      * **Total Timeout**: Defines the amount of time the user has to complete the authentication request. The default is 40 seconds.
   >
   >        **Total Timeout** must exceed **Device Timeout** by at least 15 seconds.
   >
   >    * **Pairing Key Lifetime**: Indicate how much time an issued pairing key and QR code can be used until they expire (minimum 1 minute, maximum 48 hours).
   >
   >    * **Allow Pairing**: Select the checkbox to allow users to pair PingID mobile app. To only allow users from specific IP addresses to pair PingID mobile application, in the list, select **Only these addresses**, and then enter the IP addresses in the format shown in the field.
   >
   > 3. **Limit Push Notifications**: Use this option to help you prevent attacks based on repeated push notifications that lead users to eventually accept the request. Define the number of consecutive push notifications that a user can ignore or reject within a defined period before push notifications are blocked for the application:
   >
   >    1. **Push Limit**: Number of notifications a user can decline or ignore (1 - 50).
   >
   >    2. **Time Period**: Time period during which the push notifications are counted towards the push limit (minimum 1 minute, maximum 120 minutes).
   >
   >    3. **Lock Duration**: Duration for which the device is blocked from authenticating. (1 second - 120 minutes.)
   >
   >       |   |                                                                                                                                                                                             |
   >       | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   >       |   | Limiting the number of push notifications that can be declined or ignored can reduce the likelihood of a user acknowledging a malicious push notification as part of an MFA fatigue attack. |
   >
   > 4. (Optional) Enable the following authentication options for users of PingID mobile app:
   >
   >    |   |                                                                                                                                                                                                                                                               |
   >    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   >    |   | Only the options that are enabled here are available as an Allowed Authentication Method in PingID policy. You can find more information about PingID policy in [Creating a risk policy for registration and authentication](p1_configuring_pid_policy.html). |
   >
   >    * **Push Notification**: Send push notifications to the user's device to notify them of an authentication request.
   >
   >    * **One-Time Passcode**: Allow the user to use a one-time passcode (OTP) to authenticate. The OTP can be used to authenticate even when offline.
   >
   >    * **Biometrics**: Allow the user to authenticate with their device biometrics, such as face or fingerprint authentication.
   >
   >    * **Number Matching**: Allow the user to authenticate by matching the number displayed on the user's accessing device with the corresponding number in PingID mobile app.

   > **Collapse:&#x20;**
   >
   > * In the **Allowed Authentication Methods** section, select the **Authenticator App** checkbox and then configure the following fields:
   >
   >   * **Passcode Failure Limit**: The maximum number of times that an OTP entry can fail (1 - 7).
   >
   >     |   |                                                                                                                                                                                                                               |
   >     | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   >     |   | In authentication flows that implement one-time authentication with the PingOne MFA API, users aren't blocked after exceeding the configured passcode failure limit, even if you specify a blocking period in the MFA policy. |
   >
   >   * **Lock Duration**: The amount of time PingOne locks the authentication method if the user exceeds the **Passcode Failure Limit** (2 - 30 minutes).
   >
   >   * **Passcode Grace Period**: Authenticator app passcodes are valid for 30 seconds (refresh duration). However, to cover time synchronization issues, there is a default grace period of 5 times the refresh duration in each direction. Taking the grace period into account, the passcode is valid for the base 30 seconds plus 5 x 30 = 150 seconds behind the time of issue and 150 seconds past the expiration time. Use **Passcode Grace Period** to shorten or lengthen this period. Each window represents 30 seconds in both directions.
   >
   >   * **Allow Pairing**: To prevent users from pairing their device with this authentication method, clear the checkbox.
   >
   >   * **Rename device during pairing**: Select the checkbox to allow users to define a device nickname during the pairing flow.
   >
   >   * **Show application name**: To help users recognize which application the OTP displayed in their authenticator app is for, select this option and provide the text to display alongside the OTP. If you're using the same MFA policy for multiple applications, use a name that reflects the group of applications.
   >
   >     |   |                                                                                                                                                                                                                          |
   >     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   >     |   | If you provide an application name, remember that the name is set for each user when they pair their device. If you update the name later, the new name displays only to users who paired their device after the update. |

   > **Collapse: (Workforce only)**
   >
   > * In the **Allowed Authentication Methods** section, select the **YubiKey** checkbox and then configure the following fields:
   >
   >   * **Passcode Failure Limit**: The maximum number of times that an OTP entry can fail (1 - 7).
   >
   >     |   |                                                                                                                                                                                                                               |
   >     | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   >     |   | In authentication flows that implement one-time authentication with the PingOne MFA API, users aren't blocked after exceeding the configured passcode failure limit, even if you specify a blocking period in the MFA policy. |
   >
   >   * **Lock Duration**: The amount of time PingOne locks the authentication method if the user exceeds the **Passcode Failure Limit** (2 - 30 minutes).
   >
   >   * **Allow Pairing**: To prevent users from pairing their device with this authentication method, clear the checkbox.
   >
   >   * **Rename device during pairing**: Select the checkbox to allow users to define a device nickname during the pairing flow.

   > **Collapse:&#x20;**
   >
   > * In the **Allowed Authentication Methods** section, select the **Email** checkbox, and then configure the following fields:
   >
   >   * **Passcode Failure Limit**: The maximum number of times that an OTP entry can fail (1 - 7).
   >
   >     |   |                                                                                                                                                                                                                               |
   >     | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   >     |   | In authentication flows that implement one-time authentication with the PingOne MFA API, users aren't blocked after exceeding the configured passcode failure limit, even if you specify a blocking period in the MFA policy. |
   >
   >   * **Lock Duration**: PingOne locks the authentication method if the user exceeds the **Passcode Failure Limit**. Accepted values range from 0 seconds - 30 minutes.
   >
   >   * **Passcode Lifetime**: The amount of time the passcode is valid before it expires (maximum 30 minutes).
   >
   >     |   |                                                               |
   >     | - | ------------------------------------------------------------- |
   >     |   | An OTP is valid for 30 minutes by default (refresh duration). |
   >
   >   * **Passcode Length**: Configure the length of the OTP (6 - 10 digits). The default is 6.
   >
   >   * **Allow Pairing**: To prevent users from pairing their device with this authentication method, clear the checkbox.
   >
   >   * **Rename device during pairing**: Select the checkbox to allow users to define a device nickname during the pairing flow.
   >
   >     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   >     | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   >     |   | The following options are only available in Workforce environments:- To prepopulate or restrict user registration with user directory data, follow the instructions in [Pre-populating or restricting user registration data](p1-strong-auth-pre-populate-or-restrict.html)
   >
   >     - To configure email authentication as a backup authentication method, follow the instructions in [Configuring backup authentication methods](https://docs.pingidentity.com/pingid/pingid_service_management/pid_configuring_backup_authentication_methods.html). |

   > **Collapse:&#x20;**
   >
   > 1. In the **Allowed Authentication Methods** section, select the checkbox for the relevant authentication method, and then configure the following fields for each method that you want to add:
   >
   >    * **Passcode Failure Limit**: The maximum number of times that an OTP entry can fail (1 - 7).
   >
   >      |   |                                                                                                                                                                                                                               |
   >      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   >      |   | In authentication flows that implement one-time authentication with the PingOne MFA API, users aren't blocked after exceeding the configured passcode failure limit, even if you specify a blocking period in the MFA policy. |
   >
   >    * **Lock Duration**: The amount of time PingOne locks the authentication method if the user exceeds the **Passcode Failure Limit**. Accepted values range from 0 seconds - 30 minutes.
   >
   >    * **Passcode Lifetime**: The amount of time the passcode is valid before it expires (maximum 30 minutes).
   >
   >      |   |                                                               |
   >      | - | ------------------------------------------------------------- |
   >      |   | An OTP is valid for 30 minutes by default (refresh duration). |
   >
   >    * **Passcode Length**: Configure the length of the OTP (6 - 10 digits). The default is 6.
   >
   >    * **Allow Pairing**: To prevent users from pairing their device with this authentication method, clear the checkbox.
   >
   >    * **Rename device during pairing**: Select the checkbox to allow users to define a device nickname during the pairing flow.
   >
   > 2. Configure all other SMS or voice-related configurations, including creating notification templates, limiting the number of SMS or voice messages that a user can send, localizing messages, and creating a custom sender account. Learn more in [Configuring SMS and voice authentication](p1_strong_auth_sms_voice_authentication.html)

   > **Collapse: (Customer only)**
   >
   > * In the **Allowed Authentication Methods** section, select the **WhatsApp** checkbox, and then configure the following fields.
   >
   >   |   |                                                                                                                                                                                                                                       |
   >   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   >   |   | To select the **WhatsApp** checkbox, you must define your WhatsApp Business account as a sender in PingOne. Learn more in [Configuring a custom WhatsApp sender account](../settings/p1-using-a-custom-whatsapp-sender-account.html). |
   >
   >   * **Passcode Failure Limit**: The maximum number of times that an OTP entry can fail (1 - 7).
   >
   >     |   |                                                                                                                                                                                                                                    |
   >     | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   >     |   | In authentication flows that implement one-time authentication with the PingOne MFA API, users are not blocked after exceeding the configured **Passcode Failure Limit**, even if you specify a blocking period in the MFA policy. |
   >
   >   * **Lock Duration**: The amount of time PingOne locks the authentication method if the user exceeds the **Passcode Failure Limit** (2 - 30 minutes).
   >
   >   * **Passcode Lifetime**: The amount of time the passcode is valid before it expires (maximum 30 minutes).
   >
   >   * **Passcode Length**: Configure the length of the OTP (6 - 10 digits). The default is 6.
   >
   >   * **Allow Pairing**: To prevent users from pairing their device with this authentication method, clear the checkbox.
   >
   >   * **Rename device during pairing**: Select the checkbox to allow users to define a device nickname during the pairing flow.

   > **Collapse:&#x20;**
   >
   > |   |                                                                                                                                                                                       |
   > | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > |   | Two FIDO policies are available out-of-the-box. Modify an existing policy or create additional FIDO policies. Learn more in [FIDO policies](../authentication/p1_fido_policies.html). |
   >
   > * In the **Allowed Authentication Methods** section, select the **FIDO2** checkbox, and then configure the following fields.
   >
   >   * **Failure Limit**: Define the maximum number of times that a FIDO attestation or assertion can fail.
   >
   >     |   |                                                                                         |
   >     | - | --------------------------------------------------------------------------------------- |
   >     |   | The failure limit counts only attestations and assertions that reach the PingID server. |
   >
   >   * **Lock Duration**: The amount of time that the authentication method is locked if the **Failure Limit** is exceeded. Accepted values range from 2 - 7 minutes. Default value is 3 minutes.
   >
   >   * In the **Allowed Authentication Methods** section, select **FIDO2** and in the **FIDO Policy** field, select the FIDO policy that you want to apply, or select **Use the default policy** to use the default FIDO policy.
   >
   >   * **Allow Pairing**: To prevent users from pairing their device with this authentication method, clear the checkbox.
   >
   >   * **Rename device during pairing**: Select the checkbox to allow users to define a device nickname during the pairing flow.
   >
   >     |   |                                                                                                                                                                                                                                                                                                                                        |
   >     | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   >     |   | If you're editing an existing MFA policy that's using a deprecated FIDO Biometrics or Security Key authentication method, you'll need to replace it with the FIDO2 authentication method and reference an enhanced FIDO policy. Learn more in [Updating an existing MFA policy to use FIDO2](p1_updating_an_mfa_policy_to_fido2.html). |

   > **Collapse: (Workforce only)**
   >
   > * Select **PingID Desktop**, and then configure the relevant fields.
   >
   >   |   |                                                                                                                                                                                                             |
   >   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   >   |   | * To configure PingID desktop app, you must enable users to register and manage the PingID desktop app and other devices from [MyAccount](../user_experience/p1_using_myaccount_to_manage_wf_devices.html). |
   >
   >   * **Failure Limit**: Define the maximum number of times that a PingID desktop app attestation or assertion can fail (1 - 7). This limit applies specifically to server assertion failures rather than client-side authentication errors.
   >
   >   * **Lock Duration**: The amount of time this authentication method is locked if the **Failure Limit** is exceeded. Accepted values range 0 seconds - 30 minutes.
   >
   >   * **Allow Pairing**: To prevent users from pairing their device with this authentication method, clear the checkbox.
   >
   >   * **Rename device during pairing**: Select the checkbox to allow users to define a device nickname during the pairing flow.
   >
   >   * **Relying Party Domain**: Select the unique identifier that represents the website or application requesting the user's authentication (update the default value, **pingone.com**, for the relevant geography).
   >
   >   * **Relying Party ID**: Select the relevant Relying Party ID (RPID).
   >
   > * You can find complete details of configuration requirements, including how to install the PingID desktop app in [(Workforce only) Configuring the PingID desktop application](p1_pid_desktop_app_start.html).

   > **Collapse: (Workforce only)**
   >
   > |   |                                                               |
   > | - | ------------------------------------------------------------- |
   > |   | PingID desktop app isn't available in the Singapore geography |
   >
   > 1. Select **PingID desktop app (legacy)**, and then configure the following fields:
   >
   >    * **Passcode Failure Limit**: The maximum number of times that an OTP entry can fail (1 - 7).
   >
   >    * **Lock Duration**: The amount of time this authentication method is locked if the **Failure Limit** is exceeded. Accepted values range 0 seconds - 30 minutes.
   >
   >    * **Pairing Key Lifetime**: Indicates the amount of time the pairing key and QR code remain valid before they expire. (Minimum 1 minute, maximum 48 hours).
   >
   >    * **Allow Pairing**: Select the checkbox to allow users to pair **PingID desktop app (legacy)**. To only allow users from specific IP addresses to pair PingID mobile application, in the list, select **Only these addresses**, and then enter the IP addresses in the format shown in the field.
   >
   >    * **Rename device during pairing**: Select the checkbox to allow users to define a device nickname during the pairing flow.
   >
   > 2. After you complete and save the MFA policy, you can add a proxy and add a security PIN for PingID desktop app (legacy) in the **PingID desktop app (legacy)** application settings. Learn more in [PingID desktop app (legacy)](p1_pid_desktop_app_v1.html).
   >
   > |   |                                                                                                                                                                       |
   > | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > |   | Learn more about the difference between the different PingID desktop app versions in [PingID desktop app (workforce only)](p1_pid_desktop_app_version_overview.html). |

   > **Collapse:&#x20;**
   >
   > 1. In the **Allowed Authentication Methods** section, select the **OATH Token** checkbox, and then configure the following fields:
   >
   >    * **Passcode Failure Limit**: The maximum number of times that an OTP entry can fail (1 - 7).
   >
   >      * **Lock Duration**: The amount of time PingOne locks the authentication method if the user exceeds the **Passcode Failure Limit** (0 seconds - 30 minutes).
   >
   >    * **Allow Pairing**: To prevent users from pairing their device with this authentication method, clear the checkbox.
   >
   >    * **Rename device during pairing**: Select the checkbox to allow users to define a device nickname during the pairing flow.
   >
   > 2. Click the **Configure OATH tokens** link. The OATH token configurations panel opens, showing a list of previously saved tokens. To add an OATH token, do the following:
   >
   >    1. Click **Import Token**.
   >
   >    2. In the **Import OATH Token** modal, click **Choose File**, and navigate to the token seed file. Learn more about the token seed format in [Configuring OATH token authentication](p1_pid_oath_tokens.html).
   >
   >    3. Select the **Token Type**.
   >
   >       |   |                                                                                |
   >       | - | ------------------------------------------------------------------------------ |
   >       |   | The token type and OTP length are applied to all entries in the imported file. |
   >
   >    4. If you selected a TOTP **Token Type**, select the **Algorithm** you want to use and the **Refresh Interval**.
   >
   >       |   |                                                                                     |
   >       | - | ----------------------------------------------------------------------------------- |
   >       |   | The algorithm and refresh interval are applied to all entries in the imported file. |
   >
   >    5. Click **Import**. The new tokens appear in the list.
   >
   >       |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
   >       | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   >       |   | * You can find a list of prerequisites and supported OATH tokens in [Configuring OATH token authentication](p1_pid_oath_tokens.html).
   >
   >       * Make sure your OATH seed token is valid and isn't already in use. If your seed file contains entries that duplicate an existing token, an `Incomplete Token Report` error displays.
   >
   >       * To revoke one or more OATH tokens, select the checkbox next to the tokens you want to revoke, and then click **Revoke**.
   >
   >       * To export token details to a downloadable .CSV file, select the checkbox next to the tokens you want to revoke, and then click **Export CSV**. |

3. Click **Save**.

   ### Result:

   The policy is added to the **Policy** list.

   |   |                                                                                                                              |
   | - | ---------------------------------------------------------------------------------------------------------------------------- |
   |   | In the **Policy** list, click a policy to view a summary of the policy details in the right pane or edit an existing policy. |

## Next steps

* If you haven't already, add the MFA policy to the MFA step in the relevant Authentication policy. Learn more: [Adding a multi-factor authentication or PingID step](../authentication/p1_add_mfa_step.html). This is done automatically for PingID.

* Optionally configure Notification Templates to inform users about device pairing and strong authentication events. Learn more in [Notification Templates](../user_experience/p1_notifications.html).

---

---
title: Configuring Android for Work for Microsoft Intune
description: How to configure Android for Work in Microsoft Intune to push PingID mobile app configuration and MDM token to Android devices.
component: pingone
page_id: pingone:strong_authentication_mfa:p1_pid_configuring_android_work_for_intune
canonical_url: https://docs.pingidentity.com/pingone/strong_authentication_mfa/p1_pid_configuring_android_work_for_intune.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 1, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  result: Result:
  result-2: Result:
  result-3: Result:
  result-4: Result:
  result-5: Result:
  result-6: Result:
  result-7: Result:
  result-8: Result:
  next-steps: Next steps
---

# Configuring Android for Work for Microsoft Intune

To ensure that PingID mobile app configurations can be pushed to iOS devices, install an Apple Push Notification service (APNs) certificate in Microsoft Intune.

## Before you begin

In the Intune dashboard, configure Android work profile devices. Learn more in [Enroll device and create Android work profile](https://learn.microsoft.com/en-us/mem/intune/user-help/enroll-device-android-work-profile) in the Microsoft Intune documentation.

## About this task

This is an example configuration of Android for Work without G Suite. You can also configure Android for Work for MDM with G Suite.

## Steps

1. Go to the [Microsoft Azure portal](https://portal.azure.com/) and sign on.

2. Go to **Intune > Home > Client Apps > Managed Google Play**.

   ### Result:

   The **Managed Google Play** window opens.

3. Click **Open the Managed Google Play Store**.

   ![A screen capture of the Managed Google Play window, highlighting the Open the Managed Google Play Store link.](_images/kek1564020746340.png)

   ### Result:

   Google Play opens in a new browser tab or window.

4. Search for the PingID mobile app and select it.

   ![A screen capture of Google Play search results, showing the PingID app.](_images/vks1564020747191.png)

5. Click **Approve**.

   ![A screen capture of the PingID app in Google Play.](_images/fsn1564020748917.png)

   |   |                                                                   |
   | - | ----------------------------------------------------------------- |
   |   | You might need to sign on as a managed Google Play administrator. |

   ### Result:

   The **Client Apps - Apps** window opens.

6. From the **Apps** list, click the PingID Google Play entry, and then from the left-hand menu, click **Assignments**.

   ![A screen capture of the Client Apps - Apps window.](_images/azj1564020749604.png)

   ### Result:

   The **PingID - Assignments** window opens.

7. In the **PingID - Assignments** window, assign the PingID mobile app for Android to user groups.

   Learn more about creating, managing, and assigning apps to groups in the relevant Intune documentation.

   ![A screen capture of the Assignments window.](_images/gby1564020750402.png)

8. Go to **Intune > Client Apps > App Configuration Policies**, and then click **Add**.

   ### Result:

   The **Add Configuration Policy** window opens.

9. In the **Name** field, enter a name for the policy.

10. In the **Description** field, add a description.

    ![A screen capture of the Add Configuration Policy window showing the Name field, the Description field, and the Device enrollment type list.](_images/zew1564020751584.png)

11. In the **Device Enrollment Type** list, select **Managed Devices**.

    ![A screen capture of the Device Enrollment Type list with the options for Managed devices and Managed apps.](_images/wkz1564020752154.png)

    ### Result:

    The **Platform** list is displayed.

12. From the **Platform** list, choose **Android**.

    ![A screen capture of the Platform list.](_images/fbg1564020752678.png)

13. At the bottom of the window, click **Add**.

    ### Result:

    The **Associated App** tab is displayed.

14. On the **Associated App** tab, click **PingID**.

    ![A screen capture of the Associated App tab. In this screen capture, the list of available apps include Intune Company Portal and PingID.](_images/ipq1564020753239.png)

    ### Result:

    The **Configuration Settings** tab is displayed.

15. In the **Configuration Settings Format** list, select **Use Configuration Designer**.

    ![A screen capture of the Configuration Settings tab showing the Configuration Settings Format list with the options Use Configuration Designer and Enter JSON Data.](_images/xyc1564020753910.png)

16. In the **Configuration Value** field, enter the PingID MDM token, and then click **Add**.

    Learn more in [(Workforce Only) Configuring the PingID mobile application settings](p1_configuring_pid_mobile_application.html).

    ![A screen capture of the Configuration Settings tab.](_images/exw1564020754692.png)

## Next steps

Learn more in [Adding the PingID mobile app for Android in Microsoft Intune](p1_pid_adding_pid_mobile_app_android_in_intune.html).

---

---
title: Configuring Android for Work for MobileIron
description: How to configure Android for Work in MobileIron MDM to push PingID mobile app configuration to Android devices.
component: pingone
page_id: pingone:strong_authentication_mfa:p1_pid_configuring_android_work_for_mobileiron
canonical_url: https://docs.pingidentity.com/pingone/strong_authentication_mfa/p1_pid_configuring_android_work_for_mobileiron.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 5, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring Android for Work for MobileIron

Configure Android for Work for the organization's mobile device management (MDM) so that the PingID mobile app configuration can be pushed to Android devices.

## About this task

|   |                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------- |
|   | This is an example configuration of Android for Work with G Suite. You can configure Android for Work MDM without G Suite. |

## Steps

1. Go to **Admin → Google/Android > Android for Work**, and then click **Use Alternate Setup**.

   ![Screen capture of the Android for Work window with the Alternate Setup Method option highlighted.](_images/daw1564020734284.png)

2. In the **Get Started** section, click **Google Developers Console**, and follow the on-screen instructions.

   ![Screen capture of the Android for Work window showing the Get Started, Enter Token and Connect and Authorize sections.](_images/smz1564020735175.png)

3. In MobileIron's admin portal, under **Enter Token and Connect**, connect to your organization's Google service.

4. In the **MDM Token** field, enter the token from the previous step.

5. In the **Domain** field, enter the domain by uploading the JSON file created earlier from the Google Developers Console, and click **Connect**.

6. To enable MobileIron to manage your Google users, click **Authorize**.

---

---
title: Configuring Android for Work for Workspace ONE UEM
description: How to configure Android for Work in Workspace ONE UEM to push PingID mobile app configuration to Android devices.
component: pingone
page_id: pingone:strong_authentication_mfa:p1_pid_configuring_android_work_for_workspace_one_uem
canonical_url: https://docs.pingidentity.com/pingone/strong_authentication_mfa/p1_pid_configuring_android_work_for_workspace_one_uem.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 9, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring Android for Work for Workspace ONE UEM

Configure Android for Work for the organization's mobile device management (MDM) so that the PingID mobile app configuration can be pushed to Android devices.

## About this task

|   |                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------- |
|   | This is an example configuration of Android for Work with G Suite. Android for Work can also be configured for MDM without G Suite. |

## Steps

1. In Workspace ONE UEM, go to **Settings > Devices & Users > Android > Android For Work**.

   ![Screen capture of the Devices & Users section with the Android For Work option highlighted.](_images/wln1564020709569.png)

2. Click **Click here**.

   The browser redirects to G Suite, and on completion of the configuration, returns to Workspace ONE UEM.

   ![Screen capture of the Android For Work section with 'If you are deploying G Suite, Click here' highlighted.](_images/uwo1564020710345.png)

3. In Workspace ONE UEM, in the **Android For Work** window, click **Configure**, and enter the required details.

   ![Screen capture of Android For Work showing multiple required fields for Google Admin Console Settings, such as Domain, Enterprise Token, and Google Admin Email Address, and for Google Developer Console Settings, such as Client ID, Google Service Account Email Address, and Certificate ID.](_images/wvd1564020711140.png)

---

---
title: Configuring authenticator app authentication
description: How to enable third-party authenticator app authentication in PingOne MFA, using any TOTP-based app such as Google Authenticator or Microsoft Authenticator.
component: pingone
page_id: pingone:strong_authentication_mfa:p1_strong_auth_configuring_authenticator_app
canonical_url: https://docs.pingidentity.com/pingone/strong_authentication_mfa/p1_strong_auth_configuring_authenticator_app.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 5, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
---

# Configuring authenticator app authentication

You can use any third-party authenticator app that can generate a standard time-based one-time passcode (TOTP) for multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)*. Examples include Google Authenticator or Microsoft Authenticator.

## Before you begin

To add an authenticator app as an authentication method, you need:

* A PingOne environment. The authentication policy should include the relevant MFA policy.

## About this task

External authenticator apps are a useful solution in cases such as:

* A Workforce organization that cannot allow the PingID mobile app on their devices, as PingID must be added to the allow list.

* An organization that wants to use a single authenticator app and has users that must authenticate to multiple organizations.

Users can use an authenticator app to access an account or application through the web, VPN, Mac login, or SSH. When authenticator app authentication is enabled, users can download the authenticator app of their choice and pair it with their PingOne account. Users can pair more than one authenticator app with their account.

## Steps

* Configure the authenticator app authentication method in the MFA policy. Learn more in [MFA policy](p1_creating_an_mfa_policy_for_strong_auth.html).

---

---
title: Configuring email authentication
description: How to enable email as a PingOne MFA authentication method, sending users a one-time passcode to authenticate.
component: pingone
page_id: pingone:strong_authentication_mfa:p1_strong_auth_email
canonical_url: https://docs.pingidentity.com/pingone/strong_authentication_mfa/p1_strong_auth_email.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 5, 2024
---

# Configuring email authentication

You can enable email as an authentication method.

When email authentication is configured, and the user signs on to their account or app, they are sent an email with a one-time passcode (OTP) to authenticate with. The OTP is valid for up to 30 minutes.

* Learn how to configure email authentication in PingOne in [Configuring an MFA policy for strong authentication](p1_creating_an_mfa_policy_for_strong_auth.html).

* Learn how to configure supported languages in [Languages](../user_experience/p1_languages.html).

* Learn how to create custom email templates in [Notification Templates](../user_experience/p1_notifications.html).

* Learn how to limit the number of email notifications that can be sent per day in [Notification Policies](../user_experience/p1_creating_a_notification_policy.html).

* Use the Senders page to configure your organization's SMTP email notification server. Learn more: [Configuring a custom SMTP email notification server](../settings/p1_configure_custom_smtp_server.html) and [Configuring trusted email addresses](../settings/p1_configure_trusted_email.html).

* Specify or restrict the user to a predefined email. Learn more:

  * (Workforce only): This is configured in the PingID Admin portal [Pre-populating or restricting user registration data](https://docs.pingidentity.com/pingid/pingid_service_management/pid_prepopulating_or_restricting_user_registration_data.html).

  * (Customer only): This option is only available for environments that are integrated with PingFederate, and is configured using the PingOne MFA adapter. Learn more: [PingOne MFA IdP Adapter settings reference](https://docs.pingidentity.com/integrations/pingone/pingone_mfa_integration_kit/pf_p1_mfa_ik_p1_mfa_idp_adapter_settings_reference.html).

Workforce only:

* Learn how to add email as a backup authentication method in [Configuring backup authentication methods](https://docs.pingidentity.com/pingid/pingid_service_management/pid_configuring_backup_authentication_methods.html).

  |   |                                                          |
  | - | -------------------------------------------------------- |
  |   | This option is not available in the Singapore geography. |

  * To define a secondary email address as an additional backup authentication method:

    1. Create a user attribute named `secondaryEmail`. This attribute is case sensitive. It must appear exactly as `secondaryEmail` or the secondary email address won't be recognized. Learn more in [Adding user attributes](../directory/p1_adduserattributes.html).

    2. Map each user's secondary email value from your identity provider to the `secondaryEmail` user attribute. Learn more in [Editing an identity provider](../integrations/p1_editidentityprovider.html).

---

---
title: Configuring FIDO2 authentication (Passkeys)
description: How to configure FIDO2 authentication in PingOne, including passkeys, biometrics, and security keys, by setting up a FIDO2 policy and MFA policy.
component: pingone
page_id: pingone:strong_authentication_mfa:p1_strong_auth_configuring_fido
canonical_url: https://docs.pingidentity.com/pingone/strong_authentication_mfa/p1_strong_auth_configuring_fido.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 5, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
---

# Configuring FIDO2 authentication (Passkeys)

You can configure FIDO2 devices as an authentication method. FIDO2 devices include passkeys, FIDO2 biometrics, and security keys.

## Before you begin

To add FIDO2 as an authentication method, you need:

* A PingOne environment. The authentication policy should include the relevant MFA policy.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | FIDO2 biometrics and security keys are legacy authentication methods and must be updated to support FIDO2 authentication. Learn more: [Updating an existing MFA policy to use FIDO2](p1_updating_an_mfa_policy_to_fido2.html), and for legacy PingID accounts, see [Updating a PingID account to use PingOne FIDO2 policy for Passkey support](https://docs.pingidentity.com/pingid/pingid_service_management/pid_update_to_fido2_authentication_method.html). |

## About this task

Learn more about FIDO2 authentication in [FIDO policies](../authentication/p1_fido_policies.html).

Adding FIDO2 as an authentication method involves the following steps:

## Steps

1. [Configuring a FIDO2 policy](../authentication/p1_creating_a_fido_policy.html).

2. [Configure the MFA policy to include the FIDO2 authentication method, and include the relevant FIDO2 policy](p1_creating_an_mfa_policy_for_strong_auth.html).

---

---
title: Configuring Microsoft Intune for PingID
description: How to configure Microsoft Intune to manage the PingID mobile app on iOS and Android, including APNs certificates and configuration policies.
component: pingone
page_id: pingone:strong_authentication_mfa:p1_pid_configuring_microsoft_intune_for_pid
canonical_url: https://docs.pingidentity.com/pingone/strong_authentication_mfa/p1_pid_configuring_microsoft_intune_for_pid.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 15, 2024
section_ids:
  mdm-maintenance: MDM maintenance:
---

# Configuring Microsoft Intune for PingID

To manage the PingID mobile app using Microsoft Intune, you must apply several configuration settings.

|   |                                                                                                                                                                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The following steps are for use cases where PingID mobile authenticating devices are managed by Microsoft Intune mobile device management (MDM). In cases where PingFederate is used to apply policies on accessing devices managed by Microsoft Intune, refer to the [Intune Integration Kit](https://docs.pingidentity.com/integrations/intune/pf_intune_ik.html). |

1. In Microsoft Intune, install an Apple Push Notification service (APNs) certificate for iOS. Learn more in [Installing an APNs certificate for iOS in Microsoft Intune](p1_pid_installing_apns_certificate_ios_intune.html).

2. If your organization has iOS devices, add the PingID mobile app for iOS. Learn more in [Adding the PingID mobile app for iOS in Microsoft Intune](p1_pid_adding_pid_mobile_app_ios_in_intune.html).

3. If your organization has Android devices, add the PingID mobile app for Android. Learn more in [Adding the PingID mobile app for Android in Microsoft Intune](p1_pid_adding_pid_mobile_app_android_in_intune.html).

4. Configure PingID mobile app configuration policies for Microsoft Intune. Learn more in [Setting the PingID mobile app configuration policies for Microsoft Intune](p1_pid_setting_pid_configuration_policies_for_intune.html).

## MDM maintenance:

As part of MDM maintenance activities for the PingID mobile app, you can generate new tokens and revoke old tokens. Learn more in the following:

* In PingID: In PingOne: Generate, rotate, or revoke an MDM token. Learn more in [Managing MDM tokens](p1_pid_managing_mdm_tokens.html).

* In Microsoft Intune: Learn more in [Updating a PingID token in Microsoft Intune](p1_pid_updating_token_intune.html).

---

---
title: Configuring mobile applications
description: How to configure mobile applications for PingOne MFA, covering Customer native app integration and Workforce PingID mobile app setup.
component: pingone
page_id: pingone:strong_authentication_mfa:p1_strong_authentication_configure_mobile_applications
canonical_url: https://docs.pingidentity.com/pingone/strong_authentication_mfa/p1_strong_authentication_configure_mobile_applications.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 5, 2024
---

# Configuring mobile applications

You can can configure mobile applications for Customer and Workforce use cases.

Customer use case:

* Embed strong authentication into a native mobile application.

  1. Create a mobile application.

  2. Enable and configure the mobile application in the relevant MFA policy.

  3. Add a mobile app: [Editing an application - Native](../applications/p1_edit_application_native.html)

  4. Associate an authentication policy with a mobile app.

Workforce use case:

* [Configure PingID mobile application for strong authentication](p1_configuring_pid_mobile_application.html)

---

---
title: Configuring MobileIron for PingID
description: How to configure MobileIron to manage the PingID mobile app, including APNs certificate setup, Android for Work, and MDM integration.
component: pingone
page_id: pingone:strong_authentication_mfa:p1_pid_configuring_mobileiron_for_pid
canonical_url: https://docs.pingidentity.com/pingone/strong_authentication_mfa/p1_pid_configuring_mobileiron_for_pid.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 5, 2024
section_ids:
  ongoing-maintenance: Ongoing maintenance
---

# Configuring MobileIron for PingID

To manage PingID mobile app using MobileIron, you must apply several configuration settings.

The initial MobileIron configuration comprises the following:

1. [Installing an APNs certificate for iOS in MobileIron](p1_pid_installing_apns_certificate_ios_mobileiron.html)

2. [Configuring Android for Work for MobileIron](p1_pid_configuring_android_work_for_mobileiron.html)

3. [Configuring MobileIron for PingID MDM integration](p1_pid_configuring_mobileiron_for_mdm_integration.html)

## Ongoing maintenance

As part of mobile device management (MDM) maintenance activities, new tokens for the PingID mobile app can be generated and old tokens revoked. Learn more in the following topics:

* For PingID, learn more about generating, rotating, or revoking an MDM token in PingOne in [Managing MDM tokens](p1_pid_managing_mdm_tokens.html).

* For MobileIron, learn more in [Updating a PingID token in MobileIron](p1_pid_updating_token_mobileiron.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The previous configuration steps are for use cases where PingID multi-factor authentication (MFA) authenticating devices are managed by the MobileIron MDM. In cases where PingFederate is used to apply policies on accessing devices managed by MobileIron, refer to the [PingFederate MobileIron Integration Kit](https://support.pingidentity.com/s/document-item?bundleId=integrations\&topicId=Integration_Kits/MobileIron/mobileIronIK_c_integrationKit.html) documentation. |

---

---
title: Configuring MobileIron for PingID MDM integration
description: How to configure the PingID mobile app as an MDM-managed app in MobileIron by setting up the MDM token and managed app configuration.
component: pingone
page_id: pingone:strong_authentication_mfa:p1_pid_configuring_mobileiron_for_mdm_integration
canonical_url: https://docs.pingidentity.com/pingone/strong_authentication_mfa/p1_pid_configuring_mobileiron_for_mdm_integration.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 5, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring MobileIron for PingID MDM integration

Configure PingID mobile app as a mobile device management (MDM) managed app in MobileIron.

## About this task

|   |                                                                                                                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The procedure detailed below is the iOS example for the configuration of MobileIron for PingID MDM integration. The procedure for Android is identical. If the organization's MDM manages both iOS and Android devices, configure and save the entire procedure separately for each platform. |

## Steps

1. In the MobileIron admin console, go to **Apps > App Catalog**.

2. Choose the desired app store, and then search for PingID.

   ![Screen capture of the App Catalog with the search bar highlighted.](_images/yxn1564020736364.png)

   |   |                                                                                                                                      |
   | - | ------------------------------------------------------------------------------------------------------------------------------------ |
   |   | The following steps describe the procedure for managing the PingID app for iOS. Repeat the procedure for the PingID app for Android. |

3. Select the PingID mobile app for iOS.

   ![Screen capture of the App Catalog with multiple apps listed.](_images/hkl1564020722571.png)

4. On the **App Configurations** tab, select **iOS Managed App Configuration**.

   ![Screen capture of the PingID app with the App Configurations tab and iOS Managed App Configuration highlighted.](_images/lnx1564020723242.png)

5. Click **Add**.

   ![Screen capture of the PingID App Configurations tab with the Add button highlighted.](_images/jzx1564020737014.png)

6. Enter the **Configuration Setup** parameter values.

   | Parameter       | Value                                                   |
   | --------------- | ------------------------------------------------------- |
   | **Name**        | `PINGID_MDM_TOKEN`                                      |
   | **Token value** | The token string value for MDM, as generated inPingOne. |

   ![Screen capture of the PingID App Configurations tab with the iOS Managed App Settings fields for Key and Value highlighted.](_images/kkd1564020724155.png)

7. Click **Save**.

8. Click **Application Configurations Summary**.

9. Click **Install on device**.

10. Click **Install Application configuration settings**.

    ![Screen capture of the PingID App Configurations tab with Install Application configuration settings highlighted.](_images/vvr1564020737714.png)

11. For iOS 9 and later, set the **Install on device** switch to **ON**.

12. Select the **Convert to Managed App** checkbox.

    ![Screen capture of the Configuration Setup section with the Install on Device toggle and Convert to Managed App check box highlighted.](_images/ids1564020738462.png)

    |   |                                                                                                                                     |
    | - | ----------------------------------------------------------------------------------------------------------------------------------- |
    |   | This option transitions a non-managed app downloaded from the app store to a managed app. The user must approve it on their device. |

    |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    |   | * For Apple devices earlier than iOS 9 and Android devices

      Users must execute the following steps:

      1. Unpair the PingID mobile app on the iOS device.

      2. Uninstall the PingID mobile app from the iOS device.

      3. Reinstall the PingID mobile app from the MDM's app catalog.

      4. Pair the newly installed, MDM managed PingID mobile app.

    * For Apple devices with iOS 9 and later

      The user receives a notification on their device to approve the transition to MDM management. After user approval, the PingID mobile app installed on the iOS device is managed by the MDM. |

13. Click **Save/Update**.

    * When creating a new managed app entry, the button is marked **Save**.

    * When editing an existing entry, the button is marked **Update**.

      |   |                                                                                                                                                                                                                                                                                                                 |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Repeat the entire configuration process for Android. The admin accesses the **Android for Work** options instead of **iOS Managed App Configuration**. The prerequisite to the Android app configuration is [Configuring Android for Work for MobileIron](p1_pid_configuring_android_work_for_mobileiron.html). |

---

---
title: Configuring OATH token authentication
description: How to configure OATH hardware token authentication in PingOne for MFA, covering supported token types and seed file requirements.
component: pingone
page_id: pingone:strong_authentication_mfa:p1_pid_oath_tokens
canonical_url: https://docs.pingidentity.com/pingone/strong_authentication_mfa/p1_pid_oath_tokens.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 5, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
---

# Configuring OATH token authentication

You can enable OATH tokens as an authentication method in Customer or Workforce environments. When enabled, users can pair a supported OATH token to their account or app and use it to sign on to your company services and applications with the added security of multi-factor authentication (MFA).

## Before you begin

To configure OATH tokens, you must have the following items from each token manufacturer and for each supplied token model:

* A token seed file. The seed file can be either:

  * A `.txt` file consisting of lines with a comma separating the token serial numbers and secret keys (without spaces)

  * A `.csv` file with the token serial numbers and secret keys in different cells (without spaces or commas)

    The secret keys are strings of hexadecimal digits.

* For each seed file, a single associated token type of either TOTP or HOTP.

* For TOTP types, a refresh interval of 30 - 60 seconds, and a hash algorithm of either SHA1, SHA256, or SHA512. The default values are 30 seconds, and SHA256 respectively.

|   |                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------- |
|   | For HOTP types, a start counter can be appended as an additional field in the seed file. If absent, it defaults to 0. |

**Supported OATH tokens**

Strong authentication supports hardware OTP tokens that are OATH compliant:

* HOTP SHA-1 devices

* TOTP SHA-1, SHA-256, and SHA-512 devices with 30 or 60 second OTP refresh intervals

* Any of the above devices that use a PIN code

Ping Identity doesn't:

* Sell hardware tokens

* Recommend any particular hardware token manufacturer

The following OATH tokens have been checked for use as an MFA authentication method.

| Manufacturer | Model             | Type        |
| ------------ | ----------------- | ----------- |
| Feitian      | Display card      | TOTP-60-sec |
| Feitian      | OTP c200          | TOTP-60-sec |
| Feitian      | Display card      | HOTP        |
| Gemalto      | EZIO display card | TOTP-30-sec |
| HyperSecu    | c100 token        | HOTP        |
| HyperSecu    | Edge plus         | TOTP-60-sec |
| HyperSecu    | c200 token        | TOTP-30-sec |
| HyperSecu    | HyperOTP          | TOTP-60-sec |
| HyperSecu    | Edge plus         | TOTP-30-sec |
| Protectimus  | Protectimus TWO   | TOTP-30-sec |

## About this task

You can use OATH hardware tokens to generate a one-time passcode (OTP) to authenticate. OATH hardware tokens can be useful in situations where users don't or can't have access to the internet, a USB connection, or a mobile device for security reasons.

To add OATH tokens as an authentication method for MFA:

## Steps

* Configure the MFA policy, including the OATH-specific configurations. Learn more in [Configuring an MFA policy for strong authentication](p1_creating_an_mfa_policy_for_strong_auth.html).