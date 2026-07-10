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

---

---
title: Runtime behavior implementation
description: After you specify your plugin's API at least partially, you can start implementing the runtime behavior. Use the specification that you defined previously to implement the runtime functionality.
component: pingfederate
version: 13.1
page_id: pingfederate:sdk_developers_guide:pf_runtime_behavior_implement
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/sdk_developers_guide/pf_runtime_behavior_implement.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  related-links: Related links
  checking-for-actions: Checking for actions
  extracting-models-from-requests: Extracting models from requests
  performing-additional-validation: Performing additional validation
  handling-invalid-action-ids: Handling invalid action IDs
  handling-authentication-error-exceptions: Handling authentication error exceptions
  sending-api-responses: Sending API responses
  returning-authentication-statuses: Returning authentication statuses
---

# Runtime behavior implementation

After you specify your plugin's API at least partially, you can start implementing the runtime behavior. Use the specification that you defined previously to implement the runtime functionality.

Follow this pattern in `lookupAuthN()`:

1. Check for the possible actions the adapter expects in the current state.

2. If an action is matched, then try to extract the expected model from the request and handle the action.

3. If an action is requested, but it does not match an action allowed for the current state, then return an `INVALID_ACTION_ID` error.

4. If no action is requested, render the response for the current state.

The `AuthnApiSupport` class provides much of the functionality for handling API requests and sending responses. The `TemplateRenderAdapter` stores a reference to this singleton in its `apiSupport` field.

```
private AuthnApiSupport apiSupport = AuthnApiSupport.getDefault();
```

## Related links

* [Developing authentication API-capable adapters and selectors](pf_develop_auth_api_capable_adapt_selec.html)

## Checking for actions

The following code shows the preferred approach for checking for the `submitIdentifiers` action.

The adapter performs this check two ways, depending on whether the current request is from the API endpoint. The `TemplateRenderAdapter` uses a slightly different but equivalent method.

```
/**
 * Determine if the user chose "Submit".
 */
private boolean isSubmitAttributesRequest(HttpServletRequest req)
{
	if (apiSupport.isApiRequest(req))
	{
		return ActionSpec.SUBMIT_USER_ATTRIBUTES.isRequested(req);
	}
	return StringUtils.isNotBlank(req.getParameter("pf.submit"));
}
```

## Extracting models from requests

The next step extracts the model from the request. This step varies depending on whether the request is from the API endpoint. For an API request, call the `AuthnApiSupport.deserializeAsModel()` method. For a non-API request, you must build the model from the parameters in the request.

```
private SubmitUserAttributes getSubmittedAttributes(HttpServletRequest req) throws AuthnErrorException, AuthnAdapterException
{
	if (apiSupport.isApiRequest(req))
	{
		try
		{
			return apiSupport.deserializeAsModel(req, SubmitUserAttributes.class);
		}
		catch (IOException e)
		{
			throw new AuthnAdapterException(e);
		}
	}
	else
	{
		SubmitUserAttributes result = new SubmitUserAttributes();
		result.setUsername(req.getParameter("username"));

		for (String key : extendedAttr)
		{
			result.getUserAttributes().put(key, req.getParameter(key));
		}
		return result;
	}
}
```

The `deserializeAsModel()` method also does some validation on the incoming JSON. This includes checking for fields flagged as `required` in the model, using the @Schema annotation. If a validation error occurs during this step, the method throws an `AuthnErrorException`, which the adapter can convert to an API error response. For more information, see [Handling authentication error exceptions](#_handling_authentication_error_exceptions).

## Performing additional validation

The `deserializeAsModel()` method performs some basic validation on the submitted JSON. Your adapter probably needs to perform more validation and send an `AuthnError` to the API client if it finds any errors. Here is how the `TemplateRenderAdapter` validates the names of the provided user attributes:

```
private void validateSubmittedAttributes(HttpServletRequest req, SubmitUserAttributes submitted) throws AuthnErrorException
{
	if (apiSupport.isApiRequest(req))
	{
		List<AuthnErrorDetail> errorDetails = new ArrayList<>();
		for (String attrName : submitted.getUserAttributes().keySet())
		{
			if (!extendedAttr.contains(attrName))
			{
				errorDetails.add(ErrorDetailSpec.INVALID_ATTRIBUTE_NAME.makeInstanceBuilder()
					.message("Invalid attribute name: " + attrName).build());
			}
		}
		if (!errorDetails.isEmpty())
		{
			AuthnError authnError = CommonErrorSpec.VALIDATION_ERROR.makeInstance();
			authnError.setDetails(errorDetails);
			throw new AuthnErrorException(authnError);
		}
	}
}
```

## Handling invalid action IDs

If a request from an API client includes an action ID that does not match any actions available in the current state, it is best practice to return an error to the client.

After checking all the possible actions, if none match and the request's action ID is not null, the adapter can throw an `AuthnErrorException`. The adapter catches this exception and writes an error to the API response.

```
if (apiSupport.getActionId(req) != null)
{
	// An action ID was provided but it does not match one of those expected in the current state.
	throw new AuthnErrorException(CommonErrorSpec.INVALID_ACTION_ID.makeInstance());
}
```

## Handling authentication error exceptions

If the `deserializeAsModel()` method detects an error while deserializing the model, it throws an `AuthnErrorException`. If the added validation checks in `validateSubmittedAttributes` detect an error, they also throw this exception.

The adapter should catch this exception and send an API error response using the method `AuthnApiSupport.writeErrorResponse()`.

```
try
{
	...
}
catch (AuthnErrorException e)
{
	// A validation error occurred while processing an API request, return an error response to the API client
	apiSupport.writeErrorResponse(req, resp, e.getValidationError());
	authnAdapterResponse.setAuthnStatus(AUTHN_STATUS.IN_PROGRESS);
	return authnAdapterResponse;
}
```

## Sending API responses

`AuthnApiSupport` provides several methods for writing API responses.

The following example shows how the `TemplateRenderAdapter` writes the response for the `USER_ATTRIBUTES_REQUIRED` state.

```
private void renderApiResponse(HttpServletRequest req, HttpServletResponse resp, Map<String, Object> inParameters) throws AuthnAdapterException
{
	UserAttributesRequired model = new UserAttributesRequired();
	model.setAttributeNames(new ArrayList<>(extendedAttr));
	AuthnState<UserAttributesRequired> authnState = apiSupport.makeAuthnState(req, StateSpec.USER_ATTRIBUTES_REQUIRED, model);
	try
	{
		apiSupport.writeAuthnStateResponse(req, resp, authnState);
	}
	catch (IOException e)
	{
		throw new AuthnAdapterException(e);
	}
}
```

The `makeAuthnState()` method takes an `AuthnStateSpec` and an instance of the model for that state and builds an `AuthnState` object. The `AuthnState` object can then be further modified. For example, you could remove an action that is not currently applicable using the `removeAction()` method. Then you write the `AuthnState` object to the response using the `writeAuthnStateResponse()` method.

## Returning authentication statuses

As with non-API requests, when the adapter finishes, it returns `AUTHN_STATUS.SUCCESS` or `AUTHN_STATUS.FAILURE` from `lookupAuthN()`.

If the adapter has not yet finished and has written something to the response, it should return `AUTHN_STATUS.IN_PROGRESS`.

---

---
title: SDK Developer&#8217;s Guide
description: The PingFederate Software Development Kit (SDK) enables integration with identity provider (IdP) and service provider (SP). The SDK allows your application developers and system administrators to build custom implementations for communicating authentication and security information between PingFederate and your enterprise environment.
component: pingfederate
version: 13.1
page_id: pingfederate:sdk_developers_guide:pf_sdk_developers_guide
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/sdk_developers_guide/pf_sdk_developers_guide.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 4, 2023
section_ids:
  possible-customizations: Possible customizations
  adapter-and-sts-token-translator-interfaces: Adapter and STS token-translator interfaces
  authentication-selector-interfaces: Authentication selector interfaces
  custom-data-source-interfaces: Custom data source interfaces
  password-credential-validator-interfaces: Password credential validator interfaces
  identity-store-provisioner-interfaces: Identity store provisioner interfaces
  notification-publisher-interface: Notification publisher interface
  additional-documentation: Additional documentation
---

# SDK Developer's Guide

The PingFederate Software Development Kit (SDK) *(tooltip: \<div class="paragraph">
\<p>A set of tools that allows a developer to build a custom application that integrates with or connects to a platform or service.\</p>
\</div>)* enables integration with identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* and service provider (SP) *(tooltip: \<div class="paragraph">
\<p>In SAML, an entity that receives and accepts an authentication assertion issued by an IdP, typically for the purpose of allowing access to a protected resource.\</p>
\</div>)*. The SDK allows your application developers and system administrators to build custom implementations for communicating authentication and security information between PingFederate and your enterprise environment.

You can find details about the SDK interfaces and classes in the [PingFederate Server SDK](https://download.pingidentity.com/public/documentation/pingfederate/13.0/doc/index.html).

## Possible customizations

Extending PingFederate can include:

* Authentication adapters to integrate web applications or identity-management systems.

* Authentication selectors to direct single sign-on (SSO) *(tooltip: \<div class="paragraph">
  \<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
  \</div>)* authentication to instances of authentication adapters based on specified conditions.

* WS-Trust Security Token Service (STS) *(tooltip: \<div class="paragraph">
  \<p>An entity responsible for responding to WS-Trust requests for validation and issuance of security tokens used for SSO authentication to web services.\</p>
  \</div>)* token translators, including token processors and token generators.

* Custom data source drivers.

* Password credential validators.

* Identity store provisioners.

* Notification publishers.

The PingFederate Java SDK consists of several application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)*, including:

* Adapter and STS token-translator interfaces

* Authentication selector interfaces

* Custom data source interfaces

* Password credential validator interfaces

* Identity store provisioner interfaces

* Notification publisher interface

These interfaces allow you to create your own custom PingFederate plugins to suit your organization's needs. The SDK lets you develop, compile, and deploy custom plugins to PingFederate. The package also contains example plugins for reference. You can find these example plugin projects in the `<pf_install>/sdk/plugin-src` directory.

The PingFederate [Integration overview](../introduction_to_pingfederate/pf_integr_overview.html) describes the pre-built authentication adapters Ping Identity provides for integrating web applications and identity-management systems with PingFederate. Review this document before building your own adapter to see if an available adapter fits your use case.

|   |                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Custom components might not work the same way after upgrading PingFederate. When upgrading, thoroughly retest the behavior of customizations in a non-critical upgraded environment. |

## Adapter and STS token-translator interfaces

The adapter and token-translator APIs let PingFederate integrate with IdPs or SPs. Adapter token-translator APIs are configurable UI plugins that provide required runtime integration and let you render custom configuration windows.

|   |                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Suitable adapter or token-translator implementations for your deployment might already exist. Before developing your own custom solution, you can find available implementations on the [Ping Identity Downloads](https://www.pingidentity.com/en/resources/downloads.html) website. |

## Authentication selector interfaces

Authentication selectors let you choose from multiple authentication sources and direct users to a particular adapter or IdP connection. For example, an authentication selector can map internal corporate users to use one adapter and map external non-corporate users to a different adapter. Authentication selectors are configurable UI plugins that let you render custom configuration windows.

## Custom data source interfaces

The custom data source API is a set of Java interfaces that let PingFederate integrate with datastores not covered by existing Java database connectivity (JDBC) *(tooltip: \<div class="paragraph">
\<p>A Java API that allows Java programs to interact with databases.\</p>
\</div>)* or Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
\<p>An open, cross platform protocol used for interacting with directory services.\</p>
\</div>)* drivers. This lets you retrieve attributes from your choice of data source during attribute fulfillment. Custom data source interfaces are configurable UI plugins that let you render custom configuration windows.

## Password credential validator interfaces

The password credential validator interfaces let you define credential validators that verify a given username and password in various contexts throughout the system. For example, you can use credential validators to configure OAuth *(tooltip: \<div class="paragraph">
\<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
\</div>)* Resource Owner authorization grants and the HTML Form Adapter.

## Identity store provisioner interfaces

Identity store provisioners let you provision and deprovision users to external user stores. For example, you can configure a custom identity store provisioner within an inbound provisioning IdP connection to provision users using the System for Cross-domain Identity Management (SCIM) *(tooltip: \<div class="paragraph">
\<p>An application-level, HTTP-based protocol for provisioning and managing user identity information. SCIM supplies a common schema for representing users and groups and provides a REST API.\</p>
\</div>)* protocol. Identity store provisioners are configurable UI plugins that let you render custom configuration windows.

## Notification publisher interface

PingFederate delivers messages to administrators and end users based on notification publisher settings. You can implement custom notification publishers using the `NotificationPublisherPlugin` interface.

## Additional documentation

* Javadocs provide detailed reference information. You can find the Javadocs in the `<pf_install>/pingfederate/sdk/doc` directory.

* The user guides for Java, .NET, and PHP integration kits show examples of SDK implementations.

---

---
title: SDK directory structure
description: This topic describes the directory and build components that comprise the SDK.
component: pingfederate
version: 13.1
page_id: pingfederate:sdk_developers_guide:pf_sdk_direct_struct
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/sdk_developers_guide/pf_sdk_direct_struct.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
---

# SDK directory structure

This topic describes the directory and build components that comprise the SDK.

The PingFederate SDK directory (`<pf_install>/pingfederate/sdk`) contains the following:

* `plugin-src/` — The directory where you place your custom plugin projects. This directory also contains example plugin implementations showing a wide range of functionality. You can use these examples to develop your own implementations.

* `doc/` — Contains the SDK Javadocs. Open `index.html` to get started.

* `lib/` — Contains libraries used for compiling and deploying custom components into PingFederate.

* `build.properties` — Contains properties used by the Ant build script, `build.xml`, to compile and deploy your custom components. Do not modify this file. If you need to override a property, use `build.local.properties`.

* `build.local.properties` — Allows you to specify which project you want to build and define properties specific to your environment. Use this file to declare the project you want to build.

* `build.xml` — The Ant build script used to compile, build, and deploy your component. This file should not need modification.

The Java SDK, along with Apache Ant, enables you to create directories for your project and use the build script to build, clean, or deploy it. For more information, see [Developing your own plugin](pf_develop_your_plugin.html).

---

---
title: Session state management
description: Session state management for authentication API adapters is no different than for regular adapters. The same mechanisms, such as SessionStateSupport and TransactionalStateSupport, are used to store and retrieve session attributes on behalf of a user.
component: pingfederate
version: 13.1
page_id: pingfederate:sdk_developers_guide:pf_sess_state_manage
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/sdk_developers_guide/pf_sess_state_manage.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  related-links: Related links
---

# Session state management

Session state management for authentication API adapters is no different than for regular adapters. The same mechanisms, such as `SessionStateSupport` and `TransactionalStateSupport`, are used to store and retrieve session attributes on behalf of a user.

It should not be necessary to store more state attributes just to support the authentication API. The same session attributes should cover both API and non-API requests.

You can also wrap an API-capable adapter in a PingFederate-managed authentication session. PingFederate-managed authentication sessions mean that many adapters no longer need to provide their own internal session tracking.

## Related links

* [Developing authentication API-capable adapters and selectors](pf_develop_auth_api_capable_adapt_selec.html)

---

---
title: Shared plugin interfaces
description: Plugin implementations generally invoke methods categorized as either configurable or describable. This document describes these types of plugins and how they are used in PingFederate.
component: pingfederate
version: 13.1
page_id: pingfederate:sdk_developers_guide:pf_share_plugin_interface
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/sdk_developers_guide/pf_share_plugin_interface.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  configurable-plugin: Configurable plugin
  describable-plugin: Describable plugin
---

# Shared plugin interfaces

Plugin implementations generally invoke methods categorized as either configurable or describable. This document describes these types of plugins and how they are used in PingFederate.

## Configurable plugin

Any custom plugin that requires UI settings is configurable and implements the `ConfigurablePlugin` interface. This ensures that PingFederate loads the plugin instance with the correct configuration settings.

All plugin types implement the `ConfigurablePlugin` interface and must define the following within the `ConfigurablePlugin` interface to enable configuration loading.

```
void configure(Configuration configuration)
```

During processing of a configurable plugin instance, PingFederate calls the `ConfigurablePlugin.configure()` method and passes a `Configuration` object. The `Configuration` object provides the plugin adapter instance configuration set by an administrator in the PingFederate UI.

The `SpAuthnAdapterExample.java` sample provided with the SDK shows how to use this method to initialize an adapter instance from a saved configuration. After your implementation loads the configuration values, the plugin instance can use them in other method calls.

## Describable plugin

Any plugin that requires configuration windows in the PingFederate administrative console is a describable plugin. Most plugins implement the `DescribablePlugin` interface to ensure that PingFederate renders the correct UI components based on the returned `PluginDescriptor`.

Adapter and custom data source plugins are special cases and do not implement the `DescribablePlugin` interface. However, they still return a plugin descriptor (`AuthnAdapterDescriptor` and `SourceDescriptor`) and are still describable plugins.

All describable plugins must define a UI descriptor. Use one of the following methods to implement a UI descriptor, depending on the type of plugin:

* For plugins using the `DescribablePlugin` interface

  ```
  PluginDescriptor getPluginDescriptor()
  ```

* For adapter plugins

  ```
  AuthnAdapterDescriptor getAdapterDescriptor()
  ```

* For custom data source plugins

  ```
  SourceDescriptor getSourceDescriptor()
  ```

Describable plugins can return a subclass of `PluginDescriptor`, so the return type might differ between plugin implementations. Your plugin implementation populates `PluginDescriptor` with `FieldDescriptors`, `FieldValidators`, and `Actions` and is presented as a set of UI components in the PingFederate administrative console.

|   |                                                                                                                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Some plugin types offer concrete descriptor implementations for developers. The Javadocs and examples provided with the SDK show which descriptor classes are available for each plugin type. The examples also show you how to use `FieldDescriptors`, `FieldValidators`, and `Actions` to define your plugin descriptor. |

---

---
title: Specification of the plugin API
description: The first step in adding API support to your plugin is to implement the AuthnApiPlugin interface.
component: pingfederate
version: 13.1
page_id: pingfederate:sdk_developers_guide:pf_specification_plugin_api
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/sdk_developers_guide/pf_specification_plugin_api.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  related-links: Related links
  state-model-example: State model example
  action-model-example: Action model example
  authnstatespec-and-authnactionspec-objects: AuthnStateSpec and AuthnActionSpec objects
  error-specifications: Error specifications
---

# Specification of the plugin API

The first step in adding API support to your plugin is to implement the `AuthnApiPlugin` interface.

The AuthnApiPlugin interface has two methods: `getApiSpec()` and `getApiPluginDescriptor()`. You only need to implement the `getApiSpec()` method. The API specification this method returns defines the states, models, and actions that your plugin exposes in the API.

The API specification is defined by the `*Spec` classes in the SDK. These include `AuthnStateSpec`, `AuthnActionSpec`, `AuthnErrorSpec`, and `AuthnErrorDetailSpec`. The information in these classes lets the PingFederate authentication API Explorer provide documentation for API client developers. That documentation describes your plugin's API and lets developers experiment with it.

You can access the API Explorer at https\://*PingFederate\_host*:9031/pf-ws/authn/explorer. To enable the API Explorer, go to the **Authentication API Applications** window and select the **Enable API Explorer** checkbox. An easy way to use the API Explorer is to create an authentication API application in PingFederate and set the URL for the application to the API Explorer's URL.

|   |                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When defining models for states and actions, use the @Schema annotation to describe each field in the model and show whether the field is required. |

The rest of this document primarily uses the `TemplateRenderAdapter` as an example. The source for this adapter is in the PingFederate installation package's `sdk/plugin-src/template-render-adapter-example` directory. This adapter is simple. It just prompts the user to enter their username and provide a set of string attributes. The administrator defines the list of attributes by extending the adapter contract. The attribute values are passed back in the `SubmitUserAttributes` model as a map. Representing field values using a map in the model is unusual. Usually a separate field in the model defines each allowed field, which provides better type safety in the code.

## Related links

* [Developing authentication API-capable adapters and selectors](pf_develop_auth_api_capable_adapt_selec.html)

## State model example

The following is an example of a state model used by the `TemplateRenderAdapter`.

```
/
 * This is the model for the USER_ATTRIBUTES_REQUIRED state. It defines the
 * fields that are returned to the API client in a GET response for this state.
 /
public class UserAttributesRequired
{
	private List<String> attributeNames = new ArrayList<>();

	/
	 * Get the list of user attributes supported by this adapter instance.
	 *
	 * It is recommended to annotate each getter with the @Schema annotation
	 * and provide a description. This description will be used in
	 * generating API documentation.
	 */
	@Schema(description="A list of user attribute names that are supported by this adapter instance.")
	public List<String> getAttributeNames()
	{
		return attributeNames;
	}

	/*
	 * Set the list of user attributes supported by this adapter instance.
	 */
	public void setAttributeNames(List<String> attributeNames)
	{
		this.attributeNames = attributeNames;
	}
}
```

## Action model example

The following is the model for the `submitUserAttributes` action.

```
/
 * This is the model for the submitUserAttributes API action. It defines the
 * fields that may be included in the POST body for this action.
 /
public class SubmitUserAttributes
{
	private String username;
	private Map<String,Object> userAttributes = new HashMap<>();

	/
	 * Get the username.
	 *
	 * It is recommended to annotate each getter with the @Schema annotation
	 * and provide a description. The 'required' flag can also be specified. This
	 * information will be used in generating API documentation.
	 */
	@Schema(description="The user's username.", required=true)
	public String getUsername()
	{
		return username;
	}

	/
	 * Set the username.
	 */
	public void setUsername(String username)
	{
		this.username = username;
	}

	/
	 * Get the user attributes.
	 */
	@Schema(description="Additional user attributes, as name-value pairs.")
	public Map<String, Object> getUserAttributes()
	{
		return userAttributes;
	}

	/*
	 * Set the user attributes.
	 */
	public void setUserAttributes(Map<String, Object> userAttributes)
	{
		this.userAttributes = userAttributes;
	}
}
```

## AuthnStateSpec and AuthnActionSpec objects

A fluent builder is provided for creating `AuthnStateSpec` and `AuthnActionSpec` objects.

Here is the definition of the `AuthnStateSpec` for the `USER_ATTRIBUTES_REQUIRED` state:

```
public final static AuthnStateSpec<UserAttributesRequired> USER_ATTRIBUTES_REQUIRED = new AuthnStateSpec.Builder<UserAttributesRequired>()
	.status("USER_ATTRIBUTES_REQUIRED")
	.description("The user's username and attributes are required.")
	.modelClass(UserAttributesRequired.class)
	.action(ActionSpec.SUBMIT_USER_ATTRIBUTES)
	.action(CommonActionSpec.CANCEL_AUTHENTICATION)
	.build();
```

Here is the specification for the `submitUserAttributes` action:

```
public final static AuthnActionSpec<SubmitUserAttributes> SUBMIT_USER_ATTRIBUTES = new AuthnActionSpec.Builder<SubmitUserAttributes>()
	.id("submitUserAttributes")
	.description("Submit the user's username and attributes.")
	.modelClass(SubmitUserAttributes.class)
	.error(CommonErrorSpec.VALIDATION_ERROR)
	.errorDetail(ErrorDetailSpec.INVALID_ATTRIBUTE_NAME)
	.build();
```

## Error specifications

Action specifications can include a list of possible errors and error details. Each top-level error that an authentication API request returns can include one or more error detail objects underneath it.

Typically, in the API specification, your only top-level error will be `CommonErrorSpec.VALIDATION_ERROR`. However, you can include error detail specifications that can appear under that top-level error.

The following is how the `TemplateRenderAdapter` defines the specification for the `INVALID_ATTRIBUTE_NAME` error detail.

```
public final static AuthnErrorDetailSpec INVALID_ATTRIBUTE_NAME = new AuthnErrorDetailSpec.Builder()
	.code("INVALID_ATTRIBUTE_NAME")
	.message("An invalid attribute name was provided.")
	.parentCode(CommonErrorSpec.VALIDATION_ERROR.getCode())
	.build();
```

|   |                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The error detail specification must reference the error code of its parent top-level error. This ensures that the authentication API Explorer correctly represents the error information. |

`INVALID_ATTRIBUTE_NAME` is an example of an error that would be useful for API client developers but not for end users.

For more information about defining user-facing errors, see [\[pf\_error\_messages\_localization\]](#pf_error_messages_localization).

---

---
title: State model contents
description: The model for a state includes all the information an API client would need to build a form (not necessarily an HTML form) to show the user. A state model should not include the text for messages to display to the user.
component: pingfederate
version: 13.1
page_id: pingfederate:sdk_developers_guide:pf_state_model_contents
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/sdk_developers_guide/pf_state_model_contents.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  related-links: Related links
---

# State model contents

The model for a state includes all the information an API client would need to build a form (not necessarily an HTML form) to show the user. A state model should not include the text for messages to display to the user.

Defining messages for users, and localizing them if needed, is the responsibility of the API client. One of the reasons we avoid including messages in state models is that those messages will often end up including semantic content that the API client needs to drive its code. Following the rule that models do not include messages helps ensure that our models include all the fields that an API client needs to provide the desired user experience.

Sometimes following this rule requires you to add more states. This is preferable to embedding the state information inside of a message because it makes it easier for an API client to handle that state in the desired way.

The one exception we have to this rule is around error messages. API errors include error message text, and in some cases, API clients will display the message text directly to users. This avoids every API client having to write its own messages for every user-facing error the API can generate. For more information, see [\[pf\_error\_messages\_localization\]](#pf_error_messages_localization).

## Related links

* [Developing authentication API-capable adapters and selectors](pf_develop_auth_api_capable_adapt_selec.html)