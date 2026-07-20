---
title: Accessing the application portal
description: Review each user's available applications by accessing the Application Portal.
component: pingone
page_id: pingone:pingone_tutorials:p1_tutorial_aplication_portal
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_tutorial_aplication_portal.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 23, 2024
section_ids:
  steps: Steps
---

# Accessing the application portal

Review each user's available applications by accessing the Application Portal.

## Steps

1. Go to **Applications > Applications**.

2. Expand the **PingOne Application Portal** application.

3. Click the **Policies** tab, and click the **Pencil** icon to edit.

4. Click **[icon: plus, set=fa]**to add **Multi\_Factor** to**Applied Policies**.

5. Click **Save**.

6. Go to **Environment → Properties**.

7. Click the **Application Portal URL**.

8. Sign on with each user to review the applications that are available to them.

---

---
title: Accessing the application portal
description: Review each user's available applications by accessing the Application Portal.
component: pingone
page_id: pingone:pingone_tutorials:p1_tutorial_aplication_portal_passwordless
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_tutorial_aplication_portal_passwordless.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 23, 2024
section_ids:
  steps: Steps
---

# Accessing the application portal

Review each user's available applications by accessing the Application Portal.

## Steps

1. Go to **Applications > Applications**.

2. Expand the **PingOne Application Portal** application.

3. Click the **Policies** tab, and click the **Pencil** icon to edit.

4. Click **[icon: plus, set=fa]**to add **Multi\_Factor** to**Applied Policies**.

5. Click **Save**.

6. Go to **Environment → Properties**.

7. Click the **Application Portal URL**.

8. Sign on with each user to review the applications that are available to them.

---

---
title: Add custom attributes to a user
description: Learn how to add custom attributes to a user.
component: pingone
page_id: pingone:pingone_tutorials:p1_add_custom_attributes_to_a_user
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_add_custom_attributes_to_a_user.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 13, 2023
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

   ![Screen capture of the Custom Attributes section in](_images/knd1670880066213.png)

6. Enter the value of the custom attribute.

   ![Screen capture of the Value field after choosing a costume attribute in the Custom Attribute section](_images/nwa1670880160465.png)

7. Click **Save**.

   |   |                                                                                                                                                                                                                                                                                                                                                                                    |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can view the attributes that you added in the **Custom Attributes** section of the user's **Profile** tab. This includes multi-value attributes and JavaScript Object Notation (JSON) *(tooltip: \<div class="paragraph">&#xA;\<p>An open, lightweight data-interchange format that uses human-readable text to store and transmit data.\</p>&#xA;\</div>)* object attributes. |

   ![Screen capture of the user's details, including the custom attributes section in](_images/vyj1670880330615.png)

---

---
title: Adding a new environment
description: To create a multi-factor authentication (MFA) experience, create an environment that includes PingOne and PingID.
component: pingone
page_id: pingone:pingone_tutorials:p1_tutorial_config_mfa_experience_add_environment
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_tutorial_config_mfa_experience_add_environment.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 13, 2026
section_ids:
  steps: Steps
  result: Result:
  result-2: Result:
  result-3: Result:
  next-steps: Next steps
---

# Adding a new environment

To create a multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)* experience, create an environment that includes PingOne and PingID.

## Steps

1. Sign on to the PingOne admin console.

2. In the PingOne admin console sidebar, click the Ping Identity logo to open the **Environments** page.

3. Click the **[icon: plus, set=fa]**icon.

   ![A screenshot of the Environments page in PingOne.](../getting_started_with_pingone/_images/vxj1676308916876.png)

   ### Result:

   The **Create Environment** setup assistant starts.

4. On the **Create Environment** page, under **Select a solution for your Environment**, select **Workforce solution**.

   ![Screen capture of PingOne Create Environment page with Workforce solution selected](../_images/ppz1683237101125.png)

5. Click **Next**.

   The services that will be deployed to your new environment are listed.

6. Click **Next**.

7. Define your environment by entering the following:

   | Field                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                       |
   | -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Environment Name**                                                             | A unique identifier for the environment.                                                                                                                                                                                                                                                                                                                                          |
   | **Description** (optional)                                                       | A brief description of the environment.                                                                                                                                                                                                                                                                                                                                           |
   | **Environment Type**                                                             | Select **Sandbox** or **Production**.Sandbox environments are typically used for configuration and testing before deployment. Production environments are typically used for live configurations that are deployed for real-world use. Learn more about environment types in [Sandbox and Production environments](../introduction_to_pingone/p1_introduction.html#p1-env-types). |
   | **Generate sample populations and users in this environment**                    | Select this checkbox to generate two populations and 40 sample users in the new environment.                                                                                                                                                                                                                                                                                      |
   | **Region**                                                                       | The appropriate geographical region for the environment. The list shows only regions that are included with your license.&#xA;&#xA;You can't change the region after the environment has been created.                                                                                                                                                                            |
   | **License**                                                                      | Select the license to use for this environment. The available licenses for your organization are shown in the **License** list. For more information, see [Licenses and Platform Limits](../getting_started_with_pingone/p1_licenses.html).                                                                                                                                       |
   | **Include a solution designer to easily design and test experiences** (optional) | Workforce solutions only. If selected, after you create your environment, a solution designer opens and walks you through the process of designing your experiences.                                                                                                                                                                                                              |

8. Click **Finish**.

   ### Result:

   The new environment is created in your PingOne organization.

   If you selected the solution designer option, the solution designer opens and guides you through the process of designing and testing registration and sign-on experiences in less than 5 minutes.

   If you didn't select the solution designer option, the **Environments** page opens. Locate your new environment by sorting the list alphabetically or by date created, or enter the environment name in the search box.

   ![Screen capture of the Environments page showing the environment you just added](_images/qcr1620047803921.png)

9. On the **Environments** page, click the environment to open the details panel.

10. Click **Manage Environment** to go to the **Overview** page for your environment.

    ### Result:

    The **Overview** window of your new environment displays PingOne SSO, PingID, and potentially other products in the **Services** section. The green dot in the **PingID** tile shows that PingID is deployed.

    ![Screen capture showing the details of the environment that was created, with the green dot showing that PingID is deployed.](_images/avg1699305985238.png)

## Next steps

Continue by [Creating demo users](p1_tutorial_config_mfa_experience_create_demo_users.html).

---

---
title: Adding an environment
description: The first thing you should do after you start a PingOne trial or purchase a PingOne license is create an environment. A setup assistant guides you through this process.
component: pingone
page_id: pingone:pingone_tutorials:p1_tutorial_passwordless_create_environment
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_tutorial_passwordless_create_environment.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 6, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
  result-2: Result
---

# Adding an environment

The first thing you should do after you start a PingOne trial or purchase a PingOne license is create an environment. A setup assistant guides you through this process.

## About this task

|   |                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------- |
|   | You must have the Organization Admin role or a custom role with equivalent permissions to create an environment. |

## Steps

1. In the PingOne admin console sidebar, click the Ping Identity logo to open the **Environments** page.

2. Click the **[icon: plus, set=fa]**icon.

   ![A screenshot of the Environments page in PingOne.](../getting_started_with_pingone/_images/vxj1676308916876.png)

   ### Result:

   The **Create Environment** setup assistant starts.

3. Select the type of solution that you want to support in this environment.

   ![A screenshot of the Create Environment setup assistant in PingOne.](../_images/ppz1683237101125.png)

   | Option                      | Description                                                                                                                                          |
   | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Customer solution**       | Select to design registration and subsequent sign-on experiences for your customers and test them in a sample application tailored to your industry. |
   | **Workforce solution**      | Select to design single sign-on experiences for your employees, partners, and vendors.                                                               |
   | **Build your own solution** | Select to choose from all of our services and products to build a hybrid solution that fits your unique use case.                                    |

4. Click **Next**.

   The services that will be deployed to your new environment are listed.

5. Click **Next**.

6. Define your environment by entering the following:

   | Field                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                       |
   | -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Environment Name**                                                             | A unique identifier for the environment.                                                                                                                                                                                                                                                                                                                                          |
   | **Description** (optional)                                                       | A brief description of the environment.                                                                                                                                                                                                                                                                                                                                           |
   | **Environment Type**                                                             | Select **Sandbox** or **Production**.Sandbox environments are typically used for configuration and testing before deployment. Production environments are typically used for live configurations that are deployed for real-world use. Learn more about environment types in [Sandbox and Production environments](../introduction_to_pingone/p1_introduction.html#p1-env-types). |
   | **Generate sample populations and users in this environment**                    | Select this checkbox to generate two populations and 40 sample users in the new environment.                                                                                                                                                                                                                                                                                      |
   | **Region**                                                                       | The appropriate geographical region for the environment. The list shows only regions that are included with your license.&#xA;&#xA;You can't change the region after the environment has been created.                                                                                                                                                                            |
   | **License**                                                                      | Select the license to use for this environment. The available licenses for your organization are shown in the **License** list. For more information, see [Licenses and Platform Limits](../getting_started_with_pingone/p1_licenses.html).                                                                                                                                       |
   | **Include a solution designer to easily design and test experiences** (optional) | Workforce solutions only. If selected, after you create your environment, a solution designer opens and walks you through the process of designing your experiences.                                                                                                                                                                                                              |

7. Click **Finish**.

## Result

The new environment is created in your PingOne organization.

If you chose to build a workforce solution, and selected the solution designer option, the solution designer opens and guides you through the process of designing and testing registration and sign-on experiences in less than 5 minutes.

If you did not select the solution designer option, or if you didn't build a workforce solution, the **Environments** page opens. Locate your new environment by sorting the list alphabetically or by date created, or enter the environment name in the search box.

---

---
title: Adding an existing PingID tenant to a new PingOne environment
description: Learn how to add an existing PingID tenant to a new PingOne environment.
component: pingone
page_id: pingone:pingone_tutorials:p1_tutorial_config_mfa_experience_add_existing_tenant
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_tutorial_config_mfa_experience_add_existing_tenant.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 15, 2026
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

2. Click the **[icon: plus, set=fa]**icon.

   ![A screenshot of the Environments page in PingOne.](../getting_started_with_pingone/_images/vxj1676308916876.png)

   ### Result:

   The **Create Environment** setup assistant starts.

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
revdate: November 13, 2023
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
description: This document demonstrates a basic passwordless login experience using PingOne and PingOne MFA.
component: pingone
page_id: pingone:pingone_tutorials:p1_tutorial_passwordless_overview
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_tutorial_passwordless_overview.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 23, 2024
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
description: This document demonstrates a simple multi-factor authentication (MFA) experience using PingOne and PingID. By the end of this document, you will have experienced MFA both from the administrator's perspective of configuration, and the end user's perspective of usage.
component: pingone
page_id: pingone:pingone_tutorials:p1_tutorial_config_mfa_experience
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_tutorial_config_mfa_experience.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 1, 2024
---

# Configure a multi-factor authentication experience using PingOne and PingID

This document demonstrates a simple multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)* experience using PingOne and PingID. By the end of this document, you will have experienced MFA both from the administrator's perspective of configuration, and the end user's perspective of usage.

To configure an MFA experience using PingOne and PingID, follow these steps:

1. [Start a PingOne trial](p1_start_a_trial_config_mfa_tutorial.html).

2. [Add a new environment](p1_tutorial_config_mfa_experience_add_environment.html).

3. [Add an existing PingID tenant to a new PingOne environment](p1_tutorial_config_mfa_experience_add_existing_tenant.html).

4. [Create demo users](p1_tutorial_config_mfa_experience_create_demo_users.html).

5. [Create a group with dynamic membership](p1_tutorial_config_mfa_experience_create_group_dynamic_membership.html).

6. [Create a web application](p1_tutorial_config_mfa_experience_create_web_app.html).

7. [Perform the user simulation](p1_tutorial_config_mfa_experience_perform_user_simulation.html).

8. [Access the application portal](p1_tutorial_aplication_portal.html).

9. [Review the synchronization of users in PingID](p1_tutorial_config_mfa_experience_review_synchronization_pid_users.html).

---

---
title: Control user access
description: Learn how to control user access to your applications using groups.
component: pingone
page_id: pingone:pingone_tutorials:p1_p1tutorial_control_user_access
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_p1tutorial_control_user_access.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 25, 2025
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
description: Copy the sign-on URLs into a text editor so that you can quickly complete this demo.
component: pingone
page_id: pingone:pingone_tutorials:p1_tutorial_passwordless_signon_urls
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_tutorial_passwordless_signon_urls.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 13, 2023
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
revdate: May 16, 2025
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
revdate: November 13, 2023
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
description: Create a group that features dynamic membership. Use this group to limit access to the application based on group membership.
component: pingone
page_id: pingone:pingone_tutorials:p1_tutorial_passwordless_create_group
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_tutorial_passwordless_create_group.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 13, 2023
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
description: Create an application that your users can use to log in.
component: pingone
page_id: pingone:pingone_tutorials:p1_tutorial_passwordless_login_application
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_tutorial_passwordless_login_application.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 14, 2023
section_ids:
  steps: Steps
  result: Result:
  next-steps: Next steps
---

# Creating a login application

Create an application that your users can use to log in.

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
description: Create a login policy that allows users to log in with a one-time passcode (OTP) delivered via SMS.
component: pingone
page_id: pingone:pingone_tutorials:p1_tutorial_create_passwordless_login_policy
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_tutorial_create_passwordless_login_policy.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 13, 2023
section_ids:
  steps: Steps
  result: Result:
  next-steps: Next steps
---

# Creating a passwordless login policy

Create a login policy that allows users to log in with a one-time passcode (OTP) delivered via SMS.

## Steps

1. Go to **Authentication > Authentication**.

2. Click **Add Policy**.

   ![A screen capture of the Policies screen in PingOne.](_images/vsu1620128677248.png)

3. In the **Policy Name** field, enter `Passwordless_Login`.

4. From the **Step Type** list, select **Multi-factor Authentication**.

5. Under **Available Methods**, select the **SMS** check box.

   ![A screen capture of the Authentication Policy for the Passwordless Login Application in PingOne.](_images/swu1620128679155.png)

6. Click **Save**.

   ### Result:

   PingOne saves the policy and returns you to the **Policies** list.

7. Go to **Applications > Applications**.

8. Expand the **Passwordless Login** application.

9. Click the **Policies** tab and click the **Pencil** icon.

10. Click **[icon: plus, set=fa]**or drag the **Passwordless\_Login** policy to the **Applied Policies** column.

    ![A screen capture of the Edit Policies window in PingOne.](_images/ohn1651086536876.png)

11. Click **Save**.

## Next steps

Continue by [Creating a group with dynamic membership](p1_tutorial_passwordless_create_group.html).

---

---
title: Creating a registration application
description: Create an application that your users can use to register.
component: pingone
page_id: pingone:pingone_tutorials:p1_tutorial_passwordless_registration_application
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_tutorial_passwordless_registration_application.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 14, 2023
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
description: Create a policy that includes a registration step so that users can create a user account.
component: pingone
page_id: pingone:pingone_tutorials:p1_tutorial_passwordless_registration_policy
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_tutorial_passwordless_registration_policy.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 13, 2023
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
description: Create a web application that uses a SAML connection in PingOne.
component: pingone
page_id: pingone:pingone_tutorials:p1_tutorial_config_mfa_experience_create_web_app
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_tutorial_config_mfa_experience_create_web_app.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 13, 2023
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

## Assigning the Multi\_Factor authentication policy to the application

We'll now assign the Multi-factor authentication policy to your web application. The application should still be open for edit.

### Steps

1. Go to **Applications > Applications**. Locate your application and click the application entry to open the details panel.

2. Click the **Policies** tab and then click the pencil icon.

3. Under **PingOne Policies**, select the check box for the **Multi\_Factor** policy.

   ![A screen capture showing the Policies tab](_images/hie1676406735039.png)

4. Click **Save**.

## Optional: Configuring PingID policy

You can configure the default PingID policy to add additional authentication methods and other policy criteria. Learn more in [Configuring strong authentication methods (MFA)](../strong_authentication_mfa/p1_configuring_strong_authentication_start.html).

### Steps

1. In the PingOne admin console, go to **Authentication > Authentication**.

2. Expand the **Multi\_Factor** policy and click the **Pencil** icon ([icon: pencil, set=fa]) to edit it.

3. In the **PingID Authentication step**, click the link to **Configure now**.

4. Configure the PingID policy and then click **Save**.

### Next steps

Continue this demo by [Performing the user simulation](p1_tutorial_config_mfa_experience_perform_user_simulation.html).

---

---
title: Creating demo users
description: This task walks you through the creation of users that you'll use later for the user simulation.
component: pingone
page_id: pingone:pingone_tutorials:p1_tutorial_config_mfa_experience_create_demo_users
canonical_url: https://docs.pingidentity.com/pingone/pingone_tutorials/p1_tutorial_config_mfa_experience_create_demo_users.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 13, 2023
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