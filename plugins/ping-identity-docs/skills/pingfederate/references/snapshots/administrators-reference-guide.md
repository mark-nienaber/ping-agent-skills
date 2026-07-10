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
title: Choosing a SQL method
description: PingFederate allows you to map attributes directly to a single database table, the default, or to SQL stored-procedure parameters for Java Database Connectivity (JDBC) datastores,
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:help_userprovisioningtasklet_userprovisioningsqlmethodstate
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/help_userprovisioningtasklet_userprovisioningsqlmethodstate.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Choosing a SQL method

PingFederate allows you to map attributes directly to a single database table, the default, or to SQL stored-procedure parameters for Java Database Connectivity (JDBC) datastores,

## About this task

Choose and configure the preferred method on the **SQL Method** tab.

![Screen capture of the SQL Method tab showing the Table and Stored Procedure options.](_images/nbx1564003515373.jpg)

|   |                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------- |
|   | This tab appears only when you specify Microsoft SQL Server datastore on the **User Repository** tab. |

## Steps

* Make a selection as needed and click **Next**.

  Depending on the selection, different steps appear under the **JIT Provisioning** task. See the sections indicated for more information.

* If mapping attributes directly to a table, see the topics sections immediately following:

  * [Specifying a database user-record location](help_userprovisioningtasklet_selectdatabasetableandcolumnsstate.html)

  * [Specifying a unique ID database column](help_userprovisioningtasklet_userprovisioningjdbcuniqueidstate.html)

* If using a stored procedure, skip to [Specifying a stored procedure location](help_userprovisioningtasklet_selectdatabaseschemaandstoredprocstate.html)

---

---
title: Choosing allowable SAML bindings (SAML 2.0)
description: On the Allowable SAML Bindings tab, you select the one or more bindings that your service provider (SP) partner can use to send SAML authentication requests or single logout (SLO) messages.
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:help_spprotocolsettingstasklet_allowablesamlbindingsstate
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/help_spprotocolsettingstasklet_allowablesamlbindingsstate.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  result: Result
---

# Choosing allowable SAML bindings (SAML 2.0)

On the **Allowable SAML Bindings** tab, you select the one or more bindings that your service provider (SP) partner can use to send SAML authentication requests or single logout (SLO) messages.

## Before you begin

For prerequisites and initial steps for configuring Browser SSO protocols, see [Configuring protocol settings](help_spbrowserssotasklet_spprotocolsettingsstate.html).

## About this task

This step applies only to SAML 2.0 connections when the SP-initiated SSO profile or either SLO profile is selected on the **SAML Profiles** tab.

## Steps

1. On the **Allowable SAML Bindings** tab, select the applicable SAML bindings based on your partner agreement.

   |   |                                                                                                                                                                                     |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you have specified an Assertion Consumer Service (ACS) or SLO endpoint using the artifact (outbound) binding, you must including SOAP as one of the allowable (inbound) binding. |

2. Click **Next** to save changes and proceed to **Artifact Resolver Locations**. For more information, see [Specifying artifact resolver locations (SAML 2.0)](help_spprotocolsettingstasklet_artifactconfigstate.html).

## Result

If you are editing an existing connection, you can reconfigure the allowable bindings, which might require additional configuration changes in subsequent tasks.

---

---
title: Choosing an attribute mapping method
description: You can select if and how PingFederate should query a local datastore to help fulfill the attribute contract in conjunction with attribute values from the single sign-on (SSO) token.
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:pf_choosing_attribute_mapping_method
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/pf_choosing_attribute_mapping_method.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  result: Result
---

# Choosing an attribute mapping method

You can select if and how PingFederate should query a local datastore to help fulfill the attribute contract in conjunction with attribute values from the single sign-on (SSO) token.

## Before you begin

To determine whether you need to look up additional values, compare the attribute contract against the adapter contract or the authentication policy contract. If the attribute contract does not contain the required information, determine whether a local datastore can supply it.

Alternatively, you can configure datastore queries as part of the fulfillment configuration for the applicable APC if you use authentication policies to route users through a series of authentication sources and end each successful policy path with an APC.

## About this task

You make selections on the **Adapter Data Store** tab for service provider (SP) adapter mapping or the **Attribute Retrieval** tab for authentication policy contract (APC) mapping.

|   |                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------ |
|   | To learn more about authentication policies, see [Authentication policies](pf_authentication_policies.html). |

## Steps

* If the attribute contract contains all the attributes that your application requires, click **Use only the attributes available in the SSO assertion**.

* To set up a datastore query, click **Use the SSO assertion to look up additional information**, and then follow a series of sub tasks to complete the configuration. See [Choosing a datastore](pf_choosing_datastore.html) for step-by-step instructions.

## Result

If you are editing a currently mapped adapter instance or APC, you can change the mapping method, which might require additional configuration changes in subsequent tasks.

---

---
title: Choosing an encryption certificate (SAML 2.0)
description: If SAML_SUBJECT is encrypted, either by itself or as part of a whole assertion, then all references to this name identifier in SAML 2.0 single logout (SLO) requests from your site might also be encrypted if the connection uses service provider (SP)-initiated SLO.
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:help_idp_credentialstasklet_selectxmlencryptioncertstate
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/help_idp_credentialstasklet_selectxmlencryptioncertstate.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Choosing an encryption certificate (SAML 2.0)

If `SAML_SUBJECT` is encrypted, either by itself or as part of a whole assertion, then all references to this name identifier in SAML 2.0 single logout (SLO) requests from your site might also be encrypted if the connection uses service provider (SP)-initiated SLO.

## About this task

You must also choose a certificate if encryption of the name identifier is required for an Attribute Request profile. For more information, see [Specifying XML encryption policy (for SAML 2.0)](help_idpprotocolsettingstasklet_selectidpxmlassertionencryptionstate.html).

## Steps

1. (Optional) Select an option under **Block Encryption Algorithm**.

|   |                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For Oracle Java SE Development Kit 11, the JCE jurisdiction policy defaults to unlimited strength. For more information, see the [Oracle JDK Migration Guide](https://docs.oracle.com/en/java/javase/11/migrate/) in Oracle's documentation. |

\+ The default selection is **AES-128**.

\+ For more information about XML block encryption and key transport algorithms, see [XML Encryption Syntax and Processing from W3C](https://www.w3.org/TR/xmlenc-core/).

1. Select an option under **Key Transport Algorithm**.

   |   |                                                                                                                                                                                                                                                                                               |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Due to security risks associated with the RSA-v1.5 algorithm used for key transport, it is no longer available for new connections. Existing connections in which this algorithm is configured continue to support it. However, you should upgrade such connections to use a newer algorithm. |

   The default selection is **RSA-OAEP**.

2. Select a partner certificate from the list.

   If you have not imported the certificate from your partner, click **Manage Certificates** to do so. For more information see [Managing certificates from partners](pf_managing_certificates_from_partners.html).

---

---
title: Choosing an event trigger
description: Choose whether PingFederate initiates user provisioning only when the user identifier is new, or every time your site receives a single sign-on (SSO) token.
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:help_userprovisioningtasklet_eventtriggerstate
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/help_userprovisioningtasklet_eventtriggerstate.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Choosing an event trigger

Choose whether PingFederate initiates user provisioning only when the user identifier is new, or every time your site receives a single sign-on (SSO) token.

## About this task

If you choose to have PingFederate initiate user provisioning every time your site receives an SSO token, for all SSO tokens, an existing user account is always updated with incoming attributes.

![Scree capture of the Event Trigger tab showing the two trigger options.](_images/sqb1564003520072.jpg)

|   |                                                                                                                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This tab does not appear for a Microsoft SQL Server datastore if provisioning is accomplished using a stored procedure, because the procedure is always called for all SSO tokens. The procedure should handle both provisioning new users and updating existing ones. |

## Steps

* On the **Event Trigger** tab, in the **Specify the trigger that initiates a user-provisioning event** section, select one of the following:

  ### Choose from:

  * **Only SAML Assertations Containing a New User ID**

  * **All SAML Assertations**

---

---
title: Choosing an identity mapping method for IdP SSO
description: In the Identity Mapping window, you choose the type of name identifier your partner requires. Your selection might affect the way that the service provider (SP) looks up and associates your users at the SP site. You and the SP should decide in advance which option to use.
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:help_assertioncreationtasklet_selectspaccountlinkingstate
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/help_assertioncreationtasklet_selectspaccountlinkingstate.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
---

# Choosing an identity mapping method for IdP SSO

In the **Identity Mapping** window, you choose the type of name identifier your partner requires. Your selection might affect the way that the service provider (SP) looks up and associates your users at the SP site. You and the SP should decide in advance which option to use.

The choices of name-identifier types depend on whether you use the SAML or WS-Federation protocol. For more information, see one of the following.

* [Selecting a SAML Name ID type](pf_select_saml_name_id_type.html)

* [Selecting a WS-Federation Name ID type](help_assertioncreationtasklet_wsfedidentitymappingstate.html)

|   |                                                                                                                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The **Identity Mapping** window does not apply for connections using the WS-Federation protocol in conjunction with JSON web token (JWT)-based single sign-on (SSO) tokens. Instead, work with the SP to define an attribute contract that it can use to map users to accounts at the SP site. |

---

---
title: Choosing an identity mapping method for SP SSO
description: "When configuring service provider (SP) single sign-on (SSO), PingFederate offers two methods of identity mapping you can choose from: account mapping or account linking."
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:help_usersessioncreationtasklet_selectidpaccountlinkingstate
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/help_usersessioncreationtasklet_selectidpaccountlinkingstate.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Choosing an identity mapping method for SP SSO

When configuring service provider (SP) single sign-on (SSO), PingFederate offers two methods of identity mapping you can choose from: account mapping or account linking.

## About this task

PingFederate allows an SP to use either account linking or account mapping to associate remote users with local accounts for SSO between business partners. For more information, see [Identity mapping](../introduction_to_pingfederate/pf_ident_mapp.html). On the **Identity Mapping** tab, you choose which method to use in this IdP connection. You and your partner should decide in advance which option to use. For more information, see [Federation planning checklist](../introduction_to_pingfederate/pf_fed_plan_checklist.html).

If your site is using account linking, then establishing an attribute contract is not required. Depending on your partner agreement, you can choose to supplement the account link with an attribute contract. In this configuration the account link is used to determine the user's identity, while the additional attributes might be used for authorization decisions, customized web pages, and so on, at the your site. For more information, see [User attributes](../introduction_to_pingfederate/pf_user_attrib.html).

|   |                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you have previously set up a configuration to use an attribute contract and want to change the configuration to use account linking without additional attributes, then the existing attribute contract will be discarded. |

Account linking can be used with either a clear, standard name identifier or an opaque pseudonym.

## Steps

1. Choose which identity mapping method to use in this IdP connection.

   ### Choose from:

   * If you want to dynamically associate remote users with local accounts using a known attribute to identify a user, such as a username or email address, select **Account Mapping**

     Account mapping uses the user identifier, `SAML_SUBJECT` in a SAML assertion or `sub` in an ID token, and associated user attributes to create an association between a remote user and a local account.

     |   |                                                                                                                                                                                                              |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
     |   | If you are using PingFederate's JIT provisioning, choose **Account Mapping**. For more information, see [Configuring just-in-time provisioning](help_idpconnectionconfigtasklet_userprovisioningstate.html). |

   * If you want to create a long-term association between a remote user and a local account, select **Account Linking**

     |   |                                                                                                                                                                                                                                                                                                                                                                                                               |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | Use the built-in HSQLDB only for trial or training environments. For testing and production environments, always use a secured external storage solution for proper functioning in a clustered environment.Testing involving HSQLDB is not a valid test. In both testing and production, it might cause various problems due to its limitations and HSQLDB involved cases are not supported by Ping Identity. |

   To set up an attribute contract to use in conjunction with account linking, select the **…​ includes attributes in addition to the unique name identifier** checkbox.

2. If you have selected only the SP-initiated SSO profile and you intend to enforce additional authentication requirements by placing this IdP connection in an SP authentication policy, select **No Mapping**.

3. Additionally, select **No Mapping** if you are deploying an IdP connection solely for OAuth attribute mapping without the use of an authentication policy contract. For more information, see [Configuring IdP connection grant mapping](help_idpbrowserssotasklet_oauthattributemappingstate.html).

---

---
title: Choosing an IdP connection type
description: You can use the administrative console to choose an identity provider (IdP) connection type.
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:help_idpconnectionconfigtasklet_connroleandprotocolstate
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/help_idpconnectionconfigtasklet_connroleandprotocolstate.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2026
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Choosing an IdP connection type

You can use the administrative console to choose an identity provider (IdP) connection type.

## About this task

You can indicate on the **Connection Type** tab whether the connection to this partner is for browser single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)*, WS-Trust Security Token Service (STS) *(tooltip: \<div class="paragraph">
\<p>An entity responsible for responding to WS-Trust requests for validation and issuance of security tokens used for SSO authentication to web services.\</p>
\</div>)*, OAuth, SAML, inbound provisioning, or a combination of them.

|   |                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You can add STS, OAuth, and outbound provisioning support to any existing SSO connection, or vice versa, at any time. However, when OpenID Connect is the chosen protocol for browser SSO, the other types become unavailable. |

Select the applicable protocol on the **Connection Type** tab when establishing a new connection.

|   |                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If your partner's deployment also supports multiple protocols and you intend to communicate using more than one, you must set up a separate connection for each protocol. Each connection must use a unique partner connection ID. |

## Steps

* On the **Connection Type** tab, indicate the desired type of connection to your partner.

  | Choice                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  | Configure a connection for secure browser-based SSO                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Select the **Browser SSO Profiles** checkbox and a protocol from the list, if necessary.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
  | Configure an STS connection                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Select the **WS-Trust STS** checkbox and the default token type from the list.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
  | Configure a connection that exchanges SAML assertions or JSON web tokens (JWTs) for access tokens                                                                                                                                                                                                                                                                                                                                                                                                       | Select the **OAuth Assertion Grant** checkbox.&#xA;&#xA;The OAuth Assertion Grant option is available only if at least one Access Token Manager instance has been configured on the Applications > OAuth > Access Token Management window\.For more information about these standards, see [Security Assertion Markup Language (SAML) 2.0 Profile for OAuth 2.0 Client Authentication and Authorization Grants](https://tools.ietf.org/html/rfc7522) and [JSON Web Token (JWT) Profile for OAuth 2.0 Client Authentication and Authorization Grants](https://tools.ietf.org/html/rfc7523). |
  | Configure a connection to exchange JSON Web Token (JWT) *(tooltip: \<div class="paragraph">&#xA;\<p>An IETF standard container format for a JSON object used for the secure exchange of content, such as identity or entitlement information. You can find the industry standard in \<a href="https\://datatracker.ietf.org/doc/html/rfc7519">RFC 7519\</a>.\</p>&#xA;\</div>)* for access tokens by delegating JWT Bearer Grant processing to a configured plugin. For example, the macOS SSO Adapter. | Select the **JWT Bearer Grant Processor** checkbox and select a configured [JWT Bearer Grant Processor](pf_jwt_bearer_grant_processors.html) instance in the list.                                                                                                                                                                                                                                                                                                                                                                                                                         |
  | Configure an inbound provisioning connection                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Select the **Inbound Provisioning** checkbox and choose to support provisioning of users only (**User Support**) or users and groups (**User and Group Support**). For groups, nested group membership, if any, is preserved.                                                                                                                                                                                                                                                                                                                                                              |

* (Optional) If your PingFederate license manages connections by groups, you can select a group for this connection.

  This option isn't displayed for unrestricted or other types of licenses.

---

---
title: Choosing an OAuth datastore
description: You can optionally set up OAuth datastore queries to supplement values returned from the source.
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:help_oauthidpconnection2targetmappingtasklet_oauthidpconnectionselectdatasourcedata
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/help_oauthidpconnection2targetmappingtasklet_oauthidpconnectionselectdatasourcedata.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Choosing an OAuth datastore

You can optionally set up OAuth datastore queries to supplement values returned from the source.

## Steps

1. On the **Data Store** tab, perform one of the following actions.

   ### Choose from:

   * To set up datastore queries, select a datastore from the **Active Data Store** list and then click **Next**. For configuration steps, see [Datastore query configuration](pf_datastore_query_config.html).

   * To skip this optional configuration, select **No Data Store**, and then click **Next**.

---

---
title: Choosing an SP connection template
description: The Connection Template tab allows you to choose a quick-connection template for new connection if your installation includes an optional PingFederate SaaS Connector.
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:help_spconnectionconfigtasklet_connectiontemplatestate
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/help_spconnectionconfigtasklet_connectiontemplatestate.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Choosing an SP connection template

The **Connection Template** tab allows you to choose a quick-connection template for new connection if your installation includes an optional PingFederate SaaS Connector.

## About this task

|   |                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------- |
|   | When you select a connection template, many connection settings are configured for you automatically. |

## Steps

1. Go to **Applications > Integration > SP Connections**.

2. Click **Create Connection**.

3. To use a template, select **Use a template for this connection**, then choose the template and enter additional information as required.

   |   |                                                                                                                                                                                          |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | After you click **Next**, you cannot return to this window and make a different selection. If you intended to use a different template or no template, you must create a new connection. |

---

---
title: Choosing an SP connection type
description: You can manually create service provider (SP) connections in PingFederate using browser single sign-on (SSO), WS-Trust security token service (STS), outbound provisioning, or any combination thereof.
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:help_spconnectionconfigtasklet_connroleandprotocolstate
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/help_spconnectionconfigtasklet_connroleandprotocolstate.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Choosing an SP connection type

You can manually create service provider (SP) connections in PingFederate using browser single sign-on (SSO), WS-Trust security token service (STS), outbound provisioning, or any combination thereof.

## About this task

If you are not using a connection template, which pre-configures browser-based SSO, indicate on the **Connection Type** tab whether the connection to this partner is for Browser SSO, WS-Trust STS, outbound provisioning, or any combination of them.

|   |                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------- |
|   | You can add STS, OAuth, and outbound provisioning support to any existing SSO connection, or vice versa, at any time. |

|   |                                                                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If your partner's deployment supports multiple protocols and you intend to communicate using more than one, you must set up a separate connection for each protocol. Each connection must use a unique (partner) connection ID. |

## Steps

1. Go to **Applications > Integration > SP Connections**.

2. Click **Create Connection**.

3. Select **Do not use a template for this connection**.

4. To configure a connection for secure browser-based SSO, select the **Browser SSO Profiles** checkbox.

   If you are not using a connection template, you must select the applicable protocol from the list when establishing a new connection.

   For a WS-Federation connection, select the desired token type, either **SAML 1.1**, **SAML 2.0**, or **JWT** (JSON Web Token).

   |   |                                                                                                                                                                                               |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Learn more about creating a SAML application in [Configuring a SAML application in PingFederate](https://docs.pingidentity.com/solution-guides/workforce_use_cases/htg_config_saml_app.html). |

   |   |                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------- |
   |   | If you are creating a WS-Federation connection to Microsoft Windows Azure Pack, select JWT as the token type. |

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | PingFederate can encrypt the subject and attributes of SAML 2.0 assertions.For information about configuring encryption policies on a PingFederate identity provider (IdP), see [Configuring XML encryption policy (SAML 2.0)](help_spprotocolsettingstasklet_selectspxmlassertionencryptionstate.html).For information about configuring encryption policies on a PingFederate SP, see [Specifying XML encryption policy (for SAML 2.0)](help_idpprotocolsettingstasklet_selectidpxmlassertionencryptionstate.html). |

5. (Optional) Choose one or both of the following depending on your configuration needs.

   | Connection Template       | Step                                                                                  |
   | ------------------------- | ------------------------------------------------------------------------------------- |
   | **WS-TRUST STS**          | Select the **WS-Trust STS** checkbox.                                                 |
   | **Outbound Provisioning** | Select **Outbound Provisioning** and then select the provisioning type from the list. |

6. If your PingFederate license manages connections by groups, select a license group for this connection.

   This option is not shown for unrestricted or other types of licenses.

7. To save your settings, click **Next**.

---

---
title: Choosing IdP connection options
description: On the Connection Optionstab, shown only for browser-based single sign-on (SSO) connections, you can enable browser-based SSO in conjunction with Just-in-Time (JIT) provisioning. Additionally, you can also choose to map user attributes for persistent grants used by the optional PingFederate OAuth authorization server.
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:help_idpconnectionconfigtasklet_connectionoptionsstate
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/help_idpconnectionconfigtasklet_connectionoptionsstate.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Choosing IdP connection options

On the **Connection Options**tab, shown only for browser-based single sign-on (SSO) connections, you can enable browser-based SSO in conjunction with Just-in-Time (JIT) provisioning. Additionally, you can also choose to map user attributes for persistent grants used by the optional PingFederate OAuth authorization server.

## About this task

For SAML 2.0, you can configure the **Attribute Query** profile with or without the browser-based SSO.

## Steps

* On the **Connection Options** tab, make the appropriate selections for your configuration.

  | Choice                                                                  | Action                                                                                                                                                   |
  | ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | Create a connection for browser-based SSO.                              | Select the **Browser SSO** checkbox.                                                                                                                     |
  | Enable JIT provisioning, OAuth attribute mapping, or both.              | Select the appropriate checkbox after selecting the **Browser SSO** checkbox.                                                                            |
  | Create a connection to facilitate the SAML 2.0 Attribute Query profile. | Select the **Attribute Query** checkbox. For more information, see [Attribute Query and XASP](../introduction_to_pingfederate/pf_attrib_query_xasp.html) |

---

---
title: Choosing SAML 2.0 profiles
description: A SAML profile is the message-interchange scenario that you and your federation partner have agreed to use. SAML binding, by contrast, is the transport protocol of SAML messages.
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:help_spbrowserssotasklet_selectsamlprofilesstate
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/help_spbrowserssotasklet_selectsamlprofilesstate.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Choosing SAML 2.0 profiles

A SAML profile is the message-interchange scenario that you and your federation partner have agreed to use. SAML binding, by contrast, is the transport protocol of SAML messages.

## About this task

On the **SAML Profiles** tab, select one or more SAML 2.0 profiles for your IdP Browser SSO configuration.

|   |                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The **SAML Profiles** tab is not shown for SAML 1.x connections because identity provider (IdP) single sign-on (SSO) is assumed, single logout (SLO) profiles are not supported, and the server supports the "destination-first" (SP-initiated) profile SSO automatically. This window is also not presented for WS-Federation connections because profile selection is not required. |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When configuring a local loopback connection, in which one PingFederate instance is both the identity provider and the service provider, disable the IdP-Initiated SLO and SP-Initiated SLO options on the Browser SSO window's SAML Profiles tab. These options determine whether SAML logout requests should be sent to the partner during the SLO flow. Those requests aren't necessary and can cause unexpected behavior when the partner connection exists locally. All local sessions for loopback connections are terminated during the SLO flow without the need to send SAML requests. |

For SAML 2.0, PingFederate supports all IdP- and SP-initiated SSO and SLO profiles. For more information on typical SSO and SLO profile configurations, including illustrations, see [SAML 2.0 profiles](../introduction_to_pingfederate/pf_saml20_profile.html).

## Steps

1. Go to **Applications > Integration > SP connections**.

2. Click on the SP connection you want to configure. For more information, see [Accessing SP connections](help_spconnectionstasklet_connmgmtstate.html).

3. On the **Browser SSO** tab, click **Configure Browser SSO**.

4. Select either **IdP-Initiatied SSO** or **SP-Initiated SSO** or both, depending on your partner agreement.

   You must select at least one SSO profile.

5. Select either **IdP-Initiated SLO** or **SP-Initiated SLO** or both, depending on your partner agreement.

   SLO profile options are only enabled after you choose an SSO profile. ![Screen capture of the Browser SSO configuration window with the SAML Profiles tab selected. There is a section for Single Sign-On (SSO) Profiles with IdP-Initatited SSO and SP-Initiated SSO checkboxes. The IdP-Initiated SSO checkbox is selected. There is another section for Single Logout (SLO) Profiles with IdP-Initiated SLO and SP-Initiated SLO checkboxes. The IdP-Initiated SLO checkbox is selected.](_images/swv1628281519684.png)

6. Click **Next** to save your changes.

---

---
title: Choosing SP connection options
description: On the Connection Options tab, you can enable browser-based single sign-on (SSO), Attribute Query, or both for the current connection.
component: pingfederate
version: 13.1
page_id: pingfederate:administrators_reference_guide:help_spconnectionconfigtasklet_connectionoptionsstate
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/administrators_reference_guide/help_spconnectionconfigtasklet_connectionoptionsstate.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  before-you-begin: Before you begin
  steps: Steps
---

# Choosing SP connection options

On the **Connection Options** tab, you can enable browser-based single sign-on (SSO), Attribute Query, or both for the current connection.

## Before you begin

For initial steps in creating a service provider (SP) connection, see [Choosing an SP connection type](help_spconnectionconfigtasklet_connroleandprotocolstate.html).

## Steps

1. Choose one or more of the following options.

   | Connection option   | Description                                                                                                                                                                                                                         |
   | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Browser SSO**     | Select to create a connection for browser-based SSO.                                                                                                                                                                                |
   | **IdP Discovery**   | Select to enable identity provider (IdP) discovery. This option is only available if you have configured IdP discovery. For more information, see [Configuring standard IdP Discovery](pf_configuring_standard_idp_discovery.html). |
   | **Attribute Query** | Select to create a connection that facilitates the SAML 2.0 Attribute Query profile. For more information, see [Attribute Query and XASP](../introduction_to_pingfederate/pf_attrib_query_xasp.html).                               |

2. To save your changes, click **Next**.