---
title: Adding review statuses to your authentication policy
description: By modifying your PingFederate authentication policy to include the review status from ThreatMetrix, you can dynamically change authentication requirements based on security risk level.
component: threatmetrix
page_id: threatmetrix:setup:pf_threatmetrix_ik_adding_review_statuses_to_your_authentication_policy
canonical_url: https://docs.pingidentity.com/integrations/threatmetrix/setup/pf_threatmetrix_ik_adding_review_statuses_to_your_authentication_policy.html
revdate: October 30, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding review statuses to your authentication policy

By modifying your PingFederate authentication policy to include the review status from ThreatMetrix, you can dynamically change authentication requirements based on security risk level.

## About this task

These steps are designed to help you add to an existing authentication policy. You can find general information about configuring authentication policies in [Defining authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_auth_policies.html) in the PingFederate documentation.

|   |                                                                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | ThreatMetrix automatically tunes its rules and policies based on user behavior. To accommodate an initial training period, we recommend allowing all transactions to succeed for a period of time, regardless of review status. |

## Steps

1. In the PingFederate admin console, go to **Authentication > Policies > Policies** and select the **IdP Authentication Policies** checkbox.

2. Open an existing authentication policy.

3. In the **Policy** section, select your ThreatMetrix IdP Adapter instance.

   ![Adding the adapter to the authentication policy.](_images/pf-threatmetrix-ik-adding-adapter-to-authn-policy.jpg)

4. Map the user ID into the ThreatMetrix IdP Adapter instance:

   ![A screenshot that shows the Incoming User ID modal with the user identifier selected.](_images/pf-threatmetrix-ik-incoming-user-id.jpg)

   1. Under the ThreatMetrix IdP Adapter instance, click **Options**.

   2. On the **Options** modal, in the **Source** list, select a previous authentication source that collects the user ID.

   3. In the **Attribute** list, select the user ID.

   4. Select the **User ID Authenticated** checkbox.

   5. Click **Done**.

5. Define policy paths based on the information provided by ThreatMetrix:

   ![Branching the authentication policy based on details from ThreatMetrix.](_images/pf-threatmetrix-ik-branching-authn-policy.jpg)

   1. Under the ThreatMetrix IdP Adapter instance, click **Rules**.

   2. On the **Rules** modal, in the **Attribute Name** list, select **reviewStatus**.

   3. In the **Condition** list, do one of the following:

      * For **reviewStatus**, select **equal to**.

      * For **reasonCode**, select **multi-value contains**.

   4. In the **Value** field, do one of the following:

      * For **reviewStatus**, enter `pass`, `review`, `challenge`, or `reject`.

      * For **reasonCode**, enter a ThreatMetrix reason code.

        |   |                                                                                                                                                                                                          |
        | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        |   | Reason codes reflect the policy or policies that ThreatMetrix used to determine the review status. In the ThreatMetrix admin console, set meaningful names for your policies and enter those names here. |

   5. In the **Result** field, enter a name.

      This appears as a new policy path that branches from the ThreatMetrix IdP Adapter.

   6. If you want to add more authentication paths, click **Add** and repeat steps b - e.

   7. (Optional) Clear the **Default to success** checkbox.

   8. Click **Done**.

6. Configure each of the authentication paths.

   |   |                                                                                                                                                                                                                                                                                                                                                    |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If ThreatMetrix is unreachable or returns an error, the **Failure mode** advanced setting assigns a default review status. As a result, the **Fail** outcome of the ThreatMetrix IdP Adapter instance isn't used.Learn more in [ThreatMetrix IdP Adapter settings reference](pf_threatmetrix_ik_threatmetrix_idp_adapter_settings_reference.html). |

   ![The complete authentication policy.](_images/pf-threatmetrix-ik-complete-authn-policy.jpg)

7. Click **Done**. On the **Policies** page, click **Save**.
