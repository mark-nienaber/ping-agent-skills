---
title: "<code class=\"codeph\">IdentityStoreProvisionerWithFiltering</code> interface implementation"
description: Implement the IdentityStoreProvisionerWithFiltering interface to provision and deprovision users and groups to an external user store with list/query and filtering support.
component: pingfederate
version: 13.1
page_id: pingfederate:sdk_developers_guide:identitystoreprovisionerwithfiltering_interface_implemen
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/sdk_developers_guide/identitystoreprovisionerwithfiltering_interface_implemen.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  create-user: Create user
  read-user: Read user
  read-users: Read users
  update-user: Update user
  delete-user: Delete user
  pf_section_checkForGroupProvisioningSupport: Check for group provisioning support
  create-group: Create group
  read-group: Read group
  read-groups: Read groups
  update-group: Update group
  delete-group: Delete group
---

# `IdentityStoreProvisionerWithFiltering` interface implementation

Implement the `IdentityStoreProvisionerWithFiltering` interface to provision and deprovision users and groups to an external user store with list/query and filtering support.

|   |                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------- |
|   | If you do not need to support list/query and filtering, you can implement the `IdentityStoreProvisioner` interface instead. |

Implementing this interface requires the following Java packages:

* `com.pingidentity.sdk.provision`

* `com.pingidentity.sdk.provision.exception`

* `com.pingidentity.sdk.provision.users.request`

* `com.pingidentity.sdk.provision.users.response`

* `com.pingidentity.sdk.provision.groups.response`

* `com.pingidentity.sdk.provision.groups.request`

|   |                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------- |
|   | Group support is optional (see [Check for group provisioning support](#pf_section_checkForGroupProvisioningSupport)). |

For each identity store provisioner implementation, in addition to the methods described under [Shared plugin interfaces](pf_share_plugin_interface.html), you must implement the following:

* Create user

* Read user

* Read users (not applicable to the `IdentityStoreProvisioner` interface)

* Update user

* Delete user

* Check for group provisioning support

* Create group

* Read group

* Read groups (not applicable to the `IdentityStoreProvisioner` interface)

* Update group

* Delete group

## Create user

```
UserResponseContext createUser(CreateUserRequestContext createRequestCtx)
throws IdentityStoreException
```

PingFederate invokes the `createUser()` method of your identity store provisioner in response to create-user requests made to PingFederate services, such as inbound provisioning. This method creates the user in the user store managed by the identity store provisioner.

The `CreateUserRequestContext` contains all information needed to fulfill the request. If the user is successfully provisioned, the method returns a `UserResponseContext` containing the user attributes used to provision the user. The method throws an `IdentityStoreException` if an error occurred during the creation process. See the `com.pingidentity.sdk.provision.exception` package for exceptions that can be thrown.

## Read user

```
UserResponseContext readUser(ReadUserRequestContext readRequestCtx)
throws IdentityStoreException
```

PingFederate invokes the `readUser()` method of your identity store provisioner in response to get-user requests made to PingFederate services, such as inbound provisioning. This method retrieves user data from the user store managed by the identity store provisioner.

The `ReadUserRequestContext` contains all information needed to fulfill the request. If the user data is successfully retrieved, the method returns a `UserResponseContext` containing the user attributes for the user. The method throws an `IdentityStoreException` if an error occurred during the retrieval process. See the `com.pingidentity.sdk.provision.exception` package for exceptions that can be thrown.

## Read users

```
UsersResponseContext readUsers(ReadUsersRequestContext readRequestCtx)
throws IdentityStoreException
```

PingFederate invokes the `readUsers()` method of your identity store provisioner in response to list/query requests for user attributes made to PingFederate services, such as inbound provisioning. This method retrieves user data from the user store managed by the identity store provisioner.

|   |                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The `readUsers` method applies only to the `IdentityStoreProvisionerWithFiltering` interface; it does not apply to the `IdentityStoreProvisioner` interface. |

The `ReadUsersRequestContext` contains all information needed to fulfill the request. If the user data is successfully retrieved, the method returns a `UsersResponseContext` containing the user attributes satisfying the filter. If an error occurred during the retrieval process, the method returns an `IdentityStoreException` . See the `com.pingidentity.sdk.provision.exception` package for exceptions that can be thrown.

## Update user

```
UserResponseContext updateUser(UpdateUserRequestContext updateRequestCtx)
throws IdentityStoreException
```

PingFederate invokes the `updateUser()` method of your identity store provisioner in response to update-user requests made to PingFederate services, such as inbound provisioning. This method updates the user in the user store managed by the identity store provisioner.

The `UpdateUserRequestContext` contains all information needed to fulfill the request. If the user data is successfully updated, the method returns a `UserResponseContext` containing the user's updated attributes. The method throws an `IdentityStoreException` if an error occurred during the update process. See the `com.pingidentity.sdk.provision.exception` package for exceptions that can be thrown.

## Delete user

```
void deleteUser(DeleteUserRequestContext deleteRequestCtx)
throws IdentityStoreException
```

PingFederate invokes the `deleteUser()` method of your identity store provisioner in response to delete-user requests made to PingFederate services, such as inbound provisioning. This method deprovisions the user in the user store managed by the identity store provisioner.

The `DeleteUserRequestContext` contains all information needed to fulfill the request. The method throws an `IdentityStoreException` if an error occurred during the deprovision process. See the `com.pingidentity.sdk.provision.exception` package for exceptions that can be thrown.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The plugin implementation can choose not to permanently delete the resource, but must return a `NotFoundException` for all `readUser()`, `updateUser()`, and `deleteUser()` operations associated with the previously deleted ID. In addition, the plugin must not consider the deleted user in conflict calculation. For example, a `createUser()` request for a user with a previously deleted ID should not throw a `ConflictException`. |

## Check for group provisioning support

```
boolean isGroupProvisioningSupported()
throws IdentityStoreException
```

Implement the `isGroupProvisioningSupported()` method to return true if group provisioning is supported by your identity store provisioner or false otherwise. The method throws an `IdentityStoreException` if an error occurred during the query process. See `com.pingidentity.sdk.provision.exception` package for exceptions that can be thrown.

## Create group

```
GroupResponseContext createGroup(CreateGroupRequestContext createRequestCtx)
throws IdentityStoreException
```

PingFederate invokes the `createGroup()` method of your identity store provisioner in response to create-group requests made to PingFederate services, such as inbound provisioning. This method creates the group in the user store managed by the identity store provisioner if the `isGroupProvisioningSupported()` method returns true; otherwise, it should throw `NotImplementedException`.

The `CreateGroupRequestContext` contains all information needed to fulfill the request, such as group attributes. If the group is successfully provisioned, the method returns a `GroupResponseContext` containing the group attributes used to provision the group. The method throws an `IdentityStoreException` if an error occurred during the creation process. See the `com.pingidentity.sdk.provision.exception` package for exceptions that can be thrown.

## Read group

```
GroupResponseContext readGroup(ReadGroupRequestContext readRequestCtx)
throws IdentityStoreException
```

PingFederate invokes the `readGroup()` method of your identity store provisioner in response to get-group requests made to PingFederate services, such as inbound provisioning. This method retrieves group data from the user store managed by the identity store provisioner if the `isGroupProvisioningSupported()` returns true; otherwise, it should throw `NotImplementedException`.

The `ReadGroupRequestContext` contains all information needed to fulfill the request, such as group ID. If the group data is successfully retrieved, the method returns a `GroupResponseContext` containing the group attributes. The method throws an `IdentityStoreException` if an error occurred during the retrieval process. See the `com.pingidentity.sdk.provision.exception` package for exceptions that can be thrown.

## Read groups

```
GroupsResponseContext readGroups(ReadGroupsRequestContext readRequestCtx)
throws IdentityStoreException
```

PingFederate invokes the `readGroups()` method of your identity store provisioner in response to list/query requests for group attributes made to PingFederate services, such as inbound provisioning. This method retrieves group data from the user store managed by the identity store provisioner if the `isGroupProvisioningSupported()` returns true; otherwise, it should throw `NotImplementedException`.

|   |                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `readGroups` method applies only to the `IdentityStoreProvisionerWithFiltering` interface; it does not apply to the `IdentityStoreProvisioner` interface. |

The `ReadGroupsRequestContext` will contain all information needed to fulfill the request (for example, a filter). If the group data was successfully retrieved, a `GroupsResponseContext` should be returned and contain the group attributes for the groups. An `IdentityStoreException` should be thrown if an error occurred during the retrieval process. See `com.pingidentity.sdk.provision.exception` package for different exceptions that can be thrown.

## Update group

```
GroupResponseContext updateGroup(UpdateGroupRequestContext updateRequestCtx)
throws IdentityStoreException
```

PingFederate invokes the `updateGroup()` method of your identity store provisioner in response to update-group requests made to PingFederate services, such as inbound provisioning. This method updates the group in the user store managed by the identity store provisioner if the `isGroupProvisioningSupported()` method returns true; otherwise, it should throw `NotImplementedException`.

The `UpdateGroupRequestContext` contains all information needed to fulfill the request, such as group attributes. If the group data is successfully updated, the method returns a `GroupResponseContext` containing the group's updated attributes. The method throws an `IdentityStoreException` if an error occurred during the update process. See the `com.pingidentity.sdk.provision.exception` package for exceptions that can be thrown.

## Delete group

```
void deleteGroup(DeleteGroupRequestContext deleteRequestCtx)
throws IdentityStoreException
```

PingFederate invokes the `deleteGroup()` method of your identity store provisioner in response to delete-group requests made to PingFederate services, such as inbound provisioning. This method deprovisions the group in the user store managed by the identity store provisioner if the `isGroupProvisioningSupported()` returns true; otherwise, it should throw `NotImplementedException`.

The `DeleteGroupRequestContext` contains all information needed to fulfill the request, such as a group ID. The method throws an `IdentityStoreException` if an error occurred during the deprovisioning process. See the `com.pingidentity.sdk.provision.exception` package for exceptions that can be thrown.

---

---
title: Authentication API states, actions, and models
description: To develop authentication API-capable adapters and selectors, you must understand the states, actions, and models of single sign-on (SSO) transactions through the PingFederate authentication API.
component: pingfederate
version: 13.1
page_id: pingfederate:sdk_developers_guide:pf_authentication_api_states_actions_and_models
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/sdk_developers_guide/pf_authentication_api_states_actions_and_models.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  related-links: Related links
---

# Authentication API states, actions, and models

To develop authentication API-capable adapters and selectors, you must understand the states, actions, and models of single sign-on (SSO) transactions through the PingFederate authentication API.

PingFederate assigns a flow ID to each SSO transaction that uses the authentication API. PingFederate uses the flow ID to determine a transaction's state.

As a user steps through an SSO transaction, the transaction is always in some state. The state includes a status field and other fields specific to that state. The class containing those other fields is the model for the state.

The API endpoint returns the following when the user's SSO transaction has reached the `USERNAME_PASSWORD_REQUIRED` state for the form adapter.

```json
{
	"id": "PyH5g",
	"pluginTypeId": "7RmQNDWaOnBoudTufx2sEw",
	"status": "USERNAME_PASSWORD_REQUIRED",
	"showRememberMyUsername": false,
	"showThisIsMyDevice": false,
	"thisIsMyDeviceSelected": false,
	"showCaptcha": false,
	"rememberMyUsernameSelected": false,
	"_links": {
		"self": {
			"href": "https://localhost:9031/pf-ws/authn/flows/PyH5g"
		},
		"checkUsernamePassword": {
			"href": "https://localhost:9031/pf-ws/authn/flows/PyH5g"
		}
	}
}
```

The model for this state is the class `UsernamePasswordRequired`. It includes fields such as `showThisIsMyDevice`, which help the API client know how to render the credential prompt to the user.

The API response also includes a list of available actions. In this case, the only action available is `checkUsernamePassword`. The API client can select this action by sending a `POST` request with the `Content-Type` of `application/vnd.pingidentity.checkUsernamePassword+json`. Each action has its own model containing the fields that the `POST` body can provide. For the `checkUsernamePassword` action, the model is `CheckUsernamePassword`.

The `POST` body can be as simple as the following.

```json
{
	"username": "joe",
	"password": "2Federate"
}
```

After receiving this request, PingFederate calls the `lookupAuthN()` method of the form adapter. If the form adapter encounters an error while validating the credentials, it writes a JSON API error to the response. If the form adapter successfully validates the credentials, it returns `AUTHN_STATUS.SUCCESS` from its `lookupAuthN()`method. PingFederate then goes to the next step in the authentication policy. If the next step is an API-capable adapter, PingFederate calls `lookupAuthN()`on that adapter and the adapter determines its current state and writes it to the response, along with the available actions.

|   |                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The PingFederate authentication API follows a different naming convention for actions than PingOne. PingOne names actions as `noun.verb`, such as `otp.check`. PingFederate uses `verbNoun`, such as `checkOtp`. |

## Related links

* [Developing authentication API-capable adapters and selectors](pf_develop_auth_api_capable_adapt_selec.html)

---

---
title: Building and deploying manually
description: Use a build utility to add directories, create deployment descriptors, and create a .jarfile to build and deploy your plugins with PingFederate.
component: pingfederate
version: 13.1
page_id: pingfederate:sdk_developers_guide:build_deploy_manually
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/sdk_developers_guide/build_deploy_manually.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 3, 2023
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
---

# Building and deploying manually

Use a build utility to add directories, create deployment descriptors, and create a `.jar`file to build and deploy your plugins with PingFederate.

## Before you begin

To compile your project, you must have the following directories on your classpath:

* `<pf_install>/pingfederate/server/default/lib`

* `<pf_install>/pingfederate/lib`

* `<pf_install>/pingfederate/sdk/lib`

* `<pf_install>/pingfederate/sdk/plugin-src/<subproject-name>/lib`

## About this task

To build your project with another build utility, you must create the deployment descriptors for each of your plugins. The deployment descriptor files allow PingFederate to discover your plugins. Once this is complete, use the build tool to create a `.jar` file and deploy it within the appropriate directory.

## Steps

1. Add a new directory called `PF-INF` into your project. This directory must be at the root of your `.jar` file, similar to `META-INF`.

2. In `PF-INF`, add an appropriate text file for each type of plugin you created:

   | Plugin type                   | File name                      |
   | ----------------------------- | ------------------------------ |
   | IdP Adapter                   | idp-authn-adapters             |
   | SP Adapter                    | sp-authn-adapters              |
   | Custom Data Source            | custom-drivers                 |
   | Token Processor               | token-processors               |
   | Token Generator               | token-generators               |
   | Authentication Selector       | authentication-selectors       |
   | Password Credential Validator | password-credential-validators |
   | Identity Store Provisioner    | identity-store-provisioners    |
   | CIBA Authenticator            | oob-auth-plugins               |
   | Notification Publisher        | notification-sender            |

3. In each text file added, specify the fully-qualified class name of each plugin that implements the corresponding plugin interface. Place each class name on a separate line.

4. To create a `.jar`, archive the compiled class files along with the deployment descriptors using your build tool. The deployment descriptors must be in the `PF-INF` directory, located at the root of the `.jar` file.

5. To deploy your plugin, copy the `.jar` file and any third-party `.jar` files into the `<pf_install>/pingfederate/server/default/deploy` directory of the PingFederate installation.

---

---
title: Building and deploying with Ant
description: Use the Apache Ant build script to clean, build, package, and deploy projects within the PingFederate Java SDK.
component: pingfederate
version: 13.1
page_id: pingfederate:sdk_developers_guide:build_deploy_ant
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/sdk_developers_guide/build_deploy_ant.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Building and deploying with Ant

Use the Apache Ant build script to clean, build, package, and deploy projects within the PingFederate Java SDK.

## About this task

The PingFederate Java SDK comes with an Apache Ant build script that simplifies building and deploying your projects.

## Steps

1. Edit the `build.local.properties` file and set the `target-plugin.name` property to the name of your project subdirectory (see [SDK directory structure](pf_sdk_direct_struct.html)).

   |   |                                                                                                                                                                                                                        |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can develop source code for multiple projects simultaneously, but you can build and deploy only one at a time. Change the value of the `target-plugin.name` property as needed to build and deploy other projects. |

2. If your project depends on any third-party `.jar` files, place them into your project's `lib` directory.

   If the directory does not exist, create a new directory called `lib` directly under your project's directory. For example, `pingfederate/sdk/plugin-src/<subproject-name>/lib`.

3. On the command line in the `sdk` directory, use `ant` to clean, build, and package or to build, package, and deploy your project.

   | Option                                       | Description          |
   | -------------------------------------------- | -------------------- |
   | Clean the project                            | `ant clean-plugin`   |
   | Compile the project                          | `ant compile-plugin` |
   | Compile the project and create a `.jar` file | `ant jar-plugin`     |

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The SDK creates a deployment descriptor in the `PF_INF` directory and places it in a `.jar` file. The descriptor tells PingFederate what plugin implementations are contained in the file, and the compiled class files and the deployment descriptor are placed in the `pingfederate/sdk/plugin-src/<subproject-name>/build/classes` directory. The `pf.plugins.<subproject-name>.jar` file is placed in the `pingfederate/sdk/plugin-src/<subproject-name>/build/jar` directory. |

   To compile the project, create a .`jar` file, and deploy the project to PingFederate, enter:

   ```
   ant deploy-plugin
   ```

   This build target performs the steps described above and deploys any `.jar` files found in the `lib` directory of your subproject.

   |   |                                                                                                                                                                                                                    |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | To deploy your plugin manually to an installation of the PingFederate server, copy the `.jar` file and any third-party`.jar` files into the `/server/default/deploy/` directory of that PingFederate installation. |

4. Restart the PingFederate server.

---

---
title: Developing authentication API-capable adapters and selectors
description: The PingFederate authentication API lets applications interact with authentication policies. Making an adapter or selector plugin API-capable means ensuring that an authentication application can invoke the plugin through this API.
component: pingfederate
version: 13.1
page_id: pingfederate:sdk_developers_guide:pf_develop_auth_api_capable_adapt_selec
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/sdk_developers_guide/pf_develop_auth_api_capable_adapt_selec.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2022
section_ids:
  related-links: Related links
---

# Developing authentication API-capable adapters and selectors

The PingFederate authentication API lets applications interact with authentication policies. Making an adapter or selector plugin API-capable means ensuring that an authentication application can invoke the plugin through this API.

API-capable plugins must handle JSON-based API requests. When a plugin is invoked through the authentication API endpoint, if it needs interaction from the user, the plugin sends a JSON-based response rather than rendering a template.

Adapter and selector plugins handle distinct kinds of requests and generate distinct kinds of responses. The main method you implement in adapters is `lookupAuthN()`. The main method you implement in selectors is `selectContext()`.

Developing an API-capable plugin requires a dependency on the PingFederate authentication API SDK JAR file, `pf-authn-api-sdk-version.jar`. In the PingFederate installation package, you can find the SDK JAR file in the `server/default/lib` directory. Documentation for the classes are in the Javadocs for the standard PingFederate SDK, under `sdk/doc/index.html` in the PingFederate install package.

## Related links

* [Authentication API](../developers_reference_guide/pf_authentication_api.html)

* [Authentication API states, actions, and models](pf_authentication_api_states_actions_and_models.html)

* [Specification of the plugin API](pf_specification_plugin_api.html)

* [State model contents](pf_state_model_contents.html)

* [Non-interactive plugins](pf_noninteract_plugins.html)

* [Runtime behavior implementation](pf_runtime_behavior_implement.html)

* [Session state management](pf_sess_state_manage.html)

* [Error messages and localization](pf_error_messages_localization.html)

---

---
title: Developing authentication selectors
description: This topic describes aspects of authentication selectors within the context of PingFederate, including implementation, context selection, and callbacks.
component: pingfederate
version: 13.1
page_id: pingfederate:sdk_developers_guide:pf_develop_authen_select
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/sdk_developers_guide/pf_develop_authen_select.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  authentication-selector-interface: Authentication selector interface
  context-selection: Context selection
  authentication-selector-callback: Authentication selector callback
---

# Developing authentication selectors

This topic describes aspects of authentication selectors within the context of PingFederate, including implementation, context selection, and callbacks.

## Authentication selector interface

Authentication selectors allow PingFederate to choose an appropriate authentication source, an identity provider (IdP) adapter or an IdP connection (for federation hub use cases), based on criteria defined in the authentication selector instance.

When creating an authentication selector, use the following primary Java packages:

* `org.sourceid.saml20.adapter.gui`

* `org.sourceid.saml20.adapter.conf`

* `com.pingidentity.sdk`

For each authentication selector implementation, in addition to the methods described under [Shared plugin interfaces](pf_share_plugin_interface.html), you must define the following:

* Context Selection

* Authentication selector callback

## Context selection

PingFederate calls the `selectContext()` method to determine which authentication source to select. The `mappedAuthnSourcesNames` contains the list of `AuthenticationSourceKeys` and names that are available for the selector to reference.

```
AuthenticationSelectorContext selectContext(HttpServletRequest req,
 HttpServletResponse resp,
 Map<AuthenticationSourceKey, String> mappedAuthnSourcesNames,
 Map<String, Object> extraParameters,
 String resumePath)
```

The `HttpServletRequest` can evaluate cookies, parameters, headers, and other request information to determine which authentication source to select. The `HttpServletResponse` also helps determine the appropriate authentication source to select if the authentication selector requires user interaction. If the `resp` object is written to, it is considered a committed response and returned to the user's browser. The `resumePath` is a relative URL used in conjunction with the `resp` object, such that the user's browser is sent to this URL to resume the single sign-on (SSO) work flow.

After an authentication source is selected, you can create an `AuthenticationSelectorContext` to denote which authentication source to use. You can reference the selected authentication source by its ID or by its context, which is a name that decouples authentication selectors from the configured IDs.

## Authentication selector callback

PingFederate calls the `callback()` method after authenticating against a selected source. The `callback()` method allows authentication selectors to update resulting attributes, set cookies, or perform other custom functions.

```
void callback(HttpServletRequest req,
HttpServletResponse resp,
Map authnIdentifiers,
AuthenticationSourceKey authenticationSourceKey,
AuthenticationSelectorContext authnSelectorContext);
```

|   |                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Writing content to the `resp` object in the `callback()` method is not supported, and doing so might result in unexpected behavior. Setting cookies is supported. |

---

---
title: Developing data source connectors
description: Use PingFederate to query various data sources or build data source connectors to process customized data sources.
component: pingfederate
version: 13.1
page_id: pingfederate:sdk_developers_guide:pf_develop_data_source_connect
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/sdk_developers_guide/pf_develop_data_source_connect.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  data-source-connection-testing: Data source connection testing
  data-source-available-fields-retrieval: Data source available fields retrieval
  data-source-query-handling: Data source query handling
---

# Developing data source connectors

Use PingFederate to query various data sources or build data source connectors to process customized data sources.

PingFederate can query data sources for a variety of purposes using LDAP or Java Database Connectivity (JDBC) interfaces. Use the PingFederate SDK to build data source connectors to query additional data source types. Examples of other data sources include a web service, a flat file, or a different way of using a JDBC or LDAP connection than what is supplied by PingFederate.

The following are the primary Java packages used to build a custom data source:

* `com.pingidentity.sources`

* `com.pingidentity.sources.gui`

For each implementation described in [Shared plugin interfaces](pf_share_plugin_interface.html), you must define the following:

* Connection testing

* Available fields retrieval

* Data source query handling

## Data source connection testing

```
boolean testConnection()
```

When associating a custom data source with an identity provider (IdP) or service provider (SP) connection, PingFederate tests connectivity to the data source by calling the `testConnection()` method. Your implementation of this method should perform the necessary steps to demonstrate a successful connection and return `true`, or return `false` if your implementation cannot communicate with the datastore. A `false` result prevents an administrator from continuing with the data source configuration.

## Data source available fields retrieval

```
java.util.List<java.lang.String> getAvailableFields()
```

PingFederate calls the `getAvailableFields()` method to determine the available fields that can be returned from a query of this data source. These fields are displayed to the PingFederate administrator during the configuration of a data source lookup, and the administrator selects the attributes from the data source and maps them to the adapter or attribute contract. PingFederate requires at least one field returned from this method.

## Data source query handling

```
java.util.Map<java.lang.String,java.lang.Object> retrieveValues(
  java.util.Collection<java.lang.String> attributeNamesToFill,
  SimpleFieldList filterConfiguration)
```

When processing a connection using a custom data source, PingFederate calls the `retrieveValues()` method to perform the actual query for user attributes. This method receives a list of attribute names populated with data. The method can also receive a `filterConfiguration` object populated with a list of fields. Each field contains a name/value pair determined at runtime and collectively used as the criteria for selecting a specific record. In most cases, the criteria are used to locate additional user attributes.

Create the filter criteria selections needed for this lookup by passing back a `CustomDataSourceDriverDescriptor`, an implementation of `SourceDescriptor`, from the `getSourceDescriptor()` method. A `CustomDataSourceDriverDescriptor` can include a `FilterFieldDataDescriptor` composed of a list of fields that can be used as the query criteria. This list of fields is displayed similarly to the other UI-descriptor display fields.

|   |                                                                                                                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `filterConfiguration` object is set and populated with a list of fields only if the data source was defined with a `CustomDataSourceDriverDescriptor`. If the `CustomDataSourceDriverDescriptor` was not used in the definition of the data source, the `filterConfiguration` object is set to null. |

|   |                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | To pass runtime attribute values to the filter, an administrator must reference the attributes using the `${attribute name}` format when defining a filter in the PingFederate administrative console. |

After all relevant attributes are retrieved from the data source, they must be returned as a map of name/value pairs, where the names correspond to the initial collection of attribute names passed into the method and the values are the attributes.

---

---
title: Developing identity store provisioners
description: You can create an identity store provisioner by implementing either the IdentityStoreProvisionerWithFiltering or IdentityStoreProvisioner interface.
component: pingfederate
version: 13.1
page_id: pingfederate:sdk_developers_guide:pf_develop_identit_stor_provis
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/sdk_developers_guide/pf_develop_identit_stor_provis.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
---

# Developing identity store provisioners

You can create an identity store provisioner by implementing either the `IdentityStoreProvisionerWithFiltering` or `IdentityStoreProvisioner` interface.

Both interfaces support provisioning and deprovisioning users and groups to an external user store. The `IdentityStoreProvisionerWithFiltering` interface supports list/query and filtering; the `IdentityStoreProvisioner` interface does not. Learn more about list/query and filtering in [3.2.2. List/Query Resources and 3.2.2.1. Filtering](https://simplecloud.info/specs/draft-scim-api-01.html#query-resources) in the SCIM specification.

|   |                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The `IdentityStoreUserProvisioner` interface is deprecated. Developers should implement either the `IdentityStoreProvisionerWithFiltering` or `IdentityStoreProvisioner` interfaces. |

---

---
title: Developing IdP adapters
description: Developers can use the PingFederate SDK to create identity provider (IdP) adapters.
component: pingfederate
version: 13.1
page_id: pingfederate:sdk_developers_guide:pf_develop_idp_adapt
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/sdk_developers_guide/pf_develop_idp_adapt.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 25, 2024
section_ids:
  the-idp-authentication-adapter-interface: The IdP authentication adapter interface
  looking-up-user-attributes: Looking up user attributes
  managing-session-attributes: Managing session attributes
  designing-adapters-for-use-in-password-reset-or-password-change-policies: Designing adapters for use in password reset or password change policies
  terminating-sessions: Terminating sessions
---

# Developing IdP adapters

Developers can use the PingFederate SDK to create identity provider (IdP) adapters.

IdP adapters facilitate integration with external authentication systems, allowing user attributes to be looked up and sessions to be terminated during logout. In addition to performing the primary authentication step, IdP adapters can also perform secondary authentication steps to confirm the user's identity. Administrators can configure IdP adapters in sign-on authentication policies and in policies for resetting or changing passwords.

## The IdP authentication adapter interface

Developers can create an IdP adapter by implementing the `IdpAuthenticationAdapterV2` interface. Implementing this interface requires the following Java packages:

* `org.sourceid.saml20.adapter.idp.authn`

* `org.sourceid.saml20.adapter.gui`

* `org.sourceid.saml20.adapter.conf`

For each IdP adapter implementation, in addition to the methods described in [Shared plugin interfaces](pf_share_plugin_interface.html), you must define methods for:

* User attribute lookup

* Session termination

## Looking up user attributes

PingFederate invokes the `lookupAuthN()` method of your IdP adapter to look up user attributes for a request, regardless of whether the request is for IdP- or SP-initiated single sign-on (SSO), an OAuth transaction, or direct IdP-to-SP adapter processing. PingFederate uses the same method to authenticate a user when the adapter is placed in a password reset or password change policy.

```
AuthnAdapterResponse lookupAuthN(
  HttpServletRequest req,
  HttpServletResponse resp,
  Map<String, Object> inParameters)
  throws AuthnAdapterException, IOException;
```

|   |                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `IdpAuthenticationAdapterV2` interface provides an overloaded version of the `lookupAuthN()` method. The original `lookupAuthN()` method in the `IdpAuthenticationAdapter` interface is deprecated, so only use the method in the `IdpAuthenticationAdapterV2` interface. |

The parameters for the `lookupAuthN()` method are `HttpServletRequest`, the `HttpServletResponse`, and the `inParameters` map. The `inParameters` map contains important information about the SSO transaction that an adapter can use. The parameter keys are defined and documented in the `IdpAuthenticationAdapterV2` interface.

If an adapter is able to identify the user without further interaction, it can immediately return an `AuthnAdapterResponse` containing the user attributes. If the adapter needs further interaction, it can write to the `HttpServletResponse` as appropriate and commit it. Immediately after invoking `lookupAuthN()`, PingFederate checks if the response has been committed. If it has been committed, PingFederate saves the state it needs and stops processing the current transaction. PingFederate continues processing the transaction when the browser returns to the transaction's resume path, at which point PingFederate again invokes the `lookupAuthN()` method. This series of events will be repeated until the method returns without committing the response. When that happens, which could be during the first invocation, PingFederate continues transaction processing using the result of the method.

|   |                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If the response is committed, then PingFederate ignores the return value. It only uses the return value of an invocation that does not commit the response. |

The return type of `lookupAuthN()` is `AuthnAdapterResponse`. When the adapter has completed its processing and returns a value, it must populate the `authnStatus` field of this object. If the `authnStatus` is `SUCCESS`, it must also provide the user attributes in the `attributeMap` field. There are several attribute keys with special meanings, which are defined and documented in the `IdpAuthenticationAdapterV2` interface.

Two basic styles of IdP adapter are common. In the first style, the adapter presents the user a form in which the user enters their credentials to authenticate themselves. Such adapters can use the `TemplateRendererUtil` class to render an HTML template in the user's browser. An example of such an adapter is `template-render-adapter-example`, which is in the `/sdk/plugin-src` directory of PingFederate. That example also shows how you can develop an interactive adapter that supports the PingFederate authentication API. For more information, see [Developing authentication API-capable adapters and selectors](pf_develop_auth_api_capable_adapt_selec.html).

The second style of IdP adapter redirects the user to an external authentication system. After the user has been authenticated, the external system must redirect the user to the resume path for the SSO transaction. This path is provided to the adapter in the `inParameters` map using the key `IN_PARAMETER_NAME_RESUME_PATH`.

How the user attributes are returned to the adapter is up to the implementation. If the authentication system provides an API for retrieving user attributes, a reference to the attributes can be passed through a query parameter appended to the resume URL. Alternatively, if the authentication system shares a parent domain with PingFederate, a cookie can be used to communicate the user attributes.

The following diagram and numbered list show the request sequence for an adapter that redirects to an external authentication system.

![Diagram with user, application server, and PingFederate server icons that illustrate the SSO request sequence for an IdP adapter that redirects to an external authentication system.](_images/smn1662051350052.jpg)

IdP-initiated SSO sequence:

1. A user signs on to a local application or domain through an authentication mechanism such as an identity-management system.

2. The user requests access to a protected resource located in the service provider (SP) domain. The link or other mechanism invokes the PingFederate SSO service.

3. PingFederate invokes the designated adapter's lookup method, including the `resumePath` parameter.

4. The application server returns the session information and redirects the browser along with the returned information to the `[.codeph]`resumePath\`\`\`\` URL.

5. PingFederate generates a SAML assertion and sends the browser with the SAML assertion to the SP's SAML gateway.

## Managing session attributes

The PingFederate SDK allows adapters to track session attributes. These attributes are stored in memory and replicated across multiple cluster nodes. They are looked up using the attribute name and the `PF` cookie from the user's browser.

Session attributes can be global, spanning multiple SSO transactions, or be linked to a specific transaction. To avoid prompting the user again for credentials, an adapter could use a global session attribute containing the user attributes that were obtained when the user first signed on. A multi-factor authentication (MFA) adapter can use a transaction-scoped attribute to keep track of a one-time passcode that was sent to the user's mobile device. Use `SessionStateSupport` to keep track of global attributes and use `TransactionalStateSupport` to track attributes for the current transaction. It's important to remove transactional attributes when your adapter is finished processing and about to return a result from `lookupAuthN()`. This reduces heap usage and, more importantly, helps avoid subtle security issues.

PingFederate can maintain an authentication session on behalf of your adapter. If an authentication session is enabled for your adapter and user attributes were obtained through a previous call to `lookupAuthN()`, then PingFederate will avoid calling `lookupAuthN()` during subsequent SSO transactions, provided the session idle or maximum timeout has not been exceeded.

Generally, it's better to rely on the PingFederate authentication session capability, rather than implementing your own within your adapter. If you do implement an internal session capability, ensure this session is not used when the authentication policy for the transaction indicates that reauthentication is required. The policy for the transaction is passed in the `inParameters` map using the key `IN_PARAMETER_NAME_AUTHN_POLICY`.

## Designing adapters for use in password reset or password change policies

The HTML Form Adapter can invoke an authentication policy during password reset or password change operations. When your adapter is invoked as part of such a policy, `IN_PARAMETER_NAME_USERID` refers to the username the user entered at the start of the operation.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Consider the following when designing adapters that will be used in password reset or password change policies.If your adapter can track an internal session, an existing session should not be used during a password reset or password change transaction. PingFederate will ensure the reauthenticate flag in the transaction policy (`IN_PARAMETER_NAME_AUTHN_POLICY` in the `inParameters` map) is set to `true`. When this flag is `true`, your adapter should ignore any existing session.Session attributes that track the progress of the current authentication attempt should be stored using `TransactionalStateSupport` and must be removed when returning a success or failure result from `lookupAuthN()`. In particular, if your adapter tracks a session attribute indicating the authentication was successful (for example, to render a "Success" page to the user), you should store that attribute using `TransactionalStateSupport` and ensure it's removed before returning `AUTHN_STATUS.SUCCESS` from `lookupAuthN()`. |

## Terminating sessions

During single logout (SLO) request processing, PingFederate invokes your IdP adapter's `logoutAuthN()` method to terminate a user's session. This method is invoked during IdP- or SP-initiated SLO requests.

```
boolean logoutAuthN(Map authnIdentifiers,
  HttpServletRequest req,
  HttpServletResponse resp,
  String resumePath)
  throws AuthnAdapterException, IOException
```

Like the `lookupAuthN()` method, the `logoutAuthN()` method has access to the `HttpServletRequest` and `HttpServletResponse` objects. The user attributes returned earlier from `lookupAuthN()` are also passed as the input parameter `authnIdentifiers`.

If your adapter maintains an internal session, it should remove associated session attributes during `logoutAuthN()`. If the adapter is associated with an external authentication system, it can redirect the browser to an endpoint used to terminate the session at the application. The `resumePath` parameter contains the URL to which the user is redirected to complete the SLO process.

---

---
title: Developing notification publishers
description: To develop a notification publisher, implement the NotificationPublisherPlugin interface.
component: pingfederate
version: 13.1
page_id: pingfederate:sdk_developers_guide:develop_notific_publisher
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/sdk_developers_guide/develop_notific_publisher.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
---

# Developing notification publishers

To develop a notification publisher, implement the `NotificationPublisherPlugin` interface.

PingFederate administrators can define and manage notification publishers, as described in [Managing notification publisher instances](../administrators_reference_guide/help_notificationsendertasklet_notificationsendermanagementstate.html). If those features do not meet your needs, you can develop a custom notification publisher using the PingFederate `NotificationPublisherPlugin` interface and the following Java packages:

* `com.pingidentity.sdk`

* `org.sourceid.saml20.adapter.conf`

* `org.sourceid.saml20.adapter.gui`

The `NotificationPublisherPlugin` interface, which extends the `Plugin` interface, defines the `publishNotification()` method.

For each implementation, define the `publishNotification()` method, in addition to the methods described in [Shared plugin interfaces](pf_share_plugin_interface.html). PingFederate invokes the `publishNotification()` method when publishing a notification. For example, you can configure PingFederate so that an account password change invokes the method.

```
PublishResult publishNotification(String eventType,
  Map<String, String> data,
  Map<String, String> configuration)
```

The method returns the `PublishResult`, the status of the notification that the plugin instance sent.

For more information about the `NotificationPublisherPlugin` interface, see the SDK Javadocs. You can also see a sample implementation in `pingfederate/sdk/plugin-src`.

---

---
title: Developing password credential validators
description: Password credential validators allow PingFederate administrators to define a centralized location for username/password validation, allowing PingFederate configurations to reference validator instances.
component: pingfederate
version: 13.1
page_id: pingfederate:sdk_developers_guide:pf_develop_pass_credent_vallidat
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/sdk_developers_guide/pf_develop_pass_credent_vallidat.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
---

# Developing password credential validators

Password credential validators allow PingFederate administrators to define a centralized location for username/password validation, allowing PingFederate configurations to reference validator instances.

To implement a custom password credential validator, import the following Java packages:

* `org.sourceid.saml20.adapter.gui`

* `org.sourceid.saml20.adapter.conf`

* `org.sourceid.util.log`

* `com.pingidentity.sdk`

* `com.pingidentity.sdk.password`

For each implementation, in addition to the methods described under [Shared plugin interfaces](pf_share_plugin_interface.html), you must define the following method.

```
AttributeMap processPasswordCredential(String username,
  String password)
  throws PasswordValidationException
```

This method takes a username and password and verifies the credential against an external source. If the credentials are valid, it returns an \[.apiname]AttributeMap containing at least one entry representing the principal. If the credentials are invalid, then it returns `null` or an empty map. If the plugin was unable to validate the credentials (for example, due to an offline host or network problems), it returns a `PasswordValidationException`.

To enable password changes in a password credential validator, implement the `com.pingidentity.sdk.password.ChangeablePasswordCredential` interface.

To enable password resets in a password credential validator, implement the `com.pingidentity.sdk.password.ResettablePasswordCredential` interface.

|   |                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Depending on your password management system, you might need additional system configuration to enable password changes. For example, you can change passwords in Active Directory only if LDAPS is enabled. |

---

---
title: Developing SP adapters
description: This topic describes how to create a service provider (SP) adapter, as well as the methods used during SP session creation, SP adapter session logout, and SP account linking.
component: pingfederate
version: 13.1
page_id: pingfederate:sdk_developers_guide:pf_develop_sp_adapt
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/sdk_developers_guide/pf_develop_sp_adapt.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  sp-authentication-adapter-interface: SP authentication adapter interface
  sp-session-creation: SP session creation
  sp-adapter-session-logout: SP adapter session logout
  sp-account-linking: SP account linking
---

# Developing SP adapters

This topic describes how to create a service provider (SP) adapter, as well as the methods used during SP session creation, SP adapter session logout, and SP account linking.

## SP authentication adapter interface

Create service provider (SP) adapters by implementing the `SPAuthenticationAdapter` interface. Implementing this interface requires the following Java packages:

* `org.sourceid.saml20.adapter.sp.authn`

* `org.sourceid.saml20.adapter.gui`

* `org.sourceid.saml20.adapter.conf`

For each SP adapter implementation, in addition to the methods described in [Shared plugin interfaces](pf_share_plugin_interface.html), you must define:

* SP session creation

* SP adapter session logout

* SP account linking

## SP session creation

PingFederate invokes the `createAuthN()` method during the processing of a single sign-on (SSO) request to establish a security context in the external application for the user.

```
java.io.Serializable createAuthN(SsoContext ssoContext,
  javax.servlet.http.HttpServletRequest req,
  javax.servlet.http.HttpServletResponse resp,
  java.lang.String resumePath)
```

This method resembles the `IdpAuthenticationAdapter.lookupAuthN()` method in terms of the objects passed to it and its support for asynchronous requests using the `HttpServletResponse` and `resumePath` parameters. It also accepts an `SsoContext` object, which has access to information such as user attributes and the target destination URL.

## SP adapter session logout

PingFederate invokes the `logoutAuthN()` method during a single logout (SLO) request to terminate a user's session with the external application.

```
boolean logoutAuthN (java.io.Serializable authnBean,
  javax.servlet.http.HttpServletRequest req,
  javax.servlet.http.HttpServletResponse resp,
  java.lang.String resumePath)
  throws AuthnAdapterException, java.io.IOException
```

The `HttpServletResponse` and `resumePath` objects are available to support scenarios where the user's browser redirects to an additional service to clean up any remaining sessions.

## SP account linking

PingFederate invokes the `lookupLocalUserId()` method during an SSO request when the identity provider (IdP) connection uses account linking but no account link for this user is yet established.

```
java.lang.String lookupLocalUserId(
    javax.servlet.http.HttpServletRequest req,
    javax.servlet.http.HttpServletResponse resp,
    java.lang.String partnerIdpEntityId,
    java.lang.String resumePath)
    throws AuthnAdapterException, java.io.IOException
```

After the account link is set, PingFederate maintains this information until the user defederates, which occurs when the user clicks a hyperlink redirecting them to the `/sp/defederate.ping` PingFederate endpoint.

The `HttpServletResponse` and `resumePath` objects are used to send the user to a local service where the user authenticates. After authentication, the user is redirected to the URL specified in the `resumePath` parameter and PingFederate completes the account link.

The following diagram illustrates a typical account-link sequence.

![A typical account-link sequence](_images/eri1564003666673.jpg)

Use the `HttpServletRequest` to read a local session token. The `lookupLocalUserId()` method should return a local user identifier `String` object.

---

---
title: Developing token generators
description: You can create a token-generator implementation by using the TokenGenerator interface.
component: pingfederate
version: 13.1
page_id: pingfederate:sdk_developers_guide:pf_develop_token_generat
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/sdk_developers_guide/pf_develop_token_generat.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
---

# Developing token generators

You can create a token-generator implementation by using the `TokenGenerator` interface.

The following Java packages are required for implementing the `TokenGenerator` interface:

* `org.sourceid.saml20.adapter.sp.authn`

* `org.sourceid.saml20.adapter.gui`

* `org.sourceid.saml20.adapter.conf`

* `org.sourceid.wstrust.model`

* `org.sourceid.wstrust.plugin`

* `org.sourceid.wstrust.plugin.process`

* `com.pingidentity.sdk`

For each token-generator implementation, in addition to the methods described under [Shared plugin interfaces](pf_share_plugin_interface.html), you must define the `SecurityToken generateToken(TokenContext attributeContext)` method.

PingFederate invokes the `generateToken()` method when processing a security token service (STS) request to perform necessary operations for generation of a security token. The type `BinarySecurityToken` is available and you can use it to represent custom security tokens that can be transported as Base64-encoded data. The `TokenContext` contains subject data available for insertion into the generated security token.

---

---
title: Developing token processors
description: You can create a token processor by implementing the TokenProcessor interface.
component: pingfederate
version: 13.1
page_id: pingfederate:sdk_developers_guide:pf_develop_token_process
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/sdk_developers_guide/pf_develop_token_process.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
---

# Developing token processors

You can create a token processor by implementing the `TokenProcessor` interface.

The following Java packages are required for implementing the `TokenProcessor` interface:

* `org.sourceid.saml20.adapter.attribute`

* `org.sourceid.saml20.adapter.idp.authn`

* `org.sourceid.saml20.adapter.gui`

* `org.sourceid.saml20.adapter.conf`

* `org.sourceid.wstrust.model`

* `org.sourceid.wstrust.plugin`

* `org.sourceid.wstrust.plugin.process`

* `com.pingidentity.sdk`

For each token-processor implementation, in addition to the methods described under [Shared plugin interfaces](pf_share_plugin_interface.html), you must define the `TokenContext processToken(T token)` method.

PingFederate invokes the `processToken()` method when processing a security token service (STS) request to perform necessary operations for determining the validity of a token. The type parameter `T` must extend, at a minimum, the type `SecurityToken`. The type `BinarySecurityToken` is also available to represent custom security tokens that can be transported as Base64-encoded data.

---

---
title: Developing your own plugin
description: You can set up a development environment within the SDK and use it to create a plugin.
component: pingfederate
version: 13.1
page_id: pingfederate:sdk_developers_guide:pf_develop_your_plugin
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/sdk_developers_guide/pf_develop_your_plugin.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 25, 2025
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  result: Result:
---

# Developing your own plugin

You can set up a development environment within the SDK and use it to create a plugin.

## Before you begin

Make sure the Java SDK and Apache Ant are installed.

|   |                                            |
| - | ------------------------------------------ |
|   | The PingFederate SDK only supports JDK 11. |

## About this task

The Java SDK, along with Apache Ant, enables you to create directories for your project and use the build script to build, clean, or deploy it.

## Steps

1. Create a new project directory in the `<pf_install>/pingfederate/sdk/plugin-src` directory.

2. In the new project directory, create a subdirectory named `java`.

   This is where you place the Java source code for your implementation. Follow standard Java package and directory structure layout.

3. If your project depends on third-party libraries, create another subdirectory called `lib` and place the necessary `.jar` files in it.

4. Edit the `build.local.properties` file and set `target-plugin.name` to specify the name of the directory that contains your project.

5. Run the appropriate build target to clean, build, or deploy your plugin.

6. (Optional) To display a list of available build targets, run `ant` from `<pf_install>/pingfederate/sdk`.

   |   |                                                                                                         |
   | - | ------------------------------------------------------------------------------------------------------- |
   |   | Typically, these build targets are executed in the order `clean-plugin`, `jar-plugin`, `deploy-plugin`. |

   ```
   [java] Main targets:
   [java]
   [java] clean-plugin Clean the plug-in build directory
   [java] deploy-plugin Deploy the plug-in jar and libs to PingFederate
   [java] jar-plugin    Package the plug-in jar
   [java]
   [java] Default target: help
   ```

   |   |                                                                                                                                                                                           |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Because it packages the `.jar` files with additional metadata to make them discoverable by PingFederate, we recommend building the project with the `build.xml` file included in the SDK. |

### Result:

After you successfully run the `deploy-plugin` build target, the plugin is available the next time you restart PingFederate.

---

---
title: Error messages and localization
description: Error messages are the one case where an API response could include user-facing text. The typical case is a validation error.
component: pingfederate
version: 13.1
page_id: pingfederate:sdk_developers_guide:pf_error_messages_localization
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/sdk_developers_guide/pf_error_messages_localization.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  related-links: Related links
---

# Error messages and localization

Error messages are the one case where an API response could include user-facing text. The typical case is a validation error.

For validation errors, the adapter constructs an `AuthnError` with the code `VALIDATION_ERROR`, and then adds `AuthnErrorDetail` objects for each of the errors that occurred. The `userMessage` field of the `AuthnErrorDetail` object provides the user-facing text. Like states and actions, you can define errors up front using an `AuthnErrorSpec` or an `AuthnErrorDetailSpec`. Then an instance of the error is constructed from the specification on demand.

The following example shows how you can define the specification for an invalid OTP error.

```
public final static AuthnErrorDetailSpec INVALID_OTP = new AuthnErrorDetailSpec.Builder()
	.code("INVALID_OTP")
	.message("An invalid or expired OTP code was provided.")
	.userMessage("This code is invalid or has expired.")
	.parentCode(CommonErrorSpec.VALIDATION_ERROR.getCode())
	.build();
```

The following example shows how you can use that specification to send an error response to the API client.

```
AuthnErrorDetail errorDetail = ErrorDetailSpec.INVALID_OTP.makeInstanceBuilder().build();
AuthnError authnError = CommonErrorSpec.VALIDATION_ERROR.makeInstanceBuilder().detail(errorDetail).build();
apiSupport.writeErrorResponse(req, resp, authnError);
```

To localize the error message using a properties file for your adapter, you can use `LocaleUtil` and `LanguagePackMessages` from the standard PingFederate SDK.

```
LanguagePackMessages messages = new LanguagePackMessages("my-adapter-messages", LocaleUtil.getUserLocale(req));
String errorMessage = messages.getMessage("invalid.otp.key", new String[]{});
AuthnErrorDetail errorDetail = ErrorDetailSpec.INVALID_OTP.makeInstanceBuilder().userMessage(errorMessage).build();
AuthnError authnError = CommonErrorSpec.VALIDATION_ERROR.makeInstanceBuilder().detail(errorDetail).build();
apiSupport.writeErrorResponse(req, resp, authnError);
```

For more information about how PingFederate determines the user's locale at runtime, see [Override locale using cookies](../administrators_reference_guide/pf_override_locale_cookies.html).

Some errors reflect problems with API client programming rather than with end user input. If you think an error will not be shown to an end user, then you do not need to populate the `userMessage` field.

## Related links

* [Developing authentication API-capable adapters and selectors](pf_develop_auth_api_capable_adapt_selec.html)

---

---
title: IdentityStoreUserProvisioner interface implementation
description: The IdentityStoreUserProvisioner interface is deprecated, but you can still implement it to provision and deprovision users to an external user store.
component: pingfederate
version: 13.1
page_id: pingfederate:sdk_developers_guide:identitystoreuserprovisioner_interface_implemen
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/sdk_developers_guide/identitystoreuserprovisioner_interface_implemen.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  create-user: Create user
  read-user: Read user
  update-user: Update user
  delete-user: Delete user
---

# IdentityStoreUserProvisioner interface implementation

The `IdentityStoreUserProvisioner` interface is deprecated, but you can still implement it to provision and deprovision users to an external user store.

The `IdentityStoreUserProvisioner` interface is deprecated. Developers can implement it to provision and deprovision users, but they should implement either the `IdentityStoreProvisionerWithFiltering` or `IdentityStoreProvisioner` interface.

|   |                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The `IdentityStoreUserProvisioner` interface does not provision or deprovision groups. For group support, see [`IdentityStoreProvisionerWithFiltering` interface implementation](identitystoreprovisionerwithfiltering_interface_implemen.html). |

The following Java packages are required for implementing the interface:

* `com.pingidentity.sdk.provision`

* `com.pingidentity.sdk.provision.exception`

* `com.pingidentity.sdk.provision.users.request`

* `com.pingidentity.sdk.provision.users.response`

For each identity store provisioner implementation, in addition to the methods described under [Shared plugin interfaces](pf_share_plugin_interface.html), you must implement the following methods:

* Create user

* Read user

* Update user

* Delete user

## Create user

```
UserResponseContext createUser(CreateUserRequestContext createRequestCtx)
throws IdentityStoreException
```

PingFederate invokes the `createUser()` method of your identity store provisioner in response to create-user requests made to PingFederate services, such as inbound provisioning. This method creates the user in the user store managed by the identity store provisioner.

The `CreateUserRequestContext` contains all information needed to fulfill the request. If the user is successfully provisioned, the method returns a `UserResponseContext` containing the user attributes used to provision the user. The method throws an `IdentityStoreException` if an error occurred during the creation process. See the `com.pingidentity.sdk.provision.exception` package for exceptions that can be thrown.

## Read user

```
UserResponseContext readUser(ReadUserRequestContext readRequestCtx)
throws IdentityStoreException
```

PingFederate invokes the `readUser()` method of your identity store provisioner in response to get-user requests made to PingFederate services, such as inbound provisioning. This method retrieves user data from the user store managed by the identity store provisioner.

The `ReadUserRequestContext` contains all information needed to fulfill the request. If the user data is successfully retrieved, the method returns a `UserResponseContext` containing the user attributes for the user. The method throws an `IdentityStoreException` if an error occurred during the retrieval process. See the `com.pingidentity.sdk.provision.exception` package for exceptions that can be thrown.

## Update user

```
UserResponseContext updateUser(UpdateUserRequestContext updateRequestCtx)
throws IdentityStoreException
```

PingFederate invokes the `updateUser()` method of your identity store provisioner in response to update-user requests made to PingFederate services, such as inbound provisioning. This method updates the user in the user store managed by the identity store provisioner.

The `UpdateUserRequestContext` contains all information needed to fulfill the request. If the user data is successfully updated, the method returns a `UserResponseContext` containing the user's updated attributes. The method throws an `IdentityStoreException` if an error occurred during the update process. See the `com.pingidentity.sdk.provision.exception` package for exceptions that can be thrown.

## Delete user

```
void deleteUser(DeleteUserRequestContext deleteRequestCtx)
throws IdentityStoreException
```

PingFederate invokes the `deleteUser()` method of your identity store provisioner in response to delete-user requests made to PingFederate services, such as inbound provisioning. This method deprovisions the user in the user store managed by the identity store provisioner.

The `DeleteUserRequestContext` contains all information needed to fulfill the request. The method throws an `IdentityStoreException` if an error occurred during the deprovision process. See the `com.pingidentity.sdk.provision.exception` package for exceptions that can be thrown.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The plugin implementation can choose not to permanently delete the resource, but must return a `NotFoundException` for all `readUser()`, `updateUser()`, and `deleteUser()` operations associated with the previously deleted ID. In addition, the plugin must not consider the deleted user in conflict calculation. For example, a `createUser()` request for a user with a previously deleted ID should not throw a `ConflictException`. |

---

---
title: Implementation guidelines
description: The following topics provide programming guidance for developing custom interfaces.
component: pingfederate
version: 13.1
page_id: pingfederate:sdk_developers_guide:pf_implement_guideline
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/sdk_developers_guide/pf_implement_guideline.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 26, 2023
---

# Implementation guidelines

The following topics provide programming guidance for developing custom interfaces.

* [Shared plugin interfaces](pf_share_plugin_interface.html)

* [Developing IdP adapters](pf_develop_idp_adapt.html)

* [Developing authentication API-capable adapters and selectors](pf_develop_auth_api_capable_adapt_selec.html)

* [Developing SP adapters](pf_develop_sp_adapt.html)

* [Developing token processors](pf_develop_token_process.html)

* [Developing token generators](pf_develop_token_generat.html)

* [Developing authentication selectors](pf_develop_authen_select.html)

* [Developing data source connectors](pf_develop_data_source_connect.html)

* [Developing password credential validators](pf_develop_pass_credent_vallidat.html)

* [Developing identity store provisioners](pf_develop_identit_stor_provis.html)

* [Developing notification publishers](develop_notific_publisher.html)

* [Building and deploying with Ant](build_deploy_ant.html)

* [Building and deploying manually](build_deploy_manually.html)

* [Log messages](log_messages.html)

For more details about interfaces discussed here and additional functionality, see the SDK Javadocs.

---

---
title: Log messages
description: You can use a typical logging pattern based on the Apache Commons logging framework to log messages from your adapter, token translator, or custom data source driver.
component: pingfederate
version: 13.1
page_id: pingfederate:sdk_developers_guide:log_messages
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/sdk_developers_guide/log_messages.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
---

# Log messages

You can use a typical logging pattern based on the Apache Commons logging framework to log messages from your adapter, token translator, or custom data source driver.

The service provider (SP) adapter contained in the directory `sdk/adapters-src/sp-adapter-example` shows how to use a logger for your adapter.

---

---
title: Non-interactive plugins
description: Some plugins, typically selectors, do not need to interact with the user to do their job. Making these plugins API-capable is straight-forward.
component: pingfederate
version: 13.1
page_id: pingfederate:sdk_developers_guide:pf_noninteract_plugins
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/sdk_developers_guide/pf_noninteract_plugins.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  related-links: Related links
---

# Non-interactive plugins

Some plugins, typically selectors, do not need to interact with the user to do their job. Making these plugins API-capable is straight-forward.

You still implement the `AuthnApiPlugin` interface, but you can just return null from the `getApiSpec()` method. And then you override the default implementation of `getApiPluginDescriptor()` and return an `AuthnApiPluginDescriptor` instance with the `interactive` flag set to `false`. As with many other classes in the SDK, there is an `AuthnApiPluginDescriptor.Builder` class to help in creating the descriptor.

When `interactive` is `false`, PingFederate knows that it never needs to redirect when it encounters your selector. If the request is occurring on the API endpoint, PingFederate can immediately call `selectContext()`. The same is true if the request is occurring on a front-channel endpoint, such as `/as/authorization.oauth2`.

If your selector does not implement `AuthnApiPlugin`, then PingFederate assumes that only a front-channel endpoint can call your selector. If PingFederate encounters your selector while executing an API request, PingFederate will send a `RESUME` response to the API client so that the user is redirected to PingFederate.

## Related links

* [Developing authentication API-capable adapters and selectors](pf_develop_auth_api_capable_adapt_selec.html)