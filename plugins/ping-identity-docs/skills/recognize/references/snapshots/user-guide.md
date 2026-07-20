---
title: Add account
description: Add your first account by scanning a QR code.
component: recognize
page_id: recognize:user-guide:user-guide-add-account-android
canonical_url: https://docs.pingidentity.com/recognize/user-guide/user-guide-add-account-android.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Add account

Once you have successfully downloaded the Keyless Authenticator App, you can add your first account. To add the account, click on the link you received by email from your company and follow the steps on the website.

---

---
title: Authentication
description: Authenticate using the Keyless Authenticator.
component: recognize
page_id: recognize:user-guide:user-guide-authentication
canonical_url: https://docs.pingidentity.com/recognize/user-guide/user-guide-authentication.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  windows-login: Windows login
  passwordless-login: Passwordless login
  password-keyless-mode: Password + Keyless mode
  offline-mode: Offline mode
  enabling-offline-mode: Enabling offline mode
  authenticating-when-offline: Authenticating when offline
  rdp-authentication: RDP authentication
  step-by-step-guide: Step-by-step guide
---

# Authentication

After you have linked an account, you can authenticate using the Keyless App. To authenticate, the service you linked sends a push notification to Keyless Authenticator on your smartphone.

Authentication is simple and fast, with a consistent user experience no matter which service you are authenticating to.

![Authentication on the Keyless mobile app](_images/authentication-keyless-mobile-app.gif)

## Windows login

### Passwordless login

Windows passwordless login allows you to log in to your workstation easily and securely without a password. Follow the steps below.

|   |                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | On your first Keyless passwordless login attempt, you are required to enter your existing password. This is a one-time operation to maintain high security. |

1. From your Windows lock screen, click **Sign in**.

2. You receive a push notification on your mobile phone. Clicking the notification opens the Keyless application.

3. Confirm your login attempt by clicking **Approve** in the login request screen.

4. Authenticate by looking straight into your phone camera.

[Authentication with no passwords at all](https://www.youtube.com/watch?v=NegkhI-WTKY)

### Password + Keyless mode

Windows Password + Keyless mode allows you to log in to your workstation by adding Keyless as another layer of security on top of your Windows password. Follow the steps below.

|   |                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------- |
|   | If you want to use Keyless passwordless mode and avoid entering your password, contact your IT administrator. |

1. Enter your user password on the Windows lock screen and click **Sign in**.

2. You receive a push notification on your mobile phone. Clicking the notification opens the Keyless application.

3. Confirm your login attempt by clicking **Approve** in the login request screen.

4. Authenticate by looking straight into your phone camera.

[Authenticate with Keyless after password authentication](https://www.youtube.com/watch?v=HljvRZ6Tgrs\&list=PLRsOuKOiF3Rr1ATX5aDhHsBDDnLUt_PAi\&index=6)

### Offline mode

Offline mode enables you to perform a workstation login when there is no internet connection. It is up to you when to enable and disable offline login.

#### Enabling offline mode

|   |                                                                             |
| - | --------------------------------------------------------------------------- |
|   | All users can enable and disable offline mode without escalated privileges. |

Enabling and disabling offline mode is done through the Keyless tray application in the tray bar:

![Keyless tray application](_images/keyless-tray-application.png)

By default, offline mode is enabled for all users on the specified workstation. To enable offline mode, click the Keyless tray icon and select **Enable Offline Access**.

![Enable offline access](_images/enable-offline-access.png)

**To ensure maximum security, once enabled, Offline Mode is available for at most 7 days and 10 login attempts.** Once either limit is reached, offline mode is automatically disabled and users need to re-enable offline mode or use standard online login.

|   |                                                                                        |
| - | -------------------------------------------------------------------------------------- |
|   | Each successful online login resets the counters back to 7 days and 10 login attempts. |

|   |                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------- |
|   | If you want to change the default values of 7 days and 10 login attempts, contact Keyless customer support. |

A user can view current offline access status by clicking **Show Status** from the Keyless tray app:

![Show status option](_images/show-status-option.png)![Offline status details](_images/offline-status-details.png)

* **Offline Status**: Enabled or Disabled

* **Offline Sessions Remaining**: Number of consecutive offline logins left for the user on the workstation; resets on a successful online login.

* **Offline Time Remaining**: Amount of time left for the user on the workstation for offline access; resets on a successful online login.

#### Authenticating when offline

After enabling offline mode, follow these steps to log in when offline.

1. From the Windows lock screen, select the **Offline Login** checkbox (if you are using Password + Keyless mode, first enter your password).

2. Scan the QR code with your Keyless mobile app by clicking the QR code image next to the account name inside the Keyless app.

3. Scan the QR code using the Keyless app. This generates an 8-digit one-time passcode.

4. Enter the 8-digit passcode into the password input box on your workstation.

![QR code image in the Keyless app](_images/IMG_1156.jpg)

[Enable and authenticate with Offline Mode](https://www.youtube.com/watch?v=gX4fbHdlNuo\&list=PLRsOuKOiF3Rr1ATX5aDhHsBDDnLUt_PAi\&index=7)

## RDP authentication

Keyless authentication is used for RDP sessions into all workstations that have the Keyless Workforce Access Client installed.

|   |                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------- |
|   | Keyless authentication is used only for users who are not excluded from Keyless for the specific workstation. |

### Step-by-step guide

1. Using the Remote Desktop Protocol application on your workstation, or using the command line, initiate an RDP session for a Keyless-enabled user to a Keyless-enabled workstation:

   ```shell
   mstsc /v:<your-ip-address>
   # Example: mstsc /v:10.20.30.01
   ```

   ![RDP connection dialog](_images/rdp-connection-dialog.png)![RDP sign-in screen](_images/rdp-sign-in-screen.png)

2. Once connected, you're prompted to authenticate on your mobile device.

   ![Authentication prompt](_images/authentication-prompt.png)

3. Authenticate on your device:

   ![Authenticate on device](_images/authenticate-on-device.gif)

4. Access the workstation:

   ![Workstation access](_images/workstation-access.png)

---

---
title: Delete account
description: Delete your Keyless Authenticator account.
component: recognize
page_id: recognize:user-guide:user-guide-delete-account
canonical_url: https://docs.pingidentity.com/recognize/user-guide/user-guide-delete-account.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  step-1-open-keyless-authenticator-settings: "Step 1: Open Keyless Authenticator settings"
  step-2-tap-delete-keyless-data: "Step 2: Tap Delete Keyless Data"
  step-3-authenticate: "Step 3: Authenticate"
---

# Delete account

You can delete your Keyless Authenticator account at any time. Deleting your account removes your linked accounts from the app. However, you will not be able to authenticate to those accounts if Keyless Authenticator is required for access.

|   |                                                                                     |
| - | ----------------------------------------------------------------------------------- |
|   | Check with your IT administrator for any linked accounts before deleting your data. |

## Step 1: Open Keyless Authenticator settings

Tap the gear button on the main screen to open the Keyless Authenticator settings panel.

![Open settings](_images/open-settings.png)

## Step 2: Tap Delete Keyless Data

To delete your Keyless data, tap the red **Delete Keyless Data** button at the bottom.

![Delete Keyless data](_images/delete-data.PNG)

## Step 3: Authenticate

Keyless Authenticator asks you to confirm by authenticating with your face. To complete this process, make sure your face is not covered by your hair, a mask, or a hat.

![Authenticate to confirm deletion](_images/authenticate-confirm-delete.png)

---

---
title: Enable backup
description: Enable backup to recover your account if you lose access to your device or reinstall the Keyless app.
component: recognize
page_id: recognize:user-guide:user-guide-enable-backup
canonical_url: https://docs.pingidentity.com/recognize/user-guide/user-guide-enable-backup.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  ios: iOS
  android: Android
---

# Enable backup

Backups allow you to recover your account in case:

* You lose access to your device.

* You reinstall the Keyless app.

To enable the backup functionality, make sure you have the most updated Keyless App from the App Store and follow the steps below.

## iOS

Make sure that iCloud Drive is enabled on your device and you have enough space to perform the backup (at least 1 MB):

1. Go to **Settings** > **\[Your Name]** > **iCloud** and make sure **iCloud Drive** is enabled.

2. Open the Keyless app and click the gear icon in the top right corner to go to **Settings**.

3. Check **Enable Backups** and wait a few seconds for the operation to complete.

![Enable backups from the Settings menu](_images/enable-backups-settings.PNG)

## Android

Make sure you have enough space on Google Drive to perform a backup (at least 1 MB).

1. Open the Keyless app and click the gear icon in the top right corner to go to **Settings**.

2. Check **Enable Backups** and wait a few seconds for the operation to complete.

---

---
title: Install the mobile app
description: Download and install the app on your iPhone or Android device.
component: recognize
page_id: recognize:user-guide:user-guide-install-mobile-app
canonical_url: https://docs.pingidentity.com/recognize/user-guide/user-guide-install-mobile-app.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Install the mobile app

The Keyless Authenticator is available for download from the [Apple App Store](https://apps.apple.com/us/app/keyless-authenticator/id1494269968) and the [Google Play Store](https://play.google.com/store/apps/details?id=io.keyless.push).

|   |                                                                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The Keyless Authenticator is available **only in the European and US App Store and Google Play Store**. If your account is associated with a different region, you can change it using [the troubleshooting guide](user-guide-troubleshooting.html). |

|   |                                                                                             |
| - | ------------------------------------------------------------------------------------------- |
|   | The Keyless Authenticator app does not support Huawei devices without Google Play Services. |

---

---
title: Troubleshooting
description: How to troubleshoot common issues.
component: recognize
page_id: recognize:user-guide:user-guide-troubleshooting
canonical_url: https://docs.pingidentity.com/recognize/user-guide/user-guide-troubleshooting.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  app-installation: App installation
  enrollment-and-authentication-issues: Enrollment and authentication issues
  qr-scanning-issues: QR scanning issues
  ios-troubleshooting: iOS troubleshooting
  enrollment: Enrollment
  force-quit-keyless-authenticator: Force-quit Keyless Authenticator
  restart-your-device: Restart your device
  reinstall-keyless-authenticator: Reinstall Keyless Authenticator
  authentication: Authentication
  force-quit-keyless-authenticator-2: Force-quit Keyless Authenticator
  restart-your-device-2: Restart your device
  delete-linked-account: Delete linked account
  reinstall-keyless-authenticator-2: Reinstall Keyless Authenticator
  android-troubleshooting: Android troubleshooting
  enrollment-2: Enrollment
  force-quit-keyless-authenticator-3: Force-quit Keyless Authenticator
  restart-your-device-3: Restart your device
  reinstall-keyless-authenticator-3: Reinstall Keyless Authenticator
  authentication-2: Authentication
  force-quit-keyless-authenticator-4: Force-quit Keyless Authenticator
  restart-your-device-4: Restart your device
  reinstall-keyless-authenticator-4: Reinstall Keyless Authenticator
---

# Troubleshooting

## App installation

|   |                                                                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Make sure you're running the latest version of Keyless Authenticator by visiting the [Apple App Store](https://apps.apple.com/us/app/keyless-authenticator/id1494269968) or the [Google Play Store](https://play.google.com/store/apps/details?id=io.keyless.push) on your smartphone. |

If you can't install the app, make sure your smartphone is updated to the latest operating system version supported by your device. Keyless Authenticator requires:

* iOS version 13.4.1 or newer

* Android version 6 (API level 23)

At the moment, the Keyless Authenticator app is available **only in the European and US App Store and Google Play Store**. If your account is associated with a different region, you can change it using the following guides:

* [Apple Store: Change your Apple ID country or region](https://support.apple.com/en-us/HT201389)

* [Google Play Store: Change your Google Play country](https://support.google.com/googleplay/answer/7431675?hl=en)

## Enrollment and authentication issues

If you can't enroll or authenticate, make sure:

* **The Keyless Authenticator can see your face.** Your face should be completely contained within the on-screen preview during enrollment and authentication, and shouldn't be covered by your hair, a scarf, or a hat. Make sure there's enough light in the room for your camera to see your face.

* **Your smartphone is connected to the internet.** Keyless Authenticator requires a reliable internet connection to authenticate to online services.

* **You're using a supported operating system and web browser.**

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Keyless supports the following browsers:* **Chrome** 65 or later (Windows 8 or later, MacOS 10.12 (Sierra) or later, or Ubuntu Linux 18.04 or later)

* **Firefox** 55 or later (Windows 8 or later, MacOS 10.12 (Sierra) or later, or Ubuntu Linux 18.04 or later)

* **Safari** 11 or later (Mac OS 10.12 or later)

* **Microsoft Edge** 75 or later (Windows 10)

* **Microsoft Internet Explorer** 11 (Windows 8 or later)

* **Chrome** 78 or later (Android 7 or later)

* **Safari** 12 or later (iOS 12.4 or later) |

If the problem persists, unlink your device and add it again to your external account.

## QR scanning issues

If the Keyless Authenticator can't scan the QR code, make sure:

* The camera on the back of your smartphone is facing the QR code

* The QR code covers the entire square frame on the smartphone screen when the QR code scanner is open

* The smartphone and QR code are not moving or shaking

* There aren't any other windows on screen partially covering the QR code

* You're scanning the QR code using Keyless Authenticator, rather than your smartphone's default camera app or a different QR scanner

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | If the problem persists, see platform-specific help for iOS and Android, and contact us at <https://support.keyless.io>. |

## iOS troubleshooting

This section lists common ways to address enrollment and authentication failure scenarios on iOS. If Keyless Authenticator is not working as expected, follow the procedures below. After each procedure, try Keyless Authenticator again to see whether the issue is resolved.

Always make sure you're running the latest version of Keyless Authenticator by visiting the [App Store](https://apps.apple.com/us/app/keyless-authenticator/id1494269968) on your smartphone.

### Enrollment

#### Force-quit Keyless Authenticator

1. Swipe up from the bottom of the screen and hold.

2. Swipe up on the Keyless Authenticator card to flick it off the screen.

[Watch the force-quit tutorial](https://youtu.be/DuuPSZsQ5Ok)

#### Restart your device

1. Press and hold either **Volume Up** or **Volume Down** and the **Side** button for a few seconds.

2. Drag the slider to the right, then wait 30 seconds for your device to turn off.

3. Turn your device back on by pressing and holding the side button until you see the Apple logo.

[Watch the device restart tutorial](https://youtu.be/-9zVJ9G-6t4)

#### Reinstall Keyless Authenticator

1. Touch and hold the Keyless Authenticator app.

2. Tap **Delete App**.

3. Tap **Delete**.

4. Reinstall Keyless Authenticator from the [App Store](https://apps.apple.com/us/app/keyless-authenticator/id1494269968).

[Watch the reinstall tutorial](https://youtu.be/97_5qVpEqlE)

### Authentication

#### Force-quit Keyless Authenticator

1. Swipe up from the bottom of the screen and hold.

2. Swipe up on the Keyless Authenticator card to flick it off the screen.

[Watch the force-quit tutorial](https://youtu.be/-9zVJ9G-6t4)

#### Restart your device

1. Press and hold either **Volume Up** or **Volume Down** and the **Side** button for a few seconds.

2. Drag the slider to the right, then wait 30 seconds for your device to turn off.

3. Turn your device back on by pressing and holding the side button until you see the Apple logo.

[Watch the device restart tutorial](https://youtu.be/-9zVJ9G-6t4)

#### Delete linked account

1. Open Keyless Authenticator.

2. Tap the account you want to delete, then swipe all the way to the left.

3. Authenticate to confirm account deletion.

[Watch the linked-account deletion tutorial](https://youtu.be/97_5qVpEqlE)

#### Reinstall Keyless Authenticator

1. Touch and hold the Keyless Authenticator app.

2. Tap **Delete App**.

3. Tap **Delete**.

4. Reinstall Keyless Authenticator from the [App Store](https://apps.apple.com/us/app/keyless-authenticator/id1494269968).

[Watch the reinstall tutorial](https://youtu.be/97_5qVpEqlE)

## Android troubleshooting

This section lists common ways to address enrollment and authentication failure scenarios on Android. If Keyless Authenticator is not working as expected, follow the procedures below. After each procedure, try Keyless Authenticator again to see whether the issue is resolved.

Always make sure you're running the latest version of Keyless Authenticator by visiting the [Google Play Store](https://play.google.com/store/apps/details?id=io.keyless.push) on your smartphone.

### Enrollment

#### Force-quit Keyless Authenticator

1. Long-press the Keyless Authenticator icon and tap **App info**.

2. Tap **Force stop** and confirm.

[Watch the force-quit tutorial](https://youtu.be/TgXtnhCgMqE)

#### Restart your device

1. Long-press the power button on the side or back of your device.

2. Tap **Restart** if available, or **Power off**.

3. If you tapped **Power off**, wait 30 seconds and then turn your device back on by pressing the power button.

[Watch the device restart tutorial](https://youtu.be/EvE1Wumo3MI)

#### Reinstall Keyless Authenticator

1. Long-press the Keyless Authenticator icon.

2. Tap **App info**.

3. Tap **Uninstall** and confirm.

4. Reinstall Keyless Authenticator from the [Google Play Store](https://play.google.com/store/apps/details?id=io.keyless.push).

[Watch the reinstall tutorial](https://youtu.be/GwmsyYdQBqo)

### Authentication

#### Force-quit Keyless Authenticator

1. Long-press the Keyless Authenticator icon and tap **App info**.

2. Tap **Force stop** and confirm.

[Watch the force-quit tutorial](https://youtu.be/TgXtnhCgMqE)

#### Restart your device

1. Long-press the power button on the side or back of your device.

2. Tap **Restart** if available, or **Power off**.

3. If you tapped **Power off**, wait 30 seconds and then turn your device back on by pressing the power button.

[Watch the device restart tutorial](https://youtu.be/EvE1Wumo3MI)

#### Reinstall Keyless Authenticator

1. Long-press the Keyless Authenticator icon.

2. Tap **App info**.

3. Tap **Uninstall** and confirm.

4. Reinstall Keyless Authenticator from the [Google Play Store](https://play.google.com/store/apps/details?id=io.keyless.push).

[Watch the reinstall tutorial](https://youtu.be/GwmsyYdQBqo)