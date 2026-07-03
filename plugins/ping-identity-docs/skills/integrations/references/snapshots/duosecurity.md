---
title: Adding Duo Security to your authentication policy
description: By modifying your PingFederate authentication policy to include the Duo Security IdP Adapter, you can challenge users to complete a multi-factor authentication (MFA) step.
component: duosecurity
page_id: duosecurity:duo_security_integration_kit_22:pf_duo_security_ik_22_adding_duo_security_to_your_authentication_policy
canonical_url: https://docs.pingidentity.com/integrations/duosecurity/duo_security_integration_kit_22/pf_duo_security_ik_22_adding_duo_security_to_your_authentication_policy.html
revdate: June 7, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Adding Duo Security to your authentication policy

By modifying your PingFederate authentication policy to include the Duo Security IdP Adapter, you can challenge users to complete a multi-factor authentication (MFA) step.

## About this task

These steps are designed to help you add to an existing authentication policy. You can find general information about configuring authentication policies in [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html) in the PingFederate documentation.

## Steps

1. In the PingFederate administrative console, go to the **Policies** tab.

   ### Choose from:

   * For PingFederate 10.1 or later: go to **Authentication > Policies > Policies**.

   * For PingFederate 10.0 or earlier: go to **Identity Provider > Authentication Policies > Policies**.

2. Select the **IdP Authentication Policies** check box.

3. Open an existing authentication policy, or click **Add Policy**. Learn more in [Defining authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_auth_policies.html) in the PingFederate documentation.

4. In the **Policy** area, from the **Select** list, select a Duo Security IdP Adapter instance.

5. Map the Duo Security user ID or username into the Duo Security IdP Adapter instance.

   1. Under the Duo Security IdP Adapter instance, click **Options**.

   2. On the **Options** dialog, from the **Source** list, select a previous authentication source that collects the Duo Security user ID or username.

   3. From the **Attribute** list, select the user ID. Click **Done**.

6. Configure each of the authentication paths.

   ![puc1579651708651](../_images/puc1579651708651.jpg)

7. Click **Done**.

8. In the **Policies** window, click **Save**.
