---
title: Accept Terms and Conditions node
description: Prompts users to accept the active terms and conditions during registration or sign-on journeys in Advanced Identity Cloud.
component: auth-node-ref
version: latest
page_id: auth-node-ref::accept-terms-and-conditions
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/accept-terms-and-conditions.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-04T17:39:33Z
keywords: ["Nodes &amp; Trees", "Journeys", "Terms &amp; Conditions"]
page_aliases: ["auth-node-accept-terms-and-conditions.adoc"]
superseded_by: https://docs.pingidentity.com/auth-node-ref/latest/accept-terms-and-conditions.html
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

# Accept Terms and Conditions node

The Accept Terms and Conditions node prompts the user to accept the currently active terms and conditions, configured in the Platform UI *(tooltip: Advanced Identity Cloud admin console)*.

Find more information on setting up terms and conditions in [Terms and conditions](https://docs.pingidentity.com/pingoneaic/self-service/self-registration.html#terms-conditions).

Use this node for registration, or combined with the [Terms and Conditions Decision node](terms-and-conditions-decision.html) for progressive profiling or log in.

## Example

For progressive profiling, include this node after a [Terms and Conditions Decision node](terms-and-conditions-decision.html). If the user hasn't accepted the latest version of the terms and conditions, evaluation takes them to a page that requires them to accept the current terms and conditions.

The [Patch Object node](patch-object.html) stores the acceptance response if the user accepts:

![Storing acceptance of terms and conditions](_images/trees-node-accept-terms-conditions-tree-example.png)

## Availability

| Product                                        | Available? |
| ---------------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud                | Yes        |
| PingAM (self-managed)                          | Yes (1)    |
| Ping Advanced Identity Software (self-managed) | Yes        |

(1) This functionality requires that you configure AM as part of a [Ping Advanced Identity Software deployment](https://docs.pingidentity.com/platform/8.1/sample-setup/).

## Inputs

None. This node doesn't read shared state data.

## Dependencies

None.

## Configuration

This node has no configurable properties.

## Outputs

The node writes a `termsAccepted` object to the shared node state. The object contains these fields:

* `acceptDate`: A timestamp string indicating when the user accepted the terms.

* `termsVersion`: A string indicating the version of the accepted terms.

## Callbacks

The node sends a [TermsAndConditionsCallback](https://docs.pingidentity.com/pingoneaic/am-authentication/callbacks-interactive.html#TermsAndConditionsCallback), which prompts the user to accept the current version of the terms and conditions.

## Outcomes

Single outcome path; the user accepted the terms and conditions.

## Errors

This node doesn't log any error or warning messages of its own.

---

---
title: Account Active Decision node
description: Checks whether a user account is both active and unlocked, routing the journey along True or False outcome paths in Advanced Identity Cloud.
component: auth-node-ref
version: latest
page_id: auth-node-ref::account-active-decision
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/account-active-decision.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-08T00:00:00Z
keywords: ["Nodes &amp; Trees", "Journeys", "Accounts"]
page_aliases: ["auth-node-account-active-decision.adoc"]
superseded_by: https://docs.pingidentity.com/auth-node-ref/latest/account-active-decision.html
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

# Account Active Decision node

The **Account Active Decision** node determines whether the current account is both active and unlocked, and lets the journey make a decision, based on that check.

An account is considered locked under these conditions:

* The status is inactive.

* The status is active and a duration lockout is set on the account.

An account is considered unlocked under this condition:

* The status is active and no duration lockout is set on the account.

The node determines whether the account has been locked, either through persistent (physical) lockout or duration lockout.

Find more information in [Account lockout](https://docs.pingidentity.com/pingoneaic/am-authentication/auth-nodes-and-journeys.html#account-lockout-trees).

## Example

In this simple login journey, authentication fails if the account is assessed to be `inactive` or `locked`.

![Account active Decision node in a simple login journey](_images/account-active-decision-example.png)

This example uses the following nodes:

* The [Page node](page.html) prompts the user to input their username and password:

  * The [Platform Username node](platform-username.html) collects the username and stores it in the shared state.

  * The [Platform Password node](platform-password.html) collects the password and stores it in the shared state.

* The [Data Store Decision node](data-store-decision.html) uses the username and password to determine whether the account exists.

* The **Account Active Decision** node determines whether the account is active and unlocked.

* If the account is active and unlocked, the [Increment Login Count node](increment-login-count.html) increments the login count and authentication succeeds.

* If the account is inactive or locked, authentication fails.

## Availability

| Product                                        | Available? |
| ---------------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud                | Yes        |
| PingAM (self-managed)                          | Yes        |
| Ping Advanced Identity Software (self-managed) | Yes        |

## Inputs

The node reads the user's identity from the shared state.

Implement a [Platform Username node](platform-username.html) earlier in the journey.

## Dependencies

This node has no dependencies.

## Configuration

This node has no configurable properties.

## Outputs

This node doesn't change the shared state.

## Callbacks

This node doesn't send any callbacks.

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
description: Locks or unlocks a user account profile in Advanced Identity Cloud, supporting both persistent and duration-based lockout.
component: auth-node-ref
version: latest
page_id: auth-node-ref::account-lockout
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/account-lockout.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-09T18:17:32Z
keywords: ["Nodes &amp; Trees", "Journeys", "Accounts", "User Profiles", "Authentication"]
page_aliases: ["auth-node-account-lockout.adoc"]
superseded_by: https://docs.pingidentity.com/auth-node-ref/latest/account-lockout.html
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

# Account Lockout node

The Account Lockout node locks or unlocks the authenticating user's account profile.

The node also determines whether the account has been locked through both persistent (physical) lockout and duration lockout.

Find more information in [Account lockout](https://docs.pingidentity.com/pingoneaic/am-authentication/auth-nodes-and-journeys.html#account-lockout-trees).

|   |                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can also use the [Account Active Decision node](account-active-decision.html) to check whether the account is locked at any point in the journey. |

## Example

The following simple example uses this node with the [Retry Limit Decision node](retry-limit-decision.html) to lock an account after the set number of invalid attempts:

![Lock an account after too many authentication failures](_images/retry-limit-decision-journey.png)

The [Retry Limit Decision node](retry-limit-decision.html) Retry limit (default: 3) defines the number of failed attempts before lockout.

Before using a journey like this in deployment, adapt it to reset the retry count on successful authentication.

## Availability

| Product                                        | Available? |
| ---------------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud                | Yes        |
| PingAM (self-managed)                          | Yes        |
| Ping Advanced Identity Software (self-managed) | Yes        |

## Inputs

This node requires the `username` property in the incoming node state. It uses this information to access the account status in the user profile.

It also requires the `realm` property, which the product using this node sets by default.

## Dependencies

None.

## Configuration

| Property    | Usage                                                                           |
| ----------- | ------------------------------------------------------------------------------- |
| Lock Action | Choose whether to `LOCK` or `UNLOCK` the authenticating user's account profile. |

## Outputs

This node doesn't change the shared state.

## Callbacks

This node doesn't send any callbacks.

## Outcomes

Single outcome path; the node updates the account status according to the configured Lock Action:

* `LOCK`

  The account is inactive and the user cannot authenticate.

* `UNLOCK`

  The account is active and the user can authenticate.

## Errors

If this node fails to set the account status, it logs a `failed to set the user status inactive` warning.

This node can also throw exceptions with the following messages:

* `Could not get a valid username from the context`

  Failed to read the `username` from the shared node state.

* `Could not get a valid realm from the context`

  Failed to read the `realm` from the shared node state.

* `Could not find the identity based on the information available on context`

  Failed to find the account profile with this `username` in this `realm`.

* `An error occurred when trying to lock out the user account`

  Failed to update the account status; applies when locking and unlocking the account.

---

---
title: AD Decision node
description: Verifies user credentials against an Active Directory data store and routes journeys based on account status, including locked, disabled, or expired accounts.
component: auth-node-ref
version: latest
page_id: auth-node-ref::ad-decision
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/ad-decision.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-03T18:03:31Z
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication", "Active Directory"]
superseded_by: https://docs.pingidentity.com/auth-node-ref/latest/ad-decision.html
section_ids:
  example: Example
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  callbacks: Callbacks
  outcomes: Outcomes
  ad-decision-disabled-locked-accounts: Locked and disabled accounts
  errors: Errors
---

# AD Decision node

The AD Decision node verifies that the provided username and password exist in the specified Active Directory (AD) data store. The node also checks whether the user account is locked, disabled, or has expired.

The node is similar to the [LDAP Decision node](ldap-decision.html) except for the following differences:

* It doesn't support the LDAP Behera password policy.

* It can return a specific outcome for an expired account in addition to an expired password.

* It makes a distinction between a [disabled account and a locked account](#ad-decision-disabled-locked-accounts).

|   |                                                                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The node requires a direct connection to the AD data store, for example, through a secure communication channel such as Secure Connect.Find more information in [Secure Connect](https://docs.pingidentity.com/pingoneaic/tenants/secure-connect.html). |

## Example

The following example journey collects the user credentials and checks them against the AD data store:

* If they match, the journey continues to the success outcome.

* If the password has expired, the journey ends in failure with a custom message node to inform the user.

* If the account is locked, disabled, or has expired, the journey ends in failure with an invalid account message.

![Example journey showing AD Decision node](_images/ad-decision-node-aic.png)

## Availability

| Product                                        | Available? |
| ---------------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud                | Yes        |
| PingAM (self-managed)                          | Yes        |
| Ping Advanced Identity Software (self-managed) | Yes        |

## Inputs

The node reads the `username` and `password` fields from node state.

Implement a [Platform Username node](platform-username.html) and a [Platform Password node](platform-password.html) earlier in the journey.

Alternatively, implement a [Zero Page Login Collector node](zero-page-login-collector.html).

## Dependencies

This node has no dependencies.

## Configuration

| Property                                                              | Usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Primary LDAP Server *(required)*                                      | Specify one or more primary directory servers. Specify each directory server in the following format: `host:port`.For example, `ad.example.com:389`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Secondary LDAP Server                                                 | Specify one or more secondary directory servers. Specify each directory server in the following format: `host:port`.The journey uses the secondary servers when none of the primary servers are available.For example, `ad_backup.example.com:389`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| DN to Start User Search *(required)*                                  | Specify the DN from which to start the user search. More specific DNs, such as `ou=sales,dc=example,dc=com`, result in better search performance.If multiple entries with the same attribute values exist in the directory server, make sure this property is specific enough to return only one entry.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Bind User DN, Bind User Password                                      | The credentials used to connect to the directory server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Attribute Used to Retrieve User Profile *(required)*                  | The attribute used to retrieve a user profile from the directory server.The user search will have already happened, as specified by the Attributes Used to Search for a User to be Authenticated and User Search Filter properties.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Attributes Used to Search for a User to be Authenticated *(required)* | The attributes the node uses to match the credentials provided by the user to an entry in the directory server.For example, a value of `uid` forms the search filter `uid=user`. If you specify multiple values, such as `uid` and `cn`, the node forms a complex search filter `(\|(uid=user)(cn=user))`.Multiple attribute values let the user authenticate with any one of the values. For example, if you set both `uid` and `mail`, then Barbara Jensen can authenticate with either `bjensen` or `bjensen@example.com`.&#xA;&#xA;If you're using account lockout and you set multiple attribute values here, you must add those attributes to the Alias Search Attribute Name property in the User profile. Find more information about this property in Core authentication attributes > User profile.                                                                                                                                                                      |
| User Search Filter                                                    | A filter to append to user searches.For example, if your search attribute is `mail` and you set User Search Filter to `(objectClass=inetOrgPerson)`, the node uses `(&(mail=address)(objectClass=inetOrgPerson))` as the resulting search filter. In this example, *address* is the mail address provided by the user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Search Scope                                                          | The extent of the search for users in the directory server:- `OBJECT`: The search extends only to the entry specified by the DN to Start User Search.

- `ONELEVEL`: The search extends to the entries that are direct children of the DN to Start User Search.

- `SUBTREE`: The search extends to the DN to Start User Search and every entry under it.Default: `SUBTREE`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| LDAP Connection Mode                                                  | Whether to use SSL or StartTLS to connect to the directory server. The node must be able to trust the certificates used.Possible values: `LDAP`, `LDAPS`, and `StartTLS`Default: `LDAP`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| mTLS Enabled                                                          | Enables mTLS (mutual TLS) between Advanced Identity Cloud and the directory server.This setting applies to *all* configured LDAP servers; that is, Advanced Identity Cloud uses mTLS to authenticate to all LDAP servers configured for this node.When mTLS is enabled, Advanced Identity Cloud ignores the values for Bind User DN and Bind User Password.If you enable this property, you must:- Set the LDAP Connection Mode to `LDAPS`

- Provide an mTLS Secret Label IdentifierLearn about mapping secrets in [Map and rotate secrets](https://docs.pingidentity.com/pingoneaic/tenants/esvs-signing-encryption.html#map-esv-secrets-to-secret-labels).Default: Not enabled                                                                                                                                                                                                                                                                                                  |
| mTLS Secret Label Identifier                                          | Identifier used to create a secret label for mapping to the mTLS certificate in the secret store. Advanced Identity Cloud uses this identifier to create a specific secret label for this node. The secret label takes the form `am.authentication.nodes.ad.decision.mtls.identifier.cert`, where `identifier` is the value of mTLS Secret Label Identifier. The identifier can only contain alphanumeric characters (`a-z`, `A-Z`, `0-9`) and periods (`.`). It can't start or end with a period. All LDAP servers configured for this node share the same secret label.For more security, you should rotate certificates periodically. When you rotate a certificate, update the corresponding mapping in the realm secret store configuration to reflect this label. When you rotate a certificate, Advanced Identity Cloud closes any existing connections using the old certificate. A new connection is selected from the connection pool and no server restart is required. |
| Return Account Locked Message                                         | If enabled, the node returns a specific `Account locked` message for locked accounts. Otherwise, it returns a generic `Login failure` message to hide the account's locked status.Default: Not enabled                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Return User DN to DataStore                                           | When enabled, the node returns the DN rather than the User ID. From the DN value, Advanced Identity Cloud uses the RDN to search for the user profile. For example, if a returned DN value is `uid=demo,ou=people,dc=example,dc=com`, Advanced Identity Cloud uses `uid=demo` to search the directory server.Default: Enabled                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| User Creation Attributes                                              | This list lets you map (external) attribute names from the LDAP directory server to (internal) attribute names used by Advanced Identity Cloud.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Minimum Password Length                                               | The minimum acceptable password length.Default: `8`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Trust All Server Certificates                                         | When enabled, the server blindly trusts server certificates, including self-signed test certificates.Default: Not enabled                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| LDAP Connection Heartbeat Interval                                    | Specifies how often Advanced Identity Cloud should send a heartbeat request to the directory server to ensure that the connection doesn't remain idle.Some network administrators configure firewalls and load balancers to drop connections that are idle for too long. Set the units for the interval in the `LDAP Connection Heartbeat Time Unit` property.&#xA;&#xA;Setting this property to 0 does not disable the heartbeat (keepalive) or load balancer availability checks.Default: `10`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| LDAP Connection Heartbeat Time Unit                                   | The time unit for the `LDAP Connection Heartbeat Interval`.Default: `seconds`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| LDAP Operations Timeout                                               | The timeout, in seconds, that Advanced Identity Cloud should wait for a response from the directory server.Default: `0` (means no timeout)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Use mixed case for password change messages                           | Whether the server returns password reset messages in mixed case (sentence case) or transforms them to uppercase.By default, the server transforms password reset and password change messages to uppercase. Enable this setting to return messages in sentence case.Default: Not enabled                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| LDAP Affinity Level                                                   | Level of affinity used to balance requests across directory servers.Affinity-based load balancing means that each request for the same user entry goes to the same directory server. The directory server used for a specific operation is determined by the DN of the identity involved.List the directory server instances that form part of the affinity deployment in the Primary LDAP Server and Secondary LDAP Server properties.Options are:- `NONE` – no affinity

- `BIND` – affinity for BIND requests only

- `ALL` – affinity for all requestsDefault: `NONE`                                                                                                                                                                                                                                                                                                                                                                                                          |

## Outputs

If a password reset is required, the node adds a `lastModuleState` property with the value of `changeAfterReset` to shared state.

## Callbacks

The node sends the following callbacks when a password change is required:

* `ConfirmationCallback`

  Prompts the user to submit the password change or to cancel.

* `PasswordCallback`

  Prompts the user for their current password, the new password, and a confirmation of the new password. The node sends three instances of this callback.

* `TextOutputCallback`

  Displays a status message to the user, such as a warning that the password is expiring or an error that the new password doesn't meet requirements.

Learn more in [Supported callbacks](https://docs.pingidentity.com/pingoneaic/am-authentication/callbacks-supported.html).

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

The node can log the following exceptions:

* `Invalid configuration`

  AD returns an unexpected result.

* `Server error`

  An error occurs connecting to AD.

* `Unknown login state`

  Authentication results in an unknown state.

---

---
title: Agent Data Store Decision node
description: Authenticates agents such as PingGateway and Java or web agents against the agent profile data store in Advanced Identity Cloud.
component: auth-node-ref
version: latest
page_id: auth-node-ref::agent-data-store-decision
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/agent-data-store-decision.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-03T18:03:31Z
keywords: ["Nodes &amp; Trees", "Journeys", "Agents", "Password", "Data Store"]
page_aliases: ["auth-node-agent-data-store-decision.adoc"]
superseded_by: https://docs.pingidentity.com/auth-node-ref/latest/agent-data-store-decision.html
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

| Product                                        | Available? |
| ---------------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud                | Yes        |
| PingAM (self-managed)                          | Yes        |
| Ping Advanced Identity Software (self-managed) | Yes        |

## Inputs

This node requires the `username` and `password` properties in the incoming node state.

Obtain the agent credentials from the user or with a [Zero Page Login Collector node](zero-page-login-collector.html).

## Dependencies

This node depends on the underlying data store for agent profiles.

## Configuration

This node has no configurable properties.

## Outputs

This node copies the shared and transient states into the outgoing node state.

## Callbacks

This node doesn't send any callbacks.

## Outcomes

* `True`

  The credentials match those found in the data store for agent profiles.

* `False`

  The credentials do *not* match those found in the data store for agent profiles.

## Errors

The node can log the following:

* Warnings

  * `invalid password error`

    The password doesn't match.

  * `invalid username error`

    The username doesn't match any profiles found in the data store.

  * `Exception in data store decision node`

    The node couldn't connect to the data store, or another error occurred.

* Errors

  * Password is null for username *username*

    The password is missing from the shared state for the user.

---

---
title: Akamai Account Protector node
description: Use the Akamai Account Protector node to inject the Akamai risk score into an Advanced Identity Cloud authentication journey.
component: auth-node-ref
version: latest
page_id: auth-node-ref:cloud:akamai-account-protector
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/cloud/akamai-account-protector.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-10-07T16:18:42Z
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication", "Akamai"]
section_ids:
  example: Example
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configure_akamai_account_protector: Configure Akamai Account Protector
  enable_account_protector_on_the_akamai_edge: Enable Account Protector on the Akamai Edge
  add_the_username_parameter_to_akamai_account_protector: Add the username parameter to Akamai Account Protector
  configuration: Configuration
  outputs: Outputs
  callbacks: Callbacks
  outcomes: Outcomes
  errors: Errors
---

# Akamai Account Protector node

The Akamai Account Protector node injects the Akamai risk score into your authentication journey. When the Akamai Account Protector feature is enabled for your application, the Akamai Edge service provides the risk score in an HTTP request header. Learn more in the [Akamai Account Protector](https://techdocs.akamai.com/cloud-security/docs/account-protector) documentation.

## Example

The following example inner journey uses the Akamai Account Protector node to parse the user risk score from the `Akamai-User-Risk` header and branch the journey based on the risk:

![Journey using the Akamai Account Protector node](_images/akamai-account-protector-journey.png)

The inner journey in the example is contained in an outer journey that performs user authentication and collects the username. The Akamai Account Protector node parses the `Akamai-User-Risk` HTTP request header and extracts the user risk score. Based on the risk score, the journey progresses through the appropriate outcome.

## Availability

| Product                                        | Available? |
| ---------------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud                | Yes        |
| PingAM (self-managed)                          | Yes (1)    |
| Ping Advanced Identity Software (self-managed) | Yes (1)    |

(1) For self-managed products, download the node from the [Ping Identity Marketplace](https://marketplace.pingone.com/item/akamai-account-protector).

## Inputs

This node retrieves user risk data from the `Akamai-User-Risk` HTTP request header. The header value contains semicolon-delimited key-value pairs, for example `score=50`.

## Dependencies

You must set up [Akamai Account Protector](https://www.akamai.com/resources/product-brief/account-protector) and enable it in your web application before using the Akamai Account Protector node.

### Configure Akamai Account Protector

Akamai Account Protector detects malicious activity and assigns risk scores to requests. To inject the `akamai-user-risk` header, follow these steps:

#### Enable Account Protector on the Akamai Edge

1. Sign in to the Akamai Control Center.

2. Go to Security Configuration and select your existing security policy or create a new one.

3. Enable Account Protector under the bot management settings.

4. Ensure that risk scoring is enabled and that Akamai adds the `akamai-user-risk` HTTP header.

#### Add the username parameter to Akamai Account Protector

1. In the Akamai Control Center, create an API definition pointing to your Advanced Identity Cloud hostname.

2. Add an API resource with the following details:

   * **Name:** Authenticate

   * **Path:** `/am/json/realms/root/realms/realm name/authenticate`

3. Select the `POST` method and set the request parameters.

   > **Collapse: Example request parameters for the Authenticate API resource**
   >
   > ![Example request parameters for the Authenticate API resource](_images/akamai-account-protector-set-parameters.png)

4. Similarly, set the response parameters.

   > **Collapse: Example JSON/XML schema for the request and response parameters**
   >
   > ```json
   > {
   >   "requestBody": {
   >     "content": {
   >       "application/json": {
   >         "schema": {
   >           "type": "object",
   >           "required": [
   >             "callbacks"
   >           ],
   >           "properties": {
   >             "callbacks": {
   >               "type": "array",
   >               "items": {
   >                 "type": "object",
   >                 "properties": {
   >                   "input": {
   >                     "type": "array",
   >                     "items": {
   >                       "type": "object",
   >                       "properties": {
   >                         "name": {
   >                           "type": "string"
   >                         }
   >                       }
   >                     }
   >                   }
   >                 }
   >               },
   >               "description": "callbacks"
   >             }
   >           }
   >         }
   >       },
   >       "application/xml": {
   >         "schema": {
   >           "type": "object",
   >           "required": [
   >             "callbacks"
   >           ],
   >           "properties": {
   >             "callbacks": {
   >               "type": "array",
   >               "items": {
   >                 "type": "object",
   >                 "properties": {
   >                   "input": {
   >                     "type": "array",
   >                     "items": {
   >                       "type": "object",
   >                       "properties": {
   >                         "name": {
   >                           "type": "array",
   >                           "items": {
   >                             "type": "string"
   >                           },
   >                           "maxItems": 1
   >                         }
   >                       }
   >                     }
   >                   }
   >                 }
   >               },
   >               "description": "callbacks"
   >             }
   >           },
   >           "xml": {
   >             "name": "root"
   >           }
   >         }
   >       }
   >     },
   >     "required": true
   >   }
   > }
   > ```

## Configuration

| Property                           | Usage                                                                                                                                                   |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| High Risk Threshold                | The maximum score for the Medium Risk outcome. Scores above this value receive the High Risk outcome.Default: `50`                                      |
| Medium Risk Threshold              | The maximum score for the Low Risk outcome. Scores above this value and up to the High Risk Threshold receive the Medium Risk outcome.Default: `25`     |
| Save Akamai Header to Shared State | If selected, the node writes the `Akamai-User-Risk` header key-value pairs to the shared state, in addition to the transient state.Default: Not enabled |

## Outputs

The node writes each key-value pair from the `Akamai-User-Risk` header, such as `score`, to the transient state. If you select Save Akamai Header to Shared State, the node also writes the pairs to the shared state.

## Callbacks

This node doesn't send any callbacks.

## Outcomes

The node has the following outcomes:

* `Low Risk`

  The overall score is less than or equal to the Medium Risk Threshold value.

* `Medium Risk`

  The overall score is greater than the Medium Risk Threshold and less than or equal to the High Risk Threshold value.

* `High Risk`

  The overall score is greater than the High Risk Threshold value.

* `No Score`

  The `Akamai-User-Risk` header is empty.

* `Error`

  The node couldn't parse the risk score; for example, the header doesn't contain a `score` key-value pair or the score isn't an integer.

## Errors

The node can log the following errors:

* `[AkamaiAccountProtector][Version: <version>][Marketplace]Exception occurred`

  An exception occurred while the node processed the `Akamai-User-Risk` header. The node stores the exception message and stack trace in the transient state.

---

---
title: Amster Jwt Decision node
description: Configure the Amster JWT Decision node to authenticate Amster connections to PingAM using SSH key pairs stored in an authorized_keys file.
component: auth-node-ref
version: latest
page_id: auth-node-ref:am-only:amster-jwt-decision
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/am-only/amster-jwt-decision.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-03T18:03:31Z
keywords: ["Nodes &amp; Trees", "Journeys", "Amster"]
superseded_by: https://docs.pingidentity.com/auth-node-ref/latest/am-only/amster-jwt-decision.html
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

# Amster Jwt Decision node

Not supported in Advanced Identity Cloud

The Amster Jwt Decision node lets AM authenticate Amster connections using SSH keys.

The Amster client signs the JWT using a local private key. AM verifies the signature using the list of public keys in the `authorized_keys` file. Specify the path to the `authorized_keys` file in the node configuration.

If the entry in the authorized keys file contains a `from` parameter, only connections originating from a qualifying host are permitted.

Find more information in [Private key connections](https://docs.pingidentity.com/pingam/8.1/amster/connect-am.html#private-login).

## Example

This node is used only by the `amsterService` authentication tree:

![journey amster service](_images/journey-amster-service.png)

|   |                                                                            |
| - | -------------------------------------------------------------------------- |
|   | Changing or removing this tree could prevent Amster from connecting to AM. |

## Availability

| Product                                        | Available? |
| ---------------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud                | No         |
| PingAM (self-managed)                          | Yes        |
| Ping Advanced Identity Software (self-managed) | Yes        |

## Inputs

The node reads the `NONCE_STATE_KEY` from the Amster client.

## Dependencies

This node has no dependencies.

## Configuration

| Property        | Usage                                                                                                                                                                                                            |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Authorized Keys | Location of the `authorized_keys` file used to validate remote Amster connections.This file has the same format as an [OpenSSH `authorized_keys`](https://www.ssh.com/academy/ssh/authorized-keys-openssh) file. |

## Outputs

This node doesn't change the shared state.

## Callbacks

The node sends a [HiddenValueCallback](https://docs.pingidentity.com/pingoneaic/am-authentication/callbacks-interactive.html#hiddenvaluecallback) containing a one-time nonce that the Amster client must sign in a JWT using a local private key and return to the node for verification.

## Outcomes

* True

  The journey follows this outcome if the node can validate the incoming private key against the public keys in the `authentication_keys` file. Successful authentication creates an `amAdmin` session in AM.

* False

  The journey follows this outcome if the node can't validate the incoming private key against the public keys in the `authentication_keys` file, either because the incoming key is invalid, or because the `authentication_keys` file is inaccessible.

## Errors

If the node can't read the `authorized_keys` file, it returns the error `AmsterJwtDecisionNode: Could not read authorized keys file filename`.

---

---
title: Anonymous Session Upgrade node
description: Upgrades an anonymous session to a non-anonymous session in Advanced Identity Cloud journeys.
component: auth-node-ref
version: latest
page_id: auth-node-ref::anonymous-session-upgrade
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/anonymous-session-upgrade.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-20T18:03:31Z
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication", "Sessions"]
page_aliases: ["auth-node-anonymous-session-upgrade.adoc"]
superseded_by: https://docs.pingidentity.com/auth-node-ref/latest/anonymous-session-upgrade.html
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

# Anonymous Session Upgrade node

The Anonymous Session Upgrade node lets you upgrade an anonymous session to an identified session.

## Example

After using the [Anonymous User Mapping node](anonymous-user-mapping.html) to access Advanced Identity Cloud as an anonymous user, this node lets users upgrade their session to a non-anonymous one:

![Lets anonymous users upgrade their session](_images/trees-node-anonymous-session-upgrade-example-platform.png)

## Availability

| Product                                        | Available? |
| ---------------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud                | Yes        |
| PingAM (self-managed)                          | Yes        |
| Ping Advanced Identity Software (self-managed) | Yes        |

## Inputs

None. This node doesn't read shared state data.

## Dependencies

The node requires an existing anonymous session. Use it after the [Anonymous User Mapping node](anonymous-user-mapping.html) node or another node that creates an anonymous session.

## Configuration

This node has no configurable properties.

## Outputs

The node upgrades the current anonymous session when the previous authentication session was created by an anonymous journey.

## Callbacks

This node doesn't send any callbacks.

## Outcomes

Single outcome path.

## Errors

The node can log the following errors:

* `Failed to get previous session`

  The node couldn't retrieve the session identified by the request SSO token.

* `Unable to create AMAuthenticationManager instance`

  The node couldn't load the authentication configuration for the realm. Check that the realm and its authentication configuration are available.

---

---
title: Anonymous User Mapping node
description: Maps unauthenticated users to a named anonymous account in Advanced Identity Cloud, enabling limited access without credentials.
component: auth-node-ref
version: latest
page_id: auth-node-ref::anonymous-user-mapping
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/anonymous-user-mapping.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-20T18:03:31Z
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication", "Accounts"]
page_aliases: ["auth-node-anonymous-user-mapping.adoc"]
superseded_by: https://docs.pingidentity.com/auth-node-ref/latest/anonymous-user-mapping.html
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

# Anonymous User Mapping node

The Anonymous User Mapping node lets users log in to an application or website without providing credentials, by assuming the identity of a specified existing user account. The default user for this purpose is named `anonymous`.

Take care to limit access for such users. For example, grant anonymous users access to public downloads on your site.

## Example

The following example uses this node to grant users access as an anonymous user if they've completed social authentication but don't have an existing profile:

![Example journey using the Anonymous User Mapping node](_images/anonymous-user-mapping-journey.png)

* The [Page node](page.html) containing the [Platform Username node](platform-username.html), [Platform Password node](platform-password.html), and [Select Identity Provider node](select-identity-provider.html) prompts the user to authenticate with a username and password, or to select a social identity provider.

* If the user enters their username and password, the [Data Store Decision node](data-store-decision.html) validates the username-password credentials, and authentication succeeds if their credentials are valid.

* If the user selects social authentication, the [Social Provider Handler node](social-provider-handler.html) does the following:

  * If the user has an existing user account, authenticates that user.

  * If the user doesn't have a user account, the Anonymous User Mapping node provides limited access as an anonymous user.

  * If the user interrupts the social authentication, they are routed back to the Page node to try again.

## Availability

| Product                                        | Available? |
| ---------------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud                | Yes        |
| PingAM (self-managed)                          | Yes        |
| Ping Advanced Identity Software (self-managed) | Yes        |

## Inputs

This node requires the `realm` property in the incoming node state, which Advanced Identity Cloud sets by default.

## Dependencies

The configured anonymous user must already exist in the realm, and its user status must be `active`.

## Configuration

| Property            | Usage                                                                                                                                        |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Anonymous User Name | The username of an account that represents anonymous users. This user must already exist in the realm, and its user status must be `active`. |

## Outputs

The node sets the following values:

* `username`: The configured anonymous username.

* The universal ID of the configured user.

* An anonymous authentication marker used when upgrading the session.

## Callbacks

This node doesn't send any callbacks.

## Outcomes

Single outcome path.

## Errors

The node can log the following error:

* `Anonymous user name could not be found in the configuration`

  The Anonymous User Name property is empty. Enter the username of an existing active user account.

---

---
title: App Policy Decision node
description: Evaluates application access policies automatically from journey context in Advanced Identity Cloud, routing based on accept, reject, or error outcomes.
component: auth-node-ref
version: latest
page_id: auth-node-ref::app-policy-decision
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/app-policy-decision.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-09T17:31:41Z
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication"]
superseded_by: https://docs.pingidentity.com/auth-node-ref/latest/app-policy-decision.html
section_ids:
  example: Example
  prerequisites: Prerequisites
  example_journey: Example journey
  availability: Availability
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

* An access policy with that resource is defined within the application.

The outcome of the policy evaluation, to accept or reject access, maps to the node's outcomes. It doesn't handle advices or environment conditions.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Consider the following security risks when designing journeys that include policy evaluation:- Brute force information disclosure

  An authenticated user can probe the policy framework by submitting different inputs to determine who or what passes or fails a policy evaluation.

  To prevent this, design journeys so that the policy framework isn't directly exposed to repeated probing. For example, block or lock out a session after a set number of failed attempts, just as you would for other authentication mechanisms.

- Denial of service (DoS)

  Unauthenticated users could repeatedly trigger policy evaluations, which can consume significant resources and increase the risk of a DoS attack.

  To reduce this risk:

  * Protect the deployment at the container or network edge, for example, with a reverse proxy.

  * Place the policy node after the user has authenticated whenever possible, to limit the attack surface.

  This can also prevent information disclosure, such as exposing group membership based on submitted usernames. |

## Example

This example uses an App Policy Decision node to manage access to a finance portal application based on usernames.

### Prerequisites

The following setup is assumed:

* A test end user, [added to the `Finance` group](https://docs.pingidentity.com/pingoneaic/idm-objects/manage-groups.html#add-users-to-group).

* A custom [OIDC application](https://docs.pingidentity.com/pingoneaic/app-management/register-a-custom-application.html#openid-connect-oidc), with the following settings:

  * Client ID

    `finance-app`

  * Access Policy

    `Any`

    Condition: `User Group Membership`

    equals

    Value: `Finance`

    > **Collapse: Example policy**
    >
    > ![app policy decision policy](_images/app-policy-decision-policy.png)

  * Use a journey to authenticate users to this application

    example journey

### Example journey

![Policy Decision node in an app authorization flow](_images/app-policy-decision-example.png)

* The authorization journey is invoked specifying the OAuth 2.0 client ID as the resource, for example:

  `https://tenant-env-fqdn/am/oauth2/alpha/authorize?client_id=finance-app&redirectUri=http://www.example.com/signin&scope=openid&response_type=code`

- The [Page node](page.html) containing the [Platform Username node](platform-username.html) and [Platform Password node](platform-password.html) prompts for credentials.

- The [Data Store Decision node](data-store-decision.html) validates the username-password credentials.

- A successful authentication routes the journey to the App Policy Decision node.

  The node has no configuration, but relies on the journey context to identify the OAuth 2.0 client ID resource (`finance-app`). It can then locate the access policy to evaluate whether the end user is a member of the `Finance` group.

- The outcome of the policy evaluation determines the path of the journey:

  * Accept

    The policy grants access. The [Message node](message.html) informs the end user they're authorized and the journey is successful.

  * Reject

    The policy rejects access. The [Message node](message.html) informs the end user they're not authorized.

  * Error

    An error in policy evaluation leads to the failure outcome.

  * Unknown Resource

    The node failed to identify the resource and the journey continues to the [Set Error Details node](set-error-details.html).

## Availability

| Product                                        | Available? |
| ---------------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud                | Yes        |
| PingAM (self-managed)                          | Yes        |
| Ping Advanced Identity Software (self-managed) | Yes        |

## Inputs

If policy evaluation requires a subject, make sure the username is collected earlier in the journey.

## Dependencies

This node requires the following configuration:

* An application (OAuth 2.0 client or SAML SP entity) that uses a journey with an App Policy Decision node

* An access policy defined within the application

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
description: Collects user attribute values during a journey for use in registration or profile update flows in Advanced Identity Cloud.
component: auth-node-ref
version: latest
page_id: auth-node-ref::attribute-collector
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/attribute-collector.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-04T17:39:33Z
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication", "Schema", "Policy", "Custom Attributes"]
page_aliases: ["auth-node-attribute-collector.adoc"]
superseded_by: https://docs.pingidentity.com/auth-node-ref/latest/attribute-collector.html
section_ids:
  example: Example
  add_date_and_datetime_fields_to_a_journey: Add date and datetime fields to a journey
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  callbacks: Callbacks
  outcomes: Outcomes
  errors: Errors
---

# Attribute Collector node

The Attribute Collector node collects the values of attributes for use later in the flow. For example, to populate a new account during registration.

This node supports three types of attributes:\
`string`\
`boolean`\
`number`

To request a value, the attribute must be present and viewable in the identity schema for the current identity object.

|   |                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can find more information about the identity schema in [Advanced Identity Cloud identity schema](https://docs.pingidentity.com/pingoneaic/identities/identity-cloud-identity-schema.html). |

The node lets you configure whether the attributes are required to continue and whether to use a policy filter to validate the input values.

## Example

### Add date and datetime fields to a journey

The Attribute Collector node lets you add properties (attributes) that follow a date or datetime (date and time of day). The format of the date comes from the locale set in your browser.

The following table displays the differences between date and datetime:

| Display format | Managed object field format                                   | Notes                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------- | ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Date only      | String formatExample: `frIndexedString1`                      | The format of the date comes from the locale set in your browser.For example, if the locale is English, then the format presented to the end user is `MM-DD-YYYY`. If the local is French, the format is `DD-MM-YYYY`.                                                                                                                                                                          |
| Date and time  | String format (date and time of day)Example: `frIndexedDate1` | The format of the date comes from the locale set in your browser.For example, if the locale is English (United States), the format presented to the end user is `MM-DD-YYYY`. If the locale is French, the format is `DD-MM-YYYY`.&#xA;&#xA;You can only use the date general purpose extension attributes for datetime. Don't attempt to use the indexed date properties with the date format. |

|   |                                                                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The rendering of the date to the end user changes, depending on the locale set in the browser. However, the server *stores* the date value in UTC format as `YYYY-MM-DDHH:MM:SS`. For example, `2026-06-10T08:01:00Z`. |

To render the date or datetime UI element to an end user with the Attribute Collector node, you must do the following:

1. Specify the property to use as date or datetime:

   * [General purpose extension attributes](https://docs.pingidentity.com/pingoneaic/identities/user-identity-properties-attributes-reference.html#general-purpose-extension-attributes). Recommended. Use OOTB indexed attributes:

     * Use the `String` indexed properties, such as `frIndexedString1` for date *only*.

     * Use the `Date` indexed properties, such as `frIndexedDate1` for datetime *only*.

   * [Create your own custom attributes](https://docs.pingidentity.com/pingoneaic/identities/customize-object-types.html#create-custom-properties). Create custom attributes, prefixed with `custom_`.

2. Apply formatting and policies to the property for `Date` or `Datetime`.

   1. In the Advanced Identity Cloud admin UI, go to Identities > Configure > *object type*, for example, Alpha realm - User.

   2. Switch to the Properties tab and select the property you specified.

   3. Select one of the following from the Property Format list:

      * `Date` for a date property.

      * `Date/Time` for a datetime property.

   4. On the Validation tab, select one of the following checkboxes:

      * Valid formatted date for a date property.

      * Valid datetime for a datetime property.

3. Add the property name to the Attributes to Collect field in the Attribute Collector node.

For an in-depth use case, add the `date` or `datetime` property to an Attribute Collector node in a registration flow.

The following video shows an example of a journey collecting the datetime from an end user using the Attribute Collector node:

**Video (Video)**

<\_images/mp4/attribute-collector-datetime.mp4>

## Availability

| Product                                        | Available? |
| ---------------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud                | Yes        |
| PingAM (self-managed)                          | Yes (1)    |
| Ping Advanced Identity Software (self-managed) | Yes        |

(1) This functionality requires that you configure AM as part of a [Ping Advanced Identity Software deployment](https://docs.pingidentity.com/platform/8.1/sample-setup/).

## Inputs

For validation, this node reads the Identity Attribute (default: `userName`) from the shared node state. It uses the value to look up the identity object.

It prompts the user for the attributes to collect.

## Dependencies

None.

## Configuration

| Property                | Usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Attributes to Collect   | A list of the attributes to collect from the client. The attributes must exist in the identity schema for the current identity object.Default: none                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| All Attributes Required | When enabled, all attributes collected in this node are required in order to continue.Default: Not enabled                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Validate Input          | Select this option to validate the collected attributes against the validation policies specified for the property.Learn more in [Use policies to validate data](https://docs.pingidentity.com/pingoneaic/idm-objects/policies.html).If you enable this option, the collected attributes must be *user editable*.> **Collapse: How do I make an attribute user-editable?**
>
> 1. In the Advanced Identity Cloud admin UI, go to Identities > Configure > *object type*, for example, Alpha realm - User.
>
> 2. Switch to the Properties tab and select the property you want to make user-editable.
>
> 3. On the Display tab, select the Show in User-facing Form checkbox.Default: Not enabled |
| Identity Attribute      | The property used to locate the identity.Default: `userName`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## Outputs

The node writes the attributes and their values to the shared node state.

## Callbacks

The node sends the following callbacks:

* `BooleanAttributeInputCallback`

  Prompts the user to select a boolean value for the attribute being collected.

* `NumberAttributeInputCallback`

  Prompts the user to enter a number value for the attribute being collected.

* `StringAttributeInputCallback`

  Prompts the user to enter a string value for the attribute being collected.

Learn more in [Supported callbacks](https://docs.pingidentity.com/pingoneaic/am-authentication/callbacks-supported.html).

## Outcomes

Single outcome path; on success, downstream nodes can read the attributes from the shared node state.

## Errors

This node doesn't log any error or warning messages of its own.

---

---
title: Attribute Present Decision node
description: Checks whether a specified attribute, including private attributes such as password, is present on a user object in Advanced Identity Cloud.
component: auth-node-ref
version: latest
page_id: auth-node-ref::attribute-present-decision
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/attribute-present-decision.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-04T17:39:33Z
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication", "Account", "Custom Attributes", "Update Passwords"]
page_aliases: ["auth-node-attribute-present-decision.adoc"]
superseded_by: https://docs.pingidentity.com/auth-node-ref/latest/attribute-present-decision.html
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

| Product                                        | Available? |
| ---------------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud                | Yes        |
| PingAM (self-managed)                          | Yes (1)    |
| Ping Advanced Identity Software (self-managed) | Yes        |

(1) This functionality requires that you configure AM as part of a [Ping Advanced Identity Software deployment](https://docs.pingidentity.com/platform/8.1/sample-setup/).

## Inputs

This node reads the Identity Attribute from the shared node state. If it can't read the Identity Attribute, it reads the `userName` from the shared node state.

It uses the value to look up the identity object.

## Dependencies

None.

## Configuration

| Property           | Usage                                                                                                                                                                                                                                                                                                                        |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Present Attribute  | The attribute whose presence you want to verify in the identity schema for the current identity object. This can be an otherwise private attribute, such as `password`.&#xA;&#xA;This field is case-sensitive and must exactly match the name of the IDM property. For example, givenName, not givenname.Default: `password` |
| Identity Attribute | The property used to locate the identity.Default: `userName`                                                                                                                                                                                                                                                                 |

## Outputs

This node doesn't change the shared state.

## Callbacks

This node doesn't send any callbacks.

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
description: Verifies that a user attribute satisfies a configured condition, such as presence or equality, during journeys in Advanced Identity Cloud.
component: auth-node-ref
version: latest
page_id: auth-node-ref::attribute-value-decision
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/attribute-value-decision.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-04T17:39:33Z
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication", "Custom Attributes"]
page_aliases: ["auth-node-attribute-value-decision.adoc"]
superseded_by: https://docs.pingidentity.com/auth-node-ref/latest/attribute-value-decision.html
section_ids:
  availability: Availability
  configuration: Configuration
  callbacks: Callbacks
---

# Attribute Value Decision node

Verifies that the specified attribute satisfies a specific condition.

Use this node to check whether an attribute's expected value is equal to a collected attribute value, or to validate that the specified attribute was collected.

Examples:

* To validate that a user provided the country attribute during registration, set the comparison operation to `PRESENT`, and the comparison attribute to `country`.

* To validate that the country attribute is set to the United States, set the comparison operation to `EQUALS`, the comparison attribute to `country`, and the comparison value to `United States`.

Use [Attribute Present Decision node](attribute-present-decision.html) instead when you need to check for the presence of a private attribute, such as `password`.

## Availability

| Product                                        | Available? |
| ---------------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud                | Yes        |
| PingAM (self-managed)                          | Yes (1)    |
| Ping Advanced Identity Software (self-managed) | Yes        |

(1) This functionality requires that you configure AM as part of a [Ping Advanced Identity Software deployment](https://docs.pingidentity.com/platform/8.1/sample-setup/).

## Configuration

| Property             | Usage                                                                                                                                                                                                                       |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Comparison Operation | The operation to perform on the object attribute:- `PRESENT`

  Checks the existence of an attribute regardless of its value.

- `EQUALS`

  Checks if the object's attribute value equals the configured comparison value. |
| Comparison Attribute | The object attribute to compare.                                                                                                                                                                                            |
| Comparison Value     | When Comparison Operation is `EQUALS`, compare this value to the provided attribute value.                                                                                                                                  |
| Identity Attribute   | The property used to locate the identity.                                                                                                                                                                                   |

## Callbacks

This node doesn't send any callbacks.

---

---
title: Auth Level Decision node
description: Compares the current authentication level against a configured threshold to route journeys in Advanced Identity Cloud.
component: auth-node-ref
version: latest
page_id: auth-node-ref::auth-level-decision
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/auth-level-decision.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-03T18:03:31Z
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication"]
page_aliases: ["auth-node-auth-level-decision.adoc"]
superseded_by: https://docs.pingidentity.com/auth-node-ref/latest/auth-level-decision.html
section_ids:
  availability: Availability
  callbacks: Callbacks
  outcomes: Outcomes
  configuration: Configuration
---

# Auth Level Decision node

Compares the current authentication level value against a configured value.

## Availability

| Product                                        | Available? |
| ---------------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud                | Yes        |
| PingAM (self-managed)                          | Yes        |
| Ping Advanced Identity Software (self-managed) | Yes        |

## Callbacks

This node doesn't send any callbacks.

## Outcomes

* `True`

* `False`

## Configuration

| Property                        | Usage                                                                                                                                                                                |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Sufficient Authentication Level | Evaluation continues along the `True` path if the current authentication level is equal to or greater than this integer; otherwise, the evaluation continues along the `False` path. |

---

---
title: Authenticate Thing node
description: Use the Authenticate Thing node in PingAM to authenticate IoT devices and gateways using Proof of Possession JWT or Client Assertion.
component: auth-node-ref
version: latest
page_id: auth-node-ref:self-managed:authenticate-thing
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/self-managed/authenticate-thing.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-03T18:03:31Z
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication", "Identity Store"]
page_aliases: ["self-managed/auth-node-authenticate-thing.adoc"]
superseded_by: https://docs.pingidentity.com/auth-node-ref/latest/self-managed/authenticate-thing.html
section_ids:
  examples: Examples
  availability: Availability
  dependencies: Dependencies
  callbacks: Callbacks
  outcomes: Outcomes
  configuration: Configuration
---

# Authenticate Thing node

Not supported in Advanced Identity Cloud

This node authenticates a *thing*. A thing represents an IoT device, service, or the [IoT Gateway](https://backstage.forgerock.com/docs/iot/7.4/evaluation-guide/about-iot.html#about-fr-things).

## Examples

The following example shows how to authenticate a thing when the identity already exists in the identity store and when its profile contains a confirmation key:

![trees-node-authenticate-thing-example1](_images/trees-node-authenticate-thing-example1.png)

The following example shows how to authenticate a thing when the identity does not exist, or when it needs to refresh its confirmation key:

![trees-node-authenticate-thing-example2](_images/trees-node-authenticate-thing-example2.png)

## Availability

| Product                                        | Available? |
| ---------------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud                | No         |
| PingAM (self-managed)                          | Yes        |
| Ping Advanced Identity Software (self-managed) | Yes        |

## Dependencies

Before you configure this node, you must configure the [IoT service](https://docs.pingidentity.com/pingam/8.1/setup/services-configuration.html#global-iot) for the realm.

|   |                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Support for this node is provided by the [IoT SDK](https://backstage.forgerock.com/docs/iot/7.4/evaluation-guide/about-iot.html#about-fr-things). |

The node supports two methods of authentication:

1. Proof of Possession JWT

   The node collects a proof-of-possession JWT from the request and does the following:

   * Checks that the claims are valid.

   * Checks that an identity with the same ID as the name of the JWT subject exists.

   * Checks that the identity contains a confirmation key that matches the JWT `kid`.

   * Validates the JWT signature, using the confirmation key stored in the identity.

2. Client Assertion

   The node collects a JWT Bearer token from the request for authentication and validates the request according to the [JWT Profile for OAuth 2.0 Client Authentication and Authorization Grants](https://www.rfc-editor.org/rfc/rfc7523.html#section-3).

## Callbacks

The node sends a [HiddenValueCallback](https://docs.pingidentity.com/pingoneaic/am-authentication/callbacks-interactive.html#hiddenvaluecallback), which collects the authentication JWT from the IoT SDK — either a proof-of-possession JWT containing a challenge nonce, or a client assertion JWT, depending on the configured JWT Authentication Method.

## Outcomes

* `Success`

* `Failure`

* `Requires Registration`

If all checks are successful, evaluation continues through the `Success` path, and adds the username and the verified claims to the shared node state.

If the identity does not exist, or AM cannot match the identity with the confirmation key, evaluation continues through the `Requires Registration` outcome.

If any other check fails, evaluation continues through the `Failure` outcome.

## Configuration

| Property                   | Usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| JWT Authentication Method  | Choose the required JWT authentication method:- Proof of Possession

  Prove that the signer of the JWT is the owner of the key by including a challenge nonce in the JWT. Validation is according to the [JWT Proof of Possession specification](https://tools.ietf.org/html/rfc7800).

- Client Assertion

  Present a JWT Bearer token for authentication and validate the request according to the [JWT Profile for OAuth 2.0 Client Authentication and Authorization Grants](https://www.rfc-editor.org/rfc/rfc7523.html#section-3). |
| Issue Restricted Token     | If this setting is enabled, the node adds a Proof of Possession restriction to the session token issued on successful authentication.Any requests accompanied by the token must be signed with the key that was used to sign the authentication JWT.                                                                                                                                                                                                                                                                                      |
| Additional Audience Values | Any additional audience values that will be permitted when verifying JWTs.These audience values are in addition to the AM base, issuer and token endpoint URIs for the Client Assertion authentication method or the realm path for Proof of Possession.                                                                                                                                                                                                                                                                                  |

---

---
title: Authentication node reference
description: Reference index of all Advanced Identity Cloud authentication nodes, organized by category including MFA, federation, identity management, and utility nodes.
component: auth-node-ref
version: latest
page_id: auth-node-ref::overview
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/overview.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-10-14T11:08:17Z
superseded_by: https://docs.pingidentity.com/auth-node-ref/latest/overview.html
section_ids:
  basic_authentication_nodes: Basic authentication nodes
  mfa_nodes: MFA nodes
  risk_management_nodes: Risk management nodes
  behavioral_nodes: Behavioral nodes
  contextual_nodes: Contextual nodes
  federation_nodes: Federation nodes
  identity_management_nodes: Identity management nodes
  utility_nodes: Utility nodes
  thing_nodes_pingamping_advanced_identity_software: Thing nodes (PingAM/Ping Advanced Identity Software)
  uncategorized_nodes: Uncategorized nodes
  marketplace_nodes: Marketplace nodes
---

# Authentication node reference

## Basic authentication nodes

* [AD Decision node](ad-decision.html)

* [Data Store Decision node](data-store-decision.html)

* [Failure node](failure.html)

* [Identity Store Decision node](cloud/identity-store-decision.html)

* [Kerberos node](self-managed/kerberos.html)

* [LDAP Decision node](ldap-decision.html)

* [Password Collector node](am-only/password-collector.html)

* [Success node](success.html)

* [Username Collector node](am-only/username-collector.html)

* [Zero Page Login Collector node](zero-page-login-collector.html)

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

* [OIDC ID Token Validator node](oidc-idtoken-validator.html)

* [SAML2 Authentication node](saml2.html)

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

* [Display Username node](display-username.html)

* [Identify Existing User node](identify-existing-user.html)

* [KBA Decision node](kba-decision.html)

* [KBA Definition node](kba-definition.html)

* [KBA Verification node](kba-verification.html)

* [Passthrough Authentication node](passthrough-authentication.html)

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

## Thing nodes (PingAM/Ping Advanced Identity Software)

* [Authenticate Thing node](self-managed/authenticate-thing.html)

* [Register Thing node](self-managed/register-thing.html)

## Uncategorized nodes

* [App Policy Decision node](app-policy-decision.html)

* [Identity Assertion node](identity-assertion-node.html)

* [Policy Decision node](policy-decision.html)

* [RADIUS Challenge Collector node](radius-challenge-collector.html)

* [RADIUS Decision node](radius-decision.html)

## Marketplace nodes

* PingOne integration

  * [PingOne Service](pingone/pingone-service.html)

  * [PingOne node (deprecated)](pingone/pingone.html)

  * [PingOne Authorize node](pingone/pingone-authorize.html)

  * [PingOne Credentials nodes](pingone/pingone-cred-overview.html)

  * [PingOne Credentials Delete Wallet node](pingone/pingone-cred-delete-wallet.html)

  * [PingOne Credentials Find Wallets node](pingone/pingone-cred-find-wallet.html)

  * [PingOne Credentials Issue node](pingone/pingone-cred-issue.html)

  * [PingOne Credentials Pair Wallet node](pingone/pingone-cred-pair-wallet.html)

  * [PingOne Credentials Revoke node](pingone/pingone-cred-revoke.html)

  * [PingOne Credentials Update node](pingone/pingone-cred-update.html)

  * [PingOne Credentials Verification node](pingone/pingone-cred-verify.html)

  * [PingOne DaVinci API node](pingone/pingone-davinci.html)

  * [PingOne Verify Authentication node (deprecated)](pingone/pingone-verify-authn.html)

  * [PingOne Verify Proofing node (deprecated)](pingone/pingone-verify-proof.html)

  * [PingOne Verify service (deprecated)](pingone/pingone-verify-service.html)

* [Akamai Account Protector node](cloud/akamai-account-protector.html)

* [BioCatch Session node](cloud/biocatch-session.html)

* [BioCatch Session Collector node](cloud/biocatch-session-collector.html)

* [BioCatch Session Profiler node](cloud/biocatch-session-profiler.html)

* [CLEAR ID Verification node](cloud/clear-id-verification.html)

* [Duo node (deprecated)](cloud/duo.html)

* [Duo Universal Prompt node](cloud/duo-univ-prompt.html)

* [Fingerprint nodes](cloud/fingerprint.html)

  * [Setup](cloud/fingerprint-setup.html)

  * [Fingerprint Profiler node](cloud/fingerprint-profiler.html)

  * [Fingerprint Response node](cloud/fingerprint-response.html)

* [Gateway Communication node](cloud/gateway-communication.html)

* [Google Chrome Device Trust node](cloud/google-chrome-device-trust.html)

* [HTTP Client node](cloud/http-client.html)

* [IdentityX Auth Request Decision node](cloud/identityx-auth-request-decision.html)

* [IdentityX Auth Request Initiator node](cloud/identityx-auth-request-initiator.html)

* [IdentityX Check Enrollment Status node](cloud/identityx-check-enrollment-status.html)

* [IdentityX Mobile Auth Request node](cloud/identityx-mobile-auth-request.html)

* [IdentityX Mobile Auth Request Validate node](cloud/identityx-mobile-auth-request-validate.html)

* [IdentityX Sponsor User node](cloud/identityx-sponsor-user.html)

* [iProov Authentication node](cloud/iproov.html)

* [Jumio identity verification](cloud/jumio-id-verify.html)

  * [Jumio Initiate node](cloud/jumio-initiate.html)

  * [Jumio Decision node](cloud/jumio-decision.html)

* [LexisNexis Dynamic Decision Platform (DDP)](cloud/lexis-ddp.html)

  * [LexisNexis DDP Profiler node](cloud/lexis-ddp-profiler.html)

  * [LexisNexis DDP Query node](cloud/lexis-ddp-query.html)

  * [LexisNexis DDP Review Status node](cloud/lexis-ddp-review-status.html)

  * [LexisNexis DDP Reason Code node](cloud/lexis-ddp-reason-code.html)

  * [LexisNexis DDP Update Review node](cloud/lexis-ddp-update-review.html)

* [LexisNexis InstantID Question and Answer (IIDQA)](cloud/lexis-iidqa.html)

  * [LexisNexis InstantID Get Quiz node](cloud/lexis-iidqa-get-quiz.html)

  * [LexisNexis InstantID Quiz Collector node](cloud/lexis-iidqa-quiz-collector.html)

  * [LexisNexis InstantID Quiz Decision node](cloud/lexis-iidqa-quiz-decision.html)

* [LexisNexis One-Time Passcode (OTP)](cloud/lexis-otp.html)

  * [LexisNexis OTP Sender node](cloud/lexis-otp-sender.html)

  * [LexisNexis OTP Collector node](cloud/lexis-otp-collector.html)

  * [LexisNexis OTP Decision node](cloud/lexis-otp-decision.html)

* [Microsoft Intune node](cloud/microsoft-intune-about.html)

* [NuData Captcha node](cloud/nudata-captcha.html)

* [NuData Initialize node](cloud/nudata-initialize.html)

* [NuData Score node](cloud/nudata-score.html)

* [NuData Trigger MFA node](cloud/nudata-trigger-mfa.html)

* [NuData Update node](cloud/nudata-update.html)

* [OneSpan](cloud/onespan-about.html)

  * [Set up OneSpan](cloud/onespan-setup.html)

    * [OneSpan tenant setup](cloud/onespan-setup.html#auth-node-onsepan-tenant-setup)

    * [Identity Cloud service setup](cloud/onespan-setup.html#auth-node-onespan-aux-setup)

  * [OneSpan nodes](cloud/onespan-nodes.html)

    * [OneSpan Auth Activate Device node](cloud/onespan-activate-device.html)

    * [OneSpan Auth Add Device node](cloud/onespan-add-device.html)

    * [OneSpan Auth Check Activation node](cloud/onespan-check-activation.html)

    * [OneSpan Auth Check Session Status node](cloud/onespan-check-session-status.html)

    * [OneSpan Auth VDP User Register node](cloud/onespan-vdp-register.html)

    * [OneSpan Auth Assign Authenticator node](cloud/onespan-assign-authn.html)

    * [OneSpan Auth Generate VOTP node](cloud/onespan-generate-votp.html)

    * [OneSpan Get User Authenticator node](cloud/onespan-get-user-authenticator.html)

    * [OneSpan Identity Verification node](cloud/onespan-id-verify.html)

  * [OneSpan Sample journeys](cloud/onespan-sample.html)

* [Onfido Check node](cloud/onfido-check.html)

* [Onfido Registration node](cloud/onfido-registration.html)

* [RSA SecurID node (deprecated)](cloud/rsa-securid.html)

* [Secret Double Octopus (SDO) nodes](cloud/secret-double-octopus.html)

* [Socure](cloud/socure.html)

  * [Socure DeviceId Collector node](cloud/socure-deviceid-collector.html)

  * [Socure ID+ node](cloud/socure-id.html)

  * [Socure Predictive DocV node](cloud/socure-predictive-docv.html)

* [SpyCloud Auth Node](cloud/spycloud-auth.html)

* [Twilio Identifier node](cloud/twilio-identifier.html)

* [Twilio Verify Collector Decision node](cloud/twilio-verify-collector-decision.html)

* [Twilio Verify Lookup node](cloud/twilio-verify-lookup.html)

* [Twilio Verify Sender node](cloud/twilio-verify-sender.html)

* [TypingDNA](cloud/tdna-set.html)

  * [TypingDNA Decision node](cloud/tdna-decision.html)

  * [TypingDNA Recorder node](cloud/tdna-recorder.html)

  * [TypingDNA Reset Profile node](cloud/tdna-reset-profile.html)

  * [TypingDNA Short Phrase Collector node](cloud/tdna-short-phrase-collector.html)

---

---
title: Backchannel Initialize node
description: Configure the Backchannel Initialize node to start an asynchronous journey for a different user or agent, enabling backchannel authentication in Advanced Identity Cloud.
component: auth-node-ref
version: latest
page_id: auth-node-ref::backchannel-initialize
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/backchannel-initialize.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-07T12:43:19Z
superseded_by: https://docs.pingidentity.com/auth-node-ref/latest/backchannel-initialize.html
section_ids:
  example: Example
  main_journey: Main journey
  backchannel_authentication_journey: Backchannel authentication journey
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  callbacks: Callbacks
  outcomes: Outcomes
  errors: Errors
---

# Backchannel Initialize node

The Backchannel Initialize node lets you start a separate journey that runs asynchronously, possibly by a different user or agent. The node takes an incoming user ID and generates a URL to a journey where the identified user or agent authenticates.

Together with the [Backchannel Status node](backchannel-status.html), this node lets you implement *backchannel authentication* from within a journey. Find more information in [Backchannel authentication](https://docs.pingidentity.com/pingoneaic/am-authentication/backchannel-authentication.html).

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

b The Identity Store Decision node assesses the user credentials. Find more information on this node and its outcomes in [Identity Store Decision node](cloud/identity-store-decision.html).

The main journey polls for completion of this subjourney. When this journey completes, the main journey continues.

## Availability

| Product                                        | Available? |
| ---------------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud                | Yes        |
| PingAM (self-managed)                          | Yes        |
| Ping Advanced Identity Software (self-managed) | Yes        |

## Inputs

This node optionally reads the user ID of the *subject* the journey's being initialized for from the incoming node state. The user ID is stored in the `nodeState` key specified in the Subject Name Key property.

## Dependencies

This node has no dependencies.

## Configuration

| Property            | Usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Journey             | The asynchronous journey to initialize.Select a journey from the list of configured journeys.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Subject Type        | The type of subject to initialize the journey for:- User

  The subject is a user identity.

- Agent

  The subject is a web agent or Java agent.

- None

  Setting the Subject Type to `None` means any subject can log in using the initialized journey.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Subject Name Key    | The `nodeState` key that contains the user ID of the subject you're initializing the journey for.This property is ignored if the Subject Type is `None`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Data Object Key     | The node state key that contains the data object (if present) to pass to the journey at the root level of the shared state.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Redirect URL Type   | The type of redirect URI to generate and save to node state in the `backchannel-redirectUri` key. The journey or client can use this URI to redirect the user.Possible values are:- Get

  The node generates a redirect URI based on the base URL service. The redirect uses a GET request to the `/UI/Login` endpoint.

- Post

  The node generates a redirect URI based on the base URL service. The redirect uses a POST request to the `json/authenticate` endpoint.

- Custom

  The node generates a redirect URI based on the URL specified in the Custom Redirect URL field.

- None

  The node doesn't generate a redirect URI. Use the transaction ID stored in state to construct your own redirect URL outside of the functionality of this node. Connect the node's outcome to a [Scripted Decision node](scripted-decision.html) to achieve this. |
| Custom Redirect URL | If Redirect URL Type is `Custom`, set this field to the custom redirect URL for the authentication journey.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Max Time (Seconds)  | The maximum number of seconds to wait for the backchannel journey to complete before timing out. This lets you set a specific timeout for each backchannel journey, depending on the expected completion time for the journey.	This value doesn't affect the authentication session timeout.If you don't set a value here, the backchannel journey times out after the Time to Live set for the realm.You can change this under Native Consoles > Access Management > Realms> *Realm Name* > Services > Transaction Authentication Service > Time to Live.                                                                                                                                                                                                                                                                                                         |
| Allow Retry         | When enabled, the end user can retry the backchannel journey if it fails. There's no maximum *number* of retries, but the retry window ends after the configured `Max Time`.If you disable this option, the backchannel authentication token goes into the `Failure` state the first time the backchannel journey fails. In this case, calls to the [Backchannel Status node](backchannel-status.html) go to the Failure outcome.Default: Enabled                                                                                                                                                                                                                                                                                                                                                                                                                  |

## Outputs

The node writes the following to the shared state:

| Shared state key          | Information                                                                        |
| ------------------------- | ---------------------------------------------------------------------------------- |
| `backchannel-transaction` | The transaction ID of the backchannel authentication request.                      |
| `backchannel-redirectUri` | The generated redirect URI.                                                        |
| `backchannel-data`        | An optional data object with additional information about the authenticating user. |

## Callbacks

This node doesn't send any callbacks.

## Outcomes

* `Created`

  The journey follows this outcome path if the node was able to create the backchannel authentication request.

* `Unknown Subject`

  The journey follows this outcome path if the subject in the incoming node state doesn't match an identity object in the backend identity store.

* `Error`

  The journey follows this outcome path if the node can't retrieve the subject from the node state.

## Errors

The node can log the following:

* Warnings

  * `Error retrieving subject from node state.`

    The node can't retrieve the subject from the incoming state.

* Errors

  * `Error initializing back channel transaction.`

    The node can't initialize the backchannel authentication journey.

---

---
title: Backchannel Notification node
description: Configure the Backchannel Notification node to send real-time status updates from a backchannel journey to the main authentication journey in Advanced Identity Cloud.
component: auth-node-ref
version: latest
page_id: auth-node-ref::backchannel-notification
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/backchannel-notification.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-03T18:03:31Z
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication", "Backchannel"]
superseded_by: https://docs.pingidentity.com/auth-node-ref/latest/backchannel-notification.html
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

c The Set Backchannel State Properties custom node writes the `_id`, `objectAttributes`, and `username` to the shared state.

This example uses the following configuration:

* Attribute list to set

  `_id`\
  `objectAttributes`\
  `username`

* Backchannel nodeState property

  `backchannel:data`

> **Collapse: How do I create this custom node?**
>
> The following steps provide the minimum configuration required to create this custom node. Learn more in [custom nodes](https://docs.pingidentity.com/pingoneaic/journeys/node-designer.html).
>
> 1. In the Advanced Identity Cloud admin UI, go to Journeys > Custom Nodes and click [icon: plus, set=fa]New Custom Node.
>
> 2. On the `New Custom Node` page, enter `Set Backchannel State Properties` as the name and click Next.
>
> 3. Add the following properties to the node and click Next:
>
>    * Attribute list to set
>
>      * Name: `attributeListProperty`
>
>      * Label: `Attribute list to set`
>
>      * Type: `String`
>
>      * Multi-Valued: Select this option.
>
>      * Required: Select this option.
>
>    * Backchannel nodeState property
>
>      * Name: `backchannelStateProperty`
>
>      * Label: `Backchannel nodeState property`
>
>      * Type: `String`
>
>      * Required: Select this option.
>
>      * Provide Default Value: Select this option.
>
>      * Default Value: `backchannel:data`
>
> 4. Set the following settings and click Next:
>
>    * Outcomes
>
>      `Next`
>
>    * Error Outcome
>
>      `Enabled`
>
> 5. In the script editor, add the following script to define the behavior of the node:
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
> 6. Click Save to create the custom node.

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

h The User Message To Display custom node displays a message to the help desk agent when the backchannel authentication completes successfully.

This example uses the following configuration:

* Message to display

  `User successfully authenticated`

> **Collapse: How do I create this custom node?**
>
> The following steps provide the minimum configuration required to create this custom node. Learn more in [custom nodes](https://docs.pingidentity.com/pingoneaic/journeys/node-designer.html).
>
> 1. In the Advanced Identity Cloud admin UI, go to Journeys > Custom Nodes and click [icon: plus, set=fa]New Custom Node.
>
> 2. On the `New Custom Node` page, enter `User Message to Display` as the name and click Next.
>
> 3. Add the following property to the node and click Next:
>
>    * Message to display
>
>      * Name: `message`
>
>      * Label: `Message to display`
>
>      * Type: `String`
>
>      * Required: Select this option.
>
> 4. Set the following settings and click Next:
>
>    * Outcomes
>
>      `Success`
>
> 5. In the script editor, add the following script to define the behavior of the node:
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
> 6. Click Save to create the custom node.

### Backchannel journey

This is a basic authentication journey that takes credentials and authenticates the user based on their existence in the backend identity store.

![Backchannel authentication journey with notifications](_images/backchannel-auth-notify-journey.png)

a The Page node includes a [Display Username node](display-username.html) and a [Platform Password node](platform-password.html). The username has been supplied in the shared state from the main journey. The user needs to enter their password.

b The Set Front Channel Status custom node adds data to the shared state that the Backchannel Notification node can send to the main journey.

This example uses the following configuration:

* Journey status shared state key

  `transaction:notify`

* Journey status property name

  `journeyStatus`

* Journey status message

  `User has entered their credentials`

> **Collapse: How do I create this custom node?**
>
> The following steps provide the minimum configuration required to create this custom node. Learn more in [custom nodes](https://docs.pingidentity.com/pingoneaic/journeys/node-designer.html).
>
> 1. In the Advanced Identity Cloud admin UI, go to Journeys > Custom Nodes and click [icon: plus, set=fa]New Custom Node.
>
> 2. On the `New Custom Node` page, enter `Set Front Channel Status` as the name and click Next.
>
> 3. Add the following properties to the node and click Next:
>
>    * Journey status shared state key
>
>      * Name: `journeyStatusKey`
>
>      * Label: `Journey status shared state key`
>
>      * Description: `The shared state key where the message object will be stored (e.g. transaction:notify). This is the top-level key that will be updated in the journey state.`
>
>      * Type: `String`
>
>      * Required: Select this option.
>
>      * Provide Default Value: Select this option.
>
>      * Default Value: `transaction:notify`
>
>    * Journey status property name
>
>      * Name: `journeyStatusProperty`
>
>      * Label: `Journey status property name`
>
>      * Description: `The name of the property inside the shared state object (e.g. journeyStatus). This defines the field that will hold the message value.`
>
>      * Type: `String`
>
>      * Required: Select this option.
>
>      * Provide Default Value: Select this option.
>
>      * Default Value: `journeyStatus`
>
>    * Journey status message
>
>      * Name: `journeyStatusValue`
>
>      * Label: `Journey status message`
>
>      * Description: `The message to store in shared state. This value will be used by downstream nodes (e.g. Backchannel Notification) to update the front-channel experience.`
>
>      * Type: `String`
>
>      * Required: Select this option.
>
>      * Provide Default Value: Select this option.
>
>      * Default Value: `Example Front Channel Message`
>
> 4. Set the following settings and click Next:
>
>    * Outcomes
>
>      `Success`\
>      `Error`
>
> 5. In the script editor, add the following script to define the behavior of the node:
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
> 6. Click Save to create the custom node.

c The Backchannel Notification node reads the shared state and sends a status update to the main journey to inform the help desk agent that the user has entered their credentials.

d The [Data Store Decision node](data-store-decision.html) validates the username-password credentials.

e The Set Front Channel Status custom node adds data to the shared state that the Backchannel Notification node can send to the main journey. This is the custom node you created earlier in this example.

This instance of the node uses the following configuration:

* Journey status shared state key

  `transaction:notify`

* Journey status property name

  `journeyStatus`

* Journey status message

  `User's credentials are valid`

f The Backchannel Notification node reads the shared state and sends a status update to the main journey to inform the help desk agent that the user's credentials match those stored in the data store.

## Availability

| Product                                        | Available? |
| ---------------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud                | Yes        |
| PingAM (self-managed)                          | Yes        |
| Ping Advanced Identity Software (self-managed) | Yes        |

## Inputs

This node reads data from the incoming node state using the key specified in the Data Key. The key value must be a JSON object.

Implement a node earlier in the journey to add data to the incoming node state using this key. For example, you could use [custom nodes](https://docs.pingidentity.com/pingoneaic/journeys/node-designer.html) or a [Scripted Decision node](scripted-decision.html).

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

The node can log the following:

* Warnings

  * `Transaction ID not found in context`

    The transaction ID is missing from the incoming request context.

  * `Data in state at dataKey data key was not found or incorrect type, not updating transaction.`

    The Data Key configured for the node doesn't exist in the incoming node state, or it exists but contains invalid data.

* Errors

  * `Failed to update backchannel transaction`

    An error occurred when the node attempted to update the backchannel transaction with the data from the incoming node state.

---

---
title: Backchannel Status node
description: Configure the Backchannel Status node to check the status of an asynchronous backchannel authentication journey in Advanced Identity Cloud.
component: auth-node-ref
version: latest
page_id: auth-node-ref::backchannel-status
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/backchannel-status.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-03T18:03:31Z
superseded_by: https://docs.pingidentity.com/auth-node-ref/latest/backchannel-status.html
section_ids:
  example: Example
  main_journey: Main journey
  backchannel_authentication_journey: Backchannel authentication journey
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  callbacks: Callbacks
  outcomes: Outcomes
  errors: Errors
---

# Backchannel Status node

The Backchannel Status node checks the status of an asynchronous (backchannel) user journey.

Together with the [Backchannel Initialize node](backchannel-initialize.html), this node lets you implement *backchannel authentication* from within a journey. Find more information in [Backchannel authentication](https://docs.pingidentity.com/pingoneaic/am-authentication/backchannel-authentication.html).

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

b The Identity Store Decision node assesses the user credentials. Find more information on this node and its outcomes in [Identity Store Decision node](cloud/identity-store-decision.html).

The main journey polls for completion of this subjourney. When this journey completes, the main journey continues.

## Availability

| Product                                        | Available? |
| ---------------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud                | Yes        |
| PingAM (self-managed)                          | Yes        |
| Ping Advanced Identity Software (self-managed) | Yes        |

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

## Callbacks

This node doesn't send any callbacks.

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
title: BioCatch Session Collector node
description: Collects the BioCatch unique session identifier (customerSessionID) from the user-agent during an Advanced Identity Cloud authentication journey.
component: auth-node-ref
version: latest
page_id: auth-node-ref:cloud:biocatch-session-collector
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/cloud/biocatch-session-collector.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-03T18:03:31Z
keywords: ["Nodes &amp; Trees", "Journeys", "Authentication"]
page_aliases: ["auth-node-biocatch-session-collector.adoc"]
section_ids:
  example: Example
  outcomes: Outcomes
  configuration: Configuration
---

# BioCatch Session Collector node

Collects the user's [BioCatch](https://www.biocatch.com/) unique session identifier (`customerSessionID`).

## Example

For an example in context, refer to the [BioCatch examples](biocatch-session.html#biocatch-examples).

## Outcomes

* `Next`

  Successfully collected the identifier.

* `Error`

  An error occurred.

## Configuration

This node has no configurable properties.