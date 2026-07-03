---
title: Adding review statuses to your authentication policy
description: By modifying your PingFederate authentication policy to include the Result from Azure AD Identity Protection, you can dynamically change authentication requirements based on security risk level.
component: azure
page_id: azure:azure_ad_identity_protection_integration_kit:pf_azuread_identityprotection_ik_adding_review_statuses_to_your_authentication_policy
canonical_url: https://docs.pingidentity.com/integrations/azure/azure_ad_identity_protection_integration_kit/pf_azuread_identityprotection_ik_adding_review_statuses_to_your_authentication_policy.html
revdate: June 21, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding review statuses to your authentication policy

By modifying your PingFederate authentication policy to include the Result from Azure AD Identity Protection, you can dynamically change authentication requirements based on security risk level.

## About this task

These steps are designed to help you add to an existing authentication policy. Learn more general information about configuring authentication policies in [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation.

## Steps

1. In the PingFederate administrative console, go to the **Policies** tab.

   **Choose from:**

   * For PingFederate 10.1 or later: go to **Authentication > Policies > Policies**.

   * For PingFederate 10.0 or earlier: go to **Identity Provider > Authentication Policies > Policies**.

2. Select the **IdP Authentication Policies** check box.

3. Open an existing authentication policy, or click **Add Policy**.

   Learn more about [Defining authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_auth_policies.html) in the PingFederate documentation.

4. In the **Policy** area, select the Microsoft IdP Adapter instance that you created in [Setting up the Microsoft Login Integration Kit](pf_azuread_identityprotection_ik_setting_up_the_microsoft_cloud_identity_connector.html).

   ![A screenshot that shows the authentication policy with the Microsoft IdP Adapter being added](_images/hcd1634163847787.jpg)

5. In the **Success** branch following the Microsoft IdP Adapter instance, select your Azure AD Identity Protection IdP Adapter instance.

   ![](_images/ztk1633716788773.jpg)

6. Map the Microsoft user ID into the Azure AD Identity Protection IdP Adapter instance.

   ![A screenshot that shows the Incoming User ID dialog with the user identifier selected](_images/teb1634164728456.jpg)

   1. Under the Azure AD Identity Protection IdP Adapter instance, click **Options**.

   2. On the **Options** dialog, from the **Source** list, select your Microsoft IdP Adapter instance.

   3. From the **Attribute** list, select the **id**. Click **Done**.

7. Define policy paths based on the information provided by Azure AD Identity Protection:

   ![](_images/jlv1633717420587.jpg)

   1. Under the Azure AD Identity Protection IdP Adapter instance, click **Rules**.

   2. On the **Rules** dialog, from the Attribute Name list, select **userRiskLevel**.

   3. From the **Condition** list, select **equal to**.

   4. In the **Value** field, enter "low", "medium", or "high", or one of the utility values "none", "hidden", "unknownFutureValue", or "noRiskData". The "noRiskData" value is set by the adapter when it does not find risk data for the user.

   5. In the **Result** field, enter a name. This appears as a new policy path that branches from the Azure AD Identity Protection IdP Adapter.

   6. If you want to add more authentication paths, click **Add** and repeat steps b-e.

   7. **Optional:** Clear the **Default to success** checkbox.

   8. Click **Done**.

8. Configure each of the authentication paths.

   ![](_images/nxl1633717796856.jpg)

9. Click **Done**. In the **Policies** window, click **Save**.
