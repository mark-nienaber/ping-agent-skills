---
title: Changelog
description: Web Access Management Integration Kit 2.0 – August 2014 (Current Release)
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_integration_kit:pf_wam_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_integration_kit/pf_wam_ik_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/webAccessManagement/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 18, 2024
---

# Changelog

**Web Access Management Integration Kit 2.0 – August 2014 (Current Release)**

* Added a per-adapter SLO URL field

* Added an Authentication Mapping Table with an attribute filter for the IdP adapter

* Added a Protected Resource Mapping Table to the SP adapter with an attribute filter

* Enabled cookie provider functionality during SLO

* Added an encode token field to the SP adapter

* Added support for ObFormLoginCookie with customizable rh value

**Web Access Management Integration Kit 1.2 – August 2013**

* Added support for Cookie Provider

* Added OpenToken support within WAM Adapter

* Added Authentication Level to Authentication Context mapping table

**Web Access Management Integration Kit 1.1 – March 2013**

* WAM kit now includes WAM plug-in compatible with RSA Access Manager

**Web Access Management Integration Kit 1.0.1 – December 2012**

* Updated to address security issue found since the previous release.

* Added support for OpenToken 2.5.1 Adapter

**Web Access Management Integration Kit 1.0 – November 2012**

* Initial Release

* Redesigned former product-specific kits to provide consistent functionality across multiple WAM products

---

---
title: Changelog
description: Web Access Management Token Translator 2.0 – August 2014 (Current Release)
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_token_translator:pf_wam_tt_changelog
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_token_translator/pf_wam_tt_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/webAccessManagement/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
---

# Changelog

**Web Access Management Token Translator 2.0 – August 2014 (Current Release)**

* Updated Token Translator with the WAM Agent Plugin 2.0

* Added "encode Token" field

**Web Access Management Token Translator 1.2 – August 2013**

* Updated Token Translator with the WAM Agent Plugin 1.2

**Web Access Management Token Translator 1.1 – March 2013**

* WAM Token Translator now includes WAM plug-in compatible with RSA Access Manager

**Web Access Management Token Translator 1.0.1 – December 2012**

* Updated to address security issues found since previous release

* Added support for OpenToken Adapter 2.5.1

**Web Access Management Token Translator 1.0 – November 2012**

* Initial Release

* Redesigned former product-specific kits to provide consistent functionality across multiple WAM products

---

---
title: Configuring an IdP adapter instance
description: Configure the WAM Integration Kit for an identity provider (IdP).
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_integration_kit:pf_wam_ik_configuring_an_idp_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_integration_kit/pf_wam_ik_configuring_an_idp_adapter_instance.html
llms_txt: https://docs.pingidentity.com/integrations/webAccessManagement/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 18, 2024
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
---

# Configuring an IdP adapter instance

Configure the WAM Integration Kit for an identity provider (IdP).

## Before you begin

|   |                                                                                                                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You must create a third-party WAM Web Agent in your WAM tool before starting the following procedure. Several properties that you use to configure the agent are required to fill out the **IdP Adapter** tab in the following procedure.You can find more details on agent configuration in your WAM Server documentation. |

## Steps

1. In the PingFederate administrative console, create a new IdP adapter instance:

   ### Choose from:

   * For PingFederate 10.1 or later: go to **Authentication > Integration > IdP Adapters**. Click **Create New Instance**.

   * For PingFederate 10.0 or earlier: go to **Identity Provider > Adapters**. Click **Create New Instance**.

2. On the **Type** tab, set the basic adapter instance attributes:

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. In the **Type** list, select **WAM IdP Adapter**. Click **Next**.

      |   |                                                                                                                                                                                                                                             |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | * If you are configuring the adapter for a custom plug-in (not bundled with this kit), continue to step 5.

      * If you are configuring the RSA AM Dispatcher server, continue with step 6.

      * If you are configuring OAM, continue at step 7. |

      ![A screenshot that shows the WAM IdP Adapter settings.](_images/zgf1563995786336.jpg)

3. (Only for custom plug-ins for WAM servers other than OAM or RSA) On the **IdP Adapter** tab, click **Add a new row to 'WAM Server'** and enter the following information:

   1. Enter the hostname or the IP address where the WAM server is running.

   2. Specify the remaining WAM server values required for your configuration.

   3. In the **Action** column, click **Update**.

   4. Repeat this step as needed for additional custom WAM plug-ins.

      Skip the next step.

4. (Only for the RSA bundled plug-in) On the **IdP Adapter** tab, click **Add a new row to 'RSA AM Dispatcher Server'** and enter the following information:

   |   |                                                         |
   | - | ------------------------------------------------------- |
   |   | You must specify at least one RSA AM Dispatcher Server. |

   1. Enter the hostname or the IP address and the (optional) dispatcher port where the RSA AM Dispatcher server is running.

      |   |                                                                                                                                                                                      |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | You must specify the authentication method used by the dispatcher server. If you have specified multiple dispatcher servers, each server can have individual authentication methods. |

   2. Specify the **Authentication Type** used by the RSA Dispatcher Server.

      * **Clear**: Clear text, no encryption.

      * **Anon**: Anonymous SSL, SSL encryption only.

      * **Auth**: Mutually authenticated SSL, SSL encryption with certificate-based encryption.

   3. If you select **Auth** as the **Authentication Type**, you must specify the following RSA server values:

      * **Keystore Path**: The string filename of the private keystore file (PKCS12 only).

      * **Keystore Password**: The password for the private keystore.

      * **Key Alias**: The alias to your private key in the keystore.

      * **Key Password**: The private key password for keystore.

   4. (Optional) Specify the **Timeout** value required for your configuration.

   5. In the **Action** column, click **Update**.

   6. Repeat this step as needed for additional RSA Servers.

5. (Only for custom plug-ins for WAM servers and the OAM bundled plug-in) On the **IdP Adapter** tab, click **Add a new row to 'Authentication Context Mapping Table'** and enter the following information:

   * **Authentication Level**: A specific value for a WAM system indicating the level of authentication an end-user has gone through.

   * **Authentication Context**: This is part of the SAML assertion.

   1. In the **Action** column, click **Update**. Repeat this step as needed.

6. Provide entries on the **IdP Adapter** tab, as described on the tab and in the following table.

   |   |                                                                                                                                                                                                                                                |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The selected WAM Plug-in Type may override optional and required fields.For example, if the selected **WAM Plug-in Type** is OAM, the **Agent Config Location** becomes a required field. Leaving this field blank generates an error message. |

   > **Collapse: Configuration Fields**
   >
   > | Field                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   > | ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | **WAM Plug-in Type**                 | The class name for the specific WAM implementation.	The WAM Plug-in Type determines optional and required fields.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   > | **Agent Name**                       | This value must match the value used when the third-party WAM Web Agent was configured.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   > | **Agent Secret**                     | This value must match the value used when the third-party WAM Web Agent was configured.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   > | **Agent Config Location**            | Required for OAM. This value must contain the full path to an XML network-configuration file generated by the access-management system.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   > | **Failover**                         | The default is false, indicating load balancing is enabled and user-session states and configuration data are shared among multiple WAM servers.Select **true** to enable failover, indicating that when one server fails, the next server is used.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   > | **Domain Name**                      | Enter the fully-qualified domain name for the Cookie Domain where the WAM session cookie is stored, preceded by a period.For example, `.pingidentity.com`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   > | **Cookie Path**                      | (Required) The default value is the root directory (`/`). Specify a different path for the WAM session cookie location, if necessary.You can find more details in WAM Server documentation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   > | **Protected Resource**               | (Required) The default value is all files in the root directory (`/*`). Specify a different path to the resources in the protected realm, if necessary.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   > | **Error URL**                        | Enter a URL for redirecting the user if there are errors. For example, incorrect parameters in the link.This URL can contain query parameters. The URL has an `errorMessage` query parameter appended to it, which contains a brief description of the error that happened. The error page can optionally display this message on the screen to provide guidance on remedying the problem.When using the `errorMessage` query parameter in a custom error page, adhere to Web application security best practices to guard against common content injection vulnerabilities.If no URL is specified, the appropriate default error landing page appears. Learn more in [Customizable user-facing pages](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_custom_user_facing_pages.html) in the PingFederate documentation.	If you define an error redirect URL, errors are sent to the error URL and logged in the PingFederate server log, but not the PingFederate audit log. |
   > | **User Identifier**                  | (Required) Defines which attribute parsed from the WAM session cookie is the user identifier for use in the assertion.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
   > | **Session Token Name**               | (Required) The WAM session cookie name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   > | **Session Token LOGGEDOFF Value**    | (Required) The value representing a logged-out session token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   > | **HTTP Only**                        | Enable this option to set the WAM Session Cookie as HTTP Only.If this option is enabled, the browser will send the WAM Session Cookie through HTTP or HTTPS.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   > | **Secure**                           | Enable this option to set the WAM Session Cookie as secure.If this option is enabled, the browser will send the WAM Session Cookie via HTTPS only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   > | **PingFederate Base URL**            | The base URL for PingFederate. If specified, this value is used for creating the return URL if the Cookie Provider URL is used.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   > | **Authorization Error URL**          | URL to redirect for authorization errors.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   > | **Cookie Provider URL**              | The URL for the cookie provider where PingFederate should redirect the request if the WAM session cookie is in a separate domain. This service must be protected by the WAM server and would simply redirect back to the PingFederate `resumePath`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   > | **Cookie Provider Target Parameter** | The name of the parameter used to send the return URL for the cookie provider.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   > | **Login URL**                        | An optional URL for the authentication service. If the WAM session cookie is not found in the request, PingFederate redirects the request to the URL page along with the relative `resumePath`. This service must be protected by the WAM Agent.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   > | **Per-Adapter SLO URL**              | If a URL is entered into this field, it will be used as the redirect target during SLO for this adapter instance, instead of the default value from PingFederate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   > | **Authentication Context**           | This may be any value agreed upon with your SP partner that indicates how the user was authenticated. The value is included in the SAML assertion. Standard URIs are defined in the SAML specifications. You can find more information in the [Authentication Context for the OASIS Security Assertion Markup Language(SAML) V2.0](http://docs.oasis-open.org/security/saml/v2.0/saml-authn-context-2.0-os.pdf) PDF on the OASIS site.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
   > | **Authentication Level Identifier**  | Identifier used for the Authentication Level attribute.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   > | **Repad Token String**               | Enable this to pad the incoming session token (if required).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

   ![A screenshot that shows the advanced WAM IdP Adapter settings.](_images/ptm1563995788261.jpg)

7. (Optional) Click **Show Advanced Fields** to specify OpenToken configuration values or settings, depending on your network configuration and other requirements at your site.

   This section also contains fields for configuring tokens capturing the original request information if necessary. This functionality is based on the ObFormLoginCookie from OAM.

   |   |                                                                                                                                                                             |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you want to configure the use of OpenToken as part of the WAM adapter configuration, complete the fields as described on the **IdP Adapter** tab and in the table below. |

   > **Collapse: Advanced Fields**
   >
   > | Field                                 | Description                                                                                                                                                                                                                                                          |
   > | ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | **OpenToken Name**                    | The name of the cookie or request attribute that contains the OpenToken. This name should be unique for each adapter instance.                                                                                                                                       |
   > | **OpenToken Transfer Method**         | Specifies how the OpenToken is transferred. Select one of the following options:- Through a cookie
   >
   > - As a query parameter
   >
   > - Through Form Post                                                                                                                      |
   > | **OpenToken Password**                | The password used for encrypting extended attributes.	This password is also used to generate the configuration file that the OpenToken agent uses. You must configure a value for the OpenToken Password even if the OpenToken Cipher Suite is set to NULL.          |
   > | **OpenToken Cipher Suite**            | The algorithm, cipher mode, and key size to use for token encryption.                                                                                                                                                                                                |
   > | **OpenToken Cookie Domain**           | The server domain, preceded by a period.For example, `.example.com`.If you don't specify a domain, the value is obtained from the request.                                                                                                                           |
   > | **OpenToken Cookie Path**             | The path for the cookie that contains the OpenToken.                                                                                                                                                                                                                 |
   > | **OpenToken Token Lifetime**          | The duration (in seconds) for which the OpenToken is valid. Range is 1 - 28800.                                                                                                                                                                                      |
   > | **OpenToken Session Lifetime**        | The duration (in seconds) during which the OpenToken can be re-issued without authentication. Range is 1 - 259200.                                                                                                                                                   |
   > | **Not Before Tolerance**              | The amount of time (in seconds) to allow for clock skew between servers. Range is 0 - 3600.                                                                                                                                                                          |
   > | **Session Cookie**                    | If selected, the OpenToken cookie is set as a session cookie (rather than a persistent cookie).Applies only if the **OpenToken Transfer Method** is set as `Cookie`.                                                                                                 |
   > | **Secure Cookie**                     | If selected, the OpenToken cookie is set only if the request is on a secure channel (HTTPS).Applies only if the **OpenToken Transfer Method** is set as `Cookie`.                                                                                                    |
   > | **Create Form Login Token**           | If selected, a Token is created containing the information needed to retain the original request information if a redirect to a form authentication page is required.The token contents are implemented based on the requirements of the ObFormLoginCookie from OAM. |
   > | **Form Login Cookie Name**            | The name given to the created Form Login CookieFor example, `ObFormLoginCookie`.                                                                                                                                                                                     |
   > | **Form Login Cookie Domain**          | The server domain, preceded by a period.For example, `.example.com`.                                                                                                                                                                                                 |
   > | **Form Login Cookie Path**            | The path for the cookie that contains the Form Login Cookie.                                                                                                                                                                                                         |
   > | **Form Login Cookie is Secure**       | Sets the `secure` flag on the Form Login Cookie.                                                                                                                                                                                                                     |
   > | **Form Login Cookie is HTTP Only**    | Sets the `httpOnly` flag on the Form Login Cookie.                                                                                                                                                                                                                   |
   > | **Form Login Token Transfer Method**  | Specifies how the Form Login Token is transferred. Select one of the following options:- Through a cookie
   >
   > - As a query parameter                                                                                                                                    |
   > | **Create Form Login Cookie for Host** | If selected, the Form Login Cookie is created for the hostname in the request, ignoring the **Form Login Cookie Domain**.                                                                                                                                            |
   > | **RU URL**                            | Determines how the ru URL is derived:- Base
   >
   >   Full path using the RH from the **PF BASE URL**.
   >
   > - Request
   >
   >   Full path using the RH from the HTTP request.
   >
   > - Relative
   >
   >   Use relative (do not add RH).                                                             |
   > | **Reset Invalid Session Cookie**      | If selected, the invalid session cookie is set to the configured logged-off value before redirecting to the **Login URL**.                                                                                                                                           |

8. Click **Next**.

9. On the **Actions** tab, click the **Test Connection** link to validate the WAM configuration.

   |   |                                                                                                                                                                                                                |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you're using an OpenToken Adapter Configuration, click the **Invoke Download** link and then click **Export** to download the `agent-config.txt` properties to a directory that the WAM Web Agent can read. |

10. On the **Extended Contract** tab, add any attributes that you want to include in the contract. Click **Next**.

11. On the **Adapter Attributes** tab, select **userId** or **wamSessionToken** under **Pseudonym**. You can also select any extended attributes specified on the previous screen. Click **Next**.

    Learn more in [Set pseudonym and masking options](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_pseudonym_masking_options.html) in the PingFederate documentation. Click **Next**.

12. On the **Summary** tab, check and save your configuration:

    ### Choose from:

    * For PingFederate 10.1 or later: Click **Save**.

    * For PingFederate 10.0 or earlier: Click **Done**. On the **Manage IdP Adapter Instances** tab, click **Save**.

---

---
title: Configuring an SP adapter instance
description: Configure the WAM Integration Kit for a service provider (SP).
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_integration_kit:pf_wam_ik_configuring_an_sp_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_integration_kit/pf_wam_ik_configuring_an_sp_adapter_instance.html
llms_txt: https://docs.pingidentity.com/integrations/webAccessManagement/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 18, 2024
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
---

# Configuring an SP adapter instance

Configure the WAM Integration Kit for a service provider (SP).

If you are using OAM, you can find configuration information in [Creating a Custom Authentication Scheme for OAM](pf_wam_ik_creating_a_custom_authentication_scheme_for_oam.html).

## Before you begin

|   |                                                                                                                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You must create a third-party WAM Web Agent in your WAM tool before starting the following procedure. Several properties that you use to configure the agent are required to fill out the **Instance Configuration** tab in the following procedure.You can find more details on configuring an agent in your WAM Server documentation. |

## Steps

1. In the PingFederate administrative console, create a new SP adapter instance.

   ### Choose from:

   * For PingFederate 10.1 or later: go to **Applications > Integration > SP Adapters**. Click **Create New Instance**.

   * For PingFederate 10.0 or earlier: go to **Service Provider > Adapters**. Click **Create New Instance**.

2. On the **Type** tab, set the basic adapter instance attributes:

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. In the **Type** list, select **WAM SP Adapter**. Click **Next**.

      |   |                                                                                                                                                                                                                                             |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | * If you are configuring the adapter for a custom plug-in (not bundled with this kit), continue to step 5.

      * If you are configuring the RSA AM Dispatcher server, continue with step 6.

      * If you are configuring OAM, continue at step 7. |

      ![A screenshot that shows the WAM SP Adapter settings.](_images/pgi1563995793233.jpg)

3. (Only for custom plug-ins for WAM servers other than OAM or RSA) On the **Instance Configuration** tab, click **Add a new row to 'WAM Server'** and enter the following information:

   1. Enter the Hostname or the IP address where the WAM server is running.

   2. Specify the remaining WAM server values required for your configuration.

   3. Click **Update** in the Action column.

   4. Repeat this step as needed for additional WAM plug-ins.

      Skip the next step.

4. (Only for the RSA bundled plug-in) On the **Instance Configuration** tab, click **Add a new row to 'RSA AM Dispatcher Server'** and enter the following information:

   |   |                                                         |
   | - | ------------------------------------------------------- |
   |   | You must specify at least one RSA AM Dispatcher Server. |

   1. Enter the Hostname or the IP address and the (optional) Dispatcher Port where the RSA AM Dispatcher server is running.

      |   |                                                                                                                                                                               |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | You must specify the authentication method used by the dispatcher server. If you specify multiple dispatcher servers, each server can have individual authentication methods. |

   2. Specify the **Authentication Type** used by the RSA Dispatcher Server:

      * **Clear**: Clear text, no encryption.

      * **Anon**: Anonymous SSL, SSL encryption only.

      * **Auth**: Mutually authenticated SSL, SSL encryption with certificate-based encryption.

   3. If you select **Auth** as the **Authentication Type**, you must specify the following RSA server values:

      * **Keystore Path**: String filename of the private keystore file (PKCS12 only).

      * **Keystore Password**: The password for the private keystore.

      * **Key Alias**: The alias to your private key in the keystore.

      * **Key Password**: The private key password for the keystore.

   4. (Optional) Specify the **Timeout** value required for your configuration.

   5. In the **Action** column, click **Update**.

   6. Repeat this step as needed for additional RSA Servers.

5. (Optional) Only for custom plug-ins for WAM servers and the OAM bundled plug-in) On the **SP Adapter** tab, click **Add a new row to 'Protected Resource Mapping Table'** and enter the following information:

   * **Authentication Context**: This is part of the SAML assertion.

   * **Attribute Filter**: The names and values of attributes that the assertion must contain for this protected resource.

   * **Protected Resource**: The protected resource to be accessed if the authentication context and attribute filters in the assertion match the provided values.

   Click **Update** in the Action column. Repeat this step as needed.

6. Provide entries on the **Instance Configuration** tab, as described on the tab and in the table below.

   |   |                                                                                                                                                                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The selected WAM Plug-in Type might override optional andrequired fields.For example, if the selected **WAM Plug-in Type** is OAM, the **Agent Config Location** becomes a required field. Leaving this field blank generates an error message. |

   > **Collapse: Configuration Fields**
   >
   > | Field                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   > | ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | **WAM Plug-in Type**                 | The class name for the specific WAM implementation.	The WAM Plug-in Type determines optional and required fields.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   > | **Agent Name**                       | This value must match the value used when the third-party WAM Web Agent was configured.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   > | **Agent Secret**                     | This value must match the value used when the third-party WAM Web Agent was configured.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   > | **Agent Config Location**            | Required for OAM. This value must contain the full path to an XML network-configuration file generated by the access-management system.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   > | **Failover**                         | The default is false, indicating load balancing is enabled and user-session states and configuration data are shared among multiple WAM servers.Select **true** to enable failover, indicating that when one server fails, the next server is used.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   > | **Domain Name**                      | Enter the fully-qualified domain name for the Cookie Domain where the WAM session cookie is stored, preceded by a period.For example, `.pingidentity.com`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   > | **Cookie Path**                      | (Required) The default value is the root directory (`/`). Specify a different path for the WAM session cookie location, if necessary.You can find more details in WAM Server documentation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   > | **Protected Resource**               | (Required) The default value is all files in the root directory (`/*`). Specify a different path to the resources in the protected realm, if necessary.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   > | **Error URL**                        | Enter a URL for redirecting the user if there are errors. For example, incorrect parameters in the link.This URL can contain query parameters. The URL has an `errorMessage` query parameter appended to it, which contains a brief description of the error that happened. The error page can optionally display this message on the screen to provide guidance on remedying the problem.When using the `errorMessage` query parameter in a custom error page, adhere to Web application security best practices to guard against common content injection vulnerabilities.If no URL is specified, the appropriate default error landing page appears. Learn more in [Customizable user-facing pages](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_custom_user_facing_pages.html) in the PingFederate documentation.	If you define an error redirect URL, errors are sent to the error URL and logged in the PingFederate server log, but not the PingFederate audit log. |
   > | **User Identifier**                  | (Required) Defines which attribute parsed from the WAM session cookie is the user identifier for use in the assertion.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
   > | **Session Token Name**               | (Required) The WAM session cookie name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   > | **Session Token LOGGEDOFF Value**    | (Required) The value representing a logged-out session token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   > | **HTTP Only**                        | Enable this option to set the WAM Session Cookie as HTTP Only.If this option is enabled, the browser will send the WAM Session Cookie through HTTP or HTTPS.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   > | **Secure**                           | Enable this option to set WAM Session Cookie as secure.If this option is enabled, the browser sends the WAM Session Cookie through HTTPS only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   > | **PingFederate Base URL**            | The base URL for PingFederate. If specified, this value is used for creating the return URL if the **Cookie Provider URL** is being used.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   > | **Authorization Error URL**          | The URL to redirect for authorization errors.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   > | **Cookie Provider URL**              | The URL for the cookie provider where PingFederate should redirect the request if the WAM session cookie is in a separate domain.This service must be protected by WAM and redirect back to the PingFederate `resumePath`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   > | **Cookie Provider Target Parameter** | The name of the parameter used to send the return URL for the cookie provider.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   > | **Authentication Service URL**       | The URL to which the user is redirected for an SSO event.This URL overrides the Target Resource, which is sent as a parameter to the Authentication Service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   > | **Authentication Scheme Secret**     | (Required, except for RSA) The shared secret between the adapter and the custom authentication scheme deployed on the WAM server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   > | **Per-Adapter SLO URL**              | Enter a URL to use as the redirect target during SLO for this adapter instance, instead of the default value from PingFederate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   > | **Account Link Service**             | The URL for the Account Linking Service.This service must be protected by the WAM Web Agent and redirect back to the PingFederate `resumePath`.The local user id is obtained from the WAM session cookie.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

   ![A screenshot that shows the advanced WAM SP Adapter settings.](_images/pwt1563995794959.jpg)

7. (Optional) Click **Show Advanced Fields** to configure how to send extended attributes or to specify OpenToken configuration values or settings.

   Learn more in [Configuring an OpenToken SP Adapter instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_config_opentoken_sp_adapt_instance.html) in the PingFederate documentation.

   |   |                                                                                                                                                                                 |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you want to configure the use of OpenToken as part of the WAM adapter configuration, complete the fields as described on the **IdP Adapter** tab and in the following table. |

   You can change default values or settings, depending on your network configuration and other requirements at your site.

   > **Collapse: Advanced Fields**
   >
   > | Field                          | Description                                                                                                                                                                                                                                                 |
   > | ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | **Send Extended Attributes**   | The method of sending extended attributes. These attributes can be sent along with the request through browser cookies, query parameters, or as an encrypted token.	Learn more about defining the attributes on the Extended Contract tab in step 10.       |
   > | **OpenToken Transfer Method**  | Specifies how the OpenToken is transferred. Select one of the following options:- Through a cookie
   >
   > - As a query parameter
   >
   > - Through Form Post                                                                                                             |
   > | **OpenToken Name**             | The name of the cookie or request attribute that contains the OpenToken. This name should be unique for each adapter instance.                                                                                                                              |
   > | **OpenToken Password**         | The password used for encrypting extended attributes.	This password is also used to generate the configuration file that the OpenToken agent uses. You must configure a value for the OpenToken Password even if the OpenToken Cipher Suite is set to NULL. |
   > | **OpenToken Cipher Suite**     | The algorithm, cipher mode, and key size to use for token encryption.                                                                                                                                                                                       |
   > | **OpenToken Cookie Domain**    | The server domain, preceded by a period.For example, `.example.com`.If you don't specify a domain, the value is obtained from the request.                                                                                                                  |
   > | **OpenToken Cookie Path**      | The path for the cookie that contains the OpenToken.                                                                                                                                                                                                        |
   > | **OpenToken Token Lifetime**   | The duration (in seconds) during which the OpenToken is valid. Range is 1 - 28800.                                                                                                                                                                          |
   > | **OpenToken Session Lifetime** | The duration (in seconds) during which the OpenToken can be re-issued without authentication. Range is 1 - 259200.                                                                                                                                          |
   > | **Not Before Tolerance**       | The amount of time (in seconds) to allow for clock skew between servers. Range is 0 - 3600.                                                                                                                                                                 |
   > | **Session Cookie**             | If selected, OpenToken is set as a session cookie (rather than a persistent cookie).Applies only if the **OpenToken Transfer Method** is set as `Cookie`.                                                                                                   |
   > | **Secure Cookie**              | If selected, the OpenToken cookie is set only if the request is on a secure channel (https).Applies only if the OpenToken Transfer Method is set as 'Cookie'.                                                                                               |
   > | **Set WAM Cookie**             | If cleared, the WAM Cookie isn't set in the browser.                                                                                                                                                                                                        |
   > | **Add WAM Token**              | If selected, adds the WAM session token to extended attributes in OpenToken.You can only use this flag if you're sending extended attributes through OpenToken.                                                                                             |
   > | **Encode Token**               | Select this checkbox to URL encode the token string if the WAM provider requires it.                                                                                                                                                                        |
   > | **Idle Timeout**               | The idle timeout (in seconds). This value can be used by the specific plugin while creating the session if required.                                                                                                                                        |
   > | **Max Timeout**                | The max timeout (in seconds). This value can be used by the specific plugin while creating the session.                                                                                                                                                     |

8. Click **Next**.

9. On the **Actions** tab, click **Test Connection** to validate the WAM configuration.

   |   |                                                                                                                                                                                                                |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you're using an OpenToken Adapter Configuration, click the **Invoke Download** link and then click **Export** to download the `agent-config.txt` properties to a directory that the WAM Web Agent can read. |

10. On the **Extended Contract** tab, add any attributes you want to include in the request header. Click **Next**.

11. On the **Summary** tab, check and save your configuration.

    ### Choose from:

    * For PingFederate 10.1 or later: click **Save**.

    * For PingFederate 10.0 or earlier: click **Done**. On the **Manage SP Adapter Instances** tab, click **Save**.

---

---
title: Configuring the IdP token processor
description: If you are using PingFederate as an IdP server, configure the Token Processor using the following steps:
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_token_translator:pf_wam_tt_configuring_the_idp_token_processor
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_token_translator/pf_wam_tt_configuring_the_idp_token_processor.html
llms_txt: https://docs.pingidentity.com/integrations/webAccessManagement/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring the IdP token processor

## About this task

If you are using PingFederate as an IdP server, configure the Token Processor using the following steps:

|   |                                                                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You must first create a third-party WAM Web Agent within your WAM tool. Several properties used to configure the agent are then used on the Instance Configuration screen. Refer to your WAM documentation for details on agent configuration. |

## Steps

1. Log on to the PingFederate administrative console and click **Token Processors** under Application Integration Settings in the IdP Configuration section of the Main Menu.

   If you don't see **Token Processors** on the Main Menu, enable WS-Trust under Server Settings on the Roles & Protocols screen by selecting WS-Trust for the IdP role.

   |   |                                                                                                                                                                                                                            |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To enable token exchange, you may be prompted to provide SAML 1.x and SAML 2.0 federation identifiers for the STS on the Federation Info screen. Refer to the Federation Info screen's **Help** page for more information. |

2. On the Manage Token Processor Instances screen, click **Create New Instance**.

3. On the Type screen, enter an Instance Name and Instance Id.

   The Name is any you choose for identifying this instance. The ID is used internally and may not contain spaces or non-alphanumeric characters.

4. Select WAM Token Processor 2.0 as the Type and click **Next**.

   |   |                                                                                                                                                                                                                                            |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If you are configuring the adapter for a custom plug-in (not bundled with this kit), then continue to step 5. If you are configuring the RSA Dispatcher server, then continue with step 6. If you are configuring OAM, continue at step 7. |

   ![wco1563995802333](_images/wco1563995802333.jpg)

5. (Only for custom plug-ins for WAM servers other than OAM or RSA) On the Instance Configuration screen, click **Add a new row to 'WAM Server'** and provide the following information into the table:

   1. Enter the Hostname or the IP address where the WAM server is running.

   2. Specify the remaining WAM server values required for your configuration.

   3. Click **Update** in the Action column.

   4. Repeat this step as needed, for additional WAM plug-ins.

      Skip the next step.

6. (Only for the RSA bundled plug-in) On the Instance Configuration screen, click **Add a new row to 'RSA AM Dispatcher Server'** and provide the following information in the table:

   |   |                                                        |
   | - | ------------------------------------------------------ |
   |   | You must specify at least one RSA AM Dispatcher Server |

   1. Enter the Hostname or the IP address and the (optional) Dispatcher Port where the RSA AM Dispatcher server is running.

      |   |                                                                                                                                                                                              |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | You must specify the authentication method that is used by the dispatcher server. If you have specified multiple dispatcher servers, each server can have individual authentication methods. |

   2. Specify the Authentication Type used by the RSA Dispatcher Server.

      * **Clear** – clear text, no encryption

      * **Anon** – anonymous SSL, SSL encryption only

      * **Auth** – mutually authenticated SSL, SSL encryption with certificate-based encryption

   3. If the selected Authentication Type is **Auth**, you must specify the following RSA server values:

      * **Keystore Path** – String filename of the private Keystore file (PKCS12 only)

      * **Keystore Password** – password for the private Keystore

      * **Key Alias** – the alias to your private key in the Keystore

      * **Key Password** – private Key Password for Keystore

   4. (Optional) Specify the Timeout value required for your configuration.

   5. Click **Update** in the Action column.

   6. Repeat this step as needed for additional RSA Servers.

7. Provide entries on the Instance Configuration screen, as described on the screen and in the following table.

   |   |                                                                                                                                                                                                                                   |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | selected WAM Plug-in Type may override optional/required fields. For example, if the selected WAM Plug-in Type is `OAM`, the Agent Config Location becomes a required field. Leaving this field blank generates an error message. |

   | Field                         | Description                                                                                                                                                                                                                                          |
   | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | WAM Plug-in Type              | Class name for the specific WAM implementation.&#xA;&#xA;WAM Plug-in Type determines optional/required fields.                                                                                                                                       |
   | Agent Name                    | This value must match the value used when the third-party WAM Web Agent was configured.                                                                                                                                                              |
   | Agent Secret                  | This value must match the value used when the third-party WAM Web Agent was configured.                                                                                                                                                              |
   | Agent Config Location         | Required for OAM, this value must contain the full path to an XML network-configuration file generated by the access-management system.                                                                                                              |
   | Failover                      | The default is false, indicating load balancing is enabled and user-session states and configuration data are shared among multiple WAM servers. Select **true** to enable failover, indicating that when one server fails, the next server is used. |
   | Protected Resource            | (Required) All files in the root directory (/\*) is the default. Specify a different path to the resources in the protected realm, if necessary.                                                                                                     |
   | User Identifier               | (Required) Defines which attribute that is parsed from the WAM session token is the user identifier for use in the assertion.                                                                                                                        |
   | Session Token LOGGEDOFF Value | (Required) Value representing a logged-out session token.                                                                                                                                                                                            |
   | Repad Token String            | Enable this to pad the incoming session token string for Base64 encoding (if required).                                                                                                                                                              |

8. Click **Next**.

9. (Optional) On the Token Attributes screen, select any or all attributes whose value you want to mask in the PingFederate log file.

   For more information about this screen, see the PingFederate *Administrator's Manual*. More information is available on the **Help** page.

10. Click **Next**.

11. On the Summary screen, verify that the information is correct and click **Done**.

12. On the Manage Token Processor Instances screen, click **Save**.

---

---
title: Configuring the SP token generator
description: If you are using PingFederate as a Service Provider (SP), configure the Token Generator using the following steps:
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_token_translator:pf_wam_tt_configuring_the_sp_token_generator
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_token_translator/pf_wam_tt_configuring_the_sp_token_generator.html
llms_txt: https://docs.pingidentity.com/integrations/webAccessManagement/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring the SP token generator

## About this task

If you are using PingFederate as a Service Provider (SP), configure the Token Generator using the following steps:

|   |                                                                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You must first create a third-party WAM Web Agent within your WAM tool. Several properties used to configure the agent are then used on the Instance Configuration screen. Refer to your WAM documentation for details on agent configuration. |

## Steps

1. Log on to the PingFederate administrative console and click **Token Generators** under Application Integration Settings in the SP Configuration section of the Main Menu.

   If you do not see **Token Generators** on the Main Menu, enable WS-Trust under Server Settings on the Roles & Protocols screen by selecting WS-Trust for the SP role.

   |   |                                                                                                                                                                                                                            |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To enable token exchange, you may be prompted to provide SAML 1.x and SAML 2.0 federation identifiers for the STS on the Federation Info screen. Refer to the Federation Info screen's **Help** page for more information. |

2. On the Manage Token Generator Instances screen, click **Create New Instance**.

3. On the Type screen, enter an Instance Name and Instance Id.

   The Name is any you choose for identifying this instance. The ID is used internally and may not contain spaces or non-alphanumeric characters.

4. Select WAM Token Generator 2.0 as the Type and click **Next**.

   |   |                                                                                                                                                                                                                                            |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If you are configuring the adapter for a custom plug-in (not bundled with this kit), then continue to step 5. If you are configuring the RSA Dispatcher server, then continue with step 6. If you are configuring OAM, continue at step 7. |

   ![wpc1563995803935](_images/wpc1563995803935.jpg)

5. (Only for custom plug-ins for WAM servers other than OAM or RSA) On the Instance Configuration screen, click **Add a new row to 'WAM Server'** and provide the following information into the table:

   1. Enter the Hostname or the IP address where the WAM server is running.

   2. Specify the remaining WAM server values that are required for your configuration.

   3. Click **Update** in the Action column.

   4. Repeat this step as needed, for additional WAM plug-ins.

      Skip the next step.

6. (Only for the RSA bundled plug-in) On the Instance Configuration screen, click **Add a new row to 'RSA AM Dispatcher Server'** and provide the following information in the table:

   |   |                                                        |
   | - | ------------------------------------------------------ |
   |   | You must specify at least one RSA AM Dispatcher Server |

   1. Enter the Hostname or the IP address and the (optional) Dispatcher Port where the RSA AM Dispatcher server is running.

      |   |                                                                                                                                                                                              |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | You must specify the authentication method that is used by the dispatcher server. If you have specified multiple dispatcher servers, each server can have individual authentication methods. |

   2. Specify the Authentication Type used by the RSA Dispatcher Server.

      * **Clear** – clear text, no encryption

      * **Anon** – anonymous SSL, SSL encryption only

      * **Auth** – mutually authenticated SSL, SSL encryption with certificate-based encryption

   3. If the selected Authentication Type is **Auth**, you must specify the following RSA server values:

      * **Keystore Path** – String filename of the private Keystore file (PKCS12 only)

      * **Keystore Password** – password for the private Keystore

      * **Key Alias** – the alias to your private key in the Keystore

      * **Key Password** – private Key Password for Keystore

   4. (Optional) Specify the Timeout value required for your configuration.

   5. Click **Update** in the Action column.

   6. Repeat this step as needed for additional RSA Servers.

7. Provide entries on the Instance Configuration screen, as described on the screen and in the table below.

   |   |                                                                                                                                                                                                                                       |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The selected WAM Plug-in Type may override optional/required fields. For example, if the selected WAM Plug-in Type is `OAM`, the Agent Config Location becomes a required field. Leaving this field blank generates an error message. |

   | Field                         | Description                                                                                                                                                                                                                                          |
   | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | WAM Plug-in Type              | Class name for the specific WAM implementation.&#xA;&#xA;WAM Plug Type determines optional/required fields.                                                                                                                                          |
   | Agent Name                    | This value must match the value used when the third-party WAM Web Agent was configured.                                                                                                                                                              |
   | Agent Secret                  | This value must match the value used when the third-party WAM Web Agent was configured.                                                                                                                                                              |
   | Agent Config Location         | Required for OAM, this value must contain the full path to an XML network-configuration file generated by the access-management system.                                                                                                              |
   | Failover                      | The default is false, indicating load balancing is enabled and user-session states and configuration data are shared among multiple WAM servers. Select **true** to enable failover, indicating that when one server fails, the next server is used. |
   | Protected Resource            | (Required) All files in the root directory (/\*) is the default. Specify a different path to the resources in the protected realm, if necessary.                                                                                                     |
   | User Identifier               | (Required) Defines which attribute that is parsed from the WAM session token is the user identifier for use in the assertion.                                                                                                                        |
   | Session Token LOGGEDOFF Value | (Required) Value representing a logged out session token.                                                                                                                                                                                            |
   | Authentication Scheme Secret  | (Required, except for RSA) The shared secret between the adapter and the custom authentication scheme deployed on the WAM server.                                                                                                                    |
   | Encode Token (Advanced Field) | The default is false. Check this box to url encode token string (if required).                                                                                                                                                                       |

8. Click **Next**.

9. (Optional) On the Extended Contract screen, add attributes you expect to retrieve in addition to the SAML subject (user ID). For more information, see [Extending an SP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_sessioncreationadaptertasklet_createadaptercontractstate.html) in the PingFederate documentation.

10. Click **Next**.

11. On the Summary screen, verify that the information is correct and click **Done**.

12. On the Manage Token Generator Instances screen, click **Save**.

---

---
title: Creating a custom authentication scheme for OAM
description: The Token Generator uses a custom authentication scheme when creating a WAM session and validates authentication requests coming from PingFederate. This section describes how to deploy the OAM-compatible Java-based PingFederate Custom Authentication Scheme.
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_token_translator:pf_wam_tt_creating_a_custom_authentication_scheme_for_oam
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_token_translator/pf_wam_tt_creating_a_custom_authentication_scheme_for_oam.html
llms_txt: https://docs.pingidentity.com/integrations/webAccessManagement/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Creating a custom authentication scheme for OAM

## About this task

The Token Generator uses a custom authentication scheme when creating a WAM session and validates authentication requests coming from PingFederate. This section describes how to deploy the OAM-compatible Java-based PingFederate Custom Authentication Scheme.

## Steps

1. Import the `<token_translator_install_dir>/dist/PingCustomAuthPlugin.jar` file into the OAM.

   The `PingCustomAuthPlugin.jar` file is a custom authentication scheme that supports OAM.

2. Configure your Access Server to use the custom authentication plug-in by creating or modifying a custom authentication scheme.

   Learn more in the [Oracle Support documentation](https://docs.oracle.com/cd/E21764_01/).

   |   |                                                                                                                                         |
   | - | --------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The secret you specify when creating the custom authentication scheme must match the secret stored in the PingFederate Token Generator. |

---

---
title: Creating a Custom Authentication Scheme for OAM
description: The SP Adapter uses a custom authentication scheme when creating a WAM session and validates authentication requests coming from PingFederate. This section describes how to deploy the OAM-compatible Java-based PingFederate Custom Authentication Scheme.
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_integration_kit:pf_wam_ik_creating_a_custom_authentication_scheme_for_oam
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_integration_kit/pf_wam_ik_creating_a_custom_authentication_scheme_for_oam.html
llms_txt: https://docs.pingidentity.com/integrations/webAccessManagement/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 18, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Creating a Custom Authentication Scheme for OAM

## About this task

The SP Adapter uses a custom authentication scheme when creating a WAM session and validates authentication requests coming from PingFederate. This section describes how to deploy the OAM-compatible Java-based PingFederate Custom Authentication Scheme.

## Steps

1. Import the `<integration_kit_install_dir>/dist/PingCustomAuthPlugin.jar` into the OAM.

   The `PingCustomAuthPlugin.jar` file is a custom authentication scheme that supports OAM.

2. Configure your Access Server to use the custom authentication plug-in by creating or modifying a custom authentication scheme.

   To learn more, refer to [Creating Custom Authentication Plug-ins](https://docs.oracle.com/cd/E21764_01/dev.1111/e12491/authnapi.htm#AIDEV187) in the Oracle documentation.

   |   |                                                                                                                                    |
   | - | ---------------------------------------------------------------------------------------------------------------------------------- |
   |   | The secret you specify when creating the custom authentication scheme must match the secret stored in the PingFederate SP Adapter. |

---

---
title: Custom WAM plug-in installation
description: This section describes how to deploy a custom WAM plug-in for both IdP and SP adapters.
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_integration_kit:pf_wam_ik_custom_wam_plug_in_installation
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_integration_kit/pf_wam_ik_custom_wam_plug_in_installation.html
llms_txt: https://docs.pingidentity.com/integrations/webAccessManagement/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 18, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result
---

# Custom WAM plug-in installation

## About this task

This section describes how to deploy a custom WAM plug-in for both IdP and SP adapters.

## Steps

1. If you are creating a WAM plug-in for a third-party WAM product not bundled with this kit, you must complete the tasks in the WAM plug-in SDK `<integration_kit_install_dir>/sdk/README.txt` file.

   |   |                                                                                                                                                          |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Contact the third-party vendor support department to obtain required third-party API libraries for creating a WAM plug-in to interact with PingFederate. |

2. After completing the tasks in the WAM plug-in SDK `README.txt` file, copy the resultant WAM plug-in output JAR file (`<integration_kit_install_dir>SDK/lib/pf-<WAM_TYPE>-plugin.jar`) to the `<PF-install>/pingfederate/server/default/deploy` directory.

## Result

The WAM Integration Kit requires a plug-in to connect with a specific WAM product (see the WAM plug-in SDK in the distribution package for sample code and more details on building the plug-in). The SDK consists of build scripts, libraries, and sample code.

|   |                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The WAM plug-in SDK is designed specifically to connect the WAM Integration Kit with a third-party WAM product, using an API provided by the vendor. |

---

---
title: Custom WAM plug-in installation
description: This section describes how to deploy a custom WAM plug-in for both Token Processors and Token Generators.
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_token_translator:pf_wam_tt_custom_wam_plug_in_installation
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_token_translator/pf_wam_tt_custom_wam_plug_in_installation.html
llms_txt: https://docs.pingidentity.com/integrations/webAccessManagement/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result
---

# Custom WAM plug-in installation

## About this task

This section describes how to deploy a custom WAM plug-in for both Token Processors and Token Generators.

## Steps

1. If you are creating a WAM plug-in for any third-party WAM product not bundled with this kit, you must complete the tasks in the WAM plug-in SDK `README.txt` file located in the `<token_translator_install_dir>/sdk` directory.

   |   |                                                                                                                                                              |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Contact the third-party vendor support department to obtain required third-party WAM API libraries for creating a WAM plug-in to interact with PingFederate. |

2. If you are deploying for a third-party WAM product, copy the resultant WAM plug-in output JAR file `pf-<WAM_TYPE>-plugin.jar` from the `<token_translator_install_dir>/sdk/samples/<WAM_TYPE>` directory into the `<PF_install>/pingfederate/server/default/deploy` directory.

## Result

The WAM Token Translator requires a plug-in to connect with a specific WAM product (see the WAM plug-in SDK in the distribution package for sample code and more details on building the plug-in).

|   |                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The WAM plug-in SDK is designed specifically to connect the WAM Token Translator with a third-party WAM product, using an API provided by the vendor. |

---

---
title: Download manifest
description: The following files are included in the .zip archive:
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_integration_kit:pf_wam_ik_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_integration_kit/pf_wam_ik_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/webAccessManagement/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 18, 2024
---

# Download manifest

The following files are included in the `.zip` archive:

* `ReadMeFirst.pdf` – contains links to this online documentation

* `/legal` – contains this document:

  * `Legal.pdf` – copyright and license information

* `/dist` – contains libraries needed to run the adapter:

  * `pf-wam-adapter-2.0.jar` – the WAM Adapter JAR file

  * `opentoken-adapter-2.5.1.jar` – OpenToken Adapter JAR file

* `/dist/oam` – contains Oracle Access Manager libraries needed to run the adapter:

  * `pf-oam-plugin.jar` – Pre-built OAM-compatible WAM plug-in JAR file

  * `PingCustomAuthPlugin.jar` – a Java-based PingFederate Custom Authentication Scheme

* `/dist/rsa` – contains RSA libraries needed to run the adapter:

  * `pf-rsa-plugin.jar` – Pre-built RSA-compatible WAM plug-in JAR file

  * `axm-runtime-api-6.1.4.jar `- RSA API library

  * `jsafeFIPS-6.1.jar` – RSA API library

  * `jsafeJCEFIPS-6.1.jar` – RSA API library

* `/sdk` – contains build scripts, documents, libraries, and sample code to build a WAM plug-in:

  * `README.txt` – contains instructions for creating a third-party WAM plug-in to interact with PingFederate.

  * `/docs` – contains documentation on how to build a WAM plug-in.

  * `/lib` – contains libraries and supporting files needed to build a WAM plug-in.

  * `/samples` – contains sample code used to build a WAM plug-in.

---

---
title: Download manifest
description: The distribution .zip archive for the WAM Token Translator contains the following:
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_token_translator:pf_wam_tt_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_token_translator/pf_wam_tt_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/webAccessManagement/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
---

# Download manifest

The distribution `.zip` archive for the WAM Token Translator contains the following:

* `ReadMeFirst.pdf` – contains links to this online documentation

* /legal – contains this document:

  * Legal.pdf – copyright and license information

* `/dist` – contains libraries needed to run the Token Translator:

  * `pf-wam-token-translator-2.0.jar` – the WAM Token Translator JAR file

  * `opentoken-adapter-2.5.1.jar` – OpenToken Adapter JAR file

* `/dist/oam` – contains Oracle Access Manager libraries needed to run the adapter:

  * `pf-oam-plugin.jar` – Pre-built OAM-compatible WAM plug-in JAR file

  * `PingCustomAuthPlugin.jar` – a Java-based PingFederate Custom Authentication Scheme

* `/dist/rsa` – contains RSA libraries needed to run the adapter:

  * `pf-rsa-plugin.jar` – Pre-built RSA-compatible WAM plug-in JAR file

  * `axm-runtime-api-6.1.4 `- RSA API library

  * `jsafeFIPS-6.1.jar` – RSA API library

  * `jsafeJCEFIPS-6.1.jar` – RSA API library

* `/sdk` – contains build scripts, documents, libraries, and sample code to build a WAM plug-in:

  * `README.txt `– contains documentation on how to build a WAM plug-in

  * `/docs` – contains documentation on how to build a WAM plug-in

  * `/lib` – contains libraries and supporting files needed to build WAM plug-in

  * `/samples` – contains sample code used to build a WAM plug-in

---

---
title: IdP deployment note
description: "The adapter configuration supports a \"login URL\" parameter. If the WAM session cookie is not found in the request, then the PingFederate server redirects the request to the URL page along with the relative resumePath, which is generated from PingFederate and intended for asynchronous communication between the adapter and the external application. (The state is saved in PingFederate, and processing is resumed when the application redirects to the resumePath.)"
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_integration_kit:pf_wam_ik_idp_deployment_note
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_integration_kit/pf_wam_ik_idp_deployment_note.html
llms_txt: https://docs.pingidentity.com/integrations/webAccessManagement/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 18, 2024
---

# IdP deployment note

The adapter configuration supports a "login URL" parameter. If the WAM session cookie is not found in the request, then the PingFederate server redirects the request to the URL page along with the relative `resumePath,` which is generated from PingFederate and intended for asynchronous communication between the adapter and the external application. (The state is saved in PingFederate, and processing is resumed when the application redirects to the `resumePath`.)

The login URL page can authenticate the user and redirect the request back to PingFederate. An example of a JSP code snippet for redirecting the request is shown below.

```javascript
<%
  String resumePath = request.getParameter("resumePath");
    if(resumePath != null) {
      resumePath = <PingFed_URL> + resumePath; (1)
      response.sendRedirect(resumePath);
    }
%>
```

|       |                                                                        |
| ----- | ---------------------------------------------------------------------- |
| **1** | `<PingFed_URL>` is the fully-qualified URL of the PingFederate server. |

---

---
title: IdP process overview
description: The following figure illustrates the request flow and how the WAM IdP Adapter is leveraged in generating a SAML/WS-Federation assertion using a WAM session cookie.
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_integration_kit:pf_wam_ik_idp_process_overview
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_integration_kit/pf_wam_ik_idp_process_overview.html
llms_txt: https://docs.pingidentity.com/integrations/webAccessManagement/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 18, 2024
section_ids:
  processing-steps: Processing Steps
---

# IdP process overview

The following figure illustrates the request flow and how the WAM IdP Adapter is leveraged in generating a SAML/WS-Federation assertion using a WAM session cookie.

![vwa1563995785356](_images/vwa1563995785356.jpg)

## Processing Steps

1. The user's browser attempts to access the IdP application. The third-party WAM Web Agent intercepts the request and asks for the user's identity. The user enters the requested credentials and submits the login page.

2. The WAM Server validates the user's credentials and creates a WAM session cookie. The user now has access to the application.

3. The user clicks a link that initiates an SSO transaction to the partner application. The request is redirected to the PingFederate IdP Server. The WAM session cookie generated in step 2 is included in the request.

4. The PingFederate WAM IdP Adapter uses the WAM plug-in to decrypt the WAM session cookie and then transfers the attributes to the PingFederate IdP Server. You can create an attribute contract to map the WAM session cookie and response attributes. For more information, see [Defining an attribute contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_usersessioncreationtasklet_createattributecontractstate.html) in the PingFederate documentation.

5. The PingFederate IdP server generates a SAML/WS-Federation assertion and redirects the request, with the assertion, back through the user's browser to the SP site.

---

---
title: Install or upgrade the adapter
description: This topic describes how to install the WAM Integration Kit for both the IdP and the SP adapters.
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_integration_kit:pf_wam_ik_install_or_upgrade_the_adapter
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_integration_kit/pf_wam_ik_install_or_upgrade_the_adapter.html
llms_txt: https://docs.pingidentity.com/integrations/webAccessManagement/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 18, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Install or upgrade the adapter

## About this task

This topic describes how to install the WAM Integration Kit for both the IdP and the SP adapters.

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | If you have already deployed version 2.5.1 or later of the OpenToken Adapter, skip steps 1-3 in the following procedure. |

## Steps

1. Download the WAM Integration Kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/wam-integration-kit).

2. Stop the PingFederate server if it is running.

3. Delete the following files from the `<PF_install>/pingfederate/server/default/deploy` directory:

   * The WAM adapter JAR file (`pf-wam-adapter-<version>.jar`)

   * Any existing OpenToken Adapter files (`opentoken*.jar`)

     * If the adapter JAR filename indicates version 2.1 or earlier, delete the supporting library `opentoken-java-1.x.jar`.

4. Unzip the integration-kit distribution file and copy the following files from the `/dist` directory to the `<PF_install>/pingfederate/server/default/deploy` directory.

   * `opentoken-adapter-2.5.1.jar`

   * `pf-wam-adapter-2.0.0.jar`

5. If you are running PingFederate 6.0 as a Windows service, add the following line to the `Java Library Path` section of the `pingfederate/sbin/wrapper/PingFederateService.conf` file:

   ```properties
   wrapper.java.library.path.append_system_path=true
   ```

6. Start the PingFederate server.

---

---
title: Known issues and limitations
description: Known Limitations
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_token_translator:pf_wam_tt_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_token_translator/pf_wam_tt_known_issues_and_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/webAccessManagement/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
---

# Known issues and limitations

**Known Limitations**

* Due to a limitation with PingFederate 8.1 and earlier versions, when configuring two SP connections with the same provisioner, the second connection built may be pre-populated with the channel from the first connection. To avoid conflicts, delete this pre-populated channel and create a unique channel for each connection.

---

---
title: OAM-specific configuration
description: When configuring the OAM adapter, the following values are needed:
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_integration_kit:pf_wam_ik_oam_specific_configuration
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_integration_kit/pf_wam_ik_oam_specific_configuration.html
llms_txt: https://docs.pingidentity.com/integrations/webAccessManagement/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 18, 2024
---

# OAM-specific configuration

When configuring the OAM adapter, the following values are needed:

| Field                         | Description                                                                                                                | Example Value                                  |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| Cookie Path                   | Relative path in the URL where the cookie is active.                                                                       | `/`                                            |
| Protected Resource            | The path (and optionally, the hostname) that defines the protected resource. This value comes from your OAM configuration. | `http://<OAM Host Identifier>/<Resource Path>` |
| Error URL                     | Optional field containing a URL used as a redirection target in the event of an error during SSO when using this adapter.  |                                                |
| User Identifier               | HTTP header used to identify the end userID.                                                                               | `OAM_REMOTE_USER`                              |
| Session Token Name            | The name of the encrypted cookie used for SSO.                                                                             | `ObSSOCookie`                                  |
| Session Token Loggedoff Value | The value the Session Token should be set to when the user has logged out of OAM.                                          | `loggedoutcontinue`                            |

|   |                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The above values are examples and are dependent on the OAM environment. Ask your Oracle administrator for the values required in your environment. |

Learn more about this configuration in the [Oracle Access Manager documentation](https://docs.oracle.com/cd/E52734_01/oam/index.html).

---

---
title: Overview of Web Access Management integrations
description: The PingFederate Web Access Management (WAM) Integration Kit allows developers to integrate their applications with a PingFederate server acting as either an identity provider (IdP) or a Service Provider (SP).
component: webAccessManagement
page_id: webAccessManagement::pf_is_overview_of_wam_integrations
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/pf_is_overview_of_wam_integrations.html
llms_txt: https://docs.pingidentity.com/integrations/webAccessManagement/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 12, 2024
section_ids:
  pingfederate-web-access-management-integration-kit: PingFederate Web Access Management Integration Kit
  pingfederate-web-access-management-token-translator: PingFederate Web Access Management Token Translator
---

# Overview of Web Access Management integrations

## PingFederate Web Access Management Integration Kit

The PingFederate Web Access Management (WAM) Integration Kit allows developers to integrate their applications with a PingFederate server acting as either an identity provider (IdP) or a Service Provider (SP).

## PingFederate Web Access Management Token Translator

The PingFederate Web Access Management (WAM) Token Translator provides a Token Processor and a Token Generator for use with the PingFederate WS-Trust Security Token Service (STS).

---

---
title: SP deployment notes
description: The following notes provide additional information for using the WAM Integration Kit as an SP:
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_integration_kit:pf_wam_ik_sp_deployment_notes
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_integration_kit/pf_wam_ik_sp_deployment_notes.html
llms_txt: https://docs.pingidentity.com/integrations/webAccessManagement/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 18, 2024
---

# SP deployment notes

The following notes provide additional information for using the WAM Integration Kit as an SP:

* The WAM SP Adapter relies on a custom authentication scheme to validate the authentication request coming from the PingFederate SP Adapter. The secret specified in the SP Adapter is verified against the one configured with the scheme. You can create custom authentication schemes for specific WAM systems using their API.

  The authentication scheme for OAM is included in the samples folder at the following location: `<integration_kit_install_dir>` `/sdk/samples/oam/PingCustomAuthPlugin.java`

* To support Account Linking, the Account Linking Service has to be implemented and then protected by the WAM Web Agent. This could be done as a `JSP` page that redirects back to PingFederate. The relative `resumePath` is sent as part of the request and the `JSP` page needs to create the absolute URL and redirect, as shown below.

  ```javascript
  <%
    String resumePath = request.getParameter("resumePath");
      if(resumePath != null) {
        resumePath = <PingFed_URL> + resumePath; (1)
        response.sendRedirect(resumePath);
      }
  %>
  ```

  |       |                                                                                                                                                                                                                                                                                                                                  |
  | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | **1** | `<PingFed_URL>` is the fully-qualified URL of the PingFederate server.`resumePath` is generated from PingFederate and intended for asynchronous communication between the adapter and the external application. The state is saved in PingFederate and processing is resumed when the application redirects to the `resumePath`. |

  The WAM SP Adapter retrieves the user information from the WAM session cookie and resumes SSO.

---

---
title: SP process overview
description: The following figure illustrates the request flow and how the WAM SP Adapter leverages a SAML/WS-Federation assertion to create a WAM session cookie.
component: webAccessManagement
page_id: webAccessManagement:web_access_management_wam_integration_kit:pf_wam_ik_sp_process_overview
canonical_url: https://docs.pingidentity.com/integrations/webAccessManagement/web_access_management_wam_integration_kit/pf_wam_ik_sp_process_overview.html
llms_txt: https://docs.pingidentity.com/integrations/webAccessManagement/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 18, 2024
section_ids:
  processing-steps: Processing Steps
---

# SP process overview

The following figure illustrates the request flow and how the WAM SP Adapter leverages a SAML/WS-Federation assertion to create a WAM session cookie.

![ezn1563995791248](_images/ezn1563995791248.jpg)

## Processing Steps

1. The PingFederate SP server receives a SAML/WS-Federation assertion from the IdP.

2. PingFederate parses the assertion.

3. The WAM SP Adapter uses the WAM plug-in to create a WAM session cookie and embeds the cookie in the response.

4. A request containing the WAM session cookie is redirected to the browser.

5. The request is then redirected to the SP Application, which is protected by the third-party WAM Web Agent.

6. The third-party WAM Web Agent intercepts the request, extracts and validates the WAM session cookie, and allows access to the application.