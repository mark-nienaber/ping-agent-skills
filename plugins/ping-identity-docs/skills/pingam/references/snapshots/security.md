---
title: Account lockout
description: Configure account lockout to lock user accounts after repeated failed login attempts, slowing down brute-force attacks and compensating for weak password policies
component: pingam
version: 8.1
page_id: pingam:security:account-lockout
canonical_url: https://docs.pingidentity.com/pingam/8.1/security/account-lockout.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Identities", "Features"]
page_aliases: ["security-guide:account-lockout.adoc"]
section_ids:
  to-configure-acct-lockout: Configure account lockout
  customize-lockout-messages: Customize account lockout messages
---

# Account lockout

*Account lockout* is a security mechanism that locks a user account after repeated failed login attempts. Use it to slow down brute-force attacks and compensate for weak password policies.

Most deployments use the identity store's password policy to control account lockout. If this isn't an option in your deployment, configure account lockout as explained in this section.

Use persistent lockout where possible. If that's not compatible with your company policy, use a duration lockout of at least 15 minutes.

You can configure account lockout in *one* of the following ways:

* Persistent lockout

  Persistent (physical) lockout locks the user's account indefinitely until unlocked by an administrator.

  This is the default type of account lockout and the best way to mitigate brute-force attacks.

  For persistent lockout, AM sets the user account status to `inactive` in the user profile, and tracks failed authentication attempts by writing to the user repository. The `inactive` status makes it easier for an administrator to search for user accounts with persistent lockout.

  Persistent lockout works independently of account lockout mechanisms in the underlying directory server that serves as the user datastore.

* Duration lockout

  Duration lockout locks the user account for a specified duration, keeping track of the locked state either in memory or in the datastore.

  The default configuration is to record invalid authentication attempts in the datastore. This avoids the need for sticky load balancing. If you choose to store the count of invalid attempts in memory, the counter applies to the current AM instance only. Also, if you restart AM and lockout is stored in memory, duration lockouts on all accounts are released. Otherwise, the lock is released automatically after the specified duration.

  Unlike persistent lockout, the user account status remains `active` for duration lockout.

|   |                                                                                                                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Failed login attempts during the [transactional authorization](../am-authorization/transactional-authorization.html) flow don't increment account lockout counters.If login failures are stored in AM's memory, this might result in user accounts not being locked out, even after multiple login failures. To avoid this issue, implement persistent lockout instead. |

## Configure account lockout

1. Configure account lockout:

   * In the AM admin UI, go to Realms > *realm name* > Authentication > Settings > Account Lockout.

   * Enable lockout by checking Login Failure Lockout Mode, then set the number of attempts and the lockout interval.

     You can also opt to warn users after several consecutive failures.

   * Enable Store Invalid Attempts in Data Store to save account login failures to the datastore. This setting is necessary when using server-side or client-side journey sessions. If you don't set this, users might not be locked out even after multiple login failures.

     When you store the number of failed attempts in the datastore, other AM servers accessing the user datastore also have access to that information.

   * If AM is configured to [send mail](../setup/deployment-configuration-reference.html#general-mailserver), you can set up email notification of lockouts to an administrator.

2. Configure persistent lockout:

   * Set Login Failure Lockout Duration to `0`.

   * Optionally, set Lockout Attribute Name and Lockout Attribute Value to specify an additional attribute to update on lockout.

     By default, AM sets the value of the user's `inetuserstatus` attribute to `Inactive`.

   * Optionally, set Invalid Attempts Data Attribute Name to specify a custom attribute to store the number of failed authentication attempts.

3. Configure duration lockout:

   * Set Login Failure Lockout Duration to a positive value representing the duration in minutes.

     A value of at least 15 minutes is recommended.

   * Optionally, set Lockout Duration Multiplier to increase the lockout duration on each successive lockout.

   * Enable Store Invalid Attempts in Data Store so that lockout attempts aren't stored in memory, but persisted in the repository, and applied across all AM instances.

   * Set Invalid Attempts Data Attribute Name to the default attribute `sunAMAuthInvalidAttemptsData` to prevent invalid attempts from being stored only in memory.

   Learn more in [account lockout configuration](../am-authentication/authn-core-settings.html#authn-core-account-lockout).

|   |                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To unlock a user's account:- Locate the user under Realms > *realm name* > Identities.

- Choose the user you want to unlock.

- Set their User Status property to Active.

- Click Save. |

Find information on how authentication trees handle account lockout in [Account lockout for trees](../am-authentication/auth-nodes-and-journeys.html#account-lockout-trees).

## Customize account lockout messages

To customize the messages shown to end users when their accounts are locked, follow these steps:

1. Locate the `openam-core-8.1.1.jar` file in the `WEB-INF/lib/` folder where AM is deployed.

2. Extract the `amAuth.properties` file.

3. Change the value of the `lockOut` field to control the lockout message. For example:

   ```
   lockOut=Your example.com account has been locked. Please contact your support agent.|user_inactive.jsp
   ```

4. Copy the amended `amAuth.properties` file to the `WEB-INF/classes/` folder where AM is deployed.

5. When a user whose account is locked attempts to authenticate, the custom lockout message is displayed:

   ![Custom account lockout message](_images/custom-lockout-message.png)
