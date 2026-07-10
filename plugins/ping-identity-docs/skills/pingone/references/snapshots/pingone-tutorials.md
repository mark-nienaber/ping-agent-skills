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