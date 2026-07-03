---
title: Adding multi-factor authentication to secure apps (PingID with PingAccess)
description: Learn how to synchronize a session for your web applications between PingFederate and PingAccess through PingID
component: solution-guides
page_id: solution-guides:multi-factor_authentication_use_cases:htg_add_mfa_to_secure_apps_pid_with_pa
canonical_url: https://docs.pingidentity.com/solution-guides/multi-factor_authentication_use_cases/htg_add_mfa_to_secure_apps_pid_with_pa.html
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
