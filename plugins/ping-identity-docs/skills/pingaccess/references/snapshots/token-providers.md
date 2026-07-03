---
title: Configure PingFederate as the token provider for PingAccess
description: This section explains how to manually configure PingAccess and PingFederate to work together, with PingAccess as the access manager and PingFederate as the token provider.
component: pingaccess
version: 9.1
page_id: pingaccess:token_providers:pa_configure_pf_as_the_token_provider_for_pa
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/token_providers/pa_configure_pf_as_the_token_provider_for_pa.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
---

# Configure PingFederate as the token provider for PingAccess

This section explains how to manually configure PingAccess and PingFederate to work together, with PingAccess as the access manager and PingFederate as the token provider.

For more information, see the following topics:

* [Configure PingFederate for PingAccess connectivity](pa_configure_pf_for_pa_connectivity.html)

* [Connect PingAccess to PingFederate](pa_connect_pa_to_pf.html)

The features documented here are affected by the settings in the configuration file. See the [Configuration file reference](../reference_guides/pa_config_file_ref.html) for more information.

---

---
title: Configure PingFederate for PingAccess connectivity
description: This section explains how to configure PingFederate for PingAccess connectivity.
component: pingaccess
version: 9.1
page_id: pingaccess:token_providers:pa_configure_pf_for_pa_connectivity
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/token_providers/pa_configure_pf_for_pa_connectivity.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
---

# Configure PingFederate for PingAccess connectivity

This section explains how to configure PingFederate for PingAccess connectivity.

This configuration procedure covers the following:

1. [Enabling PingFederate roles and protocols](pa_enabling_pf_roles_and_protocols.html)

2. [Creating a password credential validator](pa_creating_a_password_credential_validator.html)

3. [Configuring an IdP adapter](pa_configuring_an_idp_adapter.html)

4. [Defining the default scope](pa_defining_the_default_scope.html)

5. [Creating an access token manager](pa_creating_an_access_token_manager.html)

6. [Configuring an IdP adapter mapping](pa_configuring_an_idp_adapter_mapping.html)

7. [Configuring an access token mapping](pa_configuring_an_access_token_mapping.html)

8. [Creating an OpenID Connect policy](pa_creating_an_oidc_policy.html)

9. [Creating a resource server client](pa_creating_a_resource_server.html)

10. [Creating a web session client](pa_creating_a_web_session_client.html)

11. [Creating and exporting a certificate](pa_creating_and_exporting_a_certificate.html)

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | These steps assume you have installed PingFederate 10.1. If you are using an earlier version of PingFederate, the steps might differ. The example assumes that your PingFederate instance is available at https\://*\<mypingfedserver>*, using ports `9031` and `9999` respectively for the runtime and administration functions.These steps assume you have installed PingAccess 6.1. If you are using an earlier version of PingAccess, the steps might differ. This example assumes that your PingAccess instance is available at https\://*\<mypingaccessserver>* and that `3000` is the default listening port. |

---

---
title: Configuring a PingAccess application
description: Perform the following steps to configure PingAccess applications.
component: pingaccess
version: 9.1
page_id: pingaccess:token_providers:pa_configuring_a_pa_app
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/token_providers/pa_configuring_a_pa_app.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 10, 2023
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
---

# Configuring a PingAccess application

Perform the following steps to configure PingAccess applications.

## Before you begin

* Install PingAccess and verify that you can access the [administrative console](../installing_and_uninstalling_pingaccess/pa_accessing_the_admin_console.html). For information on installing PingAccess, see [Installing and Uninstalling PingAccess](../installing_and_uninstalling_pingaccess/pa_installing_and_uninstalling_pa.html).

  |   |                                                                                                                                                                               |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The default credential set should be changed upon first usage. The default credentials for your PingAccess installation are:```
  Username: Administrator
  Password: 2Access
  ``` |

* [Configure an application](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html) in PingOne.

* [Configure](pa_configuring_pa_to_use_p1_for_customers_as_the_token_provider.html) PingAccess to use PingOne as the token provider.

## About this task

For each application that you want to configure:

## Steps

1. Create a virtual host.

   For more information on creating a virtual host, see [Creating new virtual hosts](../pingaccess_user_interface_reference_guide/pa_creating_new_virtual_hosts.html).

   1. Click **Applications**, then go to **Applications > Virtual Hosts**.

   2. Click **[icon: plus, set=fa]Add Virtual Host**.

   3. In the **Host** filed, enter a name for the virtual host.

      For example: myHost.com. You can use a wildcard (`*`) to indicate that any host name is acceptable. A wildcard host can also be specified, such as `*.example.com`.

   4. In the **Port** field, enter the port number for the virtual host.

      For example: `1234`.

   5. In the **Agent Resource Cache TTL (s)** field, indicate the number of seconds the agent can cache resources for this application.

      |   |                                                |
      | - | ---------------------------------------------- |
      |   | Only applies to a destination of type `Agent`. |

   6. Click **Save**.

2. Create a web session.

   For more information on creating a web session, see [Creating web sessions](../pingaccess_user_interface_reference_guide/pa_creating_web_sessions.html).

   |   |                                                                                                                     |
   | - | ------------------------------------------------------------------------------------------------------------------- |
   |   | A web session is only used when protecting a web application. To protect APIs, configure an access token validator. |

   1. Click **Access**, then go to **Web Sessions > Web Sessions**.

   2. Click **[icon: plus, set=fa]Add Web Session**.

   3. In the **Name** field, enter a name for the web session.

   4. From the **Cookie Type** list, select your cookie type, either **Signed JWT** or **Encrypted JWT**.

   5. In the **Audience** field, enter a unique value.

   6. In the **Client ID** field, enter the PingOne client ID.

      |   |                                                                                   |
      | - | --------------------------------------------------------------------------------- |
      |   | You can find the Client ID on the **Profile** tab of the application you created. |

   7. From the **Client Credentials Type** list, select **Secret**.

   8. In the **Client Secret** field, enter the client secret found on the application's **Configuration** tab.

   9. Click **Show Advanced**.

   10. In the **Scopes** section, specify one or more scopes.

       |   |                                                                                                                                                      |
       | - | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
       |   | Ensure the scopes you specify match those configured for the PingOne application. Find the scopes on the **Access** tab of your PingOne application. |

   11. Click **Save**.

3. Create a site.

   For more information on creating a site, see [Adding sites](../pingaccess_user_interface_reference_guide/pa_adding_sites.html).

   |   |                                                                                                                                               |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | In some configurations, a site might contain more than one application. A site can be used with more than one application, where appropriate. |

   1. Click **Applications**, then go to **Sites > Sites**.

   2. Click **[icon: plus, set=fa]Add Site**.

   3. Specify a **Name** for the site.

   4. Enter the site **Target**.

      The target is the hostname:port pair for the server hosting the application. Do not enter the path for the application in this field. For example, an application at https\://mysite:9999/AppName will have a target value of `mysite:9999`.

   5. From the **Secure** list, select whether or not the target is expecting secure connections.

   6. If the target is expecting secure connections, from the **Trusted Certificate Group** list, select **Trust Any**.

   7. Click **Save**.

4. Create an application in PingAccess for each application that you want to protect.

   For more information on creating an application, see [Adding an application](../pingaccess_user_interface_reference_guide/pa_adding_an_app.html).

   1. Click **Applications**, then go to **Applications > Applications**.

   2. Click **[icon: plus, set=fa]Add Application**.

   3. In the **Name** field, enter a name for the application.

   4. In the **Description** field, optionally enter a description for the application.

   5. In the **Context Root** field, specify the context root for the application.

      For example, an application at https\://mysite:9999/AppName will have a context root of `/AppName`. If the application is on the root of the server, you can set the context root as `/`. The context root must begin with a slash (/), must not end with a slash (/), and can be more than one layer deep, for example, `/Apps/MyApp`.

   6. From the **Virtual Host** list, select the virtual host you created.

      |   |                                                                                |
      | - | ------------------------------------------------------------------------------ |
      |   | The combination of virtual host and context root must be unique in PingAccess. |

   7. From the **Application Type** list, select **Web**.

   8. From the **Web Session** list, select the web session you created.

   9. From the **Site** list, select the site you created that contains the application.

   10. Select the **Enabled** check box to enable the site when you save.

   11. Click **Save**.

---

---
title: Configuring an access token mapping
description: Configure an access token mapping that maps attributes to be requested from the OAuth resource server with the corresponding access token.
component: pingaccess
version: 9.1
page_id: pingaccess:token_providers:pa_configuring_an_access_token_mapping
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/token_providers/pa_configuring_an_access_token_mapping.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Configuring an access token mapping

Configure an access token mapping that maps attributes to be requested from the OAuth *(tooltip: \<div class="paragraph">
\<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
\</div>)* resource server with the corresponding access token.

## About this task

For more information, see [Managing access token mappings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_accesstokenmappingtasklet_oauthuserkey2accesstokenmappingstate.html).

## Steps

1. Go to **Applications → OAuth → Access Token Mapping**.

2. From the **Context** list, select **Default** or select your identity provider (IdP) *(tooltip: \<div class="paragraph">
   \<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
   \</div>)* adapter instance.

3. From the **Access Token Manager** list, select the access token you created in [Creating an access token manager](pa_creating_an_access_token_manager.html).

   For example, **GeneralAccessToken**.

4. Click **Add Mapping**. Click **Next**.

5. On the **Contract Fulfillment** tab, from the **Source** list, select **Persistent Grant**.

6. From the **Value** list, select **USER\_KEY**.

7. Click **Next** until the **Summary** tab is displayed. Click **Save**.

## Next steps

[Create an OpenID Connect policy](pa_creating_an_oidc_policy.html).

---

---
title: Configuring an IdP adapter
description: Configure an identity provider (IdP) adapter to look up session information and provide user identification to PingFederate. This example uses an instance of the HTML form adapter with an instance of the simple password credential validator (PCV).
component: pingaccess
version: 9.1
page_id: pingaccess:token_providers:pa_configuring_an_idp_adapter
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/token_providers/pa_configuring_an_idp_adapter.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Configuring an IdP adapter

Configure an identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* adapter to look up session information and provide user identification to PingFederate. This example uses an instance of the HTML form adapter with an instance of the simple password credential validator (PCV).

## About this task

For more information, see [Configuring an IdP adapter instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configuring_idp_adapter_instance.html).

## Steps

1. Go to **Authentication → Integration → IdP Adapters**.

2. Click **Create New Instance**.

3. In the **Instance Name** field, enter an instance name of your choosing.

   For example, `My_IdP`.

4. In the **Instance ID** field, enter an instance ID of your choosing.

   For example, `myidp`.

5. From the **Type** list, select **HTML Form IdP Adapter**, and then click **Next**.

6. On the **IdP Adapter** tab, under **Password Credential Validator Instance**, click **Add a new row to 'Credential Validators'.**

7. From the **Password Credential Validator Instance** list, select the password credential validator you created previously, for example, **My\_PCV**, and then click **Update**.

8. Click **Next** until the **Adapter Attributes** tab is displayed.

9. Locate the `username` attribute, then select the **Pseudonym** check box.

10. Click **Next** until the **Summary** tab is displayed. Click **Save**.

## Next steps

[Define the default scope](pa_defining_the_default_scope.html).

---

---
title: Configuring an IdP adapter mapping
description: Configure an identity provider (IdP) adapter mapping to map attributes.
component: pingaccess
version: 9.1
page_id: pingaccess:token_providers:pa_configuring_an_idp_adapter_mapping
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/token_providers/pa_configuring_an_idp_adapter_mapping.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Configuring an IdP adapter mapping

Configure an identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* adapter mapping to map attributes.

## About this task

For more information, see [Managing IdP adapter grant mapping](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_oauthsource2targetmappingtasklet_oauthidpadapter2targetmappingsstate.html).

## Steps

1. Go to **Authentication → OAuth → IdP Adapter Grant Mapping**.

2. From the **Source Adapter Instance** list, select the adapter you created in [Configuring an IdP adapter](pa_configuring_an_idp_adapter.html).

3. Click **Add Mapping**, then click **Next** until the **Contract Fulfillment** tab is displayed.

4. In the **USER\_KEY** row:

   1. In the **Source** column, select **Adapter**.

   2. In the **Value** column, select **username**.

5. In the **USER\_NAME** row:

   1. In the **Source** column, select **Adapter**.

   2. In the **Value** column, select **username**.

6. Click **Next** until the **Summary** tab is displayed. Click **Save**.

## Next steps

[Configure an access token mapping](pa_configuring_an_access_token_mapping.html).

---

---
title: Configuring applications for dual access with PingAccess for Azure AD
description: Configure applications for secure access both from inside and outside the network.
component: pingaccess
version: 9.1
page_id: pingaccess:token_providers:pa_apps_for_dual_access_with_azure_ad
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/token_providers/pa_apps_for_dual_access_with_azure_ad.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 6, 2024
section_ids:
  steps: Steps
  example: Example:
  example-2: Example:
  example-3: Example:
---

# Configuring applications for dual access with PingAccess for Azure AD

Configure applications for secure access both from inside and outside the network.

## Steps

1. Configure an application for secure external access using [Microsoft Entra ID (formerly Microsoft Azure AD)](https://docs.microsoft.com/en-us/azure/active-directory/application-proxy-ping-access) and [PingAccess for Azure AD](pa_get_started_with_pa_for_azure_ad.html).

2. Ensure that the application is functioning as expected by signing on using the application's external Uniform Resource Locator (URL) *(tooltip: \<div class="paragraph">
   \<p>Identifies a resource according to its internet location.\</p>
   \</div>)*.

   ### Example:

   For example, http\://app-tenant.msappproxy.net/.

3. In PingAccess, [create a new virtual host](../pingaccess_user_interface_reference_guide/pa_creating_new_virtual_hosts.html) that maps to the PingAccess host.

   ### Example:

   For example, `<PingAccessServerName>:3000`.

4. Assign the new virtual host to the application in addition to the virtual host specified for Microsoft Entra ID access.

5. In Microsoft Entra ID, go to the **App Registrations** window and select the application.

6. Click **Reply URLs** and add the internal PingAccess reply URL.

   ### Example:

   For example, `<PingAccessServerName>:3000/pa/oidc/cb`.

   |   |                                                                                                                                                                                                                                                                                                                                                              |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If you have the **Use context root as reserved resource base path** check box enabled on your PingAccess application, enter the application's context root before the reserved application context root.Using the previous example, the reply URL would be `<PingAccessServerName>:3000/myApp/pa/oidc/cb` if your application had a context root of `myApp`. |

7. Save the changes and test the configuration by signing on using the application's local URL.

---

---
title: Configuring PingAccess applications for Microsoft Entra ID
description: Configure PingAccess applications so they are accessible to users through the Microsoft Entra ID (formerly Microsoft Azure AD) MyApps portal.
component: pingaccess
version: 9.1
page_id: pingaccess:token_providers:pa_configuring_apps_for_azure
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/token_providers/pa_configuring_apps_for_azure.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 27, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  example: Example:
  example-2: Example:
---

# Configuring PingAccess applications for Microsoft Entra ID

Configure PingAccess applications so they are accessible to users through the Microsoft Entra ID (formerly Microsoft Azure AD) [MyApps](https://myapps.microsoft.com) portal.

## Before you begin

* Install PingAccess and verify that you can access the [administrative console](../installing_and_uninstalling_pingaccess/pa_accessing_the_admin_console.html). Learn more about installing PingAccess in [Installing and Uninstalling PingAccess](../installing_and_uninstalling_pingaccess/pa_installing_and_uninstalling_pa.html).

  |   |                                                                                                                                                                               |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The default credential set should be changed upon first usage. The default credentials for your PingAccess installation are:```
  Username: Administrator
  Password: 2Access
  ``` |

* Have a [Microsoft Entra ID](https://portal.azure.com) Premium account for access to the Application Proxy feature.

* Configure Microsoft Entra ID. You can find steps to configure Microsoft Entra ID in <https://docs.microsoft.com/azure/active-directory/application-proxy-ping-access>.

* [Configure](pa_configure_pa_to_use_azure_ad_as_the_token_provider.html) PingAccess to use Microsoft Entra ID as the token provider.

## About this task

For each application that you want to configure:

## Steps

1. Create a virtual host.

   Learn more about creating a virtual host in [Creating new virtual hosts](../pingaccess_user_interface_reference_guide/pa_creating_new_virtual_hosts.html).

   |   |                                                                                                     |
   | - | --------------------------------------------------------------------------------------------------- |
   |   | In a typical configuration for this solution, you will create a virtual host for every application. |

   1. Click **Applications**, then go to **Applications > Virtual Hosts**.

   2. Click **[icon: plus, set=fa]Add Virtual Host**.

   3. In the **Host** field, enter the FQDN portion of the Microsoft Entra ID **External URL**.

      ### Example:

      For example, external URLs of https\://app-tenant.msappproxy.net/ and https\://app-tenant.msappproxy.net/AppName will both have a **Host** entry of `app-tenant.msappproxy.net`.

   4. In the **Port** field, enter `443`.

   5. Click **Save**.

2. Create a web session.

   Learn more about creating a web session in [Creating web sessions](../pingaccess_user_interface_reference_guide/pa_creating_web_sessions.html).

   1. Click **Access**, then go to **Web Sessions > Web Sessions**.

   2. Click **[icon: plus, set=fa]Add Web Session**.

   3. In the **Name** field, enter a name for the web session.

   4. From the **Cookie Type** list, select your cookie type, either **Signed JWT** or **Encrypted JWT**.

   5. In the **Audience** field, enter a unique value.

   6. In the **Client ID** field, enter the Microsoft Entra ID application ID.

   7. From the **Client Credentials Type** list, select **Secret**.

   8. In the **Client Secret** field, enter the client secret you generated for the application in Microsoft Entra ID.

   9. **Optional:** To create and use custom claims with the Microsoft Entra ID GraphAPI, click **Advanced** and clear the **Request Profile** and **Refresh User Attributes** checkboxes.

      Learn more about using custom claims in [Optional - Use a custom claim](https://docs.microsoft.com/en-us/azure/active-directory/application-proxy-ping-access).

   10. Click **Save**.

3. Create an identity mapping.

   Learn more about creating an identity mapping in [Creating header identity mappings](../pingaccess_user_interface_reference_guide/pa_creating_header_identity_mappings.html).

   |   |                                                                                                                                       |
   | - | ------------------------------------------------------------------------------------------------------------------------------------- |
   |   | An identity mapping can be used with more than one application if more than one application is expecting the same data in the header. |

   1. Click **Access**, then go to **Identity Mappings > Identity Mappings**.

   2. Click **[icon: plus, set=fa]Add Identity Mapping**.

   3. In the **Name** field, enter a name.

   4. From the **Type** list, select **Header Identity Mapping**.

   5. In the **Attribute to Header Mapping** table, specify the required mappings.

      ### Example:

      For example:

      | Attribute Name | Header Name         |
      | -------------- | ------------------- |
      | upn            | x-userprinciplename |
      | email          | x-email             |
      | oid            | x-oid               |
      | scp            | x-scope             |
      | amr            | x-amr               |

   6. Click **Save**.

4. Create a site.

   Learn more about creating a site in [Adding sites](../pingaccess_user_interface_reference_guide/pa_adding_sites.html).

   |   |                                                                                                                                               |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | In some configurations, a site might contain more than one application. A site can be used with more than one application, where appropriate. |

   1. Click **Applications**, then go to **Sites > Sites**.

   2. Click **[icon: plus, set=fa]Add Site**.

   3. In the **Name** field, enter a name for the site.

   4. In the **Target** field, specify the target.

      The target is the hostname:port pair for the server hosting the application. Do not enter the path for the application in this field. For example, an application at https\://mysite:9999/AppName will have a target value of `mysite:9999`.

   5. From the **Secure** list, select whether or not the target is expecting secure connections.

   6. Click **Save**.

5. Create an application in PingAccess for each application in Microsoft Entra ID that you want to protect.

   Learn more about creating an application in [Adding an application](../pingaccess_user_interface_reference_guide/pa_adding_an_app.html).

   1. Click **Applications**, then go to **Applications > Applications**.

   2. Click **[icon: plus, set=fa]Add Application**.

   3. In the **Name** field, enter a name for the application.

   4. In the **Description** field, enter a description for the application.

   5. In the **Context Root** field, specify the context root for the application.

      For example, an application at `https://mysite:9999/AppName` will have a context root of `/AppName`. If the application is on the root of the server, you can set the context root as `/`. The context root must begin with a slash (/), must not end with a slash (/), and can be more than one layer deep, for example, `/Apps/MyApp`.

   6. From the **Virtual Host** list, select the virtual host you created.

      |   |                                                                                |
      | - | ------------------------------------------------------------------------------ |
      |   | The combination of virtual host and context root must be unique in PingAccess. |

   7. From the **Application Type** list, select **Web**.

   8. From the **Web Session** list, select the web session you created.

   9. From the **Site** list, select the site you created that contains the application.

   10. From the **Web Identity Mapping** list, select the mapping you created.

   11. Select the **Enabled** checkbox to enable the site when you save.

   12. Click **Save**.

---

---
title: Configuring PingAccess to use Microsoft Entra ID as the token provider
description: Configure PingAccess to use Microsoft Entra ID (formerly Microsoft Azure AD) as the token provider.
component: pingaccess
version: 9.1
page_id: pingaccess:token_providers:pa_configure_pa_to_use_azure_ad_as_the_token_provider
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/token_providers/pa_configure_pa_to_use_azure_ad_as_the_token_provider.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 27, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  next-steps: Next steps
---

# Configuring PingAccess to use Microsoft Entra ID as the token provider

Configure PingAccess to use Microsoft Entra ID (formerly Microsoft Azure AD) as the token provider.

## Before you begin

* Install PingAccess and verify that you can access the [administrative console](../installing_and_uninstalling_pingaccess/pa_accessing_the_admin_console.html). You can find more information about installing PingAccess in [Installing and Uninstalling PingAccess](../installing_and_uninstalling_pingaccess/pa_installing_and_uninstalling_pa.html).

  |   |                                                                                                                                                                               |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The default credential set should be changed upon first usage. The default credentials for your PingAccess installation are:```
  Username: Administrator
  Password: 2Access
  ``` |

* If your administrative node uses a proxy for HTTP requests to the token provider, select the HTTP Proxy in the **System > Clustering** section. Learn more in [Configuring administrative nodes](../pingaccess_user_interface_reference_guide/pa_configuring_admin_nodes.html).

## About this task

You can find more information about configuring the token provider in [Token provider](../pingaccess_user_interface_reference_guide/pa_token_provider.html).

## Steps

1. Click **Settings**, then go to **System > Token Provider > Common > OpenID Connect**.

   1. Go to **Settings > System > Token Provider** and select **Common Token Provider**.

2. In the **Issuer** field, enter the Microsoft Entra ID **Directory ID**.

   To obtain the directory ID from Microsoft Entra ID, in the Microsoft Entra ID directory, go to **Manage > Properties** and copy the **Directory ID** value.

3. From the **Trusted Certificate Group** list,

   ### Choose from:

   * **Java Trust Store**

   * **Trust Any**

4. Click **Save**.

## Next steps

To get the most out of the solution, see [Configuring token provider-specific options](../pingaccess_user_interface_reference_guide/pa_configuring_token_provider_specific_options.html).

---

---
title: Configuring PingAccess to use PingOne for Customers as the token provider
description: Configure PingAccess to use PingOne as the token provider in the PingAccess user interface.
component: pingaccess
version: 9.1
page_id: pingaccess:token_providers:pa_configuring_pa_to_use_p1_for_customers_as_the_token_provider
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/token_providers/pa_configuring_pa_to_use_p1_for_customers_as_the_token_provider.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 14, 2023
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
---

# Configuring PingAccess to use PingOne for Customers as the token provider

Configure PingAccess to use PingOne as the token provider in the PingAccess user interface.

## Before you begin

* Install PingAccess and verify that you can access the [administrative console](../installing_and_uninstalling_pingaccess/pa_accessing_the_admin_console.html). For more information on installing PingAccess, see [Installing and Uninstalling PingAccess](../installing_and_uninstalling_pingaccess/pa_installing_and_uninstalling_pa.html).

  |   |                                                                                                                                                                               |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The default credential set should be changed upon first usage. The default credentials for your PingAccess installation are:```
  Username: Administrator
  Password: 2Access
  ``` |

* [Configure an application](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html) in PingOne.

## About this task

For more information on configuring PingOne as the token provider, see [Configuring PingOne](../pingaccess_user_interface_reference_guide/pa_configuring_p1.html).

## Steps

1. Click **Settings**, then go to **System > Token Provider > PingOne**.

2. In the **Issuer** field, enter the PingOne Issuer URL.

   To obtain the Issuer URL, in PingOne, go to the **Configuration** tab of an application and copy the **Issuer** value.

3. **Optional:** In the **Description** field, enter a description for the connection.

4. From the **Trusted Certificate Group** list, select a trusted certificate group that PingAccess will use when authenticating to PingOne.

5. To configure the connection to use a configured proxy, click **Show Advanced** and select **Use Proxy**.

6. Click **Save**.

---

---
title: Configuring the token provider
description: Establish communication with the token provider, PingFederate.
component: pingaccess
version: 9.1
page_id: pingaccess:token_providers:pa_configuring_the_token_provider
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/token_providers/pa_configuring_the_token_provider.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Configuring the token provider

Establish communication with the token provider, PingFederate.

## About this task

For more information, see [Manage Token Provider](../pingaccess_user_interface_reference_guide/pa_token_provider.html).

## Steps

1. Click **Settings**, then go to **System > Token Provider > PingFederate > Runtime**.

2. In the **Issuer** field, enter the PingFederate issuer URI.

3. From the **Trusted Certificate Group** list, select the **PingFed** certificate group.

4. Click **Save**.

5. Click **Settings**, then go to **System > Token Provider > PingFederate > Administration**.

6. In the **Host** field, enter the host name or Internet Protocol (IP) *(tooltip: \<div class="paragraph">
   \<p>The method by which data is sent across the internet from the source host to the destination host.\</p>
   \</div>)* address for the PingFederate Admin.

   For example, `mypingfedserver`.

7. In the **Port** field, enter the port number for the PingFederate Admin.

   For example, `9999`.

8. In the **Admin Username** field, enter the username.

   This username only requires auditor (read only) permissions in PingFederate.

9. In the **Admin Password** field, enter the password.

10. From the **Secure** list, select **Secure**.

11. From the **Trusted Certificate Group** list, select the **PingFed** certificate group.

12. Click **Save**.

13. Click **Settings**, then go to **System > Token Provider > PingFederate > OAuth Resource Server**.

14. In the **Client ID** field, enter the OAuth Client ID you defined when creating the PingAccess OAuth client *(tooltip: \<div class="paragraph">
    \<p>The application in an OAuth framework that requests access to resources. If the request is approved by the authorization server, the client is issued an access token for the resources.\</p>
    \</div>)* in PingFederate.

    For example, `pa_rs`.

15. In the **Client Credentials Type** section, select **Secret**, then enter the **Client Secret** assigned when you created the PingAccess OAuth client in PingFederate.

16. In the **Subject Attribute Name** field, enter the attribute you want to use from the OAuth access token *(tooltip: \<div class="paragraph">
    \<p>A data object by which a client authenticates to a resource server and lays claim to authorizations for accessing particular resources.\</p>
    \</div>)* as the subject for auditing purposes.

    For example, `username`.

17. Click **Save**.

## Next steps

You can configure PingAccess to [Protect a web application](../pingaccess_use_cases/pa_protecting_a_web_app_with_pa_in_a_gateway_deployment.html).

---

---
title: Connect PingAccess to PingFederate
description: This section explains how to configure PingAccess to communicate with PingFederate.
component: pingaccess
version: 9.1
page_id: pingaccess:token_providers:pa_connect_pa_to_pf
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/token_providers/pa_connect_pa_to_pf.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
---

# Connect PingAccess to PingFederate

This section explains how to configure PingAccess to communicate with PingFederate.

In this configuration procedure, you will perform the following tasks:

1. [Import certificates and create a trusted certificate group](pa_importing_certificates_and_creating_a_trusted_certificate_group.html).

2. [Configure the token provider](pa_configuring_the_token_provider.html).

After configuring PingAccess to use PingFederate as a token provider, you can configure it to protect a web application. See [Protecting a web application](../pingaccess_use_cases/pa_protecting_a_web_app_with_pa_in_a_gateway_deployment.html) for more information.

---

---
title: Connecting the QuickStart utility to PingAccess and PingFederate
description: Connect the QuickStart utility to your installed PingAccess and PingFederate deployments.
component: pingaccess
version: 9.1
page_id: pingaccess:token_providers:pa_connecting_the_quickstart_utility_to_pa_and_pf
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/token_providers/pa_connecting_the_quickstart_utility_to_pa_and_pf.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  steps: Steps
  result: Result:
  next-steps: Next steps
---

# Connecting the QuickStart utility to PingAccess and PingFederate

Connect the QuickStart utility to your installed PingAccess and PingFederate deployments.

## Steps

1. Go to https\://*hostname*:8443 and sign on to the QuickStart utility.

   |   |                                                                                                                                                                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you cannot access the utility, you might need to restart it by rerunning the `.jar`file. For more information, see the final step in [Installing and configuring QuickStart components](pa_installing_and_configuring_quickstart_components.html). |

   ### Result:

   The QuickStart user interface is displayed.

2. Click **Connect**.

3. Enter the PingFederate runtime configuration.

   1. In the **Host** field, enter the host name.

   2. In the **Port** field, enter the port.

4. Enter the PingFederate admin configuration.

   1. In the **Host** field, enter the host name.

   2. In the **Port** field, enter the port.

5. In the **Username** and **Password** fields enter the admin credentials for PingFederate, and then click **Validate**.

6. Click **Next**.

7. Enter the PingAccess runtime configuration.

   1. In the **Host** field, enter the host name.

   2. In the **Port** field, enter the port.

8. Enter the PingAccess admin configuration.

   1. In the **Host** field, enter the host name.

   2. In the **Port** field, enter the port.

9. In the **Username** and **Password** fields, enter the admin credentials for PingAccess, and then click **Validate**.

10. Click **Save and Close**.

## Next steps

[Use sample applications](pa_using_sample_apps.html).

---

---
title: Creating a password credential validator
description: Create a password credential validator (PCV) and then create a username and password to use in authentication.
component: pingaccess
version: 9.1
page_id: pingaccess:token_providers:pa_creating_a_password_credential_validator
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/token_providers/pa_creating_a_password_credential_validator.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Creating a password credential validator

Create a password credential validator (PCV) and then create a username and password to use in authentication.

## About this task

For more information on PCVs, see [Configuring the Simple Username Password Credential Validator](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configure_simple_username_pcv.html).

## Steps

1. Go to **System → Data & Credential Stores → Password Credential Validators**.

2. Click **Create New Instance**.

3. In the **Instance Name** field, enter an instance name of your choosing.

   For example, `My_PCV`.

4. In the **Instance ID** field, enter an instance ID of your choosing.

   For example, `mypcv`.

5. From the **Type** list, select **Simple Username Password Credential Validator**, and then click **Next**.

6. On the **Instance Configuration** tab, click **Add a new row to 'Users'**.

7. In the **Username** field, enter a username.

8. In the **Password** fields, enter and confirm a password.

9. Click **Update**, then click **Next**.

10. On the **Summary** tab, click **Save**.

## Next steps

[Configure an IdP adapter](pa_configuring_an_idp_adapter.html).

---

---
title: Creating a resource server client
description: Configure an OAuth client for use with PingFederate token provider resource server configuration in PingAccess.
component: pingaccess
version: 9.1
page_id: pingaccess:token_providers:pa_creating_a_resource_server
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/token_providers/pa_creating_a_resource_server.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Creating a resource server client

Configure an OAuth *(tooltip: \<div class="paragraph">
\<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
\</div>)* client for use with PingFederate token provider resource server configuration in PingAccess.

## About this task

For more information, see [Manage OAuth clients](https://docs.pingidentity.com/pingfederate/latest/introduction_to_pingfederate/pf_client_management.html).

## Steps

1. Go to **Applications → OAuth → Clients**.

2. Click **Add Client**.

3. In the **Client ID** field, specify a client ID.

   ```
   pa_rs
   ```

4. In the **Name** field, specify a name.

   ```
   PingAccessResourceServer
   ```

5. In the **Client Authentication** section, select **Client Secret**.

6. In the **Client Secret** section, select **Change Secret**, and then click **Generate Secret**.

   |   |                                                                                          |
   | - | ---------------------------------------------------------------------------------------- |
   |   | Copy the secret to a secure location so that you can use it in PingAccess configuration. |

7. In the **Redirect URIs** field, enter the OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
   \<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
   \</div>)* callback redirect to the PingAccess server.

   For example, `https://mypingaccessserver:3000/pa/oidc/cb`.

8. Click **Add**.

9. In the **Allowed Grant Types** section, select the **Access Token Validation (Client is a Resource Server)** check box.

10. Click **Save**.

## Next steps

[Create a web session client](pa_creating_a_web_session_client.html).

---

---
title: Creating a web session client
description: Configure an OAuth client for use with web session configuration in PingAccess.
component: pingaccess
version: 9.1
page_id: pingaccess:token_providers:pa_creating_a_web_session_client
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/token_providers/pa_creating_a_web_session_client.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Creating a web session client

Configure an OAuth client *(tooltip: \<div class="paragraph">
\<p>The application in an OAuth framework that requests access to resources. If the request is approved by the authorization server, the client is issued an access token for the resources.\</p>
\</div>)* for use with web session configuration in PingAccess.

## About this task

For more information, see [Manage OAuth clients](https://docs.pingidentity.com/pingfederate/latest/introduction_to_pingfederate/pf_client_management.html).

## Steps

1. Go to **Applications → OAuth → Clients**.

2. Click **Add Client**.

3. In the **Client ID** field, specify a client ID.

   ```
   pa_wam
   ```

4. In the **Name** field, specify a name.

   ```
   PingAccessWebAccessManagement
   ```

5. In the **Client Authentication** section, select **Client Secret**.

6. In the **Client Secret** section, select **Change Secret**, and then click **Generate Secret**.

   |   |                                                                                          |
   | - | ---------------------------------------------------------------------------------------- |
   |   | Copy the secret to a secure location so that you can use it in PingAccess configuration. |

7. In the **Redirect URIs** field, add the OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
   \<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
   \</div>)* callback redirect to the PingAccess server.

   For example, `https://mypingaccessserver:3000/pa/oidc/cb`.

8. Click **Add**.

9. Select the **Bypass Authorization Approval** check box.

10. In the **Allowed Grant Types** section, select the **Authorization Code** check box.

11. Click **Save**.

## Next steps

[Create and export a certificate](pa_creating_and_exporting_a_certificate.html).

---

---
title: Creating an access token manager
description: Create an access token to grant access and control access parameters. This sample configuration uses an instance of the Access Token Manager (ATM) using the Internally Managed Reference Tokens data model.
component: pingaccess
version: 9.1
page_id: pingaccess:token_providers:pa_creating_an_access_token_manager
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/token_providers/pa_creating_an_access_token_manager.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Creating an access token manager

Create an access token to grant access and control access parameters. This sample configuration uses an instance of the Access Token Manager (ATM) using the Internally Managed Reference Tokens data model.

## About this task

For more information, see OAuth [Access token management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_access_token_management.html).

## Steps

1. Go to **Applications → OAuth → Access Token Management**.

2. Click **Create New Instance**.

3. In the **Instance Name** field, enter an instance name of your choosing.

   For example, `General Access Token`.

4. In the **Instance ID** field, enter an instance ID of your choosing.

   For example, `GeneralAccessToken`.

5. From the **Type** list, select **Internally Managed Reference Tokens**.

6. Click **Next** until the **Access Token Attribute Contract** tab is displayed.

7. In the **Extend the Contract** field, enter `UserName`, and then click **Add**.

8. Click **Next** until the **Summary** tab is displayed. Click **Save**.

## Next steps

[Configure an IdP adapter mapping](pa_configuring_an_idp_adapter_mapping.html).

---

---
title: Creating an OpenID Connect policy
description: Configure an OpenID Connect (OIDC) policy to define OIDC policies for client access to attributes mapped according to OpenID specifications.
component: pingaccess
version: 9.1
page_id: pingaccess:token_providers:pa_creating_an_oidc_policy
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/token_providers/pa_creating_an_oidc_policy.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Creating an OpenID Connect policy

Configure an OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)* policy to define OIDC policies for client access to attributes mapped according to OpenID specifications.

## About this task

For more information, see [Configuring OpenID Connect policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configuring_oidc_policies.html).

## Steps

1. Go to **Applications → OAuth → OpenID Connect Policy Management**.

2. Click **Add Policy**.

3. In the **Policy ID** field, enter an Policy ID of your choosing.

   For example, `OIDC`.

4. In the **Name** field, enter a name of your choosing.

   For example, `OIDC`.

5. From the **Access Token Manager** list, select the access token you created in [Configuring an access token mapping](pa_configuring_an_access_token_mapping.html).

   For example, **GeneralAccessToken**.

6. Click **Next**.

7. On the **Attribute Contract** tab, delete all items beneath the **Extend the Contract** heading.

8. Click **Next** until the **Contract Fulfillment** tab is displayed.

9. From the **Source** list, select **Access Token**.

10. From the **Value** list, select **username**.

11. Click **Next** until the **Summary** tab is displayed. Click **Save**.

12. In the **Action** column for the policy you created, if the policy is not already listed as the default, click **Set as Default**.

## Next steps

[Create a resource server client](pa_creating_a_resource_server.html).

---

---
title: Creating and exporting a certificate
description: Create and export a certificate for the PingFederate server that you will import to PingAccess to establish trust.
component: pingaccess
version: 9.1
page_id: pingaccess:token_providers:pa_creating_and_exporting_a_certificate
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/token_providers/pa_creating_and_exporting_a_certificate.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Creating and exporting a certificate

Create and export a certificate for the PingFederate server that you will import to PingAccess to establish trust.

## About this task

For more information, see [Manage SSL server certificates](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_sslservercerts_certmanagementstate.html).

## Steps

1. In the PingFederate administrative console, go to **Security → Certificate & Key Management → SSL Server Certificates**.

2. Click **Create New**.

3. In the **Common Name** field, enter the PingFederate server address.

   For example, `mypingfedserver`.

4. In the **Organization** field, enter your organization's name.

5. In the **Country** field, enter the two-letter abbreviation for your country.

6. Complete the remaining fields as required.

7. Click **Next**.

8. Click **Save**.

9. In the **Action** section, click **Activate Default for Runtime Server**.

10. In the **Action** section, click **Export**.

11. Select **Certificate Only**. Click **Next**.

12. Click **Export**, and then save the exported certificate.

13. Click **Done**.

## Next steps

[Connect PingAccess to PingFederate and configure an application](pa_connect_pa_to_pf.html).

---

---
title: Defining the default scope
description: Use the Scope Management section to define the default scope.
component: pingaccess
version: 9.1
page_id: pingaccess:token_providers:pa_defining_the_default_scope
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/token_providers/pa_defining_the_default_scope.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Defining the default scope

Use the **Scope Management** section to define the default scope.

## About this task

For more information, see [Define scopes](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/rbk1564002990993.html).

## Steps

1. Go to **System → OAuth Settings → Scope Management**.

2. Click the **Common Scopes** tab, then enter the following scope values and their descriptions one at a time, clicking **Add** with each entry.

   | Scope Value | Scope Description |
   | ----------- | ----------------- |
   | address     | address           |
   | email       | email             |
   | openid      | openid            |
   | phone       | phone             |
   | profile     | profile           |

3. Click **Next** until you reach the **Default Scope** tab.

4. On the **Default Scope** tab, enter a description.

   For example, `default scope`.

5. Click **Save**.

## Next steps

[Create an access token manager](pa_creating_an_access_token_manager.html).