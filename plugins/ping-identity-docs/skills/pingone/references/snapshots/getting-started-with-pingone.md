---
title: Accepting the administrator account registration invitation
description: Accept the administrator account registration invitation to activate your PingOne administrator account.
component: pingone
page_id: pingone:getting_started_with_pingone:p1_accept_invitation
canonical_url: https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_accept_invitation.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 10, 2026
section_ids:
  steps: Steps
  result: Result:
---

# Accepting the administrator account registration invitation

When you receive an email indicating that you were added as an administrator in PingOne, copy the invite code and paste it into PingOne to complete the registration process.

## Steps

1. Click **Complete Registration** on the email you received.

2. On the sign-on page, enter your PingOne username.

3. Click the **Complete Registration** button.

4. Copy the invite code from the email and paste it into the **Invite Code** field.

   |   |                                                                                                                                        |
   | - | -------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you enter an incorrect invite code five times, you will be locked out of the account and the invitation will need to be sent again. |

   ![A screen capture of the screen users see when they complete their registration.](_images/complete_registration.jpg)

5. Enter and verify a new password for the account and click **Continue**.

   ### Result:

   You are signed on to the PingOne admin console.

---

---
title: Accessing the PingOne admin console
description: The main point of entry into PingOne for administrators is the PingOne admin console.
component: pingone
page_id: pingone:getting_started_with_pingone:p1_access_admin_console
canonical_url: https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_access_admin_console.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 29, 2025
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  result: Result:
---

# Accessing the PingOne admin console

The PingOne admin console is the main point of entry for administrators in PingOne. The first time you access the admin console, you must register a multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)* method because MFA is required for access. After you sign on the first time, the **Environments** page displays a list of environments to which you have access. If you have the Organization Admin role, all the environments in your organization are listed. Subsequent sign-ons will take you to the admin console for the environment you last accessed.

## Before you begin

Ensure that you:

* Are an administrator of a PingOne environment.

* Set the username for your PingOne administrator account as your email address.

* [Verify your email address](../managing_your_pingone_user_profile/p1_verify_email_admins.html) in PingOne.

To access the PingOne admin console home page:

## Steps

1. Go to [pingidentity.com](http://pingidentity.com) and click **Sign On**.

2. Enter your email address and click **Continue**.

   * If this is your first time signing on from a browser, an email is sent to your email address with a verification link. Click the link to verify your email address.

   * If you have multiple administrator identities associated with the same email address, a list of environments associated with those identities across all geographies displays. Select the environment that you want to access.

     |   |                                                                                                                                                                                                         |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | Environments that have expired licenses are flagged in the list of your environments. To extend a license, contact Ping Identity Sales at <https://www.pingidentity.com/en/company/contact-sales.html>. |

3. Follow the authentication steps for your environment.

   If you are unable to sign on, contact your administrator for further assistance. You can also sign on using your direct console login URL. Learn more in [Administrators: Managing your PingOne environment](../managing_your_pingone_user_profile/p1_signin.html).

   |   |                                                                                                                                                                                         |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Administrators must sign on again after 30 minutes of inactivity in the admin console. MFA is required if the last sign-on is older than 12 hours. These settings are not configurable. |

   ### Result:

   The **Environments** page opens and lists the environments to which you have access. If this is your first time accessing this page, you're asked if you would like to take a quick tour of the admin console.

   ![A screen capture of the Environments page of the admin console, listing the environments that are in the organization.](_images/vxj1676308916876.png)

---

---
title: Adding administrators
description: Add administrator users to your PingOne environment and assign them appropriate roles.
component: pingone
page_id: pingone:getting_started_with_pingone:p1_add_admin_user
canonical_url: https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_add_admin_user.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 10, 2026
section_ids:
  steps: Steps
  next-steps: Next steps
---

# Adding administrators

You can designate an existing user as an administrator or create a new administrator user.

|   |                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------- |
|   | To prevent privilege escalation, you cannot create an administrator user if you do not have administrator privileges. |

## Steps

1. In the Administrators environment, go to **Directory > Users** and browse or search for the user you that want to make an administrator.

   |   |                                                                                                                                                                                                                                                     |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To create a new user with administrator privileges, click the **[icon: plus, set=fa]**icon. Learn more in [Adding a user in PingOne](../directory/p1_adduser.html). All administrator users should be maintained in the Administrators environment. |

2. Click the user entry to open the user details panel.

3. On the **Roles > Administrator Roles** tab, click **Grant roles**.

   |   |                                                                                                            |
   | - | ---------------------------------------------------------------------------------------------------------- |
   |   | If there aren't any application roles available in the environment, the settings are on the **Roles** tab. |

4. Select an administrator role, such as **Environment Admin**, **Identity Data Admin**, or **Organization Admin**.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | You cannot assign privileges greater than those you are assigned. When you are determining which role to assign, consider the role that has the minimum permissions necessary for the administrator to perform their job responsibilities. Scope that role according to the levels at which the administrator should have this access.Learn more in [Administrator Roles](../directory/p1_roles.html) and [Managing user roles](../directory/p1_manage_user_roles.html). |

5. Click **Save**.

6. On the **Profile** tab, click **Verify** to send a verification email to the user.

   |   |                                                          |
   | - | -------------------------------------------------------- |
   |   | All administrator users must verify their email address. |

7. Go to **Settings > Environment Properties** and copy the **Console Login URL**.

8. Contact the new administrator and provide them with the following:

   * Their PingOne user name, if different from their email address.

   * The **Console Login URL** from the previous step.

   * (Optional) A temporary password for the console (if you set one up when you created the user).

   * The instructions for [Completing the administrator account registration](p1_complete_admin_registration.html)

## Next steps

The new administrator completes their account registration.

|   |                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Older organizations might not have an **Administrators** environment by default. To improve security posture, separate administrators from end users and manage all administrators in their own environment. |

---

---
title: Adding environments
description: Add a PingOne environment for a customer, workforce, or custom identity solution to organize your Ping Identity products and services.
component: pingone
page_id: pingone:getting_started_with_pingone:p1_solution_add_environment
canonical_url: https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_solution_add_environment.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 10, 2026
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  result: Result:
  result-2: Result:
  result-3: Result
  next-steps: Next steps
---

# Adding environments

The first step in building an identity solution is adding an environment to organize your Ping products and services.

## Before you begin

Determine what type of solution you're building. Filter the products and services by the type of audience you serve with your identity and access management solution:

* Customer solutions

  Help you create sign-on experiences for your clients and consumers. Products and services relevant to serving your clients and consumers are added to the environment.

* Workforce solutions

  Help you create sign-on experiences for your organization's employees. Products and services relevant to serving your employees and partners are added to the environment.

* Build your own solution

  Allows you to build a hybrid solution by selecting from all available products and services.

|   |                                                                                                                                                                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | When you select **Customer solution** or **Workforce solution**, a combination of preselected services designed to support your customer or workforce use cases is added to the environment. If your license doesn't cover the services that are included, you can select **Build your own solution** to select from products and services for which you have a license. |

## Steps

1. In the PingOne admin console sidebar, click the Ping Identity logo to open the **Environments** page.

2. Click the **[icon: plus, set=fa]**icon.

   ![A screenshot of the Environments page in PingOne.](_images/vxj1676308916876.png)

   ### Result:

   The **Create Environment** setup assistant starts.

3. To indicate whether you are building a customer solution, workforce solution, or custom solution, select the appropriate option.

   ### Result:

   **Create Environment** lists the main tasks that can be completed using the solution type.

   ![A screenshot of the Create Environment screen in PingOne.](../_images/ppz1683237101125.png)

4. Click **Next**.

   The services that will be deployed to your new environment are listed.

5. To add or remove them from your solution, select and deselect products and services as necessary, then click **Next**.

   Many of your selections are deployed automatically, but you might be asked how to deploy a connected product. Answer the questions to the best of your ability. You can change them later.

6. Define your environment by entering the following:

   | Field                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                       |
   | -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Environment Name**                                                             | A unique identifier for the environment.                                                                                                                                                                                                                                                                                                                                          |
   | **Description** (optional)                                                       | A brief description of the environment.                                                                                                                                                                                                                                                                                                                                           |
   | **Environment Type**                                                             | Select **Sandbox** or **Production**.Sandbox environments are typically used for configuration and testing before deployment. Production environments are typically used for live configurations that are deployed for real-world use. Learn more about environment types in [Sandbox and Production environments](../introduction_to_pingone/p1_introduction.html#p1-env-types). |
   | **Generate sample populations and users in this environment**                    | Select this checkbox to generate two populations and 40 sample users in the new environment.                                                                                                                                                                                                                                                                                      |
   | **Region**                                                                       | The appropriate geographical region for the environment. The list shows only regions that are included with your license.&#xA;&#xA;You can't change the region after the environment has been created.                                                                                                                                                                            |
   | **License**                                                                      | Select the license to use for this environment. The available licenses for your organization are shown in the **License** list. For more information, see [Licenses and Platform Limits](p1_licenses.html).                                                                                                                                                                       |
   | **Include a solution designer to easily design and test experiences** (optional) | Workforce solutions only. If selected, after you create your environment, a solution designer opens and walks you through the process of designing your experiences.                                                                                                                                                                                                              |

## Result

The new environment is created in your PingOne organization.

If you chose to build a workforce solution, and selected the solution designer option, the solution designer opens and guides you through the process of designing and testing registration and sign-on experiences in less than 5 minutes.

If you did not select the solution designer option, or if you didn't build a workforce solution, the **Environments** page opens. Locate your new environment by sorting the list alphabetically or by date created, or enter the environment name in the search box.

## Next steps

Deploy your solution. Learn more in [Deploying products and services](p1_building_solutions.html#p1-deploy-products).

---

---
title: Assigning a license
description: Change the association between your environments and your licenses in PingOne.
component: pingone
page_id: pingone:getting_started_with_pingone:p1_license_assignment
canonical_url: https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_license_assignment.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 12, 2024
section_ids:
  steps: Steps
---

# Assigning a license

If you have more than one active license, use the **Licenses** page to change the association between your environments and your licenses.

|   |                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------- |
|   | A license can be associated with multiple environments, but an environment can be associated with only one license. |

![A screen capture of entitlements and environments.](_images/p1-internal-license.png)

## Steps

* To view the environments to which license is currently assigned to, click the license entry to open the license details panel and click **Environments**.

  The license details can help you determine if you need to purchase separate PingOne solutions, such as one for workforce and one for external customers.

* To reassign licenses, click the **More Options (⋮) icon** and then select a different license.

  PingOne allows you to reassign an environment to a license that doesn't contain enough services to downgrade when services are no longer needed.

  |   |                                                                                                                                                                                                                         |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | A warning appears if you choose a license that includes fewer services than the environment is currently using.You can select **Reassign** to proceed with the new license or **Cancel** to keep your current settings. |

  Each license supports a specific limit on the number of environments that can be associated with it at any given time. A warning appears when attempting to reassign an environment to a license when you exceed that limit.

* To view the license assigned to an environment on the **Environments** page, go to **Settings > Environment Properties**.

---

---
title: Building a customer solution
description: Use your PingOne trial to design and test registration and sign-on experiences for your customers.
component: pingone
page_id: pingone:getting_started_with_pingone:p1_trial_customer_solution
canonical_url: https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_trial_customer_solution.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 15, 2023
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  result: Result:
---

# Building a customer solution

By following the guidance on the **Getting Started** page in your PingOne trial environment, you'll quickly learn how to:

* Create a sign-on experience.

* Add an application to your environment.

* Assign the experience to the application.

* Integrate the application with PingOne.

* Apply branding to the registration and sign-on pages to customize the look and feel of those pages for your customers.

## Before you begin

These instructions assume that you have already created your PingOne trial environment and that you chose the **Customer solution** option. Learn more in [Starting a PingOne trial](p1_start_a_p1_trial.html).

|   |                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | After completing each step in the applicable area of PingOne, you can click **Getting Started** in the sidebar to return and determine what to do next. |

## Steps

1. Click **Getting Started**, either from the message you receive after creating your environment or from the top of the sidebar in the PingOne admin console.

   ![A screenshot of the PingOne admin console including the sidebar with the Getting Started option highlighted and the Getting Started page showing.](_images/p1-sidebar-getting-started.png)

   |   |                                                                                                                               |
   | - | ----------------------------------------------------------------------------------------------------------------------------- |
   |   | Although not required, follow the steps in the order presented on the **Getting Started** page to see how they are connected. |

2. Click **Create Experience** to open the **Design Center**.

   ![A screenshot of the Design Center page showing a list of experiences.](_images/p1-getting-started-design-center.png)

3. []()Create a sign-on and registration experience for the application.

   You can choose from three sign-on patterns to implement in your experience:

   * **Username and Password**

   * **Identifier First**

   * **Identity Provider First**

   Experiences created in the **Design Center** define how users authenticate when they access the application. The experience determines whether the user can authenticate using passwordless options, whether they're prompted to register for an account, what multi-factor authentication (MFA) methods they can choose, and more.

   Learn more about building experiences in [Design Center](../orchestration/p1_design_center_experiences.html).

4. []()Return to the **Getting Started** page and click **Add App** to add an application to the environment.

   Follow the prompts in the environment or learn more in [Adding an application](../applications/p1_applications_add_applications.html).

   |   |                                                                                                                                                                                                                                                                                                      |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For the purposes of this trial, you won't need to configure the application beyond providing a name and selecting an application type. If you want to explore further, you can learn more about application configuration in [Editing an application](../applications/p1_editing_applications.html). |

5. After you save your application, go back to the **Getting Started** page and click **Assign Experience**.

6. Follow the prompts to assign the experience you created in [step 3](#p1-gs-create-exp) to the application you created in [step 4](#p1-gs-add-app).

   Learn more in [Applying authentication policies to an application](../applications/p1_apply_auth_policy_to_applications.html).

   |   |                                                                                                                                     |
   | - | ----------------------------------------------------------------------------------------------------------------------------------- |
   |   | Experiences created in the **Design Center** are listed on the **DaVinci Policies** tab and include a **PingOne Experience** label. |

   ![A screenshot showing the DaVinci Policies tab for an application with one policy labeled as a PingOne Experience.](_images/p1-getting-started-assign-exp-to-app.png)

7. Return to the **Getting Started** page and click **Integrate**.

8. Follow the prompts to integrate your application with PingOne and test the sign-on experience in a local project.

   Learn more by following the steps in the [Integrate PingOne with a Node.js Express app](../pingone_tutorials/p1_tutorial_integrate_nodejs_express_app.html) tutorial.

9. Return to the **Getting Started** page and click **Customize** to create a new theme or modify an existing theme to apply your own branding to the sign-on forms.

   Learn more in [Branding and Themes](../user_experience/p1_branding_themes.html) and [Adding a theme](../user_experience/p1_add_theme.html).

   |   |                                                                                                                                                                                                                                                                                                         |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The forms generated when you created the experience in [step 3](#p1-gs-create-exp) are included in the **Form Preview** list on the **Forms** tab for the selected theme. Use the settings on the **Component Specific** tab in the **Theme Styles** pane to edit these forms and preview your changes. |

10. Return to the **Getting Started** page and click **Dismiss Getting Started** to close the page and remove **Getting Started** from the sidebar.

    ### Result:

    You're taken to the **Overview** page for the environment, where you can continue exploring and building your customer solution.

    |   |                                                                                                                                                                                                                                                                                                                                                                                                    |
    | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | To enable the **Getting Started** page at any time, go to **Settings > Environment Properties** and click the toggle in the **Getting Started Guides** section to the right (blue).![A screenshot of the Getting Started toggle in the on position.](_images/p1-env-props-getting-started-toggle.png)**Getting Started** is added back to the sidebar, and you can click it to return to the page. |

---

---
title: Building a workforce solution
description: Use your PingOne trial to design single sign-on experiences for employees, partners, and vendors.
component: pingone
page_id: pingone:getting_started_with_pingone:p1_trial_workforce_solution
canonical_url: https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_trial_workforce_solution.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 10, 2026
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Building a workforce solution

With your PingOne trial, you can quickly design single sign-on experiences for your employees, partners, and vendors.

## About this task

After creating a new workforce environment, the solution designer opens, which will walk you through the process of designing your experiences. To return to the designer in the future, click **Get Started** at the top of the page.

## Steps

1. The solution designer outlines the steps involved in this process. Start by clicking **Add Test Users** to add test users to your environment.

   ![Screen capture of the workforce solution designer.](_images/xaq1683240557185.png)

   The **Add Users** page opens. If you chose to have PingOne generate test users and populations to your environment, you'll see them listed on this page.

   Follow the steps outlined in the online guide to add a test user to the environment.

2. On the second step, you can browse the Application Catalog to see which applications are available in the environment or click **Add Applications** to add a new application to the environment. An online guide walks you through the process.

3. On the third step, select the type of authentication experience you want your users to have when they sign on to your application or service for the first time and click **Save**.

   Choose between:

   * **User name and password**: Require your users register with a username and password.

   * **Username, password, and MFA with the PingID app**: Requires users to provide their username, password, and additional verification through the PingID app.

   * **Risk-based MFA**: Requires users to provide their username and password, and an additional verification factor if risk signals are detected.

   * **Passwordless - FIDO2 (Biometrics, Security Keys)**: Transition to passwordless authentication. Requires users to initially provide their usernames and passwords and authenticate with MFA. Then, they can register devices to enable biometric or security key authentication.

4. To test the user sign-on experience, click **Launch Application Portal** and sign on to the application with a test user's credentials.

5. To modify these experiences, select different options in the solution designer and continue to test them until you're satisfied.

6. Continue to explore and customize your PingOne workforce trial, and explore the additional capabilities highlighted at the bottom of the page.

---

---
title: Building solutions
description: Build identity solutions in PingOne by selecting packaged solutions or creating your own.
component: pingone
page_id: pingone:getting_started_with_pingone:p1_building_solutions
canonical_url: https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_building_solutions.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 10, 2026
section_ids:
  adding-environments: Adding environments
  before-you-begin: Before you begin
  steps: Steps
  result: Result:
  result-2: Result:
  result-3: Result
  next-steps: Next steps
  p1-deploy-products: Deploying products and services
  steps-2: Steps
  result-4: Result:
---

# Building solutions

If you have an organization administrator role, you can build powerful identity solutions in minutes. Choose one of the packaged solutions or build your own.

Regardless of whether your solution includes one software product, one service, or a collection of products and services, wizards guide you through the process of creating new environments for the products and services you select, and instructions are provided for deploying each component.

For descriptions of each product and service available, click the **Explore** tab. Select a product or service icon to review its description and to access documentation, APIs, code examples, data sheets, and videos for that product or service.

![A screenshot showing information about PingOne when it is selected on the Explore tab.](_images/nuf1676326739823.png)

## Adding environments

The first step in building an identity solution is adding an environment to organize your Ping products and services.

### Before you begin

Determine what type of solution you're building. Filter the products and services by the type of audience you serve with your identity and access management solution:

* Customer solutions

  Help you create sign-on experiences for your clients and consumers. Products and services relevant to serving your clients and consumers are added to the environment.

* Workforce solutions

  Help you create sign-on experiences for your organization's employees. Products and services relevant to serving your employees and partners are added to the environment.

* Build your own solution

  Allows you to build a hybrid solution by selecting from all available products and services.

|   |                                                                                                                                                                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | When you select **Customer solution** or **Workforce solution**, a combination of preselected services designed to support your customer or workforce use cases is added to the environment. If your license doesn't cover the services that are included, you can select **Build your own solution** to select from products and services for which you have a license. |

### Steps

1. In the PingOne admin console sidebar, click the Ping Identity logo to open the **Environments** page.

2. Click the **[icon: plus, set=fa]**icon.

   ![A screenshot of the Environments page in PingOne.](_images/vxj1676308916876.png)

   #### Result:

   The **Create Environment** setup assistant starts.

3. To indicate whether you are building a customer solution, workforce solution, or custom solution, select the appropriate option.

   #### Result:

   **Create Environment** lists the main tasks that can be completed using the solution type.

   ![A screenshot of the Create Environment screen in PingOne.](../_images/ppz1683237101125.png)

4. Click **Next**.

   The services that will be deployed to your new environment are listed.

5. To add or remove them from your solution, select and deselect products and services as necessary, then click **Next**.

   Many of your selections are deployed automatically, but you might be asked how to deploy a connected product. Answer the questions to the best of your ability. You can change them later.

6. Define your environment by entering the following:

   | Field                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                       |
   | -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Environment Name**                                                             | A unique identifier for the environment.                                                                                                                                                                                                                                                                                                                                          |
   | **Description** (optional)                                                       | A brief description of the environment.                                                                                                                                                                                                                                                                                                                                           |
   | **Environment Type**                                                             | Select **Sandbox** or **Production**.Sandbox environments are typically used for configuration and testing before deployment. Production environments are typically used for live configurations that are deployed for real-world use. Learn more about environment types in [Sandbox and Production environments](../introduction_to_pingone/p1_introduction.html#p1-env-types). |
   | **Generate sample populations and users in this environment**                    | Select this checkbox to generate two populations and 40 sample users in the new environment.                                                                                                                                                                                                                                                                                      |
   | **Region**                                                                       | The appropriate geographical region for the environment. The list shows only regions that are included with your license.&#xA;&#xA;You can't change the region after the environment has been created.                                                                                                                                                                            |
   | **License**                                                                      | Select the license to use for this environment. The available licenses for your organization are shown in the **License** list. For more information, see [Licenses and Platform Limits](p1_licenses.html).                                                                                                                                                                       |
   | **Include a solution designer to easily design and test experiences** (optional) | Workforce solutions only. If selected, after you create your environment, a solution designer opens and walks you through the process of designing your experiences.                                                                                                                                                                                                              |

### Result

The new environment is created in your PingOne organization.

If you chose to build a workforce solution, and selected the solution designer option, the solution designer opens and guides you through the process of designing and testing registration and sign-on experiences in less than 5 minutes.

If you did not select the solution designer option, or if you didn't build a workforce solution, the **Environments** page opens. Locate your new environment by sorting the list alphabetically or by date created, or enter the environment name in the search box.

### Next steps

Deploy your solution. Learn more in [Deploying products and services](#p1-deploy-products).

## Deploying products and services

After creating an environment for your Ping products and services, set up the products and services.

### Steps

1. On the **Environments** page, select the environment that you just created.

   #### Result:

   The environment details pane opens and lists the products and services that are included in the environment, along with details such as the environment ID, environment type, URLs for the environment, license information, and so on. If setup is incomplete for a product, it's grayed out, and a tooltip indicates that configuration is needed.

2. Click **Manage Environment** to go to the **Overview** page for the environment.

3. In the **Services** section, locate the service that requires configuration, expand **View Setup Instructions**, and complete the setup.

   The ways in which you set up products and services vary. The following example displays the instructions for setting up PingFederate.

   ![In this screen capture, PingOne is not yet set up. Setup instructions are provided.](_images/ukn1606923357155.png)

   Cloud software products are most easily deployed using Docker images, so click the **Docker** link and complete the appropriate steps. Learn more about deploying Ping products using Docker on the [Ping Identity DevOps site](https://devops.pingidentity.com/).

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | * PingOne for Enterprise and PingOne services do not require additional setup or deployment after the environment in which they reside is created. PingOne for Enterprise environments are created as part of the procurement process or can be created in a trial using the [sign up link](https://www.pingidentity.com/en/trials/p14e-trial.html).

   * PingOne services are deployed automatically based on what is selected when the environment is added.

   * When you add other Ping products to your environment, you can set up single sign-on and centralize management through PingOne. |

---

---
title: Completing the administrator account registration
description: Complete the PingOne administrator account registration to gain access to your account and environment.
component: pingone
page_id: pingone:getting_started_with_pingone:p1_complete_admin_registration
canonical_url: https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_complete_admin_registration.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 10, 2026
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  choose-from: Choose from:
  result: Result:
  result-2: Result:
  result-3: Result
---

# Completing the administrator account registration

When you receive an email indicating that you were added as an administrator in PingOne, verify your email address and update your password to complete the registration process.

## Before you begin

You should have received the following information from the PingOne administrator who added you as an administrator:

* Your PingOne user name if it is different from your email address.

* The **Console Login URL** for the environment that you are being added to.

* (Optional) A temporary password.

## Steps

1. Go to the PingOne console using the URL you received from the administrator.

2. Enter your PingOne **Username**.

3. Update your **Password**.

   ### Choose from:

   * If you received a temporary password, enter it and create a new password when prompted.

   * Click **Forgot Password**, enter your PingOne username on the **Password Reset** window, and click **Submit**.

     An email containing a recovery code is sent to the email address associated with your PingOne user account. Paste the code where indicated on the **Enter New Password** window. Create a new password and click **Save**.

     ### Result:

   You are signed on to the PingOne administrator console.

4. On **Verify Email Address**, click **Verify**.

   ### Result:

   A new verification code is sent to your email address.

5. Paste the verification code where indicated and click **Confirm**.

## Result

Your administrator account registration is complete.

---

---
title: Creating an environment
description: Create a PingOne environment using the setup assistant to organize your Ping Identity products and services.
component: pingone
page_id: pingone:getting_started_with_pingone:p1_getting_started_adding_environment
canonical_url: https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_getting_started_adding_environment.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 10, 2026
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
  result-2: Result
---

# Creating an environment

One of the first things you should do after you start a PingOne trial or purchase a PingOne license is to create an environment. A setup assistant guides you through this process.

## About this task

|   |                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------- |
|   | You must have the Organization Admin role or a custom role with equivalent permissions to create an environment. |

## Steps

1. In the PingOne admin console sidebar, click the Ping Identity logo to open the **Environments** page.

2. Click the **[icon: plus, set=fa]**icon.

   ![A screenshot of the Environments page in PingOne.](_images/vxj1676308916876.png)

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
   | **License**                                                                      | Select the license to use for this environment. The available licenses for your organization are shown in the **License** list. For more information, see [Licenses and Platform Limits](p1_licenses.html).                                                                                                                                                                       |
   | **Include a solution designer to easily design and test experiences** (optional) | Workforce solutions only. If selected, after you create your environment, a solution designer opens and walks you through the process of designing your experiences.                                                                                                                                                                                                              |

7. Click **Finish**.

## Result

The new environment is created in your PingOne organization.

If you chose to build a workforce solution, and selected the solution designer option, the solution designer opens and guides you through the process of designing and testing registration and sign-on experiences in less than 5 minutes.

If you did not select the solution designer option, or if you didn't build a workforce solution, the **Environments** page opens. Locate your new environment by sorting the list alphabetically or by date created, or enter the environment name in the search box.

---

---
title: Getting Started with PingOne
description: Get started with the PingOne admin console.
component: pingone
page_id: pingone:getting_started_with_pingone:p1_getting_started
canonical_url: https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_getting_started.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 10, 2026
section_ids:
  environments-page: Environments page
  more-information: More information
---

# Getting Started with PingOne

The PingOne admin console simplifies environment organization and provides access to admin consoles for all Ping products and services.

From the main administrator console, you have one-click access to:

* Documentation, the API, code examples, data sheets, and videos for each product and service

* Interactive wizards that make it easy to build custom solutions and configure the Ping platform for any cloud environment scenario

To access the admin console for your organization, sign on to your account from either pingidentity.com or support.pingidentity.com and complete a few simple steps. Learn more in [Accessing the PingOne admin console](p1_access_admin_console.html).

## Environments page

The first time you access the admin console, the **Environments** page displays and lists the environments to which you have access. If you have the Organization Admin role, you'll see all of the environments in your organization.

|   |                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Subsequent sign ons take you to the admin console for the environment you last accessed. To return to the **Environments** page, click the Ping Identity logo on the sidebar or the **Home** icon at the top of the console. |

![A screen capture of the Environments page, listing the environments you have access to in your organization.](_images/vxj1676308916876.png)

Most organizations include an **Administrators** environment for keeping your administrator users separate from your end users. This environment is pinned to the top of the list.

|   |                                                                                                                                                                                                                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Older organizations might not have an **Administrators** environment by default, or the **Administrators** environment might be called something else. Whether or not you have an **Administrators** environment, you should manage all administrators in their own environment to separate them from end users and improve the security posture of your organization. |

Use a combination of the search box and the sorting options to locate the environment you want quickly.

|   |                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The **Administrators** environment stays at the top of the list, regardless of the sort order you choose. However, if you enter search criteria that does not match the **Administrators** environment, it's not displayed in the search results. |

Click an environment in the list to open the details pane.

![A screenshot of the environment details view of the BX Finance environment showing included services, a connected service that requires configuration, environment and organization IDs, and environment URLs for accessing the console, self-service portal, and the application portal.](_images/dlj1710866077378.png)

To access the dashboard for a particular service or connected product in the environment, click the service or product name under **Services** or **Connected Services**.

|   |                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------- |
|   | If a connected product or service is not configured, it's grayed out and a tooltip indicates that it requires configuration. |

Click **Manage Environment** to go to the **Overview** page for the environment, which includes:

* A list of the products and services included in the environment

* A graph showing the activity that has occurred within the environment (if the environment contains PingOne services)

* Links to documentation, APIs, and code examples for each product and service in the environment

The menu options in the sidebar vary depending on which products and services are included in the environment.

The following example shows all of the services and most of the top-level menus.

![A screen capture of an environment dashboard that provides an overview of the activity within the environment.](../_images/zla1676309052731.png)

## More information

Learn more about the PingOne APIs in the [PingOne Platform API Reference](https://developer.pingidentity.com/pingone-api/platform/introduction.html).

Learn more about configuring applications in [Editing an application](../applications/p1_editing_applications.html).

Learn more about authorization flows in [Authorization flow by grant type](https://developer.pingidentity.com/pingone-api/foundations/authentication-concepts/authorization-flow-by-grant-type.html), [OpenID Connect/OAuth 2](https://developer.pingidentity.com/pingone-api/auth/openid-connect-oauth-2.html), and [Flows](https://developer.pingidentity.com/pingone-api/auth/flows/flows-1.html).

---

---
title: Getting started with PingOne SSO
description: Get started with PingOne SSO by signing on and setting up your organization, environments, applications, and authentication policies.
component: pingone
page_id: pingone:getting_started_with_pingone:p1_gettingstarted
canonical_url: https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_gettingstarted.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 10, 2026
section_ids:
  about-this-task: About this task
  next-steps: Next steps
---

# Getting started with PingOne SSO

The first time you start PingOne, sign on with the default credentials that were set up during provisioning. The initial configuration includes a default organization, environment, and population. You can create additional environments, populations, and users for those populations.

## About this task

After you start PingOne, you can set up your applications to work with PingOne. PingOne manages access to those applications and ensures that authorized users have access to the applications that they need.

PingOne uses an organization-based model to define tenant accounts and their related entities. The organization is the top-level identifier and defines your entire enterprise within the platform.

By default, your organization includes an `Admin` license, which contains an Admin environment and Administrators population. The Administrators population contains the initial administrator user. You should create all administrators in the Administrators population to make it easier to manage them and to help prevent privilege escalation.

Your organization also includes a `Trial` license and an End-User Sandbox environment that contains two populations and some sample users.

## Next steps

These tasks can help you get started setting up PingOne for your organization:

* To sign on, see [Administrators: Managing your PingOne environment](../managing_your_pingone_user_profile/p1_signin.html).

* To replace the default Ping Identity logo with the logo for your organization, see [Editing environment branding](../user_experience/p1_edit_environment_branding.html).

* To add applications for your users, see [Adding an application](../applications/p1_applications_add_applications.html).

* To add an authentication policy, see [Adding an authentication policy](../authentication/p1_add_an_auth_policy.html).

* To manage certificates, see [Adding a certificate](../settings/p1_addcertificate.html).

* To add an external identity provider, see [External IdPs](../integrations/p1_external_idps.html).

* To find answers to common questions, see the [Support and Community portal](https://support.pingidentity.com/).

---

---
title: Inviting administrators to register
description: Invite other PingOne administrators to register by sending registration invitations.
component: pingone
page_id: pingone:getting_started_with_pingone:p1_invite_admins_register
canonical_url: https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_invite_admins_register.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 10, 2026
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  next-steps: Next steps
---

# Inviting administrators to register

You can invite administrators to register with PingOne using their name and email address. These users receive an email containing a verification code, as well as a link to complete the registration process.

You can also set an expiration time on the invitation. The maximum time allowed is 24 hours.

## Before you begin

To invite other administrators to access PingOne, you must use PingOne as your identity provider, have [administrator security](../settings/p1_administrator_security.html) enabled with PingOne or a hybrid authentication source, and have the appropriate permissions.

## Steps

1. In the PingOne admin console for the Administrators environment, go to **Directory > Users** and select **Invite Admin** from the **Users** list.

2. Enter the user's email address and first and last name in the appropriate fields.

3. Specify when you want the invitation to expire in the **Invitation Expires** field and click **Next**.

4. On the **Available responsibilities** tab, select the administrator roles you want the new administrator to have for each environment, such as **Environment Admin**, **Identity Data Admin**, or **Organization Admin**.

   |   |                                                                                                                                                                                                                                                                                                   |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You cannot assign privileges greater than those you are assigned. Best practice is to assign only the roles necessary for new administrators to do their jobs. Learn more in [Administrator Roles](../directory/p1_roles.html) and [Managing user roles](../directory/p1_manage_user_roles.html). |

5. Click **Send Invitation**.

   Invitations display on the **Users** page. The toggle indicates whether the invitation is still active. Click the user to view details about the invitation.

6. (Optional) If you want to revoke the invitation or resend it with a new authentication code, click **Revoke** or **Resend**.

   |   |                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------- |
   |   | The administrator's email address is not yet verified, but will be when the administrator accepts the invitation. |

   ![A screen capture of the Users page highlighting the administrator's email address, which is not currently verified.](_images/revoke_resends.jpg)

## Next steps

The new administrator accepts the invitation and signs on to the admin console.

---

---
title: License FAQ
description: Find answers to frequently asked questions about PingOne licenses.
component: pingone
page_id: pingone:getting_started_with_pingone:p1_license_faq
canonical_url: https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_license_faq.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 10, 2026
section_ids:
  license-types-and-expiration: License types and expiration
  license-assignment-and-activation-issues: License Assignment and Activation Issues
  service-trials-and-expansions: Service Trials and Expansions
  limits-and-usage-restrictions: Limits and Usage Restrictions
  getting-help-and-support: Getting Help and Support
---

# License FAQ

The following sections contain frequently asked questions about PingOne licenses.

## License types and expiration

* What happens when a trial license expires?

  When a trial license expires, access to the environment is disabled. You'll need to purchase a full license to continue using those services. If you're unsure about next steps, contact Ping Identity Sales at [www.pingidentity.com/en/company/contact-sales.html](https://www.pingidentity.com/en/company/contact-sales.html).

* What happens when a paid license expires?

  When a paid license expires, administrators retain access to the environment, but the ability to make configuration changes is paused. This ensures that administrators can still manage license updates or assignments as needed. End-user functionality continues without interruption. To restore full administrative functionality, assign the environment to an active license. For assistance, contact Ping Identity Sales at [www.pingidentity.com/en/company/contact-sales.html](https://www.pingidentity.com/en/company/contact-sales.html).

* Why do my PingID tenants still show as trials when I create them from PingOne, even though I have a full license?

  PingID licenses are managed separately from PingOne. Even if you have a full PingOne license, your PingID tenant remains in trial status until it is explicitly upgraded. Contact your Account Executive (AE) to ensure your PingID tenant is fully licensed.

* Why can't I change my ADMIN license to something else?

  ADMIN licenses enable specific functionality for managing administrator environments and cannot be modified or reassigned. If you need different capabilities or have questions about your current setup, contact your AE for guidance.

## License Assignment and Activation Issues

* I just purchased a PingOne service. Why am I being told I can't add that service to my environment?

  Ensure that the environment is associated with the new license. For example, if you have a PingOne MFA license and purchase PingOne Protect as an additional service, your PingOne MFA license must be upgraded to an MFA-Protect license to use PingOne Protect features in that environment. A new Protect-only license is not sufficient because you can't assign more than one license to an environment. If the new license doesn't include all of the other services you're using in that environment, contact Ping Identity Sales at [www.pingidentity.com/en/company/contact-sales.html](https://www.pingidentity.com/en/company/contact-sales.html).

* I just purchased a PingOne service. Why do I see a banner saying my license has expired?

  Ensure that the environment is associated with the new license. Learn more in [Assigning a license](p1_license_assignment.html). If the message persists, you might have other environments that are still associated with the earlier license. You can associate those environments with the new license or any other current license that provides the same set of PingOne services.

## Service Trials and Expansions

* I have services I paid for. What should I do if I want to try another service?

  You can create a trial environment for any product in combination with your paid services by creating a new environment. Select the paid services you want to use, then select the **View Trials** slider to see all the services that are not currently licensed. Adding trial services to an environment generates a 30-day trial license.

## Limits and Usage Restrictions

* Why can't I create any more environments?

  Licenses define limits for the maximum number of environments to which they can be assigned. If you need to create additional environments, contact Ping Identity Sales at [www.pingidentity.com/en/company/contact-sales.html](https://www.pingidentity.com/en/company/contact-sales.html).

* Why can't I create any more identities?

  Licenses have both a soft limit and a hard limit on the number of identities you can create. User limits are based on the total number of identities across all of the environments assigned to a license. Learn more in [Licenses and identity limits](p1_licenses_and_identities.html).

## Getting Help and Support

* Who should I contact if I need help?

  If you need help determining which license is right for your needs, reach out to your AE. If you're experiencing issues with your current license or functionality is missing, and you have a paid license, contact Ping Identity Support at <https://support.pingidentity.com>.

---

---
title: Licenses and identity limits
description: Use the following information to understand the various licensing constraints associated with PingOne products and services.
component: pingone
page_id: pingone:getting_started_with_pingone:p1_licenses_and_identities
canonical_url: https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_licenses_and_identities.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 24, 2025
section_ids:
  pingone: PingOne
  pingone-authorize: PingOne Authorize
  section_ank_jbn_5bc: PingOne DaVinci
  licensed-by-identities: Licensed by identities
  licensed-by-transactions-flow-based: Licensed by transactions (flow-based)
  pingone-for-customers-passwordless: PingOne for Customers Passwordless
---

# Licenses and identity limits

Ping Identity products have specific licensing limits that offer crucial protection for both customers and Ping Identity. Use the following information to understand the various licensing constraints associated with Ping Identity products and navigate and optimize their usage within the defined boundaries.

## PingOne

A PingOne license includes a soft limit and a hard limit for the maximum number of identities. A license can be assigned to one or more environments, and user limits are based on the total number of identities across all of the environments assigned to a license.

The soft limit is usually 12 times the licensed Monthly Active Users (MAU) or Average Annual Users (AAU) of your PingOne subscription. You can continue to add users when you've reached the soft limit, but the system will display a warning message.

The hard limit is 10% more than the soft limit, up to the maximum limit of 100 million identities. This strict limit serves as a hard cap that you can't exceed unless you have obtained explicit, written approval from Ping Identity. The need for this exception might arise if your subscribed MAU would theoretically allow for a hard limit exceeding 100 million identities, based on your contracted service levels. When you hit your license's hard limit or reach 100 million identities, whichever is lower, you can no longer add users without contacting [Ping Identity Sales](https://www.pingidentity.com/en/company/contact-sales.html) to change your license.

* Example

  If your licensed MAU is 1 million, the soft limit for your license is 12 million users. The hard limit is 13.2 million users.

  * **Approaching limit**: At 10.8 million users, or 90% of the soft limit for your license, the admin console displays a warning message stating that you are at 90% of your allowed users. At this point, you can continue to add users.

  * **Limit reached**: When you reach the soft limit of 12 million users, the admin console displays another warning message stating that you have reached 100% of your allowed users. You can still add users.

  * **Limit exceeded**: When you reach 13.2 million users, which is the hard limit for the license, the admin console displays a message stating that you can no longer add users and must upgrade your license.

To receive email notifications when you are approaching these limits, configure the following alerts in **Monitoring > Alerts**:

* **Approaching User License Limit**: Triggers an alert when you reach 90% of the soft limit for your license.

* **User License Limit Reached**: Triggers an alert when you reach 100% of the soft limit for your license.

* **User License Limit Exceeded**: Triggers an alert when you reach the hard limit for the license and can no longer add users.

Learn more in [Alerts](../monitoring/p1_alerts.html).

## PingOne Authorize

PingOne Authorize is licensed by identities, and a fair-use transaction allowance is defined for each identity tier. The fair-use transaction allowance corresponds to the total number of licensed identities specified in your PingOne subscription.

For some authorization use cases (for example, when permissions are checked for every page access or operation), the volume of authorization events can be significantly higher than the volume of authentication events. The fair-use transaction allowance provides you and Ping Identity with a shared expectation about the volume of authorization traffic. If this limit isn't sufficient, contact [Ping Identity Sales](https://www.pingidentity.com/en/company/contact-sales.html) about increasing the monthly allowance.

## PingOne DaVinci

PingOne DaVinci is licensed by identities and transactions based on flow invocations. Your limits will be based on one of the following two license types.

### Licensed by identities

PingOne DaVinci is licensed by identities as MAU or AAU with a fair-use transaction allowance as defined in the [Product terms and conditions](https://www.pingidentity.com/en/legal/product-terms.html).

The fair-use transaction allowance corresponds to the total number of licensed identities specified in your PingOne DaVinci subscription. The fair use transaction allowance provides you and Ping Identity with a shared expectation about the volume of DaVinci traffic. If the identities or fair-use limits aren't sufficient, contact [Ping Identity Sales](https://www.pingidentity.com/en/company/contact-sales.html) about increasing the allowance.

### Licensed by transactions (flow-based)

A flow invocation occurs each time a flow (a series of one or more connector executions) is initiated in DaVinci. If a flow launches one or more subflows, the subflows do not count as additional invocations. Only the initial invocation is counted.

|   |                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In the product dashboard and your license, a flow invocation is represented as a flow execution, and each flow invocation counts as a flow execution. |

The flow-based license comes with a fair-use transaction limit of 80 connector executions (previously referred to as API calls) per flow. There is no distinction between the types of connector executions. Ping Identity reserves the right to negotiate per-invoked flow pricing for PingOne DaVinci in the event that usage exceeds flow or connector execution volume limits set in the license. If the limit isn't sufficient, contact [Ping Identity Sales](https://www.pingidentity.com/en/company/contact-sales.html) about increasing volume limits as your usage increases. Learn more in [DaVinci Usage Terms](https://docs.pingidentity.com/davinci/usage_terms/davinci_best_practices_usage_terms.html).

The DaVinci license shows your flow-based entitlements per subscription year.

![Screen capture of active and in-use DaVinci licenses showing flow execution entitlements per subscription year.](_images/qtp1718930557494.png)

The DaVinci dashboard shows the number of flow executions and connector executions that have occurred in a single environment. Use the total of all environment metrics to determine usage against the entitlements.

![Screen capture of the DaVinci dashboard showing flow executions, connector executions, top flows by execution count, and top connectors by execution count for a single environment.](_images/mif1718930739444.png)

## PingOne for Customers Passwordless

PingOne for Customers Passwordless is a solution bundle that is licensed by transactions based on flow invocations (learn more in the [PingOne DaVinci](#section_ank_jbn_5bc) section). It includes using PingOne Protect, PingOne SSO (including Directory), and PingOne MFA in PingOne DaVinci. This solution bundle requires usage of each product only through DaVinci flows.

---

---
title: Licenses and Platform Limits
description: PingOne licenses define service entitlements, quantities, and valid periods for your organization.
component: pingone
page_id: pingone:getting_started_with_pingone:p1_licenses
canonical_url: https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_licenses.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 10, 2026
---

# Licenses and Platform Limits

PingOne licenses define the entitlements a customer has the right to use. That is, which PingOne services, in what quantities, and for what period of time.

If you sign up for Try Ping at [www.pingidentity.com/en/try-ping.html](https://www.pingidentity.com/en/try-ping.html), you'll get an organization and two licenses that are valid for 30 days.

* Admin license. Contains the entitlements for user administration and sign-on functionality to the Admin Portal.

* Trial license. Allows the customer to evaluate the functionality of all PingOne services for 30 days.

If you purchase one or more services, you will get a paid license to replace the trial license.

PingOne services are additive and can be used in various combinations to create a single solution. The PingOne platform operates on the principle of one license per environment, so to use multiple products in the same environment, your license must include all the products you want to use together. For more information, see [Standard license types](p1_license_types.html) or contact Ping Identity Sales at [www.pingidentity.com/en/company/contact-sales.html](https://www.pingidentity.com/en/company/contact-sales.html).

---

---
title: Managing administrator roles
description: Assign built-in or custom roles to users or groups to determine their access in PingOne.
component: pingone
page_id: pingone:getting_started_with_pingone:p1_manage_admin_roles
canonical_url: https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_manage_admin_roles.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2024
section_ids:
  managing-roles-individually: Managing roles individually
  steps: Steps
  result: Result
  managing-roles-using-groups: Managing roles using groups
  managing-group-roles: Managing group roles
  steps-2: Steps
  result-2: Result
  p1-manage-roles-external-groups: Managing administrator roles using external groups
  before-you-begin: Before you begin
  about-this-task: About this task
  steps-3: Steps
  example: Example:
  result-3: Result:
  next-steps: Next steps
---

# Managing administrator roles

You can assign built-in or custom administrator roles to individual users or to groups.

|   |                                                                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Learn more about built-in roles and creating and managing custom roles in [Administrator Roles](../directory/p1_roles.html) and [Custom role scenarios](../directory/p1_custom_roles_scenarios_intro.html) before you start assigning roles to administrators. |

## Managing roles individually

Use the **Users** page to add roles to a user.

## Steps

1. In the PingOne admin console, go to the **Administrators** environment.

   |   |                                                                                                                                                                                                              |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Older organizations might not have an **Administrators** environment by default. To improve security posture, separate administrators from end users and manage all administrators in their own environment. |

2. Go to **Directory > Users**.

3. Browse or search for an existing user or create a new one.

   Learn more in [Adding a user in PingOne](../directory/p1_adduser.html).

4. Click the user entry to open the user details panel.

5. Click the **Roles** > **Administrator Roles** tab.

   |   |                                                                                                            |
   | - | ---------------------------------------------------------------------------------------------------------- |
   |   | If there aren't any application roles available in the environment, the settings are on the **Roles** tab. |

   If roles are assigned to the user, they're listed here with information about where those roles apply. For example, in the following image, **BX User** is assigned the following administrator roles:

   * **Advanced Help Desk Admin**: They have this role over one group in one environment.

   * **Application Owner**: They have this role at the environment level in two environments. Because the role is assigned at the environment level, they have the role over all of the applications in both of those environments. In a third environment, they have the role over only one application. That is the only application they can manage in that environment.

   * **Environment Admin**: They have this role for one environment.

   * **Identity Data Admin**: They have this role over one population in one environment.

     ![A screen capture of the user details for BX User. Roles > Administrator Roles is selected, and shows the assignment of the Application Owner role over 2 environments, and in a third over one application. Also shows the Environment Admin role in one environment, the Help Desk Admin role over one group, and the Identity Data Admin over one population.](../_images/p1-user-with-roles-at-multiple-levels.png)

     |   |                                                                                                                                                                                                                                                                                                                                                                        |
     | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | Click the **Info** icon to view the permissions associated with the role. Click the down arrow on the right to view the list of environments, populations, applications, or groups for which the role is assigned. The levels at which a role can be assigned depends on the role. For example, only certain roles can be assigned at the group or application levels. |

     ![Screen capture of the Help Desk Admin role expanded to show detailed information about the group over which the user is assigned the role.](../_images/p1-user-role-level-details.png)

6. Click **Grant Roles**.

   The **Available Responsibilities** tab lists the roles that you're allowed to assign and the environments for which you're allowed to assign them. A responsibility is the combination of the role assignment and the level, or scope, at which the role is applied. Depending on the role, it could be assigned at the organization, environment, population, group, or application level.

   The **Granted Responsibilities** tab lists any roles that are currently assigned.

7. On the **Available Responsibilities** tab, click the role that you want to assign or change and perform any combination of the following:

   1. To assign the role, select the checkboxes next to the applicable environments for which you want the user to have the role.

      |   |                                                                                           |
      | - | ----------------------------------------------------------------------------------------- |
      |   | Click **Select All** or **Remove All** to select or clear all available responsibilities. |

   2. To remove a role assignment, clear the checkboxes next to the applicable environments.

   3. To grant this access for only a portion of the environment, click the **Reduce Access** icon (![image of reduce access icon](../_images/qge1710506304767.png)), select a subset of the available applications, populations, or groups on the **Limit Access** page, and click **Confirm**.

      ![A screen capture of the Limit Access page showing one population selected out of three populations](../_images/qnh1710778106962.png)

      |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | You can grant only roles that are assigned to you or that grant the permissions needed to assign that role to others. For example, if you don't have the Environment Admin role, you can't assign the Environment Admin role to others (and that role won't be listed under **Available Responsibilities**). However, even if you have only the Identity Data Admin role, you can assign either the Identity Data Admin role or the Identity Data Read Only role to others. The permissions for the Identity Data Admin role allow the bearer to assign both of these roles to others.Learn more about the permissions associated with each role in [Roles](https://developer.pingidentity.com/pingone-api/platform/roles.html) in the PingOne API documentation. |

8. Click **Save**.

## Result

The role assignments that you selected are listed on the **Granted Responsibilities** tab.

## Managing roles using groups

Use the **Groups** page to add roles to a group.

Assigning roles to groups allows you to:

* Manage roles for multiple users at once.

* Apply role changes in bulk.

* See users that have a certain role by viewing group members.

For security reasons, only static groups can have roles assigned to them. You can't assign roles to dynamic groups, which have members included based on a filter or rule. With a dynamic group, you might inadvertently add users to the group that would inherit role assignments. Learn more in [Static and dynamic groups](../directory/p1_groups_vs_populations.html#p1-static-dynamic-groups).

When adding users to groups that have roles assigned, be careful not to inadvertently assign a role to a user by adding them to a group. If a user has a role inadvertently assigned to them because they're added to a group, remove the user from the group to remove the role. If a user has a role assigned to them individually, you can remove the role from the user.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * You can assign a role to a group you're a member of only if that role is assigned to you directly as an individual user, and is not assigned to you as part of a group that you belong to.

* If a built-in role you're assigned allows you to assign a different role, you can also assign that role to a group you are a member of. For example, the Identity Data Admin role has permissions that allow it to assign the Identity Data Admin Read Only role. If you're assigned the Identity Data Admin role, you can assign that role or the Identity Data Admin Read Only role to a group.

* An administrator might not have permissions to assign roles but can add or remove users from a group that has role assignments. For example, one administrator can assign roles to a group, and a different administrator can add or remove users from that group, depending on their role assignments.

* You can't add or remove yourself from a group that has roles assigned to it.

* Roles assigned to a group won't affect roles that are assigned to a user individually. If the role isn't assigned to the user directly, the role is removed when they're removed from the group.

* You can assign roles in up to 500 groups. |

### Managing group roles

Assign roles to groups of administrators using the **Groups** page.

## Steps

1. In the PingOne admin console, go to the **Administrators** environment.

   |   |                                                                                                                                                                                                              |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Older organizations might not have an **Administrators** environment by default. To improve security posture, separate administrators from end users and manage all administrators in their own environment. |

2. Go to **Directory > Groups**.

3. Browse for an existing group or create a new one.

   Learn more in [Creating a group](../directory/p1_create_group.html).

4. Click the group entry to open the details panel.

5. Click the **Roles** > **Administrator Roles** tab.

   |   |                                                                                                            |
   | - | ---------------------------------------------------------------------------------------------------------- |
   |   | If there aren't any application roles available in the environment, the settings are on the **Roles** tab. |

   If roles are assigned to the user, they're listed here with information about where those roles apply. For example, in the following image, **BX User** is assigned the following administrator roles:

   * **Advanced Help Desk Admin**: They have this role over one group in one environment.

   * **Application Owner**: They have this role at the environment level in two environments. Because the role is assigned at the environment level, they have the role over all of the applications in both of those environments. In a third environment, they have the role over only one application. That is the only application they can manage in that environment.

   * **Environment Admin**: They have this role for one environment.

   * **Identity Data Admin**: They have this role over one population in one environment.

     ![A screen capture of the user details for BX User. Roles > Administrator Roles is selected, and shows the assignment of the Application Owner role over 2 environments, and in a third over one application. Also shows the Environment Admin role in one environment, the Help Desk Admin role over one group, and the Identity Data Admin over one population.](../_images/p1-user-with-roles-at-multiple-levels.png)

     |   |                                                                                                                                                                                                                                                                                                                                                                        |
     | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | Click the **Info** icon to view the permissions associated with the role. Click the down arrow on the right to view the list of environments, populations, applications, or groups for which the role is assigned. The levels at which a role can be assigned depends on the role. For example, only certain roles can be assigned at the group or application levels. |

     ![Screen capture of the Help Desk Admin role expanded to show detailed information about the group over which the user is assigned the role.](../_images/p1-user-role-level-details.png)

6. Click **Grant Roles**.

   The **Available Responsibilities** tab lists the roles that you're allowed to assign and the environments for which you're allowed to assign them. A responsibility is the combination of the role assignment and the level, or scope, at which the role is applied. Depending on the role, it could be assigned at the organization, environment, population, group, or application level.

   The **Granted Responsibilities** tab lists any roles that are currently assigned.

7. On the **Available Responsibilities** tab, click the role that you want to assign or change and perform any combination of the following:

   1. To assign the role, select the checkboxes next to the applicable environments for which you want the user to have the role.

      |   |                                                                                           |
      | - | ----------------------------------------------------------------------------------------- |
      |   | Click **Select All** or **Remove All** to select or clear all available responsibilities. |

   2. To remove a role assignment, clear the checkboxes next to the applicable environments.

   3. To grant this access for only a portion of the environment, click the **Reduce Access** icon (![image of reduce access icon](../_images/qge1710506304767.png)), select a subset of the available applications, populations, or groups on the **Limit Access** page, and click **Confirm**.

      ![A screen capture of the Limit Access page showing one population selected out of three populations](../_images/qnh1710778106962.png)

      |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | You can grant only roles that are assigned to you or that grant the permissions needed to assign that role to others. For example, if you don't have the Environment Admin role, you can't assign the Environment Admin role to others (and that role won't be listed under **Available Responsibilities**). However, even if you have only the Identity Data Admin role, you can assign either the Identity Data Admin role or the Identity Data Read Only role to others. The permissions for the Identity Data Admin role allow the bearer to assign both of these roles to others.Learn more about the permissions associated with each role in [Roles](https://developer.pingidentity.com/pingone-api/platform/roles.html) in the PingOne API documentation. |

8. Click **Save**.

## Result

The role assignments that you selected are listed on the **Granted Responsibilities** tab.

## Managing administrator roles using external groups

### Before you begin

Ensure that you have one administrator user with direct sign-on access to PingOne. Add this user to the Administrators environment to keep them separate from your end users.

|   |                                                            |
| - | ---------------------------------------------------------- |
|   | This task uses *PingOne Admin User* to refer to this user. |

### About this task

You can leverage just-in-time provisioning and use external groups, such as those in an identity store accessed through an external identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)*, to manage administrator role assignment in PingOne.

For example, you configure PingOne to use an external IdP with Active Directory (AD) *(tooltip: \<div class="paragraph">
\<p>A directory service for Windows domain networks, included in most Windows Server operation systems.\</p>
\</div>)* as the identity store. You then create a group in the Active Directory identity store. You add users to this group and provision it to PingOne to ensure that these users have access to PingOne with the appropriate roles.

To use an external group to manage administrator roles in PingOne:

### Steps

1. Add a custom [OIDC](../integrations/p1_add_idp_oidc.html) or [SAML](../integrations/p1_add_identity_provider_saml.html) external IdP in PingOne.

   |   |                                                                                                         |
   | - | ------------------------------------------------------------------------------------------------------- |
   |   | Managing roles using external groups is currently supported only for custom OIDC or SAML external IdPs. |

   When you get to the step for mapping attributes, you must map at least the following PingOne user attributes to the corresponding attributes for the identity provider:

   * **Username**

   * **Email Address**

   * **External Group Names**

     #### Example:

     ![Screen capture showing the mapping of the Username, Email Address, and External Group Names attributes in PingOne to the corresponding attributes in an external IdP.](_images/vcs1707858536004.png)

     The values in the previous image are for example purposes only. The external attribute names will vary depending on the provider.

     |   |                                                                                                                                                                                                                                                                             |
     | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | Set **Update Condition** for the **Email Address** and **External Group Names** attributes to **Always**. This ensures that these attributes are updated in PingOne whenever they are updated in the external IdP and that their access and permissions are always in sync. |

     Map additional attributes as needed.

   |   |                                                                                                                          |
   | - | ------------------------------------------------------------------------------------------------------------------------ |
   |   | When authenticating into PingOne from an external IdP, ensure that you enable MFA as part of your authentication policy. |

2. Create the applicable groups in your external identity store.

3. During the initial group set up, add the *PingOne Admin User* to each external group that you want to provision to PingOne.

   |   |                                                                                                                                                                                                                                                                                               |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can add more users, but at a minimum each group must contain one user with direct access to PingOne before you continue. The process for adding users to groups depends on the external identity store that you are using. Follow the steps in the documentation for your identity store. |

4. Sign on to PingOne as the *PingOne Admin User*.

   #### Result:

   The external groups are provisioned to PingOne using just-in-time provisioning.

   Learn more in [Just-in-time provisioning of external groups](../directory/p1_provision_external_groups.html).

5. Assign the appropriate admin roles to the groups in PingOne.

   Learn more on the **Using groups** tab in [Managing roles using groups](#managing-roles-using-groups).

   |   |                                                                                                                                                                                                                    |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | You must assign at least one role to each group, or the users will be unable to sign on to PingOne.These roles are assigned to all users currently in the group and to any users added to the group in the future. |

6. Add users to the external group in the external identity store as needed to ensure that they can access PingOne with the appropriate role assignments.

   Similarly, remove users from the external group to remove their access to PingOne or to move them to a group with different role assignments.

### Next steps

You should audit the users in your external directory regularly to ensure that their group membership and level of access is correct.

---

---
title: Managing administrators
description: Invite or add PingOne administrators and assign their permissions using roles.
component: pingone
page_id: pingone:getting_started_with_pingone:p1_manage_administrators
canonical_url: https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_manage_administrators.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 10, 2026
section_ids:
  invite_admin: Inviting administrators to register
  before-you-begin: Before you begin
  steps: Steps
  next-steps: Next steps
  accept_invitation: Accepting the administrator account registration invitation
  steps-2: Steps
  result: Result:
  Adding_admins: Adding administrators
  steps-3: Steps
  next-steps-2: Next steps
  Complete_registration: Completing the administrator account registration
  before-you-begin-2: Before you begin
  steps-4: Steps
  choose-from: Choose from:
  result-2: Result:
  result-3: Result:
  result-4: Result
---

# Managing administrators

If you use PingOne as your identity provider, have [administrator security](../settings/p1_administrator_security.html) enabled with PingOne or a hybrid authentication source, and you have the appropriate permissions, you can invite other administrators to register for PingOne.

Or, if you're an administrator with the appropriate permissions, you can add new administrators yourself and define their permissions using roles.

Complete the appropriate set of steps:

* [Inviting administrators to register](#invite_admin)

  * [Accepting the administrator account registration invitation](#accept_invitation)

* [Adding administrators](#Adding_admins)

  * [Completing the administrator account registration](#Complete_registration)

|   |                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------- |
|   | To prevent privilege escalation, you cannot create an administrator user if you do not have administrator privileges. |

## Inviting administrators to register

You can invite administrators to register with PingOne using their name and email address. These users receive an email containing a verification code, as well as a link to complete the registration process.

You can also set an expiration time on the invitation. The maximum time allowed is 24 hours.

### Before you begin

To invite other administrators to access PingOne, you must use PingOne as your identity provider, have [administrator security](../settings/p1_administrator_security.html) enabled with PingOne or a hybrid authentication source, and have the appropriate permissions.

### Steps

1. In the PingOne admin console for the Administrators environment, go to **Directory > Users** and select **Invite Admin** from the **Users** list.

2. Enter the user's email address and first and last name in the appropriate fields.

3. Specify when you want the invitation to expire in the **Invitation Expires** field and click **Next**.

4. On the **Available responsibilities** tab, select the administrator roles you want the new administrator to have for each environment, such as **Environment Admin**, **Identity Data Admin**, or **Organization Admin**.

   |   |                                                                                                                                                                                                                                                                                                   |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You cannot assign privileges greater than those you are assigned. Best practice is to assign only the roles necessary for new administrators to do their jobs. Learn more in [Administrator Roles](../directory/p1_roles.html) and [Managing user roles](../directory/p1_manage_user_roles.html). |

5. Click **Send Invitation**.

   Invitations display on the **Users** page. The toggle indicates whether the invitation is still active. Click the user to view details about the invitation.

6. (Optional) If you want to revoke the invitation or resend it with a new authentication code, click **Revoke** or **Resend**.

   |   |                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------- |
   |   | The administrator's email address is not yet verified, but will be when the administrator accepts the invitation. |

   ![A screen capture of the Users page highlighting the administrator's email address, which is not currently verified.](_images/revoke_resends.jpg)

### Next steps

The new administrator accepts the invitation and signs on to the admin console.

## Accepting the administrator account registration invitation

When you receive an email indicating that you were added as an administrator in PingOne, copy the invite code and paste it into PingOne to complete the registration process.

### Steps

1. Click **Complete Registration** on the email you received.

2. On the sign-on page, enter your PingOne username.

3. Click the **Complete Registration** button.

4. Copy the invite code from the email and paste it into the **Invite Code** field.

   |   |                                                                                                                                        |
   | - | -------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you enter an incorrect invite code five times, you will be locked out of the account and the invitation will need to be sent again. |

   ![A screen capture of the screen users see when they complete their registration.](_images/complete_registration.jpg)

5. Enter and verify a new password for the account and click **Continue**.

   #### Result:

   You are signed on to the PingOne admin console.

## Adding administrators

You can designate an existing user as an administrator or create a new administrator user.

|   |                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------- |
|   | To prevent privilege escalation, you cannot create an administrator user if you do not have administrator privileges. |

### Steps

1. In the Administrators environment, go to **Directory > Users** and browse or search for the user you that want to make an administrator.

   |   |                                                                                                                                                                                                                                                     |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To create a new user with administrator privileges, click the **[icon: plus, set=fa]**icon. Learn more in [Adding a user in PingOne](../directory/p1_adduser.html). All administrator users should be maintained in the Administrators environment. |

2. Click the user entry to open the user details panel.

3. On the **Roles > Administrator Roles** tab, click **Grant roles**.

   |   |                                                                                                            |
   | - | ---------------------------------------------------------------------------------------------------------- |
   |   | If there aren't any application roles available in the environment, the settings are on the **Roles** tab. |

4. Select an administrator role, such as **Environment Admin**, **Identity Data Admin**, or **Organization Admin**.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | You cannot assign privileges greater than those you are assigned. When you are determining which role to assign, consider the role that has the minimum permissions necessary for the administrator to perform their job responsibilities. Scope that role according to the levels at which the administrator should have this access.Learn more in [Administrator Roles](../directory/p1_roles.html) and [Managing user roles](../directory/p1_manage_user_roles.html). |

5. Click **Save**.

6. On the **Profile** tab, click **Verify** to send a verification email to the user.

   |   |                                                          |
   | - | -------------------------------------------------------- |
   |   | All administrator users must verify their email address. |

7. Go to **Settings > Environment Properties** and copy the **Console Login URL**.

8. Contact the new administrator and provide them with the following:

   * Their PingOne user name, if different from their email address.

   * The **Console Login URL** from the previous step.

   * (Optional) A temporary password for the console (if you set one up when you created the user).

   * The instructions for [Completing the administrator account registration](p1_complete_admin_registration.html)

### Next steps

The new administrator completes their account registration.

|   |                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Older organizations might not have an **Administrators** environment by default. To improve security posture, separate administrators from end users and manage all administrators in their own environment. |

## Completing the administrator account registration

When you receive an email indicating that you were added as an administrator in PingOne, verify your email address and update your password to complete the registration process.

### Before you begin

You should have received the following information from the PingOne administrator who added you as an administrator:

* Your PingOne user name if it is different from your email address.

* The **Console Login URL** for the environment that you are being added to.

* (Optional) A temporary password.

### Steps

1. Go to the PingOne console using the URL you received from the administrator.

2. Enter your PingOne **Username**.

3. Update your **Password**.

   #### Choose from:

   * If you received a temporary password, enter it and create a new password when prompted.

   * Click **Forgot Password**, enter your PingOne username on the **Password Reset** window, and click **Submit**.

     An email containing a recovery code is sent to the email address associated with your PingOne user account. Paste the code where indicated on the **Enter New Password** window. Create a new password and click **Save**.

     #### Result:

   You are signed on to the PingOne administrator console.

4. On **Verify Email Address**, click **Verify**.

   #### Result:

   A new verification code is sent to your email address.

5. Paste the verification code where indicated and click **Confirm**.

### Result

Your administrator account registration is complete.

---

---
title: PingOne Platform logging and reporting
description: PingOne includes various auditing and reporting tools for admins to monitor events in their PingOne environments.
component: pingone
page_id: pingone:getting_started_with_pingone:p1_logging_reporting_overview
canonical_url: https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_logging_reporting_overview.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 23, 2025
section_ids:
  audit: Audit
  webhooks: Webhooks
  pingone-api: PingOne API
  pingone-app-for-splunk: PingOne App for Splunk
  dashboards: Dashboards
  alerts: Alerts
---

# PingOne Platform logging and reporting

PingOne includes various auditing and reporting tools for admins to monitor events in their PingOne environments.

Use the information in this section to understand the various types of logs and reporting, and options for collecting and accessing log data.

You can retrieve logs through the **Audit** page, by using webhooks, or through the API. You can also use the **Dashboards** page, the **Alerts** page, and the PingOne App for Splunk to monitor your PingOne environment.

## Audit

Use the **Audit** page in the PingOne admin console to run queries on events and actions in the PingOne environment. PingOne auditing functionality captures two types of data that are governed by different retention policies:

* User events

  User events include user creation or deletion, authentications, updates to the user record, and other transactions related to end-user activity. User events are retained for 90 days.

* PingOne configuration events

  Configuration events include configuration changes made to system settings, policies, applications, an integrations. Configuration events are retained for 2 years.

To retain PingOne data for longer than the standard retention periods, set up webhooks to stream the data to your own repository and configure your own retention policy. Learn more in [Webhooks](../integrations/p1_webhooks.html).

|   |                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingOne DaVinci data is retained for 30 days. Learn more in [Debugging and analytics](https://docs.pingidentity.com/davinci/davinci_best_practices/davinci_best_practices_debugging_and_analytics.html) in the DaVinci documentation. |

Learn more about auditing in PingOne in [Audit](../monitoring/p1_reporting.html).

## Webhooks

Use the **Webhooks** page in the PingOne admin console to set up subscriptions for auditing events.

When an event of interest occurs in PingOne, the event is pushed from PingOne to a third-party monitoring system. Webhooks are available in a Splunk-friendly format, a New-Relic-friendly format, and the Ping activity format, which is a versatile, generic JSON format also used by the PingOne API for accessing event data.

Learn more in [Webhooks](../integrations/p1_webhooks.html).

## PingOne API

Use the PingOne User Activities API to monitor user activities in PingOne. The service uses stream processors that listen to `users` and `login_attempts` events. These events are collected and presented by time period.

Learn more in [User activities](https://developer.pingidentity.com/pingone-api/platform/user-activities.html) in the PingOne API documentation.

## PingOne App for Splunk

Use the PingOne App for Splunk to correlate your PingOne webhook data into a meaningful dashboard. Create custom dashboards and reports, monitor activity data, and analyze event data over time.

Learn more in [Installing the PingOne app for Splunk](../developer_tools/p1_monitor_activity_splunk.html#p1-add-splunk-app).

## Dashboards

Use the **Dashboards** page in the PingOne console to view and monitor activities for a particular service. Each capability, such as Authentication, Authorization, Identity Verification, and so on, has its own dashboard.

Learn more in [Dashboards](../introduction_to_pingone/p1_introduction.html#p1-dashboards-intro).

## Alerts

Use the **Alerts** page in the PingOne console to set up alert messages based on the status of certain resources. For a complete list of available alerts, in the PingOne admin console, go to **Monitoring > Alerts**.

Learn more in [Alerts](../monitoring/p1_alerts.html).

---

---
title: PingOne Services logging and reporting
description: Access logs and dashboards for PingOne services.
component: pingone
page_id: pingone:getting_started_with_pingone:p1_services_logging_reporting_overview
canonical_url: https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_services_logging_reporting_overview.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 10, 2026
section_ids:
  pingone-davinci-logging: PingOne DaVinci logging
  pingone-protect-logging: PingOne Protect logging
  pingone-sso-and-pingone-directory-logging: PingOne SSO and PingOne Directory logging
  pingone-verify-logging: PingOne Verify logging
  pingone-mfa-logging: PingOne MFA logging
  pingone-authorize-logging: PingOne Authorize logging
---

# PingOne Services logging and reporting

In addition to the core PingOne platform logging, each PingOne service includes a variety of logs that administrators can use to monitor their environments.

## PingOne DaVinci logging

PingOne DaVinci includes manual logging, a Flow Analytics connector, and a Webhook connector. Learn more in:

* [Debugging and Analytics](https://docs.pingidentity.com/davinci/davinci_best_practices/davinci_best_practices_debugging_and_analytics.html)

* [Flow Analytics Connector](https://marketplace.pingone.com/item/flow-analytics-connector)

* [Webhook Connector](https://marketplace.pingone.com/item/webhook-connector)

* [Dashboard](https://docs.pingidentity.com/davinci/davinci_dashboard.html)

## PingOne Protect logging

For PingOne Protect, you can use the native logging in the PingOne admin console. You can also view real-time data on the **Threat Protection Dashboard**. Learn more in [Threat Protection Dashboard](../threat_protection_using_pingone_protect/p1_protect_dashboard.html).

## PingOne SSO and PingOne Directory logging

For PingOne SSO, you can use the native logging in the PingOne admin console. You can also view real-time data on the **Authentication Dashboard**. Learn more in [Authentication dashboard](../monitoring/p1_auth_dashboard.html).

## PingOne Verify logging

For PingOne Verify, you can use the native logging in the PingOne admin console. You can also view real-time data on the **Identity Verification Dashboard**. Learn more in [using the Identity Verification Dashboard](../identity_verification_using_pingone_verify/p1_verify_monitoring.html#p1_verify_dashboard).

PingOne Verify also includes webhooks and metrics through the PingOne API. Learn more in:

* [Subscriptions](https://developer.pingidentity.com/pingone-api/platform/subscriptions-webhooks.html) in the PingOne Platform API Reference

* [Verification Metrics](https://developer.pingidentity.com/pingone-api/verify/verification-metrics.html) in the PingOne Platform API Reference

## PingOne MFA logging

For PingOne MFA, you can use the native logging in the PingOne admin console. You can also view real-time data on the **MFA Dashboard**. Learn more in [MFA dashboard](../monitoring/p1_mfa_dashboard.html).

PingOne MFA also includes device logs that you can access through the PingOne API. Learn more in [Send MFA Device Logs](https://developer.pingidentity.com/pingone-api/mfa/users/mfa-devices/send-mfa-device-logs.html) in the PingOne Platform API Reference.

## PingOne Authorize logging

For PingOne Authorize, you can use the native logging in the PingOne admin console. You can also view real-time data on the **Authorization Dashboard**. Learn more in:

* [PingOne Authorize event monitoring](../authorization_using_pingone_authorize/p1az_monitoring_decision_endpoint_events.html)

* [Authorization Dashboard](../authorization_using_pingone_authorize/p1_az_dashboard.html)