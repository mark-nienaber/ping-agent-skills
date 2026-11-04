---
title: Accessing the application portal
description: Learn how to access the PingOne application portal to verify the multi-factor authentication experience as a simulated user.
component: pingone
page_id: pingone:pingone_tutorials:p1_tutorial_aplication_portal
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_tutorial_aplication_portal.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-28T00:00:00Z
section_ids:
  steps: Steps
---

# Accessing the application portal

Review each user's available applications by accessing the Application Portal.

## Steps

1. Go to **Applications > Applications**.

2. Expand the **PingOne Application Portal** application.

3. Click the **Policies** tab, and click the **Pencil** icon to edit.

4. Click **[icon: plus, set=fa]**to add **Multi_Factor** to**Applied Policies**.

5. Click **Save**.

6. Go to **Environment → Properties**.

7. Click the **Application Portal URL**.

8. Sign on with each user to review the applications that are available to them.

---

---
title: Accessing the application portal
description: Learn how to access the PingOne application portal to verify the passwordless login experience as a user.
component: pingone
page_id: pingone:pingone_tutorials:p1_tutorial_aplication_portal_passwordless
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_tutorial_aplication_portal_passwordless.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-28T00:00:00Z
section_ids:
  steps: Steps
---

# Accessing the application portal

Review each user's available applications by accessing the application portal.

## Steps

1. Go to **Applications > Applications**.

2. Expand the **PingOne Application Portal** application.

3. Click the **Policies** tab, and click the **Pencil** icon to edit.

4. Click **[icon: plus, set=fa]**to add **Multi_Factor** to**Applied Policies**.

5. Click **Save**.

6. Go to **Environment → Properties**.

7. Click the **Application Portal URL**.

8. Sign on with each user to review the applications that are available to them.

---

---
title: Add custom attributes to a user
description: Learn how to add custom attributes to a PingOne user to define what types of data are stored for each user.
component: pingone
page_id: pingone:pingone_tutorials:p1_add_custom_attributes_to_a_user
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_add_custom_attributes_to_a_user.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-28T00:00:00Z
section_ids:
  steps: Steps
---

# Add custom attributes to a user

Learn how to add custom attributes to a user.

|   |                                                                                       |
| - | ------------------------------------------------------------------------------------- |
|   | To complete this tutorial, you must first [add a user](../directory/p1_adduser.html). |

Adding custom attributes to a user determines the types of data that are stored for each user.

## Steps

1. In the PingOne admin console, go to **Directory > Users** and browse or search for the user that you want to add a custom attribute to..

2. Click the **More Options** (⋮) icon and click **Edit User**.

3. To add a custom attribute, scroll down to the **Custom Attributes** section.

4. Click **[icon: plus, set=fa]Add**.

5. In the **New Attributes list**, select a custom attribute.

   ![Screen capture of the Custom Attributes section in the user record.](_images/knd1670880066213.png)

6. Enter the value of the custom attribute.

   ![Screen capture of the Value field after choosing a custom attribute in the Custom Attribute section](_images/nwa1670880160465.png)

7. Click **Save**.

   |   |                                                                                                                                                                                                                                                                                                                                                                                    |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can view the attributes that you added in the **Custom Attributes** section of the user's **Profile** tab. This includes multi-value attributes and JavaScript Object Notation (JSON) *(tooltip: \<div class="paragraph">&#xA;\<p>An open, lightweight data-interchange format that uses human-readable text to store and transmit data.\</p>&#xA;\</div>)* object attributes. |

   ![Screen capture of the user's details, including the custom attributes section in](_images/vyj1670880330615.png)

---

---
title: Adding a new environment that includes PingID
description: Learn how to create a PingOne environment with PingID included as the first step in the multi-factor authentication experience tutorial.
component: pingone
page_id: pingone:pingone_tutorials:p1_tutorial_config_mfa_experience_add_environment
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_tutorial_config_mfa_experience_add_environment.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-28T00:00:00Z
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  result: Result:
  result-2: Result:
  result-3: Result:
  next-steps: Next steps
---

# Adding a new environment that includes PingID

For the purposes of this tutorial, add an environment that includes PingOne SSO and **Workforce Authentication** (PingID). A setup assistant guides you through this process.

|   |                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | These instructions only apply to environments that don't reside in the Singapore or Canada geographies.Learn more in [Multi-factor authentication (MFA)](../strong_authentication_mfa/p1_intro_to_strong_authentication.html#p1-strong-auth-mfa). |

## Before you begin

If you created an environment as part of the [Starting a PingOne trial](../getting_started_with_pingone/p1_start_a_p1_trial.html) process, you can use that environment for this tutorial assuming you've selected the **Workforce** use case and included PingID in the environment. Skip this section and go to [Creating demo users](p1_tutorial_config_mfa_experience_create_demo_users.html).

If you want to create a new environment for the tutorial, complete the steps in these instructions.

## Steps

1. In the PingOne admin console sidebar, click the Ping Identity logo to open the **Environments** page.

2. Click the **Plus** icon ([icon: plus, set=fa]).

   ![A screenshot of the Environments page in PingOne.](../getting_started_with_pingone/_images/vxj1676308916876.png)

   ### Result:

   The **Add New Environment** setup assistant starts.

   ![A screenshot of the Add New Environment setup assistant in PingOne.](../_images/p1-add-env-step1-clean.png)

3. Define your environment by entering the following:

   | Field                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
   | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | **Name**                                      | A unique identifier for the environment.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   | **Description** (optional)                    | A brief description of the environment.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   | **License Type**                              | Select **Trial** or **Paid**.If you don't already have a trial license for PingOne, selecting the **Trial** option creates a 30-day trial environment which you can use to test and evaluate PingOne services you haven't yet purchased.Select **Paid** to assign a paid license to the environment. Learn more in [Licenses and Platform Limits](../getting_started_with_pingone/p1_licenses.html).                                                                     |
   | **Environment Use Case**                      | Select **Workforce**.This option allows you to design single sign-on experiences for your employees.Learn more in [What is the difference between Workforce and Customer environments?](../strong_authentication_mfa/p1_pid_what_is_the_difference.html)                                                                                                                                                                                                                 |
   | **Environment Type**                          | Select **Sandbox** or **Production**.**Sandbox** environments are typically used for configuration and testing before deployment.&#xA;&#xA;If you selected Trial for the License Type, only Sandbox is available.**Production** environments are typically used for live configurations that are deployed for real-world use. Learn more about environment types in [Sandbox and Production environments](../introduction_to_pingone/p1_introduction.html#p1-env-types). |
   | **Include DaVinci flows for getting started** | Select this checkbox to include DaVinci flows in the new environment that are used in the getting started experience. This option is only available if you have a license that includes DaVinci.                                                                                                                                                                                                                                                                         |
   | **Generate sample populations and users**     | Select this checkbox to generate two populations and 40 sample users in the new environment.                                                                                                                                                                                                                                                                                                                                                                             |

4. The next steps depend on the **License Type** you selected in step 3:

   | License Type | Next Steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Trial**    | 1. Click an option on the **Environment Setup** modal:

      * **Guide Me**: PingOne selects capabilities for you.

        &#xA;&#xA;You'll have the option to remove any of these capabilities before you finalize the environment.

      * **Do It Myself**: You select the capabilities you want to add to the environment.

      ![A screenshot of the Environment Setup modal for trial environments in PingOne.](../_images/p1-add-env-envsetup-modal-trials.png)

   2. Select capabilities based on the option you selected in the previous step:

      * If you selected **Guide Me**, a bundle of services applicable to workforce environments is automatically added to the environment, and you can select optional capabilities that might be useful for advanced use cases.

        The bundle includes:

        * PingOne SSO

        * Workforce Authentication (PingID)

        * PingOne Protect

        * PingOne DaVinci

        * PingOne Verify

      * If you selected **Do It Myself**, you can select from a list of capabilities available based on the environment use case you selected.

        &#xA;&#xA;Ensure that you include Workforce Authentication (PingID).&#xA;&#xA;When you select Workforce Authentication (PingID), PingOne SSO is selected automatically and can't be removed.

   3. Click **Next**. |
   | **Paid**     | &#xA;&#xA;To connect to an existing PingID instance you must select Paid for the license type.1. On the **Select Capabilities** page, select a **License** in the list.

      The capabilities available for the selected license are listed.

      ![A screenshot of the Select Capabilities page for paid workforce environments in PingOne.](../_images/p1-add-paid-wf-select-capabilities.png)

   2. Select the capabilities you want to include in the new environment.

      &#xA;&#xA;Ensure that you select Workforce Authentication (PingID).&#xA;&#xA;When you select Workforce Authentication (PingID), PingOne SSO is selected automatically and can't be removed.

   3. Click **Next**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

5. Click **Next**.

6. On the **Finalize Setup** page, review the details about the new environment and clear the checkboxes next to any capabilities that you don't want to include.

7. If you selected a paid license, locate **Workforce Authentication** (PingID) in the **Selected Capabilities** list and click **Create New**.

   |   |                                                                                                                                      |
   | - | ------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If you selected a trial license, a new instance of PingID is created automatically and integrated with your new PingOne environment. |

8. Click **Save**.

   ### Result:

   The new environment is created in your PingOne organization and the **Environments** page opens.

9. Browse or search for the new environment and click it to open the details panel.

10. Click **Manage Environment** to go to the **Overview** page for your environment.

    ### Result:

    The **Overview** page for your new environment displays PingOne SSO, PingID, and potentially other products in the **Environment Capabilities** section.

    ![Screen capture showing the details of the environment that was created.](_images/p1-tut-mfa-wf-overview-pingid.png)

## Next steps

Continue by [Creating demo users](p1_tutorial_config_mfa_experience_create_demo_users.html).

---

---
title: Adding an environment
description: Learn how to add a PingOne environment as the first step in the basic passwordless login tutorial.
component: pingone
page_id: pingone:pingone_tutorials:p1_tutorial_passwordless_create_environment
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_tutorial_passwordless_create_environment.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-28T00:00:00Z
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  result: Result:
  result-2: Result
---

# Adding an environment

For the purposes of this tutorial, add an environment that includes the PingOne MFA service. A setup assistant guides you through this process.

## Before you begin

If you created an environment as part of the [Starting a PingOne trial](../getting_started_with_pingone/p1_start_a_p1_trial.html) process, you can use that environment for this tutorial assuming you've selected the **Customer** use case and included PingOne MFA in the environment. Skip this section and go to [Creating a registration application](p1_tutorial_passwordless_registration_application.html).

If you want to create a new environment for the tutorial, complete the steps in these instructions.

|   |                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------- |
|   | You must have the Organization Admin role or a custom role with equivalent permissions to create an environment. |

## Steps

1. In the PingOne admin console sidebar, click the Ping Identity logo to open the **Environments** page.

2. Click the **Plus** icon ([icon: plus, set=fa]).

   ![A screenshot of the Environments page in PingOne.](../getting_started_with_pingone/_images/vxj1676308916876.png)

   ### Result:

   The **Add New Environment** setup assistant starts.

   ![A screenshot of the Add New Environment setup assistant in PingOne.](../_images/p1-add-env-step1-clean.png)

3. Define your environment by entering the following:

   | Field                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
   | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | **Name**                                  | A unique identifier for the environment.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   | **Description** (optional)                | A brief description of the environment.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   | **License Type**                          | Select **Trial** or **Paid**.If you don't already have a trial license for PingOne, selecting the **Trial** option creates a 30-day trial environment which you can use to test and evaluate PingOne services you haven't yet purchased.Select **Paid** to assign a paid license to the environment. Learn more in [Licenses and Platform Limits](../getting_started_with_pingone/p1_licenses.html).                                                                     |
   | **Environment Use Case**                  | Select **Customer**.This option allows you to design registration and subsequent sign-on experiences for your customers.Learn more in [What is the difference between Workforce and Customer environments?](../strong_authentication_mfa/p1_pid_what_is_the_difference.html).                                                                                                                                                                                            |
   | **Environment Type**                      | Select **Sandbox** or **Production**.**Sandbox** environments are typically used for configuration and testing before deployment.&#xA;&#xA;If you selected Trial for the License Type, only Sandbox is available.**Production** environments are typically used for live configurations that are deployed for real-world use. Learn more about environment types in [Sandbox and Production environments](../introduction_to_pingone/p1_introduction.html#p1-env-types). |
   | **Generate sample populations and users** | Select this checkbox to generate two populations and 40 sample users in the new environment.                                                                                                                                                                                                                                                                                                                                                                             |

4. Click **Next**.

5. The next steps depend on the **License Type** you selected in step 3:

   | License Type | Next Steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Trial**    | 1. Click an option on the **Environment Setup** modal:

      * **Guide Me**: PingOne selects capabilities for you.

        &#xA;&#xA;You'll have the option to remove any of these capabilities before you finalize the environment.

      * **Do It Myself**: You select the capabilities you want to add to the environment.

      ![A screenshot of the Environment Setup modal for trial environments in PingOne.](../_images/p1-add-env-envsetup-modal-trials.png)

   2. Select capabilities based on the option you selected in the previous step:

      * If you selected **Guide Me**, a bundle of services applicable to workforce environments is automatically added to the environment, and you can select optional capabilities that might be useful for advanced use cases.

        The bundle includes:

        * PingOne SSO

        * PingOne MFA

        * PingOne Protect

        * PingOne DaVinci

        * PingOne Verify

      * If you selected **Do It Myself**, you can select from a list of capabilities available for the customer environment use case.

        &#xA;&#xA;Ensure that you select Multi-Factor Authentication (MFA).

   3. Click **Next**. |
   | **Paid**     | 1) On the **Select Capabilities** page, select a **License** in the list.

      The capabilities available for the selected license are listed.

      For organizations in the Singapore or Canada geographies, the license selection determines the version of PingOne MFA that is available for the environment.

      ![A screenshot of the Select Capabilities page for paid workforce environments in PingOne.](../_images/p1-add-paid-cust-select-capabilities.png)

   2) Select the capabilities you want to include in the new environment.

      &#xA;&#xA;Ensure that you select Multi-Factor Authentication (MFA).

   3) Click **Next**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

6. On the **Finalize Setup** page, review the details about the new environment and clear the checkboxes next to any capabilities that you don't want to include.

7. Click **Save** to create the new environment.

## Result

The new environment is created in your PingOne organization and the **Environments** page opens.

---

---
title: Adding an existing PingID tenant to a new PingOne environment
description: Learn how to add an existing PingID tenant to a new PingOne environment.
component: pingone
page_id: pingone:pingone_tutorials:p1_tutorial_config_mfa_experience_add_existing_tenant
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_tutorial_config_mfa_experience_add_existing_tenant.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-15T00:00:00Z
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  result: Result:
  result-2: Result
---

# Adding an existing PingID tenant to a new PingOne environment

If you have a separate PingID tenant, you can easily integrate it with your PingOne environment.

## Before you begin

This task describes the steps required to add an existing PingID tenant to a PingOne environment. In order to add an existing PingID tenant, the following conditions must be met:

* You must have a full PingOne license. This option isn't available with a trial license.

* If your PingID tenant hasn't been migrated to PingOne, and the PingID Global Administrator email is linked to multiple accounts, you must create a new Global Administrator account so PingOne can identify the correct tenant. The new Global Administrator account needs:

  * A unique email address.

  * A Global Administrator role with full privileges that isn't read-only or SSO only. To learn how to set up this role, see [Assign administrative roles](https://docs.pingidentity.com/pingoneforenterprise/pingone_sso_for_saas_apps/p14saas_assign_administrators.html).

* Your PingID license must support a connection to PingOne.

|   |                                                                                                 |
| - | ----------------------------------------------------------------------------------------------- |
|   | Learn more in [Licenses and Platform Limits](../getting_started_with_pingone/p1_licenses.html). |

## Steps

1. In the PingOne admin console sidebar, click the Ping Identity logo to open the **Environments** page.

2. Click the **Plus** icon ([icon: plus, set=fa]).

   ![A screenshot of the Environments page in PingOne.](../getting_started_with_pingone/_images/vxj1676308916876.png)

   ### Result:

   The **Add New Environment** setup assistant starts.

   ![A screenshot of the Add New Environment setup assistant in PingOne.](../_images/p1-add-env-step1-clean.png)

3. In the **Select a solution for your Environment** section, click **Build your own solution**.

4. Click the **Show Trials** toggle.

5. In the **Select a solution for your Environment** section, select the **PingOne SSO** and **PingID** services.

   ![Screen capture of environment creation, adding SSO and PingID.](_images/glr1632514439337.png)

6. Click **Next**.

7. On the **PingID** tile, click **I want to integrate with an existing account**.

8. In the **Username** and **Password** fields, enter the administrator credentials for your existing PingID tenant.

9. Click **Validate Account**.

   ![Screen capture of PingID environment deployment screen, with the option selected to integrate PingID with an existing account.](_images/iki1632514706144.png)

10. After PingOne validates your account, click **Confirm**.

    ![Screen capture of PingOne environment deployment screen after successful account validation.](_images/zgt1632514782484.png)

11. Click **Next**.

12. Define your environment by entering the following:

    | Field                                                         | Description                                                                                                                                                                                                                                                                                                                                  |
    | ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | **Environment Name**                                          | A unique identifier for the environment.                                                                                                                                                                                                                                                                                                     |
    | **Description** (optional)                                    | A brief description of the environment.                                                                                                                                                                                                                                                                                                      |
    | **Environment Type**                                          | Select **Sandbox** or **Production**. Sandbox environments are for configuration and testing before deployment. Production environments are for live configurations used in real-world scenarios. Learn more about environment types in [Sandbox and Production environments](../introduction_to_pingone/p1_introduction.html#p1-env-types). |
    | **Generate sample populations and users in this environment** | Select this check box to generate two populations and 40 sample users in the new environment.                                                                                                                                                                                                                                                |
    | **Region**                                                    | The appropriate geographical region for the environment. The list shows only geographies that are included with your license.&#xA;&#xA;You can't change the Region after the environment is created.                                                                                                                                         |
    | **License**                                                   | Select the license to use for this environment. The available licenses for your organization are shown in the **License** list. Learn more in [Licenses and Platform Limits](../getting_started_with_pingone/p1_licenses.html).                                                                                                              |

13. Click **Finish**.

## Result

The new environment is created in your PingOne organization and is listed on the **Environments** page.

---

---
title: Build a custom sign-on policy
description: Learn how to build a custom sign-on policy that uses multi-factor authentication.
component: pingone
page_id: pingone:pingone_tutorials:p1_p1tutorial_build_custom_policy
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_p1tutorial_build_custom_policy.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2023-11-13T00:00:00Z
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Build a custom sign-on policy

Learn how to build a custom sign-on policy that uses multi-factor authentication (MFA).

## About this task

This tutorial walks you through the creation of an MFA sign-on policy that you can apply to an application to secure access.

## Steps

1. In the PingOne admin console, go to **Authentication > Authentication**.

2. Click **[icon: plus, set=fa]Add Policy**.

   ![A screen capture showing the Authentication Policies page.](_images/mtl1699303551918.png)

3. Enter a **Policy Name**.

4. Select a **Step Type** of **Identifier First**.

5. Click **Add Step**.

6. Select a **Step Type** of **Multi-factor Authentication**.

7. For **MFA Policy**, select **Default MFA Policy**.

8. (Optional) Specify **Required When** criteria for the policy.

   For example, you can specify that the policy is required when users are members of a particular population.

   ![A screen capture showing the authentication policy page](_images/xni1699303847012.png)

9. To test the policy, assign it to an application on the application's **Policy** tab and access the application.

   ![A screen capture showing the Edit policies page](_images/kxn1676309960100.png)

---

---
title: Configure a basic passwordless login experience using PingOne and PingOne MFA
description: Learn how to configure a basic passwordless login experience using PingOne and PingOne MFA, from environment setup through user simulation.
component: pingone
page_id: pingone:pingone_tutorials:p1_tutorial_passwordless_overview
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_tutorial_passwordless_overview.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-28T00:00:00Z
---

# Configure a basic passwordless login experience using PingOne and PingOne MFA

This document demonstrates a basic passwordless login experience using PingOne and PingOne MFA.

By the end of this document, you will have experienced multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)* both from the administrator's perspective of configuration, and the end user's perspective of usage.

To configure a basic passwordless login experience using PingOne and PingOne MFA, follow these steps:

1. [Start a PingOne trial](p1_start_a_trial_tutorial_basic_passwordless.html).

2. [Create an environment](p1_tutorial_passwordless_create_environment.html).

3. [Create a registration application](p1_tutorial_passwordless_registration_application.html).

4. [Create a login application](p1_tutorial_passwordless_login_application.html).

5. [Create a registration policy](p1_tutorial_passwordless_registration_policy.html).

6. [Create a passwordless login policy](p1_tutorial_create_passwordless_login_policy.html).

7. [Create a group with dynamic membership](p1_tutorial_passwordless_create_group.html).

8. [Copy the sign-on URLs](p1_tutorial_passwordless_signon_urls.html).

9. [Simulate a registration and successful login](p1_tutorial_passwordless_registration_login.html).

10. [Simulate a registration and access control-based login failure](p1_tutorial_passwordless_registration_login_failure.html).

11. [Access the application portal](p1_tutorial_aplication_portal_passwordless.html).

---

---
title: Configure a multi-factor authentication experience using PingOne and PingID
description: Learn how to configure a multi-factor authentication experience using PingOne and PingID, from environment setup through user simulation.
component: pingone
page_id: pingone:pingone_tutorials:p1_tutorial_config_mfa_experience
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_tutorial_config_mfa_experience.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-28T00:00:00Z
---

# Configure a multi-factor authentication experience using PingOne and PingID

This tutorial demonstrates a simple multi-factor authentication (MFA) experience using PingOne and PingID. It illustrates both the administrator and end-user experience.

To configure an MFA experience using PingOne and PingID, follow these steps:

1. [Start a PingOne trial](p1_start_a_trial_config_mfa_tutorial.html).

2. [Add a new environment that includes Workforce Authentication (PingID)](p1_tutorial_config_mfa_experience_add_environment.html).

3. [Create demo users](p1_tutorial_config_mfa_experience_create_demo_users.html).

4. [Create a group with dynamic membership](p1_tutorial_config_mfa_experience_create_group_dynamic_membership.html).

5. [Create a web application](p1_tutorial_config_mfa_experience_create_web_app.html).

6. [Simulate the end-user experience](p1_tutorial_config_mfa_experience_perform_user_simulation.html).

7. [Access the application portal](p1_tutorial_aplication_portal.html).

8. [Review the synchronization of users in PingID](p1_tutorial_config_mfa_experience_review_synchronization_pid_users.html).

---

---
title: Control user access
description: Learn how to configure application access control in PingOne by applying groups to restrict which users can access an application.
component: pingone
page_id: pingone:pingone_tutorials:p1_p1tutorial_control_user_access
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_p1tutorial_control_user_access.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-28T00:00:00Z
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Control user access

Learn how to control user access to your applications using groups.

## About this task

This tutorial walks you through the configuration of application access control using groups. When no groups are applied to an application, all users have access. Learn more in [Application access control](../applications/p1_application_access_control.html) and [Configuring application access control](../applications/p1_application_access_control.html#configure_app_access).

|   |                                                                                                |
| - | ---------------------------------------------------------------------------------------------- |
|   | To complete this tutorial, you must first [create a group](p1_p1tutorial_create_a_group.html). |

## Steps

1. In the PingOne admin console, go to **Applications > Applications** and browse or search for the application you want to configure.

2. Click the application entry to open the details panel for the application.

3. On the **Access** tab, click the **Pencil** icon.

   ![A screen capture showing the Application details panel](_images/tjq1676311439543.png)

4. To add a group to the access list, select its checkbox.

5. Click **Save**.

   ![A screen capture showing the Application details panel with a group selected](_images/ohg1676311501164.png)

6. To test access control, try accessing the application with a user in the applied group and another who's not a member of the group.

---

---
title: Copying the sign-on URLs
description: Learn how to copy the sign-on URLs from the Registration and Self-Service applications in PingOne to use in the passwordless tutorial.
component: pingone
page_id: pingone:pingone_tutorials:p1_tutorial_passwordless_signon_urls
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_tutorial_passwordless_signon_urls.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-28T00:00:00Z
section_ids:
  steps: Steps
  next-steps: Next steps
---

# Copying the sign-on URLs

Copy the sign-on URLs into a text editor so that you can quickly complete this demo.

## Steps

1. Go to **Applications > Applications**.

2. Expand the **Registration** application and click the **Configuration** tab.

3. Copy the **Initiate Single Sign-On URL** and paste it into a text editor.

   ![A screen capture of the Application Configuration tab in PingOne.](_images/csq1651089981045.png)

4. Expand the **PingOne Self-Service** application.

5. Copy the **Home Page URL** and paste it into a text editor.

   ![A screen capture of the PingOne Self-Service application Profile tab.](_images/ffv1651091442207.png)

6. Expand the **Passwordless Login** application and click the **Configuration** tab.

7. Copy the **Initiate Single Sign-On URL** and paste it into a text editor.

   ![A screen capture of the Passwordless Login Application Configuration tab in PingOne.](_images/ila1651092182900.png)

## Next steps

Continue by [Simulating a registration and successful login](p1_tutorial_passwordless_registration_login.html).

---

---
title: Create a group
description: Learn how to create a group in PingOne to better manage your users and to provide improved access control to your applications.
component: pingone
page_id: pingone:pingone_tutorials:p1_p1tutorial_create_a_group
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_p1tutorial_create_a_group.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-05-16T00:00:00Z
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Create a group

Learn how to create a group to better manage your users and to provide improved access control to your applications.

This tutorial walks you through the creation of a group that you can use to manage access to your applications. You can create groups with a manually specified membership or by specifying criteria that dynamically adds users when a match is found.

|   |                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------- |
|   | To add users either manually or dynamically to a group, you must first [create users](../directory/p1_adduser.html). |

## Steps

1. In the PingOne admin console, go to **Directory > Groups**.

2. Click the **Plus** icon ([icon: plus, set=fa]) to add a group.

3. Enter the following information:

   * **Group name**: A name for the group. The name must be unique within the environment for environment groups, and unique within a population for population groups.

   * **Description** (optional): A brief description of the group.

   * **Population** (optional): The population in which the group will be created. Users with the Environment Admin role can create groups at the environment level, but users with the Identity Admin role must assign a group to a population for which they are an Identity Admin. If you select a population, the group can contain users from that population only.

   * **Metadata Properties** (optional): Custom metadata properties associated with the group, represented as key-value pairs for administrative purposes.

4. Click **Save**.

   ![A screen capture showing the Create Group page](_images/qvw1676310255152.png)

5. Click the **Users** tab.

6. Do one of the following:

   ### Choose from:

   * To add users from a list of users in the environment (for environment-level groups) or in the population (for population-level groups), click **Add Individually**. Learn more on the **Manually from Groups** tab of [Managing group membership](../directory/p1_add_members_to_group.html).

   * To create a filter to determine group membership, click **Add with a Filter**. Learn more on the **Dynamically from Groups** tab of [Managing group membership](../directory/p1_add_members_to_group.html).

     ![A screen capture showing the Group Details panel](_images/vlg1676310520752.png)

---

---
title: Creating a group with dynamic membership
description: Learn how to create a group with dynamic membership in PingOne.
component: pingone
page_id: pingone:pingone_tutorials:p1_tutorial_config_mfa_experience_create_group_dynamic_membership
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_tutorial_config_mfa_experience_create_group_dynamic_membership.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2023-11-13T00:00:00Z
section_ids:
  steps: Steps
  next-steps: Next steps
---

# Creating a group with dynamic membership

Creating groups for your users is not required, but groups are useful for organizing users who share the same criteria such as job title, region, and so on.

As part of this demo, you can experience group based access control during the user simulation. For the purposes of this demo, creating a group is optional.

## Steps

1. In the PingOne admin console, go to **Directory > Groups**.

2. Click the **[icon: plus, set=fa]**icon.

3. In the **Create New Group** panel, enter a **Group Name**, and select **Default** in the **Population** list.

   ![Screen capture of the Create New Group page with Sales entered as the Group Name and Default selected in the Population field](_images/wnz1619716968577.png)

4. Click **Finish & Save**.

5. Click your new group to show the summary panel.

6. Click the **Users** tab.

   ![A screen capture of the Users tab](_images/dyk1676328412405.png)

   You can add members either individually or through a filter. For this example, we'll dynamically add users to the Sales group who have titles starting with "Sales."

7. Click **Add with a Filter**.

8. In the **Attribute** list, select **Title**, in the **Operator** list, select **Starts with**, and in the **Value** field, enter `Sales`. **Click Save Filtered Users**.

   ![Screen capture of the Create Dynamic Group page with the Attribute field set to Title, the Operator set to Starts with, and Sales entered in the Value field](_images/nil1619732536623.png)

   As you can see, George and Lucy have been added to the Sales group.

   ![Updated screen capture of the Sales group showing two new members](_images/jos1619720413515.png)

## Next steps

Continue by [Creating a web application](p1_tutorial_config_mfa_experience_create_web_app.html).

---

---
title: Creating a group with dynamic membership
description: Learn how to create a PingOne group with dynamic membership to control access to the passwordless login application.
component: pingone
page_id: pingone:pingone_tutorials:p1_tutorial_passwordless_create_group
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_tutorial_passwordless_create_group.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-28T00:00:00Z
section_ids:
  steps: Steps
  result: Result:
  next-steps: Next steps
---

# Creating a group with dynamic membership

Create a group that features dynamic membership. Use this group to limit access to the application based on group membership.

## Steps

1. Go to **Directory > Groups**.

2. To add a new group, click **[icon: plus, set=fa]**.

3. In the **Group Name** field, enter `Allowed Users`.

4. From the **Population** list, select **Default**.

5. Click **Save**.

   ![A screen capture of the Create New Group window in PingOne.](_images/ppi1651087821045.png)

   ### Result:

   PingOne creates the user group and displays it in the **Groups** list.

6. In the configuration panel, click **Users**.

7. Click **Add Users with a Filter**.

8. In the **Create Dynamic Group** dialog, enter the following group criteria:

   | Field         | Value           |
   | ------------- | --------------- |
   | **Attribute** | **Username**    |
   | **Operator**  | **Starts with** |
   | **Value**     | `Sally`         |

   ![A screen capture of the Create Dynamic Group screen in PingOne.](_images/bak1620128673482.png)

9. Click **Save Filtered Users**.

10. Go to **Applications > Applications**.

11. Expand the **Passwordless Login** application.

12. Click the **Access** tab and click the **Pencil** icon.

13. Click **[icon: plus, set=fa]**or drag the **Allowed Users** group to the **Applied Groups** column.

14. Click **Save**.

![A screen capture of the Edit Access window in PingOne.](_images/cdt1651088963118.png)

## Next steps

Continue by [Copying the sign-on URLs](p1_tutorial_passwordless_signon_urls.html).

---

---
title: Creating a login application
description: Learn how to create a SAML application in PingOne that users can use to sign on without a password.
component: pingone
page_id: pingone:pingone_tutorials:p1_tutorial_passwordless_login_application
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_tutorial_passwordless_login_application.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-28T00:00:00Z
section_ids:
  steps: Steps
  result: Result:
  next-steps: Next steps
---

# Creating a login application

Create an application that your users can use to sign on.

## Steps

1. Go to **Applications > Applications**.

2. Click the **[icon: plus, set=fa]**icon.

3. In the **Application Name** field, enter `Passwordless Login`. Optionally, add a **Description** and an **Icon**.

4. Click **SAML Application**, and then click **Configure**.

   ![A screenshot of the Add Application SAML Application window in PingOne.](_images/fqd1651083769036.png)

5. Click **Manually Enter**.

6. In the **ACS URLs** field, enter `https://decoder.pingidentity.cloud/saml`.

7. In the **Entity ID** field, enter `samldecoder`, and click **Save**.

   ![A screenshot of the SAML Configuration window in PingOne.](_images/moj1651084324113.png)

   ### Result:

   PingOne adds the application to the **Applications** list.

8. Click the **Configuration** tab, and then click the **Pencil** icon.

9. In the **Assertion Validity Duration (in seconds)** field, enter `180`.

10. Click **Save**.

11. Click the toggle in the top right to enable the application.

    ![A screenshot of the toggle to enable an application in PingOne.](_images/wav1651084933781.png)

## Next steps

Continue by [Creating a registration policy](p1_tutorial_passwordless_registration_policy.html).

---

---
title: Creating a passwordless login policy
description: Learn how to create a PingOne sign-on policy that allows users to sign on with an SMS one-time passcode.
component: pingone
page_id: pingone:pingone_tutorials:p1_tutorial_create_passwordless_login_policy
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_tutorial_create_passwordless_login_policy.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-28T00:00:00Z
section_ids:
  steps: Steps
  result: Result:
  next-steps: Next steps
---

# Creating a passwordless login policy

Create a login policy that allows users to sign on with a one-time passcode (OTP) delivered via SMS.

## Steps

1. Go to **Authentication > Authentication**.

2. Click **Add Policy**.

   ![A screen capture of the Policies screen in PingOne.](_images/vsu1620128677248.png)

3. In the **Policy Name** field, enter `Passwordless_Login`.

4. From the **Step Type** list, select **Multi-factor Authentication**.

5. Under **Available Methods**, select the **SMS** checkbox.

   ![A screen capture of the Authentication Policy for the Passwordless Login Application in PingOne.](_images/swu1620128679155.png)

6. Click **Save**.

   ### Result:

   PingOne saves the policy and returns you to the **Policies** list.

7. Go to **Applications > Applications**.

8. Expand the **Passwordless Login** application.

9. Click the **Policies** tab and click the **Pencil** icon.

10. Click **[icon: plus, set=fa]**or drag the **Passwordless_Login** policy to the **Applied Policies** column.

    ![A screen capture of the Edit Policies window in PingOne.](_images/ohn1651086536876.png)

11. Click **Save**.

## Next steps

Continue by [Creating a group with dynamic membership](p1_tutorial_passwordless_create_group.html).

---

---
title: Creating a registration application
description: Learn how to create a SAML application in PingOne that users can use to self-register.
component: pingone
page_id: pingone:pingone_tutorials:p1_tutorial_passwordless_registration_application
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_tutorial_passwordless_registration_application.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-28T00:00:00Z
section_ids:
  steps: Steps
  result: Result:
  next-steps: Next steps
---

# Creating a registration application

Create an application that your users can use to register.

## Steps

1. Go to **Applications > Applications**.

2. Click the **[icon: plus, set=fa]**icon.

3. In the **Application Name** field, enter `Registration`.

4. Click **SAML Application**, and then click **Configure**.

   ![A screenshot of the Add Application SAML Application window in PingOne.](_images/ggk1651075630645.png)

5. Click **Manually Enter**.

6. In the **ACS URLs** field, enter `https://httpbin.org/anything`.

   ![A screenshot of the SAML Configuration window in PingOne.](_images/fgs1651076317943.png)

7. In the **Entity ID** field, enter `httpbin`, and then click **Save**.

   ### Result:

   PingOne adds the application the **Applications** list.

8. Click the **Configuration** tab, and then click the **Pencil** icon.

9. In the **Assertion Validity Duration (in seconds)** field, enter `180`.

10. Click **Save**.

11. In the **Applications** list, click the toggle in the top right to enable the application.

    ![A screenshot of the toggle to enable an application in PingOne.](_images/cyk1651080311715.png)

## Next steps

Continue by [Creating a login application](p1_tutorial_passwordless_login_application.html).

---

---
title: Creating a registration policy
description: Learn how to create a PingOne sign-on policy with a registration step so users can create an account.
component: pingone
page_id: pingone:pingone_tutorials:p1_tutorial_passwordless_registration_policy
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_tutorial_passwordless_registration_policy.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-28T00:00:00Z
section_ids:
  steps: Steps
  next-steps: Next steps
---

# Creating a registration policy

Create a policy that includes a registration step so that users can create a user account.

## Steps

1. Go to **Authentication > Authentication**.

2. Click **Add Policy**.

   ![A screenshot of the Policies screen in PingOne.](_images/vsu1620128677248.png)

3. In the **Policy Name** field, enter `Registration`.

4. From the **Step Type** list, select **Login**.

5. Select the **Enable Registration** check box.

6. From the **Population** list, select **Default**.

   ![A screenshot of the Authentication Policy for the Registration Application in PingOne.](_images/kle1620128675185.png)

7. Click **Save**.

8. Go to **Applications > Applications**.

9. Expand the **Registration** application and click the **Pencil** icon.

10. Click the **Policies** tab.

11. Click **[icon: plus, set=fa]**or drag the **Registration** policy to the **Applied Policies** column.

    ![A screenshot of the Applied Policies for the Registration Application in PingOne.](_images/njl1651085895703.png)

12. Click **Save**.

## Next steps

Continue by [Creating a passwordless login policy](p1_tutorial_create_passwordless_login_policy.html).

---

---
title: Creating a web application
description: Learn how to create a web application that uses a SAML connection in PingOne.
component: pingone
page_id: pingone:pingone_tutorials:p1_tutorial_config_mfa_experience_create_web_app
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_tutorial_config_mfa_experience_create_web_app.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2023-11-13T00:00:00Z
section_ids:
  steps: Steps
  limiting-access-to-the-application: Limiting access to the application
  steps-2: Steps
  assigning-the-multi_factor-authentication-policy-to-the-application: Assigning the Multi_Factor authentication policy to the application
  steps-3: Steps
  optional-configuring-pingid-policy: "Optional: Configuring PingID policy"
  steps-4: Steps
  next-steps: Next steps
---

# Creating a web application

Now that we've added our environment, and created new users and a group, we'll create a web application that uses a SAML connection.

## Steps

1. In the PingOne admin console, go to **Applications > Applications**.

2. Click the **[icon: plus, set=fa]**icon.

   ![Screen capture of the Applications page showing the Add Application icon](_images/pai1676405241170.png)

3. In the **Add Application** panel, enter an **Application Name**.

   You can also enter a **Description** (optional).

   |   |                                                                                                         |
   | - | ------------------------------------------------------------------------------------------------------- |
   |   | Add an icon for your application so that it's easy to identify in the **External Applications** portal. |

   ![A screen capture of the application details panel](_images/tlt1676405435151.png)

4. Click **SAML Application** and then click **Configure**.

5. For SAML Configuration, select **Manually Enter**.

6. Enter the following:

   * **ACS URLs**: `https://decoder.pingidentity.cloud/saml`

   * **Entity ID**: `pingidsamldecoder`

7. Click **Save**.

8. At the top of the panel, click the toggle to enable the application.

   ![A screen capture of the application details panel showing the enable toggle switch](_images/cye1676406015343.png)

## Limiting access to the application

We'll now limit access to the application to the Sales group.

### Steps

1. Go to **Applications > Applications**. Locate your application and click the application entry to open the details panel.

2. Click the **Access** tab and then click the pencil icon.

3. Under **Groups**, select the check box for the **Sales** group.

   ![Screen capture of the web application open in edit mode to the Access tab with the Sales group selected](_images/krj1676406476320.png)

4. Click **Save**.

## Assigning the Multi_Factor authentication policy to the application

We'll now assign the Multi-factor authentication policy to your web application. The application should still be open for edit.

### Steps

1. Go to **Applications > Applications**. Locate your application and click the application entry to open the details panel.

2. Click the **Policies** tab and then click the **Pencil** icon ([icon: pencil, set=fa]).

3. Under **PingOne Policies**, select the checkbox for the **Multi_Factor** policy.

   ![A screen capture showing the Policies tab](_images/hie1676406735039.png)

4. Click **Save**.

## Optional: Configuring PingID policy

You can configure the default PingID policy to add additional authentication methods and other policy criteria. Learn more in [Configuring strong authentication methods (MFA)](../strong_authentication_mfa/p1_configuring_strong_authentication_start.html).

### Steps

1. In the PingOne admin console, go to **Authentication > Authentication**.

2. Expand the **Multi_Factor** policy and click the **Pencil** icon ([icon: pencil, set=fa]) to edit it.

3. In the **PingID Authentication step**, click the link to **Configure now**.

4. Configure the PingID policy and then click **Save**.

### Next steps

Continue this demo by [Simulate the end-user experience](p1_tutorial_config_mfa_experience_perform_user_simulation.html).

---

---
title: Creating demo users
description: Learn how to create demo users in PingOne to use in the multi-factor authentication user simulation.
component: pingone
page_id: pingone:pingone_tutorials:p1_tutorial_config_mfa_experience_create_demo_users
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_tutorial_config_mfa_experience_create_demo_users.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-28T00:00:00Z
section_ids:
  steps: Steps
  next-steps: Next steps
---

# Creating demo users

This task walks you through the creation of users that you'll use later for the user simulation.

## Steps

1. Go to **Directory > Users**.

2. On the **Users** page, click the **[icon: plus, set=fa]**icon.

3. In the **Add User** panel, enter a **Given Name** of `George` and a **Family Name** of `Jones`.

4. Enter a **Username** of `GeorgeJones`.

   ![A screen capture of the Add User panel](_images/kuh1676327723778.png)

5. Click **Save**.

6. On the details panel for the user George Jones, click the options menu and then click **Reset Password** to create a temporary password so that George can log in to the web application that we'll create later.

   ![A screen capture of the user details panel with Reset Password option selected](_images/amq1676327981858.png)

7. Click the **[icon: plus, set=fa]**icon, and repeat these steps to create another user with the **Given Name** `Sally`, **Family Name** `Smith`, and **Username** `SallySmith`.

8. Add another user with **Given Name** `Lucy`, **Family Name** `Greene`, and **Username** `LucyGreene`.

## Next steps

Continue by [Creating a group with dynamic membership](p1_tutorial_config_mfa_experience_create_group_dynamic_membership.html).