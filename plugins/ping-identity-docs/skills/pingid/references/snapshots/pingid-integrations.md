---
title: (Legacy) Configuring a PingFederate policy for passwordless authentication with a security key
description: For admins running PingFederate 13.0.0 or later with the PingID integration kit 2.30 and later, you can benefit from a more consistent passwordless authentication experience.
component: pingid
page_id: pingid:pingid_integrations:pid_configuring_pf_policy_for_passwordless_authentication_security_key
canonical_url: http://docs.pingidentity.com/pingid/pingid_integrations/pid_configuring_pf_policy_for_passwordless_authentication_security_key.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 18, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
---

# (Legacy) Configuring a PingFederate policy for passwordless authentication with a security key

|   |                                                                                                                                                                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For admins running PingFederate 13.0.0 or later with the PingID integration kit 2.30 and later, you can benefit from a more consistent passwordless authentication experience.Learn more in [Configuring a PingFederate policy for a consistent passwordless authentication experience](pid_configuring_pf_policy_for_passwordless_authentication.html). |

Configure a PingFederate policy for passwordless authentication with a security key.

## Before you begin

Before configuring PingID for passwordless authentication, make sure you do the following:

* In the PingID admin portal, [configure security key for passwordless authentication](../pingid_service_management/configuring_security_key_auth.html).

* Install [PingID Integration Kit](installing_the_pid_i_for_pf.html) 2.10 or later.

* Download the [PingID properties file](pid_pf.html).

* Configure an [HTML Form Adapter](https://support.pingidentity.com/s/document-item?bundleId=pingfederate-93\&topicId=xvy1564003022890.html) instance.

* For PingFederate 10.1 or earlier, optionally [customize the HTML Form Adapter](customizing_html_adapter_for_passwordless_auth_security_key.html) to:

  * Add a passwordless authentication flow icon for the HTML Form Adapter.

  * Only show the security key button when the browser supports WebAuthn.

  These options are automatically included in PingFederate 10.2 and later.

* [Configure a PingID Adapter](configuring_a_pid_adapter_instance.html) instance.

* Review the [(Legacy) Security key authentication requirements and limitations](../pingid_service_management/security_key_auth_requirements_and_limitations.html).

* (Optional) If you wish to configure the application name or application icon, do so in PingFederate. See [Identify the target application](http://docs.pingidentity.com/pingfederate/12.3/administrators_reference_guide/pf_identifying_target_application.html).

## About this task

To use a security key with PingID as a passwordless authentication solution for federated single sign-on (SSO) with PingFederate, in PingFederate you'll need to:

* Create an authentication policy contract.

* Create a local identity profile and associate it with the HTML Form Adapter instance.

* Create an authentication policy.

## Steps

1. In the PingFederate administrative console, create an authentication policy contract: (see also [Policy Contracts](https://support.pingidentity.com/s/document-item?bundleId=pingfederate-93\&topicId=aat1564002989773.html)).

   1. Got to Policy Contracts:

      * PingFederate 10.1 and higher: Click **Authentication → Policies**, and then click **Policy Contracts**.

      * PingFederate 10 and lower: In the **Identity Provider** tab, in the **Authentication Policies** area, click **Policy Contracts**.

   2. Click **Create New Contract**.

   3. In the**Contract Name** field, enter a name for the policy contract and click **Next**.

   4. In the **Contract Attributes** tab, for each attribute you want to add, in the **Extend the Contract** area, type the name of the attribute and then click **Add**. For a list of PingID attributes, see [PingID authentication attributes](pid_authentication_attributes.html).

   5. Click **Next**, and then click **Save**.

2. Create a local identity profile for passwordless authentication:

   1. Go to Local Identity Profiles:

      * PingFederate 10.1 and higher: Click **Authentication → Policies**, and then click **Local Identity Profiles**.

      * PingFederate 10 and lower: In the **Identity Provider** tab, click **Identity Profiles**.

   2. Click **Create New Profile**.

   3. In the**Profile Info** tab, enter the following information, and then click **Next**:

      * **Local Identity Profile Name**: enter a meaningful name for the profile.

      * **Authentication Policy Contract**: select your policy contract.

   4. In the **Authentication Sources** tab, in the **Authentication Source** field, enter **Security Key** as the name of your authentication source, click **Add**, and then click **Next**.

   5. In the **Summary** tab, click **Save** The local identity profile is saved.

3. Associate the HTML Adapter instance with the local identity profile:

   1. Go to IdP Adapters:

      * PingFederate 10.1 and higher: Click **Authentication**, and then click **IdP Adapters.**

      * PingFederate 10 and lower: In the **Security Identity Provider** tab, click **Adapters**.

   2. Click the **HTML Form Adapter**, and then click the **IdP Adapter** tab.

   3. Go to the **Local Identity Profile** field, and in the dropdown list select the local identity profile that you created.

   4. Click **Save**.

4. Create a PingFederate authentication policy for passwordless authentication using a security key: (see also [Policies](http://docs.pingidentity.com/pingfederate/12.3/administrators_reference_guide/qmq1564002987890.html)).

   1. Go to Policies:

      * PingFederate 10.1 and higher: Click **Authentication**, and then click **Policies**.

      * PingFederate 10 and lower: In the **Identity Provider** tab, under **Authentication Policies**, click **Policies**.

   2. In the **Policies** tab, ensure the **IdP Authentication Policies** check box is selected, and then click **Add Policy**.

   3. In the **Name** field, enter a meaningful name for the authentication policy.

   4. In the **Policy** dropdown, select **IdP Adapters** and then select the **HTML Form Adapter**. A branch for the **HTML form Adapter** is added to the PingFederate policy tree, and **FAIL**/**SUCCESS** fields are added.

   5. Directly under the **HTML form Adapter** field, click **Rules** and in the **Rules** popup window enter the following information, and then click **Done**:

      * **Attribute Name**: Select **policy.action**.

      * **Condition**: Select **equal to (case insensitive)**.

      * **Value**: Type **Security Key** as your authentication source.

      * **Result**: Type **Security Key** as your authentication source.

      * Select the **Default to success** check box.

        A Security Key branch is added to the PingFederate policy tree.

   6. In the **HTML Form Adapter** branch **FAIL** field, click **Done**.

   7. In the **HTML Form Adapter** branch **Security Key** field dropdown list, select **IdP Adapters**, and then select the PingID Adapter. **SUCCESS** and **FAIL** fields are added to the Security Key branch.

      1. Under the Security Key branch **FAIL** field, click **Done**.

      2. In the Security branch **SUCCESS** field list select the endpoint you require. For example:

         * **Policy Contracts**: Select the policy contract you created earlier and complete the relevant mapping (see [Configuring contract mapping](http://docs.pingidentity.com/pingfederate/12.3/administrators_reference_guide/pf_configuring_contract_mapping.html)).

         * **Local Identity Profiles**: Select the Local Identity Profile you created earlier and then complete the relevant mapping (see [Configuring local identity mapping](https://support.pingidentity.com/s/document-item?bundleId=pingfederate-93\&topicId=waw1564002988686.html)).

   8. In the **HTML Form Adapter** branch **SUCCESS** field dropdown list, select the action that you want to apply and configure it appropriately. For example:

      * If configuring the PingID Adapter (recommended), do the following:

        1. In the **SUCCESS** branch dropdown list, select **IdP Adapters** and then select **PingID Adapter**. **SUCCESS** and **FAIL** fields are added to the branch.

        2. Under the PingID Adapter **FAIL** field, click **Done**.

        3. In the PingID Adapter **SUCCESS** field, select the local identity profile you created earlier.

        4. Under the local identity profile click **Local Identity Mapping** and complete the relevant mapping with the PingID Adapter (see also [Configuring contract mapping](http://docs.pingidentity.com/pingfederate/12.3/administrators_reference_guide/pf_configuring_contract_mapping.html)).

           |   |                                                                                                                                                                   |
           | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
           |   | For a list of attributes that can be used upon successful authentication with PingID, see [PingID authentication attributes](pid_authentication_attributes.html). |

        5. Under the **PingID Adapter** entry, click **Options** and specify the following fields:

           * **Source**: HTML Form Adapter

           * **Attribute**: Username

      * If configuring a local identity profile:

        1. In the **SUCCESS** branch dropdown list, select the **Local Identity Profiles**, and then select the local identity profile that you created earlier.

        2. Directly under the **HTML Form Adapter** branch **SUCCESS** field click **Local Identity Mapping**, complete the relevant mapping from your source to the local identity contract, (see [Configuring local identity mapping](https://support.pingidentity.com/s/document-item?bundleId=pingfederate-93\&topicId=waw1564002988686.html)), and then click **Done**.

5. Save the PingFederate policy.

6. Add any further configurations, for example:

   * Browser SSO: [Configure IdP Browser SSO](https://support.pingidentity.com/s/document-item?bundleId=pingfederate-93\&topicId=ikb1564003000542.html).

   * OAuth: [OAuth configuration](https://support.pingidentity.com/s/document-item?bundleId=pingfederate-93\&topicId=zlc1564002990614.html).
