---
title: Adding Intune security posture results to your authentication policy
description: By modifying your PingFederate authentication policy to include the isManaged and isCompliant results from Intune, you can control access to resources based on the device's security posture.
component: intune
page_id: intune:setup:pf_intune_ik_adding_intune_security_posture_results_to_your_authentication_policy
canonical_url: https://docs.pingidentity.com/integrations/intune/setup/pf_intune_ik_adding_intune_security_posture_results_to_your_authentication_policy.html
revdate: March 5, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding Intune security posture results to your authentication policy

By modifying your PingFederate authentication policy to include the `isManaged` and `isCompliant` results from Intune, you can control access to resources based on the device's security posture.

## About this task

These steps are designed to help you add to an existing authentication policy. Learn more about configuring authentication policies in [Policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/qmq1564002987890.html) in the PingFederate documentation.

## Steps

1. Sign on to the PingFederate administrative console.

2. On the **Identity Provider** page, under **Authentication Policies**, click **Policies**.

3. Open an existing authentication policy, or create a new one. Learn more in [Defining authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_auth_policies.html) in the PingFederate documentation.

4. In the **Policy** area, in the **Select** list, select an Intune IdP Adapter instance.

   ![A screen capture of the fail and success paths for the HTML Form Adapter.](_images/jmc1588867003421.jpg)

5. Map the `deviceId` (shown as **CN**) or `userPrincipalName` from your X.509 Adapter instance into the Intune IdP Adapter instance.

   ![Screen capture of the Incoming User ID page, showing the userPrincipalName attribute mapped to X.509 adapter.](_images/syn1588867161010.jpg)

   1. Under the Intune IdP Adapter instance, click **Options**.

   2. On the **Options** dialog, from the **Source** list, select your X.509 Adapter instance.

   3. From the **Attribute** list, select **CN** or **userPrincipalName**. Click **Done**.

6. Define policy paths based on the two security posture attributes, `isCompliant` and `isManaged`.

   ![Screen capture of the Rules area. If the isCompliant attribute is equal to false, the result is notCompliant. If the isManaged attribute is equal to false, the result is notManaged.](_images/nlc1588867246179.jpg)

   1. Under the Intune IdP Adapter instance, click **Rules**.

   2. On the **Rules** dialog, in the **Attribute Name** list, select **isCompliant**.

   3. In the **Condition** list, select **equal to**.

   4. In the **Value** field, enter `true` or `false`.

   5. In the **Result** field, enter a name. This appears as a new policy path that branches from the authentication source.

   6. Repeat steps b - e for **isManaged**.

   7. Click **Done**.

7. Configure each of the authentication paths, including **Fail**, **Success**, and the paths that you defined in the **Rules** dialog.

   ![Screen capture of the Fail and Success paths for the HTML Form Adapter.](_images/atl1588867472580.jpg)

8. Click **Done**.

9. In the **Policies** window, click **Save**.
