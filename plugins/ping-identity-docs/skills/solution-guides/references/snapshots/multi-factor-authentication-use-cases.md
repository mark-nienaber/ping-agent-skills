---
title: Adding multi-factor authentication to secure apps (PingID with PingAccess)
description: Learn how to synchronize a session for your web applications between PingFederate and PingAccess through PingID
component: solution-guides
page_id: solution-guides:multi-factor_authentication_use_cases:htg_add_mfa_to_secure_apps_pid_with_pa
canonical_url: https://docs.pingidentity.com/solution-guides/multi-factor_authentication_use_cases/htg_add_mfa_to_secure_apps_pid_with_pa.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 24, 2025
page_aliases: ["multi-factor_authentication_use_cases:pf_saml_authentication_policy_contract.adoc", "multi-factor_authentication_use_cases:pf_creating_authentication_selector.adoc", "multi-factor_authentication_use_cases:pf_creating_authenticationpolicy_tree.adoc", "multi-factor_authentication_use_cases:pf_oauth_authenticationpolicy_mapping.ado", "multi-factor_authentication_use_cases:pa_settings_policyrules.adoc"]
section_ids:
  components: Components
  before-you-begin: Before you begin
  creating-a-saml-authentication-policy-contract: Creating a SAML authentication policy contract
  about-this-task: About this task
  steps: Steps
  creating-an-authentication-selector: Creating an authentication selector
  about-this-task-2: About this task
  steps-2: Steps
  creating-an-authentication-policy-tree: Creating an authentication policy tree
  about-this-task-3: About this task
  steps-3: Steps
  adding-an-oauth-authentication-policy-mapping: Adding an OAuth authentication policy mapping
  before-you-begin-2: Before you begin
  steps-4: Steps
  adding-access-settings-and-policy-rules-in-pingaccess: Adding access settings and policy rules in PingAccess
  steps-5: Steps
---

# Adding multi-factor authentication to secure apps (PingID with PingAccess)

Learn how to synchronize a session for your web applications between PingFederate and PingAccess through PingID

## Components

* PingFederate 10.3

* PingAccess 6.3

* PingID

## Before you begin

* Verify that PingFederate 10.3 and PingAccess 6.3 are installed and running.

* Create an OpenID Connect (OIDC) connection between PingFederate and PingAccess, as described in [Configure PingFederate for PingAccess connectivity](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-63.pdf#page=512) (page 512).

* Register a PingID account, as described in [Register the PingID service](https://docs.pingidentity.com/pingid/pingid_integrations/registering_the_pid_service.html).

* Set up a PingID adapter in PingFederate, as described in [Managing IdP adapters](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-103.pdf#page=396) (page 396).

|   |                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This use case was developed with the specified product versions. With more recent product versions, the general workflow should apply although specific menu options and screens might differ. |

## Creating a SAML authentication policy contract

### About this task

Create a SAML authentication policy contract, as described in [Policy contracts](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-103.pdf#page=274) (page 274).

### Steps

1. In PingFederate, go to **Authentication > Policies > Policy Contracts**.

2. Click **Create New Contract**.

3. On the **Contract Info** tab, in the **Contract Name** field, enter a name for your SAML authentication policy contract.

4. On the **Contract Attributes** tab, in the **Extend the Contract** section, enter `SAML_AUTHN_CTX`. Click **Add**.

5. Click **Next**.

6. On the **Summary** tab, click **Save**.

## Creating an authentication selector

### About this task

Create an authentication selector as described in [Configuring the Requested AuthN Context Authentication Selector](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-103.pdf#page=233) (page 233).

### Steps

1. In PingFederate, go to **Authentication > Policies > Selectors**.

2. Click **Create New Instance** and enter the following values on the **Type** tab.

   | Parameter       | Value                                             |
   | --------------- | ------------------------------------------------- |
   | `Instance Name` | `PA Step Up Authentication`                       |
   | `Instance Id`   | `PAStepUpAuth`                                    |
   | `Type`          | `Requested AuthN Content Authentication Selector` |

3. On the **Authentication Selector** tab, select the **Field Value** checkbox next to **Add or Update Authn Context Attribute**. Click **Next**.

4. On the **Selector Result Values** tab, add `htmlForm` and `pingid` as **Result Values**. Click **Next**.

5. On the **Summary** tab, click **Save**.

## Creating an authentication policy tree

### About this task

Create an authentication policy tree, as described in [Defining authentication policies](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-103.pdf#page=242) (page 242).

### Steps

1. Go to **IdP Configuration > Authentication Policies → Policies**.

2. Click **Enable IdP Authentication Policies**.

3. In the **Action** list, select your authentication selector

4. For the `htmlForm success` result, click **Contract Mapping** to enable your authentication policy to fulfill the contract based on a username submitted on an HTML form.

5. For the `pingid success` result, click **Options** to link the form source with the `username` attribute.

6. For the `pingid success` result, click **Contract Mapping** to enable your authentication policy to fulfill the contract based on passing the username through PingID.

## Adding an OAuth authentication policy mapping

### Before you begin

Optionally, go to **OAuth settings → Token & Attribute Mapping → IdP Adapter Mapping** to remove any existing identity provicer (IdP) adapter mappings.

### Steps

1. In PingFederate, go to **Authentication → OAuth → Policy Contract Grant Mapping**.

2. In the **Mappings** section, in the **Policy Contract** list, select the authentication policy contract that you created earlier and click **Add Mapping**.

3. Click **Next**.

4. On the **Contract Fulfillment** tab, in the **USER\_KEY** row:

   * In the **Source** list, select **Authentication Policy Contract**.

   * In the **Value** list, select **subject**.

5. In the **USER\_NAME** row:

   * In the **Source** list, select **Authentication Policy Contract**.

   * In the **Value** list, select **subject**.

6. Click **Next** until you reach the **Summary** tab.

7. Click **Save**.

## Adding access settings and policy rules in PingAccess

### Steps

1. In PingAccess, to add access settings for `htmlForm` and `pingid`, go to **Access > Authentication > Authentication Requirements**.

   You can find more information in [Configuring an authentication requirements list](https://docs.pingidentity.com/pingaccess/7.2/pingaccess_user_interface_reference_guide/pa_adding_an_authn_requirements_rule.html).

2. To add rules as described in [Rule Management](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-63.pdf#page=268) (page 268), go to **Access > Rules**:

   1. Create a Step Up Authentication rule for PingAccess.

   2. Create an HTML Form Authentication rule.

3. Go to **Applications > Applications**, expand your application, and click the **Pencil** ([icon: pencil, set=fa]) icon to edit:

   1. On the **Resources** tab, expand the **Root Resource** and click the **Pencil** ([icon: pencil, set=fa]) icon to edit.

   2. On the **Web Policy** tab, under **Available Rules**, click the **[icon: plus, set=fa]**icon next to your Step Up Authentication rule from the previous step. Click **Save**.

      Learn more in [Rule Management](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-63.pdf#page=268) (page 268).

---

---
title: Configuring offline MFA with PingID
description: Components
component: solution-guides
page_id: solution-guides:multi-factor_authentication_use_cases:htg_config_offline_mfa_pid
canonical_url: https://docs.pingidentity.com/solution-guides/multi-factor_authentication_use_cases/htg_config_offline_mfa_pid.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 16, 2022
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  related-links: Related links
---

# Configuring offline MFA with PingID

## Before you begin

**Components**

* PingID mobile app 1.8

* PingFederate 9.1

* PingID Integration Kit 2.4

|   |                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This use case was developed with the specified product versions. With more recent product versions, the general workflow should apply although specific menu options and screens might differ. |

Do the following:

* Make sure the components are installed and running.

* For offline multi-factor authentication (MFA) to work, you must configure it before a service disruption. The device information that is stored in the directory is only populated once the user has authenticated "normally."

## About this task

Follow these steps to set up offline MFA to use when the PingID infrastructure is unavailable due to a network outage or similar issue. When a user successfully authenticates while the service is online, PingID returns device information and a public key to PingFederate. PingFederate stores this information in the customer's directory. In the event of a disruption to the PingID service, PingFederate uses that device information to generate an encrypted QR code.![Workflow as described in text.](_images/bkq1564001137118.png)

## Steps

1. If you do not have the Java Cryptography Extension (JCE) unlimited policy files, download and install them from the Oracle web site at <https://www.oracle.com/java/technologies/downloads/archive/#JavaSE>.

2. If you use PingDirectory, update the Directory Schema as explained in [Configure an LDAP directory for client storage](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-91.pdf#page=184) (page 184).

3. Decide where to store device records.

   ### Choose from:

   * Store device records as an attribute on the user record in whatever directory the user records reside.

   * Store device records in a separate organizational unit (OU) that can be in a directory other than where the user records reside.

4. Configure PingID Adapter settings as described in [Configuring offline MFA (PingID adapter)](https://docs.pingidentity.com/pingid/pingid_integrations/pid_adapter_configuring_offline_mfa.html).

   * State Attribute: If you store the device records with the user records, set this value to `Bypass`.

   * Authentication During Errors: Passive relies on the heartbeat; Enforce will use offline for each attempt.

   * LDAP Data Store: If you store the device records separately from the user records, set the **pf-pingid-local-fallback** value to the directory in which to store the device records.

   * Encryption Key for Devices: When this key is changed, users need to authenticate online once before an outage occurs.

   * Distinguished Name Pattern: If you store the device records separately from the user records, set the pattern to specify where the device information is stored (for example, `CN={username},OU=PingID-Devices,DC=myDomain,DC=com`).

5. Test the offline MFA feature.

   ### Choose from:

   * Choose **Enforce offline authentication** for Authentication During Errors in your PingID Adapter settings.

   * Break the network. For example, set the PingID network to localhost.

6. **Optional:** To configure MFA on Windows while offline, store device information in the Windows registry instead of in Active Directory.

   You must configure the Windows behavior during installation.

## Related links

* [PingID Offline MFA](https://docs.pingidentity.com/pingid/pingid_offline_mfa/pid_offline_mfa.html)

* [Supporting multiple access mode](https://docs.pingidentity.com/pingid/pingid_integrations/pid_supporting_multiple_access_mode.html)

* [PingID Outage: What to do (support article)](https://support.pingidentity.com/s/article/PingID-Outage-What-to-do)

---

---
title: Configuring PingFederate for MFA-only VPN
description: PingFederate 9.3
component: solution-guides
page_id: solution-guides:multi-factor_authentication_use_cases:htg_config_pf_for_mfa_only_vpn
canonical_url: https://docs.pingidentity.com/solution-guides/multi-factor_authentication_use_cases/htg_config_pf_for_mfa_only_vpn.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 24, 2025
page_aliases: ["multi-factor_authentication_use_cases:htg_config_pf_for_mfa_only_vpn_connect_datastore.adoc", "multi-factor_authentication_use_cases:htg_config_pf_for_mfa_only_vpn_identifier_first.adoc", "multi-factor_authentication_use_cases:htg_config_pf_for_mfa_only_vpn_pid.adoc", "multi-factor_authentication_use_cases:htg_config_pf_for_mfa_only_vpn_authn_policy.adoc"]
section_ids:
  components: Components
  before-you-begin: Before you begin
  creating-a-datastore-connection: Creating a datastore connection
  about-this-task: About this task
  steps: Steps
  configuring-an-identifier-first-adapter: Configuring an Identifier First Adapter
  steps-2: Steps
  configuring-a-pingid-adapter: Configuring a PingID Adapter
  steps-3: Steps
  configuring-an-authentication-policy: Configuring an authentication policy
  steps-4: Steps
---

# Configuring PingFederate for MFA-only VPN

## Components

* PingFederate 9.3

* PingID

## Before you begin

* Verify that PingFederate 9.3 is installed and running.

* Register a PingID account as explained in [Register the PingID service](https://docs.pingidentity.com/pingid/pingid_integrations/registering_the_pid_service.html).

## Creating a datastore connection

### About this task

If you have already configured a data store connection in PingFederate, you can skip this task.

### Steps

1. If you have not already configured a data store connection, use the following steps to configure one:

2. Sign on to PingFederate.

3. Select **System > Data Stores** to open the **Data Stores** screen.

4. On the **Data Stores** screen, click **Add New Data Store**.

5. Type a name for the data store.

6. Select the type of data store you are connecting to, and click **Next**.

Depending on which data store you chose, click one of the following links for configuration instructions:

* **Database (JDBC)** - [Configuring a JDBC connection](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-93.pdf#page=167) (page 167)

* **Directory (LDAP)** - [Configuring an LDAP connection](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-93.pdf#page=170) (page 170)

* **REST API** - [Configuring a REST API data store](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-93.pdf#page=178) (page 178)

## Configuring an Identifier First Adapter

The Identifier First Adapter allows PingFederate to collect the user identifier and then determine how to challenge the user for credentials. Learn more in [Identifier First Adapter](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-93.pdf#page=710).

### Steps

1. Select **Identity Provider > Adapters**.

2. On the **Manage IdP Adapter Instances** screen, click **Create New Instance**.

3. Enter an **Instance Name** and an **Instance ID**. The Instance Name is any name you want to use to identify this adapter instance. The Instance ID is used internally, and cannot contain spaces or non-alphanumeric characters.

4. Select **Identifier First Adapter** in the **Type** list.

5. Click **Next**, and follow the instructions in [Configure an Identifier First Adapter instance](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-93.pdf#page=710) (page 710) to complete the configuration.

## Configuring a PingID Adapter

### Steps

1. Select **Identity Provider > Adapters**.

2. **On the Manage IdP Adapter Instances** screen, click **Create New Instance**.

3. Enter an **Instance Name** and an **Instance ID**.

   The Instance Name is any name you want to use to identify this adapter instance. The Instance ID is used internally, and cannot contain spaces or non-alphanumeric characters.

4. Select **PingID Adapter 2.5.1** in the **Type** list.

5. Click **Next**.

6. Click **Show Advanced Fields**.

7. Follow the instructions in [Use PingID for Primary Authentication](https://docs.pingidentity.com/pingid/pingid_integrations/configuring_a_pid_adapter_instance.html) to complete the configuration.

## Configuring an authentication policy

### Steps

1. Select **Identity Provider → Policies** to open the **Authentication Policies** screen.

2. Click **Add Policy**.

3. Enter a name for the policy and optionally a description.

4. In the **Policy** list, click the down-arrow and select the Identifier First Adapter that you configured in step 3. **Fail** and **Success** fields appear.

5. Under **Fail**, select **Restart**.

6. Under **Success**, click the down-arrow and select the PingID Adapter that you configured in step 4. **Fail** and **Success** fields are displayed again.

7. Under **Fail**, select **Done**.

8. Under **Success**, click the down-arrow, and select a Policy Contract.

   An example configuration is shown in the following figure.

   ![mow1564001139984](_images/mow1564001139984.png)

9. Under the PingID adapter in the **Success** field, click **Options**.

   ![oxs1564001140813](_images/oxs1564001140813.png)

10. In the **Incoming User ID** modal, select the Identifier First Adapter for the **Source** and **subject** for the **Attribute**.

    This configuration maps the user identifier to use with PingID MFA.

    ![xez1636744317440](_images/xez1636744317440.png)

11. Click **Done**.

12. Click **Contract Mapping** under the Policy Contract in the **Success** field.

    ![bxe1564001142363](_images/bxe1564001142363.png)

13. Click **Next** to view the **Contract Fulfillment** screen.

14. Select the Identifier First Adapter for the **Source** and **subject** for the **Attribute**.

    This configuration maps the attributes into your authentication policy contract.

    ![apm1564001142938](_images/apm1564001142938.png)

15. Click **Next**, and then click **Next** again to view the **Summary** screen.

16. Click **Done** to save your contract mapping, and then click **Done** again to save your authentication policy.

---

---
title: Configuring PingOne for Amazon Alexa account linking
description: To configure PingOne as an identity provider for Amazon Alexa Skills, perform the following steps.
component: solution-guides
page_id: solution-guides:multi-factor_authentication_use_cases:htg_config_p1_for_amazon_alexa_acct_linking
canonical_url: https://docs.pingidentity.com/solution-guides/multi-factor_authentication_use_cases/htg_config_p1_for_amazon_alexa_acct_linking.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 18, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
---

# Configuring PingOne for Amazon Alexa account linking

## About this task

To configure PingOne as an identity provider for Amazon Alexa Skills, perform the following steps.

## Steps

1. Build a new PingOne application.

   1. Sign on to your PingOne admin console.

   2. Go to **Connections > Applications**.

   3. Click **[icon: plus, set=fa]Application**.

   4. Click **Advanced Configuration** and then click **Configure OIDC**.

   5. Enter your application name. Click **Next**.

   6. Enter a dummy URL in the **Redirect URLs** field. Click **Save and Continue**.

      |   |                                                                 |
      | - | --------------------------------------------------------------- |
      |   | You will update the URL after you have configured Amazon Alexa. |

   7. On the **Grant Access** page, click **Save and Continue**.

   8. On the **Applications** page, click the expand icon on your new application and then click the pencil icon to edit.

   9. On the **Configuration** tab, click **Generate New Secret** and then configure your application using the following table as a guide.

      | Parameter                              | Value                                                                       |
      | -------------------------------------- | --------------------------------------------------------------------------- |
      | `Response Type`                        | `Code` and `Token`                                                          |
      | `Grant Type`                           | `Authorization Code`, `Implicit`, `Client Credentials`, and `Refresh Token` |
      | `Redirect URLs`                        | https\://www\.example.com                                                   |
      | `Token Endpoint Authentication Method` | `Client Secret Basic`                                                       |

      |   |                                                                                                                                             |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Copy your `Client ID,` `Client Secret`, `Authorization URL`, and `Token Endpoint`. They are required for Alexa skills configurations later. |

   10. On the **Access** tab, click the **Plus** icon for the `email` and `p1:read:user` scopes to add them to the **Scopes Grant** list. Click **Save**.

       |   |                                                                        |
       | - | ---------------------------------------------------------------------- |
       |   | You can add more scope grants, but only the previous two are required. |

   11. Return to the **Application** page and click the toggle to enable your application.

2. Build a new Amazon Alexa skill.

   1. Sign on to [Amazon Alexa Developer Console](https://developer.amazon.com/alexa).

   2. Go to **Your Alexa Consoles > Skills** and click **Create Skill**.

   3. Build your Alexa skill with a custom configuration.

      |   |                                                                                                                                                                                 |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | You can find more information on building an Alexa skill in [Steps to Build a Custom Skill](https://developer.amazon.com/docs/custom-skills/steps-to-build-a-custom-skill.html) |

3. Link your PingOne application to your Alexa skill.

   1. In your Alexa Developer Console, select your Alexa skill and click **Account Linking** on the sidebar.

   2. Enter the information for your PingOne application using the following table as a guide.

      | Parameter                                                                            | Value                                              |
      | ------------------------------------------------------------------------------------ | -------------------------------------------------- |
      | **Do you allow users to create an account or link to an existing account with you?** | `Enabled`                                          |
      | **Allow users to enable skill without account linking**                              | `Disabled`                                         |
      | **Authorization grant type**                                                         | `Auth Code Grant`                                  |
      | **Authorization URI**                                                                | Your PingOne Authorization URI                     |
      | **Access Token URI**                                                                 | Your PingOne Token Endpoint                        |
      | **Client ID**                                                                        | Your PingOne Client ID from step 9                 |
      | **Client Secret**                                                                    | Your PingOne Client Secret from step 9             |
      | **Client Authentication Scheme**                                                     | `HTTP Basic`                                       |
      | **Scope**                                                                            | `email`, `p1:read:user`, and `p1:read:environment` |
      | **Domain List**                                                                      | `auth.pingone.com` and `api.pingone.com`           |
      | **Default Access Token Expiration Time**                                             | `30`                                               |

      |   |                                                                                     |
      | - | ----------------------------------------------------------------------------------- |
      |   | Copy the URLs from the **Redirect URLs** field. They are required in the next step. |

4. Enter the redirect URLs from your Alexa skill into PingOne.

   1. Sign on to your PingOne admin console.

   2. Go to **Connections > Applications**.

   3. To edit your application, click the **Expand** icon and then click the **Pencil**.

   4. Click the **Configuration** tab and then paste the redirect URLs into the **Redirect URLs** field. Click **Save**.

5. To beta test your Alexa skills, register your Alexa Account as a beta tester.

   1. In your Alexa Developer Console, go to **Distribution > Availability** and expand the **Beta Test** section.

   2. Add your email address to **Beta Test Administrator Email Address** and click **Add**.

6. Test account linking on the Amazon Alexa site.

   1. Sign on to [Amazon Alexa](https://alexa.amazon.com).

   2. Locate your skill and then click **Link Account**.

   3. You will be redirected to PingOne. Provide your credentials.

      ### Result:

      After you've successfully linked, a confirmation screen will appear.

---

---
title: Integrating MFA with SSO (PingID with PingFederate)
description: Establish a quick connection between PingFederate and PingID.
component: solution-guides
page_id: solution-guides:multi-factor_authentication_use_cases:htg_integrate_mfa_with_sso_pid_with_pf
canonical_url: https://docs.pingidentity.com/solution-guides/multi-factor_authentication_use_cases/htg_integrate_mfa_with_sso_pid_with_pf.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 29, 2022
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  related-links: Related links
---

# Integrating MFA with SSO (PingID with PingFederate)

Establish a quick connection between PingFederate and PingID.

## Before you begin

**Components**

* PingFederate 10.2 and later

* PingID

* PingOne for Enterprise

|   |                                                                             |
| - | --------------------------------------------------------------------------- |
|   | PingID is hosted on Ping's cloud identity platform, PingOne for Enterprise. |

Do the following:

* Verify that PingFederate 10.2 or later is installed and running.

* Ensure that you have internet access.

* If you do not already have a PingOne for Enterprise account, create an account at <https://admin.pingone.com/web-portal/register>. You can find more information in [Registering the PingID service](https://docs.pingidentity.com/pingid/pingid_integrations/registering_the_pid_service.html).

## Steps

1. Sign on to the PingOne for Enterprise admin console at <https://admin.pingone.com/web-portal/login>.

2. On the **Setup** page, create a PingOne for Enterprise directory as explained in [Select PingOne for Enterprise Directory](https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_p1directory.html).

3. On the **Setup > PingID > Client Integration** page, make sure there is at least one PingID client in the **Integrate with PingFederate and Other Clients** section.

4. Click **Download** beside the PingID client to download the corresponding `pingid.properties` file.

   The `pingid.properties` file contains the connection information that PingFederate needs to connect to your PingID instance.

5. Configure the PingID Adapter in PingFederate as explained in [Managing IdP adapters](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-102.pdf#page=389) (page 389).

## Related links

* [PingID Administration Guide](https://docs.pingidentity.com/pingid/pid_landing_page.html)

* [Integrating PingID with PingFederate through APIs](../developer_api_use_cases/htg_integrate_pid_pf_thru_apis.html)

---

---
title: Multi-factor Authentication Use Cases
description: Adding multi-factor authentication to secure apps (PingID with PingAccess)
component: solution-guides
page_id: solution-guides:multi-factor_authentication_use_cases:htg_mfa_user_cases
canonical_url: https://docs.pingidentity.com/solution-guides/multi-factor_authentication_use_cases/htg_mfa_user_cases.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 24, 2025
---

# Multi-factor Authentication Use Cases

| Use case                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Adding multi-factor authentication to secure apps (PingID with PingAccess)](htg_add_mfa_to_secure_apps_pid_with_pa.html)                              | Learn how to synchronize a session for your web applications between PingFederate and PingAccess through PingID.                                                                                                                                                                                                                                                                                   |
| [Configuring offline MFA with PingID](htg_config_offline_mfa_pid.html)                                                                                 | Learn how to configure offline MFA with PingID to use when the PingID infrastructure is unavailable due to a network outage or similar issue.                                                                                                                                                                                                                                                      |
| [Configuring PingFederate for MFA-only VPN](htg_config_pf_for_mfa_only_vpn.html)                                                                       | Learn how to configurePingFederate for MFA-only VPN.                                                                                                                                                                                                                                                                                                                                               |
| [Configuring PingOne for Amazon Alexa account linking](htg_config_p1_for_amazon_alexa_acct_linking.html)                                               | Learn how to configure PingOne for Amazon Alexa account linking.                                                                                                                                                                                                                                                                                                                                   |
| [Integrating MFA with SSO (PingID with PingFederate)](htg_integrate_mfa_with_sso_pid_with_pf.html)                                                     | Establish a quick connection between PingFederate and PingID.                                                                                                                                                                                                                                                                                                                                      |
| [Securing your VPN with MFA through PingID](htg_secure_vpn_with_mfa_pid.html)                                                                          | To enable PingID for VPN, use PingFederate Bridge and the PingOne for Enterprise admin portal. This secures your VPN with multi-factor authentication (MFA).                                                                                                                                                                                                                                       |
| [Setting up multi-factor authentication with Ping Identity products](htg_mfa_with_ping_products.html)                                                  | Multi-factor authentication (MFA) is used to ensure that digital users are who they say they are by requiring that they provide at least two pieces of evidence to prove their identity. Each piece of evidence must come from a different category: something they know, something they have, or something they are. Ping Identity provides a number of products and methods for configuring MFA. |
| [Using SAML and token exchange to federate into AWS through the AWS Command Line Interface](htg_use_saml_and_token_exchange_to_federate_into_aws.html) | This use case shows you how to use PingFederate to issue a token to Amazon Web Services (AWS) to authenticate an end-user for API access.                                                                                                                                                                                                                                                          |

---

---
title: Securing your VPN with MFA through PingID
description: To enable PingID for VPN, use PingFederate Bridge and the PingOne for Enterprise admin portal. This secures your VPN with multi-factor authentication (MFA).
component: solution-guides
page_id: solution-guides:multi-factor_authentication_use_cases:htg_secure_vpn_with_mfa_pid
canonical_url: https://docs.pingidentity.com/solution-guides/multi-factor_authentication_use_cases/htg_secure_vpn_with_mfa_pid.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 24, 2025
page_aliases: ["multi-factor_authentication_use_cases:htg_secure_vpn_with_mfa_pid_p14e.adoc", "multi-factor_authentication_use_cases:htg_secure_vpn_with_mfa_pid_vpn_pfbridge.adoc", "multi-factor_authentication_use_cases:htg_secure_vpn_with_mfa_pid_pfbridge.adoc"]
section_ids:
  components: Components
  before-you-begin: Before you begin
  enabling-pingid-for-vpn-through-the-pingone-for-enterprise-admin-portal: Enabling PingID for VPN through the PingOne for Enterprise admin portal
  about-this-task: About this task
  steps: Steps
  result: Result:
  enable-pingid-vpn-thru-pfbridge: Enabling PingID for VPN through PingFederate Bridge
  about-this-task-2: About this task
  steps-2: Steps
  result-2: Result:
  result-3: Result:
  configure-pingid-vpn-with-pfbridge: Configuring PingID for VPN with PingFederate Bridge
  steps-3: Steps
  result-4: Result
---

# Securing your VPN with MFA through PingID

To enable PingID for VPN, use PingFederate Bridge and the PingOne for Enterprise admin portal. This secures your VPN with multi-factor authentication (MFA).

## Components

* PingOne for Enterprise

* PingFederate Bridge (available through PingOne for Enterprise)

## Before you begin

You must have:

* A PingOne for Enterprise admin portal account

  You can sign up for a free trial of PingOne for Enterprise.

* An instance of PingFederate Bridge

## Enabling PingID for VPN through the PingOne for Enterprise admin portal

### About this task

You can enable PingID for VPN through the PingOne for Enterprise admin portal or PingFederate Bridge. To enable PingID VPN through the PingOne for Enterprise admin portal:

### Steps

1. Sign on to the PingOne for Enterprise admin portal.

2. Click **Setup**.

3. Click **PingID → Client Integration**.

4. Click **Setup PingFederate for PingID**.

   ![Screen capture of the Client Integration tab. At the bottom, two buttons read Generate and Setup for , the latter is highlighted with a red box. The text above reads: Integrate with and Other Clients and Use these properties files to Integrate with external clients such as AD FS, SSH, VPN, Windows Login (servers) or APIs. These files will contain sensitive information such as encryption keys. Two buttons read Download and Revoke. Across the top, the tabs read Configuration, Client Integration, Branding, Device and Pairing, and Policy.](_images/skl1602610223192.png)

5. To choose your server platform, follow the on-screen instructions.

6. To download PingFederate Bridge, follow the on-screen instructions.

7. To install and configure PingFederate Bridge, follow the on-screen instructions.

   |   |                                                                  |
   | - | ---------------------------------------------------------------- |
   |   | *Your Server Domain* is your fully qualified domain name (FQDN). |

8. In the PingFederate administrative console, review the license agreement. Click **Accept**.

9. In the PingOne for Enterprise admin portal, in the**Install and Configure PingFederate Bridge** section, from the **Complete Quick Start** section, copy the activation key.

   ![Screen capture of the Complete Quick Start section. The Activation Key field is highlighted with a red box. Below the activation key field reads: To connect to your PingOne account, copy this unique activation key into when prompted. This is a single-use activation key. A new key will be generated for each PingOne session.](../_images/ebu1602608416395.png)

10. In the PingFederate administrative console, click **Yes, Connect to PingOne for Enterprise**.

11. In the **Activation Key** field, paste the activation key you copied from the PingOne for Enterprise admin portal. Click **Next**.

    #### Result:

    The PingFederate administrative console displays the **Identities** section.

12. Proceed to [Configuring PingID for VPN with PingFederate Bridge](#configure-pingid-vpn-with-pfbridge).

## Enabling PingID for VPN through PingFederate Bridge

### About this task

You can enable PingID for VPN through the PingOne for Enterprise admin portal or PingFederate Bridge.

### Steps

1. Install PingFederate from the [Ping Identity Downloads Page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html).

2. Start the PingFederate server by running this script: `<YOUR PINGFEDERATE DIRECTORY>/pingfederate/bin/run.sh`.

3. Open the PingFederate administrative console.

   1. Open a browser and enter `https://Your Server Domain:9999/pingfederate/app`.

      |   |                                                                  |
      | - | ---------------------------------------------------------------- |
      |   | *Your Server Domain* is your fully qualified domain name (FQDN). |

   2. To proceed, review the license agreement. Click **Accept**.

4. Click **Yes, Connect to PingOne for Enterprise**.

5. Click **Sign on to PingOne for Enterprise** and enter your credentials to sign on.

   #### Result:

   The admin portal displays the activation key.

6. Copy the activation key from the PingOne for Enterprise admin portal to your clipboard.

7. In the PingFederate administrative console, in the **Activation Key** field, paste the key value.

8. Click **Next**.

   #### Result:

   The PingFederate administrative console displays the **Identities** section.

9. [Configuring PingID for VPN with PingFederate Bridge](#configure-pingid-vpn-with-pfbridge).

## Configuring PingID for VPN with PingFederate Bridge

### Steps

1. From the PingFederate administrative console **Identities** section, select **Yes, Connect a Directory Server**.

2. Enter information in the fields that is appropriate for your directory server.

   | Field                  | Description                                                                                                                                                                                                                                                                                                                                                                                                       |
   | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Directory Type**     | Select the type of directory server from the list.                                                                                                                                                                                                                                                                                                                                                                |
   | **Data Store Name**    | Enter the name of the datastore.                                                                                                                                                                                                                                                                                                                                                                                  |
   | **Hostname**           | Enter the fully qualified domain name (FQDN) for your directory server.                                                                                                                                                                                                                                                                                                                                           |
   | **Service Account DN** | Enter the distinguished name (DN) of the service account that PingFederate can use to communicate with the directory server.                                                                                                                                                                                                                                                                                      |
   | **Password**           | Enter the password associated with the service account.                                                                                                                                                                                                                                                                                                                                                           |
   | **Search Base**        | Enter the DN of the location in the directory where PingFederate begins its datastore queries.                                                                                                                                                                                                                                                                                                                    |
   | **Search Filter**      | Specify how the username provided by a user at login is mapped to an attribute in your directory.The default value is either `sAMAccountName=${username}` or `uid=${username}`, depending on the selected directory type.If you require a more advanced search filter, enter the value in the following format: `<Your attribute Name>=${username}`. For more information, consult your directory administrators. |

3. Click **Next**.

   |   |                                                                                                                                                                                                                                   |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If your directory server is SSL-enabled and presents an untrusted certificate, PingFederate prompts you to upload the server's certificate. Click **Choose Certificate**, select the appropriate certificate, and click **Next**. |

4. In the **Use Cases** section, select the **PingID VPN (RADIUS)** checkbox. Click **Begin**.

5. In the **Basic Settings** section, configure the basic settings:

   1. In the **Client IP** field, enter the IP address of the VPN server.

   2. In the **Client Shared Secret** field, enter the secret shared between the VPN server and PingFederate Bridge.

   3. Verify that the **Validate with LDAP** checkbox is selected.

   4. In the **PingID Username Attribute** field, enter the value you entered in the **Search Filter** field in step 2.

      |   |                                                               |
      | - | ------------------------------------------------------------- |
      |   | The integrated RADIUS server listens on port 1812 by default. |

6. Click **Next**.

7. In the **Provisioning** section, the **Configure Provisioning** checkbox should be unselected. Click **Next**.

8. In the **Summary** section, review your configuration. Click **Done**.

9. Click **Next**.

10. In the **Basic Information** section, in the **Base URL** field, enter `https://Your Server Domain:9031`.

    |   |                                                                  |
    | - | ---------------------------------------------------------------- |
    |   | *Your Server Domain* is your fully qualified domain name (FQDN). |

11. Click **Next**.

12. To apply the configuration to PingFederate Bridge, click **Next**.

13. Click **Done**.

### Result

PingID for VPN is enabled in PingFederate Bridge for use.

|   |                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can find more information on configuring your VPN client/server settings in [Integrating PingID with your VPN/Remote access system](https://docs.pingidentity.com/pingid/pingid_integrations/pid_integration_with_vpn_intro.html). |

---

---
title: Setting up multi-factor authentication with Ping Identity products
description: "Multi-factor authentication (MFA) is used to ensure that digital users are who they say they are by requiring that they provide at least two pieces of evidence to prove their identity. Each piece of evidence must come from a different category: something they know, something they have, or something they are. Ping Identity provides a number of products and methods for configuring MFA."
component: solution-guides
page_id: solution-guides:multi-factor_authentication_use_cases:htg_mfa_with_ping_products
canonical_url: https://docs.pingidentity.com/solution-guides/multi-factor_authentication_use_cases/htg_mfa_with_ping_products.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 2, 2024
section_ids:
  configuring-mfa-with-pingid: Configuring MFA with PingID
  configuring-mfa-with-pingfederate-and-pingone: Configuring MFA with PingFederate and PingOne
  integrating-mfa-with-sso-using-pingid-and-pingfederate: Integrating MFA with SSO using PingID and PingFederate
  setting-up-mfa-for-pingone: Setting up MFA for PingOne
  configuring-mfa-for-the-pingfederate-administrative-console-using-pingid: Configuring MFA for the PingFederate administrative console using PingID
---

# Setting up multi-factor authentication with Ping Identity products

Multi-factor authentication (MFA) is used to ensure that digital users are who they say they are by requiring that they provide at least two pieces of evidence to prove their identity. Each piece of evidence must come from a different category: something they know, something they have, or something they are. Ping Identity provides a number of products and methods for configuring MFA.

## Configuring MFA with PingID

PingID MFA is a strong authentication solution that allows you to authenticate to your app, application portal, or desktop machine using additional authentication methods, such as your mobile device, to enhance security and provide ease of access to your apps. You can find more information in the following sections in the [*PingID End User Guide*](https://docs.pingidentity.com/pingid-user-guide/secure_authentication_with_pingid/pid_end_user_guide.html).

* [PingID authentication for the web](https://docs.pingidentity.com/pingid-user-guide/secure_authentication_with_pingid/pid_ug_authentication_for_the_web.html): You can use PingID as a second factor of authentication when accessing multiple web applications in your browser or mobile device.

* [PingID authentication for VPN](https://docs.pingidentity.com/pingid-user-guide/secure_authentication_with_pingid/pid_ug_authentication_for_vpn.html): You can use PingID as a second factor of authentication when accessing your VPN or any remote access clients that support the RADIUS protocol.

* [PingID authentication for Windows login](https://docs.pingidentity.com/pingid-user-guide/secure_authentication_with_pingid/ug_pid_authentication_for_windows_login.html): Using a supported, paired device, you can use PingID to authenticate to your Windows machine using either passwordless or second-factor authentication.

* [PingID authentication for Mac login](https://docs.pingidentity.com/pingid-user-guide/secure_authentication_with_pingid/pid_ug_mac_login_auth.html): Using a supported, paired device, you can use PingID as a second factor of authentication when signing on to your Apple Mac machine.

## Configuring MFA with PingFederate and PingOne

The PingOne MFA Integration Kit allows PingFederate to use the PingOne MFA service for multi-factor authentication (MFA). This allows you to integrate MFA into SAML, WS-Fed, OAuth, and OIDC flows in a seamless way leveraging one configuration for all use cases. Learn more in [PingOne MFA Integration Kit](https://docs.pingidentity.com/integrations/pingone/pingone_mfa_integration_kit/pf_p1_mfa_ik.html).

## Integrating MFA with SSO using PingID and PingFederate

You can configure PingID with PingFederate to establish a connection between the two products for the purpose of integrating MFA with single-signon (SSO) capabilities. This allows you to integrate MFA into SAML, WS-Fed, OAuth, and OIDC flows in a seamless way leveraging one configuration for all use cases. For more information, see [Integrating MFA with SSO (PingID with PingFederate)](https://docs.pingidentity.com/solution-guides/multi-factor_authentication_use_cases/htg_integrate_mfa_with_sso_pid_with_pf.html).

## Setting up MFA for PingOne

PingOne MFA is a cloud-based service that enables customers to protect their organization's network, applications, and data resources. You can use the MFA service to integrate MFA into your applications that leverage PingOne SSO. You can find instructions on configuring PingOne MFA in [Getting started with PingOne MFA](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_getting_started_with_strong_authentication_mfa.html).

## Configuring MFA for the PingFederate administrative console using PingID

PingID is a cloud service that enables multi-factor authentication using a mobile application. The PingFederate administrative console supports authentication through the RADIUS protocol, which provides a common approach for implementing strong authentication in a client-server configuration.

By combining these two capabilities, you can configure PingID to provide MFA to protect access to the PingFederate administrative console, which meets the requirement of stronger authentication for administrators accessing security-related software products.

You can find instructions on configuring MFA for the PingFederate administrative console in [Multi-factor console authentication using PingID](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_multifactor_console_authentication_using_pid.html).

---

---
title: Using SAML and token exchange to federate into AWS through the AWS Command Line Interface
description: This use case shows you how to use PingFederate to issue a token to Amazon Web Services (AWS) to authenticate an end-user for API access.
component: solution-guides
page_id: solution-guides:multi-factor_authentication_use_cases:htg_use_saml_and_token_exchange_to_federate_into_aws
canonical_url: https://docs.pingidentity.com/solution-guides/multi-factor_authentication_use_cases/htg_use_saml_and_token_exchange_to_federate_into_aws.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 24, 2025
page_aliases: ["multi-factor_authentication_use_cases:htg_use_saml_and_token_exchange_to_federate_into_aws_pf_sp_connect.adoc", "multi-factor_authentication_use_cases:htg_use_saml_and_token_exchange_to_federate_into_aws_download_jar.adoc", "multi-factor_authentication_use_cases:htg_use_saml_and_token_exchange_to_federate_into_aws_change_sys_props.adoc", "multi-factor_authentication_use_cases:htg_use_saml_and_token_exchange_to_federate_into_aws_create_token.adoc", "multi-factor_authentication_use_cases:htg_use_saml_and_token_exchange_to_federate_into_aws_use_ws_trust_sts.adoc", "multi-factor_authentication_use_cases:htg_use_saml_and_token_exchange_to_federate_into_aws_get_security_token.adoc"]
section_ids:
  component: Component
  before-you-begin: Before you begin
  create-new-sp-connection-in-pf: Creating a new SP connection in PingFederate
  about-this-task: About this task
  steps: Steps
  downloading-aws-jar-files: Downloading AWS .jar files
  steps-2: Steps
  modifying-pingfederate-system-properties: Modifying PingFederate system properties
  about-this-task-2: About this task
  steps-3: Steps
  creating-a-token-processor: Creating a token processor
  steps-4: Steps
  changing-the-aws-saml-connection-to-use-ws-trust-sts: Changing the AWS SAML connection to use WS-Trust STS
  about-this-task-3: About this task
  steps-5: Steps
  writing-a-script-to-get-the-security-token-from-aws: Writing a script to get the security token from AWS
  about-this-task-4: About this task
  steps-6: Steps
---

# Using SAML and token exchange to federate into AWS through the AWS Command Line Interface

This use case shows you how to use PingFederate to issue a token to Amazon Web Services (AWS) to authenticate an end-user for API access.

You can automate getting the AWS Access Key ID and AWS Secret Access Key (which are your account credentials) by using PingFederate to authenticate against the user store (such as ActiveDirectory), get a SAML assertion to federate into AWS, and then exchange the SAML assertion for an access token to make CLI commands to AWS.

## Component

PingFederate 9.2

## Before you begin

Make sure of the following:

* PingFederate 9.2 is installed and running.

* You have a functioning AWS SP SAML connection in PingFederate. To accomplish this, install the AWS Connector and the AWS CLI tool. For documentation on the AWS Command Line Interface (CLI), see the [Amazon CLI User Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html).

  |   |                                                                                                                                                                                                                                                                                                                                  |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The CLI tool is installed on your hard drive (usually in a hidden folder) and includes two files: `config` and `credentials`. The credentials file is where the ID and Key are stored and look similar to this:```
  aws_access_key_id = ARIAIY4DSCACQLFZSULQ
  aws_secret_access_key = /zf8dHb2FDJQ0IPxQZeoOLftZ5gif0ve6f8gibtu
  ``` |

## Creating a new SP connection in PingFederate

### About this task

There are three main contract attributes you need to define in the SP configuration:

* SAML\_SUBJECT

* https\://aws.amazon.com/SAML/Attributes/Role

* https\://aws.amazon.com/SAML/Attributes/RoleSessionName

The AWS metadata URL (<https://signin.aws.amazon.com/static/saml-metadata.xml>) includes these attributes and will simplify making the SP connection in PingFederate.

### Steps

1. Log in to the PingFederate Administration console.

2. In the **SP Connections** section of the **Identity Provider** tab, click **Create New**.

3. Select **Browser SSO Profiles**. Click **Next**.

4. On the **Connection Options** tab, select the **Browser SSO** checkbox and click **Next**.

5. On the **Import Metadata** tab, select `URL`, **Manage Partner Metadata URLs**, then **Add New URL**.

6. Add the AWS metadata URL (https\://signin.aws.amazon.com/static/saml-metadata.xml), then click **Next**. Click **Save**.

7. Select the AWS metadata URL from the **Metadata URL** list on the **Import Metadata** tab and then click **Load Metadata**. Click **Next**.

8. On the **General Info** tab, name your connection in the **Connection Name** field. Click **Next**.

9. On the **Browser SSO** tab, click **Configure Browser SSO**. Select the **IDP-Initiated SSO** and **SP-Initiated SSO** checkboxes and click **Next** until you reach the **Assertion Creation** tab. Click **Configure Assertion Creation**.

10. On the **Attribute Contract** tab, select `urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified` from the **Subject Name Format** list for `SAML_SUBJECT` . Click **Next**.

    |   |                                                                                                                                                                                                           |
    | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | There are several extra attributes included in the AWS metadata URL (such as `urn:oid:1.3.6.1.4.1.5923.1.1.1.1`). These attributes are not required and can be deleted on the **Attribute Contract** tab. |

11. On the **Authentication Source Mapping** tab, click **Map New Adapter Instance**.

12. Select your adapter instance and click **Next** until you reach the **Attribute Contract Fulfillment** tab.

13. On the **Attribute Contract Fulfillment** tab, select `Text` from the **SAML\_SUBJECT** **Source** list and in the **SAML\_SUBJECT** **Value** field, enter `null`.

14. Select `Text` from the **https\://aws.amazon.com/SAML/Attributes/Role** **Source** field and in the **https\://aws.amazon.com/SAML/Attributes/Role** `Value` field, enter the value using the following example:

    ```
    arn:aws:iam::<your AWS instance number>:role/<your Role you created in AWS>,arn:aws:iam::<your AWS instance number>:saml-provider/<your SAML Provider you created in AWS>
    ```

15. Select `Adapter` from the **https\://aws.amazon.com/SAML/Attributes/RoleSessionName** **Source** list and select `username` from the **Value** list. Click **Next** and **Done** until you complete the IdP Adapter Mapping.

16. Click **Next**. Click **Done** to complete the Assertion Creation configuration.

17. On the **Protocol Settings** tab, click **Configure Protocol Settings**.

18. On the **Allowable SAML Bindings** tab, clear the `Artifact` and `Soap` checkboxes and then click **Next** and **Done** until you complete the Protocol Settings configuration.

19. Click **Next** then **Done** to complete the Browser SSO configuration.

20. On the **Credentials** tab, click **Configure Credentials** and then select a signing certificate from the **Signing Certificate** list. Click **Done**.

21. Click **Save** on the **Activation and Summary** tab to complete the SP connection configuration.

## Downloading AWS .jar files

### Steps

* Now that you have a functioning SAML connection between your PingFederate and AWS instances, download and install the following:

  * `aws-java-sdk-1.11.604.jar` from `aws-java-sdk-1.11.604`. This is available from [AWS Downloads](https://sdk-for-java.amazonwebservices.com/latest/aws-java-sdk.zip).

  * All `.jar` files from `lib` of `PingFederate_WS-Trust_STS_Client_SDK-1.1.1`. This is available from PingIdentity.

## Modifying PingFederate system properties

### About this task

Set the `pf.idp.wstrust.samlp.resp` system property to `true`.

### Steps

1. Do one of the following depending on how you are running PingFederate:

   * If your PingFederate is running as a Windows service, this is done in `<PF install location>\pingfederate\sbin\wrapper\PingFederateService.conf`

     1. Find the `# Java Additional Parameters` section.

     2. Attribute the next number in the list to a `wrapper.java.additional` parameter. For example: `wrapper.java.additional.15=-Dpf.idp.wstrust.samlp.resp=true`

   * If you are not running PingFederate as a Windows service, you will need to append the appropriate run file in the bin folder (`run.bat` or `run.sh`). For example, in `run.sh` add `JAVA_OPTS="$JAVA_OPTS -Dcom.ncipher.provider.announcemode=on -Dpf.idp.wstrust.samlp.resp=true"`

2. Restart PingFederate. Learn more in [Start and stop PingFederate](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-92.pdf#page=22) (page 22).

## Creating a token processor

### Steps

1. In the PingFederate Administrative console, click the **System** tab and then click **Protocol Settings.** Click the **Roles & Protocols** tab.

2. Select the **WS-Trust** checkbox for IDP roles. Click **Save**.

3. On the **Identity Provider** tab, click **Token Processors** and then click **Create New Instance**.

4. Enter the appropriate values in the **Instance Name** and **Instance ID** fields. From the **Type** menu, select **Username Token Processor**. Click **Next**.

5. From the `Password Credential Validator Instance` menu, select your password credential validator instance. Click **Next**.

6. Click **Next** and **Done** until you complete the Token Processor Instance configuration.

   |   |                                                            |
   | - | ---------------------------------------------------------- |
   |   | Only the `username` attribute is required in the Contract. |

## Changing the AWS SAML connection to use WS-Trust STS

### About this task

Change the AWS SP SAML connection to use the STS processor and map the attributes.

### Steps

1. On the **Identity Provider** tab, from the **SP connections** list, select your AWS connection.

2. Click **Connection Type** and select the **WS-Trust STS** checkbox. Click **Next**.

3. On the **WS-Trust STS** tab, click **Configure WS-Trust STS** and enter `https://signin.aws.amazon.com/saml` in the **Partner Service Identifier** field. Click **Add** and then click **Next**.

4. On the **Token Creation** screen, click **Configure Token Creation**.

5. Enter `https://aws.amazon.com/SAML/Attributes/Role` in the **Extend the Contract** field. Click **Add**.

6. Enter `https://aws.amazon.com/SAML/Attributes/RoleSessionName` in the **Extend the Contract** field and click **Add**. Click **Next**.

7. On the **IdP Token Processor Mapping** tab, click **Map New Token Processor Instance** and specify the token processor. Click **Next**.

8. Map the **Attribute Contract Fulfillment** section. See steps 13 - 15 in [Creating a new SP connection in PingFederate](#create-new-sp-connection-in-pf).

9. Click **Next** and **Save** on the **Summary** tab.

## Writing a script to get the security token from AWS

### About this task

Write a script to automate the authentication and get the security token from AWS.

### Steps

* The following template is an example script written in `.java`, exported as a runnable `.jar` file, and executed in a terminal window.

  |   |                                                       |
  | - | ----------------------------------------------------- |
  |   | You can write your automation script in any language. |

  ```java
  package com.pingidentity.sts;
  import com.amazonaws.auth.AnonymousAWSCredentials;
  import com.amazonaws.services.securitytoken.AWSSecurityTokenServiceClient;
  import com.amazonaws.services.securitytoken.model.AssumeRoleWithSAMLRequest;
  import com.amazonaws.services.securitytoken.model.AssumeRoleWithSAMLResult;
  import com.pingidentity.sts.clientapi.STSClient;
  import com.pingidentity.sts.clientapi.STSClientConfiguration;
  import com.pingidentity.sts.clientapi.model.RequestSecurityTokenData;
  import com.pingidentity.sts.clientapi.model.STSResponse;
  import com.pingidentity.sts.clientapi.tokens.wsse.UsernameToken;
  import java.util.Scanner;
  public class AssumeRoleWithSAMLSample {
    private static final String PING_STS = "";
    https://<pingfedserver>:9031/idp/sts.wst
    private static final String PRINCIPAL_ARN = "arn:aws:iam::736827903656:saml-provider/PingFed";
    private static final String ROLE_ARN = "arn:aws:iam::736827903656:role/Administrators";
  public static void main(String[] args) throws Exception {
    AssumeRoleWithSAMLSample sample = new AssumeRoleWithSAMLSample();
    sample.getTemporaryCredential(sample.getSAMLAssertion());
  }
  protected String getTemporaryCredential (String assertion) {
    AWSSecurityTokenServiceClient client = new AWSSecurityTokenServiceClient(new AnonymousAWSCredentials());
    AssumeRoleWithSAMLRequest assumeRoleRequest = new AssumeRoleWithSAMLRequest();
    assumeRoleRequest.setPrincipalArn(PRINCIPAL_ARN);
    assumeRoleRequest.setRoleArn(ROLE_ARN);
    assumeRoleRequest.setSAMLAssertion(assertion);
    AssumeRoleWithSAMLResult result = client.assumeRoleWithSAML(assumeRoleRequest);
    System.out.println(result.toString());
    return result.toString();
  }
  protected String getSAMLAssertion () throws Exception {
    Scanner user_input = new Scanner( System.in );
    String username;
    String password;
    System.out.print("Enter your AD UserID: ");
    username = user_input.next();
    System.out.print("Enter your AD Password: ");
    password = user_input.next();
    System.out.println("Getting assertion from PingFederate . . .");
    STSClientConfiguration stsClientConfiguration = new STSClientConfiguration();
    stsClientConfiguration.setStsEndpoint(PING_STS);
    stsClientConfiguration.setIgnoreSSLTrustErrors(true);
    STSClient client = new STSClient(stsClientConfiguration);
    RequestSecurityTokenData requestData = new RequestSecurityTokenData();
    requestData.setRequestType("");
    http://docs.oasis-open.org/ws-sx/ws-trust/200512/Issue
    requestData.setTokenType("urn:oasis:names:tc:SAML:2.0:profiles:SSO:browser");
    requestData.setAppliesTo("");
    https://signin.aws.amazon.com/saml
    org.w3c.dom.Element token = null;
    UsernameToken usernameToken = new UsernameToken();
    usernameToken.setUsername(username);
    usernameToken.setPassword(password);
    token = usernameToken.getRoot();
    STSResponse respData;
    respData = client.makeRequest(requestData, token, null, null);
    String result = respData.getRstr().getToken().getFirstChild().getTextContent();
    System.out.println("Returninig " + result);
    return result;
    }
  }
  ```