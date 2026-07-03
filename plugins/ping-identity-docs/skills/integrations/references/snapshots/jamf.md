---
title: Adding Jamf security posture results to your authentication policy
description: By modifying your PingFederate authentication policy to include the isManaged or isMDMCapable results from Jamf Pro, you can control access to resources dynamically based on the device's security posture.
component: jamf
page_id: jamf:setup:pf_jamf_ik_adding_jamf_security_posture_results_to_your_authentication_policy
canonical_url: https://docs.pingidentity.com/integrations/jamf/setup/pf_jamf_ik_adding_jamf_security_posture_results_to_your_authentication_policy.html
revdate: November 4, 2025
section_ids:
  steps: Steps
---

# Adding Jamf security posture results to your authentication policy

By modifying your PingFederate authentication policy to include the `isManaged` or `isMDMCapable` results from Jamf Pro, you can control access to resources dynamically based on the device's security posture.

These steps are intended to help you add to an existing authentication policy. You can find general information about configuring authentication policies in [Defining authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_auth_policies.html) in the PingFederate documentation.

## Steps

1. In the PingFederate admin console, go to **Authentication > Policies > Policies**.

2. Select the **IdP Authentication Policies** checkbox.

3. Open an existing authentication policy.

4. In the **Policy** area, in the **Select** list, select a Jamf IdP Adapter instance.

   ![Adding the Jamf IdP Adapter to the authentication policy.](_images/pf-jamf-ik-adding-the-adapter-to-the-authn-policy.jpg)

5. Map the attribute that contains the device identifier (shown here as **SerialNumber**) from your X.509 Certificate IdP Adapter instance into the Jamf IdP Adapter instance.

   ![Passing the user ID from the first-factor authentication adapter.](_images/pf-jamf-ik-passing-the-user-id.jpg)

   1. Under the Jamf IdP Adapter instance, click **Options**.

   2. On the **Options** modal, in the **Source** list, select your X.509 Certificate IdP Adapter instance.

   3. In the **Attribute** list, select an attribute that matches the **Device Identifier** you selected in your adapter configuration. Click **Done**.

6. Define policy paths based on the security posture attribute `isCompliant`.

   ![Branching the authentication policy based on the device's security posture.](_images/pf-jamf-ik-branching-the-authn-policy.jpg)

   1. Under the Jamf IdP Adapter instance, click **Rules**.

   2. On the **Rules** modal, in the **Attribute Name** list, select `isCompliant`.

   3. In the **Condition** list, select **equal to**.

   4. In the **Value** field, enter `true` or `false`.

   5. In the **Result** field, enter a name.

      This appears as a new policy path that branches from the authentication source.

   6. (Optional) Repeat steps a - e for `isMDMCapable` or any attributes that you mapped in the **Jamf API Attribute Mappings** table in the adapter configuration.

   7. (Optional) Clear the **Default to success** checkbox to ensure the authentication flow follows one of the paths you defined.

   8. Click **Done**.

7. Configure each of the authentication paths.

   ![The complete authentication policy.](_images/pf-jamf-ik-example-authn-policy.jpg)

8. Click **Done**.

9. In the **Policies** window, click **Save**.
