---
title: Adding device postures to your authentication policy
description: Create an authentication policy to pass the Workspace ONE device ID from the X.509 Certificate Adapter instance to the Workspace ONE IdP Adapter instance.
component: workspaceone-uem
page_id: workspaceone-uem:setup:pf_workspaceone_uem_ik_create_an_authentication_policy
canonical_url: https://docs.pingidentity.com/integrations/workspaceone-uem/setup/pf_workspaceone_uem_ik_create_an_authentication_policy.html
revdate: July 10, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding device postures to your authentication policy

Create an authentication policy to pass the Workspace ONE device ID from the X.509 Certificate Adapter instance to the Workspace ONE IdP Adapter instance.

## About this task

These steps are designed to help you add to an existing authentication policy. You can find general information about configuring authentication policies in [PingFederate Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation.

## Steps

1. In the PingFederate admin console, go to the **Policies** tab.

   * For PingFederate 10.1 or later, go to **Authentication > Policies > Policies**.

   * For PingFederate 10.0 or earlier, go to **Identity Provider > Authentication Policies > Policies**.

2. Select the **IdP Authentication Policies** checkbox.

3. Open an existing authentication policy, or click **Add Policy**.

   You can find help in [Defining authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_auth_policies.html) in the PingFederate documentation.

4. In the **Policy** area, in the **Select** list, select the X.509 Certificate Adapter instance that you created in [Create an X.509 Certificate Adapter instance](pf_workspaceone_uem_ik_create_an_x509_certificate_adapter_instance.html).

5. In the X.509 **Fail** section, configure the failure result.

6. In the X.509 **Success** section, select the Workspace ONE IdP Adapter instance that you created in [Configuring a Workspace ONE IdP Adapter instance](pf_workspaceone_uem_ik_configuring_a_workspace_one_idp_adapter_instance.html). Click **Options**.

7. On the **Incoming User ID** modal, in the **Source** list, select the X.509 Certificate Adapter instance.

8. In the **Attribute** list, select the attribute that you added to the extended contract of the X.509 Certificate Adapter instance. Click **Done**.

9. In the Workspace ONE IdP Adapter **Fail** section, configure the failure result.

10. In the Workspace ONE IdP Adapter **Success** section, select the policy contract that you created in [Create a policy contract](pf_workspaceone_uem_ik_create_a_policy_contract.html).

11. Click **Contract Mapping**.

12. On the **Contract Fulfillment** tab, in the **Source** list, select the X.509 Certificate Adapter instance.

13. In the **Value** list, select the attribute that contains the Workspace ONE device ID.

14. Click **Done**. In the **Policies** window, click **Save**.
