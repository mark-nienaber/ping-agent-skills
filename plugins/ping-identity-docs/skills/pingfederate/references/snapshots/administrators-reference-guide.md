---
title: About Administration
description: This guide provides information about using PingFederate to deploy a secure internet single sign-on (SSO) solution based on the latest security and e-business standards.
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:pf_administrators_reference_guide
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/pf_administrators_reference_guide.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
---

# About Administration

This guide provides information about using PingFederate to deploy a secure internet single sign-on (SSO) solution based on the latest security and e-business standards.

Use this guide to learn about the following:

* [Attribute mapping expressions](pf_attribute_mapping_expressions.html)

* [Authentication policies](pf_authentication_policies.html)

* [Bundled adapters](pf_bundled_adapt.html)

* [Customer IAM configuration](pf_customer_iam_config.html)

* [Customizing assertions and authentication requests](pf_customiz_assert_and_auth_requests.html)

* [Fulfillment by datastore queries](pf_fulfill_by_datastore_queri.html)

* [IdP-to-SP bridging](pf_idp_to_sp_bridg.html)

* [Identity provider SSO configuration](pf_ident_provid_sso_config.html)

* [OAuth configuration](pf_oauth_config.html)

* [Security management](pf_security_management.html)

* [Self-service user account management](pf_self_service_user_account_management.html)

* [Service provider SSO configuration](pf_servic_provid_sso_config.html)

* [System administration](pf_sys_admin.html)

* [System settings](pf_system_settings.html)

* [Troubleshooting PingFederate](pf_troubleshooting.html)

* [WS-Trust STS configuration](pf_wstrust_sts_config.html)

---

---
title: About Configuration
description: All the pre-runtime architectural and setup tasks necessary to prepare the PingFederate server and its dependencies before it handles live traffic.
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:pf_about_configuration
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/pf_about_configuration.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# About Configuration

The Configuration section covers all the pre-runtime architectural and setup tasks necessary to prepare the PingFederate server and its dependencies before it handles live traffic.

This category includes initial setup, file-based configuration, core security establishment, data source linking, and policy infrastructure creation.

---

---
title: Accept Azure Primary Refresh Tokens
description: Primary Refresh Tokens (PRTs) are issued by Microsoft Entra to enable single sign-on (SSO) when Entra is your identity provider (IdP). PRTs are issued and verified only by Entra, and don't allow for offline verification. Learn more about PRTs in Understanding Primary Refresh Token in the Microsoft documentation.
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:pf_accept_azure_prt
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/pf_accept_azure_prt.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 29, 2026
section_ids:
  before-you-begin: Before you begin
  register-an-application-in-microsoft-entra: Register an application in Microsoft Entra
  create-an-oidc-idp-connection-in-pingfederate: Create an OIDC IdP Connection in PingFederate
  configure-browsers-to-accept-prts: Configure browsers to accept PRTs
---

# Accept Azure Primary Refresh Tokens

Primary Refresh Tokens (PRTs) are issued by Microsoft Entra to enable single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)* when Entra is your identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)*. PRTs are issued and verified only by Entra, and don't allow for offline verification. Learn more about PRTs in [Understanding Primary Refresh Token](https://learn.microsoft.com/en-us/entra/identity/devices/concept-primary-refresh-token) in the Microsoft documentation.

You can configure PingFederate to accept PRTs for workforce users by creating an OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)* IdP connection, with Entra as an external IdP.

This configuration has three main components:

1. Register an application in Microsoft Entra.

2. Create an IdP connection in PingFederate.

3. Configure user browsers to accept PRTs.

## Before you begin

For testing purposes, you should have a device connected to Entra as a joined device. Learn more in [Microsoft Entra joined devices](https://learn.microsoft.com/en-us/entra/identity/devices/concept-directory-join) in the Microsoft documentation.

You can test whether your device is joined by running `dsregcmd /status` in the command line. If your device is joined, it returns:

```shell
isDeviceJoined: YES
AzureAdPrt: YES
```

## Register an application in Microsoft Entra

Follow the steps in [Register an application with the Microsoft identity platform](https://learn.microsoft.com/en-us/graph/auth-register-app-v2) in the Microsoft documentation.

While registering an application, do the following so you can connect to PingFederate:

* Create a client secret and have it ready to copy into PingFederate.

* Add a redirect URI from PingFederate. You can find the Redirect URI in PingFederate on the **Summary & Activation** tab after you finish configuring the IdP connection.

## Create an OIDC IdP Connection in PingFederate

1. Follow the steps in [Creating an OpenID Connect IdP connection](pf_creating_oidc_idp_connection.html).

   While creating the connection, do the following to connect with your Entra application:

   * On the **General Info** tab, paste the **Client ID** and **Client Secret** values from your application.

   * On the **OpenID Provider Info** tab, add the following request parameter:

     | Name     | Type   | Value  |
     | -------- | ------ | ------ |
     | `prompt` | `text` | `none` |

     This prevents Entra from displaying the Microsoft sign-on page when PRT authorization fails.

2. If necessary, create an authentication policy for the new IdP connection. Learn more in [Defining authentication policies](pf_defining_auth_policies.html).

## Configure browsers to accept PRTs

The following table describes how to enable PRT authentication in various browsers:

| Browser            | Compatibility                                                                                                                | How to Enable                                                                                                                                                                    |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Chrome 111+        | Device-based Conditional Access                                                                                              | Enable the [CloudAPAuthEnabled](https://chromeenterprise.google/policies/#CloudAPAuthEnabled) registry                                                                           |
| Firefox 91+        | Device-based Conditional Access                                                                                              | 1. In the address bar, enter `about:preferences#privacy`.

2. Under the **Passwords** section, select **Allow Windows single sign-on for Microsoft, work, and school accounts**. |
| Microsoft Edge 85+ |                                                                                                                              | User must be signed on to the browser to pass device identity. This sign-on might not happen automatically if the device is a hybrid join.                                       |
| Safari             | Device-based Conditional Access. Can't satisfy the **Require approved client app** or **Require app protection** conditions. | No action needed                                                                                                                                                                 |

Learn more about [Conditional Access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/) in the Microsoft documentation.

After configuring your browser, you can test the connection by triggering an authentication flow on the joined device. Check the `audit.log` file to verify that authentication at the IdP connection succeeds.

---

---
title: Access token management
description: PingFederate supports multiple access token management (ATM) instances. You can configure different access token policies and attribute contracts for different OAuth clients. You can also control validation of access tokens to one or more resource servers.
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:pf_access_token_management
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/pf_access_token_management.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 3, 2024
---

# Access token management

PingFederate supports multiple access token management (ATM) instances. You can configure different access token policies and attribute contracts for different OAuth clients. You can also control validation of access tokens to one or more resource servers.

When defining an ATM instance, you can customize various settings, including token format, lifetime, session validation settings, and attribute contract for this instance. You can also limit the ATM instance to a list of resource URIs, a set of clients in an access control list (ACL), or both.

For example, you can use the ACL to limit which clients can obtain access tokens from a particular ATM instance. You can also add a resource server client to the ACL of multiple ATMs instances, so that only the resource server client can submit token validation requests for access tokens issued by those ATM instances.

When there are multiple ATM instances, OAuth clients can specify the desired ATM instance by providing the ATM ID (`access_token_manager_id`) , or a resource URI (`aud` or `resource`) parameter in their requests to the PingFederate OAuth authorization server at the `/as/authorization.oauth2` authorization endpoint, the `/as/token.oauth2` token endpoint, and the `/as/introspect.oauth2` introspection endpoint.

|   |                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------- |
|   | Clients can include multiple `resource` parameters, but only one `aud`. Otherwise, the two parameters behave the same. |

For resource server clients, you can configure on a per-client basis whether a resource server client must specify the desired ATM instance in its token validation requests at runtime. For more information, see [Configuring OAuth clients](pf_configuring_oauth_clients.html).

At runtime, the PingFederate OAuth authorization server uses the following rules to determine which ATM instances to use:

1. PingFederate limits the eligible ATM instances to those that are available in the context of the request. For most requests, these are instances that have an attribute mapping defined in the **Access Token Mapping** window. For OAuth Assertion Grant requests, it is the set of instances for which a mapping is defined in the IdP connection. If configured, the ACL can also limit which ATM instances are eligible.

2. If the request comes with an `access_token_manager_id`, `aud`, or `resource` parameter, PingFederate uses the information to determine the applicable ATM instance.

3. If the request does not come with either parameter, for OAuth clients supporting the OpenID Connect protocol by including the `openid` scope value, PingFederate uses the ATM instance specified by the OpenID Connect policy associated with the client. For resource server clients, you can optionally configure PingFederate to use any eligible ATM instances for the purpose of token validation.

4. If the request comes with neither of the two parameters nor the `openid` scope, PingFederate uses the default ATM instance of the client if configured, or the default ATM instance defined for the installation if eligible. For token validation requests, if resource server clients do not provide either the `access_token_manager_id`, `aud`, or `resource` parameter in their requests and the resource server clients have not been configured to validate against any eligible ATM instances, the same logic applies.

If no match can be found in the eligible list of ATMs, PingFederate aborts the request.

---

---
title: Accessing IdP connections
description: In the IdP Connections window, you can create or import a connection, or edit a recently modified connection by clicking on its connection name.
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:help_idpconnectionstasklet_connmgmtstate
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/help_idpconnectionstasklet_connmgmtstate.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Accessing IdP connections

In the **IdP Connections** window, you can create or import a connection, or edit a recently modified connection by clicking on its connection name.

## About this task

The **IdP Connections** window displays 20 connections at a time. As needed, use the pagination controls to navigate through the rest of your connections. You can also search connections by their names or connection IDs.

|   |                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------- |
|   | A connection is included in the search results so long as its name or ID is a partial, case-insensitive match to a search term. |

You can sort by connection name, partner connection ID, default virtual server ID, creation date, or last modified timestamps; narrow by protocol and status; and perform various connection-related tasks.

## Steps

1. Go to the **Authentication > Integration > IdP Connections**.

   | Choice                                                                        | Action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | Edit a connection                                                             | Select the connection by its name. For the setting you want to change, select the corresponding tab and follow the configuration wizard to complete the task.                                                                                                                                                                                                                                                                                                                                                                  |
   | Create a connection                                                           | Click **Create Connection**, then follow the configuration wizard to create a new connection to your identity provider (IdP) partner.                                                                                                                                                                                                                                                                                                                                                                                          |
   | Copy a connection                                                             | Click **Select action > Copy**, then follow the configuration wizard to create a new connection based on an existing (source) connection.This is most useful if the new connection and the source connection share many common setting values.                                                                                                                                                                                                                                                                                 |
   | Export a connection                                                           | Click **Select Action > Export Connection**, then save the XML file as prompted.This is useful in situations where you want to make a backup of a connection prior to making changes to it.                                                                                                                                                                                                                                                                                                                                    |
   | Import a connection                                                           | Click **Import Connection**, then follow the on-screen instructions to complete the task.If the connection already exists, you have the option to overwrite the existing connection.+&#xA;&#xA;Prior to the import, you can modify the XML file to suit your needs. The XML file can also be imported to another PingFederate environment acting in the same federation role (SP) at your site. The source and the target must run the same version of PingFederate.                                                           |
   | Export metadata for any SAML browser single sign-on (SSO) connection          | Click **Select Action > Export Metadata**, then follow the on-window instructions to complete the task.                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | Update a SAML browser SSO connection                                          | Click **Select Action > Update with Metadata**, then follow the on-screen instructions to complete the task.You can update a connection via a metadata XML file or a metadata URL.+&#xA;&#xA;The update operation might require additional configuration. Review the connection after the update operation.                                                                                                                                                                                                                    |
   | Toggle the status of a connection                                             | Slide the toggle switch to enable or disable a connection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   | Remove a connection                                                           | Click **Select Action > Delete**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
   | Override the verbosity of runtime transaction logging for all IdP connections | Click **Show Advanced Fields** and the select the desired override option.- Off

     Select this option and let the per-connection **Logging Mode** configuration determine the amount of information PingFederate records in the runtime transaction log.This is the default selection.- On

     Select this option, followed by one of the four logging modes, to set the verbosity of runtime transaction logging for all IdP connections. This is most useful when troubleshooting an issue that affects multiple connections. |
   | Turn off automatic multi-connection error checking                            | Click **Show Advanced Fields** and the select the **Disable Automatic Connection Validation** checkbox.This checkbox is not selected by default.Once selected or cleared, the state of this setting is reflected on **Applications > Integration > SP Connections** as well.For more information about this advanced setting and its impact, refer to [Configuring automatic connection validation](pf_configuring_automatic_connection_validation.html).                                                                      |
   | Keep your changes                                                             | Click **Save**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   | Discard your changes                                                          | Click **Cancel**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

---

---
title: Accessing SP connections
description: The SP Connections window lists all service provider connections and displays up to 20 connections at a time. As needed, you can sort connections by connection name, partner connection ID, default virtual server ID, creation date, or last modified timestamps; narrow by protocol type or status; use the pagination controls to navigate through your connections; and search for connections by name or ID.
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:help_spconnectionstasklet_connmgmtstate
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/help_spconnectionstasklet_connmgmtstate.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 22, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Accessing SP connections

The **SP Connections** window lists all service provider connections and displays up to 20 connections at a time. As needed, you can sort connections by connection name, partner connection ID, default virtual server ID, creation date, or last modified timestamps; narrow by protocol type or status; use the pagination controls to navigate through your connections; and search for connections by name or ID.

## About this task

A connection is included in the search results so long as its name or ID is a partial, case-insensitive match to a search term.

## Steps

* Go to **Applications > Integration > SP Connections**.

* To edit a connection, select the connection by its name. For the setting you want to make a change, select the corresponding window title and then follow the configuration wizard to complete the task.

* To create a connection, click **Create Connection** and follow the on-screen steps.

* To copy a connection, click **Select Action > Copy** and then follow the on-screen steps.

  This is most useful if the new connection and the source connection share many common setting values.

  |   |                                                                                                                                                                                                                   |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | PingFederate doesn't include outbound provisioning configurations in connection copies. For more information, see [Configuring outbound provisioning](help_spconnectionconfigtasklet_saasprovisioningstate.html). |

* To export a connection, click **Select Action > Export Connection** and then save the XML file as prompted.

  This is useful in situations where you want to make a backup of a connection prior to changing it.

* To import a connection, click **Import Connection**. For more information, see [Importing a connection](help_connectionimporttasklet_connectionimportstate.html).

  If the connection already exists, you have the option to overwrite the existing connection.

  |   |                                                                                                                                                                                                                                                                        |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Prior to the import, you can modify the XML file to suit your needs. The XML file can also be imported to another PingFederate environment acting in the same federation role (IdP) at your site. The source and the target must run the same version of PingFederate. |

* To export metadata for any SAML Browser SSO connection, click **Select Action > Export Metadata** and then follow the on-screen instructions.

* To update a SAML Browser SSO connection, click **Select Action > Update with Metadata**, then follow the on-screen instructions. For more information, see [Importing SP metadata](pf_importing_sp_metadata.html).

  You can update a connection via a metadata XML file or a metadata URL.

  |   |                                                                                                                |
  | - | -------------------------------------------------------------------------------------------------------------- |
  |   | The update operation might require additional configuration. Review the connection after the update operation. |

* Click the toggle to enable or disable a connection.

* To remove a connection, click **Select Action > Delete**.

* To override the verbosity of runtime transaction logging for all SP connections, click **Show Advanced Fields** and the select the desired override option.

  | Override option | Description                                                                                                                                                                                                                     |
  | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | **Off**         | Select this option and let the per-connection **Logging Mode** configuration determine the amount of information PingFederate records in the runtime transaction log.This is the default selection.                             |
  | **On**          | Select this option, followed by one of the four logging modes, to set the verbosity of runtime transaction logging for all SP connections. This is most useful when troubleshooting an issue that affects multiple connections. |

* To turn off automatic multi-connection error checking, click **Show Advanced Fields > Disable Automatic Connection Validation** checkbox.

  This checkbox is not selected by default.

  Once selected or cleared, the state of this setting is also reflected on the **Authentication > Integration > IdP Connections** window.

  For more information about this advanced setting and its impact, refer to [Configuring automatic connection validation](pf_configuring_automatic_connection_validation.html).

* To keep your changes, click **Save**.

* To discard your changes, click **Cancel**.

---

---
title: Account lockout protection
description: Account lockout protection provides a level of security to the user and can operate in multiple ways based on the PingFederate environment.
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:pf_account_lockout_protection
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/pf_account_lockout_protection.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  related-links: Related links
---

# Account lockout protection

Account lockout protection provides a level of security to the user and can operate in multiple ways based on the PingFederate environment.

Account lockout protection prevents user accounts from locking at the underlying user repository based on too many failed authentication attempts. It also adds a layer of protection against brute force and dictionary attacks because the user is locked out for a time period when the number of failed attempts exceeds the threshold. This protection is enabled in many areas of PingFederate, including the HTML Form Adapter, the Username Token Processor, the OAuth resource owner password credentials grant type, and the native authentication scheme for the administrative console and API.

|   |                                                                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The HTML Form Adapter and the Username Token Processor provide a per-instance setting for the maximum number of failed attempts such that administrators can use unique values for different instances of the adapter or the token processor. |

In a PingFederate clustered environment, depending on the chosen runtime state-management architecture, the account locking-state information is shared across a replica set, multiple replica sets, or all nodes in the cluster.

Settings for account lockout protection are stored in the `com.pingidentity.common.security.AccountLockingService.xml` configuration file, located in the `<pf_install>/pingfederate/server/default/data/config-store` directory.

## Related links

* [Account Locking Service](../server_clustering_guide/pf_acc_lock_service.html)

* [Adaptive clustering](../server_clustering_guide/pf_adaptiv_cluster.html)

* [Directed clustering](../server_clustering_guide/pf_directed_cluster.html)

---

---
title: Account-linking datastores
description: Configure where you want to store account links, either internally or externally.
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:pf_account_link_datastore
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/pf_account_link_datastore.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 15, 2023
section_ids:
  related-links: Related links
---

# Account-linking datastores

Configure where you want to store account links, either internally or externally.

When a service provider (SP) is configured to use account linking for an identity provider (IdP) connection, by default PingFederate uses the built-in Hyper SQL Database (HSQLDB) as the account-link repository. You can also configure PingFederate to store account links on an external database server or directory server. For specific instructions on how to configure these options, see the following topics:

* [Configuring external databases for account-link storage](pf_config_external_database_for_account_link_storag.html)

* [Configuring directories for account-link storage](pf_config_directori_account_link_storag.html)

|   |                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Use the built-in HSQLDB only for trial or training environments. For testing and production environments, always use a secured external storage solution for proper functioning in a clustered environment.Testing involving HSQLDB is not a valid test. In both testing and production, it might cause various problems due to its limitations and HSQLDB involved cases are not supported by Ping Identity. |

## Related links

* [Account linking](../introduction_to_pingfederate/pf_acc_link.html)

* [About Server Clustering](../server_clustering_guide/pf_server_clustering_guide.html)

---

---
title: Activating tracking ID in templates
description: You can configure PingFederate to display the tracking ID in the user-facing error Velocity templates. When an error occurs, use the tracking ID to look for the related log messages.
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:pf_activat_tracking_id_templates
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/pf_activat_tracking_id_templates.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result
---

# Activating tracking ID in templates

You can configure PingFederate to display the tracking ID in the user-facing error Velocity templates. When an error occurs, use the tracking ID to look for the related log messages.

## About this task

You can find the Velocity template files in the `<pf_install>/pingfederate/server/default/conf/template` directory.

The Velocity variable is `$TrackingId` and is available in the following templates:

* `general.error.page.template.html`

* `generic.error.msg.page.template.html`

* `idp.slo.error.page.template.html`

* `idp.sso.error.page.template.html`

* `sourceid-wsfed-idp-exception-template.html`

* `sp.slo.error.page.template.html`

* `sp.sso.error.page.template.html`

* `state.not.found.error.page.template.html`

## Steps

1. Open the applicable Velocity template file.

2. Search for the `$TrackingId` variable.

3. Follow the inline instructions to activate the variable.

   |   |                                                                    |
   | - | ------------------------------------------------------------------ |
   |   | Template customization does not require a restart of PingFederate. |

4. For a clustered PingFederate environment, repeat these steps on each engine node.

## Result

The following screen capture demonstrates the user experience after the `$TrackingId` variable is activated and an error has occurred. In this example, `V3IwuUsy8PQp-9ZbE9UfUjOEo9c` is the tracking ID.

![Sample error message with Tracking ID](_images/pyx1564003632972.png)

---

---
title: Active Directory and Kerberos
description: You can configure PingFederate to authenticate users through the following identity provider (IdP) adapters or token processors.
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:pf_active_directory_kerberos
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/pf_active_directory_kerberos.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 3, 2022
---

# Active Directory and Kerberos

You can configure PingFederate to authenticate users through the following identity provider (IdP) adapters or token processors.

| Adapter or Token Processor                       | Description                                                                                                                                                                                                           |
| ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingFederate integrated Kerberos Adapter         | Using the built-in Kerberos Adapter with a configured AD domain allows a PingFederate identity provider (IdP) server to perform single sign-on (SSO) to service provider (SP) applications based on Kerberos tickets. |
| PingFederate integrated Kerberos Token Processor | The built-in Kerberos Token Processor accepts and validates Kerberos tokens through a configured Kerberos Realm from a web service client.                                                                            |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | As of version 10.3 and above, PingFederate no longer supports the IWA integration kit. You can find more information about Migrating from the IWA Integration Kit to the PingFederate Kerberos adapter in [Migrating from the Integrated Windows Authentication integration kit to the PingFederate Kerberos adapter](https://support.pingidentity.com/s/article/Migrating-from-the-Integrated-Windows-Authentication-integration-kit-to-the-PingFederate-Kerberos-adapter) in the Ping Identity Support Portal. |

---

---
title: Adapter Mappings
description: Configuring adapter mappings allows administrators to map attributes from an authentication policy contract directly to a service provider (SP) adapter instance.
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:pf_adapt_mappings
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/pf_adapt_mappings.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
---

# Adapter Mappings

Configuring adapter mappings allows administrators to map attributes from an authentication policy contract directly to a service provider (SP) adapter instance.

This allows the administrators to chain multiple authentication sources in an SP authentication policy, to build an authentication policy contract using attributes from authentication sources in the policy path, and to apply the authentication policy contract to the target application.

---

---
title: Adapter-to-adapter mappings
description: PingFederate can act as both identity provider (IdP) and service provider (SP) running on the same server with this configuration.
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:pf_adaptertoadapter_mappings
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/pf_adaptertoadapter_mappings.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
---

# Adapter-to-adapter mappings

PingFederate can act as both identity provider (IdP) and service provider (SP) running on the same server with this configuration.

This configuration is provided for special use cases in which PingFederate is acting as both an IdP and an SP, and user attributes from an IdP adapter are used to create an authenticated session with an SP adapter on the same PingFederate server. Generally, these cases involve software-as-a-service (SaaS) providers who might not support standards-based single sign-on (SSO) but do provide proprietary SSO with "delegated authentication", such as Salesforce and Workday.

In effect, this configuration provides an alternative to setting up complete connections to send SAML assertions and other messages back and forth between an IdP and an SP running on the same PingFederate server in a loop-back configuration to enable nonstandard use cases. Instead, attributes that would normally be sent in an assertion are mapped directly from the IdP authentication adapter to an SP adapter, resulting in a secure SP user session.

To use this configuration, ensure that you have already configured the required IdP and SP adapter instances. You can reuse instances that are also in use for connection configurations.

---

---
title: Adding a new datastore
description: On the Data Stores window, you can create and configure a new datastore.
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:help_datasourcetasklet_selectdatasourcetypestate
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/help_datasourcetasklet_selectdatasourcetypestate.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  steps: Steps
---

# Adding a new datastore

On the **Data Stores** window, you can create and configure a new datastore.

## Steps

1. Go to **System > Data & Credential Stores > Data Stores**.

2. Click **Add New Data Store**.

3. Enter a name for the datastore.

4. From the **Type** list, select the type of datastore.

   Available types are limited to the ones currently installed on your server.

5. (Optional) To mask attribute values returned from this datastore in PingFederate logs, select the **Mask Values in Log** checkbox.

6. Click **Next**.

---

---
title: Adding Active Directory domains and Kerberos realms
description: You can configure Active Directory domains or Kerberos realms that PingFederate uses to contact the domain controllers or the key distribution centers (KDCs) for verifying user authentication.
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:pf_adding_active_directory_domains_kerberos_realms
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/pf_adding_active_directory_domains_kerberos_realms.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 15, 2025
section_ids:
  about-this-task: About this task
  adding-domains-and-realms-in-pingfederate-on-premise-deployments: Adding domains and realms in PingFederate on-premise deployments
  steps: Steps
  choose-from: Choose from:
  adding-domains-and-realms-in-pingfederate-cloud-deployments: Adding domains and realms in PingFederate cloud deployments
  before-you-begin: Before you begin
  steps-2: Steps
  adding-domains-and-realms-without-kdc-connectivity: Adding domains and realms without KDC connectivity
  steps-3: Steps
  choose-from-2: Choose from:
---

# Adding Active Directory domains and Kerberos realms

You can configure Active Directory domains or Kerberos realms that PingFederate uses to contact the domain controllers or the key distribution centers (KDCs) for verifying user authentication.

## About this task

The steps for adding an Active Directory domain or Kerberos realm differ between on-premise PingFederate deployments and cloud PingFederate deployments. Follow the steps in the appropriate section for your deployment.

## Adding domains and realms in PingFederate on-premise deployments

Use the following procedure when PingFederate is deployed on-premise.

### Steps

1. In the PingFederate admin console, go to the **Manage Domain/Realm** tab.

2. In the **Connection Type** list, select **Directly**.

3. In the **Domain/Realm Name** field, enter the fully-qualified domain or realm name. For example, companydomain.com.

4. For **Credential Storage**, click one of the following:

   ### Choose from:

   * Click **Internally Managed** to store credentials in PingFederate.

   * Click **Secret Manager** to store credentials in an external secret manager.

     Learn more in [Secret managers](pf_secret_managers.html).

5. In the **Domain/Realm Username** field, enter the ID for the domain or realm account name.

6. Depending on the **Credential Storage** option you chose, enter a domain password or reference.

   1. In the **Domain/Realm Password** field, enter the password for the domain or realm account.

   2. In the **Domain/Realm Password Reference** field, enter the password reference generated by your secret manager.

7. (Optional) Select the **Retain Previous Keys on Password Change** checkbox and click **Save** to avoid locking out end users with existing Kerberos tickets when the service account password is updated.

   PingFederate retains each previous key for the period specified in the **Key Set Retention Period** field on the **Manage Domain/Realm Settings** tab of the **Active Directory Domains/Kerberos Realms** page. The default period is 610 minutes. Learn more in [Managing domain connectivity settings](help_kerberosrealmstasklet_kerberosrealmssettingsstate.html).

   |   |                                                                                      |
   | - | ------------------------------------------------------------------------------------ |
   |   | To clear the previous keys from PingFederate, clear the checkbox and click **Save**. |

   This checkbox is selected by default.

8. In the **Domain Controller/Key Distribution Center Host Names** field, enter the host name or IP address of your domain controller or KDC, such as `dc01-yvr`, and then click **Add**. Repeat this step to add multiple servers.

   If a host name is used, PingFederate appends the domain to the host name to formulate the fully qualified domain name (FQDN) of the server unless the **Suppress DC/Domain Concatenation** checkbox is selected.

   If unspecified, PingFederate uses a DNS lookup.

9. (Optional) Select the **Suppress DC/Domain Concatenation** checkbox to specify the desired FQDNs under **Domain Controller/Key Distribution Center Host Names**.

   When selected, PingFederate doesn't append the domain to the host names.

10. (Optional) Click **Test Domain/Realm Connectivity** to test access to the domain controller or KDC from the administrative-console server.

    When a connection to any of the configured controllers or KDCs is successful, the message `Test Successful` appears. Otherwise, the test returns error messages near the top of the window.

    |   |                                                                                                                                                                                                              |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    |   | To help resolve connectivity issues, select the **Debug Log Output** checkbox on the **Manage Domain/Realm Settings** tab, run the test again, and review the debug messages in the PingFederate server log. |

    This test stops at the first successful result when multiple domain controllers or KDCs are specified, so not all servers are necessarily verified. Depending on the network architecture, the engine nodes deployed in a cluster could establish connections differently. As a result, the engine nodes and the console node might connect to different domain controllers or KDCs.

11. Click **Save**.

## Adding domains and realms in PingFederate cloud deployments

Use the following procedure when PingFederate is deployed in a cloud.

### Before you begin

* [Create an LDAP gateway in your PingOne environment](https://docs.pingidentity.com//pingone/integrations/p1_add_ldap_gateway.html)

* [Create a connection between your PingFederate and PingOne environments](help_p1connections_p1connectioncreate.html)

* [Configure an LDAP datastore](pf_configuring_p1_ldap_gateway_datastore.html)

### Steps

1. In the PingFederate admin console, go to the **Manage Domain/Realm** page.

2. In the **Connection Type** list, select **Through PingOne LDAP Gateway**.

3. In the **Domain/Realm Name** field, enter the fully-qualified domain or realm name. For example, companydomain.com.

4. In the **PingOne LDAP Gateway Data Store** list, select the datastore that was configured for the PingOne LDAP Gateway.

5. (Optional) Click the **Test Domain/Realm Connectivity** checkbox to test access to the domain controller or KDC from the administrative console server.

   When a connection to the configured PingOne LDAP Gateway is successful, the message `Test Successful` appears. Otherwise, the test returns error messages near the top of the window.

6. Click **Save**.

## Adding domains and realms without KDC connectivity

Use the following procedure when PingFederate is deployed in the cloud without Key Distribution Center (KDC) *(tooltip: \<div class="paragraph">
\<p>The Kerberos Key Distribution Center (KDC) authenticates the client and issues tickets allowing access to a server on the network.\</p>
\</div>)* connectivity.

|   |                                                                                                                                                                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The Windows gMSA secret manager isn't supported when Kerberos domains and realms are added using the **Local Validation** connection type. If you want to use the Windows gMSA secret manager, use the **Direct** connection type. Learn more in [Configuring a secret manager for Windows gMSA](pf_configuring_secret_manager_windows_gmsa.html). |

### Steps

1. In the PingFederate admin console, go to the **Manage Domain/Realm** page.

2. In the **Connection Type** list, **Local Validation**.

3. In the **Domain/Realm Name** field, enter the fully-qualified domain or realm name. For example, companydomain.com.

4. For **Credential Storage**, click one of the following:

   ### Choose from:

   * Click **Internally Managed** to store credentials in PingFederate.

   * Click **Secret Manager** to store credentials in an external secret manager.

     Learn more in [Secret managers](pf_secret_managers.html).

5. In the **Domain/Realm Username** field, enter the ID for the domain or realm account name.

   |   |                                                                                                                                   |
   | - | --------------------------------------------------------------------------------------------------------------------------------- |
   |   | **Domain/Realm Username** is case-sensitive. The value must match the username part of the service account's `userPrincipleName`. |

6. Depending on the **Credential Storage** option you chose, enter a domain password or reference.

   1. In the **Domain/Realm Password** field, enter the password for the domain or realm account.

   2. In the **Domain/Realm Password Reference** field, enter the password reference generated by your secret manager.

7. (Optional) Select the **Retain Previous Keys on Password Change** checkbox and click **Save** to avoid locking out end users with existing Kerberos tickets when the service account password is updated.

   PingFederate retains each previous key for the period specified in the **Key Set Retention Period** field on the **Manage Domain/Realm Settings** tab of the **Active Directory Domains/Kerberos Realms** page. The default period is 610 minutes. Learn more in [Managing domain connectivity settings](help_kerberosrealmstasklet_kerberosrealmssettingsstate.html).

   |   |                                                                                      |
   | - | ------------------------------------------------------------------------------------ |
   |   | To clear the previous keys from PingFederate, clear the checkbox and click **Save**. |

   This checkbox is selected by default.

8. Click **Save**.

---

---
title: Adding custom HTTP response headers
description: The PingFederate administrative console and runtime server are capable of returning custom HTTP response headers, such as HTTP Strict-Transport-Security (HSTS), to enforce HTTPS-based access and P3P.
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:pf_adding_custom_of_http_headers
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/pf_adding_custom_of_http_headers.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  steps: Steps
---

# Adding custom HTTP response headers

The PingFederate administrative console and runtime server are capable of returning custom HTTP response headers, such as HTTP Strict-Transport-Security (HSTS), to enforce HTTPS-based access and P3P.

## Steps

1. Edit the `response-header-admin-config.xml` file or the `response-header-runtime-config.xml` file, or both, located in the `<pf_install>/pingfederate/server/default/data/config-store` directory.

2. Save your changes.

3. Restart PingFederate.

   For a clustered PingFederate environment, perform these steps on the console node, and then click **Replicate Configuration** on **System > Server > Cluster Management**.

---

---
title: Adding virtual issuers for OpenID Connect
description: You can define one or more virtual issuers for OpenID Connect, with or without a relative path. When minting an ID token, PingFederate populates the issuer claim according to the virtual issuer setting and the authorization request.
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:pf_adding_virtual_issuers_openid_connect
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/pf_adding_virtual_issuers_openid_connect.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 10, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding virtual issuers for OpenID Connect

You can define one or more virtual issuers for OpenID Connect, with or without a relative path. When minting an ID token, PingFederate populates the issuer claim according to the virtual issuer setting and the authorization request.

## About this task

To add a virtual issuer to PingFederate, perform the following procedure. If you have multiple virtual issuers, ensure the combination of host and path values are unique.

|   |                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | After you define virtual issuers, you can map them to sets of ID token signing keys. For more information, see [Mapping ID token signing keys to virtual issuers](pf_mapping_id_token_signing_keys_virtual_issuers.html). |

## Steps

1. Go to **System > OAuth Settings > Virtual Issuers**.

2. Click **Add Virtual Issuer**.

3. Enter a unique issuer **Name**.

4. Enter the **Host**.

5. Optional: Enter the relative **Path**, which must start with the value of the `pf.runtime.context.path` property in the `run.properties` file.

6. Click **Save**.

---

---
title: Administrative accounts
description: PingFederate supports five authentication schemes for administrative accounts.
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:help_administrativeaccountstasklet_administrativeaccountsstate
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/help_administrativeaccountstasklet_administrativeaccountsstate.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 19, 2023
section_ids:
  related-links: Related links
---

# Administrative accounts

PingFederate supports five authentication schemes for administrative accounts.

The authentication schemes are:

* Native authentication

* LDAP authentication

* RADIUS authentication

* Certificate-based authentication

* OIDC-based authentication

For role-based access control, PingFederate provides two account types and four administrative roles, as shown in the following table.

**PingFederate User Access Control**

| Account type | Administrative role   | Access privileges                                                                                                                                                                                    |
| ------------ | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Admin        | User Admin            | Create users, deactivate users, change or reset passwords, and install replacement license keys.                                                                                                     |
| Admin        | Admin                 | Configure partner connections and most system settings, except the management of local accounts and the handling of local keys and certificates.                                                     |
| Admin        | Expression Admin      | Map user attributes by using the Object-Graph Navigation Language (OGNL) expression language.                                                                                                        |
| Admin        | Crypto Admin          | Manage local keys and certificates.                                                                                                                                                                  |
| Admin        | Data Collection Admin | Collects support data using the [Collect Support Data](pf_collecting_support_data_admin_console.html) menu.Administrators must have Admin, User Admin, and Crypto Admin roles to be given this role. |
| Auditor      | Not applicable        | View-only permissions for all administrative functions. When the **Auditor** role is assigned, no other administrative roles can be set.                                                             |

For native authentication, access and authorization are controlled by the local accounts defined on the **Administrative Accounts** window.

As needed, you can switch from native authentication to an alternative console authentication. Access and authorization are defined in the respective configuration file.

An administrative user can sign on from more than one browser or location, and multiple administrative users can sign on to the PingFederate administrative console at a time. You can optionally restrict the administrative console to one administrative user at a time by modifying the `pf.console.login.mode` property in the `<pf_install>/pingfederate/bin/run.properties` file. Regardless of the property configuration, any number of auditors can sign on at any time.

|   |                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For security, after three failed sign-on attempts from the same location within a short time period, the administrative console and the administrative API will temporarily lock out further attempts by the same user. The user must wait one minute to try again. |

Local accounts defined on the **Administrative Accounts** window are shared between the administrative console and the administrative API if they are both configured to use native authentication, the default. If the administrative console is configured to use an alternative console authentication, the **Administrative Accounts** window appears only if the administrative API is left to use native authentication, and vice versa.

|   |                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you have connected PingFederate to PingOne for Enterprise, you can also single sign-on from the PingOne admin portal to the administrative console. |

## Related links

* [Alternative console authentication](pf_alternative_console_authentication.html)

---

---
title: Administrative API
description: At System > Administrative API, you can configure the behavior of the PingFederate administrative API.
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:pf_administrative_api
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/pf_administrative_api.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 27, 2026
---

# Administrative API

At **System > Administrative API**, you can configure the behavior of the PingFederate administrative API.

You can access documentation for the administrative API from [Accessing the API interactive documentation](../developers_reference_guide/pf_access_api_interact_documentation.html).

---

---
title: Administrative API audit log
description: PingFederate records actions performed through the administrative API in the <pf_install>/pingfederate/log/admin-api.log file.
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:pf_admin_api_audit_log
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/pf_admin_api_audit_log.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2023
---

# Administrative API audit log

PingFederate records actions performed through the administrative API in the `<pf_install>/pingfederate/log/admin-api.log` file.

While the events are not configurable, Log4j 2 configuration settings in the `<pf_install>/pingfederate/server/default/conf/log4j2.xml` file can be adjusted to deliver the desired level of detail surrounding each event.

Each log entry contains information relating to the event, including:

* Time the event occurred on the PingFederate server

* Administrator username performing the action

* Authentication method

* Client IP

* HTTP method

* REST endpoint

* HTTP status code

* jti (JWT ID)

  |   |                                                                                                                                                                                                                                        |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The `jti` is the ID of the outbound JSON Web Token (JWT) request. This information is applicable when the PingFederate administrative API authentication scheme is OAuth2 and the client authentication method is *private\_key\_jwt*. |

* The hash of the inbound access token

  |   |                                                                                                                                                                                                                                                 |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The hash logging is applicable when the PingFederate administrative API authentication scheme is OAuth2. To calculate the hash value for a token or authorization code, run the `calculatehash.sh/bat` script in the PingFederate `bin` folder. |

  |   |                                                                                                                     |
  | - | ------------------------------------------------------------------------------------------------------------------- |
  |   | This feature should only be enabled in production environments when actively troubleshooting authentication issues. |

* HTTP request header

* TLS version

|   |                                                                                                                                                                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `<pf_install>/pingfederate/log/admin-api.log` does not include the HTTP request header and TLS version values by default. You can customize this log to include additional or less information by modifying the pattern elements in the `log4j2.xml` file. For more information, see [Log4j 2 logging service and configuration](pf_log4j_2_loggin_service_and_config.html). |

Each of these fields is separated by a vertical pipe (`\|`) for ease of parsing.

|   |                                                                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingFederate also records actions performed through the administrative API in the `<pf_install>/pingfederate/log/admin.log` file. For more information, see [Administrator audit logging](pf_admin_audit_loggin.html). |

---

---
title: Administrative console migration
description: Use the configcopy tool to migrate data in the administrative console.
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:pf_admin_console_migration
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/pf_admin_console_migration.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  copying-configuration-files: Copying configuration files
  managing-certificates: Managing Certificates
---

# Administrative console migration

Use the `configcopy` tool to migrate data in the administrative console.

|   |                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------- |
|   | As of PingFederate 10.2, the `configcopy` tool has been deprecated and will be removed in a future release. |

For migrating data configured with the source server's administrative console, the `configcopy` tool performs these overall processing steps:

1. Retrieves specified connection and other configuration data (XML) from a source PingFederate server

2. Modifies the configuration with any changes required for the target environment, according to settings in one or more properties files, command-line arguments, or both

3. Imports the updated configuration into the PingFederate target server

The `configcopy` tool can perform these functions in real time, from server to server, or by using an intermediate file. The latter option is useful when both the source and target PingFederate servers are either not running at the same time or not accessible from the same operating system command window.

|   |                                                                                                                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For one-time configuration transfers from one version of PingFederate to a newer version, use a complete configuration archive, either with `configcopy` archive export/import commands, or manually through the administrative console, or the administrative API. Other `configcopy` commands are not supported for this purpose. |

Operational capabilities include:

* Listing of source partner connections, adapter or STS token-translator instances, outbound-provisioning channels, or datastore connections.

  List commands include optional filter settings, when applicable.

* Copying one or more partner connections, outbound-provisioning channels, or instances of adapters or token translators.

* Copying one or more datastore connections.

* Copying server settings.

* Exporting and importing full configuration archives.

## Copying configuration files

The `configcopy` tool supports copying configuration files containing runtime properties, including those needed for server clustering, that might have been manually customized for the source configuration and need to be migrated. The file-copy command can also copy the PingFederate internal, HSQLDB database when needed.

|   |                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Use the built-in HSQLDB only for trial or training environments. For testing and production environments, always use a secured external storage solution for proper functioning in a clustered environment.Testing involving HSQLDB is not a valid test. In both testing and production, it might cause various problems due to its limitations and HSQLDB involved cases are not supported by Ping Identity. |

## Managing Certificates

Administrators can use the `configcopy` tool to perform the following certificate-management tasks on the target PingFederate server:

* List source trusted certificate authorities (CAs) and target key aliases

* Copy one or all trusted CAs from the source server

* Create certificates

* Create Certificate Signing Requests (CSRs)

* Import CA-signed and PKCS-12 certificates