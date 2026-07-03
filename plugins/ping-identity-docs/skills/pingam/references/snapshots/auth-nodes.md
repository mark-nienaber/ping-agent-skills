---
title: Access an identity&#8217;s profile
description: "Access an identity's profile in PingAM authentication tree nodes to read and write permanent data storage beyond session or node state"
component: pingam
version: 8.1
page_id: pingam:auth-nodes:access-identity-profile
canonical_url: https://docs.pingidentity.com/pingam/8.1/auth-nodes/access-identity-profile.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Extensibility", "Nodes &amp; Trees"]
section_ids:
  read_an_identitys_profile: Read an identity's profile
  read_attributes_of_an_identitys_profile: Read attributes of an identity's profile
  write_a_value_into_an_identitys_profile: Write a value into an identity's profile
---

# Access an identity's profile

AM allows a node to read and write data to and from an identity's profile. This is useful if a node needs to store information more permanently than when using either the authentication trees' `NodeState` or the identity's session.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Any node that reads or writes to an identity's profile must only occur in a tree after the identity has been verified. For example, as the final step in a tree or directly after a [Data Store Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/data-store-decision.html).To store a verified identity in the journey session, call `ActionBuilder.withIdentifiedIdentity()`. This ensures identities with the same username are correctly resolved. |

## Read an identity's profile

Use the `IdUtils` static class:

```java
AMIdentity id = IdUtils.getIdentity(username, realm);
```

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | Use the [IdUtilsWrapper](../_attachments/apidocs/com/sun/identity/idm/IdUtilsWrapper.html) class to assist with testing. |

If AM is configured to search for the identity's profile using a different search attribute than the default, provide the attributes as a third argument to the method.

To obtain the attributes, you could request them in the configuration of the node or obtain them from the realm's authentication service configuration.

The following example demonstrates how to obtain the user alias:

```java
public AMIdentity getIdentityFromSearchAlias(String username, String realm) {
    ServiceConfigManager mgr = new ServiceConfigManager(
            ISAuthConstants.AUTH_SERVICE_NAME,
            AccessController.doPrivileged(AdminTokenAction.getInstance());

    ServiceConfig serviceConfig = mgr.getOrganizationConfig(realm, null);

    Set<String> realmAliasAttrs = serviceConfig.getAttributes()
        .get("iplanet-am-auth-alias-attr-name");

   return IdUtils.getIdentity(username, realm, realmAliasAttrs);
}
```

By combining these approaches, you can search for an identity by using the ID and whichever configured attribute field(s) as necessary.

## Read attributes of an identity's profile

After obtaining the profile, use the `AMIdentity.getAttribute(String name)` method.

## Write a value into an identity's profile

Create a `Map<String, Set<String>>` structure of the attributes you want to write, as follows:

```java
Map<String, Set<String>> attrs = new HashMap<>();
attrs.put("attribute", Collections.singleton("value"));
user.setAttributes(attrs);
user.store();
```

---

---
title: Action class
description: Understand the Action class that encapsulates changes to authentication tree state and flow control in PingAM authentication nodes
component: pingam
version: 8.1
page_id: pingam:auth-nodes:core-action
canonical_url: https://docs.pingidentity.com/pingam/8.1/auth-nodes/core-action.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Extensibility", "Nodes &amp; Trees", "Scripts"]
section_ids:
  action_fields_and_methods: Action fields and methods
---

# Action class

The `Node` class returns an `Action` instance from its `process()` method.

The `Action` class encapsulates changes to authentication tree state and flow control.

For example, the following implementation demonstrates an authentication level decision:

```java
@Override
public Action process(TreeContext context) throws NodeProcessException {
  NodeState state = context.getStateFor(this);
  if (!state.isDefined(authLevel)) {
    throw new NodeProcessException("Auth level is required");
  }
  JsonValue authLevel = state.get(authLevel);
  boolean authLevelSufficient =
    !authLevel.isNull()
    && authLevel.asInteger() >= config.authLevelRequirement();
  return goTo(authLevelSufficient).build();
}
```

Learn more in the [Action](../_attachments/apidocs/org/forgerock/openam/auth/node/api/Action.html) class.

## Action fields and methods

The `Action` class uses the following fields:

| Fields                             | Description                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `callbacks`                        | A list of the callbacks requested by the node. This list may be `null`.                                                                                                                                                                                                                                                                                                             |
| `errorMessage`                     | A custom error message string included in the response JSON if the authentication tree reaches the [Failure node](https://docs.pingidentity.com/auth-node-ref/8.1/failure.html).Each node in a tree can replace or update the error message string as the user traverses through the authentication tree.If required, your custom node or custom UI must localize the error string. |
| `identifiedIdentity`               | The identity that's confirmed to exist in an identity store.                                                                                                                                                                                                                                                                                                                        |
| `lockoutMessage`                   | A custom lockout message string included in the response JSON when the user is locked out.If required, your custom node or custom UI must localize the error string.                                                                                                                                                                                                                |
| `logoutHooks`                      | The list of logout hooks that run synchronously after logout.                                                                                                                                                                                                                                                                                                                       |
| `maxIdleTime`                      | The maximum idle time for the user.                                                                                                                                                                                                                                                                                                                                                 |
| `maxSessionTime`                   | The maximum session time for the user.                                                                                                                                                                                                                                                                                                                                              |
| `maxTreeDuration`                  | The maximum duration of the journey session.                                                                                                                                                                                                                                                                                                                                        |
| `outcome`                          | The result of the node.                                                                                                                                                                                                                                                                                                                                                             |
| `returnProperties`                 | A map of properties returned to the client.Use the `withHeader`, `withStage`, and `withDescription` methods to add a property to the map.                                                                                                                                                                                                                                           |
| `sessionHooks`                     | The list of classes implementing the TreeHook interface that run after a successful login.                                                                                                                                                                                                                                                                                          |
| `sessionProperties`                | A map of properties added to the final session if the authentication tree completes successfully.Use `putSessionProperty(String key, String value)` and `removeSessionProperty(String key)` to add or remove entries from the map.                                                                                                                                                  |
| `sharedState` and `transientState` | *Deprecated*.Use the `NodeState` object instead. Learn more in [Store values in a tree's node states](store-values-shared-state.html#store-values-in-transient-state).                                                                                                                                                                                                              |
| `suspendDuration`                  | The length of time a journey session is suspended.                                                                                                                                                                                                                                                                                                                                  |
| `webhooks`                         | The list of webhooks that run after logout.Use the `addWebhook` and `addWebhooks` methods to populate this list.                                                                                                                                                                                                                                                                    |

The `Action` class provides the following static methods to create an `ActionBuilder`:

| Methods            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `goTo`             | Specify the exit path to take, and move on to the next node in the tree.For example:```java
return goTo(false).build();
```                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `send`             | Send the specified callbacks to the user for them to interact with.For example, the [Username Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/am-only/username-collector.html) uses the following code to send the `NameCallback` callback to the user to request the `USERNAME` value:```java
return send(new NameCallback(bundle.getString("callback.username"))).build();
```                                                                                                                                                                              |
| `sendingCallbacks` | Returns true if the action is a request for input from the user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `suspend`          | Suspends the authentication tree and lets the user resume it from the point it was suspended. You can also control how long it is suspended for.For example, the following call is taken from the [Email Suspend node](https://docs.pingidentity.com/auth-node-ref/8.1/email-suspend.html):```java
return suspend(resumeURI -> createSuspendOutcome(context, resumeURI, recipient, templateObject)).build();
```Use the [SuspensionHandler](../_attachments/apidocs/org/forgerock/openam/auth/node/api/SuspensionHandler.html) interface for handling the suspension request. |

The inner class `ActionBuilder` provides the following methods for constructing the `Action` object and setting action-related properties:

| Methods                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `addNodeType`                                    | Add a node type to the session properties and shared state. Replace any existing shared state with the specified TreeContext's shared state.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `addSessionHook` and `addSessionHooks`           | Add one or more session hook classes for AM to run after a successful login.Learn more in [Register an authentication tree hook](../am-authentication/post-authn-plugins-treehook.html#register-tree-hook).                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `addWebhook` and `addWebhooks`                   | Add one or more webhook names to the list of webhooks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `build`                                          | Creates and returns an Action instance providing the mandatory fields are set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `putSessionProperty`                             | Add a new session property.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `registerLogoutHook`                             | Register a logout hook.Learn more in [Register a logout hook](../am-authentication/create-logout-hook.html#register-logout-hook).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `removeSessionProperty`                          | Remove the specified session property.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `replaceSharedState` and `replaceTransientState` | *Deprecated*.Use the `NodeState` object instead. Learn more in [Store values in a tree's node states](store-values-shared-state.html#store-values-in-transient-state).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `withDescription`                                | Set a description for this action.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `withErrorMessage`                               | Set a custom message for when the authentication tree reaches the failure node.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `withHeader`                                     | Set a header for this action.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `withIdentifiedIdentity`                         | Add an identity, authenticated or not, that's confirmed to exist in an identity store. Specify the username and identity type or an `AMIdentity` object.Use this method to record the type of identified user. If the advanced server property, `org.forgerock.am.auth.trees.authenticate.identified.identity` is set to true, AM uses the stored identified identities to decide which user to log in.This lets the authentication tree engine correctly resolve identities that have the same username.Learn more in [advanced server properties](../setup/deployment-configuration-reference.html#org.forgerock.am.auth.trees.authenticate.identified.identity). |
| `withLockoutMessage`                             | Set a custom message for when the user is locked out.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `withMaxIdleTime`                                | Set the maximum idle time for the authenticated session in minutes.This overrides the [maximum idle time](../am-sessions/session-state-session-termination.html#auth-session-termination-config) set in the journey or the Session service.	If a user has session timeouts set, the user-specific settings are always used.                                                                                                                                                                                                                                                                                                                                         |
| `withMaxSessionTime`                             | Set the maximum authenticated session time in minutes.This overrides the [maximum authenticated session time](../am-sessions/session-state-session-termination.html#auth-session-termination-config) set in the journey or the Session service.	If a user has session timeouts set, the user-specific settings are always used.                                                                                                                                                                                                                                                                                                                                     |
| `withMaxTreeDuration`                            | Set the maximum duration of a journey session in minutes.This overrides the [maximum duration](../am-authentication/suspended-auth.html#maximum-duration) set in the journey or authentication settings.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `withStage`                                      | Set a stage name to return to the client to aid the rendering of the UI. The property is only sent if the node also sends callbacks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `withUniversalId`                                | *Deprecated*.Use `withIdentifiedIdentity` instead.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

Learn more about the supported methods in [ActionBuilder](../_attachments/apidocs/org/forgerock/openam/auth/node/api/Action.ActionBuilder.html).

---

---
title: Authentication nodes
description: Understand how authentication nodes and trees provide fine-grained authentication with multiple paths and decision points throughout the authentication flow
component: pingam
version: 8.1
page_id: pingam:auth-nodes:about-nodes
canonical_url: https://docs.pingidentity.com/pingam/8.1/auth-nodes/about-nodes.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Extensibility", "Nodes &amp; Trees"]
section_ids:
  types-of-nodes: Node types
  collector_nodes: Collector nodes
  decision_nodes: Decision nodes
  splitting-nodes: Restrict a node's functionality
---

# Authentication nodes

Authentication trees provide fine-grained authentication by allowing multiple paths and decision points throughout the authentication flow.

Authentication trees are made up of authentication nodes that define actions taken during authentication. Each node performs a single task during authentication, such as collecting a username or making a simple decision. Nodes can have multiple outcomes rather than just success or failure.

You can create complex yet customer-friendly authentication experiences by linking nodes together, creating loops, and nesting nodes within a tree, as follows:

![Create multiple paths for authentication by linking nodes within trees.](_images/trees-ui-example.png)Figure 1. Example authentication tree

## Node types

Nodes are designed to have a single responsibility. Where appropriate, they should be loosely coupled with other nodes, enabling reuse in multiple situations.

For example, if a newly written node requires a username value, it should not collect it itself, but rely on another node, namely the [Username Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/am-only/username-collector.html).

There are two broad node types: collector nodes and decision nodes.

### Collector nodes

Collector nodes capture data from a user during the authentication process. This data is often captured by a *callback* that is rendered in the UI as a text field, drop-down list, or other form component.

Examples of collector nodes include the [Username Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/am-only/username-collector.html) and [Password Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/am-only/password-collector.html).

![The output from a username collector node.](_images/username-collector.png)

Collector nodes can perform basic processing of the collected data, before making it available to subsequent nodes in the authentication tree.

The [Choice Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/choice-collector.html) provides a drop-down list, populated with options defined when the tree is created, or edited.

![The output from a choice collector node.](_images/choice-collector.png)

Not all collector nodes use callbacks. For example, the [Zero Page Login Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/zero-page-login-collector.html) retrieves a username and password value from the request headers, if present.

### Decision nodes

Decision nodes do the following:

* Retrieve the state produced by one or more nodes.

* Perform some processing on that state.

* Optionally, store some derived information in the shared state.

* Provide one or more outcomes, depending on the result.

The simplest decision node returns a boolean outcome - `true`, or `false`.

Complex nodes may have additional outcomes. For example, the [LDAP Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/ldap-decision.html) provides the additional outcomes *Locked*, *Expired*, and *Cancelled*. The tree administrator decides what to do with each outcome; for example, the `True` outcome is often routed to a *Success* node, or to additional nodes for further authentication.

In the following example tree, two collector nodes are connected before a [Data Store Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/data-store-decision.html). The node then uses the credentials to authenticate the user against the identity stores configured for the realm. In this instance, an unsuccessful login attempt leads directly to failure; the user must restart the process from scratch.

![A tree containing a data store decision node.](_images/data-store-decision.png)

A more user-friendly approach might route unsuccessful attempts to a [Retry Limit Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/retry-limit-decision.html). In the following example, unsuccessful authentication attempts at the [Data Store Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/data-store-decision.html) stage are routed into a [Retry Limit Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/retry-limit-decision.html). Depending on how many retries have been configured, the node either retries or rejects the new login attempt. Rejected attempts lead to a locked account.

![A tree containing a data store decision node, with multiple retries and account lockout.](_images/data-store-decision-with-retry.png)

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Nodes can have prerequisite stagesSome Decision nodes are only applicable when used in conjunction with other nodes. For example, the [Persistent Cookie Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/persistent-cookie-decision.html) looks for a persistent cookie that has been set in the request, typically by the [Set Persistent Cookie node](https://docs.pingidentity.com/auth-node-ref/8.1/set-persistent-cookie.html). The [OTP Collector Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/otp-collector-decision.html), which is both a collector and a decision node, only works when used in conjunction with a one-time password generated by a [HOTP Generator node](https://docs.pingidentity.com/auth-node-ref/8.1/hotp-generator.html). |

## Restrict a node's functionality

To determine the functionality of a node, reduce the node's responsibility to its core purpose. For example, the [Password Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/am-only/password-collector.html) just captures the user's password.

Before you create a set of nodes, assess the level of granularity the nodes should produce. For example, a customer's environment may require a series of utility nodes that, on their own, don't perform authentication actions, but have multiple use cases in many authentication journeys. In this case, you can create nodes that take values from the shared state and save it to the user's profile.

Individual nodes can respond to a variety of inputs and outputs, and return different sets of callbacks to the user without leaving the node.

The following guidelines help a node developer determine the best point at which to split a node into multiple instances:

* If a node's process method takes input from the user, and immediately processes it:

  Consider splitting the functionality over two nodes:

  * A collector node returns callbacks to the user and stores the response in the shared state.

  * A decision node uses the inputs collected so far in the tree to determine the next course of action.

  A node that takes input from the user and makes a decision should only be designed as a single node if there is no possible additional use for the data gathered, other than making that specific decision.

* If a processing stage in a node is duplicated in other nodes:

  In this case, take the repeating stage out and place it in its own node. Connect this node appropriately to each of the other nodes.

  If multiple nodes contain the same step in processing, such as returning a set of callbacks to ask the user for a set of data before processing it in different ways, the common functionality should be pulled out into its own node.

* If a single function within the node has obvious use cases in other authentication journeys:

  In this case, the functionality should be written into a single, reusable node. For example, in multi-factor authentication, a mechanism for reporting a lost device is applicable to many node types, such as mobile push, OATH, and others.

---

---
title: Build and install Java nodes
description: Build and install custom Java authentication nodes for use in PingAM authentication trees
component: pingam
version: 8.1
page_id: pingam:auth-nodes:build-install-nodes
canonical_url: https://docs.pingidentity.com/pingam/8.1/auth-nodes/build-install-nodes.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "Extensibility", "Customization", "Nodes &amp; Trees"]
section_ids:
  proc-build-install-custom-node: Build and install a custom Java node
---

# Build and install Java nodes

This section explains how to build and install Java nodes for use in authentication trees.

## Build and install a custom Java node

1. Change to the root directory of the Maven project of the custom nodes.

   For example:

   ```bash
   $ cd /Users/Ping/Repositories/am-external/openam-auth-trees/auth-nodes
   ```

2. Run the `mvn clean package` command.

   The project will generate a `.jar` file containing your custom nodes. For example, `auth-nodes-version.jar`.

3. Include the custom `.jar` file in the AM `.war` file, as described in [Customize the AM `.war` file](../installation/customize-openam.html).

   |   |                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------- |
   |   | Delete or overwrite older versions of the nodes `.jar` file from the `WEB-INF/lib/` folder, to avoid clashes. |

   |   |                                                                                                                                                                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you are using custom nodes with version `0.0.0` in trees, you must remove them from the trees before restarting AM and reinsert them after the restart. If you do not do this, the entire tree cannot be viewed in the UI after the restart. |

4. Restart AM for the new nodes to become available.

   The custom authentication node is now available in the tree designer to add to authentication trees:

   ![Custom nodes appear alongside built-in authentication nodes in the Administration console.](_images/auth-node-custom-installed.png)Figure 1. Custom node in a tree

   Learn more about using the tree designer to manage authentication trees in [Create a tree in the UI](../am-authentication/create-auth-trees.html#create-authn-tree-ui).

For information on upgrading custom nodes, refer to [Upgrade nodes and change node configuration](node-upgrade.html).

---

---
title: Changelog
description: Document changelog entries in custom authentication node `.properties` files to track version changes and retrieve them via the versionInfo endpoint
component: pingam
version: 8.1
page_id: pingam:auth-nodes:changelog
canonical_url: https://docs.pingidentity.com/pingam/8.1/auth-nodes/changelog.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Extensibility", "Nodes &amp; Trees", "Scripts"]
---

# Changelog

Add a changelog to the node's `.properties` file for each node version to provide a record of changes for a node.

1. Make sure there's a `.properties` file under `src/main/resources/org.forgerock.openam.auth.nodes` with the same name as your node class.

2. At the end of the `.properties` file, add a changelog property in the following format:

   ```none
   changelog.n.n=changelog text
   ```

   For example:

   ```properties
   changelog.2.0=Updated the node to replace the secretValue attribute with secretLabelIdentifier.
   ```

To retrieve all the changelogs for a node, send a `POST` request to the `realm-config/authentication/authenticationtrees/nodes/node-name?_action=versionInfo` endpoint.

Example response:

```json
[
  {
    "version": "1.0",
    "changelog": "No changelog entry found"
  },
  {
    "version": "2.0",
    "changelog": "Updated the node to replace the secretValue attribute with secretLabelIdentifier."
  }
]
```

Include the node version in the request URL to return the changelog only for the specified node version.

---

---
title: Config interface
description: Define node configuration properties using the Config interface in custom PingAM authentication nodes
component: pingam
version: 8.1
page_id: pingam:auth-nodes:core-config
canonical_url: https://docs.pingidentity.com/pingam/8.1/auth-nodes/core-config.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Extensibility", "Nodes &amp; Trees", "Scripts"]
section_ids:
  define_node_properties: Define node properties
  attribute_annotation: Attribute annotation
---

# Config interface

The `Config` interface defines the configuration data for a node. A node can't have state, but it can have configuration data. Configuration is per node. Different nodes of the same type in the same tree have their own configuration.

You don't need to write a class that implements the interface you define. AM automatically creates this as required.

## Define node properties

Configure the node properties using *methods*. To provide a default value to the tree administrator, mark the method as `default` and define both a method and a value. To omit a default value, define the method's signature but not the implementation.

For example:

```java
public interface Config {

  //This will have no default value for the UI
  @Attribute(order = 10)
  String noDefaultAttribute();

  //This will default to the value LOCK.
  @Attribute(order = 20)
  default LockStatus lockAction() {
    return LockStatus.LOCK;
  }
}
```

For this `Config` example, a custom enum named `LockStatus` is returned.

The defined properties appear as configurable options in the tree designer view when adding a node of the relevant type. The options display to the user automatically.

Attribute names are used when localizing the node's text. Learn more in [Internationalize nodes](i18n-nodes.html).

![The output from an example Config interface](_images/config-interface-in-ui.png)

You can find more information in the [Config](../_attachments/apidocs/org/forgerock/openam/annotations/sm/Config.html) annotation type in the *AM Public API Javadoc*.

## Attribute annotation

The `Attribute` annotation is required. It defines the properties that appear as configurable options when you add or update a node.

Consider the following when using the `Attribute` annotation:

* You must specify an integer value for `order` to determine the position of the attribute in the UI.

* Only use compatible Java types as attributes.

  > **Collapse: Compatible Java types**
  >
  > | Java type                                      | Additional information                                                                                                                                               |
  > | ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  > | `java.lang.String`                             |                                                                                                                                                                      |
  > | `java.lang.Integer`                            |                                                                                                                                                                      |
  > | `java.lang.Long`                               |                                                                                                                                                                      |
  > | `java.lang.Boolean`                            |                                                                                                                                                                      |
  > | `java.lang.Enum`                               | Use any enum type.                                                                                                                                                   |
  > | `org.forgerock.json.JsonValue`                 |                                                                                                                                                                      |
  > | `java.util.Locale`                             |                                                                                                                                                                      |
  > | `java.net.URL`                                 |                                                                                                                                                                      |
  > | `char[]` (char array)                          | Use for passwords, but consider using `org.forgerock.secrets.Purpose` instead.                                                                                       |
  > | `java.util.List``java.util.Set``java.util.Map` | Use with the following elements:- Boolean
  >
  > - Duration
  >
  > - Integer
  >
  > - Locale
  >
  > - Long
  >
  > - String
  >
  > - URL
  >
  > - JsonValue
  >
  > - char\[]Keys must be strings for `java.util.Map`. |
  > | `java.util.Optional`                           | Use with any of these compatible Java types.                                                                                                                         |
  > | `org.forgerock.secrets.Purpose`                | Use for secret values such as passwords.You must annotate this type with `@SecretPurpose` to define the secret label.                                                |

* Include `requiredValue = true` if the attribute is a required value.

  Any attributes that aren't required should be an Optional attribute unless they're already part of a collection through `List`, `Map`, or `Set`.

  Attributes aren't required by default when either `requiredValue` is omitted or set to `false`.

* Specify one or more `validators` if you need to validate the attribute values provided.

  Create any validator classes that you require by implementing the [ServiceAttributeValidator](../_attachments/apidocs/com/sun/identity/sm/ServiceAttributeValidator.html) interface.

  > **Collapse: Example**
  >
  > The following example creates a validator called `GreaterThanZeroValidator`:
  >
  > ```java
  > public class GreaterThanZeroValidator implements ServiceAttributeValidator {
  >
  >     @Override
  >     public boolean validate(Set<String> values) {
  >         boolean isValid = true;
  >         for (String value : values) {
  >             if (Integer.parseInt(value) <= 0) {
  >                 isValid = false;
  >                 break;
  >             }
  >         }
  >         return isValid;
  >     }
  > }
  > ```

For example:

```java
public interface Config {
  @Attribute(order = 1)
  String domain();                                                       1

  @Attribute(order = 2, validators = {GreaterThanZeroValidator.class})   2

  int exampleNumber();

  @Attribute(order = 3, requiredValue = true)
  boolean isVerificationRequired();                                      3

  @Attribute(order = 4)
  @TextArea                                                              4
  String textBox();

  @Attribute(order = 5)
  @Password                                                              5
  char[] clientSecret();

  @Attribute(order = 6)
  default YourCustomEnum action() {
    return YourCustomEnum.LockScreen;                                    6

  @Attribute(order = 7, requiredValue = true, resourceName = "secretLabelIdentifier")
  @SecretPurpose("am.authentication.nodes.customauth.%s.secret")
  Purpose<GenericSecret> secretValuePurpose();                           7
  };
}
```

1 The `domain` attribute defines a String-type node property for display in the UI. Access the attribute in the `process` method by using a reference to the `config` interface. For example, `config.domain()`.

2 Specify one or more validator classes as the `validators` parameter.

3 The boolean attribute is defined as a required value.

4 Use the [TextArea](../_attachments/apidocs/org/forgerock/openam/sm/annotations/adapters/TextArea.html) annotation to indicate a String-type node property that needs a larger text input than a single line.

5 Use the [Password](../_attachments/apidocs/org/forgerock/openam/sm/annotations/adapters/Password.html) annotation to mask the input characters and encrypt the value of the attribute.

6 A custom enum attribute. This provides type safety and negates the misuse of Strings as generic type-unsafe value holders. The UI will correctly handle the enum and only let the tree administrator choose from the defined enum values.

Learn more in the [Attribute](../_attachments/apidocs/org/forgerock/openam/annotations/sm/Attribute.html) annotation type in the *AM Public API Javadoc*.

7 An identifier used to create a secret label for the node that maps to a secret in a secret store. The default custom authentication node secret label is `am.authentication.nodes.customauth.%s.secret` where `%s` is the value of the identifier. The identifier can only contain alphanumeric characters `a-z`, `A-Z`, `0-9`, and periods (`.`). It can't start or end with a period.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To retrieve the secret using the identifier from your custom node, use the [Secrets](../_attachments/apidocs/org/forgerock/openam/secrets/Secrets.html) class, for example:```java
var validSecrets = secrets.getRealmSecrets(realm)
        .getValidSecrets(config.secretValuePurpose())
        .getOrThrowIfInterrupted()
        .map(s → s.revealAsUtf8(String::new))
        .collect(Collectors.toList());
```Learn more in:- The [SecretPurpose](../_attachments/apidocs/org/forgerock/openam/sm/annotations/adapters/SecretPurpose.html) annotation

- The [org.forgerock.secrets](../_attachments/apidocs/org/forgerock/secrets/package-summary.html) package

- [Map and rotate secrets](../security/secret-mapping.html) |

---

---
title: Create versioned nodes
description: Create a new version of an authentication node to safely test configuration changes before deploying to existing authentication flows
component: pingam
version: 8.1
page_id: pingam:auth-nodes:create-versioned-nodes
canonical_url: https://docs.pingidentity.com/pingam/8.1/auth-nodes/create-versioned-nodes.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Extensibility", "Nodes &amp; Trees", "Scripts"]
---

# Create versioned nodes

When you want to make changes to an existing node, it's best practice to create a new version of the node. This gives you greater control over how and when the changes are deployed to existing authentication flows. For example, you could test the changes on a subset of users first, before rolling them out more widely.

|   |                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To ensure consistency, decide on a naming convention for versioned nodes before you start. For example, append V*n* to node class names where *n* is the version.For example, MyNodeV2 is version 2 of a node whose class name is `MyNode`. |

To create a new versioned node:

1. Create a Java class for your new versioned node that implements the `Node` interface. Find more information in [Node class](core-class.html).

   Depending on the scale of changes, you could start with a copy of the existing class.

2. Name the class according to your naming conventions.

3. Add the [VersionMetadata annotation](versionmetadata.html) to specify the name or class name of the original node, the version of the new node, and optionally, the `upgrader` class name.

4. If you specify an `upgrader` class name, add the following:

   * The [NodeVersionUpgrader.UpgraderMetadata annotation](nodeversionupgrader.html) to specify the version of the new node and the name of the previous upgrader class.

     If an `upgrader` class name has been specified but the `NodeVersionUpgrader.UpgraderMetadata` annotation is missing, the new node won't install.

   * The [Upgrader class](upgrader-class.html) to define the upgrade logic to update the node's configuration from one version to another.

5. Add a [Changelog](changelog.html) to the node's `.properties` file to detail the changes introduced in the new version. This step is optional, but it's helpful to keep a record of changes for a node.

---

---
title: Custom Java nodes
description: Develop and maintain custom Java authentication nodes in PingAM, including security best practices, internationalization, and installation guidance
component: pingam
version: 8.1
page_id: pingam:auth-nodes:preface
canonical_url: https://docs.pingidentity.com/pingam/8.1/auth-nodes/preface.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Extensibility", "Integration", "Nodes &amp; Trees"]
page_aliases: ["index.adoc"]
---

# Custom Java nodes

These topics provide guidance and best practices for developing and maintaining Java authentication nodes in AM.

|   |                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------- |
|   | To create your own custom scripted nodes, use the [Node Designer](../am-authentication/node-designer.html). |

[icon: sitemap, set=fad, size=3x]

#### [About authentication nodes](about-nodes.html)

Learn how nodes define actions taken during authentication.

[icon: check-square, set=fad, size=3x]

#### [Prepare your environment](preparing-for-nodes.html)

Discover the prerequisites for building and customizing Java authentication nodes.

[icon: bomb, set=fad, size=3x]

#### [Secure nodes](secure-nodes.html)

Learn about security best practices when developing authentication nodes.

[icon: cogs, set=fad, size=3x]

#### [Develop nodes](develop-maintain-nodes.html)

Learn how to develop and maintain authentication nodes.

[icon: language, set=fad, size=3x]

#### [Translate nodes](i18n-nodes.html)

Internationalize the text in your nodes.

[icon: wrench, set=fad, size=3x]

#### [Build and install nodes](build-install-nodes.html)

Find out how to build and install authentication nodes for use in authentication trees.

You can find information on configuring and using authentication trees in [Trees](../am-authentication/auth-trees.html).

---

---
title: Develop and maintain nodes
description: Develop custom authentication nodes for PingAM by implementing the Node interface, managing versions, storing state, accessing identity profiles, and creating plugin classes
component: pingam
version: 8.1
page_id: pingam:auth-nodes:develop-maintain-nodes
canonical_url: https://docs.pingidentity.com/pingam/8.1/auth-nodes/develop-maintain-nodes.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Extensibility", "Nodes &amp; Trees"]
---

# Develop and maintain nodes

The following table describes the tasks involved in developing and maintaining custom nodes:

| Task                                                                                                                                                                                                                 | Resources                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Create a Java class that implements the `Node` interfaceThis class is your custom authentication node. It should define all aspects of your node, such as configuration data, version, outcomes, and business logic. | [Node class](core-class.html)                                          |
| Create versioned nodesCreate new versions of a node and define the upgrade logic to transform the node's configuration from one version to another.                                                                  | [Create versioned nodes](create-versioned-nodes.html)                  |
| Store values in shared tree stateUse the tree state to store values for use by downstream nodes.                                                                                                                     | [Store values in shared tree state](store-values-shared-state.html)    |
| Access an identity's profileRead or write data to and from an identity's profile. The identity must be verified before it can be accessed.                                                                           | [Access an identity's profile](access-identity-profile.html)           |
| Include callbacksUse existing callbacks to interact with the authenticating user.                                                                                                                                    | [Include callbacks](include-callbacks.html)                            |
| Handle multiple visits to a nodeAllow the authentication flow to return to the same node if needed.                                                                                                                  | [Handle multiple visits to the same node](handle-multiple-visits.html) |
| Create a plugin class that implements the `AmPlugin` interfaceThe plugin class provides details about your node to AM.                                                                                               | [Plugin class](plugin-class.html)                                      |

---

---
title: Handle errors
description: Handle errors in authentication nodes, including reporting messages to users and administrators, and managing unrecoverable errors
component: pingam
version: 8.1
page_id: pingam:auth-nodes:core-error-handling
canonical_url: https://docs.pingidentity.com/pingam/8.1/auth-nodes/core-error-handling.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Extensibility", "Nodes &amp; Trees", "Scripts"]
section_ids:
  authentication_errors: Authentication errors
  unrecoverable_errors: Unrecoverable errors
  configuration_errors: Configuration errors
---

# Handle errors

This page covers error handling in authentication nodes, including how to report errors to end users and tree administrators, as well as handling unrecoverable errors.

Authentication trees provide a number of ways to output error messages to the user.

## Authentication errors

The most common error to display is a message in the event of an unsuccessful authentication. In an authentication tree, this occurs when the authentication process terminates at the failure node:

![Error message shown by a tree that terminated at the failure node.](_images/auth-tree-failure.png)

## Unrecoverable errors

By default, when a catastrophic error occurs during node processing, a `NodeProcessException` exception should be thrown, which halts the authentication journey immediately, and displays a generic error message. This may not be desirable, as it could create a negative user experience.

Instead, errors that occur during node processing should be caught within the processing block of the node's code, and the user should be routed to an erroneous state outcome. It may be appropriate to have a single error outcome, multiple error outcomes, or no error outcome at all, depending on the node.

It is valuable to store information about the cause of the error in the shared state, in case a node further along the tree processes it. This information should include error text to display to the user. If the shared state is used for this purpose, it is important to document not only the meaning of the various outcomes, but also the keys used to store information in the shared state.

## Configuration errors

You can display error messages to the tree administrator; for example, when a configuration property of a node is required, but not provided.

To automatically display an appropriate error message when required values are missing, add `requiredValue=true` to your config property, as follows:

```java
@Attribute(order = 300, requiredValue = true)
Set<String> accountSearchBaseDn();
```

To control the messages displayed on error, ensure there is a `.properties` file under `src/main/resources/org.forgerock.openam.auth.nodes` with the same name as your node class. Learn more in [Internationalize nodes](i18n-nodes.html).

---

---
title: Handle multiple visits to the same node
description: Handle multiple visits to the same authentication node by using Action.send() to re-route directly or Retry Limit Decision node to control retry attempts
component: pingam
version: 8.1
page_id: pingam:auth-nodes:handle-multiple-visits
canonical_url: https://docs.pingidentity.com/pingam/8.1/auth-nodes/handle-multiple-visits.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Extensibility", "Nodes &amp; Trees"]
---

# Handle multiple visits to the same node

An authentication flow can return to a decision node in the following ways:

* Route the failure outcome through a [Retry Limit Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/retry-limit-decision.html).

  This node can limit how many times a user can enter incorrect authentication details when the user is directed to an earlier node in the tree to re-enter their information. For example, to an earlier [Username Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/am-only/username-collector.html).

* Re-route directly to the current processing node.

  To achieve this, use the `Action.send()` method rather than `Action.goTo()`. The `Action.goTo` method passes control to the next node in the tree. The `Action.send()` method takes a list of callbacks that you can construct in the current node. The return value is an `ActionBuilder` that can be used to create an `Action` as follows:

  ```java
  ActionBuilder action = Action.send(ImmutableList.of(new ChoiceCallback(), new ConfirmationCallback()));
  ```

A typical example of returning to the same node is a password change screen where the user must enter their current password, new password, and new password confirmation. The node that processes these callbacks needs to remain on the screen and display an error message if any of the data entered by the user is incorrect. For example, if the new password and password confirmation don't match.

When a `ConfirmationCallback` is invoked on a screen that was produced by `Action.send()`, it always routes back to the node that created it. After the details are valid, return an `Action` created using `Action.goTo()` and tree processing can continue as normal.

---

---
title: Include callbacks
description: Use callbacks in PingAM authentication nodes to enable user interaction, retrieve user responses, and execute client-side JavaScript
component: pingam
version: 8.1
page_id: pingam:auth-nodes:include-callbacks
canonical_url: https://docs.pingidentity.com/pingam/8.1/auth-nodes/include-callbacks.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Extensibility", "Nodes &amp; Trees"]
section_ids:
  client-side-javascript: Send and execute JavaScript in a callback
---

# Include callbacks

Nodes use *callbacks* to enable interaction with the authenticating user.

You can't create your own callbacks, but there are many existing implementations available to you. Learn more in [Supported callbacks](../am-authentication/callbacks-supported.html).

Calling the `getCallbacks(Class<t> callbackType)` method on a `TreeContext`, the sole argument to the `process()` method of a node, returns all callbacks of a particular type for the most recent request from the current node. For example, calling `context.getCallbacks(PasswordCallback.class)` returns a list of the `PasswordCallback` callbacks displayed in the UI most recently.

The following is an example of multiple callbacks created by a node and passed to the UI:

![An example of multiple callbacks created by a node and passed to the UI.](_images/callbacks.png)

To process the responses to callbacks, you must know the order of the callbacks in the list. You can find the position of the callbacks created by the current node by using the constant properties for each callback position in the processing node.

If the callbacks were created in previous nodes, their positions must be stored in the shared state before subsequent nodes can use them.

The following is the code that created the UI displayed in the previous image:

```java
ImmutableList.of(
  new TextOutputCallback(messageType, message.toUpperCase()),
  new PasswordCallback(bundle.getString("oldPasswordCallback"), false),
  new PasswordCallback(bundle.getString("newPasswordCallback"), false),
  new PasswordCallback(bundle.getString("confirmPasswordCallback"), false),
  confirmationCallback
);
```

The order of callbacks defined in the code is preserved in the UI.

## Send and execute JavaScript in a callback

A node can provide JavaScript for execution on the client-side browser.

For example, the following is a simple JavaScript script named `hello-world.js`:

```java
alert("Hello, World!");
```

Execute the script on the client by using the following code:

```java
String helloScript = getScriptAsString("hello-world.js");
ScriptTextOutputCallback scriptCallback = new ScriptTextOutputCallback(helloScript);
ImmutableList<Callback> callbacks = ImmutableList.of(scriptCallback);
return send(callbacks).build();
```

Variables can be injected using your favorite Java String utilities, such as `String.format(script, myValue)`.

To retrieve the data back from the script, add `HiddenValueCallback` to the list of callbacks sent to the user, as follows:

```java
HiddenValueCallback hiddenValueCallback = new HiddenValueCallback("myHiddenOutcome", "false");
```

The JavaScript needs to add the required data to the `HiddenValueCallback` and submit the form, for example:

```javascript
document.getElementById('myHiddenOutcome').value = "client side data";
document.getElementById("loginButton_0").click();
```

In the process method of the node, retrieve the hidden callback as follows:

```java
Optional<String> result = context.getCallback(HiddenValueCallback.class)
  .map(HiddenValueCallback::getValue)
  .filter(scriptOutput -> !Strings.isNullOrEmpty(scriptOutput));

if (result.isPresent()) {
  String myClientSideData = result.get();
}
```

---

---
title: Inject objects into a node instance
description: Use Guice dependency injection to inject objects into authentication node instances, including realm, node ID, tree metadata, and custom configuration objects
component: pingam
version: 8.1
page_id: pingam:auth-nodes:core-inject
canonical_url: https://docs.pingidentity.com/pingam/8.1/auth-nodes/core-inject.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Extensibility", "Nodes &amp; Trees", "Scripts"]
section_ids:
  using-a-cache: Use a cache
  send-http-request: Send an HTTP request
  custon-guice-bindings: Custom Guice bindings
---

# Inject objects into a node instance

A node instance is constructed every time the node is reached in a tree and is discarded as soon as it's been used to process the state once.

State stored in a node is lost when the node's process method completes. To make state available for other nodes in the tree, nodes must return the state to the user or store it in the *shared state*.

AM uses Google's *Guice* dependency injection framework for authentication nodes and uses Guice to manage most of its object lifecycles. Use *just-in-time* bindings from the constructor to inject an object from Guice.

The following node-specific instances are available from Guice:

* @Assisted Realm

  The realm that the node is in.

* @Assisted UUID

  The unique ID of the node instance.

* @Assisted TreeMetadata

  The metadata for the tree that the node belongs to.

* \<T> @Assisted T

  The configuration object that is an instance of the interface specified in the `configClass` metadata parameter.

|   |                                                                                                     |
| - | --------------------------------------------------------------------------------------------------- |
|   | Any other objects in AM that are managed by Guice can also be obtained from within the constructor. |

The following example is the configuration injection used by the [Debug node](https://docs.pingidentity.com/auth-node-ref/8.1/am-only/debug.html):

```java
@Inject
public DebugNode(@Assisted DebugNode.Config config) {
  this.config = config;
  ...
}
```

Learn more in the [Inject](https://google.github.io/guice/api-docs/latest/javadoc/com/google/inject/Inject.html) and [Assisted](https://google.github.io/guice/api-docs/latest/javadoc/com/google/inject/assistedinject/Assisted.html) annotation types in the *Google Guice Javadoc*.

## Use a cache

You can use Guice injection to cache information in a node by annotating the object that contains the cache with the `@Singleton` annotation.

|   |                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The Guice injected singleton will be used by multiple threads, so it must be thread safe. The following example uses the Google `LoadingCache`, which is thread safe. Alternatively, use `java.util.concurrent.ConcurrentMap` if you prefer to use a built-in Java class. |

For example:

```java
@Node.Metadata(
  outcomeProvider = SingleOutcomeNode.OutcomeProvider.class,
  configClass = MyCustomNode.Config.class)
  public class MyCustomNode extends SingleOutcomeNode {

    public interface Config {
      String url();
    }

    private final Config config;
    private final MyCustomNodeCache cache;

    @Inject
    public MyCustomNode(@Assisted Config config, MyCustomNodeCache cache) {
      this.config = config;
      this.cache = cache;
    }

    @Override
    public Action process(TreeContext context) {
      CachedThing thing = cache.getThing(config.url());
      // implement node logic here
    }
}

@Singleton
class MyCustomNodeCache {
   private final LoadingCache<String, CachedThing> cache =
      CacheBuilder.newBuilder()
         .build(CacheLoader.from(url -> read(url)));

   public CachedThing get(String url) {
      return cache.get(url);
   }

   private CachedThing read(String url) {
      // Access resource and construct
   }
}
```

## Send an HTTP request

You can use Guice injection to send an HTTP request by injecting the `CloseableHttpClientHandler` into the node instance. This means the node uses the standard AM HTTP client handler, and all the httpClient settings and tuning apply.

The following example demonstrates sending an HTTP POST request to the `https://www.example.com/api` endpoint:

```java
@Inject
public MyCustomNode(@Named("CloseableHttpClientHandler") Handler httpClientHandler) {
  this.httpClientHandler = httpClientHandler;
}

@Override
public Action process(TreeContext context) {
   URI uri = URI.create("https://www.example.com/api");

   Request request = new Request()
           .setUri(uri)
           .setMethod(HttpConstants.Methods.POST);

   JsonValue body = json(object(field("sampleKey", "sampleValue")));
   request.getEntity().setJson(body);

   Response response = httpClientHandler.handle(new RootContext(), request).getOrThrow();
}
```

## Custom Guice bindings

If just-in-time bindings aren't sufficient for your use case, you can add your own Guice module into the injector configuration by implementing your own `com.google.inject.Module` and registering it using the service loader mechanism. For example:

```java
// com/example/MyCustomModule.java
public class MyCustomModule extends AbstractModule {
   @Override
   protected void configure() {
      bind(Thing.class).to(MyThing.class);
      // and so on
   }
}
```

```java
// META-INF/services/com.google.inject.Module
// Learn more in https://docs.oracle.com/javase/tutorial/ext/basics/spi.html
com.example.MyCustomModule
```

The `MyCustomModule` object will then be automatically configured as part of the injector creation.

---

---
title: Internationalize nodes
description: Create Java resource bundles to internationalize node UI text, error messages, and administrator-facing content using locale-specific properties files
component: pingam
version: 8.1
page_id: pingam:auth-nodes:i18n-nodes
canonical_url: https://docs.pingidentity.com/pingam/8.1/auth-nodes/i18n-nodes.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Extensibility", "Nodes &amp; Trees", "Scripts", "Translation"]
section_ids:
  to-localize-callback-node-text: Localize node UI text
---

# Internationalize nodes

Internationalization (i18n) of content targets both the end user and the node administrator. Messages sent to users and other UIs can be internationalized.

You can also internationalize error messages and administrator-facing UI using the same mechanism for better user and admin experience.

Internationalized nodes use the locale of the request to find the correct resource bundle, with a default fallback if none is found.

## Localize node UI text

1. Create a Java resource bundle under the `resources` folder in the Maven project for your node.

   The path and filename must match that of the core class that will use the translated text.

   For example, the resource bundle for the [Username Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/am-only/username-collector.html) is located in the following path: `src/main/resources/org/forgerock/openam/auth/nodes/UsernameCollectorNode`.

   ![The resource bundle for the username collector node as displayed in the project window in the IntelliJ IDE.](_images/auth-node-resource-bundle.png)Figure 1. Example resource bundle

2. Add the properties and strings that the node will display to the user.

   For example:

   ```java
   callback.username=User Name
   ```

3. Create a `.properties` file in the resource bundle for each language your node will display.

   The filename must include the language identifier, as per [rfc5646 - Tags for Identifying Languages](https://datatracker.ietf.org/doc/html/rfc5646).

   For example, for French translations your `.properties` file could be called `UsernameCollectorNode_fr.properties`.

4. Replicate the properties and translate the values in each `.properties` files.

   For example:

   ```java
   callback.username=Nom d'utilisateur
   ```

5. In the core class for your node, specify the path to the resource bundle from which the node will retrieve the translated strings:

   ```java
   private static final String BUNDLE = "org/forgerock/openam/auth/nodes/UsernameCollectorNode";
   ```

6. Define a reference to the bundle using the `getBundleInPreferredLocale` function to enable retrieval of translated strings:

   ```java
   ResourceBundle bundle = context.request.locales.getBundleInPreferredLocale(
           BUNDLE, getClass().getClassLoader());
   ```

7. Use the `getString` function whenever you need to retrieve a translation from the resource bundle:

   ```java
   return send(new NameCallback(bundle.getString("callback.username"))).build();
   ```

---

---
title: Metadata annotation
description: Use the Metadata annotation to specify outcome providers, configuration classes, validators, and other metadata for authentication nodes
component: pingam
version: 8.1
page_id: pingam:auth-nodes:core-metadata
canonical_url: https://docs.pingidentity.com/pingam/8.1/auth-nodes/core-metadata.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Extensibility", "Nodes &amp; Trees", "Scripts"]
section_ids:
  outcome-provider: Outcome provider
  config-class: Configuration class
  config-validator: Configuration validator
  extensions: Extensions
  tags: Tags
---

# Metadata annotation

The `Metadata` annotation specifies two required attributes: the `outcomeProvider` and the `configClass`. Typically, the `configClass` attribute is an inner interface in the node implementation class.

You can also specify the following optional attributes: `configValidator`, `extensions`, and `tags`.

For example, the following is the `@Node.Metadata` annotation for the [Data Store Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/data-store-decision.html):

```java
@Node.Metadata(outcomeProvider = AbstractDecisionNode.OutcomeProvider.class,
        configClass = DataStoreDecisionNode.Config.class,
        tags = {"basic authn", "basic authentication"})
```

## Outcome provider

The `outcomeProvider` class defines the possible node outcomes.

The abstract implementations of the node interface, `org.forgerock.openam.auth.node.api.SingleOutcomeNode` and `org.forgerock.openam.auth.node.api.AbstractDecisionNode`, define outcome providers you can use for simple use cases. Provide your own implementation for more complex use cases.

To ensure the node is available to the [Configuration Provider node](https://docs.pingidentity.com/auth-node-ref/8.1/config-provider.html), your outcome provider class must implement the `StaticOutcomeProvider` or the `BoundedOutcomeProvider` interfaces.

Learn more about these implementations and interfaces in the [org.forgerock.openam.auth .node.api](../_attachments/apidocs/org/forgerock/openam/auth/node/api/package-summary.html) package.

For example, the following is the custom outcome provider from the [LDAP Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/ldap-decision.html), which has `True`, `False`, `Locked`, `Cancelled`, and `Expired` exit paths:

```java
    /**
     * Defines the possible outcomes from this Ldap node.
     */
    public static class LdapOutcomeProvider implements StaticOutcomeProvider {
        @Override
        public List<Outcome> getOutcomes(PreferredLocales locales) {
            ResourceBundle bundle = locales.getBundleInPreferredLocale(LdapDecisionNode.BUNDLE,
                    LdapOutcomeProvider.class.getClassLoader());
            return ImmutableList.of(
                    new Outcome(LdapOutcome.TRUE.name(), bundle.getString("trueOutcome")),
                    new Outcome(LdapOutcome.FALSE.name(), bundle.getString("falseOutcome")),
                    new Outcome(LdapOutcome.LOCKED.name(), bundle.getString("lockedOutcome")),
                    new Outcome(LdapOutcome.CANCELLED.name(), bundle.getString("cancelledOutcome")),
                    new Outcome(LdapOutcome.EXPIRED.name(), bundle.getString("expiredOutcome")));
        }
    }
```

## Configuration class

The `configClass` contains the configuration of any attributes requested by the node when using it as part of a tree.

Learn more in the [Config interface](core-config.html).

## Configuration validator

The optional `configValidator` class validates the provided configuration at the class level. This can be useful when you have two attributes that depend on each other for validation. For example, an attribute is only required if another attribute is set to `true`.

The `configValidator` class must implement the [ServiceConfigValidator](../_attachments/apidocs/org/forgerock/openam/sm/ServiceConfigValidator.html) interface.

For example, the following is the `@Node.Metadata` annotation for the [Message node](https://docs.pingidentity.com/auth-node-ref/8.1/message.html):

```java
@Node.Metadata(outcomeProvider = AbstractDecisionNode.OutcomeProvider.class,
        configClass = MessageNode.Config.class,
        configValidator = MessageNode.MessageNodeValidator.class,
        tags = {"utilities"})
```

Where the `MessageNode.MessageNodeValidator.class` validates the locales entered:

```java
    /**
     * Validates the message node, ensuring all provided Locales are valid.
     */
    public static class MessageNodeValidator implements ServiceConfigValidator {

        private final Logger logger = LoggerFactory.getLogger(MessageNodeValidator.class);

        private static String getLocaleStringFromMessage(String message) {
            return StringUtils.substringBetween(message, "[", "]");
        }

        @Override
        public void validate(Realm realm, List<String> configPath, Map<String, Set<String>> attributes)
                throws ServiceConfigException, ServiceErrorException {
            for (String messageAttribute : MESSAGE_ATTRIBUTES) {
                validateMessageAttribute(attributes, messageAttribute);
            }
        }

        private void validateMessageAttribute(Map<String, Set<String>> attributes, String messageAttribute)
                throws ServiceConfigException {
            Set<String> attributesSet = attributes.get(messageAttribute);
            Set<Locale> messageLocales = attributesSet.stream()
                    .map(MessageNodeValidator::getLocaleStringFromMessage)
                    .map(com.sun.identity.shared.locale.Locale::getLocale)
                    .collect(Collectors.toSet());
            for (Locale messageLocale : messageLocales) {
                if (!LocaleUtils.isAvailableLocale(messageLocale)) {
                    logger.debug("Invalid messageLocale {} for {} attribute", messageLocale.toString(),
                            messageAttribute);
                    throw new ServiceConfigException("Invalid locale provided");
                }
            }
        }
    }
```

## Extensions

The optional `extensions` class provides additional metadata information about the node. The Java class is serialized into JSON.

For example, the following is the `@Node.Metadata` annotation for the [Username Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/am-only/username-collector.html) with an `extensions` class added:

```java
@Node.Metadata(outcomeProvider = SingleOutcomeNode.OutcomeProvider.class,
        configClass = UsernameCollectorNode.Config.class,
        extensions = UsernameCollectorNode.ExtraMetadata.class,
        tags = {"basic authn", "basic authentication"})
```

Where the `UsernameCollectorNode.ExtraMetadata.class` adds extra metadata:

```java
/**
     * Extra Metadata for the username collector node.
     */
    public static class ExtraMetadata {

        /**
         * The owner of the node.
         */
        public String owner = "Ping Identity";

    }
```

To retrieve the metadata for a node, send a `POST` request to the `realm-config/authentication/authenticationtrees/nodes/node-name/n.0?_action=getType` endpoint.

Example response:

```json
"metadata": {
    "owner": "Ping Identity",
     ...
},
```

## Tags

The optional `tags` attribute contains a list of tags to categorize the node within the tree designer view.

Tags are made up of one or more text strings that let users find the node more easily when designing trees. For example, you could include common pseudonyms for the functionality the node provides, such as `mfa` for a node that provides multi-factor authentication functionality.

The tree designer view organizes nodes into a number of categories, based on the presence of certain tag values, as described in the table below:

**Authentication node tag categories**

| Category             | Tag                      | Example nodes                                                                                                                                                                                                                       |
| -------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Basic Authentication | `"basic authentication"` | [Data Store Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/data-store-decision.html) [Username Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/am-only/username-collector.html)                     |
| MFA                  | `"mfa"`                  | [Push Sender node](https://docs.pingidentity.com/auth-node-ref/8.1/push-sender.html) [WebAuthn Authentication node](https://docs.pingidentity.com/auth-node-ref/8.1/webauthn-authentication.html)                                   |
| Risk                 | `"risk"`                 | [Account Lockout node](https://docs.pingidentity.com/auth-node-ref/8.1/account-lockout.html) [CAPTCHA node](https://docs.pingidentity.com/auth-node-ref/8.1/captcha.html)                                                           |
| Behavioral           | `"behavioral"`           | [Increment Login Count node](https://docs.pingidentity.com/auth-node-ref/8.1/increment-login-count.html) [Login Count Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/login-count-decision.html)                     |
| Contextual           | `"contextual"`           | [Cookie Presence Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/cookie-presence-decision.html) [Set Persistent Cookie node](https://docs.pingidentity.com/auth-node-ref/8.1/set-persistent-cookie.html)             |
| Federation           | `"federation"`           | [OAuth 2.0 node](https://docs.pingidentity.com/auth-node-ref/8.1/am-only/oauth2.html) [OpenID Connect node](https://docs.pingidentity.com/auth-node-ref/8.1/am-only/oidc.html)                                                      |
| Identity Management  | `"identity management"`  | [Anonymous User Mapping node](https://docs.pingidentity.com/auth-node-ref/8.1/anonymous-user-mapping.html) [Terms and Conditions Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/terms-and-conditions-decision.html) |
| Utilities            | `"utilities"`            | [Choice Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/choice-collector.html) [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/scripted-decision.html)                                     |

|   |                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------- |
|   | Nodes that aren't tagged with one of these tags appear in an **[icon: square, set=fa]Uncategorized** section. |

For example, the `@Node.Metadata` annotation for [Timer Start node](https://docs.pingidentity.com/auth-node-ref/8.1/timer-start.html) places it in the Utilities section:

```java
@Node.Metadata(outcomeProvider = SingleOutcomeNode.OutcomeProvider.class,
        configClass = TimerStartNode.Config.class,
        tags = {"metrics", "utilities"})
```

Learn more in the [Annotation Interface Node.Metadata](../_attachments/apidocs/org/forgerock/openam/auth/node/api/Node.Metadata.html).

To retrieve the tags for a node, send a `POST` request to the `realm-config/authentication/authenticationtrees/nodes/node-name/n.0?_action=getType` endpoint.

Example response:

```json
"tags": [
    "metrics",
    "utilities"
],
```

---

---
title: Node class
description: Implement the Node interface to access persisted state, request user input via callbacks, and define exit paths for authentication nodes in PingAM trees
component: pingam
version: 8.1
page_id: pingam:auth-nodes:core-class
canonical_url: https://docs.pingidentity.com/pingam/8.1/auth-nodes/core-class.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Extensibility", "Nodes &amp; Trees", "Scripts"]
---

# Node class

The `Node` class can access and modify the persisted state shared between the nodes within a tree, and can request input by using callbacks. The class also defines the possible exit paths from the node.

In Java terms, an authentication node is a class that implements the `Node` interface, `org.forgerock.openam.auth.node.api.Node`.

The `UsernameCollectorNodeV2` class shows the steps to implement the Node interface:

```java
package org.forgerock.openam.auth.nodes;

import static java.util.Objects.requireNonNull;
import static org.forgerock.openam.auth.node.api.Action.send;
import static org.forgerock.openam.auth.node.api.SharedStateConstants.USERNAME;

import java.util.ResourceBundle;

import javax.inject.Inject;
import javax.security.auth.callback.NameCallback;

import org.forgerock.openam.annotations.sm.Attribute;
import org.forgerock.openam.auth.node.api.Action;
import org.forgerock.openam.auth.node.api.InputState;
import org.forgerock.openam.auth.node.api.Node;
import org.forgerock.openam.auth.node.api.OutputState;
import org.forgerock.openam.auth.node.api.SingleOutcomeNode;
import org.forgerock.openam.auth.node.api.TreeContext;
import org.forgerock.openam.utils.StringUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.google.inject.assistedinject.Assisted;

/
 * A node that collects a username from the user using a name callback.
 *
 * <p>Allows setting of a customizable, localizable prompt and a default value retrieved from shared state</p>
 *
 * <p>Places the result in the shared state as 'username'.</p>
 /
@Node.Metadata(outcomeProvider = SingleOutcomeNode.OutcomeProvider.class,              1
        configClass = UsernameCollectorNodeV2.Config.class,
        tags = {"basic authn", "basic authentication"})
@Node.VersionMetadata(name = "UsernameCollectorNode", version = 2)                     2
public class UsernameCollectorNodeV2 extends SingleOutcomeNode {                       3

    private final Config config;                                                       4

    @Inject                                                                            5
    UsernameCollectorNodeV2(@Assisted Config config) {
        this.config = config;
    }
    /
     * Configuration for the username collector node V2.
     */
    public interface Config {                                                          6
        /*
         * If true, will prepopulate the username field with a value from shared state.
         *
         * @return Whether to prepopulate the username input field with a value from shared state
         */
        @Attribute(order = 100)
        default boolean prepopulate() {
            return false;
        }
    }

    private static final String BUNDLE = UsernameCollectorNodeV2.class.getName();
    private final Logger logger = LoggerFactory.getLogger(UsernameCollectorNodeV2.class);

    @Override                                                                          7
    public Action process(TreeContext context) {
        logger.debug("UsernameCollectorNode started");
        var nameCallback = context.getCallback(NameCallback.class);
        if (nameCallback.isPresent() && StringUtils.isNotEmpty(nameCallback.get().getName())) {
            context.getStateFor(this).putShared(USERNAME, nameCallback.get().getName());
            return goToNext().build();
        }

        return collectUsername(context);
    }

    private Action collectUsername(TreeContext context) {
        logger.debug("collecting username");
        ResourceBundle bundle = context.request.locales.getBundleInPreferredLocale(BUNDLE, getClass().getClassLoader());
        var nameCallback = new NameCallback(bundle.getString("callback.username"));
        var nodeState = context.getStateFor(this);
        if (config.prepopulate() && nodeState.isDefined(USERNAME)) {
            nameCallback.setName(requireNonNull(nodeState.get(USERNAME)).asString());
        }
        return send(nameCallback).build();
    }

    @Override
    public OutputState[] getOutputs() {
        return new OutputState[]{
                new OutputState(USERNAME)
        };
    }

    @Override
    public InputState[] getInputs() {
        return new InputState[]{
                new InputState(USERNAME)
        };
    }
}
```

| Step                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Further information                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 Apply the `@Node.Metadata` annotation        | The `Metadata` annotation specifies the outcome provider, configuration class, and optionally, the configuration validator, extensions and tags.Use an existing outcome provider such as `SingleOutcomeNode.OutcomeProvider` or `AbstractDecisionNode.OutcomeProvider`, or create a custom provider and reference the class from the annotation.                                                                                                                                                                                                                                        | [Metadata annotation](core-metadata.html)                                                                                                                                                                                                                                                                                              |
| 2 Apply the `@Node.VersionMetadata` annotation | Create a versioned node.The `VersionMetadata` annotation specifies the name, version, and optionally, the upgrader class.                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [VersionMetadata annotation](versionmetadata.html)                                                                                                                                                                                                                                                                                     |
| 3 Implement the `Node` interface               | Extend one of the following abstract classes to implement the `Node` interface:- `SingleOutcomeNode`

  For nodes with a single exit path. For example, [Modify Auth Level node](https://docs.pingidentity.com/auth-node-ref/8.1/modify-auth-level.html).

- `AbstractDecisionNode`

  For nodes with a boolean-type exit path (true/false, allow/deny). For example, [Data Store Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/data-store-decision.html).Alternatively, write your own implementation of the `OutcomeProvider` interface to define custom exit paths. | Javadoc:- [Node](../_attachments/apidocs/org/forgerock/openam/auth/node/api/Node.html) interface

- [SingleOutcomeNode](../_attachments/apidocs/org/forgerock/openam/auth/node/api/SingleOutcomeNode.html) class

- [AbstractDecisionNode](../_attachments/apidocs/org/forgerock/openam/auth/node/api/AbstractDecisionNode.html) class |
| 4 Define private constants and methods         | *Optional*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                        |
| 5 Inject dependencies                          | Inject objects using Guice as this makes it easier to unit test your node.This example specifies `config` as a parameter. You can also include supported AM classes, instances of third-party dependencies, or your own types.                                                                                                                                                                                                                                                                                                                                                          | [Inject objects into a node instance](core-inject.html)                                                                                                                                                                                                                                                                                |
| 6 Implement the `Config` interface             | The `Config` interface defines the configuration data for a node.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | [Config interface](core-config.html)                                                                                                                                                                                                                                                                                                   |
| 7 Override the `process` method                | The `process` method is where you store and retrieve state if required.It takes a `TreeContext` parameter that you can use to access the request, callbacks, shared state and other input.The method returns an `Action` object. This can be a response or callback to the user, an update of state, or a choice of outcome. The `Action` object encapsulates changes to state and flow control.The choice of outcome in a simple decision node is `true` or `false`, resulting in the authentication tree flow moving from the current node to a node at the relevant connection.      | [Action class](core-action.html)                                                                                                                                                                                                                                                                                                       |

---

---
title: NodeVersionUpgrader.UpgraderMetadata annotation
description: Use the NodeVersionUpgrader.UpgraderMetadata annotation to specify version and previousUpgrader attributes for custom node upgraders
component: pingam
version: 8.1
page_id: pingam:auth-nodes:nodeversionupgrader
canonical_url: https://docs.pingidentity.com/pingam/8.1/auth-nodes/nodeversionupgrader.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Extensibility", "Nodes &amp; Trees", "Scripts"]
section_ids:
  version: Version
  previous_upgrader: Previous Upgrader
---

# NodeVersionUpgrader.UpgraderMetadata annotation

The `NodeVersionUpgrader.UpgraderMetadata` annotation on the `upgrader` class specifies the `version` and the `previousUpgrader` attributes, both of which are required.

For example, the following is the `@NodeVersionUpgrader.UpgraderMetadata` annotation for version 2 of a Custom node:

```java
@NodeVersionUpgrader.UpgraderMetadata(version = 2, previousUpgrader = NoUpgrades.class)
```

## Version

The `version` attribute specifies the version of the new node.

## Previous Upgrader

The `previousUpgrader` attribute specifies the class name of the previous `upgrader`:

* If this annotation is for the node's first upgrader (upgrading from version 1 to version 2), set `previousUpgrader = NoUpgrades.class` to signify there isn't a previous upgrader.

* If this annotation is for a subsequent upgrader (for example, upgrading from version 2 to version 3), set `previousUpgrader` to the class name of the `upgrader` for the previous node version.

  For example, if this annotation is for an upgrade from version 2 to version 3, specify the name of the `upgrader` class for the version 2 node.

---

---
title: Plugin class
description: Create a plugin class that implements AmPlugin to register custom authentication nodes with PingAM using the plugin framework
component: pingam
version: 8.1
page_id: pingam:auth-nodes:plugin-class
canonical_url: https://docs.pingidentity.com/pingam/8.1/auth-nodes/plugin-class.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Extensibility", "Integration", "Nodes &amp; Trees", "Scripts", "Upgrade"]
---

# Plugin class

The plugin class is responsible for informing AM about the details of the customized authentication node. There is little variation between the plugin class for each authentication node, other than the version number and class names within.

Authentication nodes are installed into the product using the AM plugin framework. All AM plugins are created by implementing the `org.forgerock.openam.plugins.AmPlugin` interface and registering it using the Java service architecture - placing a file in META-INF/services.

For plugins that provide authentication nodes, there's an abstract implementation of the `AmPlugin` interface named `org.forgerock.openam.auth.node.api.AbstractNodeAmPlugin`.

The following is an example of the plugin class for an authentication node:

```java
public class MyCustomNodePlugin extends AbstractNodeAmPlugin {         1

  private static final String CURRENT_VERSION = "2.0.0";               2

  @Override
  protected Map<String, Iterable<? extends Class<? extends Node>>>
  getNodesByVersion() {                                                3
        return Map.of("1.0.0", List.of(MyCustomNode.class),
                "2.0.0", List.of(MyCustomNodeV2.class));
  }

  @Override
  public void upgrade(String fromVersion) throws PluginException {     4
      pluginTools.upgradeAuthNode(MyCustomNode.class);
      pluginTools.upgradeAuthNode(MyCustomNodeV2.class);
      super.upgrade(fromVersion);
    }

  @Override
  public String getPluginVersion() {
    return MyCustomNodePlugin.CURRENT_VERSION;
  }
}
```

1 The name of the plugin class. This should be the class name of the node with *Plugin* appended. For example, `MyCustomNodePlugin`.

2 The current version number of the authentication node.

3 The core classes of the authentication nodes to install and register. In this example, AM will register and install two versions of the same node.

4 The core classes of the authentication nodes for plugin-specific upgrades.

AM plugins are notified of the following events:

* `onInstall`

  The plugin has been found during AM startup, and is being installed for the first time. It should create all the services and objects it needs.

* `onStartup(StartupType startupType)`

  The plugin is installed and is being started. Any dependency plugins can be relied on as having been started.

  The type of startup is provided:

  * `FIRST_TIME_INSTALL`. The AM instance has been installed for the first time.

  * `NORMAL_STARTUP`. The AM instance is starting from a previously installed state, or is joining an already installed cluster.

* `onShutdown`

  The AM instance is in the process of shutting down cleanly. Any resources the plugin is using should be released and cleaned up.

* `upgrade(String fromVersion)`

  An existing version of the plugin is installed, and a new version has been found during startup. The plugin should make any changes it needs to the services and objects used in the previous version, and create all the services and objects required by the new version.

  The version of the plugin being upgraded is provided.

* `onAmUpgrade(String fromVersion, String toVersion)`

  An AM system upgrade is in progress. Any updates needed to accommodate the AM upgrade should be made.

  Plugin-specific upgrades shouldn't be made here, because `upgrade` is called if the plugin version also changes.

  The AM version being upgraded from, and to, are provided.

The plugin is responsible for maintaining a version number for its content, which is used for triggering appropriate events for installation and upgrade.

Learn more in [amPlugin](../_attachments/apidocs/org/forgerock/openam/plugins/AmPlugin.html) in the *AM Public API Javadoc*.

---

---
title: Post-installation tasks
description: Test and debug authentication nodes using unit tests, functional tests, manual testing, and remote debugging to ensure proper operation and code coverage
component: pingam
version: 8.1
page_id: pingam:auth-nodes:post-install-tasks
canonical_url: https://docs.pingidentity.com/pingam/8.1/auth-nodes/post-install-tasks.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Extensibility", "Nodes &amp; Trees", "Scripts", "Testing"]
page_aliases: ["maintaining-nodes.adoc"]
section_ids:
  testing-nodes: Test nodes
  unit_tests: Unit tests
  functional_tests: Functional tests
  manual_testing: Manual testing
  debugging-nodes: Debug nodes
  use-debug-node: Use the Debug node
  attach-debugger-tomcat: Attach a debugger to Apache Tomcat
  add-debug-logging: Add debug logging
  auditing-nodes: Audit logging
  monitoring-nodes: Monitor nodes
---

# Post-installation tasks

This page covers post-installation tasks relating to authentication nodes, such as testing, debugging, auditing, and performance monitoring.

## Test nodes

You can test authentication nodes in multiple ways, including unit tests, functional tests, and performing exploratory or manual testing.

Authentication nodes are well suited to tests that have a high percentage of code coverage. The low number of static dependencies lets you unit test the node class as well as the business logic classes.

### Unit tests

Your unit tests should aim to cover a high percentage of the code. Most of the business logic is defined by the tree layout instead of within the nodes themselves, which simplifies unit testing.

At a minimum, the `process(TreeContext context)` method must be tested to make sure all appropriate code paths are triggered, based on whether appropriate values in the shared state and callbacks exist.

The `TreeContext` class and contents have been designed to simplify unit tests without needing to mock.

### Functional tests

Functional tests involve creating an authentication tree in an AM instance and testing it using the REST API. You should write them to cover all the possible authentication flows, including successful and unsuccessful outcomes.

Consider the following when writing functional tests:

* All relevant code paths discovered through unit testing should be functionally tested to ensure helper, utility, and related mechanisms function as expected.

* Functional tests must make sure the business logic is called correctly and processed as expected.

* Mocking expected services can be useful when functionally testing nodes that make calls to third-party services.

To perform functional testing, write a series of REST requests to create the authentication tree and test all the identified flows through the authentication tree. The REST API returns a JSON payload, which lets you programmatically step through each node and collect responses at every stage.

You can find details about creating a tree using the REST API in [Create a tree over REST](../am-authentication/create-auth-trees.html#create-authn-tree-rest).

|   |                                                                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Test your tree in the UI first and use the Developer Tools in your browser to copy relevant web requests as a curl command. The resulting curl command includes all the headers, options, and data sent for the selected web request. You can use this information and the REST syntax as the basis of your REST calls. |

You can use a third-party tool such as [Postman](https://www.postman.com) for REST-based testing.

### Manual testing

Manual testing should occur both during and after node development.

During development, it is expected a node developer will frequently load and reload nodes to ensure they operate as expected, including configuration and execution, as well as any expected error conditions.

After development, manual testing should continue in an exploratory fashion. Using a node multiple times can often highlight areas left unpolished, or particular usability issues that can be missed by automated testing.

## Debug nodes

You might need to debug your nodes during development as well as prepare your nodes to allow debug logging after they are deployed.

### Use the Debug node

During development, it can be useful to include one or more Debug nodes in your authentication tree to inspect the tree state.

1. Insert the [Debug node](https://docs.pingidentity.com/auth-node-ref/8.1/am-only/debug.html) in the tree between the node you want to inspect and the next node in the flow. For example, if you wanted to inspect the Custom Node, where the next node was a Scripted Decision node, you would insert the Debug node as follows:

   ![Debug Node](_images/debug-node.png)

2. Save your changes.

3. Test your tree in a new incognito browser window (or a separate browser).

   When the Debug node is reached, a pop-up window displays details about the tree state.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If the browser blocks the pop-up window, unblock it:- For Chrome, follow the instructions under the "Allow pop-ups and redirects from a site" section in this support article: <https://support.google.com/chrome/answer/95472>.

   - For other [supported browsers](https://docs.pingidentity.com/pingam/release-notes/requirements.html#supported-clients), consult the browser documentation.Refresh the browser window. The pop-up window should now appear. |

4. Remove the Debug node once you finish debugging.

### Attach a debugger to Apache Tomcat

During development, you may want to attach a remote debugger to Tomcat to let you debug the node development with an IDE (for example, to set breakpoints).

1. Set a `CATALINA_OPTS` environment variable to enable the debugger on Tomcat. For example, add the following in your `setenv` file:

   * Linux

   * Windows

   In `$CATALINA_BASE/bin/setenv.sh`:

   ```bash
   export CATALINA_OPTS="$CATALINA_OPTS -Xdebug -Xrunjdwp:transport=dt_socket,
   address=*:8000,server=y,suspend=n"
   ```

   In `$CATALINA_BASE/bin/setenv.bat`:

   ```powershell
   set "CATALINA_OPTS=%CATALINA_OPTS% -Xdebug -Xrunjdwp:transport=dt_socket,
   address=*:8000,server=y,suspend=n"
   ```

   The `*:` in the `address` option lets you debug remote servers as well as developments running on `localhost`.

2. Start the web container as normal.

3. Connect your IDE to Tomcat as a remote JVM debug instance. The way you do this depends on your IDE, but make sure the following settings are correct:

   * `Port`: the port in the IDE debug configuration must match the port set in the `setenv` file (`8000` in this example).

   * `Address`: the address should either be the IP address of the Tomcat instance if it's running on a different machine or `localhost`.

4. Remove the debugger options from your `setenv` file once you finish debugging.

### Add debug logging

Add debug logging to your custom node to help administrators and support staff investigate any issues that arise in production.

To add debug logging to a node, include a reference to the `amAuth` SLF4J Logger instance.

For example, you can assign the logger to a private field as follows:

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

// ...

private final Logger logger = LoggerFactory.getLogger("amAuth");
```

|   |                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Consider the logging level you use. Excessive use of the `error` or `warning` level can cause debug logs to fill, and can have a negative performance impact, if your node is used frequently. |

You can also use the SLF4J `varargs` methods to defer string concatenation to SLF4J. This means you can skip string concatenation if the configured logging level means your message won't be written.

The following example uses the `debug` level:

```java
logger.debug("authLevelSufficient {}", authLevelSufficient);
```

## Audit logging

Audit logging helps administrators to investigate user and system behavior.

AM records all incoming calls as access events. Additionally, to capture further details about the authentication flows, AM records an authentication audit event for each node, and the tree outcome.

A node can provide extra data to be included in the standard audit event which is logged when an authentication node completes.

AM logs an `AM-NODE-LOGIN-COMPLETED` audit event each time an authentication node completes. To add extra information to this audit event, override the node interface method `getAuditEntryDetail`.

For example, the [Retry Limit Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/retry-limit-decision.html) overrides this method to record how many retries remain:

```java
@Override
public JsonValue getAuditEntryDetail() {
  return json(object(field("remainingRetries", String.valueOf(retryLimitCount))));
}
```

When this node is processed, it results in an audit event similar to the following:

```json
{
  "realm": "/",
  "transactionId": "45453155-cf94-4e23-8ee9-ecdfc9f97e12-1785617",
  "component": "Authentication",
  "eventName": "AM-NODE-LOGIN-COMPLETED",
  "entries": [
    {
      "info": {
        "nodeOutcome": "Retry",
        "treeName": "Example",
        "displayName": "Retry Limit Decision",
        "nodeType": "RetryLimitDecisionNode",
        "nodeId": "bf010b6b-61f8-457e-80f3-c3678e5606d2",
        "authLevel": "0",
        "nodeExtraLogging": {
          "remainingRetries": "2"
        }
      }
    }
  ],
  "timestamp": "2018-08-24T09:43:55.959Z",
  "trackingIds": [
    "45453155-cf94-4e23-8ee9-ecdfc9f97e12-1785618"
  ],
  "_id": "45453155-cf94-4e23-8ee9-ecdfc9f97e12-1785622"
}
```

The result of the `getAuditEntryDetail` method is stored in the `nodeExtraLogging` field.

## Monitor nodes

You can track authentication flows that complete with success, failure, or timeout as an outcome by using the metrics functionality built-in to AM.

Learn more in [Monitor AM instances](../monitoring/monitoring-am.html).

You can also use the following nodes in a tree to create custom metrics:

* [Meter node](https://docs.pingidentity.com/auth-node-ref/8.1/meter.html)

* [Timer Start node](https://docs.pingidentity.com/auth-node-ref/8.1/timer-start.html)

* [Timer Stop node](https://docs.pingidentity.com/auth-node-ref/8.1/timer-stop.html)

---

---
title: Prepare for development
description: Set up a Maven project to build custom authentication nodes for PingAM using an archetype or sample projects
component: pingam
version: 8.1
page_id: pingam:auth-nodes:preparing-for-nodes
canonical_url: https://docs.pingidentity.com/pingam/8.1/auth-nodes/preparing-for-nodes.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Extensibility", "Integration", "Nodes &amp; Trees", "Setup &amp; Configuration"]
section_ids:
  proc-custom-auth-nodes-prerequisites: Prepare an environment for building custom authentication nodes
  proc-custom-auth-nodes-project: Set up a Maven project to build custom authentication nodes
  files-in-maven-project: Files contained in the Maven project
  maven-custom-auth-nodes: Tips for custom authentication node projects
---

# Prepare for development

This page explains the prerequisites for building custom authentication nodes, and shows how to use either a Maven archetype, or the samples provided with AM, to set up a project for building nodes.

|   |                                                                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You can find information about customizing post-authentication hooks for a tree in [Create tree hooks](../am-authentication/post-authn-plugins-treehook.html) and customizing logout hooks in [Create logout hooks](../am-authentication/create-logout-hook.html). |

## Prepare an environment for building custom authentication nodes

1. Make sure your Backstage account is part of a subscription:

   * In a browser, go to the [Backstage](https://backstage.pingidentity.com) website and sign on or register for an account.

   * Confirm or request your account is added to a subscription. Learn more in [Getting access to product support](https://support.pingidentity.com/s/article/Getting-access-to-product-support) in the *Knowledge Base*.

2. Install Apache Maven 3.6.3 or later, and Oracle JDK or OpenJDK version 17 or later.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To verify the installed versions, run the `mvn --version` command:```bash
   $ mvn --version
   Apache Maven 3.9.11 (bc0240f3c744dd6b6ec2920b3cd08dcc295161ae)
   Maven home: /opt/homebrew/Cellar/maven/3.9.11/libexec
   Java version: 25.0.1, vendor: Homebrew, runtime: /opt/homebrew/Cellar/openjdk/25.0.1/libexec/openjdk.jdk/Contents/Home
   Default locale: en_GB, platform encoding: UTF-8
   OS name: "mac os x", version: "15.7.1", arch: "aarch64", family: "mac"
   ``` |

3. Configure Maven to be able to access the proprietary repositories by adding your Backstage credentials to the Maven `settings.xml` file. Learn more in [How do I access the proprietary protected Maven repositories?](https://support.pingidentity.com/s/article/How-do-I-access-the-proprietary-Maven-repositories).

   If you want to use the archetype to create a project for custom authentication nodes, you also need access to the `forgerock-private-releases` repository. Make sure your `settings.xml` file contains a profile similar to the following:

   ```xml
   <profiles>
     <profile>
     <id>forgerock</id>
     <repositories>
         <repository>
             <id>forgerock-private-releases</id>
             <url>https://maven.forgerock.org/artifactory/private-releases</url>
             <releases>
                 <enabled>true</enabled>
                 <checksumPolicy>fail</checksumPolicy>
             </releases>
             <snapshots>
                 <enabled>false</enabled>
                 <checksumPolicy>warn</checksumPolicy>
             </snapshots>
         </repository>
     </repositories>
     </profile>
   </profiles>
   <activeProfiles>
     <activeProfile>forgerock</activeProfile>
   </activeProfiles>
   ```

## Set up a Maven project to build custom authentication nodes

Ping Identity provides a Maven archetype that creates a starter project, suitable for building an authentication node. You can also download the projects used to build the authentication nodes included with AM and modify those to match your requirements.

|   |                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Complete the steps in [Prepare an environment for building custom authentication nodes](#proc-custom-auth-nodes-prerequisites) before proceeding. |

Complete either of the following steps to set up or download a Maven project to build custom authentication nodes:

1. To use the `auth-tree-node-archetype` archetype to generate a starter Maven project:

   * In a terminal window, go to a folder where you'll create the new Maven project. For example:

     ```bash
     $ cd ~/Repositories
     ```

   * Run the `mvn archetype:generate` command, providing the following information:

     * `groupId`

       A domain name you control, used for identifying the project.

     * `artifactId`

       The name of the JAR created by the project, without version information. Also the name of the folder created to store the project.

     * `version`

       The version assigned to the project.

     * `package`

       The package name in which your custom authentication node classes are generated.

     * `authNodeName`

       The name of the custom authentication node, also used in the generated `README.md` file and for class file names.

       |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
       | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
       |   | AM stores installed nodes with a reference generated from the node's class name. An installed node registered through a plugin is stored with the name returned as a result of calling `Class.getSimpleName()`.AM doesn't protect installed node names. The most recently installed node with a specific name will overwrite any previous installation of that node (including the nodes that are provided with AM by default). You must therefore choose a unique name for your custom node, and make sure the name isn't already used for an existing node. |

       For example:

       ```bash
       $ mvn archetype:generate \
         -DgroupId=com.example \
         -DartifactId=custom-auth-node \
         -Dversion=1.0.0-SNAPSHOT \
         -Dpackage=com.example.custom \
         -DauthNodeName=MyCustomAuthNode \
         -DarchetypeGroupId=org.forgerock.am \
         -DarchetypeArtifactId=auth-tree-node-archetype \
         -DarchetypeVersion=8.1.1 \
         -DinteractiveMode=false
       [INFO] Project created from Archetype in dir: /Users/Ping/Repositories/custom-auth-node
       [INFO] ------------------------------------------------------------------------
       [INFO] BUILD SUCCESS
       [INFO] ------------------------------------------------------------------------
       [INFO] Total time: 11.397 s
       [INFO] Finished at: 2024-09-25T15:45:06+00:00
       [INFO] ------------------------------------------------------------------------
       ```

       A new custom authentication node project is created. For example, in the `/Users/Ping/Repositories/custom-auth-node` folder.

       > **Collapse: Example**
       >
       > ![In this example, the archetype has created the basic structure required to create a custom authentication node.](_images/authn-tree-sample-project.png)
       >
       > Figure 1. Node project created by using the archetype

2. To download the project containing the default AM authentication nodes from the `am-external` repository:

   * Clone the `am-external` repository:

     ```bash
     $ git clone https://github.com/ForgeRock/am-external.git
     ```

   * Check out the `release/8.1.1` branch:

     ```bash
     $ cd am-external
     $ git checkout releases/8.1.1
     ```

     The AM authentication nodes project is located in the `am-external/openam-auth-trees/auth-nodes/` folder.

     > **Collapse: Example**
     >
     > ![In this example, the project was cloned from the am-external repository.](_images/authn-tree-sample-project-am-external.png)
     >
     > Figure 2. Node Project Cloned from the 
     >
     > `am-external`
     >
     >  repository

### Files contained in the Maven project

* `pom.xml`

  Apache Maven project file for the custom authentication node.

  This file specifies how to build the custom authentication node, and also specifies its dependencies on AM components.

  > **Collapse: Example**
  >
  > The following is an example `pom.xml` file from a node project:
  >
  > ```xml
  > <project>
  >   <modelVersion>4.0.0</modelVersion>
  >
  >   <groupId>com.example</groupId>
  >   <artifactId>example-node-plugin</artifactId>
  >   <version>1.0.0</version>
  >
  >   <dependencyManagement>
  >     <dependencies>
  >       <dependency>
  >         <groupId>org.forgerock.am</groupId>
  >         <artifactId>openam-bom</artifactId>
  >         <version>7.2.0-SNAPSHOT</version>
  >         <scope>import</scope>
  >       </dependency>
  >     </dependencies>
  >   </dependencyManagement>
  >
  >   <dependencies>
  >     <dependency>
  >       <groupId>org.forgerock.am</groupId>
  >       <artifactId>auth-node-api</artifactId>
  >       <scope>provided</scope>
  >     </dependency>
  >     <dependency>
  >       <groupId>org.forgerock.am</groupId>
  >       <artifactId>openam-annotations</artifactId>
  >       <scope>provided</scope>
  >     </dependency>
  >     <dependency>
  >       <groupId>com.google.guava</groupId>
  >       <artifactId>guava</artifactId>
  >       <version>26.0-jre</version>
  >     </dependency>
  >   </dependencies>
  >
  >   <build>
  >     <plugins>
  >       <plugin>
  >         <groupId>org.apache.maven.plugins</groupId>
  >         <artifactId>maven-shade-plugin</artifactId>
  >         <configuration>
  >           <shadedArtifactAttached>false</shadedArtifactAttached>
  >           <createDependencyReducedPom>true</createDependencyReducedPom>
  >           <relocations>
  >             <relocation>
  >               <pattern>com.google</pattern>
  >               <shadedPattern>com.example.node.guava</shadedPattern>
  >             </relocation>
  >           </relocations>
  >           <filters>
  >             <filter>
  >               <artifact>com.google.guava:guava</artifact>
  >               <excludes>
  >                 <exclude>META-INF/**</exclude>
  >               </excludes>
  >             </filter>
  >           </filters>
  >           <transformers>
  >             <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
  >               <manifestEntries>
  >                 <Import-Package>javax.annotation;resolution:=optional,sun.misc;resolution:=optional</Import-Package>
  >               </manifestEntries>
  >             </transformer>
  >           </transformers>
  >         </configuration>
  >       </plugin>
  >     </plugins>
  >   </build>
  > </project>
  > ```

* `authNodeName.java`

  Core class for the custom authentication node. Learn more in [Node class](core-class.html).

* `authNodeNamePlugin.java`

  Plugin class for the custom authentication node. Learn more in [Plugin class](plugin-class.html).

* `authNodeName.properties`

  Properties file containing the properties and strings displayed by the custom authentication node to the user.

  You must include a `nodeDescription` property in this file to include your node in the authentication tree designer. AM uses the `nodeDescription` property value as the name of your node.

  You can also create locale specific versions of this file to provide translated text to users. Learn more in [Internationalize nodes](i18n-nodes.html).

The *authNodeName* reflects the name of your authentication node. For example, the `auth-tree-node-archetype` for Maven uses `MyCustomAuthNode` as the *authNodeName*.

## Tips for custom authentication node projects

When you configure a project for creating custom nodes, consider the following points:

* Your node may be deployed into a different AM version to the one you compiled against.

  Nodes from previous product versions *should* be compatible with subsequent product versions if you have only used `@Supported` APIs. Learn more in the [PingAM Java API Specification](../_attachments/apidocs/index.html).

  For example, a node built against AM 7.5 APIs can be deployed in an AM 8.1 instance.

* Other custom nodes may depend on your node, which may be being built against a different version of the AM APIs.

* Other custom nodes, or AM itself, may be using the same libraries as your node. For example, Guava or Apache Commons, and so on. This may cause version conflicts.

To help protect against some of these issues, consider the following recommendations:

* Mark all product dependencies as `provided` in your build system configuration.

* Repackage all external, non-proprietary dependencies inside your own `.jar` file. Repackaged dependencies won't clash with a different version of the same library from another source.

  |   |                                                                                                                                      |
  | - | ------------------------------------------------------------------------------------------------------------------------------------ |
  |   | If you're using Maven, use the [maven-shade-plugin](https://maven.apache.org/plugins/maven-shade-plugin/) to repackage dependencies. |