---
title: Accessing PingCentral
description: Instructions for accessing PingCentral.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_application_owners:pingcentral_accessing/pingcentral_accessing_pc
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_application_owners/pingcentral_accessing/pingcentral_accessing_pc.html
revdate: October 14, 2025
section_ids:
  steps: Steps
---

# Accessing PingCentral

PingCentral is a web-based application that you access from a URL. For the best possible experience, use Chrome or Firefox as your browser.

## Steps

1. Contact your IAM Administrator for the PingCentral URL and your sign-on credentials.

2. Enter your credentials.

   |   |                                                                                                              |
   | - | ------------------------------------------------------------------------------------------------------------ |
   |   | If you have multiple failed login attempts, you wil be locked out of PingCentral for a short period of time. |

---

---
title: Adding applications
description: Instructions for adding applications to PingCentral.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_application_owners:pingentral_adding_apps/pingcentral_adding_apps
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_application_owners/pingentral_adding_apps/pingcentral_adding_apps.html
revdate: October 13, 2025
page_aliases: ["pingcentral_info_pa_templates.adoc", "pingcentral_pa_templates.adoc", "pingcentral_path_patterns.adoc", "pingcentral_resources.adoc", "pingcentral_rules_policies.adoc", "pingcentral_selecting_template.adoc", "pingcentral_using_oauth_templates.adoc", "pingcentral_using_saml_templates.adoc"]
section_ids:
  select_template: Selecting a template
  steps: Steps
  oauth_template: Using OAuth and OIDC templates
  before-you-begin: Before you begin
  steps-2: Steps
  saml_template: Using SAML 2.0 templates
  before-you-begin-2: Before you begin
  steps-3: Steps
  pa_template: Using PingAccess templates
  before-you-begin-3: Before you begin
  steps-4: Steps
  pa_info: Information needed to add PingAccess applications
  resources: Resources
  path-patterns: Path patterns
  rules-and-policies: Rules and policies
---

# Adding applications

Before you can promote applications to development environments for testing, you must add them to PingCentral.

To add applications to PingCentral, you can use OAuth, OIDC, SAML, and PingCentral templates to apply security configurations to your applications. Wizards guide you through these processes.

Learn more:

* [Selecting a template](#select_template)

* [Using OAuth and OIDC templates](#oauth_template)

* [Using SAML templates](#saml_template)

* [Using PingAccess templates](#pa_template)

Administrators can also assign applications directly to you. These applications display on your **Applications** page, where you can promote them, test them on development environments, modify them, and manage them throughout their life cycles.

## Selecting a template

IAM Administrators can create OAuth *(tooltip: \<div class="paragraph">
\<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
\</div>)*, OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)*, Security Assertion Markup Language (SAML) *(tooltip: \<div class="paragraph">
\<p>A standard, XML-based, message-exchange framework enabling the secure transmittal of authentication tokens and other user attributes across domains.\</p>
\</div>)*, and PingAccess templates and make them available for you to use to apply security configurations to your application.

### Steps

1. Click **Add Application**.

2. Review the template descriptions to determine which template you should use.

   ![A screen capture of the Select Template page, which lists the templates available for application owners to use. This screen capture shows the templates for Public Application, which is an OpenID Connect template; Internal Application (and Partners), which is an OAuth template; Access Control Policy, which is a template; and Existing Application. A side bar appears to the right of the template list to provide a guide for choosing which template to select.](../../_images/jwq1600185986194.jpg)

   On this page, you can:

   * Select the filtering options to filter OAuth, OpenID Connect, SAML, and PingAccess templates.

   * Click the **Review Configuration** link within the template description to view the details associated with each template.

   If you are unclear about what type of template to select, keep the following in mind:

   * OAuth and OIDC are most commonly used by consumer applications and services so users do not need to sign up for a new username and password. "Sign in with Google," or "Log in with Facebook" are examples of OAuth protocols you are likely familiar with. You might also use OAuth if your application is consumed on a mobile device.

   * SAML is most commonly used by businesses to allow their users to access services they pay for. Salesforce and Gmail are examples of service providers an employee could gain access to after completing a SAML sign on. SAML templates can also be used for web applications created and used within your organization.

   * PingAccess templates can be used to apply access policy to Web and API applications.

   * If an environment is offline or if a PingCentral administrator has set the environment status to **Disabled**, you will be unable to select a disabled or offline environment for template creation.

3. Select the template you want to use, or the existing application you want to add to PingCentral and click **Next**.

4. To proceed, see the appropriate topic:

   * [Using OAuth and OIDC templates](#oauth_template)

   * [Using SAML templates](#saml_template)

   * [Using PingAccess templates](#pa_template)

## Using OAuth and OIDC templates

After selecting an OAuth or OIDC template, use that template to apply user authentication and authorization support to an application.

### Before you begin

Prepare to provide the following:

* Name of the application.

* A brief, accurate description of your application.

* Scopes, which are optional and can be customized to meet your needs. See [Scopes and scope management](https://docs.pingidentity.com/access/sources/dita/topic?resourceid=pf_scopes_and_scope_management) in the PingFederate documentation for additional information.

### Steps

1. If you want to add scopes to the applications, begin typing the name of the scope you want to add and select it from the list when it displays.

   |   |                                                                                                                                                                                                             |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The names of scopes added to applications cannot contain spaces, nor can the **Scopes** field contain spaces before or after the scope name. If spaces exist, applications cannot be successfully promoted. |

   When this application is later promoted, the target PingFederate scope management configuration is referenced to satisfy the scope requirements of the client. Any named scope identified as a common scope in the target environment is configured within the client as a restricted scope.

   If the named scope does not exist in the target environment, the scope is created as an exclusive scope. In that case, or if the scope already exists as an exclusive scope, then the scope is associated with the client as an exclusive scope.

2. Click **Next**.

3. On the **Describe Application** page, enter the name of your application and a description of the application in the **Name** and **Description** fields.

   You are adding this application to PingCentral, so your name will automatically populate the **Owners** field.

4. (Optional) To add owners, or groups of owners, select additional owners from the **Owners** list. If the name you are looking for does not display in the list, contact your PingCentral administrator and request that the person be provisioned.

   ![This example shows the Describe Application page, which contains the Name, Description, and Owners fields.](../_images/tji1617032771105.png)

5. Click **Save and Close**.

The application appears at the top of the list of applications on the **Applications** page.

## Using SAML 2.0 templates

After selecting a SAML template, use that template to apply user authentication and authorization support to an application.

### Before you begin

You must provide:

* The name of the application.

* A brief, accurate description of your application.

* Attribute mapping information, used to map your application attributes to the identity attributes required from the identity provider to verify user identities.

### Steps

1. In PingCentral, on the **Select Metadata** page, complete one of the following tasks:

   * Provide a metadata file from service provider (SP) connections, which might include entity IDs, ACS URLs, and certificates. Click **Choose file** to provide the file.

   * Provide a URL to the metadata file. Click **Or Use URL** to provide the URL.

   * Skip this step and provide the Entity ID, ACS URL, certificate, and attributes, or all of this information, during the promotion process.

   If you choose to provide a metadata file, the information in the file shows on the page.

   ![Screen capture of the Select Metadata page after a metadata file is provided.](../_images/hac1582759323012.png)

2. Click **Next**.

3. On the **Map Attributes** page, to map the application attributes to the identity attributes required to fulfill the authentication policy contract in PingFederate, select identity attributes in the **Identity Attribute** list or click to add static values in the **Static Value** field.

   1. (Optional) If attribute sources are defined in the underlying connection, select the **- Data Store -** identity attribute option and the applicable data store values.

      |   |                                                                                                                                                                          |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | To ensure successful promotion, the target PingFederate must have the necessary Data Stores with identical names as required for authentication policy contract mapping. |

   2. (Optional) To define an OGNL expression and fine-tune attribute values to meet your needs, select the **- Expression -** identity attribute option and enter an **Expression Value** in the appropriate field.

      ![Screen capture of the expressions you can add to your application attributes.](../_images/ldx1635364871454.png)

4. When you're finished, click **Next**.

5. On the **Describe Application** page, enter the name of the application and a description in the appropriate fields.

   You are adding this application to PingCentral, so your name will automatically populate the **Owners** field.

   1. (Optional) To add owners or groups of owners, click the **Owners** field and select additional owners in the list. Click **Next**.

      |   |                                                                                                                                               |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | If the name you are looking for isn't showing in the list, contact your PingCentral administrator and request that the person be provisioned. |

6. Click **Save and Close**.

   The application is added at the top of the list of applications on the **Applications** page.

## Using PingAccess templates

After selecting a PingAccess template, use that template to apply user authentication and authorization support to an application.

### Before you begin

Prepare to define the following as appropriate:

* The application context root and resources

* The application policy

* The resource policy

* The application name and description

You can find details on each of these items in [Information needed to add PingAccess applications](#pa_info).

### Steps

1. On the **Define Resources** page, enter the context root for the application.

   The context root is the common root of all application resources, specifies where in the URL path the application begins, and starts with a slash. In the example URL, `den-ping.com:8443/mygreatapp/home`, the `/mygreatapp` is the context root.

2. Add, delete, or reorder application resources for your application.

   Every application has at least one root resource.

   If resource reordering is available, a **Reorder Resources** link displays on the page, as shown in the following example. If resource ordering was not enabled in the PingAccess application that was used to create this template, it is not enabled in PingCentral.

   ![A screen capture showing the Define Resources page with the Context Root field and the Resources section. Next to the heading for the Resources section is the hyperlink option to Add Resource and the hyperlink option to Reorder Resources, which displays on the Define Resources page if resource reordering is enabled.](../_images/lhp1600200935995.jpg)

   |   |                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------- |
   |   | Virtual resources are available in PingAccess version 6.2 or later, but are not yet supported in PingCentral. |

   To add a new resource:

   1. Click **Add Resource** and in the **Resource Name** field, enter the name of the resource.

   2. In the **Path Patterns** field, enter a list of URL path patterns that identify this resource. Path patterns start with a forward slash (/), begin after the context root, and extend to the end of the URL. There are two different types of path patterns: Basic and Regex. Select the **Regex** option when appropriate.

   3. In the **Resource Authentication** section, select the type of authentication the resource requires.

      If the resource requires the same authentication as the root application, select **Standard**. If authentication is not required to access the resource, select **Anonymous** or **Unprotected**.

   4. If the application is an API or Web + API application, in the **Methods** field, select the HTTP methods supported by the resource. Leave this field empty if the resource supports all methods.

   5. To log information regarding requests to this resource, select the **Audit** check box.

   6. Resources are enabled when they are added by default. To disable a resource, clear the **Enable** check box.

   7. If resource reordering is available, a **Reorder Resources** link displays on the page. To change the order of these resources, click the link, rearrange the resources, and click **Done**.

   To delete the resource, click the associated **Delete** icon.

3. On the **Define Application Policy** page, customize the policy for the application, if needed.

   To apply rules or rule sets, drag them from the **Available Rules** list to the **Policy** list. Click **Next**.

4. (Optional) On the **Define Resource Policy** page, customize the policy for each of your resources.

   To apply rules or rule sets to each resource, drag them from the **Available Rules** list to the **Policy** list. Click **Next**.

5. On the **Describe Application** page, enter the name of the application and a description in the appropriate fields.

   By adding this application to PingCentral, your name automatically populates the **Owners** field.

6. (Optional) To add owners, or groups of owners, click the **Owners** field and select additional owners from the list. Click **Next**.

   If the name you are looking for does not display in the list, contact your PingCentral administrator and request that the person be provisioned.

7. Click **Save and Close**.

   The application displays at the top of the list of applications on the **Applications** page.

## Information needed to add PingAccess applications

When you use templates to PingAccess applications to PingCentral, you provide the application context root and then define its resources, application policy, and resource policies. This section describes these items in detail and explains why you are prompted to provide this information.

There are three different types of PingAccess applications: Web, API, and Web + API. With Web + API applications, administrators can configure both Web and API settings for an application. These applications can switch between web and API processing behaviors on the fly based on whether the inbound request contains a web session cookie (Web) or an OAuth token (API).

* Resources

* Path patterns

* Rules and policies

### Resources

Each application consists of one or more resources, which you define in PingCentral. Resources are components of an application that require different levels of security. When you define resources within an application, you also define security regarding those resources.

![A diagram showing how user requests are routed to the requested resources.](../_images/xzg1600361729933.jpg)

Resources are protected by rules, which let you specify who can access your applications and resources, how and when they can do so, and what modifications can be made to the requested content. When rules, or sets of rules, are applied to applications and resources, they are called policies. Policies are applied to requests, which determine whether users are granted or denied access to the requested resource.

To access an application, users enter a URL. This URL consists of a virtual host, a context root, and the name of the resource they want to access.

![A screen capture identifying the virtual host, context root, and resource within a URL.](../_images/zvs1600361777811.jpg)

When you use a template to add a PingAccess application to PingCentral, you are prompted to provide the context root and define the resources within it. You can find more information in [Application resources](https://docs.pingidentity.com/pingaccess/latest/pingaccess_user_interface_reference_guide/pa_application_resources.html) in the PingAccess documentation.

### Path patterns

When handling requests, PingAccess uses resource path patterns to match resources. There are two different types of path patterns: Basic and Regex.

* **Basic patterns**: The default path pattern type, which defines a path to a specific resource or a pattern that matches multiple paths. Basic patterns can contain any number of "\*" wildcards. For example:

  ```
  /path/x/*
  ```

  matches any of these request paths:

  ```
  /path/x/
  /path/x/index.html
  /path/x/y/z/index.html
  ```

* **Regex patterns**: Regex patterns contain regular expressions and allow for more flexibility in resource matching as they support resource ordering. For example:

  ```
  /[^/]+/[a-z]+\.html
  ```

  matches any of these request paths:

  ```
  /images/gallery.html
  /search/index.html
  ```

  However, it would not match any of these request paths:

  ```
  /images/gallery2.html
  /search/pages/index.html
  /index.html
  ```

  |   |                                                                                                                                                                                                                                                                         |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Although Regex path patterns function in an agent deployment, system performance might decrease if they are used. Agents are unable to interpret Regex path patterns, so they must consult PingAccess for policy decisions for each resource with a Regex path pattern. |

When one or more path patterns match a request, PingAccess uses the first matching pattern it identifies, so the order in which path patterns are evaluated is important. By default, PingAccess orders path patterns automatically so that the most specific patterns are matched first. However, if more explicit control is needed, or if you are using regular expressions, enable resource ordering to manually specify the order in which path patterns are evaluated.

For example, an application might have three resources, such as:

* `/images/logo.png` (Basic)

* `/images/*` (Basic)

* `/.+/[a-z]\.png` (Regex)

A request to resource `/images/logo.png` is matched by all 3 path patterns, yet each resource can have different policy requirements. Resource ordering allows you to specify which of these path patterns is parsed first, further allowing you to control the policy that is applied to a particular request.

When you define the application resources in PingCentral, you are prompted to provide path pattern information. For more information, see [Path patterns reference](https://docs.pingidentity.com/bundle/pingaccess-61/page/ean1572449478234.html) in the *PingAccess User Interface Reference Guide*.

### Rules and policies

Rules let you specify who can access your applications and resources, how and when they can do so, and what modifications can be made to the requested content. There are two different types of rules: access control rules and processing rules. Access control rules determine whether users can access a resource, and processing rules determine how requests are processed.

When you put rules together, they are called policies.

* **Application policies**: Rules applied to the application as a whole. You can define Web rules and API rules for Web + API applications.

* **Resource policies**: Rules applied to specific resources. Every application has at least one resource.

Rules can limit access based on information such as user attributes, client network range, time of day. You can combine rules to create rule sets, which are reusable and can be applied to many different resources and applications. Rule sets grant requests if any or all of the constituent rules are successful:

* **Any**: An any rule set is evaluated from top to bottom and stops at the first rule that has its criteria met. If all rules fail, the request is denied.

* **All**: An all rule set is evaluated from top to bottom and stops when it gets to the first rule that does not have its criteria met. If one rule fails, the request is denied.

Since rules within a rule set are evaluated from top to bottom, the order in which rules display in rule sets is important. In PingCentral, you can customize policies by dragging rules from the **Available Rules** list to the **Policy** list and changing the order to meet your needs.

![A screen capture showing how the Available Rules list and the Policy list display side-by-side in PingCentral.](../_images/hji1600876577837.jpg)

Learn more in [Rules](https://docs.pingidentity.com/pingaccess/latest/pingaccess_user_interface_reference_guide/pa_rules.html) in the PingAccess documentation.

---

---
title: Introduction to PingCentral
description: An introduction to PingCentral and a high-level explanation of how it works.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_application_owners:pingcentral_intro/pingcentral_ao_intro
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_application_owners/pingcentral_intro/pingcentral_ao_intro.html
revdate: October 9, 2025
---

# Introduction to PingCentral

Use PingCentral to add user authentication and authorization support to your applications, promote them to the appropriate development environments for testing, and monitor them throughout their life cycles.

PingCentral:

* Makes it possible for you to apply security configurations to your applications without assistance from an administrator.

* Allows you to promote these applications yourself, when you are ready, rather than submitting a request and waiting for someone else to promote them for you.

* Provides a central monitoring location for greater visibility into applications across deployment life cycles.

* Minimizes the risk of promoting applications with vulnerable security policies within your organization.

Using PingCentral does not require extensive training. However, for the best possible experience, become familiar with how the platform works before getting started.

1. IAM Administrators create OAuth, OpenID Connect (OIDC), SAML, and PingAccess templates based on clients, connections, and application security configurations they think are worth replicating.

2. Administrators can also add clients, connections, and applications directly to PingCentral and assign owners to them.

3. You use SAML, OAuth, OIDC, and PingAccess templates to apply security configurations to your applications. A wizard guides you through the process of providing a name and description for each application you add to PingCentral. Another wizard guides you through the process of promoting your application to the target environment.

4. When you're ready, promote applications to the appropriate development environments to test them and promote them directly to production environments if your permissions allow.

   ![This flowchart illustrates the tasks application owners perform to add applications to and promote them to PingFederate or PingAccess development, staging, or production environments.](../../_images/nuq1601349842175.jpg)

---

---
title: Managing applications
description: Instructions for managing applications within PingCentral.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_application_owners:pingcentral_managing_apps/pingcentral_managing_apps
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_application_owners/pingcentral_managing_apps/pingcentral_managing_apps.html
revdate: October 9, 2025
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Managing applications

If you are an owner of an application, the application displays on the **Applications** page. From this page, you can add new applications, view and update existing applications, and delete them from PingCentral when they are no longer needed.

## Steps

1. Use the menu at the top of the page to sort the list of applications by modified date or by application name, or use the search feature to locate an application by name.

   OAuth, OIDC, SAML, and PingAccess applications are listed in the order in which they were last modified, by default, with the most recently modified at the top of the list.

   ![This image displays an example of the Applications page for an application owner.](../_images/tgt1592861474520.jpg)

2. On the **Applications** page, you can:

   * View information about an application. Click the expandable icon associated with it.

     Learn more in [Viewing application information](../pingcentral_viewing_apps/pingcentral_viewing_apps.html).

   * Add a new SAML, OAuth, or OIDC application to PingCentral. Click **Add Application**, select a template, and follow the wizard prompts.

     Learn more in [Adding applications](../pingentral_adding_apps/pingcentral_adding_apps.html).

     |   |                                                                                                                                              |
     | - | -------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | Administrators can also assign you as the owner of an application, in which case the application will display on your **Applications** page. |

   * Promote applications to development or production environments. Click the expandable icon associated with the application you want to promote and click the **Promote** tab. Learn more in [Promoting applications](../pingcentral_promoting_apps/pingcentral_promoting_apps.html).

   * Delete an application from PingCentral. Click its associated **Delete** icon.

     ### Choose from:

     * To delete an application from PingCentral only, click the **Delete** button.

     * To delete an application from all environments, depending on the application type, select the **Delete from PingFederate in all environments** or **Delete from PingAccess in all environments** checkbox and click the **Delete** button.

       |   |                                                                                                                                          |
       | - | ---------------------------------------------------------------------------------------------------------------------------------------- |
       |   | If a PingCentral administrator restricts access to application deletion, you cannot delete applications from PingFederate or PingAccess. |

---

---
title: Managing approvals (application owners)
description: Instructions for monitoring approval requests and promoting approved applications.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_application_owners:pingcentral_manage_approvals/pingcentral_app_owner_manage_approvals
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_application_owners/pingcentral_manage_approvals/pingcentral_app_owner_manage_approvals.html
revdate: October 11, 2025
section_ids:
  steps: Steps
---

# Managing approvals (application owners)

If you submit a request for application promotion to your administrator, you can track the application's approval status by accessing the **Promotion Approvals** page, located under the **Management** tab.

From this page, you can:

* Filter for approved, promoted, pending, rejected, or canceled approvals, or by environments or integration type. Use the **Visible** filter, which is enabled by default, to hide approvals that are in a canceled, promoted, or rejected status.

* **Promote** an approved application, or **Cancel** an approval request.

  |   |                                                                                                      |
  | - | ---------------------------------------------------------------------------------------------------- |
  |   | You see a bell icon in the top navigation bar when an administrator approves your promotion request. |

  ![Screen capture of console for application owners that displays the Approvals page with active approval requests. Status is filtering for Approved, Pending, and Rejected approval requests.](../_images/mkq1687889008190.jpg)

## Steps

1. Select your filters.

   You can filter by:

   * **Status**: **Approved**, **Pending**, or **Rejected**. The page automatically filters for any approved, pending, or rejected approval requests.

   * Environments.

   * Integration types (OAuth and OIDC or SAML).

   Click the filters to add or remove them.

2. To promote approved applications to an environment, click **Promote** in the row for the application that you want to promote.

   Learn more in [Promoting applications](../pingcentral_promoting_apps/pingcentral_promoting_apps.html).

   |   |                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------- |
   |   | There can only be one outstanding promotion approval request per application to an environment. |

   |   |                                                                                                                                                                                                                                                                                                                                            |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If an environment is offline or if a PingCentral administrator has set the environment status to **Disabled**, the environment is undergoing maintenance. During this time, the **Promote** button is inaccessible. You will be unable to promote the application while the environment is offline or disabled and undergoing maintenance. |

3. To cancel an approval request, click **Cancel** in the row for the application that you no longer want to request promotion approval.

---

---
title: Promoting applications
description: Instructions for promoting OAuth, OIDC, SAML, and PingAccess applications.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_application_owners:pingcentral_promoting_apps/pingcentral_promoting_apps
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_application_owners/pingcentral_promoting_apps/pingcentral_promoting_apps.html
revdate: May 14, 2026
page_aliases: ["pingcentral_info_pa_apps.adoc", "pingcentral_promoting_oauth_apps.adoc", "pingcentral_promoting_pa_apps.adoc", "pingcentral_promoting_saml_apps.adoc pingcentral_agent_deploy.adoc", "pingcentral_gateway_deploy.adoc", "pingcentral_metadata_saml_apps.adoc"]
section_ids:
  oauth: Promoting OAuth and OIDC applications
  before-you-begin: Before you begin
  steps: Steps
  saml: Promoting SAML applications
  before-you-begin-2: Before you begin
  steps-2: Steps
  metadata: Using metadata to promote SAML applications
  steps-3: Steps
  pingaccess: Promoting PingAccess applications
  before-you-begin-3: Before you begin
  steps-4: Steps
  pa_information: Information needed to promote PingAccess applications
  gateway: Gateway deployment
  agent: Agent deployment
---

# Promoting applications

You can promote all applications assigned to you to development environments for testing, and to production environments if your permissions allow.

Learn more in the following:

* [Promoting OAuth and OIDC applications](#oauth)

* [Promoting SAML applications](#saml)

* [Promoting PingAccess applications](#pingaccess)

|   |                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If an environment is offline, or if a PingCentral administrator has set the environment status to **Disabled**, you cannot promote the application. |

## Promoting OAuth and OIDC applications

You can promote the OAuth and OIDC applications assigned to you.

### Before you begin

Prepare to provide the following:

* Redirect URIs, if required. These are the URIs your users will be directed to after they receive authorization to access your application. Redirect URIs are only required when promoting applications that use an authorization code and implicit grant types.

  Redirect URIs are not limited to the number of characters they can contain, but cannot include wildcards or some special characters.

* If a client secret is required to authenticate your application, you can create a custom secret, generate a secret, or leave the field empty and PingCentral will generate a client secret for you.

### Steps

1. To promote the application to an environment, click the expandable icon associated with the application, select the **Promote** tab, and click **Promote**.

   |   |                                                                                                                                                                                                    |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If an environment is offline or if a PingCentral administrator has set the environment status to **Disabled**, you will be unable to promote the application to a disabled or offline environment. |

2. From the **Available Environments** list, select the environment to which you want to promote the application.

   |   |                                                                                                                                                  |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If you have the Application Owner role, you cannot promote applications to protected environments, which have shield icons associated with them. |

3. If curly brackets ({}) display in the upper right corner of the window, you can edit the underlying application JSON yourself. Or, you can complete the fields in this window.

   If you choose to complete the fields in this window, refer to the following:

   1. If redirect URIs are required to promote the application, enter them in the **Redirect URIs** field.

   2. If a client secret is required to authenticate your application, you can either:

      * Generate a new secret by selecting the option at the bottom of the modal.

      * Continue using the existing secret. Bypass the **Generate New Secret** button and promote the application.

   3. If extended properties are visible and editable, you can add or remove the values used for this application.

   To edit the JSON yourself:

   1. Click the curly brackets.

      The application JSON displays in the window.

   2. Update the JSON to meet your needs. Built-in JSON syntax validation occurs as you make updates to help prevent mistakes.

   3. When you're finished, promote the application.

      PingCentral promotes your application to the designated environment in PingFederate. You will see the new promotion in the **History** section of the page.

4. To configure the SSO connection, provide the following information to your service provider:

   * The client ID. Click **View Client Details** to access the **Promotion Details** window, which displays the client ID.

   * The OIDC discovery endpoint and client secret are also available in this window.

     ![This example displays the Client ID, the OIDC discovery endpoint, and the client secret on the Promotion Details modal.](../_images/ezi1718751416428.jpg)

## Promoting SAML applications

You can promote the SAML applications assigned to you.

### Before you begin

Prepare to provide the following:

* **Entity ID**: used to uniquely identify the application and obtained from the service provider ACS URL, the application's URL to which SAML assertions from the identity provider will be sent after user authentication occurs.

* **ACS URL**(s): the application's URL to which SAML assertions from the identity provider will be sent after user authentication occurs.

* **SLO Service URL**(s): the application's URL utilized for single logout (SLO) functionality.

* **SP certificates**: if the template you select is based on a PingFederate connection that requires a certificate.

* **An assertion encryption certificate**: required if encryption is enabled for the connection.

When SAML applications are promoted, the connection metadata is exported and stored as part of that application. This metadata is available to download as a `.xml` file, which you can use to promote similar SAML applications. Learn more about this process in [Using metadata to promote SAML applications](#metadata).

### Steps

1. To promote the application to an environment, click the **Expand** icon associated with the application, select the **Promote** tab, and click **Promote**.

   |   |                                                                                                                                                                                                    |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If an environment is offline or if a PingCentral administrator has set the environment status to **Disabled**, you will be unable to promote the application to a disabled or offline environment. |

2. In the **Available Environments** list, select the environment to which you want to promote the application.

   |   |                                                                                                                                                  |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If you have the Application Owner role, you cannot promote applications to protected environments, which have shield icons associated with them. |

3. If curly brackets ({}) display in the upper right corner of the window, you can edit the underlying application JSON yourself. Or, you can complete the fields in this window.

   If you choose to complete the fields in this window, refer to the following:

   1. In the **Entity ID**, **ACS URL**, and **SLO Service URL** fields, enter the appropriate information.

      If you provided a metadata file when you added your application to PingCentral, the **Promote to Environment** window is prepopulated with the information from the other SAML application. You can modify this information as necessary.

   2. If extended properties are visible and editable, you can add or remove the values used for this application.

   3. In the **Signing Certificate** list, select the appropriate certificate:

      * If the PingFederate environment contains signing certificates, those certificates display in the list.

        The signing certificate that was added to the environment when it was created or last updated displays as the **Environment Default** certificate.

      * If signing certificates are not available in the PingFederate environment and an environment default certificate isn't available, or if an environment default certificate is available but expired, the **Automatically generate certificate** option displays in the list.

        |   |                                                                                                                                                                                                                                                                                                                                                                                   |
        | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        |   | If you used signing certificates that were automatically generated to promote applications in PingCentral 1.7 or earlier, and you want to promote those applications to the same environments, you need to locate the signing certificates. Search for a signing certificate with a subject DN that matches the name of the application and select it as the signing certificate. |

   4. Upload SP certificates, if required. SP certificates are required for PingFederate SP connections when:

      * Either of the single logout (SLO) options, **IdP-Initiated-SLO** or **SP-Initiated-SLO**, are selected as the SAML profile.

      * Digital signatures are required, and the Signature Policy is set to the **Require authn requests to be signed when received via the POST or redirect bindings** option.

      * Inbound backchannel authentication is configured. You can find more information in the following topics in the PingFederate documentation:

        * [Configuring digital signatures for service provider connections](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configuring_digital_signatures_service_provider_connections.html).

        * [Configuring signature verification settings (SAML 2.0)](https://docs.pingidentity.com/pingfederate/12.3/administrators_reference_guide/pf_configuring_signature_verification_settings_saml_20.html)

   5. If encryption is enabled for the connection, click in the **Assertion Encryption Certificate** field. Select an assertion encryption certificate used for a previous promotion in the list or provide a new one.

      |   |                                                                                                                                    |
      | - | ---------------------------------------------------------------------------------------------------------------------------------- |
      |   | Only whole encryption is currently supported, so if a connection has attributes specified for encryption, the promotion will fail. |

   To edit the JSON yourself:

   1. Click the curly brackets.

      The application JSON displays in the window.

   2. Update the JSON to meet your needs. Built-in JSON syntax validation occurs as you make updates to help prevent mistakes.

4. Verify that the information displayed in the **Promote to Environment** window is correct and click **Promote**.

   PingCentral promotes your application to the designated environment in PingFederate. The new promotion shows in the**History** section of the page. If the signature verification certificate used during promotion is available in the PingFederate environment, that certificate is used. If not, a new certificate is created.

5. To configure a single sign-on (SSO) connection, provide the application Entity ID and the SSO endpoint URL to your service provider.

   To locate the SSO endpoint URL, click the **View Connections Detail** link associated with the promotion. The URL displays on the **Promotion Details** window.

   ![This example shows the Promotion Details page, which contains information regarding the promotion, such as the ACS URL, SSO endpoint URL, and certificates associated with the connection.](../_images/kio1624578838404.png)

### Using metadata to promote SAML applications

When SAML applications are promoted, the connection metadata is exported and stored as part of that application. This metadata is available to download as a `.xml` file, which you can use to promote similar SAML applications.

#### Steps

1. On the **Applications** page, locate an application that has a configuration you want to replicate in a new SAML application and click the expandable icon associated with that application.

2. Go to the **Promote** tab and click the **View Connection Details** link.

   The promotion information displays.

   ![A screen capture of the promotion information displayed in the Promotion Details window.](../_images/epd1686691021018.png)

3. Click **Download Identity Provider Metadata** to download the metadata as a `.xml` file and click **Close**.

4. Use the metadata on the service provider (SP) side to update the connection to the identity provider (IdP), as appropriate.

## Promoting PingAccess applications

Promote the PingAccess applications assigned to you.

### Before you begin

The information required to promote PingAccess Web applications, API applications, and Web + API applications varies by type. Prepare to provide the following information:

| Web applications            | API applications                                                        | Web + API applications              |
| --------------------------- | ----------------------------------------------------------------------- | ----------------------------------- |
| Virtual host (required)     | Virtual host (required)                                                 | Virtual host (required)             |
|                             | Access validation method (required if an identity mapping is specified) | Access validation method (required) |
| Web session (optional)      | Web session (optional)                                                  | Web session (required)              |
| Identity mapping (optional) | Identity mapping (optional)                                             | Identity mapping (optional)         |
| Site or agent (required)    | Site or agent (required)                                                | Site or agent (required)            |

Learn more about each of these items in [Information needed to promote PingAccess applications](#pa_information).

|   |                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Customized authentication challenge responses, which support single-page applications, are available in PingAccess version 6.2 or later. Applications with this type of policy can be added to PingCentral, but cannot be promoted to another environment unless the authentication challenge policy also exists in the target environment. |

### Steps

1. To promote the application to an environment, click the Expand icon associated with the application, select the **Promote** tab, and click **Promote**.

   |   |                                                                                                                                                                                                    |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If an environment is offline or if a PingCentral administrator has set the environment status to **Disabled**, you will be unable to promote the application to a disabled or offline environment. |

2. From the **Available Environments** list, select the environment to which you want to promote the application.

   |   |                                                                                                                                                  |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If you have the Application Owner role, you cannot promote applications to protected environments, which have shield icons associated with them. |

3. On the **Configure Promotion** page, click the **Virtual Hosts** field, and select the virtual hosts you want to add.

   To remove a virtual host, click the **X** icon next to the virtual host name.

4. Complete the remaining fields, which vary, depending on the type of application you are promoting.

   The following example shows the fields available to provide information for a Web + API application.

   ![A screen capture showing the options available on the Configure Promotion page for a Web + API application.](../_images/wih1600890414430.jpg)

5. Click **Next**.

6. On the **Review Promotion** page, review promotion information you added.

   Additional detail is available in the **Summary** and **Application** sections of the page.

7. Click **Promote and Close**.

8. To review details regarding the promotion, click the **View History Details** link associated with the promotion.

### Information needed to promote PingAccess applications

When you promote PingAccess applications to PingAccess environments, you provide virtual host, access validation, web session, and identity mapping information, as appropriate.

PingAccess can be deployed in one of two ways:

* [Gateway deployment](#gateway): In a gateway deployment, the destination is a site. Requests are routed to a PingAccess web server, which then forwards authorized requests to the target application or API on the site.

* [Agent deployment](#agent): In an agent deployment, the destination is an agent. Requests are intercepted at the web server hosting the target application or API by the PingAccess agent plugin. The agent communicates with the PingAccess policy server to validate access before allowing the request to proceed to the target application or API.

The key difference between these deployments is where the initial request is directed. In a gateway deployment, the initial request is routed to a PingAccess web server, so the destination is a site. In an agent deployment, the initial request is routed to the web server that hosts the target application or API, so the destination is an agent. When you promote PingAccess applications, you are prompted to provide the name of the site or agent.

#### Gateway deployment

This diagram shows how users are authenticated, and how access policies and identity mappings are applied to requests to access applications or APIs with a gateway deployment.

![This diagram shows how users are authenticated, and how access policies and identity mappings are applied to requests to access applications or APIs with a gateway deployment.](../_images/rki1599598432959.jpg)

1. Users enter a URL that consists of a unique virtual host and context root.

   * **Virtual host**: The public-facing host name and host port. For example, `den.ping.com:8443`.

     A wildcard (`*`) can be used either to define either any host (`*:8443`, for example) or any host within a domain (`*.ping.com`, for example). If a request matches more than one virtual host, the most specific match is used.

   * **Context root**: The common root of all resources, specifies where in the URL path the application begins, and starts with a slash. In the example URL, `den-ping.com:8443/mygreatapp/home`, `/mygreatapp/` is the context root.

   PingCentral prompts you for the context root when you add the application, and for the virtual hosts when you promote it.

2. The PingAccess web server determines whether a PingAccess session cookie (Web) or an OAuth token (API) exists for the user. If it does not, a web session starts. Web sessions define the policy for web application session creation, lifetime, timeouts, and their scope.

   |   |                                                                                                                                                                       |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you promote Web + API applications in PingCentral, you must select a Web session from a list. This information is not required to promote Web or API applications. |

3. You can configure API and Web + API applications to use access token validators to locally verify signed and encrypted access tokens. If you are promoting an API or Web + API application in PingCentral, you can specify the access validation method, whether it be a token provider or a token validator, if appropriate.

4. Users are authenticated through the web session.

5. Policies are applied to the request. Policies are rules, or sets of rules, that are applied to application resources. makes policy-based decisions to grant or deny access to the requested resource.

   You can customize application and resource policies when you use templates to add applications to PingCentral.

6. Identity mapping is applied to the request if the target application expects user information to be included to further authenticate the user.

   PingCentral prompts you for the name of the Web and/or API Identity mapping, as appropriate, when you promote it.

7. The user accesses the target web application or API.

#### Agent deployment

The following diagram shows how users are authenticated, and how access policies and identity mappings are applied to requests to access applications or APIs with an agent deployment.

![This diagram shows hows users are authenticated, and how access policies and identity mappings are applied to requests to access applications or APIs with an agent deployment.](../_images/ywn1599605492379.jpg)

1. Users enter a URL to request access to a resource and their requests.

2. The PingAccess agent plugin intercepts the request. Agents use names and shared secrets to authenticate with the policy server. These names and secrets do not need to be unique. Any number of agents can have the same name and secret, and they are all treated equally by the policy server.

3. If the agent does not have previously cached policies for the resource, it contacts the PingAccess policy server for instructions.

4. The PingAccess policy server receives claims from the token provider, which provides instructions for handling the request.

5. Policies are applied to the request and PingAccess makes policy-based decisions to grant or deny access to the requested resource.

6. Identity mapping is applied to the request if the target application expects user information to be included to further authenticate the user.

7. The user accesses the target web application or API.

---

---
title: Reverting applications to previously promoted versions
description: Instructions for reverting applications to previously promoted versions.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_application_owners:pingdirectory_revert_apps/pingcentral_revert_ao_apps
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_application_owners/pingdirectory_revert_apps/pingcentral_revert_ao_apps.html
revdate: October 10, 2025
section_ids:
  steps: Steps
---

# Reverting applications to previously promoted versions

When you revert applications to previously promoted versions, the reverted versions of the application will not exist outside of PingCentral until you promote them again, at which point they will also be available in PingFederate or PingAccess.

## Steps

1. On the **Applications** page, locate the application you want to revert to a previously promoted version.

   |   |                                                                             |
   | - | --------------------------------------------------------------------------- |
   |   | You cannot revert applications created in previous versions of PingCentral. |

2. Click the expandable icon associated with the application, select the **Promote** tab, and then click **View Details**.

3. In the **Promotion Details** window, click **Revert Application**.

   A message displays asking you if you are sure you want to revert this application.

4. Click **Revert**.

   The reverted version of the application displays in your applications list.

   |   |                                                                                                                                                                                                                                                                                                                                                                                 |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Reverting OAuth and OIDC applications to previously promoted versions overrides client secrets, so you will need to create or generate new secrets before you promote them again. Reverting SAML applications to previously promoted versions overrides the Entity IDs, ACS URLs, and certificates, so you might need to update this information before you promote them again. |

---

---
title: Updating applications
description: Instructions for updating PingCentral applications.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_application_owners:pingcentral_updating_apps/pingcentral_ao_updating_apps
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_application_owners/pingcentral_updating_apps/pingcentral_ao_updating_apps.html
revdate: October 9, 2025
section_ids:
  steps: Steps
---

# Updating applications

To keep your applications secure, rotate certificates and client secrets on a regular basis and apply updated security configurations to applications built from templates if new configuration templates become available. You don't need to recreate your applications in PingCentral to apply new templates. Replace the templates associated with your applications and promote them again.

## Steps

1. Click the **Expand** icon associated with the application you want to update and click the **Pencil** icon.

   All the editable information is shown on one page.

2. To update the name, description, and owners, change the information in the **Name**, **Description**, and **Owners** fields. Click **Save**.

3. To change the template used to create the application, click **Change Template** and select a new template from the **Select Template** page. Click **Save and Close**.

   |   |                                                                                                                                              |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You cannot apply a SAML template to an OAuth or OpenID Connect (OIDC) application nor apply an OAuth or OIDC template to a SAML application. |

4. **Optional:** To update OAuth or OIDC application information:

   * In the **Client** section, change the scopes associated with OAuth or OIDC applications. Select or clear the appropriate checkboxes and click **Save**.

     |   |                                                                                                                                                                                                                                   |
     | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | You cannot edit scopes for applications created in PingCentral 1.2.0. However, you can update the template associated with an application to a template created in a later version, which allows you to update scope information. |

   * In the **Promote** section, change the information in the **Redirect URI** fields for the appropriate environments and click **Save**.

   * To change client secrets, return to the **Applications** page, promote the application again, and generate a new secret.

5. **Optional:** To update SAML application information:

   * In the **Attribute Mappings** section, add or remove attributes and expressions, or update attribute and expression values, and click **Save**.

   * In the **Promotions** section, upload a new `.xml` file that contains service provider metadata, such as the Entity ID, ACS URL, certificates, and attribute information, from another SAML application. Click **Choose File** or **Or Use URL** to provide the metadata file.

     |   |                                                                                                                                    |
     | - | ---------------------------------------------------------------------------------------------------------------------------------- |
     |   | If metadata is used, the attribute mapping section might also need to be updated to include new attributes from the metadata file. |

   * Change the information in the **Entity ID** or **ACS URL** fields and click **Save**.

   * To change the signing certificate, select the appropriate certificate in the **Signing Certificate** list and click **Save**.

   * To change the service provider (SP) certificate, click **SP Certificate** to upload a new certificate, or click **Remove** to remove it. Click **Save**.

6. **Optional:** To update PingAccess application information:

   * On the **Properties** tab, in the **Promote** section, update the **Virtual Hosts**, **Access Validation**, **Identity Mapping**, and **Site** or **Agent** names, as appropriate. Click **Save**.

   * On the **Resources** tab, update information regarding each resource and click **Save**.

   * On the **Policy** tab, click the **Pencil** icon associated with the policy you want to update. Make changes and click **Save**.

---

---
title: Viewing application information
description: Instructions for viewing application information.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_application_owners:pingcentral_viewing_apps/pingcentral_viewing_apps
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_application_owners/pingcentral_viewing_apps/pingcentral_viewing_apps.html
revdate: October 9, 2025
section_ids:
  steps: Steps
---

# Viewing application information

If you are an owner of an application, the application displays on the **Applications** page.

## Steps

1. Use the menu at the top of the page to sort the list of applications by modified date or by application name, or use the search feature to locate an application by name.

   Security Assertion Markup Language (SAML) *(tooltip: \<div class="paragraph">
   \<p>A standard, XML-based, message-exchange framework enabling the secure transmittal of authentication tokens and other user attributes across domains.\</p>
   \</div>)*, OAuth *(tooltip: \<div class="paragraph">
   \<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
   \</div>)*, OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
   \<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
   \</div>)*, and PingAccess applications are listed in the order in which they were last modified, by default, with the most recently modified at the top of the list.

2. To view details regarding an application, click the expandable icon associated with it.

   Applications promoted to development environments (such as development, staging, or production) display icons associated with each environment. If an application has not yet been promoted to a specific environment, you will not see an icon representing that environment.

   ![A screen capture of what the Applications page might look like for an application owner.](../_images/plp1582749215404.png)

3. To review additional information about the application, click each tab.

   * **Summary tab**: This tab displays the application or connection name, description, owners, the date on which the application was last modified, and additional information specific to the application, client, or connection.

   * **Template tab**: This tab displays if the application was created from a template. It includes the name of the template applied to the application, and details regarding the application, client or connection on which the template was based.

   * **Client tab**: This tab displays if the application was created from an OAuth or OIDC application that was directly added to PingCentral from PingFederate. It includes the client name, ID, grant types, attributes, and applicable policies.

   * **Connection tab**: This tab displays if the application was created from a SAML application that was directly added to PingCentral from PingFederate. It includes the name of the connection, browser profiles, and binding information.

   * **Application tab**: This tab displays if the application was directly added to PingCentral from PingAccess. It includes the application name, description, and details regarding the application.

   * **Promote tab**: This tab displays the promotion history of this application, which includes the date and time each promotion occurred.

     |   |                                                                                                                                                                                                                                                      |
     | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If an environment is offline or if a PingCentral administrator has set the environment status to **Disabled**, you may still view the application details, however, you will be unable to edit the application in a disabled or offline environment. |

4. To access additional information regarding the application and its promotion history, click **View Client Details**.

---

---
title: Accessing PingCentral
description: Instructions for accessing PingCentral.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_application_owners:pingcentral_accessing/pingcentral_accessing_pc
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_application_owners/pingcentral_accessing/pingcentral_accessing_pc.html
revdate: October 14, 2025
section_ids:
  steps: Steps
---

# Accessing PingCentral

PingCentral is a web-based application that you access from a URL. For the best possible experience, use Chrome or Firefox as your browser.

## Steps

1. Contact your IAM Administrator for the PingCentral URL and your sign-on credentials.

2. Enter your credentials.

   |   |                                                                                                              |
   | - | ------------------------------------------------------------------------------------------------------------ |
   |   | If you have multiple failed login attempts, you wil be locked out of PingCentral for a short period of time. |

---

---
title: Adding applications
description: Instructions for adding applications to PingCentral.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_application_owners:pingentral_adding_apps/pingcentral_adding_apps
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_application_owners/pingentral_adding_apps/pingcentral_adding_apps.html
revdate: October 13, 2025
page_aliases: ["pingcentral_info_pa_templates.adoc", "pingcentral_pa_templates.adoc", "pingcentral_path_patterns.adoc", "pingcentral_resources.adoc", "pingcentral_rules_policies.adoc", "pingcentral_selecting_template.adoc", "pingcentral_using_oauth_templates.adoc", "pingcentral_using_saml_templates.adoc"]
section_ids:
  select_template: Selecting a template
  steps: Steps
  oauth_template: Using OAuth and OIDC templates
  before-you-begin: Before you begin
  steps-2: Steps
  saml_template: Using SAML 2.0 templates
  before-you-begin-2: Before you begin
  steps-3: Steps
  pa_template: Using PingAccess templates
  before-you-begin-3: Before you begin
  steps-4: Steps
  pa_info: Information needed to add PingAccess applications
  resources: Resources
  path-patterns: Path patterns
  rules-and-policies: Rules and policies
---

# Adding applications

Before you can promote applications to development environments for testing, you must add them to PingCentral.

To add applications to PingCentral, you can use OAuth, OIDC, SAML, and PingCentral templates to apply security configurations to your applications. Wizards guide you through these processes.

Learn more:

* [Selecting a template](#select_template)

* [Using OAuth and OIDC templates](#oauth_template)

* [Using SAML templates](#saml_template)

* [Using PingAccess templates](#pa_template)

Administrators can also assign applications directly to you. These applications display on your **Applications** page, where you can promote them, test them on development environments, modify them, and manage them throughout their life cycles.

## Selecting a template

IAM Administrators can create OAuth *(tooltip: \<div class="paragraph">
\<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
\</div>)*, OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)*, Security Assertion Markup Language (SAML) *(tooltip: \<div class="paragraph">
\<p>A standard, XML-based, message-exchange framework enabling the secure transmittal of authentication tokens and other user attributes across domains.\</p>
\</div>)*, and PingAccess templates and make them available for you to use to apply security configurations to your application.

### Steps

1. Click **Add Application**.

2. Review the template descriptions to determine which template you should use.

   ![A screen capture of the Select Template page, which lists the templates available for application owners to use. This screen capture shows the templates for Public Application, which is an OpenID Connect template; Internal Application (and Partners), which is an OAuth template; Access Control Policy, which is a template; and Existing Application. A side bar appears to the right of the template list to provide a guide for choosing which template to select.](../../_images/jwq1600185986194.jpg)

   On this page, you can:

   * Select the filtering options to filter OAuth, OpenID Connect, SAML, and PingAccess templates.

   * Click the **Review Configuration** link within the template description to view the details associated with each template.

   If you are unclear about what type of template to select, keep the following in mind:

   * OAuth and OIDC are most commonly used by consumer applications and services so users do not need to sign up for a new username and password. "Sign in with Google," or "Log in with Facebook" are examples of OAuth protocols you are likely familiar with. You might also use OAuth if your application is consumed on a mobile device.

   * SAML is most commonly used by businesses to allow their users to access services they pay for. Salesforce and Gmail are examples of service providers an employee could gain access to after completing a SAML sign on. SAML templates can also be used for web applications created and used within your organization.

   * PingAccess templates can be used to apply access policy to Web and API applications.

   * If an environment is offline or if a PingCentral administrator has set the environment status to **Disabled**, you will be unable to select a disabled or offline environment for template creation.

3. Select the template you want to use, or the existing application you want to add to PingCentral and click **Next**.

4. To proceed, see the appropriate topic:

   * [Using OAuth and OIDC templates](#oauth_template)

   * [Using SAML templates](#saml_template)

   * [Using PingAccess templates](#pa_template)

## Using OAuth and OIDC templates

After selecting an OAuth or OIDC template, use that template to apply user authentication and authorization support to an application.

### Before you begin

Prepare to provide the following:

* Name of the application.

* A brief, accurate description of your application.

* Scopes, which are optional and can be customized to meet your needs. See [Scopes and scope management](https://docs.pingidentity.com/access/sources/dita/topic?resourceid=pf_scopes_and_scope_management) in the PingFederate documentation for additional information.

### Steps

1. If you want to add scopes to the applications, begin typing the name of the scope you want to add and select it from the list when it displays.

   |   |                                                                                                                                                                                                             |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The names of scopes added to applications cannot contain spaces, nor can the **Scopes** field contain spaces before or after the scope name. If spaces exist, applications cannot be successfully promoted. |

   When this application is later promoted, the target PingFederate scope management configuration is referenced to satisfy the scope requirements of the client. Any named scope identified as a common scope in the target environment is configured within the client as a restricted scope.

   If the named scope does not exist in the target environment, the scope is created as an exclusive scope. In that case, or if the scope already exists as an exclusive scope, then the scope is associated with the client as an exclusive scope.

2. Click **Next**.

3. On the **Describe Application** page, enter the name of your application and a description of the application in the **Name** and **Description** fields.

   You are adding this application to PingCentral, so your name will automatically populate the **Owners** field.

4. (Optional) To add owners, or groups of owners, select additional owners from the **Owners** list. If the name you are looking for does not display in the list, contact your PingCentral administrator and request that the person be provisioned.

   ![This example shows the Describe Application page, which contains the Name, Description, and Owners fields.](../_images/tji1617032771105.png)

5. Click **Save and Close**.

The application appears at the top of the list of applications on the **Applications** page.

## Using SAML 2.0 templates

After selecting a SAML template, use that template to apply user authentication and authorization support to an application.

### Before you begin

You must provide:

* The name of the application.

* A brief, accurate description of your application.

* Attribute mapping information, used to map your application attributes to the identity attributes required from the identity provider to verify user identities.

### Steps

1. In PingCentral, on the **Select Metadata** page, complete one of the following tasks:

   * Provide a metadata file from service provider (SP) connections, which might include entity IDs, ACS URLs, and certificates. Click **Choose file** to provide the file.

   * Provide a URL to the metadata file. Click **Or Use URL** to provide the URL.

   * Skip this step and provide the Entity ID, ACS URL, certificate, and attributes, or all of this information, during the promotion process.

   If you choose to provide a metadata file, the information in the file shows on the page.

   ![Screen capture of the Select Metadata page after a metadata file is provided.](../_images/hac1582759323012.png)

2. Click **Next**.

3. On the **Map Attributes** page, to map the application attributes to the identity attributes required to fulfill the authentication policy contract in PingFederate, select identity attributes in the **Identity Attribute** list or click to add static values in the **Static Value** field.

   1. (Optional) If attribute sources are defined in the underlying connection, select the **- Data Store -** identity attribute option and the applicable data store values.

      |   |                                                                                                                                                                          |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | To ensure successful promotion, the target PingFederate must have the necessary Data Stores with identical names as required for authentication policy contract mapping. |

   2. (Optional) To define an OGNL expression and fine-tune attribute values to meet your needs, select the **- Expression -** identity attribute option and enter an **Expression Value** in the appropriate field.

      ![Screen capture of the expressions you can add to your application attributes.](../_images/ldx1635364871454.png)

4. When you're finished, click **Next**.

5. On the **Describe Application** page, enter the name of the application and a description in the appropriate fields.

   You are adding this application to PingCentral, so your name will automatically populate the **Owners** field.

   1. (Optional) To add owners or groups of owners, click the **Owners** field and select additional owners in the list. Click **Next**.

      |   |                                                                                                                                               |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | If the name you are looking for isn't showing in the list, contact your PingCentral administrator and request that the person be provisioned. |

6. Click **Save and Close**.

   The application is added at the top of the list of applications on the **Applications** page.

## Using PingAccess templates

After selecting a PingAccess template, use that template to apply user authentication and authorization support to an application.

### Before you begin

Prepare to define the following as appropriate:

* The application context root and resources

* The application policy

* The resource policy

* The application name and description

You can find details on each of these items in [Information needed to add PingAccess applications](#pa_info).

### Steps

1. On the **Define Resources** page, enter the context root for the application.

   The context root is the common root of all application resources, specifies where in the URL path the application begins, and starts with a slash. In the example URL, `den-ping.com:8443/mygreatapp/home`, the `/mygreatapp` is the context root.

2. Add, delete, or reorder application resources for your application.

   Every application has at least one root resource.

   If resource reordering is available, a **Reorder Resources** link displays on the page, as shown in the following example. If resource ordering was not enabled in the PingAccess application that was used to create this template, it is not enabled in PingCentral.

   ![A screen capture showing the Define Resources page with the Context Root field and the Resources section. Next to the heading for the Resources section is the hyperlink option to Add Resource and the hyperlink option to Reorder Resources, which displays on the Define Resources page if resource reordering is enabled.](../_images/lhp1600200935995.jpg)

   |   |                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------- |
   |   | Virtual resources are available in PingAccess version 6.2 or later, but are not yet supported in PingCentral. |

   To add a new resource:

   1. Click **Add Resource** and in the **Resource Name** field, enter the name of the resource.

   2. In the **Path Patterns** field, enter a list of URL path patterns that identify this resource. Path patterns start with a forward slash (/), begin after the context root, and extend to the end of the URL. There are two different types of path patterns: Basic and Regex. Select the **Regex** option when appropriate.

   3. In the **Resource Authentication** section, select the type of authentication the resource requires.

      If the resource requires the same authentication as the root application, select **Standard**. If authentication is not required to access the resource, select **Anonymous** or **Unprotected**.

   4. If the application is an API or Web + API application, in the **Methods** field, select the HTTP methods supported by the resource. Leave this field empty if the resource supports all methods.

   5. To log information regarding requests to this resource, select the **Audit** check box.

   6. Resources are enabled when they are added by default. To disable a resource, clear the **Enable** check box.

   7. If resource reordering is available, a **Reorder Resources** link displays on the page. To change the order of these resources, click the link, rearrange the resources, and click **Done**.

   To delete the resource, click the associated **Delete** icon.

3. On the **Define Application Policy** page, customize the policy for the application, if needed.

   To apply rules or rule sets, drag them from the **Available Rules** list to the **Policy** list. Click **Next**.

4. (Optional) On the **Define Resource Policy** page, customize the policy for each of your resources.

   To apply rules or rule sets to each resource, drag them from the **Available Rules** list to the **Policy** list. Click **Next**.

5. On the **Describe Application** page, enter the name of the application and a description in the appropriate fields.

   By adding this application to PingCentral, your name automatically populates the **Owners** field.

6. (Optional) To add owners, or groups of owners, click the **Owners** field and select additional owners from the list. Click **Next**.

   If the name you are looking for does not display in the list, contact your PingCentral administrator and request that the person be provisioned.

7. Click **Save and Close**.

   The application displays at the top of the list of applications on the **Applications** page.

## Information needed to add PingAccess applications

When you use templates to PingAccess applications to PingCentral, you provide the application context root and then define its resources, application policy, and resource policies. This section describes these items in detail and explains why you are prompted to provide this information.

There are three different types of PingAccess applications: Web, API, and Web + API. With Web + API applications, administrators can configure both Web and API settings for an application. These applications can switch between web and API processing behaviors on the fly based on whether the inbound request contains a web session cookie (Web) or an OAuth token (API).

* Resources

* Path patterns

* Rules and policies

### Resources

Each application consists of one or more resources, which you define in PingCentral. Resources are components of an application that require different levels of security. When you define resources within an application, you also define security regarding those resources.

![A diagram showing how user requests are routed to the requested resources.](../_images/xzg1600361729933.jpg)

Resources are protected by rules, which let you specify who can access your applications and resources, how and when they can do so, and what modifications can be made to the requested content. When rules, or sets of rules, are applied to applications and resources, they are called policies. Policies are applied to requests, which determine whether users are granted or denied access to the requested resource.

To access an application, users enter a URL. This URL consists of a virtual host, a context root, and the name of the resource they want to access.

![A screen capture identifying the virtual host, context root, and resource within a URL.](../_images/zvs1600361777811.jpg)

When you use a template to add a PingAccess application to PingCentral, you are prompted to provide the context root and define the resources within it. You can find more information in [Application resources](https://docs.pingidentity.com/pingaccess/latest/pingaccess_user_interface_reference_guide/pa_application_resources.html) in the PingAccess documentation.

### Path patterns

When handling requests, PingAccess uses resource path patterns to match resources. There are two different types of path patterns: Basic and Regex.

* **Basic patterns**: The default path pattern type, which defines a path to a specific resource or a pattern that matches multiple paths. Basic patterns can contain any number of "\*" wildcards. For example:

  ```
  /path/x/*
  ```

  matches any of these request paths:

  ```
  /path/x/
  /path/x/index.html
  /path/x/y/z/index.html
  ```

* **Regex patterns**: Regex patterns contain regular expressions and allow for more flexibility in resource matching as they support resource ordering. For example:

  ```
  /[^/]+/[a-z]+\.html
  ```

  matches any of these request paths:

  ```
  /images/gallery.html
  /search/index.html
  ```

  However, it would not match any of these request paths:

  ```
  /images/gallery2.html
  /search/pages/index.html
  /index.html
  ```

  |   |                                                                                                                                                                                                                                                                         |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Although Regex path patterns function in an agent deployment, system performance might decrease if they are used. Agents are unable to interpret Regex path patterns, so they must consult PingAccess for policy decisions for each resource with a Regex path pattern. |

When one or more path patterns match a request, PingAccess uses the first matching pattern it identifies, so the order in which path patterns are evaluated is important. By default, PingAccess orders path patterns automatically so that the most specific patterns are matched first. However, if more explicit control is needed, or if you are using regular expressions, enable resource ordering to manually specify the order in which path patterns are evaluated.

For example, an application might have three resources, such as:

* `/images/logo.png` (Basic)

* `/images/*` (Basic)

* `/.+/[a-z]\.png` (Regex)

A request to resource `/images/logo.png` is matched by all 3 path patterns, yet each resource can have different policy requirements. Resource ordering allows you to specify which of these path patterns is parsed first, further allowing you to control the policy that is applied to a particular request.

When you define the application resources in PingCentral, you are prompted to provide path pattern information. For more information, see [Path patterns reference](https://docs.pingidentity.com/bundle/pingaccess-61/page/ean1572449478234.html) in the *PingAccess User Interface Reference Guide*.

### Rules and policies

Rules let you specify who can access your applications and resources, how and when they can do so, and what modifications can be made to the requested content. There are two different types of rules: access control rules and processing rules. Access control rules determine whether users can access a resource, and processing rules determine how requests are processed.

When you put rules together, they are called policies.

* **Application policies**: Rules applied to the application as a whole. You can define Web rules and API rules for Web + API applications.

* **Resource policies**: Rules applied to specific resources. Every application has at least one resource.

Rules can limit access based on information such as user attributes, client network range, time of day. You can combine rules to create rule sets, which are reusable and can be applied to many different resources and applications. Rule sets grant requests if any or all of the constituent rules are successful:

* **Any**: An any rule set is evaluated from top to bottom and stops at the first rule that has its criteria met. If all rules fail, the request is denied.

* **All**: An all rule set is evaluated from top to bottom and stops when it gets to the first rule that does not have its criteria met. If one rule fails, the request is denied.

Since rules within a rule set are evaluated from top to bottom, the order in which rules display in rule sets is important. In PingCentral, you can customize policies by dragging rules from the **Available Rules** list to the **Policy** list and changing the order to meet your needs.

![A screen capture showing how the Available Rules list and the Policy list display side-by-side in PingCentral.](../_images/hji1600876577837.jpg)

Learn more in [Rules](https://docs.pingidentity.com/pingaccess/latest/pingaccess_user_interface_reference_guide/pa_rules.html) in the PingAccess documentation.

---

---
title: Introduction to PingCentral
description: An introduction to PingCentral and a high-level explanation of how it works.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_application_owners:pingcentral_intro/pingcentral_ao_intro
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_application_owners/pingcentral_intro/pingcentral_ao_intro.html
revdate: October 9, 2025
---

# Introduction to PingCentral

Use PingCentral to add user authentication and authorization support to your applications, promote them to the appropriate development environments for testing, and monitor them throughout their life cycles.

PingCentral:

* Makes it possible for you to apply security configurations to your applications without assistance from an administrator.

* Allows you to promote these applications yourself, when you are ready, rather than submitting a request and waiting for someone else to promote them for you.

* Provides a central monitoring location for greater visibility into applications across deployment life cycles.

* Minimizes the risk of promoting applications with vulnerable security policies within your organization.

Using PingCentral does not require extensive training. However, for the best possible experience, become familiar with how the platform works before getting started.

1. IAM Administrators create OAuth, OpenID Connect (OIDC), SAML, and PingAccess templates based on clients, connections, and application security configurations they think are worth replicating.

2. Administrators can also add clients, connections, and applications directly to PingCentral and assign owners to them.

3. You use SAML, OAuth, OIDC, and PingAccess templates to apply security configurations to your applications. A wizard guides you through the process of providing a name and description for each application you add to PingCentral. Another wizard guides you through the process of promoting your application to the target environment.

4. When you're ready, promote applications to the appropriate development environments to test them and promote them directly to production environments if your permissions allow.

   ![This flowchart illustrates the tasks application owners perform to add applications to and promote them to PingFederate or PingAccess development, staging, or production environments.](../../_images/nuq1601349842175.jpg)

---

---
title: Managing applications
description: Instructions for managing applications within PingCentral.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_application_owners:pingcentral_managing_apps/pingcentral_managing_apps
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_application_owners/pingcentral_managing_apps/pingcentral_managing_apps.html
revdate: October 9, 2025
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Managing applications

If you are an owner of an application, the application displays on the **Applications** page. From this page, you can add new applications, view and update existing applications, and delete them from PingCentral when they are no longer needed.

## Steps

1. Use the menu at the top of the page to sort the list of applications by modified date or by application name, or use the search feature to locate an application by name.

   OAuth, OIDC, SAML, and PingAccess applications are listed in the order in which they were last modified, by default, with the most recently modified at the top of the list.

   ![This image displays an example of the Applications page for an application owner.](../_images/tgt1592861474520.jpg)

2. On the **Applications** page, you can:

   * View information about an application. Click the expandable icon associated with it.

     Learn more in [Viewing application information](../pingcentral_viewing_apps/pingcentral_viewing_apps.html).

   * Add a new SAML, OAuth, or OIDC application to PingCentral. Click **Add Application**, select a template, and follow the wizard prompts.

     Learn more in [Adding applications](../pingentral_adding_apps/pingcentral_adding_apps.html).

     |   |                                                                                                                                              |
     | - | -------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | Administrators can also assign you as the owner of an application, in which case the application will display on your **Applications** page. |

   * Promote applications to development or production environments. Click the expandable icon associated with the application you want to promote and click the **Promote** tab. Learn more in [Promoting applications](../pingcentral_promoting_apps/pingcentral_promoting_apps.html).

   * Delete an application from PingCentral. Click its associated **Delete** icon.

     ### Choose from:

     * To delete an application from PingCentral only, click the **Delete** button.

     * To delete an application from all environments, depending on the application type, select the **Delete from PingFederate in all environments** or **Delete from PingAccess in all environments** checkbox and click the **Delete** button.

       |   |                                                                                                                                          |
       | - | ---------------------------------------------------------------------------------------------------------------------------------------- |
       |   | If a PingCentral administrator restricts access to application deletion, you cannot delete applications from PingFederate or PingAccess. |

---

---
title: Managing approvals (application owners)
description: Instructions for monitoring approval requests and promoting approved applications.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_application_owners:pingcentral_manage_approvals/pingcentral_app_owner_manage_approvals
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_application_owners/pingcentral_manage_approvals/pingcentral_app_owner_manage_approvals.html
revdate: October 11, 2025
section_ids:
  steps: Steps
---

# Managing approvals (application owners)

If you submit a request for application promotion to your administrator, you can track the application's approval status by accessing the **Promotion Approvals** page, located under the **Management** tab.

From this page, you can:

* Filter for approved, promoted, pending, rejected, or canceled approvals, or by environments or integration type. Use the **Visible** filter, which is enabled by default, to hide approvals that are in a canceled, promoted, or rejected status.

* **Promote** an approved application, or **Cancel** an approval request.

  |   |                                                                                                      |
  | - | ---------------------------------------------------------------------------------------------------- |
  |   | You see a bell icon in the top navigation bar when an administrator approves your promotion request. |

  ![Screen capture of console for application owners that displays the Approvals page with active approval requests. Status is filtering for Approved, Pending, and Rejected approval requests.](../_images/mkq1687889008190.jpg)

## Steps

1. Select your filters.

   You can filter by:

   * **Status**: **Approved**, **Pending**, or **Rejected**. The page automatically filters for any approved, pending, or rejected approval requests.

   * Environments.

   * Integration types (OAuth and OIDC or SAML).

   Click the filters to add or remove them.

2. To promote approved applications to an environment, click **Promote** in the row for the application that you want to promote.

   Learn more in [Promoting applications](../pingcentral_promoting_apps/pingcentral_promoting_apps.html).

   |   |                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------- |
   |   | There can only be one outstanding promotion approval request per application to an environment. |

   |   |                                                                                                                                                                                                                                                                                                                                            |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If an environment is offline or if a PingCentral administrator has set the environment status to **Disabled**, the environment is undergoing maintenance. During this time, the **Promote** button is inaccessible. You will be unable to promote the application while the environment is offline or disabled and undergoing maintenance. |

3. To cancel an approval request, click **Cancel** in the row for the application that you no longer want to request promotion approval.

---

---
title: Promoting applications
description: Instructions for promoting OAuth, OIDC, SAML, and PingAccess applications.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_application_owners:pingcentral_promoting_apps/pingcentral_promoting_apps
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_application_owners/pingcentral_promoting_apps/pingcentral_promoting_apps.html
revdate: May 14, 2026
page_aliases: ["pingcentral_info_pa_apps.adoc", "pingcentral_promoting_oauth_apps.adoc", "pingcentral_promoting_pa_apps.adoc", "pingcentral_promoting_saml_apps.adoc pingcentral_agent_deploy.adoc", "pingcentral_gateway_deploy.adoc", "pingcentral_metadata_saml_apps.adoc"]
section_ids:
  oauth: Promoting OAuth and OIDC applications
  before-you-begin: Before you begin
  steps: Steps
  saml: Promoting SAML applications
  before-you-begin-2: Before you begin
  steps-2: Steps
  metadata: Using metadata to promote SAML applications
  steps-3: Steps
  pingaccess: Promoting PingAccess applications
  before-you-begin-3: Before you begin
  steps-4: Steps
  pa_information: Information needed to promote PingAccess applications
  gateway: Gateway deployment
  agent: Agent deployment
---

# Promoting applications

You can promote all applications assigned to you to development environments for testing, and to production environments if your permissions allow.

Learn more in the following:

* [Promoting OAuth and OIDC applications](#oauth)

* [Promoting SAML applications](#saml)

* [Promoting PingAccess applications](#pingaccess)

|   |                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If an environment is offline, or if a PingCentral administrator has set the environment status to **Disabled**, you cannot promote the application. |

## Promoting OAuth and OIDC applications

You can promote the OAuth and OIDC applications assigned to you.

### Before you begin

Prepare to provide the following:

* Redirect URIs, if required. These are the URIs your users will be directed to after they receive authorization to access your application. Redirect URIs are only required when promoting applications that use an authorization code and implicit grant types.

  Redirect URIs are not limited to the number of characters they can contain, but cannot include wildcards or some special characters.

* If a client secret is required to authenticate your application, you can create a custom secret, generate a secret, or leave the field empty and PingCentral will generate a client secret for you.

### Steps

1. To promote the application to an environment, click the expandable icon associated with the application, select the **Promote** tab, and click **Promote**.

   |   |                                                                                                                                                                                                    |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If an environment is offline or if a PingCentral administrator has set the environment status to **Disabled**, you will be unable to promote the application to a disabled or offline environment. |

2. From the **Available Environments** list, select the environment to which you want to promote the application.

   |   |                                                                                                                                                  |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If you have the Application Owner role, you cannot promote applications to protected environments, which have shield icons associated with them. |

3. If curly brackets ({}) display in the upper right corner of the window, you can edit the underlying application JSON yourself. Or, you can complete the fields in this window.

   If you choose to complete the fields in this window, refer to the following:

   1. If redirect URIs are required to promote the application, enter them in the **Redirect URIs** field.

   2. If a client secret is required to authenticate your application, you can either:

      * Generate a new secret by selecting the option at the bottom of the modal.

      * Continue using the existing secret. Bypass the **Generate New Secret** button and promote the application.

   3. If extended properties are visible and editable, you can add or remove the values used for this application.

   To edit the JSON yourself:

   1. Click the curly brackets.

      The application JSON displays in the window.

   2. Update the JSON to meet your needs. Built-in JSON syntax validation occurs as you make updates to help prevent mistakes.

   3. When you're finished, promote the application.

      PingCentral promotes your application to the designated environment in PingFederate. You will see the new promotion in the **History** section of the page.

4. To configure the SSO connection, provide the following information to your service provider:

   * The client ID. Click **View Client Details** to access the **Promotion Details** window, which displays the client ID.

   * The OIDC discovery endpoint and client secret are also available in this window.

     ![This example displays the Client ID, the OIDC discovery endpoint, and the client secret on the Promotion Details modal.](../_images/ezi1718751416428.jpg)

## Promoting SAML applications

You can promote the SAML applications assigned to you.

### Before you begin

Prepare to provide the following:

* **Entity ID**: used to uniquely identify the application and obtained from the service provider ACS URL, the application's URL to which SAML assertions from the identity provider will be sent after user authentication occurs.

* **ACS URL**(s): the application's URL to which SAML assertions from the identity provider will be sent after user authentication occurs.

* **SLO Service URL**(s): the application's URL utilized for single logout (SLO) functionality.

* **SP certificates**: if the template you select is based on a PingFederate connection that requires a certificate.

* **An assertion encryption certificate**: required if encryption is enabled for the connection.

When SAML applications are promoted, the connection metadata is exported and stored as part of that application. This metadata is available to download as a `.xml` file, which you can use to promote similar SAML applications. Learn more about this process in [Using metadata to promote SAML applications](#metadata).

### Steps

1. To promote the application to an environment, click the **Expand** icon associated with the application, select the **Promote** tab, and click **Promote**.

   |   |                                                                                                                                                                                                    |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If an environment is offline or if a PingCentral administrator has set the environment status to **Disabled**, you will be unable to promote the application to a disabled or offline environment. |

2. In the **Available Environments** list, select the environment to which you want to promote the application.

   |   |                                                                                                                                                  |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If you have the Application Owner role, you cannot promote applications to protected environments, which have shield icons associated with them. |

3. If curly brackets ({}) display in the upper right corner of the window, you can edit the underlying application JSON yourself. Or, you can complete the fields in this window.

   If you choose to complete the fields in this window, refer to the following:

   1. In the **Entity ID**, **ACS URL**, and **SLO Service URL** fields, enter the appropriate information.

      If you provided a metadata file when you added your application to PingCentral, the **Promote to Environment** window is prepopulated with the information from the other SAML application. You can modify this information as necessary.

   2. If extended properties are visible and editable, you can add or remove the values used for this application.

   3. In the **Signing Certificate** list, select the appropriate certificate:

      * If the PingFederate environment contains signing certificates, those certificates display in the list.

        The signing certificate that was added to the environment when it was created or last updated displays as the **Environment Default** certificate.

      * If signing certificates are not available in the PingFederate environment and an environment default certificate isn't available, or if an environment default certificate is available but expired, the **Automatically generate certificate** option displays in the list.

        |   |                                                                                                                                                                                                                                                                                                                                                                                   |
        | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        |   | If you used signing certificates that were automatically generated to promote applications in PingCentral 1.7 or earlier, and you want to promote those applications to the same environments, you need to locate the signing certificates. Search for a signing certificate with a subject DN that matches the name of the application and select it as the signing certificate. |

   4. Upload SP certificates, if required. SP certificates are required for PingFederate SP connections when:

      * Either of the single logout (SLO) options, **IdP-Initiated-SLO** or **SP-Initiated-SLO**, are selected as the SAML profile.

      * Digital signatures are required, and the Signature Policy is set to the **Require authn requests to be signed when received via the POST or redirect bindings** option.

      * Inbound backchannel authentication is configured. You can find more information in the following topics in the PingFederate documentation:

        * [Configuring digital signatures for service provider connections](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configuring_digital_signatures_service_provider_connections.html).

        * [Configuring signature verification settings (SAML 2.0)](https://docs.pingidentity.com/pingfederate/12.3/administrators_reference_guide/pf_configuring_signature_verification_settings_saml_20.html)

   5. If encryption is enabled for the connection, click in the **Assertion Encryption Certificate** field. Select an assertion encryption certificate used for a previous promotion in the list or provide a new one.

      |   |                                                                                                                                    |
      | - | ---------------------------------------------------------------------------------------------------------------------------------- |
      |   | Only whole encryption is currently supported, so if a connection has attributes specified for encryption, the promotion will fail. |

   To edit the JSON yourself:

   1. Click the curly brackets.

      The application JSON displays in the window.

   2. Update the JSON to meet your needs. Built-in JSON syntax validation occurs as you make updates to help prevent mistakes.

4. Verify that the information displayed in the **Promote to Environment** window is correct and click **Promote**.

   PingCentral promotes your application to the designated environment in PingFederate. The new promotion shows in the**History** section of the page. If the signature verification certificate used during promotion is available in the PingFederate environment, that certificate is used. If not, a new certificate is created.

5. To configure a single sign-on (SSO) connection, provide the application Entity ID and the SSO endpoint URL to your service provider.

   To locate the SSO endpoint URL, click the **View Connections Detail** link associated with the promotion. The URL displays on the **Promotion Details** window.

   ![This example shows the Promotion Details page, which contains information regarding the promotion, such as the ACS URL, SSO endpoint URL, and certificates associated with the connection.](../_images/kio1624578838404.png)

### Using metadata to promote SAML applications

When SAML applications are promoted, the connection metadata is exported and stored as part of that application. This metadata is available to download as a `.xml` file, which you can use to promote similar SAML applications.

#### Steps

1. On the **Applications** page, locate an application that has a configuration you want to replicate in a new SAML application and click the expandable icon associated with that application.

2. Go to the **Promote** tab and click the **View Connection Details** link.

   The promotion information displays.

   ![A screen capture of the promotion information displayed in the Promotion Details window.](../_images/epd1686691021018.png)

3. Click **Download Identity Provider Metadata** to download the metadata as a `.xml` file and click **Close**.

4. Use the metadata on the service provider (SP) side to update the connection to the identity provider (IdP), as appropriate.

## Promoting PingAccess applications

Promote the PingAccess applications assigned to you.

### Before you begin

The information required to promote PingAccess Web applications, API applications, and Web + API applications varies by type. Prepare to provide the following information:

| Web applications            | API applications                                                        | Web + API applications              |
| --------------------------- | ----------------------------------------------------------------------- | ----------------------------------- |
| Virtual host (required)     | Virtual host (required)                                                 | Virtual host (required)             |
|                             | Access validation method (required if an identity mapping is specified) | Access validation method (required) |
| Web session (optional)      | Web session (optional)                                                  | Web session (required)              |
| Identity mapping (optional) | Identity mapping (optional)                                             | Identity mapping (optional)         |
| Site or agent (required)    | Site or agent (required)                                                | Site or agent (required)            |

Learn more about each of these items in [Information needed to promote PingAccess applications](#pa_information).

|   |                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Customized authentication challenge responses, which support single-page applications, are available in PingAccess version 6.2 or later. Applications with this type of policy can be added to PingCentral, but cannot be promoted to another environment unless the authentication challenge policy also exists in the target environment. |

### Steps

1. To promote the application to an environment, click the Expand icon associated with the application, select the **Promote** tab, and click **Promote**.

   |   |                                                                                                                                                                                                    |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If an environment is offline or if a PingCentral administrator has set the environment status to **Disabled**, you will be unable to promote the application to a disabled or offline environment. |

2. From the **Available Environments** list, select the environment to which you want to promote the application.

   |   |                                                                                                                                                  |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If you have the Application Owner role, you cannot promote applications to protected environments, which have shield icons associated with them. |

3. On the **Configure Promotion** page, click the **Virtual Hosts** field, and select the virtual hosts you want to add.

   To remove a virtual host, click the **X** icon next to the virtual host name.

4. Complete the remaining fields, which vary, depending on the type of application you are promoting.

   The following example shows the fields available to provide information for a Web + API application.

   ![A screen capture showing the options available on the Configure Promotion page for a Web + API application.](../_images/wih1600890414430.jpg)

5. Click **Next**.

6. On the **Review Promotion** page, review promotion information you added.

   Additional detail is available in the **Summary** and **Application** sections of the page.

7. Click **Promote and Close**.

8. To review details regarding the promotion, click the **View History Details** link associated with the promotion.

### Information needed to promote PingAccess applications

When you promote PingAccess applications to PingAccess environments, you provide virtual host, access validation, web session, and identity mapping information, as appropriate.

PingAccess can be deployed in one of two ways:

* [Gateway deployment](#gateway): In a gateway deployment, the destination is a site. Requests are routed to a PingAccess web server, which then forwards authorized requests to the target application or API on the site.

* [Agent deployment](#agent): In an agent deployment, the destination is an agent. Requests are intercepted at the web server hosting the target application or API by the PingAccess agent plugin. The agent communicates with the PingAccess policy server to validate access before allowing the request to proceed to the target application or API.

The key difference between these deployments is where the initial request is directed. In a gateway deployment, the initial request is routed to a PingAccess web server, so the destination is a site. In an agent deployment, the initial request is routed to the web server that hosts the target application or API, so the destination is an agent. When you promote PingAccess applications, you are prompted to provide the name of the site or agent.

#### Gateway deployment

This diagram shows how users are authenticated, and how access policies and identity mappings are applied to requests to access applications or APIs with a gateway deployment.

![This diagram shows how users are authenticated, and how access policies and identity mappings are applied to requests to access applications or APIs with a gateway deployment.](../_images/rki1599598432959.jpg)

1. Users enter a URL that consists of a unique virtual host and context root.

   * **Virtual host**: The public-facing host name and host port. For example, `den.ping.com:8443`.

     A wildcard (`*`) can be used either to define either any host (`*:8443`, for example) or any host within a domain (`*.ping.com`, for example). If a request matches more than one virtual host, the most specific match is used.

   * **Context root**: The common root of all resources, specifies where in the URL path the application begins, and starts with a slash. In the example URL, `den-ping.com:8443/mygreatapp/home`, `/mygreatapp/` is the context root.

   PingCentral prompts you for the context root when you add the application, and for the virtual hosts when you promote it.

2. The PingAccess web server determines whether a PingAccess session cookie (Web) or an OAuth token (API) exists for the user. If it does not, a web session starts. Web sessions define the policy for web application session creation, lifetime, timeouts, and their scope.

   |   |                                                                                                                                                                       |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you promote Web + API applications in PingCentral, you must select a Web session from a list. This information is not required to promote Web or API applications. |

3. You can configure API and Web + API applications to use access token validators to locally verify signed and encrypted access tokens. If you are promoting an API or Web + API application in PingCentral, you can specify the access validation method, whether it be a token provider or a token validator, if appropriate.

4. Users are authenticated through the web session.

5. Policies are applied to the request. Policies are rules, or sets of rules, that are applied to application resources. makes policy-based decisions to grant or deny access to the requested resource.

   You can customize application and resource policies when you use templates to add applications to PingCentral.

6. Identity mapping is applied to the request if the target application expects user information to be included to further authenticate the user.

   PingCentral prompts you for the name of the Web and/or API Identity mapping, as appropriate, when you promote it.

7. The user accesses the target web application or API.

#### Agent deployment

The following diagram shows how users are authenticated, and how access policies and identity mappings are applied to requests to access applications or APIs with an agent deployment.

![This diagram shows hows users are authenticated, and how access policies and identity mappings are applied to requests to access applications or APIs with an agent deployment.](../_images/ywn1599605492379.jpg)

1. Users enter a URL to request access to a resource and their requests.

2. The PingAccess agent plugin intercepts the request. Agents use names and shared secrets to authenticate with the policy server. These names and secrets do not need to be unique. Any number of agents can have the same name and secret, and they are all treated equally by the policy server.

3. If the agent does not have previously cached policies for the resource, it contacts the PingAccess policy server for instructions.

4. The PingAccess policy server receives claims from the token provider, which provides instructions for handling the request.

5. Policies are applied to the request and PingAccess makes policy-based decisions to grant or deny access to the requested resource.

6. Identity mapping is applied to the request if the target application expects user information to be included to further authenticate the user.

7. The user accesses the target web application or API.

---

---
title: Reverting applications to previously promoted versions
description: Instructions for reverting applications to previously promoted versions.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_application_owners:pingdirectory_revert_apps/pingcentral_revert_ao_apps
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_application_owners/pingdirectory_revert_apps/pingcentral_revert_ao_apps.html
revdate: October 10, 2025
section_ids:
  steps: Steps
---

# Reverting applications to previously promoted versions

When you revert applications to previously promoted versions, the reverted versions of the application will not exist outside of PingCentral until you promote them again, at which point they will also be available in PingFederate or PingAccess.

## Steps

1. On the **Applications** page, locate the application you want to revert to a previously promoted version.

   |   |                                                                             |
   | - | --------------------------------------------------------------------------- |
   |   | You cannot revert applications created in previous versions of PingCentral. |

2. Click the expandable icon associated with the application, select the **Promote** tab, and then click **View Details**.

3. In the **Promotion Details** window, click **Revert Application**.

   A message displays asking you if you are sure you want to revert this application.

4. Click **Revert**.

   The reverted version of the application displays in your applications list.

   |   |                                                                                                                                                                                                                                                                                                                                                                                 |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Reverting OAuth and OIDC applications to previously promoted versions overrides client secrets, so you will need to create or generate new secrets before you promote them again. Reverting SAML applications to previously promoted versions overrides the Entity IDs, ACS URLs, and certificates, so you might need to update this information before you promote them again. |

---

---
title: Updating applications
description: Instructions for updating PingCentral applications.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_application_owners:pingcentral_updating_apps/pingcentral_ao_updating_apps
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_application_owners/pingcentral_updating_apps/pingcentral_ao_updating_apps.html
revdate: October 9, 2025
section_ids:
  steps: Steps
---

# Updating applications

To keep your applications secure, rotate certificates and client secrets on a regular basis and apply updated security configurations to applications built from templates if new configuration templates become available. You don't need to recreate your applications in PingCentral to apply new templates. Replace the templates associated with your applications and promote them again.

## Steps

1. Click the **Expand** icon associated with the application you want to update and click the **Pencil** icon.

   All the editable information is shown on one page.

2. To update the name, description, and owners, change the information in the **Name**, **Description**, and **Owners** fields. Click **Save**.

3. To change the template used to create the application, click **Change Template** and select a new template from the **Select Template** page. Click **Save and Close**.

   |   |                                                                                                                                              |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You cannot apply a SAML template to an OAuth or OpenID Connect (OIDC) application nor apply an OAuth or OIDC template to a SAML application. |

4. **Optional:** To update OAuth or OIDC application information:

   * In the **Client** section, change the scopes associated with OAuth or OIDC applications. Select or clear the appropriate checkboxes and click **Save**.

     |   |                                                                                                                                                                                                                                   |
     | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | You cannot edit scopes for applications created in PingCentral 1.2.0. However, you can update the template associated with an application to a template created in a later version, which allows you to update scope information. |

   * In the **Promote** section, change the information in the **Redirect URI** fields for the appropriate environments and click **Save**.

   * To change client secrets, return to the **Applications** page, promote the application again, and generate a new secret.

5. **Optional:** To update SAML application information:

   * In the **Attribute Mappings** section, add or remove attributes and expressions, or update attribute and expression values, and click **Save**.

   * In the **Promotions** section, upload a new `.xml` file that contains service provider metadata, such as the Entity ID, ACS URL, certificates, and attribute information, from another SAML application. Click **Choose File** or **Or Use URL** to provide the metadata file.

     |   |                                                                                                                                    |
     | - | ---------------------------------------------------------------------------------------------------------------------------------- |
     |   | If metadata is used, the attribute mapping section might also need to be updated to include new attributes from the metadata file. |

   * Change the information in the **Entity ID** or **ACS URL** fields and click **Save**.

   * To change the signing certificate, select the appropriate certificate in the **Signing Certificate** list and click **Save**.

   * To change the service provider (SP) certificate, click **SP Certificate** to upload a new certificate, or click **Remove** to remove it. Click **Save**.

6. **Optional:** To update PingAccess application information:

   * On the **Properties** tab, in the **Promote** section, update the **Virtual Hosts**, **Access Validation**, **Identity Mapping**, and **Site** or **Agent** names, as appropriate. Click **Save**.

   * On the **Resources** tab, update information regarding each resource and click **Save**.

   * On the **Policy** tab, click the **Pencil** icon associated with the policy you want to update. Make changes and click **Save**.

---

---
title: Viewing application information
description: Instructions for viewing application information.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_application_owners:pingcentral_viewing_apps/pingcentral_viewing_apps
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_application_owners/pingcentral_viewing_apps/pingcentral_viewing_apps.html
revdate: October 9, 2025
section_ids:
  steps: Steps
---

# Viewing application information

If you are an owner of an application, the application displays on the **Applications** page.

## Steps

1. Use the menu at the top of the page to sort the list of applications by modified date or by application name, or use the search feature to locate an application by name.

   Security Assertion Markup Language (SAML) *(tooltip: \<div class="paragraph">
   \<p>A standard, XML-based, message-exchange framework enabling the secure transmittal of authentication tokens and other user attributes across domains.\</p>
   \</div>)*, OAuth *(tooltip: \<div class="paragraph">
   \<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
   \</div>)*, OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
   \<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
   \</div>)*, and PingAccess applications are listed in the order in which they were last modified, by default, with the most recently modified at the top of the list.

2. To view details regarding an application, click the expandable icon associated with it.

   Applications promoted to development environments (such as development, staging, or production) display icons associated with each environment. If an application has not yet been promoted to a specific environment, you will not see an icon representing that environment.

   ![A screen capture of what the Applications page might look like for an application owner.](../_images/plp1582749215404.png)

3. To review additional information about the application, click each tab.

   * **Summary tab**: This tab displays the application or connection name, description, owners, the date on which the application was last modified, and additional information specific to the application, client, or connection.

   * **Template tab**: This tab displays if the application was created from a template. It includes the name of the template applied to the application, and details regarding the application, client or connection on which the template was based.

   * **Client tab**: This tab displays if the application was created from an OAuth or OIDC application that was directly added to PingCentral from PingFederate. It includes the client name, ID, grant types, attributes, and applicable policies.

   * **Connection tab**: This tab displays if the application was created from a SAML application that was directly added to PingCentral from PingFederate. It includes the name of the connection, browser profiles, and binding information.

   * **Application tab**: This tab displays if the application was directly added to PingCentral from PingAccess. It includes the application name, description, and details regarding the application.

   * **Promote tab**: This tab displays the promotion history of this application, which includes the date and time each promotion occurred.

     |   |                                                                                                                                                                                                                                                      |
     | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If an environment is offline or if a PingCentral administrator has set the environment status to **Disabled**, you may still view the application details, however, you will be unable to edit the application in a disabled or offline environment. |

4. To access additional information regarding the application and its promotion history, click **View Client Details**.

---

---
title: Accessing PingCentral
description: Instructions for accessing PingCentral.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_application_owners:pingcentral_accessing/pingcentral_accessing_pc
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_application_owners/pingcentral_accessing/pingcentral_accessing_pc.html
revdate: October 14, 2025
section_ids:
  steps: Steps
---

# Accessing PingCentral

PingCentral is a web-based application that you access from a URL. For the best possible experience, use Chrome or Firefox as your browser.

## Steps

1. Contact your IAM Administrator for the PingCentral URL and your sign-on credentials.

2. Enter your credentials.

   |   |                                                                                                              |
   | - | ------------------------------------------------------------------------------------------------------------ |
   |   | If you have multiple failed login attempts, you wil be locked out of PingCentral for a short period of time. |

---

---
title: Adding applications
description: Instructions for adding applications to PingCentral.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_application_owners:pingentral_adding_apps/pingcentral_adding_apps
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_application_owners/pingentral_adding_apps/pingcentral_adding_apps.html
revdate: October 13, 2025
page_aliases: ["pingcentral_info_pa_templates.adoc", "pingcentral_pa_templates.adoc", "pingcentral_path_patterns.adoc", "pingcentral_resources.adoc", "pingcentral_rules_policies.adoc", "pingcentral_selecting_template.adoc", "pingcentral_using_oauth_templates.adoc", "pingcentral_using_saml_templates.adoc"]
section_ids:
  select_template: Selecting a template
  steps: Steps
  oauth_template: Using OAuth and OIDC templates
  before-you-begin: Before you begin
  steps-2: Steps
  saml_template: Using SAML 2.0 templates
  before-you-begin-2: Before you begin
  steps-3: Steps
  pa_template: Using PingAccess templates
  before-you-begin-3: Before you begin
  steps-4: Steps
  pa_info: Information needed to add PingAccess applications
  resources: Resources
  path-patterns: Path patterns
  rules-and-policies: Rules and policies
---

# Adding applications

Before you can promote applications to development environments for testing, you must add them to PingCentral.

To add applications to PingCentral, you can use OAuth, OIDC, SAML, and PingCentral templates to apply security configurations to your applications. Wizards guide you through these processes.

Learn more:

* [Selecting a template](#select_template)

* [Using OAuth and OIDC templates](#oauth_template)

* [Using SAML templates](#saml_template)

* [Using PingAccess templates](#pa_template)

Administrators can also assign applications directly to you. These applications display on your **Applications** page, where you can promote them, test them on development environments, modify them, and manage them throughout their life cycles.

## Selecting a template

IAM Administrators can create OAuth *(tooltip: \<div class="paragraph">
\<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
\</div>)*, OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)*, Security Assertion Markup Language (SAML) *(tooltip: \<div class="paragraph">
\<p>A standard, XML-based, message-exchange framework enabling the secure transmittal of authentication tokens and other user attributes across domains.\</p>
\</div>)*, and PingAccess templates and make them available for you to use to apply security configurations to your application.

### Steps

1. Click **Add Application**.

2. Review the template descriptions to determine which template you should use.

   ![A screen capture of the Select Template page, which lists the templates available for application owners to use. This screen capture shows the templates for Public Application, which is an OpenID Connect template; Internal Application (and Partners), which is an OAuth template; Access Control Policy, which is a template; and Existing Application. A side bar appears to the right of the template list to provide a guide for choosing which template to select.](../../_images/jwq1600185986194.jpg)

   On this page, you can:

   * Select the filtering options to filter OAuth, OpenID Connect, SAML, and PingAccess templates.

   * Click the **Review Configuration** link within the template description to view the details associated with each template.

   If you are unclear about what type of template to select, keep the following in mind:

   * OAuth and OIDC are most commonly used by consumer applications and services so users do not need to sign up for a new username and password. "Sign in with Google," or "Log in with Facebook" are examples of OAuth protocols you are likely familiar with. You might also use OAuth if your application is consumed on a mobile device.

   * SAML is most commonly used by businesses to allow their users to access services they pay for. Salesforce and Gmail are examples of service providers an employee could gain access to after completing a SAML sign on. SAML templates can also be used for web applications created and used within your organization.

   * PingAccess templates can be used to apply access policy to Web and API applications.

   * If an environment is offline or if a PingCentral administrator has set the environment status to **Disabled**, you will be unable to select a disabled or offline environment for template creation.

3. Select the template you want to use, or the existing application you want to add to PingCentral and click **Next**.

4. To proceed, see the appropriate topic:

   * [Using OAuth and OIDC templates](#oauth_template)

   * [Using SAML templates](#saml_template)

   * [Using PingAccess templates](#pa_template)

## Using OAuth and OIDC templates

After selecting an OAuth or OIDC template, use that template to apply user authentication and authorization support to an application.

### Before you begin

Prepare to provide the following:

* Name of the application.

* A brief, accurate description of your application.

* Scopes, which are optional and can be customized to meet your needs. See [Scopes and scope management](https://docs.pingidentity.com/access/sources/dita/topic?resourceid=pf_scopes_and_scope_management) in the PingFederate documentation for additional information.

### Steps

1. If you want to add scopes to the applications, begin typing the name of the scope you want to add and select it from the list when it displays.

   |   |                                                                                                                                                                                                             |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The names of scopes added to applications cannot contain spaces, nor can the **Scopes** field contain spaces before or after the scope name. If spaces exist, applications cannot be successfully promoted. |

   When this application is later promoted, the target PingFederate scope management configuration is referenced to satisfy the scope requirements of the client. Any named scope identified as a common scope in the target environment is configured within the client as a restricted scope.

   If the named scope does not exist in the target environment, the scope is created as an exclusive scope. In that case, or if the scope already exists as an exclusive scope, then the scope is associated with the client as an exclusive scope.

2. Click **Next**.

3. On the **Describe Application** page, enter the name of your application and a description of the application in the **Name** and **Description** fields.

   You are adding this application to PingCentral, so your name will automatically populate the **Owners** field.

4. (Optional) To add owners, or groups of owners, select additional owners from the **Owners** list. If the name you are looking for does not display in the list, contact your PingCentral administrator and request that the person be provisioned.

   ![This example shows the Describe Application page, which contains the Name, Description, and Owners fields.](../_images/tji1617032771105.png)

5. Click **Save and Close**.

The application appears at the top of the list of applications on the **Applications** page.

## Using SAML 2.0 templates

After selecting a SAML template, use that template to apply user authentication and authorization support to an application.

### Before you begin

You must provide:

* The name of the application.

* A brief, accurate description of your application.

* Attribute mapping information, used to map your application attributes to the identity attributes required from the identity provider to verify user identities.

### Steps

1. In PingCentral, on the **Select Metadata** page, complete one of the following tasks:

   * Provide a metadata file from service provider (SP) connections, which might include entity IDs, ACS URLs, and certificates. Click **Choose file** to provide the file.

   * Provide a URL to the metadata file. Click **Or Use URL** to provide the URL.

   * Skip this step and provide the Entity ID, ACS URL, certificate, and attributes, or all of this information, during the promotion process.

   If you choose to provide a metadata file, the information in the file shows on the page.

   ![Screen capture of the Select Metadata page after a metadata file is provided.](../_images/hac1582759323012.png)

2. Click **Next**.

3. On the **Map Attributes** page, to map the application attributes to the identity attributes required to fulfill the authentication policy contract in PingFederate, select identity attributes in the **Identity Attribute** list or click to add static values in the **Static Value** field.

   1. (Optional) If attribute sources are defined in the underlying connection, select the **- Data Store -** identity attribute option and the applicable data store values.

      |   |                                                                                                                                                                          |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | To ensure successful promotion, the target PingFederate must have the necessary Data Stores with identical names as required for authentication policy contract mapping. |

   2. (Optional) To define an OGNL expression and fine-tune attribute values to meet your needs, select the **- Expression -** identity attribute option and enter an **Expression Value** in the appropriate field.

      ![Screen capture of the expressions you can add to your application attributes.](../_images/ldx1635364871454.png)

4. When you're finished, click **Next**.

5. On the **Describe Application** page, enter the name of the application and a description in the appropriate fields.

   You are adding this application to PingCentral, so your name will automatically populate the **Owners** field.

   1. (Optional) To add owners or groups of owners, click the **Owners** field and select additional owners in the list. Click **Next**.

      |   |                                                                                                                                               |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | If the name you are looking for isn't showing in the list, contact your PingCentral administrator and request that the person be provisioned. |

6. Click **Save and Close**.

   The application is added at the top of the list of applications on the **Applications** page.

## Using PingAccess templates

After selecting a PingAccess template, use that template to apply user authentication and authorization support to an application.

### Before you begin

Prepare to define the following as appropriate:

* The application context root and resources

* The application policy

* The resource policy

* The application name and description

You can find details on each of these items in [Information needed to add PingAccess applications](#pa_info).

### Steps

1. On the **Define Resources** page, enter the context root for the application.

   The context root is the common root of all application resources, specifies where in the URL path the application begins, and starts with a slash. In the example URL, `den-ping.com:8443/mygreatapp/home`, the `/mygreatapp` is the context root.

2. Add, delete, or reorder application resources for your application.

   Every application has at least one root resource.

   If resource reordering is available, a **Reorder Resources** link displays on the page, as shown in the following example. If resource ordering was not enabled in the PingAccess application that was used to create this template, it is not enabled in PingCentral.

   ![A screen capture showing the Define Resources page with the Context Root field and the Resources section. Next to the heading for the Resources section is the hyperlink option to Add Resource and the hyperlink option to Reorder Resources, which displays on the Define Resources page if resource reordering is enabled.](../_images/lhp1600200935995.jpg)

   |   |                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------- |
   |   | Virtual resources are available in PingAccess version 6.2 or later, but are not yet supported in PingCentral. |

   To add a new resource:

   1. Click **Add Resource** and in the **Resource Name** field, enter the name of the resource.

   2. In the **Path Patterns** field, enter a list of URL path patterns that identify this resource. Path patterns start with a forward slash (/), begin after the context root, and extend to the end of the URL. There are two different types of path patterns: Basic and Regex. Select the **Regex** option when appropriate.

   3. In the **Resource Authentication** section, select the type of authentication the resource requires.

      If the resource requires the same authentication as the root application, select **Standard**. If authentication is not required to access the resource, select **Anonymous** or **Unprotected**.

   4. If the application is an API or Web + API application, in the **Methods** field, select the HTTP methods supported by the resource. Leave this field empty if the resource supports all methods.

   5. To log information regarding requests to this resource, select the **Audit** check box.

   6. Resources are enabled when they are added by default. To disable a resource, clear the **Enable** check box.

   7. If resource reordering is available, a **Reorder Resources** link displays on the page. To change the order of these resources, click the link, rearrange the resources, and click **Done**.

   To delete the resource, click the associated **Delete** icon.

3. On the **Define Application Policy** page, customize the policy for the application, if needed.

   To apply rules or rule sets, drag them from the **Available Rules** list to the **Policy** list. Click **Next**.

4. (Optional) On the **Define Resource Policy** page, customize the policy for each of your resources.

   To apply rules or rule sets to each resource, drag them from the **Available Rules** list to the **Policy** list. Click **Next**.

5. On the **Describe Application** page, enter the name of the application and a description in the appropriate fields.

   By adding this application to PingCentral, your name automatically populates the **Owners** field.

6. (Optional) To add owners, or groups of owners, click the **Owners** field and select additional owners from the list. Click **Next**.

   If the name you are looking for does not display in the list, contact your PingCentral administrator and request that the person be provisioned.

7. Click **Save and Close**.

   The application displays at the top of the list of applications on the **Applications** page.

## Information needed to add PingAccess applications

When you use templates to PingAccess applications to PingCentral, you provide the application context root and then define its resources, application policy, and resource policies. This section describes these items in detail and explains why you are prompted to provide this information.

There are three different types of PingAccess applications: Web, API, and Web + API. With Web + API applications, administrators can configure both Web and API settings for an application. These applications can switch between web and API processing behaviors on the fly based on whether the inbound request contains a web session cookie (Web) or an OAuth token (API).

* Resources

* Path patterns

* Rules and policies

### Resources

Each application consists of one or more resources, which you define in PingCentral. Resources are components of an application that require different levels of security. When you define resources within an application, you also define security regarding those resources.

![A diagram showing how user requests are routed to the requested resources.](../_images/xzg1600361729933.jpg)

Resources are protected by rules, which let you specify who can access your applications and resources, how and when they can do so, and what modifications can be made to the requested content. When rules, or sets of rules, are applied to applications and resources, they are called policies. Policies are applied to requests, which determine whether users are granted or denied access to the requested resource.

To access an application, users enter a URL. This URL consists of a virtual host, a context root, and the name of the resource they want to access.

![A screen capture identifying the virtual host, context root, and resource within a URL.](../_images/zvs1600361777811.jpg)

When you use a template to add a PingAccess application to PingCentral, you are prompted to provide the context root and define the resources within it. You can find more information in [Application resources](https://docs.pingidentity.com/pingaccess/latest/pingaccess_user_interface_reference_guide/pa_application_resources.html) in the PingAccess documentation.

### Path patterns

When handling requests, PingAccess uses resource path patterns to match resources. There are two different types of path patterns: Basic and Regex.

* **Basic patterns**: The default path pattern type, which defines a path to a specific resource or a pattern that matches multiple paths. Basic patterns can contain any number of "\*" wildcards. For example:

  ```
  /path/x/*
  ```

  matches any of these request paths:

  ```
  /path/x/
  /path/x/index.html
  /path/x/y/z/index.html
  ```

* **Regex patterns**: Regex patterns contain regular expressions and allow for more flexibility in resource matching as they support resource ordering. For example:

  ```
  /[^/]+/[a-z]+\.html
  ```

  matches any of these request paths:

  ```
  /images/gallery.html
  /search/index.html
  ```

  However, it would not match any of these request paths:

  ```
  /images/gallery2.html
  /search/pages/index.html
  /index.html
  ```

  |   |                                                                                                                                                                                                                                                                         |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Although Regex path patterns function in an agent deployment, system performance might decrease if they are used. Agents are unable to interpret Regex path patterns, so they must consult PingAccess for policy decisions for each resource with a Regex path pattern. |

When one or more path patterns match a request, PingAccess uses the first matching pattern it identifies, so the order in which path patterns are evaluated is important. By default, PingAccess orders path patterns automatically so that the most specific patterns are matched first. However, if more explicit control is needed, or if you are using regular expressions, enable resource ordering to manually specify the order in which path patterns are evaluated.

For example, an application might have three resources, such as:

* `/images/logo.png` (Basic)

* `/images/*` (Basic)

* `/.+/[a-z]\.png` (Regex)

A request to resource `/images/logo.png` is matched by all 3 path patterns, yet each resource can have different policy requirements. Resource ordering allows you to specify which of these path patterns is parsed first, further allowing you to control the policy that is applied to a particular request.

When you define the application resources in PingCentral, you are prompted to provide path pattern information. For more information, see [Path patterns reference](https://docs.pingidentity.com/bundle/pingaccess-61/page/ean1572449478234.html) in the *PingAccess User Interface Reference Guide*.

### Rules and policies

Rules let you specify who can access your applications and resources, how and when they can do so, and what modifications can be made to the requested content. There are two different types of rules: access control rules and processing rules. Access control rules determine whether users can access a resource, and processing rules determine how requests are processed.

When you put rules together, they are called policies.

* **Application policies**: Rules applied to the application as a whole. You can define Web rules and API rules for Web + API applications.

* **Resource policies**: Rules applied to specific resources. Every application has at least one resource.

Rules can limit access based on information such as user attributes, client network range, time of day. You can combine rules to create rule sets, which are reusable and can be applied to many different resources and applications. Rule sets grant requests if any or all of the constituent rules are successful:

* **Any**: An any rule set is evaluated from top to bottom and stops at the first rule that has its criteria met. If all rules fail, the request is denied.

* **All**: An all rule set is evaluated from top to bottom and stops when it gets to the first rule that does not have its criteria met. If one rule fails, the request is denied.

Since rules within a rule set are evaluated from top to bottom, the order in which rules display in rule sets is important. In PingCentral, you can customize policies by dragging rules from the **Available Rules** list to the **Policy** list and changing the order to meet your needs.

![A screen capture showing how the Available Rules list and the Policy list display side-by-side in PingCentral.](../_images/hji1600876577837.jpg)

Learn more in [Rules](https://docs.pingidentity.com/pingaccess/latest/pingaccess_user_interface_reference_guide/pa_rules.html) in the PingAccess documentation.