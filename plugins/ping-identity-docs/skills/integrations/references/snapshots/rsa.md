---
title: Configuring an adapter instance
description: Configure the RSA SecurID IdP Adapter to determine how PingFederate communicates with the RSA Authentication Manager server.
component: rsa
page_id: rsa:rsa_securid_integration_kit:pf_rsa_securid_ik_configuring_an_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/rsa/rsa_securid_integration_kit/pf_rsa_securid_ik_configuring_an_adapter_instance.html
revdate: June 21, 2024
section_ids:
  steps: Steps
---

# Configuring an adapter instance

Configure the RSA SecurID IdP Adapter to determine how PingFederate communicates with the RSA Authentication Manager server.

## Steps

1. If you are upgrading from version 2.x of the integration kit, note the configuration details of your existing adapter instance, and then delete the adapter instance. Restore your configuration as you complete the steps below.

2. In the PingFederate administrative console, go to **Authentication > Integration > IdP Adapters**. Click **Create new Instance**.

3. On the **Type** tab, set the basic adapter instance attributes.

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. From the **Type** list, select **RSA SecurID IdP Adapter**. Click **Next**.

4. (Optional) On the **IdP Adapter** screen, configure additional RSA Authentication Manager servers to try, in order, in case the primary server fails to respond.

   1. In the **Failover Servers** section, click **Add a new row to 'Failover Servers'**.

   2. In the **RSA Base API URL** field, enter the complete URL and endpoint of the RSA Authentication Manager server.

   3. If you want to skip hostname verification to prevent errors, clear the **Verify HTTPS Hostname** checkbox.

   4. In the **Action** column, click **Update**.

   5. To add another property, repeat steps a - d.

5. On the **IdP Adapter** tab, configure the adapter instance by referring to [RSA SecurID IdP Adapter settings reference](pf_rsa_securid_ik_rsa_securid_idp_adapter_settings_reference.html). Click **Next**.

6. On the **Actions** screen, test your connection to the RSA Authentication API. Resolve any issues that are reported and then click **Next**.

7. On the **Extended Contract** tab, add any attributes that you want to include in the contract. Click **Next**.

8. On the **Adapter Attributes** tab, set pseudonym and masking options as shown in [Set pseudonym and masking options](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_pseudonym_masking_options.html) in the PingFederate documentation. Click **Next**.

9. On the **Adapter Contract Mapping** tab, configure the contract fulfillment details for the adapter as shown in [Define the IdP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_authnadapterinstancetasklet_plugincontractstate.html) in the PingFederate documentation. Click **Next**.

10. On the **Summary** tab, check and save your configuration. Click **Save**.

11. Create or modify a connection to the service provider using the RSA SecurID IdP Adapter instance. Learn more in [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html) in the PingFederate documentation.
