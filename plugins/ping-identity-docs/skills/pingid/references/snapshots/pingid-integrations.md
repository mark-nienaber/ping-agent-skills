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

---

---
title: (Legacy) Configuring a PingFederate policy for passwordless authentication with FIDO biometrics
description: For admins running PingFederate 13.0.0 or later with the PingID integration kit 2.30 and later, you can benefit from a more consistent passwordless authentication experience.
component: pingid
page_id: pingid:pingid_integrations:pid_configuring_pf_policy_for_passwordless_authentication_fido_biometrics
canonical_url: http://docs.pingidentity.com/pingid/pingid_integrations/pid_configuring_pf_policy_for_passwordless_authentication_fido_biometrics.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 18, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
---

# (Legacy) Configuring a PingFederate policy for passwordless authentication with FIDO biometrics

|   |                                                                                                                                                                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For admins running PingFederate 13.0.0 or later with the PingID integration kit 2.30 and later, you can benefit from a more consistent passwordless authentication experience.Learn more in [Configuring a PingFederate policy for a consistent passwordless authentication experience](pid_configuring_pf_policy_for_passwordless_authentication.html). |

Configure a PingFederate policy for passwordless authentication with FIDO biometrics.

## Before you begin

Before configuring PingID for passwordless authentication, make sure you:

* Install the [PingID Integration Kit](installing_the_pid_i_for_pf.html) 2.7 or later.

* Download the [PingID properties file](pid_pf.html).

* Configure an [HTML Form Adapter](https://support.pingidentity.com/s/document-item?bundleId=pingfederate-93\&topicId=xvy1564003022890.html) instance.

* [Configure a PingID Adapter](configuring_a_pid_adapter_instance.html) instance.

* (Optional) If you wish to configure the application name or application icon, do so in PingFederate. See [Identify the target application](http://docs.pingidentity.com/pingfederate/12.3/administrators_reference_guide/pf_identifying_target_application.html).

* Review the [(Legacy) FIDO2 biometrics authentication requirements and limitations](../pingid_service_management/fido2_biometrics_auth_requirements_and_limitations.html).

## About this task

To use PingID as a passwordless authentication solution for federated single sign-on (SSO) with PingFederate, in PingFederate you'll need to:

* Create an authentication policy contract.

* Create a local identity profile and associate it with the HTML Form Adapter instance.

* Create an authentication policy.

## Steps

1. In PingFederate, create an authentication policy contract: (see also [Policy Contracts](https://support.pingidentity.com/s/document-item?bundleId=pingfederate-93\&topicId=aat1564002989773.html)).

   1. In the **Identity Provider** tab, under **AUTHENTICATION POLICIES** area, click **Policy Contracts**.

   2. Click **Create New Contract**.

   3. In the**Contract Name** field, enter a name for the policy contract and click **Next**.

   4. In the **Contract Attributes** tab, for each attribute you want to add, in the **Extend the Contract** area, type the name of the attribute and then click **Add**. For a list of PingID attributes, see [PingID authentication attributes](pid_authentication_attributes.html).

   5. Click **Next**, and then click **Done**.

2. Create a local identity profile for passwordless authentication:

   1. In the **Identity Provider** tab, click **Identity Profiles** and then click**Create New Profile**.

   2. In the **Profile Info** tab, enter the following information, and then click **Next**:

      * **Local Identity Profile Name**: Enter a meaningful name for the profile.

      * **Authentication Policy Contract**: Select your policy contract.

   3. In the**Authentication Sources** tab, in the **Authentication Source** field, enter **FIDO** as the name of your authentication source, click **Add**, and then click **Next**.

   4. Click **Done**, and then click **Save**. The local identity profile is saved.

3. In the **Identity Provider** tab, associate the HTML Form Adapter instance with the local identity profile:

   1. Click **Adapters**.

   2. Click the**HTML Form Adapter** and then click the **IdP Adapter** tab.

   3. Scroll down, and in the **Local Identity Profile** field, select the local identity profile that you created. Then click **Done**, and **Save**.

4. Create a PingFederate authentication policy for passwordless authentication. (See also [Policies](http://docs.pingidentity.com/pingfederate/12.3/administrators_reference_guide/qmq1564002987890.html).)

   1. In the **Identity Provider** tab, under **Authentication Policies**, click **Policies**.

   2. In the **Policies** tab, ensure the **IdP Authentication Policies** checkbox is selected, and then click **Add Policy**.

   3. In the **Name** field, enter a meaningful name for the authentication policy.

   4. In the **Policy** dropdown, select **IdP Adapters**, and then select the **HTML Form Adapter**. A branch for the **HTML Form Adapter** is added to the PingFederate policy tree, and **FAIL**/**SUCCESS** fields are added.

   5. Directly under the **HTML Form Adapter** field, click **Rules**. In the **Rules** popup window, enter the following information, and then click **Done**:

      * **Attribute Name**: Select **policy.action**.

      * **Condition**: Select **equal to**.

      * **Value**: Enter **FIDO** as your authentication source.

      * **Result**: Enter **FIDO** as your authentication source.

      * **Default to success**: Ensure the checkbox is selected.

   6. In the **HTML Form Adapter** branch **FAIL** field, click **Done**.

   7. In the **HTML Form Adapter** branch **SUCCESS** field dropdown list, select the action that you want to apply and configure it appropriately. For example:

      * If configuring the PingID Adapter (recommended), do the following:

        1. In the **SUCCESS** branch dropdown list, select **IdP Adapters**, and then select **PingID Adapter**. **SUCCESS**/**FAIL** fields are added to the branch.

        2. Under the PingID Adapter **FAIL** field, click **Done**.

        3. In the PingID Adapter **SUCCESS** field, select the local identity profile you created earlier.

        4. Under the local identity profile, click **Local Identity Mapping** and complete the relevant mapping. (See also [Configuring contract mapping](http://docs.pingidentity.com/pingfederate/12.3/administrators_reference_guide/pf_configuring_contract_mapping.html).)

           |   |                                                                                                                                                                   |
           | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
           |   | For a list of attributes that can be used upon successful authentication with PingID, see [PingID authentication attributes](pid_authentication_attributes.html). |

        5. Under the **PingID Adapter** entry, click **Options** and specify the following fields:

           * **Source**: HTML Form Adapter

           * **Attribute**: Username

      * If configuring a local identity profile:

        1. In the **SUCCESS** branch dropdown list, select the **Local Identity Profiles**, and then select the local identity profile that you created earlier.

        2. Directly under the **HTML Form Adapter** branch **SUCCESS** field, click **Local Identity Mapping**, complete the relevant mapping from your source to the local identity contract (see [Configuring local identity mapping](https://support.pingidentity.com/s/document-item?bundleId=pingfederate-93\&topicId=waw1564002988686.html)) and click **Done**.

           The **FIDO** policy branch is added to the policy tree.

   8. In the **FIDO** branch:

      1. In the dropdown list, select **IdP Adapters**, and then select the **PingID Adapter**. **SUCCESS**/**FAIL** fields are added.

      2. In the **FAIL** field, click **Done**.

      3. In the **SUCCESS** field dropdown list, select the endpoint you require. For example:

         * **Policy Contracts**: Select the policy contract you created earlier and complete the relevant mapping. (See [Policy Contracts](https://support.pingidentity.com/s/document-item?bundleId=pingfederate-93\&topicId=aat1564002989773.html).)

         * **Local Identity Profiles**: Select the Local Identity profile you created earlier and then complete the relevant mapping. (See [Configuring local identity mapping](https://support.pingidentity.com/s/document-item?bundleId=pingfederate-93\&topicId=waw1564002988686.html).)

5. Save the PingFederate policy.

6. Add any further configurations, for example:

   * Browser SSO: [Configure IdP Browser SSO](https://support.pingidentity.com/s/document-item?bundleId=pingfederate-93\&topicId=ikb1564003000542.html)

   * OAuth: [OAuth configuration](https://support.pingidentity.com/s/document-item?bundleId=pingfederate-93\&topicId=zlc1564002990614.html)

7. To complete the passwordless configuration, see [(Legacy) Configuring FIDO2 passwordless authentication](../pingid_service_management/pid_configuring_fido2_passwordless_auth.html).

---

---
title: (Legacy) Configuring a PingFederate policy for passwordless authentication with FIDO2 passkeys
description: For admins running PingFederate 13.0.0 or later with the PingID integration kit 2.30 and later, you can benefit from a more consistent passwordless authentication experience. Learn more in Configuring a PingFederate policy for a consistent passwordless authentication experience.
component: pingid
page_id: pingid:pingid_integrations:pid_configuring_pf_policy_for_passwordless_authentication_fido2_passkeys
canonical_url: http://docs.pingidentity.com/pingid/pingid_integrations/pid_configuring_pf_policy_for_passwordless_authentication_fido2_passkeys.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 26, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
---

# (Legacy) Configuring a PingFederate policy for passwordless authentication with FIDO2 passkeys

|   |                                                                                                                                                                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For admins running PingFederate 13.0.0 or later with the PingID integration kit 2.30 and later, you can benefit from a more consistent passwordless authentication experience. Learn more in [Configuring a PingFederate policy for a consistent passwordless authentication experience](pid_configuring_pf_policy_for_passwordless_authentication.html). |

Configure a PingFederate policy for passwordless authentication with FIDO2 passkeys.

## Before you begin

Before configuring PingID for passwordless authentication, make sure you:

* Install the [PingID Integration Kit](installing_the_pid_i_for_pf.html) 2.7 or later.

* Download the [PingID properties file](pid_pf.html).

* Configure an [HTML Form Adapter](http://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_config_html_form_adapt_instance.html) instance.

* [Configure a PingID Adapter](configuring_a_pid_adapter_instance.html) instance.

* (Optional) If you want to configure the application name or application icon, do so in PingFederate. Learn more in [Identify the target application](http://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_identifying_target_application.html).

* Review the [FIDO2 authentication requirements and limitations](../pingid_service_management/fido2_auth_requirements_and_limitations.html).

|   |                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The default policy's handling of null chain attributes optimizes the user authentication process by avoiding redundant LDAP queries and continuing straight to the PPM request stage. Therefore, the use of chained attributes isn't permitted. |

## About this task

To use PingID as a passwordless authentication solution for federated single sign-on (SSO) with PingFederate, in PingFederate you'll need to:

* Create an authentication policy contract.

* Create a local identity profile and associate it with the HTML Form Adapter instance.

* Create an authentication policy.

## Steps

1. Create a PingFederate authentication policy for passwordless authentication using a security key: (learn more in [Policies](http://docs.pingidentity.com/pingfederate/12.3/administrators_reference_guide/qmq1564002987890.html)).

   1. Go to Policies:

      * PingFederate 10.1 and later: Click **Authentication**, and then click **Policies**.

      * PingFederate 10 and earlier: In the**Identity Provider** tab, under **Authentication Policies**, click **Policies**.

   2. In the **Policies** tab, ensure the **IdP Authentication Policies** checkbox is selected, and then click **Add Policy**.

   3. In the **Name** field, enter a meaningful name for the authentication policy.

   4. In the **Policy** list, select **IdP Adapters** and then select the **HTML Form Adapter**. A branch for the **HTML Form Adapter** is added to the PingFederate policy tree, and **FAIL**/**SUCCESS** fields are added.

   5. Directly under the **HTML Form Adapter** field, click **Rules** and in the **Rules** modal, enter the following information, and then click **Done**:

      * **Attribute Name**: Select **policy.action**.

      * **Condition**: Select **equal to (case insensitive)**.

      * **Value**: Type **Security Key** as your authentication source.

      * **Result**: Type **Security Key** as your authentication source.

      * Select the **Default to success** checkbox.

        A Security Key branch is added to the PingFederate policy tree.

   6. In the **HTML Form Adapter** branch **FAIL** field, click **Done**.

   7. In the **HTML Form Adapter** branch **Security Key** field list, select **IdP Adapters**, and then select the PingID Adapter. **SUCCESS** and **FAIL** fields are added to the Security Key branch.

      1. Under the Security Key branch **FAIL** field, click **Done**.

      2. In the Security branch **SUCCESS** field list, select the endpoint you require. For example:

         * **Policy Contracts**: Select the policy contract you created earlier and complete the relevant mapping (learn more in [Configuring contract mapping](http://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configuring_contract_mapping.html)).

         * **Local Identity Profiles**: Select the Local Identity Profile you created earlier and then complete the relevant mapping (learn more in [Configuring local identity mapping](http://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configuring_local_identity_mapping.html)).

   8. In the **HTML Form Adapter** branch **SUCCESS** field list, select the action that you want to apply and configure it appropriately. For example:

      * If configuring the PingID Adapter (recommended), do the following:

        1. In the **SUCCESS** branch list, select **IdP Adapters** and then select**PingID Adapter**. **SUCCESS** and **FAIL** fields are added to the branch.

        2. Under the PingID Adapter **FAIL** field, click **Done**.

        3. In the PingID Adapter **SUCCESS** field, select the local identity profile you created earlier.

        4. Under the local identity profile click **Local Identity Mapping** and complete the relevant mapping with the PingID Adapter (learn more in [Configuring contract mapping](http://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configuring_contract_mapping.html)).

           |   |                                                                                                                                                                          |
           | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
           |   | You can find a list of attributes that can be used upon successful authentication with PingID in [PingID authentication attributes](pid_authentication_attributes.html). |

        5. Under the **PingID Adapter** entry, click **Options** and specify the following fields:

           * **Source**: HTML Form Adapter

           * **Attribute**: Username

           * Make sure the **User ID Authenticated** checkbox is selected.

      * If configuring a local identity profile:

        1. In the **SUCCESS** branch list, select the **Local Identity Profiles**, and then select the local identity profile that you created earlier.

        2. Directly under the **HTML Form Adapter** branch **SUCCESS** field click **Local Identity Mapping**, complete the relevant mapping from your source to the local identity contract, (learn more in [Configuring local identity mapping](http://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configuring_local_identity_mapping.html)), and then click **Done**.

2. Save the PingFederate policy.

3. Add any further configurations, for example:

   * Browser SSO: [Configure IdP Browser SSO](http://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html).

   * OAuth: [OAuth configuration](http://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_oauth_config.html).

---

---
title: (Legacy) Customizing the HTML Form Adapter for passwordless authentication with a security key
description: Customize the passwordless authentication flow by adding a security key icon to the passwordless flow button. You can also choose to show the security key button when using webAuthn-compatible browsers only.
component: pingid
page_id: pingid:pingid_integrations:customizing_html_adapter_for_passwordless_auth_security_key
canonical_url: http://docs.pingidentity.com/pingid/pingid_integrations/customizing_html_adapter_for_passwordless_auth_security_key.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 18, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
---

# (Legacy) Customizing the HTML Form Adapter for passwordless authentication with a security key

Customize the passwordless authentication flow by adding a security key icon to the passwordless flow button. You can also choose to show the security key button when using webAuthn-compatible browsers only.

## Before you begin

Before you start, [create a PingFederate policy for passwordless authentication with a security key](pid_configuring_pf_policy_for_passwordless_authentication_security_key.html).

## About this task

PingFederate 10.2 and later automatically includes a passwordless security key icon with the HTML Form Adapter, and automatically hides the security key button when the browser is not compatible with WebAuthn. For PingFederate 10.1 and lower, manually customize the HTML Form Adapter to:

* Add an icon to the passwordless flow button in the HTML Form Adapter. Add the security key icon provided by Ping Identity, or add your own custom icon.

* Choose to show the security key button only when the browser is webAuthn compatible.

## Steps

1. To add a passwordless authentication flow icon:

   1. Download the security key image [here](https://pingone-downloads.s3.amazonaws.com/pingid/Documentation+Resources+/icon_securitykey%402x.png), and in the relevant PingFederate folder, save the icon to the `server/default/conf/template/assets/images` folder as `icon-securitykey.png`.

   2. In the PingFederate folder, go to `server/default/conf/template/assets/css` and open the `main.css `file in a text editor.

   3. Add the following code to the `main.css `file, and then save the file.

      ```
      body .button-container .social-media.securitykey {
        background-image: url("../images/icon-securitykey.png");
        background-size: auto 10px;
        background-position: left 10px center
      }
      ```

2. To hide the security key button when a browser does not support WebAuthn:

   1. In the relevant PingFederate folder, go to `server/default/conf/template` and open `html.form.login.template.html` file in a text editor.

   2. In the html body add `isSecurityKeyAvailable();` to the `onload` attribute.

      ```
      <body onload="setFocus();isSecurityKeyAvailable();isWebAuthnPlatformAuthenticatorAvailable();">
      ```

   3. In the `script` element, add a new function, and then save the file.

      ```
      function isSecurityKeyAvailable() {
          var webauthnSupported = IsWebAuthnSupported();
          if (!webauthnSupported) {
              theElement = document.getElementById("securitykey-div");
              if (theElement) {
                  theElement.style.display = "none";
              }
          }
      }
      ```

---

---
title: Adding a New Authentication Realm
description: To configure Juniper for PingID multi-factor authentication (MFA), you must add a new authentication realm.
component: pingid
page_id: pingid:pingid_integrations:pid_adding_new_authentication_realm
canonical_url: http://docs.pingidentity.com/pingid/pingid_integrations/pid_adding_new_authentication_realm.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 27, 2024
section_ids:
  steps: Steps
  result: Result:
  result-2: Result:
  result-3: Result:
  result-4: Result:
  result-5: Result:
---

# Adding a New Authentication Realm

To configure Juniper for PingID multi-factor authentication (MFA), you must add a new authentication realm.

## Steps

1. In the left-hand navigation pane, go to **Users → User Realms → New**.

   ### Result:

   The **New Authentication Realm** window opens.

   ![A screen capture of the New Authentication Realm window.](_images/oul1564020872743.png)

2. In the **Name** field, enter a name for the Authentication Realm.

3. In the **Servers** section, enter the following information:

   1. From the **Authentication** list, select the name of the RADIUS server created in [Adding a RADIUS Server](pid_adding_radius_server.html).

   2. From the **User Directory/Attribute** list, select **Same as Above**.

   3. From the **Accounting** list, select the name of the RADIUS server created in [Adding a RADIUS Server](pid_adding_radius_server.html).

   4. From the **Device Attributes** list, select the default value of **None**.

4. Click **Save Changes**.

   ### Result:

   The Authentication Realm is saved and three additional tabs appear.

   ![A screen capture JuniperDemoRealm window, as configured in the previous step. The screen capture currently shows the Role Mapping tab.](_images/dqt1564020875036.png)

5. On the **Role Mapping** tab, click **New Rule**.

   ### Result:

   The **Role Mapping Rule** window opens.

   ![A screen capture of the Role Mapping Rule window.](_images/wds1564020877035.png)

6. In the **Role Mapping Rule** window, enter the following information:

   1. From the **Rule Based On** list, select **Username**.

   This is the default value.

   1. In the **Name** field, enter a name for the rule.

   2. In the **\* Rule: If Username…​** section, select **is** from the list, and then enter `*` in the text box.

   3. In the **…​Then Assign These Roles** section, select **Users** in the **Available Roles** list, and then click **Add**.

      ### Result:

      The **Users** role is added to the **Selected Roles** list.

7. Click **Save Changes**.

   ### Result:

   The Authentication Realm is saved.

---

---
title: Adding a RADIUS rule
description: To configure Checkpoint VPN for PingID multi-factor authentication (MFA), you must add a RADIUS rule.
component: pingid
page_id: pingid:pingid_integrations:pid_adding_radius_rule
canonical_url: http://docs.pingidentity.com/pingid/pingid_integrations/pid_adding_radius_rule.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 30, 2024
section_ids:
  steps: Steps
  result: Result:
  result-2: Result:
---

# Adding a RADIUS rule

To configure Checkpoint VPN for PingID multi-factor authentication (MFA), you must add a RADIUS rule.

## Steps

1. In the **Checkpoint** toolbar, click the **Firewall** tab.

2. In the upper left-hand tree, click **Policy**.

   ### Result:

   The rules of the existing policy are listed.

3. In the row for **Any**, in the **No.** column, right-click and select **Add Rule → Above**.

   ![A screen capture of the Add Rule menu cascade, accessed by right-clicking in the Number column and Any row.](_images/xws1564021011878.jpg)

   ### Result:

   A new row is added to this policy.

4. In the new row, in the **Source** column, right-click **Any**, and then go to **Add Objects → Add Legacy User Access**.

5. In the **Legacy User Access** window, select the RADIUS user configured earlier. Click **OK**.

   For more information, see [Configure a RADIUS user profile](pid_configuring_radius_user_profile.html).

   ![A screen capture of the Legacy User Access window.](_images/xpx1564021012397.jpg)

6. In the **Destination** column, right-click **Any** and select **Network Object**.

7. In the **Add Object** window, select the VPN network configured by your network administrator. Click **OK**.

   ![A screen capture of the Add Object window.](_images/iep1564021012936.jpg)

8. In the **VPN** column, right-click **Any Traffic**, and then click **Edit Cell**.

9. In the **VPN Match Conditions** window, select **Only Connections Encrypted in Specific VPN Communities**.

   ![A screen capture of the VPN Match Conditions window.](_images/kyp1564021013472.jpg)

10. Add the RemoteAccess community to the rule.

    1. In the **VPN Match Conditions** window, click **Add**.

    2. Select **RemoteAccess**. Click **OK**.

    3. To return to the main menu, click **OK**.

11. In the **Action** column of your RADIUS rule, right-click and select **Accept**.

12. In the **Track** column of your RADIUS rule, right-click **None**, and then select **Log**.

    ![A screen capture of the Policy list, showing the new RADIUS rule.](_images/ynd1564021014102.jpg)

---

---
title: Adding a RADIUS Server
description: To configure Juniper for PingID multi-factor authentication (MFA), you must add a RADIUS server.
component: pingid
page_id: pingid:pingid_integrations:pid_adding_radius_server
canonical_url: http://docs.pingidentity.com/pingid/pingid_integrations/pid_adding_radius_server.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 28, 2024
section_ids:
  steps: Steps
  result: Result:
  result-2: Result:
---

# Adding a RADIUS Server

To configure Juniper for PingID multi-factor authentication (MFA), you must add a RADIUS server.

## Steps

1. Sign on to Juniper with your administrator ID and password.

2. In the left-hand navigation pane, go to **Authentication → Auth. Servers**.

   ![A screen capture of the Authentication Servers window showing the New list with the buttons New Server and Delete and a table with a header row that shows Authentication/Authorization Servers, Type, User Record Synchronization, and Logical Auth Server Name. There is a check box column at the left most side. Example servers Administrators and System Local appear as separate entries under the Authentication/Authorization Servers column. Under the Type column, there are two entries for Local Authentication. The columns for User Record Synchronization and Logical Auth Server Name have no entries..The row that contains the System Local entry has a check box in the left most column.](_images/opn1564020863507.png)

3. From the **New** list, select **RADIUS Server**, and then click **New Server**.

   ### Result:

   The**New Radius Server** window opens.

   ![A screen capture of the New Radius Server window. The window includes the Name and NAS-Identifier fields followed by sections for Primary Server and Backup Server. The Primary Server section includes fields for Radius Server, Authentication Port, Shared Secret, Accounting Port, NAS-IP-Address, Timeout, and Retries. There is also a check box option for Users authenticate using tokens or one-time passwords with the note: "If you select this, the device will send the user's authentication method as 'token' if you use SAML, and this credential will not be used in automatic SSO in backend applications. In this screen capture, the Backup Server section includes the specification that it is required only if Backup server exists and fields for Radius Server, Authentication Port, Shared Secret, and Accounting Port."](_images/nst1564020866108.png)

4. In the **New Radius Server** window, enter the following information:

   1. In the **Name** field, enter the RADIUS Server name.

   2. In the **NAS-Identifier** field, enter the name of the device as known to the RADIUS server.

   3. In the **Radius Server** field, enter the DNS name or IP address of the RADIUS server password credential validator (PCV).

   4. In the **Authentication Port** field, enter the port configured in the RADIUS server PCV. The default value is `1812`.

   5. In the **Shared Secret** field, enter the shared secret configured in the RADIUS server PCV.

   6. In the **Accounting Port** field, enter the port used for RADIUS accounting.

      |   |                                                        |
      | - | ------------------------------------------------------ |
      |   | The default value is `1813` and should not be changed. |

   7. In the **Timeout** field, enter `60`.

      The default value is `30`.

      |   |                                                                                                    |
      | - | -------------------------------------------------------------------------------------------------- |
      |   | The **Timeout** field determines the amount of time in seconds before the connection is timed out. |

5. Click **Save Changes**.

   ### Result:

   The Custom Radius Rules section is enabled.

   ![A screen capture of the Custom Radius Rules section.](_images/ujg1564020868445.jpg)

6. Click **New Radius Rule**.

   The following window is didplayed:

   ![A screen capture of the Add Custom Radius Rule window showing the configuration details from the previous configuration steps.](_images/pon1564020869349.png)

7. In the **Add Custom Radius Rule** window, enter the following information:

   1. In the **Name** field, enter `Offline`.

   2. From the **Response Packet Type** list, select **Access Challenge**.

   This is the default value.

   1. Select the **Show Generic Login Page** check box.

8. Click **Save Changes**.

---

---
title: Adding PingID for MFA
description: In the NGFW admin portal, click the Device tab, and then go to Server Profiles → Multi Factor Authentication.
component: pingid
page_id: pingid:pingid_integrations:pid_adding_pid_for_mfa
canonical_url: http://docs.pingidentity.com/pingid/pingid_integrations/pid_adding_pid_for_mfa.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 28, 2024
section_ids:
  steps: Steps
  result: Result:
  result-2: Result:
---

# Adding PingID for MFA

## Steps

1. In the NGFW admin portal, click the **Device** tab, and then go to **Server Profiles → Multi Factor Authentication**.

2. Click **+Add**.

   ### Result:

   The **Multi Factor Authentication Server Profile** window appears.

   ![A screen capture of the Multi Factor Authentication Server Profile window. In this screen capture, the Profile Name field says, "PingID". The Certificate Profile drop-down list shows three options: PingID-cert-profile, vm-series-cert-profile, and New Certificate Profile. PingID-cert-profile is selected.](_images/dht1568630937029.png)

3. In the **Profile Name** field, enter a name for the profile. We will use **PingID**.

4. From the **Certificate Profile** list, select the certificate profile that you previously created.

   |   |                                                                                                                                                                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you have not yet created a certificate profile for PingID, see [Configure a Certificate Profile](https://docs.paloaltonetworks.com/pan-os/9-1/pan-os-admin/certificate-management/configure-a-certificate-profile) in the Palo Alto documentation. |

5. From the **MFA Vendor** list, select **PingID**.

   ### Result:

   Several fields populate automatically.

   ![A screen capture of the Multi Factor Authentication Server Profile window, showing populated fields in the Server Settings section with MFA Vendor PingID selected. The populated fields are Base URI, Host name, and Timeout (sec).](_images/jfb1567510659530.png)

6. From the PingID properties file, complete the three fields listed in the following table.

   The relationships between the PingID properties fields and the fields listed in the **Multi Factor Authentication Server Profile** window are described in the following table.

   | Display Name                      | Certificate Field | Illustrative value                           |
   | --------------------------------- | ----------------- | -------------------------------------------- |
   | **Use Base64 Key**                | `use_base64_key`  | APixxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx7ct4z7LOM= |
   | **Token**                         | `token`           | c85cxxxxxxxxxxxxxxxxxxxxxxxxx4c1             |
   | **PingID Client Organization ID** | `Org_alias`       | faxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxx779         |

7. Ensure that the **Use Base64 Key**, **Token**, and **PingID Client Organization ID** fields are populated, and then click **OK**.

   ![A screen capture of the Multi Factor Authentication Server Profile window with all fields populated.](_images/ofi1567517453593.png)

---

---
title: Background concepts for the  PingID for Windows Login - Passwordless integration
description: Background concepts for the  PingID for Windows Login - Passwordless integration.
component: pingid
page_id: pingid:pingid_integrations:pid_integrating_pid_passwordless_windows_login
canonical_url: http://docs.pingidentity.com/pingid/pingid_integrations/pid_integrating_pid_passwordless_windows_login.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 27, 2026
section_ids:
  the_environment: The environment
  security_concepts: Security concepts
  authentication_protocols: Authentication protocols
  troubleshooting: Troubleshooting
---

# Background concepts for the PingID for Windows Login - Passwordless integration

These resources support administrators integrating PingID with Windows Login - Passwordless authentication. This integration bridges the PingID cloud platform and on-premise Windows Active Directory environments, as well as Entra ID-joined machine environments. Effective implementation requires deep expertise in both domains.

The following topics cover areas that contribute to a successful integration. Some of these areas are vendor specific. They can change and require greater detail than a background article can cover. You should stay up to date on information relevant to supporting your integration.

The resources are organized into the following areas:

* [The environment](#the_environment): Resources about the underlying infrastructure that supports the integration. This covers Active Directory fundamentals, Domain Controllers, and networking concepts. Network concepts include components like Group Policy Objects (GPOs) for deploying software and the Windows Credential Provider framework, which allows for the custom login experience.

* [Security concepts](#security_concepts): The integration relies on certificates to bridge cloud and on-premise. Information covers digital certificates including the distinction between Key Distribution Center (KDC) certificates (issued by internal certificate authorities for Active Directory) and issuance certificates (managed within PingOne).

* [Authentication protocols](#authentication_protocols): Resources about the mechanics of the login process. This includes materials about the Kerberos protocol, the PKINIT configuration for certificate-based authentication, and the FIDO2 and WebAuthn standards used by security keys.

* [Troubleshooting](#troubleshooting): Diagnostic tools for verifying trust chains and checking revocation status.

## The environment

It's important to understand the existing environment to better understand how it integrates with PingID. The integration directly modifies the Windows login mechanism using the Credential Provider framework, which acts as the software bridge between the local Logon UI and the PingID cloud services.

The following areas will help you understand your environment:

* **Active Directory**: A directory service for Windows domain networks. The centralized directory that manages the domain-joined clients that are integrated using PingID with passwordless Windows login.

  Learn more about Active Directory in [AD DS Overview](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview) in the Microsoft documentation.

* **Domain controller (DC)**: Required to manage the security and identity requests in a Windows domain and hosts the Key Distribution Center (KDC). It runs the Active Directory Domain Services (AD DS) role.

* **Active Directory Domain Services (AD DS)**: Provides the fundamental structure for user and group management and domain integrity. It issues the KDC certificates that are crucial for the Kerberos authentication process in the passwordless login flow.

  Learn more in [AD DS Overview](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview).

* **Microsoft Entra ID (Azure AD)**: In addition to on-premise Active Directory environments, the integration supports Entra ID-joined machines. When users are in an Entra ID-only environment, the integration uses certificate-based authentication (CBA) through Entra ID rather than the on-premise Kerberos-based flow.

  Learn more in [Configuration for use with Entra ID-joined devices](pid_configuration_for_use_with_entra_id.html) and [Microsoft Entra certificate-based authentication technical concepts](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-certificate-based-authentication-technical-deep-dive#username-binding-policy) in the Microsoft documentation.

- **Group Policy Management Console and Group Policy Objects (GPO)**: The GPO is the method used to push out and install the PingID integration software onto client machines using the provided Microsoft Installer (MSI). It also pushes out configuration settings that PingID needs to function properly on managed, domain-joined clients.

  Learn more in the Microsoft [Group Policy Management Console](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/gpmc/group-policy-management-console-portal) documentation.

- **Windows credential providers**: The specific framework PingID hooks into to override standard credential prompts with a custom passwordless interface. It orchestrates a handshake between the local Windows session, the Active Directory identity, and the PingID Cloud account to validate the user's identity.

  Learn more about Windows credential providers in [Credential Providers](https://learn.microsoft.com/en-us/windows/win32/secauthn/credential-providers-in-windows).

- **Networking and connectivity**: Facilitation of authorized traffic between clients, domain controllers, and PingOne cloud requires well-configured DNS and firewall rules to resolve properly.

- **DNS**: Maps human-readable domain names to IP addresses. Having DNS configured correctly ensures that clients can resolve the needed services and endpoints for authentication.

  * Learn more in [Domain Names - Implementation and Specification](https://datatracker.ietf.org/doc/html/rfc1035).

  * [DNS Visualization Tool](https://dnsviz.net/): A tool to understand and troubleshoot DNS Security Extensions deployments.

- **Firewall:** Monitors and controls incoming and outgoing network traffic based on configured security rules. Because firewalls can block or inspect HTTPS traffic, their configuration is a common source of connectivity issues. For the Windows Login – Passwordless integration, ensure the firewall allows outbound HTTPS connections to the required PingID endpoints.

  Learn more in [What is a Firewall?](https://www.fortinet.com/resources/cyberglossary/firewall)

* **Trusted Platform Module (TPM)**: A hardware-based security component that provides secure storage for cryptographic keys. In a passwordless context, the TPM acts as the secure storage for the private keys used in FIDO2 and WebAuthn flows, ensuring no process can export or tamper with them.

  Learn more about TPM in [TPM 2.0 Library](https://trustedcomputinggroup.org/resource/tpm-library-specification/) and [Trusted Platform Module Overview](https://learn.microsoft.com/en-us/windows/security/information-protection/tpm/trusted-platform-module-overview).

* **Remote Desktop Protocol (RDP)**: You can configure Windows Login (passwordless) for use with RDP.

  Learn more in [Configuration for use with RDP](pid_configuration_for_use_with_rdp.html) and [Remote Desktop Protocol](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/welcome-to-rds).

## Security concepts

Important security concepts for the integration include the use of certificates for authentication, the role of the KDC in issuing Kerberos tickets, and the FIDO2 and WebAuthn standards for passwordless authentication.

* **Certificates**: The integration relies on **certificate-based authentication** to sign the user on without a passcode.

  Learn more about certificates in [What is Certificate-Based Authentication?](https://www.yubico.com/resources/glossary/what-is-certificate-based-authentication/).

* **Public Key Infrastructure (PKI)**: Background in trust chains and digital certificates to help in creating specific certificates for authentication. In PKI-reliant systems, certificate errors often are the reason for deployment failure. Administrators must ensure the validity of the entire trust chain. The integration relies on KDC certificates issued by an internal CA and issuance certificates managed within PingOne. If there are issues with the certificates, the authentication process will fail, so understanding PKI concepts is crucial for troubleshooting.

  Learn more in [What is Public Key Infrastructure (PKI)?](https://www.ssl.com/article/what-is-public-key-infrastructure-pki/), [What is a Digital Certificate?](https://www.ssl.com/article/what-is-a-digital-certificate/) and [Check for Certificate Configuration Errors](pid_troubleshooting_passwordless_windows_login.html#check-for-certificate-configuration-errors).

* **Certificate Authority (CA)**: An internal CA, like AD CS, is necessary to issue the KDC certificate.

  Learn more in [What is a Certificate Authority (CA)?](https://www.ssl.com/article/what-is-a-certificate-authority-ca/).

* **Key Distribution Center (KDC) certificates**: Issued by an internal certificate authority like AD CS for Active Directory, they're used in the Kerberos authentication process.

  Learn more in [Domain Controller Certificate Requirements](https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/kerberos-authentication-troubleshooting-guidance) and [An introduction to the key distribution center, mathematical algorithms, and the hashing function](https://www.infosecinstitute.com/resources/cryptography/an-introduction-to-the-key-distribution-center-mathematical-algorithms-and-the-hashing-function/).

* **Issuance certificates**: Managed within PingOne, they are used to establish trust between the on-premise environment and the PingID cloud services.

  Learn more about issuance certificates in [Creating an issuance certificate in PingOne](pid_creating_issuance_certificate_in_p1.html).

## Authentication protocols

Specific protocols used during the login process and how they work.

* **Kerberos (protocol):** The integration relies on the KDC issuing Kerberos tickets. Understanding this is crucial for troubleshooting.

  Learn more about Kerberos in [Kerberos: The Network Authentication Protocol](https://web.mit.edu/kerberos), [Kerberos Protocol Tutorial](https://www.kerberos.org/software/tutorial.html), and [Kerberos Authentication Troubleshooting Guidance](https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/kerberos-authentication-troubleshooting-guidance).

* **Public Key Cryptography for Initial Authentication (PKINIT) configuration:** Allows the use of certificates and public key cryptography in the Kerberos protocol initial authentication exchange.

  Learn more in [PKINIT Configuration](https://web.mit.edu/kerberos/krb5-1.12/doc/admin/pkinit.html).

* **FIDO2 and WebAuthn**: FIDO2 is a set of specifications for passwordless authentication using public key cryptography. It includes the web authentication API (WebAuthn) to perform secure authentication.

  Learn more in [FIDO2 Overview](https://fidoalliance.org/fido2/overview/) and [WebAuthn Specification](https://www.w3.org/TR/webauthn-2/).

* [WebAuthn.io](https://webauthn.io/): A tool you can use to test the WebAuthn protocol.

* **CBA for Entra ID-joined machines**: In an Entra ID-only environment, the integration uses CBA instead of the Kerberos-based flow used in on-premise Active Directory environments. The issuance certificate created in PingOne is uploaded to Entra ID as a trusted certificate authority, and Entra ID authenticates the user by validating the certificate presented during sign-on. This requires configuring authentication binding and username binding rules in Entra ID.

  Learn more in [Configuration for use with Entra ID-joined devices](pid_configuration_for_use_with_entra_id.html) and [Microsoft Entra certificate-based authentication](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-certificate-based-authentication) in the Microsoft documentation.

## Troubleshooting

Administrators should monitor their installation, verify MSI installations, inspect trust chains, and troubleshoot Credential Provider "hooks" during the login process. Also maintaining certificates requires a specialized diagnostic toolkit.

The following tools are helpful for monitoring, troubleshooting, and diagnosing problems:

* **Audit the PingOne log files**: The PingOne log files provide detailed activity information about Windows Login - Passwordless.

  Learn more in [Check the log files](pid_troubleshooting_passwordless_windows_login.html#check_the_log_files).

* **Windows Event Viewer**: Use the Applications and Services Logs to diagnose issues. Check entries for the PingID Credential Provider to determine why a login attempt failed.

  Learn more in [Check Windows Event Viewer](pid_troubleshooting_passwordless_windows_login.html#check-windows-event-viewer).

* **certmgr.msc**: The Microsoft Management Console (MMC) snap-in to manage the current user's certificates. You can use it to verify that root and intermediate CAs are correctly placed in the user's certificate store. To open it, run `certmgr.msc` from the **Run** command or command prompt.

* **certutil**: A command-line utility that you can use for verifying certificate validity and checking revocation status.

* **PowerShell**: Essential for automating environment configuration and bulk management.

  Learn more in [Introduction to PowerShell](https://learn.microsoft.com/en-us/training/modules/introduction-to-powershell/).

* **[SSL Shopper](https://www.sslshopper.com/ssl-checker.html)**: A tool to visualize and verify the certificate trust chains, ensuring that the server is configured correctly.

.

---

---
title: Checking that response pages are enabled
description: In the Palo Alto NGFW admin portal, go to Network → Interfaces and check that the interface you used for the Redirect Host has a management profile.
component: pingid
page_id: pingid:pingid_integrations:pid_checking_that_response_pages_are_enabled
canonical_url: http://docs.pingidentity.com/pingid/pingid_integrations/pid_checking_that_response_pages_are_enabled.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 27, 2024
section_ids:
  before-you-begin: Before you begin
  steps: Steps
---

# Checking that response pages are enabled

## Before you begin

In the Palo Alto NGFW admin portal, go to **Network → Interfaces** and check that the interface you used for the Redirect Host has a management profile.

![A screen capture of the Interface list. The Interface list also includes categories for Interface Type, Management Profile, Link State, IP Address, Virtual Router, Tag, VLAN/Virtual-Wire, Security Zone, and Features.](_images/axy1567604002420.png)

If no management profile exists, you must add a management profile for the interface. The following steps show how to edit an existing profile.

## Steps

1. In the Palo Alto NGFW admin portal, go to **Network → Network Profiles → Interface Mgmt**.

2. Click the **Interface Management Profile** for the required interface.

3. Ensure that the **Response Pages** check box is selected, and then click **OK**.

   ![A screen capture of the Interface Management Profile window, showing the Response Pages check box, highlighted with a red circle and selected.](_images/log1567604587126.png)

4. Commit all changes.

---

---
title: Committing the changes
description: To apply the configuration, commit the changes.
component: pingid
page_id: pingid:pingid_integrations:pid_committing_the_changes
canonical_url: http://docs.pingidentity.com/pingid/pingid_integrations/pid_committing_the_changes.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 27, 2024
section_ids:
  steps: Steps
  result: Result:
---

# Committing the changes

To apply the configuration, commit the changes.

## Steps

1. In the **Checkpoint** menu bar, click **Install Policy**.

   ![A screen capture of the Install Policy window. The window shows a list of installation targets with one gateway selected and an Advanced section. In the Advanced section, there are settings for Installation Mode and Revision Control. The Install on each selected gateway independently option is selected.](_images/obs1564021017434.jpg)

2. Ensure that the **Install on Each Selected Gateway Independently** option is selected, and then click **OK**.

   ### Result:

   The configuration is verified and installed. A message appears when the policy installation is complete.

---

---
title: Configuration example of ForceCommand for AIX
description: This is an example configuration of PingID SSH for ForceCommand on AIX.
component: pingid
page_id: pingid:pingid_integrations:pid_configuration_example_forcecommand_aix
canonical_url: http://docs.pingidentity.com/pingid/pingid_integrations/pid_configuration_example_forcecommand_aix.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 30, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuration example of ForceCommand for AIX

This is an example configuration of PingID SSH for ForceCommand on AIX.

## About this task

|   |                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------- |
|   | This assumes that you specified `--prefix=/usr` in the configure command, or installed from the binary package. |

## Steps

1. Edit the sshd\_config file:

   `sudo vi /etc/ssh/sshd_config`

2. Add these lines to the end of the file:

   ```
   #enable pingid for all users
   ForceCommand /usr/sbin/pingid_fc
   ```

   |   |                                                                                                                                                                          |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Disable `PermitTunnel` and `AllowTcpForwarding` in the `sshd_config` file because tunneling and port forwarding are performed before PingID authentication is triggered. |

3. Restart the sshd service:

   `sudo service sshd restart`

---

---
title: Configuration example of ForceCommand for HP-UX
description: This is an example configuration of PingID SSH for ForceCommand on HP-UX.
component: pingid
page_id: pingid:pingid_integrations:pid_configuration_example_forcecommand_hp_ux
canonical_url: http://docs.pingidentity.com/pingid/pingid_integrations/pid_configuration_example_forcecommand_hp_ux.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 28, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuration example of ForceCommand for HP-UX

This is an example configuration of PingID SSH for ForceCommand on HP-UX.

## About this task

|   |                                                                                 |
| - | ------------------------------------------------------------------------------- |
|   | This assumes that you specified `--prefix=/usr/local` in the configure command. |

## Steps

1. Edit the sshd\_config file:

   ```
   sudo vi /opt/ssh/etc/sshd_config
   ```

2. Add these lines to the end of the file:

   ```
   #enable pingid for all users
   ForceCommand /usr/local/sbin/pingid_fc
   ```

   |   |                                                                                                                                                                          |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Disable `PermitTunnel` and `AllowTcpForwarding` in the `sshd_config` file because tunneling and port forwarding are performed before PingID authentication is triggered. |

3. Restart the sshd service:

   ```
   sudo /sbin/init.d/secsh stop
   sudo /sbin/init.d/secsh start
   ```

---

---
title: Configuration example of ForceCommand for Red Hat
description: This is an example configuration of PingID SSH for ForceCommand on Red Hat.
component: pingid
page_id: pingid:pingid_integrations:pid_configuration_example_forcecommand_for_red_hat
canonical_url: http://docs.pingidentity.com/pingid/pingid_integrations/pid_configuration_example_forcecommand_for_red_hat.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuration example of ForceCommand for Red Hat

This is an example configuration of PingID SSH for ForceCommand on Red Hat.

## About this task

|   |                                                                                   |
| - | --------------------------------------------------------------------------------- |
|   | This process assumes that you specified `--prefix=/usr` in the configure command. |

## Steps

1. Edit the `sshd_config` file.

   ```
   sudo vi /etc/ssh/sshd_config
   ```

   1. Add `pingid_fc` with its full path.

      ```
      Match User joe
      ForceCommand /usr/sbin/pingid_fc
      ```

   |   |                                                                                                                                                                          |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Disable `PermitTunnel` and `AllowTcpForwarding` in the `sshd_config` file because tunneling and port forwarding are performed before PingID authentication is triggered. |

2. To apply the changes and activate PingID MFA integration with SSH, restart the sshd service.

   ```
   sudo service sshd restart
   ```

---

---
title: Configuration example of ForceCommand for Solaris
description: This is an example configuration of PingID SSH for ForceCommand on Solaris.
component: pingid
page_id: pingid:pingid_integrations:pid_configuration_example_forcecommand_for_solaris
canonical_url: http://docs.pingidentity.com/pingid/pingid_integrations/pid_configuration_example_forcecommand_for_solaris.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 30, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuration example of ForceCommand for Solaris

This is an example configuration of PingID SSH for ForceCommand on Solaris.

## About this task

|   |                                                                                   |
| - | --------------------------------------------------------------------------------- |
|   | This process assumes that you specified `--prefix=/usr` in the configure command. |

## Steps

1. Edit the `sshd_config` file.

   ```
   sudo vi /etc/ssh/sshd_config
   ```

   1. Add `pingid_fc` with its full path.

      ```
      # enable pingid for all users
      ForceCommand /usr/sbin/pingid_fc
      ```

   |   |                                                                                                                                                                          |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Disable `PermitTunnel` and `AllowTcpForwarding` in the `sshd_config` file because tunneling and port forwarding are performed before PingID authentication is triggered. |

2. To apply the changes and activate PingID MFA integration with SSH, restart the sshd service.

   ```
   sudo service sshd restart
   ```

---

---
title: Configuration example of ForceCommand for Ubuntu/Debian
description: This is an example configuration of PingID SSH for ForceCommand on Ubuntu and Debian distributions.
component: pingid
page_id: pingid:pingid_integrations:pid_configuration_example_forcecommand_for_ubuntu_debian
canonical_url: http://docs.pingidentity.com/pingid/pingid_integrations/pid_configuration_example_forcecommand_for_ubuntu_debian.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 29, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuration example of ForceCommand for Ubuntu/Debian

This is an example configuration of PingID SSH for ForceCommand on Ubuntu and Debian distributions.

## About this task

|   |                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------- |
|   | This process assumes that you specified `--prefix=/usr` in the configure command or installed from the binary package. |

## Steps

1. Edit the sshd\_config file.

   ```
   sudo vi /etc/ssh/sshd_config
   ```

   1. Add the following lines to the end of the file.

      ```
      #enable pingid for all users
      ForceCommand /usr/sbin/pingid_fc
      ```

   |   |                                                                                                                                                                          |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Disable `PermitTunnel` and `AllowTcpForwarding` in the `sshd_config` file because tunneling and port forwarding are performed before PingID authentication is triggered. |

2. To apply the changes and activate PingID MFA integration with SSH, restart the sshd service.

   ```
   sudo service sshd restart
   ```

---

---
title: Configuration example of PAM for AIX
description: This is an example configuration of PingID SSH for PAM on AIX.
component: pingid
page_id: pingid:pingid_integrations:pid_configuration_example_pam_aix
canonical_url: http://docs.pingidentity.com/pingid/pingid_integrations/pid_configuration_example_pam_aix.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 30, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Configuration example of PAM for AIX

This is an example configuration of PingID SSH for PAM on AIX.

## About this task

|   |                                                                           |
| - | ------------------------------------------------------------------------- |
|   | This assumes that you specified `--prefix=/usr` in the configure command. |

## Steps

1. Edit the `/etc/security/login.cfg` file and change this line near the bottom of the file.

   From:

   ```
   auth_type = STD_AUTH
   ```

   To:

   ```
   auth_type = PAM_AUTH
   ```

2. Edit the `/etc/pam.conf` file as follows:

   ### Choose from:

   * **To add MFA to SSH:**Change the lines starting with `sshd`:

     From:

     ```
     sshd auth required pam_aix
     ```

     To:

     ```
     sshd auth requisite pam_aix
     sshd auth required /usr/lib/security/pam_pingid.so
     ```

   * **To add MFA to SU:** Change the lines starting with `su`:

     From:

     ```
     su auth sufficient pam_allowroot
     su auth required pam_aix
     ```

     To:

     ```
     su auth sufficient pam_allowroot
     su auth requisite pam_aix
     su auth required /usr/lib/security/pam_pingid.so
     ```

---

---
title: Configuration example of PAM for HP-UX
description: This is an example configuration of PingID SSH for PAM on HP-UX.
component: pingid
page_id: pingid:pingid_integrations:pid_configuration_example_pam_for_hp_ux
canonical_url: http://docs.pingidentity.com/pingid/pingid_integrations/pid_configuration_example_pam_for_hp_ux.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 23, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Configuration example of PAM for HP-UX

This is an example configuration of PingID SSH for PAM on HP-UX.

## About this task

|   |                                                                                 |
| - | ------------------------------------------------------------------------------- |
|   | This assumes that you specified `--prefix=/usr/local` in the configure command. |

## Steps

1. Create a backup of the common PAM configuration file, `/etc/pam.conf`.

2. Edit the `/etc/pam.conf` file as follows:

   ### Choose from:

   * **To add MFA to SSH:** Change the lines starting with `sshd`:

     From:

     ```
     sshd auth required libpam_hpsec.so.1
     sshd auth required libpam_unix.so.1
     ```

     To:

     ```
     sshd auth required libpam_hpsec.so.1
     sshd auth required /usr/lib/security/pam_pingid.so
     ```

     1. Apply PingID to SSH by editing the sshd\_config file:

        ```
        sudo vi /opt/ssh/etc/sshd_config
        ```

     2. Set `UsePAM` to 'yes', `ChallengeResponseAuthentication` to 'yes' and `PasswordAuthentication` to 'no'.

     3. Configure PAM for public key authentication by adding the following line to the SSHD configuration file,`sshd_config`:

        ```
        AuthenticationMethods publickey,keyboard-interactive
        ```

        |   |                                                 |
        | - | ----------------------------------------------- |
        |   | To check the OpenSSH version, run```
        ssh -V
        ``` |

     4. Restart the sshd service:

        ```
        sudo /sbin/init.d/secsh stop
        sudo /sbin/init.d/secsh start
        ```

   * **To add MFA to SU:** Change the lines starting with `su`:

     From:

     ```
     su auth required libpam_hpsec.so.1 bypass_setaud
     su auth required libpam_unix.so.1
     ```

     To:

     ```
     su auth required libpam_hpsec.so.1 bypass_setaud
     su auth requisite libpam_unix.so.1
     su auth required /usr/lib/security/pam_pingid.so
     ```

---

---
title: Configuration example of PAM for Red Hat
description: This procedure is an example configuration of PingID SSH for PAM on Red Hat.
component: pingid
page_id: pingid:pingid_integrations:pid_configuration_example_pam_for_red_hat
canonical_url: http://docs.pingidentity.com/pingid/pingid_integrations/pid_configuration_example_pam_for_red_hat.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuration example of PAM for Red Hat

This procedure is an example configuration of PingID SSH for PAM on Red Hat.

## About this task

|   |                                                                           |
| - | ------------------------------------------------------------------------- |
|   | This assumes that you specified `--prefix=/usr` in the configure command. |

## Steps

1. Edit the relevant PAM `conf` file. `sudo vi /etc/pam.d/system-auth`

2. Replace this line:

   ```
   auth      sufficient  pam_unix.so nullok try_first_pass
   ```

   with these lines:

   ```
   auth      requisite   pam_unix.so nullok try_first_pass
   auth      sufficient  pam_pingid.so
   ```

3. Apply PingID to SSH by editing the `sshd_config` file:

   1. Run

      ```
      sudo vi /etc/ssh/sshd_config
      ```

   2. Set the following parameters:

      * `usePAM` to `yes`

      * `ChallengeResponseAuthentication` to `yes`

      * `PasswordAuthentication` to `no`

4. Configure PAM for public key authentication by adding the following line to the SSHD configuration file, `sshd_config`.

   ```
   AuthenticationMethods publickey,keyboard-interactive
   ```

   Remove `pam_unix.so` from the PAM configuration for SSHD, to prevent display of a password prompt for the keyboard-interactive authentication method.

   |   |                                                                                                                                                            |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | PAM authentication is supported for SSHD with public key authentication, only when using OpenSSH 6.2 and later.To check the OpenSSH version, run `ssh -V`. |

5. Restart the sshd service.

   `sudo service sshd restart`

---

---
title: Configuration example of PAM for Solaris
description: This is an example configuration of PingID SSH for PAM on Solaris.
component: pingid
page_id: pingid:pingid_integrations:pid_configuration_example_pam_for_solaris
canonical_url: http://docs.pingidentity.com/pingid/pingid_integrations/pid_configuration_example_pam_for_solaris.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 25, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuration example of PAM for Solaris

This is an example configuration of PingID SSH for PAM on Solaris.

## About this task

|   |                                                                           |
| - | ------------------------------------------------------------------------- |
|   | This assumes that you specified `--prefix=/usr` in the configure command. |

## Steps

1. Edit the `pam.conf` file.

   ```
   sudo vi /etc/pam.conf
   ```

2. Replace these lines:

   ```
   #
   # Default definitions for Authentication management
   # Used when service name is not explicitly mentioned for authentication
   #
   other   auth requisite          pam_authtok_get.so.1
   other   auth required           pam_dhkeys.so.1
   other   auth required           pam_unix_cred.so.1
   other   auth required           pam_unix_auth.so.1
   ```

   with these lines:

   ```
   #
   # Default definitions for Authentication management
   # Used when service name is not explicitly mentioned for authentication
   #
   other   auth requisite          pam_authtok_get.so.1
   other   auth required           pam_dhkeys.so.1
   other   auth required           pam_unix_cred.so.1
   other   auth requisite          pam_unix_auth.so.1
   other   auth required           pam_pingid.so
   ```

3. If you want to apply PingID on SSH, edit the `sshd_config` file.

   ```
   sudo vi /etc/ssh/sshd_config
   ```

   1. Set the following configurations:

      * `PAMAuthenticationViaKBDInt` to `yes`

      * `ChallengeResponseAuthentication` to `yes`

      * `PasswordAuthentication` to `no`

4. Configure PAM for public key authentication by adding the following line to the SSHD configuration file, `sshd_config`.

   ```
                  AuthenticationMethods publickey,keyboard-interactive
   ```

5. Remove `pam_unix.so` from the PAM configuration for SSHD to prevent PingID from displaying a password prompt for the keyboard-interactive authentication method.

   |   |                                                   |
   | - | ------------------------------------------------- |
   |   | To check the OpenSSH version, run:```
    ssh -V
   ``` |

6. To apply the changes and activate PingID multi-factor authentication (MFA) integration with SSH, restart the sshd service.

   ```
   sudo service sshd restart
   ```