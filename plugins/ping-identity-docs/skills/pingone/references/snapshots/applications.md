---
title: Access tokens and ID tokens
description: Learn how PingOne uses access tokens and ID tokens in OAuth 2 and OIDC requests.
component: pingone
page_id: pingone:applications:p1_access_token_id_token
canonical_url: https://docs.pingidentity.com/pingone/applications/p1_access_token_id_token.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 9, 2023
section_ids:
  related-links: Related links
---

# Access tokens and ID tokens

Access tokens are credential strings that represent authorization to access a protected resource.

Client applications obtain access tokens by making OAuth 2 or OpenID Connect (OIDC) requests to an authorization server. Resource servers require clients to authenticate using access tokens.

Access tokens are obtained from the token endpoint, when using the client credentials grant type, or from the authorization endpoint, when using the implicit grant type. Access tokens are typically granted on behalf of a specific authenticated user. Tokens granted directly to applications are called application tokens.

## Related links

* [Customizing access tokens](p1_customize_access_token.html)

---

---
title: Adding a custom resource
description: Use the Resources page to add a custom resource to PingOne.
component: pingone
page_id: pingone:applications:p1_adding_custom_resource
canonical_url: https://docs.pingidentity.com/pingone/applications/p1_adding_custom_resource.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 10, 2025
section_ids:
  steps: Steps
  next-steps: Next steps
---

# Adding a custom resource

Use the **Resources** page to add a custom resource to PingOne.

## Steps

1. In the PingOne admin console, go to **Applications > Resources**.

2. In the **Create Resource Profile** step, enter the following information:

   * **Resource Name**: A unique identifier for the resource.

   * **Audience** (optional): The intended audience for the resource. If you don't provide a value, PingOne will default to the resource name.

   * **Description** (optional): A brief description of the resource.

   * **Access token time to live (seconds)**: The maximum time that the access token will be valid for use in the application, in seconds.

3. Click **Next**.

4. In the **Attributes** step, map resource attributes to user attributes in PingOne.

   Resources can use JSON attributes in their attribute mappings. You can use these attributes to pass complex information to applications through an access token. Learn more in [Adding user attributes](../directory/p1_adduserattributes.html).

   1. Enter a resource attribute and then select the corresponding PingOne attribute in the list.

      For example, you could map the `OIDC family_name` attribute to the PingOne `Family Name` attribute.

   2. (Optional) Click the **Gear** icon ([icon: gear, set=fa]) to use advanced expressions. Learn more in [Using the expression builder](../pingone_expression_language/p1_use_expression_builder.html).

   3. (Optional) Select the **Required** checkbox to make the attribute required.

      * For any attributes except the `sub` attribute

        If it can't find a value for an attribute set as required, PingOne doesn't issue an access token for the resource and instead issues an error message in the token response.

      * For the `sub` attribute

        The following table lists how PingOne handles the `sub` attribute based on whether it's set as required and what grant type the application is using:

        | `sub` set as required? | Application grant type                                                | If PingOne can't find an attribute mapping value?                                                                 |
        | ---------------------- | --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
        | Yes                    | Any grant type requiring user interaction, such as authorization code | PingOne doesn't issue an access token for the resource and instead issues an error message in the token response. |
        | Yes                    | Client credentials                                                    | PingOne doesn't issue an access token for the resource and instead issues an error message in the token response. |
        | No                     | Any grant type requiring user interaction                             | PingOne populates the `sub` attribute with the PingOne user ID of the authenticated user.                         |
        | No                     | Client credentials                                                    | PingOne returns an access token without including the `sub` attribute.                                            |

   4. To add more attributes, click **[icon: plus, set=fa]Add** and enter an attribute and the corresponding PingOne mapping.

   5. To delete an attribute, click the **Delete** icon ([icon: trash, set=fa]) for the appropriate attribute.

      ![A screen capture of the Attributes step when adding a custom resource.](_images/p1-add-custom-resource.png)

5. Click **Next**.

6. In the **Scopes** step, configure the appropriate scopes for the resource. Each resource can have one or more scopes.

   To add a scope, click **[icon: plus, set=fa]Add Scope** and enter the following:

   * **Scope Name**: The name of the scope to be used for this resource. Scopes are defined by the resource server.

   * **Description** (optional): A brief description of the scope.

7. Click **Save**.

## Next steps

* You can add more scopes to the custom resource. Learn more in [Editing a resource](p1_editresource.html).

* With PingOne Authorize, you can define application resources and permissions to set up role-based access control for the custom resource. Learn more in [Application permissions](p1_application_permissions.html) and [Editing a resource](p1_editresource.html).

* You can enable an OIDC-based application to request scopes from multiple resources in a single request. Learn more about the **Request scopes to access multiple resources** option in [Editing an application - OIDC](p1_edit_application_oidc.html).

---

---
title: Adding Amazon Web Services to the PingOne application portal
description: Add Amazon Web Services to the PingOne application portal.
component: pingone
page_id: pingone:applications:p1_adding_amazon_web_services_p1_application_portal
canonical_url: https://docs.pingidentity.com/pingone/applications/p1_adding_amazon_web_services_p1_application_portal.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 10, 2025
section_ids:
  steps: Steps
  result: Result:
  next-steps: Next steps
---

# Adding Amazon Web Services to the PingOne application portal

Use the application catalog to add Amazon Web Services (AWS) *(tooltip: \<div class="paragraph">
\<p>An Amazon subsidiary providing cloud computing platforms.\</p>
\</div>)* to your application portal.

## Steps

1. In PingOne, go to **Applications > Application Catalog**.

2. In the **Search for applications** field, enter `Amazon Web Services`.

3. Click the **Amazon Web Services** entry to open the details panel.

4. Review the following:

   * **Name**. Enter a new name to replace the default application name (optional).

   * **Icon**. Select a new image to replace the default application icon (optional).

   * **Entity ID**. The field is pre-populated with the correct value for AWS.

5. Click **Next**.

6. On the **Map Attributes** page, review the AWS to PingOne attribute mappings.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                              |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Common attributes are pre-populated with the Security Assertion Markup Language (SAML) *(tooltip: \<div class="paragraph">&#xA;\<p>A standard, XML-based, message-exchange framework enabling the secure transmittal of authentication tokens and other user attributes across domains.\</p>&#xA;\</div>)* subject, the SAML role session name, and the SAML session duration. You must map any required attributes before you can continue. |

   | Option                                 | Description                                                                                                                                                                                                                                                                                                      |
   | -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | To change an attribute mapping         | Enter or select a new attribute in the PingOne Mappings list.                                                                                                                                                                                                                                                    |
   | To add an attribute                    | Click **[icon: plus, set=fa]Add**. Enter the appropriate attribute mappings. To use the expression builder, or to map the attribute to a literal string value, click the **Gear** icon. For more information, see [Using the expression builder](../pingone_expression_language/p1_use_expression_builder.html). |
   | To designate the attribute as required | Select the **Required** check box.                                                                                                                                                                                                                                                                               |
   | To delete an attribute mapping         | Click the **Delete** icon.                                                                                                                                                                                                                                                                                       |

7. Click **Next**.

8. For **Select Groups**, enter the name of the groups that you want to have access to the application.

   |   |                                                                                                                           |
   | - | ------------------------------------------------------------------------------------------------------------------------- |
   |   | By default, all users have access to the application. Assigning groups restricts application access to only those groups. |

9. Click **Save**.

   ### Result:

   The application is now configured for PingOne. You might have to perform additional configuration on the application side.

## Next steps

To see applications that have already been configured, click the **Configured** tab on the **Application Catalog** page.

On the **Connection Details** page, you can download or copy metadata required by the application for single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)* configuration.

This information includes:

* PingOne metadata

* The PingOne signing certificate

* The PingOne Issuer ID Uniform Resource Locator (URL) *(tooltip: \<div class="paragraph">
  \<p>Identifies a resource according to its internet location.\</p>
  \</div>)*

* The PingOne SSO Service URL

* The PingOne identity provider (IdP) *(tooltip: \<div class="paragraph">
  \<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
  \</div>)* Metadata URL

* The PingOne Initiate SSO URL

After you configure the application, you can manage it at **Applications > Applications**. For more information about advanced settings, see [Editing an application](p1_editing_applications.html).

---

---
title: Adding an application
description: Add applications to your environment so that PingOne can manage access to the applications.
component: pingone
page_id: pingone:applications:p1_applications_add_applications
canonical_url: https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 23, 2026
page_aliases: ["p1_enable_application.adoc"]
section_ids:
  steps: Steps
  choose-from: Choose from:
  next-steps: Next steps
---

# Adding an application

Add applications to your environment so that PingOne can manage access to the applications.

Use the **Applications** page to add an application to be managed by PingOne. Learn more about the different types of applications in [Applications](p1_application_types.html).

|   |                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Some application settings can only be configured after the application is created. Learn more in [Editing an application](p1_editing_applications.html). |

PingOne supports the following application types:

* SAML

* OIDC

* Native

* Single page

* Device authorization

* Worker

|   |                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To use a templated service provider integration instead of creating a new application, go to the **Application Catalog**. Learn more in [Application catalog](p1_application_catalog.html). |

## Steps

1. In the PingOne admin console, go to **Applications > Applications**.

2. Click the **[icon: plus, set=fa]**icon.

3. Create the application profile by entering the following:

   * **Application Name**: A unique identifier for the application. The maximum name length is 256 characters.

   * **Description** (optional): A brief description of the application.

   * **Icon** (optional): An image that represents the application. Use a file up to 1 MB in JPG, JPEG, GIF, or PNG format.

4. Choose the **Application Type**. Learn more in [Applications](p1_application_types.html).

5. If you're creating a **SAML Application**, click **Configure**, and then specify the details of the connection between the application and PingOne.

   You can enter the values manually, or import them from a file or URL.

   ### Choose from:

   * **Import Metadata**: Select to import the configuration details from an XML metadata file.

     1. Click **Select a File** and then choose an XML metadata file on your file system.

     2. Click **Open**.

        The configuration values are populated based on the information in the metadata file.

        |   |                                                                                                                |
        | - | -------------------------------------------------------------------------------------------------------------- |
        |   | If the metadata file doesn't specify all the configuration values, you must enter the missing values manually. |

   * **Import from URL**: Select to import the configuration details from a metadata URL.

     1. Enter the URL and then click **Import**.

        |   |                                       |
        | - | ------------------------------------- |
        |   | The URL must be a valid absolute URL. |

        The configuration values are populated based on the information from the URL.

   * **Manually Enter**: Select to enter the configuration details manually.

     1. In the **ACS URLs** field, enter the Assertion Consumer Service (ACS) URLs. You must specify at least one URL, and the first URL in the list is used as the default.

     2. In the **Entity ID** field, enter the service provider entity ID used to look up the application. The **Entity ID** is a required property and is unique within the environment.

6. Click **Save**.

7. To enable the application, click the toggle at the top of the details panel to the right (blue).

   You can disable the application by clicking the toggle to the left (gray).

## Next steps

After the application is created, you can edit the application settings, configure application policies, and control application access. Learn more in:

* [Editing an application](p1_editing_applications.html)

* [Applying authentication policies to an application](p1_apply_auth_policy_to_applications.html)

* [Application access control](p1_application_access_control.html)

---

---
title: Adding an application from the application catalog
description: Use the PingOne application catalog to configure single sign-on (SSO) for popular applications.
component: pingone
page_id: pingone:applications:p1_applicationcatalog
canonical_url: https://docs.pingidentity.com/pingone/applications/p1_applicationcatalog.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 29, 2025
section_ids:
  steps: Steps
  choose-from: Choose from:
  result: Result:
  next-steps: Next steps
---

# Adding an application from the application catalog

Use the PingOne application catalog to configure single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)* for popular applications.

## Steps

1. In PingOne admin console, go to **Applications > Application Catalog** and browse or search for applications.

2. Click the application entry to open the details panel.

3. For **Quick Setup**, enter the following information:

   * To change the application name, enter a new name in the **Name** field.

     |   |                                                                                                                                |
     | - | ------------------------------------------------------------------------------------------------------------------------------ |
     |   | The application name must be unique, and cannot be the same as any applications configured at **Applications > Applications**. |

   * To change the icon for the application, click the icon image and select a new file.

     |   |                                                                                                                       |
     | - | --------------------------------------------------------------------------------------------------------------------- |
     |   | Some applications require additional configuration inputs, such as **AccountID**, **Domain Name**, or **Vanity URL**. |

4. Click **Next**.

5. For **Map Attributes**, set up user attribute mapping from the application to PingOne.

   |   |                                                                                                                                                                                                              |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | The required attributes for each application are pre-populated. In most cases, you won't need to alter the mappings.Required attributes must be mapped before you can proceed to the next configuration tab. |

   ### Choose from:

   * To change the attribute mapping, enter or select a new attribute in the **PingOne Mappings** list.

   * To designate the attribute as required, select the **Required** checkbox.

   * To use the expression builder or map the attribute to a literal string value, click the **Gear** icon. Learn more in [Using the expression builder](../pingone_expression_language/p1_use_expression_builder.html).

   * To delete an attribute mapping, click the **Delete** icon.

6. (Optional) To add a new attribute:

   1. Click **[icon: plus, set=fa]Add**.

   2. In the application field for the new attribute, enter the name of the attribute as it appears in the application.

   3. In the **PingOne Mappings** field for the new attribute, enter or select the PingOne attribute to map to.

      To use the expression builder or map the attribute to a literal string value, click the **Gear** icon. Learn more in [Using the expression builder](../pingone_expression_language/p1_use_expression_builder.html).

7. When you're finished mapping attributes, click **Next**.

8. For **Select Groups**, specify the groups that you want to have access to the application.

   |   |                                                                                                                           |
   | - | ------------------------------------------------------------------------------------------------------------------------- |
   |   | By default, all users have access to the application. Assigning groups restricts application access to only those groups. |

   Learn more in [Groups](../directory/p1_groups.html).

9. Click **Save**.

   ### Result:

   The application is now configured for PingOne. There may be additional configuration necessary on the application side.

10. To see applications that have already been configured, click the **Configured** tab.

11. On the **Overview** tab, download or copy information required by the application to complete the SSO configuration.

    This information includes the following PingOne details:

    * Metadata

    * Signing certificate

    * **Issuer ID** URL

    * **Initiate Single Sign-on URL**

    * **Single Signon Service** URL

    * **IdP Metadata URL**

## Next steps

After you configure the application, you can manage it from **Applications > Applications**.

To configure advanced application settings, go to the **Configuration** tab for the application to see all application settings, including but are not limited to:

* **ACS URLs**: The Assertion Consumer Service URLs.

* **Signing key**: The certificate that confirms that requests, responses, and assertions actually came from the application.

* **Entity ID**: The service provider (SP) entity ID used to look up the application.

* **SLO endpoint**: The SAML single logout endpoint URL.

* **Subject NameID format**: A string that specifies the format of the `Subject NameID` attribute in the SAML assertion.

Learn more about advanced settings in [Editing an application](p1_editing_applications.html).

---

---
title: Adding application permissions
description: Define application permissions by assigning actions to custom resources in PingOne.
component: pingone
page_id: pingone:applications:p1_add_application_permissions
canonical_url: https://docs.pingidentity.com/pingone/applications/p1_add_application_permissions.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 10, 2025
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Adding application permissions

Define application permissions for the application resources that you want to protect.

## Before you begin

* [Add PingOne Authorize to your environment](../authorization_using_pingone_authorize/p1az_adding_p1az_service_to_your_environment.html).

* [Add a custom resource](p1_adding_custom_resource.html) for your protected endpoints.

## About this task

Application resources are features that users want to access, such as checking and savings accounts, an investment services add-on, or an invoicing module in a business application.

|   |                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingOne platform resources, such as identities and PingOne APIs, are protected by PingOne platform roles and permissions. Application resources protect access to resources that are developed by your organization's engineering teams. |

An [application permission](p1_application_permissions.html) is the combination of an action and a resource. Think of permissions as actions that can be taken on a resource. Configure application permissions by assigning actions to application resources.

|   |                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------- |
|   | You can add up to 128 application resources and 128 application permissions in each PingOne environment. |

For example, consider a business application called BizPro that has invoicing capabilities. Endpoints for the associated invoicing API allow the following actions on the `invoices` resource:

* Read invoices: `GET /bizpro/invoices`

* Create an invoice: `POST /bizpro/invoices`

* Update an invoice: `PUT /bizpro/invoices/\{{invoiceId}}`

* Pay an invoice: `POST /bizpro/invoices/\{{invoiceId}}/pay`

* Void an invoice: `POST /bizpro/invoices/\{{invoiceId}}/void`

To control access to invoices, you create corresponding application permissions:

* `Invoices:Read`

* `Invoices:Write`

* `Invoices:Update`

* `Invoices:Pay`

* `Invoices:Void`

## Steps

1. Go to **Applications > Resources** and browse or search for the custom resource for your protected endpoints.

2. Click the custom resource to open the details pane, then click the **Permissions** tab.

3. (Optional) To include user permissions in access tokens created for this custom resource, click the **Include user permissions in Access Token** toggle.

   Permissions for the authenticated user are included in the `p1.permissions` claim in the access token.

   ![Screen capture showing the Include user permissions in Access Token toggle and the + Add Permissions button on the Permissions tab.](_images/yxw1705001938848.png)

   |   |                                                                                                                                                                                                            |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If your organization requires a large number of permissions, consider using permissions-based rules for permissions enforcement. Learn more in [Application permissions](p1_application_permissions.html). |

4. Click **[icon: plus, set=fa]Add Permissions**.

5. To create an application resource, enter a unique **Name** and an optional **Description**. Click **Next**.

   ![Screen capture showing the Name and Description fields in the Create Application Resource window.](_images/for1705002092070.png)

   |   |                                                                                                                                                                     |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The name can include Unicode letters, marks, numbers, spaces, forward slashes, dots, apostrophes, underscores, and hyphens, with a maximum length of 20 characters. |

6. Configure permissions for the application resource:

   1. Click **[icon: plus, set=fa]Add** to add an **Action** that you want to protect with a permission.

      |   |                                                                                 |
      | - | ------------------------------------------------------------------------------- |
      |   | The action can include Unicode letters, with a maximum length of 20 characters. |

   2. (Optional) Enter a **Description** for the action.

      ![Screen capture showing the Application Resource, Action, and Description columns in the Configure Permission window.](_images/gng1705002320734.png)

   3. To add more actions, click **[icon: plus, set=fa]Add**.

7. Click **Save**.

## Next steps

Add application roles to simplify the assignment of application permissions to users. For example, David, an invoicing processor, might have permissions to create and pay invoices, while Melissa, the billing supervisor, can view and void invoices. Learn more in [Adding an application role](../authorization_using_pingone_authorize/p1_az_adding_application_roles.html).

---

---
title: Adding Microsoft 365 to allow users to sign on using PingOne
description: Use the application catalog in PingOne to add Microsoft 365 to your application portal.
component: pingone
page_id: pingone:applications:p1_adding_microsoft_365
canonical_url: https://docs.pingidentity.com/pingone/applications/p1_adding_microsoft_365.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 21, 2025
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  choose-from: Choose from:
  next-steps: Next steps
---

# Adding Microsoft 365 to allow users to sign on using PingOne

Use the application catalog to add Microsoft 365 to your application portal and connect the application to a Microsoft Entra ID domain.

PingOne supports the Microsoft 365 passive and active profiles for single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)*:

* Passive profile

  Passive profile enables web browser SSO, where Microsoft 365 redirects the user's browser to PingOne for authentication, and the user provides their PingOne credentials.

  If the PingOne environment is configured with an [LDAP gateway](../integrations/p1_ldap_gateways.html), PingOne can validate the credentials against an on-premise LDAP server, such as Microsoft Active Directory (AD). If the LDAP gateway is configured with [Kerberos authentication](p1_enabling_kerberos_authentication.html), the user can sign on seamlessly to Microsoft 365 using the Kerberos protocol.

* Active profile

  Active profile allows an application to collect the user's credentials and initiates an exchange with PingOne for a security token. The exchange uses the WS-Trust protocol to allow the user to access Microsoft 365.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you plan to set up hybrid join to join users and devices to existing on-premise AD deployments and sync them in the cloud with Microsoft Entra ID now or later, follow the steps in [Setting up PingOne as the federated IdP for Microsoft Entra ID](../use_cases/p1_microsoft_entra_hybrid_join.html). You can configure PingOne to allow users to sign on to Microsoft 365 now and then complete the hybrid join configuration at a later time. |

## Before you begin

You must have a Microsoft Azure account with a custom domain configured in Microsoft Entra ID as either of the following:

* Managed domain, where Entra ID is the identity provider (IdP) *(tooltip: \<div class="paragraph">
  \<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
  \</div>)* and manages authentication. In step 12, you'll change the domain to a federated domain and set up PingOne as the federated IdP for this domain.

* Federated domain, where Entra ID redirects users to a federated IdP for authentication. In step 12, you'll update Entra ID to use PingOne as the federated IdP for this domain.

Learn more about domains in [Managing custom domain names](https://learn.microsoft.com/en-us/entra/identity/users/domains-manage) in the Entra ID documentation.

|   |                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Each Microsoft 365 custom domain requires a unique `IssuerURI` value. To set up PingOne as the federated IdP for multiple domains, you must add a Microsoft 365 application for each domain. |

## Steps

1. In the PingOne admin console, go to **Applications > Application Catalog**.

2. In the **Search for applications** bar, enter `Microsoft 365`.

3. Click the **Microsoft 365** entry to open the details panel.

4. On the **Quick Setup** page, review the following:

   * **Name** (optional): Enter a new name to replace the default application name.

   * **Icon** (optional): Select a new image to replace the default application icon.

   * **Domain Name**: Enter the `<Custom Domain>` value from your Entra ID account. You can find your \<Custom Domain> in the Microsoft Entra admin center by going to **Identity > Settings > Domain Names**.

   * **Subject NameIdentifier Format**: Select the value in the list to use for the `Subject NameIdentifier` attribute in the WS-Federation security token.

     Possible values are `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress` (default) or `urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified`.

     |   |                                                                                                               |
     | - | ------------------------------------------------------------------------------------------------------------- |
     |   | If the application is already configured, click **View in Applications list** to view the full configuration. |

5. Click **Next**.

6. On the **Map Attributes** page, select the PingOne attributes to map to the required `ImmutableID`, `Subject`, and `UPN` Microsoft 365 attributes.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | **ImmutableID** uniquely identifies a user in Entra ID. You can find the **ImmutableID** value by running the `Get-MgUser` command in PowerShell after you configure federation with Entra ID. Learn more about [Get-MgUser](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.users/get-mguser) in the Microsoft documentation.For **Subject**, the mapping attribute defaults to **Email Address** but can be configured to a different value.For **UPN**, use an email address with a domain name that matches the domain name registered with Microsoft 365. |

   * If your user identities are stored in the PingOne Directory, use the default mapping of `ImmutableID` to `ExternalID`. `ExternalID` is the user's **User ID** in PingOne.

   * If the Microsoft 365 users are migrated into PingOne from Entra ID through the LDAP gateway, and the source of the `ExternalID` is `objectGUID` or `ms-DS-ConsistencyGuid`, add an expression to the mapping configuration:

     1. Locate the `ImmutableID` mapping.

     2. Click the **Gear** icon ([icon: gear, set=fa]) to open the **Advanced Expression** modal.

     3. Enter the following expression:

        ```
        #string.uuidAsBase64Guid(user.externalId,null)
        ```

        Learn more in [Using `ms-DS-ConsistencyGuid` as `sourceAnchor`](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/plan-connect-design-concepts#using-ms-ds-consistencyguid-as-sourceanchor) in the Entra ID documentation.

     4. Click **Save**.

   * To create a custom PingOne user attribute instead of using `ExternalID`, map `objectGUID` or `ms-DS-ConsistencyGuid` as the attribute source:

     1. Locate the `ImmutableID` mapping.

     2. Click [icon: gear, set=fa]to open the **Advanced Expression** modal.

     3. Enter the following expression:

        ```
        #string.uuidAsBase64Guid(user.customAttrName,null)
        ```

        where `customAttrName` represents the custom PingOne user attribute. You can also replace `null` with a custom value, such as an error.

     4. Click **Save**.

7. Click **Next**.

8. On the **Select Groups** page, click the name of the user groups that you want to have access to the application.

   You can browse or search for groups. Click the **Added** tab to see the groups that currently have access to the application.

   |   |                                                                                                                           |
   | - | ------------------------------------------------------------------------------------------------------------------------- |
   |   | By default, all users have access to the application. Assigning groups restricts application access to those groups only. |

9. Click **Save**.

10. Click the **View in Applications list** link.

11. On the **Overview** tab, locate the **Microsoft Graph PowerShell cmdlets**.

12. Copy the PowerShell cmdlets to configure PingOne as the federated IdP:

    ### Choose from:

    * **Entra managed domain**: Set up identity federation settings for the first time to use PingOne as the IdP:

      1. Locate the **Microsoft Graph PowerShell cmdlets**.

      2. Click the **Copy to clipboard** icon ([icon: copy, set=fa]) for the appropriate section.

    * **Entra federated domain**: Update existing identity federation settings to use PingOne as the IdP:

      1. Locate **Microsoft Graph PowerShell cmdlets**.

      2. Click [icon: copy, set=fa]for the appropriate section.

    |   |                                                                    |
    | - | ------------------------------------------------------------------ |
    |   | You might have to scroll to the right to see [icon: copy, set=fa]. |

13. Open Windows PowerShell.

14. In PowerShell, paste the copied commands and run them.

    These commands update the domain authentication in Entra ID to SSO. Learn more about the Microsoft cmdlets used in PingOne in the following topics in the Microsoft documentation:

    * [Connect-MgGraph](https://learn.microsoft.com/en-us/powershell/microsoftgraph/authentication-commands)

    * [New-MgDomainFederationConfiguration](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.identity.directorymanagement/new-mgdomainfederationconfiguration)

    * [Update-MgDomainFederationConfiguration](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.identity.directorymanagement/update-mgdomainfederationconfiguration)

15. On the **Policies** tab, click the **Pencil** icon ([icon: pencil, set=fa]) to add an authentication policy for the application.

    * If you have a DaVinci license, you can select a PingOne policy or DaVinci flow policy, but not both. If you don't have a DaVinci license, you'll see PingOne policies only.

    * To add a PingOne authentication policy, click the **PingOne Policies** tab. If the application was previously configured with a DaVinci flow policy, click **Deselect all other Policies** to remove it from the application and select the PingOne authentication policy you want to apply to the application.

    * To add a DaVinci flow policy, click the **DaVinci Policies** tab. If the application was previously configured with a PingOne authentication policy, click **Deselect all other Policies** to remove it from the application and select the DaVinci flow policy you want to apply to the application.

      Learn more in [Authentication policies for applications](p1_auth_policies_for_applications.html).

16. Click **Save**.

## Next steps

* Add an MFA claim in the Microsoft 365 application to communicate to Entra ID that PingOne will handle MFA. Learn more in [Configuring an authentication claim for the Microsoft 365 application](p1_configure_authentication_claim_microsoft_365.html).

* After you configure the application, you can manage it in **Applications > Applications**.

* For passive profile sign-ons only, do the following as needed:

  * [Fine-tune the assertion validity duration](p1_fine-tuning_assertion_validity_duration.html).

  * [Set the WS-Trust version](p1_setting_ws-trust_version.html).

---

---
title: Adding non-application-portal applications
description: Add applications to PingOne that are excluded from the Application Portal.
component: pingone
page_id: pingone:applications:p1_external_apps_not_included_in_apps_portal
canonical_url: https://docs.pingidentity.com/pingone/applications/p1_external_apps_not_included_in_apps_portal.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2025
section_ids:
  steps: Steps
---

# Adding non-application-portal applications

You can also use the External Applications page to add applications that will not be included in the Application Portal but can be used in contexts such as [targeted risk policies](../threat_protection_using_pingone_protect/p1_protect_risk_policies.html):

## Steps

1. Go to **Applications > External Applications**.

2. Click the **[icon: plus, set=fa]**icon to add a new application.

3. Enter the name to display for the application.

4. In the **External Application ID** field, enter the ID to use for the application in contexts such as targeted risk policies.

5. Click **Save**.

---

---
title: Adding resource links to the application portal
description: Add links in PingOne to resources your users might find useful.
component: pingone
page_id: pingone:applications:p1_adding_resource_links_to_application_portal
canonical_url: https://docs.pingidentity.com/pingone/applications/p1_adding_resource_links_to_application_portal.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 10, 2025
section_ids:
  steps: Steps
  next-steps: Next steps
---

# Adding resource links to the application portal

You can add links to resources your users might find useful, such as status pages, user guides, and applications that aren't accessible through single sign-on (SSO). You can add a link to any resource that has a URL.

|   |                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can customize the branding and themes for the application portal. Learn more in [Configuring the application portal](p1_configuring_the_application_portal.html). |

## Steps

1. In the PingOne admin console, go to **Applications > External Applications**.

2. To add a link to a resource other than an SSO application, in the **Applications** section, click the **[icon: plus, set=fa]**icon.

3. Enter the following **Profile** details:

   * **Application Name**: The name to use for the application in the application portal. The maximum name length is 256 characters.

   * **Description** (optional): A description of the application.

   * **Icon** (optional): An image that represents the application. Use a file up to 1 MB in JPG, JPEG, GIF, or PNG format.

   * **External Application ID** (optional): If you want the application to be included in contexts such as the application list for [targeted risk policies](../threat_protection_using_pingone_protect/p1_protect_risk_policies.html), enter the target resource ID that should be used for the application.

   * Verify that **Show in the Application Portal** is selected.

   * **URL**: The URL to which the user will be directed. It must be an HTTPS URL.

4. Click **Save**.

## Next steps

You can edit the visibility settings after you create the link. The visibility settings determine which groups can access the link. Learn more in [Editing a resource link](p1_edit_a_resource_link.html).

---

---
title: Application access control
description: Use application access control to define access to PingOne applications through roles and groups.
component: pingone
page_id: pingone:applications:p1_application_access_control
canonical_url: https://docs.pingidentity.com/pingone/applications/p1_application_access_control.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 28, 2025
page_aliases: ["p1_config_app_access_control.adoc", "p1_audit_access_events.adoc"]
section_ids:
  configure_app_access: Configuring application access control
  steps: Steps
  auditing-access-events: Auditing access events
  steps-2: Steps
  next-steps: Next steps
---

# Application access control

Use application access control to define access to applications through roles and groups.

For each application, specify the conditions that must be met by an authenticating user to access an application. You can use application access control with all types of applications.

|   |                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can define application permissions to control access to custom-developed application features after users authenticate. Learn more in [Application permissions](p1_application_permissions.html). |

* Role type

  Specifies that a user with an administrator role is required to access the application. The user must have one of the following roles:

  * Organization Admin

  * Environment Admin

  * Identity Data Admin

  * Client Application Developer

  Learn more in [Administrator Roles](../directory/p1_roles.html). If no option is selected, an administrator role is not required to access the application.

* Group type

  Specifies that a user must be a member of a particular group or groups to access the application. If you have two or more groups, you can specify how group access is applied:

  * **Any**: The user must be a member of at least one of the specified groups.

  * **All**: The user must be a member of all specified groups.

  If no option is selected, group membership is not required to access the application. If an existing group is removed from the environment, then any members of the group might no longer have access to the application, depending on their other group memberships and how group evaluation is configured.

* Application portal

  Determines whether an application icon appears in the application portal, even if the user would see the application in the application portal based on the group membership policy.

  For example, you could use this option if the SSO flow is being triggered through means other than on the application portal or because you're [creating multiple application deep links](p1_adding_resource_links_to_application_portal.html) that will be shown in the application portal rather than the actual application. Learn more in [Application portal](../introduction_to_pingone/p1_introduction.html#p1-app-portal).

## Configuring application access control

Use application access control to define access to applications through roles and groups. For each application, specify the conditions that must be met by an authenticating user to access an application. You can use application access control with all types of applications.

## Steps

1. In the PingOne admin console, go to **Applications > Applications** and browse or search for the application you want to configure.

2. Click the application entry to open the details panel for the application.

3. On the **Access** tab, click the **Pencil** icon.

4. For **Admin Only Access**, to specify whether an administrator role is required to access the application, select the **Must have admin role** checkbox.

   Available roles are:

   * **Organization Admin**

   * **Environment Admin**

   * **Identity Data Admin**

   * **Client Application Developer**

     Learn more in [Administrator Roles](../directory/p1_roles.html).

5. For **Group Membership Policy**, specify the groups that can access the application by searching or browsing for the group.

   The list is updated as you enter the search criteria. Do one or more of the following:

   | Option                              | Description                                                                                                                                                                  |
   | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Add a group to the access list      | On the **Groups** tab, select the checkbox for a group name to add it to the **Applied Groups** list.                                                                        |
   | Remove a group from the access list | On the **Applied Groups** tab, clear the checkbox for the group name you want to remove.                                                                                     |
   | Require any group membership        | If you apply two or more groups, select **User is a member of any applied group** to require the user to be a member of any of the applied groups to access the application. |
   | Require all group membership        | If you apply two or more groups, select **User must be a member of all applied groups** to require the user to be a member of all applied groups to access the application.  |

   |   |                                                                                                                                |
   | - | ------------------------------------------------------------------------------------------------------------------------------ |
   |   | If you remove an existing group from the environment, then any members of the group lose access to the configured application. |

6. Click **Save**.

## Auditing access events

You can use the **Audit** page to see a summary of user access events related to application access control.

## Steps

1. In the PingOne admin console, go to **Monitoring > Audit**.

2. For **Time Range**, select the desired time span.

3. For **Filter Type**, select **Event Type**.

4. For **Filter**, select one of the following:

   * **User Access Allowed**: The user accessed the resource successfully.

   * **User Access Denied**: The user was denied access to the resource.

5. Click **Run**.

## Next steps

* In the **Activities** list, see the **Description** column for specific events.

* In the **Details** column, click **View** to see more detailed information about the event.

---

---
title: Application catalog
description: Use the PingOne Application catalog to find and configure applications from service providers.
component: pingone
page_id: pingone:applications:p1_application_catalog
canonical_url: https://docs.pingidentity.com/pingone/applications/p1_application_catalog.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 10, 2025
---

# Application catalog

The Application catalog contains popular applications that service providers have made available through PingOne.

After selecting an application from the catalog, follow the configuration instructions to add the application and make it available to your users.

---

---
title: Application permissions
description: Application permissions allow you to control the types of actions that users can perform in your applications and APIs.
component: pingone
page_id: pingone:applications:p1_application_permissions
canonical_url: https://docs.pingidentity.com/pingone/applications/p1_application_permissions.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 5, 2025
section_ids:
  resources-and-permissions: Resources and permissions
  configuring-application-permissions: Configuring application permissions
  enforcing-permissions: Enforcing permissions
  p1-permissions-access-tokens: Permissions claim in access tokens
  permissions-based-rules: Permissions-based rules
  extending-access-control: Extending access control
---

# Application permissions

Application permissions allow you to control the types of actions that users can perform in your applications and APIs.

To implement access control based on permissions, commonly known as [role-based access control (RBAC)](https://www.pingidentity.com/en/resources/identity-fundamentals/authorization/authorization-methods.html), define permissions for application features, then group these permissions into roles. Assigning roles to users grants access to features and API resources.

Application permissions and roles in PingOne help you centralize access control, making it easier to quickly and repeatedly assign permissions to users and adjust them as your business needs change.

|   |                                                                                      |
| - | ------------------------------------------------------------------------------------ |
|   | To use application permissions, you must have PingOne Authorize in your environment. |

## Resources and permissions

Applications are built on top of APIs, and application features are often represented as API operations. Accordingly, you define permissions against an API. **Application resources** are the things that you want to protect in your API or application.

An **application permission** specifies an action that a user can perform on an application resource. For example, if you have an invoicing application, you might define an invoice resource with permissions to view, create, pay, and void invoices. Learn more about this scenario in [Adding application permissions](p1_add_application_permissions.html).

## Configuring application permissions

Complete the following steps to configure application permissions:

1. [Add PingOne Authorize to your environment](../authorization_using_pingone_authorize/p1az_adding_p1az_service_to_your_environment.html).

2. [Add application permissions to a custom API resource](p1_add_application_permissions.html).

3. [Add application roles](../authorization_using_pingone_authorize/p1_az_adding_application_roles.html). This includes assigning permissions to roles, and then assigning roles to users.

## Enforcing permissions

To enable your application to retrieve and enforce permissions, you can include the permissions claim in access tokens or use permissions-based rules.

### Permissions claim in access tokens

To include permissions in access tokens, enable the **Include user permissions in Access Token** toggle on the **Permissions** tab for a custom resource. When the toggle is enabled, the `p1.permissions` claim is included in access tokens scoped to the custom resource.

* When an OAuth 2.0 client application requests an access token on behalf of a user, the claim is populated with the authenticated user's permissions. The application must be scoped to the custom resource. Permissions are not included in tokens obtained through the Client Credentials grant type.

* The claim is empty if the authenticated user isn't assigned to a role that has application permissions.

A resource server can use this JWT claim to identify the token holder's permissions in order to make authorization decisions.

|   |                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `p1.permissions` claim increases access token size and the time required to generate a token. Use this type of permissions enforcement only if your organization doesn't require a large number of permissions. |

The `p1.permissions` claim contains an array of strings. Each member of the array is a permission key, such as `invoices:read`. For example, consider a business application called BizPro that has invoicing capabilities. A decoded token for a BizPro user with permissions to read, write, and pay invoices looks something like this:

```json
{
  "aud": [
    "BizPro Invoices API"
  ],
  "client_id": "2be7e2f8-02d8-46ca-9ebb-35e129a78452",
  "exp": 1702659466,
  "iat": 1702655866,
  "iss": "https://auth.pingone.com/672e060d-e6c9-49d9-81b8-22ac46e55c85/as",
  "p1.permissions": [
    "invoices:read",
    "invoices:write",
    "invoices:pay"
  ],
  "scope": "bizpro:invoices",
  "sid": "d11d5eb0-b2cb-4674-b4ef-2cdc211d379c",
  "sub": "c52cc34d-2f29-442d-adf8-00fc89f7bbd8"
}
```

You can use the token introspection endpoint to return information about claims in the access token. Learn more in the [Token Introspection](https://developer.pingidentity.com/pingone-api/auth/openid-connect-oauth-2/token-introspection-access-token.html) API reference documentation.

### Permissions-based rules

If your organization has more extensive use cases that require a large number of permissions, you can define permissions-based rules that work with your API gateway to enforce entitlements.

After you configure application permissions, complete the following steps to define permissions-based rules for permissions enforcement:

1. [Connect your API gateway to PingOne](../authorization_using_pingone_authorize/p1az_api_gateway_is.html).

2. [Register the API](../authorization_using_pingone_authorize/p1az_add_api_service.html) in order to enforce permissions.

3. [Define access control rules for API operations](../authorization_using_pingone_authorize/p1az_add_api_service_operations.html).

## Extending access control

When your organization's access control needs progress beyond static permissions, you can leverage real-time contextual information in your access control decisions. Fine-grained authorization policies can factor in a range of contextual attributes, such as user characteristics, risk signals, and environment properties such as location and time.

You can use PingOne's API Access Management custom policy capabilities in conjunction with application permissions to satisfy these access control requirements. Learn more in [API services](../authorization_using_pingone_authorize/p1az_api_services.html).

---

---
title: Application portal
description: The PingOne application portal shows the applications accessible to users through single sign-on (SSO) based on their group memberships.
component: pingone
page_id: pingone:applications:p1_application_portal_showing_applications
canonical_url: https://docs.pingidentity.com/pingone/applications/p1_application_portal_showing_applications.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 21, 2025
---

# Application portal

The application portal shows the applications accessible to users through single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)* based on their group memberships. This includes SAML applications and OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)* applications that have the `Initiate Login URI` configured. The applications that a user sees depend on the access controls for that application. Learn more in [Adding an application](p1_applications_add_applications.html).

|   |                                                                                                                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | To make an OIDC application available in the application portal, the application must have an `Initiate Login URI` configured. To add the URI to an existing application, go to the application's **Configuration** tab and enter the URI in the **Initiate Login URI** field. Learn more in [Editing an application - OIDC](p1_edit_application_oidc.html). |

You can also add links to other resources your users might find useful, such as status pages, user guides, and applications that aren't accessible through SSO, and select the sign-off method that PingOne uses when users sign off from the application portal. Learn more in [Configuring the application portal](p1_configuring_the_application_portal.html).

---

---
title: Applications
description: Learn about the application types supported in PingOne.
component: pingone
page_id: pingone:applications:p1_application_types
canonical_url: https://docs.pingidentity.com/pingone/applications/p1_application_types.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 26, 2025
---

# Applications

You can add applications to your environment so that PingOne can manage access to the applications.

When you add an application, PingOne creates a client ID for the application, which is a unique identifier for the application and cannot be changed.

|   |                                                                                     |
| - | ----------------------------------------------------------------------------------- |
|   | To enable or disable an application, click the toggle in the **Applications** list. |

PingOne supports several application types. Use the application type that best fits your requirements.

* SAML application

  A browser-based application with a server-side component, such as .NET web apps, JSP/Java, Node.js, or Ruby on Rails. SAML applications typically have functions similar to desktop applications, and use SAML for authentication.

  * [Adding an application](p1_applications_add_applications.html)

  * [Editing an application - SAML](p1_edit_application_saml.html)

* OIDC Web application

  A browser-based application with a server-side component, such as .NET web apps, JSP/Java, Node.js, or Ruby on Rails. OIDC web applications typically have functions similar to desktop applications, and use OIDC for authentication.

  * [Adding an application](p1_applications_add_applications.html)

  * [Editing an application - OIDC](p1_edit_application_oidc.html)

* Native application

  An application that's installed and run directly on the local operating system, like Java, Objective-C, Swift, or React. Native applications are typically intended for mobile devices. Native applications use OIDC for authentication. A native application can be used as both an accessing application and as an authenticating application for MFA.

  * [Adding an application](p1_applications_add_applications.html)

  * [Editing an application - Native](p1_edit_application_native.html)

* Single page application

  A browser-based application that runs on the front-end with no server-side component, such as Sencha Touch, AngularJS, and React. A single page application runs on the client side after it loads, so it can't keep a client secret. Single page applications use OIDC for authentication.

  * [Adding an application](p1_applications_add_applications.html)

  * [Editing an application - Single page](p1_edit_application_singlepage.html)

* Device authorization

  An application that allows a device to obtain authorization from the user through a second device, such as a smartphone. Device authorization is typically used for applications that run on an input-constrained, Internet-connected device, such as a smart TV.

  * [Adding an application](p1_applications_add_applications.html)

  * [Editing an application - Device authorization](p1_edit_application_device_auth.html)

* Worker

  An administrator application that can have the same roles as human administrators. Worker applications are configured with the client credentials grant type by default, but can be configured to support multiple grant/response types, just like the other application types. Worker applications use OIDC for authentication.

  You can use Worker applications to create a userless service application that can perform administrator functions. The role assignments determine which functions the application can do. The Worker application can also perform administrator functions with the role of its user. To do this, give the application an additional grant type, which is used instead of the role assignments.

  Worker applications can use a user-based grant type (`implicit` or `authorization_code`). With this configuration, you can assign only OIDC scopes to the application. When getting a token using a user-based grant type, the user's role assignments are used. When getting a token using the `client_credentials` grant type, the application's role assignments are used.

  |   |                                                                                                                   |
  | - | ----------------------------------------------------------------------------------------------------------------- |
  |   | Worker apps can't be used to facilitate end-user sign-ons, but they can be used to sign on users that have roles. |

  * [Adding an application](p1_applications_add_applications.html)

  * [Editing an application - Worker](p1_edit_application_worker.html)

---

---
title: Applications
description: The Applications in PingOne contains the Applications, Application Catalog, Resources, and External Applications pages.
component: pingone
page_id: pingone:applications:p1_applications_menu
canonical_url: https://docs.pingidentity.com/pingone/applications/p1_applications_menu.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 23, 2026
page_aliases: ["getting_started_with_pingone:p1_mfa_creating_a_native_app.adoc"]
---

# Applications

The **Applications** section contains the following:

* [Applications](p1_application_types.html)

* [Application catalog](p1_application_catalog.html)

* [Resources](p1_resources.html)

* [External applications](p1_external_applications.html)

---

---
title: Applying authentication policies to an application
description: Authentication policies define sign-on requirements for accessing an application in PingOne.
component: pingone
page_id: pingone:applications:p1_apply_auth_policy_to_applications
canonical_url: https://docs.pingidentity.com/pingone/applications/p1_apply_auth_policy_to_applications.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 23, 2025
section_ids:
  before-you-begin: Before you begin
  steps: Steps
---

# Applying authentication policies to an application

Authentication policies define sign-on requirements for accessing an application.

## Before you begin

Add an authentication policy in PingOne. Learn more in [Adding an authentication policy](../authentication/p1_add_an_auth_policy.html) and [Authentication policies](../authentication/p1_authenticationpolicies.html).

|   |                                                                                                                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The PingOne admin console uses a system policy configured in **Settings > Administrator Security** instead of the default authentication policy. You can't assign a different policy to the admin console.Learn more in [Administrator security](../settings/p1_administrator_security.html). |

## Steps

1. In the PingOne admin console, go to **Applications > Applications** and browse or search for the application you want to edit.

2. Click the application entry to open the **Details** panel.

3. On the **Policies** tab, click the **Pencil** icon.

4. Select the applicable tab and then select the checkboxes for the policies that you want to apply:

   * **DaVinci Policies** tab: Displays flow policies that you can apply to the application if you have a DaVinci license. If you don't have a DaVinci license, this tab isn't displayed. This tab includes policies built in DaVinci as well as those created in the **Design Center**. Learn more in [Flow Policies](https://docs.pingidentity.com/davinci/applications/davinci_flow_policies.html) in the DaVinci documentation and in the [Design Center](../orchestration/p1_design_center_experiences.html) documentation.

   * **PingOne Policies** tab: Displays PingOne policies that you can apply to the application.

     |   |                                                                                                                                                                                                                        |
     | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | You can select a maximum of 20 policies, and the policies are applied in the order listed on the **Selected Policies** tab.You can assign either DaVinci policies or PingOne policies to an application, but not both. |

     ![A screen capture showing the Edit policies page](_images/p1-apps-assign-auth-policy-to-app.png)

5. (Optional) Go to the **Selected PingOne Policies** or **Selected DaVinci Policies** tab and drag and drop the policies to change the order in which they are applied.

   |   |                                                                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | There is only one **Selected Policies** tab. The tab name displayed depends on whether you are using DaVinci flow policies or PingOne policies. |

6. Click **Save**.

---

---
title: Applying authentication policies to the application portal
description: The application portal in PingOne is an OIDC-based application.
component: pingone
page_id: pingone:applications:p1_apply_application_portal_policy
canonical_url: https://docs.pingidentity.com/pingone/applications/p1_apply_application_portal_policy.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 27, 2025
section_ids:
  steps: Steps
  result: Result
  next-steps: Next steps
---

# Applying authentication policies to the application portal

The application portal itself is an OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)*-based application. Like other OIDC-based applications, you can configure an authentication policy for the application portal.

The authentication policy defines the sign-on requirements for accessing the application.

* Default domain

  By default, the application portal **Home Page URL** is https\://apps.pingone.\<geography>/\<envId>/myapps/

* Custom domain

  If you use a custom domain, the **Home Page URL** is https\://\<customDomain>/myapps/

Learn more about how authentication policies are evaluated in [Authentication policies for applications](p1_auth_policies_for_applications.html).

To apply authentication polices to the application portal:

## Steps

1. In the PingOne admin console, go to **Applications > Applications** and click the **PingOne Application Portal** application to open the details panel.

2. On the **Policies** tab, click the **Pencil** icon ([icon: pencil, set=fa]).

3. Select the policy that you want to apply.

4. Click **Save**.

## Result

PingOne applies the selected policies to the **PingOne Application Portal** application. Learn more about how authentication policies are evaluated in [Authentication policies for applications](p1_auth_policies_for_applications.html).

## Next steps

To control which authentication policy is used when users access the portal, append the `policy` HTTP request parameter to the end of the URL for the application when you share the URL with users.

For example, the application portal is configured with three authentication policies named One, Two, and Three, and the policies are listed in that order on the **Policies** tab. You want a certain group of users to use policy Two when accessing the portal. Before you share the URL for the portal with these users, append the `policy` parameter to the URL as follows:

* If you're using the default domain

  https\://apps.pingone.\<geography>/\<envId>/myapps/**?policy=Two**

* If you're using a custom domain

  https\://\<customDomain>/myapps/**?policy=Two**

|   |                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------- |
|   | To use a PingOne DaVinci flow policy instead of an authentication policy, use the policy ID for the `policy` parameter value. |

If the policy name or ID doesn't match any configured policy, then PingOne returns an error.

---

---
title: Associating an authentication policy with a web app
description: Associate an MFA sign-on policy with a web application in PingOne.
component: pingone
page_id: pingone:applications:p1_mfa_associating_sign_on_policy_with_web_app
canonical_url: https://docs.pingidentity.com/pingone/applications/p1_mfa_associating_sign_on_policy_with_web_app.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 12, 2024
section_ids:
  associating-your-authentication-policy-with-your-web-app-console: Associating your authentication policy with your web app console
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  example: Example:
  next-steps: Next steps
  associating-your-authentication-policy-with-your-web-app-api-alternative: Associating your authentication policy with your web app API alternative
  about-this-task-2: About this task
  steps-2: Steps
  next-steps-2: Next steps
---

# Associating an authentication policy with a web app

Depending on the sensitivity of information and processing capabilities of each application, an organization can determine that multi-factor authentication (MFA) requirements for some applications are more stringent than for others.

PingOne provides the capability to define multiple MFA sign-on policies. You can configure one application to use a particular sign-on policy and another application to use a different policy.

The authentication flow is configured at the application level through a sign-on policy. If you don't assign a sign-on policy to your web application, it uses the environment's default sign-on policy. You can create multiple sign-on policies and associate them with different OpenID Connect (OIDC) applications.

You can also associate multiple sign-on policies with a single application. Policies are applied in the order in which they appear in the list. PingOne evaluates the first policy in the list first. If the requirements of the policy are not met, PingOne moves to the next policy in the list.

* Console

* API alternative

## Associating your authentication policy with your web app console

### Before you begin

Before assigning your authentication policy with a web app, first create the application. Learn more in [Configuring web applications](p1_strong_auth_configuring_web_apps.html).

### About this task

You can find information about how to perform this task from the API in [POST: Create SOP Assignment](https://developer.pingidentity.com/pingone-api/platform/applications/application-sign-on-policy-assignments/create-sop-assignment.html).

### Steps

1. Go to **Applications > Applications**.

2. Locate your web application and click it to open the details panel.

3. Click the **Policies** tab.

4. Click the **Pencil** icon to enter edit mode.

5. In the **PingOne Policies** list, locate the policy you created in the previous step.

   #### Example:

   For example, **MFA-only**.

6. Select the checkbox for the appropriate policy.

7. Click **Save**.

### Next steps

[Create a user](../directory/p1_adduser.html)

## Associating your authentication policy with your web app API alternative

### About this task

Application developers can use the API operations to associate a sign-on policy with an application.

### Steps

* Use the access token generated through the worker app and the following `POST` operation to assign the new authentication policy to an application:

  ```
  POST https://api.pingone.com/v1/environments/{{envId}}/applications/{{appID}}/signOnPolicyAssignments
  ```

  See [POST: Create SOP Assignment](https://developer.pingidentity.com/pingone-api/platform/applications/application-sign-on-policy-assignments/create-sop-assignment.html).

### Next steps

[Create a user](../directory/p1_adduser.html)

---

---
title: Attribute access control
description: Learn how PingOne self-management scopes control which user profile attributes are accessible.
component: pingone
page_id: pingone:applications:p1_attribute_access_control
canonical_url: https://docs.pingidentity.com/pingone/applications/p1_attribute_access_control.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 23, 2024
section_ids:
  related-links: Related links
---

# Attribute access control

Some PingOne platform self-management scopes allow organizations to specify which user profile attributes are accessible to end users.

An administrator might want to prevent end users from seeing or modifying particular attributes that should remain private, such as custom attributes for entitlements, internal foreign keys, account status information, or any profile data that should not be exposed to an individual user. With access control scopes, organizations can store additional private data in the user profile without risk that the end user can see the data.

These access control scopes designate a specific set of user attributes, which is often a subset of attributes that the user is allowed to read or update. For example, a `p1:update:user:email-only` scope could remove all other user schema attributes except the user's email address. A user with this scope could update only their email address. All other visible attributes would not allow modification.

## Related links

* [Configuring attribute access control](p1_configure_attribute_access_control.html)

---

---
title: Authentication policies for applications
description: You can configure which authentication policies should be used for a particular application in PingOne.
component: pingone
page_id: pingone:applications:p1_auth_policies_for_applications
canonical_url: https://docs.pingidentity.com/pingone/applications/p1_auth_policies_for_applications.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 23, 2025
section_ids:
  no-authentication-policy-assignments: No authentication policy assignments
  one-authentication-policy-assignment: One authentication policy assignment
  two-or-more-authentication-policy-assignments: Two or more authentication policy assignments
---

# Authentication policies for applications

You can configure which authentication policies should be used for a particular application.

An application can have zero or more associated authentication policies that determine how users are authenticated. The number of sign-on policies assigned to an application also controls how the authentication steps progress.

If you have a DaVinci license, you can select PingOne policies or DaVinci flow policies, but not both. If you don't have a DaVinci license, you can only assign PingOne policies.

|   |                                                                                                                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The PingOne admin console uses a system policy configured in **Settings > Administrator Security** instead of the default authentication policy. You can't assign a different policy to the admin console.Learn more in [Administrator security](../settings/p1_administrator_security.html). |

Policies are applied in the order in which you add them. The first policy in the list overrides any subsequent policies. The default policy is always used if no policies are applied to an application.

Learn more about assigning a sign-on policy to an application in [Applying authentication policies to an application](p1_apply_auth_policy_to_applications.html).

|   |                                                                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If an application is assigned only one authentication policy, such as the Passwordless sign-on policy, then the application uses only that policy. If the application is assigned multiple policies, it uses policies in the order they appear in the list. |

## No authentication policy assignments

Applications that aren't assigned an authentication policy use the environment's default authentication policy to authenticate users. Every environment has one authentication policy configured as its default policy. If the environment's default authentication policy changes, then the application uses the updated default policy.

## One authentication policy assignment

Applications that are assigned one authentication policy always use that policy to authenticate users. For example, if the application is assigned the `Single_Factor` authentication policy, the application always uses this basic authentication method that prompts users to enter a username and password to authenticate the account.

## Two or more authentication policy assignments

If an application is assigned two or more authentication policies, the authentication flow uses the policy with the highest priority first. If authentication is successful, the authentication flow is complete. If authentication fails, the flow initiates the authentication policy with the next highest priority. If authentication fails again, the authentication flow initiates the next authentication policy. The authentication flow continues until one of the assigned policies is completed successfully or all policies have been tried and failed.