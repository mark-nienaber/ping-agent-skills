---
title: Adjusting the OIDC policy configuration
description: Adjust the OIDC policy configuration to include the access token manager (ATM) and attributes you've configured.
component: microsoft-eam
page_id: microsoft-eam:setup:pf_ms_eam_adjusting_the_oidc_policy_configuration
canonical_url: https://docs.pingidentity.com/integrations/microsoft-eam/setup/pf_ms_eam_adjusting_the_oidc_policy_configuration.html
revdate: September 17, 2025
section_ids:
  steps: Steps
---

# Adjusting the OIDC policy configuration

Adjust the OIDC policy configuration to include the access token manager (ATM) and attributes you've configured.

You can find more information in the [Configuring OpenID Connect policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configuring_oidc_policies.html) section of the PingFederate documentation.

## Steps

1. Go to **Applications > OpenID Connect Policy Management** and open the policy configuration you plan to use.

2. On the **Manage Policy** tab:

   1. Make sure that you've configured a unique **Policy ID** and **Name**.

   2. In the **Access Token Manager** list, select the ATM you configured in [Configuring an access token manager](pf_ms_eam_configuring_an_atm.html).

   3. Select the **Include x.509 Thumbprint Header in ID token** checkbox.

      This configures the OIDC policy to expose the X5T header when PingFederate issues the `id_token` for Microsoft Entra ID.

   You can find more configuration information in [configuring policy and ID token settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_policymanagementtasklet_policymanagementstate.html) in the PingFederate documentation.

3. On the **Attribute Contract** tab, make sure that the attribute contract includes `acr`, `amr`, and any optional attributes you configured into the issued id\_token:

   1. In the **Extend the Contract** section, enter `acr`.

   2. In the **Action** column, click **Add**.

   3. Repeat this process for `amr` and any optional attributes that you extended the contract for in step 4 of [Configuring an adapter instance](pf_ms_eam_configuring_an_adapter_instance.html).

   4. Click **Next**.

   You can find more information about configuration options in [Configuring the policy attribute contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_policymanagementtasklet_createpolicycontractstate.html) in the PingFederate documentation.

4. On the **Attribute Scopes** tab, make sure that the `acr` and `amr` attributes, plus any optional attributes, are returned with the `openid` scope:

   1. In the **Scope** list, select **openid**.

   2. In the **Attributes** section, select the checkboxes for `acr`, `amr`, and any optional attributes that you configured.

   3. In the **Action** column, click **Add**.

   4. Click **Next**.

   You can find more information about configuration options in [Configuring attribute scopes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_policymanagementtasklet_attributescopesstate.html) in the PingFederate documentation.

5. On the **Attribute Sources & User Lookup** tab, click **Next**.

6. On the **Contract Fulfillment** tab, fulfill the attribute contract for `acr`, `amr`, `sub`, and any optional attributes that you configured.

   For example, to configure contract fulfillment for the `acr` attribute:

   1. In the **Source** list, select **Access Token**.

   2. In the **Value** list, select **acr**.

   3. Repeat for `amr`, `sub`, and any optional attributes that you extended the contract for in step 4 of [Configuring an adapter instance](pf_ms_eam_configuring_an_adapter_instance.html).

      * For the `amr` attribute, in the **Source** list, select **Access Token**, and in the **Value** list, select **amr**.

      * For the `sub` attribute, in the **Source** list, select **Persistent Grant**, and in the **Value** list, select `USER_KEY`.

   4. Click **Next**.

   You can find more information about configuration options in [Configuring ID token fulfillment](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_policymanagementtasklet_policycontractmappingstate.html) in the PingFederate documentation.

7. (Optional) On the **Issuance Criteria** tab, configure the criteria for use with this OIDC policy.

   You can find more information about configuration options in [Defining issuance criteria for policy mapping](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_policymanagementtasklet_policyissuancecriteriastate.html) in the PingFederate documentation.

8. On the **Summary** tab, click **Save**.
