---
title: Accept Terms and Conditions node
description: Prompts users to accept the active terms and conditions during registration or sign-on journeys in PingAM.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref::accept-terms-and-conditions
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/accept-terms-and-conditions.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Terms &amp; Conditions"]
page_aliases: ["auth-node-accept-terms-and-conditions.adoc"]
section_ids:
  example: Example
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  outcomes: Outcomes
  errors: Errors
---

# Accept Terms and Conditions node

The Accept Terms and Conditions node prompts the user to accept the currently active terms and conditions, configured in the Platform UI *(tooltip: Advanced Identity Cloud admin console)*.

Use this node for registration, or combined with the [Terms and Conditions Decision node](terms-and-conditions-decision.html) for progressive profiling or log in.

## Example

For progressive profiling, include this node after a [Terms and Conditions Decision node](terms-and-conditions-decision.html). If the user has not accepted the latest version of the terms and conditions, evaluation takes them to a page that requires them to accept the current terms and conditions.

The [Patch Object node](patch-object.html) stores the acceptance response in the underlying identity service (PingIDM) if the user accepts:

![Storing acceptance of terms and conditions](_images/trees-node-accept-terms-conditions-tree-example.png)

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes 1      |
| Ping Identity Platform (self-managed) | Yes        |

1 This functionality requires that you configure AM as part of a [Ping Identity Platform deployment](https://docs.pingidentity.com/platform/8.1/sample-setup/).

## Inputs

None. This node doesn't read shared state data.

## Dependencies

This node depends on the underlying identity service (PingIDM) for the active terms and conditions.

## Configuration

This node has no configurable properties.

## Outputs

The node writes a `termsAccepted` object to the shared node state. The object contains these fields:

* `acceptDate`: A timestamp string indicating when the user accepted the terms.

* `termsVersion`: A string indicating the version of the accepted terms.

## Outcomes

Single outcome path; the user accepted the terms and conditions.

## Errors

This node doesn't log any error or warning messages of its own.

---

---
title: Account Active Decision node
description: Checks whether a user account is both active and unlocked, routing the journey along True or False outcome paths in PingAM.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref::account-active-decision
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/account-active-decision.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Accounts"]
page_aliases: ["auth-node-account-active-decision.adoc"]
section_ids:
  example: Example
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  outcomes: Outcomes
  errors: Errors
---

# Account Active Decision node

The **Account Active Decision** node determines whether the current account is both active and unlocked, and lets the journey make a decision, based on that check.

An account is considered locked under these conditions:

* The status is inactive.

* The status is active and a duration lockout is set on the account.

An account is considered unlocked under this condition:

* The status is active and no duration lockout is set on the account.

The node determines whether the account has been locked through both persistent (physical) lockout and duration lockout.

Find more information in [Account lockout](https://docs.pingidentity.com/pingam/8.1/am-authentication/auth-nodes-and-journeys.html#account-lockout-trees).

## Example

For progressive profiling, include this node after a [Terms and Conditions Decision node](terms-and-conditions-decision.html). If the user has not accepted the latest version of the terms and conditions, evaluation takes them to a page that requires them to accept the current terms and conditions.

The [Patch Object node](patch-object.html) stores the acceptance response in the underlying identity service (PingIDM) if the user accepts:

![Storing acceptance of terms and conditions](_images/trees-node-accept-terms-conditions-tree-example.png)

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

## Inputs

The node reads the user's identity from the shared state. Implement a [Username Collector node](am-only/username-collector.html) (standalone AM) or [Platform Username node](platform-username.html) (Ping Identity Platform deployments) earlier in the journey.

## Dependencies

This node has no dependencies.

## Configuration

This node has no configurable properties.

## Outputs

This node doesn't change the shared state.

## Outcomes

* `True`

  The journey follows this outcome path if the account is assessed to be `active` and `unlocked`.

* `False`

  The journey follows this outcome path if the account is assessed to be `inactive` or `locked`.

## Errors

If the node cannot read the identity of the account, it throws the following exception:

`Failed to get the identity object`

---

---
title: Account Lockout node
description: Locks or unlocks a user account profile in PingAM, supporting both persistent and duration-based lockout.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref::account-lockout
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/account-lockout.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Accounts", "User Profiles", "Authentication"]
page_aliases: ["auth-node-account-lockout.adoc"]
section_ids:
  example: Example
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  outcomes: Outcomes
  errors: Errors
---

# Account Lockout node

The Account Lockout node locks or unlocks the authenticating user's account profile.

The node also determines whether the account has been locked through both persistent (physical) lockout and duration lockout.

Find more information in [Account lockout](https://docs.pingidentity.com/pingam/8.1/am-authentication/auth-nodes-and-journeys.html#account-lockout-trees).

|   |                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can also use the [Account Active Decision node](account-active-decision.html) to check whether the account is locked at any point in the journey. |

## Example

The following simple example uses this node with the [Retry Limit Decision node](retry-limit-decision.html) to lock an account after the set number of invalid attempts:

![Lock an account after too many authentication failures](_images/retry-limit-decision-journey.png)

The [Retry Limit Decision node](retry-limit-decision.html) Retry limit (default: 3) defines the number of failed attempts before lockout.

Before using a journey like this in deployment, adapt it to reset the retry count on successful authentication.

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

## Inputs

This node requires the `username` property in the incoming node state. It uses this information to access the account status in the user profile.

It also requires the `realm` property, which the product using this node sets by default.

## Dependencies

This node depends on the underlying identity service that stores the user profile.

## Configuration

| Property    | Usage                                                                           |
| ----------- | ------------------------------------------------------------------------------- |
| Lock Action | Choose whether to `LOCK` or `UNLOCK` the authenticating user's account profile. |

## Outputs

This node doesn't change the shared state.

## Outcomes

Single outcome path; the node updates the account status according to the configured Lock Action:

* `LOCK`

  The account is inactive and the user cannot authenticate.

* `UNLOCK`

  The account is active and the user can authenticate.

## Errors

If this node fails to set the account status, it logs a `failed to set the user status inactive` warning.

This node can also throw exceptions with the following messages:

| Message                                                                     | Notes                                                                               |
| --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `Could not get a valid username from the context`                           | Failed to read the `username` from the shared node state                            |
| `Could not get a valid realm from the context`                              | Failed to read the `realm` from the shared node state                               |
| `Could not find the identity based on the information available on context` | Failed to find the account profile with this `username` in this `realm`             |
| `An error occurred when trying to lock out the user account`                | Failed to update the account status; applies when locking and unlocking the account |

---

---
title: AD Decision node
description: Verifies user credentials against an Active Directory data store and routes journeys based on account status, including locked, disabled, or expired accounts.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref::ad-decision
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/ad-decision.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication", "Active Directory"]
section_ids:
  example: Example
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  outcomes: Outcomes
  ad-decision-disabled-locked-accounts: Locked and disabled accounts
  errors: Errors
---

# AD Decision node

The AD Decision node verifies that the provided username and password exist in the specified Active Directory data store. The node also checks whether the user account is locked, disabled, or has expired.

The node is similar to the [LDAP Decision node](ldap-decision.html) except for the following differences:

* It doesn't support the LDAP Behera password policy.

* It can return a specific outcome for an expired account in addition to an expired password.

* It makes a distinction between a [disabled account and a locked account](#ad-decision-disabled-locked-accounts).

## Example

The following example journey collects the user credentials and checks them against the AD data store:

* If they match, the journey continues to the success outcome.

* If the password has expired, the journey ends in failure with a custom message node to inform the user.

* If the account is locked, disabled, or has expired, the journey ends in failure with an invalid account message.

![Example journey showing AD Decision node](_images/ad-decision-node-aic.png)

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

## Inputs

The node reads the `username` and `password` fields from node state.

For standalone AM deployments, implement a [Username Collector node](am-only/username-collector.html) and a [Password Collector node](am-only/password-collector.html) earlier in the journey.

For Ping Identity Platform deployments, implement a [Platform Username node](platform-username.html) and a [Platform Password node](platform-password.html) earlier in the journey.

Alternatively, implement a [Zero Page Login Collector node](zero-page-login-collector.html).

## Dependencies

This node has no dependencies.

## Configuration

| Property                                                              | Usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Primary LDAP Server *(required)*                                      | Specify one or more primary directory servers. Specify each directory server in the following format: `host:port`.For example, `ad.example.com:389`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Secondary LDAP Server                                                 | Specify one or more secondary directory servers. Specify each directory server in the following format: `host:port`.The journey uses the secondary servers when none of the primary servers are available.For example, `ad_backup.example.com:389`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| DN to Start User Search *(required)*                                  | Specify the DN from which to start the user search. More specific DNs, such as `ou=sales,dc=example,dc=com`, result in better search performance.If multiple entries with the same attribute values exist in the directory server, make sure this property is specific enough to return only one entry.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Bind User DN, Bind User Password                                      | The credentials used to connect to the directory server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Attribute Used to Retrieve User Profile *(required)*                  | The attribute used to retrieve a user profile from the directory server.The user search will have already happened, as specified by the Attributes Used to Search for a User to be Authenticated and User Search Filter properties.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Attributes Used to Search for a User to be Authenticated *(required)* | The attributes the node uses to match the credentials provided by the user to an entry in the directory server.For example, a value of `uid` forms the search filter `uid=user`. If you specify multiple values, such as `uid` and `cn`, the node forms a complex search filter `(\|(uid=user)(cn=user))`.Multiple attribute values let the user authenticate with any one of the values. For example, if you set both `uid` and `mail`, then Barbara Jensen can authenticate with either `bjensen` or `bjensen@example.com`.&#xA;&#xA;If you're using account lockout and you set multiple attribute values here, you must add those attributes to the Alias Search Attribute Name property in the User profile. Find more information about this property in Core authentication attributes > User profile.                                                                                                                               |
| User Search Filter                                                    | A filter to append to user searches.For example, if your search attribute is `mail` and you set User Search Filter to `(objectClass=inetOrgPerson)`, the node uses `(&(mail=address)(objectClass=inetOrgPerson))` as the resulting search filter. In this example, *address* is the mail address provided by the user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Search Scope                                                          | The extent of the search for users in the directory server:- `OBJECT`: The search extends only to the entry specified by the DN to Start User Search.

- `ONELEVEL`: The search extends to the entries that are direct children of the DN to Start User Search.

- `SUBTREE`: The search extends to the DN to Start User Search and every entry under it.Default: `SUBTREE`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| LDAP Connection Mode                                                  | Whether to use SSL or StartTLS to connect to the directory server. The node must be able to trust the certificates used.Possible values: `LDAP`, `LDAPS`, and `StartTLS`Default: `LDAP`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| mTLS Enabled                                                          | Enables mTLS (mutual TLS) between AM and the directory server.This setting applies to *all* configured LDAP servers; that is, AM uses mTLS to authenticate to all LDAP servers configured for this node.When mTLS is enabled, AM ignores the values for Bind User DN and Bind User Password.If you enable this property, you must:- Set the LDAP Connection Mode to `LDAPS`

- Provide an mTLS Secret Label IdentifierLearn about mapping secrets in [Map and rotate secrets](https://docs.pingidentity.com/pingam/8.1/security/secret-mapping.html).Default: Not enabled                                                                                                                                                                                                                                                                                                                                                                   |
| mTLS Secret Label Identifier                                          | Identifier used to create a secret label for mapping to the mTLS certificate in the secret store. AM uses this identifier to create a specific secret label for this node. The secret label takes the form `am.authentication.nodes.ldap.decision.mtls.identifier.cert` , where `identifier` is the value of mTLS Secret Label Identifier. The identifier can only contain alphanumeric characters (`a-z`, `A-Z`, `0-9`) and periods (`.`). It can't start or end with a period. All LDAP servers configured for this node share the same secret label.For more security, you should rotate certificates periodically. When you rotate a certificate, update the corresponding mapping in the realm secret store configuration to reflect this label. When you rotate a certificate, AM closes any existing connections using the old certificate. A new connection is selected from the connection pool and no server restart is required. |
| Return Account Locked Message                                         | If enabled, the node returns a specific `Account locked` message for locked accounts. Otherwise, it returns a generic `Login failure` message to hide the account's locked status.Default: Not enabled                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Return User DN to DataStore                                           | When enabled, the node returns the DN rather than the User ID. From the DN value, AM uses the RDN to search for the user profile. For example, if a returned DN value is `uid=demo,ou=people,dc=example,dc=com`, AM uses `uid=demo` to search the directory server.Default: Enabled                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| User Creation Attributes                                              | This list lets you map (external) attribute names from the LDAP directory server to (internal) attribute names used by AM.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Minimum Password Length                                               | The minimum acceptable password length.Default: `8`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Trust All Server Certificates                                         | When enabled, the server blindly trusts server certificates, including self-signed test certificates.Default: Not enabled                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| LDAP Connection Heartbeat Interval                                    | Specifies how often AM should send a heartbeat request to the directory server to ensure that the connection doesn't remain idle.Some network administrators configure firewalls and load balancers to drop connections that are idle for too long. Set the units for the interval in the `LDAP Connection Heartbeat Time Unit` property.&#xA;&#xA;Setting this property to 0 does not disable the heartbeat (keepalive) or load balancer availability checks.&#xA;&#xA;You can only disable these features at the global level.Default: `10`                                                                                                                                                                                                                                                                                                                                                                                               |
| LDAP Connection Heartbeat Time Unit                                   | The time unit for the `LDAP Connection Heartbeat Interval`.Default: `seconds`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| LDAP Operations Timeout                                               | The timeout, in seconds, that AM should wait for a response from the directory server.Default: `0` (means no timeout)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Use mixed case for password change messages                           | Whether the server returns password reset messages in mixed case (sentence case) or transforms them to uppercase.By default, the server transforms password reset and password change messages to uppercase. Enable this setting to return messages in sentence case.Default: Not enabled                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| LDAP Affinity Level                                                   | Level of affinity used to balance requests across directory servers.Affinity-based load balancing means that each request for the same user entry goes to the same directory server. The directory server used for a specific operation is determined by the DN of the identity involved.List the directory server instances that form part of the affinity deployment in the Primary LDAP Server and Secondary LDAP Server properties.Options are:- `NONE` – no affinity

- `BIND` – affinity for BIND requests only

- `ALL` – affinity for all requestsDefault: `NONE`                                                                                                                                                                                                                                                                                                                                                                   |

## Outputs

If a password reset is required, the node adds a `lastModuleState` property with the value of `changeAfterReset` to shared state.

## Outcomes

* `True`

  The provided credentials match those found in the AD user data store.

* `False`

  The credentials don't match those found in the AD user data store.

* `Password Expired`

  The credentials are valid, but the password has expired. The journey doesn't automatically initiate a password reset.

* `Disabled`

  The credentials are valid, but the user account is [disabled](#ad-decision-disabled-locked-accounts).

* `Account Expired`

  The credentials are valid, but the user account has expired. This is different to the outcome where the *password* has expired.

* `Account Locked`

  The username is valid, but the user account is [locked](#ad-decision-disabled-locked-accounts)..

* `Cancelled`

  If the account requires a password reset, the journey prompts the user to change their password. The user then cancels the password reset.

### Locked and disabled accounts

In AD, a *locked account* is a temporary, automated security measure to protect against suspicious login activity, and it often resolves itself.

In contrast, a *disabled account* is a deliberate, long-term administrative action to revoke access, which the administrator must reverse manually.

| Feature    | Locked Account                                                          | Disabled Account                                                                  |
| ---------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Trigger    | Automatic system action, usually from too many failed login attempts.   | Manual action by an administrator or an automated de-provisioning process.        |
| Purpose    | A security measure to prevent brute-force password attacks.             | An administrative action to block access, often due to employment status changes. |
| Duration   | Temporary. It can unlock automatically after a set time.                | Permanent, until it is manually re-enabled.                                       |
| Resolution | The user can wait for the lockout to expire, or an admin can unlock it. | An administrator must manually re-enable the account.                             |

|   |                                                                                                                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The [Account Lockout node](account-lockout.html) performs an administrative account lockout, so be cautious when using this with the AD Decision node. If a user with such an account tries to authenticate, the AD Decision node interprets the account as disabled, not locked, which results in the `Disabled` outcome. |

## Errors

The node logs the following exceptions:

* `Invalid configuration`: If AD returns an unexpected result.

* `Server error`: If an error occurs connecting to AD.

* `Unknown login state`: If authentication results in an unknown state.

---

---
title: Agent Data Store Decision node
description: Authenticates agents such as PingGateway and Java or web agents against the agent profile data store in PingAM.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref::agent-data-store-decision
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/agent-data-store-decision.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Agents", "Password", "Data Store"]
page_aliases: ["auth-node-agent-data-store-decision.adoc"]
section_ids:
  example: Example
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  outcomes: Outcomes
  errors: Errors
---

# Agent Data Store Decision node

The Agent Data Store Decision node authenticates the agent using the data store for agent profiles and sets its authentication identifier if successful.

|   |                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This node only authenticates agents, such as PingGateway and the Java and web agents.Use the [Data Store Decision node](data-store-decision.html) for other identities. |

## Example

The following example uses this node to authenticate an agent with the credentials provided:

![Journey to authenticate an agent](_images/agent-journey.png)

* The [Zero Page Login Collector node](zero-page-login-collector.html) collects the username and password from HTTP headers if provided.

* The [Page node](page.html) collects the username and password interactively from the user.

* The Agent Data Store Decision node verifies the agent credentials match those in the data store.

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

## Inputs

This node requires the `username` and `password` properties in the incoming node state.

Obtain the agent credentials from the user or with a [Zero Page Login Collector node](zero-page-login-collector.html).

## Dependencies

This node depends on the underlying data store for agent profiles.

## Configuration

This node has no configurable properties.

## Outputs

This node copies the shared and transient states into the outgoing node state.

## Outcomes

* `True`

  The credentials match those found in the data store for agent profiles.

* `False`

  The credentials do *not* match those found in the data store for agent profiles.

## Errors

This node can log the following warnings:

* `Exception in data store decision node`

  The node couldn't connect to the data store, or another error occurred.

* `invalid password error`

  The password doesn't match.

* `invalid username error`

  The username doesn't match any profiles found in the data store.

---

---
title: Anonymous Session Upgrade node
description: Upgrades an anonymous session to a non-anonymous session in PingAM journeys.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref::anonymous-session-upgrade
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/anonymous-session-upgrade.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication", "Sessions"]
page_aliases: ["auth-node-anonymous-session-upgrade.adoc"]
section_ids:
  example: Example
  availability: Availability
  outcomes: Outcomes
  configuration: Configuration
---

# Anonymous Session Upgrade node

Upgrades an anonymous session to a non-anonymous session.

Use this as the first node in the flow.

## Example

After using the [Anonymous User Mapping node](anonymous-user-mapping.html) to access AM as an anonymous user, this node lets users upgrade their session to a non-anonymous one:

![Lets anonymous users upgrade their session](_images/trees-node-anonymous-session-upgrade-example-platform.png)

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

## Outcomes

Single outcome path.

## Configuration

This node has no configurable properties.

---

---
title: Anonymous User Mapping node
description: Maps unauthenticated users to a named anonymous account in PingAM, enabling limited access without credentials.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref::anonymous-user-mapping
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/anonymous-user-mapping.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication", "Accounts"]
page_aliases: ["auth-node-anonymous-user-mapping.adoc"]
section_ids:
  example: Example
  availability: Availability
  outcomes: Outcomes
  configuration: Configuration
---

# Anonymous User Mapping node

Lets users log in to an application or website without providing credentials, by assuming the identity of a specified existing user account. The default user for this purpose is named `anonymous`.

Take care to limit access for such users. For example, grant anonymous users access to public downloads on your site.

## Example

The following example uses this node to grant access as an anonymous user to users who have performed social authentication access and do not have an existing profile:

![Optionally authenticating as an anonymous user](_images/trees-node-anonymous-user-mapping-tree-example-platform.png)

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

## Outcomes

Single outcome path.

## Configuration

| Property            | Usage                                                                                                                                                  |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Anonymous User Name | Specifies the username of an account that represents anonymous users. This user must already exist in the realm, and its user status must be `active`. |

---

---
title: App Policy Decision node
description: Evaluates application access policies automatically from journey context in PingAM, routing based on accept, reject, or error outcomes.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref::app-policy-decision
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/app-policy-decision.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication"]
section_ids:
  example: Example
  prerequisites: Prerequisites
  example_journey: Example journey
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  callbacks: Callbacks
  outcomes: Outcomes
  errors: Errors
---

# App Policy Decision node

The App Policy Decision node is a specialized version of the [Policy Decision node](policy-decision.html) designed to simplify the evaluation of application access policies within a journey.

For example, use the node to restrict access based on user attributes, such as ensuring only end users in a specific finance group can access a finance portal.

You don't need to configure the node because it automatically identifies the policy set and resource from the journey context. However, the node assumes the following prerequisites:

* The node is used within an OAuth 2.0/OIDC or SAML application journey.

* The application ID (OAuth 2.0 client ID or SP entity ID) is specified as the resource when the journey is invoked.

* A policy with that resource is defined within the `Customer Application Policy Set`.

The outcome of the policy evaluation, to accept or reject access, map to the node's outcomes. It doesn't handle advices or environment conditions.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Consider the following security risks when designing journeys that include policy evaluation:- Brute force information disclosure

  An authenticated user can probe the policy framework by submitting different inputs to determine who or what passes or fails a policy evaluation.

  To prevent this, design journeys so that the policy framework isn't directly exposed to repeated probing. For example, block or lock out a session after a set number of failed attempts, just as you would for other authentication mechanisms.

- Denial of service (DoS)

  Unauthenticated users could repeatedly trigger policy evaluations, which can consume significant resources and increase the risk of a DoS attack.

  To reduce this risk: \* Protect the deployment at the container or network edge, for example, with a reverse proxy. \* Place the policy node after the user has authenticated whenever possible, to limit the attack surface.

  + This can also prevent information disclosure, such as exposing group membership based on submitted usernames. |

## Example

This example uses an App Policy Decision node to manage access to a finance portal application based on usernames.

### Prerequisites

The following setup is assumed:

* Standalone AM

* Ping Identity Platform deployments

- A test end user.

- An OAuth 2.0 provider service with default settings.

- A public OAuth 2.0 client, with the following settings:

  * Client ID

    `finance-app`

  * Scope(s)

    `openid`

  * Tree Name

    example journey

- A policy that allows access based on a username. It must be defined in the `Customer Application Policy Set`.

  * Resources

    `finance-app`

  * Actions

    `ACCESS:Allowed`

  * Subjects

    * Type

      `OpenID Connect/JWT Claim`

    * Claim Name

      `sub`

    * Claim Value

      username

    > **Collapse: Example policy**
    >
    > ![app policy decision ampolicy](_images/app-policy-decision-ampolicy.png)

  Learn about configuring policies in [Policies in the UI](https://docs.pingidentity.com/pingam/8.1/am-authorization/policies-ui.html).

* A test end user, added to the `Finance` group.

* An OIDC application, with the following settings:

  * Client ID

    `finance-app`

  * Use a journey to authenticate users to this application

    example journey

* A policy that allows access to an end user in the Finance group.

  * Resources

    `finance-app`

  * Actions

    `ACCESS:Allowed`

  * Subjects

    ```
    {
      "type": "NOT",
      "subject": {
        "type": "NONE"
      }
    }
    ```

  * Environments

    ```
    {
      "type": "OR",
      "conditions": [
        {
          "type": "IdmUser"
          "identityResource": "managed/alpha_user",
          "queryField": "/_id",
          "decisionField": "/effectiveGroups/*/_refResourceId",
          "comparator": "EQUALS",
          "value": "Finance"
         }
      ]
    }
    ```

> **Collapse: How to create this policy**
>
> 1. Go to Native Consoles > Access Management, go to Realms > *Realm Name* > Authorization > Policy Sets.
>
> 2. Click Customer Application Policy Set to add a policy.
>
>    You *must* use this policy set for app authorization.
>
> 3. Click + Add a Policy.
>
> 4. Provide a name and select Authentication as the resource type.
>
> 5. Select `*` as the resource pattern and add the client application ID, `finance-app`, as the resource.
>
> 6. Click Create.
>
> 7. Add an action of type `Access` and save your changes.
>
> 8. Add a subject condition of type `Never Match` in a `Not` logical block and save your changes.
>
> 9. Add an environmental condition:
>
>    1. Click Add an Environment Condition, select `IDM User`, and add the following values:
>
>       * Identity Resource
>
>         `managed/alpha_user`
>
>       * Query Field
>
>         `/_id`
>
>       * Decision Field
>
>         `/effectiveGroups/*/_refResourceId`
>
>       * Comparator
>
>         `Equal to`
>
>       * Value
>
>         `Finance`
>
>    2. Click the checkmark ([icon: check, set=fa]) button to finish.
>
>    3. Click Add a Logical Operator, select `Any of..`, and move the enviromment condition into the logical block.
>
>    4. Save your changes.
>
> Verify that the policy summary looks like this:
>
> ![app policy decision idmuserpolicy](_images/app-policy-decision-idmuserpolicy.png)
>
> Learn about configuring policies in [Policies in the UI](https://docs.pingidentity.com/pingam/8.1/am-authorization/policies-ui.html).

### Example journey

![Policy Decision node in an app authorization flow](_images/app-policy-decision-example.png)

* The authorization journey is invoked specifying the OAuth 2.0 client ID as the resource, for example:

  `https://am.example.com:8443/am/oauth2/alpha/authorize?client_id=finance-app&redirectUri=http://www.example.com/signin&scope=openid&response_type=code`

- The [Page node](page.html) containing the [Platform Username node](platform-username.html) and [Platform Password node](platform-password.html) prompts for credentials.

- The [Data Store Decision node](data-store-decision.html) validates the username-password credentials.

- A successful authentication routes the journey to the App Policy Decision node.

  The node has no configuration, but relies on the journey context and prerequisite configuration to identify the OAuth 2.0 client ID resource (`finance-app`). It can then locate the access policy to evaluate whether the end user is an authorized user for the finance app.

- The outcome of the policy evaluation determines the path of the journey:

  * Accept

    The policy grants access. The [Message node](message.html) informs the end user they're authorized and the journey is successful.

  * Reject

    The policy rejects access. The [Message node](message.html) informs the end user they're not authorized.

  * Error

    An error in policy evaluation leads to the failure outcome.

  * Unknown Resource

    The node failed to identify the resource and the journey continues to the [Set Error Details node](set-error-details.html).

## Inputs

If policy evaluation requires a subject, make sure the username is collected earlier in the journey.

## Dependencies

This node requires the following configuration:

* An application (OAuth 2.0 client or SAML SP entity) that uses a journey with an App Policy Decision node

* The `Customer Application Policy Set` must have a policy with the client or entity ID set as the resource.

## Configuration

This node has no configurable properties.

## Outputs

This node doesn't change the shared state.

## Callbacks

This node doesn't send any callbacks.

## Outcomes

* Accept

  Policy evaluation succeeded.

* Reject

  Policy evaluation didn't succeed.

* Error

  If an error occurs during policy evaluation.

* Unknown Resource

  If the node failed to identify the OAuth 2.0 or SAML 2.0 resource.

## Errors

The node logs an error if policy evaluation fails.

---

---
title: Attribute Collector node
description: Collects user attribute values during a journey for use in registration or profile update flows in PingAM.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref::attribute-collector
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/attribute-collector.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication", "Schema", "Policy", "Custom Attributes"]
page_aliases: ["auth-node-attribute-collector.adoc"]
section_ids:
  example: Example
  add_date_and_datetime_fields_to_a_journey: Add date and datetime fields to a journey
  date-formatting-policies: Apply formatting and policies
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  outcomes: Outcomes
  errors: Errors
---

# Attribute Collector node

The Attribute Collector node collects the values of attributes for use later in the flow; for example, to populate a new account during registration.

This node supports three types of attributes:\
`string`\
`boolean`\
`number`

To request a value, the attribute must be present and viewable in the identity schema for the current identity object.

The node lets you configure whether the attributes are required to continue and whether to use a policy filter of the underlying identity service (PingIDM) to validate them.

Use the node alone or within a [Page node](page.html).

## Example

|   |                                                                         |
| - | ----------------------------------------------------------------------- |
|   | These examples assume a self-managed Ping Identity Platform deployment. |

### Add date and datetime fields to a journey

The Attribute Collector node lets you add properties (attributes) that follow a date or datetime (date and time of day). The format of the date comes from the locale set in your browser.

The following table displays the differences between date and datetime:

| Display format | Managed object field format          | Notes                                                                                                                                                                                                                              |
| -------------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Date only      | String format                        | The format of the date comes from the locale set in your browser.For example, if the locale is English, then the format presented to the end user is `MM-DD-YYYY`. If the local is French, the format is `DD-MM-YYYY`.             |
| Date and time  | String format (date and time of day) | The format of the date comes from the locale set in your browser.For example, if the locale is English (United States), the format presented to the end user is `MM-DD-YYYY`. If the locale is French, the format is `DD-MM-YYYY`. |

|   |                                                                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The rendering of the date to the end user changes, depending on the locale set in the browser. However, the server *stores* the date value in UTC format as `YYYY-MM-DDHH:MM:SS`. For example, `2023-09-13T08:01:00Z`. |

To render the date or datetime UI element to an end user with the Attribute Collector node, you must do the following:

1. Specify the IDM property:

   * In the Ping Identity Platform admin UI, go to Configure > Managed Objects > *Select object*, for example, User.

   * Use an existing `string` property or create your own string property.

     Learn more in [Property Configuration Properties](https://docs.pingidentity.com/pingidm/8.1/objects-guide/appendix-managed-objects.html#managed-object-property-config-properties) in the IDM documentation.

2. Apply [formatting and policies](#date-formatting-policies) to the property in the IDM admin UI for `Date` or `Datetime`.

### Apply formatting and policies

1. In the IDM admin UI, go to Configure > Managed Objects > *object-type*, for example, User.

2. Select the property to use.

3. To select the format of the attribute, on the Details tab, click the Format field, and select one of the following:

   * For date property — `Date`

   * For datetime property — `Datetime`

4. Click Save.

5. On the Validation tab, click + Add Policy.

6. In the Policy Id field, enter one of the following:

   * For date property — `valid-formatted-date`

   * For datetime property — `valid-datetime`

   Find more information in [Apply policies to managed objects](https://docs.pingidentity.com/pingidm/8.1/objects-guide/configuring-default-policy.html).

7. Click Add.

8. In your journey, in the Attribute Collector node, add the property name to the Attributes to Collect field.

   For an in-depth use case, add the `date` or `datetime` property to an Attribute Collector node in a registration flow.

The following video shows an example of a journey collecting the datetime from an end user using the Attribute Collector node:

**Video (Video)**

<\_images/mp4/attribute-collector-datetime.mp4>

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes 1      |
| Ping Identity Platform (self-managed) | Yes        |

1 This functionality requires that you configure AM as part of a [Ping Identity Platform deployment](https://docs.pingidentity.com/platform/8.1/sample-setup/).

## Inputs

For validation, this node reads the Identity Attribute (default: `userName`) from the shared node state. It uses the value to look up the identity object.

It prompts the user for the attributes to collect.

## Dependencies

This node depends on the underlying identity service (PingIDM) to store the user profile and perform validation.

## Configuration

| Property                | Usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Attributes to Collect   | A list of the attributes to collect based on those in the identity schema (PingIDM schema) for the current identity object.Default: none                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| All Attributes Required | When enabled, all attributes collected in this node are required in order to continue.Default: false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Validate Input          | When enabled, validate the content against any policies specified in the identity schema (IDM schema) for each collected attribute.Learn more in [Use policies to validate data](https://docs.pingidentity.com/pingidm/8.1/objects-guide/policies.html#scripting-api-node-nodeState).If you enable this property, the collected identity attributes must be *User Editable*. To make an attribute user-editable in the IDM admin UI:1) Go to Configure > Managed Objects > *object-name*.

2) Click the pencil ([icon: pencil-alt, set=fa]) icon, then click Show advanced options.

3) Select the User Editable toggle.Learn more in [Property configuration properties](https://docs.pingidentity.com/pingidm/8.1/objects-guide/appendix-managed-objects.html#managed-object-property-config-properties).Default: false |
| Identity Attribute      | The attribute used to identify the managed object in the underlying identity service (PingIDM).Default: `userName`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## Outputs

The node writes the attributes and their values to the shared node state.

## Outcomes

Single outcome path; on success, downstream nodes can read the attributes from the shared node state.

## Errors

This node doesn't log any error or warning messages of its own.

---

---
title: Attribute Present Decision node
description: Checks whether a specified attribute, including private attributes such as password, is present on a user object in PingAM.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref::attribute-present-decision
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/attribute-present-decision.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication", "Account", "Custom Attributes", "Update Passwords"]
page_aliases: ["auth-node-attribute-present-decision.adoc"]
section_ids:
  example: Example
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  outcomes: Outcomes
  errors: Errors
---

# Attribute Present Decision node

The Attribute Present Decision node checks whether an attribute is present on an object, including private attributes. There is no need to specify the value of the attribute.

Use this node during an update password flow to check whether the local account has a password, for example.

This node is similar to the [Attribute Value Decision node](attribute-value-decision.html) when that node is set to use the `PRESENT` operator, except it can't return the value of the attribute, but can work with private attributes.

## Example

This journey to update a password uses the Attribute Present Decision node to check whether the account has a password:

![Checking whether an account has a password](_images/update-password-journey.png)

The user has already authenticated before beginning this journey:

* The [Get Session Data node](get-session-data.html) stores the `userName` from the session.

* The Attribute Present Decision node checks whether the user object has a password attribute.

* If so, the first [Page node](page.html) with the [Platform Password node](platform-password.html) prompts the user for the current password.

* Otherwise, the [Email Suspend node](email-suspend.html) sends an email to the user and suspends the flow until the user follows the link in the message.

* The [Data Store Decision node](data-store-decision.html) confirms the username-password credentials.

* The second [Page node](page.html) with the [Platform Password node](platform-password.html) prompts the user for the new password.

* The [Patch Object node](patch-object.html) updates the user object with the new password.

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes 1      |
| Ping Identity Platform (self-managed) | Yes        |

1 This functionality requires that you configure AM as part of a [Ping Identity Platform deployment](https://docs.pingidentity.com/platform/8.1/sample-setup/).

## Inputs

This node reads the Identity Attribute from the shared node state. If it can't read the Identity Attribute, it reads the `userName` from the shared node state.

It uses the value to look up the identity object.

## Dependencies

This node depends on the underlying identity service (PingIDM) to look up the user object.

## Configuration

| Property           | Usage                                                                                                                                                                                                                                                                                                                                                   |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Present Attribute  | The attribute whose presence you want to verify in the the underlying identity service (PingIDM) object. This can be an otherwise private attribute, such as `password`.&#xA;&#xA;This field is case-sensitive and must match the the underlying identity service (PingIDM) object attribute. For example, givenName, not givenname.Default: `password` |
| Identity Attribute | The attribute used to identify the managed object in the underlying identity service (PingIDM).Default: `userName`                                                                                                                                                                                                                                      |

## Outputs

This node doesn't change the shared state.

## Outcomes

* `True`

  The node found the attribute in the managed identity object.

* `False`

  Any other case.

## Errors

This node doesn't log any error or warning messages of its own.

---

---
title: Attribute Value Decision node
description: Verifies that a user attribute satisfies a configured condition, such as presence or equality, during journeys in PingAM.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref::attribute-value-decision
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/attribute-value-decision.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication", "Custom Attributes"]
page_aliases: ["auth-node-attribute-value-decision.adoc"]
section_ids:
  availability: Availability
  configuration: Configuration
---

# Attribute Value Decision node

Verifies that the specified attribute satisfies a specific condition.

Use this node to check whether an attribute's expected value is equal to a collected attribute value, or to validate that the specified attribute was collected.

Examples:

* To validate that a user provided the country attribute during registration, set the comparison operation to `PRESENT`, and the comparison attribute to `country`.

* To validate that the country attribute is set to the United States, set the comparison operation to `EQUALS`, the comparison attribute to `country`, and the comparison value to `United States`.

Use [Attribute Present Decision node](attribute-present-decision.html) instead when you need to check for the presence of a private attribute, such as `password`.

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes 1      |
| Ping Identity Platform (self-managed) | Yes        |

1 This functionality requires that you configure AM as part of a [Ping Identity Platform deployment](https://docs.pingidentity.com/platform/8.1/sample-setup/).

## Configuration

| Property             | Usage                                                                                                                                                                                                                       |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Comparison Operation | The operation to perform on the object attribute:- `PRESENT`

  Checks the existence of an attribute regardless of its value.

- `EQUALS`

  Checks if the object's attribute value equals the configured comparison value. |
| Comparison Attribute | The object attribute to compare.                                                                                                                                                                                            |
| Comparison Value     | When Comparison Operation is `EQUALS`, compare this value to the provided attribute value.                                                                                                                                  |
| Identity Attribute   | The attribute used to identify the managed object in the underlying identity service (PingIDM).                                                                                                                             |

---

---
title: Auth Level Decision node
description: Compares the current authentication level against a configured threshold to route journeys in PingAM.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref::auth-level-decision
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/auth-level-decision.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication"]
page_aliases: ["auth-node-auth-level-decision.adoc"]
section_ids:
  availability: Availability
  outcomes: Outcomes
  configuration: Configuration
---

# Auth Level Decision node

Compares the current authentication level value against a configured value.

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

## Outcomes

* `True`

* `False`

## Configuration

| Property                        | Usage                                                                                                                                                                                |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Sufficient Authentication Level | Evaluation continues along the `True` path if the current authentication level is equal to or greater than this integer; otherwise, the evaluation continues along the `False` path. |

---

---
title: Authentication node reference
description: Reference index of all PingAM authentication nodes, organized by category including MFA, federation, identity management, and utility nodes.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref::overview
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/overview.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  basic_authentication_nodes: Basic authentication nodes
  mfa_nodes: MFA nodes
  risk_management_nodes: Risk management nodes
  behavioral_nodes: Behavioral nodes
  contextual_nodes: Contextual nodes
  federation_nodes: Federation nodes
  identity_management_nodes: Identity management nodes
  utility_nodes: Utility nodes
  thing_nodes_pingamping_identity_platform: Thing nodes (PingAM/Ping Identity Platform)
  uncategorized_nodes: Uncategorized nodes
---

# Authentication node reference

## Basic authentication nodes

* [AD Decision node](ad-decision.html)

* [Data Store Decision node](data-store-decision.html)

* [Kerberos node](self-managed/kerberos.html)

* [LDAP Decision node](ldap-decision.html)

* [Password Collector node](am-only/password-collector.html)

* [Username Collector node](am-only/username-collector.html)

* [Zero Page Login Collector node](zero-page-login-collector.html)

* [Failure node](failure.html)

* [Success node](success.html)

## MFA nodes

* [Combined MFA Registration node](combined-mfa-registration.html)

* [Device Binding node](device-binding.html)

* [Device Binding Storage node](device-binding-storage.html)

* [Device Signing Verifier node](device-signing-verifier.html)

* [Enable Device Management node](enable-device-management.html)

* [Get Authenticator App node](get-authenticator-app.html)

* [HOTP Generator node](hotp-generator.html)

* [MFA Registration Options node](mfa-registration-options.html)

* [OATH Device Storage node](oath-device-storage.html)

* [OATH Registration node](oath-registration.html)

* [OATH Token Verifier node](oath-token-verifier.html)

* [Opt-out Multi-Factor Authentication node](opt-out-multi-factor.html)

* [OTP Collector Decision node](otp-collector-decision.html)

* [OTP Email Sender node](otp-email-sender.html)

* [OTP SMS Sender node](otp-sms-sender.html)

* [Push Registration node](push-registration.html)

* [Push Result Verifier node](push-result-verifier.html)

* [Push Sender node](push-sender.html)

* [Push Wait node](push-wait.html)

* [Recovery Code Collector Decision node](recovery-code-collector-decision.html)

* [Recovery Code Display node](recovery-code-display.html)

* [RSA SecurID node](rsa-securid.html)

* [WebAuthn Authentication node](webauthn-authentication.html)

* [WebAuthn Device Storage node](webauthn-device-storage.html)

* [WebAuthn Registration node](webauthn-registration.html)

## Risk management nodes

* [Account Active Decision node](account-active-decision.html)

* [Account Lockout node](account-lockout.html)

* [Auth Level Decision node](auth-level-decision.html)

* [CAPTCHA node](captcha.html)

* [reCAPTCHA Enterprise node](recaptcha-enterprise.html)

* [Legacy CAPTCHA node](legacy-captcha.html)

* [Modify Auth Level node](modify-auth-level.html)

* [PingOne Protect Evaluation node](pingone/pingone-protect-evaluation.html)

* [PingOne Protect Initialize node](pingone/pingone-protect-initialize.html)

* [PingOne Protect Result node](pingone/pingone-protect-result.html)

## Behavioral nodes

* [Increment Login Count node](increment-login-count.html)

* [Login Count Decision node](login-count-decision.html)

## Contextual nodes

* [Certificate Collector node](certificate-collector.html)

* [Certificate User Extractor node](certificate-user-extractor.html)

* [Certificate Validation node](certificate-validation.html)

* [Cookie Presence Decision node](cookie-presence-decision.html)

* [Device Geofencing node](device-geofencing.html)

* [Device Location Match node](device-location-match.html)

* [Device Match node](device-match.html)

* [Device Profile Collector node](device-profile-collector.html)

* [Device Profile Save node](device-profile-save.html)

* [Device Tampering Verification node](device-tampering-verification.html)

* [Persistent Cookie Decision node](persistent-cookie-decision.html)

* [Set Custom Cookie node](set-custom-cookie.html)

* [Set Persistent Cookie node](set-persistent-cookie.html)

## Federation nodes

* [OAuth 2.0 node (deprecated)](am-only/oauth2.html)

* [OpenID Connect node (deprecated)](am-only/oidc.html)

* [OIDC ID Token Validator node](oidc-idtoken-validator.html)

* [Provision Dynamic Account node](am-only/provision-dynamic-account.html)

* [Provision IDM Account node (deprecated)](am-only/provision-IDM-account.html)

* [SAML2 Authentication node](saml2.html)

* [Social Facebook node (deprecated)](am-only/social-facebook.html)

* [Social Google node (deprecated)](am-only/social-google.html)

* [Social Ignore Profile node (deprecated)](am-only/social-ignore-profile.html)

* [Social Provider Handler node](social-provider-handler.html)

* [Legacy Social Provider Handler node](legacy-social-provider-handler.html)

* [Write Federation Information node](write-federation-information.html)

## Identity management nodes

* [Accept Terms and Conditions node](accept-terms-and-conditions.html)

* [Attribute Collector node](attribute-collector.html)

* [Attribute Present Decision node](attribute-present-decision.html)

* [Attribute Value Decision node](attribute-value-decision.html)

* [Consent Collector node](consent-collector.html)

* [Create Object node](create-object.html)

* [Create Password node (deprecated)](am-only/create-password.html)

* [Display Username node](display-username.html)

* [Identify Existing User node](identify-existing-user.html)

* [KBA Decision node](kba-decision.html)

* [KBA Definition node](kba-definition.html)

* [KBA Verification node](kba-verification.html)

* [Pass-through Authentication node](passthrough-authentication.html)

* [Patch Object node](patch-object.html)

* [PingOne Create User node](pingone/pingone-create-user.html)

* [PingOne Delete User node](pingone/pingone-delete-user.html)

* [PingOne Identity Match node](pingone/pingone-identity-match.html)

* [PingOne Verify Completion Decision node](pingone/pingone-verify-completion-decision.html)

* [PingOne Verify Evaluation node](pingone/pingone-verify-evaluation.html)

* [Platform Password node](platform-password.html)

* [Platform Username node](platform-username.html)

* [Profile Completeness Decision node](profile-completeness-decision.html)

* [Query Filter Decision node](query-filter-decision.html)

* [Required Attributes Present node](required-attributes-present.html)

* [Select Identity Provider node](select-identity-provider.html)

* [Terms and Conditions Decision node](terms-and-conditions-decision.html)

* [Time Since Decision node](time-since-decision.html)

## Utility nodes

* [Agent Data Store Decision node](agent-data-store-decision.html)

* [Amster Jwt Decision node](am-only/amster-jwt-decision.html)

* [Anonymous Session Upgrade node](anonymous-session-upgrade.html)

* [Anonymous User Mapping node](anonymous-user-mapping.html)

* [Backchannel Initialize node](backchannel-initialize.html)

* [Backchannel Notification node](backchannel-notification.html)

* [Backchannel Status node](backchannel-status.html)

* [Choice Collector node](choice-collector.html)

* [Configuration Provider node](config-provider.html)

* [Email Suspend node](email-suspend.html)

* [Email Template node](email-template.html)

* [Failure URL node](failure-url.html)

* [Flow Control node](flow-control.html)

* [Get Session Data node](get-session-data.html)

* [Inner Tree Evaluator node](inner-tree-evaluator.html)

* [JWT Password Replay node](jwt-password-replay.html)

* [Message node](message.html)

* [Meter node](meter.html)

* [Page node](page.html)

* [Polling Wait node](polling-wait.html)

* [Query Parameter node](query-parameter.html)

* [Register Logout Webhook node](register-logout-webhook.html)

* [Remove Session Properties node](remove-session-properties.html)

* [Request Header node](request-header.html)

* [Retry Limit Decision node](retry-limit-decision.html)

* [Scripted Decision node](scripted-decision.html)

* [Set Error Details node](set-error-details.html)

* [Set Failure Details node](set-failure-details.html)

* [Set Logout Details node](set-logout-details.html)

* [Set Session Properties node](set-session-properties.html)

* [Set State node](set-state.html)

* [Set Success Details node](set-success-details.html)

* [State Metadata node](state-metadata.html)

* [Success URL node](success-url.html)

* [Timer Start node](timer-start.html)

* [Timer Stop node](timer-stop.html)

* [Update Journey Timeout node](update-journey-timeout.html)

## Thing nodes (PingAM/Ping Identity Platform)

* [Authenticate Thing node](self-managed/authenticate-thing.html)

* [Register Thing node](self-managed/register-thing.html)

## Uncategorized nodes

* [Debug node](am-only/debug.html)

* [App Policy Decision node](app-policy-decision.html)

* [Identity Assertion node](identity-assertion-node.html)

* [Policy Decision node](policy-decision.html)

* [RADIUS Challenge Collector node](radius-challenge-collector.html)

* [RADIUS Decision node](radius-decision.html)

---

---
title: Backchannel Initialize node
description: Configure the Backchannel Initialize node to start an asynchronous journey for a different user or agent, enabling backchannel authentication in PingAM.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref::backchannel-initialize
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/backchannel-initialize.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  example: Example
  main_journey: Main journey
  backchannel_authentication_journey: Backchannel authentication journey
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  outcomes: Outcomes
  errors: Errors
---

# Backchannel Initialize node

The Backchannel Initialize node lets you start a separate journey that runs asynchronously, possibly by a different user or agent. The node takes an incoming user ID and generates a URL to a journey where the identified user or agent authenticates.

Together with the [Backchannel Status node](backchannel-status.html), this node lets you implement *backchannel authentication* from within a journey. Find more information in [Backchannel authentication](https://docs.pingidentity.com/pingam/8.1/am-authentication/backchannel-authentication.html).

## Example

This example uses the Backchannel Initialize and Backchannel Status nodes to implement backchannel authentication.

The example shows two journeys:

* The main journey initializes a backchannel authentication journey.

* The backchannel journey is a simple authentication journey.

### Main journey

![backchannel nodes main journey](_images/backchannel-nodes-main-journey.png)

a The Collect User to Login node is a [Scripted Decision node](scripted-decision.html). The script writes the attributes required for the backchannel authentication into the shared state.

> **Collapse: Sample Scripted Decision node script**
>
> The script queries the backend identity object to get the `userId`, then writes that and the attributes required for the backchannel authentication into the shared state.
>
> ```bash
> if (callbacks.isEmpty()) {
>     // Request callbacks
>     callbacksBuilder.nameCallback("User to authenticate");
> } else {
>     // Callbacks returned from browser, save username and password
>     var username = callbacks.getNameCallbacks().get(0);
>     var queryRes = openidm.query("managed/alpha_user", {
>         "_queryFilter": `/userName eq '${username}'`
>     }, ["*", "_id"]);
>     var userId = queryRes.result[0]._id
>     var identity = idRepository.getIdentity(userId);
>     nodeState.putShared("backchannel-user", identity.getName());
>     nodeState.putShared("backchannel-data", {
>         "username": username,
>         "objectAttributes": {
>             "userName": username,
>             "_id": userId
>         }
>     });
>     nodeState.putShared("_id", userId);
>     outcome = "outcome";
> }
> ```

b The Backchannel Initialize node reads the value of the `backchannel-user` key from the shared state. This key contains the `userName`:

* If the `userName` is available and is valid, the node generates a redirect URI to start the backchannel authentication journey. The node writes the redirect URI and the transaction ID of the backchannel transaction to the shared state, and the journey proceeds to the Backchannel Status node.

* If the `userName` can't be read, the journey follows the Error outcome and fails.

* If the `userName` can be read but the user or agent isn't valid, the journey proceeds to a [Message node](message.html) (c) and redirects the user to the start of the journey to attempt gathering data again.

d The Backchannel Status node reads the transaction ID and provides status on the authentication request:

* If the backchannel authentication request is `Pending`, the journey proceeds to the Display Redirect URL Poll node (e), which is a [Configuration Provider node](config-provider.html).

* When the backchannel authentication is `In progress`, the journey proceeds to the In Progress Poll node (f), which is a [Polling Wait node](polling-wait.html).

* When the backchannel authentication completes successfully, the journey proceeds to the Display Tree Results node (g), which is a [Scripted Decision node](scripted-decision.html).

e The Configuration Provider node imitates a [Polling Wait node](polling-wait.html) that uses a script to display the backchannel redirect URI as long as the backchannel authentication request is in a `Pending` state.

> **Collapse: Sample Config Provider node script**
>
> ```bash
> var uri = nodeState.get("backchannel-redirectUri").asString();
> config = {
>     "spamDetectionTolerance": 3,
>     "spamDetectionEnabled": true,
>     "exitMessage": {},
>     "waitingMessage": {
>         "en": uri
>     },
>     "secondsToWait": 5,
>     "exitable": true
> };
> ```

* After 5 seconds, the journey returns to the Backchannel Status node.

* If the journey exits before it returns to the Backchannel Status node, the user is redirected to the start of the main journey to attempt gathering data again.

* If the Configuration Provider node detects spam or misconfiguration, the main journey follows the failure outcome path.

f The In Progress Poll node is a [Polling Wait node](polling-wait.html) that pauses the main journey until the Backchannel journey is complete.

* After 8 seconds, the journey returns to the Backchannel Status node.

* If the journey exits before it returns to the Backchannel Status node, the user is redirected to the start of the main journey to attempt gathering data again.

* If the node detects spam, the main journey follows the failure outcome path.

g The Display Tree Results node is a [Scripted Decision node](scripted-decision.html) that displays the outcome of the backchannel authentication journey.

> **Collapse: Sample Scripted Decision node script**
>
> ```bash
> /*
> - Data made available by nodes that have already executed are available in the sharedState variable.
> - The script should set outcome to either "true" or "false".
> */
> if (callbacks.isEmpty()) {
>     var sessionProperties = nodeState.get("backchannel-sessionProperties");
>     callbacksBuilder.textOutputCallback(0, sessionProperties);
> } else {
>     outcome = "outcome";
> }
> ```

|   |                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------- |
|   | This journey always ends on the [Failure node](failure.html) as it is not in itself an authentication journey. |

### Backchannel authentication journey

![backchannel nodes sub journey](_images/backchannel-nodes-sub-journey.png)

This is a basic authentication journey that takes credentials and authenticates the user based on their existence in the backend identity store.

a The Page node includes a [Display Username node](display-username.html) and a [Platform Password node](platform-password.html). The username has been supplied in the shared state from the main journey. The user needs to enter their password.

b Replace the Identity Store Decision node with a [Data Store Decision node](data-store-decision.html) to check the username and password.

The main journey polls for completion of this subjourney. When this journey completes, the main journey continues.

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

## Inputs

This node optionally reads the user ID of the *subject* the journey's being initialized for from the incoming node state. The user ID is stored in the `nodeState` key specified in the Subject Name Key property.

## Dependencies

This node has no dependencies.

## Configuration

| Property            | Usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Journey             | The asynchronous journey to initialize.Select a journey from the list of configured journeys.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Subject Type        | The type of subject to initialize the journey for:- User

  The subject is a user identity.

- Agent

  The subject is a web agent or Java agent.

- None

  Setting the Subject Type to `None` means any subject can log in using the initialized journey.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Subject Name Key    | The `nodeState` key that contains the user ID of the subject you're initializing the journey for.This property is ignored if the Subject Type is `None`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Data Object Key     | The node state key that contains the data object (if present) to pass to the journey at the root level of the shared state.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Redirect URL Type   | The type of redirect URL to save to node state:By default, the base URL of the redirect URI is retrieved from the incoming HTTP request.- Get

  The node redirects the user to a URL based on the base URL service. The redirect uses a GET request to the `/XUI/Login` endpoint.

- Post

  The node redirects the user to a URL based on the base URL service. The redirect uses a POST request to the `authenticate` endpoint.

- Custom

  The node redirects the user to the URL specified in the Custom Redirect URL field.

- None

  If none of the redirect URL mechanisms (`Get`, `Post`, or `Custom`) meet your business requirements, you can use the transaction ID stored in state to make your own redirect URL outside of the functionality of this node. Connect this output to a [Scripted Decision node](scripted-decision.html) to achieve this. |
| Custom Redirect URL | If Redirect URL Type is `Custom`, set this field to the custom redirect URL for the authentication journey.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Max Time (Seconds)  | The maximum number of seconds to wait for the backchannel journey to complete before timing out. This lets you set a specific timeout for each backchannel journey, depending on the expected completion time for the journey.	This value doesn't affect the authentication session timeout.If you don't set a value here, the backchannel journey times out after the Time to Live set for the realm.You can change this under Realms> *Realm Name* > Services > Transaction Authentication Service > Time to Live.                                                                                                                                                                                                                                                                                                                                                  |
| Allow Retry         | When enabled, the end user can retry the backchannel journey if it fails. There's no maximum *number* of retries, but the retry window ends after the configured `Max Time`.If you disable this option, the backchannel authentication token goes into the `Failure` state the first time the backchannel journey fails. In this case, calls to the [Backchannel Status node](backchannel-status.html) go to the Failure outcome.Default: Enabled                                                                                                                                                                                                                                                                                                                                                                                                                     |

## Outputs

The node writes the following to the shared state:

| Shared state key          | Information                                                                        |
| ------------------------- | ---------------------------------------------------------------------------------- |
| `backchannel-transaction` | The transaction ID of the backchannel authentication request.                      |
| `backchannel-redirectUri` | The generated redirect URI.                                                        |
| `backchannel-data`        | An optional data object with additional information about the authenticating user. |

## Outcomes

* `Created`

  The journey follows this outcome path if the node was able to create the backchannel authentication request.

* `Unknown Subject`

  The journey follows this outcome path if the subject in the incoming node state doesn't match an identity object in the backend identity store.

* `Error`

  The journey follows this outcome path if the node can't retrieve the subject from the node state.

## Errors

* If the node can't retrieve the subject from the incoming state, it logs the following warning:

  ```none
  Error retrieving subject from node state.
  ```

* If the node can't initialize the backchannel authentication journey, it logs the following error:

  ```none
  Error initializing back channel transaction.
  ```

---

---
title: Backchannel Notification node
description: Configure the Backchannel Notification node to send real-time status updates from a backchannel journey to the main authentication journey in PingAM.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref::backchannel-notification
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/backchannel-notification.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication", "Backchannel"]
section_ids:
  example: Example
  main_journey: Main journey
  backchannel_journey: Backchannel journey
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  callbacks: Callbacks
  outcomes: Outcomes
  errors: Errors
---

# Backchannel Notification node

The Backchannel Notification node adds data to the backchannel transaction from the backchannel journey, which the [Backchannel Status node](backchannel-status.html) can read. This lets you send real-time status updates to the main journey from the backchannel journey.

## Example

The following example shows how the Backchannel Notification node can be used in an out-of-band authentication journey to keep a help desk agent informed of progress while they're verifying a user's identity. The help desk agent can see real-time status updates when the user enters their password and when their credentials have been confirmed.

The example shows two journeys:

* The main journey initializes a backchannel authentication journey and displays status updates to the help desk agent.

* The backchannel journey is a simple authentication journey that adds status updates to the shared state and uses the Backchannel Notification node to add this data to the backchannel transaction.

### Main journey

![Example help desk agent journey](_images/backchannel-agent-help-desk-journey.png)

a The [Page node](page.html) with an [Attribute Collector node](attribute-collector.html) prompts the help desk agent for the end user's email address.

b The [Identify Existing User node](identify-existing-user.html) attempts to look up the username by matching the email address to the email address in an identity profile.

The lookup fails if no matching email address is found, or if more than one user profile uses the same email address.

c The Set Backchannel State Properties custom scripted node writes the `_id`, `objectAttributes`, and `username` to the shared state.

This example uses the following configuration:

* Attribute list to set

  `_id`\
  `objectAttributes`\
  `username`

* Backchannel nodeState property

  `backchannel:data`

> **Collapse: How do I create this custom scripted node?**
>
> The following steps provide the minimum configuration required to create this custom scripted node. Learn more in [custom scripted nodes](https://docs.pingidentity.com/pingam/8.1/am-authentication/node-designer.html).
>
> 1. In the AM admin UI, go to Realms > alpha > Authentication > Node Designer and click [icon: plus, set=fa]Create Node Type.
>
> 2. On the `New Node Type` page, enter the following details and click Create:
>
>    * Service Name
>
>      `setbackchannelstateproperties`
>
>    * Display Name
>
>      `Set Backchannel State Properties`
>
> 3. In the Outcomes field, enter `Next`.
>
> 4. In the Properties field, add the following JSON object to define the properties for this node:
>
>    ```json
>    {
>      "attributeListProperty": {
>        "title": "Attribute list to set",
>        "description": "List of attributes to include in the backchannel nodeState object",
>        "type": "STRING",
>        "required": true,
>        "multivalued": true
>      },
>      "backchannelStateProperty": {
>        "title": "Backchannel nodeState property",
>        "description": "Property name set in nodeState for the backchannel journey to consume",
>        "type": "STRING",
>        "required": true,
>        "defaultValue": "backchannel:data",
>        "multivalued": false
>      }
>    }
>    ```
>
> 5. In the Script field, add the following script to define the behavior of the node:
>
>    ```javascript
>    (function () {
>      logger.error(scriptName + "Node execution started");
>
>      //Get node properties
>      var nodeStateProperty = properties.backchannelStateProperty;
>      var attributeList = properties.attributeListProperty;
>
>      //Loop to get and set attributes into the nodeStateProperty nodeState variable
>      var out = {};
>      for (var i = 0; i < attributeList.length; i++) {
>        var k = attributeList[i];
>        var v = nodeState.get(k);
>        if (v !== null && v !== undefined) out[k] = v;
>      }
>      nodeState.putShared(nodeStateProperty, out);
>        logger.error(scriptName + "Node execution completed");
>      action.goTo("Next");
>    })();
>    ```
>
> 6. Enable the Error Outcome and click Save Changes to create the custom node.

d The [Backchannel Initialize node](backchannel-initialize.html) reads the `username` from the shared state.

* If the `username` is valid, the node generates a redirect URI to start the backchannel authentication journey. The node writes the redirect URI and the transaction ID of the backchannel transaction to the shared state, and the journey proceeds to the Backchannel Status node.

* If the `username` can't be read, the journey follows the Error outcome and fails.

e The [Backchannel Status node](backchannel-status.html) reads the transaction ID and provides status on the authentication request.

This example requires the following configuration:

* Record Transaction Data

  `Enabled`

* Transaction Data Key

  `transaction:data`

f The Pending Wait node is a [Polling Wait node](polling-wait.html) that pauses this journey when the backchannel authentication request has a status of `Pending`. After 3 seconds, the journey returns to the Backchannel Status node.

g The In Progress Wait node is a [Configuration Provider node](config-provider.html). It imitates a [Polling Wait node](polling-wait.html) and uses a script to display messages from the backchannel journey to the help desk agent when the backchannel authentication has a status of `In progress`.

> **Collapse: Sample Config Provider node script**
>
> ```javascript
> var message;
> var data = nodeState.get("transaction:data");
> //Make sure this property name matches the Transaction Data Key configured in the Backchannel Status node
> if (data) {
>     message = data["journeyStatus"];
> //Make sure this property name matches the Journey status property name configured in the Set Front Channel Status node.
> } else {
>     message = "Authentication in progress...";
> }
> config = {
>     "secondsToWait": 3,
>     "spamDetectionEnabled": false,
>     "spamDetectionTolerance": 3,
>     "waitingMessage": { "en": message },
>     "exitable": false,
>     "exitMessage": {}
> };
> ```

h The User Message To Display custom scripted node displays a message to the help desk agent when the backchannel authentication completes successfully.

This example uses the following configuration:

* Message to display

  `User successfully authenticated`

> **Collapse: How do I create this custom scripted node?**
>
> The following steps provide the minimum configuration required to create this custom scripted node. Learn more in [custom scripted nodes](https://docs.pingidentity.com/pingam/8.1/am-authentication/node-designer.html).
>
> 1. In the AM admin UI, go to Realms > alpha > Authentication > Node Designer and click [icon: plus, set=fa]Create Node Type.
>
> 2. On the `New Node Type` page, enter the following details and click Create:
>
>    * Service Name
>
>      `usermessagetodisplay`
>
>    * Display Name
>
>      `User Message to Display`
>
> 3. In the Outcomes field, enter `Success`.
>
> 4. In the Properties field, add the following JSON object to define the properties for this node:
>
>    ```json
>    {
>      "message": {
>        "title": "Message to display",
>        "description": "Message to display to the user",
>        "type": "STRING",
>        "required": true,
>        "multivalued": false
>      }
>    }
>    ```
>
> 5. In the Script field, add the following script to define the behavior of the node:
>
>    ```javascript
>    (function () {
>      logger.error(scriptName + "Node execution started");
>
>      if (callbacks.isEmpty()) {
>        var userMessage = properties.message;
>        callbacksBuilder.textOutputCallback(0, userMessage);
>      } else {
>        logger.error(scriptName + "Node execution completed");
>        action.goTo("Success");
>      }
>    })();
>    ```
>
> 6. Click Save Changes to create the custom node.

### Backchannel journey

This is a basic authentication journey that takes credentials and authenticates the user based on their existence in the backend identity store.

![Backchannel authentication journey with notifications](_images/backchannel-auth-notify-journey.png)

a The Page node includes a [Display Username node](display-username.html) and a [Platform Password node](platform-password.html). The username has been supplied in the shared state from the main journey. The user needs to enter their password.

b The Set Front Channel Status custom scripted node adds data to the shared state that the Backchannel Notification node can send to the main journey.

This example uses the following configuration:

* Journey status shared state key

  `transaction:notify`

* Journey status property name

  `journeyStatus`

* Journey status message

  `User has entered their credentials`

> **Collapse: How do I create this custom scripted node?**
>
> The following steps provide the minimum configuration required to create this custom scripted node. Learn more in [custom scripted nodes](https://docs.pingidentity.com/pingam/8.1/am-authentication/node-designer.html).
>
> 1. In the AM admin UI, go to Realms > alpha > Authentication > Node Designer and click [icon: plus, set=fa]Create Node Type.
>
> 2. On the `New Node Type` page, enter the following details and click Create:
>
>    * Service Name
>
>      `setfrontchannelstatus`
>
>    * Display Name
>
>      `Set Front Channel Status`
>
> 3. In the Outcomes field, enter `Success` and `Error`.
>
> 4. In the Properties field, add the following JSON object to define the properties for this node:
>
>    ```json
>    {
>      "journeyStatusKey": {
>        "title": "Journey status shared state key",
>        "description": "The shared state key where the message object will be stored (e.g. transaction:notify). This is the top-level key that will be updated in the journey state.",
>        "type": "STRING",
>        "required": true,
>        "defaultValue": "transaction:notify",
>        "multivalued": false
>      },
>      "journeyStatusProperty": {
>        "title": "Journey status property name",
>        "description": "The name of the property inside the shared state object (e.g. journeyStatus). This defines the field that will hold the message value.",
>        "type": "STRING",
>        "required": true,
>        "defaultValue": "journeyStatus",
>        "multivalued": false
>      },
>      "journeyStatusValue": {
>        "title": "Journey status message",
>        "description": "The message to store in shared state. This value will be used by downstream nodes (e.g. Backchannel Notification) to update the front-channel experience.",
>        "type": "STRING",
>        "required": true,
>        "defaultValue": "Example Front Channel Message",
>        "multivalued": false
>      }
>    }
>    ```
>
> 5. In the Script field, add the following script to define the behavior of the node:
>
>    ```javascript
>    /**
>     * Script to update sharedState with a key and object value retrieved from properties.value of the custom node
>     * This sharedState key/value is then used by the Backchannel Notification node to update the front channel state
>     * Example property values:
>     *   journeyStatusKey      = "transaction:notify"
>     *   journeyStatusProperty = "journeyStatus"
>     *   journeyStatusValue    = "Front Channel Message"
>     *
>     * sharedState Result:
>     *   ["transaction:notify"] = { journeyStatus: "Front Channel Message" }
>     */
>
>    var nodeOutcomes = {
>        SUCCESS: "Success",
>        ERROR: "Error"
>    };
>
>    (function () {
>        logger.error(scriptName + ": Node execution started");
>        try {
>            var stateKey = properties.journeyStatusKey;
>            var propertyName = properties.journeyStatusProperty;
>            var propertyValue = properties.journeyStatusValue;
>            var obj = {};
>            obj[propertyName] = propertyValue;
>            nodeState.putShared(stateKey, obj);
>            logger.error(scriptName + ": Node execution completed");
>            action.goTo(nodeOutcomes.SUCCESS);
>        } catch (e) {
>            logger.error(scriptName + ": Failed to update sharedState. Exception: " + e);
>            action.goTo(nodeOutcomes.ERROR);
>        }
>    })();
>    ```
>
> 6. Click Save Changes to create the custom node.

c The Backchannel Notification node reads the shared state and sends a status update to the main journey to inform the help desk agent that the user has entered their credentials.

d The [Data Store Decision node](data-store-decision.html) validates the username-password credentials.

e The Set Front Channel Status custom scripted node adds data to the shared state that the Backchannel Notification node can send to the main journey. This is the custom scripted node you created earlier in this example.

This instance of the node uses the following configuration:

* Journey status shared state key

  `transaction:notify`

* Journey status property name

  `journeyStatus`

* Journey status message

  `User's credentials are valid`

f The Backchannel Notification node reads the shared state and sends a status update to the main journey to inform the help desk agent that the user's credentials match those stored in the data store.

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

## Inputs

This node reads data from the incoming node state using the key specified in the Data Key. The key value must be a JSON object.

Implement a node earlier in the journey to add data to the incoming node state using this key. For example, you could use [custom scripted nodes](https://docs.pingidentity.com/pingam/8.1/am-authentication/node-designer.html) or a [Scripted Decision node](scripted-decision.html).

## Dependencies

This node has no dependencies.

## Configuration

| Property | Usage                                                                                                                                                                                    |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Data Key | The shared state key that contains the data you want to add to the backchannel transaction. For example `transaction:notify`.This key is used to read data from the incoming node state. |

## Outputs

This node doesn't change the shared state.

## Callbacks

This node doesn't send any callbacks.

## Outcomes

* Success

  The backchannel notification was successfully sent.

* Error

  An error occurred when sending the backchannel notification.

## Errors

The node can log the following errors:

* `Failed to update backchannel transaction`

  An error occurred when the node attempted to update the backchannel transaction with the data from the incoming node state.

The node can log the following warnings:

* `Transaction ID not found in context`

  The transaction ID is missing from the incoming request context.

* `Data in state at dataKey data key was not found or incorrect type, not updating transaction.`

  The Data Key configured for the node doesn't exist in the incoming node state, or it exists but contains invalid data.

---

---
title: Backchannel Status node
description: Configure the Backchannel Status node to check the status of an asynchronous backchannel authentication journey in PingAM.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref::backchannel-status
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/backchannel-status.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  example: Example
  main_journey: Main journey
  backchannel_authentication_journey: Backchannel authentication journey
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  outcomes: Outcomes
  errors: Errors
---

# Backchannel Status node

The Backchannel Status node checks the status of an asynchronous (backchannel) user journey.

Together with the [Backchannel Initialize node](backchannel-initialize.html), this node lets you implement *backchannel authentication* from within a journey. Find more information in [Backchannel authentication](https://docs.pingidentity.com/pingam/8.1/am-authentication/backchannel-authentication.html).

## Example

This example uses the Backchannel Initialize and Backchannel Status nodes to implement backchannel authentication.

The example shows two journeys:

* The main journey initializes a backchannel authentication journey.

* The backchannel journey is a simple authentication journey.

### Main journey

![backchannel nodes main journey](_images/backchannel-nodes-main-journey.png)

a The Collect User to Login node is a [Scripted Decision node](scripted-decision.html). The script writes the attributes required for the backchannel authentication into the shared state.

> **Collapse: Sample Scripted Decision node script**
>
> The script queries the backend identity object to get the `userId`, then writes that and the attributes required for the backchannel authentication into the shared state.
>
> ```bash
> if (callbacks.isEmpty()) {
>     // Request callbacks
>     callbacksBuilder.nameCallback("User to authenticate");
> } else {
>     // Callbacks returned from browser, save username and password
>     var username = callbacks.getNameCallbacks().get(0);
>     var queryRes = openidm.query("managed/alpha_user", {
>         "_queryFilter": `/userName eq '${username}'`
>     }, ["*", "_id"]);
>     var userId = queryRes.result[0]._id
>     var identity = idRepository.getIdentity(userId);
>     nodeState.putShared("backchannel-user", identity.getName());
>     nodeState.putShared("backchannel-data", {
>         "username": username,
>         "objectAttributes": {
>             "userName": username,
>             "_id": userId
>         }
>     });
>     nodeState.putShared("_id", userId);
>     outcome = "outcome";
> }
> ```

b The Backchannel Initialize node reads the value of the `backchannel-user` key from the shared state. This key contains the `userName`:

* If the `userName` is available and is valid, the node generates a redirect URI to start the backchannel authentication journey. The node writes the redirect URI and the transaction ID of the backchannel transaction to the shared state, and the journey proceeds to the Backchannel Status node.

* If the `userName` can't be read, the journey follows the Error outcome and fails.

* If the `userName` can be read but the user or agent isn't valid, the journey proceeds to a [Message node](message.html) (c) and redirects the user to the start of the journey to attempt gathering data again.

d The Backchannel Status node reads the transaction ID and provides status on the authentication request:

* If the backchannel authentication request is `Pending`, the journey proceeds to the Display Redirect URL Poll node (e), which is a [Configuration Provider node](config-provider.html).

* When the backchannel authentication is `In progress`, the journey proceeds to the In Progress Poll node (f), which is a [Polling Wait node](polling-wait.html).

* When the backchannel authentication completes successfully, the journey proceeds to the Display Tree Results node (g), which is a [Scripted Decision node](scripted-decision.html).

e The Configuration Provider node imitates a [Polling Wait node](polling-wait.html) that uses a script to display the backchannel redirect URI as long as the backchannel authentication request is in a `Pending` state.

> **Collapse: Sample Config Provider node script**
>
> ```bash
> var uri = nodeState.get("backchannel-redirectUri").asString();
> config = {
>     "spamDetectionTolerance": 3,
>     "spamDetectionEnabled": true,
>     "exitMessage": {},
>     "waitingMessage": {
>         "en": uri
>     },
>     "secondsToWait": 5,
>     "exitable": true
> };
> ```

* After 5 seconds, the journey returns to the Backchannel Status node.

* If the journey exits before it returns to the Backchannel Status node, the user is redirected to the start of the main journey to attempt gathering data again.

* If the Configuration Provider node detects spam or misconfiguration, the main journey follows the failure outcome path.

f The In Progress Poll node is a [Polling Wait node](polling-wait.html) that pauses the main journey until the Backchannel journey is complete.

* After 8 seconds, the journey returns to the Backchannel Status node.

* If the journey exits before it returns to the Backchannel Status node, the user is redirected to the start of the main journey to attempt gathering data again.

* If the node detects spam, the main journey follows the failure outcome path.

g The Display Tree Results node is a [Scripted Decision node](scripted-decision.html) that displays the outcome of the backchannel authentication journey.

> **Collapse: Sample Scripted Decision node script**
>
> ```bash
> /*
> - Data made available by nodes that have already executed are available in the sharedState variable.
> - The script should set outcome to either "true" or "false".
> */
> if (callbacks.isEmpty()) {
>     var sessionProperties = nodeState.get("backchannel-sessionProperties");
>     callbacksBuilder.textOutputCallback(0, sessionProperties);
> } else {
>     outcome = "outcome";
> }
> ```

|   |                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------- |
|   | This journey always ends on the [Failure node](failure.html) as it is not in itself an authentication journey. |

### Backchannel authentication journey

![backchannel nodes sub journey](_images/backchannel-nodes-sub-journey.png)

This is a basic authentication journey that takes credentials and authenticates the user based on their existence in the backend identity store.

a The Page node includes a [Display Username node](display-username.html) and a [Platform Password node](platform-password.html). The username has been supplied in the shared state from the main journey. The user needs to enter their password.

b Replace the Identity Store Decision node with a [Data Store Decision node](data-store-decision.html) to check the username and password.

The main journey polls for completion of this subjourney. When this journey completes, the main journey continues.

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

## Inputs

This node requires the transaction ID of the backchannel authentication request from the node state. Implement a [Backchannel Initialize node](backchannel-initialize.html) before this node in the journey to provide this input.

## Dependencies

This node has no dependencies.

## Configuration

| Property                    | Usage                                                                                                                                                                                                                                    |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Record Journey Session Info | When enabled, the node records the session information returned from the journey in the transient state when the journey completes successfully.                                                                                         |
| Record Transaction Data     | When enabled, the node writes the transaction data received from the [Backchannel Notification node](backchannel-notification.html) to the shared state for the following transaction states:- `PENDING`

- `IN_PROGRESS`

- `COMPLETED` |
| Transaction Data Key        | The key used to record the transaction data in shared state when Record Transaction Data is enabled. For example `transaction:data`.Leave blank to use the default `backchannel-transactionData` key.                                    |

## Outputs

* If Record Journey Session Info is enabled, the node writes the journey session properties to the transient state in the `backchannel-sessionProperties` key.

* If Record Transaction Data is enabled, the node writes transaction data to the shared state in the key specified in Transaction Data Key. If no key is specified, data is written to the default `backchannel-transactionData` key.

  This data includes anything added to the transaction by the [Backchannel Notification node](backchannel-notification.html) for real-time updates.

## Outcomes

* Pending

  The journey follows this outcome if the backchannel authentication journey has not yet started.

* In Progress

  The journey follows this outcome if the backchannel authentication journey has been started but not yet completed.

* Success

  The journey follows this outcome if the backchannel authentication journey has completed successfully.

* Failure

  The journey follows this outcome if the backchannel authentication journey completed but failed.

* Unknown

  The journey follows this outcome if the node is unable to assess the status of the backchannel authentication journey, usually because it timed out.

* Error

  The journey follows this outcome in any other case.

## Errors

If the node is unable to assess the status of the backchannel authentication journey, it writes the following error to the log:

```none
Error checking back channel transaction status.
```

---

---
title: CAPTCHA node
description: Configure the CAPTCHA node to verify CAPTCHA responses from providers such as Google reCAPTCHA v2, reCAPTCHA v3, and hCaptcha during PingAM authentication journeys.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref::captcha
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/captcha.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication", "CAPTCHA"]
page_aliases: ["auth-node-captcha.adoc"]
section_ids:
  example: Example
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  outcomes: Outcomes
  errors: Errors
---

# CAPTCHA node

The CAPTCHA node adds CAPTCHA support by verifying the response token received from the CAPTCHA provider and creating a callback for the UI to interact with.

By default, the node is configured for Google's reCAPTCHA v2.

## Example

The following journey uses a [Page node](page.html) and a [Data Store Decision node](data-store-decision.html) to collect and verify the credentials and a CAPTCHA response:

![The CAPTCHA node in context](_images/trees-node-captcha-example-platform.png)

This example uses the following nodes:

* The [Page node](page.html) prompts the user to input their username and password:

  * The [Platform Username node](platform-username.html) collects the username and stores it in the shared state.

  * The [Platform Password node](platform-password.html) collects the password and stores it in the shared state.

  * The [CAPTCHA node](captcha.html) collects and verifies the CAPTCHA response.

* The [Data Store Decision node](data-store-decision.html) uses the username and password to determine whether authentication is successful.

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

|   |                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * This node only supports reCAPTCHA v2 and v3, and hCaptcha.

  For Google reCAPTCHA Enterprise support, use the [reCAPTCHA Enterprise node](recaptcha-enterprise.html).

* This node doesn't support hCaptcha's [passive or invisible mode](https://docs.hcaptcha.com/invisible). |

## Inputs

None. This node doesn't read shared state data.

## Dependencies

You need to sign up for access to the [reCAPTCHA API](https://www.google.com/recaptcha/admin/create) to get the API key pair required for configuring the node.

## Configuration

| Property                          | Usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CAPTCHA Site Key *(required)*     | The CAPTCHA site key supplied by the CAPTCHA provider when you sign up for access to the API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| CAPTCHA Secret Key                | The CAPTCHA secret key supplied by the CAPTCHA provider when you sign up for access to the API.&#xA;&#xA;This property is deprecated and will be removed in a future release. Use the CAPTCHA Secret Label Identifier instead.&#xA;&#xA;If you set a CAPTCHA Secret Label Identifier and the product using this node finds a matching secret in a secret store, the CAPTCHA Secret Key is ignored.                                                                                                                                                                                                                                                                                                                                                  |
| CAPTCHA Secret Label Identifier   | An identifier used to create a *secret label* for mapping to a secret in a secret store.The product using this node uses this identifier to create a specific secret label for this node. The secret label takes the form `am.authentication.nodes.captcha.identifier.secret` where identifier is the value of CAPTCHA Secret Label Identifier.The identifier can only contain alphanumeric characters `a-z`, `A-Z`, `0-9`, and periods (`.`). It can't start or end with a period.If you set a CAPTCHA Secret Label Identifier and the product using this node finds a matching secret in a secret store, the CAPTCHA Secret Key is ignored.                                                                                                       |
| CAPTCHA Verification URL          | The URL used to verify the CAPTCHA submission.Possible values are:- Google: `https://www.google.com/recaptcha/api/siteverify`

- hCaptcha: `https://hcaptcha.com/siteverify`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| CAPTCHA API URL *(required)*      | The URL of the JavaScript that loads the CAPTCHA widget.Possible values are:- Google: `https://www.google.com/recaptcha/api.js`

- hCaptcha: `https://hcaptcha.com/1/api.js`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Class of CAPTCHA HTML Element     | The class of the HTML element required by the CAPTCHA widget.Possible values are:- Google: `g-recaptcha`

- hCaptcha: `h-captcha`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ReCaptcha V3 node                 | If you're using Google reCAPTCHA, specify whether it's v2 or v3. Turn on for v3.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Score Threshold                   | If you're using Google reCAPTCHA v3, or hCaptcha, enter a score threshold.The CAPTCHA provider returns a score for each user request, based on observed interaction with your site. CAPTCHA "learns" by observing real site traffic, so scores in a staging environment or in a production deployment that has just been implemented might not be very accurate.A score of 1.0 is likely a good user interaction, while 0.0 is likely to be a bot.The threshold you set here determines whether to allow or deny access, based on the score returned by the CAPTCHA provider.Start with a threshold of 0.5.Learn more about score thresholds in the [Google documentation](https://developers.google.com/recaptcha/docs/v3#interpreting_the_score). |
| Disable submission until verified | If selected, form submission is disabled until CAPTCHA verification succeeds.Default: Enabled                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## Outputs

This node doesn't change the shared state.

## Outcomes

* `True`

  The CAPTCHA response was successfully verified.

* `False`

  The CAPTCHA response wasn't verified or failed verification.

## Errors

This node can throw exceptions with the following messages:

* `CAPTCHA response required for verification`

* `Unable to verify CAPTCHA response`

* `Unable to retrieve state from token response`

* `No secret key found`

---

---
title: Certificate Collector node
description: Configure the Certificate Collector node to collect X.509 digital certificates from incoming requests for use as authentication credentials in PingAM journeys.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref::certificate-collector
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/certificate-collector.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication", "Certificates"]
page_aliases: ["self-managed/auth-node-certificate-collector.adoc"]
section_ids:
  example: Example
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  callbacks: Callbacks
  outcomes: Outcomes
  errors: Errors
---

# Certificate Collector node

The Certificate Collector node collects an X.509 digital certificate or a chain of certificates from the incoming request. The journey can then use the collected certificates as authentication credentials for a user or an OAuth 2.0 client.

By default, AM collects the chain of certificates. Set the `am.nodes.certificatechain.validation.enforced` [advanced server property](https://docs.pingidentity.com/pingam/8.1/setup/server-advanced.html#am.nodes.certificatechain.validation.enforced) to `false` to collect only the *first* certificate in a certificate chain (the user certificate).

AM accepts certificates in PEM and DER format.

|   |                                                                                                                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can't use this node in isolation because it only *collects* certificates from the request. It doesn't extract or validate the certificate's content. Use a [Certificate Validation node](certificate-validation.html) to validate certificates and a [Certificate User Extractor node](certificate-user-extractor.html) to extract the user details from the certificate. |

## Example

This example shows an authentication journey using a certificate as credentials.

![journey certificate auth](_images/journey-certificate-auth.png)

1. The Certificate Collector node attempts to collect the certificate from the request body or the header.

   * If the node can collect the certificate, the journey proceeds to the [Certificate Validation node](certificate-validation.html).

   * If the node can't collect the certificate, the journey proceeds to a [Page node](page.html) containing a [Platform Username node](platform-username.html) and a [Platform Password node](platform-password.html) to let the user authenticate with username/password credentials.

2. The Certificate Validation node attempts to validate the certificate based on the configuration of that node.

   * If the certificate can be validated, the journey proceeds to the [Certificate User Extractor node](certificate-user-extractor.html).

   * If the certificate is invalid, the journey proceeds to the Failure node.

   * In all other cases, the journey proceeds to a [Page node](page.html) containing a [Platform Username node](platform-username.html) and a [Platform Password node](platform-password.html) to let the user authenticate with username/password credentials.

3. The Certificate User Extractor node extracts the user ID from the certificate and attempts to find a match in the identity store.

   * If the username can be extracted and a matching user is found in the identity store, the journey increments the login count and authenticates the user.

   * If the username can't be extracted or no matching user is found in the identity store, the journey proceeds to the Failure node.

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

## Inputs

This node reads the certificate or chain of certificates from the request payload or request header. It doesn't read anything from the shared state.

## Dependencies

This node has no dependencies.

## Configuration

| Property                                    | Usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Certificate Collection Method               | How the node should collect the certificate or chain of certificates from the request. Possible values are:- `Request`

  The node locates the certificates in the request. Use this option if TLS termination happens at AM.

- `Header`

  The node locates the certificates in an HTTP header. Specify the header name in the HTTP Header Name for the Client Certificate property. Use this option if TLS termination happens in a proxy or load balancer outside AM.

- `Either`

  The node attempts to locate the certificates in the request. If there are no certificates in the request, the node attempts to locate the certificates in the HTTP header specified in HTTP Header Name for the Client Certificate.Default: `Either` |
| HTTP Header Name for the Client Certificate | The name of the HTTP header that contains the certificates. If you set the Certificate Collection Method to `Header` or `Either`, you must set a value here.Default: No value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Trusted Remote Hosts                        | A list of IP addresses trusted to supply certificates on behalf of the authenticating client, such as load balancers doing TLS termination.If you don't set a value here, AM rejects certificates supplied by remote hosts. If you set a value of `any`, AM trusts certificates supplied by any remote host, on behalf of the authenticating client.Default: No value                                                                                                                                                                                                                                                                                                                                                                         |

## Outputs

The node outputs the X.509 certificate or chain of certificates to the transient state to be consumed by the [Certificate Validation node](certificate-validation.html).

## Callbacks

This node doesn't send any callbacks.

## Outcomes

* `Collected`

  The node was able to collect the certificates.

* `Not Collected`

  The node was unable to collect the certificates.

## Errors

* If no certificates are provided in the configured location (either header or request), the node logs the following error:

  `Certificate was not successfully collected based on node configuration and client request`

* If there's a problem with the certificates provided in the header or in the request, the node logs the following error:

  `CertificateFromParameter decode failed, possibly invalid Base64 input`

---

---
title: Certificate User Extractor node
description: Configure the Certificate User Extractor node to extract a user identifier from an X.509 certificate and match it against an identity in the identity store.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref::certificate-user-extractor
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/certificate-user-extractor.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication", "Certificates", "Identity Store", "Users", "User Profiles"]
page_aliases: ["self-managed/auth-node-certificate-user-extractor.adoc"]
section_ids:
  example: Example
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  callbacks: Callbacks
  outcomes: Outcomes
  errors: Errors
---

# Certificate User Extractor node

The Certificate User Extractor node extracts an identifier from the certificate collected by the [Certificate Collector node](certificate-collector.html) and searches for that identifier in the identity store. The purpose of this node is to match the collected certificate with a user in the identity store.

## Example

This example shows an authentication journey using a certificate as credentials.

![journey certificate auth](_images/journey-certificate-auth.png)

1. The Certificate Collector node attempts to collect the certificate from the request body or the header.

   * If the node can collect the certificate, the journey proceeds to the [Certificate Validation node](certificate-validation.html).

   * If the node can't collect the certificate, the journey proceeds to a [Page node](page.html) containing a [Platform Username node](platform-username.html) and a [Platform Password node](platform-password.html) to let the user authenticate with username/password credentials.

2. The Certificate Validation node attempts to validate the certificate based on the configuration of that node.

   * If the certificate can be validated, the journey proceeds to the [Certificate User Extractor node](certificate-user-extractor.html).

   * If the certificate is invalid, the journey proceeds to the Failure node.

   * In all other cases, the journey proceeds to a [Page node](page.html) containing a [Platform Username node](platform-username.html) and a [Platform Password node](platform-password.html) to let the user authenticate with username/password credentials.

3. The Certificate User Extractor node extracts the user ID from the certificate and attempts to find a match in the identity store.

   * If the username can be extracted and a matching user is found in the identity store, the journey increments the login count and authenticates the user.

   * If the username can't be extracted or no matching user is found in the identity store, the journey proceeds to the Failure node.

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

## Inputs

This node reads the value of the `X509Certificate` property from the transient state.

Implement the [Certificate Collector node](certificate-collector.html) as input to this node to obtain the `X509Certificate`.

## Dependencies

This node has no dependencies.

## Configuration

| Property                                            | Usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Certificate Field Used to Access User Profile       | Specifies the field in the certificate that AM uses to search for the user in the identity store. Possible values are:- `Subject DN`

- `Subject CN`

- `Subject UID`

- `Email Address`

- `Other`

- `None`If you select `Other`, provide an attribute name in the Other Certificate Field Used to Access User Profile property.Select `None` if you want to specify an alternate way of looking up the user profile in the SubjectAltNameExt Value Type to Access User Profile property.Default: `Subject CN` |
| Other Certificate Field Used to Access User Profile | Specifies a custom certificate field to use as the base of the user search.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| SubjectAltNameExt Value Type to Access User Profile | Specifies how to look up the user profile:- `None`

  AM uses the value specified in the Certificate Field Used to Access User Profile or the Other Certificate Field Used to Access User Profile properties when looking up the user profile.

- `RFC822Name`

  AM looks up the user profile using the value of the `RFC822Name` field.

- `UPN`

  AM looks up the user profile as the User Principal Name attribute used in Active Directory.Default: `None`                                                 |

## Outputs

If the node can extract a value from the certificate, that value is stored in the `username` key in the shared node state.

## Callbacks

This node doesn't send any callbacks.

## Outcomes

* `Extracted`

  The node extracted the user ID from the certificate and found a match in the identity store.

* `Not Extracted`

  The node couldn't extract the user ID from the certificate or couldn't match the ID to an identity in the identity store.

## Errors

If the node can't extract the user ID from the certificate, it logs the following error:

`Unable to parse user token ID from Certificate`

---

---
title: Certificate Validation node
description: Configure the Certificate Validation node to validate X.509 digital certificates against LDAP stores, CRLs, and OCSP in PingAM authentication journeys.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref::certificate-validation
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/certificate-validation.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication", "Certificates", "LDAP", "TLS/SSL"]
page_aliases: ["self-managed/certificate-validation.adoc"]
section_ids:
  example: Example
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  callbacks: Callbacks
  outcomes: Outcomes
  errors: Errors
---

# Certificate Validation node

The Certificate Validation node validates the X.509 digital certificate or chain of certificates collected by the [Certificate Collector node](certificate-collector.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | **Certificate validation rules**- If you add this node to a journey, you *must* configure it. With no configuration, the node returns `True` as the outcome by default, regardless of the validity of the certificate provided in the journey.

- This node validates all certificates in a certificate chain by default. Make sure all intermediate and root certificates from the chain are present in the truststore.

  If any intermediate or root certificates are missing from the truststore, certificate validation fails.

  To validate only the *first* certificate in a certificate chain (the user certificate) and ignore the remaining certificates in the chain, set the `am.nodes.certificatechain.validation.enforced` [advanced server property](https://docs.pingidentity.com/pingam/8.1/setup/server-advanced.html#am.nodes.certificatechain.validation.enforced) to `false`.

- If the collected user certificate is a self-signed certificate (test environments only), the self-signed user certificate must be present in the truststore for certificate validation to succeed.

- If the collected user certificate is signed by a valid issuer, the issuing certificates (intermediate, or intermediate and root) must be present in the truststore for certificate validation to succeed.

  If the issuing certificates are missing from the truststore, certificate validation fails.

- The node uses the intermediate and user certificates to verify certificate revocation status. |

## Example

This example shows an authentication journey using a certificate as credentials.

![journey certificate auth](_images/journey-certificate-auth.png)

1. The Certificate Collector node attempts to collect the certificate from the request body or the header.

   * If the node can collect the certificate, the journey proceeds to the [Certificate Validation node](certificate-validation.html).

   * If the node can't collect the certificate, the journey proceeds to a [Page node](page.html) containing a [Platform Username node](platform-username.html) and a [Platform Password node](platform-password.html) to let the user authenticate with username/password credentials.

2. The Certificate Validation node attempts to validate the certificate based on the configuration of that node.

   * If the certificate can be validated, the journey proceeds to the [Certificate User Extractor node](certificate-user-extractor.html).

   * If the certificate is invalid, the journey proceeds to the Failure node.

   * In all other cases, the journey proceeds to a [Page node](page.html) containing a [Platform Username node](platform-username.html) and a [Platform Password node](platform-password.html) to let the user authenticate with username/password credentials.

3. The Certificate User Extractor node extracts the user ID from the certificate and attempts to find a match in the identity store.

   * If the username can be extracted and a matching user is found in the identity store, the journey increments the login count and authenticates the user.

   * If the username can't be extracted or no matching user is found in the identity store, the journey proceeds to the Failure node.

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

## Inputs

This node requires an `X509Certificate` property in the incoming node state.

Implement the [Certificate Collector node](certificate-collector.html) as input to the Certificate Validation node.

## Dependencies

This node has no dependencies.

## Configuration

| Property                                                                | Usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Match Certificate in LDAP                                               | When enabled, AM matches the collected certificates with a certificate stored in the identity store.Set the Subject DN Attribute Used to Search LDAP for Certificates to specify which LDAP property to search for certificate information.Default: Not enabled                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Check Certificate Expiration                                            | When enabled, AM checks if the collected certificates have expired.Default: Not enabled                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Subject DN Attribute Used to Search LDAP for Certificates               | The attribute AM uses to search the identity store for the certificates. The search filter is based on this attribute and the value of the Subject DN as it appears in the certificate.Default: `CN`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Match Certificate to CRL                                                | When enabled, AM checks if the collected certificates have been revoked according to a Certificate Revocation List (CRL) in the identity store.Define related CRL properties later in the node configuration.Default: Not enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Issuer DN Attribute(s) Used to Search LDAP for CRLs                     | The name of the attribute or attributes in the issuer certificate that AM uses to locate the CRL in the identity store.- If you specify only one attribute here, the LDAP search filter used is `(attr-name=attr-value-in-subject-DN)`.

  For example, if the subject DN of the issuer certificate is `C=US, CN=Some CA, serialNumber=123456`, and the attribute specified is `CN`, AM uses a search filter of `(CN=Some CA)` to locate the CRL.

- Specify several CRLs for the same CA issuer in a comma-separated list (`,`) where the names are in the same order in which they appear in the subject DN.

  In this case, the LDAP search filter used is `(attr1=attr1-value-in-subject-DN,attr2=attr2-value-in-subject-DN,…​)`, and so on.

  For example, if the subject DN of the issuer certificate is `C=US, CN=Some CA, serialNumber=123456`, and the attributes specified are `CN,serialNumber`, the LDAP search filter used to find the CRL is `(CN=Some CA,serialNumber=123456)`.Default: `CN` |
| HTTP Parameters for CRL Update                                          | Parameters AM includes in any HTTP CRL call to the CA that issued the certificate.If the client or CA certificate includes the `IssuingDistributionPoint` extension, AM uses this information to retrieve the CRL from the distribution point.Add the parameters as key-value pairs in a comma-separated list (`,`). For example, `param1=value1,param2=value2`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Cache CRLs in Memory                                                    | When enabled, AM caches CRLs in memory.If this option is enabled, Update CA CRLs from CRLDistributionPoint must also be enabled.Default: Enabled                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Update CA CRLs from CRLDistributionPoint                                | When enabled, AM fetches new CA CRLs from the CRL Distribution Point and updates them in the identity store. If the CA certificate includes either the `IssuingDistributionPoint` or the `CRLDistributionPoint` extensions, AM attempts to update the CRLs when they're out of date.Default: Enabled                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| OCSP Validation                                                         | When enabled, AM checks the validity of certificates using the Online Certificate Status Protocol (OCSP).If you enable this option, the AM instance must be able to connect to the internet. You must also configure OCSP for AM under Configure > Server Defaults > Security > Online Certificate Status Protocol Check.Default: Not enabled                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Certificate Identity Store                                              | Select the identity store (configured for the realm) that AM must search for certificates. If you select an identity store here, AM uses the connection details defined for that identity store and ignores all the server settings below this field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| LDAP Server Where Certificates are Stored                               | The LDAP server that holds certificates. Enter the server details in the format `ldap-server:port` .To associate multiple AM servers in a site with corresponding LDAP servers, use the format `am_server\|ldapserver:_port_`. For example, `am.example.com\|ldap1.example.com:636`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| LDAP Search Start or Base DN                                            | Valid base DN for the LDAP search, such as `dc=example,dc=com`. To associate AM servers with different search base DNs, use the format `am_server\|base_dn`. For example, `am.example.com\|dc=example,dc=com` `am1.test.com\|dc=test,dc=com`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| LDAP Server Authentication User and LDAP Server Authentication Password | The credentials used to connect to the LDAP directory that holds the certificates.If you enable mTLS, the node ignores these credentials.Default Authentication User: `cn=Directory Manager`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| mTLS Enabled                                                            | Enables mTLS (mutual TLS) between AM and the directory server.When mTLS is enabled, the node ignores the values for LDAP Server Authentication User and LDAP Server Authentication Password.If you enable this property, you must:- Enable Use SSL/TLS for LDAP Access.

- Provide an mTLS Secret Label Identifier.Default: Not enabled                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| mTLS Secret Label Identifier                                            | An identifier used to create a secret label for mapping to the mTLS certificate in the secret store. AM uses this identifier to create a specific secret label for this node. The secret label takes the form `am.authentication.nodes.certificate.validation.mtls.identifier.cert` , where `identifier` is the value of mTLS Secret Label Identifier. The label can only contain alphanumeric characters (`a-z`, `A-Z`, `0-9`) and periods (`.`). It can't start or end with a period.For greater security, you should [rotate certificates](https://docs.pingidentity.com/pingam/8.1/security/secret-mapping.html) periodically. When you rotate a certificate, update the corresponding mapping in the realm secret store configuration to reflect this identifier. When you rotate a certificate, AM closes any existing connections using the old certificate. A new connection is selected from the connection pool and no server restart is required.                                                  |
| Use SSL/TLS for LDAP Access                                             | When enabled, AM uses SSL/TLS to access the LDAP directory. Make sure that AM trusts the certificate from the LDAP server when enabling this option.Default: Not enabled                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

## Outputs

This node doesn't change the shared state.

## Callbacks

This node doesn't send any callbacks.

## Outcomes

* `True`

  The node could validate the certificates.

  When the outcome is `True`, add a [Certificate User Extractor node](certificate-user-extractor.html) to extract the values of the user certificate.

* `False`

  The node couldn't validate the certificates. The journey follows this path when the node can't validate the certificates and there isn't a more specific outcome available.

* `Not found`

  The Match Certificate in LDAP property is enabled, but the certificates weren't found in the LDAP store.

* `Expired`

  The Check Certificate Expiration property is enabled, and the certificates have expired.

* `Path Validation Failed`

  The Match Certificate to CRL property is enabled, and the certificate path is invalid.

* `Revoked`

  The OCSP Validation property is enabled, and the certificates have been revoked.

## Errors

This node doesn't log any error or warning messages of its own.