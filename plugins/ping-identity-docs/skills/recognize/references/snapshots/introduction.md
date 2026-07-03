---
title: Account recovery
description: This page explains the options customers have when using PingOne Recognize to support account recovery.
component: recognize
page_id: recognize:introduction:account_recovery
canonical_url: https://docs.pingidentity.com/recognize/introduction/account_recovery.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 15, 2026
section_ids:
  enroll-a-new-device-via-client-state: Enroll on a new device
  how-it-works: How it works
  managing-multiple-enrolled-devices: Managing multiple enrolled devices
  keyless-client-devices: PingOne Recognize Client Devices
---

# Account recovery

PingOne Recognize helps organizations recover accounts and enroll new devices when users lose access to their originally enrolled device. The account recovery and device enrollment flows use the PingOne Recognize Mobile SDK.

PingOne Recognize offers two services as part of a device or account recovery experience:

* [Enroll a new device](#enroll-a-new-device-via-client-state)

* [Managing multiple enrolled devices](#managing-multiple-enrolled-devices)

## Enroll on a new device

For customers who've already established trusted alternative second factors, such as passwords, SMS one-time passwords (OTPs), or email magic links, PingOne Recognize's face matching is typically used in combination with existing factors to enroll the new device.

### How it works

1. The user downloads the app on a new device, enters their username, and authenticates using a first factor (for example, password, SMS OTP, or email magic link).

2. Customers invoke the PingOne Recognize Mobile SDK, retrieve the PingOne Recognize ID associated with the user and the client state generated during enrollment, and send this to the SDK to enable secure account recovery.

3. The SDK recovery flow captures a selfie and authenticates that the originally enrolled user is genuinely present, without revealing or processing biometric data outside the user's device.

4. If successful, the new device is bound to the user's identity, enabling ongoing authentication for login, step-up, or payment use cases.

5. Optional: Users can review and [delete previously bound devices](#managing-multiple-enrolled-devices).

Learn more in [Account Recovery (Mobile SDK)](../mobile-sdk/mobile-sdk-account-recovery.html).

Learn more in [Retrieve and delete devices via API](https://docs.keyless.io/consumer/server-api/devices).

## Managing multiple enrolled devices

Customers can use the API to retrieve and delete devices bound to user identities. This allows users to have multiple devices and reduces risks associated with device loss.

Use GET and DELETE APIs to build a device management experience that allows users to:

* View and manage bound devices.

* Delete any listed device.

* Add a new device when needed.

Learn more in [GET and DELETE user devices](https://docs.keyless.io/consumer/server-api/devices)

Learn more in [Add user device](../mobile-sdk/mobile-sdk-account-recovery.html)

## PingOne Recognize Client Devices

For account recovery, PingOne Recognize Client Devices and Client States are relevant subsets of device entities. PingOne Recognize Client Devices represent user profiles containing non-PII data that allows a user to authenticate on a new device or channel (mobile or web apps).

Within this category, PingOne Recognize allows customers to generate a **Client State** during enrollment for device types before activation or binding for ongoing two-factor authentication. After binding, a new **SDK Device** is generated. Each device receives a DeviceID and can be one of the following types:

1. **Backup:** The **Client State** typically stored by the PingOne Recognize customer so a user can later authenticate on a new camera-enabled physical device. Generated through IDV Bridge or Live Enrollment and later used during account recovery.

2. **Temporary:** Similar to Backup, but recommended when the customer does not need to store the client state beyond the current flow, such as when enrollment is immediately followed by activation or binding.

3. **SDK:** Applied when a user profile has been activated through a mobile or web app to support ongoing authentication via the Mobile SDK. It contains additional keys and metadata to support device and facial authentication in a privacy-preserving manner.
