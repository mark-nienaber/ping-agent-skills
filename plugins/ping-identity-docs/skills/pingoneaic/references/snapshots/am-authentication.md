---
title: Account lockout
description: Lock user accounts after repeated failed login attempts to defend against brute-force attacks
component: pingoneaic
page_id: pingoneaic:am-authentication:account-lockout
canonical_url: https://docs.pingidentity.com/pingoneaic/am-authentication/account-lockout.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  configure-account-lockout: Configure account lockout
  success-and-failure-nodes: Success and Failure nodes
  success-node: Success node
  failure-node: Failure node
  lockout_specific_nodes: Lockout-specific nodes
---

# Account lockout

Account lockout is a security mechanism that locks a user account after repeated failed login attempts. It is used to slow down brute-force attacks and compensate for weak password policies.

You can configure account lockout in one of the following ways:

* Persistent lockout

  Persistent (physical) lockout locks the user account indefinitely. A tenant administrator can release the lock by setting the account status to active.

  For persistent lockout, Advanced Identity Cloud sets the user account status to inactive. This makes it easy for a tenant administrator to search for user accounts with a persistent lockout set. It also means that if you synchronize your user accounts from Advanced Identity Cloud to another datastore, you can track locked accounts in the downstream datastore.

  This is the default type of account lockout and Ping Identity recommends it as the best way to mitigate brute force attacks.

* Duration lockout

  Duration lockout locks the user account for a specified duration. The lock is automatically released after the specified duration.

  Unlike persistent lockout, the user account status remains active. Instead, Advanced Identity Cloud tracks the locked state internally. This makes it harder for a tenant administrator to search for user accounts with a duration lockout set. It also means that if you synchronize your user accounts from Advanced Identity Cloud to another datastore, you cannot track locked accounts in the downstream datastore. However, it is possible to configure the Invalid Attempts Data Attribute Name to persist metadata about failed authentication attempts to a specified user account attribute — refer to [Configure account lockout](#configure-account-lockout).

|   |                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Failed login attempts during the [transactional authorization](../am-authorization/transactional-authorization.html) flow do not increment account lockout counters. |

## Configure account lockout

1. In the Advanced Identity Cloud admin console, select Native Consoles > Access Management.

2. Go to Realms > *Realm Name* > Authentication > Settings > Account Lockout.

3. Enable lockout by checking Login Failure Lockout Mode, then set the number of attempts and the lockout interval. You can also opt to warn users after several consecutive failures.

4. To configure persistent lockout:

   1. Set Login Failure Lockout Duration to 0.

   2. Check Store Invalid Attempts in Data Store.

5. To configure duration lockout:

   1. Set Login Failure Lockout Duration to a positive integer value representing number of minutes. Set a value of at least 15. Optionally, configure a multipier to increase the lockout duration on each successive lockout.

   2. Check Store Invalid Attempts in Data Store.

   3. Set Invalid Attempts Data Attribute Name to `sunAMAuthInvalidAttemptsData`. Alternatively, to persist invalid attempts metadata to the user account, set Invalid Attempts Data Attribute Name to a valid attribute; for example, `fr-attr-istr1`. For a list of valid attributes, refer to the [User identity attributes and properties reference](../identities/user-identity-properties-attributes-reference.html).

6. Click Save Changes.

## Success and Failure nodes

If you enable account lockout in a realm, the Success and Failure nodes play a key role in modifying journey behavior. The Success node resets the number of invalid attempts to zero. The Failure node increments the number of invalid attempts and triggers Warn User After N Failures messages.

### Success node

This node does the following:

* Checks the Status property of the user profile, when reached. If the account is marked as `Inactive`, the node fails the authentication with an error message:

  ![Account locked error when reaching Success node.](_images/trees-error-lockout.png)

  The error message is returned in the JSON response if authenticating to the journey over REST:

  ```json
  {
      "code":401,
      "reason":"Unauthorized",
      "message":"User Locked Out.",
      "detail":
      {
          "failureUrl":""
      }
  }
  ```

* If the User Status property is set to `Active`, the node resets the failure count in the user profile, when reached.

### Failure node

This node does the following:

* If you select Authentication > Settings > Account Lockout > Login Failure Lockout Mode for the realm (under Native Consoles > Access Management), the node checks the invalid attempts property of the user profile. It returns a warning message if the number of failed attempts is equal to or greater than the configured Warn User After N Failures value:

  ![Invalid attempts limit warning when reaching Failure node.](_images/trees-warning-attempts.png)

  The error message is returned in the JSON response if authenticating to the journey over REST:

  ```json
  {
      "code":401,
      "reason":"Unauthorized",
      "message":"Warning: You will be locked out after 1 more failure(s).",
      "detail":
      {
          "failureUrl":""
      }
  }
  ```

* Increments the failure count in the user profile, when reached.

* Returns an error message if the account is marked as `Inactive`:

  ![Account locked error when reaching Failure node.](_images/trees-error-lockout.png)

  The error message is returned in the JSON response if authenticating to the journey over REST:

  ```json
  {
      "code":401,
      "reason":"Unauthorized",
      "message":"User Locked Out.",
      "detail":
      {
          "failureUrl":""
      }
  }
  ```

## Lockout-specific nodes

Authentication journeys also provide lockout-specific nodes for checking and changing the status of a user:

* [Account Active Decision node](https://docs.pingidentity.com/auth-node-ref/latest/account-active-decision.html)

  Use this node to determine whether an account is considered locked or unlocked.

  * The account is considered locked under these conditions:

    * The status is `inactive`.

    * The status is `active` and a duration lockout is set on the account.

  * The account is considered unlocked under this condition:

    * The status is `active` and no duration lockout is set on the account.

* [Account Lockout node](https://docs.pingidentity.com/auth-node-ref/latest/account-lockout.html)

  Use this node to change the account's status to inactive or active.

  When setting an account to inactive, the node does not consider the realm's account lockout settings, so effectively sets a persistent lockout on the account.

  When setting an account to active, the node also resets the failed attempts and lockout duration counters.
